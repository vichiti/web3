from hedera import (
    Client,
    ContractExecuteTransaction,
    AccountId
)
from app.config import Config

client = Client.for_testnet()
client.set_operator(AccountId.from_string("0.0.your-account-id"), "your-private-key")

def get_counter(contract_id):
    response = (
        ContractExecuteTransaction()
        .setContractId(contract_id)
        .setGas(100000)
        .setFunction("getCounter")
        .execute(client)
    )
    return response.get_receipt(client).call_result.to_int()

def increment_counter(contract_id):
    response = (
        ContractExecuteTransaction()
        .setContractId(contract_id)
        .setGas(100000)
        .setFunction("increment")
        .execute(client)
    )
    return response.get_receipt(client).transaction_id.to_string()