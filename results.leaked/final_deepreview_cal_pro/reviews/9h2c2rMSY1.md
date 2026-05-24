Now I have a thorough understanding of the paper and good calibration anchors. Let me synthesize the final review.

---

## Summary

This paper proposes a weighted conformal prediction (CP) framework for uncertainty quantification in time-dependent PDE surrogate models. The authors prove that in function space, solution distributions at different times are mutually singular (TV=1), making exact CP impossible. They then derive explicit Gaussian marginal distributions for discretized linear PDE solutions with Gaussian initial conditions (Theorem 4.2) and propose likelihood-ratio weights for weighted CP based on these marginals. Experiments on synthetic PDEs demonstrate that the method maintains target coverage while naive CP and LSCI baselines fail under temporal distribution shift.

## Strengths

- **Theorem 4.1 (TV = 1 in function space)** provides a rigorous negative result showing that even for the simple heat equation with Gaussian initial conditions, solution distributions at any two distinct times have maximal total variation distance. This cleanly motivates the shift to a discretized setting and is a genuinely non-obvious theoretical contribution (Section 4.2, Appendix A.2).

- **Theorem 4.2 (explicit Gaussian laws for discretized solutions)** derives closed-form mean and covariance for the discretized solution of linear PDEs under Gaussian initial conditions. This is a useful result that directly enables computation of density ratios between any two time points (Section 4.3).

- **Strong empirical validation**: Figure 3 and Table 1 show WCP consistently maintaining near-target coverage across a sweep of PDE parameters ($a \in \{-0.005, -0.0075, -0.01\}$, $c \in \{-0.5, 0, 0.5\}$) and prediction horizons, while naive CP and LSCI degrade severely as the PDE becomes more unstable. The transparent reporting of $n_\infty$ (fraction of infinite-band samples) is a commendable practice.

- **Clear problem formulation**: Section 4.1 maps time-dependent PDEs to evolving pushforward measures, providing a clean mathematical foundation for analyzing why exchangeability breaks. The failure analysis of local exchangeability (Section 2, Figure 2) empirically demonstrates that fine time discretization alone cannot salvage coverage.

## Weaknesses

### Major

- **Insufficient theoretical justification for the weighted CP weights (Equation 1)**. The paper uses the ratio of marginal densities of the PDE solution $\mathbf{u}_t$ as weights for weighted CP. However, the conformal score (maximum absolute error) depends on the pair $(\mathbf{u}_0, \mathbf{u}_t)$, and weighted CP requires the likelihood ratio between the joint calibration and test distributions of the full data point that enters the score. The joint distributions of $(\mathbf{u}_0, \mathbf{u}_t)$ at different times are supported on different $n$-dimensional affine subspaces of $\mathbb{R}^{2n}$ and are mutually singular with respect to Lebesgue measure on $\mathbb{R}^{2n}$, so a density ratio does not exist in the standard sense. The paper provides no derivation connecting the marginal $\mathbf{u}_t$ density ratio to the correct importance weights for the score distribution. The claim of "exact coverage guarantees" (Section 4.4, line 228; also Abstract and introduction) is therefore not adequately supported by the theory presented. The empirical results suggest the weighting is effective in practice, but the theoretical gap between Theorem 4.2 (which is correct) and the claimed CP guarantees must be addressed — either through a proper derivation or by qualifying the claim as empirically supported.

- **Test-point weight depends on the unknown response**. Equation (1) states that weights are computed for "all $\mathbf{u}_i$ belonging to the calibration set together with the target test point." The test-point weight depends on $\mathbf{u}_{t+\delta}$, the unknown future solution. The paper does not discuss how this weight is evaluated in practice, leaving the CP procedure under-specified. This issue compounds the first: even if the weighting scheme were theoretically valid, the implementation for the test point is unresolved without additional mechanism (e.g., a grid over candidate responses).

### Minor

- **The connection between the function-space TV result (Theorem 4.1) and the discretized method is asserted rather than derived**. The paper argues that discretization "mitigates" the mutual singularity issue (Section 4.2, final paragraph), but the transition lacks rigor: the same mutual singularity in the joint distributions persists after discretization, which is directly relevant to the weighted CP framework. A more precise discussion of what changes in the discretized setting and why this enables the proposed approach would strengthen the narrative.

- **Experimental setup details are deferred to the appendix** (Section 5: "more details in appendix A.5"). The main text does not specify the calibration time $t$, how prediction horizons map to $\delta$ values, or the model training procedure. While appendices exist in the original submission, the core experimental argument should be self-contained enough to assess without them.

## Nice-to-Haves

- A comparison against a baseline that estimates distribution shift from data (e.g., a density-ratio estimator applied to the calibration scores directly) would help contextualize the value of the PDE-derived closed-form weights versus a purely data-driven approach.
- Reporting overall coverage *including* samples where infinite bands are returned (i.e., trivial coverage of 1.0), in addition to the already-reported conditional coverage, would give a more complete picture of practical utility.
- Extending the analysis beyond linear PDEs (acknowledged in Section 6) and beyond Gaussian initial conditions to the location-scale family (noted in Remark 4.3 but not empirically tested in the main text) would broaden applicability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic claim about "mutual singularity in discretized space making likelihood ratio impossible"** — This point is substantially correct as a theoretical observation, but the critic frames it as fatally invalidating the entire method. The empirical evidence shows the weighting works in practice. The theoretical gap is real and has been retained as a Major weakness above, but the critic's assertion that the paper "cannot be accepted" based on this alone overstates the case given the paper's other contributions (Theorems 4.1 and 4.2, strong empirical results).

- **Harsh critic claim that "the paper does not rigorously connect the negative function-space result to the choice of a discretized approach"** — Demoted from "structural" to Minor. The narrative connection (function-space TV=1 motivates discretization) is conceptually clear even if not formally bridged.

- **Strength finder claim about "real-world test on pulsed-thermography dataset"** — The appendix containing these results is stripped. While the claim is plausible, I cannot verify the evidence. This does not count against the paper (the original submission includes the appendix), but I cannot use it as a strength either.

- **Harsh critic claim about "the reporting of coverage excludes samples for which infinite bands are returned, which inflates the apparent failure rate"** — The paper explicitly reports $n_\infty$ and discusses this caveat in Section 5. The reporting is transparent.

- **Harsh critic mention of missing related works** — Removed per instructions.

## Novel Insights

The paper's Theorem 4.1 — that the TV distance between solution distributions of the heat equation at any two distinct times is exactly 1 — is a clean and surprising result that crystallizes why function-space CP is fundamentally ill-posed for time-dependent PDEs, even in the simplest linear-Gaussian setting. This goes beyond the usual observation that "distributions drift" and provides a formal impossibility result that may be of independent interest to the neural operator community.

## Suggestions

- Reframe the weighted CP contribution: either provide a rigorous derivation of the correct importance weights (potentially by working directly in the space of initial conditions $\mathbf{u}_0$, where the score is a deterministic function of a fixed distribution), or explicitly present the method as a well-motivated heuristic with strong empirical support, backing off from claims of "exact coverage guarantees."
- Address the test-point weight issue by describing how the procedure is implemented in practice (e.g., is the test-point weight set to a fixed value? Is a grid search used?).
- Include a brief discussion of what conditions would be needed for the marginal $\mathbf{u}_t$ density ratio to serve as a valid proxy for the score-distribution importance weights.
- Move key experimental parameters (calibration time, prediction horizons, model architecture) into the main text for self-contained assessment.

## Score and Decision

**Calibration anchors:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| cF6OoaYcRa | 4.50 | R1 | Our paper is stronger: more theory, better experiments, more novel problem framing |
| 5KqveQdXiZ | 5.25 | R1 | Less relevant (constrained learning for PDEs, not CP); our paper has stronger empirical validation |
| vcX0k4rGTt | 5.75 | R1 | Comparable quality; our paper addresses a more novel problem but has a more significant theoretical gap |
| j511LaqEeP | 6.00 | R2 | Most comparable anchor (non-exchangeable CP). Similar level of contribution. Our paper has better empirical scope and domain-specific theory (Theorems 4.1, 4.2), but the theoretical gap in the CP weighting justification is more concerning than j511LaqEeP's incrementality criticism |
| aJ3tiX1Tu4 | 6.67 | R2 | Stronger theoretically; our paper has a more impactful application domain but weaker theoretical grounding |
| LgfaMR6Sst | 6.80 | R2 | Different topic (active learning for PDEs); not directly comparable |

**Round 1 bracket:** 4.5 – 6.8 based on topic-relevant anchors.

**Round 2 narrowing:** The paper sits below aJ3tiX1Tu4 (6.67) and around or slightly below j511LaqEeP (6.00), primarily due to the theoretical gap in the CP weighting. It is clearly above cF6OoaYcRa (4.50). This places it in the 5.0–6.0 range. The presence of two solid theorems, strong empirical results across a parameter sweep, and a well-motivated problem pulls it above the midpoint. The unresolved theoretical justification for the central CP claim pulls it below the stronger non-exchangeable CP papers. I settle at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>