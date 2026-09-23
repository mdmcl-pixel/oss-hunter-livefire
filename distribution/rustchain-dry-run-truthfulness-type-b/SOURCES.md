# Source Map

## Primary source — merged PR #8298
https://github.com/Scottcjn/Rustchain/pull/8298

Supports all of the following claims:
- `--dry-run` previously called UTXO table initialization against the target database.
- The fix opens the dry-run target read-only.
- The dry-run path only inspects existing UTXO tables when present and rejects partial schema.
- Prospective genesis boxes are built in memory for dry-run.
- The preview state root is computed from those prospective boxes rather than current on-disk UTXO state.
- The new tests prove schema non-mutation and preview-root equality with a real migration from identical balances.
- The PR body reports `2 passed in 0.12s`, successful Python compilation, and clean `git diff --check`.
- PR #8298 is merged.

## Related bounty context
https://github.com/Scottcjn/rustchain-bounties/issues/2819

Use only for context that the contribution was submitted within the RustChain UTXO/security review bounty lane. Do not infer a token-to-fiat value from the bounty.

## Claim safeguards
- No claim that production funds were lost.
- No claim that this defect was exploited.
- No claim that the preview wrote balances; the verified mutation was schema initialization.
- No unverified benchmarks or token prices.
- No private system evidence is required for the video.
