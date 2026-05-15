Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces VoSI (Value of Sensory Information), a framework to empirically measure how much task-relevant value a pre-trained look-ahead policy loses when sensory feedback is withheld for varying durations at different states. Using VoSI, the authors study seven robotic tasks with TD-MPC2 and Diffusion Policy agents, finding that (1) sensory information is surprisingly rarely critical in many standard benchmarks (especially Robosuite manipulation tasks), (2) better-trained policies degrade less under reduced sensing, and (3) VoSI profiles fall into three prototypical shapes (flat, gradual, stepped) that reflect task-phase structure.

## Strengths

- **Novel state-wise VoSI framework (Equation 1).** The idea of measuring regret from withholding sensing for exactly *h* steps starting from a specific state, rather than only studying fixed-rate execution across entire episodes, enables fine-grained analysis of *when* sensing matters. This clean operationalization is the paper's main methodological contribution.

- **Surprising empirical finding that several standard benchmarks show near-zero regret under open-loop execution.** Figure 3 robustly demonstrates that all three Robosuite manipulation tasks (coffee-pod, square-nut, threading) lose negligible performance even when sensing only once at the start of a trajectory. This is a concrete, reproducible observation that challenges assumptions about the necessity of dense sensing in popular benchmarks.

- **Demonstration of inverse correlation between policy proficiency and sensing sensitivity (Figure 5).** The paper shows that agents with more training steps or larger model capacity degrade less at reduced sensing rates. This holds across two different policy types (TD-MPC2 and Diffusion Policy) and is consistent with the paper's theoretical argument that finite expressivity substitutes for stochasticity in creating sensing needs.

- **Categorization of VoSI profiles into three interpretable shape prototypes (Figure 7).** The flat/gradual/stepped taxonomy provides an intuitive vocabulary for discussing when and why sensing matters at different phases of a task (e.g., stepped profiles at phase changes in cup-catch, flat profiles in the upright phase of swingup). This qualitative categorization, while not yet quantified, offers a useful conceptual framework.

- **Theoretical grounding in Section 4.1.** The formal argument that optimal policies with deterministic dynamics need no sensing (H(s_{t+1})=0) and the extension to finite-expressivity policies provides a principled lens for interpreting the empirical results. The four-rooms gridworld validation (Figure 4) cleanly illustrates how stochasticity and model error independently drive sensing needs.

## Weaknesses

### Fatal
None.

### Major

- **VoSI measures policy-specific sensitivity to sensor omission, not a task-inherent property — but some conclusions overreach what the metric supports.** VoSI(s,h) as defined in Equation (1) is the reward gap between closed-loop and mixed-loop execution of a *specific, pre-trained frozen policy π*. It quantifies how much that *particular policy* degrades when sensing is withheld. Yet the paper occasionally frames its findings as characterizations of the *tasks* themselves — e.g., "sensory complexity" ordering of tasks (Section 4), "Robosuite tasks may be outliers in terms of how little sensing... they require" — which sound task-inherent rather than policy-dependent. A different policy (e.g., one trained to be sensing-efficient) could yield different VoSI values. The paper acknowledges this tension in Section 6 ("our findings can only approximate this through what π can achieve") but does not fully reconcile it with the strength of the claims earlier in the paper. This is the single most important limitation: readers should interpret the findings as properties of the *studied policies* on these tasks, not fundamental limits of the tasks themselves.

### Minor

- **VoSI profile shapes lack statistical quantification and error bars.** Figures 7 and 10 show VoSI curves with no confidence intervals, error bars, or quantile bands. Each VoSI estimate is based on only 5 trajectory rollouts per *h* (stated in the implementation paragraph), which is a small sample for Monte Carlo estimation, especially on stochastic or contact-rich tasks. Without error bars, the reader cannot distinguish whether a "stepped" profile reflects a genuine phase change or sampling noise, nor whether a "flat" profile is truly flat or merely has wide intervals. The qualitative categorization into three prototypes would be stronger with a formal criterion (e.g., threshold on maximum derivative, or a clustering algorithm) rather than visual inspection.

- **The "inverse correlation" claim (proficiency ↔ sensing robustness) has a plausible confound not ruled out.** Figure 5 shows that larger/more-trained policies degrade less at reduced sensing rates. The paper frames this as evidence that better policies rely *less on sensory input*. However, an alternative hypothesis is that these policies are simply more robust to *any* distribution shift (including the OOD open-loop execution), not necessarily because they have learned to depend less on sensing. The paper's own theory (Section 4.1) predicts this result as a consequence of finite expressivity — better policies approximate the optimal policy better, and optimal policies need no sensing. So the finding is consistent with theory, but the "curiously" framing overstates the novelty. A control experiment measuring degradation under non-sensory distribution shifts would help distinguish these accounts.

- **Only two policy architectures (TD-MPC2, Diffusion Policy) are used, and each fails on complementary subsets of tasks.** This limits the generality of claims about "varying architectures." The paper acknowledges this honestly (line 44) but the resulting coverage is sparse: on any single task, typically only one architecture is evaluated. The cross-architecture comparisons that are possible (swingup, Push-T) show similar trends, which is a useful partial validation, but the evidence is thinner than the broad language in the introduction suggests.

### Trivial

- The theoretical analysis in Section 4.1 is presented as though it applies to the main empirical study, but the conditions (optimal policy, perfect dynamics model, deterministic dynamics) do not hold for any of the learned policies in the main experiments. The paper bridges this gap with a verbal argument about "finite expressivity" but validates it only on a toy gridworld, not on the main tasks. This makes the theory section feel somewhat disconnected from the experiments.

## Nice-to-Haves

- **Optimal-baseline comparison:** For a representative task, measuring VoSI using a policy trained to maximize reward *under the sensing-omission pattern*, not just a closed-loop-only policy. This would clarify whether the reported VoSI values reflect the task's inherent sensory requirements or artifacts of closed-loop-only training.
- **Stochastic dynamics in main tasks:** Adding action noise or randomized physics to the main robotic tasks and measuring VoSI on the same policies would directly test the paper's central theoretical claim that stochasticity drives sensing needs.
- **Cross-task quantitative comparison:** Using a summary statistic (e.g., average VoSI over states for a fixed *h*) to compare tasks quantitatively rather than through qualitative ordering.
- **Quantitative criteria for profile shapes:** A formal measure (e.g., maximum discrete second derivative, or a clustering algorithm) to replace visual sorting into flat/gradual/stepped categories.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that the distinction from Majumdar et al. (2023) is "unfair":** This is a subjective opinion about related-work positioning, not a substantive weakness of the paper. The paper's comparison accurately identifies a difference in approach (bounds vs. empirical analysis of when to sense). Removed per instruction to avoid subjective related-work critiques.
- **"Only two architectures" as a fatal weakness:** The paper uses the two dominant paradigms (model-based RL and imitation learning) and is transparent about which policy works on which task. "Varying" is accurate for n=2. Removed as a nitpick that does not harm any core claim.
- **Criticism that the Section 4.1 theory is "correct but trivial":** Whether a theoretical observation is trivial is subjective. The paper uses this analysis as a conceptual framework for interpreting experiments, not as a novel theoretical contribution. The finite-expressivity extension adds non-trivial insight. Removed as a subjective framing critique.
- **The "greedy sensing strategy" not being summarized in the main text:** The results are in the appendix (which the parser strips). The paper acknowledges this by listing it as Contribution 4. Removed per the rule about missing appendix content.

## Novel Insights

The single most penetrating observation across the reviews is the deep tension between the paper's metric and its interpretive framing. The harsh critic correctly identifies that VoSI measures *policy-specific* sensitivity to sensor dropout, yet the paper occasionally speaks of task "sensory complexity" as if the metric revealed a task-inherent property. This is not a fatal flaw — the paper acknowledges the limitation in Section 6 — but it points to an important subtlety: any empirical tool that probes a frozen policy will reflect properties of that policy alongside properties of the task. The paper's findings are best read as "these SOTA policies, trained only for closed-loop performance, happen to be surprisingly robust to sensor omission on these tasks" rather than "these tasks inherently require little sensing." This reframing preserves the value of the empirical observations while avoiding overclaiming. The profile-shape taxonomy (flat/gradual/stepped) is a genuinely useful descriptive tool that is largely orthogonal to this concern, since it characterizes *when* (not just *whether*) sensing matters for a particular policy on a particular task.

## Suggestions

1. **Reframe the main claims to explicitly acknowledge the policy-specific nature of VoSI.** Replace language like "sensory complexity of tasks" with "sensory sensitivity of the studied policies on these tasks." The abstract and conclusion should consistently attribute findings to the specific trained agents rather than to the tasks in general.

2. **Add confidence intervals or quantile bands to VoSI profile plots (Figures 7, 10).** With only 5 trajectories per *h*, the variance is likely substantial. Even bootstrapped confidence bands would greatly improve the reader's ability to assess whether profile shapes are meaningful. This is a straightforward addition that would substantially strengthen the paper's empirical rigor.

3. **Provide a formal criterion for categorizing profile shapes** (e.g., maximum of the discrete second derivative exceeding a threshold for "stepped," slope below a threshold for "flat"). This would replace visual inspection with a reproducible method.

4. **Include a brief control experiment** (or at minimum a discussion) distinguishing sensing-specific robustness from general OOD robustness. For example, comparing degradation under action noise vs. sensing reduction on a representative task would help validate the interpretation of Figure 5.

5. **Soften the "curiously" framing** around the proficiency-correlation finding (Figure 5), since this result is exactly what the paper's own theory (Section 4.1) predicts: better policies more closely approximate the optimal policy, which needs no sensing.

## Score and Decision

The paper introduces a genuinely novel and practically useful empirical framework (VoSI), applies it across diverse tasks, and produces several interesting observations. The main limitation — that VoSI measures policy-specific robustness rather than task-inherent sensory value — is a genuine structural concern, but it is partially acknowledged in the paper and does not invalidate the core contributions. The framework itself is sound, and the findings, when interpreted as properties of the studied policies, are informative. With a more careful reframing of claims and addition of statistical quantification on the profile plots, the paper would be a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>