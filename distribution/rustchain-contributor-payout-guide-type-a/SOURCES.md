# Sources and Claim Map

## Source 1 — RustChain CONTRIBUTING.md
https://github.com/Scottcjn/Rustchain/blob/main/CONTRIBUTING.md

Supports:
- Quick-start flow: browse bounties / good-first issues, comment, fork, submit a PR, payment after merge.
- Code should work against the live node and include meaningful evidence.
- AI-generated bulk PRs without testing evidence, placeholder data and fake screenshots are rejected.
- Read-only live endpoints include `/health`, `/api/miners`, and `/epoch`.
- RTC wallet address is not required before opening the PR; the wallet is requested during payout after merge.
- BCOS tier label is required for non-doc PRs; L1 for normal work, L2 for security-sensitive wallet/transfer/consensus/reward/auth/crypto/supply-chain work.
- Documentation-only exception and SPDX requirement for new code files.
- Review guidance to keep PRs small, tested, documented, and free of unrelated changes.
- Four miner artifacts are checksum-pinned and require regenerating `miners/checksums.sha256` when changed.
- Only @Scottcjn or clearly labeled project automation with matching project-issued pending ID + transaction hash is payout authority.

## Source 2 — merged PR #8271
https://github.com/Scottcjn/Rustchain/pull/8271

Supports:
- The wallet-timing clarification was added by a merged change.
- Exact rule: an RTC wallet is not needed before opening the PR; the project asks for it during payout after merge.

## Source 3 — repository
https://github.com/Scottcjn/Rustchain

Supports project identity and public source availability.

## Safeguards
No token-to-fiat value is quoted. No payout is described as guaranteed. No private account or wallet balance is shown. The video distinguishes documented process from final maintainer acceptance.
