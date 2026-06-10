## Summary
KOALA proposes a reactive adversarial example detector based on label disagreement between two nearest-prototype classifiers—one using KL divergence (sensitive to dense perturbations) and one using a thresholded L0-based measure (sensitive to sparse perturbations). The paper provides a formal proof (Theorem 1) that under sufficient inter-class prototype separation in feature space, no norm-bounded perturbation can simultaneously fool both classifiers. A lightweight clean-only fine-tuning procedure aligns backbone embeddings with both metrics. Experiments are conducted on ResNet-18/CIFAR-10 and CLIP ViT-B/32/Tiny-ImageNet.

## Strengths
- **Theory-to-empirics validation on compliant samples (Theorem 1 + Table 1):** Table 1 shows that on theorem-compliant samples, all detection metrics (accuracy, precision, recall, F1) are exactly 1.0 across all four settings (ResNet/CIFAR-10 and CLIP/Tiny-ImageNet at ε=2/255 and 4/255). This is a concrete, falsifiable prediction of the theory that experiments confirm—a meaningful advance over purely empirical detectors.
- **Effective KL+L0 combination validated by thorough ablation (Table 2):** On ResNet/CIFAR-10, KL+L0 achieves accuracy 0.88 and F1 0.87, substantially outperforming all other two- and three-metric combinations (next best: KL+Cosine at 0.78/0.74). The ablation tests all plausible pairings.
- **Clean-only fine-tuning yields meaningful adversarial robustness (Table 3):** KL+L0 fine-tuning on ResNet/CIFAR-10 achieves 57.32% adversarial accuracy under PGD ε=2/255 versus the 45.50% baseline—a 26% relative improvement—while preserving comparable clean accuracy (94.78% vs 95.16%).
- **Honest analysis of detection-robustness distinction on CLIP (Section 4.3):** The paper correctly attributes the high detection rate of KL+L0+Cosine on CLIP to the model becoming non-robust (adversarial accuracy drops to 14.93% in Table 4), demonstrating intellectual honesty.
- **Insightful analysis of Cosine's harmful interaction (Table 3 + Section 4.4):** Any objective including Cosine similarity yields lower adversarial robustness. The explanation that Cosine's angular alignment conflicts with KL and L0's per-dimension alignment shows careful thinking about metric interactions.

## Weaknesses

### Fatal
None.

### Major
- **No comparison to any existing adversarial detection method.** The related work section discusses MagNet, Mahalanobis, LID, NIC, CADet, feature squeezing, and Bayesian uncertainty, but the experiments compare only within KOALA's own framework (metric-pairing variants in Table 2, fine-tuning objectives in Tables 3/4). This makes it impossible to assess whether KOALA is competitive with existing detectors. A paper proposing a new detector must compare against existing detectors.

- **Non-standard confusion matrix conflates detection with robustness, making headline results misleading.** The TP definition (Section 4.2) counts an adversarial example as a "true positive" even when the detector fails to flag it, as long as the system correctly classifies it: TP := [a=1] ∧ [(â,ŷ)=(1,⊥) ∨ (â,ŷ)=(0, y*)]. Similarly, FP counts a clean sample as "false positive" if it is misclassified even when not flagged. The abstract reports "precision of 0.94 and recall of 0.81" using these system-level metrics, but Theorem 1 is a *detection* guarantee. The reader cannot separate detection performance from classification-under-attack performance.

- **The feature-space / input-space perturbation gap is not empirically bridged.** Assumption A2 assumes ||δ|| ≤ ε in embedding space, justified by "Lipschitz continuity of the backbone encoder" (Section 3.2). For deep networks the effective Lipschitz constant can be very large, meaning a small input-space ℓ∞ perturbation can map to a much larger embedding-space perturbation. The paper does not measure actual feature-space perturbation norms under PGD/CW/AutoAttack to verify they remain within ε, leaving the theorem's applicability to the experimental setup unsubstantiated beyond the compliant/non-compliant partition.

- **Theorem conditions met for only ~10% of CLIP/Tiny-ImageNet samples, limiting the guarantee's practical reach.** Table 1 shows only 510/5000 (~10%) of Tiny-ImageNet samples satisfy Theorem 1 at ε=2/255, vs 3345/5000 (~67%) for CIFAR-10. The overall CLIP system metrics (precision 0.66, recall 0.85 from Table 2) reflect behavior the theory does not explain. A "provably correct" detector whose proof covers 10% of its operating regime has limited practical value for that setup.

### Minor
- **"No architectural changes" claim is contradicted.** The abstract and intro claim "no architectural changes," but Section 3.1 states "KOALA replaces this conventional classifier head with a novel component" and Section 4.1 says "The final fully connected layer (classifier head) is removed." The backbone is preserved but the end-to-end architecture is changed.
- **"Semantics-free" claim is contradicted by the CLIP experimental setup.** The CLIP experiments use text-encoder prototypes ("a photo of [CLASS]" per Section 4.1), which is inherently semantic.
- **Missing adaptive attack evaluation.** An empirical evaluation against an attacker who specifically targets the detector (e.g., by optimizing to keep both KL and L0 predictions aligned) is standard in adversarial defense literature and is absent.
- **Overclaims on scope.** "Extensive experiments" describes two model-dataset pairs. "Plug-and-play solution for various data modalities" is unsupported—only image classification is tested, and fine-tuning the backbone encoder is required.
- **No sensitivity analysis for hyperparameters τ and ϕ.** The L0 metric uses τ=0.75 and ϕ=0.5 (Section 4.1) without justification or sensitivity analysis. Given that the theorem's applicability depends on τ (Prop. 4 in the proof sketch), this matters.

### Trivial
None.

## Nice-to-Haves
- Empirical measurement of feature-space perturbation norms under the evaluated attacks would substantially strengthen the theory-practice connection.
- Reporting standard detection metrics (TP=flagged attack, FP=false alarm on clean, FN=missed attack) alongside the system-level metrics.
- Evaluation on additional datasets (e.g., CIFAR-100) to strengthen generalizability claims.
- A limitations section discussing the theory-practice gap and the low CLIP compliance rate.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "No limitations section" — while notable, this is a presentation choice; many accepted papers lack one. Demoted to nice-to-have.
- Statistical reporting (no variance/confidence intervals) — single-run evaluation is common in this literature.
- L0 naming convention nitpick — the paper explains the metric clearly in Eq. 2; this is a style issue, not a substance issue.

## Novel Insights
The paper's most novel contribution is the empirical validation that KL+L0 complementary metric pairing demonstrates mutual exclusivity of stability bands, confirmed by Table 1's perfect 100% detection on compliant samples across all four experimental settings. The finding that Cosine similarity actively harms robustness when combined with KL+L0 (Table 3) provides useful guidance for metric-learning-for-robustness. The CLIP analysis (L0 alone is best for robustness due to CLIP's pre-existing sparsity-aware structure, Section 4.4) reveals that pre-training history matters for metric combination effectiveness—a nuance worth further investigation.

## Suggestions
- Add 2–3 detection baselines (Mahalanobis, MagNet, LID) evaluated on the same setup.
- Report standard detection confusion matrices separately from system-level metrics.
- Measure and report the ℓ2 norms of feature-space perturbations under PGD/CW/AutoAttack.
- Revise "no architectural changes" to "backbone architecture preserved."
- Qualify "semantics-free" for the CLIP setup or rerun with image-derived prototypes.
- Add sensitivity analysis for τ and ϕ.

---

## Calibration Report

### Round 1 — Bracketing (3 queries)

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Detecting Adversarial Examples (layer regression) | KAWlH5pfQu | 3.00 | R1 | KOALA is clearly stronger: formal proofs, better experiments, two datasets |
| Statistical attack-agnostic detection | kz78RIVL7G | 2.60 | R1 | KOALA much stronger |
| Information-theoretically safe bias classifier | lEsNGN1SjG | 2.00 | R1 | KOALA much stronger |
| Efficient Adversarial Detection with Diffusion | AHqXvTK4KG | 3.50 | R1 | KOALA stronger: formal guarantees, better theoretical grounding |
| Randomized Feature Squeezing (clean training) | kfYM5lBzB6 | 4.75 | R1 | Similar clean-only training idea; KOALA has formal proofs and better ablation, but similar evaluation gaps (no adaptive attacks) |
| REAL: Rectified Adversarial Sample | Oi6BhzIu7R | 4.67 | R1 | KOALA stronger: formal guarantees, more thorough experiments |
| CleanerCLIP backdoor defense | pA8oI8a00l | 4.25 | R1 | Different domain; KOALA stronger on theoretical contribution |
| Prototype-based Optimal Transport for OOD | J2we1sVd9m | 4.60 | R1 | KOALA stronger: adversarial focus with formal guarantees |
| Adversarial Attacks as Near-Zero Eigenvalues | YmQyEdLIkU | 5.50 | R1 | Similar theoretical ambition; KOALA has much better experiments (2 setups vs MNIST only) |
| DDAD: Two-Pronged Adversarial Defense | RzdtpxL0H5 | 6.20 | R1 | DDAD has proper baselines and comprehensive evaluation; KOALA has stronger formal guarantee but worse evaluation completeness |
| GNN robustness from OOD perspective | DCD918ZkI | 5.75 | R1 | Has adaptive attack evaluation; KOALA has formal proofs but less complete evaluation |
| DUCAT: New Paradigm of Adversarial Training | sBpYRQOrMn | 5.75 | R1 | Better baselines but weaker theoretical contribution than KOALA |
| Anomaly Detection via Tabular Data Distribution | 7QDIFrtAsB | 5.75 | R1 | Different domain; less comparable |
| GNNCert: Deterministic Certification | IGzaH538fz | 8.00 | R1 | Much stronger: deterministic guarantees, 8 datasets, SOTA comparisons. KOALA is well below. |
| Robustness Reprogramming for Representation | SuH5SdOXpe | 7.50 | R1 | Much stronger and more complete contribution. KOALA below. |
| Robust Classification via Single Diffusion | I5lcjmFmlc | 8.00 | R1 | Stronger contribution overall. KOALA below. |
| Vulnerability of Adversarially Trained Models | mXpNp8MMr5 | 7.33 | R1 | Stronger paper with novel threat model. KOALA below. |

**Round 1 bracket: 4.5–6.5.** KOALA is clearly above the weak detection papers (3.0–4.75) due to its formal proofs and better experiments, but below papers with complete evaluation (DDAD at 6.2, GNNCert at 8.0).

### Round 2 — Narrowing (2 queries)

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Randomized Feature Squeezing | kfYM5lBzB6 | 4.75 | R2 | KOALA has stronger theory; similar evaluation gaps. KOALA above. |
| REAL: Rectified Adversarial Sample | Oi6BhzIu7R | 4.67 | R2 | KOALA clearly above. |
| CleanerCLIP | pA8oI8a00l | 4.25 | R2 | KOALA above. |
| Prototype-based OT for OOD | J2we1sVd9m | 4.60 | R2 | KOALA above. |
| DDAD | RzdtpxL0H5 | 6.20 | R2 | DDAD has better evaluation; KOALA has stronger formal guarantee. Close — KOALA slightly below. |
| DUCAT | sBpYRQOrMn | 5.75 | R2 | KOALA has stronger theoretical novelty; DUCAT has better baselines. Comparable. |
| GNN robustness OOD | DCD918ZkI | 5.75 | R2 | KOALA has formal proofs but less evaluation. Comparable. |
| Contrastive Teacher-Student for Novelty | FR2WQcwjG4 | 5.60 | R2 | Less comparable domain. |

**Round 2 assessment:** KOALA is clearly above the 4.5–5.0 anchors and slightly below DDAD (6.2). It is comparable to DUCAT (5.75) and GNN robustness (5.75). KOALA's theoretical contribution is stronger than both, but its evaluation is less complete. The formal proof with 100% detection on compliant samples is a genuine differentiator that pushes it slightly above 5.5, but the four major weaknesses (no baselines, conflated metrics, unbridged theory-practice gap, low CLIP compliance) prevent it from reaching 6.0.

**Final score: 5.5.** This positions KOALA above the 4.75 anchors (which had comparable evaluation gaps but no formal guarantees) and at parity with the 5.5–5.75 anchors (which had similar theoretical ambition). The formal proof is a genuine novelty that could merit a higher score with the evaluation issues addressed.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>