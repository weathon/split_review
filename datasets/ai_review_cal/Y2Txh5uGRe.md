- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 3, 6
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

The paper proposes Text2Data, a two-stage diffusion framework for low-resource text-to-data generation. Stage 1 learns an unconditional data distribution from abundant unlabeled data via diffusion. Stage 2 finetunes the model on scarce text-labeled data using a novel constraint-optimization objective (lexicographic optimization) that regularizes the finetuned parameters to stay near the pretrained distribution, thereby mitigating catastrophic forgetting. The method is evaluated on three modalities: molecules (QM9), motions (HumanML3D), and time series (Yahoo Finance stock data).

## Strengths

1. **Constraint-optimization finetuning directly addresses catastrophic forgetting.** The learning objective (Eq. 4, Algorithm 1) explicitly enforces that finetuned parameters stay close to the pretrained distribution, and the ablation against unconstrained finetuning (MDM-finetune, DiffTS-finetune, EDM-finetune) provides direct evidence that the constraint helps. For example, in Table 1, Text2Data consistently achieves higher R Precision and lower Multimodal Distance than both MDM and MDM-finetune at proportions 8% and above on motion generation.

2. **Evaluated across three distinct low-resource modalities.** The framework is tested on molecules, human motions, and time series — domains with very different data structures (3D coordinates, sequential joint angles, 1D series) and different evaluation protocols. This multi-modal evaluation demonstrates generality, whereas prior work on low-resource text-to-data generation has focused on single domains.

3. **Generation quality is maintained or improved alongside controllability.** While the primary focus is controllability, the paper also reports improvements on quality metrics (e.g., 36.05% FID improvement over MDM on motions, and improvements in molecular validity, stability, and atom stability over EDM), showing that the constraint does not trade off quality for control.

4. **Two-stage design avoids label-ambiguity issues of semi-supervised learning.** Rather than inferring pseudo-labels for unlabeled data — which is problematic for nuanced text — Stage 1 only learns the marginal data distribution via unconditional diffusion, eliminating the semantic ambiguity that plagues semi-supervised approaches for text-to-data tasks.

## Weaknesses

### Fatal
None.

### Major

1. **Narrow scope of baselines for a paper claiming "comprehensive" comparison.** The experimental comparison includes: (a) the base diffusion model trained only on labeled data (EDM/MDM/DiffTS), and (b) the base model finetuned on labeled data without the constraint. While these ablations isolate the constraint's effect, the paper also discusses data augmentation, semi-supervised learning, and transfer learning as alternative strategies in the introduction (Section 1) and related work (Section 2.2) — yet provides **no experimental comparison** against any of these approaches. The baselines section (Sec. 5.2) mentions "directly applied to augmented text-data pairs" as a condition, but no results for this condition appear in any table or figure. Without comparisons against explicit data-augmentation baselines (e.g., simple noise injection on labeled samples) or alternative regularization schemes for preventing forgetting (e.g., elastic weight consolidation, synaptic intelligence), the paper cannot substantiate its claim of "superior performance baselines" over the broader landscape of low-resource methods.

2. **The theoretical analysis (Theorem 1) has a gap between assumptions and application.** The theorem assumes a **finite** hypothesis class $\Theta$ and derives confidence bounds using $\log|\Theta|$. The paper then interprets $|\Theta|$ as the number of neural network parameters (14 million). This is not theoretically valid — the bound holds for a finite set of hypotheses, not for a continuous parameter space. While the theorem provides useful intuition, it does not constitute a rigorous generalization guarantee for the neural-network instantiation, and the claim that it "theoretically validates" the constraint selection is overstated.

3. **The time-series experimental evidence is thin.** (a) The time series dataset is custom-assembled from Yahoo Finance with overlapping 120-day sliding windows, which creates correlated samples and lacks the standing of an established benchmark. (b) Many reported improvements in Table 2 are small and within one standard deviation of the baselines (e.g., Frequency at 2%: 2.59±0.20 vs 2.62±0.20; Mean at 2%: 0.63±0.39 vs 0.63±0.39). No statistical significance tests are reported. (c) The t-SNE visualization (Figure 3) is qualitative only. The time-series results are the weakest link in the empirical story and do not convincingly demonstrate a decisive advantage.

### Minor

4. **Text2Data underperforms unconstrained finetuning at very low label proportions (2–4%) for motion generation.** In Table 1, at 2% and 4% labeled data, MDM-finetune achieves higher R Precision than Text2Data (0.37 vs 0.34 at 2%; 0.42 vs 0.39 at 4%). The paper's explanation ("milder catastrophic forgetting during finetuning with a smaller sample size") suggests the constraint is too restrictive in the extreme low-resource regime the paper specifically targets. This limitation needs more honest discussion and analysis rather than a brief hand-waving attribution.

5. **No ablation or sensitivity analysis for the constraint relaxation hyperparameter $\rho$.** The paper introduces $\rho$ (line 156) to relax the constraint $\hat{\xi} = \rho \cdot \inf \hat{\mathcal{L}}_1$, noting the constraint "may be overly strict." Since the constraint is the core novelty, the sensitivity of results to $\rho$ should be analyzed — e.g., what happens when $\rho$ is too small (constraint too strict, underfits labeled data) vs. too large (constraint vacuous, catastrophic forgetting). Its absence weakens the empirical validation of the mechanism.

6. **Missing comparison against explicit continual-learning baselines.** Since the paper's core argument is that the constraint mitigates catastrophic forgetting, a natural comparison is against standard continual-learning/regularization methods (e.g., EWC, SI, MAS) applied to the same two-stage pipeline. This would isolate whether the specific form of the constraint (on the unconditional diffusion loss) provides benefits over generic parameter regularization.

### Trivial

7. The paper claims the method "can be seamlessly adapted to other generative models such as generative adversarial networks" (Conclusion) without any evidence or discussion of how. This is unsupported speculation.

## Nice-to-Haves
- Reporting computational cost (training time, memory) for the two-stage pipeline compared to baselines.
- Statistical significance tests (paired bootstrap or permutation tests) for the main metric comparisons across all three modalities.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Hyperparameter values for $\alpha,\beta,\gamma,\rho$ not reported** — These are likely in the appendix (stripped by the parser). Per policy, do not penalize for missing appendix content.
- **Proof not provided (assumed in appendix)** — Removed per policy about missing appendix content.
- **"Method for converting numerical properties to text is not described"** — Likely detailed in the appendix. Removed per policy.
- **t-SNE is "subjective and unrepeatable"** — t-SNE visualization is standard evaluation practice for generative models; this is a generic criticism applicable to most papers using it.
- **"The paper compares only against ablations of the same method"** — This is factually inaccurate in its strong form: EDM and MDM are published, peer-reviewed methods, not the authors' own ablations. The valid core (missing comparison against other low-resource strategies) is retained as Weakness #1 above.
- **"No analysis of computational cost"** — This is a nice-to-have, not a core weakness.
- **"Parser artifact (missing axis scales)"** — Removed per policy on parser artifacts.
- **The claim about $\log|\Theta|$ being "not significantly larger than $N_p$"** — The critic's numerical analysis (log(14M) ≈ 16.8) actually supports the paper's numerical claim that the bound value is small; the valid issue is the finite-$\Theta$ assumption (retained in Weakness #2).

## Novel Insights

The harsh critic surfaces an insightful structural tension: the constraint in Eq. (5) bounds the unconditional loss on the *labeled subset* using an infimum computed on the *full dataset*. If the labeled subset distribution differs from the full distribution — which is likely under non-random sampling in low-resource settings — the bound could be either vacuous or impossible to satisfy. The paper introduces $\rho$ to handle this but provides no analysis of its effect. This is a genuinely subtle issue that the paper's framing glosses over. The Strength Finder correctly identifies the multi-modal evaluation as a genuine differentiator from prior single-domain work, and the ablation against unconstrained finetuning is the right experimental design to isolate the contribution. The two sources of insight together suggest the paper's core idea is sound but its validation is incomplete — particularly the missing link between the theoretical framing and the algorithmic heuristic, and the absence of explicit comparison against generic forgetting-prevention methods.

## Suggestions
1. Add explicit data-augmentation baselines (e.g., simple noise injection on labeled samples) and at least one continual-learning baseline (e.g., EWC regularization over the unconditional diffusion loss) to the experiments.
2. Provide an ablation study on the relaxation coefficient $\rho$ showing how varying it affects the controllability vs. forgetting trade-off.
3. For the time-series experiments, either replace the custom stock dataset with an established low-resource benchmark (e.g., ECG classification with few text annotations) or report statistical significance tests for the current comparisons and clarify the overlapping-window issue.
4. Acknowledge and analyze the regime (very low label proportions, 2–4% on motions) where the constraint is harmful, and discuss when the method is and is not appropriate.
5. Either tighten the theory by connecting it to neural-network-specific bounds (e.g., PAC-Bayes) or reframe it as heuristic motivation rather than a formal guarantee.
