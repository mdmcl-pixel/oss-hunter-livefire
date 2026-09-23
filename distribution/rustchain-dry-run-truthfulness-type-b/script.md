# Narration Script — 4–5 minutes

## 0:00–0:25 — Hook

A dry run is supposed to answer one question: “What would happen if I did this?” It should not quietly change the thing it is inspecting. In a blockchain migration tool, that distinction matters because preview commands are often used exactly when an operator is trying to reduce risk.

RustChain PR 8298 fixed a dry-run path that violated that expectation in two separate ways.

## 0:25–1:05 — The migration

The target was RustChain’s UTXO genesis migration. The tool reads existing account balances and creates the UTXO genesis boxes that represent those balances in the new model.

It also supports a `--dry-run` mode. The promise is straightforward: calculate what the migration would create, print the preview, and leave the target database unchanged.

Before the fix, that promise was not fully true.

## 1:05–1:55 — Bug one: a preview that writes

The old dry-run path constructed the normal UTXO database object and called its table-initialization routine against the real target database.

That meant a user could point dry-run at an account-only SQLite database and finish with new UTXO schema objects that did not exist before the preview.

The migration had not transferred balances, but the supposed read-only operation had still mutated the database schema.

PR 8298 changed the dry-run path to open the target SQLite database in read-only mode. It inspects existing UTXO tables only when they already exist, and it avoids the normal connection path that can enable journals or initialize schema.

The regression test makes the contract explicit: record the schema, run dry-run, then assert the schema is exactly unchanged.

## 1:55–2:50 — Bug two: the wrong state root

The second defect was subtler.

A dry run should report the root of the state it is proposing to create. But the old implementation called the normal on-disk state-root calculation after previewing the genesis boxes.

So the displayed root could describe the current UTXO state on disk rather than the prospective genesis state shown by the preview.

That is dangerous because a preview can look internally consistent while its integrity value refers to something else.

The fix builds the prospective genesis boxes in memory and computes their Merkle-style state root using the same leaf fields, ordering, count prefix and tree-reduction rules as the normal UTXO state-root calculation.

## 2:50–3:35 — How the fix is proved

The new regression suite tests both failure modes.

Test one creates a database containing only balances, runs dry-run, and proves the schema remains just the balances table.

Test two creates two identical balance databases. One is previewed with dry-run. The other runs the real migration. The test then asserts that the preview root exactly equals the root produced by the real migration, while the preview database still has no UTXO schema mutation.

The submitted validation reported two focused tests passing, Python compilation succeeding, and a clean diff check.

## 3:35–4:20 — Why this pattern matters

This is bigger than one migration script.

Operational software often has commands named dry-run, plan, preview, validate, or check. Users treat those words as a safety boundary. If the command writes state, creates schema, changes metadata, or reports integrity data for the wrong object, the command can make a risky operation harder to reason about instead of safer.

A good preview should satisfy two properties: observational behavior — it does not change the target — and semantic equivalence — the result it reports matches what the real operation would produce from the same starting state.

## 4:20–4:40 — Close

PR 8298 makes those properties executable instead of implied: read-only access for the preview, in-memory construction of prospective boxes, and a regression that compares preview output with a real migration.

The lesson is simple: if a tool says dry-run, “dry” should be a testable invariant, not just a flag name.
