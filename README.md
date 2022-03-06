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

____________

## Eventbridge
1. Go to Amazon Eventbridge and create a new rule
2. Set Event pattern as one of [these custom patterns](https://github.com/gavinsauder/discord-aws-deployment-notifications/tree/main/eventbridge-rules)
3. Set Target as "SNS Topic"
4. Set Topic as the new SNS topic we created for these notification messages
5. Configure Target Input as "Input transformer"
6. Set Input Path to set a varible to be used in the message: {"pipeline":"$.detail.pipeline"} or use {"deploy":"$.detail.application"}
7. Finally, set your message with quotes. Such as: "The application \**\<pipeline>** has deployed successfully.  :white_check_mark:"
