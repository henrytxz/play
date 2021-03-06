#!/bin/bash
#
# Log time in jira
#

## exports my credentials
. $HOME/.cw-passwd

## hardcoded creds
PP_USER=$USER
PP_PASS=$PASSWORD

MONTH=$1

## Jira issues for maintenance and new dev
MAINT=TT-7
NEWD=TT-8

#### CHANGE ME ####
## Day,TIME_IN_MAINT,TIME_IN_NEW
#WORK="$(for weekday in `weekdays.sh ${MONTH}`; do if [ $(( $RANDOM % 2 )) -eq 0 ]; then echo "${weekday},0h,8h"; else echo "${weekday},8h,0h"; fi; done)"
WORK="2017-11-1,8h,0h
2017-11-2,8h,0h
2017-11-3,8h,0h
2017-11-6,8h,0h
2017-11-7,8h,0h
2017-11-8,8h,0h
2017-11-9,8h,0h
2017-11-10,8h,0h
2017-11-13,8h,0h
2017-11-14,8h,0h
2017-11-15,8h,0h
2017-11-16,8h,0h
2017-11-17,8h,0h
2017-11-27,8h,0h
2017-11-28,8h,0h
2017-11-29,8h,0h
2017-11-30,8h,0h
"
for ENTRY in $WORK; do

DAY=$(echo "$ENTRY" | cut -d"," -f1 )
TIME_IN_MAINT=$(echo "$ENTRY" | cut -d"," -f2 | tr -d ' ')
TIME_IN_NEWD=$(echo "$ENTRY" | cut -d"," -f3 | tr -d ' ')

if [ "${TIME_IN_MAINT}" != "0h" ]; then
echo "Attempting to log ${TIME_IN_MAINT} on ${DAY} for ${MAINT} for Maintenance"
curl -s -u ${PP_USER}:${PP_PASS} -X POST -d "{\"started\": \"${DAY}T12:00:00.000-0400\", \"timeSpent\": \"${TIME_IN_MAINT}\"}" -H "Content-Type: application/json" "http://jira.pulse.corp/rest/api/2/issue/${MAINT}/worklog"
echo ""
fi

if [ "${TIME_IN_NEWD}" != "0h" ]; then
echo "Attempting to log ${TIME_IN_NEWD} on ${DAY} for ${NEWD} for New Development"
curl -s -u ${PP_USER}:${PP_PASS} -X POST -d "{\"started\": \"${DAY}T12:00:00.000-0400\", \"timeSpent\": \"${TIME_IN_NEWD}\"}" -H "Content-Type: application/json" "http://jira.pulse.corp/rest/api/2/issue/${NEWD}/worklog"
echo ""
fi

done
