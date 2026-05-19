- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 5, 8
Now I have all the information I need. Let me produce the final consolidated review.

## Summary
This paper integrates Deep Evidential Regression (DER) into Video Temporal Grounding (VTG) to handle uncertainty from open-vocabulary queries and out-of-distribution videos. It identifies two biases in a DER-based baseline — modality imbalance (over-reliance on vision vs. text) and counterintuitive uncertainty (mismatch between error magnitude and uncertainty) — and proposes three components to address them: a Reflective Flipped Fusion (RFF) block for progressive cross-modal alignment, a query reconstruction (QR) auxiliary task to strengthen text sensitivity, and a Geom-regularizer that replaces the vanilla DER regularizer to better align evidence with prediction accuracy. Experiments on QVHighlights, TACoS, Charades-STA, and TVSum show competitive or state-of-the-art results.

## Strengths

- **First integration of DER into VTG with competitive task accuracy.** Table 1 shows DDM-VTG outperforms prior SOTA methods across multiple datasets (e.g., +8.0% R1@0.5 over MomentDiff on QVHighlights, +2.3% R1@0.5 over UniVTG on TACoS). This provides concrete evidence that DER can be adapted to VTG without sacrificing grounding performance.

- **Explicit identification and targeted quantitative mitigation of modality imbalance.** Section 5.2 and Table 3(a) introduce Var\_vis, Var\_text, and Δ\_Var metrics to directly measure uncertainty sensitivity to each modality. The results show that RFF+QR reduce Δ\_Var, and Figure 6 visualizes the balanced uncertainty distributions — providing separate, interpretable evidence that each component contributes to its intended goal.

- **Thorough ablation with dedicated metrics for each proposed component.** Rather than relying solely on task accuracy for ablation, Table 3(a) measures modality balance via Δ\_Var and Table 3(b) measures uncertainty calibration via information entropy and EUCM. This gives disentangled evidence for the RFF block, QR task, and Geom-regularizer.

- **Generalization across multiple VTG subtasks.** DDM-VTG is evaluated on moment retrieval (Table 1), highlight detection (Table 1), and video summarization (Table 2), achieving strong results on all three. This shows the debiasing framework is not tailored to a single task formulation.

- **Informative qualitative analysis of temporal bias and uncertainty.** Figure 8 provides an insightful visualization of how ground-truth moments are distributed in QVHighlights and how different regularization methods affect epistemic uncertainty in temporally sparse (OOD) regions. The progression from (b) to (e) clearly shows the Geom-regularizer producing higher epistemic uncertainty in temporal OOD regions, unlike alternatives.

## Weaknesses

### Fatal
None.

### Major

- **The key calibration metric EUCM is never defined in the main paper.** Table 3(b) reports "EUCM" alongside information entropy as the primary quantitative evidence that the Geom-regularizer improves uncertainty calibration. However, the paper never defines what EUCM stands for or how it is computed. It is mentioned only in passing (line 203: "results in a lower EUCM score"). Since the paper's central claim is better uncertainty calibration, the absence of this definition is a serious omission — readers of the main paper cannot evaluate the quantitative calibration claims. (The appendix likely contains the definition, but the main text is expected to be self-contained for a key metric.)

- **The baseline (DER+VTG without debiasing) is not included in Table 1.** The paper builds a baseline in Section 4.2, identifies two biases in it, and then proposes DDM-VTG to fix them. Yet Table 1, which reports the primary task performance, contains only DDM-VTG and prior published methods, omitting the baseline from which the paper measures improvement. Without this column, readers cannot determine how much of the reported gain over prior methods comes from the DER integration itself versus the specific debiasing components. The ablation in Table 3 uses custom metrics (Δ\_Var, EUCM), not the standard VTG metrics (R1@0.5, MAP), so the baseline's task accuracy is unreported.

### Minor

- **The Geom-regularizer is introduced as a heuristic without principled justification.** The paper's motivation (accurate predictions should have high evidence) is intuitive, and the gradient analysis in Figure 4 shows *that* the gradient differs from the vanilla regularizer. However, the specific linear constraint $\overline{\Phi} + \overline{\Delta} = 1$ is not derived from any risk bound, proper scoring rule, or formal criterion. The paper does not discuss whether this constraint could introduce its own biases (e.g., forcing high evidence on samples with irreducible aleatoric noise). A principled justification or a more rigorous discussion of limitations would strengthen the contribution.

- **The gradient of delta in Eq. (10) is set to zero without justification or ablation.** Line 180 states: "Since our purpose of using DER is to optimize uncertainty without affecting the model's grounding capability, the gradient of delta in Eq. (10) is set to zero." This means the error term $\overline{\Delta}$ is effectively detached from gradient updates in the Geom-regularizer — the model only receives gradients through $\overline{\Phi}$. This is a non-standard implementation choice that is neither justified theoretically nor ablated empirically.

- **The normalization procedure for $\overline{\Delta}$ and $\overline{\Phi}$ is ambiguous.** The paper states "we normalize $\Delta$ to $\overline{\Delta}$ and $\Phi$ to $\overline{\Phi}$ (i.e.2)" (line 137 — the "i.e.2" is a parser artifact, likely a reference to an appendix subsection). The mathematical definition of the normalization (min-max, z-score, or other) is not given in the main paper, making the Geom-regularizer's exact form ambiguous.

- **The OOD evaluation is scoped only to temporal distribution shift within the dataset.** The paper repeatedly motivates the need for handling open-vocabulary queries and OOD videos (abstract, introduction). Yet the only OOD analysis (Figure 8) studies temporal bias — distribution shift within the dataset's own temporal structure. This is a valid form of OOD, but it does not address more challenging scenarios such as unseen video domains, entirely different caption distributions, or adversarial queries, which the motivation suggests.

- **The two-stage training and QR head freezing are not ablated.** The QR head is used for warm-up and then frozen in the second stage (line 121). The paper does not explore whether continuing the QR loss throughout training would further improve results, or whether the freezing is essential.

### Trivial

- The normalization type for $\overline{\Delta}$ and $\overline{\Phi}$ should be specified explicitly in the main text.
- The text contains a few minor typos (e.g., "trainging" line 14, "fti" line 19, "regularizor" line 101) that do not affect comprehension.

## Nice-to-Haves

- Reporting statistical significance (variance across runs) for the main results would strengthen confidence, particularly for gains of 2-8%.
- Replacing the qualitative scatter plots in Figure 7 with quantitative calibration metrics (e.g., Spearman correlation between error and uncertainty, expected calibration error for regression) would make the calibration claim more rigorous.
- Including the baseline's task performance in Table 1 would resolve the most central ambiguity.
- Evaluating on a held-out-domain OOD benchmark (e.g., train on QVHighlights, test on a different domain) would more directly support the robustness claims.

## Removed Points

These points are flagged to be removed. Treat them with caution.

- *"Baseline numbers unreported" (framed as "hollow" / fatal)*: The harsh critic argued that without the baseline in Table 1, the "primary claim is hollow." This overstates the issue — the paper's primary claim is that DDM-VTG outperforms prior SOTA, which Table 1 does support. The missing baseline is a major weakness but not fatal. Retained as Major above.

- *"Comparison fairness not established — backbone not controlled"*: The paper explicitly states it follows Lin et al. (2023) and Li et al. (2024) in using CLIP (ViT-B/32) + SlowFast (ResNet-50) as a frozen backbone. This is a standard and adequate way to ensure fair comparison. Removed as factually incomplete.

- *"RFF block is a known architecture" + "first extension of DER is architecturally trivial"*: These are opinions about novelty, not verifiable weaknesses. The paper does not claim architectural novelty for the cross-attention pattern; its contribution is in the debiasing framework.

- *"Code not available"*: Per the hard rules, criticisms about release status of cited artifacts are removed.

- *"Baseline model ambiguity (simple modality concatenation or unimodal self-attention)"*: The paper's phrase "simple modality concatenation or unimodal self-attention" describes prior general approaches, not the paper's own baseline architecture. The baseline is clearly defined in Section 4.2 as DER+VTG.

- *"Table 2 on TVSum significance"*: Requesting significance for a small-dataset result is a field-standards issue; moved to nice-to-have.

- *"The paper overstates its novelty"* in Section-by-Section notes: Subjective opinion removed.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface the same core tension: the paper makes a clear and reasonable set of methodological improvements to a DER-based VTG baseline and provides solid ablation evidence for component contributions, but the presentation of the central quantitative calibration evidence (EUCM) is incomplete, and the main results table would benefit from directly showing the baseline's performance. Neither reviewer identifies a perspective or connection the paper itself does not already articulate.

## Suggestions

1. **Define EUCM explicitly in the main paper.** Since this is the key calibration metric, include a brief definition in Section 5.2 or in a dedicated metrics paragraph.

2. **Add the baseline (DER + VTG without debiasing) to Table 1.** This single change would let readers directly attribute gains to the debiasing components vs. the DER integration itself.

3. **Justify or ablate the "gradient of delta set to zero" choice.** Either explain why detaching delta is principled, or run an ablation comparing the detached vs. attached gradient variants.

4. **Specify the normalization formula** for $\overline{\Delta}$ and $\overline{\Phi}$ (min-max across the batch? fixed range based on dataset statistics?) in the main text.

5. **Replace qualitative calibration plots (Figure 7) with quantitative metrics** such as Spearman correlation or ECE-for-regression, alongside the existing qualitative analysis, to strengthen the calibration claim.

6. **Clarify the scope of OOD evaluation.** The paper's OOD analysis is limited to temporal distribution shift. Either acknowledge this scope explicitly in the conclusion/limitations, or add experiments on a cross-domain OOD setting.
