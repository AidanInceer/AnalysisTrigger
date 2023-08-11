import json

from google.cloud import pubsub_v1, storage


def trigger_(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """

    # fetch game json info from message
    # validate json message
    # publish message using the json data provided to the topic i

    bucket_name = event["bucket"]
    blob_name = event["name"]

    storage_client = storage.Client

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    contents = blob.download_as_string()

    data = json.loads(contents.decode("utf-8"))

    # Replace with your actual project ID and topic name
    project_id = 'united-axle-390115'
    topic_id = 'chess-analysis-trigger'

    # Compose the topic path
    topic_path = f'projects/{project_id}/topics/{topic_id}'

    # Publish the JSON data as a message
    publisher = pubsub_v1.PublisherClient()
    future = publisher.publish(topic_path, data=data.encode('utf-8'))

    return f"Message published successfully to {topic_path}"
