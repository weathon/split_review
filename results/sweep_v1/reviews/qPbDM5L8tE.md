Now I have all the evidence needed. Let me produce the consolidated review.

## Summary

CoRAL proposes a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation that decouples perception (FoundationPose + VLM for physical parameters), reasoning (LLM for cost function generation and contact strategies), and low-level control (MPPI). It also includes a memory unit for experience reuse and an online adaptation loop for parameter refinement. The paper evaluates on six simulated manipulation tasks against VLA baselines and human-designed cost baselines.

## Strengths

1. **Clear empirical demonstration that separating VLM (perception) from LLM (reasoning) is critical**: The CoRAL (Unified VLM) ablation, which tasks a single VLM with both perception and strategy, collapses to 0/10 on four of six tasks and only 2/10 on the simplest, while the full separated model succeeds on all tasks (Table 1, Section 4.1.3). This provides concrete support for the paper's central design claim.

2. **Informative comparison against human-designed cost baselines**: The paper includes both a single-stage human-designed MPPI cost and a phase-aware FSM baseline. This is more informative than comparing only against end-to-end VLAs — it shows that CoRAL (4/10) outperforms a fixed single-stage human cost (0/10) on the hardest task (T1), while the FSM expert provides a reasonable upper bound (8/10). The single-stage expert comparison in particular controls for the MPPI controller, isolating the benefit of the LLM's adaptive cost function.

3. **Ablation study convincingly demonstrates the necessity of each component**: The w/o Refinement (0/10 on T1), w/o Memory (2/10 → 4/10 with memory), and w/o Pose Tracking (0/10 on all contact-rich tasks) ablations collectively show that every piece of the architecture contributes to performance. This is well-structured evidence.

4. **LLM-generated contact strategy prunes the search space effectively**: On T6 (Flip with Wall), the guided contact strategy reduces planning steps from 199 to 32 (83.9% faster) and end-effector travel from 3.69m to 1.33m (63.9% shorter), showing that the LLM's symbolic contact reasoning makes long-horizon contact problems computationally tractable (Section 4.1.4).

## Weaknesses

### Major

1. **Mass correction result is significantly overclaimed**: The paper states that the LLM's online adaptation corrected the mass estimate to be "remarkably close to their true values" (Section 4.1.4). In reality, Figure 4 shows the estimate corrected from 1.0 kg to ~0.85 kg, while the ground truth is 0.1 kg — an error of 8.5×, not "remarkably close." The text says the evaluation world initialized with 2.0 kg, but the figure shows the estimated mass starting at 1.0 kg and converging to 0.85 kg. Even taking the text at face value, the correction from 2.0 kg → 0.85 kg still leaves an 8.5× discrepancy from the 0.1 kg truth. The claim that the friction parameter also "converged" is unverifiable from the paper: no friction correction plot is provided. This overstatement undermines the robustness analysis, which is a core claimed capability.

2. **"Zero-shot" framing is in tension with the memory unit**: The title, abstract, introduction, and methodology repeatedly describe CoRAL as a "zero-shot" system. However, the memory unit (Section 3.2, Figure 2) retrieves and reuses prior successful episodes' cost functions and contact strategies, and the ablations show that memory provides a substantial boost (e.g., T1: 2/10 → 4/10, T3: 9/10 → 10/10, T6: 5/10 → 7/10). Retrieving and applying stored task-specific plans from previous executions is *few-shot* reuse, not zero-shot. Since the memory unit is a core architectural component (not an optional add-on), the "zero-shot" characterization is misleading.

3. **Limited statistical evidence**: All experiments use only 10 trials per task × method. No confidence intervals, standard errors, or significance tests are reported. Given the small sample size, the difference between 2/10 and 4/10 on T1, for instance, is not statistically meaningful; a single lucky/unlucky trial flips the result. This is compounded by the randomized object parameters (mass, friction, dimensions), which introduce additional variance that 10 trials cannot adequately capture.

4. **Evaluation is entirely in simulation despite sim-to-real framing**: The paper repeatedly motivates the work by appealing to real-world contact-rich manipulation and claims robustness to sim-to-real gaps (Section 3.3, Eq. 7: "robustness against the inherent sim-to-real gap"). However, all experiments are conducted in MuJoCo simulation. The reactive augmentation (Eq. 7) uses force feedback from the *same* simulator used for planning rollouts, so there is no distribution shift to test robustness against. Without real-robot validation, the sim-to-real claims are unsupported.

### Minor

5. **LLM cost function generation is underspecified for reproducibility**: The paper provides one illustrative cost function (Eq. 2) and states the LLM is "free to introduce any cost terms constructible from the available state, pose, and action variables" (Section 3.2). But it does not describe how the LLM's natural-language output is parsed into executable code, how invalid outputs are handled, how weights are verified, or how the contact strategy parameters (region centers \(c_j\), radii \(e_j\), Eq. 3) are extracted from text. This is a meaningful gap for a method whose central claim is using an LLM to generate structured cost functions and strategies.

6. **Memory retrieval mechanism lacks detail**: The RAG retrieval equation (Eq. 1: \((J_{\text{memb}}, C_{\text{memb}}) = \text{RAG}_{\text{Retrieve}}(T, \theta)\)) does not specify how the similarity metric works. "The LLM embeds the current task into a latent semantic space" (Section 3.2) is vague — which LLM produces the embeddings? How is the stored episode indexed? What defines "sufficiently similar"? Without these details, the memory mechanism is not reproducible.

7. **Friction correction is claimed but not visualized**: The robustness analysis (Section 4.1.4) states that both mass and friction "converged remarkably close to their true values," but Figure 4 only shows mass. The friction correction trajectory is absent, making the claim unverifiable from the presented evidence.

### Trivial

8. **Terminology inconsistency**: The paper uses "zero-shot" in the title/abstract while describing memory-based retrieval, and "sim-to-real" robustness while evaluating only in simulation. These framing issues should be resolved.

## Nice-to-Haves

- Running more trials (50–100) with confidence intervals would substantially strengthen the statistical basis of the results.
- Reporting the friction correction over time (analogous to Figure 4 for mass) would complete the robustness analysis.
- An explicit description of how LLM outputs are parsed into executable MPPI cost structures (e.g., showing a raw LLM output example) would resolve the reproducibility concern.
- A comparison against at least one decoupled neuro-symbolic baseline (e.g., ThinkAct, Inner Monologue) would better position the work within the related literature it cites.

## Removed Points

These points were flagged by the reviewers but are removed or demoted for the following reasons:

- **"CoRAL underperforms a simple human-engineered FSM baseline"**: The paper openly acknowledges this and positions the FSM as an upper bound ("the Expert (FSM) variant achieves the strongest overall performance"). The meaningful comparison is against the single-stage expert (MPPI with a fixed human cost), which CoRAL outperforms on contact-heavy tasks (0/10 → 4/10 on T1). This is not a weakness; it is an honest and informative baseline.

- **"Baselines are cherry-picked"**: The paper includes VLA baselines (OpenVLA-OFT, π0.5) to show that end-to-end approaches fail on out-of-distribution contact-rich tasks, which supports the paper's motivation. It also includes the human-designed cost baselines (single-stage and FSM) that *do* work on these tasks. The set of baselines is informative and not unfairly stacked.

- **"State-transition model f is not specified"**: Section 3.3 describes the MPPI formulation, and the implementation details (Section 4) state rollouts are performed in the MuJoCo-based planning world. This level of specification is standard for simulation-based MPPI papers.

- **"The memory unit stores past experiences which are a form of dataset"**: This is a semantic stretch. The memory stores successful episodes collected *during online execution*, not a pre-collected teleoperation dataset. The "without extensive tele-operated action datasets" claim in the abstract is about pre-collected training data, which is distinct from online experience.

- **"Single-stage expert is not a fair comparison because it uses a single cost while CoRAL can adapt"**: This comparison *directly* tests the benefit of the LLM's adaptive cost generation over a fixed human-designed cost. The single-stage expert baseline *is* MPPI with a fixed human cost, and CoRAL outperforms it. The critic's proposed "MPPI with fixed phase-aware costs" is precisely what the FSM baseline already provides.

## Novel Insights

None beyond the paper's own contributions. The main insight — that separating VLM perception from LLM reasoning and using the LLM to generate cost functions for MPPI can enable zero-shot contact-rich manipulation — is clearly presented by the paper. The reviews do not surface a genuinely novel perspective beyond what the paper already articulates.

## Suggestions

1. **Correct the overclaim about mass correction**: The text "converged remarkably close to their true values" should be replaced with an honest assessment. 0.85 kg vs 0.1 kg ground truth is not close, and the fact that the w/o Refinement ablation fails entirely (0/10) already makes the point that online adaptation is useful without inflating the convergence claim.

2. **Resolve the zero-shot / memory tension**: Either reframe the contribution as "few-shot" or "zero-shot with optional experience bootstrapping," or clearly delineate that the base system without memory is zero-shot while the memory-augmented variant is few-shot. The current framing is inconsistent.

3. **Add confidence intervals or more trials**: Given the randomized parameters and small sample size, reporting at least bootstrapped confidence intervals would help readers assess the reliability of the results.

4. **Show the friction correction trajectory**: Include a plot analogous to Figure 4 for the friction coefficient to support the convergence claim, or remove the friction claim if it cannot be plotted.

5. **Provide an example of raw LLM output**: Showing the actual output from GPT-4o for one task, including how it is parsed into the MPPI cost function and contact strategy, would resolve the underspecification issue.

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration set):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| KsUh8MMFKQ (Thin-Shell Object Manipulations) | 8.00 | Substantially stronger — real-robot results, differentiable simulation, rigorous evaluation across diverse tasks. CoRAL falls short of this standard. |
| QOfswj7hij (Online Neuro-Symbolic Predicate Invention) | 7.33 | Stronger — comprehensive evaluation across 5 domains, clean methodology, clear claims. CoRAL has more overclaiming issues. |
| c0chJTSbci (SuSIE: Zero-Shot Robotic Manipulation) | 6.25 | Somewhat stronger — includes real-world validation and CALVIN benchmark results. CoRAL is comparable in novelty but weaker in evidence. |
| iTsHStJKcm (Make a Donut) | 5.25 | Comparable — similar LLM+MPC approach for manipulation, similar level of underspecification. CoRAL has better ablations but less evidence overall. |
| KTtEICH4TO (CORN) | 4.75 | Comparable — contact-rich manipulation with 300+ simulated and 20+ real objects. CoRAL has more architectural novelty but thinner evaluation. |
| WtHKqtHVXo (Generating Robot Policy Code) | 4.00 | Comparable — LLM for contact-rich tasks with real-robot validation but weak baselines. CoRAL has more thorough ablations but similar overclaiming issues. |
| wl1Kup6oES (From Appearance to Motion) | 3.00 | Weaker — limited experiments, insufficient evidence for claims. CoRAL has a clearer contribution and more thorough evaluation. |

The paper proposes a genuinely interesting modular architecture for contact-rich manipulation, with clean ablations that support its design choices. However, the evidence is undermined by statistically underpowered experiments (10 trials), overclaimed results (mass correction is not "remarkably close"), a zero-shot framing that contradicts the core memory component, and simulation-only evaluation despite sim-to-real claims. These issues are significant but not fatal — the architecture and ablations have clear value. Relative to the calibration anchors, the paper sits between the "Make a Donut" (5.25) and "Generating Robot Policy Code" (4.00) papers: it has a more interesting architecture and better ablations than the latter, but suffers from more overclaiming than the former.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>