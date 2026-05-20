Now I have everything I need. Here is my consolidated final review.

---

## Summary

This paper introduces a novel classification of saddle points in neural network loss landscapes — Type-I (where gradient noise persists at the saddle) and Type-II (where gradient noise vanishes in escape directions) — and shows that Type-II saddles can be attractive for SGD even when the Hessian has negative eigenvalues. The authors characterize this attractivity via Lyapunov exponents of a random matrix product process, deriving a sharp condition (Theorem 1) for 1D dynamics and linking it to a phase diagram with at least four distinct regimes. Experiments on a synthetic task, a controlled two-layer network, and deep ResNets support the theory, with the key application being an explanation of why large learning rates at initialization lead to training stagnation.

## Strengths

1. **Novel and well-motivated classification of saddle points (Definition 1, Section 3).** The Type-I/Type-II distinction is conceptually clean and practically relevant. It moves beyond the existing "strict vs. non-strict" saddle dichotomy by recognizing that the *vanishing of gradient noise* in escape directions — not just the Hessian spectrum — determines SGD's ability to escape. The paper provides concrete examples of Type-II saddles (permutation symmetry, GELU without symmetry) and Theorem 4 establishes that the origin is Type-II for a broad family of networks, grounding the classification in realistic architectures.

2. **Principled theoretical framework connecting probabilistic stability to Lyapunov exponents (Theorems 1–3).** The derivation of the sharp condition $\mathbb{E}_x[\log|1 - \lambda h(x)|] < 0$ (Theorem 1) is a clean result that bridges ergodic theory and SGD dynamics. Theorem 2 showing that $L_p$-stability has measure-zero initializations around any saddle is a concrete mathematical advance — it rigorously justifies *why* moment-based analyses (e.g., Wu et al. 2018) are insufficient for saddle points and why probabilistic stability is the right tool. Theorem 3 linking the Lyapunov exponent sign to probabilistic stability provides a computable quantity for determining attractivity.

3. **Clear experimental validation in controlled settings (Section 5.1, Figure 3; Figure 6).** The synthetic experiment (Section 5.1) directly compares probabilistic stability against $L_2$-stability on a two-layer network and shows that probabilistic stability correctly predicts the transition from minima to saddles as learning rate increases, while $L_2$-stability makes incorrect predictions. Figure 6 provides a quantitative validation on a two-layer network where the theoretical phase boundary (from numerically integrating Proposition 2) is overlaid and matches the empirical rank transition — this is the strongest experimental evidence in the paper.

4. **Phase diagram revealing complex dynamics near Type-II saddles (Proposition 2, Figure 2, Section 5.2).** The paper characterizes at least five distinct phases (correct learning with/without norm stability, incorrect learning, low-rank collapse, instability) and shows how the phase boundaries depend on the gradient signal-to-noise ratio. The observation that increasing batch size makes low-rank collapse harder is a testable prediction. The fractal-like phase structure at finite data sizes (Figure 4) is interesting and suggests richness beyond the asymptotics.

## Weaknesses

### Fatal
None.

### Major

1. **Deep network experiments (Figures 5 and 7) lack quantitative theoretical comparison.** Figure 5 (tanh networks of varying depth) shows training loss vs. learning rate with labeled phases but no theoretical curve — the Lyapunov exponent is not estimated, and the claimed phase boundaries are marked only by visual inspection. Figure 7 (ResNet sparsity) similarly shows density transitions but without the theoretical boundary that Figure 6 provides. The paper states these experiments "show that Type-II saddles are indeed a major obstacle in the initial phase of training," but without a computed Lyapunov exponent or theoretical phase boundary overlaid, alternative explanations (e.g., simple divergence, flatness-related effects, or optimization difficulty unrelated to Type-II saddles) are not ruled out. This creates a gap between the paper's claim of explaining practical deep learning phenomena and the evidence actually provided. The paper would be substantially stronger if it computed or estimated the maximal Lyapunov exponent (e.g., via the QR method on products of batch Hessians) for at least one of these settings and showed alignment with the observed transition.

2. **Scope of applicability of Type-II saddles during training is not sufficiently discussed.** The definition requires that per-sample gradients vanish in escape directions for *all* data points — a strong condition. While the paper cites parameter symmetries as a source and gives Theorem 4 (origin is Type-II for locally-linear activations), it does not address whether Type-II saddles are encountered *after* the first few steps of training. The paper cites Jacot et al. (2021) on saddle-to-saddle dynamics but does not argue that those subsequent saddles are Type-II. If Type-II saddles are primarily confined to the initialization point, the theory's relevance to training dynamics beyond the first phase is limited. A brief discussion of this scope limitation would improve the paper.

### Minor

3. **Phase-counting inconsistency.** The abstract and introduction state "four distinct dynamic phases," but the concrete enumeration in Section 5.2 yields five phases (Ia, Ib, II, III, IV), and the Figure 2 caption says "at least five different phases." While this can be reconciled (Ia and Ib are sub-cases of "correct learning"), the inconsistency as written creates confusion about what the paper claims. This should be harmonized.

4. **The 1D eigenvalue approximation (using the largest eigenvalue of the batch Hessian) is used without discussion of its domain of validity.** In Section 4.4, the paper notes that using the largest eigenvalue $h^*(x)$ of $\hat{H}(x)$ gives a sufficient condition for convergence, and that the diagonal approximation decomposes the problem. However, neither the synthetic experiment (Section 5.1, where the 2D dynamics is reduced to the largest eigenvalue) nor the network experiments discuss when this approximation introduces significant error. In high-dimensional settings where escape directions may not align with the leading eigenvector, the approximation could break down silently.

5. **The paper does not directly test the core Lyapunov exponent condition (Eq. 10) on the deep network experiments.** While Theorem 3 states that probabilistic stability is equivalent to $\Lambda < 0$, the deep network experiments measure loss curves (Figure 5) and weight sparsity (Figure 7) rather than estimating $\Lambda$ or verifying the attractivity condition from Theorem 1. Estimating the Lyapunov exponent even approximately (e.g., via the QR method or the diagonal approximation mentioned in the paper) would substantially strengthen the link between theory and the practical phenomena claimed.

### Trivial

6. The labeling of phases differs across the abstract (4 phases), the figure caption (5 phases), and the body (5 phases listed as Ia, Ib, II, III, IV). This should be made consistent.

7. The GELU example footnote (page 3) would benefit from stating explicitly that the network output is identically zero at the origin, which trivially makes the gradient zero for all data points — making clear that this is a special case even without traditional symmetry.

## Nice-to-Haves

- An experiment directly manipulating batch size for the deep networks to test the prediction (mentioned in the theory but not in the deep-network experiments) would provide a clean additional test.
- A brief discussion of how the Lyapunov exponent could be estimated in practice for realistic networks (e.g., via the QR decomposition of products of $I - \lambda \hat{H}(x_t)$) would help practitioners connect the theory to experiments.
- The paper notes that the diagonal approximation works in practice for the controlled experiment; showing where it might fail (e.g., when off-diagonal Hessian terms dominate) would help set appropriate expectations.

## Removed Points

- **Criticism that experiments provide no quantitative link at all.** The harsh critic's blanket statement that deep-network experiments lack quantitative validation is overly broad: Figure 6 *does* overlay a theoretical phase boundary (white dashed line computed from Proposition 2) and the text explicitly states "the theoretical boundary agrees well with the numerical results." The weakness is specific to Figures 5 and 7, not all deep network experiments. This nuance is reflected in Major weakness 1 above.

- **Criticism about missing batch size ablation.** The paper references batch size experiments in the appendix ("see Figure 11, for example" and "Appendix A.4 for the experiment with a varying batch size"). Since the appendix is stripped from the submitted version, this criticism cannot be verified and is removed per guidelines.

- **Request for more discussion of the GELU example.** The example is already explained and the footnote is sufficiently clear. This is a presentation preference, not a substantive weakness.

- **General concerns about "unfair comparison with baselines."** The comparison in the synthetic experiment (Figure 3) is framed against the baseline's own stability predictions, and the asymmetry favors the baseline (the baseline's prediction is the one that fails). Per guidelines, this is removed.

- **Strength Finder's generic strengths removed.** Claims such as "this paper addressed an important problem" or generic praise without specific evidence are removed. Only concretely grounded strengths (numbered 1–4 above) are retained.

## Novel Insights

The harsh critic correctly identifies that the deepest weakness is the gap between the elegant theory (Lyapunov exponents for Type-II saddles) and the empirical support for the claimed practical significance. However, this gap is narrower than the critic suggests — the controlled network experiment (Figure 6) *does* provide quantitative validation, and the paper never claims to have provably demonstrated that ResNet training stagnation is driven by Lyapunov exponent crossing zero. A more interesting observation that emerges from synthesizing both reviews is that the paper's framework is arguably strongest as a *qualitative explanation* (the theory explains *why* large learning rates at initialization can be harmful, and the experiments confirm the qualitative phase structure), and the main missing piece is a single, clean computation of the Lyapunov exponent for a small but realistic network — which would turn the "plausible story" into a directly verified prediction. The paper is also unusual in directly confronting the failure of moment-based stability analysis for saddles, a point that the strengths and weaknesses both converge on as a significant contribution.

## Suggestions

1. **Compute the Lyapunov exponent for at least one deep-network setting.** For a small CNN or an MLP on a simple dataset (e.g., a two-layer network on MNIST from Figure 5), estimate the maximal Lyapunov exponent via the QR method on the product of batch Hessians (or via the diagonal approximation already mentioned). Show that the learning rate at which $\Lambda$ crosses zero aligns with the observed stagnation boundary. This single experiment would address the most significant weakness.

2. **Harmonize the phase-counting.** Decide whether the classification yields 4 major phases (with Ia/Ib as sub-phases of "correct learning") or 5 phases, and state this consistently in the abstract, introduction, and figure captions.

3. **Add a brief discussion of when Type-II saddles arise beyond initialization.** Even a speculative paragraph would help readers assess the scope: e.g., "Symmetry-induced saddles are known to occur at initialization (Theorem 4), and recent work (Jacot et al., 2021) suggests SGD visits multiple saddles during training. Whether these later saddles are Type-II depends on whether the gradient vanishes in all escape directions at those points, which requires further investigation."

4. **Add a note on the validity of the 1D eigenvalue approximation.** A sentence acknowledging that the largest-eigenvalue approximation is a sufficient (not necessary) condition in multi-dimensional settings, and discussing when it might be overly conservative or optimistic, would strengthen the methodology section.

---

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Queried for papers on "saddle point stochastic gradient descent lyapunov exponent stability" across three score bands.

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| PwoplYNsBI (SGD convergence myths) | 2.50 | 1 | Much weaker; has fatal flaws in central claims. Current paper is far stronger. |
| lK0WxHeups (SGD iteration/SFO complexity) | 2.50 | 1 | Pure optimization complexity; no conceptual novelty comparable to Type-II classification. |
| CrMyHiUttz (Bilinear zero-sum games) | 3.00 | 1 | Different topic, weaker evaluation. Not comparable. |
| UMOlFJzLfL (SGD stability via loss geometry) | 5.75 | 1, 2 | Most similar topic. Poster at ICLR. Current paper has stronger theoretical novelty (Type-II classification) but weaker experiments (UMOlFJzLfL had limited engineered-quadratic experiments; current paper's Figure 6 is better controlled but Figures 5/7 are qualitative). |
| ogKE7LcvW6 (ReLU landscape, saddle escape) | 7.00 | 1, 2 | Poster at ICLR. Narrower scope (2-layer ReLU only) but stronger theoretical completeness within that scope. Current paper is broader but less definitive empirically. |
| MHjigVnI04 (High-dim SGD aligns with eigenspaces) | 7.67 | 1 | Spotlight at ICLR. More rigorous theoretical development; current paper is weaker on the empirical side but addresses a complementary question. |
| CQF8mTF7qx (Simplicity bias via sharpness) | 6.00 | 2 | Rejected at ICLR despite solid theory, largely due to unrealistic assumptions. Current paper's assumptions are more realistic, and the theory is comparably solid. |

**Round 1 bracket:** Initial assessment placed the paper between 5.5 and 7.0.

**Round 2 (Narrowing):** Queried for papers on related topics within (4.5, 6.5) and (5.5, 7.5) bands.

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| FZa1UCC9SC (signSGD risk curves) | 5.00 | 2 | Different focus; no saddle classification. Current paper is stronger. |
| BAX3NXJ6vU (Escaping saddle in min-max) | 5.33 | 2 | Optimization theory with presentation issues. Current paper has clearer conceptual contributions. |
| x45vUUY4nT (SGDM bounds) | 5.00 | 2 | Pure convergence bounds; no conceptual framework comparable to Type-II/Lyapunov contribution. |
| h7GAgbLSmC (Sharper guarantees for NN classifiers) | 7.00 | 2 | Poster at ICLR. Strong algorithmic stability analysis, different framing. |

**Final score determination:** The paper is clearly stronger than the ~5.0-5.33 papers (which are incremental optimization analyses or have presentation issues). It is comparable to the 5.75-6.0 range (papers with solid theoretical contributions but incomplete experimental validation). The paper falls short of the 7.0+ level (which require tighter empirical-theoretical alignment, as in ogKE7LcvW6 or MHjigVnI04). The core theoretical contributions are genuine, but the experimental gap for the claimed practical significance limits the score.

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**