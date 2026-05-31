Now I have all the information needed for calibration. Let me synthesize my analysis.

**Round 1 Bracket:** Based on the anchors, this paper sits between the 4.40 (weak hyperbolic optimization paper) and 6.00 (strong hyperbolic CNN paper) anchors. The most comparable papers are ekz1hN5QNh (HCNN-Lorentz, 6.00) and bwOndfohRK (Symmetric Spaces, 6.00), which share similar theoretical contribution types. The paper is clearly above 4.40 (WOopKWDWtS) since it has proper theorems and proofs rather than just empirical modifications. My initial bracket: **5.0 - 6.5**.

**Round 2 Narrowing:** The close-in anchors are ekz1hN5QNh (6.00), bwOndfohRK (6.00), MEnPLXJNng (4.75), and 30aSE3FB3L (5.67). Comparing:

- The PVNN paper is slightly weaker than ekz1hN5QNh (6.00) because: (a) the gradient comparison methodology issue is not present in that anchor, and (b) some components (convolution, activation) are less developed. But PVNN has more comprehensive ablations and more diverse task evaluation.
- The PVNN paper is comparable to 30aSE3FB3L (5.67) — both provide a complete toolkit for a specific geometry with similar experimental breadth.
- The PVNN paper is clearly stronger than MEnPLXJNng (4.75) which had weaker experiments and less well-grounded theory.

Final score: **5.5** — a solid contribution with some methodological concerns in the numerical stability evaluation and marginal empirical gains that prevent it from reaching the 6.0 level of the strongest comparable anchors.

Now let me write the final review.## Summary

This paper introduces Proper Velocity (PV) Neural Networks, leveraging the PV model — an unconstrained representation of hyperbolic space rooted in special relativity — as an alternative to the constrained Poincaré ball and hyperboloid (Lorentz) models. The authors establish the complete Riemannian geometry toolkit for PV space (exponential/logarithmic maps, parallel transport, geodesic distance), derive core neural layers (MLR, FC, convolution, activation, batch normalization), and evaluate on numerical stability, image classification, graph node classification, and genomic sequence learning. The key selling point is that PV's unconstrained nature offers better numerical stability while remaining isometric to the Poincaré ball.

## Strengths

- **First complete Riemannian toolkit for the PV model (Theorem 4.3):** The paper derives closed-form expressions for the exponential map, logarithmic map, parallel transport, and geodesic distance on PV space. This is the core theoretical contribution and foundation for all downstream neural layers. The isometry with the Poincaré ball (Theorem 4.2) provides a clean theoretical grounding.

- **Efficient PV MLR formulation (Theorem 5.2):** The PV MLR score reduces to a simple expression involving inner products ⟨x, z_k⟩, avoiding costly per-class gyroaddition and enabling efficient minibatch computation via matrix multiplication. This directly addresses practical efficiency concerns that plague naive hyperbolic MLR formulations.

- **Demonstrated numerical stability advantages:** PV achieves a round-trip error of 2.1×10⁻⁷ vs. 2.1×10⁻⁴ (Poincaré) and 1.0×10⁰ (hyperboloid) in FP32 (Table 2). The gradient magnitudes remain in a stable band [1.1×10⁻⁴, 2.1×10⁻⁶] across varying radii, while alternatives exhibit vanishing (10⁻¹¹–10⁻¹³) or exploding/NaN gradients (Table 3). PV also maintains zero failure rate up to r=1000 in FP32 while the hyperboloid model fails catastrophically (Table 1).

- **Competitive performance across diverse tasks:** PVNN achieves strong results on graph learning (97.96% on Airport vs. 92.10% for KNN, +5.86%), genomic sequence learning (81.83% vs. 76.12% on LINEs), and matches or slightly exceeds baselines on image classification. The experiments span four distinct modalities, demonstrating broad applicability.

- **Rigorous theoretical grounding for PV GyroBN (Theorem 5.4):** The paper proves homogeneity of Fréchet mean and dispersion under the PV GyroBN operations, providing principled guarantees that centering and scaling behave as intended.

- **Comprehensive ablation studies (Tables 6–9):** The paper systematically tests tangent-space vs. Riemannian FC/normalization, the effect of Exp₀ for input embedding, different activation strategies, and computational cost of Fréchet mean iterations. These ablations help isolate the contribution of each design choice.

## Weaknesses

### Major

- **The gradient magnitude comparison (Table 3) does not fully account for differences in the underlying Riemannian metric.** The norm ‖∇_x f_r(x)‖ depends on the metric tensor, which differs substantially across models — especially near the Poincaré ball boundary vs. in unconstrained PV space. The paper provides no mathematical justification for comparing raw gradient norms across different geometries, so the claim that "PV maintains gradients in a safer band" lacks rigorous support. The qualitative pattern (PV avoids the extreme vanishing of Poincaré and the NaN/exploding of hyperboloid) is still informative, but the specific quantitative ranges should not be taken as directly comparable.

- **No statistical significance tests are reported anywhere.** The image classification results (Table 4) show margins of ≤0.24% (e.g., 95.30 vs. 95.12 on CIFAR-10) that fall within one standard deviation of the baselines. Without significance tests (e.g., paired t-tests, confidence intervals), the reader cannot assess whether these differences are meaningful or reflect random variation. This is especially important given that the paper's framing ("largest gains on CIFAR-100") implies a consistent advantage that the raw numbers do not clearly support.

### Minor

- **The gyro operator experiment (Table 1) shows PV and the Poincaré ball are tied on stability.** Both achieve 0% failure and 0% violation at all radii. The paper's framing ("PV maintains zero failures up to r=1000") could misleadingly imply an advantage, when the experiment primarily demonstrates PV > hyperboloid (where the hyperboloid fails badly). This is a presentation issue rather than a methodological one, but it should be acknowledged.

- **The ablation on Exp₀ (Table 8) shows differences ≤0.2% across all datasets.** This suggests the choice of input embedding (using the exponential map vs. treating Euclidean features directly as PV coordinates) is essentially irrelevant. While the paper acknowledges this, the near-identical performance partially undermines the claim that the PV geometry itself drives improvements, since the geometry can be bypassed entirely at the input stage with no cost.

- **The Euclidean activation variant (Table 9) catastrophically degrades on Cora (38.10% vs. 51–52% for other variants).** This is a 14+ point drop that the paper documents but does not explain. Understanding why direct PV-space activation fails so dramatically on one dataset would help users of PVNNs avoid similar pitfalls.

- **No curvature sensitivity analysis or discussion.** All experiments use a fixed curvature K=-1. In practice, optimal curvature depends on the dataset's hierarchical structure. The paper does not study whether PVNNs benefit from learnable or tuned curvature, nor does it discuss this as a limitation.

- **The PV convolution section (Section 5.3) is brief and underspecified.** The definition relies on "standard Euclidean concatenation" because "PV space is unconstrained," and the convolution itself reduces to applying the PV FC layer to concatenated inputs. While this is arguably valid given PV's coordinate representation, it means the "PV convolution" does not actually operate geometrically on the manifold — it operates in the ambient Euclidean coordinates and uses the FC layer to map back to PV space. This contrasts with more geometrically principled convolutions in the Lorentz model.

### Trivial

- None beyond the paper's own acknowledged future work and limitations.

## Nice-to-Haves

- A discussion of whether Euclidean or Riemannian optimizers (Adam, SGD) are used for PV parameters and why. If Euclidean optimization works directly on PV coordinates, this is a practical advantage worth highlighting.
- A failure-case analysis showing a concrete training scenario where Poincaré or hyperboloid models underperform but PV succeeds, rather than the current synthetic stability experiments.
- Computational cost comparison (wall-clock time, not just fit time per epoch) between PVNN and the best-performing baseline on each task.

## Removed Points

These points were raised in inputs but are removed with justifications:

- *"The round-trip error experiment fixes ‖v‖=10, which is unfair because it corresponds to different geodesic distances"* — **Removed.** The round-trip Log₀(Exp₀(v)) is identity regardless of geodesic distance; testing all models on the same tangent vector norm is a valid comparison of numerical implementation quality.
- *"HCNN-S is a weak variant; comparison is unfair"* — **Removed.** Speculation about the baseline variant without evidence.
- *"KNN baseline on Airport at 92.10% is unusually high"* — **Removed.** Speculation without evidence.
- *"PV concatenation is a conceptual error"* — **Removed.** The concatenation operates on Euclidean coordinates of PV space (which is ℝⁿ as a set), and the geometry is applied via the subsequent PV FC layer; this is a standard approach.
- *"Missing proofs in appendix"* — **Removed.** Parser strips appendix content; proofs exist in original submission.
- *"Missing reproducibility details / code not released"* — **Removed.** Parser strips supplementary; code release upon acceptance is standard.
- *"Theorem 4.3 lacks derivation, Theorem 5.2 needs verification"* — **Removed.** The paper states proofs are in App. E, which is stripped by the parser.
- *"The paper does not mention curvature as a tunable parameter"* — Demoted from Major to Minor (retained above as Minor).
- *"The hyperboloid violation rates suggest poor implementation rather than geometric issues"* — **Removed.** This conflates implementation quality with geometry; the experiment tests the model as it would be used in practice, which is a valid test.
- Various formatting, typo, and presentation nitpicks — **Removed** as parser artifacts or non-substantive.

## Novel Insights

None beyond the paper's own contributions. The main intellectual value is in recognizing that the PV model (from relativistic physics) has properties — particularly the unconstrained coordinate representation — that directly address known numerical stability problems in hyperbolic neural networks. This is a clean insight applied well.

## Suggestions

1. **Redesign the gradient comparison** to either normalize by the Riemannian metric or explicitly justify that the ambient Euclidean gradient norm is the correct quantity to compare across models. Even better: compare training dynamics (loss curves, gradient norms during actual training) in a controlled setup where only the hyperbolic model varies.
2. **Report statistical significance tests** (paired t-tests or bootstrap confidence intervals) for the main comparisons, especially Tables 4 and 5 where margins are small. This is standard practice when performance differences are narrow.
3. **Add a dedicated limitations section** acknowledging that: (a) image classification gains are within noise margins, (b) the convolution layer is essentially Euclidean concatenation + PV FC, (c) curvature is fixed with no sensitivity analysis, and (d) the gradient comparison has methodology limitations.
4. **Clarify optimizer choices** — state explicitly whether Euclidean optimizers (Adam, SGD) are used on PV coordinates, and if so, why this is justified. This is a potentially significant practical advantage over constrained models.
5. **Explain the Cora Euc. Act. failure** — why does applying activations directly in PV space cause a 14-point drop on Cora but not on other datasets? A hypothesis or analysis would greatly help future users.

---

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- `HDmmwwTIlf.md` — avg 2.50 — PDE solver paper, much weaker, not topically similar
- `SYiOxXWlKU.md` — avg 2.50 — Stiff ODEs PINN, weaker, not topically similar
- `R5FzCFR5yU.md` — avg 3.33 — Hybrid numerical PINN, weaker
- `b2FFWnwZxl.md` — avg 3.40 — Hyperbolic Vision Transformer (HVT), weaker experiments, marginal gains
- `bwOndfohRK.md` — avg 6.00 — Symmetric Spaces NN, comparable theoretical contribution, cleaner evaluation
- `WOopKWDWtS.md` — avg 4.40 — Hyperbolic deep learning optimization, weaker — fewer theorems, marginal gains
- `ekz1hN5QNh.md` — avg 6.00 — Fully Hyperbolic CNNs (Lorentz), most similar anchor — complete toolkit for a hyperbolic model, similar criticisms about marginal gains
- `MEnPLXJNng.md` — avg 4.75 — Riemannian Transformation Layers, weaker experimental validation
- `Xo0Q1N7CGk.md` — avg 8.00 — Grid cells / conformal isometry, stronger, different subfield
- `3i13Gev2hV.md` — avg 8.00 — Hyperbolic VL models, stronger, different subfield
- `EzjsoomYEb.md` — avg 8.00 — Topological deep learning, stronger, different subfield
- `JWtrk7mprJ.md` — avg 7.60 — Residual deep GPs on manifolds, stronger

**Round 2 (Narrowing):**
- `ekz1hN5QNh.md` — avg 6.00 — As above. **PVNN is slightly weaker**: gradient comparison methodology issue not present in this anchor, and some PVNN components (convolution, activation) are less developed. However PVNN has more diverse experiments and stronger ablations.
- `bwOndfohRK.md` — avg 6.00 — As above. **PVNN is comparable** in theoretical depth but weaker in empirical rigor.
- `EyWKb7Ltcx.md` — avg 5.00 — Intrinsic Riemannian Classifiers on SPD. Less similar topic.
- `MEnPLXJNng.md` — avg 4.75 — As above. **PVNN is clearly stronger** — better theoretical grounding, more experiments.
- `30aSE3FB3L.md` — avg 5.67 — Matrix Manifold NN++. **PVNN is comparable** — similar mix of theoretical derivation + empirical evaluation with mixed results.
- `xhCZD9hiiA.md` — avg 6.00 — Batch Normalization theory. Different topic.

**Round 1 bracket:** [5.0, 6.5]

**Score determination:** The PVNN paper is slightly weaker than the 6.0 anchors (ekz1hN5QNh, bwOndfohRK) due to the methodology concern in the gradient comparison, the lack of statistical significance testing, and the brevity of the convolution/activation sections. It is solidly above the 4.4–4.75 range (WOopKWDWtS, MEnPLXJNng) due to stronger theoretical contributions and more comprehensive evaluation. It is comparable to 30aSE3FB3L (5.67). The most appropriate score is **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>