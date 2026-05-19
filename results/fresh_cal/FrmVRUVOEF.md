## Summary

This paper proposes TC-tSNE, a temporally coherent variant of t-SNE for time-dependent data. The key idea is to add a temporal cost term to the t-SNE objective — derived from a structural-temporal duality — that enforces temporal coherence over *all* time pairs (long-range), not just adjacent frames. The spatial cost uses t-SNE (with its clustering-inducing Student-t distribution) while the temporal cost uses symmetric SNE (Gaussian), with a tunable parameter λ controlling the trade-off. The method is demonstrated on dynamic network embeddings of a primary school face-to-face interaction dataset and evaluated on six benchmark datasets against six existing approaches.

---

## Strengths

- **Principled long-range temporal coherence via structural-temporal duality.** The paper defines temporal coherence symmetrically with spatial coherence (Equations 1–2, Section 3.1) — the key insight that swapping data-point and time indices makes the two definitions isomorphic. This yields the clean additive cost decomposition $C = \frac{1}{T}\sum_t C^t + \frac{\lambda}{n}\sum_i \tilde{C}_i$ (Equation 3), together with the separable gradient form $\frac{\partial C}{\partial y_i^t} = \frac{1}{T}\frac{\partial C^t}{\partial y_i^t} + \frac{\lambda}{n}\frac{\partial \tilde{C}_i}{\partial y_i^t}$ (Equation 4). This is a genuinely novel and elegant contribution over prior strategies (aligned, continuous, velocity-penalised) that only enforce local ($s=t-1$) coherence.

- **Compelling qualitative case study on real dynamic network data.** Figures 1–3 apply TC-tSNE to UASE embeddings of a primary-school face-to-face interaction network. The 1D TC-tSNE embedding (Figure 1) clearly separates classes during morning/afternoon periods, shows merging during lunch, and returns to class structure after. Figure 3 compares six alternative methods: Independent t-SNE lacks temporal coherence, Global t-SNE has poor spatial quality, Aligned/Continuous t-SNE drift after the lunch break, and both Landmark Dynamic variants and Principal Component Dynamic t-SNE show degraded spatial clustering. This visually demonstrates that TC-tSNE simultaneously maintains spatial quality and long-range temporal coherence where existing methods fail on at least one axis.

- **Systematic taxonomy and critique of existing strategies.** Section 2 provides a clear, concise classification of six existing approaches (Independent, Global, Aligned, Continuous, Velocity-penalised, Guided) with concrete failure modes for each. This frames the gap TC-tSNE fills and gives context for its design choices.

- **Plug-and-play gradient decomposition.** The gradient separates cleanly into independent spatial and temporal terms, each computable using the base method's existing gradient routines. As the paper notes, this allows the strategy to be dropped into any neighbor-embedding algorithm with minimal code changes (Section 3.2).

- **Competitive quantitative results across diverse datasets.** On six benchmark datasets (Section 6, Figure 4), TC-tSNE "performs competitively sometimes achieving the best temporal and spatial metrics, and is never among the worst" — a modest, fairly stated claim that the evidence supports.

---

## Weaknesses

### Fatal
None.

### Major

- **No error bars, multiple trials, or statistical significance.** t-SNE is inherently stochastic (random initialisation, sampling noise). The paper reports only a single run per method per dataset. Without variance estimates or significance tests, the reader cannot determine whether TC-tSNE's observed advantage over baselines is systematic or noise. Figure 4 plots individual data points with no errorbars. This is the paper's most significant evidential gap, and it weakens the quantitative comparison substantially.

- **Hyperparameter selection protocol for TC-tSNE's λ, μ, and ῦ in the quantitative evaluation is underspecified.** For the case study, λ=0.3, μ=30, ῦ=5 are given. For the six benchmark datasets in Section 6, the paper states that "for methods with hyperparameters, we computed the metrics for a variety of parameter choices" and plotted non-dominated ones, but does not specify the ranges of λ, μ, and ῦ tested for TC-tSNE itself, nor how they were selected. Perplexities are said to be "chosen by eye before the experiment using independent t-SNE embeddings" but this is stated for "all t-SNE based methods" — still informal and hard to reproduce. Since TC-tSNE has three tunable knobs (λ, μ, ῦ) that directly control the spatial-temporal trade-off, inadequate documentation of the tuning procedure raises concerns about potential overfitting.

### Minor

- **Qualitative comparison in the case study uses a subjective selection protocol.** The paper states it "chose the parameters which looks best by eye" for competing methods in Figure 3. This is not reproducible and introduces evaluator bias. The visual superiority of TC-tSNE over alternatives is compelling, but the selection protocol weakens the comparison.

- **Only one temporal metric is used.** The quantitative evaluation uses a temporal Shepard diagram metric (over all time pairs) for temporal quality but three spatial metrics. The temporal Shepard diagram alone has limited diagnostic power — as the paper implicitly acknowledges by plotting it jointly with spatial axes. Incorporating additional temporal metrics (e.g., a temporal neighborhood hit or temporal trustworthiness) would strengthen the evaluation.

- **No ablation study over λ.** The paper's core claim is that enforcing temporal coherence over all time pairs yields better visualisations than short-range methods. A simple ablation varying λ on multiple datasets, showing how spatial and temporal metrics trade off and demonstrating that the method dominates the Pareto frontier rather than just sliding along it, would directly substantiate the central thesis. This is particularly important for distinguishing TC-tSNE's all-pairs objective from a carefully-tuned velocity-penalised baseline.

- **The choice of SNE (not t-SNE) for the temporal cost is justified but untested.** The paper says t-SNE "induces clustering which is not necessarily meaningful in the temporal domain" (Section 4). This is a plausible rationale, but no ablation compares the SNE temporal cost against a t-SNE temporal cost to verify the claim empirically.

- **No runtime or complexity analysis.** The paper mentions Barnes-Hut and FFT acceleration (Section 4, line 153) but provides no actual runtime measurements or complexity analysis. For a method whose gradient computation involves $T$ datasets of $n$ points and $n$ datasets of $T$ points, this is a notable omission for practitioners evaluating practical feasibility.

- **No discussion of limitations or failure cases.** The conclusion (Section 7) does not discuss scenarios where TC-tSNE's notion of temporal coherence may be inappropriate (e.g., when data-point identity changes meaning over time, or when the same entity is not perfectly tracked across frames). A brief limitations paragraph would strengthen the paper.

- **Claim of generality is asserted but not demonstrated.** The paper states the strategy "can be plugged into any neighbor embedding algorithm with little modification" (Section 3.2) but demonstrates it only with t-SNE. A companion UMAP variant — even without full quantitative evaluation — would substantiate the generality claim.

### Trivial
None.

---

## Nice-to-Haves

- The quantitative evaluation would benefit from including D-tSNE for the case study datasets where it can be run (the paper correctly notes that the primary school data has missing values, but this is a case-study limitation, not a general one). Note: D-tSNE **is** included in the quantitative benchmark (Section 6 lists it among compared methods), so this does not apply to the quantitative evaluation.

---

## Removed Points

- **"D-tSNE is excluded from the quantitative results because it cannot handle missing values."** — Factually wrong. The paper states D-tSNE could not be applied to the *case study* (primary school network) due to missing values. In the quantitative evaluation (Section 6, line 176), D-tSNE is explicitly listed as a compared method across all six benchmark datasets. The reviewer conflated these two sections.

- **"Neighborhood metric is not clearly defined."** — The paper specifies: "we report the average of these four metrics [neighborhood preservation, neighborhood hit, trustworthiness, continuity]... We call the value the neighborhood metric" (Section 6, lines 182–183). This is clearly stated.

- **"The temporal Shepard diagram metric has limited diagnostic power" as a standalone complaint.** The paper acknowledges the trade-off by plotting it against spatial metrics. This is a reasonable design choice for two-axis evaluation. Removed as an area-of-concern sweep rather than a specific actionable criticism.

- **General formatting/style nitpicks** — removed per policy (parser artifacts, not author errors).

- **Reproducibility nitpick about undisclosed optimisation details.** The paper references the original t-SNE optimisation (vanilla gradient descent with momentum, early exaggeration) and points to references for accelerated variants. This is standard practice for t-SNE work and does not warrant a weakness.

---

## Novel Insights

The structural-temporal duality framing (Section 3.1–3.2) is the paper's most intellectually interesting contribution and is worth highlighting beyond the paper's own discussion. By defining temporal coherence as the exact transpose of spatial coherence (swapping the data-point and time indices), the paper reveals that these two criteria are not fundamentally different objectives but rather the same relational-preservation objective applied over different axes of the data tensor. This insight cleanly explains why an additive decomposition of the cost function (Equation 3) is natural rather than ad-hoc, and it immediately implies that the method inherits any theoretical or practical properties of the base neighbor-embedding algorithm. This framing could plausibly generalise beyond visualisation to other problems involving multi-index data tensors where coherence along one axis is desired.

---

## Suggestions

1. **Add multiple restarts with error bars.** Run each method 5–10 times with different random seeds and report mean ± std for all metrics. This is the single highest-leverage improvement.
2. **Document hyperparameter tuning explicitly.** State the ranges of λ, μ, and ῦ tested for TC-tSNE across the six benchmark datasets, and describe the selection criterion (e.g., held-out temporal frames, validation metric).
3. **Include an ablation study over λ** on at least 2–3 datasets, showing the spatial-temporal Pareto front and demonstrating that TC-tSNE's all-pairs objective produces a different trade-off curve from tuning a short-range method.
4. **Replace or supplement the "by eye" parameter selection** for competing methods in the case study with a principled protocol, such as optimising for the temporal Shepard metric or grid-searching over reasonable ranges.
5. **Add one additional temporal metric** (e.g., a temporal version of neighborhood preservation or trustworthiness) to strengthen the temporal evaluation.
6. **Include a brief limitations paragraph** in the conclusion, discussing computational scaling and scenarios where the method may not be appropriate.

---

## Score and Decision

The paper introduces a well-motivated, elegant variant of t-SNE with a principled duality framework, a compelling qualitative demonstration on real dynamic network data, and competitive quantitative results. The main weaknesses — lack of error bars, underspecified hyperparameter tuning, and the absence of several ablations — are evidential rather than structural. The claims are appropriately modest ("performs competitively"). The contribution is genuine and clearly communicated. On balance, the paper merits acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>