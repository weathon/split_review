Now I have all the data I need. Let me write the final consolidated review.

## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), leveraging the unconstrained Proper Velocity (PV) model of hyperbolic geometry—rooted in Einstein's special relativity—as an alternative to the constrained Poincaré ball and hyperboloid models. The authors derive the full Riemannian toolkit (exponential/log maps, parallel transport, geodesic distance) for PV space via its isometry to the Poincaré ball, then construct core neural network layers (MLR, FC, convolution, activation, batch normalization). Experiments across four tasks (numerical stability, image classification, graph node classification, genomic sequence learning) show PVNNs match or outperform existing hyperbolic baselines, with especially large gains on graph and genomic tasks, while avoiding the numerical instabilities of constrained models.

## Strengths

**1. First complete Riemannian toolkit for PV space.** Section 4 derives closed-form exponential map, logarithmic map, parallel transport, and geodesic distance (Theorems 4.3–4.4), all essential for building neural networks. These operators were previously unavailable for the PV model, and the derivation leverages the isometry to Poincaré (Theorem 4.2) to obtain clean expressions.

**2. Numerical stability advantage is rigorously demonstrated across three dimensions.** Section 6.1 (Tables 1–3) shows PV achieves zero failure/violation rates for gyro operations up to radius 1000, round-trip error of 2.1×10⁻⁷ (FP32) for Riemannian operators versus 2.1×10⁻⁴ (Poincaré) and 1.0×10⁰ (hyperboloid), and stable gradient magnitudes [1.1×10⁻⁴, 2.1×10⁻⁶] across radii compared to Poincaré's vanishing gradients (~10⁻¹²) and hyperboloid's explosion (includes NaN). This is the paper's clearest advantage.

**3. Closed-form, memory-efficient PV MLR and FC layers.** Theorem 5.2 (Eq. 19) provides an MLR formulation that avoids costly per-class gyroaddition by relying on inner products ⟨x, zₖ⟩, preventing the memory blow-up of an intermediate b×C×n tensor. Theorem 5.3 (Eq. 22) gives an equally clean closed form for the FC layer. Both recover their Euclidean counterparts as K→0⁻.

**4. Strong empirical results on graph and genomic tasks, with thorough ablations.** PVNN achieves +5.86% on Airport (97.96% vs. 92.10% for KNN), +1.25% on Disease (81.15% vs. 79.90%), and +9.33 MCC on SINEs over HCNN (93.78% vs. 84.45%). Tables 6–9 systematically ablate tangent vs. Riemannian FC, tangent vs. GyroBN, Fréchet vs. approximate statistics, exponential-map lifting, and activation strategies, providing a clear picture of where each design choice matters.

**5. GyroBN with provable normalization properties.** Theorem 5.4 shows that PV GyroBN satisfies homogeneity of the Fréchet mean (Eq. 26) and scaling of dispersion (Eq. 27), guaranteeing that centering shifts the batch mean to 𝟎 and scaling sets variance to s². This theoretical grounding surpasses many earlier Riemannian normalization schemes.

## Weaknesses

### Major
None.

### Minor

**1. Image classification gains are marginal and not statistically tested.** Table 4 shows PV MLR outperforming the best Poincaré baseline by 0.18% on CIFAR-10 (95.30 vs. 95.12) and 0.24% on CIFAR-100 (78.20 vs. 77.96)—both well within one standard deviation. The paper's claim of "competitive or superior performance" is fair for competitiveness but the evidence supports only parity, not superiority, on this task. The strong gains on graph and genomic tasks carry the empirical weight, but the vision results do not add meaningful evidence. A simple significance test would clarify this.

**2. The PV space is Riemannian isometric to the Poincaré ball.** Theorem 4.2 establishes this directly: every PV element maps smoothly to a Poincaré element with metric preserved. This means PV offers zero additional representational capacity—its advantage is purely numerical (unconstrained optimization, no boundary singularities, stable gradients). The paper acknowledges the isometry in Section 4.1 but the abstract and introduction frame PV as an "alternative" without clearly stating that it is a numerically favorable coordinate system for the *same* geometry. The framing is not dishonest (the paper calls it "an unconstrained representation of hyperbolic space" in the abstract), but being more explicit would strengthen the paper. This is a presentation issue, not a technical flaw—the practical contribution of numerically stable parameterization is real and valuable.

**3. No controlled comparison with a stabilized Poincaré baseline.** The numerical stability experiments (Tables 1–3) convincingly show PV avoids pathologies that raw Poincaré operators exhibit (gradient vanishing ~10⁻¹²). However, practitioners routinely address Poincaré gradient vanishing with careful initialization, gradient clipping, or norm regularization. The downstream graph/genomic experiments compare PVNN against standard Poincaré baselines (HNN, HNN++) that do not incorporate such stabilization tricks. It is therefore unclear whether PVNN's gains come from intrinsic numerical stability or simply from avoiding known pathologies that could have been mitigated in baselines. A tuned Poincaré variant with explicit stabilization would clarify this.

**4. The Cora underperformance is mentioned but not analyzed.** On the weakly hyperbolic Cora graph (δ=11), PVNN scores 51.42% versus the hyperboloid LNN's 53.34%—the only dataset where PVNN is not competitive. The paper notes this briefly ("On the weakly hyperbolic Cora dataset, PVNN remains comparable... and worse than the hyperboloid-based one") but offers no analysis. Understanding whether this is due to low hyperbolicity, embedding radius distribution, or some other factor would improve the paper's credibility and help practitioners decide when to use PVNN.

### Trivial
None.

## Nice-to-Haves

- **Complexity analysis:** The paper would benefit from a runtime/FLOPS comparison of core PV operators (Exp, Log, PT) against their Poincaré counterparts. Table 7 reports runtime for GyroBN variants but not for the core layers. This would help practitioners weigh the numerical stability gain against potential overhead.
- **Direct formula investigation for Log_x:** The logarithmic map (Eq. 11) involves dπₓ(v) which is a per-point linear map. The paper could discuss whether simpler direct formulas exist for PV space or note any implementation considerations.
- **Analysis of why PVNN underperforms on Cora:** As noted in Weakness 4, a brief diagnostic (e.g., checking δ-hyperbolicity thresholds or embedding radius distributions) would strengthen the paper.

## Removed Points

- **"Missing related works"** — Removed per rules (cannot confirm from external sources).
- **"Missing appendix / proofs in appendix"** — Removed per rules (parser artifact; these sections exist in the original submission).
- **"Formatting/style nitpicks," "typos," "missing parentheses in Eq. (2)"** — Removed per rules (parser/formatting artifacts).
- **"PV operators are computationally nontrivial per-point" with no evidence** — The paper provides runtime in Table 7. The claim that dπₓ(v) computation is "nontrivial" is speculative without measurement. Removed.
- **"Reproducibility concern about Log_x implementation"** — The paper states code will be released; the formula is explicit. Removed per rules.
- **Strength Finder's generic strengths about "addressing an important problem"** — These are not specific to the paper's content. Removed.
- **Strength Finder's claim about "SOTA" on all tasks** — The paper does not claim SOTA explicitly; it claims "competitive or superior." Slightly overstated. Modified.

## Novel Insights

The reviews surface an interesting tension: the paper's most rigorous contribution (numerical stability evidence) and its most practically impressive results (graph/genomic gains) are not directly causally linked by the experiments. The numerical stability experiments use low-level operator probes (gyromultiplication, round-trip error, gradient norms), while the downstream tasks use full network stacks where many factors interact (architecture choices, initialization, optimization dynamics). The reviewers' suggestion to compare against a stabilized Poincaré baseline addresses exactly this gap. Independently, the reviews highlight that the PV model's unconstrained nature provides benefits beyond mere numerics: it enables simple concatenation for convolution (Section 5.3), allows direct Euclidean activation without log/exp maps, and trivializes the "without Exp₀" variant that treats Euclidean features as PV coordinates—a flexibility that constrained models cannot offer. This suggests that the practical value of PV may stem as much from its *simplicity of interface* with Euclidean components as from raw numerical stability.

## Suggestions

1. Reframe the contribution in the abstract and introduction to cleanly separate what PV shares with Poincaré (isometric geometry) from what PV adds (unconstrained parameterization → numerical stability + simpler interface with Euclidean components). A sentence like "PV is isometric to the Poincaré ball—the geometry is the same—but its unconstrained coordinates eliminate boundary singularities, stabilize gradients, and simplify integration with Euclidean layers" would preempt the main criticism.

2. Add one controlled comparison in the graph learning experiments: PVNN versus a Poincaré variant with explicit gradient clipping and norm regularization. If PVNN still wins, the numerical stability argument is substantially strengthened. If not, discuss what else drives the gains.

3. Add a brief diagnostic for the Cora result—e.g., checking whether embedding radii on Cora are small enough that boundary effects do not matter, or whether the low hyperbolicity (δ=11) reduces the importance of accurate hyperbolic geometry.

4. Report statistical significance for the key comparisons (Airport, Disease, SINEs) where gains are large. While the gains are visually convincing, a t-test or effect size would formalize the evidence.

## Score and Decision

### Calibration

**Round 1 (Bracketing):**
- Weak anchors (<3.5): avg 3.00 — hyperbolic clustering, music, graph, EEG papers with fundamental flaws.
- Middle anchors (3.5–7.5): ILNN 4.50 (Accept Poster), Cartan 4.00 (Reject), Hyperbolic Implicit Eq. 4.00 (Reject), HypeCodeNet 5.50 (Accept Poster), HEEGNet 5.50 (Accept Poster), HexFormer 5.50 (Reject).
- Strong anchors (>7.5): 8.00–8.50 — rotation estimation, quantum networks, matrix methods — topically unrelated and much higher impact.

**Round 1 bracket:** The paper sits clearly in the 4.0–6.0 range, between rejected hyperbolic architecture papers (4.00) and accepted ones (~5.50).

**Round 2 (Narrowing within bracket):** Compared directly against the most topically similar anchors:
- **ILNN (4.50, Accept):** Both propose new hyperbolic layers with marginal vision gains. The current paper is more comprehensive (4 tasks vs. 2, with graph learning) and has more thorough ablations. **This paper is stronger.**
- **Cartan Networks (4.00, Reject):** Both propose alternative hyperbolic formulations. The current paper has much stronger empirical validation. **This paper is substantially stronger.**
- **HypeCodeNet (5.50, Accept):** Both provide strong empirical validation across multiple tasks with thorough ablations. HypeCodeNet has sharper application framing (code is hierarchical); this paper has broader coverage (numerical stability + graph + genomics). **Comparable quality.**
- **HEEGNet (5.50, Accept):** Both apply hyperbolic methods with solid results. This paper's theoretical contribution (first PV Riemannian toolkit) is stronger, while HEEGNet's application framing is sharper. **Comparable or slightly stronger on theory.**

**Final score:** 5.5. The paper provides a solid theoretical contribution (first complete Riemannian toolkit for PV), clear empirical value (numerical stability + strong graph/genomic results), and thorough ablations. The main limitations—isometric equivalence to Poincaré (acknowledged), marginal vision results, and the lack of a stabilized Poincaré baseline—are real but do not undermine the core contribution. The paper is comparable to accepted poster papers in this space.

**Anchors retrieved (all rounds):**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| nxzgr96uyV.md | 3.00 | R1 | Deep hyperbolic clustering — weaker contribution, rejected |
| rIyS3dYAiH.md | 3.00 | R1 | Hyperbolic music — weaker, rejected |
| vgG29qA4Vb.md | 3.00 | R1 | Hyperbolic graph — weaker, rejected |
| USbGgzaIiy.md | 3.00 | R1 | Hyperbolic EEG — weaker, rejected |
| hkssAkOako.md | 4.00 | R1/R2 | Hyperbolic Implicit Eq. — weaker, rejected |
| NNnkLi1ALt.md | 4.50 | R1 | ILNN — similar type, less comprehensive, accepted |
| Xq64xkQCak.md | 4.50 | R1 | Hyperbolic training dynamics — different topic |
| XwM7DlWPdR.md | 4.00 | R1 | Cartan Networks — weaker empirical validation, rejected |
| VaS6xcDrTb.md | 8.50 | R1 | Rotation estimation — stronger, topically unrelated |
| 248ysaRatx.md | 8.00 | R1 | Quantum networks — stronger, topically unrelated |
| yRtgZ1K8hO.md | 8.00 | R1 | Matrix sign — stronger, topically unrelated |
| DTQIjngDta.md | 8.00 | R1 | Visual geometry — stronger, topically unrelated |
| pdxJXBtLDT.md | 5.00 | R2 | Hyperbolic tanh normalization — different topic, rejected |
| 7rfdenlP1L.md | 4.50 | R2 | Hyperbolic RL — different topic, accepted |
| 1tJVBCpVD0.md | 4.00 | R2 | Transformation layers for Riemannian NNs — withdrawn |
| oq4jXWaFyH.md | 5.50 | R2/R3 | HypeCodeNet — comparable quality, accepted |
| ERVvLA5BJL.md | 5.50 | R2/R3 | HexFormer — comparable quality, rejected |
| CNDNRjpVIL.md | 5.50 | R2/R3 | HEEGNet — comparable quality, accepted |
| fu7iSvTwXm.md | 5.50 | R2 | Hyperbolic-like Euclidean regions — different topic, rejected |
| v6WrkzScHC.md | 4.67 | R3 | Riemannian correlation networks — comparable type, rejected |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>