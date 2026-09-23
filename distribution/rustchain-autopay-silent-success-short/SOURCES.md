# Sources and Claim Map

All claims are grounded in public repository evidence checked for this package.

## Source 1 — merged fix
https://github.com/Scottcjn/Rustchain/pull/8474

Supports:
- `scripts/auto-pay.py` used a Git ref as the payment mutex.
- An existing ref produced GitHub 422 / “reference already exists”.
- The previous branch printed “Payment already in progress ... Skipping.” and returned `False`.
- The merged change replaces that silent-success branch with an error message and `RuntimeError`.
- The regression test asserts the second run raises while still asserting exactly one created ref and one transfer attempt.
- PR #8474 was merged.

## Source 2 — payout audit bounty
https://github.com/Scottcjn/rustchain-bounties/issues/16471

Supports:
- The bounty specifically targets payout/reward paths that can report success while achieving nothing or the wrong effect.
- Silent-success failures in payout automation are an explicitly documented reliability problem in this ecosystem.

## Source 3 — maintainer review on PR #8474
https://github.com/Scottcjn/Rustchain/pull/8474#pullrequestreview-5253533507

Supports:
- Maintainer independently confirmed that an orphaned `rtc-autopay-locks/*` ref could turn later runs into a green “Skipping” outcome with no transfer.
- Maintainer agreed that failing loudly is the safe direction while one transfer remains protected.

## Wording safeguards
- The script says the workflow **could** finish without surfacing the failure; it does not claim a specific user lost funds.
- It does not claim production exploitation or production testing.
- It does not quote an RTC-to-fiat price.
- It does not expose credentials or private operational data.
