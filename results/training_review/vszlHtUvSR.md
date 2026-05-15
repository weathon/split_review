Now I have all the information needed to construct the final review. Let me synthesize everything.

---

## Summary

This paper proposes RDHNet, a network architecture for multi-agent reinforcement learning that achieves both permutation invariance and continuous rotation invariance by converting absolute Cartesian coordinates into relative polar coordinates (using the agent-reference entity line as the zero axis) and aggregating through hypernetworks. The method is evaluated on Cooperative Prey Predator and Cooperative Navigation tasks, outperforming baselines including FACMAC, MADDPG, IDDPG, COVDN, and COMIX in 4 out of 5 scenarios.

## Strengths

- **First MARL architecture to handle continuous (arbitrary-angle) rotations, not just 90° multiples**: The paper clearly identifies the limitation of prior work (van der Pol et al., 2021; Yu et al., 2023, 2024) to discrete rotations and proposes a principled approach using relative polar coordinates that is theoretically rotation-invariant for any angle (Section 2.2). This is a genuine gap in the MARL literature.

- **Clean, principled architectural design combining rotation and permutation invariance**: The Relative Direction Layer (Section 4.1) converts Cartesian coordinates to polar coordinates relative to the agent-entity line, eliminating dependence on an absolute coordinate system. The use of separate hypernetworks per entity class (Section 4.2) maintains expressiveness while enforcing both invariances, building on HPN (Jianye et al., 2022).

- **Ablation study structured to separate PI and RI effects**: The ablation compares COMIX (no invariance), COMIX+HPN (PI only), and RDHNet (PI+RI), showing that adding rotation invariance on top of permutation invariance consistently improves performance, and that PI alone can sometimes hurt (e.g., Navigation). This provides evidence that rotational symmetry is a distinct and important factor (Section 5.3, Fig. 5).

- **Honest discussion of limitations**: Section 6 openly acknowledges the quadratic computational complexity, limited task diversity, and the lack of an effective actor-critic variant, rather than overclaiming.

## Weaknesses

### Fatal
None.

### Major

- **Ablation conflates rotation invariance with the use of relative coordinates**: The ablation compares PI-only (absolute coordinates + HPN) against PI+RI / RDHNet (relative polar coordinates + both invariances). Because these two conditions differ simultaneously in the coordinate representation (absolute vs. relative) and the symmetry constraint (PI-only vs. PI+RI), the observed gains cannot be attributed specifically to the rotation invariance property. Relative distances and angles are inherently more informative features for these tasks (e.g., "how far is the predator from the prey") regardless of whether invariance is enforced. A control that uses relative coordinates *without* enforcing the symmetry constraint (e.g., raw relative vectors fed through a non-symmetric network) would isolate the benefit of the invariance constraint from the benefit of better feature engineering. As it stands, the paper conflates two variables in a single comparison.

- **Direct empirical validation of rotational generalization is absent**: While the architecture is theoretically rotation-invariant by construction (polar coordinates relative to a reference entity remove dependence on absolute orientation), the paper never *empirically* demonstrates that this invariance holds in practice. A standard test would train on a fixed set of orientations and then evaluate on states rotated by arbitrary angles, measuring whether RDHNet's performance degrades less than baselines'. Without such an experiment, the paper's central claim — that handling *continuous* rotations is the source of improvement — rests on architectural reasoning rather than direct evidence. The omission is notable given that this is positioned as the paper's primary contribution over prior work.

### Minor

- **Statistical reporting is incomplete**: The paper states experiments were run with "different random seeds" but does not state the number of seeds (Section 5.1). Table 1 reports mean and standard deviation but does not specify how many runs these statistics are computed over. Figure 4 shows learning curves without error bars or confidence bands. While this level of reporting is common in some MARL venues, the combination of the small performance gaps on some tasks and the lack of variance visualization makes it difficult to assess whether the reported improvements are statistically reliable.

- **Claim about policy-network use is unsupported**: The abstract and Section 1 state that RDHNet "can be used for both predicting actions and evaluating action values/utilities" and "can be used to construct not only an action value/utility evaluation network but also a policy network." However, the experiments only test the value-based variant (using COMIX with CEM for action selection). The policy-network claim is never demonstrated. The conclusion acknowledges this as future work ("we have yet to develop more effective optimization strategies for the actor-critic version of RDHNet"), but the earlier claims remain overstated relative to what is validated.

- **Imprecise formalization of rotation in the problem statement**: Section 3 defines $U$ as "the set of all $m\times m$ rotation matrices" and writes $h(P\cdot u, Z)$. For 2D spatial coordinates where each $p_k$ is a 2D position, $P$ would be $m\times 2$ and multiplying by an $m\times m$ matrix is dimensionally inconsistent. The intended operation (applying the same 2D rotation to each entity's position) is clear, but the notation is technically incorrect. Additionally, the composition of permutation and rotation invariance is described algorithmically but not formalized in the symmetry definitions.

### Trivial

- The paper mentions the period ambiguity of arctan (Section 4.1, line 67-68) but does not specify using `atan2` to resolve it, which is the standard fix.
- Figure labels and captions use inconsistent abbreviations ("IE" vs. "RI" and "PE" vs. "PI" across figures and text).

## Nice-to-Haves

- **Test generalization to unseen rotations**: Train on a fixed orientation and evaluate on states rotated by arbitrary angles, measuring whether RDHNet degrades less than baselines. This would provide direct empirical support for the rotation-invariance claim.
- **Relative-coordinates-without-symmetry ablation**: Compare RDHNet against a version using relative coordinates but without symmetric aggregation, to isolate the effect of the invariance constraint.
- **t-SNE/PCA visualization** of internal representations for states and their rotated versions to demonstrate invariance visually.
- **Broader task diversity**: The current experiments span only two tasks (Predator-Prey and Navigation). More diverse continuous-rotation environments would strengthen generality claims.

## Removed Points

These points are flagged to be removed; treat them with caution:
- **Criticism about rotation invariance not being empirically validated (as a "nearly structural" flaw)**: The critic framed this as nearly fatal, but the architecture is theoretically rotation-invariant by construction (relative polar coordinates remove dependence on absolute orientation). While a direct generalization experiment would be strengthening, the absence does *not* invalidate the core claim — the paper's contribution is the architecture itself, which is provably invariant. This point was downgraded from "nearly structural" to a verified major weakness about absence of *empirical* validation of the generalization, not the claim itself. The reviewer's language ("the paper does not establish that rotational invariance is responsible for the gains") is also partially addressed by the ablation showing PI+RI > PI-only.
- **Criticism that the paper overstates "no work can handle continuous rigid transformations"**: The paper specifically discusses prior MARL work (van der Pol et al., Yu et al.), not all fields. The critic's reference to SE(3)-Transformers is outside the MARL scope the paper explicitly targets. This is a strawman.
- **Criticism that hypernetwork architecture is not described**: The paper references prior work (Jianye et al., 2022). This is standard practice and not a weakness.
- **Criticism that task descriptions are too brief**: Experimental details would typically be in the appendix, which was stripped by the parser. The paper provides sufficient high-level description for understanding the experiments.
- **Criticism that only off-policy methods are compared**: This is an observation, not a weakness. The paper does not claim to cover all paradigms.
- **Strength from Strength Finder about "strong empirical validation with ablation isolating rotational and permutational contributions"**: This conflicts with the verified weakness that the ablation conflates rotation invariance with relative coordinates. Per the rules, the weakness wins, so this strength is removed.
- **Pure formatting and style nitpicks**: Removed per hard rules.

## Novel Insights

The paper's central insight — that relative polar coordinates with a reference entity chosen as the zero axis can achieve continuous rotation invariance for MARL — is well-executed and fills a clear gap. However, beyond the paper's own contributions, the reviews do not surface a genuinely novel observation that the authors themselves did not already articulate. The most interesting cross-cutting point is the ablation finding that permutation invariance alone (HPN) can *hurt* performance in some tasks (Navigation), which the authors attribute to reduced representational capacity. This suggests that symmetry constraints are not universally beneficial and must be applied judiciously — a point worth exploring further but already noted by the paper.

## Suggestions

1. **Run an ablation with relative coordinates but no symmetric aggregation**. This is the single most important experiment to add: it would isolate whether the performance gains come from the symmetry constraint or just from using relative features (distances + angles) as inputs.
2. **Add a direct rotational generalization test**: train on one orientation, evaluate on states rotated by arbitrary angles, and report how much each method's performance degrades.
3. **Report the number of seeds explicitly** and add error bars / confidence bands to the learning curves in Figure 4.
4. **Either remove or substantiate the policy-network claim** — if it is not tested, state it as future capability rather than a contribution of the current submission.
5. **Fix the dimensional inconsistency** in the formalization (the rotation matrix $U$ applied to $P$ should be $2\times 2$, not $m\times m$).

## Score and Decision

The paper addresses a genuine problem with a principled architectural solution and demonstrates competitive empirical results. However, the two major weaknesses — the conflated ablation that cannot isolate rotation invariance from relative-coordinate features, and the absence of a direct empirical test of rotational generalization — prevent the paper from fully establishing its central claim. These issues are addressable with additional experiments but are significant enough that the current submission does not provide clean evidence for its headline contribution. The minor issues (statistical reporting, overclaimed policy-network scope) further reduce confidence.

Overall, the paper has a solid idea and a plausible architecture, but the evaluation design needs work before the central claim is convincingly supported.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>