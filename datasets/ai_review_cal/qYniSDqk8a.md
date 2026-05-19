- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3
Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper tackles the problem of inconsistent body shapes predicted across frames by standard HME models. It introduces A2B, a learned model (SVR or small NN) that converts 36 anthropometric measurements into SMPL-X body shape (β) parameters — claimed as the first such conversion. The paper further proposes a full pipeline combining a finetuned sequence-based 3D HPE model (UU) with inverse kinematics (IK) and A2B to generate meshes with consistent body shapes and accurate poses. Evaluations on ASPset and fit3D show that replacing HME model shape estimates with A2B predictions (derived from pseudo-GT measurements) improves MPJPE by 2–11mm across all tested models, and the full pipeline (UU+IK+A2B) achieves an MPJPE of 55.14mm on ASPset compared to SMPLer-X's 86.02mm.

---

## Strengths

- **First model to map anthropometric measurements to SMPL-X shape parameters.** Section 4.3 and Table 2 show the SVR trained on uniformly-sampled extended data achieves an anthropometric reconstruction error of only 0.082 mm (male) and 0.136 mm (female) on the AGORA test set. This enables explicit control over body shape via human-interpretable measurements.

- **Reveals and quantifies shape inconsistencies in widely-used GT datasets.** Section 3 and Table 1 show that for ASPset, the relative range of forearm measurements for a single person reaches 92%, and fit3D's β-parameter standard deviation per person averages 0.65. This is a concrete, empirically-grounded finding that the paper uses to motivate its approach.

- **Replacing HME model shape parameters with A2B predictions from pseudo-GT measurements improves all tested HME models.** Table 3 shows consistent MPJPE reductions: SMPLer-X from 86.02 to 78.38 mm, OSX from 92.34 to 89.28 mm, and Multi-HMR from 102.54 to 99.28 mm on ASPset. The body height standard deviation (σ) drops to zero, directly solving the shape inconsistency problem while also improving pose accuracy.

- **The full pipeline (finetuned HPE + IK + A2B) achieves mesh results that substantially exceed off-the-shelf HME models on challenging sports data.** Table 5 reports IK-UU+A2B at 55.14 mm (ASPset) and 37.46 mm (fit3D), versus 86.02 mm and 72.87 mm for the best compared HME models. This demonstrates the practical viability of decoupling pose estimation from shape estimation using a sequence-based 3D HPE backbone.

---

## Weaknesses

### Fatal
None.

### Major

- **The main evaluation uses pseudo-GT (perfect) anthropometric measurements, not realistic noisy measurements. The practical scenario — where a person takes measurements with finite precision — is never tested.** The paper states "we do not have access to the athletes to measure their anthropometric values. Therefore, we use the ground truth" (Sec. 5, line 153). All results in Tables 3 and 5 that show large improvements (2–11 mm on HME models, 12 mm on IK-UU) rely on measurements derived from clean GT shapes or poses. The paper's central motivation — that measuring a person once (like tailors do) yields superior meshes — is not tested under any realistic noise or measurement-error condition. This is a structural gap between the claimed ease-of-use and what is actually evaluated.

- **The headline improvement over HME models (30+ mm on ASPset) is largely driven by the finetuned 3D HPE model (UU), not the novel A2B component, and the comparison with off-the-shelf HME models conflates multiple sources of gain.** UU is finetuned on the training splits of ASPset/fit3D (Sec. 5.2, line 219), while the HME baselines (SMPLer-X, OSX, Multi-HMR) are used off-the-shelf — except for SMPLer-X which is omitted from fit3D because it was already trained on that dataset (Sec. 5.1, line 162). UU alone (stick-figure pose, 63.85 mm) already beats SMPLer-X (86.02 mm) on ASPset. The fairer evaluation (Table 3: A2B shapes dropped into existing HME models without changing the pose estimator) shows more modest improvements of 2–11 mm. The paper's abstract and conclusion do not sufficiently demarcate what the A2B model contributes versus what the overall system architecture contributes.

- **On fit3D, using A2B with GT measurements degrades MPJPE relative to inconsistent original shapes (37.46 mm vs 36.89 mm), and the paper's own GT analysis (Sec. 3) shows the ground truth is inconsistent (β stddev = 0.65).** The paper acknowledges this (line 243: "inconsistent shapes in the GT are likely to cause this behavior") but continues to use MPJPE against the flawed GT as the primary metric without correction or pose-only evaluation. This makes the fit3D quantitative conclusions unreliable — a consistently-shaped mesh may genuinely be more accurate yet score worse against inconsistent GT. The paper should either recompute per-person average GT shapes as targets, or report pose error after Procrustus alignment to factor out shape.

### Minor

- **When GT measurements are unavailable and median model-derived measurements are used instead (the realistic non-GT scenario), A2B yields only marginal improvements over simply using median β parameters directly.** Tables 4 and 5 (row 3) show improvements typically <1 mm, and sometimes the A2B variant is worse. The paper acknowledges this (line 212: "using our A2B models increases the performance slightly") but does not discuss the practical implications: if you need GT-quality measurements to get substantial gains, the method's applicability is limited to settings where accurate anthropometric measurements are already available.

- **The IK step introduces a 4 mm (ASPset) to 8 mm (fit3D) degradation from UU's pose accuracy (Table 5, rows 1–2), which is not ablated or analyzed.** The paper states that "incorporating a clearly defined mesh helps fix some typical errors of UU" (line 242) when A2B is added, but the net improvement from UU (63.85) to IK-UU+A2B (55.14) on ASPset conflates the cost of IK with the benefit of consistent shapes. The degradation is not separately analyzed.

- **On fit3D, the UU-based pipeline significantly outperforms HME models in MPJPE (29.60 mm vs 72.87 mm), but the paper does not clarify whether the HME models' poor scores are due to shape issues, pose issues, or joint regressor differences.** The evaluation asymmetry (finetuned UU vs off-the-shelf HME models) makes it hard to attribute the gap.

### Trivial

- In Table 5, the row for "IK-UU" with "GT" measurements on fit3D shows a dashed entry ("-") for median, but the narrative would benefit from noting explicitly that median is inapplicable here since GT measurements are used directly.

---

## Nice-to-Haves

- **Synthetic noise experiments**: Adding ±1–2 cm noise to the anthropometric measurements would directly probe the method's robustness. If A2B degrades gracefully under noise, the practical claim would be substantially strengthened.
- **Finetuned HME baselines**: Finetuning an HME model (e.g., SMPLer-X) on the same training splits used for UU would isolate the contribution of the A2B+IK approach from the benefit of dataset-specific finetuning.
- **Pose-only or shape-corrected metrics**: Reporting MPJPE after aligning per-frame shapes (e.g., Procrustes-aligned MPJPE, or reconstructing with per-person average GT shapes) would make fit3D results interpretable even given the GT inconsistency.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"IK-UU with median row is missing"** — The paper's Table 5 DOES include a median column showing values (67.16 for ASPset, 38.29 for fit3D). The critic was mistaken.
- **"No baseline for shape consistency (averaging β estimates)"** — The paper explicitly compares against median β in Tables 4 and 5. This baseline exists.
- **"Code is anonymous; cannot verify implementation"** — Code anonymization is standard for double-blind review. Removed per hard rules.
- **"Missing frames are omitted from MPJPE"** — The paper reports missing-frame rates for all compared methods. This is standard practice.
- **Various formatting and reproducibility nitpicks** — Removed per hard rules (trivial formatting, parser artifacts, etc.).

---

## Novel Insights

The two-reviewer synthesis surfaces an important tension that the paper itself does not fully resolve: the method's two evaluation regimes (pseudo-GT measurements vs. model-derived median measurements) paint very different pictures of its practical value. In the pseudo-GT regime, improvements are clear and sometimes large (12 mm on IK-UU+ASPset). In the median-derived regime, improvements are marginal (<1 mm) and sometimes negative. This bifurcation suggests that the A2B model's real value depends almost entirely on having access to high-quality, low-noise anthropometric measurements — but the paper never characterizes this dependency. A systematic sensitivity analysis (varying measurement noise, number of measurements available) would reveal whether the method is broadly useful or requires near-perfect inputs. This dependency on input quality, rather than on the finetuning asymmetry or the fit3D metric issue, is arguably the deepest open question about the work.

---

## Suggestions

1. Add a robustness experiment with synthetic noise on the anthropometric measurements to validate the practical claim.
2. Finetune at least one HME model (e.g., SMPLer-X using LoRA or full finetuning) on the same training splits to enable a fairer system-level comparison.
3. Report shape-corrected metrics on fit3D (e.g., compute per-person average GT shapes and use those as targets for MPJPE, or report pose error after Procrustes alignment).
4. More crisply separate what A2B contributes vs. what the full system contributes, both in the abstract and in the conclusion.

---
