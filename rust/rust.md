
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
sudo apt remove rustc

source $HOME/.cargo/env

sudo apt-get install cargo
sudo apt-get update
sudo apt-get upgrade

INDEXER
https://github.com/near/near-state-indexer

sudo apt-get install g++ libclang-dev libssl-dev git  -y

RUSTFLAGS="-C instrument-coverage" cargo build
cargo run --release -- --home-dir /root/.near/mainnet init --chain-id mainnet --download-config

cargo run --release -- --home-dir ~/.near/mainnet run --store-genesis --stream-while-syncing --non-strict-mode --stop-after-number-of-blocks 100 --concurrency 1 sync-from-latest

cargo run --release -- --home-dir ~/.near/mainnet run --store-genesis --non-strict-mode --concurrency 100 sync-from-block --height 62540760

git clone https://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@github.com/vdnank/indexer

sudo docker run -d --name some-redis -p 6379:6379 redis


sudo apt-get install ruby-dev
gem install redis-browser --version '~> 0.4.0'
redis-browser --url redis://207.180.214.78:6379


sudo apt-get install awscli -y


aws s3 --no-sign-request cp s3://near-protocol-public/backups/mainnet/rpc/latest .
LATEST=$(cat latest)
nohup aws s3 --no-sign-request cp --no-sign-request --recursive s3://near-protocol-public/backups/mainnet/rpc/$LATEST .  &


aws s3 --no-sign-request cp s3://near-protocol-public/backups/testnet/rpc/latest .
LATEST=$(cat latest)
nohup  aws s3 --no-sign-request cp --no-sign-request --recursive s3://near-protocol-public/backups/testnet/rpc/$LATEST . &