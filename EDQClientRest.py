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
        
        """Creation of Job with request body
            with as filelist
        
        """
        params = {'filelist':file_list}
        json_response = self._create_job_configuration(params)
        return {"status":f"Job ID created: {json_response['datasetConfigurationId']}"}
    

    def _create_ruleset(self,file_list):
        """
        create ruleset and get the ruleset Id
        """
        #YTD input params
        params = {} 
        json_response = self._create_job_configuration(params)
        return {"status":f"Job ID created: {json_response['rulesetId']}"}
    
    def _create_rule(self,rules):
        """
        creation of rules and attaching rules to ruleset
        
        """
        params = {'rules':rules}
        json_response = self._create_job_configuration(params)
        return {"status":f"Job ID created: {json_response['jobId']}"}
    
    def _schedule_job(self,jobId):
        """
        Job Schedule based on Job  Id
        
        """
        params = {'datasetConfigurationId':config.default_config.datasets[config.default_config.datasets.keys()[0]],
                  'jobId':jobId}
        json_response = self._create_job_configuration(params)
        return {"status":f"Job ID created: {json_response['jobId']}"}
    
