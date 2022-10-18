touch .pdrunner_creds
echo HELLO
export ID="01D9MEJ692U3JMT7QDMOJRJPBY"
export SECRET="01D9MEJ692Q8G5M0XIR1W4FGYJ"
export TOKEN="u+1zNxXJiNzLLLEkpKvg"
eval 'echo "id:$ID";echo "secret:$SECRET";echo "token:$TOKEN"' > .pdrunner_creds
ls
java -jar pd-runner.jar