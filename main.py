import json

from google.cloud import pubsub_v1, storage

PROJECT = "united-axle-390115"
TOPIC = "chess-analysis-trigger"


def analysis_trigger(event, context):
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

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    contents = blob.download_as_string()

    publisher = pubsub_v1.PublisherClient()
    topic_path = f"projects/{PROJECT}/topics/{TOPIC}"
    publisher.publish(topic_path, data=contents)

    return f"Message published successfully to {topic_path}"
