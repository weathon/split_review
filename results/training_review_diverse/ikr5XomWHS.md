Now I have verified the paper thoroughly. Let me cross-check each reviewer claim against the actual paper content.

**Verification results:**

1. **Policy-dependence claim**: The paper explicitly acknowledges this in Section 6 (line 119): "our findings can only approximate this through what π can achieve." The paper's language is mostly careful — "For each robotic agent, we characterize..." (abstract), "most task policies in our study" (Section 4). Some broader phrasing exists ("sensory information is rarely task-critical") but is generally qualified.

2. **Tautological claim**: The paper does use "counter-intuitively" in line 12. Section 4.1's theory (lines 54-59) shows optimal policies need no sensing in deterministic settings. The empirical finding that better policies need less sensing follows directly. Valid observation about framing.

3. **OOD claim**: The paper acknowledges this explicitly in lines 88-89 but provides no quantitative diagnostics. Valid concern.

4. **Thin stochastic experiments claim**: Only the four-rooms gridworld. Valid.

5. **Computational cost claim**: Lines 90 explicitly state "These are expensive evaluations: for each state...we must generate 100x5=500 trajectories." The reviewer is factually wrong. **REMOVE.**

6. **Greedy strategy claim**: The contributions list mentions it but no evaluation in main text — likely in the appendix. **REMOVE per rules about missing appendix content.**

Now writing the consolidated review.

## Summary

This paper proposes a framework called Value of Sensory Information (VoSI) that empirically measures how much task performance degrades when sensory feedback is withheld from a frozen policy at different moments during task execution. Applied to seven robotics benchmarks (DM-control, Robosuite, Push-T) with TD-MPC2 and DiffusionPolicy agents, the framework reveals that sensory information is surprisingly rarely task-critical in many standard setups — several tasks incur near-zero regret even under fully open-loop execution. The paper also demonstrates that stochastic dynamics drive sensing needs and that more competent policies are more robust to sensor loss.

## Strengths

- **Novel empirical methodology (VoSI):** The paper introduces a clean, state-wise regret measure that quantifies the task-relevant value of sensory information at specific moments, going beyond prior work focused on constrained optimization or theoretical bounds. The methodology is clearly defined (Eq. 1) and practically implemented via mixed-loop execution of lookahead policies.

- **Systematic empirical finding that sensing is rarely critical in common benchmarks:** Figure 3 shows that for 6 of 7 tasks, policies achieve near-zero normalized regret even when sensing only once every 5 steps. For Robosuite tasks, even fully open-loop execution performs as well as closed-loop control. This result is demonstrated across two different policy architectures (TD-MPC2 and DiffusionPolicy) and supported by a theoretical argument (Section 4.1) about optimal policies in deterministic environments.

- **Identification of prototypical VoSI profile shapes:** The paper categorizes VoSI profiles into flat, gradual, and stepped shapes (Figures 7-8) and provides intuitive explanations linking each shape to task phases (e.g., flat after goal achievement, gradual from hard-to-model contacts, stepped from phase changes like losing track of a ball). This taxonomy provides a clear visual language for understanding when sensing matters.

- **Critical observation about benchmark sensory complexity:** The paper notes that Robosuite manipulation tasks show no performance loss under open-loop execution, suggesting these benchmarks may underestimate the sensory demands of real-world robotics — a useful observation for the community.

- **Demonstration of competency-sensor dependency:** Figure 5 empirically shows that policies at later training stages and with higher model capacity degrade less at lower sensing rates, validating the theoretical expectation that more competent policies are more robust to sensor loss.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contribution — the VoSI methodology and the empirical finding that sensing is rarely critical in common benchmarks — is sound and supported by evidence. The issues below are genuine but do not invalidate the central claims.

### Minor

1. **The VoSI framework is inherently policy-dependent, and the paper occasionally uses broader language that blurs this distinction.** The paper acknowledges this in the limitations (Section 6: "our findings can only approximate this through what π can achieve"), and most claims are attributed to the specific policies studied. However, statements like "sensory information is surprisingly rarely task-critical" (abstract) and the task-level "sensory complexity" ordering in Section 4 elide the policy-dependence. What the paper actually measures is how specific policies (TD-MPC2, DiffusionPolicy) handle open-loop execution. A different policy with better internal dynamics prediction could produce different VoSI profiles. The paper would benefit from either computing VoSI across multiple policy families on the same task or consistently qualifying claims as policy-specific.

2. **The out-of-distribution concern for mixed-loop execution is acknowledged but not quantitatively validated.** The paper (Section 5) correctly notes that policies trained for closed-loop execution are operating out-of-distribution in mixed-loop mode, and asserts that they "hold up well enough to produce coherent and interpretable findings." However, no quantitative diagnostics are provided — e.g., comparing action distributions from closed-loop vs. open-loop rollouts, or verifying that mixed-loop state visitations stay within the training distribution. If mixed-loop rollouts from some states produce erratic trajectories, VoSI profiles could reflect policy failure modes rather than task-relevant sensor value. The coherence of the results partially mitigates this concern, but systematic validation would substantially strengthen the framework.

3. **The inverse correlation between policy competency and sensor dependency is presented as "counter-intuitively" but is a straightforward consequence of the paper's own theoretical analysis.** Section 4.1 shows that optimal policies in deterministic environments need zero sensing beyond timestep 0. The empirical finding (Figure 5) that more competent policies (better trained, higher capacity) are more robust to sensor loss is a direct validation of this theory, not a surprising new discovery. The paper should reframe this finding as empirical confirmation of the theoretical expectation rather than presenting it as "counter-intuitive."

4. **The stochastic dynamics experiments are too thin to support the claimed generality.** Contribution 3 claims VoSI is applicable "in other settings by showing proof-of-concept applications to environments with stochastic dynamics and model/sensing noise." The only evidence is a single toy four-rooms gridworld (Figure 4). This is far from demonstrating applicability to the complex, high-dimensional tasks studied in the main experiments. The paper would be stronger by either removing this contribution claim or including experiments on stochastic variants of DM-control or Push-T tasks.

5. **The VoSI profile classification (flat/gradual/stepped) is post-hoc and qualitative.** While the taxonomy aids exposition and provides useful intuition, it is not used to make any testable predictions or validated quantitatively. This descriptive categorization is reasonable for an empirical analysis paper but should be presented with appropriate humility about its limitations.

### Trivial

- The term "normalized regret" (fraction of closed-loop reward lost) is reasonable but could be confused with regret relative to an optimal policy. Clarification would help.

## Nice-to-Haves

- **Multi-policy analysis on the same task:** Computing VoSI for multiple policies (varying capacity, architecture, training budget) on the same task would directly address the policy-dependence concern and potentially strengthen task-level interpretations if profiles are consistent.
- **Mixed-loop diagnostics:** Providing quantitative evidence (e.g., action distribution comparisons, state-visitation analysis) that mixed-loop rollouts stay within the training distribution.
- **Cost analysis and approximations:** A brief discussion of how to approximate VoSI (e.g., via importance sampling or learned surrogate models) to reduce the 500-trajectory-per-state cost would enhance practical relevance.
- **Comparison to a theoretical lower bound:** Deriving a lower bound on VoSI from environment dynamics entropy would help separate policy limitations from irreducible task requirements.

## Removed Points

These points were flagged by reviewers but are removed per the review guidelines:

- **"Computational cost not discussed":** The paper explicitly states "These are expensive evaluations: for each state for which we compute VoSI, we must generate 100x5=500 trajectories" (line 90). The reviewer's claim that this is not discussed is factually incorrect.
- **"Greedy strategy not described/evaluated in main text":** The greedy strategy is listed as Contribution 4 and is likely detailed in the appendix, which was stripped by the parser. Per guidelines, criticisms about missing appendix content are removed.
- **"Formatting/style nitpicks" and "typos":** Any such criticisms reflect parser artifacts, not author errors.

## Novel Insights

Beyond the paper's own contributions, the most striking insight synthesizable from the reviews is that the paper's central empirical finding — that sensing is rarely critical — may be partly an artifact of the benchmark ecosystem itself. The paper shows Robosuite tasks are essentially open-loop solvable, DM-control tasks need modest sensing, and only Push-T shows meaningful sensor dependence. This suggests the field's standard benchmarks may be selecting for policies and tasks that systematically underweight the role of sensory feedback, a methodological critique that goes beyond the paper's explicit conclusions. The fact that two very different policy classes (TD-MPC2 and DiffusionPolicy) produce similar VoSI profiles on shared tasks further suggests that this weakness is not an artifact of any single algorithmic family but a property of the benchmark regime.

## Suggestions

1. **Clarify the scope of claims:** Consistently frame findings as "VoSI profiles of these specific policies on these tasks" rather than occasionally implying task-level properties. Add a brief statement early in the paper (not just in the limitations) that VoSI is policy-dependent by construction.
2. **Add quantitative mixed-loop diagnostics:** Provide a simple analysis (e.g., comparing the distribution of actions or state visitation frequencies between closed-loop and mixed-loop rollouts) to verify that mixed-loop behavior does not degenerate catastrophically.
3. **Reframe the competency correlation:** No longer present the competency-sensor dependency as "counter-intuitive" — it follows directly from Section 4.1's theory. Present it as empirical validation of the theoretical expectation.
4. **Either expand the stochastic experiments or tone down Contribution 3:** Add a stochastic variant of at least one DM-control or Push-T task, or replace Contribution 3 with a more modest claim.

## Score and Decision

**Originality:** The VoSI methodology and the empirical finding that sensing is rarely critical in standard benchmarks are original contributions. Prior work focused on constrained optimization or theoretical bounds rather than empirical measurement on modern benchmarks.

**Importance of research question:** Understanding when sensing matters is a fundamental question for robotics and sequential decision-making. The paper's findings have implications for sensor design, policy deployment, and benchmark design.

**Claims support:** The central claims about VoSI profiles and sensing needs on the tested tasks are well-supported by Figures 3 and 7. The competency correlation is supported by Figure 5 but its framing as "counter-intuitive" is overblown. The stochastic dynamics claim (Contribution 3) is under-supported.

**Soundness:** The methodology is sound and clearly described. The main concern is the unresolved OOD issue for mixed-loop execution, which the paper acknowledges but does not quantitatively verify.

**Clarity:** The paper is well-written and clearly organized. Concepts are introduced systematically and visualizations are effective.

**Value to the community:** The VoSI framework provides a useful tool for analyzing sensor requirements, and the finding that common benchmarks may have low sensory complexity is a valuable critique.

The paper has real contributions and is clearly above the acceptance threshold. The weaknesses are addressable and do not undermine the central claims.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>