## Summary

This paper develops an information-theoretic framework for designing experiments to distinguish between likelihood-coding (e.g., probabilistic population codes) and posterior-coding (e.g., neural sampling) hypotheses about probabilistic representations in sensory neural populations. The central contribution is the **information gap**—the expected difference in decoder cross-entropy between optimal likelihood and posterior decoders—which is derived analytically for both coding hypotheses (Eqs. 1–5), validated on simulated Poisson and gain-modulated Poisson populations (Figs. 3–4), and used to compute information gap landscapes over task parameter spaces for optimizing stimulus prior distributions (Figs. 5–6).

---

## Strengths

- **Clean theoretical derivation of a needed quantity.** The paper provides closed-form expressions for the information gap under both coding hypotheses, giving a theoretically grounded measure for quantifying how distinguishable two probabilistic coding hypotheses are under a given task design. This fills a genuine gap: prior work lacked a quantitative, principled metric for comparing experimental designs for this specific question.

- **Strong simulation validation.** Figs. 3 and 4 provide compelling evidence that the theoretical information gap accurately predicts the *empirical* decoder performance difference across diverse settings (three contrast levels, two neural models, wide range of task parameters). The near-perfect alignment with the identity line in Fig. 4 is the paper's strongest result and convincingly establishes the validity of the framework within its simulation domain.

- **Well-motivated, timely problem.** The paper addresses an open question in computational neuroscience—whether early sensory populations encode likelihood functions or posterior distributions—that has remained unresolved in part because there was no quantitative way to determine which experimental design would be most informative. The paper articulates the tradeoff (sufficient prior difference vs. sufficient stimulus overlap) clearly.

- **Useful null result on real data.** The Allen dataset analysis (Fig. 7) shows that single-context experiments produce a decoder performance difference indistinguishable from zero, confirming the theoretical prediction and motivating the need for multi-context designs. This is a clean sanity check.

---

## Weaknesses

### Major

1. **No analysis connecting information gap magnitudes to practical experimental feasibility.** The paper notes that Δₚₒₛₜ is typically 0.0–0.06 nats—an order of magnitude smaller than Δₗᵢₖ (0.0–0.6 nats)—but provides no guidance on whether such small gaps are practically detectable. An experimentalist needs to know: given a predicted Δ of, say, 0.03 nats and realistic neural variability, how many trials and neurons are needed to detect a statistically significant decoder performance difference? The convergence curves in Fig. 3 show *mean* convergence to the theoretical value but do not address the detection problem at finite sample sizes. Without this connection, the framework identifies theoretically optimal designs but cannot tell an experimentalist whether those designs are practically feasible within realistic recording constraints. This is the most consequential gap given the paper's stated goal of enabling experimental design.

2. **Absence of positive empirical validation.** The only real-data result (Fig. 7) is a null finding that is consistent with the framework but does not *positively* validate it. The paper would be substantially stronger if it included any demonstration that the framework can make falsifiable predictions that are borne out in data—for example, using the framework to predict which of two held-out task designs produces a larger empirical decoder performance difference, then testing that prediction.

### Minor

1. **Qualitative rather than formal design optimization.** The "strategic selection" of sweet spots (asterisks in Fig. 5) is described as "where posterior-coding information gap approaches its maximum while likelihood-coding maintains sufficient discriminative signal." What counts as "sufficient" is not defined, and no decision criterion (e.g., maximizing a weighted combination or the minimum of the two scaled gaps) is formalized. The landscapes themselves are the substantive contribution, but the selection procedure as described is not reproducible. The paper's headline claim of "principled optimization" would be better served by an explicit objective function.

2. **Limited discussion of discretization sensitivity for Δₚₒₛₜ.** The derivation of Δₚₒₛₜ depends on identifying observation pairs (xⱼ, xₖ) satisfying pᴬ(θ|xⱼ) = pᴮ(θ|xₖ). The framework is formulated for discretized observations from the start, and the simulation results confirm empirical validity at the chosen resolution. However, the paper does not discuss how discretization resolution is selected or whether the computed Δₚₒₛₜ is stable with respect to resolution changes—a natural question for anyone applying the framework to a new stimulus domain.

3. **Limited exploration of model sensitivity.** The landscapes are computed for specific generative model parameters (tuning curve widths, noise distributions). Since the generative model must be estimated from pilot data, it would be valuable to know whether the optimal task parameters change substantially under moderate misspecification. No sensitivity or robustness analysis is provided.

### Trivial

None.

---

## Nice-to-Haves

- A formal optimization objective for selecting sweet spots (e.g., maximize the minimum of the two information gaps after scaling by their respective ranges).
- A brief sample-size analysis using the simulation framework to produce operating characteristic curves for a few representative scenarios.
- A sensitivity analysis showing how robust the identified optimal designs are to moderate misspecification of generative model parameters.
- Discussion of how the framework could be used iteratively (pilot → estimate model → optimize → full experiment).

---

## Removed Points

The following criticisms from the input reviews were removed as they are either misunderstandings, scope creep, or unsupported by the available text:

1. **Criticism about decoder context access** (Harsh Critic): The reviewer suggested the posterior decoder should use context labels since "context is explicitly cued." The paper states context is cued to the *subjects*, not to the decoders. Decoders (Fig. 2C) take population responses as input; for likelihood-coding populations, responses are context-independent, so the optimal posterior decoder correctly marginalizes over contexts. This is a misunderstanding of the experimental setup.

2. **Criticism about missing comparison with alternative methods** (Harsh Critic): Demanding a comprehensive comparison with all potential approaches for distinguishing coding hypotheses is scope creep not required for evaluating this specific framework.

3. **Criticism about handling uncertain generative models** (Harsh Critic): The paper acknowledges this limitation ("requires reasonable generative models"). A full treatment is beyond the paper's scope.

4. **Criticism that the mixed-hypotheses extension is undeveloped** (Harsh Critic): The paper explicitly states this is discussed in Appendix A.5 and Fig. 11, which are stripped by the parser. The authors do address this.

5. **Strength Finder strength about "principled optimization yielding sweet spots"**: Overstates the paper's contribution given the qualitative selection procedure. The landscapes are valuable, but calling this "principled optimization" inflates what is actually demonstrated.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that substantially reframes or deepens the paper's own narrative.

---

## Suggestions

1. **Add a sample-size analysis.** Use the simulation framework to generate, for a few representative scenarios, curves showing the number of trials/neurons required to detect a statistically significant decoder performance difference as a function of the predicted information gap. This directly addresses the most critical gap for experimentalists.

2. **Formalize the design optimization.** Replace the qualitative sweet-spot selection with an explicit objective function (e.g., maximize the minimum of Δₗᵢₖ and Δₚₒₛₜ scaled by their achievable ranges, or maximize a weighted sum). This would make the selection reproducible and the "principled" claim substantive.

3. **Include a sensitivity/robustness analysis.** Show how the optimal task parameters shift under moderate misspecification of generative model parameters (e.g., tuning curve width, noise level). This would help experimentalists understand how robust the design recommendations are to the unavoidable uncertainty in pilot model estimates.

---

## Score and Decision

**Calibration procedure.** Round 1 (bracketing) used three queries covering low (score < 3.5), middle (3.5–7.5), and high (7.5+) ranges with topically similar papers. Low-band anchors averaged ~3.0 (clearly weaker than the current paper), high-band anchors averaged 8.0–9.0 (clearly stronger). The initial bracket was set to 5–7. Round 2 (narrowing) used queries for computational-neuroscience theory papers with scores between 4.5 and 7.5. Anchors in this range included: "Inverse decision-making using neural amortized Bayesian actors" (6.00, Accept), "Complex priors and flexible inference in recurrent circuits" (5.75, Accept), "Complementary Coding of Space with Coupled Place Cells and Grid Cells" (5.33, Reject), "Beyond single neurons: population response geometry in digital twins" (6.33, Accept), and "Manipulating dropout reveals an optimal balance" (6.00, Accept). The current paper is stronger than the 5.33 anchor (better validation, more timely problem) but weaker than the 6.00 and 6.33 anchors (those papers have complete practical pipelines or positive empirical validation). It is comparable to the 5.75 anchor (clean theory with limited practical validation). The final score sits at 5.5—a contribution with genuine theoretical value and strong simulation support, but with practical gaps that prevent it from reaching the accept threshold.

**All anchor papers retrieved:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|------------------------|
| MNGMpHxi1I | 3.00 | 1 | Much weaker; unrelated topic |
| NYPJz0CL5X | 3.00 | 1 | Much weaker; unrelated topic |
| BBldjKEBlJ | 3.00 | 1 | Much weaker; different subfield |
| S3zKrEQpRr | 3.00 | 1 | Much weaker; unrelated topic |
| hbon6Jbp9Q | 2.33 | 1 | Much weaker |
| z2QdVmhtAP | 3.00 | 1 | Much weaker |
| fmWVPbRGC4 | 5.67 | 1 | Comparable; different subfield |
| APWIZgehDT | 6.00 | 1 | Stronger empirical validation |
| 905dpz8K73 | 5.33 | 1,2 | Slightly weaker; less well-validated |
| kSISSDUYFh | 6.33 | 1 | Stronger; real data validation |
| 4GfEOQlBoc | 5.25 | 1 | Comparable; more psychophysical |
| ADDCErFzev | 6.00 | 1 | Stronger; real neural data |
| cNmu0hZ4CL | 8.00 | 1 | Stronger; broader impact |
| kbjJ9ZOakb | 8.00 | 1 | Stronger; more complete |
| RWJX5F5I9g | 8.00 | 1 | Stronger |
| agPpmEgf8C | 8.00 | 1 | Stronger |
| Xo0Q1N7CGk | 8.00 | 1 | Stronger |
| nwDRD4AMoN | 9.00 | 1 | Stronger |
| SyPrLti4PG | 5.67 | 2 | Comparable; different subfield |
| BYUdBlaNqk | 5.25 | 2 | Slightly weaker |
| cWEfRkYj46 | 6.00 | 2 | Stronger practical validation |
| i4jHy0ewke | 4.67 | 2 | Weaker |
| zxO4WuVGns | 6.00 | 2 | Stronger; fully developed method |
| S5aUhpuyap | 5.75 | 2 | Comparable; theory with limited validation |
| UvfI4grcM7 | 6.75 | 2 | Stronger |
| vgt2rSf6al | 5.75 | 2 | Comparable; different domain |
| RyUvzda8GH | 5.25 | 3 | Comparable; different domain |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>