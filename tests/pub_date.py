import re
from datetime import datetime
s = '2021. 4. 15. ... Docker 이미지 배포 가능한 PaaS (K8s + Helm)- Heroku 와 비슷한 UI로 상태/로그/히스토리 확인- AWS/GCP/DO 의 K8s 클러스터에 쉽게 배포 가능\xa0...'

match_date_string = re.search(r'\d{4}. \d{1,2}. \d{1,2}.', s)
print(match_date_string)
match_date = datetime.strptime(match_date_string.group(), "%Y. %m. %d.").date()


