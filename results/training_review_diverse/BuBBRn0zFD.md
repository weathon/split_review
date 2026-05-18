Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper derives two theoretically grounded tests for detecting pairwise interactions between perturbations from unstructured data: a **separability test** (KL-divergence based) that detects whether two perturbations affect overlapping latent variables, and a **disjointedness test** (MMD based) that detects whether perturbations affect disjoint outcome domains. These tests are integrated into an active learning pipeline using Information Directed Sampling (IDS) framed as active matrix completion, enabling efficient selection of perturbation pairs. The approach is validated on synthetic data (tabular and images) and on a real CRISPR knockout experiment with 50 gene pairs in HUVEC cells using microscopy images, where IDS discovers significantly more known biological interactions than baselines.

## Strengths

- **Theoretical derivation of testable separability condition (Theorem 1):** Under a causal DAG and diffeomorphism assumptions, separable perturbations imply the density ratio of the double perturbation equals the product of single-perturbation density ratios. This yields a principled, testable condition for interaction detection without requiring latent disentanglement — a genuine theoretical advance over prior work that assumed separability for generative modeling (e.g., Wang et al. 2023).

- **Formulation of a disjointedness test enabling compositional generalization (Definition 2, Theorem 2):** Proves that disjoint perturbations yield additive centered summary statistics, providing a practical MMD-based test and enabling prediction of pairwise outcomes from single perturbations. This directly supports efficient experimental design by allowing the system to skip experiments where compositional generalization holds.

- **Active learning pipeline with IDS for pairwise interaction discovery (Algorithm 1):** Reduces experiment selection to active matrix completion with IDS, balancing exploration and exploitation over test statistics. Empirical results (Figure 5) show IDS recovers all top-5% scoring pairs within 500 experiments and achieves 12–15% more known biological interactions than random search, UCB, Thompson sampling, and uncertainty sampling baselines.

- **Validation on real biological perturbation data:** Using CRISPR knockout experiments on 50 gene pairs with microscopy images, the paper shows that both separability and disjointedness tests recover known biological relationships (apoptosis pathway members, proteasome components) and that interaction scores align with synthetic lethality expectations (Section 5.2, Figure 3).

- **Cross-modality synthetic validation:** The tests are validated on both 3D tabular data and 3×128×128 images with ground-truth interaction structures (Figures 1–2), demonstrating the generality of the theoretical claims beyond a single data modality.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Low-rank assumption for the reward matrix is asserted without empirical validation.** The sublinear regret guarantee of ASD relies on the assumption that the test-statistic matrix **R** is approximately low-rank (line 329). No analysis of the singular value spectrum, effective rank, or low-rank approximation error is provided for either the MMD-based or KL-based score matrices. While the empirical success of IDS is encouraging, the theoretical motivation would be strengthened by showing that the observed reward matrices satisfy (or approximately satisfy) this structural condition.

- **Scaling of the KL-based separability test to 1,225 pairs is not explained.** The paper details the NRE + SMILE estimation procedure (lines 350–354) but does not clarify how it scales to the full 50-gene set: whether a single conditional neural network is shared across all perturbation pairs, whether separate classifiers are trained per pair, or what the computational cost is. The full KL matrix in Figure 4 (right) was computed offline, and the active learning experiments use MMD-based scores, so this does not affect the main experimental results, but the omission makes the offline results harder to reproduce.

- **The "unstructured data" framing is imprecise regarding the real-data experiments.** The abstract states tests "can be run on unstructured data, such as the pixels in an image" — which is true (demonstrated on synthetic 3×128×128 images). However, the real biological experiments use 1024-dimensional embeddings from a pretrained masked autoencoder (lines 426–428). The paper is transparent about this, but the framing could create an expectation that raw pixels are used throughout. The tests are representation-agnostic, and the paper would benefit from explicitly stating this and briefly discussing how the choice of embedding affects results.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis of the KL separability test under more complex nonlinear latent-to-observation maps beyond the synthetic setups tested would help characterize the regimes where the test breaks down.
- Including cosine similarity-based embeddings as a baseline for comparison against the interaction test statistics themselves (not just in the active learning comparison) would help contextualize the added value of the proposed tests. The paper qualitatively notes complementarity (line 68), but a quantitative comparison on the 50-gene dataset would be informative.
- A discussion of posterior misspecification risk — e.g., what happens if the low-rank prior is a poor match for the true reward matrix — would strengthen the active learning framing.

## Removed Points

- **Harsh Critic's claim that the synthetic image experiment "likely uses learned features, though this is not explicitly stated."** This is factually incorrect. The paper explicitly states the synthetic image data is "images (of size 3×128×128)" (line 359) generated by sampling from a latent distribution followed by a deterministic mapping g(·) (lines 361–362). No learned embeddings are used in the synthetic image experiment.
- **Criticisms about missing appendix content (proofs, experimental details).** The parser strips all appendix sections; these exist in the original submission. The paper references `\cref{apdx:proof}`, `\cref{apdx:klest}`, `\cref{apdx:expt}`, etc., which would contain the missing details.
- **The demand for a "small ablation comparing greedy batch to sampled batches"** — this is a wishlist item for a non-central design choice, not a weakness affecting the core claims.
- **Request for a "brief sensitivity analysis (e.g., varying the kernel or bandwidth)" for the MMD test** — the paper already tests two kernels (RBF and Matern 2.5) with consistent results, which is sufficient to support the claim of relative insensitivity.

## Novel Insights

The most interesting cross-perspective insight is that the two reviewers disagree on the severity of the "unstructured data" framing issue. The harsh critic treats it as a near-critical discrepancy, but the paper's own structure resolves it cleanly: the synthetic experiments run directly on pixels (demonstrating the claim), and the real experiments use embeddings as a practical necessity for high-dimensional biological data (which the paper discloses transparently). The deeper methodological question this raises — how much of the test's success depends on the quality of the learned representation versus the test itself — is a genuinely interesting open question that the paper scopes out but that future work could productively investigate.

## Suggestions

1. **Validate the low-rank assumption** by computing and reporting the singular value spectrum or effective rank of the MMD-based and KL-based reward matrices on the 50-gene dataset. If the matrix is not approximately low-rank, discuss whether the regret guarantee holds approximately or whether IDS's success stems from other properties (e.g., smoothness in embedding space).
2. **Clarify the KL estimation scaling** by stating whether a single conditional NRE model was trained across all perturbation pairs, and note the sample sizes and compute requirements. This is a small addition that would significantly improve reproducibility of the offline KL results.
3. **Qualify the "unstructured data" language** slightly: e.g., "Our tests can be run on unstructured data (such as pixels) or on learned representations thereof — the key requirement is that the tests are representation-agnostic." This preempts the framing concern without weakening the claim.
4. Add a brief note on what effect, if any, the choice of pretrained embedding has on the test results (e.g., raw pixels vs. PCA vs. MAE embeddings on a small subset of the data).

## Score and Decision

The paper makes a solid contribution: two well-motivated interaction tests with clean theoretical derivations, an elegant active learning wrapper, and convincing empirical validation on both synthetic and real biological data. The weaknesses are minor and addressable — none threaten the core claims. The paper is clearly written, the experiments are well-designed, and the value to the community (particularly in computational biology and experimental design) is substantial.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>