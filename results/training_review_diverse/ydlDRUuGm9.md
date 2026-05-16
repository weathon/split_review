I have thoroughly cross-checked all reviewer claims against the paper. Let me now produce the final consolidated review.

---

## Summary

This paper provides both theoretical and empirical comparisons between Kolmogorov-Arnold Networks (KANs) and multi-layer perceptrons (MLPs), focusing on two axes: representation/approximation capacity and spectral bias during training. It proves representation theorems showing mutual embeddability (MLP→KAN without overhead; KAN→MLP with a grid-size-dependent parameter blowup, absent the SiLU term), derives approximation rates for deep KANs on Sobolev spaces via these embeddings, and analyzes the Hessian of a single-layer KAN to argue for reduced spectral bias. Experiments on 1D frequency fitting, Gaussian random field regression, and a 1D Poisson equation support the claim that KANs learn high frequencies more readily than MLPs.

## Strengths

- **Formal representation equivalence (Theorems 3.1 and 3.2):** The paper rigorously establishes that any ReLU$^k$ MLP can be exactly represented by a KAN of comparable size (width $W$, depth at most $2L$, grid size $G=2$), and any KAN without the SiLU nonlinearity can be represented by an MLP whose width scales as $O(GW)$. These results give a precise theoretical account of the relative expressiveness of the two architectures and formalize the intuition that KANs can be parametrically more efficient for large grid sizes.

- **Novel spectral-bias analysis for shallow KANs (Theorem 4.1):** The Hessian analysis of the least-squares loss for a single-layer KAN shows that the condition number is bounded by $O(d)$ (independent of the grid size $G$), in contrast to the $\Omega(n^4)$ scaling reported for two-layer ReLU MLPs. This is a genuine theoretical contribution that identifies a concrete mechanism—well-conditioned B-spline Gram matrix—by which KANs can avoid the severe frequency bias of ReLU networks. The paper is transparent that this analysis covers only the single-layer, SiLU-free case.

- **Consistent experimental evidence across multiple problems:** The 1D wave (Figures 1–2), GRF (Figures 3–4), and Poisson (Figure 5) experiments all show the same qualitative pattern: KANs learn high-frequency content substantially better than MLPs, even when MLPs are given more parameters and more training steps. This cross-task consistency strengthens the empirical case that the reduced spectral bias is a genuine architectural property, not an artifact of a single benchmark.

- **Practical hyperparameter insights:** The paper systematically varies depth, width, and grid size for KANs and shows how these interact with spectral bias. The finding that larger grid sizes and depths enable simultaneous learning of all frequencies, and that reduced spectral bias can lead to overfitting in data-scarce regimes, provides actionable guidance for practitioners. The connection between grid extension and multi-level learning is also discussed.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Spectral-bias theory is restricted to single-layer KANs without SiLU, while all experiments use deeper KANs with SiLU.** The paper is fully transparent about this gap (Section 4.1 explicitly calls the analysis "necessarily highly simplified and heuristic" and states "we only analyze a single layer"), but this means the theoretical result does not directly cover the architectures evaluated. The experiments serve as empirical evidence, and the theory provides intuition for the shallow core, but the central claim that "KANs are less biased toward low frequencies" rests more on the experiments than the theory for the deep case. Adding even a heuristic argument for how depth interacts with the well-conditioned basis would narrow this gap.

- **The KAN→MLP representation theorem (Theorem 3.2) and the spectral-bias theory both assume $w_b=0$ (no SiLU).** This is an acknowledged limitation, but it leaves open the question of whether the SiLU term significantly affects either expressiveness or spectral bias. Since the default KAN implementation includes SiLU and the experiments use it, the theoretical bounds technically apply to a variant of the architecture. A simple ablation experiment (KAN with $w_b=0$ vs. standard KAN) would clarify whether the assumption is benign.

- **GRF and PDE experiments lack variance information.** The 1D wave experiments average over 10 random phase seeds, but the GRF and PDE results are reported without error bars, confidence bands, or mention of multiple trials. Extending the same reporting standard to all experiments would increase confidence in the conclusions.

- **No experiments directly validate the single-layer theory.** The theory applies strictly to $L=1$ KANs without SiLU, but every experiment uses deeper KANs. A controlled experiment comparing a single-layer KAN against a single-hidden-layer MLP (where the theory directly applies) would provide a cleaner bridge between the theoretical and empirical contributions.

### Trivial
None.

## Nice-to-Haves

- An ablation study removing the SiLU term ($w_b=0$) to test whether the theoretical assumptions are benign for spectral bias in practice.
- Error bars or confidence bands on the GRF and PDE figures.
- A brief discussion or experiment involving Fourier feature networks or SIRENs, which the paper already cites in the introduction but does not compare against empirically.
- A controlled comparison where MLP and KAN parameter counts are matched (even if the design choice to give MLPs more resources strengthens the empirical case, a matched-control experiment would isolate the architectural cause).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Experimental comparisons are not controlled for model size, depth, or training budget"** — The asymmetry in all experiments (MLPs given more parameters and/or more training iterations) favors the baseline, not the author's method. This is an intentionally asymmetric design that proves a stronger point. Per the hard rules, criticisms of unfair comparison are removed when the asymmetry favors the baseline.

2. **"The paper does not cite recent work on spectral bias of other architectures (Fourier feature networks, SIRENs)"** — The paper explicitly cites SIRENs and Fourier feature mapping in the introduction (Section 1, lines 19–20). This criticism is factually wrong.

3. **"The proofs are not provided in the parsed text (assumed in the appendix)"** — Per the hard rules, criticisms about missing appendix content are removed (appendix sections are stripped by the parsing pipeline and exist in the original submission).

4. **Several presentation nitpicks and minor phrasing concerns** about whether the corollary "adds little" — the paper itself describes the corollary as following "immediately" from prior results; it is correctly labeled as a transfer of known rates to KANs.

## Novel Insights

The most novel observation that emerges from reading the reviews against the paper is that the single-layer Hessian analysis (Theorem 4.1) and the B-spline conditioning result have an independent value that the paper under-leverages. The fact that the condition number depends only on $d$ (input dimension) and not on $G$ (grid size) is a strong statement, and the $d'(d-1)$ redundant eigenvectors are cleanly explained by the parameterization symmetry of B-splines across input dimensions. This analysis could stand as a useful lemma even if separated from the deep-learning context. The reviews do not surface additional novel insights beyond the paper's own contributions.

## Suggestions

1. **Add a shallow-KAN experiment ($L=1$, $w_b=0$) to directly test Theorem 4.1.** This would close the largest gap between theory and experiment and would not require changing the paper's scope.
2. **Include an ablation comparing standard KANs ($w_b\neq0$) against KANs with $w_b=0$** on at least the 1D wave problem, to verify that the SiLU term does not materially affect spectral bias.
3. **Add error bars or individual-trial visualizations** to the GRF and PDE results to match the reporting standard of the 1D experiments.
4. **In the concluding remarks, explicitly separate the two evidential threads:** (a) the rigorous theory for shallow KANs without SiLU, and (b) the empirical evidence for deeper KANs with SiLU. The current conclusion blends them into "we have demonstrated" without distinguishing the strength of support.

## Score and Decision

**Originality:** Moderate–high. The representation theorems are new and the spectral-bias analysis for KANs has not appeared elsewhere.

**Importance of research question:** High. KANs are a rapidly growing area, and understanding their fundamental properties relative to MLPs is of broad interest.

**Claims well supported:** Reasonably. The theoretical claims are precise and caveated. The experimental claims are supported by consistent qualitative patterns, though the lack of controlled comparisons and variance information weakens the quantitative support.

**Soundness of experiments:** Moderate. The qualitative trend is convincing, but the absence of matched-size comparisons, error bars on two of three experiments, and an ablation for the SiLU term are clear limitations.

**Clarity of writing:** Good. The paper is well-structured, notation is clear, and limitations are honestly acknowledged.

**Value to the research community:** Good. Provides a theoretical foundation for understanding KAN expressiveness and training dynamics that practitioners and theorists can build on.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>