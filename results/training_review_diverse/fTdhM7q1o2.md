Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes using the Bradley-Terry model with ties (BTT) for preference modeling in RLHF, arguing that standard binary-preference data collection forces labelers to break ties arbitrarily, which introduces systematic bias in measured preference strength. The authors provide a theoretical derivation of this bias (Theorem 2), propose a bias-correction algorithm (Algorithm 1) applicable to conventional datasets without ties, and construct synthetic tie-labeled datasets using LLMs to empirically demonstrate that training with BTT (TDPO) outperforms standard DPO.

## Strengths

1. **First to introduce BTT for RLHF preference modeling**. The paper identifies a genuinely underappreciated problem—standard BT preference modeling does not account for ties, which are common in human judgment—and applies the established BTT model (Rao, 1967) to this setting. This is a novel and well-motivated departure from the standard BT assumption.

2. **Theoretical derivation of bias from ignoring ties**. Theorems 1 and 2 (Section 4.2) analytically characterize the bias that arises when fitting a BT model to data generated under BTT. The bias is shown to be a sigmoid-shaped function bounded by log((1+θ²)/(2θ)), but practically significant within the range of preference strengths observed in real RLHF datasets. This formal result is a clear theoretical contribution independent of any empirical validation.

3. **Bias-correction algorithm that makes the theory actionable**. Algorithm 1 provides a practical method to correct the bias by solving a nonlinear equation derived from Theorem 2. The approach explicitly connects to ODPO and margin-based methods, offering a principled theoretical justification for why such offsets help—beyond what any ad-hoc constant offset could provide.

4. **Empirical validation on synthetic tie datasets**. The experiments in Section 5.3 show TDPO (training with BTT) achieving win rates significantly above 50% against DPO as the proportion of tied samples increases, with win rates reaching well above 50% when only tied samples are used (Figure 2). This pattern is consistent across different labeler/evaluator combinations (Llama and Qwen).

## Weaknesses

### Fatal

None. The theoretical contributions are sound and the empirical trends, while not rigorously quantified, point consistently in the same direction.

### Major

1. **No statistical rigor—all results are reported as single numbers without error bars, confidence intervals, or any measure of variability.** This applies to Table 1 (bias differences), Table 2 (test accuracy for θ selection), Table 3 (win rates), and Figure 1 (win-rate curves). In Table 2, the difference between θ=5 (0.6042) and θ=10 (0.5958) is small enough that it could fall within noise, especially given the small model (Pythia-160M) and single-epoch training. Without error bars, the reader cannot assess whether the reported advantages are meaningful or due to random variation. Since the paper's central empirical claims rest on these comparisons, this is a structural weakness that cuts across all experimental sections (5.1–5.3).

2. **The hyperparameter θ is selected based on test set accuracy, invalidating the test results.** The paper states (lines 252, 286): "Due to limited computing resources, we only conducted experiments for the optimal θ, i.e., 5, as indicated in Table 2" — where Table 2 reports *test* accuracy. This means the same data used to choose θ is used to report final accuracy, opening the door to overfitting to test-set noise. Subsequent experiments (Tables 3, Figure 1) then fix θ=5 based on this selection, propagating the issue. A proper evaluation would use a validation split for θ selection or report results across all θ values without cherry-picking the best test-set performer.

3. **No comparison to ODPO with a tuned constant offset, so the BTT-specific benefit is not isolated.** The paper acknowledges (lines 199, 238) that its method "can be viewed as a variant of ODPO" but only compares to vanilla DPO (θ=1, which is simply no offset at all). The claimed advantage could therefore be entirely due to introducing *any* positive offset, not to the specific functional form derived from the BTT model. Without a baseline with a tuned or learned constant offset, the paper cannot support its claim that the BTT-derived correction is the source of improvement—the novelty and justification of the bias-correction method would collapse if a constant offset performs equally well.

4. **Assumption 1 (random tie-breaking) is central but untested.** The entire bias derivation (Theorem 2) and Algorithm 1 rely on the assumption that when ties are forced into a binary choice, labelers pick uniformly at random. In practice, human labelers may exhibit systematic biases (e.g., preferring longer responses, or the first-listed response). The paper does not discuss this assumption's plausibility, test robustness via simulation under non-uniform tie-breaking, or explore alternative models. If the assumption fails, the correction term is misspecified.

### Minor

1. **Synthetic tie label quality is not analyzed.** The paper uses Llama3-70b and Qwen2-72b-instruct to label ties in HH-RLHF (Section 5.3), but provides no analysis of label quality—no inter-labeler agreement, no comparison to a human-annotated subset, no discussion of the striking discrepancy (847 tied samples for Llama vs. 3553 for Qwen). The entire experiment depends on these labels being reasonable, yet this is not validated.

2. **No discussion of computational overhead or numerical stability of Algorithm 1.** The bias-correction method involves solving a nonlinear equation at each optimization step, but the paper gives no details about how this is implemented in practice, its computational cost, or whether numerical stability is a concern. This is a practical gap for anyone wanting to reproduce or deploy the method.

3. **No practical guidance for setting θ.** The paper treats θ as a known parameter, but offers no guidance on how practitioners should set or estimate it when the true tie propensity is unknown, beyond running a range of values.

### Trivial

None.

## Nice-to-Haves

- The synthetic tie experiments use only Pythia-2.8B; a single additional experiment with a 7B or larger model (even on a data subset) would strengthen generalizability claims.
- A comparison or discussion of how the BTT model relates to the Plackett-Luce model for ties, given that PL is mentioned in related work.
- The paper could acknowledge prior uses of ties in preference learning contexts (e.g., dueling bandits) to contextualize the "first" claim more precisely.

## Removed Points

- *"The first-to-propose-BTT claim would be strengthened by acknowledging prior work on ties in dueling bandits"*: The paper is about RLHF, not dueling bandits. Citing Rao (1967) for BTT is sufficient. This is scope creep.
- *"No comparison to Plackett-Luce model"*: PL is for multiple comparisons, not pairwise ties. The paper correctly identifies PL as handling a different setting (multiple comparisons) in related work. Not a valid weakness against this paper.
- *"Only Pythia-2.8B, not representative of larger models"*: The paper acknowledges compute constraints, and single-model experiments at this scale are standard for academic submissions. Demanding 7B+ experiments is practically infeasible for the authors' stated resources.
- *"The paper should add X" wishlist items whose absence does not affect the believability of the core contribution*: These have been moved to Nice-to-Haves where appropriate.

## Novel Insights

The most interesting observation emerging across reviews is that the paper's theoretical contribution (characterizing the bias from ignoring ties) is arguably stronger and more durable than its empirical validation. The bias formula in Theorem 2 is clean, provably correct, and immediately useful—it shows that ignoring ties attenuates preference strength in a predictable sigmoid-shaped way, with a known maximum magnitude. This result stands regardless of experimental limitations. The weaker link is the empirical claim that the BTT-specific correction *form* (vs. any constant offset) is responsible for the gains, because the missing ODPO-baseline comparison makes it impossible to distinguish between the principled theory and a generic margin effect. A well-designed ablation could turn this paper from a suggestive empirical paper into a definitive one.

## Suggestions

1. **Add error bars to all experiments.** Re-run Tables 2–3 and Figure 1 with at least 3–5 random seeds and report means ± standard errors or bootstrap confidence intervals. This is the single highest-leverage fix.
2. **Hold out a validation split for θ selection.** Use the validation set to choose θ (or report results for all θ values in downstream tasks without cherry-picking), and report test-set results only once.
3. **Include an ODPO-with-constant-offset baseline.** Tune the offset value on a validation set and compare against the BTT-derived correction. If the BTT form still wins, the paper's specific contribution is supported.
4. **Run a robustness simulation for Assumption 1.** Generate synthetic data where ties are broken non-uniformly and measure how much the correction degrades. If it is robust, report that; if not, discuss the limitation honestly.
5. **Analyze synthetic tie label quality** by reporting inter-labeler agreement (Cohen's κ) between Llama and Qwen on a shared subset, and note the large discrepancy in tie counts.

## Score and Decision

The paper addresses an important and genuinely underappreciated problem with a clean theoretical derivation. The core idea is sound and well-motivated. However, the empirical validation has significant methodological gaps—no error bars, test-set-based hyperparameter selection, and a missing baseline that makes it impossible to attribute improvements to the BTT-specific correction rather than a generic offset. These are addressable but go beyond what can be fixed in a rebuttal. The paper would be substantially stronger after the recommended revisions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>