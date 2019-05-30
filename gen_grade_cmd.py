assignment_csv = {
 'Homework 1': 'scores_cal_cs61a_fa15_Homework_1.csv',
 'Homework 2': 'scores_cal_cs61a_fa15_Homework_2.csv',
 'Homework 3': 'scores_cal_cs61a_fa15_Homework_3.csv',
 'Homework 4': 'scores_cal_cs61a_fa15_Homework_4.csv',
 'Homework 5': 'scores_cal_cs61a_fa15_Homework_5.csv',
 'Homework 6': 'scores_cal_cs61a_fa15_Homework_6.csv',
 'Homework 7': 'scores_cal_cs61a_fa15_Homework_7.csv',
 'Homework 8': 'scores_cal_cs61a_fa15_Homework_8.csv',
 'Homework 9': 'scores_cal_cs61a_fa15_Homework_9.csv',
 'Lab 1': 'scores_cal_cs61a_fa15_Lab_1.csv',
 'Lab 10': 'scores_cal_cs61a_fa15_Lab_10.csv',
 'Lab 11': 'scores_cal_cs61a_fa15_Lab_11.csv',
 'Lab 12': 'scores_cal_cs61a_fa15_Lab_12.csv',
 'Lab 14': 'scores_cal_cs61a_fa15_Lab_14.csv',
 'Lab 2': 'scores_cal_cs61a_fa15_Lab_2.csv',
 'Lab 3': 'scores_cal_cs61a_fa15_Lab_3.csv',
 'Lab 4': 'scores_cal_cs61a_fa15_Lab_4.csv',
 'Lab 5': 'scores_cal_cs61a_fa15_Lab_5.csv',
 'Lab 6': 'scores_cal_cs61a_fa15_Lab_6.csv',
 'Lab 7': 'scores_cal_cs61a_fa15_Lab_7.csv',
 'Lab 8': 'scores_cal_cs61a_fa15_Lab_8.csv',
 'Lab 9': 'scores_cal_cs61a_fa15_Lab_9.csv',
 'Project 1': 'scores_cal_cs61a_fa15_Hog.csv',
 'Project 1 Composition': 'scores_cal_cs61a_fa15_Hog.csv',
 'Project 2': 'scores_cal_cs61a_fa15_Maps.csv',
 'Project 2 Composition': 'scores_cal_cs61a_fa15_Maps.csv',
 'Project 3': 'scores_cal_cs61a_fa15_Ants.csv',
 'Project 3 Composition': 'scores_cal_cs61a_fa15_Ants.csv',
 'Project 4': 'scores_cal_cs61a_fa15_Scheme.csv',
 'Project 4 Composition': 'scores_cal_cs61a_fa15_Scheme.csv',
 'Quiz 1': 'scores_cal_cs61a_fa15_Quiz_1.csv',
 'Quiz 2': 'scores_cal_cs61a_fa15_Quiz_2.csv',
 'Quiz 3': 'scores_cal_cs61a_fa15_Quiz_3.csv',
 'Quiz 4': 'scores_cal_cs61a_fa15_Quiz_4.csv'
}

emails = ['tran_nghi1909@berkeley.edu','froicervania96@berkeley.edu','hritchie@berkeley.edu','suyanglu@berkeley.edu','siyuanff@berkeley.edu','yiwen0729@berkeley.edu','thatguyken@berkeley.edu','usa@berkeley.edu']
script = 'python3 enter_grades.py {flags} "{name}" {csv} {postpend};'

def late_enroll(emails):
    flags = "--ok  --updateonly --force "
    postpend = "--email " + ' '.join(emails)


    for bcourse, grades in assignment_csv.items():
        assign_flags = flags 
        location = "dec17scores/"
        if "Composition" in bcourse:
            assign_flags = flags + " --composition"
            if "Scheme" in bcourse or "Ants" in bcourse:
                grades = grades[:-4] + "_raw.csv"
                location = "scores/" # raw CSV contains composition and is in a seperate folder

        grade_cmd = script.format(flags=assign_flags, name=bcourse, csv=location+grades, postpend=postpend)
        print(grade_cmd)

def remap(): 
    flags = "--ok --remap --updateonly --force"
    postpend = ""

    for bcourse, grades in assignment_csv.items():
        assign_flags = flags 
        location = "scores/"
        if "Lab 14" in bcourse:
            grade_cmd = script.format(flags=assign_flags, name="Homework 10", csv=location+grades, postpend=postpend)
            print(grade_cmd)
            
        if "Composition" in bcourse:
            assign_flags = flags + " --composition"
            if "Scheme" in grades or "Ants" in grades:
                grades = grades[:-4] + "_raw.csv"

        grade_cmd = script.format(flags=assign_flags, name=bcourse, csv=location+grades, postpend=postpend)
        print(grade_cmd)

if __name__ == "__main__":
    # late_enroll
    remap()

