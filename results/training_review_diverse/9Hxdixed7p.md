Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper identifies three critical properties in DPO—**D**rastic drop in rejected likelihood, **D**egradation into response suppression, and **D**ispersion to unseen responses (the "3D-properties")—and argues these are inherent to DPO's gradient structure, explaining why DPO underperforms reward-model-based methods like PPO. The authors provide a theoretical gradient analysis at the probability level, validate the mechanism on a controlled toy model, conduct real LLM experiments (Baichuan2-13B/33B) on math and creative tasks, and propose Flex-DPO regularization to mitigate the identified issues.

## Strengths

1. **Novel theoretical derivation of the 3D-properties (Section 3.1, Corollaries 1–3).** The paper formulates a clean gradient analysis showing that as the rejected response likelihood π⁻ approaches zero, the gradient on the chosen response vanishes while the gradient on the rejected response diverges (under β<1). This provides a mechanistic, optimization-trajectory-level explanation for DPO's degradation into response suppression—going beyond prior endpoint-only analyses (e.g., Xu et al., 2024a) and purely empirical observations (e.g., Tang et al., 2024).

2. **Controlled toy model that cleanly isolates the predicted dynamics (Section 3.2, Figures 2–3).** The three-layer MLP with a discrete 4-prompt/10-response space directly visualizes the three properties: chosen likelihood rising then falling, rejected likelihood plummeting, and unseen likelihood increasing. The four on/off-policy scenarios (Figure 3) systematically show that on-policy initialization mitigates the effect, which is precisely what the theory predicts.

3. **Grounded theoretical comparison showing why RM training avoids 3D-properties (Section 3.4).** The paper derives that RM gradients (Equation 6) are balanced—the sigmoid symmetry ensures neither chosen nor rejected gradient dominates—and then confirms this empirically (Figure 5: RM accuracy steadily improves while DPO degrades after epoch 2). This provides a clean, principled explanation for a well-known but poorly understood performance gap.

4. **Practical regularization (Flex-DPO) grounded in the theoretical analysis (Section 3.3, Figure 4).** Rather than proposing an ad-hoc fix, the paper derives from Proposition 1 that moderating the rejected-likelihood decline rate is beneficial, then implements this via separate β⁺/β⁻. Figure 4 shows a clear trade-off: reducing β⁻ too much regresses toward SFT, while the right value improves poem generation. This is a principled, not heuristic, contribution.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical analysis operates at the probability level (π⁺, π⁻) but is not shown to translate to parameter-level updates in real LLMs.** The gradient derivation in Section 3.1 treats π⁺ and π⁻ as independent scalar parameters. In real LLMs, these probabilities are computed from a shared parameter vector through a softmax over the entire vocabulary. The gradient w.r.t. any parameter is a sum over all tokens in the response, and the ratio structure derived for probability-level gradients does not automatically carry over. The paper acknowledges this gap in Section 3.2.2 ("While the toy model differs from real LLM training…") but the bridge is qualitative, not formal. This means the paper's strongest claim—that 3D-properties are *inherent* to DPO's optimization—rests on an unverified analogy between probability-space and parameter-space dynamics. A rigorous argument (e.g., analyzing logit gradients before softmax) is needed to substantiate the claim.

2. **Real LLM experiments provide only indirect evidence for the 3D-properties in the actual training setting.** The experiments on Baichuan models (Section 4) show that on-policy DPO outperforms off-policy, that DPO is less stable than RM training, and that Flex-DPO improves results. These findings are *consistent with* the 3D-properties, but they do not directly confirm that the properties actually occur during real LLM training. The paper never tracks the log-likelihood of chosen/rejected/unseen responses over epochs in the real model—something it does for the toy model (Figure 2). Alternative explanations are plausible: the on-policy advantage could stem from dataset quality differences (GPT-4 selection vs. Qwen-7B generation), and the DPO instability could reflect overfitting to a finite preference dataset. Without direct likelihood measurements on the real LLM, the causal claim that 3D-properties drive the observed performance gaps is unsubstantiated.

3. **Evaluation methodology for poem and slogan tasks (Table 2, Section 4.5) is underspecified.** The paper lists metrics (Row Number, Words per Row, Rhythm, Tone Pattern, Title for poems; Word Count, Content for slogans) but never states who or what performs the evaluation. For MATH, the paper explicitly says "We evaluated the policy model using GPT-4" (Section 4.2). For poems/slogans, no equivalent statement exists. If these are automated checks, the rules should be specified; if GPT-4-based, potential biases need discussion; if human-rated, inter-annotator agreement should be reported. This gap makes the central DPO-vs-PPO comparison (Table 2) difficult to interpret or reproduce, and it also affects Figure 4's Flex-DPO tuning results.

### Minor

1. **No statistical significance or variance reported.** Tables 1, 2, and 9 present point estimates without error bars, standard deviations, or significance tests. Given the modest differences in some conditions (e.g., Scenario 1 vs Scenario 2 in Table 1: 72.93 vs 69.42), it is unclear whether these gaps are reliable. This is standard practice for empirical ML papers and would substantially improve interpretability.

2. **Limited model scope.** Experiments are conducted exclusively on the Baichuan2 family (13B and 33B). The 3D-properties are claimed to be fundamental to DPO's optimization, yet they are tested on only one architecture. Experiments on another family (e.g., Llama, Mistral, Qwen) would significantly strengthen the generality claim.

3. **Asymmetric comparison between DPO and RM training (Section 4.4, Figure 5).** DPO directly optimizes the policy, while the RM is a classifier trained on the same preference pairs. The claim that "RM avoids 3D-properties" is supported by the gradient analysis (balanced sigmoid gradients) and the RM accuracy curve, but the comparison is not apples-to-apples: the RM's evaluation metric (accuracy on preference classification) is naturally aligned with its training objective, while DPO's goal is policy optimization, not classification. A cleaner comparison would evaluate both on downstream task performance.

4. **The β<1 condition in Corollary 2 is stated but not discussed.** The paper's key gradient limits depend on β<1. While this holds for typical DPO implementations (β=0.1–0.5), the analysis would benefit from discussing what happens when β≥1 and why this regime is not relevant in practice.

### Trivial
None.

## Nice-to-Haves
- Direct measurement of likelihood trajectories (π⁺, π⁻, and unseen token probabilities) during real LLM DPO training would directly prove Properties 1 and 3 in the actual setting.
- A theoretical argument showing that the gradient ratio structure carries over to logit-level or parameter-level gradients (even approximately) would bridge the gap between the probability-level analysis and real LLMs.
- An ablation study isolating whether Flex-DPO outperforms a well-tuned vanilla DPO (with a single β) or is specifically better due to the asymmetry in β⁺/β⁻.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **"The condition β<1 is not discussed in the main text."** Incorrect. The paper explicitly states "given that β<1 and π⁻→0" in Corollary 2 (Section 3.1). The condition is stated, though not elaborated. Removed as factually wrong.
- **"No open release of checkpoints or data to allow independent verification."** Per policy, removing criticisms about large artifacts impractical to include in a submission. The paper states code is in supplementary material.
- **"Tension between abstract claiming DPO is resource-efficient and showing it's suboptimal."** Strawman criticism. The paper is clear: DPO is resource-efficient *but has limitations it aims to explain*. There is no unresolved tension.
- **"Toy model repeatedly samples same few data points, exaggerating gradient imbalance."** The paper explicitly designs the toy model to amplify effects for visualization (Section 3.2.2: "The toy model serves as an abstract simulation that amplifies the effect of 3D-properties"). This is a feature, not a bug.
- **"RM might also be overfitting" (re: Figure 5).** Speculative, unsupported by evidence in the review. The RM steadily improves on the eval set.
- **"The paper should have reproduced Observation 1 in its own setup."** Subsumed under Major weakness #2—the broader issue of direct measurement.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add direct likelihood tracking in real LLM training.** Monitor log-probabilities of chosen, rejected, and held-out responses over DPO training epochs on Baichuan2 models. This single experiment would directly validate Properties 1 and 3 and address the most significant evidential gap.
2. **Provide a logit-level or parameter-level gradient analysis.** Show that the gradient ratio structure (Corollary 1) at least approximately holds under softmax parameterization, or characterize the conditions under which it breaks down. This would bridge the gap between the elegant probability-level derivation and real-world optimization.
3. **Specify the poem/slogan evaluation protocol clearly.** Describe whether evaluations are rule-based (and if so, publish the rules), GPT-4-based (and discuss potential biases), or human-rated (report inter-annotator agreement).
4. **Add confidence intervals or standard deviations to all experimental results.** Even if computed from a small number of runs (e.g., 3 seeds), this would dramatically improve the reliability of the quantitative comparisons.
5. **Run at least one experiment on a different model family** (e.g., Llama-3-8B) to demonstrate generality of the 3D-properties beyond Baichuan.

## Score and Decision

**Overall assessment:** The paper identifies a genuine and important issue—DPO's gradient dynamics can lead to over-suppression of rejected responses, degrading performance. The theoretical derivation at the probability level is correct, the toy model cleanly illustrates the mechanism, and Flex-DPO is a principled mitigation. However, the paper has two significant gaps that prevent the central claim from being fully convincing: (1) the probability-level theory is not shown to translate to parameter-level updates in real LLMs, and (2) the real-LLM experiments provide only indirect evidence for the 3D-properties, relying on performance comparisons rather than direct likelihood measurements. The underspecified poem/slogan evaluation further weakens the key DPO-vs-PPO comparison. The contribution is real but the evidence falls short of proving the causal mechanism in practice. The paper is borderline and could become a strong contribution with the suggested revisions.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>