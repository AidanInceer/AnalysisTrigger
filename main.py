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

    # Compose the topic path
    topic_path = "projects/united-axle-390115/topics/chess-analysis-trigger"

    # Publish the JSON data as a message
    publisher = pubsub_v1.PublisherClient()
    publisher.publish(topic_path, data=data.encode('utf-8'))

    return f"Message published successfully to {topic_path}"
