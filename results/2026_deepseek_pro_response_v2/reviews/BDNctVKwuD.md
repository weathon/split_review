Now I have a clear calibration picture. Let me compare:

- **Q95MaWfF4e (7.00)**: Identifies CAV directional divergence, proposes pattern-based CAVs. Similar pattern to my paper (theory → fix → evaluation) but with narrower experiments and simpler theory. My paper's M-invariance insight and CFCE framework are more substantial.
- **OZWHYyfPwY (7.00)**: Questions feature visualization reliability with adversarial attacks + theory. Deep theoretical analysis, but doesn't propose a practical fix. My paper is comparable in rigor but more action-oriented.
- **Tj3xLVuE9f (6.80)**: Systematic study of shortcut learning with NTK theory. Foundational and broad. My paper is more applied but with cleaner mathematical insight.
- **57NfyYxh5f (6.25)**: Empirical study of probing techniques. My paper has stronger theoretical contributions.

The paper sits between 6.25 and 7.00. The architectural confound and missing hyperparameters pull it below 7.0, but the clean theory and strong Hard-ImageNet results put it above 6.25. Final score: **6.5**.

Now let me write the final review.

## All anchors retrieved:

Round 1:
- wZiH43e5Ah (3.00) — CAN concept extraction — clearly below current paper
- WYsLU5TEEo (2.50) — counterfactual GAN images — clearly below
- FTSUDBM6lu (2.50) — Patch Ranking Map — clearly below
- FHQDCQFD8y (3.00) — Grad-TopoCAM for EEG — clearly below
- Tj3xLVuE9f (6.80) — Shortcut Learning foundations — comparable, slightly higher
- bkdWThqE6q (6.00) — Interpretable Transformer — current paper is stronger
- mKGXdsq7fD (4.33) — Pixel-level XAI evaluation — current paper is stronger
- U7VW3KBm34 (6.00) — SRD explanations — current paper is stronger
- 5Ca9sSzuDp (8.00) — CLIP interpretability — clearly above current paper
- 25kAzqzTrz (8.00) — FixMatch theory — clearly above
- uHLgDEgiS5 (8.00) — Training data influence — clearly above
- 2dnO3LLiJ1 (8.00) — ViT registers — clearly above

Round 2:
- bkdWThqE6q (6.00) — Interpretable Transformer (repeated)
- 57NfyYxh5f (6.25) — How to Probe — current paper is stronger
- Tj3xLVuE9f (6.80) — Shortcut Learning (repeated)
- U7VW3KBm34 (6.00) — SRD (repeated)
- OZWHYyfPwY (7.00) — Feature visualization unreliability — comparable, current paper slightly below
- GjfIZan5jN (7.33) — Representation classifiability — clearly above current paper
- Q95MaWfF4e (7.00) — Pattern-based CAVs — comparable, current paper slightly below
- khuIvzxPRp (6.80) — CLIP adversarial fine-tuning — comparable

Bracket: 6.0–7.5 → narrowed to 6.5 based on round-2 comparisons.Now let me write the final review.

## Summary
This paper makes two linked contributions: (1) it identifies that HiResCAM explanations are not uniquely determined due to softmax shift-invariance — the same predictions can correspond to infinitely many HiResCAMs shifted by an arbitrary matrix M — and proposes ContrastiveCAMs, a pairwise-difference formulation that provably cancels this spurious shift; (2) it leverages ContrastiveCAMs to derive Core-Focused Cross-Entropy (CFCE), a loss that penalizes non-core region contributions and is proven classification-calibrated. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show CFCE-trained models dramatically increase reliance on core regions while maintaining competitive accuracy.

## Strengths
- **Rigorous identification of a fundamental HiResCAM limitation (Theorem 3.2)**: The proof that HiResCAMs admit arbitrary spurious shifts by a matrix M while corresponding to identical probability predictions is clean, correct, and has been overlooked in prior CAM-family work. The redundancy ratio γ (Table 1) quantifies empirically that this shift is non-negligible in practice (γ = 0.201–0.367 across datasets).

- **ContrastiveCAMs are a principled, provably invariant solution (Theorem 3.5)**: The pairwise-difference formulation elegantly cancels the spurious M, yielding uniquely determined explanations. The class-versus-class granularity reveals structure hidden by HiResCAM (Figure 2), such as environmental cues for "dog sled" vs. "volleyball" — a level of analysis unavailable from prior CAM methods.

- **Dramatic improvement in core-region reliance on Hard-ImageNet (Table 2)**: CFCE models show gray-mask accuracy dropping from 76.53% (CE w/ Arch) to 41.78% (CFCE), tile-mask from 71.02% to 34.31%, with RFS flipping from −0.23 to +0.224. The combination of low ablation accuracy and high positive RFS is a strong, internally consistent signal that the model genuinely depends on core regions rather than spurious features. The ContrastiveCAM IoU improvement from 30.27% (CE w/ Arch) to 89.22% (CFCE) further supports improved feature alignment.

- **CFCE is theoretically grounded via classification calibration (Theorem 4.6)**: The proof that optimizing CFCE-risk converges to optimal Core-Constrained Risk Minimization distinguishes this from ad-hoc regularizers. The decomposition of cross-entropy via ContrastiveCAMs (Proposition 4.2) provides a direct theoretical explanation for why standard training permits feature misalignment and directly motivates the CFCE objective.

- **Robustness to annotation quality (Oxford-IIIT Pets, §5.2)**: CFCE achieves strong IoU with auto-generated SAM masks (83.54% CFCE+KL) and bounding-box supervision (79.13%), demonstrating that pixel-perfect annotations are not required — a practically significant finding for broader applicability.

- **Downstream segmentation transfer benefits (§5.3)**: Core-focused backbones yield improved IoU on PASCAL VOC segmentation in both fine-tuned and end-to-end settings, suggesting the learned representations are genuinely better aligned with object structure rather than merely overfitting to the classification IoU metric.

## Weaknesses

### Fatal
None.

### Major
- **Architectural modifications are not fully disentangled from the CFCE loss**: The ResNet-50 modifications required by the method (bias removal, plus unspecified changes in Appendix C) degrade the CE w/ Arch baseline substantially on some metrics — e.g., binary IoU on Oxford-IIIT Pets drops from 78.37% (CE) to 39.07% (CE w/ Arch). While CE w/ Arch serves as a same-architecture baseline and CFCE's improvements over it are dramatic (82.92% vs. 39.07%), the paper does not ablate how much of the alignment gain comes from the loss function versus interactions with the modified architecture. An ablation training CFCE on the unmodified architecture (if feasible) or adapting the method to not require bias removal would strengthen the causal attribution of improvement to the loss.

### Minor
- **The M-invariance problem is demonstrated theoretically but not shown to degrade explanations on real models**: Theorem 3.2 is a clean theoretical result, and the redundancy ratio γ in Table 1 quantifies the magnitude of the spurious component. However, the paper does not show a concrete instance where HiResCAM produces a visibly misleading explanation on a standard CE-trained model that ContrastiveCAM corrects. Figure 1 is a schematic with hand-crafted numbers. A qualitative comparison on a real image would ground the theoretical motivation in empirical practice.

- **CFBCE is not defined in the main text**: The PASCAL VOC experiments (§5.3) use "CFBCE" without providing its definition; the reader is directed to Appendix B. Since this is one of the three main experimental settings, the core formulation should be summarized in the main text.

- **Large and unexplained standard deviations in some baselines**: On Oxford-IIIT Pets binary, CE w/ Arch has valid IoU of 39.07 ± 16.98; on PASCAL VOC, CE has valid IoU of 44.50 ± 16.57. The variance is orders of magnitude larger than CFCE/CFBCE's (e.g., CFBCE: 82.07 ± 0.91). This discrepancy warrants discussion — it may reflect genuine instability in the baselines or a methodological artifact.

- **Hyperparameter values (λ₁, λ₂, λ₃) not reported in the main text**: The KL regularization term (Definition 4.7) introduces three hyperparameters whose values are never specified in the main body, and no sensitivity analysis is provided. This makes it harder to assess how much tuning was required.

- **Accuracy cost not fully discussed**: CFCE incurs a non-trivial accuracy drop — on Hard-ImageNet: 93.69% (CE w/ Arch) → 90.53% (CFCE); on Pets multiclass: 94.41% (CE) → 92.96% (CFCE) → 90.08% (CFCE+KL). The paper acknowledges this ("at the cost of some un-ablated performance") but does not explore whether the trade-off can be tuned or whether the improved alignment compensates for the accuracy loss in practice.

### Trivial
- Table 1's "Core" and "Non-Core" values lack explicit units or formula definition in the main text, making cross-dataset comparisons hard to interpret without consulting the appendix.
- The PASCAL VOC segmentation transfer results are presented only as a bar chart without a numerical table, preventing precise comparison between methods.
- Computational cost (C−1 ContrastiveCAM computations per training step) is not discussed.

## Nice-to-Haves
- Computing ContrastiveCAM IoU for the CORM and DFR baselines (which use the unmodified architecture) would provide additional context, though the CE w/ Arch comparison already anchors the same-architecture evaluation.
- Demonstrating that the M-invariance problem produces misleading HiResCAM explanations on a standard (non-CFCE) trained model would strengthen the motivational narrative.
- Discussing the accuracy–alignment trade-off and whether it can be controlled (e.g., via λ tuning or loss weighting).

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"ContrastiveCAM IoU is not reported for any baseline"** — REMOVED as factually incorrect. Table 2 reports Contrastive-CAM IoU for the CE w/ Arch baseline at 30.27 ± 0.39, providing a direct same-architecture comparison. The other baselines (CORM, DFR, CORM+DFR) use the unmodified architecture, making ContrastiveCAM IoU not directly comparable, but CE w/ Arch is a valid baseline and its ContrastiveCAM IoU is reported.
- **"The paper never evaluates faithfulness of ContrastiveCAM against HiResCAM on standard models" with implication that the abstract's claim is unsupported** — REMOVED. The abstract's claim that ContrastiveCAMs are "more faithful" refers to their theoretical M-invariance property (Theorem 3.5), which is rigorously proven. The empirical evaluation tests whether ContrastiveCAMs, when integrated into training via CFCE, improve feature alignment — a different but related claim.
- **"Circularity: ContrastiveCAM IoU is circular because CFCE is defined in terms of ContrastiveCAMs"** — REMOVED. CFCE does not optimize ContrastiveCAM IoU; it penalizes non-core contributions. The IoU improvement from 30.27% (CE w/ Arch, which doesn't use ContrastiveCAMs in its loss) to 89.22% (CFCE) on the same architecture is a fair comparison. Moreover, the GradCAM IoU and model-agnostic ablation metrics provide independent corroboration.
- **"Scale-sensitivity argument — Core and Non-Core values have no units" as a major criticism** — DEMOTED to trivial. This is a clarity issue, not an evidential gap.
- **"Segmentation transfer results as bar chart only" as evidence that the paper is incomplete** — DEMOTED to trivial. The bar chart conveys the comparative pattern clearly; numerical values would be helpful but their absence doesn't undermine the core claim.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add an ablation that isolates the architectural modifications' effect — e.g., train CFCE on the unmodified architecture (if the bias can be handled differently), or train the modified architecture with a simpler non-core penalty that doesn't depend on ContrastiveCAMs, to confirm the loss function itself drives the improvement.
- Report λ₁, λ₂, λ₃ values and a brief sensitivity analysis to give readers a sense of tuning difficulty.
- Discuss the large baseline variance (especially CE w/ Arch on Pets, CE on PASCAL VOC) — is this due to seed sensitivity, metric instability, or something else?
- Define CFBCE explicitly in the main text or note that it is the binary/multilabel analog of CFCE as detailed in Appendix B.

## Score and Decision

### Calibration anchors

**Round 1 (bracketing):**
- wZiH43e5Ah (3.00) — CAN concept extraction — clearly below current paper; weaker theory and evaluation
- WYsLU5TEEo (2.50) — Counterfactual GAN images — clearly below; less rigorous
- FTSUDBM6lu (2.50) — Patch Ranking Map — clearly below; narrower scope
- FHQDCQFD8y (3.00) — Grad-TopoCAM for EEG — clearly below; domain-specific
- Tj3xLVuE9f (6.80) — Shortcut Learning foundations — comparable; broader theory but no practical fix
- bkdWThqE6q (6.00) — Interpretable Transformer — current paper stronger; better theory
- mKGXdsq7fD (4.33) — Pixel-level XAI evaluation — current paper clearly stronger
- U7VW3KBm34 (6.00) — SRD explanations — current paper stronger; more comprehensive evaluation
- 5Ca9sSzuDp (8.00) — CLIP interpretability — clearly above current paper; broader impact
- 25kAzqzTrz (8.00) — FixMatch theory — clearly above; more foundational contribution
- uHLgDEgiS5 (8.00) — Training data influence — clearly above
- 2dnO3LLiJ1 (8.00) — ViT registers — clearly above; field-shaping impact

**Round 2 (narrowing):**
- bkdWThqE6q (6.00) — Interpretable Transformer — current paper stronger
- 57NfyYxh5f (6.25) — How to Probe — current paper stronger; more theoretical depth
- Tj3xLVuE9f (6.80) — Shortcut Learning — comparable; current paper more applied with practical fix
- U7VW3KBm34 (6.00) — SRD — current paper stronger
- OZWHYyfPwY (7.00) — Feature visualization unreliability — comparable but slightly above; deeper theoretical framework
- GjfIZan5jN (7.33) — Representation classifiability — clearly above current paper
- Q95MaWfF4e (7.00) — Pattern-based CAVs — comparable pattern (theory→fix→evaluation); current paper has broader experiments but slightly less polished contribution
- khuIvzxPRp (6.80) — CLIP adversarial fine-tuning — comparable

**Bracket:** 6.0–7.5 (Round 1) → narrowed to **6.5** (Round 2). The paper is comparable to Tj3xLVuE9f (6.80) and Q95MaWfF4e (7.00) in the identify-limitation→propose-fix pattern, with cleaner theory than Tj3xLVuE9f but a less polished contribution than Q95MaWfF4e. The architectural confound and missing hyperparameters pull it below 7.0, but the strong empirical results and theoretical depth keep it well above 6.0.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>