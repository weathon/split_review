## Summary

This paper introduces the *neural snowflake*, a trainable deep architecture that implements fractal-like (quasi-)metrics on ℝ<sup>d</sup>. The authors prove that a neural snowflake combined with a simple MLP encoder can isometrically embed any finite weighted graph (Theorem 4.1), and that under kernel regularity assumptions, the parameter count is polynomial in the number of nodes, avoiding exponential dependence on ambient dimension. Synthetic experiments show orders-of-magnitude lower embedding error than Euclidean baselines, and on Cora, CiteSeer, Tadpole, and Aerothermodynamics benchmarks, the neural snowflake DGM matches or surpasses state-of-the-art latent graph inference models without requiring combinatorial search over candidate geometries.

## Strengths

1. **Universal isometric embedding guarantee (Theorem 4.1)**: The paper proves that any finite weighted graph can be isometrically embedded by an MLP encoder into the metric space induced by a neural snowflake. This is a stronger theoretical guarantee than any prior latent graph inference method using fixed non-learnable geometries, and it rigorously justifies why the neural snowflake is a universal representation space. The strict separation result (Theorem 4.2) further shows that Euclidean-only MLPs are strictly less expressive.

2. **Polynomial parameter complexity under kernel regularity (Theorem 4.3)**: When the latent graph can be represented via a radially symmetric positive-definite kernel, the neural snowflake + MLP require only O(I²) width and O(I√I log I) depth — polynomial in the number of nodes *I*, with no exponential dependence on the ambient dimension. This is a meaningful contrast with universal approximation theorems where parameter counts typically scale exponentially in the input dimension.

3. **Superior metric learning on synthetic tasks (Table 2)**: Neural snowflake models with 847–4169 parameters achieve mean square embedding errors orders of magnitude lower (e.g., 0.00004 vs 0.1738 for one metric) than a Euclidean MLP with 5422 parameters across six diverse non-Euclidean target metrics. The comparison is intentionally asymmetric in favor of the baseline, making the result stronger.

4. **Competitive latent graph inference without random search (Tables 3-4)**: On Cora, CiteSeer, Tadpole, and Aerothermodynamics, the neural snowflake DGM matches or surpasses all compared Riemannian and product-manifold DGMs while learning the geometry end-to-end via backpropagation, eliminating the combinatorial search over candidate geometries required by prior approaches.

5. **Clean experimental design**: The benchmark experiments control for all factors except the latent geometry (same GCN model, same latent dimensionality, same training setup), enabling a direct comparison of the metric space's effectiveness.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Theory-experiment gap**: The paper's central theoretical claim is that the neural snowflake enables *isometric* embedding of any weighted graph (Theorem 4.1), but the benchmark experiments do not test whether the learned distances are actually isometric to the latent graph structure. Instead, the experiments use the snowflake as a distance function inside a DGM pipeline with Gumbel top-k edge sampling, and the reported metric is downstream accuracy. This means the theory neither predicts nor explains the empirical results — the universality guarantee is not directly validated. The paper acknowledges this gap (Section 5, lines 670-671: "the development of improved edge sampling algorithms to foster better synergy between metric space learning and graph construction is not the primary focus of this paper"), but the disconnect remains.

2. **Modest and inconsistent gains on benchmarks**: The neural snowflake's improvements over Euclidean and product-manifold baselines are typically 1–3% accuracy on Cora/CiteSeer. No single geometry dominates across all datasets — the Neural Snowflake DGM, DGM with Snowflake (non-learnable), and product-manifold variants all take turns being the top performer. The synthetic experiments show dramatic advantages, but these do not translate into similarly decisive wins on real benchmarks.

3. **The Riemannian impossibility result (Proposition 4.1) is accompanied only by a sketch in the main text**: The claim that a simple 5-node graph cannot be isometrically embedded into *any* complete connected smooth Riemannian manifold is quite strong. While the intuitive argument about geodesic uniqueness is provided in the figure caption, the main text does not contain a formal proof — the rigorous argument would need to be in the appendix. This makes the claim hard to fully evaluate from the main paper alone.

### Trivial

- The paper mentions that neural snowflake weights must be non-negative but does not specify how this constraint is enforced during training (e.g., via clipping, projection, or reparameterization). This is a minor practical detail worth clarifying.
- The neural snowflake architecture (Eq. 5) could benefit from a more explicit worked example showing how the dimensions flow through the matrices A, B, C.

## Nice-to-Haves

- An experiment that explicitly tests the isometric embedding guarantee: pick a graph known to be unembeddable in any Riemannian manifold (e.g., the 5-node graph from Proposition 4.1), train the neural snowflake to learn its metric, and measure the embedding distortion directly. This would directly validate the claimed advantage over Riemannian geometries.
- A controlled comparison isolating the benefit of *learnability*: compare the neural snowflake DGM against a DGM with a fixed (non-learnable) snowflake metric such as ‖·‖⁰·⁵. This would separate the contribution of the adaptive geometry from the snowflake structure itself.
- Multi-seed or confidence-interval reporting for the synthetic embedding experiments to confirm that the order-of-magnitude gaps are statistically robust.

## Removed Points

These points were flagged by the reviewer but are removed per policy:

- **"Theorem 3.1 is not credible as stated / proof is missing"** — The reviewer's numbering ("3.1") does not match the paper; the theorem in question is Theorem 4.1 (labeled \ref{thrm:qualitative}). The reviewer's claim that "the only justification is a citation to Andoni, Naor, Neiman (2018) and Kratsios (2021)" is factually incorrect: those citations appear in a *comparison* section after the theorem, not as its proof. The rigorous proof was in the appendix (stripped by the PDF parser). Per hard rules, criticisms about missing appendix proofs are removed.

- **"Proposition 2.1 needs a correct and complete argument"** — The proposition in question is labeled \ref{prop:Embedding_Impossible} (Section 4.1.1, not Section 2). A sketch is given in the figure caption; the full proof was in the appendix. Removed per the same rule.

- **"Curse of dimensionality claim is misleading"** — The paper's claim is that parameter count is polynomial in *I* (number of nodes) rather than exponential in *D* (ambient dimension), which is a fair and explicit contrast with universal approximation theorems. The reviewer conflates this with a different claim. The paper's statement is technically accurate and appropriately qualified ("in cases where the latent weighted graph has favourable geometry").

- **"MLP baseline is weak"** — The paper *intentionally* gives the MLP baseline more parameters (5422 vs. 847–4169), creating an asymmetry that favors the baseline. Per hard rules, this criticism is removed.

- **"Definition of neural snowflake not clearly explained"** — The architecture is specified with dimension annotations for matrices A, B, C and the activation function. While a worked example would help, the description meets a reasonable standard of clarity.

- **"Non-negativity constraints not discussed"** — This is a minor implementation detail. Moved to Trivial.

## Novel Insights

None beyond the paper's own contributions. The key insight — that a trainable fractal-like metric can serve as a universal representation space for latent graph inference — is well-articulated in the paper itself.

## Suggestions

1. In a revision, consider adding a direct test of the isometric embedding guarantee: measure the distortion between the learned neural snowflake distances and the ground-truth graph distances on a synthetic graph with known structure, including the "hard" 5-node graph from Proposition 4.1.
2. Clarify the implementation of the non-negativity constraint on the neural snowflake weights (e.g., whether absolute values, softplus, clipping, or projection is used).
3. Add an ablation separating the effect of *learnability* from the effect of the snowflake structure itself, e.g., compare against a fixed snowflake metric such as ‖·‖⁰·⁵.

## Score and Decision

**Originality**: High — the neural snowflake architecture and its theoretical analysis are novel.
**Importance**: Good — latent graph inference is an active area and a principled, differentiable solution to geometry search has clear value.
**Claims**: The paper's empirical claims are well-supported; the theoretical claims are ambitious and plausible but cannot be fully verified from the main text alone.
**Soundness**: Solid — the experiments are well-controlled and the synthetic results are convincing. The theory-experiment gap is the main limitation.
**Clarity**: Generally clear, though the neural snowflake equations could benefit from a more annotated example.
**Value**: The neural snowflake is a practically useful module that can be dropped into existing DGM pipelines, and the theoretical analysis provides a principled foundation.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>