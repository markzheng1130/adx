from azure.kusto.data import KustoClient, KustoConnectionStringBuilder

cluster = "https://mkadxcluster.eastus.kusto.windows.net"
kcsb = KustoConnectionStringBuilder.with_az_cli_authentication(cluster)
client = KustoClient(kcsb)

db = "TestDatabase"
query = "TestTable | take 3"

response = client.execute(db, query)

for row in response.primary_results[0]:
    print(f'{row}')
