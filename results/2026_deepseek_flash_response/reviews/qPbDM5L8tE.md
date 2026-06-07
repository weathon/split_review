Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

**CoRAL** proposes a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation that separates a VLM (perception, physical parameter estimation) from an LLM (cost function generation, contact strategy, online adaptation), connected to an MPPI controller with a memory unit for experience reuse. The system is evaluated on six simulated manipulation tasks against OpenVLA, π0.5, and human-expert-designed cost baselines.

## Strengths

1. **Empirical evidence that separating VLM from LLM roles is critical**: The Unified VLM ablation — which collapses perception and reasoning into a single GPT-4o call — scores 0/10 on four of six tasks, while the full separated-role architecture achieves 9–10/10 on four tasks and 7/10 on the hardest (Table 1, line 182). This directly validates the paper's core architectural claim and goes beyond prior decoupled frameworks (IMPACT, VLMPC) that use a single VLM.

2. **LLM-generated cost function structure (not just goal identification) is novel and quantified**: The LLM generates the *mathematical structure and weights* of the MPPI cost function itself (Eq. 2, lines 89–91). On T6, the LLM-guided contact strategy makes the system **83.9% faster** (32 vs. 199 steps) with a **63.9% shorter end-effector path** (1.33 m vs. 3.69 m) compared to providing only the cost function without contact strategy (Section 4.1.4, lines 216–218).

3. **Ablation study systematically isolates each design choice**: Five ablations (w/o Pose Tracking → 0/10 on 5 tasks, Unified VLM → 0/10 on 4 tasks, w/o Refinement → drops on T1 and T6, w/o Memory → drops on T1 and T3, full CoRAL) target distinct claims with clear degradation patterns that are difficult to attribute to confounding factors.

4. **Quantified benefit of memory-based experience reuse**: The memory module boosts success rate on the multi-stage T1 task from 2/10 to 4/10 and on T3 from 9/10 to 10/10, while reducing completion times on several tasks (Table 1, lines 179–180). This provides concrete evidence after only a single stored successful episode.

5. **Meaningful upper-bound baseline via human-expert-designed cost functions with FSM**: The paper compares against both single-stage and FSM expert-designed costs (Table 1, lines 176–177), providing an honest upper bound that isolates the gap between LLM-generated and human-designed costs. This is stronger baseline design than typical "just compare to VLAs" evaluations.

## Weaknesses

### Major

- **Asymmetric VLA baseline comparison undermines the central comparative claim**: The paper claims CoRAL "significantly outperforms both state-of-the-art baselines" (line 193), but this comparison is structurally asymmetric. OpenVLA-OFT and π0.5 are evaluated using their LIBERO checkpoints on tasks (T1, T4, T5, T6) that are *not* LIBERO tasks — they are custom tasks outside the baselines' training distribution. On the two tasks that *are* from LIBERO (T2, T3), CoRAL is comparable (10/10 vs. 10/10 and 10/10 vs. 9/10/8/10) but 5–10× slower (45–49 s vs. 5–13 s). While evaluating VLAs zero-shot on novel tasks is informative, the headline claim of "significant outperformance" conflates distribution mismatch with genuine superiority. This does not invalidate the paper's other contributions (the ablations and human-expert comparisons are independent), but it does mean the paper claims more than the evidence supports. The authors should reframe the VLA comparison as assessing zero-shot generalization rather than a head-to-head contest on equal footing.

### Minor

- **Sim-only evaluation despite sim-to-real robustness claims**: All experiments are conducted in MuJoCo simulation. The paper states that the reactive control augmentation (Eq. 7) is designed for "robustness against the inherent sim-to-real gap" (line 126), and the mass-adaptation experiment is presented as demonstrating robust parameter correction. However, the gap is never crossed — there are no real-robot experiments. Claims about robustness to unmodeled dynamics, sensor noise, and real-world contact physics remain unsupported.

- **Small evaluation sample size**: Each task is evaluated over 10 trials with a binary success metric. No confidence intervals, standard deviations, or statistical significance tests are reported. Several ablation comparisons (e.g., 4/10 vs. 2/10 on T1 with/without memory) rest on differences of 1–3 trials, which may not be statistically meaningful.

- **The "zero-shot" framing is imprecise**: The paper describes CoRAL as "zero-shot" (abstract, line 28, line 49). The system requires known 3D geometric models of all objects, a pre-built physics simulator (MuJoCo) with known robot dynamics, FoundationPose (a trained pose estimator requiring object meshes), and carefully hand-tuned MPPI hyperparameters (K=200, H=50, λ=0.1, N_retry=15). This is closer to "does not require task-specific teleoperation demonstrations" than to zero-shot in a practically unconstrained sense. The framing should be scoped more precisely.

- **Mass adaptation experiment needs clarification**: The paper states the evaluation world was initialized with a mass of 2.0 kg vs. ground truth 0.1 kg, and claims the corrected mass converged "remarkably close to their true values" (line 222). The figure description shows corrected mass converging to ~0.85 kg — still an 8.5× error vs. the stated 0.1 kg ground truth. Additionally, the figure's y-axis (0.75–1.00 kg) does not show the 2.0 kg or 0.1 kg values mentioned in the text. This discrepancy between claim and data needs resolution (the figure description may be a parser artifact, but as presented it is confusing).

- **VLM physical parameter estimation is not independently validated**: The VLM (GPT-4o) estimates mass and friction from visual appearance, but there is no evaluation of how accurate these initial estimates are before the outer loop corrects them. The ablation shows the outer loop can correct errors, but the base accuracy of the VLM's physical reasoning remains uncharacterized.

- **Memory retrieval mechanism is underspecified**: The paper states the LLM "embed[s] the current task into a latent semantic space" (lines 75–76) for retrieval, but provides no details about the embedding mechanism, similarity metric, or retrieval threshold. This is insufficient for reproducibility.

### Trivial

- Hyperparameter N_retry=15 (outer-loop trigger threshold) is stated without justification (line 134).
- The feedback gain K_f in Equation 7 is mentioned but no values or tuning procedure are provided.
- The randomized object dimension for the box (line 155) raises a question about FoundationPose tracking — if the object model M provided to FoundationPose is not updated to match the randomized dimension, pose tracking would break. This detail needs clarification.

## Nice-to-Haves

- Sensitivity analysis on MPPI hyperparameters (K=200, H=50, λ=0.1, N_retry=15, K_f)
- Computational cost reporting: per-step planning time, number of LLM API calls per task, total compute cost
- Systematic failure analysis across all tasks instead of the single anecdotal case
- A single real-robot experiment on a Franka arm, even with a simplified setup, to ground the sim-to-real robustness claims
- Independent validation of the VLM's accuracy in estimating mass and friction from visual appearance

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism that human expert baselines outperform CoRAL (Harsh Critic Issue 3)**: The paper is transparent about this comparison, explicitly calls Expert (FSM) an "upper bound" (line 196), and honestly reports all numbers in Table 1. The phrase "narrows the gap" (line 197) accurately describes the comparison against the single-stage expert baseline, where CoRAL achieves higher success rates on T1 and T5. This is not a weakness — it is honest calibration.

- **"Zero-shot" claim (full version, Harsh Critic Issue 2)**: Downgraded to Minor. The paper defines what it means by zero-shot in context (no task-specific teleoperation data). The infrastructure requirements are real but typical for this genre of work.

- **Generic concerns about missing related works, appendix content, formatting, reproducibility of trivial details**: Removed per instructions (appendix is parser-stripped, missing related works cannot be verified, typos are parser artifacts).

## Novel Insights

The most informative tension revealed by combining the two reviews is the following: the VLA comparison is structurally asymmetric (baselines evaluated out-of-distribution), yet the Unified VLM ablation — which uses the *same* GPT-4o model in a monolithic prompt — also fails catastrophically (0/10 on four of six tasks). Together, these results suggest the paper's most defensible contribution is not "CoRAL beats VLA models" but rather "the modular separation of perception (VLM) and planning (LLM) within an MPPI loop is empirically necessary for reliable contact-rich manipulation." The evidence for this narrower claim — supported by the Unified VLM ablation, the T6 contact-strategy analysis, and the w/o Refinement ablation — is actually quite strong and independent of the problematic VLA comparison.

## Suggestions

1. **Reframe the VLA comparison** as a zero-shot generalization assessment of pre-trained VLAs on novel contact-rich tasks, not as a head-to-head comparison. Focus the quantitative evaluation on the comparison against the human-expert-designed cost baselines, which properly control for the MPPI infrastructure and isolate the LLM's contribution.
2. **Add confidence intervals** (e.g., bootstrap) or exact binomial tests for the success rate metrics to substantiate comparisons where differences are small (e.g., 4/10 vs. 2/10).
3. **Clarify the mass adaptation figure**: what precisely is plotted, what the ground truth values are, and whether convergence to within what margin of error is achieved.
4. **Validate the VLM's initial mass and friction estimates** independently (e.g., a correlation study across a range of objects with known physical parameters).
5. **Specify the memory retrieval mechanism**: embedding model, similarity metric, retrieval threshold.
6. **Run at least one real-robot experiment** to ground the sim-to-real robustness claims that the paper explicitly makes.

---

## Calibration Anchors

**Round 1 — Bracketing**: Initial bracket placed the paper between low-band (score < 3.5) and high-band (score > 7.5) submissions on LLM-based robotic manipulation. The most relevant anchor was "Generating Robot Policy Code for High-Precision and Contact-Rich Manipulation Tasks" (avg 4.00, Reject), which used LLMs for contact-rich tasks with real-robot validation but had limited tasks and weak ablations. The high-band anchors (avg 8.00, Accept) were substantially stronger papers with real hardware, large-scale benchmarks, or differentiable physics. Initial bracket: **[4.0, 6.5]**.

**Round 2 — Narrowing**: Pulled anchors inside (3.5, 5.5) and (5.5, 7.0). Key comparisons:
- *"Generating Robot Policy Code..."* (avg 4.00, Reject): CoRAL is clearly stronger — more tasks (6 vs. 2), better ablation structure, clearer architecture. **CoRAL > 4.0**.
- *"Make a Donut"* (avg 5.25, Reject): Hierarchical LLM+MPC for deformable objects. Had real-robot experiments. Comparable in method novelty; CoRAL lacks real-robot. **CoRAL ≈ 5.0**.
- *"LLaRP"* (avg 5.75, Accept): LLM as policy with RL training on 1,000-task benchmark. Stronger evaluation scale. **CoRAL < 5.75**.
- *"SuSIE"* (avg 6.25, Accept): Zero-shot with diffusion models, real-robot, CALVIN benchmark. **CoRAL < 6.25**.
- *"Instruct2Act"* (avg 5.00, Reject): LLM-based framework with real-robot. Comparable in scope but CoRAL's method is more novel (cost function generation vs. code generation). **CoRAL ≈ 5.0–5.5**.

**Final score**: The paper has a genuine architectural contribution and strong ablations, but is held back by an overclaimed VLA comparison, sim-only evaluation, small sample size, and several underspecified components. It is stronger than the 4.00 contact-rich code-gen paper but weaker than the accepted papers at 5.75–6.25 that have real-robot validation or larger-scale evaluation.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>