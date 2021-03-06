## Injective Python SDK

### Dependencies

**Ubuntu**
```bash
sudo apt install python3.X-dev autoconf automake build-essential libffi-dev libtool pkg-config
```
**Fedora**
```bash
sudo dnf install python3-devel autoconf automake gcc gcc-c++ libffi-devel libtool make pkgconfig
```

**macOS**

```bash
brew install autoconf automake libtool
```

### Quick Start
Installation
```bash
pip install injective-py
```

### Usage
Requires Python 3.7+

[Examples](https://github.com/InjectiveLabs/sdk-python/tree/master/examples)
```bash
$ pipenv shell
$ pipenv install

# connecting to Injective Exchange API
# and listening for new orders from a specific spot market
$ python examples/async/exchange_client/spot_exchange_rpc/8_StreamOrders.py

# sending a msg with bank transfer
# signs and posts a transaction to the Injective Chain
$ python examples/async/chain_client/1_MsgSend.py
```
Upgrade `pip` to the latest version, if you see these warnings:
  ```
  WARNING: Value for scheme.platlib does not match. Please report this to <https://github.com/pypa/pip/issues/10151>
  WARNING: Additional context:   user = True   home = None   root = None   prefix = None
  ```

### Development
1. Generate proto binding & build
  ```
  make gen
  python -m build
  ```

2. Enable dev env
  ```
  pipenv shell
  pipenv install --dev
  ```

3. Install pkg
  ```
  # from local build
  pip uninstall injective-py
  pip install injective-py --no-index --find-links /path/to/injective/sdk-python/dist

  # from pypi
  pip uninstall injective-py
  pip install injective-py
  ```

4. Fetch latest denom config
```
python pyinjective/fetch_metadata.py
```

Note that the [sync client](https://github.com/InjectiveLabs/sdk-python/blob/master/pyinjective/client.py) has been deprecated as of April 18, 2022. If you are using the sync client please make sure to transition to the [async client](https://github.com/InjectiveLabs/sdk-python/blob/master/pyinjective/async_client.py), for more information read [here](https://github.com/InjectiveLabs/sdk-python/issues/101)


### Changelogs
**0.5.6.6**
* Add PO orders in local order hash computation function
* Add automatic timeout height in transactions
* Add automatic session renewal for K8S
* Add MsgDelegate and MsgWithdrawDelegatorReward in the composer
* Re-gen ini files

**0.5.6.5**
* Add MsgRelayPriceFeedPrice in the composer
* Add Post-only orders in the composer
* Add OrderbooksRequest in the clients
* Add support for multiple markets in StreamTrades and StreamPosition
* Add support for multiple subaccounts in StreamTrades and StreamPosition
* Add K8S endpoint to mainnet network options
* Add MsgRegisterAsDMM to the composer
* Add functions to close chain/exchange channels
* Re-gen ini files


**0.5.6.4**
* Add K8S endpoint on testnet as default
* Add root CA certs for mainnet & testnet for secure gRPC connections
* Add method to unpack responses inside MsgExec
* Fix type hints in composer & clients
* Add Peggy contract ABI
* Add reduce-only support for market orders
* Add sticky session cookie for broadcast methods
* Add historical funding rates in clients
* Fixes in spot conversions for price/quantity returned from the backend
* Add MsgSendToEth & SendToCosmos in the composer for INJ <> ETH transfers
* Add function to compute order hashes locally
* Add load balancer endpoint on mainnet as default
* Re-gen ini files



## License

Apache Software License 2.0
