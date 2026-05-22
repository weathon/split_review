Now I have strong calibration. Let me write the final review.

---

## Summary

This paper identifies and formalizes the "squeezing effect" in LLM unlearning: when gradient ascent (GA) or NPO suppresses a target response, the softmax normalization redistributes probability mass into semantically related high-likelihood regions (rephrasings), producing only spurious unlearning. To counter this, the authors propose a bootstrapping (BS) framework that incorporates the model's own high-confidence predictions — its "beliefs" — as additional forgetting targets. BS-T (token-level) mixes the one-hot target with the top-k token distribution as a soft target; BS-S (sequence-level) samples entire high-confidence generations from the model and augments them as additional unlearning data. Experiments on TOFU, WMDP, and MUSE across multiple model scales show consistent improvements over strong baselines, and a LaaJ evaluation confirms reductions in spurious unlearning.

## Strengths

1. **Novel identification and mechanistic characterization of the squeezing effect.** Figure 2 provides compelling evidence for the phenomenon: (a) beam-search samples from high-likelihood regions remain semantically close to the original target even after unlearning; (b–c) probability dynamics show that GA and NPO consistently redirect mass into these neighborhoods. This goes beyond speculation by quantifying the effect and directly linking it to spurious unlearning. This is a genuine, actionable insight — understanding this mechanism points toward a specific remedy rather than merely observing that forgetting is imperfect.

2. **Elegant and well-motivated algorithmic response.** The bootstrapping framework (BS-T and BS-S) is a clean, principled answer to the diagnosed problem: if probability mass escapes into the model's own high-confidence predictions, directly incorporate those predictions as forgetting targets. The token- and sequence-level instantiations are natural, and the framework's compatibility with existing losses (GA, NPO, GradDiff) is a practical strength.

3. **Consistent empirical improvement across multiple benchmarks and model scales.** On TOFU (Table 1), BS-S achieves the best aggregate score in 8 of 9 settings across 1B/3B/8B models at 1%/5%/10% forget rates. On WMDP (Table 2), BS-S reaches near-random QA accuracy on Bio (0.26) while achieving competitive MMLU retention. The consistency across architectures and benchmarks strengthens the case that the benefit is robust.

4. **LaaJ evaluation demonstrating reduced spurious unlearning.** Figure 4c shows that BS-T and BS-S achieve higher similarity and naturalness scores than baselines on TOFU 10%, providing evidence that the metric improvements in Tables 1–2 correspond to genuinely more thorough forgetting, not just better scores on the same imperfect proxies.

## Weaknesses

### Major

1. **Limited LLM-based evaluation scope.** The paper convincingly argues (Sec. 3.1) that classical metrics (ROUGE, Truth Ratio, etc.) can misreport unlearning success. Yet the LLM-as-a-judge (LaaJ) evaluation that would address this is reported for only one setting (TOFU 10%, one LLM judge). WMDP, MUSE, and the 5%/1% TOFU settings lack this verification. Given the paper's own critique of metric reliability, the LaaJ evaluation needed to span a broader set of conditions to fully bridge this gap.

2. **Missing variance estimates.** No confidence intervals, standard deviations, or significance tests are reported for any of the main results. The improvements over NPO/RMU are often 0.01–0.04 on aggregate scores (e.g., Table 1: BS-S Agg. 0.61 vs. NPO 0.58 on 1B 10%; 0.64 vs. 0.63 on 8B 10%). Without variance information, it is difficult for the reader to assess whether these differences represent robust improvement or fall within the noise of the evaluation.

3. **Theoretical analysis adds limited insight beyond the loss construction.** Theorem 5.2 expresses the BS-T residual as the GA residual plus an extra term involving the top-k distribution. This is a direct algebraic consequence of the BS-T loss definition and does not derive any property (e.g., a bound on semantic similarity, a guarantee that probability mass does not reappear in rephrasings) that would independently substantiate the claim of "more thorough forgetting." The theory is correct but thin — it formalizes what is evident from the construction rather than proving a non-trivial consequence of it.

### Minor

1. **Hyperparameter sensitivity is deferred to the appendix.** BS-T introduces λ_BST and k; BS-S adds λ_BSS, N, temperature, and the choice of underlying loss. Given that these parameters control the trade-off between forgetting the target and suppressing the belief neighborhood, a main-text analysis of at least the key parameters would help establish robustness.

2. **The off-policy vs. on-policy distinction for BS-S is mentioned but not empirically compared.** The paper notes that on-policy BS-S (periodically resampling during training) could be used but is out of scope for the theoretical analysis. Since the empirical results likely use the off-policy variant, explicitly stating this and providing a comparison would be helpful.

### Trivial

None.

## Nice-to-Haves

- Extending the LaaJ evaluation to the WMDP and MUSE benchmarks, and to additional TOFU settings, would substantiate the claim that BS methods reduce spurious unlearning more broadly.
- Reporting individual components of the aggregate Memorization score (Extraction Strength, Exact Memorization, Paraphrased Probability, Truth Ratio) would help readers see where improvement comes from.
- A brief discussion of the computational cost of BS-S (which requires sampling N sequences per forget prompt) in the main text would aid practitioners in assessing the trade-off.

## Removed Points

These points were raised by reviewers but are excluded from the main review for the reasons given:

- **"Improvements over strong baselines are small (0.01–0.03)."** The actual improvements range from 0.01 to 0.07 (e.g., +0.07 on 8B 5%). The margins are modest but consistent, and this is common in the LLM unlearning literature. The point is merged into "Missing variance estimates" above rather than treated as a separate weakness. Many accepted papers in this space (e.g., OFMU, 5.50 Poster) show similar margins.

- **"The paper should have included a self-distillation baseline."** The paper's method is self-distillation-like by design (it is explicitly compared to self-distillation in Sec. 4.2). A separate baseline would be a nice-to-have but is not required to validate the core contribution. The comparison to NPO, RMU, GradDiff, SimNPO, and WGA already covers the relevant baselines.

- **"The connection to Yarowsky (1995) is superficial."** The paper uses "bootstrapping" in a reasonable analogical sense. This is a stylistic observation, not a substantive weakness.

- **"No comparison of computational cost in the main text."** The paper defers this to the appendix. Acceptable for a conference paper where space is limited, but acknowledged as a nice-to-have above.

- **"No comparison to a self-distillation baseline."** The BS framework is explicitly connected to self-distillation in the paper, and the key novelty is using the model's own predictions for *erasure* rather than reinforcement. The existing baselines cover the relevant comparison space.

## Novel Insights

The connection between the squeezing effect and the softmax normalization constraint is individually well-known from the fine-tuning literature (Ren & Sutherland, 2025), but this paper is the first to systematically demonstrate that this mechanism is the primary driver of spurious unlearning in GA/NPO-based methods, and to show empirically that probability mass concentrates specifically in the model's *own* high-confidence semantic neighborhoods rather than being distributed uniformly. The insight that model beliefs — which are both the destination of squeezed probability mass and the natural target for additional forgetting — can be harnessed as auxiliary unlearning signals is genuinely novel and practically useful.

## Suggestions

1. Add error bars (over multiple seeds or bootstrapped over test instances) to Tables 1 and 2, or report significance tests.
2. Extend the LaaJ evaluation to at least one additional setting (e.g., WMDP or TOFU 5%) to broaden the evidence that metric improvements reflect genuine forgetting.
3. Include a main-text sensitivity figure for the key hyperparameters (λ_BST and N) to demonstrate robustness.
4. Explicitly state in the experimental setup which BS variant (off-policy or on-policy) is used for the main results.

## Calibration Report

**Round 1 bracket:** 5.0–6.5, based on comparison with anchors found for LLM unlearning papers.

**Round 2 anchors consulted:**
- *OFMU* (5.50, Accept Poster, scores 6,6,6,4) — bi-level optimization for unlearning; similar improvement margins and evaluation scope. Our paper has a stronger problem diagnosis but comparable empirical validation. → Our paper is slightly stronger.
- *Label Smoothing Improves GA* (4.50, Reject, scores 4,4,6,4) — similar structure (identify GA failure → propose fix → evaluate on TOFU/MUSE/WMDP). Our paper has a more novel finding and broader evaluation. → Our paper is clearly stronger.
- *Stable Forgetting* (4.67, Reject, scores 6,4,4) — theoretical analysis of gradient instability + bounded LoRA fix. Stronger theory but weaker empirical finding. → Our paper is stronger.
- *Memorize to Forget* (5.50, Reject, scores 4,4,8,6) — model extrapolation as alternative to GA. Very mixed reviews; insufficient novelty concern. → Our paper is stronger.
- *KnowledgeSmith* (6.67, Poster, scores 4,8,8) — a benchmark/analysis framework rather than a new unlearning method. Different scope; not directly comparable.

**Final score:** 5.5. The paper has a genuinely novel and well-supported finding (the squeezing effect) and a principled algorithmic response with consistent empirical support. However, the limited scope of the LLM-based evaluation, missing variance estimates, and thin theoretical analysis prevent it from reaching the top of the scoring range. The paper is comparable to OFMU (5.50, Poster) and clearly stronger than the 4.5-level papers.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>