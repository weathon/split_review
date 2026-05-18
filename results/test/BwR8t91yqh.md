Here is my consolidated review, synthesized from the paper content and the reviewer inputs.

---

## Summary

This paper introduces Interactive Speculative Planning, a system that accelerates LLM-based agent planning by running a fast approximation agent (A) in parallel with a slow target agent (T), accepting A's output when it matches T's, and falling back to T on mismatch. A novel UI rescheduling mechanism presents the asynchronous outputs sequentially and allows users to actively interrupt prolonged computations. Experiments on OpenAGI and TravelPlanner across four different A/T configurations show 20–42% average latency reductions, and the paper provides theoretical analysis of worst-case bounds on time, tokens, and concurrency rate.

## Strengths

1. **Novel human-centered co-design of system and UI for agent efficiency.** The paper is the first to combine speculative execution (borrowed from LLM decoding) with an interactive UI that treats human interruptions as a first-class acceleration mechanism rather than a nuisance. The three-agent framing (A, T, human) in Section 3 and the UI design in Algorithm 2 that enables active (not just prompted) user intervention are genuine contributions.

2. **Comprehensive theoretical analysis with formal bounds.** Section 4 provides closed-form expressions for latency (Eq. 3), total tokens (Eq. 6–7), and concurrency rate (Eq. 10), with explicit best-case and worst-case derivations. The worst-case guarantee that speculative planning is upper-bounded by normal planning time (line 257) provides a useful formal assurance under idealized (constant-time, no-interference) assumptions.

3. **Consistent and significant empirical latency reductions across diverse settings.** On OpenAGI, total time reductions range from 20.37% (Setting 4, direct generation) to 42.30% (Setting 3, multi-agent debate). On TravelPlanner, reductions range from 19.18% to 25.46%. The experiments span four different A/T combinations (DG→DG, DG→CoT, DG→ReAct, CoT→MAD) with different backbone models (GPT-3.5-turbo, GPT-4-turbo), demonstrating robustness.

4. **Systematic simulation ablation of key hyperparameters.** Section 4.4 provides three simulation series varying A's accuracy, A's speed, and the lookahead parameter k, giving practical guidance about operating regimes (e.g., k < 3 is suboptimal; higher accuracy always helps). The user interruption simulation (Figure 9) supports the claim that active human input further reduces latency.

5. **Honest and detailed discussion of limitations.** Section 6 transparently acknowledges the exact-match acceptance bottleneck, the spectre-like security vulnerabilities, the additional cost burden, and the lack of backtracing in the UI. This candor strengthens the paper's credibility.

## Weaknesses

### Fatal
None.

### Major

1. **The practical latency guarantee fails in a non-trivial fraction of cases, and the paper does not characterize this failure.** The theoretical worst-case bound (Eq. 3) assumes constant per-step times and no cross-call interference. The experiments confirm negative latency improvement cases exist in "almost all settings for both datasets" (line 508), and the paper correctly attributes this to token-generation randomness and API concurrency overhead (line 509). However, it does not report: (a) what fraction of tasks show negative improvement, (b) how large the slowdown is in those cases, or (c) what mitigations exist (e.g., reducing k in rate-limited settings). A reader cannot assess whether the method is safe to deploy in a given environment. This is the most significant threat to the paper's central claim that speculative planning "will not exceed the time taken by the traditional, non-speculative approach" (line 257). *Note: The paper does identify the cause of the discrepancy, which is more than the harsh critic gives it credit for, but the lack of characterization is a genuine gap.*

2. **The exact-match acceptance criterion makes the reported empirical results conservative lower bounds whose distance from the method's potential is unknown.** The paper itself states this limitation clearly (Section 6): exact match "is overly aggressive and inefficient, as it essentially decreases the accuracy of A" (line 556). On OpenAGI (limited action space), exact match is defensible. On TravelPlanner, the Levenshtein-based soft match on parameters helps but does not handle semantically equivalent but surface-different outputs. The paper does not quantify how often mismatches are truly errors versus acceptable alternatives (e.g., via manual inspection of a sample). Because the same strict match is used both as the acceptance gate during execution and as the accuracy metric for A, the reported latency improvements and accuracy numbers are coupled in a way that conflates implementation conservatism with the algorithm's potential. This is a real limitation — though honestly disclosed, it weakens the headline results.

### Minor

3. **The UI rescheduling algorithm (Algorithm 2) is underspecified.** The pseudocode describes a single decision step (choose whether to present the next A output or next T output based on trackers), but the overall control loop is not specified: when is this function called relative to the async process completion? How do the process queues (As, Ts) get populated and updated? The signal handler for user interruption is sketched but its integration with the main event loop, race conditions, and how user input feeds back into the agent trajectory are not specified. For a paper foregrounding "co-design of system and user interface," this level of specification is insufficient for reproducibility. *However, the conceptual design is clearly described in prose (Section 3.2), so this is a reproducibility gap, not a conceptual flaw.*

4. **No ablation of the lookahead parameter k in real experiments.** All real-world experiments use k=4 (line 383). The simulations (Section 4.4) show k substantially affects both latency and token cost, and the theoretical analysis identifies k as a key control parameter. A small real-world ablation (e.g., k ∈ {2, 4, 8} on one benchmark) would validate whether the simulation trends hold under realistic API conditions and would provide practical deployment guidance.

5. **Cost increase is reported but the latency–cost trade-off is not analyzed.** Tables 1 and 2 show speculative planning consistently costs more than normal planning. The paper acknowledges this in Section 6 but does not discuss when the latency savings (20–40%) justify the extra cost, nor does it provide a cost-sensitivity analysis. For a practitioner, the value proposition depends on this trade-off, which remains unquantified.

6. **Minor numerical discrepancy in reported reduction.** For TravelPlanner Setting 3, the paper states total time reduction of 25.46% (line 421), but the values in Table 2 (568.10 speculative vs. 733.12 normal MAD) yield 22.51%. The other settings match closely or exactly. This appears to be a calculation or rounding issue and should be corrected.

### Trivial
None of consequence.

## Nice-to-Haves

- A simulation with non-constant (e.g., log-normal or empirically sampled) step times would better characterize when negative latency improvements are likely.
- A comparison against a "parallel-only" baseline (always take T's answer from k parallel calls) would isolate how much of the speedup comes from parallelism versus from A's cheaper per-step generation.
- Reporting histograms or percentile breakdowns of latency improvement (rather than just mean±std) would clarify the distribution and the frequency of negative-improvement cases.

## Removed Points

These points were removed per verification against the paper; they are flagged here for completeness:

- **"The paper's theoretical guarantee does not hold"** — kept as Major weakness 1, but the paper *does* identify the cause of the discrepancy (lines 508–509), contrary to the reviewer's framing that it "does not adequately analyze why."
- **"Novelty claim about 'first system' needs qualification"** — removed as a scope-creep nitpick. The paper adequately positions itself against EcoAssistant and System-1.x Planner (line 58), and the claim is about the *combination* of speculative parallelism with an interactive UI, which is reasonable.
- **"Exact match is used both as condition and metric" conflating implementation with evaluation** — kept but downgraded from the reviewer's framing. The paper acknowledges this limitation explicitly (Section 6), so it is not a hidden flaw, but it is a genuine limitation of the main results.
- **"Reproducibility: code not released"** — removed per hard rules (cited releases are assumed to exist as of 2026-05-17; code release is promised).
- **"Pure formatting/style nitpicks"** — removed per hard rules.

## Novel Insights

The reviewers' complementary perspectives surface one insight beyond the paper's own contributions: the speculative planning approach for agents faces a structural tension that speculative decoding for LLMs does not. In decoding, the draft model and target model operate on the same token-level output space, making exact-match verification natural. For agent planning, the output space (action steps) is sparser and admits many valid alternatives, so exact-match verification is an artificial bottleneck. The paper's honest acknowledgment of this (Section 6) inadvertently highlights that **planning is a fundamentally harder domain for speculative execution than language generation**, and that semantic or learned verification is not a nice-to-have but a requirement for the idea to reach its potential. This makes the paper's empirical results *lower bounds* in a stronger sense than usual — they demonstrate viability under the hardest verification regime.

## Suggestions

1. **Characterize the negative-improvement cases.** Report the fraction of tasks with negative latency improvement, the magnitude of slowdown in those cases, and the correlation with A's accuracy and k. This would make the practical limitations explicit and allow the authors to recommend operational regimes.
2. **Measure the actual API latency degradation under concurrency.** Control k on one benchmark and plot per-step latency vs. concurrent call depth to show where the parallelism overhead erodes the speculative gains.
3. **Replace exact-match acceptance with a semantic or LLM-based verifier in at least one experiment.** Even a small-scale manual audit (e.g., sample 50 mismatched cases and report how many are actually acceptable alternatives) would bound the gap between current results and the method's potential.
4. **Specify the UI control loop fully.** Provide pseudocode for the main event loop, clarify how process queues are managed, and describe the interaction between signal handlers and the presentation thread.
5. **Correct the TravelPlanner Setting 3 TT reduction percentage** (or clarify the calculation if the discrepancy stems from a different aggregation method).

## Score and Decision

This paper introduces a well-motivated and original approach to agent latency reduction, with solid theoretical analysis, diverse empirical validation, and transparent discussion of limitations. The core idea (speculative parallelism for agent planning + interactive UI) is sound and the reported latency improvements (20–42%) are practically meaningful. However, two unresolved issues keep the contribution from being fully convincing: (1) the theoretical worst-case guarantee does not hold under realistic API concurrency, and the paper does not characterize when or how badly it fails; (2) the exact-match acceptance criterion means the empirical results are lower bounds whose gap from the method's true potential is unknown. These are fixable but non-trivial. The contribution is real and should be accepted, pending attention to the practical latency analysis and acceptance criterion in a revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>