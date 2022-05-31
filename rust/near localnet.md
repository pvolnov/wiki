https://docs.near.org/docs/tools/kurtosis-localnet

# cross kurtosis
brew install kurtosis-tech/tap/kurtosis-cli
kurtosis config init dont-send-metrics

curl -o ~/launch-local-near-cluster.sh https://raw.githubusercontent.com/kurtosis-tech/near-kurtosis-module/master/launch-local-near-cluster.sh -L
chmod u+x ~/launch-local-near-cluster.sh

~/launch-local-near-cluster.sh
~/launch-local-near-cluster.sh --execute-params '{"backendIpAddress":"1.2.3.4"}'


alias local_near='NEAR_ENV="local" NEAR_CLI_LOCALNET_NETWORK_ID="localnet" NEAR_NODE_URL="http://127.0.0.1:62285" NEAR_CLI_LOCALNET_KEY_PATH="/Users/benjaminkurrek/.neartosis/2021-12-02T13.37.41/validator-key.json" NEAR_WALLET_URL="http://127.0.0.1:62292" NEAR_HELPER_URL="http://127.0.0.1:62286" NEAR_HELPER_ACCOUNT="test.near" NEAR_EXPLORER_URL="http://127.0.0.1:62290" near'


# Full local
