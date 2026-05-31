Now let me run calibration searches.Round 1 bracket: The paper looks similar in scope to HCNN (avg 6) and Symmetric Spaces (avg 6). Both develop Riemannian operators and layers on a new hyperbolic model with multiple tasks. The bracket is roughly 4.5 to 7. Let me read these two anchors closely and narrow.Round 1 bracket: 5 to 7. Let me narrow.Round 2 narrowing: The PV paper closely resembles HCNN (avg 6, accept) and Matrix Manifold NN++ (avg 5.67, accept) — both extend established gyrovector machinery to a new hyperbolic representation with neural layers and multi-task validation, with the recurring critique that derivations are pull-backs from prior work and downstream gains are not always clearly attributable. PV adds compelling stability microbenchmarks (Tab 2-3) and broader task coverage; the central framing tension (unconstrained ⇒ stable vs. isometry to Poincaré) and the within-1σ CIFAR results pull it back to roughly the same band. Final placement: 6.0.

## Summary
The paper introduces Proper Velocity Neural Networks (PVNNs), a parameterization of hyperbolic geometry derived from Ungar's gyrovector framework. It establishes closed-form Riemannian operators on the PV manifold (Thm. 4.3) via an isometry to the Poincaré ball (Thm. 4.2), develops PV-space MLR, FC, convolutional, activation, and gyro-batch-normalization layers, and validates the framework with numerical-stability microbenchmarks, image classification (CIFAR-10/100), node classification (Disease/Airport/PubMed/Cora), and genomic sequence learning (TEB).

## Strengths
- **Closed-form Riemannian toolkit for PV space (Sec. 4.2, Thm. 4.3).** The paper derives Exp/Log maps, parallel transport, and distance in PV coordinates and shows (Thm. 4.4) that gyro operations can be re-expressed via the Riemannian operators. Even though the operators are obtained by pullback through the isometry π, the explicit PV-coordinate forms appear to be new and immediately useful.
- **Efficient PV MLR reformulation (Thm. 5.2, Eq. 19).** The (z_k, r_k) reparameterization eliminates the b×C×n gyroaddition tensor and reduces PV MLR to inner products, recovering Euclidean MLR as K→0⁻. This is a concrete computational win that addresses real engineering concerns with the naive form.
- **Genuine numerical-stability evidence in the round-trip and gradient probes (Tabs. 2–3).** The PV round-trip error 2.1×10⁻⁷ vs. Poincaré's 2.1×10⁻⁴ in FP32 is a real ~10³× gap, and PV's gradient magnitudes ([1.1×10⁻⁴, 2.1×10⁻⁶]) avoid both Poincaré's vanishing and the hyperboloid's NaN behavior under the same conditions. These directly support the stability claim for the PV *chart*.
- **Broad experimental coverage.** Four task families (microbenchmarks, image classification, graph node classification, genomic CNN), four graph datasets spanning δ-hyperbolicity from 0 to 11, and multiple ablations on layer type, normalization variant, embedding choice, and activation (Tabs. 6–9).

## Weaknesses

### Fatal
None.

### Major
- **The "unconstrained ⇒ stable" framing is in tension with the paper's own isometry result.** Thm. 4.2 shows PV is Riemannian-isometric to the Poincaré ball, and the operators in Thm. 4.3 are explicit pullbacks: Log_x relies on ‖π(z)‖, PT invokes Möbius gyration on π(x), π(y), and the distance is tanh⁻¹(√-K‖π(·)‖). For large ‖x‖ in PV, ‖π(x)‖ → 1/√-K, i.e. exactly the Poincaré boundary. So whenever a PV embedding strays from the origin, the implementation still touches the very boundary region whose instability motivated the paper. The contribution is really "a better-conditioned coordinate chart for hyperbolic geometry," not "a new geometry." The paper never separates these claims, and that conflation propagates through the abstract, intro, and §6.1 narrative. Confirmed against Sec. 4.1, Eq. (4), Thm. 4.3, and Eq. (13).
- **The stability microbenchmark is reported at a single operating point and does not separate PV from Poincaré on the gyro-operator probe.** Tab. 1 shows 0% failures for both PV and Poincaré at all r up to 1000; only the hyperboloid fails. The "violation rate" for PV is N/A by definition, not by measurement. The headline-supporting results (Tabs. 2–3) are reported at K=−1, n=16, ‖v‖=10 with no sweep over K or ‖v‖ and no decomposition of which step of the Poincaré pipeline (Möbius addition? tanh? near-boundary clipping?) loses precision. The conclusion may be correct, but the supporting evidence is thinner than the abstract's framing.
- **The Airport 5.86% gap is unexplained given the isometry.** Because PV is Riemannian-isometric to the Poincaré ball used by HNN/HNN++, a 5.86-point accuracy gap on Airport (Tab. 5) cannot come from geometry — it must come from optimization trajectory differences, layer design differences, or FP32 numerics. The paper does not diagnose which one. A direct FP64 sanity check on the Poincaré baselines would resolve the ambiguity.
- **Image-classification results do not statistically separate PV from baselines.** In Tab. 4, PV MLR (95.30 ± 0.18) is well within 1σ of Unidirectional MLR (95.12 ± 0.20) on CIFAR-10, and PV (78.20 ± 0.37) is within ~1σ of Lorentz MLR (77.96 ± 0.09) on CIFAR-100. The abstract's "stability and effectiveness of PVNNs" leans more on the graph and genomic tables than on CIFAR. Worth toning down or supplementing with significance tests.

### Minor
- **§6.4 lacks a Poincaré convolutional baseline.** The only hyperbolic comparator is HCNN-S; without a Poincaré variant on the same backbone, it's unclear whether the gain is "PV vs. hyperboloid" (consistent with the stability story) or "PV vs. Poincaré" (which would be more surprising given the isometry).
- **Tab. 7 Fréchet ∞ entries are worse than 10-iter on Disease, Airport, and PubMed.** The gap on PubMed (71.16 vs. 74.34) is substantial. If converged Fréchet computation hurts, the iterative solver is acting as a noise injector rather than a Fréchet-mean estimator at the operating point that performs best. The paper does not flag or discuss this.
- **On Cora (weakly hyperbolic, δ=11), PVNN+TBN drops to 45.36±2.44 and PVNN+GyroBN to 46.64±5.45 — both much worse than no-BN PVNN at 52.26±1.32 (Tab. 6).** Batch normalization is harming performance precisely on the dataset where hyperbolic structure is weakest, but the discussion does not address this.
- **Implementation detail in PV GyroBN.** The paper notes that the PV Fréchet mean is computed by mapping to the Poincaré ball, computing the Poincaré mean (Lou et al., 2020, Alg. 1), and mapping back. If this is the production path, the numerical stability of the Fréchet-statistics variant is bounded by Poincaré's, which is worth flagging in §6.1.
- **CIFAR-10 Poincaré MLR variance (σ ≈ 1.5) is an order of magnitude larger than other entries (Tab. 4).** This stands out and could use a sentence explaining or addressing it.

### Trivial
None retained (all candidates were either formatting artifacts or below the bar).

## Nice-to-Haves
- Log the distribution of ‖x‖ in each hidden layer during training of PVNN vs. HNN++ to show whether HNN++ actually pushes points into the boundary regime where its operators degrade — this would tie the microbenchmarks in §6.1 to the downstream gain in §6.3.
- Re-run HNN++ in FP64 on Airport: if the gap closes, the story is "FP32 hurts Poincaré more than PV"; if not, the gap is in layer design and should be acknowledged.
- Sweep K (e.g., −10⁻², −1, −10²) and ‖v‖ in §6.1 to convert single-point numbers into a map of the operating regime.
- Reframe the contribution as "the PV coordinate chart is a numerically better-conditioned implementation of hyperbolic geometry than Poincaré, especially far from the origin" — owning the chart-vs.-manifold distinction would strengthen the paper.
- Probe whether under-converged Fréchet iterations are actually acting as a regularizer (Tab. 7), which would be a more interesting story than the homogeneity theorem alone.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"Tab. 1 is set up in a way that does not distinguish PV from the Poincaré ball; the violation rate is N/A by construction."* — Partially true but already implicit in the paper's own discussion (§6.1 explicitly says PV's violation rate is N/A because PV is unconstrained); kept only the substantive part of this concern under Major (single-condition reporting). The constructive aspect of the criticism is preserved; the rhetorical part is redundant.
- *Strength: "Comprehensive evaluation across four diverse tasks demonstrates that PV is not domain-limited."* — Generic breadth claim; the specific evidentiary value of the tasks is already captured above. Move to general background, not a standalone strength.
- *Strength: "Establishment of complete Riemannian toolkit for PV space."* — Kept in modified form, but the "complete toolkit" framing oversells novelty given the operators follow by pullback from Thm. 4.2. The retained strength notes the closed-form coordinate expressions specifically, not novelty of the geometry.

## Novel Insights
None beyond the paper's own contributions. The most non-obvious observation the reviews surface — that under-converged Fréchet iterations may be acting as a regularizer in the GyroBN ablation (Tab. 7) — is a diagnostic hypothesis worth following up but not a separate insight.

## Suggestions
- Recast the contribution as a better-conditioned coordinate chart rather than a new manifold; explicitly acknowledge that several PV operators invoke π and inherit Poincaré-boundary behavior.
- Add a K and ‖v‖ sweep for Tabs. 2–3 and isolate which Poincaré operation loses precision first.
- Provide a diagnostic for the Airport 5.86% gap — either an FP64 ablation on HNN++ or a per-layer ‖x‖ distribution comparison.
- Add a Poincaré convolutional baseline in §6.4.
- Add significance tests or larger n on the CIFAR table; explain the σ≈1.5 outlier for Poincaré MLR.
- Address the Tab. 7 "Fréchet ∞ worse than 10 iter" observation explicitly.

## Axis Evaluation
- **Originality**: Moderate. The PV chart for hyperbolic geometry is under-explored in ML, and providing closed-form Riemannian operators and PV-coordinate neural layers is a fresh framing. However, the geometry is isometric to the well-studied Poincaré ball; novelty lies primarily in coordinate-specific formulae and the efficient MLR reparameterization.
- **Importance of research question**: Modest-to-meaningful. Numerical stability of hyperbolic networks is a recognized practical pain point; offering a chart that demonstrably reduces FP32 round-trip error by ~10³× addresses a real engineering issue.
- **Claims supported by evidence**: Mixed. Numerical microbenchmarks support the stability claim in the FP32 round-trip and gradient probes; downstream claims are partially supported (graph and genomic gains are real) but CIFAR results are within noise and the Airport gap is unexplained.
- **Soundness of experiments**: Generally sound but thin in places: single-condition microbenchmarks, no FP64 ablation on Poincaré baselines, no Poincaré convolutional baseline on TEB.
- **Clarity of writing**: Good. Theorems are clearly stated, the derivative pull-back structure is honestly indicated in Sec. 4.2, and ablations are thorough.
- **Value to the community**: Real. Practitioners who use Poincaré-ball-based HNNs and run into FP32 precision issues at training-trajectory boundaries have a drop-in chart that may help; the closed-form layers are immediately usable.

## Anchors Used
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/b2FFWnwZxl.md — HVT, avg 3.40 (round 1, weak): much weaker than this paper; broad claims, less rigor.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/xA25Ib7H8U.md — Ricci flows, avg 2.33 (round 1, weak): not closely comparable.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/q6WtaLj8O1.md — H2GNN, avg 3.00 (round 1, weak): below this paper.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/NYPJz0CL5X.md — HDC, avg 3.00 (round 1, weak): not closely comparable.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/ekz1hN5QNh.md — HCNN, avg 6.00 (round 1, mid; read in full): direct precedent (Lorentz CNN); reviewers noted within-margin results, lack of clear hypothesis — same pattern as PV's CIFAR table. PV paper is similar in scope with stronger stability evidence.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/bwOndfohRK.md — Symmetric Spaces NN, avg 6.00 (round 1, mid; read in full): more general (symmetric noncompact spaces) but more abstract; PV is narrower with sharper empirical signal.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/WOopKWDWtS.md — Robust hyperbolic learning, avg 4.40 (round 1, mid): below this paper.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/jzneu6AO2x.md — Hyperbolic Prototypical, avg 4.25 (round 1, mid): below this paper.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/Xo0Q1N7CGk.md — Conformal Isometry / Grid Cells, avg 8.00 (round 1, strong): substantially stronger, different topic.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/3i13Gev2hV.md — Compositional Entailment Hyperbolic V-L, avg 8.00 (round 1, strong): substantially stronger downstream story.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/JWtrk7mprJ.md — Residual DGP on Manifolds, avg 7.60 (round 1, strong): not closely comparable.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/kbjJ9ZOakb.md — Invariance manifolds, avg 8.00 (round 1, strong): not closely comparable.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/30aSE3FB3L.md — Matrix Manifold NN++, avg 5.67 (round 2; read in full): very similar profile — pull-back-style derivations, modest empirical gains; reviewer split 3/6/8. PV paper has stronger empirical breadth and stability evidence than this anchor.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/MEnPLXJNng.md — Riemannian Transformation Layers, avg 4.75 (round 2): below PV.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/IUmDBY4NOQ.md — Geometry-aware Distance, avg 4.75 (round 2): below PV.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/bUgni8nH8Z.md — ReLU activation analysis, avg 5.00 (round 2): not closely comparable.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/TTonmgTT9X.md — Hyperboloid Decision Trees, avg 6.60 (round 2): different method but with clearer practical wins; PV paper closer to it on theoretical contribution side but with within-σ CIFAR vs. clear wins for HyperDT.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/ZkBg5D2lgT.md — Robotics taxonomies hyperbolic GPLVM, avg 6.25 (round 2): different domain.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/YcaFqY8LWD.md — GyroAtt, avg 6.25 (round 2; read in full): same family (gyro framework + new layers + multi-task), reviewers split 5/6/8/6, ultimately rejected for unclear motivation and within-margin gains. PV paper has clearer practical story (stability microbenchmarks) and stronger graph/genomic gains than GyroAtt, so should sit slightly higher.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/7PLpiVdnUC.md — LieLAC, avg 6.50 (round 2): different topic.

## Bracket Reasoning
Round-1 bracket: 5 to 7, by analogy to HCNN and Symmetric Spaces (both avg 6, accept) which propose new hyperbolic-NN frameworks with comparable scope. Round-2 narrowing: closest peers are HCNN (6.0), Matrix Manifold NN++ (5.67), and GyroAtt (6.25). PV has stronger stability microbenchmarks and broader task coverage than Matrix Manifold NN++, comparable theoretical rigor to HCNN, and clearer empirical signal than GyroAtt — but is held back by the framing-vs.-isometry tension and within-σ CIFAR results that mirror HCNN's criticism. Final placement: 6.0, right at the HCNN anchor.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>