Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the consolidated review.

## Summary

The paper proposes Text2Data, a diffusion-based framework for text-to-data generation under low-resource conditions. The method operates in two stages: (1) pretraining an unconditional diffusion model on abundant unlabeled data to capture the overall data distribution, and (2) finetuning on scarce text-labeled data using a lexicographic constraint-optimization objective (Eq. 4, Algorithm 1) that regularizes parameters to stay near the pretrained space, thereby mitigating catastrophic forgetting while learning controllability. Experiments across three modalities (molecules, human motions, time series) at varying label proportions (2 %–40 %) show improvements over base diffusion models and their unconstrained finetuned variants.

## Strengths

- **Addresses a genuinely underexplored problem.** Low-resource text-to-data generation for modalities like molecules, motions, and time series is practically important and relatively neglected compared to image/text/audio domains where large labeled datasets exist. The paper identifies this gap and proposes a targeted solution.

- **Multi-modal evaluation across three diverse domains.** The paper evaluates on molecules (QM9, 6 properties), human motions (HumanML3D, 14 K motions), and time series (stock data, 210 K series), each at 8 different label proportions. This breadth, while uneven in treatment, provides evidence that the method generalizes beyond a single data type.

- **Consistent improvements over the compared baselines.** Text2Data outperforms the base model (EDM/MDM/DiffTS) and the unconstrained finetune ablation across most settings. For example, on motion generation (Table 1), Text2Data surpasses MDM and MDM-finetune in R Precision with average margins of 5.57 % and 2.31 %, respectively. On time series (Table 2), it achieves consistently lower MAE on frequency, skewness, and mean across all label proportions.

- **Clean problem formulation and method description.** The two-stage pipeline (distribution mastery via unconditional diffusion → controllable finetuning with constraint) is clearly motivated from the observation that p_θ(x) ≈ ∫ p_θ(x|c) p(c) dc, and the constraint optimization is technically well-specified in Algorithm 1.

## Weaknesses

### Major

- **Missing comparisons against established low-resource learning and anti-forgetting techniques.** The paper discusses data augmentation, semi-supervised learning with pseudo-labels, and transfer learning (including catastrophic forgetting) in its introduction and related work, dismissing each with reasoned arguments. Yet none of these approaches are included as experimental baselines. Concretely, the paper should compare against at least one representative from each class — e.g., (a) data augmentation on the labeled set, (b) pseudo-labeling on unlabeled data (a standard semi-supervised approach), and (c) explicit anti-forcing methods such as elastic weight consolidation (EWC) or L2 regularization toward the pretrained parameters. Without these, the claim of "superior performance over existing approaches" (line 23) is not adequately supported — the experiments only show superiority over the base model and an unconstrained finetune, which is the weakest possible comparison for testing the constraint's value. The two compared baselines (base model, unconstrained finetune) are necessary ablations but insufficient to establish the method's advantage over the broader landscape of low-resource learning strategies.

- **The theoretical analysis (Theorem 1) rests on an unrealistic assumption and offers no practical guidance.** The theorem assumes the parameter space Θ is *finite* (line 142), which does not hold for neural networks with continuous parameters. The paper's attempt to handwave this (lines 156–157: "log|Θ| is not significantly larger than N_p... even though it is usually much larger than N") does not resolve the issue — a continuous space is not just "large" but uncountably infinite, and the bound's derivation via union bound over a finite set does not apply. Moreover, the bound is a generic uniform-convergence statement that does not depend on the diffusion objective, the specific form of the constraint, or the two-stage training procedure. It offers no insight into why the constraint mitigates catastrophic forgetting and provides no guidance for hyperparameter selection (e.g., how to set ρ). The paper's claim of having "theoretically validated" the approach (line 22) is overstated.

- **Hyperparameter values (α, β, γ, ρ, ω) are not reported for any experiment.** The method's behavior depends critically on these values — especially ρ, which controls constraint relaxation — yet none are specified in the paper. This omission undermines reproducibility and prevents readers from assessing the sensitivity of results to these choices. No ablation or sensitivity analysis is provided for these parameters either.

### Minor

- **The "text" framing conflates genuinely different settings.** For molecules and time series, the "textual descriptions" are template-generated from numerical property values (e.g., "very low polarizability," "frequency = 2.59×10⁻¹"). This is synthetic structured conditioning, not natural language. Only the motion domain uses genuine human-annotated text. The paper treats all three as "text-to-data generation," but the molecule and time-series tasks are essentially property-conditioned generation with a text-based interface. The claimed generality to "low-resource language understanding" is not tested — the method may simply be learning property-conditioning better, not language understanding. These settings should be clearly separated and discussed.

- **The method underperforms unconstrained finetune at the lowest label proportions (2 %, 4 % on motion).** Table 1 shows MDM-finetune outperforming Text2Data on both R Precision and Multimodal Distance at 2 % and 4 % labels. The paper acknowledges this (line 289: "owing to milder catastrophic forgetting during finetuning with a smaller sample size") but does not investigate further. This anomaly is significant — it suggests the constraint can hurt when the labeled set is very small, which is precisely the setting the method targets. A diagnostic experiment (e.g., varying ρ at low proportions) is needed to understand this failure mode.

- **Classifier accuracy for molecular property evaluation is not discussed.** The paper trains classifiers to extract molecular properties from generated molecules and computes MAE against intended properties (line 231). If these classifiers are themselves trained on the same limited labeled data, their predictions may be unreliable, and the reported MAEs could reflect classifier error rather than true property mismatch. No information about classifier training data size, accuracy, or validation is provided.

- **The time-series baseline (DiffTS) is a custom-designed model, not an established benchmark.** There is no comparison against any published text-to-time-series method. Combined with the synthetic template-based "text" for this modality, the time-series experiments are less convincing than they could be.

### Trivial

- **The claim that Text2Data "can be seamlessly adapted to other generative models" (line 325) is speculative and undemonstrated.** Adapting the constraint optimization framework to GANs, for example, would require substantial re-engineering given the different loss structure.

## Nice-to-Haves

- A comparison against simpler regularization alternatives during finetuning (e.g., L2 weight decay toward pretrained parameters, a KL penalty on the unconditional score, or EWC) would directly isolate whether the lexicographic constraint formulation adds value beyond generic anti-forgetting.
- A study of how the relaxation parameter ρ affects performance, especially at low label proportions, could address the anomaly where the constraint hurts.
- Reporting the accuracy/validation error of the molecular property classifiers would strengthen confidence in the molecular controllability results.

## Removed Points

- **Criticism about novelty being "a minor variation of existing techniques"**: This is retained in weakened form under Major (the missing comparisons against alternatives is the real issue, not whether the technique is technically novel). The reviewer's characterization of the method as "standard pipeline with a well-known regularization technique" is a reasonable judgment call about contribution level, not a factual error, so it is kept as context for the missing baselines point rather than as a standalone claim.

- **"DiffTS is not an established baseline"**: Retained as a Minor point since the paper acknowledges designing DiffTS. The reviewer's stronger language about this being a fatal flaw is removed — the paper is upfront about DiffTS being custom-designed, and there is no single established text-to-time-series baseline in the literature.

- **The criticism that "the paper does not articulate why this particular constraint is better suited to diffusion models than simpler alternatives"**: Partially addressed by the existing missing-baselines point (Major weakness #1). The reviewer's standalone framing as a novelty criticism is merged into that point.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known tradeoffs in constrained fine-tuning (the constraint can hurt at very low label proportions) but do not reveal fundamentally new observations about the method or problem.

## Suggestions

1. Add comparisons against at least one representative from each class of low-resource learning strategy: data augmentation, semi-supervised pseudo-labeling, and explicit anti-forgetting (EWC or L2 regularization toward pretrained parameters). This is the most critical gap.
2. Report the values of all hyperparameters (α, β, γ, ρ, ω) used in experiments and include a sensitivity study for ρ, especially at low label proportions.
3. Clearly separate the three modalities in presentation — distinguish property-conditioned generation (molecules, time series) from true text-conditioned generation (motions) — and discuss what conclusions apply to each.
4. Either strengthen the theoretical analysis (e.g., relate the bound to forgetting, relax the finite-Θ assumption with Rademacher complexity or VC dimension) or acknowledge its limitations and reposition it as heuristic motivation.
5. Report the accuracy and training details of the molecular property classifiers.
6. Investigate why the constraint hurts at 2 %–4 % labels on motion and whether adaptive ρ scheduling could address this.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>