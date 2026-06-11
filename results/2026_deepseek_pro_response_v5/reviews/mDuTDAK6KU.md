Now I have a clear picture. Let me synthesize everything and write the final review.

**Bracket analysis:**

- Round 1 placed KOALA between ~3.0 (the "Detecting Adversarial Examples" paper at 3.00 — similar evaluation gaps but weaker theory) and ~4.67 (REAL — a more comprehensively evaluated defense).
- Round 2 narrowed this: the closest comparator is "Multi-Task Consistency-based Detection of Adversarial Attacks" at 3.75, which shares KOALA's disagreement-based detection concept and evaluation gaps. KOALA is roughly comparable — it has a stronger theoretical contribution (formal proof) and more attack types, but also has unique issues (inflated detection metrics, CLIP results contradicting the central claim). KOALA is somewhat better than "Detecting Adversarial Examples" (3.00) and roughly on par with, or slightly below, the Multi-Task paper (3.75) given the metric inflation problem.

Applying the hint to lower by 1–2 points for <5 papers to counteract overestimation: **final score 3.5**.

---

## Summary
KOALA proposes an adversarial detector based on disagreement between two complementary nearest-prototype classifiers — one using KL divergence (sensitive to dense, low-amplitude perturbations) and one using an L0-based metric (sensitive to sparse, high-impact changes). The paper provides a theoretical proof that under sufficient inter-class prototype separation, no single bounded perturbation can simultaneously flip both metrics' predictions, guaranteeing detection. Training requires only clean-image fine-tuning. Experiments on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet evaluate detection and adversarial accuracy under PGD, CW, and AutoAttack.

## Strengths
- **Formal theoretical guarantee (Theorem 1):** The paper proves that under Assumptions A1–A4, when a sufficient coordinate-wise gap exists between class prototypes, no perturbation with bounded norm can simultaneously flip both the KL and L0 predictions to the adversarial class. The proof sketch (Section 3.2) decomposes into three clear propositions (necessary conditions for KL flip, L0 flip, and their incompatibility), giving the argument a logical, auditable structure distinct from purely empirical detectors.
- **Clean-only fine-tuning (no adversarial training):** KOALA's composite loss (Eq. 6, Section 3.3) is trained exclusively on clean images. On ResNet/CIFAR-10, the KL+L0 fine-tuned model achieves 57.32% adversarial accuracy under PGD ℓ∞²/²⁵⁵ versus 45.5% for the baseline, while maintaining 94.78% clean accuracy (vs. 95.16% baseline). This makes the approach lightweight and attack-agnostic.
- **Ablation confirms metric complementarity on ResNet (Table 2):** On ResNet/CIFAR-10, KL+L0 achieves Accuracy 0.88, Precision 0.94, Recall 0.81, F1 0.87 at ε=2/255, versus the next-best (KL+Cosine) at 0.78/0.92/0.62/0.74. The consistent margin supports the claim that KL and L0 are complementary for detection on this architecture.
- **Multi-attack evaluation:** The method is tested against PGD, CW, and AutoAttack at two perturbation budgets (ε=2/255 and 4/255) on both architectures, going beyond a single attack type.

## Weaknesses

### Fatal
None.

### Major
- **No comparison to any existing adversarial detector:** All experiments compare KOALA against ablated variants of itself (KL+Cosine, L0+Cosine, KL+L0+Cosine) but never against any published detector — not LID (Ma et al., 2018), Mahalanobis (Lee et al., 2018), feature squeezing (Xu et al., 2018), MagNet (Meng & Chen, 2017), NIC (Ma & Liu, 2019), or any of the methods discussed in the related work (Section 2). The ablation study tells us KL+L0 works better than KL+Cosine within KOALA's framework but tells us nothing about whether KOALA is competitive with existing approaches. For a paper whose primary contribution is a new detection method, this makes it impossible to assess whether the contribution is significant.

- **TP metric definition inflates detection metrics (Section 4.2, line 188):** The confusion matrix defines a True Positive for an attacked input (a=1) as including the disjunct (â,ŷ)=(0,y*) — meaning an undetected adversarial example that happens to be classified correctly counts as a detection success. This inflates the reported Precision and Recall by giving the detector credit for attacks it failed to flag. Standard detection evaluation would define TP strictly as attacks that are flagged. This affects all detection metrics reported in Tables 1 and 2.

- **CLIP results contradict the central claim that KL+L0 is the superior combination (Table 4):** On CLIP/Tiny-ImageNet, L0-only fine-tuning achieves 25.43% adversarial accuracy under AutoAttack ε=2/255 and 37.49% under CW ε=2/255, substantially outperforming KL+L0 (16.18% and 11.91%, respectively). KL-only also outperforms KL+L0 on several metrics. The Table 4 caption erroneously states "The KL+L0 objective demonstrates superior adversarial accuracy" — this is factually incorrect for CLIP. The post-hoc explanation (lines 274–277) about CLIP's pre-training was not hypothesized before seeing results and undermines the claimed universality of the KL+L0 combination.

### Minor
- **No empirical adaptive attack evaluation:** The paper criticizes prior detectors for degrading under adaptive attacks (Section 2, lines 44, 48) and claims its theoretical proof addresses this. While Theorem 1 provides a norm-bounded guarantee regardless of attack generation method, an adaptive attacker could target samples that do not satisfy the coordinate-gap condition (~90% of CLIP/Tiny-ImageNet samples, per Table 1) or craft perturbations to induce false positives on benign inputs (not covered by the theorem). Empirical testing against detector-aware attacks would strengthen the security claim.

- **Theorem scope is narrow; abstract overstates the guarantee:** Table 1 shows only ~10% of CLIP/Tiny-ImageNet samples satisfy the theorem's coordinate-gap condition. On non-compliant samples, F1 drops to 0.53–0.72. The abstract's "formal proof of correctness" does not convey this limitation. Additionally, the paper does not specify how the Theorem-Compliant split is operationalized (what is the exact value of Γᵢ(ε) used?).

- **Experiment 1 is partially tautological:** Perfect scores (1.0) on Theorem-compliant samples essentially confirm the theorem was applied correctly but do not provide independent evidence for KOALA's effectiveness. The more informative result — how performance degrades near the boundary of the condition — is not explored.

- **Threshold τ is underexplored:** The theorem claims "we can always find a threshold τ" but τ=0.75 is fixed in all experiments. Sensitivity to τ is never analyzed.

- **Adversarial accuracy protocol underspecified (Experiment 3):** Line 236 defines adversarial accuracy as "performance on successfully attacked images that were not detected," but for the baseline model (which has no detector), there is no notion of "not detected." It is unclear whether this metric is computed comparably across all rows in Tables 3 and 4.

### Trivial
- Table 4 caption incorrectly claims KL+L0 is superior on CLIP (it is not; L0-only and KL-only outperform it). This appears to be a copy-paste error from Table 3.

## Nice-to-Haves
- The evaluation scope is limited to two datasets (CIFAR-10, Tiny-ImageNet), two architectures (ResNet-18, CLIP ViT-B/32), and only ℓ∞ attacks. ℓ₂ attacks would be a natural addition given the theory is framed around ℓ₂-bounded perturbations.
- The paper conflates two distinct contributions — the KOALA detector (disagreement-based detection) and the fine-tuning procedure (composite loss training). An experiment applying the fine-tuned backbone with a standard single-metric nearest-prototype classifier (no detection) would isolate whether robustness gains come from the detection mechanism or from the fine-tuning alone.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic: "Proposition 2 assumes linear approximation to KL divergence" and "L0 metric threshold creates circularity for theoretical analysis."** REMOVED — both points speculate about gaps in a proof whose full version is in the stripped appendix. Per the hard rules, speculative claims about stripped appendix content are removed.
- **Harsh Critic: "KL divergence forces softmax normalization — unusual and restrictive design choice."** REMOVED — this is a design choice explicitly acknowledged as Assumption A1, not a flaw. The paper is transparent about this requirement.
- **Strength Finder: "Clean, plug-and-play architecture."** REMOVED — generic praise without specific evidence distinguishing it from other plug-and-play methods.
- **Strength Finder: "Direct empirical validation of the theorem (Table 1)" as a separate strength.** Merged into the theoretical guarantee discussion; the verification is partially tautological (see Minor weakness).

## Novel Insights
The paper's observation that two complementary distance metrics (distribution-sensitive KL and sparsity-sensitive L0) can be paired to create mutually exclusive prediction stability bands is genuinely novel. The theoretical framing that dense and sparse perturbations stress fundamentally different geometric properties of the feature space — and that this can be exploited for guaranteed detection — represents a fresh perspective in adversarial detection beyond the standard statistical-deviation or semantic-consistency paradigms.

## Suggestions
- Add comparisons to at least 2–3 representative detectors (LID, Mahalanobis, feature squeezing) on the same datasets and attack budgets. This is essential for establishing KOALA's competitiveness.
- Revise the TP metric definition to use standard detection evaluation: TP = attack flagged (â=1), FP = benign flagged, independent of classification correctness. Report classification accuracy as a separate axis.
- Either redesign KOALA to handle the CLIP regime or clearly characterize the conditions under which KL+L0 works (e.g., models trained from scratch vs. contrastive pre-training). The current paper claims universality but the data shows otherwise.
- Test against adaptive attacks that explicitly try to force agreement between the two metrics (e.g., multi-objective PGD minimizing both KL and L0 distances to a target class simultaneously).
- Analyze sensitivity to τ and specify how the Theorem-Compliant split is operationalized.

## Score and Decision

**Calibration anchors retrieved:**

Round 1:
- MV5j4Qpq7N (2.33) — jailbreak defense; clearly worse than KOALA
- lEsNGN1SjG (2.00) — bias classifier defense; clearly worse
- qx07JhIs8E (2.33) — TRADES analysis; different topic, clearly worse
- 4Hf5pbk74h (2.33) — nearest neighbor decision boundaries; clearly worse
- KAWlH5pfQu (3.00) — "Detecting Adversarial Examples"; similar gaps, weaker theory; KOALA is better
- kz78RIVL7G (2.60) — compressive sensing detection; weaker than KOALA
- AHqXvTK4KG (3.50) — diffusion detection/purification; roughly comparable
- EWP9BVRRbA (4.00) — VLM adversarial detection; somewhat stronger evaluation
- Oi6BhzIu7R (4.67) — REAL test-time defense; stronger evaluation, KOALA is weaker
- R1crLHQ4kf (5.00) — audio adversarial detection; different domain, stronger
- RzdtpxL0H5 (6.20) — DDAD defense; clearly stronger, more comprehensive

Round 2:
- kz78RIVL7G (2.60) — already seen
- Trg9qb0d5U (3.67) — DNN classifier identification; different topic
- 4BYzyGKIcb (4.00) — sharpness-aware geometric defense; somewhat stronger evaluation
- adhxppqQAn (3.75) — **Multi-Task Consistency detection; closest match in methodology (disagreement-based detection); KOALA is comparable — stronger theory, more attacks, but has metric inflation and CLIP contradiction issues**
- 4ciEeIiIJ7 (3.83) — collective disagreement; different domain
- xdnoULh5Sv (4.00) — CARSO defense; stronger adaptive evaluation, KOALA is weaker

**Bracket:** Round 1 narrowed to 3.0–4.5. Round 2 narrowed to 3.0–4.0, with the Multi-Task Consistency paper (3.75) as the closest anchor. KOALA is comparable but with the additional metric-inflation issue. Applying the overestimation correction for <5 papers yields a final score of **3.5**.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>