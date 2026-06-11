Now I have sufficient calibration. Let me write the final review.

## Summary
Marginal Flow introduces a density estimation framework where the model q_θ(x) is a finite mixture whose component parameters w_i are sampled from a learnable distribution q_θ(w) (implemented by passing noise through an unconstrained neural network f_θ). By resampling w_i at each evaluation rather than optimizing them directly, the model avoids the architectural constraints of normalizing flows (bijectivity, Jacobian computation) and flow-matching methods (ODE solving), while retaining exact density evaluation and single-step sampling. Experiments span synthetic 2D densities, Wishart mixtures on positive-definite matrices, simulation-based inference, and qualitative latent-space traversals.

## Strengths
1. **Simultaneous efficient exact likelihood and efficient sampling** — Marginal Flow is the only method in Table 1 achieving unqualified checkmarks for both operations. Figure 3 empirically demonstrates orders-of-magnitude speedups over NF, FM, and FFF for both sampling and density evaluation across dimensions 10²–10⁵, with the explanation (Section 2.2) being clear: evaluation requires neither inverting the network, computing Jacobian determinants, nor solving ODEs.

2. **Faster training convergence** — Figure 7 shows Marginal Flow's test log-likelihood reaching its asymptote orders of magnitude earlier in wall-clock time than NF, FM, and FFF across five synthetic benchmarks. This follows directly from the efficient density evaluation used in the training objective.

3. **Lower-dimensional manifold learning** — Section 2.3 and Figure 4 demonstrate that Marginal Flow correctly recovers a 1D manifold from 2D spiral data while providing exact density. It is the only method in Table 1 that combines "Exact likelihood" and "Lower dim. base distr." checkmarks.

4. **Flexibility beyond Gaussian component distributions (Wishart experiment)** — Section 4.3 adapts the model to symmetric positive-definite matrices by changing q(x|w) from Gaussian to Wishart. For 10×10 matrices, Marginal Flow achieves test KL ≈ 0.0088 versus NF's ≈ 0.82 (Figure 9), and for 100×100 matrices, NF is computationally prohibitive while Marginal Flow succeeds. This demonstrates a degree of architectural flexibility that existing density estimators do not offer.

5. **Multi-modal target handling** — Figure 5 shows Marginal Flow recovering all five modes from 150 data points with 5 clusters, while NF, FM, and FFF produce blurred or collapsed results. The explanation (Section 2.3) about why bijections struggle with new modalities is sound.

6. **Reverse KL training without data observations** — Figure 8 shows Marginal Flow achieving lower or comparable reverse KL than NF on several synthetic distributions when trained only by querying the unnormalized target density.

## Weaknesses

### Fatal
None.

### Major
1. **Critical hyperparameter N_c is never specified or analyzed across experiments** — The number of mixture components N_c (Eq. 2) determines both the computational cost and the Monte Carlo variance of the density estimate. The paper illustrates the idea with N_c=10 in Figure 1 but never reports what N_c is used in any experiment — not for synthetic data, not for Wishart mixtures, not for image experiments. Without knowing N_c, the runtime comparisons (Figure 3) are uninterpretable at the level of absolute numbers, and the density quality results cannot be properly evaluated or reproduced. The claim that "modeling capacity is not directly linked to N_c anymore" (line 64) is itself overstated: while the expressivity is less constrained than in a fixed GMM, the Monte Carlo variance of the density estimator does depend on N_c, and so does computational cost. This relationship is never studied.

2. **No ablation studies** — The paper makes several design choices (base distribution dimensionality m, number/size of MLP layers, choice of component distribution q(x|w), and most importantly N_c) but never ablates any of them. For instance: how does manifold dimensionality m affect learned density quality? How does the number of MLP layers affect results? How do different choices of q(x|w) perform on the same task (rather than different tasks)? The framework's claimed flexibility is asserted but not systematically demonstrated through controlled comparisons.

3. **Limited quantitative evaluation on standard density estimation benchmarks** — The paper's quantitative evaluation is restricted to synthetic 2D densities, Wishart mixtures (compelling but specific), and SBI results (in the appendix). Standard benchmarks for density estimation — UCI tabular datasets (POWER, GAS, HEPMASS, MINIBOONE) or image log-likelihoods (binarized MNIST, CIFAR-10) — are absent. The image experiments (MNIST, JAFFE) are purely qualitative with no FID scores, log-likelihoods, or baseline comparisons. This gap between the breadth of the claims ("flexible and efficient framework") and the narrowness of the evaluation is the paper's most significant weakness.

### Minor
4. **"Exact density" framing is imprecise relative to normalizing flows** — The Table 1 checkmark for "Efficient exact likelihood" uses the same ✓ as NF, but Marginal Flow's density estimate has Monte Carlo variance: evaluating the same point twice with different w_i samples yields different values (variance O(1/N_c)), whereas NF's exact density is deterministic. The paper does acknowledge the approximation in the text (line 64: "the resampling induces an approximation to the marginal distribution"), so this is a presentation issue, but the table is misleading without qualification.

5. **Some overclaiming in the text** — The paper states Marginal Flow "can perfectly learn all densities" (Section 4.1), but the visualization in Figure 6 shows learned densities that are visibly more diffuse than ground truth. Claims like "alleviate altogether the common shortcomings of current approaches" (abstract and introduction) are overly broad given the evaluation scope.

6. **Runtime-quality trade-off not fully characterized** — While Figure 7 shows faster convergence, the final converged log-likelihood values are not tabulated with confidence intervals, making it difficult to assess whether faster convergence is toward a competitive fixed point. The caption caveat "In most cases" suggests the advantage is not universal, and without final numbers the reader cannot evaluate the significance.

### Trivial
None.

## Nice-to-Haves
- A systematic study of N_c (test log-likelihood vs. N_c for one or two datasets) would resolve the most significant ambiguity.
- Adding one standard quantitative benchmark (e.g., test log-likelihood on a UCI tabular dataset or binarized MNIST) would substantially strengthen the empirical evidence.
- Reporting confidence intervals on the Figure 7 log-likelihood curves.
- A brief discussion of the gradient variance introduced by resampling w_i during training.

## Removed Points
These points were raised by the reviewers but removed per filtering rules:
1. **SBI results being in the appendix** — The parser strips appendices from all papers; these results exist in the original submission and should not be penalized.
2. **"Universal" claim made without reference** — The paper does cite Micchelli et al. (2006) for the universality property when q(x|w) is a kernel. This criticism is factually incorrect.
3. **Fatal framing of the exact-density issue** — The paper explicitly states that resampling induces an approximation (line 64), so this is a matter of presentation precision, not a hidden fatal flaw.
4. **Missing confidence intervals on Figure 7** — While true, Figure 8 does include 95% CI error bars. This is duplicative with the broader minor concern about characterization.
5. **Questions about OOM errors reflecting implementation specifics rather than fundamental limitations** — Without evidence, this is speculation.
6. **Strength about SBI state-of-the-art** — Treated as existing per protocol since the appendix is stripped by the parser.

## Novel Insights
None beyond the paper's own contributions. The core observation — that marginalizing over resampled component parameters from a neural-network-generated distribution avoids the architectural constraints of flows while maintaining efficient exact density evaluation and sampling — is the paper's genuine contribution, and the review surfaces no unexpected deeper insight beyond it.

## Suggestions
1. Report N_c used in every experiment and add a figure analyzing test log-likelihood vs. N_c for at least one synthetic and one real dataset.
2. Add ablation studies for: N_c, manifold dimensionality m, network width/depth, and choice of q(x|w) on a held-out task.
3. Include at least one standard quantitative benchmark (UCI tabular dataset or binarized MNIST log-likelihood) to demonstrate real-world competitiveness.
4. Qualify the "exact likelihood" claim in Table 1 with a footnote about Monte Carlo variance.
5. Tone down absolute language ("perfectly learn," "alleviate altogether") to match the scope of the evidence.

## Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kBNIx4Biq4.md | 6.50 | 1 | "Lifting Architectural Constraints of Injective Flows" — topically similar (lifts constraints on flows for manifold learning). Has more comprehensive real-world experiments (tabular + CelebA with FID) but similar missing-ablations weakness. Marginal Flow is somewhat weaker on experimental validation. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/zrxlSviRqC.md | 5.00 | 1 | "Self-normalising the likelihood for EBMs" — only low-dimensional experiments, no scaling evidence. Marginal Flow is clearly stronger empirically. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/7ZUUNMjM9T.md | 4.00 | 1 | "Flow Matching MLE by second-order trace" — marginal improvements, incomplete experiments. Marginal Flow is stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/99YEbiBbdy.md | 6.75 | 2 | "Dimension-Independent Rates" — theory paper, different contribution type with limited experiments. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jQ596tXT3k.md | 5.67 | 2 | "OOD Detection Paradox" — different domain, less comparable. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ZLSdwjDevK.md | 5.67 | 2 | "Riemannian Diffusion Mixture" — different methodology, manifold-based generative model. |

**Round 1 bracket:** 5.0 – 6.5  
**Round 2 narrowing:** The most directly comparable anchor is the injective flows paper at 6.50. Marginal Flow has a conceptually cleaner idea but weaker experimental validation (missing N_c, no ablations, no standard benchmarks). It is clearly stronger than the 5.00-level anchor. Placed at 5.5 — a paper with a genuinely novel idea whose evidence does not yet fully support the breadth of its claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>