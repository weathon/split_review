## Summary

This paper proposes Phy-DRL, a framework with three "invariant-embedding" designs: (1) a residual action policy combining a linear model-based controller with a DRL policy, (2) a safety-embedded reward constructed via linear matrix inequalities (LMIs) that converts multi-dimensional safety constraints into a scalar reward, and (3) physics-knowledge-enhanced neural networks via Taylor-series input augmentation and structured weight/activation masking. The paper claims a mathematically provable safety guarantee, strict compliance of networks with physics knowledge, and provides experimental validation on a cart-pole system and a quadruped robot.

## Strengths

- **LMI-based systematic conversion of safety constraints to a scalar reward (Lemma 1, Theorem 1, Section 5)**. The paper provides a principled, offline-computable method for constructing a safety-embedded reward from polyhedral safety constraints. The connection between the safety envelope Ω (ellipsoidal), the safety set X (polyhedral), and the reward condition via LMIs is the most technically novel contribution and goes well beyond ad-hoc reward shaping. Unlike prior CLF-based DRL rewards (Westenbroek et al. 2022) that require manual design, this construction is systematic.

- **NN editing for enforcing partial physics knowledge in actor/critic networks (Theorem 2, Algorithm 2, Section 6)**. The structured weight masking and activation editing approach is a principled way to enforce that network outputs contain only monomials permitted by known physics knowledge sets. This addresses an open problem (defa3) that prior physics-informed NN methods cannot solve for DRL, because the action-value function lacks compact governing PDEs.

- **Honest discussion of core limitations in the conclusion (Section 8)**. The paper acknowledges that the safety guarantee depends on a linear model and that a faulty P may admit no safe policies, and that practical testing of the condition is future work. This candor is appreciated, even though these limitations should be flagged earlier and more prominently.

## Weaknesses

### Major

- **Main-text experimental validation is almost entirely qualitative**. The cart-pole experiment (Section 6.1) reports zero numerical metrics — no safety-violation counts, success rates, cumulative returns, convergence times, or run-to-run variance. The quadruped experiment (Section 6.2) similarly provides only phase plots with textual claims ("remarkably better velocity-regulation performance, fewer learning parameters, fast and stable training") backed by no numerical results in the main text. The paper deflects all quantitative evidence to appendices. For a top conference, claims of "guaranteed safety," "fewer learning parameters," and "fast training" require at minimum a summary table in the main paper (e.g., violation rates, parameter counts, velocity RMSE).

- **No ablation study isolates the three claimed innovations**. Three separate architectural designs are presented (residual policy, safety-embedded reward, NN editing), yet no experiment removes any component to measure its individual contribution. In particular, the NN editing mechanism (Algorithm ned) — which receives substantial algorithmic space — has zero empirical validation isolating its effect. There is no "Phy-DRL without NN editing" condition (e.g., replacing PKN-15 with a standard MLP while keeping the residual policy and safety reward). Similarly, no condition tests whether the residual structure alone (a_phy=0) would suffice. This makes it impossible to attribute any observed behavior to specific mechanisms and is a significant gap in experimental design.

- **Baseline comparison in the quadruped experiment is difficult to interpret without tuning details**. The DRL baseline receives 10× more training steps (10⁷ vs. 10⁶ for Phy-DRL) and fails in all environments. While this asymmetry could demonstrate sample efficiency, the more natural interpretation without tuning details is that the baseline may be poorly configured. The baseline also uses the same P matrix derived from Phy-DRL's own LMI formulation, meaning its reward is constructed from the proposed method's framework — a non-neutral setup. No information about hyperparameter optimization for either method is provided in the main text.

### Minor

- **"Provable safety guarantee" framing overstates what is proven**. Theorem 1 is a conditional statement: IF the realized sub-reward satisfies r ≥ α−1 ∀k, THEN safety follows. The paper's abstract and contributions sections phrase this as "a mathematically provable safety guarantee" without qualification, which is misleadingly absolute. The condition depends on the learned policy's behavior and is not automatically guaranteed. (The paper does provide empirical evidence that the condition holds in the cart-pole experiment, line 350, which partly addresses this — but the framing should be corrected.)

- **Linear model restriction is central but understated**. The entire theoretical framework — LMIs, safety envelope, model-based policy a_phy = F·s — assumes linear dynamics (A,B) with an unknown mismatch f. The paper acknowledges this only in the conclusion (line 393). No bound or analysis on tolerable mismatch magnitude ∥f∥ is provided, so there is no way to know for which classes of systems the method is applicable. The cart-pole experiment's explicit "large model mismatch" demonstrates the importance of this limitation.

- **NN input augmentation combinatorial growth not discussed**. Algorithm aug generates all non-redundant monomials up to order r. For the 12-state quadruped with r=2, this yields 91 monomials; with r=3, 455. For deeper layers the growth compounds. The paper does not discuss computational or memory implications.

### Trivial

None.

## Nice-to-Haves

- Add a "Phy-DRL without NN editing" ablation (standard MLP replacing PKN-15, keeping residual policy and safety reward) to isolate the editing mechanism's contribution.
- Provide a bound on tolerable model mismatch ∥f∥ or a condition under which the safety guarantee degrades gracefully.
- Report results across multiple random seeds with variance bars or intervals.
- Equalize baseline training steps or provide a performance-vs.-training-steps curve for fair comparison.

## Removed Points

All removed points are excluded with the following justifications (included here for completeness):

1. **Critic's complaint that the appendix "cannot be accessed":** Hard rule — the parser strips appendices from all papers. Do not penalize missing appendix content.
2. **Critic's claim that there is "no guarantee whatsoever" the learned policy satisfies r≥α−1:** The paper provides empirical evidence that this holds in the cart-pole experiment (line 350: "r(s(k), s(k+1)) ≥ α−1 holds in final training episode"). The conditional framing concern is retained as a Minor weakness, not escalated to Major/Fatal as the critic suggested.
3. **Strength finder's claim of "concrete evidence for fast training":** Overstated given the qualitative nature of main-text results. Retained as contextual support but removed the "concrete evidence" characterization.
4. **Critic's demand for a "Phy-DRL without model-based action" ablation:** Subsumed by the general ablation weakness; moved to Nice-to-Haves as one possible ablation direction.
5. **Strength finder's generic/superficial praise** (e.g., "this paper addressed an important problem"): These are not specific, evidence-grounded strengths.
6. **Critic's note about missing random seeds, hyperparameters in main text:** Partially addressed by appendix references. The main-text quantitative gap is covered by the Major weakness above.
7. **Critic's assertion that "no information about hyperparameter tuning for either method" makes comparison uninterpretable:** The training steps and network configuration details are provided; the concern is reframed as a Moderate-level issue about tuning transparency rather than a complete invalidation of the comparison.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add one quantitative table per experiment to the main text. For cart-pole: % trajectories within Ω, mean episode return, whether r≥α−1 held across episodes. For quadruped: velocity RMSE per environment, peak constraint violations, number of learning parameters, training steps to convergence.
2. Add at least one ablation: Phy-DRL with standard MLP replacing the physics-enhanced DNN (removing NN editing while keeping residual policy and safety reward).
3. Provide a training-time comparison curve (performance vs. steps) for all methods, or equalize training steps with proper justification.
4. Reframe the safety guarantee language throughout to clearly state it as a conditional safety certificate, not an unconditional guarantee of the learned policy's behavior.
5. Discuss the combinatorial cost of Taylor-series input augmentation for higher-dimensional systems.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>