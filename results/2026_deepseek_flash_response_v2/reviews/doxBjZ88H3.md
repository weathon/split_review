# Final Consolidated Review

## Summary

This paper proposes an information-theoretic framework for optimizing experimental designs to distinguish between two competing hypotheses about probabilistic neural coding in early sensory areas: likelihood coding (probabilistic population codes) and posterior coding (neural sampling codes). The key contribution is the derivation of the "information gap" — a KL-divergence-based measure quantifying the expected decoder performance difference under each coding hypothesis for a given stimulus distribution. The paper validates the theory through simulations with synthetic neural populations and demonstrates how maximizing the information gap yields task parameter recommendations. The framework addresses a genuine open problem in computational neuroscience.

## Strengths

1. **Closed-form analytic derivation of the information gap (Eqs. 1-5, Section 2):** The paper derives explicit formulas for the expected decoder performance difference under both likelihood and posterior coding hypotheses. The key insight — identifying Bayes-optimal estimators under mismatched decoding (Eq. 2 for posterior-decoding on likelihood-coding populations, Eq. 5 for likelihood-decoding on posterior-coding populations) — converts an ill-posed experimental design question into a concrete, computable objective. Prior work identified the experimental challenge but lacked this analytic machinery.

2. **Comprehensive simulation validation across diverse conditions (Figures 3-4, Section 3):** The theoretical information gap predictions closely match empirical decoder performance differences across three contrast levels, multiple task parameter sets, and two different neural models (standard Poisson and the more bio-realistic gain-modulated Poisson). Figure 4 shows tight clustering along the diagonal across 12 subplots, and Figure 3 confirms convergence with increasing trials and neurons. This establishes predictive validity across the relevant parameter space.

3. **Information gap landscape analysis yields non-obvious insights (Figures 5-6, Section 4):** By mapping the 2D parameter space of prior separation and standard deviation, the paper reveals that optimal parameters differ between the two hypotheses, necessitating strategic compromise designs. The analysis of heavy-tailed priors (student's t, Cauchy) showing near-zero posterior-coding information gap provides useful negative guidance, with a mechanistic explanation rooted in Eq. 4.

## Weaknesses

### Major

1. **Validation is self-consistent rather than independently probative.** The simulations generate synthetic data from Poisson spiking models whose generative process (p(x|θ), Gaussian tuning curves, context priors) exactly matches the assumptions baked into the theoretical derivation of the information gap. This confirms the math is correct and the neural network decoders approach optimality with sufficient data — but it does not validate that the framework would successfully discriminate the two coding hypotheses in a real biological preparation. The only real-data test (Section 5, Allen Institute dataset) confirms the trivial null prediction that Δ=0 under a uniform prior. This is a necessary sanity check but not a strong validation. The paper lacks any retrospective analysis of an existing multi-context dataset where the framework's predictions could be tested, or any demonstration that the optimized parameters would yield measurably different experimental outcomes than heuristic designs. Since the paper's title and framing promise "optimizing experimental design," this gap between theoretical derivation and demonstrated practical utility is the most significant limitation.

### Minor

2. **No quantitative comparison against alternative (heuristic) experimental design strategies.** The paper argues that heuristic approaches (e.g., maximally different priors) are suboptimal and explains why ("this would limit stimulus overlap across contexts and thus prevent observing how different context priors modulate neural population responses to identical stimuli"), but never demonstrates this quantitatively. A small simulation comparing the discriminative power of optimized vs. heuristic designs would make the case concretely. The "strategic sweet spots" in Section 4.1 are identified by visual inspection of the landscape rather than a formal optimization criterion.

3. **The notation for the information gap is inconsistent across sections.** The paper uses Δ_L^info (Eq. 1) for likelihood coding, Δ_p^info (Eq. 3) for posterior coding, and Δ_info^post / Δ_info^lik (Section 4.1). On line 125 both the likelihood-coding and posterior-coding information gaps are typeset as Δ_p^info — a clear typo where the first should be Δ_L^info. In a paper whose central contribution is a quantitative measure, this inconsistency is distracting.

4. **Limited exploration of generative model sensitivity.** The paper uses Gaussian p(x|θ) and Gaussian tuning curves throughout. How sensitive the optimal task parameters (e.g., d≈30°, σ≈20°) are to the choice of generative model is not analyzed, which limits confidence in the generality of the specific parameter recommendations.

### Trivial

5. **The posterior-coding derivation depends on a condition (Eq. 4) that is acknowledged to make Δ_P^info an order of magnitude smaller than Δ_L^info, but the paper does not quantify how frequently such matching observation pairs arise in practice.** The heavy-tailed prior analysis (Section 4.2) provides some indirect insight, but a direct analysis would strengthen the practical guidance.

## Nice-to-Haves

- **Power analysis translating Δ values to sample size requirements:** The framework would be more directly actionable if it translated information gap values (in nats) into concrete experimental design guidance such as "for Δ = X nats, N trials and M neurons are needed to achieve statistical power 0.8 at α = 0.05." This could leverage the existing simulation infrastructure.
- **Formalizing the sweet-spot selection:** Rather than visually identifying tradeoff points, the paper could define a scalar objective (e.g., maximize the minimum information gap across both hypotheses, or minimize the larger of the two hypotheses' Type II error rates) and solve for optimal parameters explicitly.

## Removed Points

- Criticism about missing code release: removed per instruction (not to question existence/availability of cited resources).
- Criticism about fixed-point iteration convergence not being discussed in main text: the paper explicitly references Appendix A.1 for details. The appendix is stripped by the parser.
- Criticism about framework not being "actionable" in a general sense: weakened to Nice-to-Have. The paper does provide specific parameter recommendations (d≈30°, σ≈20°) and the landscapes are actionable for experimental design choices.
- Criticism about "binary framing" of likelihood vs. posterior coding: the paper explicitly acknowledges mixed hypotheses in the Discussion (Section 6) and Appendix A.5.
- Strength Finder's strength #4 about empirical confirmation on real data: kept but properly contextualized as a null result (Δ=0 under uniform prior) — it is a valid sanity check confirming theory, not an independent validation.

## Novel Insights

The main insight beyond the paper's own contributions is the observation that the information gap asymmetry (Δ_L^info >> Δ_P^info) has a clear structural explanation: for likelihood-coding populations every observation contributes, while for posterior-coding populations only observation pairs whose posteriors match (Eq. 4) contribute. This asymmetry is inherent to the problem and forces experimenters to prioritize designs that maximize posterior-coding discriminability, since the likelihood-coding side is easier to detect. The heavy-tailed prior analysis (Section 4.2) showing near-zero posterior-coding Δ is a concrete consequence that would not be obvious from intuition alone.

## Suggestions

1. **(Most impactful) Apply the framework to at least one existing multi-context neural dataset** if any can be identified, or simulate a realistic experiment comparing optimized vs. heuristic designs to demonstrate that the framework yields superior discriminative power. This would transform the paper from "here is a theoretical framework" to "here is a framework that demonstrably works for experimental design."
2. Fix the notation inconsistency on line 125 (both gaps labeled Δ_p^info) and unify notation across sections.
3. Add a small quantitative comparison against heuristic designs (e.g., maximally different priors, uniform priors) to show that optimizing Δ yields measurable improvements in discriminative power.

## Score and Decision

**Calibration anchors:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|-----------|
| sJAlw561AH (Uncertainty-Perception Tradeoff) | 5.50 | R2 | Closest structural match — information-theoretic framework paper criticized for lacking practical demonstration. Our paper has stronger simulation validation but shares the gap in proving practical utility. |
| S5aUhpuyap (Complex priors, flexible inference) | 5.75 | R1 | Theoretical neuroscience paper accepted despite toy data and biological plausibility concerns. Our paper has more thorough validation but the core weakness (lack of real-world demonstration) is more central to our paper's claims. |
| 4GfEOQlBoc (Image Statistics & Perception) | 5.25 | R1 | Perception paper criticized for methodological gap between claims and evidence. Our paper similarly has a gap between "optimizing experimental design" framing and actual demonstration. |
| At9JmGF3xy (Generalizing Brain Decoding) | 5.75 | R2 | Empirical paper with established comparisons. More practically grounded but less theoretically novel. |
| zxO4WuVGns (Inverse Decision-Making) | 6.00 | R1 | Practical method paper with real data validation. Our paper is stronger theoretically but weaker empirically. |
| 0kWd8SJq8d (MINDE) | 6.50 | R2 | Strong empirical validation and benchmark comparisons. A higher bar that our paper does not reach in terms of demonstrated practical utility. |

**Round 1 bracket:** (4.5, 7.0) — clearly above the weak band (~3) and below the strong band (~8).

**Round 2 narrowing:** Compared to the most structurally similar anchor (sJAlw561AH, 5.50, Reject), our paper has stronger simulation validation but shares the core weakness: the framework's practical utility is asserted rather than demonstrated on real data. Compared to S5aUhpuyap (5.75, Accept), our paper has more thorough validation but less novelty in the proposed biological mechanism.

This is a genuine theoretical contribution with clear writing and competent execution. However, the gap between what the paper's title and framing promise ("optimizing experimental design") and what is actually delivered (theoretical bounds validated on self-consistent simulations, with a null-result real-data test) is significant enough to warrant rejection in its current form. The paper reads as a well-executed first half of a two-part project: the theoretical framework is established, but the practical demonstration of its utility for actual experimental design is deferred. A substantially strengthened version — ideally with retrospective analysis on multi-context data or a formal comparison against heuristic designs — would be a strong contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>