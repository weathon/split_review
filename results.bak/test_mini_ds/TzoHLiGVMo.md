## Summary

The paper introduces ODEFormer, the first transformer capable of inferring *multidimensional* ODE systems in symbolic form from noisy, irregularly sampled trajectory data. It also presents ODEBench, a curated benchmark of 63 ODEs from the literature (1D–4D). Through extensive experiments, ODEFormer consistently outperforms GP-based and other baselines (PySR, AFP, SINDy, ProGED, etc.) across noise levels and subsampling conditions, while running orders of magnitude faster than all non-SINDy methods.

---

## Strengths

1. **First transformer for multidimensional dynamical SR.** The paper demonstrates that ODEFormer handles dimensions ≥2 for ODE symbolic regression, which prior transformer-based work (Becker et al. 2023) explicitly could not (limited to 1D). The system generates random ODEs up to 6D during training and evaluates on up to 4D in the benchmark.

2. **Introduction of ODEBench, a substantial new benchmark.** ODEBench contains 63 ODEs (1D–4D) curated from real-world phenomena in Strogatz (2000) and Wikipedia, with proper integration, two initial conditions per system, and public release. This addresses the severe limitations of the existing 7-system, 2D-only Strogatz dataset and provides a more holistic testbed for the community.

3. **Consistent SOTA across noise and subsampling levels.** On both Strogatz and ODEBench, ODEFormer achieves the highest average accuracy, with the largest advantage at high noise levels where GP methods degrade sharply (Figure 3). The advantage is robust across two subsampling ratios and six noise levels.

4. **Generalization evaluation on unseen initial conditions.** The paper explicitly evaluates not just reconstruction but also generalization to new initial conditions (Figure 4, Figure 5), an evaluation criterion absent from prior dynamical SR work. This provides a more meaningful measure of whether the symbolic ODE captures true dynamics rather than just fitting the observed trajectory.

5. **Faster inference.** ODEFormer runs in seconds, whereas GP methods and ProGED require minutes per system. This is a concrete practical advantage for any application requiring rapid equation discovery.

6. **Honest and thorough limitations discussion.** Section 7 explicitly acknowledges limitations (first-order only, all variables observed, struggles with chaotic systems, single-trajectory inference) and suggests concrete directions for addressing each, which strengthens confidence in the authors' understanding of their method's scope.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Baseline operator library configuration is underspecified.** The paper states that "for each baseline model, we perform a separate hyperparameter optimization for each run to ensure maximal fairness," but the reported hyperparameter search only covers derivative estimation (approximation order, Savitzky-Savgol filter). For GP methods (AFP, FE-AFP, EHC, EPLEX, PySR) and ProGED, the choice of operator library is a critical input that directly determines whether a method can express the correct skeleton. The paper does not explicitly state whether baselines were given the same operator set as ODEFormer's training vocabulary (sin, 1/x, x², +, ×). Without this detail, readers cannot fully assess whether the comparison is on equal footing. *This is addressable by providing the actual operator lists in a table.*

2. **Rescaling by initial value is undefined for zero-valued initial components.** The rescaling step divides each observed variable by its initial value: $\tilde{x}_i(t) = x_i(t) / x_i(t_0)$. This is undefined if any component of the initial condition is zero. The paper does not discuss this case or any workaround (e.g., adding a small epsilon, rescaling by max absolute value instead). While it likely does not affect most ODEBench examples, it is a robustness gap that should be acknowledged and handled.

3. **Variance/repeatability information is limited.** The box plots show distributions across benchmark examples but it is unclear whether multiple stochastic inference runs (different random seeds, beam sampling variations) were performed. Reporting statistics over multiple runs would strengthen the reliability of the reported results.

### Trivial
None.

---

## Nice-to-Haves

- **Analysis of generalization failures.** The paper notes that generalization accuracy drops by roughly half relative to reconstruction across all methods. A breakdown of what the failed generalizing predictions look like (e.g., correct skeleton but wrong constants vs. wrong operators) would provide deeper insight into where the method falls short and would support the claim that the model is "inferring laws" rather than fitting trajectories. Currently this striking result is reported but left unanalyzed.

- **The 90% filtering threshold for low-oscillation examples is a potential distribution bias.** Discarding 90% of non-oscillating systems means the model is primarily trained on oscillating or slowly diverging trajectories, but many real-world systems converge to fixed points. An experiment showing performance on non-oscillating test examples would clarify whether this bias matters in practice.

---

## Removed Points

*These points from the inputs were removed with justification:*

- **Generalization gap undermines headline accuracy claim** (from Harsh Critic, Weakness #2). The paper *already acknowledges* this gap in Section 6 ("Consistently across all models, accuracies drop by about half, meaning that half the correctly reconstructed ODEs do not match the ground truth symbolically. This highlights the importance of evaluating dynamical SR on different initial conditions."). The paper does not conflate reconstruction with identification; it explicitly uses both metrics and discusses their relationship. The critic's framing implies a deception that does not exist. The request for deeper analysis is valid but belongs in Nice-to-Haves.

- **Missing variance bars on Figure 2 ablation** (from Harsh Critic notes). The reviewer attributes this as a weakness, but box plots inherently show distributional information. The paper says it averages over 10,000 examples per panel. This is a minor presentation preference, not a weakness.

- **SINDy library not specified** (from Harsh Critic). The appendix (stripped from the extracted text) likely contains this detail; the paper states "for more details, please refer to \cref{app:baselines}." The parser strips appendices.

- **Strawman: complexity metric criticism** (from Harsh Critic). The paper *itself* acknowledges that counting constituents is crude ("We acknowledge that this is a crude measure...") and notes that it follows common practice in the literature. The critic is critiquing the paper for a limitation the paper already identifies.

- **Strength Finder generic strengths removed.** Claims like "addressing an important problem" and generic praise without specific content anchors were removed.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the authors do not already articulate in their discussion of limitations and future work.

---

## Suggestions

1. **Add a table specifying the exact operator library / basis set provided to each baseline** (GP methods, SINDy, ProGED) and confirm it matches ODEFormer's training vocabulary, or justify any mismatch.
2. **Handle the zero-initial-condition rescaling edge case** — either by switching to max-value rescaling or adding a small epsilon, with a brief experiment or comment.
3. **Add a one-paragraph analysis** categorizing generalization failures (correct skeleton + wrong constants vs. wrong operators) to help readers interpret the 50% gap.
4. **Report statistics over multiple inference runs** (e.g., 5 random seeds) for ODEFormer's beam sampling to quantify stochastic variability.

---

## Score and Decision

**Calibration Report**

*Round 1 bracket:* 5–7.5 (inferred from comparing weak anchors at ~2–3, middle anchors at 4–7, and strong anchors at 8).

*Comparisons to anchors (all calibration corpus paths relative to calibration directory):*

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|-------------------------|
| PI-NDSR (RdFpj6z4nE) | 5.67 | 1 | Weaker — GP+NN for network dynamics, limited to 1D node states, rejected by reviewers |
| PROSE (12zKEh2APn) | 5.33 | 1 | Weaker — only 15 ODEs, no proper baselines, less thorough evaluation |
| LLM-SR (m2nmp8P5in) | 8.00 | 1 | Stronger — leverages LLM priors, real-world evaluation across 3 domains, accepted with 8/8/8/8 |
| MDLformer (ljAS7cPAU0) | 5.67 | 1 | Comparable in quality but for functional SR, not dynamical SR (different problem) |
| KinFormer (nhrXqy5d5q) | 6.00 | 2 | Slightly weaker — domain-specific (chemical kinetics), only 20 systems, accepted but with split scores (8,5,8,3) |
| No Equations Needed (kbm6tsICar) | 6.50 | 2 | Similar quality — different approach (semantic rather than symbolic), limited to 1D, accepted with good scores |
| Zero-shot Imputation (NPSZ7V1CCY) | 6.25 | 2 | Different task (imputation vs. equation discovery), similar scope of contribution |

*Narrowing:* The paper is stronger than PROSE (5.33) and PI-NDSR (5.67) due to handling multidimensional systems, introducing a substantial benchmark (63 ODEs), and comparing against more baselines. It is comparable to or slightly stronger than KinFormer (6.0) because it is domain-agnostic and has a larger benchmark. It is comparable to the "No Equations Needed" paper (6.5) in overall quality, though the contributions are in different directions. It is not at the level of LLM-SR (8.0).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>