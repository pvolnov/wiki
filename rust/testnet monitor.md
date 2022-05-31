
sudo apt-get install clang libzmq3-dev libssl-dev pkg-config libpq-dev build-essential -y



``
clap = { version = "3.1.0", features = ["derive"]}
```


git clone git@github.com:near/near-indexer-for-explorer.git
cd near-indexer-for-explorer
echo "DATABASE_URL=postgres://user:password@host/db_name" > .env

RUSTFLAGS="-C instrument-coverage" cargo build


./target/release/indexer-explorer --home-dir ~/.near/testnet init --chain-id testnet --download-config --download-genesis

cargo run --release -- --home-dir ~/.near/testnet init --chain-id testnet --download-config  --download-genesis

sleep 3600 && nohup cargo run --release -- --home-dir ~/.near/testnet/ run
nohup cargo run --release -- -z 9556 --home-dir ~/.near/testnet/ run &


nohup wget https://near-protocol-public.s3.ca-central-1.amazonaws.com/backups/mainnet/rpc/data.tar && tar -xf data.tar &


sudo mount -t ntfs /dev/md2 /root/
