default_config = {
    "base_url":'https://api-it.capitalone.com',
    'gateway':'/internal-operations.data-management/data-quality-configuration',
    "job_config":{
        "create_job":'/job-configurations',
        "search_by_job_id":"/job-configurations/{0}",
        "schedule_job":"/job-configuration-schedules"
    },
    "rule_config":{
        "create_ruleset":"/job-configuration-rulesets",
        "create-rule":"/job-configuration-rules"

    },
    "dataset_config":{
        "create_dataset":"/job-configuration-datasets"
    },
"datasets":{
    "PR_GR_A1_LEDGER":"3fa85f64-5717-4562-b3fc-2c963f66afa6"
}



}
