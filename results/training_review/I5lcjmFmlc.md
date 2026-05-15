Now I have a complete understanding of the paper and all reviewer claims. Let me construct the consolidated review.

---

## Summary

This paper proposes Robust Diffusion Classifier (RDC), a generative classifier built from a single pre-trained diffusion model. RDC computes class probabilities via Bayes' theorem using conditional likelihoods approximated by the diffusion model's variational lower bound, after Likelihood Maximization (LM) pre-optimization that moves inputs to high-likelihood regions. A multi-head diffusion backbone is introduced to reduce computational cost. The method achieves 75.67% robust accuracy under $\ell_\infty$ ($\epsilon=8/255$) on a 512-image CIFAR-10 subset, surpassing prior defenses, and exhibits strong generalization to unseen threat models like StAdv.

## Strengths

- **Principled conversion of a diffusion model into a generative classifier.** Theorem 1 derives $p_\theta(y|\mathbf{x})$ directly from the diffusion loss via Bayes' theorem, without requiring a separate discriminative network. This is a conceptually clean departure from prior diffusion-based defenses that only purify or augment data.

- **Theoretical analysis establishing an upper bound on robustness.** The optimal diffusion classifier (Corollary 1) provably achieves 100% robust accuracy under standard threat models on its training set, providing a theoretical ceiling and justifying the generative-classifier direction.

- **Likelihood Maximization pre-processing substantially closes the empirical gap.** LM improves robust accuracy from 35.94% (un-optimized Diffusion Classifier) to 75.67% (RDC) under $\ell_\infty$, effectively addressing the gap between the empirical and optimal models. The ablation studying the budget $\eta$ (Fig. 1b) provides clear guidance.

- **Thorough adaptive attack evaluation.** The paper tests BPDA, exact gradient (for $N=1$), Lagrange attacks, and gradient randomness analysis (cosine similarity $\sim$98.48%), convincingly ruling out obfuscated gradients as the source of robustness.

- **Compelling generalization to unseen threat models.** Under StAdv attacks, RDC achieves 89.45% robust accuracy, exceeding all baselines by more than 53.90 percentage points, demonstrating that the method is not overfitted to a specific perturbation type.

## Weaknesses

### Fatal

None.

### Major

1. **The headline robustness claims are not verified on the full CIFAR-10 test set.** The evaluation uses a 512-image subset (line 247). The paper asserts that "robust accuracy of most baselines does not change much on our selected subset" (line 262) without providing comparative data. Since AT-EDM's published results on RobustBench use the full 10,000-image test set, the claimed +4.77% improvement over AT-EDM rests on an unverified assumption that the subset is representative. Even though 512-image subsets are precedented in this subfield (DiffPure), the SOTA claim demands stronger evidence.

2. **The multi-head diffusion backbone is not validated against the alternative it replaces.** The paper modifies the last convolutional layer of a pre-trained UNet to predict noises for all $K$ classes simultaneously (line 231), reducing NFEs from $K\times T$ to $T$. However, no comparison is reported between the classification accuracy/robustness of the multi-head model and that of the original single-head model evaluated with $K$ separate forward passes. Without this, it is unclear whether the multi-head modification introduces any accuracy degradation or whether the results can be fully attributed to the original pre-trained model.

3. **The link between unconditional Likelihood Maximization and improved conditional classification is asserted, not demonstrated.** The paper minimizes the unconditional diffusion loss (Eq. 6) to "increase the likelihood $p(\mathbf{x})$" (line 183) and argues this will also increase $p(\mathbf{x}|y)$ (line 188). However, no analysis is provided showing that LM actually reduces the gap $d(\mathbf{x},y,\theta)$ for the true class, or that the unconditional loss correlates with conditional classification accuracy. The ablation shows *that* LM works (Table 1) but not *why*, leaving the mechanism somewhat opaque.

### Minor

1. **Computational cost is never quantified.** The paper frames efficiency improvements (multi-head, systematic sampling) as a contribution, but does not report runtime per image (in seconds or GPU-hours) for RDC or any baseline. Without this, the practical significance of the robustness numbers is hard to assess. While efficiency is not the paper's primary contribution, the lack of any runtime data is a gap.

2. **The claim that DiffPure's poor robustness is "largely due to the vulnerability of downstream classifiers" (line 17) is stated without controlled experiments.** The authors reduce DiffPure's robust accuracy using stronger attacks, but do not isolate whether the cause is the downstream classifier, the purification process, or their interaction. This weakens the motivating narrative.

3. **The exact-gradient attack is only feasible for $N=1$ Likelihood Maximization steps (line 322).** For the default configuration ($N=5$), only BPDA and Lagrange attacks are used. While BPDA and exact gradient agree closely for $N=1$, the paper does not test an attack that differentiates through the full $N=5$ LM optimization (e.g., gradient checkpointing), leaving a residual gap in the adaptive attack evaluation.

4. **Ablation studies use only 100 images (line 352).** While this is common for computationally expensive ablations, the small sample size raises questions about statistical reliability, especially for the timestep ablation (Fig. 1c) which directly informs a practical trade-off.

### Trivial

None.

## Nice-to-Haves

- A comparison of the multi-head diffusion model's accuracy/robustness against an ensemble of per-class forward passes using the original single-head model.
- Runtime/GPU-hour comparisons between RDC, AT-EDM, and DiffPure on the same hardware.
- Per-image gradient variance plots (alongside the averaged cosine similarity in Fig. 1a) to confirm low variance is consistent, not an artifact of averaging.
- Application to a higher-resolution or multi-class dataset (e.g., Tiny ImageNet) to demonstrate scalability of the multi-head approach.

## Removed Points

*These points were flagged for removal per the review guidelines. They are recorded here for traceability but should not be weighted in the assessment.*

- **Asymmetric attack strength inflates RDC's relative performance (from Point 1):** The critic claimed attacks against DiffPure are strengthened while RDC is evaluated with BPDA, creating asymmetry that inflates RDC's performance. However, the stronger attack (PGD-200+EOT) is applied to the baseline (DiffPure), not to RDC, so the asymmetry favors the baseline, not RDC. **Removed per rule: asymmetry favoring baselines is acceptable.**

- **Multi-head modification contradicts "pre-trained" claim (from Point 3):** The critic claimed modifying the last layer contradicts the claim that RDC is "constructed from a pre-trained diffusion model." Modifying a single output layer of a pre-trained backbone does not contradict this claim, and "does not require training on particular adversarial attacks" remains accurate since no adversarial training is involved. **Removed as a strawman weakness.**

- **$\eta=8/255$ being the same as the attack budget is "suspiciously coincidental" (from Likelihood Maximization notes):** The paper's ablation (Fig. 1b) shows $\eta=8/255$ is optimal. Using the same budget as the attack perturbation to undo it is intuitive, not suspicious. **Removed as a strawman.**

- **Training details for multi-head diffusion omitted (from Point 3):** The paper references \cref{sec:training_details} for more details. This section was stripped by the PDF parser; it exists in the original submission. **Removed per rule about parser-stripped appendix content.**

- **SBGC uses more principled likelihood estimation (from Related Work note):** Subjective and debatable; the ELBO is a standard, well-motivated approximation directly tied to the diffusion training objective. **Removed as a nitpick.**

- **100% robust accuracy proof depends on unstated class-separation assumption (from Sec. 3.2.1 note):** The paper reports 100% robust accuracy as an *empirical* finding about the optimal model on the specific dataset (evaluated by AutoAttack), not as a claim that holds for any dataset. The critic's concern is speculative. **Removed as speculation not grounded in the paper's claims.**

- Several generic strengths from Strength Finder were filtered: strengths that were generic, superficial, or conflicted with verified weaknesses. **Removed per filtering guidelines.**

## Novel Insights

The most novel insight from the cross-review is the observation that the paper's theoretical contribution (optimal classifier achieving 100% robustness) and its empirical gap (35.94% for the un-optimized DC) are both presented honestly and the LM pre-processing is positioned as a practical bridge, but the paper never quantifies *how much* of the theoretical gap LM actually closes. Showing that minimizing unconditional diffusion loss improves conditional classification is empirically validated but mechanistically unexplained — does LM smooth the input, move it toward the true class's likelihood region, or both? The ablation on $\eta$ hints that the optimal budget exactly matches the attack perturbation, suggesting LM essentially reverses the adversarial perturbation, but this is not explicitly analyzed. This gap between the elegant theory and the heuristic practice is the paper's central tension that future work could resolve.

## Suggestions

1. **Validate on a larger evaluation set.** Report robust accuracy on at least 1,000–2,000 images (or the full 10,000 if feasible) and compare directly to published RobustBench numbers for AT-EDM on the same subset. If computational cost is prohibitive, provide statistical evidence (e.g., bootstrap confidence intervals across multiple 512-image subsets) that the subset is representative.

2. **Add a controlled experiment comparing multi-head vs. ensemble forward passes.** Report clean accuracy, robust accuracy, and runtime for both variants on the same 512-image subset to validate that the multi-head modification does not degrade performance.

3. **Provide mechanistic analysis of Likelihood Maximization.** Show per-class diffusion loss before/after LM on correctly classified vs. misclassified examples, and quantify the change in the gap $d(\mathbf{x},y,\theta)$ for the true class. This would strengthen the motivation for the approach.

4. **Report runtime.** Include average seconds per image on the same GPU for RDC, DC, LM-only, AT-EDM, and DiffPure, so readers can assess the practical trade-off between robustness and compute.

## Score and Decision

The paper tackles an important problem with a conceptually interesting approach and provides a generally thorough evaluation. However, the major weaknesses — particularly the unverified 512-image subset for SOTA claims and the unvalidated multi-head backbone — prevent the paper's headline claims from being fully substantiated in its current form. The core ideas are promising and the adaptive attack evaluation is commendable, but the evidence is not yet compelling enough for acceptance without significant revision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>