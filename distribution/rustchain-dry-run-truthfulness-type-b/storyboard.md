# Storyboard — 16:9 YouTube, 4–5 minutes

## Scene 1 — 0:00–0:25
**Visual:** PR #8298 title in a browser crop, then an original title card reading “WHEN A DRY RUN ISN'T DRY”.
**Capture:** public GitHub PR only.
**On-screen text:** “Preview ≠ Mutation”.

## Scene 2 — 0:25–1:05
**Visual:** simple original diagram: Accounts DB → Genesis Migration → UTXO Boxes.
**Then:** show the PR summary sentence describing the intended `--dry-run` behavior.
**Motion:** slow left-to-right build of the diagram.

## Scene 3 — 1:05–1:55
**Visual:** crop of the removed call to `UtxoDB.init_tables()` in the dry-run path.
**Overlay:** “DRY RUN → init_tables() → schema changed”.
**Cut:** original before/after schema card:
- Before: balances
- After: balances + UTXO schema
Label this explicitly as a conceptual illustration, not a production screenshot.

## Scene 4 — 1:55–2:50
**Visual:** show the old on-disk `compute_state_root()` call, then the added `_state_root_from_boxes(preview_boxes)` branch.
**Overlay:** “CURRENT STATE ROOT” crossed out → “PROSPECTIVE STATE ROOT”.
**Diagram:** boxes in memory → sorted leaves → pairwise hashes → root.

## Scene 5 — 2:50–3:35
**Visual:** display the two regression-test names from the PR diff.
**Split screen:**
Left: “Schema unchanged”
Right: “Preview root = real migration root”
**Proof card:** “2 passed in 0.12s” exactly as reported in the PR body.

## Scene 6 — 3:35–4:20
**Visual:** original checklist animation:
1. No writes
2. No schema creation
3. Preview describes proposed state
4. Preview equals real result from same input
**Caption:** “Make safety promises executable”.

## Scene 7 — 4:20–4:40
**Visual:** merged PR badge/state from public GitHub.
**End card:** “If it says DRY RUN, test that it is dry.”
Small footer: “RustChain PR #8298 · @mdmcl-pixel”.

### Rights / capture notes
Use only original diagrams/title cards and screen captures from the public GitHub URLs in SOURCES.md. No third-party footage, music, logos beyond ordinary GitHub/RustChain public-page capture needed. Do not show private wallets, credentials or production dashboards.
