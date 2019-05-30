import csv

def normalize_email(email):
    email = email.lower()
    email = email[:email.index('@')].replace('.', '') + email[email.index('@'):]
    return email

def convert_emails_to_bcourses_id(roster_csv, gradebook_csv):
    # convert email to sis_login_id
    email_to_sis_login_id = {}
    with open(roster_csv) as f:
        roster = csv.reader(f)
        header = next(roster) # ignore header
        for student in roster:
            email = student[4]
            sis_login_id = student[2]
            if email in email_to_sis_login_id:
                print('Warning: {} has multiple SIS login IDs'.format(email))
            email_to_sis_login_id[email] = sis_login_id

    # convert sis_login_id to bcourses_id
    sis_login_id_to_bcourses_id = {}
    with open(gradebook_csv) as f:
        gradebook = csv.reader(f)
        header = next(gradebook)
        points_possible = next(gradebook)
        for student in gradebook:
            sis_login_id = student[3]
            bcourses_id = student[1]
            if sis_login_id in sis_login_id_to_bcourses_id:
                print('Warning: {} has multiple bCourses IDs'.format(sis_login_id))
            sis_login_id_to_bcourses_id[sis_login_id] = bcourses_id

    # convert email to bcourses_id
    email_to_bcourses = {}
    for email, sis_login_id in email_to_sis_login_id.items():
        bcourses_id = sis_login_id_to_bcourses_id[sis_login_id]
        email = normalize_email(email)
        if email in email_to_bcourses:
            print('Warning: {} has multiple bCourses IDs'.format(email))
        email_to_bcourses[email] = bcourses_id

    return email_to_bcourses

email_to_bcourses = convert_emails_to_bcourses_id(
    'course_1364195_rosters.csv',
    '30_Sep_00-53_Grades-COMPSCI_61A_-_LEC_001.csv'
)
