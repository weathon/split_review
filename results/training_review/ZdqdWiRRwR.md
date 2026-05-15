Now I have a thorough understanding of the paper. Let me format the final consolidated review.

## Summary

The paper proposes Recursive Metadata Normalization (R-MDN), a layer that removes confounder effects from intermediate neural network features by performing statistical regression via the recursive least squares (RLS) algorithm. Unlike prior work (MDN), R-MDN operates at the level of individual examples rather than batch-level statistics, making it compatible with vision transformers and continual learning settings where confounder distributions shift across training stages. Experiments on synthetic data, ABCD neuroimaging (static), and HAM10000 dermatoscopic images (continual learning) demonstrate that R-MDN reduces correlation between learned features and confounders, improves fairness across demographic groups, and mitigates forgetting of confounder effects in continual learning.

## Strengths

- **Individual-example-level operation enables ViT compatibility**: The paper clearly identifies MDN's reliance on batch-level statistics as a fundamental limiter for modern architectures, and R-MDN's RLS-based approach genuinely removes this constraint. This claim is validated empirically in Section 4.2.2 where R-MDN is successfully integrated into a ViT for HAM10000 classification, while MDN cannot be (Section 3.2).

- **Effective confounder removal across continual learning stages**: On the synthetic continual learning dataset (Section 4.2.1), R-MDN consistently achieves accuracy near the theoretical maximum and the lowest squared distance correlation (dcor²) with the confounder across all stages (Figure 8c, Table 3). On HAM10000 with a ViT, all R-MDN variants achieve substantially lower dcor² than the base model and continual learning baselines (EWC, LwF, PackNet) — e.g., R-MDN(C) reaches 0.039 vs. 0.388 for the base model (Table 4).

- **Mitigation of catastrophic forgetting of confounder effects**: In the HAM10000 continual learning experiment (Table 4), R-MDN(C) achieves average test accuracy of 0.638, outperforming the base model (0.482), EWC (0.553), LwF (0.548), and PackNet (0.525). On the synthetic dataset, R-MDN demonstrates the best forward transfer distance (FWTd) across all three datasets, indicating that features learned with R-MDN transfer well to future stages even as confounder distributions shift.

- **Promotes equitable predictions across population groups**: In the ABCD sex classification task (Section 4.1.2, Table 2), R-MDN achieves the lowest mean difference between TPR and TNR (0.028) compared to all other methods, and low dcor² for both boys (0.110) and girls (0.122). Qualitative evidence (Figure 4) shows R-MDN avoids relying on the cerebellum — the region most confounded by pubertal stage — demonstrating genuinely confounder-free feature learning.

- **Robust generalization when confounder is absent**: In the synthetically controlled experiment (Figure 5), R-MDN maintains stable accuracy across the full range of confounder intensity (present to absent), while the base model, BR-Net, and P-MDN exhibit sharp performance drops when the confounder is removed — directly relevant to real-world distribution shifts.

## Weaknesses

### Fatal

None.

### Major

- **Missing MDN baseline in the ViT/continual learning experiment that most directly tests the paper's claimed advantage**: The paper argues that MDN's reliance on batch statistics makes it unsuitable for ViTs and continual learning. Yet the HAM10000 experiment (Section 4.2.2, Table 4) — the only experiment using a ViT in a continual learning setting — does not include MDN as a baseline. The paper asserts incompatibility without demonstrating it. Even if MDN cannot be naively inserted into a ViT's per-example computation path, a reasonable adaptation (e.g., recomputing Σ⁻¹ on each stage's training set and applying the transformation as a pre-processing step per stage) would provide a direct competitor and strengthen the claim. Without this comparison, the advantage of R-MDN over MDN in the ViT/continual learning setting is asserted rather than demonstrated. Given that static learning results (Table 1) show MDN and R-MDN perform similarly at batch size 128 (CIs overlap), this gap is significant.

- **Underspecified adaptation of baseline methods to the continual learning setup**: For the synthetic continual learning experiments (Section 4.2.1, Table 3), the paper does not explain how MDN, BR-Net, and P-MDN are adapted to the multi-stage training protocol. For MDN: is Σ⁻¹ recomputed per stage, or pre-computed across all stages? For P-MDN and BR-Net: are separate networks trained per stage, or is a single network fine-tuned sequentially? The fairness of the comparison depends on these details. This lack of specification undermines confidence in the reported metrics (Table 3) and makes the results difficult to reproduce or interpret.

### Minor

- **Missing ablation on inclusion of y in the regression**: The paper includes the label y in the regression (X = [x̃, y]) to "preserve the variance related to the labels" while removing confounder effects. An ablation that regresses only on the confounder x̃ (i.e., X = [x̃]) would validate this design choice and clarify whether including y materially affects the results.

- **Multiple comparisons not corrected**: The synthetic continual learning experiments report numerous metrics (Table 3: BWTd, FWTd across 3 datasets) without correction for multiplicity. While the trends appear consistent, this weakens the statistical claims.

- **No analysis of internal state evolution across stages**: In the continual learning setup, the internal state (R⁻¹, Q) accumulates all past data. The paper does not analyze how these values evolve, whether the method is sensitive to stage order, or whether stability guarantees hold when confounder distributions shift non-monotonically.

### Trivial

- The paper uses the notation $\tilde{\sigma}$ instead of $\tilde{x}$ in one residual equation ("$r=z-\tilde{\mathbf{\sigma}}\tilde{\beta_{x}}$"), indicating a minor transcription inconsistency.

## Nice-to-Haves

- A comparison with RegBN (Ghahremani Boozandani & Wachinger, 2024), a contemporary confounder removal method also cited by the paper, would broaden the empirical positioning. The paper cites RegBN in the introduction but does not compare against it.
- Per-stage dcor² trajectories for the HAM10000 experiment (rather than only after the final stage) would clarify whether R-MDN continuously removes confounder influence or only at the end.
- Extension to multiple confounders (more columns in X) would test a natural next step: real-world scenarios often involve multiple confounding variables.

## Removed Points

- **Criticism about missing test-time/inference procedure (Harsh Critic #1)**: The reviewer claims "the method as presented cannot be directly applied to standard evaluation protocols" and that "the paper never describes how R-MDN operates during evaluation." This is incorrect. The paper defines the residual as $r = z - \tilde{x}\tilde{\beta}_x$, where $z$ is the intermediate feature (always available during a forward pass), $\tilde{x}$ is the known confounder metadata (available at test time — the paper explicitly states confounders are "often available as auxiliary information or metadata"), and $\tilde{\beta}_x$ is learned during training and used as-is at test time. This is the same computation regardless of train/test; the only difference is that the RLS update is omitted at test time (standard practice for normalization layers). The method is fully specified and straightforward to apply at inference.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the method or problem that the paper itself does not already articulate.

## Suggestions

1. **Include an adapted MDN baseline in the ViT/continual learning experiment**: Even if MDN's batch-level approach cannot be naively integrated into ViT's per-example path, a per-stage MDN variant (recomputing Σ⁻¹ on each stage's training set and applying the learned transformation) would be a fair and informative baseline. This directly tests whether the paper's claimed advantage holds.

2. **Explicitly describe the continual learning adaptation for each baseline method** (MDN, BR-Net, P-MDN) in Section 4.2.1 — how are they configured for multi-stage training? Are they trained per-stage from scratch or fine-tuned sequentially?

3. **Add an ablation that regresses only on the confounder** (X = [x̃] instead of X = [x̃, y]) to validate the design choice of including y in the regression.

4. **Briefly clarify test-time behavior**: A single sentence stating that at inference, the learned $\tilde{\beta}_x$ is frozen and $r = z - \tilde{x}\tilde{\beta}_x$ is computed with the confounder $\tilde{x}$ from the test sample would preempt confusion, even though this behavior is already implied.

## Score and Decision

The paper proposes a technically sound and well-motivated method for confounder removal that genuinely addresses a limitation of prior work (MDN's batch-statistics requirement). The static learning experiments are convincing, and the continual learning results on HAM10000 with ViT are promising. However, the absence of MDN from the experiment most relevant to the paper's core claim (ViT + continual learning) and the underspecified baseline adaptations in the synthetic continual learning experiments are significant methodological gaps that prevent the paper from being fully convincing. These are addressable in revision. The core contribution is solid, and no fatal issues exist.

**Score: 6.5** — A solid paper with a clear contribution, weakened by two significant but addressable experimental gaps.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>