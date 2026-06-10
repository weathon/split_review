Now let me write the final consolidated review.

## Summary

The paper addresses the problem of zero-shot generalization across RL environments with different state spaces, observation spaces, and dynamics. It proposes a "structurized state space" model (Definition 3.1) that decouples state into an invariant task representation and a task-agnostic background, and introduces Non-Parameterized Randomization (NPR), which randomizes task-agnostic components during training rather than relying on parametric environment models (as Domain Randomization does). Theorem 4.1 shows that training in randomized environments provides an optimizable lower bound for a "non-optimizable adaption gap." Experiments evaluate NPR on cross-environment tasks (MuJoCo→BabyAI, 2D gym→3D Torcs, 3rd-person→1st-person view) with reported improvements over baselines.

## Strengths

1. **Formal framework for environmental generalization.** Definition 3.1's decoupled state representation $s_t^e = \psi_t(I) \oplus \xi_t^e$ provides a clean mathematical language for discussing cross-environment generalization, distinguishing shared task semantics ($I$) from environment-specific background ($\xi_t^e$). This is explicitly differentiated from Block-MDP models that assume a shared state space (lines 64–65).

2. **Theorem 4.1 (Approximating Feasibility).** The result showing that training in randomized environments yields a lower bound on the original return, with slack $\alpha$ depending on the KL divergence between the unseen-environment distribution and the randomization distribution (lines 122–130), is a non-trivial theoretical contribution. It provides formal grounding for why randomization helps in this setting.

3. **Ambitious cross-environment evaluation.** The paper tackles genuinely hard generalization problems — MuJoCo→BabyAI, 2D gym→3D Torcs, 3rd-person→1st-person view — where baselines reportedly achieve near-zero performance while NPR achieves non-trivial success. The gap in results (Tables 1–3, as images in the original) is striking and suggests the method captures something the baselines miss.

## Weaknesses

### Major

1. **The "non-parameterized" distinction from Domain Randomization is overstated and unformalized.** The paper repeatedly frames NPR as categorically different from DR because DR "relies on a parameterized dynamics model" (lines 19, 38, 139). However, NPR still requires specifying what to randomize, by how much, according to what distribution, and which components are task-relevant — this is a form of parameterization, just of a different kind. The paper acknowledges needing "expert priors" (line 143) but continues to frame NPR as fundamentally non-parameterized. Remark 4.2 claims that parameterized methods add "another term" to the bound, but this is **asserted without formal proof** — no theorem or explicit expression is given showing that NPR's bound is tighter than DR's under comparable conditions. Absent this, the claimed theoretical advantage over DR is not substantiated.

2. **Critical experimental details are missing, making the core results uninterpretable.** The paper claims zero-shot generalization from MuJoCo→BabyAI (line 159) and 2D gym→3D Torcs (line 160) — environments with radically different dynamics, action spaces, and observation modalities. While the paper states that pixel-based CNN observations are used (line 164) and that "the action space is discrete and executed by the simulator" (line 159), it provides **no description** of how these environments were modified to share a common interface:
   - How was MuJoCo's continuous torque control reconciled with BabyAI's discrete gridworld actions? What specific modifications were made?
   - What are the exact observation dimensionalities, preprocessing steps, and network architectures?
   - What specific randomization distributions and schedules were used for each environment?
   
   Without this information, the reader cannot determine whether the results reflect genuine cross-environment generalization or an artifact of how the environments were adapted. The fact that baselines fail while NPR succeeds could simply mean NPR's randomization happens to exploit a shared substructure created by undisclosed modification choices.

### Minor

3. **Proposition 3.3's "non-optimizable adaption gap" is largely tautological.** The decomposition into an invariant-learning term and a transition-discrepancy term (lines 93–99) is mathematically valid, but labeling the second term as "non-optimizable because it only depends on the distribution of the background of the environments which are unseen" (line 107) essentially restates the definition of the problem: you cannot train on environments you have not seen. This framing is a description of the difficulty, not an analysis that yields actionable insight.

4. **Proposition 3.4 (Implicit Invariant Learning) is definitional.** Showing that, under sparse reward, maximizing return equals maximizing goal-completion probability (lines 101–105) is a restatement of the sparse-reward setup, not a new theoretical result. Including it as a formal proposition inflates the paper's theoretical contributions.

5. **The implementation description is too vague to be reproducible.** Section 4.2 describes "soft randomizing with a continuous and slow episodic change" (line 145), "parallel online learning algorithms" (line 145), and using "actor-critic-like algorithms... and PPO" (line 145). These are high-level concepts without specifics — no randomization schedule, no parallelization details, no hyperparameters. At a top venue, this level of vagueness is insufficient.

6. **Baseline fairness is unclear.** Standard RL algorithms (PPO, Droq) and augmentation methods (DrAC, DR) were tested on the same cross-environment tasks, but the paper does not describe whether these baselines received any hyperparameter tuning for this specific setting. Given that these methods were not designed for cross-environment generalization with different dynamics, their poor performance is expected and does not strongly demonstrate NPR's superiority. A more informative comparison would benchmark NPR against DR on a task where DR is applicable (e.g., sim-to-real with visual variation) to directly test the claimed advantage.

7. **The "challenging" MuJoCo→MiniWorld task is a one-step decision (line 202).** The paper acknowledges this ("one-step decision to find the correct object"), making it a perceptual identification task rather than a test of sequential decision-making generalization. This weakens the claim that the method solves cross-environment generalization for full RL tasks.

### Trivial

None.

## Nice-to-Haves

- Formalize the claimed advantage of NPR over DR as a theorem with explicit expressions, rather than an informal remark (Remark 4.2).
- Report concrete numerical values from tables in the text and provide error bars over more seeds.
- Add an ablation comparing NPR to DR on tasks where both methods are applicable (e.g., visual domain randomization benchmarks) to directly test the claimed advantage.

## Removed Points

These points were flagged by the harsh critic or strength finder but are removed per the filtering rules:

- *"No concrete numerical values in prose (only images)"* — Tables appear as images in the original PDF; this is a parser artifact, not a paper flaw.
- *"Adaption gap not formally defined"* — Proposition 3.3 does formally define the gap via the error decomposition.
- *"Reproducibility: cannot verify cited references"* — All cited works are assumed to exist per hard rules.
- *Strength: Proposition 3.4 connecting return to invariant learning* — This is definitional, not a genuine strength.
- *Generic strengths about "important problem"* — Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely recapitulate what the paper itself states, though the harsh critic correctly identifies the tension between the "non-parameterized" branding and the practical need for expert-specified randomization rules. This tension is present in the paper but not resolved by either review.

## Suggestions

1. **Provide a complete experimental appendix** describing the exact environment modifications, action space reconciliation, observation preprocessing, network architecture, hyperparameters, randomization distributions, and schedules used in each experiment. Without this, the results cannot be interpreted or reproduced.

2. **Formalize the claimed advantage over DR.** Either prove that NPR's bound is strictly tighter than DR's under explicitly stated conditions, or drop the claim of categorical superiority. Remark 4.2 as written is insufficient.

3. **Re-evaluate the "non-parameterized" framing.** Acknowledge that NPR replaces one form of parameterization (physics-engine parameters) with another (human-specified scene-randomization rules), and frame the contribution as randomizing a different, more general class of components rather than being "parameter-free."

4. **Add a controlled comparison** between NPR and DR on a benchmark where DR is applicable (e.g., standard sim-to-real with visual/dynamic randomization) to demonstrate the claimed advantage in a setting where both methods can be fairly compared.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>