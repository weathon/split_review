## Summary

This paper identifies, formalizes, and corrects the "equivalent action problem" in GFlowNet-based graph generation: when multiple distinct actions (e.g., adding a node to different symmetric attachment points) lead to the same graph, naive implementations systematically bias sampling away from highly symmetric graphs (in atom-based generation) or toward symmetric fragments (in fragment-based generation). The paper proves that this bias is proportional to the size of the automorphism group of the generated graph, and proposes a simple reward-scaling correction (multiplying the reward by |Aut(G)|) that requires only a single automorphism computation per trajectory. The theory is validated on a small-graph environment where exact probabilities are tractable, and applied to molecule generation tasks.

## Strengths

1. **Rigorous theoretical formalization of the bias.** The paper explicitly relates graph space G to state space S via equivalence classes, defines equivalent actions through orbits, and proves (Lemma 2, Theorem 1) that the ratio of forward to backward equivalent actions between successive states equals |Aut(G)|/|Aut(G′)|. This is a non-trivial and principled theoretical contribution that cleanly characterizes the problem.

2. **Simple and computationally efficient correction.** The proposed fix — scaling the final reward by |Aut(G)| — requires only one automorphism computation per trajectory rather than the O(K × T) graph-isomorphism checks that would be needed to remove equivalent actions at every step. The paper reports no significant slowdown using the bliss algorithm, making the method practical.

3. **Conclusive small-graph experiment.** On 2,999 small graphs where exact model probabilities are tractable (Section 6.1, Figure 3), the corrected method (TB+AC) achieves nearly identical correlation and L₁ error to the gold-standard baseline that explicitly removes equivalent actions (TB+RM). The strip plot showing the target-to-model ratio matching |Aut(x)| for vanilla TB and constant for corrected methods is a clean, compelling existence proof.

4. **Unbiased model-likelihood estimator.** Equation (3) provides an importance-sampling estimator for p_S^⊤(x) that correctly divides by |Aut(x)|, enabling rigorous evaluation of distributional fit beyond the usual proxy metrics.

5. **Practical motivation.** The observation that over 50% of molecules in ZINC250k have more than one automorphism (with 18% having four or more) grounds the problem in real drug-discovery applications.

## Weaknesses

### Fatal
None.

### Major
None. The core claims — that the equivalent action bias exists, that it is proportional to |Aut(G)|, and that reward-scaling corrects it for the TB objective — are well-supported by theory and experiment.

### Minor

1. **DB justification is stated but not derived.** Theorem 2 asserts that *if* the graph-level DB condition holds with reward scaling, sampling is proportional to R. The paper then claims "scaling the reward alone is sufficient for both TB and DB objectives." However, it does not explicitly show that training the standard per-transition DB objective (which uses state-level flows F(s) and policies p_S, q_S) with reward scaling implies the graph-level DB condition (which uses F(G) and p_G, q_G). The derivation is straightforward from Theorem 1 (substituting p_S/q_S = (|Aut(G)|/|Aut(G′)|)·(p_G/q_G) into the DB loss and defining F′(G) = F([G])/|Aut(G)|), but the paper omits these steps. Since no experiments use DB, this does not affect the empirical results, but the presentation overreaches slightly.

2. **Approximate correction (TB+XC) is under-specified.** The paper says "we assign a number to each fragment based on how many equivalent actions it is likely to incur during generation" (line 163) but provides no concrete procedure for determining these numbers. The TB+XC results in Table 2 are thus not reproducible. Since the exact correction (TB+AC) is the main contribution and the approximate method is presented as a side experiment, this does not undermine the paper, but it should be clarified or removed.

3. **Equal-probability assumption is not empirically verified.** The derivation that p_S(a|s) = |A(G,e)|·p_G(e|G) (Equation 2) assumes permutation-equivariant networks assign equal probability to actions in the same orbit. While this is a known theoretical property of such architectures with invariant aggregators, the paper does not verify it on the *trained* molecule-generation models (e.g., by checking that predicted logits are nearly equal across symmetric actions on partial graphs). The small-graph experiment provides indirect validation, but direct verification would strengthen the claim.

4. **Modest fit on the atom-based molecule task.** The Pearson correlation between log likelihood and log reward is only ~0.15–0.2 for the atom task (Figure 4), regardless of correction method. The paper briefly acknowledges this (line 214: "matching the rewards is relatively difficult") but does not discuss whether the correction's limited benefit on this task stems from insufficient model capacity, training difficulty, or other factors. This tempers the claim that "accurately modeling the target distribution yields the best results" for the atom setting.

### Trivial
None.

## Nice-to-Haves

- **Comparison to Ma et al. (2024).** The paper positions its exact correction against Ma et al.'s approximate positional-encoding approach but does not include any experimental comparison (even on the small-graph environment). A small-scale comparison would demonstrate whether and when the approximation introduces meaningful error.
- **DB validation.** Since Theorem 2 claims the correction works for DB, one experiment (e.g., on the small graphs) using the DB objective would be a natural completeness check.
- **More bias examples.** The cyclohexane overcounting (5220 vs. 1042 instances) is effective; additional concrete examples of symmetric molecules that vanilla TB over- or under-samples would further illustrate the practical impact.

## Removed Points

The following points from the provided reviews were removed per the rules:

- **Harsh critic's formatting/style nitpicks** (Section 3 notation clarity, Section 6 presentation notes): parser artifacts or subjective presentation preferences, not substantive weaknesses.
- **Harsh critic's demand for comparison to Ma et al. as a "missing experiment" weakness**: moved to Nice-to-Haves; the paper's core contribution stands without it.
- **Strength Finder's "general applicability across GFlowNet objectives"**: this claim is the subject of the DB weakness and is overstated — moved to Removed Points since a verified weakness (insufficient DB derivation) conflicts with this strength being presented without caveat.
- **Strength Finder's "handling of fragment-based generation" and "practical motivation"**: kept in Strengths as they are specific and evidence-backed; the vague claim about "general applicability" was removed.
- **Critic's "obvious next steps" and "deeper analysis needed"**: these are speculative suggestions, not verified weaknesses.

## Novel Insights

The novel insight emerging from this review is that the paper's theory and small-graph validation are much stronger than its molecule-generation results. The small-graph experiment is a rare "existence proof" environment where exact probabilities are computable, and the correction works perfectly. Yet when moving to real molecules, the improvement on atom-based generation is modest and the distributional fit remains poor regardless of correction. This decoupling — a provably correct fix that nonetheless yields only small practical gains in one setting — suggests that for atom-based molecular GFlowNets, the equivalent-action bias may not be the dominant source of error; other factors (model capacity, training dynamics, reward landscape) may matter more. This is a useful observation that the paper itself only touches on briefly.

## Suggestions

1. **Spell out the DB derivation.** Add 3–4 lines of algebra showing how Theorem 1 transforms the standard DB loss into the graph-level DB condition when terminal flows are set to |Aut(G)|R(G). This would make Theorem 2 a clean corollary rather than a conditional statement.
2. **Either specify or remove the approximate correction (TB+XC).** Provide the concrete assignment rule for N(C) (or replace it with a citation if the procedure follows a prior work). Without this, the experiment is not reproducible.
3. **Acknowledge the equal-probability assumption as a condition to verify.** Add a brief sentence noting that users of the correction should verify that their architecture satisfies this property, or that the small-graph experiments serve as indirect validation.
4. **Discuss the atom-task fit limitation more explicitly.** A paragraph acknowledging that the low likelihood-reward correlation on the atom task may reflect model-capacity or optimization challenges beyond the bias correction — and that the correction's value there is more about removing a known bias than about dramatically improving samples — would improve intellectual honesty.

## Score and Decision

The paper makes a genuine theoretical contribution (formalizing and proving the equivalent-action bias), proposes a simple and correct fix, and validates it convincingly on a tractable small-graph benchmark. The molecule-generation experiments are supportive but not transformative, and the minor weaknesses (DB overclaim, under-specified approximation, unverified assumption) are addressable. The paper's core claims about the existence of the bias and the TB correction are solid.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>