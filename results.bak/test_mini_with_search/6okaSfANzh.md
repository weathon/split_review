## Summary

This paper introduces an LLM cascade for cost-efficient reasoning, where a weaker LLM (GPT-3.5-turbo) answers each question first, and a decision-maker based on *answer consistency* determines whether to route the question to a stronger LLM (GPT-4). The key novelty is using a **mixture of thought (MoT) representations**—simultaneously sampling from Chain-of-Thought and Program-of-Thought prompts—to generate diverse samples whose agreement signals question difficulty. The paper instantiates ten cascade variants (vote-based and verification-based) and evaluates them on six reasoning benchmarks. The headline result—MoT cascades matching GPT-4-CoT-SC accuracy (~0.929 vs 0.931) at 40% of the cost—is well-supported by the experiments.

---

## Strengths

1. **Novel and practical MoT-based routing signal.** The idea of using *cross-representation* consistency (CoT vs. PoT) as a routing signal is both clean and effective. Unlike prior cascades that train external verifiers, this approach is training-free and directly leverages the diversity of reasoning representations. The analysis in Section 4.3 (Figure 4) backs this up with concrete evidence: MoT produces a larger gap in consistency scores between easy and hard questions, and the paper explains *why*—CoT and PoT tend to make different mistakes on hard questions, lowering consistency precisely where routing to the stronger LLM is needed. This gives mechanistic insight beyond "more samples help."

2. **Strong empirical support for the central efficiency claim.** The average plot across six datasets (Section 4.2) shows MoT variants achieving ~0.929 accuracy vs. GPT-4-CoT-SC's 0.931 at 40% relative cost. On CREPE, MoT even outperforms GPT-4-CoT-SC (0.885 vs. 0.871) at 47% cost. These results are concrete, reproducible in principle, and directly support the paper's main claim. The robustness evaluation (Section 4.4, Figure 6) further shows MoT-1D-Vote consistently outperforms CoT-2D-Vote across different temperatures (0.4, 0.8) and sample sizes (20, 40).

3. **Training-free cascade consistently beats trained verifiers.** Section 4.5 (Figure 5) compares against fine-tuned RoBERTa and prompted-GPT-3.5 verifiers on GSM8k, DATE, and CREPE. The best verifier reaches 0.892 accuracy on GSM8k, while MoT cascades reach ~0.951—a compelling demonstration that consistency-based routing is more effective than supervised verifiers for reasoning tasks. This is a non-trivial result that strengthens the paper's contribution.

4. **Systematic exploration of sampling diversity sources.** The paper cleanly disentangles three sources of answer diversity (in-distribution sampling, different demonstrations, different thought representations) and evaluates all combinations (10 variants). This allows for clear attribution: 2D demonstrations add 1.4% absolute accuracy over 1D (CoT-2D-Vote vs. CoT-1D-Vote at equal cost), and MoT adds further gains. The experimental design enables principled conclusions rather than a black-box comparison.

---

## Weaknesses

### Major

1. **Sections 2 and 3 are near-duplicate descriptions of the same methods.** Section 2 presents the cascade pipeline, vote-based decision-making, and verification-based decision-making; Section 3 covers the same ground as "Voting Percentage Checking" and "Consistency Verifying over Different Prompting Results" with nearly identical formalism. Compare Eq.~1 (vote-based, p.~3) with Eq.~2 (voting percentage, p.~5)—they are the same equation with different notation. This duplication is confusing and gives the impression the paper was assembled from separate drafts. The authors should merge these into a single, coherent methods section.

2. **Section 4.5 ends with a truncated sentence.** The paragraph "Can our method generalize to factual-based tasks?" (line 227) reads: *"We also explored whether our method can be generalized to factual-based reasoning tasks in"* —the sentence cuts off with no continuation, results, or conclusion. This is an unambiguous editing error that signals incomplete manuscript preparation. The authors must either provide the results or remove the paragraph entirely.

### Minor

3. **Routing rate (fraction of questions sent to the stronger LLM) is not reported.** The paper reports only the *relative cost* (total API spend vs. GPT-4-CoT-SC), but not the routing rate—i.e., what percentage of questions are actually deferred to GPT-4. Without this, readers cannot tell whether the 40% cost comes from correctly deferring only hard questions (the ideal case) or from accepting many wrong answers from the weaker LLM on easy questions (which would also lower cost but degrade accuracy). Reporting routing rates per dataset would make the cost-efficiency argument significantly more transparent.

4. **Threshold selection for vote-based methods is underspecified.** The vote-based curves sweep τ from 0.4 to 1.0, and the paper reports the point at 40% cost. It is not stated whether τ was tuned on a held-out validation set or selected post-hoc from test-set curves. If the latter, the reported accuracy at a given cost may be optimistically biased. **However, this is mitigated** by the verification-based methods (MoT-1D/2D-Verify), which require no threshold tuning and achieve the same headline result (~40% cost, matching GPT-4 accuracy). The authors should clarify the selection procedure and, ideally, present results at a fixed threshold common to all vote-based methods.

### Trivial

5. **Reproducibility statement is incomplete.** Line 263 cuts off mid-sentence: *"All of our implementations (including the complete prompt scripts, the code for training external verifiers, the code for approach evaluation, etc."* — this clearly intended to continue. The authors should complete this statement and specify where code/prompts will be released.

---

## Nice-to-Haves

- Reporting the routing rate per dataset (the fraction of questions sent to GPT-4) would strengthen the cost-efficiency analysis.
- The cost of the decision-making process (C^d in Eq.~1) is mentioned but never quantified. A brief note confirming it is negligible (simple arithmetic) would be helpful.
- Showing the second set of demonstrations (for "2D" approaches) in an appendix would improve reproducibility, though the current description ("randomly sample and manually annotate") is arguably sufficient.

---

## Removed Points

These points were raised by reviewers but are removed after verification:

- **"Missing statistical significance / variance reporting"** (Harsh Critic): Single-run API evaluation is standard practice in this line of work, and the paper's robustness section already varies temperature and sample size. This is not a meaningful gap given the paper's experimental scope.
- **"Comparison unfair favoring weaker baselines"**: The harsh critic did not raise this concern. The strength finder did not either. Not applicable.
- **"Cost of decision-making (C^d) should be quantified"**: The paper mentions it but never argues it affects conclusions. The critic agrees it is negligible; this is a nice-to-have, not a weakness.
- **"Prompt details for 2D demonstrations not shown"**: The paper states they randomly sample and manually annotate additional examples. This is sufficient for reproducibility; showing the full prompts would be helpful but is not a missing piece.

---

## Novel Insights

The harsh critic's observation that the verification-based methods are the paper's strongest evidence—because they are threshold-free yet achieve the same headline result—is genuinely insightful and not foregrounded in the paper itself. The authors currently give equal billing to the vote-based variants (six approaches) and verification methods (four approaches), but the case would be sharper if the verification methods were positioned as the primary contribution. The structural argument that MoT's advantage stems from CoT and PoT making *different* mistakes on hard questions (Figure 4, bottom panel) is well-made by the paper, but the threshold robustness angle is a useful synthesis from the review.

---

## Suggestions

1. **Merge Sections 2 and 3** into one unified methods section. Keep the clearer formalism from Section 2 (vote-based and verification-based) and drop the redundant "Voting Percentage Checking" / "Consistency Verifying" nomenclature from Section 3.
2. **Complete or remove** the truncated factual-task paragraph in Section 4.5. If the results are preliminary, state that explicitly; if omitted, do not tease them.
3. **Report routing rates** (fraction of questions deferred) for each method at the 40% cost point. This is easy to compute from existing data and would substantially strengthen the transparency of the cost-efficiency claim.
4. **Clarify threshold selection:** state whether the vote-based curves use a validation set for threshold tuning or whether they are post-hoc test-set curves. If the latter, explicitly note that the verification results are the primary evidence.
5. **Complete the reproducibility statement** on line 263 and specify the release plan for code and prompts.

---

## Score and Decision

**Score: 6.0 — Accept (Poster)**

**Decision: Accept**

**Calibration:**

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Stability-Aware Post-Training Cascade of Experts (NWK6) | 1.50 | 1 | Much weaker; withdrawn paper with major methodological issues |
| Framework of Thoughts (UZlJ) | 3.00 | 1 | Weaker; lacked novelty beyond engineering, rejected |
| Interactive LLM Cascade (fIFY) | 4.00 | 1 | Weaker; failed to differentiate from RAG, rejected |
| Mixture of Thoughts: Learning to Aggregate (x9tSy) | 4.00 | 1 | Weaker; marginal gains with high overhead, rejected |
| Cascadia (wkrW) | 5.50 | 2 | Similar tier; systems paper with strong engineering but less conceptual novelty. My paper has a more novel algorithmic contribution but worse presentation (redundant sections, truncated sentence) |
| Routing, Cascades, and User Choice (VqAh) | 5.50 | 2 | Similar tier; theoretical framing but narrower empirical scope |
| Universal Model Routing (ka82) | 6.50 | 2 | Slightly stronger; broader scope (dynamic pools, 30+ LLMs), theoretical bounds, but my paper has cleaner experiments and more focused evaluation |

**Round 1 bracket:** 5.0–7.0. The paper is clearly above the 1.5–4.0 range (those papers had major scientific or novelty flaws), and below the 8+ range (papers with polished theoretical contributions or broader impact).

**Narrowing (Round 2):** The paper compares favorably to Cascadia (5.5) and Routing/Cascades/User Choice (5.5) in conceptual novelty and empirical thoroughness, but its presentation issues (redundant sections, truncated sentence) bring it below Universal Model Routing (6.5). Final score of **6.0** reflects a solid, well-supported contribution with fixable presentation flaws.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>