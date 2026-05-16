Now I have a thorough understanding of the paper and can evaluate each reviewer claim against the actual content. Let me write the consolidated review.

## Summary

This paper proposes ASID, a three-stage pipeline for sim-to-real transfer: (1) train an exploration policy in simulation that maximizes Fisher information about unknown physical parameters, (2) deploy it in the real world for a single episode, then perform optimization-based system identification to refine the simulator, and (3) train a downstream task policy in the refined simulator for zero-shot real-world transfer. The method is evaluated on rod balancing, sphere striking, and articulation tasks in simulation, and on rod balancing and shuffleboard in the real world.

## Strengths

- **Principled, well-motivated pipeline for targeted exploration.** The paper grounds exploration policy design in the Cramér-Rao lower bound, using A-optimal experiment design (trace of inverse Fisher information) as the training objective. The connection between Fisher information maximization and collecting trajectories sensitive to unknown parameters is clearly articulated (Section 4.1), and the relaxation via domain randomization over the prior $q_0$ is a reasonable practical approximation.

- **Strong quantitative outperformance on rod balancing in simulation.** In Table 1, ASID+SysID achieves near-perfect tilt angles (0.00°, 0.72°, 0.00°) across three inertia configurations, while every baseline (random exploration: 4.20°–15.34°, Kumar2019: 2.82°–15.26°, domain randomization: 1.13°–26.69°, ASID+estimator: 4.65°–17.73°) yields substantially worse results. This directly supports the claim that the combination of Fisher-information-guided exploration and optimization-based sysID is critical for accurate parameter estimation.

- **Real-world validation on two challenging manipulation tasks.** On rod balancing, ASID succeeds 6/9 times across three inertia settings vs. 0/9 for domain randomization. On shuffleboard, ASID succeeds 7/10 times vs. 3/10 for DR. These experiments demonstrate that the pipeline can be executed fully autonomously end-to-end and outperforms the leading sim-to-real alternative (DR) that uses no real data.

- **Ablation isolating the importance of optimization-based sysID.** The "ASID + estimator" row in Table 1 replaces optimization-based sysID with a learned estimator, and performance collapses (rod balancing: 4.65°–17.73°, sphere striking: 11.00%). This shows that the full pipeline — not just good exploration — is required, and the optimization-based sysID step is the key enabler.

- **Effective multi-parameter exploration visualization.** The visitation heatmap (Figure 3) shows ASID's exploration policy achieving near-uniform coverage over three friction regions, while the Kumar2019 baseline barely leaves the starting region. This provides qualitative but striking evidence that Fisher-information maximization yields genuinely exploratory behavior.

## Weaknesses

### Fatal
None.

### Major

- **Unexplained asymmetry between rod balancing and sphere striking results.** The paper's core claim is that a single episode of Fisher-information-guided exploration enables accurate system identification. On rod balancing, the results are near-perfect (0.00° tilt). On sphere striking, the success rate is only 28.00% ± 9.7% — the method fails three-quarters of the time. While this is still ~3× better than any baseline (~10%), the paper offers no analysis of *why* the same pipeline succeeds dramatically on one task but barely improves on another. The paper frames the method as broadly effective, but this asymmetry is a genuine puzzle that should be explained. Is sphere striking harder because the friction parameter is harder to excite? Because the downstream task is more sensitive to residual error? Because the Gaussian dynamics assumption (Eq. 3) is a worse fit for contact-rich striking dynamics? Without an analysis, the reader cannot assess the scope of applicability.

- **Real-world experiments lack proper baselines to isolate the value of targeted exploration.** The real-world experiments compare ASID only against domain randomization (DR), which uses *zero* real-world data. The relevant scientific question is: given a budget of one real-world episode, does Fisher-information-guided exploration yield better results than simpler alternatives (e.g., a random exploration policy, or a coverage-maximizing policy) with the *same* system identification and policy training pipeline? The simulation experiments include a random exploration baseline (Table 1), but the real-world experiments do not. This makes it impossible to attribute the real-world improvements to the Fisher information objective versus merely having *any* real data or *any* directed exploration.

- **Limited statistical rigor in real-world experiments.** The rod balancing experiment uses only 3 trials per inertia condition (6/9 overall), and the shuffleboard experiment uses 5 trials per target zone (7/10 overall). No confidence intervals, bootstrapped estimates, or statistical significance tests are reported. With such small counts, a single trial outcome shift changes the conclusion. While small-N real-world experiments are common in robotics, the paper's claims about "efficacy" and "effectiveness" would be substantially strengthened by at least reporting exact binomial confidence intervals.

### Minor

- **No direct measurement of parameter estimation accuracy.** The paper evaluates only downstream task success, which conflates exploration quality, sysID quality, and policy optimization. Reporting actual parameter estimates (e.g., estimated mass, friction, inertia vs. ground truth) would directly validate the exploration and sysID steps and help explain why sphere striking succeeds only 28% of the time — is the parameter estimate sometimes accurate but the policy still fails, or is the estimate always poor?

- **Number of seeds/runs for simulation experiments is not stated.** Table 1 reports means and standard deviations, but the paper never states how many independent seeds or runs these statistics cover. This is a basic reproducibility detail.

- **Exploration policy training is underspecified.** The paper says it uses PPO to solve the objective in Eq. 6, but does not describe the reward function formulation used to drive PPO (e.g., how -tr(I(θ,π)^{-1}) is converted into a reward signal), the network architecture, or the number of simulation rollouts per policy update. While the core method is clear, these details would help practitioners reproduce the approach.

- **The paper does not discuss the computational cost of finite-differences gradient approximation.** The finite-differences approach (Section 4.1) scales linearly (or worse) with the number of unknown parameters, but the paper never analyzes this cost or validates its accuracy for the parameter spaces used.

### Trivial

- The paper mentions the articulation environment and reports an 80% vs. 20% interaction rate, but the main text provides no quantitative downstream task results. (The appendix is referenced and presumably contains fuller evaluation; the parser strips appendices, so this is noted but not weighed heavily.)

## Nice-to-Haves

- Varying the number of real-world exploration episodes (1, 2, 5, 10) and plotting task success vs. parameter estimation error would directly test the central claim that a single episode suffices.
- A failure analysis for real-world experiments (why did 3/9 rod-balancing trials and 3/10 shuffleboard trials fail?) would greatly improve practical guidance.
- Sensitivity analysis to the choice of prior $q_0$ over parameters would help understand when the exploration policy's domain randomization assumption holds.
- Reporting parameter estimation accuracy alongside downstream task success would isolate the contribution of each pipeline stage.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about "the paper does not clearly distinguish itself from prior work" (Kumar et al. 2019):** The paper explicitly contrasts its Fisher-information objective with Kumar et al.'s mutual-information objective (Section 5.1, line 224) and situates its contribution as bridging classical experiment design with modern sim2real (Section 2, lines 42-46). The distinction is adequately drawn.

- **Criticism about the articulation experiment being "incomplete and cannot be evaluated":** The paper references the appendix (apdx:articulation) for quantitative results, which the parser strips. Per policy, appendix content is assumed to exist in the original submission. The main text does provide a qualitative metric (80% vs. 20% interaction rate).

- **Criticism about the Gaussian dynamics assumption (Eq. 3) lacking evidence for robustness:** The paper explicitly argues this is an intuitive approximation even when dynamics deviate (line 178: "even in cases when the dynamics may not follow it exactly"), and the empirical success on real tasks provides indirect evidence. This is a standard approximation argument, not an unsubstantiated claim.

- **Criticism about "the paper would be better served by a more measured presentation":** The abstract's claim ("only a small amount of real-world data can allow for effective sim-to-real transfer") is supported by the rod balancing (near-perfect sim, 6/9 real) and shuffleboard (7/10 real) results. The sphere striking result is weaker but the paper reports it transparently with standard deviation.

- **Various nitpicks about undisclosed hyperparameters (learning rate, batch size, architecture, etc.):** These are trivial implementation details that are standard to leave out of a conference submission, per policy.

- **Criticism about actions being unobservable for system identification:** Actions are commanded by the robot's controller; they are observable by definition. The paper's approach of replaying the same action sequence is standard.

- **Criticism that the "ASID + estimator" ablation performs poorly and the paper doesn't explain why:** The table caption (line 303) states "Learned system identification doesn't generalize to unseen trajectories," which is a clear explanation of the phenomenon.

- **Complaints about the method being applied to "modern, real-world robotics tasks" as a novelty claim not being distinctive:** The paper positions itself as bridging classical experiment design with modern sim2real, which is a legitimate contribution framing.

## Novel Insights

A genuinely novel observation that emerges from this review is that the exploration policy transfers from sim to real much more reliably than the task policy does — the paper's "ball-hitting" analogy (any contact suffices for exploration, but precise contact is needed for the task) is well-supported by the evidence. However, the large gap between rod balancing (near-perfect) and sphere striking (28%) suggests a more nuanced principle: Fisher-information-guided exploration works best when the unknown parameters are *directly and strongly* coupled to the dynamics (inertia directly determines rod behavior under gravity), and degrades when parameters have more diffuse or higher-order effects (friction affects the ball's rolling/bouncing trajectory over many steps). This is a testable hypothesis the paper could and should investigate.

## Suggestions

1. Add an explicit failure analysis section discussing why sphere striking succeeds only 28% of the time while rod balancing succeeds nearly perfectly. This is the single most important addition.
2. Include a real-world baseline using random exploration (or a simpler directed exploration policy) with the same system identification pipeline to isolate the value of Fisher-information-guided exploration.
3. Report parameter estimation accuracy (estimated vs. true parameters) alongside downstream task success.
4. State the number of seeds/runs for all simulation experiments explicitly.
5. Report exact binomial confidence intervals for real-world trial counts.
6. Add a limitations section discussing when the method may fail (high-dimensional parameter spaces, poor sim-to-real transfer of exploration policies, tasks requiring precise timing).

## Score and Decision

The paper proposes a well-motivated and principled pipeline, demonstrates strong results on rod balancing (both sim and real), provides useful ablations, and includes real-world validation on two tasks. However, the unexplained asymmetry between near-perfect rod balancing and weak (28%) sphere striking results, the lack of proper real-world baselines that isolate the exploration contribution, and the limited statistical rigor in real-world experiments are significant gaps that prevent strong acceptance. The core idea is sound and the paper merits a borderline score.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>