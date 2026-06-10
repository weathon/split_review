## Summary

MaxInfoRL augments Boltzmann exploration in model-free off-policy RL with an information gain bonus about the forward dynamics. It introduces a two-temperature formulation that separately controls policy entropy and directed exploration, with the latter auto-tuned via a target-policy-based constraint. The framework is applied to SAC, REDQ, DrQ, and DrQv2, and experiments across state-based and visual continuous-control tasks show consistent improvements over the base algorithms.

## Strengths

- **Modularity demonstrated across multiple base algorithms.** MaxInfoRL is combined with SAC, REDQ, DrQ, and DrQv2, and each combination improves over its respective base algorithm (Figures 2, 6, 7). This shows the framework is not tied to a single method and can be plugged into different off-policy learners.

- **Novel auto-tuning mechanism for the intrinsic reward coefficient (Section 3.2, Eqs. 10–11).** The two-temperature formulation with separate α₁ (policy entropy) and α₂ (information gain) is well-motivated. The target-policy-based constraint for auto-tuning α₂ is a principled alternative to fixed weighting (Burda et al., 2018) or the extrinsic optimality constraint (Chen et al., 2022), and the paper demonstrates empirically that it avoids the collapse-to-greedy problem that SACEIPO suffers from (Figure 5).

- **Consistent empirical improvements across diverse tasks.** MaxInfoRL outperforms baselines on a range of state-based DMC and OpenAI Gym tasks (Figure 2), on hard-exploration problems with action costs (Figure 5), on HumanoidBench (Figure 3), and on visual control tasks (Figures 6, 7). The phase plot (Figure 4) provides concrete visualization of faster state-space coverage.

- **Convergence guarantee (Theorem 3.1).** The paper shows that the modified soft Q-learning with the information gain bonus preserves the convergence properties of SAC under standard boundedness assumptions. While this is a direct extension of Haarnoja et al. (2018), it provides formal assurance that the bonus does not break the algorithm's convergence.

## Weaknesses

### Major

- **No ablation studies.** The method has three nontrivial design choices: (a) the information gain bonus vs. policy entropy bonus vs. both; (b) the auto-tuning mechanism for α₂ vs. fixed temperature; (c) the target policy for the constraint in Eq. (10). None of these are ablated. Without ablations, it is impossible to determine whether the reported improvements are driven by the information gain bonus itself, the auto-tuning, or simply the additional model capacity from the dynamics ensemble. This is the most significant barrier to evaluating the paper's contribution.

- **Unsubstantiated SOTA claim on visual humanoid tasks (line 210).** The paper states that MaxInfoDrQV2 achieves "the highest returns reached in these challenging visual control tasks by model-free RL algorithms in the literature" but provides no quantitative comparison to any published SOTA results. The only experimental comparison on these tasks is against the base DrQv2 algorithm (Figure 7), which lacks any intrinsic reward mechanism. Without comparison to DrQv2+RND, DrQv2+disagreement, or other intrinsic-reward-augmented variants, this claim is unsupported.

- **Limited baselines on visual control tasks (Figures 6, 7).** The only baselines for visual tasks are DrQ and DrQv2 — the base algorithms without any intrinsic reward mechanism. This reduces the comparison to "our method with intrinsic exploration vs. the same method without." To establish that the *specific formulation* of MaxInfoRL is better than simpler alternatives, the paper would need to compare against DrQ+RND, DrQv2+disagreement, or similar methods that also add intrinsic rewards to the base algorithms.

### Minor

- **Theorem 3.1 is a straightforward extension of Haarnoja et al. (2018).** The convergence result adds a bounded bonus term to the soft policy evaluation and update. The paper acknowledges this ("exhibits the same convergence properties"), but the nonstationarity of I_u (which depends on the growing dataset D_n) is not addressed — the Bellman operator itself changes over time, which standard soft policy iteration proofs do not cover unless the bonus is uniformly bounded (which is assumed but the effect of time-variation on convergence is not discussed).

- **Only 5 seeds reported without significance tests.** For deep RL benchmarks, 5 seeds is below the emerging standard of 10, and no statistical significance tests or confidence intervals are provided beyond standard error bars.

- **No computational cost comparison.** The paper acknowledges that the dynamics ensemble adds overhead (line 234), but no wall-clock time or FLOPs comparison is reported. The reader cannot assess the practical cost of the improvement.

- **Imprecise derivation in Eq. (8).** The transition from line 2 to line 3 writes the objective as E[Q] + αH(š', a|s), omitting a constant term (−αE[H(š'|s,a,f*)], the noise entropy, which is independent of π and thus does not affect the argmax). While the argmax statement is mathematically correct, the presentation obscures the reasoning and leads to the misleading claim that the objective equals E[Q] + αH(š', a|s) rather than being *equivalent up to a constant in the argmax*.

### Trivial

None.

## Nice-to-Haves

- Provide wall-clock time comparison or FLOPs to quantify the overhead of the dynamics ensemble.
- Increase to 10 seeds and report confidence intervals.
- If the MAB sublinear-regret result (advertised in the abstract) exists in the appendix, include at least the theorem statement in the main text.
- Clarify the relationship between the ε-MaxInfoRL variant (Section 3.1) and the Boltzmann variant (Section 3.2) in the experimental evaluation — which experiments use which?

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **MAB sublinear regret claim unsubstantiated.** The harsh critic claims this central advertised result has "zero evidentiary footprint" in the main text. However, the paper references "Theorem A" (line 225), which suggests the formal statement and proof reside in the appendix. Per the filtering rules, weaknesses about proofs deferred to the appendix (which was stripped by the parser) are removed. *Action: removed per missing-appendix-content rule.*

2. **Mathematical error in Eq. (8) conflating information gain with state entropy.** The harsh critic claims the derivation is incorrect. However, the argmax of E[−α log π + αI] equals αH(š', a|s) up to a constant (−αE[H(š'|s,a,f*)], the entropy of the Gaussian process noise), which does not depend on π and therefore does not change the argmax. The derivation is technically sloppy (equality is claimed where argmax-equivalence is the precise statement) but not incorrect. *Action: removed because the criticism is factually incorrect about a mathematical error; softened to a minor imprecision above.*

3. **Baselines are "deliberately weak" for state-based tasks.** The harsh critic argues that DISAGREEMENT and CURIOSITY use explore-then-exploit (25%), SACIntrinsic uses fixed λ, and SACEIPO quickly reduces its weight to zero. These are standard baselines from the literature (Sukhija et al., 2024b; Burda et al., 2018; Chen et al., 2022) and the paper explicitly discusses each limitation. The comparison is standard practice, not stacking. *Action: removed — the baselines are appropriate for the setting, and the paper's method is designed to address exactly these limitations.*

4. **Missing baselines (RND, ICM, Plan2Explore).** SACIntrinsic is described as "based on Burda et al. (2018)" (the RND paper), and Curiosity is based on Pathak et al. (2017) (the ICM paper). Plan2Explore is a model-based method, outside the paper's stated scope (model-free off-policy RL). *Action: removed.*

5. **Reference to Figure 1 not found.** This is a parser artifact — figures embedded as images may not survive extraction. Not a paper flaw.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run ablations isolating the three design choices:** (i) information gain bonus vs. policy entropy only; (ii) auto-tuned α₂ vs. fixed α₂; (iii) target-policy constraint vs. a simpler baseline like fixed target information gain. This is the single most important improvement needed.

2. **Replace or supplement the visual-task baselines** with DrQ+RND and DrQv2+disagreement (or similar intrinsic-reward baselines) so the reader can evaluate whether the specific MaxInfoRL formulation adds value over simpler ways of adding intrinsic rewards.

3. **Either substantiate or retract the SOTA claim** for visual humanoid tasks — provide a table of published returns from competing model-free methods, or remove the claim.

4. **State the MAB theorem** in the main text (even if the proof is deferred to the appendix) since it is advertised in the abstract.

5. **Report wall-clock time** so readers can assess the computational trade-off of the dynamics ensemble.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>