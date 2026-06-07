Now I have a clear picture from both rounds. Let me compile the final review.

**Round 1 Bracket:** CoRAL sits between 4.0 (the `WtHKqtHVXo` anchor — LLM policy code for contact-rich tasks) and 8.0 (GenSim anchor — strong, well-validated LLM-for-robotics paper). Narrowed bracket: **5.0–6.5**.

**Round 2 Narrowing:** CoRAL is clearly stronger than `WtHKqtHVXo` (4.00) and comparable to or slightly better than `iTsHStJKcm` (5.25, "Make a Donut"). It is more focused and better-evaluated than `fZZ4ubttru` (5.50, GenBot), which was overly ambitious with insufficient validation. It does not reach the evaluation scale of `u6imHU4Ebu` (5.75, LLaRP). CoRAL has genuine architectural innovations (nested loops, contact strategy biasing, role separation) validated by strong ablations, but the underspecified core mechanism and asymmetric VLA comparison cap its score.

**Final score: 5.5**

## Summary

CoRAL proposes a modular neuro-symbolic framework for zero-shot, contact-rich robotic manipulation. It separates vision (VLM for perception and physical parameter estimation, FoundationPose for 6-DoF tracking) from reasoning (LLM for cost function formulation and contact strategy), integrates both with an MPPI reactive controller, and adds nested feedback loops for online adaptation and a memory unit for experience reuse. The paper evaluates on six tasks in a MUJoCo/ROBOSUITE environment, comparing against VLA baselines, human-designed cost functions, and several ablations.

## Strengths

- **LLM formulates the mathematical structure of MPPI cost functions, not just perceptual guidance**: Unlike prior work (IMPACT, VLMPC) where VLMs provide sub-goals or cost maps, CoRAL's LLM generates the actual terms, weights, and structure of the cost function J₀ (Eq. 2, Section 3.2). The LLM is "free to introduce any cost terms constructible from the available state, pose, and action variables" — grounding commonsense reasoning directly into the optimal control formulation. This is a meaningful conceptual advance over prior neuro-symbolic manipulation frameworks.

- **Unified VLM ablation provides strong validation of the role-separation thesis**: The CoRAL (Unified VLM) variant, which merges perception and planning into a single multimodal prompt, achieves 0/10 on four of six tasks (Table 1, Section 4.1.3). This near-total collapse provides compelling evidence that separating VLM (perception) from LLM (strategy) is essential for the framework to function.

- **LLM contact strategy biasing yields large, quantified efficiency gains**: On the "Flip with Wall" task (T6), the LLM-proposed contact strategy (Eq. 3) achieves an 83.9% reduction in planning steps (32 vs. 199) and a 63.9% shorter end-effector path (1.33 m vs. 3.69 m) compared to uninformed MPPI sampling (Section 4.1.4). This quantifies how symbolic contact strategies transform a computationally intractable exploration problem into a tractable one.

- **Online adaptation loop demonstrated with parameter convergence**: Figure 4 shows that when initialized with intentionally wrong mass/friction values, the outer loop's LLM-driven correction progressively converges estimates toward ground truth. The w/o Refinement ablation confirms this is causal: removing refinement drops T1 from 4/10 to 0/10 and T3 from 10/10 to 3/10 (Table 1).

- **Randomized evaluation protocol with meaningful expert baselines**: Each task runs 10 trials with randomized initial poses, masses, friction, and box dimensions. The Expert (FSM) and Expert (single-stage) baselines provide interpretable performance ceilings, showing that CoRAL narrows the gap to FSM expert on the hardest tasks while requiring no manual tuning.

## Weaknesses

### Fatal

None.

### Major

- **The LLM-to-cost-function interface is underspecified, limiting reproducibility and assessment of the core mechanism**: The paper's central claim is that the LLM "generates the mathematical structure and relative weights of a cost function" (Section 3.2). But the paper provides only one illustrative example (Eq. 2) with a disclaimer that it is merely illustrative. The reader cannot determine: (a) what the actual LLM prompt looks like, (b) what output format the LLM uses (code? JSON? natural language that is then parsed?), (c) how LLM outputs are translated into executable cost terms that plug into the MPPI framework, or (d) what happens when the LLM produces structurally invalid cost terms. This is the paper's core mechanism, and without specification of this interface, the method cannot be fully evaluated or reproduced.

- **The VLA comparison is structurally asymmetric and does not isolate the architectural contribution**: CoRAL receives known 3D object models (M) for FoundationPose, force/torque feedback from the physics engine, a full MUJoCo simulator for MPPI trajectory rollouts, an online adaptation loop with N_retry = 15, and task descriptions as text. The VLA baselines (OpenVLA-OFT, π₀.₅) receive RGB images and produce actions — no force feedback, no simulator, no object models, no retry budget. Moreover, these VLAs are evaluated on the authors' re-implemented ROBOSUITE/MUJoCo environment rather than the original LIBERO environment, introducing a potential distribution shift. The paper's headline claim that CoRAL "significantly outperforms" VLAs on contact-rich tasks rests on a comparison where it is unclear whether the performance gap comes from the architectural design or from the extensive scaffolding only CoRAL receives.

### Minor

- **Small sample size with no statistical testing**: All results are based on 10 trials per condition. Effect sizes attributed to components like the Memory Unit (2/10 → 4/10 on T1, i.e., one additional success per 5 trials) are presented as "boosting the success rate significantly" (line 234) without confidence intervals or statistical tests. The directional trends are plausible, but the strength of the conclusions would benefit from larger sample sizes or appropriate statistical reporting.

- **Absolute performance on the hardest designed task is modest (40% success)**: On T1 (Push and Pick Cutting Board) — the task most directly demonstrating the framework's multi-stage reasoning and contact-rich capabilities — CoRAL achieves only 4/10. This is well below the Expert FSM baseline (8/10). While the paper honestly reports this, the framing in the abstract and introduction ("robust execution," "zero-shot planning") should be better calibrated to the actual reliability on the most challenging scenarios.

- **Explainability claim rests on a single qualitative anecdote**: The paper claims "inherent explainability" (Section 4.1.4) based on one example where the LLM "provided a correct natural language diagnosis." A single curated example does not constitute a demonstrated capability. The claim should either be supported with systematic evaluation or recast as an illustrative qualitative observation.

- **No characterization of natural VLM physical parameter estimation accuracy**: While the robustness experiment (Fig. 4) shows correction from intentionally wrong initializations, the paper never reports how accurate the VLM's mass/friction estimates are compared to ground truth under normal operation. Without this, the reader cannot assess whether the outer loop is correcting rare catastrophic errors or routinely fixing systematic misestimates.

- **Memory ablation protocol is underspecified**: The paper does not clarify which successful trials populate the memory before evaluation, whether there is a train/test split, or how "sufficiently similar" past experiences are determined. The retrieval equation (Eq. 1) is purely notational. This makes the memory contribution difficult to assess independently.

- **No latency/timing data**: The system queries GPT-4o, runs MPPI with K=200 trajectories at H=50 horizons, and may make additional LLM calls for adaptation. The paper acknowledges "computational latency" as a limitation (Section 5) but provides no wall-clock timing data, which matters for a framework positioned for reactive control.

### Trivial

- The claim that CoRAL "eliminates the need for prior demonstration datasets containing [force] data" (line 45) is slightly misleading: the framework still requires known 3D object models and a physics simulator, which are forms of prior knowledge that may not be available in real settings.

## Nice-to-Haves

- A systematic study of when and why the VLM's physical parameter estimates are inaccurate, and how often the outer loop can recover from natural (rather than intentional) misestimates.
- Comparison against a variant where VLAs are given the same retry budget, or where CoRAL's simulator and force-feedback privileges are removed, to better isolate the architectural contribution.
- Larger-scale evaluation (30-50 trials) with confidence intervals, particularly for the ablation study.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that the VLA comparison is "stacked" to the point of complete invalidity** — While the comparison is asymmetric, the paper does not hide this asymmetry; it honestly reports the VLA setup (using official LIBERO checkpoints). A 0/10 result on contact-rich tasks the VLAs were never trained for is genuinely informative about the limitations of end-to-end VLA approaches, even if the comparison doesn't isolate the architectural contribution. The asymmetry is a legitimate concern (retained as Major) but the claim that it makes the comparison entirely invalid is overstatement.

- **Harsh Critic claim about "no analysis of VLM physical parameter accuracy" being a fatal gap** — Retained as Minor. The robustness experiment demonstrates the outer loop's corrective capability even from extreme misestimates (2.0 kg vs 0.1 kg ground truth), which partly mitigates this concern.

- **Harsh Critic claim that the Expert FSM comparison is "within the MPPI paradigm" and doesn't compare paradigms** — This is a feature, not a bug. The Expert baselines serve as upper bounds on what MPPI can achieve with perfect cost functions, which is exactly the right comparison for evaluating whether the LLM is generating reasonable cost functions. Removed.

- **Harsh Critic claim about strawman argument regarding LIBERO fine-tuning** — The paper says the VLAs were "fine-tuned on the LIBERO benchmark, which should theoretically demonstrate some generalization" (line 193). This is a reasonable point: these VLAs were fine-tuned for manipulation and might show some transfer. The phrasing is slightly imprecise but not a straw man. Removed.

- **Harsh Critic claim that the w/o Pose Tracking ablation is "tautological"** — The paper presents this ablation to demonstrate that a dedicated pose estimator is necessary, which is a valid ablation even if the result is unsurprising. It's useful to quantify just how critical this component is. Removed.

- **Strength Finder claim about "Large performance gap over fine-tuned SOTA VLAs" as a standalone strength** — The gap is real but the comparison asymmetry limits how strongly it supports the architectural claim. Merged with the corresponding Major weakness.

- **Strength Finder claim about "Explainability through natural language failure diagnosis" as a strength** — The single anecdote does not constitute a demonstrated strength. Moved to Minor weakness.

- **Harsh Critic claim that LIBERO tasks were re-implemented without discussing distribution shift** — This is a real concern but the paper states these tasks were "incorporated for evaluation" and provides results. VLAs actually perform well on T2 (10/10 for both) suggesting the re-implementation is reasonably faithful for simple tasks. Retained as part of the Major VLA comparison weakness rather than a separate point.

## Novel Insights

The paper's contribution of having an LLM directly formulate the structure of an MPPI cost function — rather than just providing perceptual sub-goals or cost maps — represents a genuinely deeper neuro-symbolic integration than prior work. The contact strategy biasing mechanism (Eq. 3) and its demonstrated 83.9% reduction in planning steps is a concrete, quantifiable insight about how symbolic reasoning can prune the search space for contact-rich manipulation. The nested-loop architecture (inner MPPI loop for reactive control, outer LLM loop for world-model adaptation) is also a well-motivated design pattern that could generalize beyond this specific instantiation.

## Suggestions

- Specify the LLM-MPPI interface concretely: include at least one full, end-to-end prompt and output example, and describe how the LLM's output is parsed into executable cost terms. Discuss failure modes and how invalid outputs are handled.
- Either expand the VLA comparison to give VLAs comparable scaffolding (retry budget, object models where available), or reframe the comparison honestly as "VLAs applied zero-shot to out-of-distribution contact-rich tasks" rather than a head-to-head that CoRAL wins.
- Report wall-clock timing data for the full pipeline (GPT-4o latency, MPPI rollout time, adaptation loop time).
- Either conduct a systematic evaluation of explainability or recast the claim as an illustrative qualitative observation.

## Anchor Comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `wl1Kup6oES` (vision pre-training for manipulation) | 3.00 | R1 | Less relevant; CoRAL is stronger |
| `I0To0G5J7g` (online self-improvement for embodied models) | 3.20 | R1 | Different approach; CoRAL has better validation |
| `oyXoGJQlUf` (GRAIL, LLM action-rule induction) | 3.00 | R1 | Less mature; CoRAL clearly stronger |
| `Q6HYM1EMu8` (LARG2, LLM reward generation) | 3.00 | R1 | Less sophisticated; CoRAL clearly stronger |
| `WtHKqtHVXo` (LLM policy code for contact-rich manipulation) | 4.00 | R1 | Very similar topic; CoRAL has more tasks (6 vs 2), better architecture, more thorough ablations |
| `qGL6fE1lqd` (LLMPhy, LLM+simulator physical reasoning) | 4.40 | R1 | Similar LLM+physics paradigm; CoRAL adds MPPI control and is more complete |
| `KTtEICH4TO` (CORN, contact-based object representation) | 4.75 | R2 | Different focus; CoRAL is more ambitious in scope |
| `iTsHStJKcm` ("Make a Donut", LLM+differential physics for deformables) | 5.25 | R2 | Similar LLM+physics planning paradigm; CoRAL has better error recovery (nested loops) and more thorough ablations |
| `pRIPRDALBV` (LLM-Regress, open-world planning) | 5.50 | R1 | Different problem; comparable quality |
| `fZZ4ubttru` (GenBot, generative simulation for skills) | 5.50 | R2 | More ambitious but weaker validation; CoRAL is more focused and better evaluated |
| `u6imHU4Ebu` (LLaRP, LLMs as generalizable policies) | 5.75 | R2 | Stronger evaluation at scale; CoRAL doesn't match this breadth |
| `OI3RoHoWAN` (GenSim, LLM task generation) | 8.00 | R1 | Clearly stronger — more thorough evaluation, real-world transfer, larger scale |
| `7BLXhmWvwF` (geometry-aware RL for manipulation) | 8.00 | R1 | Less relevant; different approach |
| `KsUh8MMFKQ` (differentiable physics for thin-shell objects) | 8.00 | R1 | Less relevant; different approach |
| `7gUrYE50Rb` (embodied QA) | 8.00 | R1 | Not relevant |

**Round 1 bracket:** 5.0–6.5. **Round 2 narrowed to:** 5.0–5.75. CoRAL's architectural innovations and ablation study place it above the 5.25 anchor but its underspecified core mechanism and asymmetric comparison prevent it from reaching 5.75.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>