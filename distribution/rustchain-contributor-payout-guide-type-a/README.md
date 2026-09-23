# RustChain Contributor Payout Guide — Type A Full Production Kit

**Bounty:** Scottcjn/rustchain-bounties#16601  
**Package:** Type A — YouTube full production kit  
**Author credit:** @mdmcl-pixel  
**Target runtime:** ~4–5 minutes  
**Working title:** *From First PR to RTC Payout: How RustChain Contributions Actually Move*

## Pitch

A practical contributor-facing video that follows the verified RustChain path from choosing a task, through testing and BCOS requirements, to merge and RTC payout. It focuses on the parts that commonly create avoidable friction: when a wallet is actually required, which PRs need BCOS labels, what “test against the live node” means, and who is authorized to issue a payout notice.

This is distinct from the author's prior #16601 packages:
- Type C: auto-pay orphaned-lock silent-success fix (Rustchain PR #8474)
- Type B: UTXO genesis dry-run correctness (Rustchain PR #8298)

## Package contents

- `script.md` — full narration script
- `voiceover/*.txt` — exact per-section narration source
- `voiceover/*.wav` — generated narration audio after the asset workflow runs
- `voiceover/ENGINE.md` — engine and rebuild instructions
- `visuals/*.png` — original 1920×1080 diagrams/title cards
- `assembly.md` — timed edit map
- `thumbnail.png` + 2 alternates — 1280×720
- `metadata.md` — titles, description, chapters and tags
- `SOURCES.md` — claim-by-claim source map
- `build_assets.py` — deterministic asset generator

All claims are grounded in the public RustChain repository and merged PR #8271. No private account state, secret, payout balance, or fabricated transaction is shown.

AI assistance was used to draft, verify, and package this deliverable. By submitting it under bounty #16601, @mdmcl-pixel grants Elyan Labs permission to publish this package's content on official channels with permanent author attribution, consistent with the bounty terms.
