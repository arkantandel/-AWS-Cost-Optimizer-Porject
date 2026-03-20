import boto3, os

ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    print("⚡ Executor triggered")

    resource_id = event.get("resourceId")
    action = event.get("action")

    if not resource_id or not action:
        return {
            "statusCode": 400,
            "body": "Missing resourceId or action"
        }

    if action == "stop_ec2":
        ec2.stop_instances(InstanceIds=[resource_id])
        return {
            "statusCode": 200,
            "body": f"EC2 {resource_id} stopped"
        }

    return {
        "statusCode": 400,
        "body": "Unknown action"
    }
