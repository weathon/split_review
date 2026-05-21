Now I have a good understanding of the calibration landscape. Let me write the consolidated review.

## Summary

The paper proposes two methods for Geodesic Principal Component Analysis (GPCA) in Wasserstein space: (1) a method for centered Gaussian distributions that lifts the problem to GL_d via Bures-Wasserstein geometry (Propositions 3-5), and (2) GPCAGEN, a neural-network-based method for general absolutely continuous measures using Otto's fiber bundle to parametrize geodesics with MLPs without requiring input-convex neural networks.

## Strengths

- **Clean theoretical contributions for the Gaussian case.** Propositions 3-5 are well-motivated and provide genuine insight. Proposition 4 explicitly quantifies the distortion between TPCA and GPCA for covariance matrices with equal eigenvalues (showing distortion grows with |a-b|/(a+b)), and Proposition 5 proves that univariate GPCA stays within the Gaussian submanifold. The lifted formulation (Proposition 3) elegantly reframes the problem as optimization over GL_d.

- **Novel parametrization of Wasserstein geodesics avoiding ICNNs.** The paper parametrizes geodesics as μ(t) = (id + t∇f_ψ)_#(φ_θ_#ρ) using MLPs without requiring convexity of f, explicitly noting that "Otto's parametrization also allowed us to avoid relying on input convex neural networks (ICNNs)." This is a genuine methodological advance over prior work that required convexity constraints.

- **Quantitative comparison between GPCA and TPCA for the Gaussian case.** Figure 4 shows up to ~35% cost improvement of GPCA over TPCA at high distortion ratios, backed by Proposition 4's formula. This gives a concrete, measurable understanding of when and why the two methods diverge.

- **GPCAGEN's synthetic MNIST verification.** The MNIST experiment (Figure 5) where GPCAGEN recovers a known pair of intersecting orthogonal geodesics (one interpolating digits, one interpolating color) serves as a useful sanity check that the optimization converges to the intended structure.

## Weaknesses

### Major

- **Insufficient evaluation of GPCAGEN on its own terms.** The paper claims GPCAGEN solves the exact GPCA problem for a.c. measures, yet the experimental validation for the general case is almost entirely qualitative. The paper does not report the GPCA cost (Equation 1) for either GPCAGEN or the TPCA baseline on any of the point cloud or image datasets. The statement that "a direct numerical comparison between the two methods is therefore not meaningful" (Section 5.2) is unconvincing: one can straightforwardly evaluate the GPCA objective by projecting each distribution onto the learned continuous geodesic and computing the sum of squared Wasserstein distances. Without this comparison, the reader cannot judge whether GPCAGEN's geometric fidelity translates into quantitatively better components. The qualitative artifacts shown for TPCA in the appendix are suggestive but insufficient to support the paper's central claim.

- **Overstated "exactness" for the general case.** The abstract and introduction describe both methods as "exact in the sense that they do not rely on a linearization of the Wasserstein space" and producing "true geodesics that minimize the cost." For GPCAGEN, this label is misleading: the method uses (a) neural networks with finite capacity that cannot represent all diffeomorphisms, (b) the Sinkhorn divergence as an approximation of W₂², and (c) eigenvalue estimates on finite minibatches to enforce the diffeomorphism condition. The paper does acknowledge these approximations in Section 4, but the "exact" branding in the high-level claims sets expectations that the method does not meet. GPCAGEN is better described as a direct (non-linearized) approximate GPCA.

### Minor

- **No ablation or sensitivity analysis for regularization parameters.** The regularization coefficients λ_I and λ_O are set to 1.0 for all experiments with the assertion that this "ensures the algorithm works as expected" (Section 5.2). No ablation study varying these parameters is provided, and no analysis of their effect on intersection or orthogonality quality is shown.

- **Absence of quantitative evaluation on Gaussian real-data experiment.** The weather dataset experiment (Section 5.1) only shows a scatter plot of projection times. The paper does not evaluate whether GPCA provides better clustering, lower residual variance, or any other quantitative metric compared to TPCA on this data.

- **No discussion of computational cost or convergence.** The paper does not report runtimes, convergence behavior, or scaling properties for any of the experiments, making it difficult to assess practical applicability.

### Trivial

- The Gaussian GPCA algorithm is described only in prose; a pseudocode box similar to Algorithm 1 would aid reproducibility.

## Nice-to-Haves

- An ablation study for λ_I and λ_O, showing the effect on intersection/orthogonality quality and convergence of the GPCA cost.
- Scalability demonstration of the Gaussian GPCA to higher dimensions (e.g., d=10 or d=50).
- Discussion of how the algorithm handles failure cases (e.g., when eigenvalue monitoring detects t_min > t_max during training).

## Removed Points

- Concerns about missing pseudocode for Gaussian GPCA, missing implementation details for SO_d optimization, and missing parameter settings: these are deferred to the (stripped) appendix and by instruction we assume the original submission contains them.
- Criticism about the weather dataset figure not being shown: the figure (Figure 14) is in the appendix which is stripped.
- Comments about typos/formatting: parser artifacts, not author errors.
- General "missing related work" concerns: cannot verify without external sources.

## Novel Insights

The harsh critic's framing of the evaluation gap as the central weakness is accurate and well-supported by the paper's content. However, a more subtle point emerges from the comparison: the Gaussian case (Section 3) is both theoretically cleaner and better evaluated, yet its own experiments show that GPCA and TPCA differ meaningfully only in pathological cases (same eigenvalues, different orientations). This raises the question of whether the general-case method's main advantage is also confined to similarly special settings, or whether it consistently improves over TPCA across realistic data regimes. The paper currently provides no evidence either way for the general case, which is precisely the gap.

## Suggestions

1. **For the general case, add a quantitative comparison with TPCA on the GPCA cost (Equation 1).** This can be done on the synthetic MNIST data where ground truth is known, and on at least one real dataset (point clouds or images). Report the ratio of the objective values, similar to Figure 4 for the Gaussian case. Even if the improvement is marginal, this is an honest finding that advances understanding.

2. **Temper the "exact" claims for GPCAGEN.** Replace "exact" with "direct" or "non-linearized" when describing the general-case method, and be explicit about the approximations (neural network capacity, Sinkhorn divergence, eigenvalue estimates) in the abstract or introduction.

3. **Add an ablation study for λ_I and λ_O** showing the effect on intersection and orthogonality quality, and report the convergence of the GPCA cost during training.

4. **Add a pseudocode box for the Gaussian GPCA** similar to Algorithm 1 to improve reproducibility.

## Score and Decision

### Calibration and Score Determination

**Round 1 (Bracketing):** Weak anchors (scores < 3.5, e.g., 2.33–3.00) are clearly weaker than this paper — they lack the theoretical contributions and clear problem framing. Middle anchors (3.5–7.5) include GeONet (avg 5.0, reject), PGPCA (avg 7.33, accept spotlight), Lagrangian Flows (avg 6.0, reject), and Diffeomorphic Mesh Deformation (avg 7.0, accept). Strong anchors (>7.5) are clearly stronger in terms of experimental rigor and completeness. **Initial bracket: 4.5–6.5.**

**Round 2 (Narrowing):** Compared to GeONet (avg 5.0, reject) — a neural operator for Wasserstein geodesics with insufficient experiments — this paper has stronger theory (Propositions 3–5) but shares the problem of inadequate quantitative evaluation for its main claimed contribution. The current paper is somewhat better than GeONet (stronger theoretical foundations, MNIST sanity check, real-data demonstrations), placing it above 5.0. Compared to Lagrangian Flows (avg 6.0, reject), this paper is weaker in experimental completeness — Lagrangian Flows had similar issues with not directly measuring the optimization objective but had more extensive real-data evaluation on scRNA-seq. The current paper's Gaussian-case theory is a genuine asset, but the general-case evaluation gap is too large to place it at 6.0 or above.

Several anchors in moderate ranges (Score-based pullback at 5.25, Sum-of-Squares for MTW at 5.6) have similar profiles: genuine contributions undermined by evaluation gaps. This paper's theoretical contributions for the Gaussian case are stronger than those anchors, but the evaluation gap for GPCAGEN is equally prominent.

**Final score: 5.5.** The paper has genuine strengths (Gaussian theory, novel parametrization, clean problem framing) that elevate it above weak reject territory, but the insufficient quantitative evaluation of GPCAGEN — the method that is positioned as the paper's main contribution filling "the gap" — prevents it from reaching the acceptance threshold. A major revision addressing the evaluation gap could move this to a 6–7 range.

**Anchors consulted:**
- /home/wg25r/review_agent/human_reviews/qcyn7ESaM8.md (avg 2.50, R1) — much weaker, no relevant theory
- /home/wg25r/review_agent/human_reviews/YKfESGFdas.md (avg 5.00, R1+R2) — GeONet: similar topic, weaker theory, similar evaluation gaps
- /home/wg25r/review_agent/human_reviews/gxhRR8vUQb.md (avg 7.00, R1) — Diffeomorphic Mesh Deformation: stronger experiments, similar OT flavor
- /home/wg25r/review_agent/human_reviews/gFBTNDNDUG.md (avg 6.00, R1+R2) — Lagrangian Flows: more complete evaluation but similar "not comparing objective" criticism
- /home/wg25r/review_agent/human_reviews/mkDam1xIzW.md (avg 7.33, R1) — PGPCA: stronger experiments and baselines
- /home/wg25r/review_agent/human_reviews/emSgz2bKVq.md (avg 5.25, R2) — Score-based pullback: similar level, synthetic-only evaluation
- /home/wg25r/review_agent/human_reviews/0AHkdAtFW8.md (avg 5.60, R2) — SOS for MTW: solid theory but limited ML relevance
- /home/wg25r/review_agent/human_reviews/gQlxd3Mtru.md (avg 8.67, R1) — far stronger in experimental rigor
- /home/wg25r/review_agent/human_reviews/P1aobHnjjj.md (avg 7.75, R1) — far stronger in theoretical depth
- /home/wg25r/review_agent/human_reviews/1HCN4pjTb4.md (avg 7.60, R1) — far stronger in completeness
- /home/wg25r/review_agent/human_reviews/MHjigVnI04.md (avg 7.67, R1) — far stronger in analysis

**MY FINAL SCORE: <score>5.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**