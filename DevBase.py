import requests
import config



class DevBase:
    def __init__(self) -> None:
        self.base_url = config.default_config.base_url
        self.gateway  = config.default_config.gateway
        self.headers={"Content-Type":"application/json"}
        pass
    
    def _create_dataset(self,**kwargs):
        create_dataset = config.default_config.dataset_config.create_dataset
        response = requests.post(f"{self.base_url}{self.gateway}{create_dataset}",params=kwargs,headers=self.headers)
        if response.status_code == 200:
            return response
        else:
            return {'status':'Invalid Response'}
        
    def _create_job_configuration(self,**kwargs):
        create_job = config.default_config.job_config.create_job
        response = requests.post(f"{self.base_url}{self.gateway}{create_job}",params=kwargs,headers=self.headers)
        if response.status_code == 200:
            return response
        else:
            return {'status':'Invalid Response'}

    def _create_rule_set(self,**kwargs):
        create_rule_set = config.default_config.rule_config.create_ruleset
        response = requests.post(f"{self.base_url}{self.gateway}{create_rule_set}",params=kwargs,headers=self.headers)
        if response.status_code == 200:
            return response
        else:
            return {'status':'Invalid Response'}
    
    def _create_rule(self,**kwargs):
        create_rule_set = config.default_config.rule_config.create_ruleset
        response = requests.post(f"{self.base_url}{self.gateway}{create_rule_set}",params=kwargs,headers=self.headers)
        if response.status_code == 200:
            return response
        else:
            return {'status':'Invalid Response'}
        
    def _check_if_rule_exists(self,**kwargs):
        create_rule_set = config.default_config['rule_config']['create_rule']
        response = requests.post(f"{self.base_url}{self.gateway}{create_rule_set}",params=kwargs,headers=self.headers)
        if response.status_code == 200:
            return [row.ruleId for row in response]
        else:
            return []
        
    def _check_if_dataset_exists(self,**kwargs):
        params = {'datasetId':kwargs['datasetId']}
        create_dataset = config.default_config.dataset_config.create_dataset
        response = requests.post(f"{self.base_url}{self.gateway}{create_dataset}",params=kwargs,headers=self.headers)
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False


    def _retrieve_all_rulesets(self,**kwargs):
        




