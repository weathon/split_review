- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper and can write the consolidated review.

---

## Summary

AdaSAP proposes a three-phase framework (adaptive perturbation warmup → pruning → uniform SAM finetuning) that connects sharpness-aware optimization with structured pruning to produce sparse networks robust to unseen corruptions. The core idea is to adapt per-neuron perturbation radii during warmup based on importance scores, so that unimportant neurons are forced into flatter minima before being pruned. Experiments on ImageNet classification (ResNet50) and Pascal VOC detection (SSD512) show consistent gains in both validation accuracy and robustness to corruptions over several pruning baselines.

## Strengths

- **Consistent robust accuracy gains across multiple compression levels.** Tables 1 and 2 show AdaSAP improving ImageNet-C accuracy over the strongest baseline at every size tier (e.g., 37.30 vs. 33.93 at 0.20×, 43.22 vs. 40.73 at 0.77×). The robustness ratio R_C at 0.77× size reaches 0.55, matching the dense model, while all other pruning methods remain lower. This directly supports the paper's central claim that AdaSAP reduces the disproportionate degradation of robust accuracy under sparsity.

- **Ablation evidence that the adaptive perturbation mechanism provides incremental value.** Table 5 (tab:ablation) compares AdaSAP$_P$ (adaptive perturbations + ASAM finetuning) against "SAM + ASAM" (uniform perturbations throughout) at comparable sparsity. Adaptive perturbations yield +0.7% validation accuracy and +0.64% ImageNet-C accuracy, isolating the benefit of the paper's key algorithmic novelty. The trend is consistent in the "without ASAM" comparison (AdaSAP$_P$ vs. Taylor+SAM: +0.76% val, +1.37% IN-C).

- **Generality to a second task.** Object detection results on Pascal VOC (Table tab:obj-det) show AdaSAP improving HALP by +2.1–2.5 mAP on clean images and +3.6–3.7 mAP on corrupted images, demonstrating the method transfers beyond classification.

- **Sharpness analysis provides mechanistic support for the approach.** Table tab:sharpness shows AdaSAP produces flatter minima both before and after pruning compared to Taylor pruning (e.g., sharpness 0.037 vs. 0.039 pre-pruning at 0.40× size), consistent with the paper's hypothesis that flatness mediates the observed robustness gains.

## Weaknesses

### Fatal
None.

### Major

- **The main comparison tables (Tables 1, 2, detection) lack a sharpness-aware baseline, making it impossible to fully attribute gains to the adaptive component.** AdaSAP applies SAM/ASAM optimization throughout all three phases, while the baselines (magnitude, Taylor, HALP) use standard SGD. The large margins in the main tables (e.g., +2–3% on IN-C) could therefore be substantially due to the known generalization benefits of SAM/ASAM rather than the novel *adaptive* perturbation design. The ablation (Table 5) provides a partial control but is only shown at one sparsity level (~20% size) and the "SAM + ASAM" row's pruning criterion is not explicitly stated, leaving ambiguity about whether the comparison is fully matched. A reader cannot tell whether the bulk of the gain comes from "adding SAM to any pruning pipeline" or from the adaptive radius mechanism itself.

- **Unsubstantiated claim of MobileNet V1/V2 coverage.** The contributions list (line 65) explicitly claims results covering "four networks (ResNet50 and MobileNet V1/V2 for classification, SSD512 for detection)." No MobileNet results or references to where they appear are present in the provided text. If these results exist in the appendix (stripped by the parser), the paper should at least mention them in the experiments section. As presented, this claim of broad architectural generality is unsubstantiated.

### Minor

- **The perturbation scoring function ψ is never specified concretely for any experiment.** The paper defines ψ as a function that computes importance for adaptive perturbation radii, and φ as the pruning criterion, noting they "may be the same or different." However, it never states what ψ actually is in the experiments — whether AdaSAP$_P$ uses ℓ₂ norm for ψ (same as φ), Taylor importance, or something else. This makes it impossible to reproduce the method precisely and leaves open the question of whether the benefit is simply from double-counting the same importance signal.

- **No variance or standard errors reported for any result.** Given that many reported improvements are small (e.g., 0.2–0.7% in the ablation, 0.23% for AdaSAP$_{P,\text{Taylor}}$ over Taylor+SGD), the absence of multiple seeds or confidence intervals makes it impossible to assess whether these differences are statistically significant. This is a reproducibility concern, especially for the sharpness analysis (Table 3), where the reported differences (0.037 vs. 0.039) are tiny and no variance is given.

- **Hyperparameters are not comprehensively reported.** The paper mentions "90 epochs" for finetuning in the ablation and provides total runtime, but does not specify: number of warmup epochs, pruning epochs, learning rate schedule, weight decay, batch size, optimizer settings, or prune frequency. These are essential for reproducibility.

### Trivial
- Algorithm 1's gradient approximation step states "$g_i \approx \nabla_{\mathbf{w}_i} L_{b, \mathbf{w}}(\mathbf{w}_i)|_{\mathbf{w}_i + \hat{\epsilon}_i}$" without clarifying that this requires a second forward-backward pass (standard for SAM but should be noted in the algorithm block for clarity).

## Nice-to-Haves
- A dedicated "adaptive vs. uniform" ablation under fully matched conditions: same pruning criterion, same sparsity target, same schedule, varying only whether perturbation radii are adaptive or uniform. Table 5 approximates this but the pruning criterion for "SAM + ASAM" needs clarification.
- Sensitivity analysis for the hyperparameters $\rho_{\min}$ and $\rho_{\max}$, which control perturbation radius range and likely affect the trade-off between pruning readiness and robustness.
- Including a method like Hydra or other robust pruning approaches in discussion, even though they use a different setting (adversarial training-time knowledge vs. unseen corruptions) — a brief positioning statement would strengthen the paper's novelty claim.
- Reporting the number of epochs for each phase (warmup, pruning, finetune) as concrete values.

## Removed Points
- **"Object detection numbers are suspicious because HALP at 0.40 and 0.20 have nearly identical mAP."** This is speculation without evidence. HALP optimizes for latency, not parameter count, so size reduction from 0.40 to 0.20 need not produce a linear change in accuracy. The AdaSAP values also cluster tightly at these two sparsities, consistent with this explanation. Without a demonstrated error, this concern is not verifiable from the paper.
- **"The SAM + ASAM row uses Taylor pruning, while AdaSAP_P uses magnitude pruning, so the comparison is confounded."** The paper does not state what pruning criterion "SAM + ASAM" uses; the critic infers Taylor from context, but this is an assumption. The real problem is that the paper fails to specify the criterion — this is captured in the Minor weakness about missing clarity in Table 5. The stronger claim of a definitively confounded comparison is not supported.
- **Various formatting/style nitpicks** (not present in original; parser artifacts).

## Novel Insights
A genuinely novel observation emerges from cross-referencing the reviews: when the paper switches from its default ℓ₂-norm-based scoring (for both ψ and φ) to Taylor importance as the pruning criterion (Table tab:adasap_taylor), the gains over the SGD baseline shrink dramatically (~0.23% on IN-C vs. ~1.8% for magnitude-based AdaSAP). This suggests the adaptive perturbation mechanism may derive much of its benefit from aligning ψ and φ — using the same ℓ₂-norm signal to both decide which neurons are "unimportant" and to regulate those same neurons into flat minima. If ψ and φ are different (ℓ₂-norm for perturbations, Taylor for pruning), the adaptive radii target different neurons than those actually removed, which could dilute the benefit. The paper does not discuss this alignment dependency, but the data pattern is suggestive and merits investigation. This observation is not present in either review individually — it emerges from combining the harsh critic's concern about ψ/φ specification with the actual numbers in Table tab:adasap_taylor.

## Suggestions

1. **Add a sharpness-aware baseline to the main tables.** Include a row for "magnitude + SAM + ASAM" (uniform perturbations throughout) at representative sparsity levels. This would let readers directly see the incremental value of the adaptive radius design over the full range of results, not just in one ablation.
2. **Specify ψ explicitly for every experiment.** State whether AdaSAP$_P$ uses ℓ₂ norm, Taylor, or another scoring function for the adaptive perturbation radii, and whether it is the same as or different from the pruning criterion φ. This is needed for both reproducibility and scientific interpretation.
3. **Clarify the "SAM + ASAM" ablation row:** state which pruning criterion is used (and ensure it matches AdaSAP$_P$'s criterion so the comparison isolates adaptive vs. uniform perturbations).
4. **Either show MobileNet results or remove that claim from the contributions.** If results exist in the appendix, add a sentence in Section 4 referencing them.
5. **Report variance** (at least 3 seeds) for key results, especially the ablation and sharpness comparisons where differences are small.
6. **Add a hyperparameter table** to the appendix with epochs per phase, learning rate schedule, weight decay, batch size, optimizer settings, and ρ_min/ρ_max values.
