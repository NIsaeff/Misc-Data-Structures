import csv

def read_jobs_from_csv(filename):
    jobs=[]
    with open(filename, newline='')as file:
        reader = csv.DictReader(file)
        for row in reader:
            jobs.append({'JobID': row['JobID'],
                         'Start': int(row['Start']),
                         'End': int(row['End']),
                         'Salary': int(row['Salary'])
                         })
    return jobs

# print(read_jobs_from_csv('jobs.csv'))

def pay_per_unit(job):
    duration = job['End'] - job['Start']
    return job['Salary'] / duration if duration > 0 else 0

def jobs_overlap(a, b):
    return a['End'] >= b['Start']

def find_jobs(current_job, remaining_jobs):
    selected_jobs = []
    for idx, job in enumerate(remaining_jobs):
        if jobs_overlap(current_job, job):
            if pay_per_unit(job) > pay_per_unit(current_job):
                return find_jobs(job, remaining_jobs[idx+1:])
        else:
            selected_jobs.append(current_job)
            return selected_jobs + find_jobs(job, remaining_jobs[idx+1:])
    selected_jobs.append(current_job)
    return selected_jobs

    
if __name__ == "__main__":
    jobs = read_jobs_from_csv('jobs.csv')
    jobs.sort(key=lambda x: x['Start'])
    if jobs:
        final_schedule = find_jobs(jobs[0], jobs[1:])
        for job in final_schedule:
            print(job)
