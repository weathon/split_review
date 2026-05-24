Now I have sufficient calibration data. Let me compose the final review.

## Understanding round-1 bracket and narrowing

**Round 1 bracket:** Initial bracketing across weak (score <3.5), middle (3.5-7.5), and strong (>7.5) anchors placed the paper between ~4 and ~6.5, closer to the Instruct2Act (5.0) and HAMSTER (6.0) anchors than to the strong 8.0 anchors.

**Round 2 narrowing:** Additional searches in (4.5,6.0) and (5.5,7.0) confirmed the paper sits near the 5.0-5.5 range, with Make a Donut (5.25) and CORN (4.75) as useful comparables.

Here is my final consolidated review:

## Summary
CoRAL proposes a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation. It separates perception (FoundationPose + VLM for physical parameter estimation) from reasoning (LLM for cost function generation, contact strategy formulation, and online adaptation), and uses an MPPI controller for reactive execution with a memory unit for experience reuse. The core idea — using an LLM to generate structured cost functions and contact strategies within an MPPI loop, with closed-loop adaptation — is timely and well-motivated.

## Strengths
1. **Zero-shot performance on contact-rich tasks where VLA baselines fail**: Table 1 shows CoRAL achieves 9/10 on "Push with Constant Force" (T4) and 7/10 on "Flip with Wall" (T6), while both OpenVLA-OFT and π₀.₅ achieve 0/10 on those tasks. This demonstrates genuine generalization to contact dynamics that end-to-end policies cannot handle without task-specific training.

2. **Modular separation of VLM/LLM roles is causally validated**: The "Unified VLM" ablation, where a single model handles both perception and planning, fails catastrophically (0/10 on 4 of 6 tasks, 1/10 on T4). This provides direct causal evidence that the modular design choice is necessary, not merely beneficial — a stronger ablation than many papers in this space provide.

3. **LLM-driven online adaptation and memory both show measurable benefits**: The w/o Refinement ablation drops from 4/10 to 0/10 on multi-stage T1 and from 5/10 to 2/10 on T6. Memory adds further gains (2/10→4/10 on T1, 9/10→10/10 on T3, and reduces average completion time on T4 from 109s to 52s). These ablations, despite small sample sizes, consistently point in the same direction.

4. **LLM-generated contact strategy dramatically prunes the search space**: On the Flip with Wall task, the guided strategy required 32 vs. 199 planning steps (83.9% faster) and 1.33 m vs. 3.69 m end-effector travel (63.9% shorter path). This quantifies a key advantage over prior VLM+planner approaches like IMPACT.

## Weaknesses

### Major
1. **Figure 4 contains a clear factual inconsistency in the central adaptation experiment**: The text (Section 4.1.4) states the Evaluation World was initialized with a severely overestimated mass of 2.0 kg (ground truth 0.1 kg) and friction 0.9 (ground truth 0.5). However, Figure 4's y-axis ranges from 0.75–1.0 kg, the "Initial Mass" trace is constant at 1.0 kg, and the "Corrected Mass" converges to ~0.85 kg — neither the initial value (1.0 kg) nor the converged value (0.85 kg) matches the text claims (2.0 kg initial, 0.1 kg ground truth). The friction correction is mentioned but never shown. Since this is the paper's primary demonstration of online physical parameter adaptation, this inconsistency is a serious credibility problem that must be resolved.

2. **Statistical power is insufficient for the categorical claims**: All experiments use only 10 trials per condition. Several critical ablation conclusions (e.g., memory "significantly boosted" performance: 2/10 → 4/10 on T1, refinement on T1: 0/10 vs. 4/10) rest on differences of 1–2 successes. With 10 trials, the 95% CI for 2/10 is 0.03–0.56 and for 4/10 is 0.12–0.74 — these intervals heavily overlap. No confidence intervals, error bars, or statistical tests are reported. The paper's categorical conclusions about component necessity are not supported at this sample size.

3. **LLM cost function generation is critically under-specified**: The paper claims the LLM can "introduce any cost terms constructible from the available state, pose, and action variables" and generates a mathematical cost functional from scratch. However, every experiment likely uses the fixed structure of Equation 2 (distance + contact indicator + control cost) with LLM-assigned weights. There is (a) no evidence the LLM ever introduces genuinely novel cost terms, (b) no description of how arbitrary symbolic expressions are safely parsed and instantiated in MPPI, (c) no prompt template provided, and (d) no mechanism described for how force-related costs (critical for contact-rich tasks like "Push with Constant Force") are encoded. This gap prevents reproducibility.

### Minor
4. **Contact strategy ablation result lacks variance information**: The claim that the guided contact strategy is "83.9% faster" (32 vs. 199 steps) and travels a "63.9% shorter path" (1.33 m vs. 3.69 m) appears drawn from a single trajectory pair (referenced to an appendix figure). No error bars or multiple-run statistics are reported. This is insufficient evidence for a quantitative claim of this magnitude.

5. **Memory module and outer loop behavior lack critical details**: The RAG retrieval mechanism is described in one generic sentence. What embedding model? What similarity metric or threshold? How is the episode log E_t structured? How many times is the outer LLM invoked per trial? What fraction of refinements actually improve success? These are central components for both understanding and reproduction.

6. **Reactive augmentation equation (Eq. 7) underspecified**: The feedback term K_f · (x_des − x_measured) leaves x_des and x_measured undefined — are they joint positions, end-effector poses, or forces? Since the paper states the error comes from "force/torque, proprioception," the quantity being compared is dimensionally ambiguous.

### Trivial
7. **Figure 1 caption describes the image with vague or incomplete formatting** (e.g., "(WORK)" appears as a placeholder in the caption).

## Nice-to-Haves
- A real-robot experiment, even on a single task, would substantially strengthen the claim that the framework handles "sim-to-real" gaps conversationally.
- Reporting actual MPPI control frequency (Hz) achieved during execution, rather than just hardware specs.
- A gradual degradation analysis of pose-tracking accuracy (rather than the binary "w/o Pose Tracking" ablation) would illuminate the system's actual dependency on FoundationPose.

## Removed Points
- **"Comparison against OpenVLA/π₀.₅ is a strawman"** — Removed. Testing baselines on out-of-distribution tasks is a standard and valid protocol for demonstrating zero-shot generalization. The paper shows CoRAL handles contact-rich tasks that the VLA baselines cannot, which is a meaningful finding.
- **"VLM mass/friction estimation limitations should be acknowledged more"** — Removed. The paper does acknowledge these limitations implicitly through the entire online adaptation design, which is built precisely to correct initial VLM errors.
- **"The paper lacks related work on X"** — Removed per instructions (I cannot verify the existence of missing citations).
- **Various formatting/style nitpicks** — Removed per instructions.
- **Strength 6 about explainability** — Dropped because the claimed explainability example is deferred to a missing appendix section and no quantitative evidence is provided.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Fix Figure 4**: Align the figure axes and traces with the text claims. Show both mass and friction corrections. Report data from multiple trials, not a single trajectory.
2. **Increase trial counts**: A minimum of 30–50 trials per condition with reported confidence intervals would transform the ablation comparisons from suggestive to convincing.
3. **Release the prompt templates and cost function parsing details**: Without knowing how the LLM output is translated into executable MPPI costs, the claimed generality cannot be assessed.
4. **Report outer-loop statistics**: How many times does the LLM get invoked per task? What fraction of refinements succeed? This would give readers a concrete picture of the adaptation dynamics.
5. **Provide concrete examples of LLM-generated cost functions** beyond Eq. 2 to substantiate the claim that the LLM introduces genuinely novel cost terms.

## Score and Decision

**Calibration Anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Instruct2Act (JWrl5pJCnl) | 5.00 | R1 | Similar framework using LLM for robotic manipulation. CoRAL tackles harder tasks (contact-rich vs. pick-and-place) but has the Figure 4 inconsistency that Instruct2Act does not. Comparable overall quality. |
| GRAIL (oyXoGJQlUf) | 3.00 | R1 | Weak paper — CoRAL is clearly stronger in experimental scope and evidence. |
| HAMSTER (h7aQxzKbq6) | 6.00 | R1/R2 | Hierarchical VLA with real-world experiments. CoRAL lacks real-world validation that HAMSTER provides. HAMSTER's evaluation is cleaner; CoRAL's contribution is more novel architecturally. CoRAL is slightly below. |
| VLFM/RoboFlamingo (lFYj0oibGR) | 6.50 | R1/R2 | Strong, clean benchmark results on CALVIN. CoRAL's tasks are more diverse and challenging, but the evidence quality is not as clean. |
| LLaRA (iVxxgZlXh6) | 5.25 | R1 | VLM-based policy with auxiliary tasks. CoRAL has a more novel architecture but LLaRA has cleaner execution. Comparable tier. |
| Make a Donut (iTsHStJKcm) | 5.25 | R2 | LLM for subgoal generation, zero-shot, has real-world experiments. CoRAL is in a similar tier but lacks real-world validation. |
| CORN (KTtEICH4TO) | 4.75 | R2 | Contact-based representation for nonprehensile manipulation. CoRAL has a broader framework and stronger comparative results. Slightly above. |
| GenBot (fZZ4ubttru) | 5.50 | R2 | Generative simulation for skill learning. Different approach, similar ambition level. |

**Round-1 bracket:** 4.0–6.5 (between weak anchors at 3.0 and strong anchors at 8.0).  
**Round-2 narrowing:** Papers in the 5.0–5.5 range provide the closest comparables. CoRAL has a more novel architectural contribution than Instruct2Act (5.0) but suffers from a clear data inconsistency (Figure 4) that papers like Make a Donut (5.25) do not. Its lack of real-world validation weighs against it relative to HAMSTER (6.0). The strongest evidence (Unified VLM ablation, zero-shot results on contact-rich tasks) is genuinely compelling, but the Figure 4 issue and small trial counts undermine the overall persuasiveness.

**Final calibration:** CoRAL is above CORN (4.75) due to stronger ablation evidence and clearer contribution. It is comparable to Instruct2Act (5.0) — both have interesting frameworks but imperfect evaluations. The Figure 4 inconsistency is the single largest factor preventing a higher score.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>