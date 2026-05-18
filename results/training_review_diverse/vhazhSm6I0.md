Here is my consolidated review:

---

## Summary

This paper proposes a two-step test-time adaptation (TTA) method for graph neural networks. The first step (BNSA) adapts BN layer statistics (μ, σ²) by computing a data-driven weighting factor via Jensen-Shannon divergence between training and test activation distributions, combined with a learnable binary mask that selects which BN dimensions to update. The second step (BNPA) refines the BN scale/shift parameters (γ, β) using an energy-based model with entropy-filtered and confidence-weighted pseudo-labels. The method is evaluated on seven datasets with three GNN backbones (GCN, GraphSAGE, GAT) and compared against seven baselines.

## Strengths

1. **Principled two-step separation of BN statistic and parameter adaptation.** The paper correctly identifies that most TTA methods adjust BN statistics (μ, σ²) while leaving the scale/shift parameters (γ, β) unchanged, even though γ and β were optimized with respect to the training-time statistics. The proposed two-step design (BNSA then BNPA) directly addresses this mismatch. The ablation study (Table 2) confirms that using either step alone degrades performance.

2. **Data-driven weighting factor α computed from JS divergence without grid search.** Instead of relying on empirical tuning common in prior work (a-BN, DUA), the method estimates activation distributions and computes α as the average JS divergence between training-test instance pairs (Eqs. 3–4). The ablation ("BNSA w/o A") shows a clear accuracy drop when replacing this learned α with a fixed weight, providing direct empirical support.

3. **Consistent strong empirical results across diverse settings.** Table 1 reports results across seven datasets × three backbones (21 configurations), with the proposed method achieving best or second-best accuracy on the vast majority. Gains are notable in several cases (e.g., +2.84% on Cora with GCN, +2.60% on Elliptic with GraphSAGE). Results are averaged over ten random seeds, providing reasonable statistical reliability.

4. **Learnable mask matrix M with Gumbel-Max sampling.** The mask allows selective dimension-wise BN adaptation. The ablation ("BNSA w/o M") shows decreased performance, and Figure 3 (described in text) suggests the mask helps prevent model collapse on FB-100, a known failure mode for entropy-minimization methods.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient method specification for reproducibility (non-parametric density estimation, mask learning protocol, hyperparameters).** Several critical components are underspecified:
   - **Non-parametric density estimation** (Section 3.1): The paper states it uses "non-parametric density estimation" but never specifies the estimator (histogram? KDE with what bandwidth? How many bins?). The abstract mentions "a small histogram matrix," but this is never defined in the method section.
   - **Mask learning optimization**: It is unclear whether the Bernoulli matrix B is optimized per test batch, per test graph, or once over the entire test set. No optimization details (number of steps, learning rate, whether GNN parameters are frozen) are given.
   - **Hyperparameter values not reported**: None of the following are given: λ (Eq. 8), temperature τ (Eq. 5), step size k (Eq. 9), SGLD step size δ and number of steps T (Eq. 13), entropy threshold τ_e (Eq. 15), probability thresholds τ_c¹, τ_c² (Eq. 16). Without these, the method cannot be reproduced.

   **Why this is major**: The method as described is not reproducible. Overspecification in critical algorithmic components and missing hyperparameter values are barriers to verification and adoption.

### Minor

2. **Ablation study does not fully disentangle the contribution of individual components.** The ablation (Table 2) removes entire blocks (e.g., "BNSA w/o A" removes all weighting; "BNSA w/o M" removes the entire mask). This does not test whether simpler alternatives could achieve comparable results — e.g., using a fixed α=0.5, replacing the EBM with standard cross-entropy on pseudo-labels, or thresholding JS divergence directly instead of learning a mask. The paper acknowledges that gains from the mask are "marginal in some cases" and defers to calibration results in Section 4.4 (not present in the extract), but no calibration metrics (ECE, reliability diagrams) are shown in the visible text to substantiate this claim.

3. **Contrastive learning for mask optimization is not clearly motivated.** The paper optimizes the mask B using an InfoNCE contrastive loss with DropEdge augmentation and feature shuffling (Eqs. 7–8). This is a significant departure from typical TTA workflows (which avoid modifying graph structure), and the paper does not explain why contrastive learning is needed to learn the mask or what signal the mask captures that the JS divergence alone misses. The connection between the contrastive objective and the masking goal is left implicit.

4. **Adaptation of image-based TTA baselines to graphs is not discussed.** Baselines originally designed for images (TENT, SAR, MEMO, DELTA, a-BN, DUA) are used without commentary on how they were adapted to the non-i.i.d. node classification setting, where test samples have structural dependencies. While the paper states "experimental settings were adopted from their respective publications" (line 239), the practical differences between image-level and node-level TTA are nontrivial and should be explicitly addressed. Additionally, the dataset-specific OOD settings (what constitutes the distribution shift for each dataset) are referenced to prior work but not summarized.

5. **No runtime or computational cost comparison.** The paper acknowledges SGLD sampling increases computational cost (lines 221–222) but provides no wall-clock time per adaptation step or per test graph. For a practical TTA method, this information is important for assessing the performance-efficiency trade-off.

### Trivial

6. **Non-standard Gumbel-Max citation.** The paper cites "Jin et al., 2022a" for the Gumbel-Max trick, whereas the standard references are Jang et al. (2017) or Maddison et al. (2017). The paper should cite the original work.

## Nice-to-Haves

- A simpler baseline using fixed α (e.g., 0.5) + entropy minimization on BN parameters would quantify the benefit of the full framework over the simplest plausible approach.
- Calibration metrics (ECE, reliability diagrams) should be included to support the claimed calibration improvement.
- Pseudo-label quality analysis (accuracy before and after filtering) would strengthen validation of the filtering mechanism.
- Reporting standard deviations with significance tests (e.g., paired t-test) for the main comparisons would strengthen the claims.

## Removed Points

These points were removed per the review guidelines; they are listed here for transparency in case they are useful:

- **Criticism about typos and formatting artifacts** ("Networkorks," "$\mathrm{Xu}$," missing backslash, garbled abstract phrase, duplicated figure caption) — Removed per rule: these are treated as parser/formatting issues, not author errors.
- **Criticism about missing Section 4.4 / missing calibration results in the extract** — The parser strips sections; these likely exist in the original submission.
- **Criticism about the paper needing more graph-specific baselines** — Removed as scope creep; the paper already includes GTRANS and EERM as graph-specific baselines.
- **Suggestion that a-BN, DUA are "designed for images"** — While TENT, SAR, MEMO, DELTA are originally for images, a-BN and DUA are BN-statistic methods that are architecture-agnostic; this part of the criticism was overbroad.
- **Criticism about "marginal gains" being framed as fatal** — The paper's own ablation shows consistent (if sometimes modest) improvements, and the marginal-gain observation is the authors' own honest reporting. Not a fatal flaw.

## Novel Insights

The most interesting observation across the reviews is that the paper's core tension — high method complexity vs. sometimes marginal component-level gains — is itself informative. The JS divergence weighting and the learnable mask are motivated by a real limitation (fixed α via grid search is fragile; full BN dimension adaptation may hurt), but the contrastive learning objective for mask training feels bolted on rather than organically derived from the BN adaptation problem. An alternative framing where the mask is derived directly from the JS divergence values (e.g., by thresholding) rather than learned through a separate contrastive loop could reduce complexity without sacrificing performance — and the paper's own admission that mask gains are "marginal in some cases" indirectly supports this. The EBM-based BNPA step is more distinctive and less common in the TTA literature; its pseudo-label filtering mechanism is a practical contribution worth preserving even if the contrastive mask learning were simplified.

## Suggestions

1. **Specify every underspecified component.** Provide pseudocode for the full TTA procedure. Report the specific non-parametric density estimator used (e.g., histogram with bin count per dimension). State the mask learning protocol: per-batch or per-test-set, number of optimization steps, learning rate, whether GNN weights are frozen. Report all hyperparameter values in a table.

2. **Tighten the ablation study.** Test simpler alternatives: (a) replace the learned mask with a threshold on JS divergence values, (b) replace the EBM with standard cross-entropy on filtered pseudo-labels, (c) replace contrastive learning with KL regularization alone for mask training. Include calibration metrics (ECE) to substantiate the claimed calibration benefits.

3. **Motivate or remove the contrastive learning step for mask training.** Either explain why DropEdge + InfoNCE is the right objective for learning which BN dimensions to adapt, or simplify by learning the mask more directly (e.g., via the KL divergence term alone).

4. **Summarize the OOD setting for each dataset.** Describe what distribution shift each dataset represents (e.g., train/test time split, domain shift, cross-graph generalization) so readers can assess the evaluation scope without referencing prior papers.

5. **Provide runtime comparisons** for the proposed method and strongest baselines, even as wall-clock time per test graph.

6. **Fix the Gumbel-Max citation** to Jang et al. (2017) or Maddison et al. (2017).

## Score and Decision

The paper introduces a novel and principled two-step BN adaptation framework for GNN TTA, supported by strong empirical results across diverse settings. However, the method is insufficiently specified for reproducibility (missing hyperparameters, underspecified density estimation and mask learning protocols), which is a major barrier to verification and adoption. The ablation study also does not fully disentangle whether the elaborate framework's complexity is warranted. These issues are addressable in revision but are significant enough in the current form to preclude acceptance.

**Overall assessment**: The core ideas have merit, and the empirical results suggest the method works well, but the paper requires major revision — particularly in method specification and ablation rigor — before it is ready for publication.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>