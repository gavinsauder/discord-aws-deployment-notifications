# Get Discord Notifications for AWS Deployment Updates
Setup your AWS account to receive discord notifications for code deploy and code pipeline status messages. Receive a message if a deployment or pipeline fails or succeeds.

There are 3 pieces that need setup in your AWS account. 

1. Eventbridge
   - Setup triggers for what messages you want to send and what you want the messages to say
2. Amazon SNS
   - Configure connector between Eventbridge and Lambda function 
3. Lamda Function
   - Setup function and required dependancies to send webhook request


You will also need an webhook url from the discord channel you'd like to receive these messages in. And you finally need to create the dependencies for your Lambda function imports.
