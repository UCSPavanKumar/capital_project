from EDQClientRest import EDQClientRest
from s3_handler import S3handler
import pandas as pd
from datetime import datetime
import datetime

class DQhandler(EDQClientRest):
    def __init__(self) -> None:
        self.s3_handler = S3handler()
        super().__init__(self)
    
    def _create_ruleset(self):
        """
        Create ruleset for the dataset ID
        """
        pass
    
    def _create_ruleset(self):
        """
        creation of ruleset and attach rulelist to the ruleset
        """
        rulelist = self._create_rulelist()
        response = self._create_rulesetId(rulelist)
        return response


    def _create_rulelist(self):
        csv_data = self.s3_handler.get_s3_file()
        df = pd.read_csv(csv_data)
        columns = df.columns
        rulelist = []
        for col in columns:
            data = {"column_name":col,"description":"xyz","data_type":"String","rule_type":"NOT_NULL","client":"capitalone"}
            rule = self._create_rule_payload(data)
            rulelist.append(rule)
        return rulelist
    
    def _create_rule_payload(self,**kwargs):
        payload = {
            "ruleName":kwargs['column_name']+'_not_null_check',
            "description":kwargs["description"],
            "fieldName":kwargs['column_name'],
            "ruleType":"NOT_NULL",
            "ruleTags":[
                kwargs['column_name']+'_not_null'
                ],
                "inputFilter":{
                    "filterConditionsOperator":"AND",
                    "filterConditions":[
                        {
                            "fieldName":kwargs['datatype'],
                            "filterType":kwargs['rule_type']
                        }
                    ]
                },
                "ruleVersion":1,
                "createdByClientId":kwargs["client"],
                "createdUtcTimeStamp":datetime.now(datetime.timezone.utc)
        }

        return payload
    

    

 




