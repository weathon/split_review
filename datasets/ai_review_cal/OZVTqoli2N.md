- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6
Now I have a thorough understanding of the paper and all reviewer claims. Let me write the final consolidated review.

## Summary

This paper studies model compositionality in non-linear networks through a second-order Taylor expansion of the loss around pre-training weights. The theoretical framework yields a Jensen inequality relating the composed model's risk to individual models' risks, and an exact gap decomposition (Theorem 1). From this, the authors derive two incremental training algorithms — ITA (individual training with an EWC-like regularizer anchored at pre-training) and IEL (ensemble training with a pairwise alignment penalty) — and evaluate them on class-incremental benchmarks. Both algorithms achieve strong results, with ITA additionally supporting zero-shot specialization and unlearning via task-vector arithmetic.

## Strengths

- **Generalization of compositionality theory to non-linear networks (verified, lines 48–69)**. The paper derives a Jensen inequality (Eq. 4) for the second-order approximation of the loss, showing that the composed model's risk is bounded by a convex combination of individual risks. This is explicitly contrasted with Liu et al. (2023), whose inequality holds only for linearized models. The paper's formulation applies to any fine-tuning strategy (LoRA, IA3, full fine-tuning) and is not restricted to tangent-space training.

- **Theorem 1 provides an exact decomposition of the compositionality gap (verified, lines 107–114)**. The paper quantifies the gap \(\Omega(\cdot)\) between the composed model's second-order loss and the weighted average of individual losses, in terms of pairwise task-vector alignment under the Hessian-induced metric. This decomposition directly motivates the regularization terms used in both ITA and IEL.

- **Strong empirical results across multiple benchmarks (verified, lines 180–184)**. ITA and IEL outperform or match existing methods (EWC, LwF-MC, L2P, CODA-Prompt, SEED, TMC, APT, InfLoRA) on most of the 7 class-incremental datasets tested, including low-similarity domains (RESISC45, CropDisease) where the pre-training optimality assumption is most challenged. The paper uses the same backbone for all methods and reports hyperparameter tuning via grid search.

- **Honest and informative ablation study (verified, lines 186–195)**. The ablation in Table 2 separates the effect of regularizing all layers vs. only the classification head, and shows that PEFT methods (LoRA, IA3) are more robust than full fine-tuning when regularization is removed. Figure 1 directly visualizes how ITA's regularization tightens the Jensen upper bound, providing empirical support for the theoretical framing.

- **Demonstration of zero-shot specialization and unlearning for ITA (verified, lines 197–200)**. The paper shows that ITA supports task-vector addition/subtraction to specialize on subsets of tasks or unlearn specific tasks, with quantitative comparisons against TMC. This is a practically valuable capability that goes beyond standard multi-task composition.

## Weaknesses

### Fatal
None.

### Major

- **The core theoretical assumption (pre-training weights are a local minimum over all tasks) is not empirically verified, and the practical strategy to enforce it is only partial.** The paper assumes \(\theta_{\text{pre}}\) is a local minimum of \(\mathcal{L}_{\text{emp}}(\theta)\) across all tasks (line 55) to guarantee Hessian positive semidefiniteness. The practical enforcement via linear probing (line 157) only trains the classification head while keeping backbone weights fixed. This means the backbone's Hessian over the combined task distribution is never directly checked — the paper provides no empirical measurement (e.g., eigenvalue spectrum, gradient norm, or third-order remainder) to confirm the condition holds in any of the 7 experimental settings. The paper candidly discusses this limitation (Section 7) and tests low-similarity domains where the assumption is "challenged," which is commendable. Still, the theory is presented as the paper's central framework, and the gap between the strong condition required and the evidence provided is non-trivial. A reader cannot assess whether the method works *because* of the second-order structure or despite it.

### Minor

- **The gap between the second-order theory and the full loss used in practice is acknowledged but not directly bridged.** The paper explicitly states (line 161) that derivations use the quadratic approximation \(\bar{\ell}\) while algorithms optimize the full loss \(\ell\). This is a common pattern in theory-motivated ML, but the paper does not measure the third-order remainder \(\|\ell(\theta) - \bar{\ell}(\theta)\|\) along training trajectories to confirm the approximation is faithful. Figure 1 shows the regularization tightens the second-order bound, which provides partial empirical support, but a direct fidelity check would strengthen the connection.

- **IEL fails at the very editing operations (specialization/unlearning) that the introduction advertises as a contribution.** The paper honestly reports (line 200) that IEL "leads to a severe drop during specialization" and the dual-algorithm presentation is balanced. However, the abstract and introduction describe "the pool of incrementally learned modules" enabling unlearning and specialization without distinguishing which algorithm provides this capability. A reader could reasonably conclude both algorithms support editing. The paper's own data shows only ITA does.

- **ITA's regularization is structurally similar to EWC with a fixed anchor at pre-training (the paper acknowledges this, line 103).** While the theoretical framing is new and the fixed-anchor choice is principled, the algorithmic contribution of ITA is modest on its own. The paper already compares against standard EWC as a baseline (line 182). Adding a direct ablation comparing ITA against a variant using an L2 penalty toward pre-training (without Fisher weighting) would help disentangle whether the Fisher-weighted regularization or simply the distance-to-pre-training constraint drives the gains.

### Trivial

- None.

## Nice-to-Haves

- A more precise statement of when the O(1) complexity claim applies. The paper already qualifies it (line 163: "provided we are not interested in more complex forms of composition"), but this qualification could be moved earlier in the presentation (e.g., to the abstract or introduction) to avoid misleading readers.
- A direct comparison of specialization/unlearning results in the main paper rather than primarily in the supplementary. The main paper describes the setup but key numbers are deferred to \cref{tab:results_composition_suppl}.
- A per-task breakdown of editing results across all tasks (not just first, central, and last) would strengthen the claim about editing capabilities.

## Removed Points

These points were raised by reviewers but are removed or downweighted for the reasons noted:

- **"The theory applies to the second-order approximation but the algorithms optimize the full loss — the connection is not validated"** → Downgraded from a critical issue to a Minor weakness. The paper transparently acknowledges this gap (line 161), Figure 1 provides partial indirect validation, and this is standard practice in theory-motivated ML.
- **"The claimed constant complexity is misleading because editing requires storing all task vectors"** → Removed. The paper explicitly qualifies the claim (line 163), stating it applies only when not using complex composition forms needed for editing. The paper is not misleading; this is the reviewer misreading the qualification.
- **"Comparison with SEED is not entirely fair"** → Removed. The paper fairly notes SEED's trade-off (parameter-inefficient Mixture of Experts vs. weight averaging) and the comparison is standard for the field.
- **"Statistical significance not discussed"** → Removed. The paper reports averaging over 3 runs with standard deviation deferred to supplementary, which is standard practice for this type of benchmark.
- **"Closed-form gradient claim not verified"** → Removed. The paper references the supplementary for the derivation, which is standard.
- Generic strengths about "addressing an important problem" or "well-written" → Removed as they are generic and do not add concrete evidence.
- **"The novelty is modest and ITA is essentially EWC"** → Downgraded from a critical issue to a Minor weakness. The paper acknowledges the connection and the theoretical framing is new; the similarity to EWC is an observation, not an error.

## Novel Insights

The main novel insight emerging from synthesizing the reviews is that the paper's most compelling contribution may be empirical rather than theoretical. The combination of (a) the finding that PEFT methods (LoRA, IA3) exhibit intrinsic compositionality benefits over full fine-tuning even without regularization (Table 2), and (b) ITA's editing capabilities surviving domain shift, together suggest that "staying close to pre-training" is sufficient to produce composable modules — and the second-order framework is a reasonable way to justify this intuition, even if the strict assumptions are not perfectly satisfied. The paper's value may ultimately be in providing a principled vocabulary (pre-training basin, Hessian-induced metric, task-vector alignment) for a phenomenon that was previously understood only empirically.

## Suggestions

1. Add an empirical sanity check of the core assumption: measure the gradient norm or the smallest eigenvalue of the Hessian at \(\theta_{\text{pre}}\) (post-LP) on the combined task data for at least one benchmark. This would directly address the main theoretical concern.
2. Include an ablation that replaces the Fisher-weighted EWC term in ITA with a simple L2 penalty toward \(\theta_{\text{pre}}\) (or weight decay). This would isolate whether the Fisher weighting matters or if the benefit comes purely from staying close to pre-training.
3. Make the abstract and introduction more precise about which algorithm supports editing. A phrase like "ITA enables specialization and unlearning" rather than "the pool of incrementally learned modules enables..." would avoid potential confusion.
