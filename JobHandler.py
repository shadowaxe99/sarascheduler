import time


class JobHandler:
    def __init__(self):
        self.jobs = {}

    def add_job(self, job_id, job_data):
        self.jobs[job_id] = job_data

    def remove_job(self, job_id):
        if job_id in self.jobs:
            del self.jobs[job_id]

    def get_job(self, job_id):
        return self.jobs.get(job_id)

    def get_all_jobs(self):
        return self.jobs

    def run(self):
        while True:
            for job_id, job_data in self.jobs.items():
                print(f'Running job {job_id}')
                # Run the job
                job_data['job'].run()

                # Check if the job is completed
                if job_data['job'].is_completed():
                    print(f'Job {job_id} completed')
                    # Remove the job
                    self.remove_job(job_id)

            # Sleep for 1 second
            time.sleep(1)
