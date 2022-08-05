record=$(curl -s "https://sonarcloud.io/api/measures/component_tree?component=HimanshuKapoor328_bc-25&metricKeys=reliability_rating&ps=100&p=1")
value=$(echo $record | jq -r '.baseComponent.measures[0].value')
echo $value
A="1.0"
B="2.0"
C="3.0"
D="4.0"
if [[ "$value" = "$A" ]];
then
  python3 /home/runner/work/bc-25/bc-25/p1.py
elif [[ "$value" = "$B" ]];
then
  python3 /home/runner/work/bc-25/bc-25/p2.py
elif [[ "$value" = "$C" ]];
then
  python3 /home/runner/work/bc-25/bc-25/p3.py
elif [[ "$value" = "$D" ]];
then
  python3 /home/runner/work/bc-25/bc-25/p4.py
else
  python3 /home/runner/work/bc-25/bc-25/p5.py
fi

