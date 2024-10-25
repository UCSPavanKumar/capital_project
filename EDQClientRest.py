from DevBase import DevBase
import config
class EDQClientRest(DevBase):
    def __init__(self):
        super().__init__(self)

    def _create_job(self,job_name):

        """Creation of Job with request body
            with datasetId and job Name
        
        """
        params = {'datasetConfigurationId':config.default_config.datasets[config.default_config.datasets.keys()[0]],
                  'job_name':job_name}
        json_response = self._create_job_configuration(params)
        return {"status":f"Job ID created: {json_response['jobId']}"}
    

    def _create_dataset(self,file_list):
        params = {'datasetConfigurationId':config.default_config.datasets[config.default_config.datasets.keys()[0]],
                  'job_name':job_name}
        json_response = self._create_job_configuration(params)
        return {"status":f"Job ID created: {json_response['jobId']}"}