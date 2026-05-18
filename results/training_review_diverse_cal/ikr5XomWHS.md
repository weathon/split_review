Now let me write the consolidated final review.

## Summary

This paper introduces VoSI (Value of Sensory Information), a regret-based diagnostic that measures how much task performance degrades when a frozen look-ahead policy is forced to operate open-loop for a window of time. The authors apply VoSI to 7 robotic tasks (DM-control, Robosuite, Push-T) using state-of-the-art policies (Diffusion Policy, TD-MPC2) and find that: (1) sensing is rarely task-critical in many standard benchmarks, (2) VoSI profiles fall into three characteristic shapes (flat, gradual, stepped), and (3) more proficient/larger policies depend less on frequent sensing. The paper also provides a theoretical argument linking sensing needs to stochastic dynamics and policy expressivity.

## Strengths

1. **Novel empirical methodology for quantifying sensory value at scale.** VoSI extends value-of-information ideas to complex, continuous-control settings where prior work (Flaspohler et al., Majumdar et al.) was limited to simple analytic environments or short-horizon/finite-action tasks. The paper demonstrates VoSI on 7 diverse tasks with SOTA policies (TD-MPC2, DiffusionPolicy), as shown in Figures 3, 7, and 10.

2. **Counterintuitive empirical finding that sensing is rarely critical in standard benchmarks.** The paper provides concrete evidence (Figure 3) that across multiple tasks, fixed-rate mixed-loop execution with sensing only once every 5 steps (or even fully open-loop on Robosuite) achieves near-zero regret. This challenges the common assumption that closed-loop sensing is essential and aligns with recent observations (Dasari et al., Raffin et al., Wang et al.).

3. **Demonstration that task proficiency inversely correlates with sensor dependency.** The paper shows that fully trained high-performing agents are more robust to sensor loss than novice agents (Figure 5, left), and that higher-capacity models degrade less at low sensing rates (Figure 5, right). This insight is supported by both the four-rooms toy experiment and the training-stage analysis on actual robotic tasks.

4. **Theoretical grounding connecting sensing needs to stochastic dynamics and policy expressivity.** Section 4.1 provides a clear analytical argument that an optimal policy with perfect deterministic dynamics has zero value for sensing beyond the first step, and uses a four-rooms grid-world to empirically show how stochasticity generates regret profiles that resemble those in complex benchmarks (Figure 4). This bridges theory and empirical observation.

## Weaknesses

### Fatal

None.

### Major

1. **The paper systematically conflates policy-specific properties with task-level properties in its main narrative.** VoSI is defined for a *specific frozen policy* — it measures what that particular policy can get away with, not an inherent property of the task MDP. Yet the abstract states "sensory information is surprisingly rarely task-critical in many commonly studied task setups," and the text says "Robosuite tasks are outliers in terms of how little sensing they require" — both framing VoSI findings as task properties. Section 6 does acknowledge the limitation ("The VoSI framework in this paper is limited to a particular kind of agent"), but the main narrative (abstract, contributions, Section 4) does not carry this caveat. A different policy trained differently or to a different level might exhibit very different VoSI profiles. This is a structural overclaim that weakens the paper's scientific conclusions.

2. **Mixed-loop execution of closed-loop-trained policies is out-of-distribution, and the paper provides no quantitative validation that the resulting behavior is meaningful.** The paper identifies this concern in Section 5 ("would be operating out-of-distribution when executed in mixed loop mode… might produce erratic behaviors") but dismisses it with a single qualitative sentence: "appear to hold up well enough to produce coherent and interpretable findings." No quantitative evidence is provided — no trajectory success rates, no constraint violations, no distributional checks. If the policy's open-loop action chunks produce degenerate states, then the VoSI estimate reflects policy collapse rather than the value of sensory information per se. This is especially concerning for the Robosuite tasks where open-loop performance is near-perfect: it could simply reflect that those policies happen to produce safe action chunks, not that the tasks genuinely require little sensing.

### Minor

1. **The explanatory mechanism for sensing needs on deterministic tasks is a plausible hypothesis, not a demonstrated cause.** Section 4.1 argues that finite policy complexity plays a role analogous to stochasticity in creating sensing needs. However, the paper never directly measures model error or predictive uncertainty on the main 7 tasks. Figure 5 shows that better-trained/larger policies depend less on sensing, which is *consistent with* the model-error story but does not confirm it. Without a direct measure of the policy's simulation accuracy, the paper's core explanation of *why* sensing matters on deterministic tasks remains an untested hypothesis. This does not undermine the VoSI diagnostic itself but weakens the explanatory narrative.

2. **The claim about manipulation benchmarks being "outliers" goes beyond the evidence.** The paper states (Section 4) that "robot learning benchmarks for manipulation as represented by these three Robosuite tasks may be outliers in terms of how little sensing / perceptual capabilities they require." While the text uses hedging language ("speculating," "may be"), this conclusion rests on only 3 Robosuite tasks with similar quasi-static, contact-free or low-contact dynamics. This does not represent the breadth of manipulation (dynamic manipulation, sliding, in-hand manipulation). The speculation should be either removed or more narrowly scoped to the specific task instances studied.

3. **Action-chunk length (look-ahead horizon n) is not reported or ablated.** The look-ahead horizon of the policy likely affects VoSI — longer chunks can compensate for longer open-loop windows. The paper does not specify n for each task or compare it to the tested open-loop horizons. This is important context for interpreting the results.

4. **VoSI profiles are estimated from only 5 trajectories per state per horizon value.** For states with high variance (e.g., near-contact dynamics), this yields noisy estimates. The paper provides confidence intervals on task-level regret (Figure 3) but not on the state-level VoSI curves (Figure 7). This is likely a computational cost constraint, but it limits the reliability of fine-grained VoSI comparisons.

### Trivial

None.

## Nice-to-Haves

- Directly measuring predictive error (e.g., learned dynamics model error for TD-MPC2, implied state trajectory error for DP) and correlating it with VoSI across states would turn the model-error hypothesis into tested evidence.
- Comparing VoSI profiles from the frozen policy to those from a policy fine-tuned for mixed-loop operation would resolve the OOD concern.
- Reporting confidence intervals or variance bands on the VoSI curves in Figure 7 would improve interpretability.
- Using VoSI to design an adaptive sensing schedule and comparing it against fixed-rate sensing would concretely demonstrate the diagnostic's utility (if this is not already done in the appendix).

## Removed Points

- **Contribution 4 (greedy execution strategy) missing from the provided text.** Per the parser note, appendix sections are stripped from the extracted text; they exist in the original submission. This point is removed as a parser artifact.
- **Claim about "only one IL method and one MBRL method" being too limited.** The paper evaluates two SOTA approaches (Diffusion Policy for IL, TD-MPC2 for MBRL) on tasks where each is applicable. This is a reasonable scope for a single empirical paper; demanding more methods is scope creep.
- **Missing related works.** The paper's related work covers the relevant literature. No specific missing references were identified.

## Novel Insights

The most striking finding — that fully open-loop execution induces near-zero regret on several standard benchmarks — challenges a deeply held assumption in the robotics community that closed-loop sensing is necessary for good performance. The taxonomy of VoSI profile shapes (flat/gradual/stepped) provides a compact language for describing when sensing matters, and the correlation between policy proficiency and sensor independence is a non-obvious result that could have practical implications for efficient deployment. However, these findings must be interpreted as properties of the *specific policies studied*, not of the tasks themselves.

## Suggestions

1. **Reframe the paper's claims as policy-level diagnostics, not task-level properties.** Revise the abstract and Section 4 to consistently say "for the policies we studied" rather than implying these are inherent task properties.
2. **Provide quantitative validation of mixed-loop trajectory quality.** At minimum, report the fraction of mixed-loop trajectories that remain within success criteria or do not violate constraints, for a representative subset of states and horizons.
3. **Report action-chunk lengths for each task** and discuss how they relate to the tested open-loop horizons.
4. **Soften or remove the speculation about "manipulation benchmarks being outliers"** — or support it with a broader range of manipulation tasks.
5. **Include at least a brief summary of the greedy execution strategy in the main text** (assuming it exists in the appendix) so readers can assess the practical application of VoSI without reading the appendix.

## Score and Decision

The paper makes a novel empirical contribution with the VoSI diagnostic and reveals genuinely interesting patterns about sensing needs in standard robotic benchmarks. The methodology is well-motivated and the experiments are systematic. However, the paper consistently overstates the generality of its findings by presenting policy-specific results as task-level properties, and it provides no quantitative validation that the mixed-loop execution used to compute VoSI produces meaningful behavior. These are real rather than fatal weaknesses — they do not invalidate the core contribution but require the authors to substantially revise their claims and provide supporting evidence.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>