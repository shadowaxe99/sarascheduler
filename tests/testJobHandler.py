import unittest
from JobHandler import JobHandler


class TestJobHandler(unittest.TestCase):
    def test_add_job(self):
        # Test case 1
        job_handler = JobHandler()
        job_id = 1
        job_data = {'name': 'Job 1'}
        job_handler.add_job(job_id, job_data)
        self.assertEqual(job_handler.get_job(job_id), job_data)
        
        # Test case 2
        job_id = 2
        job_data = {'name': 'Job 2'}
        job_handler.add_job(job_id, job_data)
        self.assertEqual(job_handler.get_job(job_id), job_data)
        
        # Test case 3
        job_id = 3
        job_data = {'name': 'Job 3'}
        job_handler.add_job(job_id, job_data)
        self.assertEqual(job_handler.get_job(job_id), job_data)

    def test_remove_job(self):
        # Test case 1
        job_handler = JobHandler()
        job_id = 1
        job_data = {'name': 'Job 1'}
        job_handler.add_job(job_id, job_data)
        job_handler.remove_job(job_id)
        self.assertIsNone(job_handler.get_job(job_id))
        
        # Test case 2
        job_id = 2
        job_data = {'name': 'Job 2'}
        job_handler.add_job(job_id, job_data)
        job_handler.remove_job(job_id)
        self.assertIsNone(job_handler.get_job(job_id))
        
        # Test case 3
        job_id = 3
        job_data = {'name': 'Job 3'}
        job_handler.add_job(job_id, job_data)
        job_handler.remove_job(job_id)
        self.assertIsNone(job_handler.get_job(job_id))


if __name__ == '__main__':
    unittest.main()
