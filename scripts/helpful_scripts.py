from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3


DECIMAL = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks(account):
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")

    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMAL, STARTING_PRICE, {"from": account})

    print("Mocks Deployed!")
