# Discord Notifications for AWS Deployments
Setup your AWS account to receive discord notifications for code deploy and code pipeline status messages. Receive a message if a deployment or pipeline fails or succeeds.

There are 3 pieces that need setup in your AWS account. 

1. Eventbridge
   - Setup triggers for what messages you want to send and what you want the messages to say
2. Amazon SNS
   - Configure connector between Eventbridge and Lambda function 
3. Lambda Function
   - Setup function and required dependancies to send webhook request


You will also need an webhook url from the discord channel you'd like to receive these messages in. And you finally need to create the dependencies for your Lambda function imports.

____________

## Lambda Setup
1. Go to Amazon Lambda and create a new function with Python 3.8 runtime
2. Use this script [the source code](https://github.com/gavinsauder/discord-aws-deployment-notifications/blob/main/lambda_function.py)
3. Add your discord webhook to this script
4. Click save and exit function edit page. 
5. We need to create the python dependencies required for python to run. We'll do this using ubuntu & docker
   - 1. In ubuntu, create a python virtual environment with this command: `python3 -m venv venv`
   - 2. Activate the virtual environment: `source venv/bin/activate`
   - 3. Create a file of python dependancies: `sudo pip freeze > requirements.txt`
   - 4. I edited this requirements.txt and remove everything exept those referencing "requests" and "json"
   - 5. Now use docker to build these dependancies we listed in this requirements.txt file: `docker run --rm --volume=$(pwd):/lambda-build -w=/lambda-build lambci/lambda:build-python3.8 pip install -r requirements.txt --target python`
   - 6. If successful, zip the python folder it created: `zip -r layer python/`
8. On the Lambda Layers page, create a new layer and upload this newly created zipped folder of python dependancies
9. Go back to your function and add your custom layer you just created

## SNS Setup
1. Go to SNS and create a new topic
2. Create a subscription for this topic with a protocol of "AWS Lambda"
3. Select your Lambda function as the subscription endpoint
4. Go back to your Lambda function and set a new trigger as "SNS" and choose your SNS topic

## Eventbridge Setup
1. Go to Amazon Eventbridge and create a new rule
2. Set Event pattern as one of [these custom patterns](https://github.com/gavinsauder/discord-aws-deployment-notifications/tree/main/eventbridge-rules)
3. Set Target as "SNS Topic"
4. Set Topic as the new SNS topic we created for these notification messages
5. Configure Target Input as "Input transformer"
6. Set Input Path to set a variable to be used in the message: `{"pipeline":"$.detail.pipeline"}` or use `{"deploy":"$.detail.application"}`
7. Finally, set your message with quotes. Such as: `"The application **<pipeline>** has deployed successfully. :white_check_mark:"`


Congrats! You should now start receiving discord messages for the eventbridge rule you just created. Eventbridge receives messages from cloudwatch and allows you to create a message to be sent to SNS. SNS relays your message to the lambda function, and then lambda passes that message on to the discord webhook.

You can create more than 1 eventbridge rule attached to the same SNS message. I created a 3 eventbridge rules: pipeline success, pipeline fail, and also deployment success.
