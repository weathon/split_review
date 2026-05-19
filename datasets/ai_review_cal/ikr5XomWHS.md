- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 5, 6
Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes VoSI (Value of Sensory Information), an empirical framework for measuring how valuable sensory observations are to a pretrained robot policy at different moments during task execution. The core idea is to characterize regret induced by withholding state observations for varying durations (mixed-loop execution) using look-ahead policies. The paper studies 7 robotic tasks across DM-Control, Robosuite, and Push-T, with two SOTA architectures (TD-MPC2 and DiffusionPolicy), finding that (1) open-loop execution works surprisingly well on several benchmarks, (2) stochastic dynamics and model error are the main drivers of sensing need, and (3) better-trained policies are more robust to sensor dropout.

## Strengths

1. **A novel state-wise measure of sensory value (VoSI) that goes beyond aggregate sensing rates.** Section 5 defines VoSI (Equation 1) as the performance gap between closed-loop and mixed-loop execution starting from a specific state, then profiles this gap as a function of open-loop duration. The paper demonstrates three empirically distinct profile shapes (flat, gradual, stepped) across tasks, revealing that sensory value varies sharply with the moment and task phase. This granularity is absent in prior VoI work (Flaspohler et al. 2020, Majumdar et al. 2023) that aggregates over time or restricts to simple environments.

2. **Systematic empirical study across 7 diverse tasks and 2 SOTA architectures.** Figure 3 plots normalized regret vs. sensing frequency for TD-MPC2 and DiffusionPolicy across DM-Control, Robosuite, and Push-T. On three Robosuite tasks, even fully open-loop execution yields near-zero regret; on DM-Control tasks, sensing every 5 steps matches closed-loop performance. The study covers varied robot morphologies and policy synthesis approaches (RL, imitation), providing a broad empirical landscape.

3. **Clean causal isolation of stochasticity vs. model error using a toy gridworld.** Section 4.1's four-rooms experiment (Figure 4) independently varies stochastic dynamics and model misspecification, producing regret profiles that align with theoretical intuition. This controlled reference strengthens interpretation of the more complex robotic experiments and validates that the VoSI measurement recovers expected patterns in a tractable setting.

4. **Demonstration of an inverse correlation between policy proficiency and sensor dependency.** Figure 5 shows that as training progresses on Push-T and swingup, regret at low sensing rates shrinks, and higher-capacity models degrade less when sensing is reduced. This counter-intuitive finding — better-trained agents rely *less* on moment-by-moment sensing — is supported on two tasks with two policy types.

5. **A complexity ordering of task suites derived from sensory regret profiles.** The paper establishes an ordering (Robosuite < DM-Control < Push-T) in terms of sensory demand, providing a concrete, reproducible fingerprint that can guide future benchmark design.

## Weaknesses

### Fatal
None.

### Major

1. **The mixed-loop execution methodology has an unresolved out-of-distribution confound.** The central experiments execute pretrained closed-loop policies in mixed-loop mode (receiving a state at the start of a block, then executing the action chunk open-loop for h steps). The paper acknowledges (Section 5) that policies "would be operating out-of-distribution when executed in mixed loop mode" and that "τMixL... might produce erratic behaviors," but the dismissal — "appear to hold up well enough to produce coherent and interpretable findings" — lacks rigorous validation. The observed regret could stem from either (a) the genuine task-relevant value of withheld sensory information, or (b) the policy producing degraded actions because its architecture is not designed for open-loop execution. These are different quantities, and the paper does not disentangle them. A validation experiment comparing action divergence between open-loop and closed-loop execution from the same state, or a control experiment on a task with known ground-truth sensory value, would significantly strengthen the claims. As written, the interpretation of every quantitative result in Sections 4 and 5 is partly ambiguous.

### Minor

2. **The VoSI profile analysis (Section 5) is purely qualitative with no quantitative characterization.** The classification into "flat," "gradual," and "stepped" profiles is based on visual inspection of selected states (Figure 7). The paper does not provide quantitative definitions or thresholds for the profile types, report the distribution of profile types across all sampled states for each task, or offer summary statistics (e.g., fraction of states where VoSI exceeds a threshold for a given h). The overlays in Figure 10 are mentioned but no statistics accompany them. Given that the paper samples 5,000 states per task, the analysis could be substantially more informative.

3. **The framing of findings as "surprising" is overstated given the experimental setup.** The abstract claims "sensory information is surprisingly rarely task-critical." However, the paper's own theoretical analysis (Section 4.1) establishes that for optimal policies under deterministic dynamics, open-loop execution should work perfectly. The paper further acknowledges that "these Robosuite tasks may be outliers in terms of how little sensing / perceptual capabilities they require" and that all main experiments use "deterministic dynamics, as in most robotic benchmark tasks." The empirical finding that open-loop works on simple, deterministic tasks with learned policies is consistent with theory and intuition. The paper would be strengthened by more carefully scoping the "surprise" to the specific finding that even complex contact tasks (Push-T, cup-catch) tolerate low sensing rates, rather than the existence of the phenomenon itself.

4. **Limited evidence for the training-proficiency correlation claim.** The finding that better-trained agents are more robust to sensor dropout (Figure 5) is demonstrated on only two tasks (Push-T and swingup). While suggestive and interesting, this is presented as a general finding but lacks sufficient breadth of evidence.

### Trivial

None.

## Nice-to-Haves

- **Validation of the OOD concern via action divergence analysis:** Recording the actions produced by the policy at timestep t+h when given the true state (closed loop) vs. when executing the chunk from s_t (open loop) would directly address the major weakness. If these actions are similar, the regret measured genuinely reflects missing state information.
- **Stochastic dynamics on a non-toy task:** The paper argues that stochasticity is the key driver of sensing need but only tests this on the gridworld. Adding mild action noise to one of the main robotic tasks (e.g., swingup or Push-T) would substantially strengthen the causal argument.
- **Quantitative profile analysis:** Reporting histograms of VoSI(1) values across states, or the fraction of states where VoSI(h) exceeds a threshold, would give readers a sense of how pervasive sensing value is rather than showing a few curated examples.

## Removed Points

The following points from the reviews were removed with justifications:

- **Missing appendix content (Contributions 3 and 4: stochastic dynamics on non-toy tasks, greedy sensing strategy):** The reviewer faults the paper for not including these in the main body. Per policy, the parser strips appendix sections from all papers; these exist in the original submission. Removed.
- **Missing related works on active perception / attention:** Per policy, missing related works should not be flagged as the reviewer does not have complete knowledge of the literature. Removed.
- **Gridworld uses optimal policies not learned policies:** This criticism misunderstands Section 4.1, which is explicitly about establishing the theoretical baseline using optimal policies. The section's purpose is to validate the VoSI measurement under known ground truth. Removed.
- **Reproducibility nitpicks about undisclosed hyperparameters / training details:** Per policy, trivial implementation details impractical for a submission should not be flagged. Removed.
- **Formatting, style, and presentation nitpicks:** Per policy, parser artifacts are not author errors. Removed.

## Novel Insights

The harsh critic's most valuable contribution is the identification that the OOD confound is not adequately resolved. This is not merely a "limitation to be discussed" but a structural ambiguity in the main result's interpretation. Conversely, the fusion of the two reviews reveals an interesting tension: the paper's gridworld validation (Figure 4) actually provides partial evidence against the OOD concern — in that controlled setting, the optimal model-based policy *does* behave as theory predicts under mixed-loop execution, suggesting the methodology at least recovers correct answers in a tractable case. The fact that the paper does not leverage this as an explicit validation of the mixed-loop methodology (e.g., by comparing action divergence in the gridworld) is a missed opportunity that neither reviewer fully articulated.

## Suggestions

1. **Add a validation experiment for the mixed-loop methodology.** For a sample of states across tasks, record actions produced by the policy at timestep t+h when given the true state vs. when executing the chunk from s_t. If these actions are similar (low divergence), the regret genuinely measures missing information. If they diverge, the confound is real and the claims need re-scoping.

2. **Provide quantitative VoSI profile statistics.** Report for each task: the fraction of states where VoSI(h) exceeds X for each h, the most common profile shape per task (with a concrete classification algorithm), and histograms of VoSI values.

3. **Temper the abstract's language.** Replace "surprisingly rarely task-critical" with a more measured claim: "open-loop execution performs comparably to closed-loop on several standard benchmarks under deterministic dynamics, with important exceptions in contact-rich and dynamically complex tasks."

4. **Add stochastic dynamics to at least one main robotic task** (e.g., 5% action noise on swingup or Push-T) and show that VoSI increases, directly testing the paper's central causal hypothesis.
