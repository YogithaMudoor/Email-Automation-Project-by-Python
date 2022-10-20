def extract():
    with open('C:/Users/HP/Desktop/schedule.txt') as schedules: #read file schedule line by line
         schedule_contents = schedules.readlines()
    dateschedule=[]
    for datemodule in schedule_contents:
        dateschedule.append(datemodule.strip().split('-'))
        schedule= [schedules[0] for schedules in dateschedule]
        module=[modules[1] for modules in dateschedule]
    result = {}  
    for dt, mod in zip(schedule, module):
        result[dt] = mod
    return result