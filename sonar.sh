export ACCESS_TOKEN=$(curl -X POST "https://accounts.zoho.com/oauth/v2/token?client_id=1000.YGGMXBB1YU9A40C80WHS8OSBDB3XQP&client_secret=051c88c05a0441e2cd428cc5e14fbee829432984ba&redirect_uri=http://application_name.com/&grant_type=refresh_token&scope=ZohoCliq.Channels.CREATE,ZohoCliq.Channels.READ,ZohoCliq.Channels.UPDATE,ZohoCliq.Channels.DELETE,ZohoCliq.Webhooks.CREATE&refresh_token=1000.e1bfbdf5bf6e538ac9b24d9ce2f59993.a9fd55931be231c784cad769af8c51e5" | jq '.["access_token"]' | sed 's/\"//g')

record=$(curl -s "https://sonarcloud.io/api/measures/component_tree?component=HimanshuKapoor328_bc-25&metricKeys=reliability_rating&ps=100&p=1")
value=$(echo $record | jq -r '.baseComponent.measures[0].value')
export value

python3 /home/runner/work/bc-25/bc-25/msg.py


# RATING=$(curl -u $SONAR_TOKEN: "https://sonarcloud.io/api/measures/component?component=sonar-test-ayush&metricKeys=reliability_rating" | jq '.["component"]["measures"][0]["value"]')
