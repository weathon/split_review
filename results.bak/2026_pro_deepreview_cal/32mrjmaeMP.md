Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

This paper proposes TAK (Task Arithmetic with KFAC regularization), a dataless regularizer for task arithmetic that penalizes representation drift during fine-tuning. The key insight is reformulating the data-dependent drift penalty as a quadratic form of the Jacobian Gram matrix, which is an instance of the Generalized Gauss-Newton (GGN) matrix. By approximating this via Kronecker-Factored Approximate Curvature (KFAC), the regularizer becomes pre-computable and reusable without external data during fine-tuning. The authors further propose an aggregation heuristic that merges per-task KFAC factors into a single surrogate, achieving constant O(1) complexity in the number of tasks.

## Strengths

- **Elegant theoretical derivation connecting representation drift to curvature matrices** (Section 3.1-3.2): The paper shows that under linearization, the representation drift regularizer reduces to a quadratic form \(\tau^\top G_t(\theta_0) \tau\) where \(G_t\) is the Jacobian Gram — an instance of the GGN when the squared loss is used. This connection eliminates the data dependency and is clearly stated: "the matrix \(G_t(\theta_0)\) of the quadratic form in Eq. (3) corresponds to a curvature matrix: the GGN of the loss when the training criterion is the squared loss."

- **Effective KFAC approximation** (Section 3.3): Using KFAC to approximate the intractable Jacobian Gram reduces storage from O(P²) to per-layer Kronecker factors. The gains over a diagonal GGN baseline (Table 1) validate that capturing intra-layer correlations matters — e.g., ViT-B/32 normalized accuracy improves from 92.3% (Diag. GGN) to 97.6% (TAK) at α=1.

- **O(1) aggregation heuristic** (Section 3.4, Eq. 8): Merging per-task Kronecker factors into a single surrogate eliminates linear scaling in T. Table 3 demonstrates this is nearly lossless — on ViT-B/16 the accumulated form (88.3 abs.) actually slightly exceeds the naïve O(T) form (88.0 abs.).

- **State-of-the-art dataless performance** (Tables 1-2): TAK matches the data-dependent τJp baseline while being dataless — e.g., ViT-L/14 normalized accuracy 99.3% vs. τJp's 98.5%. For task negation, TAK achieves the lowest target accuracy (3.4-3.5%) while best preserving control-task performance, outperforming all baselines including data-dependent ones.

- **Robustness to α and task localization** (Figures 4a, 5): TAK maintains high accuracy across a broad range of scaling coefficients, eliminating the need for held-out validation tuning. The Jacobian-norm histograms (Fig. 5) provide compelling evidence that TAK forces task vectors to influence only their own task's inputs.

- **Thorough efficiency analysis** (Figures 6-8): KFAC pre-computation takes only ~4 minutes for 8 tasks with MC=1. Training overhead is modest (+12% memory in linear regime). The method works with as few as 32-128 examples, supports 87% KFAC storage compression with only ~1 point accuracy drop, and tolerates sparse penalty application (every 16 steps).

- **Cross-domain validation**: Results are demonstrated on both vision (CLIP, 8 tasks) and language (T5-base, 6 tasks), with consistent gains across both modalities.

## Weaknesses

### Fatal

None.

### Major

None. The core derivation is sound, and the empirical evidence robustly supports the central claims.

### Minor

- **Criterion specification in experiments**: The paper clearly states in Section 3.2 that the squared loss must be used for the GGN to equal the Jacobian Gram. However, the experimental section never explicitly reconfirms that squared loss (rather than the training criterion, e.g., cross-entropy) was used when computing KFAC factors. The MC variant with M=1 is standard for squared-loss KFAC, so this is almost certainly what was done, but a one-sentence confirmation in Section 4 would close the loop between theory and practice.

- **Hyperparameter β selection not discussed**: The paper introduces β as the overall regularization strength (Eq. 7) but does not describe how it was chosen (grid search, fixed constant, validation split). Given that robustness to hyperparameters is a selling point, a brief note on β tuning would strengthen reproducibility.

- **Merging heuristic lacks theoretical justification**: Equation (8) replaces a sum of Kronecker products with a product of sums, acknowledged as heuristic. Table 3 validates it empirically, but the paper would benefit from a brief remark on when this approximation is exact (e.g., if all \(B_t^l\) are identical) and when it might degrade. This is not a fatal gap given the strong empirical validation, but would sharpen the contribution.

### Trivial

- The term "dataless" is slightly overstated — the method requires pre-computing KFAC factors on task data (a one-time cost). The paper already clarifies this in Section 3.4, but the abstract and introduction could frame it more precisely (e.g., "data-free during fine-tuning" rather than "dataless").

- Figure 4's distinction between linearized fine-tuning (for TA curves) and non-linear fine-tuning (for TSV/ISO/TIES) could be made more explicit in the caption to avoid reader confusion.

## Nice-to-Haves

- A brief discussion of whether shared KFAC factors could leak information about training data would preempt privacy-sensitive readers' concerns, though this is outside the paper's stated scope.
- An ablation comparing KFAC factors computed under squared loss vs. the training criterion (e.g., cross-entropy) would empirically verify the theoretical motivation, though the strong results already provide indirect evidence.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "The description of KFAC computation retains the general formulation using the Hessian of the training criterion without explicitly stating that squared loss must be used"** → REMOVED as a fatal/major claim. The paper explicitly states in Section 3.2: "If we choose squared error... the GGN becomes the Jacobian Gram matrix exactly" and "Hence, the matrix \(G_t(\theta_0)\) corresponds to... the GGN of the loss when the training criterion is the squared loss." This is explicit. The general KFAC exposition that follows naturally simplifies under squared loss (\(\nabla^2 c_n = I_C\)). The criticism was demoted to Minor as a clarity point about experimental confirmation.

- **Harsh Critic: "Privacy implications of sharing KFAC factors"** → REMOVED. This is outside the paper's stated scope; the paper's contribution is about enabling dataless regularization, not about provable privacy guarantees.

- **Harsh Critic: "The term 'dataless' is slightly overstated"** → Demoted to Trivial. The paper acknowledges the pre-computation requirement in Section 3.4.

## Novel Insights

The paper's most insightful contribution is the clean bridge between representation drift regularization and curvature approximation — specifically, recognizing that the Jacobian Gram's quadratic form measuring interference is exactly the GGN under squared loss, which opens the door to the entire KFAC toolbox. This connection is both theoretically elegant and practically fruitful, as it transforms a data-access problem into a matrix-approximation problem. The O(1) aggregation trick (Eq. 8) is pragmatically clever: replacing a sum of Kronecker products with a product of sums is not mathematically justified in general, yet the paper demonstrates it works surprisingly well and provides a plausible intuition (exact when B factors are identical).

## Suggestions

- Add one sentence to the experimental setup confirming that KFAC factors were computed under the squared loss, explicitly closing the theory-practice loop.
- Briefly describe how β was selected (e.g., grid search over what range, or fixed to a constant).
- Add a sentence on when the merging heuristic (Eq. 8) is exact vs. approximate to help readers assess its limits.

## Score and Decision

**Originality:** High. The connection between representation drift and KFAC is novel and non-obvious. The O(1) aggregation trick is a creative practical contribution.

**Importance:** High. Enabling dataless weight disentanglement addresses a real bottleneck in decentralized and privacy-sensitive fine-tuning scenarios. The method makes task arithmetic more practical.

**Claims well supported:** Yes. The theoretical derivation is clear, and experiments comprehensively cover task addition, negation, localization, robustness, efficiency, and cross-domain transfer.

**Soundness of experiments:** Strong. Multiple model scales, both vision and language domains, extensive ablations (data efficiency, MC samples, compression, scheduling), and fair comparisons against data-dependent and dataless baselines.

**Clarity:** Generally good. The derivation flows logically, and figures are informative. Minor caption synchronization issues.

**Value to community:** High. The method is practical, efficient, and builds on well-established KFAC infrastructure. The paper also opens directions for applying curvature approximations to other modular fine-tuning paradigms.

Compared against calibration anchors: TAK is clearly stronger than τJp (6.00, which TAK matches while being dataless) and attention-only FT (6.25). It is somewhat stronger than partial linearization with LoRA (7.00) — TAK has a cleaner theoretical motivation and broader experimental validation. Compared to the second-order compositionality paper (7.50), TAK has a comparably deep theoretical framework, cleaner motivation, broader experiments (vision + language), and an additional practical O(1) aggregation contribution. I place TAK at 7.5.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>