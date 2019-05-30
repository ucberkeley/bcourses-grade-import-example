import argparse
import csv
import requests
import sys

from auth import token
from get_assignment_data import assignment_ids
from get_student_data import normalize_email, email_to_bcourses

def handle_unknown_email(email):
    # TODO: figure out exactly what to do / how to contact them
    print('Unknown email:', email)

def convert_score(assignment_name, score):
    if assignment_name.startswith('Lab') or assignment_name.starts('Discussion'):
        return 'complete' if float(score) > 0 else 'incomplete'
    return score

HEADERS = {'authorization': 'Bearer ' + token}

# https://bcourses.berkeley.edu/doc/api/submissions.html#method.submissions_api.update
def enter_ok_grades(assignment_name, grades_csv):
    assignment_id = assignment_ids[assignment_name]
    assignment_url = 'https://bcourses.berkeley.edu/api/v1/courses/1364195/' + \
                     'assignments/{0}/'.format(assignment_id) + \
                     'submissions/{bcourses_id}'

    to_upload = [] # (email, bcourses_id, score, message)
    with open(grades_csv) as f:
        grades = csv.reader(f)
        headers = next(grades)
        for email, score, message, _, _ in grades:
            if not email.strip():
                continue
            email = normalize_email(email)
            try:
                bcourses_id = email_to_bcourses[email]
            except KeyError:
                handle_unknown_email(email)
                continue
            to_upload.append((email,
                              bcourses_id,
                              convert_score(assignment_name, score),
                              message))

    print('About to upload', len(to_upload), 'scores for', assignment_name)
    to_continue = input('Continue? [Y/n] ')
    if to_continue.lower() != 'y':
        return

    for email, bcourses_id, score, message in to_upload:
        print(email, score)
        url = assignment_url.format(bcourses_id=bcourses_id)
        querystring = {
            'include[visibility]': 'false',
            'submission[posted_grade]': score,
            'comment[text_comment]': message
        }
        response = requests.request('PUT', url, headers=HEADERS, params=querystring)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('assignment_name')
    parser.add_argument('grades')
    parser.add_argument('--ok', action='store_true')
    parser.add_argument('--gradescope', action='store_true')
    args = parser.parse_args()

    if args.assignment_name not in assignment_ids:
        print('Unknown assignment:', args.assignment_name)
        print('Try one of these:')
        print(','.join(sorted(assignment_ids)))
        sys.exit(1)

    if args.ok:
        enter_ok_grades(args.assignment_name, args.grades)
