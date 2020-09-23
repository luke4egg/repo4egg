


# this command will build new docker image and store it locally only
docker build -t luke4egg/phase3:latest .
echo
echo "check if build above is successful"
read -p "and continue... " dummyVariableToPauseExecution


# this is an example how to push it to docker hub:
# docker push luke4egg/phase3:latest
# it is commented out since password is required

docker run --rm -it -p 8080:8080 luke4egg/phase3:latest


