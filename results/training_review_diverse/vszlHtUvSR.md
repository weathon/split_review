Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes RDHNet, a neural network architecture for multi-agent reinforcement learning that achieves both permutation invariance and *continuous* rotation invariance (for arbitrary angles, not just 90° multiples). The key idea is a Relative Direction Layer (RDL) that converts absolute Cartesian coordinates of entities into relative polar coordinates with respect to a chosen reference entity, combined with entity-type-specific hypernetworks and symmetric aggregation. Experiments on Cooperative Prey Predator and Cooperative Navigation tasks show strong empirical performance against continuous-action MARL baselines, with the advantage growing as the number of entities increases.

## Strengths

- **Clear formalization of symmetry in MARL.** Section 3 provides explicit mathematical definitions distinguishing permutation invariance and rotation invariance, which prior work often conflates or treats informally. This is a useful contribution for future research.

- **Addresses continuous (not just discrete) rotational symmetry.** Prior methods (van der Pol et al., 2021; Yu et al., 2023, 2024) are limited to 90° multiples. RDHNet's use of relative polar coordinates with a reference entity achieves invariance under arbitrary continuous rotations, which is more realistic for real-world scenarios (Section 2.2, 4.1).

- **Strong empirical evidence, especially on larger state spaces.** RDHNet achieves the best mean returns in 4 out of 5 tasks (Table 1), and on the 6-predator variant of Cooperative Prey Predator it shows "overwhelming superiority" (Figure 4). As the paper argues, this is consistent with the intuition that compressing redundant representation space matters more when that space is larger.

- **Ablation study that cleanly separates PI from RI effects.** Figure 5 compares baseline (COMIX), PI-only (COMIX+HPN), and PI+RI (RDHNet). It shows that adding PI alone sometimes degrades performance (e.g., Cooperative Navigation), while adding both PI and RI consistently helps, with the gap widening as entity count increases. This provides evidence that rotational symmetry is a distinct, impactful factor.

- **Practical advantage of not requiring absolute coordinates.** As noted in the abstract and conclusion, RDHNet can make decisions based solely on relative observations, making it applicable in settings where absolute positioning information is unavailable.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No direct empirical test of rotation invariance.** The paper claims RDHNet extracts rotation-invariant representations, and the architecture is *theoretically* rotation-invariant by construction (relative polar coordinates cancel out global rotations). However, no experiment directly verifies this — e.g., taking a trained RDHNet, feeding the same state rotated by different angles, and showing that the policy output or Q-value changes negligibly. While the theoretical argument is sound and the strong empirical results are consistent with the claimed property, a direct invariance sanity check would make the core claim more convincing. This is the most significant gap.

- **Environmental symmetry assumptions are not explicitly clarified.** The paper states that obstacles are present (Section 5.1) but does not clarify whether obstacles and target points are entities whose coordinates are included in the global state and rotate with the configuration, or whether they are fixed in an absolute frame. The RDL-based method would produce invariant representations of whatever entity positions it receives, but whether the *MDP itself* is rotationally symmetric depends on whether the dynamics and rewards are preserved under global rotation of all relevant entities. This should be explicitly discussed to connect the theoretical motivation to the experimental setup.

- **Reference-entity averaging is not analyzed.** The paper selects each entity alternately as the reference and averages the outputs (Section 4.3). It does not analyze whether representations for different reference entities are consistent, nor whether averaging could corrupt the invariance property. An ablation comparing single-reference results against the averaged result would be informative.

- **Statistical rigor is limited.** Table 1 reports means and standard deviations, but several values have overlapping error bars with baselines (e.g., PreyPredator-4p: RDHNet −39.35 ± 10.77 vs. COMIX −48.88 ± 6.79). No significance tests or confidence intervals are reported. This is common in MARL benchmark papers but still worth noting.

### Trivial

- The notation in the permutation invariance definition (Section 3) is slightly tangled — the use of overbraces and ellipses makes it harder to follow than necessary.

## Nice-to-Haves

- **Comparison against discrete-rotation baselines.** The paper cites van der Pol et al. (2021) and Yu et al. (2023, 2024) as related work that handles only 90° rotations, but does not include them as baselines. Adding a discrete-rotation method (or a data-augmentation variant) would help isolate the benefit of *continuous* invariance vs. any form of rotation-awareness.

- **Direct invariance test** (as described under Minor weaknesses) would convert the theoretical claim into a demonstrated one.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about "not yet released" or "cannot be verified."** The harsh critic's language implying that aspects of the paper cannot be independently verified is removed per the hard rules — all cited models, benchmarks, and references are assumed to exist.

- **Criticism about missing sample size / number of seeds not being stated.** The paper states experiments were conducted "with different random seeds" (line 127). Exact counts could be in the appendix (stripped by the parser). Per the hard rules, weaknesses about details that may reside in the appendix are removed.

- **Criticism that "the conclusion may be correct but the evidence does not support it."** This overstates the severity. The paper provides both a theoretical argument for invariance (via RDL construction) and strong empirical results consistent with the claimed property. The evidence is not absent — it is indirect. This has been downgraded to a Minor concern.

- **Criticism that the evaluation protocol is "disconnected from the problem framing" and a "structural issue."** This overstates the gap. The environments do involve force-vector actions and entities whose relative geometry matters, which is exactly the setting the method targets. The missing clarification about obstacle behavior is a minor oversight, not a structural disconnection.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any new interpretation or framing that the paper itself does not already articulate.

## Suggestions

1. **Add a direct invariance check** — take a trained RDHNet policy, rotate the input state by several random angles (e.g., 10°, 45°, 120°, 200°), and show that the action outputs or Q-values vary negligibly. This single experiment would directly confirm the claimed property and is easy to include.

2. **Clarify the symmetry properties of the test environments** — explicitly state whether obstacles and target points are included in the observed entity set and whether the MDP dynamics/rewards are invariant under global rotation of all entities. If they are not perfectly symmetric, discuss why the method still helps (e.g., relative representations reduce input redundancy even in approximately symmetric settings).

3. **Analyze the reference-entity averaging** — compare single-reference performance against the averaged variant to validate that averaging is safe and that different reference entities produce consistent representations.

4. **Report confidence intervals or significance tests** — especially for results where error bars overlap with baselines, to clarify which comparisons are statistically meaningful.

## Score and Decision

This paper identifies a genuine underexplored problem (continuous rotational symmetry in MARL), provides a clean theoretical formalization, proposes a well-motivated architecture, and demonstrates strong empirical results — particularly on larger-scale tasks where the advantage is pronounced. The weaknesses are primarily in the validation methodology (no direct invariance test, environmental assumptions not clarified) rather than in the core idea. These are addressable in revision and do not undermine the paper's contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>