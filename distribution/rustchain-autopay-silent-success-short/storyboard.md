# Storyboard — 9:16 vertical

## 0:00–0:05 — Hook
Capture the title of Scottcjn/Rustchain PR #8474 in a mobile-width browser crop.
Overlay: **“GREEN WORKFLOW. NO PAYMENT?”**
Slow 105% push-in. No third-party footage.

## 0:05–0:15 — The lock
Capture the PR description paragraph explaining the Git-ref mutex and orphaned lock.
Overlay a simple generated diagram:
`runner → create lock ref → crash → orphaned ref`

## 0:15–0:26 — Silent success
Capture the removed lines from the PR diff:
`Payment already in progress ... Skipping.`
`return False`
Highlight only those lines.
Overlay: **“422 → SKIP → NORMAL RETURN”**

## 0:26–0:34 — Why it matters
Use an original two-column graphic:
Left: “Transfer: DID NOT HAPPEN”
Right: “Workflow: CAN LOOK SUCCESSFUL”
Do not show a fabricated balance or transaction.

## 0:34–0:44 — The fix
Capture the added PR diff where the code emits `::error::` and raises `RuntimeError`.
Then capture the test change wrapping the second run in `pytest.raises(...)`.
Overlay: **“FAIL LOUDLY”**

## 0:44–0:50 — Result
Capture the maintainer approval on PR #8474 and the merged state badge.
Overlay:
**“ONE TRANSFER ATTEMPT”**
**“NO SILENT NO-PAYMENT”**
End card: “RustChain • public fix • PR #8474”

All captures must come from the public GitHub pages listed in SOURCES.md. Use original screen captures or generated text/shape graphics only.
