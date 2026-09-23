# Metadata

## Primary title
When a “Dry Run” Writes to Your Database | RustChain PR #8298

## Alternate titles
1. The Preview That Wasn't Read-Only — Fixing a Blockchain Migration Dry Run
2. How to Prove a Dry Run Is Actually Dry

## Description
A dry-run command should preview a state transition without changing the target. RustChain PR #8298 fixed two correctness problems in its UTXO genesis migration preview: the dry-run path could initialize UTXO schema objects, and its displayed state root could describe current on-disk state instead of the prospective genesis boxes.

The merged fix opens the preview database read-only, constructs prospective boxes in memory, computes the preview root from those boxes, and adds regression tests proving the schema stays unchanged and the preview root matches a real migration from identical balances.

Source PR:
https://github.com/Scottcjn/Rustchain/pull/8298

Related bounty:
https://github.com/Scottcjn/rustchain-bounties/issues/2819

RustChain:
https://github.com/Scottcjn/Rustchain

Author: @mdmcl-pixel  
AI assistance disclosed.

## Chapters
00:00 What “dry run” should mean
00:25 The genesis migration
01:05 Hidden schema mutation
01:55 The wrong preview root
02:50 Regression proof
03:35 The general safety invariant
04:20 Closing lesson

## Tags
RustChain, Python, SQLite, blockchain, migration, dry run, UTXO, testing, reliability engineering, state migration, open source

## Thumbnail text
**DRY RUN… THAT WRITES?**
