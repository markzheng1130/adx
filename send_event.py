import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def run():
    event_hub_name = 'test-hub'
    connecting_string = 'Endpoint=sb://markzheng1130eventhubnamespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=iPbqBo8Yx5guLC/o7DAuwf2qNX136u+byD3rabTqbhA='
    producer = EventHubProducerClient.from_connection_string(conn_str=connecting_string, eventhub_name=event_hub_name)
    async with producer:
        event_data_batch = await producer.create_batch()

        event_data_batch.add(EventData('First event '))
        event_data_batch.add(EventData('Second event'))
        event_data_batch.add(EventData('Third event'))

        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()

print(f'[start]')
loop.run_until_complete(run())
print(f'[end]')