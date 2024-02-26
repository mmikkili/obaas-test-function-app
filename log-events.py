import os
from azure.eventgrid import EventGridConsumer

# Set your Azure Event Grid topic endpoint and key
topic_endpoint = os.environ["https://mycustomtopicmmikkili.eastus2-1.eventgrid.azure.net/api/events"]
topic_key = os.environ["tIoSa+X9Loq/IA8CDEdYz3jwagYZZJrqVT9EXleymWQ="]

# Create an Event Grid consumer
consumer = EventGridConsumer()

# Define a callback function to handle incoming events
def handle_event(event):
    # Log the event data
    print("Received event:")
    print(event)

# Start consuming events from the subscription
consumer.consume_events(topic_endpoint, topic_key, handle_event)