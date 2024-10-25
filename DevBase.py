import requests
import config
import s3_handler


class DevBase:
    def __init__(self) -> None:
        self.s3_handler = s3_handler()

        self.base_url = config.default_config.base_url
        self.gateway  = config.default_config.gateway
        
        pass
    
    def _create_job_configuration(self,**kwargs):
        
        create_job = config.default_config.job_config.create_job
        payload = {}
        response = requests.post(f"{self.base_url}{self.gateway}{create_job}")


