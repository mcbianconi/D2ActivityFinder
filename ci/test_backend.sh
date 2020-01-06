#!/bin/bash
export COMPOSE_PROJECT_NAME=destiny_project_${CI_COMMIT_SHA}
docker-compose -f docker/compose/test.yml run destiny_project unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
