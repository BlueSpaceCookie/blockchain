#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from .utils import (
    Wallet, HDPrivateKey, HDKey
)
from .network import *
import inspect


def generate_mnemonic(strength=128):
    _, seed = HDPrivateKey.master_key_from_entropy(strength=strength)
    return seed


def generate_child_id():
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(
        hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return int((int(now.strftime(
        '%y%m%d')) + seconds_since_midnight*1000000) // 100)


def create_address(network='btctest', xpub=None, child=None, path=0):
    assert xpub is not None

    if child is None:
        child = generate_child_id()

    # else ...
    wallet_obj = Wallet.deserialize(xpub, network=network.upper())
    child_wallet = wallet_obj.get_child(child, is_prime=False)

    net = JorisRobinMainNet

    return {
        "path": "m/" + str(wallet_obj.child_number) + "/" +str(child_wallet.child_number),
        "bip32_path": net.BIP32_PATH + str(wallet_obj.child_number) + "/" +str(child_wallet.child_number),
        "address": child_wallet.to_address(),
        # "xpublic_key": child_wallet.serialize_b58(private=False),
        # "wif": child_wallet.export_to_wif() # needs private key
    }

def create_wallet(children=1):
    seed = generate_mnemonic()

    net = JorisRobinMainNet
    wallet = {
        "coin": net.COIN,
        "seed": seed,
        "private_key": "",
        "public_key": "",
        "xprivate_key": "",
        "xpublic_key": "",
        "address": "",
        "wif": "",
        "children": []
    }

    my_wallet = Wallet.from_master_secret(network=net, seed=seed)

    # account level
    wallet["private_key"] = my_wallet.private_key.get_key().decode()
    wallet["public_key"] = my_wallet.public_key.get_key().decode()
    wallet["xprivate_key"] = my_wallet.serialize_b58(private=True)
    wallet["xpublic_key"] = my_wallet.serialize_b58(private=False)
    wallet["address"] = my_wallet.to_address()
    wallet["wif"] = my_wallet.export_to_wif()

    prime_child_wallet = my_wallet.get_child(0, is_prime=True)
    wallet["xpublic_key_prime"] = prime_child_wallet.serialize_b58(private=False)

    # prime children
    for child in range(children):
        child_wallet = my_wallet.get_child(child, is_prime=False, as_private=False)
        wallet["children"].append({
            "xpublic_key": child_wallet.serialize_b58(private=False),
            "address": child_wallet.to_address(),
            "path": "m/" + str(child),
            "bip32_path": net.BIP32_PATH + str(child_wallet.child_number),
        })
    return wallet