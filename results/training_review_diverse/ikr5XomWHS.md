Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes VoSI (Value of Sensory Information), an empirical framework for measuring how much task performance degrades when sensing is withheld at specific states along a robot's trajectory. Using look-ahead policies (TD-MPC2 and Diffusion Policy) across 7 robotics tasks (DM-control, Robosuite, Push-T), the authors compute state-wise "VoSI profiles" and categorize them into three prototypical shapes (flat, gradual, stepped). The key empirical findings are that sensory information is rarely task-critical in many standard benchmarks, and that better-trained policies are more robust to sensor loss.

## Strengths

1. **Novel state-wise VoSI profiles enable fine-grained temporal analysis of sensing needs.** Unlike prior value-of-information work (e.g., Majumdar et al. 2023) that provides global bounds or only studies fixed-rate sensing, this paper proposes VoSI profiles (Section 5, Eq. 1) that measure, per state, how task performance degrades when sensing is withheld for varying durations. The classification into flat, gradual, and stepped profile shapes (Figure 7) with concrete visualizations (Figures 8, 10) is genuinely new and provides actionable insight into *when* along a trajectory sensing matters.

2. **Systematic empirical study across diverse tasks and two SOTA policy architectures.** The paper evaluates 7 tasks spanning dynamic locomotion (DM-control), static tabletop manipulation (Robosuite), and contact-rich pushing (Push-T), using both a model-based RL policy (TD-MPC2) and an imitation learning policy (Diffusion Policy). This breadth (Section 4, Figures 2-3) supports the paper's descriptive findings about sensory requirements varying across task types.

3. **Counterintuitive finding with practical implications.** Figure 3 shows that on Robosuite tasks, policies achieve near-zero regret (within 95% CI) even under fully open-loop execution. DM-control swingup and Push-T also show strong robustness at reduced sensing rates. The paper correctly connects this to recent observations by Dasari et al. (2022) and Wang et al. (2024), lending credibility to the finding.

4. **Four-rooms toy experiment causally identifies task characteristics driving sensing needs.** The controlled experiment in Section 4.1 (Figure 4) shows that increasing environment stochasticity (varying p) and dynamics model error both produce progressively higher regret from reduced sensing. This provides a principled explanation for the observed variation across tasks.

5. **Demonstration that competency correlates with sensor robustness.** Figure 5 shows that policies at later training stages and with higher model capacity degrade less at lower sensing rates. This inverse correlation between performance and sensor dependency is a nontrivial empirical finding with potential implications for efficient deployment.

## Weaknesses

### Fatal
None.

### Major

1. **The VoSI measure conflates information value with policy robustness, and the paper's response to this confound is insufficient.** The paper defines VoSI as the reward gap between closed-loop and mixed-loop execution of a *frozen policy* trained only for closed-loop operation. The paper acknowledges this (Section 5: "standard pre-trained look-ahead policies ... would be operating out-of-distribution when executed in mixed loop mode") but dismisses it with a hand-wavy "appear to hold up well enough to produce coherent and interpretable findings" and a circular appeal to alignment with Section 4.1's theoretical expectations. This is not adequate. The performance drop could reflect the policy's inability to handle out-of-distribution execution patterns rather than the inherent value of the withheld sensory information. The Robosuite results are especially ambiguous: these are deterministic tabletop tasks where open-loop success could reflect either (a) genuinely low sensory requirements or (b) policies that have learned highly stereotyped trajectories requiring no mid-trajectory correction. VoSI as defined cannot separate these. Even acknowledging this limitation explicitly, as the paper does, the core framing of VoSI as measuring the "value" of sensory information rather than "policy fragility under distribution shift" overstates what has been demonstrated. This does not invalidate the framework but means the paper's headline claims must be interpreted as *observations about how specific trained policies behave under reduced sensing*, not about the inherent sensory requirements of the tasks.

2. **The paper's framing overclaims generality relative to the evidence.** The title "The Value of Sensory Information to a Robot" and abstract claims like "sensory information is surprisingly rarely task-critical in many commonly studied task setups" imply conclusions that extend beyond the 7 tasks, 2 architectures, and single-seed training runs studied. The limitations section (Section 6) partially addresses this, but the main contributions (Section 1) and the narrative throughout Sections 4-5 frame the findings as revealing task-level properties rather than policy-level ones. The paper would be substantially stronger and more honest if reframed as "an empirical study of the sensory requirements of current SOTA policies on standard benchmarks" rather than as revealing general truths about sensing and task performance.

### Minor

3. **The connection between the optimal-policy analysis (Section 4.1) and the experiments is suggestive but not evidential.** The paper correctly shows that for an optimal policy with perfect sensing and deterministic dynamics, sensing after the first step has zero value. It then argues that "finite expressivity" drives the need for sensing in the main experiments. However, the experiments only vary training checkpoint and model capacity (Figure 5), showing a correlation consistent with this hypothesis, without directly testing whether the policy is capable of learning the deterministic dynamics or quantifying the role of expressivity limitations. The four-rooms toy experiment provides intuition but is not run on the 7 actual tasks. This does not invalidate the claim, but the link between theory and experiments is looser than the paper's narrative suggests.

4. **Statistical precision is thin for the fine-grained VoSI profiles.** The paper uses 5 rollouts per state per h-value (Section 5) to estimate VoSI. While the fixed-rate analysis (Figure 3) reports 95% confidence intervals, the state-wise VoSI profile figures (Figures 7, 10) do not report any variance estimates. Given the contact dynamics and stochastic elements in tasks like Push-T and cup-catch, some profile shapes may be noisy. Given the computational expense noted by the authors (500 trajectories per state), this is understandable, but it weakens confidence in the finer-grained claims about profile shapes.

5. **Contributions 3 and 4 are underdeveloped.** Contribution 3 (VoSI applicability under stochastic dynamics and noise) and Contribution 4 (greedy sensing strategy) are mentioned in the contribution list but receive minimal treatment in the paper. The "greedy strategy" is especially thin — no task it was tested on, no baseline comparison, no quantification of improvement. These should either be fleshed out with experimental results or removed from the contribution list to avoid over-promising.

6. **Interaction between look-ahead chunk length n and VoSI is not discussed.** The paper studies VoSI and fixed-rate sensing as a function of open-loop window h, but the policy's action-chunk length n is a design parameter that directly affects how robust the policy naturally is to missing sensing. A policy with very long chunks might be inherently more stable under open-loop execution. This is a potentially important confound that is not analyzed.

### Trivial
None.

## Nice-to-Haves

- **Validation against an oracle.** On tasks with known dynamics (e.g., DM-control), computing the performance of a truly optimal open-loop trajectory (via model-based planning) and comparing it to the mixed-loop policy execution would calibrate how much of VoSI is attributable to information necessity vs. policy suboptimality.
- **Variance estimates for VoSI profiles.** Adding confidence bands to Figures 7 and 10 would significantly strengthen the credibility of the profile shape classification.
- **Seed-averaged VoSI.** Computing VoSI profiles across an ensemble of policies trained from different random seeds would distinguish task-driven VoSI from policy-idiosyncratic VoSI.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The framing 'more sensing always improves task performance' is a straw man."** The paper describes a common intuition and immediately cites Mason (1993) and Erdmann & Mason (1988) who argue the opposite. The paper's own claim is precisely about understanding *when* sensing is valuable, so it is not setting up a straw man.
- **"The optimal-policy analysis is trivial."** The analysis (deterministic dynamics → no value to sensing after step 1) is simple but serves its purpose as a theoretical baseline. The paper uses it to motivate the empirical question, not as a contribution. This is not a weakness.
- **"The paper should also cover Y / domain Z / additional tasks."** The paper studies 7 tasks across 3 benchmarks with 2 architectures. For a first empirical study proposing a new measurement framework, this is a reasonable scope. Demanding more tasks or domains is scope creep.
- **Complaints about missing appendix or proofs.** The parser strips supplementary material; these likely exist in the original submission.

## Novel Insights

The reviews surface one genuinely valuable insight the paper itself does not fully articulate: the VoSI framework, as implemented, is best understood not as measuring the inherent "value of sensory information" to a robot in general, but as diagnosing the *open-loop robustness footprint* of a specific trained policy. The fact that VoSI profiles are policy-dependent (the paper shows this in Figure 5) is actually the feature, not the bug — the framework could be used as a diagnostic tool for policy generalization and robustness, analogous to how saliency maps are used in vision. The harmful framing mismatch is that the paper presents this as revealing task properties when the measure is fundamentally about policy properties. Reframed as "a method for characterizing when a learned policy relies on sensory feedback," the contribution would be cleaner and the limitations would become less problematic.

## Suggestions

1. Reframe the paper's claims explicitly as being about *trained policies* rather than about tasks or robots in general. This would honestly characterize what VoSI measures and make the limitations less damaging.
2. Add a validation experiment on at least one task where the ground-truth sensory requirements are known (e.g., by introducing a state-dependent perturbation mid-trajectory and showing VoSI correctly spikes at that moment).
3. Either flesh out the greedy sensing strategy with concrete experiments or drop it from the contribution list. It currently exists only as a placeholder.
4. Add confidence intervals or variance bands to the VoSI profile figures (Figures 7, 10), or at minimum a discussion of the noise level.
5. Discuss how the action-chunk length n of the look-ahead policy interacts with the VoSI measurements.

## Score and Decision

The paper proposes a novel and genuinely useful framework for analyzing when sensory information matters to a decision-making policy. The VoSI profile shapes (flat, gradual, stepped) are intuitively meaningful and well-visualized. The core empirical finding — that many standard benchmark tasks can be solved with surprisingly little mid-trajectory sensing — is interesting and connected to concurrent observations in the literature. However, the paper has two significant issues: (1) the VoSI measure has a known confound (policy robustness vs. information value) that is acknowledged but not resolved, and the paper's dismissal of it is too casual; (2) the framing consistently overclaims generality, presenting policy-level observations as task-level truths. These do not invalidate the contribution but mean the paper needs substantial revision in framing and at least one validation experiment to be fully convincing. On balance, the novelty of the framework outweighs the limitations, but just barely in the current form.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>