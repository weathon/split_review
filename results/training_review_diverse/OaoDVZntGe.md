Now I have all the information needed. Let me compose the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
// leave empty

### Major
- weakness 1 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

## Summary

The paper introduces the Inverse Attention Agent, a multi-agent reinforcement learning approach that combines a self-attention architecture with an inverse attention network that infers the attentional states of other agents from their observations. The agent uses these inferred attention weights to update its own attention via a learned UW network, aiming to improve ad-hoc coordination with unseen teammates. The method is evaluated across five MPE environments against five baselines, with additional human experiments and population-scale ablations.

## Strengths

1. **Novel and well-motivated approach to ad-hoc coordination.** The paper shifts from traditional Bayesian ToM modeling to an end-to-end neural framework that explicitly models attention as a key mental state — a conceptually interesting departure from prior work. The three-phase training pipeline (self-attention → inverse network → integrated agent) is clearly described and implementable from the provided equations and algorithm.

2. **Large and consistent empirical gains across all environments.** Inverse-Att outperforms all five baselines (MAPPO, IPPO, MAA2C, ToM2C*, Self-Att) on every metric in Table 1, often by wide margins (e.g., Navigation: 497.96 vs. 328.24 for next-best Self-Att; Spread: 404.14 vs. 283.89). This consistency across cooperative, competitive, and mixed games provides strong evidence that the overall approach is effective.

3. **Robustness across population scales.** Tables 3–5 show that Inverse-Att maintains its advantage over Self-Att and MAPPO at scales 2, 3, and 4 agents in Spread, Adversary, and Grassland, demonstrating that the method generalizes beyond a single configuration.

4. **Human experiments provide supplementary validation.** Despite the small sample size (n=5), the human-agent results show Inverse-Att achieving the highest reward in 4 out of 5 roles (Table 2, e.g., Spread: 332.3 vs. Self-Att 272.0; Adversary Wolf: 286.9 vs. 197.4), offering behavioral evidence that the agent adapts to previously unseen human partners.

## Weaknesses

### Major

1. **The inverse attention network is only validated on data from the agent's own policy, yet it is applied to agents from different training methods in the ad-hoc evaluation.** The inverse network is trained exclusively on observation–attention-weight pairs collected from the Self-Att agent during Phase 1 (Section 5.2, Algorithm 1). In the ad-hoc evaluation (Section 6.2), Inverse-Att is paired with MAPPO, IPPO, MAA2C, and ToM2C* agents — whose behavioral patterns likely differ substantially from the Self-Att agent. Section 6.6 validates prediction accuracy only against the Self-Att agent's own ground-truth weights (Figure 3). The paper provides no evidence that the inverse network produces accurate attention predictions for agents trained with different algorithms. Since the entire mechanism — inferring others' attention and updating based on that inference — depends on this generalization, the paper's core causal claim is not fully supported. The performance gains could partly come from the UW network fine-tuning (Phase 3) or the initialization strategy rather than from meaningful inference. **A proper ablation (e.g., replacing inferred weights with random noise while keeping the UW network) is needed to isolate the contribution of the inverse inference.**

### Minor

1. **The gradient field representation is underspecified.** Section 3.2 devotes a full page to denoised score matching theory, but the paper never states how GFs are obtained for the specific tasks (data source for pre-training, whether learned jointly or separately, dimensionality of the `gf` vectors, etc.). The only usage description is in Section 6.1: "our application of the GF function atop raw observations, resulting in a gf representation structured as {gf_1,...,gf_N,gf_wall}." While the paper references prior GF work (wu2022targf, long2024socialgfs), the lack of detail makes this component of the method difficult to reproduce. The score-matching equation (Eq. 1) is never referenced again, and the section could be streamlined.

2. **Human experiments are underpowered and lack statistical testing.** Only five participants were recruited, each playing five episodes per condition. No statistical significance tests (e.g., t-tests, bootstrapped confidence intervals) are reported, and standard deviations are large relative to means. In Grassland (Wolf), Self-Att actually achieves a higher mean (197.9 vs. 185.7) with overlapping error bars — the paper acknowledges this exception but does not discuss what it implies about the method's robustness. Claims about "better emulating human behaviors" are also unsupported: only reward is reported, not behavioral similarity metrics (action overlap, trajectory distance, etc.).

3. **No ablation isolates the contribution of the inverse inference mechanism from the UW network and Phase 3 fine-tuning.** The paper shows that Self-Att alone is dramatically better than all non-attention baselines (Table 1), and Inverse-Att adds a smaller increment on top of Self-Att. Without an ablation that separates the effect of (a) the inverse network's predictions from (b) the additional capacity of the UW network + Phase 3 training, it is unclear how much of the improvement is attributable to attention inference specifically. The UW network is initialized to preserve Self-Att output (1 for self, 0 for others), then fine-tuned — this alone could produce improvements even with uninformative inferred weights.

4. **The self-attention mechanism is not fully specified.** Equation 2 (π_i(o_i) = h_i(W_i(f_i(o_i)), V_i(f_i(o_i)))) and Equation 3 (attention(f_i(o_{i,i}), f_i(o_{i,j}))) do not describe the specific attention formulation used (e.g., scaled dot-product, additive attention, how queries/keys/values are derived). While the paper cites Vaswani et al. (2017) and long2020evolutionary, the exact instantiation should be stated for reproducibility.

### Trivial

- The paper describes the training as "end-to-end" (Abstract, line 4), but the pipeline involves three distinct phases with separate training of the inverse network (Phase 2 via offline supervised learning), which stretches the usual meaning of end-to-end differentiable training.
- No statistical confidence intervals or significance tests are reported for any of the mix-and-match evaluations (Tables 1, 3–5). While standard deviations are reported, a reader cannot assess whether differences like Adversary Wolf (Self-Att 107.93 ± 2.26 vs. Inverse-Att 110.15 ± 3.74) are reliable.

## Nice-to-Haves

- A qualitative analysis of the inverse network's predictions on held-out agent types (e.g., visualizing predicted vs. behaviorally inferred attention for a MAPPO agent's observations).
- Reporting the number of random seeds used for each method, and whether the same seeds were used across methods for fair comparison.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism about the Bratman (1987) citation being "odd" for attention.** This is a citation appropriateness concern that cannot be verified without external sources, and even if the connection is tenuous, it does not affect the paper's technical contributions. *Moved to Removed Points as a citation nitpick.*

2. **Criticism that the inverse network and self-attention network have "the same functional form."** The paper explicitly states "Similar to the attention weight function" (line 129) — the similarity is by design, since the inverse network places itself in the other agent's perspective. The networks are trained differently (Eq. 4 uses supervised regression on D, while Eq. 2 is trained via MARL). *Moved to Removed Points as a misunderstanding of the design.*

3. **Criticism about "Self-Att already dramatically better" being a weakness.** This is an observation about the relative contribution of components, not a flaw. It is reframed in Minor #3 as a missing ablation concern, which is the substantive issue. *Moved to Removed Points as a mischaracterization.*

4. **Criticism about the "end-to-end" phrasing being misleading.** This is a minor phrasing issue, moved to Trivial. *Reference kept in Trivial section.*

## Novel Insights

None beyond the paper's own contributions. The key novel observation — that attention inference can be operationalized as a learnable inverse mapping from observations to attention weights and integrated into a MARL policy — is the paper's own contribution. The reviews do not surface a genuinely novel insight that the paper itself lacks.

## Suggestions

1. **Validate the inverse network on out-of-distribution agents.** Collect observations from agents trained with different methods (MAPPO, IPPO, etc.) and evaluate whether the predicted top-1 attention aligns with what a domain expert would expect (e.g., for a sheep being chased by a wolf, the inverse network should predict high attention on the wolf's GF). Even qualitative case studies would substantially strengthen the core claim.

2. **Add a proper ablation study.** Compare Inverse-Att against a variant where the inferred attention weights are replaced with noise (drawn from the same distribution) while keeping the UW network and Phase 3 fine-tuning. If Inverse-Att outperforms this noisy-UW variant, the inverse inference provides meaningful signal; if not, the benefit comes from the UW network or fine-tuning alone.

3. **Report statistical significance.** Add bootstrapped confidence intervals or pairwise t-tests for all comparisons, especially where standard deviations overlap (e.g., Adversary Wolf, Grassland Wolf in human experiments).

4. **Clarify GF details or cite a specific source where the reader can find the exact procedure.** Move the score-matching theory to an appendix and describe in the main text: (a) what offline data was used to train GFs, (b) the dimensionality of the gf vectors, and (c) whether GFs were frozen or fine-tuned during MARL training.

5. **Provide the exact self-attention formulation** (e.g., "we use scaled dot-product attention with query = key = value = f_i(o_{i,j}) after a linear projection").

## Score and Decision

The Inverse Attention Agent is a novel approach with strong empirical results, but the central mechanism — inferring attention of agents with different policies — is not validated. The paper needs to demonstrate that the inverse network actually produces meaningful predictions for the out-of-distribution agents it encounters in the ad-hoc evaluation. Without this validation, the reader cannot attribute the performance gains to the claimed mechanism rather than to the UW network's additional capacity or the Phase 3 fine-tuning. The remaining issues (GF underspecification, small human study, missing ablation) are less severe but add to the overall evidential gap.

The paper would become a strong contribution with targeted revisions; in its current form, the evidence for the core claim is incomplete.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>