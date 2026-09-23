# Script — target 45–50 seconds

**0:00–0:05**  
Can a payment system fail while every dashboard still looks green? RustChain found a real example.

**0:05–0:15**  
Its auto-pay script uses a Git reference as a mutex. If a runner died after creating that lock but before cleanup, the reference could remain orphaned.

**0:15–0:26**  
On the next run, GitHub returned “reference already exists.” The old code printed “Payment already in progress — skipping” and returned normally.

**0:26–0:34**  
That meant no transfer, but the automation could still finish without surfacing the failure.

**0:34–0:44**  
Merged PR 8474 changed that branch to raise a RuntimeError instead. The regression test still confirms only one transfer attempt.

**0:44–0:50**  
Duplicate-payment protection stays. Silent non-payment does not. In payout automation, failing loudly can be safer than succeeding silently.
