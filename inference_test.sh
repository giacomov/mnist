alias go='(echo -n "{\"data\": \""; base64 301.png; echo "\"}") |  curl -X POST       http://mnist-7-1.ca.apps.cnvrg.io/api/v1/endpoints/xsjyzrycxf9yhm2tdv3a -H "Cnvrg-Api-Key: JefSHWv2Kx8ikWW9Q7Q6KhRx" -H "Content-Type: application/json" -d @-'

for i in $(seq 1 100); do go; done
