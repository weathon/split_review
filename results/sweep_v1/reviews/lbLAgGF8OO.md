Now I have all the evidence I need. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper introduces Dig-DEC, a model-free decision-estimation coefficient that drives exploration purely through information gain (KL divergence plus an additional divergence term) rather than optimism. The authors apply Dig-DEC to both stochastic and hybrid MDPs, claiming improved regret rates in the stochastic setting and the first model-free regret bounds for hybrid MDPs with bandit feedback. The framework unifies prior AIR approaches and provides a concrete example (3-armed bandit) where Dig-DEC strictly outperforms optimistic DEC.

## Strengths
1. **Conceptual contribution of Dig-DEC with strict improvement guarantee**: The paper defines Dig-DEC in Eq. (8) and proves in Theorem 13 that it is always no larger than optimistic DEC plus an additive η. Theorem 14 provides a concrete 3-armed bandit where optimistic DEC suffers Ω(√T) regret while Dig-DEC achieves constant regret, demonstrating that the improvement can be arbitrarily large in specific settings. This is a genuinely novel complexity measure.

2. **General framework with flexible divergence design**: Algorithm 1 operates with a general divergence D (Eq. 2), and the analysis via Bregman divergences (Eqs. 5-6) recovers results of [XZ23] and [LWZ25] as special cases while enabling new posterior update rules. This flexibility is a genuine methodological contribution that could facilitate future work.

3. **Improved online function estimation**: The unbiased estimator for average estimation error (Theorem 7, Algorithm 4) using sample splitting replaces the biased estimator of [FGQ+23] and achieves Est ≲ N log|Φ| T^{1/2}. For squared error minimization in Bellman-complete MDPs, Theorem 11 bounds Est by a constant (log²|Φ|), enabling √T regret — this is the first time a DEC-based method matches optimism-based approaches in Bellman-complete MDPs (Table 1, last three rows).

4. **Honest discussion of limitations**: The paper explicitly acknowledges that Assumptions 3-4 do not cover all hybrid MDPs (e.g., low-rank MDPs with unknown reward features), and notes that computational cost of solving the minimax problem is not addressed.

## Weaknesses

### Major
1. **Mismatch between abstract's claimed regret rates and Table 1**: The abstract (line 19) claims "improving their regret bounds from T^{3/4} to T^{3/5} (on-policy) and from T^{5/6} to T^{7/8} (off-policy)" for average estimation error minimization. However, Table 1 reports T^{2/3} for both on-policy and off-policy bilinear classes with D̄_av (lines 268-271). The exponents T^{3/5} ≈ 0.6, T^{7/8} ≈ 0.875, and T^{2/3} ≈ 0.667 are all different. The paper provides no explanation for this discrepancy or any derivation of T^{3/5} or T^{7/8} in the main text. A reader cannot determine which rates are correct. This undermines the paper's advertised central contribution.

2. **Hybrid regret bounds in Table 2 are superlinear for most entries**: Table 2 (lines 297-301) reports regrets of T^{3/2} (on-policy bilinear with D̄_av), T^{13/8}=T^{1.625} (off-policy bilinear with D̄_av), and T^{3/2} (on-policy bilinear⋆ with D̄_sq). Only one entry (off-policy bilinear⋆ with completeness) achieves T^{1/2}. However, the paper claims (line 38) "the first sublinear regret for model-free learning in hybrid bilinear classes." If the reported T^{3/2} and T^{13/8} exponents are intentional, they are superlinear, contradicting the sublinear claim and making most of the hybrid results not meaningful as regret bounds. If they are typos, the paper's most important table is corrupted.

3. **Line 219 claims an "improvement" that is not an improvement**: The text states "our construction of the estimator improves their rate of Est from √T to T^{1/2}" — these are the same rate (√T = T^{1/2}). This is a factual error in the paper as written. (The surrounding context suggests this is likely a garbled claim where the original intended improvement was from something like T^{3/4} to T^{1/2}, but as submitted it is wrong.)

### Minor
4. **Introduction's comparative rate claims are garbled/unclear**: Line 39 states "improve the T^{3/2}/T^{5/8} regret of [FGQ+23] to T^{3/2}/T^{5/6} in the former case." If this is supposed to mean improvement from T^{5/8} (≈0.625) to T^{5/6} (≈0.833), this would be a regression, not an improvement. This is inconsistent with the abstract's claims and confusing as written. The notation T^{3/2}/T^{5/8} is never explained.

5. **The derivation linking the Est bound (T^{1/2}) to the final regret rates in Table 1 is not verifiable from the main text**: Theorem 7 gives Est ≲ N log|Φ| T^{1/2}, and Table 1 states dig-dec = H²dη for on-policy bilinear. A naive plug-in gives Reg ≈ T·H²dη + (log|Φ|T^{1/2})/η, which optimizes to T^{3/4} (not the T^{2/3} reported in Table 1). Since the optimization over η is claimed to produce T^{2/3}, a derivation sketch in the main text would be necessary for the reader to verify the claim. (The appendix containing the derivation is not available in the submission.)

6. **Theoretical comparison with [FGQ+23] lacks a sketch of Theorem 13**: Theorem 13 states dig-dec ≤ o-dec + η, which is central to the paper's claim that Dig-DEC recovers and can improve upon optimistic DEC. No proof sketch is provided in the main text to help the reader assess the plausibility of this key result.

### Trivial
7. The paper's dig-dec bound for the 3-armed bandit (Theorem 14) is not illustrated with a regret curve, which would ground the theoretical improvement.

## Nice-to-Haves
- A simple regret plot for the 3-armed bandit example (Theorem 14) would strengthen the paper's demonstration that Dig-DEC can be arbitrarily better.
- A brief sketch of how the Est bound (T^{1/2}) combines with the dig-dec bounds to produce the reported T-exponents in Table 1 would help readers verify the claims without needing the full appendix.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic's claim that "Est ~ √T and dig-dec ~ η gives regret ~ T^{2/3}, not T^{3/5"** — This criticism conflates two issues. The mismatch between abstract (T^{3/5}) and Table 1 (T^{2/3}) is a real verifiable inconsistency already covered in Weakness 1. The specific calculation about T^{3/4} vs T^{2/3} depends on details in the (removed) appendix and cannot be definitively verified from the main text alone. It is noted as a concern but not retained as a standalone weakness since the verifiable inconsistency (abstract vs Table 1) is sufficient.
- **"Missing experiments/derivations" and "deeper analysis" suggestions** — These are nice-to-have requests, not weaknesses.
- **Strength Finder's generic strengths about "addressing an important problem"** — Removed as generic/superficial.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a novel observation about the paper that the paper itself does not already articulate.

## Suggestions
1. **Reconcile the abstract with Table 1**: Either correct the abstract to match the T^{2/3} rates in Table 1, or provide a separate derivation that yields T^{3/5} and T^{7/8} and explain how these relate to Table 1's entries. Every numeric claim in the abstract should be traceable to a result in the body.
2. **Fix the hybrid table**: The T^{3/2} and T^{13/8} entries in Table 2 are superlinear. If these are typos (intended to be T^{2/3} etc.), correct them. If they are correct, clarify that these are not sublinear and explain what form of "regret bound" is being claimed, as T^{3/2} is not a meaningful guarantee.
3. **Correct line 219**: "improves from √T to T^{1/2}" is a non-statement. Fix the rate to what was actually achieved.
4. **Clarify the introduction's comparative rates (line 39)**: The T^{3/2}/T^{5/8} → T^{3/2}/T^{5/6} notation is confusing and appears to claim a worse rate. Either correct the numbers or explain the notation.
5. **Add a derivation sketch**: Show how the Est bound (T^{1/2}) and dig-dec (O(η) or O(√η)) combine to produce the final T^{2/3} regret in Table 1 via optimal η selection.

## Score and Decision

**Calibration anchors** (retrieved from review corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/riQmzq5FaQ.md` | 3.75 | RL with Elastic Time Steps — limited contribution, rejected. The current paper has stronger theoretical ideas but more serious numerical inconsistencies. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mBJF0p9yRR.md` | 3.25 | Almost Sure Convergence of Avg Reward TD — technically sound but limited scope. Current paper's issues are more about reliability than scope. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/op19LjpHkH.md` | 5.75 | Decoupled Actor-Critic — interesting ideas but insufficient empirical justification, rejected. Current paper has stronger theoretical novelty but more severe presentation/numerical issues. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2h3m61LFWL.md` | 4.25 | Value-Biased MLE for Linear MDPs — reasonable theory but limited novelty. Current paper's theory is more innovative but has verifiable numerical inconsistencies. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aPNwsJgnZJ.md` | 6.00 | Horizon-free Adversarial RL — accepted, solid theory, near-optimal results. Current paper has more significant issues preventing acceptance. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/L8UNn7Llt4.md` | 7.50 | O-DICE — accepted, strong theory + experiments, well-supported claims. Current paper's claims are not as well-supported. |

The paper has a genuinely interesting core idea (Dig-DEC) and makes a real theoretical contribution. However, the verifiable inconsistencies between the abstract's claims (T^{3/5}, T^{7/8}) and Table 1 (T^{2/3}), the superlinear rates in Table 2 that contradict the "sublinear" claim, and the garbled "improvement from √T to T^{1/2}" statement mean the paper as submitted does not reliably support its own advertised results. The ideas are worth pursuing, but the paper needs substantial revision to be publication-ready.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>