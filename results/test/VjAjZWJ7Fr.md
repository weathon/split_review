I now have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper proposes a graph-theoretic framework for jointly addressing OOD generalization and OOD detection. The authors construct a graph whose vertices are augmented data (both labeled ID and unlabeled wild data), with edges based on a combination of self-supervised (augmentation co-occurrence) and supervised (same-class) connectivity. They derive the Spectral Learning with Wild Data (SLW) loss, prove its equivalence to spectral decomposition of the normalized adjacency matrix (Theorem 3.1), and use this connection to analyze closed-form representations for a 5-point illustrative example. Empirically, SLW shows competitive OOD detection and generalization on CIFAR-10 compared to wild-data baselines including SCONE.

## Strengths

- **Principled graph construction integrating supervised and self-supervised signals.** The edge weights (Eq. 3) combine augmentation-based connectivity with class-label connectivity via tunable coefficients η_u and η_l. This cleanly formalizes the wild-data setting (labeled ID + heterogeneous unlabeled data) within a spectral graph framework, extending prior spectral contrastive learning (HaoChen et al. 2021, Shen et al. 2022, Sun et al. 2023) to the more complex heterogeneous mixture setting.

- **Exact equivalence between the SLW loss and spectral decomposition of the normalized adjacency matrix (Theorem 3.1).** This connection grounds the learned representations in a closed-form spectral structure (Section 4.1: Z = D^{-1/2} V_k √Σ_k), providing a formal basis for the subsequent analysis of OOD generalization and detection. The loss is end-to-end trainable with standard SGD.

- **Empirical competitiveness against the closest wild-data baseline.** On CIFAR-10, SLW achieves notable gains on individual datasets (e.g., 25.10% FPR95 reduction on Textures vs. SCONE). The visualizations (Figure 4) show embedding structures consistent with the framework's predictions: covariate-shifted OOD data clusters near ID data, while semantic OOD data is separated.

## Weaknesses

### Fatal

None. The paper's core contributions — the graph formulation, the SLW loss, and the spectral equivalence — are sound.

### Major

1. **Theory-practice gap due to post-training fine-tuning (undermines the claimed theoretical support).** After SLW contrastive training, the model is fine-tuned with cross-entropy loss on labeled ID data (Section 5.1). All reported metrics (ID Acc, OOD Acc, FPR95, AUROC) and visualizations come from this fine-tuned model, not from the raw SLW representations. The theoretical analysis (Theorems 3.1, 4.1, 4.2; Section 4.1) applies to the pre-fine-tuning representations Z whose closed form derives from spectral decomposition. Fine-tuning can arbitrarily alter the feature space, breaking the theoretical connection. The paper does not address this gap or provide any justification (theoretical or empirical) for why the spectral properties should persist after fine-tuning. This is a standard limitation in contrastive learning papers that fine-tune, but it is especially consequential here because the paper's central claim is *theoretical understanding* of the learned representations — the fine-tuning step severs that link.

2. **The "provable error" and "theoretical insight" (contribution 2) are delivered only for a 5-point illustrative example, not as general results.** Theorems 4.1 and 4.2 provide closed-form eigenvectors and a separability expression for a toy setup with exactly five data points (angel sketch, tiger sketch, angel painting, tiger painting, panda), hand-specified augmentation probabilities (four parameters ρ, α, β, γ), and fixed hyperparameters (η_u=5, η_l=1). The paper is transparent in calling this "An Illustrative Example" (Section 4.3), but the abstract and introduction frame the contribution in far more general terms ("provable error quantifying OOD generalization and detection performance," "formal theoretical characterization of performance through graph factorization"). There is no general theorem bounding OOD generalization error or OOD detection performance for arbitrary graph sizes, data distributions, or augmentation schemes. The theoretical contribution is therefore more limited than the framing suggests.

3. **No standard deviations, confidence intervals, or error bars for any experimental result.** Given the stochasticity in wild data composition, training, and fine-tuning, single-run reporting is insufficient. This is a significant empirical reporting gap for a paper that relies on experiments as the primary evidence for the method's practical value.

### Minor

1. **Limited empirical scope.** Results are reported on a single ID dataset (CIFAR-10). While this follows the prior work (SCONE), evaluating on CIFAR-100 or a subset of ImageNet would substantially strengthen the claim that the method generalizes beyond one benchmark.

2. **The separability measure S(f) (Eq. 8) is not formally linked to standard OOD detection metrics (AUROC, FPR95).** The paper states "Larger S(f) suggests better OOD detection capability," but no bound or monotonic relationship is established. Larger inter-class Euclidean distance does not guarantee better detection performance in non-spherical embedding geometries.

3. **The augmentation model in the theoretical analysis (Eq. 9) differs substantially from the augmentations used in practice.** The theoretical analysis conditions on class and domain labels (y(x), d(x)), while the actual experiments use standard augmentations (Gaussian blur, color distortion, random cropping). The adjacency matrix construction in theory and practice is therefore not directly aligned. The paper does not discuss this gap.

### Trivial

- The loss component equations (Eq. 6) contain garbled LaTeX (\ddots symbols) in the PDF extraction, though the textual interpretation (lines 133-135) provides a clear functional description of each L1–L5 term.

## Nice-to-Haves

- Report linear probing results *without* fine-tuning to directly validate the spectral decomposition analysis.
- An ablation study on the effect of η_u and η_l on both OOD generalization and detection metrics.
- A formal link between S(f) and standard OOD detection metrics (e.g., a bound relating S(f) to the optimal AUROC under Gaussianity assumptions).

## Removed Points

- *Criticism that the loss function is not clearly defined / not reproducible.* The textual description (lines 133-135) clearly specifies each of the five loss components (L1: two views from same-class labeled images; L2: two views from same image; L3–L5: various negative pairings). The proof of Theorem 3.1 is likely in the appendix (stripped by the parser). The \ddots symbols are parser artifacts, not author errors. [Rationale: Parser artifact + textual description is sufficient + missing appendix/proofs are parser-stripped.]

- *Criticism that identical baseline ID/OOD Acc values are "suspicious" or indicate formatting errors.* The table caption explicitly explains: "(*Since all the OOD detection methods use the same model trained with the CE loss on P_in, they display the same ID and OOD accuracy on CIFAR-10-C.)" The reviewer missed this. [Rationale: Factually wrong — the paper already explains this.]

- *Criticism about missing results for Places365/LSUN-R (Table 2).* The caption explicitly references Table 2 for these results; Table 2 is present in the original submission but not in the parser's text extraction. [Rationale: Parser artifact.]

- *Criticism about no results on larger benchmarks (CIFAR-100, ImageNet).* The paper follows the existing setup (Bai et al. 2023) and evaluates on a representative set. Adding more ID datasets would strengthen the paper but its absence is not a flaw — it's scope for future work. [Rationale: Scope creep.]

- *Criticism that the related work section "reads as a list."* This is a presentation preference, not a weakness affecting the paper's technical merit. [Rationale: Style nitpick.]

- *Complaints that the novelty is "in the framing rather than the algorithm."* The algorithm differs from prior spectral contrastive learning by integrating both supervised and self-supervised signals for the specific wild-data setting (heterogeneous mixture of ID, covariate OOD, and semantic OOD), which is a genuine adaptation. [Rationale: Subjective taste disagreement, not a verifiable weakness.]

## Novel Insights

The most interesting observation from the reviews is that the fine-tuning gap — often dismissed as a minor implementation detail in contrastive learning papers — becomes a *first-order* problem here because the paper's selling point is theoretical grounding. This suggests a general tension in the spectral-contrastive-learning literature: when a method's theoretical appeal depends on closed-form spectral solutions, any post-hoc fine-tuning step must be justified or the theoretical claims apply to a different model than the one actually evaluated. The paper's framework could be strengthened by measuring how much fine-tuning actually changes the embedding geometry relative to the spectral predictions, which would be a novel and useful analysis for the field.

## Suggestions

1. **Address the fine-tuning gap.** Either (a) report linear probing results on raw SLW embeddings (without fine-tuning) to directly validate the theoretical predictions, or (b) provide theoretical or empirical justification for why fine-tuning preserves the spectral structure (e.g., measured cosine similarity or Procrustes alignment between pre- and post-fine-tuning representations). Without this, the claimed theoretical support applies to a different model than the one evaluated.

2. **Provide a genuinely general theoretical result.** Even a bound under simplifying assumptions (e.g., on the spectral gap of the graph, or the alignment of top eigenvectors with class indicators) would be far more valuable than the current 5-point worked example. The spectral-contrastive-learning literature provides templates for such bounds (HaoChen et al. 2021).

3. **Report standard deviations** for all metrics across at least 3 random seeds / wild-data compositions.

## Score and Decision

**Originality:** Moderate. The graph-based framework for joint OOD generalization/detection is a novel application of spectral contrastive learning, though it builds directly on prior spectral methods (HaoChen et al. 2021, Shen et al. 2022, Sun et al. 2023).

**Importance:** High. Jointly handling OOD generalization and detection is an important and underexplored problem.

**Claims vs. evidence:** The core framework and loss are well-motivated, but the "provable error" (contribution 2) is significantly overclaimed relative to what is actually delivered (a toy example). The empirical evidence is competitive but lacks statistical rigor (no error bars) and comes from a single ID dataset.

**Soundness:** The theoretical equivalence (Theorem 3.1) is sound, and the empirical methodology follows prior work. However, the fine-tuning gap weakens the connection between theory and practice.

**Clarity:** Generally well-written, though the loss equation is partially garbled in the extracted text; the textual description compensates.

**Value:** The framework and loss design offer a promising perspective, but the paper needs stronger theoretical results and cleaner empirical reporting to deliver on its promises.

The paper presents a well-motivated framework but the execution has three significant gaps: (1) the "provable error" theoretical contribution is limited to a toy example, (2) the fine-tuning step breaks the claimed theoretical connection, and (3) the empirical evaluation lacks error bars and is limited to one ID dataset. These issues are addressable but substantial. I recommend rejection in the current form, with the note that the core idea has merit and could form a stronger paper with the suggested revisions.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>