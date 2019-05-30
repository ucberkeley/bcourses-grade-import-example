import requests

assignment_ids = {
    'Discussion 1': 6896437,
    'Discussion 10': 6896446,
    'Discussion 11': 6896447,
    'Discussion 2': 6896438,
    'Discussion 3': 6896439,
    'Discussion 4': 6896440,
    'Discussion 5': 6896441,
    'Discussion 6': 6896442,
    'Discussion 7': 6896443,
    'Discussion 8': 6896444,
    'Discussion 9': 6896445,
    'Final': 6896414,
    'Homework 1': 6896390,
    'Homework 10': 6896403,
    'Homework 2': 6896394,
    'Homework 3': 6896395,
    'Homework 4': 6896396,
    'Homework 5': 6896397,
    'Homework 6': 6896398,
    'Homework 7': 6896399,
    'Homework 8': 6896401,
    'Homework 9': 6896402,
    'Lab 1': 6896423,
    'Lab 10': 6896433,
    'Lab 11': 6896434,
    'Lab 12': 6896435,
    'Lab 13': 6896436,
    'Lab 2': 6896424,
    'Lab 3': 6896425,
    'Lab 4': 6896426,
    'Lab 5': 6896427,
    'Lab 6': 6896428,
    'Lab 7': 6896429,
    'Lab 8': 6896430,
    'Lab 9': 6896431,
    'Midterm 1': 6896412,
    'Midterm 1 Recovery': 6896449,
    'Midterm 2': 6896413,
    'Midterm 2 Recovery': 6896450,
    'Project 1': 6896404,
    'Project 1 Composition': 6896415,
    'Project 1 Contest': 6896421,
    'Project 2': 6896405,
    'Project 2 Composition': 6896417,
    'Project 3': 6896406,
    'Project 3 Composition': 6896419,
    'Project 4': 6896407,
    'Project 4 Composition': 6896420,
    'Project 4 Contest': 6896422,
    'Quiz 1': 6896408,
    'Quiz 2': 6896409,
    'Quiz 3': 6896410,
    'Quiz 4': 6896411
}

from auth import token
HEADERS = {'authorization': 'Bearer ' + token}

def paginate_request(http_method, url, headers=HEADERS, verbose=True):
    responses = []
    while True:
        if verbose:
            print(url)
        response = requests.request(http_method, url, headers=headers)
        responses.append(response.json())

        # pagination
        next_url = [l for l in response.headers['link'].split(',') if l.endswith('rel="next"')]
        if not next_url:
            break
        next_url = next_url[0]
        url = next_url[next_url.index('<')+1:next_url.index('>')]
    return responses

def get_assignment_ids():
    url = 'https://bcourses.berkeley.edu/api/v1/courses/1364195/assignments'
    responses = paginate_request('GET', url, HEADERS)

    results = []
    for response in responses:
        results += [(assignment['name'], assignment['id']) for assignment in response]

    return dict(results)
