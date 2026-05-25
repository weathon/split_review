Now I have thoroughly read the paper. Let me construct the final consolidated review.

## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), providing the first systematic treatment of the Proper Velocity (PV) manifold as a representation space for hyperbolic deep learning. The authors derive the complete Riemannian toolkit for PV space (exponential map, logarithmic map, parallel transport, geodesic distance) via an isometry to the Poincaré ball, and build fundamental neural network layers (MLR, FC, convolution, activation, batch normalization) upon it. Extensive experiments across numerical stability, image classification, graph node classification, and genomic sequence learning demonstrate that PVNNs offer significant numerical stability advantages over prior hyperbolic models (Poincaré ball, hyperboloid) while matching or exceeding their performance.

## Strengths

- **Clear and compelling numerical stability advantage.** Tables 1–3 provide strong, well-designed evidence: PV maintains zero gyro-operation failures up to r=1000 in FP32 (vs. hyperboloid failing by r=20), yields round-trip map error ~10⁻⁷ in FP32 (vs. ~10⁻⁴ for Poincaré, ~10⁰ for hyperboloid), and keeps gradients in a safe band without vanishing or exploding. This is the paper's strongest empirical contribution and directly supports the central claim.

- **First complete Riemannian toolkit and neural network layers for the PV manifold.** Theorem 4.2 establishes the PV↔Poincaré isometry, Theorem 4.3 provides closed-form Riemannian operators (Exp, Log, PT, geodesic distance), and Section 5 builds PV MLR (Thm. 5.2), PV FC (Thm. 5.3), convolution, activation, and GyroBN (Thm. 5.4) layers. The efficient MLR parameterization (Thm. 5.2) that reduces to a matrix multiplication is a practical highlight, avoiding the memory blow-up of naive gyro-addition per class.

- **Broad and thorough empirical validation.** The paper evaluates PVNNs on four diverse tasks (numerical stability, image classification with ResNet-18, graph node classification, genomic sequence learning) with extensive ablations: tangent vs. Riemannian FC and BN (Table 6), batch statistics computation methods (Table 7), Exp₀ lifting (Table 8), and activation variants (Table 9). These ablations systematically validate the design choices and provide useful practical guidance.

- **Principled batch normalization with provable guarantees.** Theorem 5.4 proves that PV GyroBN normalizes the Fréchet mean and variance of a batch, providing a theoretical grounding that earlier Riemannian BN approaches lacked.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The graph learning experiments (Table 5) compare PVNN only against other hyperbolic models (KNN, HNN, HNN++, LNN) without a standard Euclidean GNN baseline (e.g., GCN).** The paper's stated conclusion is that "PV geometry is more effective on strongly hyperbolic graphs" — this is a comparative claim among hyperbolic geometries, so the hyperbolic baselines are appropriate for that specific claim. However, the absence of a simple Euclidean GCN makes it difficult to contextualize the absolute performance, especially on Cora where PVNN (51.42%) lags behind the hyperboloid LNN (53.34%) — a reader cannot tell whether all hyperbolic models underperform a straightforward Euclidean alternative on this dataset. Including a GCN would not weaken the paper's hyperbolic-vs-hyperbolic claims and would strengthen the overall evaluation. (This is partially mitigated by the genomic experiments in Table 10, which do include a Euclidean CNN baseline where PVCNN outperforms it on all five tasks.)

- **The main text does not explicitly state the optimizer used for training each model, which undercuts the paper's most practically significant selling point.** The paper repeatedly emphasizes that PV space is "unconstrained" and that the PV MLR parameterization "avoids Riemannian optimization" (Sec. 5.1), strongly implying that PVNN can be trained with standard Euclidean optimizers (Adam, SGD) while baselines require Riemannian SGD or constrained projections. Stating this plainly (e.g., "PVNN models were trained with Adam without any Riemannian correction") would make the contribution clearer and more actionable for practitioners. This information likely resides in the (stripped) appendix, but it deserves prominence in the main text. (The paper's Reproducibility Statement also notes that code will be released upon acceptance, which addresses the underlying reproducibility concern.)

- **The internal tension between PV's unconstrained geometry and its hyperbolic inductive bias is noted but not empirically resolved.** The paper shows that on CIFAR image classification, the PV MLR variant without Exp₀ lifting is marginally better than with it (Table 4: 95.30 vs. 95.27 on CIFAR-10, within one standard deviation), and activations can be applied directly in PV space because it is ℝⁿ (Sec. 5.3). While these are correctly presented as practical benefits of PV's unconstrained nature, the paper does not provide evidence (e.g., tracking the norm of activations during training) that the network is consistently exploiting the hyperbolic volume rather than simply benefiting from training stability. An analysis showing that representations grow beyond the Euclidean regime would sharpen the geometric narrative.

### Trivial
None.

## Nice-to-Haves

- **Add a Euclidean GNN baseline (e.g., GCN or GAT) to Table 5.** As discussed above, this would contextualize the hyperbolic-vs-hyperbolic results without weakening any claims.
- **Include wall-clock time and memory comparison** for PV vs. Poincaré vs. hyperboloid FC layers, building on the timing data already present in Table 7 for the GyroBN ablations. This would help practitioners assess the practical trade-offs.
- **Conduct a controlled analysis of activation norms** during training to demonstrate that PV representations grow beyond a small-‖x‖ Euclidean regime, thereby resolving the curvature-vs.-stability ambiguity.

## Removed Points

*These points are flagged to be removed per filtering rules; treat them with caution.*

- **Criticism that missing Euclidean baseline is a "structural gap in experimental design" (Harsh Critic, Issue 1).** The paper's scope is a comparative evaluation of hyperbolic geometries for neural networks. The hyperbolic baselines (KNN, HNN, HNN++, LNN) are the correct comparators for the paper's claims about PV geometry vs. other hyperbolic models. A Euclidean GCN would be informative but its absence is not a structural gap. Removed as scope-creep (the paper explicitly compares hyperbolic models, not hyperbolic vs. Euclidean across the board).
- **Reproducibility concern about undisclosed optimizer (Harsh Critic, Issue 2, part).** The paper states "More details are provided in App. C" for experimental setup. The appendix is stripped by the parser but present in the original submission. The code will also be released. Removed as a parser artifact / nitpick about appendix-deferred details. (The narrative/missed-opportunity aspect is kept in Minor weaknesses.)
- **Assertion that the "internal tension" means PVNN "is a Euclidean network" rather than a hyperbolic one (Harsh Critic, Issue 3).** The PV manifold is a valid model of hyperbolic space — it is isometric to the Poincaré ball (Thm. 4.2). The Riemannian metric (Eq. 1) is non-Euclidean; the fact that the ambient space is ℝⁿ does not make the geometry Euclidean. Removed as a misunderstanding of the mathematical relationship. (The request for norm-tracking analysis is kept as a Nice-to-Have.)

## Novel Insights

None beyond the paper's own contributions. The harsh critic correctly identifies the numerical stability results as the strongest evidence, the strength finder correctly flags the efficient MLR parametrization, and the paper's own ablations provide the most useful comparative insights.

## Suggestions

1. **Explicitly state in Section 6 (or each experiment subsection) that PVNN models are trained with a standard Euclidean optimizer (e.g., Adam) without any Riemannian correction steps**, and whether the same optimizer is used for baselines with their Riemannian constraints. This single change would substantially increase the paper's practical impact.
2. **Add a Euclidean GCN baseline to Table 5** — even as a supplementary table — to let readers contextualize the absolute performance levels across datasets.
3. **Include a figure or table showing the distribution of ‖x‖ across training for PVNN representations** on a representative dataset (e.g., Airport or Disease), to clarify whether the network operates in a regime where the hyperbolic volume is actually being exploited.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>