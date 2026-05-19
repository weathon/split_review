- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8
Now I have thoroughly read the paper. Let me produce the final consolidated review.

## Summary

This paper introduces Conservative Density Estimation (CDE), an offline RL method that applies explicit pessimism in the stationary state-action occupancy distribution space. CDE combines a DICE-style marginal importance sampling framework with an explicit OOD density constraint (Eq. 5–7) to bound the concentrability coefficient and avoid the support mismatch problem that plagues prior DICE methods. The paper provides theoretical guarantees (bounded OOD importance ratios, performance gap decomposition) and demonstrates strong empirical results on D4RL tasks, particularly in sparse-reward and scarce-data settings where CDE substantially outperforms baselines when dataset size shrinks to 1% of trajectories.

## Strengths

1. **First explicit pessimism in the stationary distribution space.** The paper formulates a new constrained optimization (Eq. 4–6) that directly caps OOD state-action density via a dual variable λ, yielding closed-form solutions for the importance ratio and regularized advantage (Propositions 1–2). This is a principled departure from prior conservative methods that operate on Q-values and lack a direct handle on occupancy measure constraints.

2. **Automatic bounding of the concentrability coefficient.** Proposition 2 and Theorem 2 prove that CDE's OOD importance ratio is provably bounded without assuming bounded concentrability—a condition typically assumed in prior work (e.g., Rashidinejad et al., 2021). The bound depends on a hyperparameter, but the structure of the method *guarantees* bounded ratios, unlike prior DICE methods that can produce arbitrarily large ratios under support mismatch.

3. **Compelling performance under extreme data scarcity.** Figure 3 (sub-dataset experiments) shows that CDE maintains high rewards with only 1% of trajectories on Maze2D and sparse-MuJoCo tasks, while OptiDICE and all other baselines suffer sharp drops. This directly validates the paper's core claim that the OOD density constraint and mixed proposal distribution mitigate support mismatch—the fundamental weakness of prior DICE approaches.

4. **Performance gap bound with interpretable error decomposition.** Theorem 3 decomposes suboptimality into a state-marginal mismatch term and a sample-size-dependent term converging at rate \(N^{-1/(4+h)}\). This provides formal justification for why dataset quality and size matter, beyond what prior DICE or conservative methods offer.

5. **Disentangled value and policy learning.** CDE updates the policy only after the value function converges (Algorithm 1, lines 4–8 vs. 10–12), avoiding the interleaved optimization errors typical of actor-critic methods. The empirical advantage over AlgaeDICE (which uses policy gradients) supports this design choice.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by evidence, and no verifiable flaw invalidates its main contributions.

### Minor

1. **The derivation from the constrained problem (Eq. 4–6) to the practical objective (Eq. 11) could be more rigorous.** The paper introduces a mixed proposal distribution \(\hat{d}^\mathcal{D} = \zeta d^\mathcal{D} + (1-\zeta)\mu\) and replaces the original \(f\)-divergence \(D_f(d^\pi\|d^\mathcal{D})\) with \(D_f(d^\pi\|\hat{d}^\mathcal{D})\) to avoid support mismatch (line 90). This modification is transparently explained as a practical design choice, and the theoretical results (Propositions 1–2, Theorem 2) are developed for the modified objective—so there is no disconnect between the theory and the implemented algorithm. However, the paper could more clearly distinguish between the initial theoretical formulation and the practical instantiation, and could discuss the cost of this approximation (e.g., how it affects the original OOD constraint's tightness). As written, the transition from Eq. 7 to Eq. 11 reads as a direct consequence, when it is actually a thoughtful design modification.

2. **Missing baseline hyperparameter documentation for custom sparse-MuJoCo tasks.** The paper states "We adopt the scores of baselines if they are reported in original paper" (line 234). For the standard sparse-reward tasks (Maze2D, Adroit), this is appropriate. However, for the custom sparse-MuJoCo tasks (Table 2) and the sub-dataset experiments (Figure 3), these are non-standard settings requiring re-running baselines. The paper does not report whether baseline hyperparameters were re-tuned, how many seeds were used for each baseline (though 5 seeds are stated for CDE), or whether baseline implementations from published repositories were used as-is. This is a reproducibility concern, though not a fatal one given that the main competitive advantages hold across multiple settings.

3. **Empirical narrative slightly overstates performance in full-data settings.** The paper states CDE "consistently matches or surpasses the performance of the best baseline across nearly all tasks" (line 237). This is largely accurate (CDE matches or surpasses on ~14 of 17 tasks across Tables 1–2). However, the paper could more explicitly acknowledge the few tasks where CDE clearly underperforms: hammer-human (CQL 4.4 vs. CDE 1.9), door-human (CQL 9.9 vs. CDE 7.7), pen-expert (BCQ 114.9 vs. CDE 105.0), and halfcheetah-medium (CQL 97.6% vs. CDE 82.0%). Discussing possible reasons (e.g., the uniform OOD action prior may be a poor match for high-dimensional manipulation) would strengthen credibility.

4. **The state-marginal mismatch term \(\mathrm{TV}(d^\mathcal{D}(s)\|d^*(s))\) in Theorem 3 is qualitative.** The paper acknowledges this term depends on the unknown optimal state distribution (line 216: "This bound explicitly highlights two crucial factors influencing the final performance"), but the bound cannot be computed in practice. This is not a flaw—the insight is still valuable—but the paper should note the qualitative nature more clearly.

### Trivial

- The TV term in Theorem 3 is correctly identified as qualitative but could be discussed more explicitly as a limitation.
- The parameter study on ζ (Figure 6) shows sensitivity at low ζ values but provides only a brief explanation ("in-distribution learning being overshadowed"). A more detailed analysis would be useful though not required.

## Nice-to-Haves

- A sensitivity analysis on the OOD action threshold \(\Delta a\) would demonstrate robustness of the uniform prior assumption.
- Practical heuristics for selecting \(\tilde{\epsilon}\) and \(\zeta\) would increase the method's usability.
- A discussion of why CDE underperforms CQL on specific Adroit human tasks (hammer, door) would help understand the method's failure modes.

## Removed Points

- **"Automatic bound is not automatic because it depends on a hyperparameter."** REMOVED: This misunderstands the paper's claim. Prior work *assumes* bounded concentrability as an external condition; CDE's structure *guarantees* bounded ratios given any finite choice of \(\tilde{\epsilon}\). The hyperparameter controls tightness, not existence of the bound.
- **"Figure axes not fully labeled."** REMOVED: Likely a parser artifact from the embedded figure image. The original submission's figure has axis labels in the rendered image.
- **"Should acknowledge prior safe RL work on occupancy measure constraints."** REMOVED: Scope creep—the paper is about offline RL with pessimism, not safe RL.
- **"The introduction says 'first approach to explicitly apply pessimism in stationary distribution space' is overstated."** REMOVED: The claim is specific to applying *pessimism* (conservatism) in the stationary distribution space for *offline RL*. This is a reasonably novel claim that the paper supports.
- **"Weakness about missing related works."** REMOVED per instructions: I cannot verify existence of missing references.
- **Criticisms about the paper lacking appendix/proof details.** REMOVED per instructions: The parser strips appendices.

## Novel Insights

The reviews do not surface any genuinely novel insight beyond the paper's own contributions. However, the interaction between the two reviews highlights an interesting tension: the harsh critic frames the mixed proposal distribution as a "gap" between theory and practice, while the strength finder correctly recognizes it as a deliberate mechanism to handle support mismatch. This tension actually points to a subtle point the authors could clarify: the mixed proposal is not a departure from the theory but an instantiation of it—the theory analyzes the method *as implemented* (with the mixed proposal), not the idealized starting point. Making this explicit would eliminate the perceived gap entirely.

## Suggestions

1. Clearly distinguish between the starting theoretical formulation (Eq. 4–6) and the practical objective (Eq. 11) by adding a sentence acknowledging the mixed proposal as an approximation and discussing the error introduced.
2. Add a paragraph detailing baseline hyperparameter configurations and seeds for the custom sparse-MuJoCo tasks (Table 2) and sub-dataset experiments (Figure 3).
3. Add a brief discussion of the few tasks where CDE underperforms, analyzing possible causes (e.g., uniform OOD action prior's limitations in high-dimensional manipulation).
4. Consider adding a sensitivity study on the OOD action threshold \(\Delta a\) to demonstrate robustness.
