
Macros
-----

```rust
macro_rules! pay_win {
    // using a ty token type for macthing datatypes passed to maccro
    ($self:expr, $bets:ident, $multiplicator:expr) => {
        for user in $self.$bets.iter() {
            let amount = user.1 * $multiplicator;
            $self.game_balance = $self.game_balance - amount;

            let account_id = user.0;
            let old_deposit = $self.users_balance.get(&account_id);
            let deposit = old_deposit.unwrap_or(0) + amount;
            $self.users_balance.insert(&account_id, &deposit);
            env::log(
                format!(
                    "Send user win {} to {}, total balance : {}",
                    amount, account_id, deposit
                )
                .as_bytes(),
            );
        }
    };
}
```