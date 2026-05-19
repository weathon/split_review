- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 6, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper studies how pre-training data imbalance (termed "parameter imbalance") affects downstream long-tailed learning, alongside the usual downstream "data imbalance." It provides empirical analysis showing that parameter imbalance persists after logit adjustment (which effectively handles data imbalance), and proposes a causal framework where different foundation models embody different "incomplete semantic factors" acting as confounders. The proposed method fine-tunes multiple foundation models (CLIP, OpenCLIP, MetaCLIP) with PEFT + Logit Adjustment and averages their predictions. Results on ImageNet-LT, Places365-LT, and iNaturalist2018 show improvements over single-model baselines.

## Strengths

- **Empirical separation of parameter imbalance from data imbalance (Section 4.1, Figs. 2–3):** The paper splits classes by both data imbalance (D-Many/Medium/Few) and parameter imbalance (P-Many/Medium/Few). Figure 3 shows that LA nearly eliminates the accuracy gap across D groups but leaves a large gap across P groups, and Figure 2 shows the worst performance at the intersection of D-Few and P-Few. This cleanly visualizes that pre-training imbalance has a distinct, persistent effect.

- **Demonstration that training-time logit adjustment fails for parameter imbalance (Table 3):** GLA-Train (extending GLA into the training loss) achieves only 38.53% overall accuracy — similar to LA (38.10%) and far below GLA (42.92%). This shows that including the parameter prior in the training loss does not correct parameter imbalance, supporting the claim that the bias is embedded differently from data imbalance.

- **Consistent gains across three datasets (Tables 5–7):** The method outperforms strong baselines (LIFT, VL-LTR, RAC) on Places365-LT (+2.91% over VL-LTR), ImageNet-LT (+3.49% on D-Few over LIFT), and iNaturalist2018 (+1.91% over RAC), with the largest gains on tail classes.

- **Ablation linking number of models to tail-class gains (Table 8):** Increasing M from 1 to 3 improves ImageNet-LT D-Few by +3.29%, with smaller gains on Many/Medium. This shows that fusing multiple models particularly benefits underrepresented classes.

- **Feature representation analysis (Table 4):** KNN accuracy shows re-balancing methods (LA, GLA-Train) barely improve D-Few representations (55.35% → 55.68% on ImageNet-LT) while D-Many accuracy drops. This supports the claim that logit-based re-balancing works through the classifier rather than fixing the encoder-level bias.

## Weaknesses

### Fatal
None. The empirical contributions — identifying the persistent effect of pre-training imbalance and showing that fusing multiple foundation models helps — are real and reproducible.

### Major

- **The causal framing is not experimentally separated from naive ensembling (Section 5.2).** The proposed method fine-tunes each foundation model independently with PEFT + LA and averages their predictions with equal weights. The paper frames this as a "backdoor adjustment" via "incomplete semantic factors" (C), but provides no experiment that distinguishes this from a simple ensemble. The causal graph assumptions (P(c)=1/M, that CLIP/OpenCLIP/MetaCLIP are valid instantiations of different C values, that the back-door criterion is satisfied) are stated without any validation or sensitivity analysis. The ablation (Table 8) shows monotonic improvement with more models, which is consistent with any ensemble method. Without evidence that the causal structure produces predictions distinct from naive ensembling, the causal language adds complexity without demonstrated justification.

- **Asymmetric comparison against single-model baselines (Tables 5–7).** Every baseline (LiVT, LPT, VL-LTR, RAC, LIFT, etc.) is based on a single foundation model, while the proposed method uses three. The paper never compares against a baseline that uses the same multi-model approach with a simpler aggregation (e.g., fine-tune CLIP/OpenCLIP/MetaCLIP each with the same PEFT+LA and average — which is what the method already does, so the missing baseline is any non-causal multi-model method). More critically, it doesn't compare against ensembling three copies of the same foundation model fine-tuned independently, which would control for whether the gains come from causal adjustment or simply from increased capacity/diversity. The comparison structure makes the method look more novel than it is.

### Minor

- **The claim that parameter imbalance "cannot be effectively addressed by current re-balancing techniques" (Abstract, Section 4.2) is overbroad.** The paper evaluates logit-based adjustments (LA, GLA, GLA-Train) and shows they fail for parameter imbalance. But other common re-balancing approaches — class-balanced sampling, re-weighting, post-hoc logit scaling on representations — are not tested. While the paper's evidence is suggestive and internally consistent, the sweeping conclusion goes beyond what the experiments cover.

- **The estimated prior (Eq. 3) is used to define P-Many/Medium/Few groups, but the paper does not analyze how robust its conclusions are to estimation error in this prior.** Since the entire "parameter imbalance" grouping inherits this noise (as the paper acknowledges: "Since the P_P(Y) is not accessible, we use the estimated prior"), a brief robustness analysis (e.g., varying the estimation parameters) would strengthen the empirical claims.

### Trivial
None that rise above parser artifact level.

## Nice-to-Haves

- Compare against an ensemble of the same model class (e.g., 3 independently fine-tuned CLIP models) to separate the effect of ensembling from the effect of diverse pre-training distributions.
- Test whether learned fusion weights (from a validation set) or median fusion outperform the assumed equal-weight averaging.
- Include a cost-effectiveness comparison against a single larger model (e.g., ViT-L) with more PEFT capacity.
- Provide a quantitative measure of semantic diversity across models' attention maps (beyond the anecdotal Grad-CAM examples in Fig. 4).

## Removed Points

These points from the inputs are removed with justification:

- **"GLA-Train is the authors' own extension, so the failure of this single variant does not rule out other re-balancing strategies" (Harsh Critic):** Retained in weakened form (Minor weakness 1). However, the critic's framing that the paper relies solely on GLA-Train is inaccurate — the paper also shows LA fails for parameter imbalance (Figure 3) and GLA succeeds post-hoc but can't be extended to training. The claim has more support than the critic acknowledges.

- **"The analysis relies on a specific PEFT method (Adaptformer) without testing sensitivity" (Harsh Critic):** Removed. The paper uses both Adaptformer and VPT (stated in Section 4.1: "we select two typical PEFT techniques, Adaptformer and VPT"). Testing every possible PEFT variant is scope creep.

- **"The Grad-CAM visualization is anecdotal; a quantitative measure would strengthen the argument" (Harsh Critic):** Moved to Nice-to-Haves. It's a valid suggestion but not a weakness — the visualization supports rather than undermines the claim.

- **"The paper does not compare GLA-Train against other methods like class-balanced sampling" (Harsh Critic):** Merged into Minor weakness 1 (overbroad claim about re-balancing). The critic's framing as a fatal omission is disproportionate.

- **"The introduction overstates novelty: GLA also recognizes this issue" (Harsh Critic):** Removed. The paper cites GLA (Zhu et al., 2024) and explicitly discusses how their work differs. The critic's claim that the paper says "previous methods overlook the inherent biases" ignores the nuance — the paper states they "overlook" it in the context of fine-tuning paradigms specifically, which is a defensible claim about emphasis.

- **"No analysis of whether improvement saturates or if backdoor adjustment differs from averaging" (Harsh Critic):** Moved to Nice-to-Haves. A valid experiment to add, not a flaw in what was done.

- **"No computational comparison to a single-model baseline with larger capacity or different PEFT design" (Harsh Critic):** Moved to Nice-to-Haves. This is outside the paper's stated scope.

- Generic strengths from Strength Finder about "addressing an important problem" or generic praise: Removed. Only concrete, specific strengths are retained.

## Novel Insights

The two reviews together surface a tension that is more nuanced than either presents alone. The harsh critic correctly identifies that the causal framing lacks empirical teeth — the method is, in practice, an equal-weight ensemble of independently fine-tuned models, and nothing in the experiments demonstrates that the causal graph constrains the design in a way that differs from naive ensembling. But the strength finder correctly identifies that the empirical analysis of parameter imbalance vs. data imbalance (Figures 2–3, Tables 3–4) is a legitimate contribution regardless of the causal framing. The paper's actual value may be in (a) documenting that pre-training distribution imbalance has a separable, persistent effect on downstream long-tailed learning that logit adjustment cannot fix, and (b) showing that fusing multiple foundation models is a practical workaround. The causal language is a framing choice, not a demonstrated mechanism. The most productive path forward would be to acknowledge that the method is an ensemble motivated by a causal intuition, and to position the contribution as an empirical finding about the persistence of pre-training imbalance and a practical multi-model solution, rather than a validated causal inference method.

## Suggestions

1. Add an ablation comparing the proposed equal-weight fusion against (a) an ensemble of 3 independently fine-tuned copies of the same model (e.g., 3× CLIP), and (b) against a simple baseline where you fine-tune each of CLIP/OpenCLIP/MetaCLIP independently and average logits — which is what the method already is. If (b) matches the proposed method exactly, then reframe the contribution accordingly: the causal story is an intuition/motivation, not a validated mechanism.

2. Narrow the claim about "re-balancing techniques cannot address parameter imbalance" to specify logit-based adjustments. Add experiments with at least one sampling-based re-balancing method (e.g., class-balanced sampling) to strengthen or qualify the claim.

3. Include a brief robustness analysis showing how the P-Many/Medium/Few grouping changes under different estimation procedures for the prior.

4. Consider evaluating learned fusion weights on a validation set as an alternative to equal weighting — this would either strengthen the causal framing (if equal weights are near-optimal, supporting the P(c)=1/M assumption) or reveal interaction effects.
