1. Download the AWS CDK for your operating system. Because I'm on a Mac, I'll use Brew.
https://docs.aws.amazon.com/cdk/latest/guide/cli.html

2. Open up the terminal and inside of the directory where you want your new CDK app to exist, run the following command:
`cdk init app --language python`

3. You'll now see several different files and directories.

4. Notice how there's a `requirements.txt` file, which are the Python requirements needed to install the AWS CDK. Run:
`pip3 install -r requirements.txt`

4. Run `cdk deploy` and you'll see the new CloudFormation stack being created.

5. Run `cdk destroy` to destroy the CDK project in AWS