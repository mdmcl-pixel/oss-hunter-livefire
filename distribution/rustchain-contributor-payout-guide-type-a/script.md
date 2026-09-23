# Narration Script — target 4–5 minutes

## 0:00–0:35 — The real path to a RustChain bounty

A RustChain contribution is not “open a pull request and hope.” The public contributor guide defines a specific path: find an open bounty or good first issue, comment before starting to reduce duplicate work, fork the repository, make a focused change, test it, open a pull request that references the issue, and get paid in RTC after merge.

The useful part is knowing which steps are mandatory before the pull request, and which steps happen only after acceptance.

## 0:35–1:15 — You do not need a wallet before the PR

One of the clearest rules is easy to miss: you do not need an RTC wallet address before opening your pull request. The contributor guide says the project asks for the wallet during the payout step after the pull request is merged.

That matters because payout setup should not block the engineering work. The sequence is review, merge, wallet request, then transfer from the community fund.

Merged PR #8271 added that clarification directly to CONTRIBUTING.md, so this is not an inferred workflow — it is a documented project rule.

## 1:15–2:05 — The quality gate is evidence, not volume

RustChain says it merges code that works against the live node, meaningful tests, documentation a human can follow end to end, security fixes with proof, and tools that make the ecosystem more useful.

The same guide explicitly rejects AI-generated bulk pull requests with no testing evidence, placeholder data, fake screenshots, and changes that do not match the bounty.

For practical verification, the repository gives live read-only endpoints such as /health, /api/miners, and /epoch. A contributor can use those to validate assumptions without pretending a production write happened.

## 2:05–2:55 — BCOS: know whether your PR needs a tier

For non-documentation pull requests, RustChain requires a BCOS tier label: BCOS-L1 for normal features and refactors, or BCOS-L2 for security-sensitive changes such as wallet, transfer, consensus, rewards, authentication, cryptography, or supply-chain work.

Documentation-only pull requests are exempt when they only touch documentation, Markdown, or common image and PDF files.

New code files also need an SPDX license header. The point is not ceremony for its own sake; the checks make provenance and review expectations explicit before merge.

## 2:55–3:40 — Keep the change small and reproducible

The public review guidelines are straightforward: keep the pull request focused, test locally, update documentation when behavior changes, and avoid unrelated changes.

For miner files, there is an extra reproducibility rule: four miner artifacts are pinned by SHA-256 in miners/checksums.sha256. If one changes, the manifest must be regenerated in the same commit or CI will fail even if thousands of other tests pass.

This is a good example of why evidence matters more than a large diff. A small change with the exact focused test is easier to review and safer to merge.

## 3:40–4:25 — Payment authority and the final handoff

The contributor guide also defines who can authorize an RTC bounty disbursement. Only @Scottcjn, or a clearly labeled project automation account acting on his behalf with a matching project-issued pending ID and transaction hash, counts as payout authority.

So a comment from an unrelated account saying “I will send the RTC” is not valid payout evidence.

The workflow ends with a clean separation: engineering evidence proves the contribution; merge proves acceptance into the codebase; the wallet handoff enables payment; and the project-issued payout evidence records the transfer.

## 4:25–4:45 — Close

If you want to contribute, start with the public CONTRIBUTING.md and an open issue, not with a giant speculative patch. Keep the change narrow, prove what you tested, use the right BCOS tier when required, and do not let wallet setup block the pull request.

The fastest path is usually the most auditable one: small scope, real evidence, clear merge, clear payout.
