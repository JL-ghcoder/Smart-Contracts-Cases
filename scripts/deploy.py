from brownie import FundMe, network, config
from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
 
def deploy_fund_me():
    account = get_account()
    funde_me = FundMe.deploy({"from": account})
    print(f"Contract deployed to {funde_me.address}")


def main():
    deploy_fund_me()