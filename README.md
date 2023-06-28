KOOGLE 실행

1. python -m venv venv

2. source venv/bin/activate 

3. pip install -r requirements.txt

```bash
export WHATAP_HOME=${PWD}
export LICENSE_KEY='LICENSE_KEY'

whatap-setting-config \                
--host 15.165.146.117 \
--license ${LICENSE_KEY} \
--app_name mtp_test \
--app_process_name python

whatap-start-agent python koogle_run.py
```


