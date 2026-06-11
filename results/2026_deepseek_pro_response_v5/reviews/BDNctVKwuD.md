Now I have a good calibration picture. Let me finalize the review.

**Round 2 comparison:**

- **zKvrOOBouT (6.50)**: Well-executed spurious correlation mitigation method. Clean methodology, strong results, well-defined approach. Our paper has more theoretical novelty (ContrastiveCAMs, CE decomposition, consistency proof) but more rough edges.
- **8DuJ5FK2fa (6.00)**: Spurious correlation robustness, incremental contributions, some unfair comparison issues. Our paper has more novel contributions and stronger external validation.
- **ONhLaNbxVV (5.75)**: Incremental improvements to ProtoPNet. Our paper is more ambitious.
- **3b8CgMO5ix (5.50)**: Poor presentation, missing comparisons. Our paper is clearly better presented and more comprehensive.

Our paper sits between 5.75 and 6.50. I'll place it at **6.0** — strong enough for acceptance with revision, but not as polished as the 6.50 EvA paper. The training procedure concern (deferred to appendix) is addressable, and the core contributions are genuinely novel and well-validated.

---

## Summary
This paper identifies a theoretical ambiguity in HiResCAM explanations — they are not uniquely determined due to softmax shift-invariance, admitting an arbitrary spatial shift matrix M while corresponding to the same prediction. The authors propose ContrastiveCAMs, pairwise class-difference CAMs that cancel this ambiguity while providing richer class-versus-class explanations. They then leverage ContrastiveCAMs to decompose cross-entropy loss into core and non-core region contributions, revealing that CE does not inherently favor target-relevant features, and propose Core-Focused Cross-Entropy (CFCE), which penalizes non-core region contributions during training. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC demonstrate substantially improved feature alignment, with a particularly compelling Pareto improvement on PASCAL VOC where alignment doubles while preserving classification performance. Downstream segmentation transfers provide genuine external validation.

## Strengths
- **ContrastiveCAMs provide an M-invariant, class-versus-class extension of HiResCAM (Theorem 3.5, Definitions 3.3–3.4):** The pairwise-difference formulation cancels the spurious M-matrix exactly, and class-reconstructed variants recover single-class summaries. The class-versus-class granularity reveals model behaviors that single-class CAMs obscure, as demonstrated qualitatively in Figure 2.
- **Cross-entropy is formally decomposed into core and non-core region contributions via ContrastiveCAMs (Proposition 4.2, Remark 4.3):** This provides a clean theoretical basis for understanding feature misalignment — CE will use non-core surrogates when targets are small. Table 1 empirically corroborates this: on Hard-ImageNet, non-core contributions (42.138) dominate core contributions (14.817) despite 95.73% accuracy.
- **CFCE+KL achieves dramatic improvements in feature alignment on Hard-ImageNet (Table 2):** ContrastiveCAM IoU reaches 93.39% vs. 30.27% for CE w/ Arch; Relative Foreground Sensitivity flips from −0.23 (CE) to +0.236 (CFCE+KL), confirming the model fundamentally reorients predictions around core regions.
- **Pareto improvement on PASCAL VOC (Section 5.3):** CFBCE+KL simultaneously improves Average Precision (87.19% vs. 87.32%) and nearly doubles IoU (85.39% vs. 44.50% for CE), a rare case where adding an alignment constraint does not force an accuracy trade-off. The downstream segmentation bar chart provides genuine external validation that learned features transfer better.
- **Practical viability with approximate masks (Section 5.2):** CFCE achieves competitive IoU using SAM-generated masks (83.95%) and bounding boxes (79.13%), compared to 82.92% with ground-truth masks, weakening the objection that the method requires expensive pixel-level annotations.
- **Consistency proof (Theorem 4.6):** CFCE is classification-calibrated with respect to the Core-Constrained Risk Minimization objective, providing theoretical justification beyond ad-hoc regularization.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **The practical significance of the M-invariance finding is not directly demonstrated.** Theorem 3.2 is mathematically correct but no real example is shown where a trained model's HiResCAM explanation is misleading due to the M-shift. Figure 1 is a schematic diagram, not a real model output. The ContrastiveCAM contribution stands on its own merits regardless, but the paper overclaims slightly by presenting this as exposing a critical flaw rather than a sensible extension.
- **Partially circular evaluation on Hard-ImageNet.** The core evaluation metrics — accuracy under core-region ablation and RFS — directly quantify reliance on core regions, which is precisely what CFCE's loss function optimizes. Improvements on these metrics are therefore expected rather than surprising. This is partially mitigated by the downstream segmentation results on PASCAL VOC and by IoU metrics, but the Hard-ImageNet results should be interpreted as validation that the loss achieves its intended effect rather than as fully independent evidence.
- **CE w/ Arch baseline degradation is unexplained.** On Oxford-IIIT Pets, CE w/ Arch achieves 39% IoU vs. 78% for plain CE — the architectural modifications alone severely degrade alignment. This raises questions about whether CFCE's improvements partly compensate for damage introduced by the modifications. The paper states these are "detailed in Appendix C" (line 231) but the main text should at minimum characterize them. Note that CFCE still improves over plain CE (82.92% vs. 78.37%), so the core method works independently.
- **CFBCE is undefined in the main text.** The multilabel variant used on PASCAL VOC (Section 5.3) appears only in the results table without definition. Even a brief sketch would improve self-containedness.
- **Core/non-core contribution metric in Table 1 is not explicitly defined.** The table reports "Core" and "Non-Core" average contributions but the exact formula is not stated.
- **The training procedure for CFCE is deferred entirely to Appendix B.** The CFCE loss (Eq. 15) depends on ContrastiveCAMs, which are themselves functions of gradients (Eq. 2). The main paper should at minimum note what approach is taken (e.g., stop-gradient on CAMs). This is standard for CAM-based training methods and the appendix likely resolves it, but a sentence in the main text would improve readability.

### Trivial
- **Discussion section is too brief** and omits acknowledgment of limitations such as the need for core-region masks, the clean-accuracy trade-off on Hard-ImageNet, and the single-layer classifier assumption.

## Nice-to-Haves
- A brief discussion of computational cost (wall-clock or FLOP overhead of computing ContrastiveCAMs during training vs. standard CE training).
- Comparison to conceptually related prior work on explanation-guided training (e.g., Ross et al. 2017 "Right for the Right Reasons") would contextualize the value of the ContrastiveCAM-based formulation.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that CFCE training requires "second-order optimization" and is a "fatal" reproducibility gap:** The main paper defers implementation details to Appendix B, which is standard practice. The harsh critic speculates about what the appendix may or may not contain — this is a speculation, not a verifiable flaw. Many CAM-based training methods use stop-gradient; the paper's deferral to the appendix is not a fatal gap. Demoted from fatal/major to minor.
- **Harsh critic's claim that "(1−H) ⊙ |CAM| penalizes even helpful non-core contributions":** The paper's stated goal is to suppress all non-core contributions; whether some non-core contextual cues are helpful is a philosophical question about feature alignment definitions, not a flaw in the method.
- **Strength finder's claim that Theorem 3.2 is a "rigorous identification of a fundamental HiResCAM limitation":** The M-shift is a straightforward consequence of well-known softmax shift-invariance (Proposition 3.1). The observation is mathematically correct but its practical significance is unproven.
- **Any formatting/typo complaints:** Removed per hard rules (parser artifacts).
- **Missing related work citations / missing baselines like "Right for the Right Reasons":** Removed per hard rules.
- **Request for compute time analysis, testing on larger datasets, or using larger models:** Generic weakness that could apply to almost any paper. Nice-to-have at most.

## Novel Insights
The paper's decomposition of cross-entropy into spatially-attributable core and non-core region contributions via ContrastiveCAMs (Proposition 4.2, Remark 4.3) is genuinely novel. It provides a precise mathematical mechanism explaining why standard training produces misaligned features when targets occupy small image regions — going beyond prior empirical observations of shortcut learning. The insight that CE will "learn the best non-core surrogate to the actual target" when core regions are small (Section 4.1, scale-sensitivity discussion) is a crisp theoretical contribution.

## Suggestions
- Add a sentence in Section 4.2 noting how gradients through ContrastiveCAMs are handled in practice (e.g., "we use stop-gradient on the CAM computation during training").
- Provide a one-sentence sketch of CFBCE in the main text rather than deferring entirely to the appendix.
- Add a short limitations paragraph to the Discussion acknowledging the need for masks and the single-layer classifier assumption.
- Consider reframing Theorem 3.2 as a motivating observation for ContrastiveCAMs rather than a "limitation" of HiResCAM, since the practical impact of the M-shift is not demonstrated.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Tj3xLVuE9f (Shortcut Learning Foundations) | 6.80 | R1 | More polished, cleaner theoretical story; our paper has more applied contribution |
| zKvrOOBouT (EvA) | 6.50 | R2 | Cleaner methodology, better defined approach; our paper has comparable novelty |
| mutJBk3ILg (SSL Feature Augmentation) | 6.25 | R2 | Similar quality tier; our paper has stronger theoretical grounding |
| 8DuJ5FK2fa (EVaLS) | 6.00 | R2 | Incremental contributions, comparison issues; our paper is more novel |
| ONhLaNbxVV (ProtoPNet Improvement) | 5.75 | R2 | More incremental; our paper is more ambitious with broader validation |
| 3b8CgMO5ix (Classifiers→Segmentation) | 5.50 | R2 | Poor presentation, missing comparisons; our paper is clearly better |
| T7q5LBGISH (Saliency Smoothing) | 5.25 | R2 | Less ambitious scope; our paper has broader contributions |

**Bracket:** Round 1 placed the paper between 5.0 and 6.5. Round 2 narrowed this to roughly 5.75–6.25 by comparison with the most topically similar anchors (EvA at 6.50 and EVaLS at 6.00). The paper is clearly stronger than the 5.50 and 5.75 anchors but not as polished as the 6.50 EvA paper. The core contributions (ContrastiveCAMs, CE decomposition, CFCE) are novel and well-validated across multiple datasets, with the PASCAL VOC Pareto improvement being particularly compelling evidence.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>