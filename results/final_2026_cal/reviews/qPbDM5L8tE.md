Now I have a clear calibration picture. Let me construct the final consolidated review.

## Summary

CoRAL proposes a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation. It decouples perception (VLM → physical parameters) from reasoning (LLM → MPPI cost functions and contact strategies), uses an online adaptation loop to refine plans upon failure, and includes a RAG-based memory unit for experience reuse. Experiments on six simulated tasks demonstrate success on contact-rich scenarios where end-to-end VLA baselines (OpenVLA-OFT, π₀.₅) fail entirely.

## Strengths

1. **LLM-generated cost functions and contact strategies enable zero-shot planning on contact-rich tasks without training.** The LLM produces both the MPPI cost structure (Eq. 2) and focused contact regions (Eq. 3). Table 1 shows CoRAL achieves non-zero success on all six tasks (e.g., 4/10 on T1, 7/10 on T6) while OpenVLA-OFT and π₀.₅ score 0/10 on T1, T4, and T6 — directly demonstrating that the LLM's symbolic outputs meaningfully ground the controller for force-reasoning tasks.

2. **The guided-contact-strategy ablation is compelling evidence that the LLM prunes a computationally intractable search space.** On T6 (Flip with Wall), providing only the cost function (no contact strategy) yields 199 steps and 3.69 m path length; adding the LLM's contact strategy reduces this to 32 steps and 1.33 m — an 83.9% reduction in steps and 63.9% shorter path (Sec. 4.1.4). This controlled ablation quantifies the causal contribution of the contact-strategy mechanism.

3. **Modular separation of VLM (perception) from LLM (reasoning) is convincingly shown to be important for this architecture.** The Unified VLM ablation collapses to 0/10 on T1, T3, T5, T6 and at most 2/10 on T2, T4 (Table 1), while the full CoRAL achieves e.g. 10/10 on T2, 9/10 on T4. The gap is dramatic and consistent across all tasks, supporting the design's specific division of labor.

4. **The online adaptation loop demonstrably converts failures into successes through world-model correction.** On T1, removing the outer loop (w/o Refinement) drops success from 4/10 to 0/10 (Table 1). The paper traces this to the LLM diagnosing a misestimated friction coefficient from the push outcome and updating both the world model and plan (Sec. 4.1.3).

5. **CoRAL approaches expert-designed performance without manual tuning.** The Expert (FSM) baseline (hand-crafted phase-specific costs) achieves the best overall results. CoRAL narrows this gap substantially (e.g., T1: 4/10 vs. 8/10; T6: 7/10 vs. 9/10), showing the LLM recovers much of the structure an expert would manually engineer.

6. **The memory unit provides measurable improvements.** On T1, memory raises success from 2/10 to 4/10 and cuts completion time from 212 s to 162 s; on T3, from 9/10 to 10/10 with time reduced from 61 s to 49 s (Table 1).

## Weaknesses

### Major

1. **Mass-adaptation claim is contradicted by the presented evidence.** The paper states (Sec. 4.1.4) that the evaluation world was initialized with mass 2.0 kg vs. ground truth 0.1 kg, and that "after several adaptation cycles, the agent's belief about both mass and friction converged remarkably close to their true values." However, the figure description for Figure 4 shows the "Corrected Mass" settling at approximately 0.85 kg — which is **not** close to 0.1 kg (a factor of 8.5× error remains). The y-axis (0.75–1.00) does not even span the true value. Either the figure axes are from a different experimental condition, the ground truth is misstated, or the claim is unsupported. This discrepancy undermines a central robustness demonstration. Since the adaptation claim is used to argue that CoRAL can overcome large sim-to-real parameter mismatches, this contradiction needs resolution — either a corrected figure, corrected text, or an honest acknowledgment of the limitation.

2. **The LLM-to-controller interface — the critical binding layer — is unspecified, making the method non-reproducible.** The paper describes the LLM generating "the mathematical structure and relative weights of a cost function" (Eq. 2) and contact surface regions (Eq. 3), and states the LLM "is free to introduce any cost terms constructible from the available state, pose, and action variables." But it never specifies the output format (structured JSON? code? natural language?), the parsing mechanism that converts the LLM's text output into executable MPPI cost terms, or how a textual description of a "surface region" becomes the 3D coordinates and tangent vectors of Eq. 3. Without this specification, readers cannot assess the approach's plausibility or reproduce it. The paper presents an architecture that depends on this binding layer but does not document it.

3. **Missing comparison against force-aware baselines.** The related work section discusses ForceVLA, TLA, VLA-Touch, RDP, and FACTR — methods designed specifically for contact-rich manipulation with force/tactile feedback. The paper claims CoRAL "significantly outperforms both state-of-the-art baselines" on contact-rich tasks, but the two chosen baselines (OpenVLA-OFT, π₀.₅) are general-purpose VLA models, not the most relevant competitors for force-aware tasks. The paper argues these force-aware methods create a "data bottleneck" (Sec. 2), but this is a motivation for CoRAL's different approach, not a justification for excluding them from comparison. Without at least one force-aware learned baseline, the headline claim of superiority for contact-rich manipulation is incompletely supported.

4. **Small sample size (n=10 per condition) with no confidence intervals or statistical tests.** Binary success/failure with 10 trials yields very wide credible intervals — e.g., 4/10 (40%) is statistically consistent with a true success rate anywhere from roughly 15% to 70%. Differences like 2/10 vs. 4/10 on T1 or 5/10 vs. 7/10 on T6 could be noise. Reporting bootstrapped confidence intervals or increasing the number of trials would substantially strengthen the quantitative evidence.

### Minor

5. **The Unified VLM ablation establishes that this particular unified instantiation fails, but the claim that separation is "crucial" is somewhat stronger than the evidence supports.** The Unified VLM variant uses a single multimodal model for both perception and planning, and fails on most tasks. This is consistent with the paper's thesis but does not rule out alternative unified designs (e.g., a larger model, different prompting, or a different training approach) that might handle both roles. The claim could be softened to "important for performance in our architecture" rather than "crucial in general."

6. **Memory unit details are vague.** The paper describes using RAG with an LLM embedding the task into a "latent semantic space" (Eq. 1) but does not specify the embedding model, similarity metric, retrieval mechanism, or how retrieved plans are adapted to new geometric configurations.

7. **Reactive control augmentation (Eq. 7) is underspecified.** The feedback term K_f · (x_des − x_measured) is presented without describing how x_des is defined or how K_f is chosen (task-dependent or fixed).

### Trivial

8. **The paper cites an appendix for the natural-language diagnosis example, but this section was removed by the parser.** This is not the authors' fault but means the claim about explainability is unverifiable from the main paper.

## Nice-to-Haves

- Include at least one force-aware baseline (e.g., RDP or FACTR reproduced in simulation) to substantiate the claim of contact-rich superiority.
- Report bootstrapped confidence intervals or increase trial counts (n=10 is very small for binary success metrics).
- Ablate hyperparameter sensitivity: N_retry=15, MPPI temperature λ=0.1, K=200, H=50 are reported but never varied.
- Provide computational latency numbers (time per adaptation cycle, time per MPPI step) to assess real-time feasibility.
- Discuss the sim-to-real gap: FoundationPose requires known 3D object models, and GPT-4o API calls add latency. A discussion of deployment plans would help.
- Analyze failure modes: do failures stem from pose tracking errors, VLM mis-estimation, or MPPI local optima?

## Removed Points

*The following points from the reviews were removed for the reasons stated:*

- **Criticism about the appendix being absent** (Harsh Critic: "The text cites an appendix that is not included"). → Removed per rule: parser strips appendix sections from all papers; this is a format artifact, not an author error.
- **Criticism that OpenVLA-OFT and π₀.₅ are "not the relevant state of the art" and claiming the comparison is "staged to inflate advantage"** → Partially kept: the missing force-aware baselines point is valid, but the framing that the paper "staged" results is removed as editorializing. The paper honestly reports both baselines' successes (10/10 on T2, 9/10 on T3) and failures; there is no data manipulation.
- **Criticism that the paper doesn't discuss whether the expert tuned on the test distribution** → The paper states costs were "tuned in a separate design environment and then evaluated as-is in our randomized test environment," which directly addresses this concern.
- **Complaints about missing hyperparameter search for MPPI** → Moved to Nice-to-Haves as an ablation suggestion, not a core weakness.
- **Claim that the paper does not provide statistical significance** → Kept as Major (#4) with adjusted severity. The small sample size is a real concern.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") → Removed. Only concrete, evidence-backed strengths are retained.

## Novel Insights

The most interesting finding is not simply that an LLM can generate cost functions, but that the *contact strategy* (the set of focused surface regions) contributes far more to performance than the cost function alone — the guided-vs-unguided ablation (83.9% faster, 63.9% shorter path on T6) cleanly isolates this effect. This suggests that in contact-rich domains, *where* to touch matters more than *how* to optimize the trajectory. A second insight is that the decoupled perception/reasoning architecture (separate VLM for physical parameters, separate LLM for strategy) is not just an engineering convenience but appears necessary for this particular pipeline: forcing a single VLM to do both causes catastrophic failure across nearly all tasks. The memory unit's modest but consistent improvement (especially cutting completion time by 24% on T1) hints that the system genuinely learns to bootstrap better MPPI initializations, though the effect size is small enough that noise cannot be ruled out at n=10.

## Suggestions

1. **Fix the mass-adaptation discrepancy.** Either correct Figure 4 (axes, values, or legend) to match the experimental condition described in the text, or correct the text to honestly report the achieved correction (e.g., "corrected from 2.0 kg to 0.85 kg, reducing error by 60%"). If the adaptation only corrects moderate errors, this is still useful but should be presented accurately.

2. **Specify the LLM output format.** Provide the prompt template, the structured output schema (JSON, code, etc.), and the parsing routine that converts the LLM's text into the cost terms and geometric regions used by MPPI. This is essential for reproducibility and for readers to assess whether the approach is plausible.

3. **Add at least one force-aware baseline, even in simulation.** Reproduce RDP or FACTR in the MuJoCo environment, or provide a convincing argument for why they cannot be compared. Without this, the strongest claims about contact-rich performance are incompletely supported.

## Score and Decision

### Calibration Summary

**Round 1 — Bracketing:**
- Weak anchors (<3.5): L0pYHTvAH6 (3.33, multi-robot LLM planning), tkLDNUzL80 (2.67, physically grounded commonsense), zHexNab8uH (2.50, LLM-guided MIP motion planning), Fchtg9ejki (3.00, deformable object manipulation) — CoRAL is clearly stronger than these (better experiments, clearer architecture, concrete ablations).
- Middle anchors (3.5–7.5): Y1VgLHbzCC (5.50, PDDLLM — Accept Poster), 4jcnded6fA (5.33, BiNoMaP — Reject), LmyjuhNgML (4.00, LLM object search — Reject), KfaZaYYCvt (5.00, Semantic World Models — Reject) — CoRAL is comparable to the 5.0–5.5 range in this band.
- Strong anchors (>7.5): kkBOIsrCXh (8.00, navigation foundation model), PGUC3mmMoi (7.00, RoboInter — Accept Poster) — CoRAL is below these due to its methodological gaps and smaller scale.

**Round 1 bracket: 4.0–6.0**

**Round 2 — Narrowing (4.0–6.0):**
- yngvAamNQi (6.00, FSD — Accept Poster, scores: 6,6,6,6): A VLM-based manipulation framework with extensive benchmarks but issues with 2D→3D lifting and inference cost. CoRAL has a more novel architecture but weaker evidence (mass discrepancy, missing interface specification). CoRAL is slightly below FSD.
- Y1VgLHbzCC (5.50, PDDLLM — Accept Poster): LLM domain derivation for TAMP. CoRAL is comparable but with more significant individual weaknesses.
- brqEUN4i2s (4.00, GeoManip — Withdrawn): Geometric constraints for manipulation. CoRAL is clearly above this.

**Final score anchored against: FSD (6.00) and PDDLLM (5.50).** CoRAL is slightly below FSD due to the mass-adaptation contradiction and unspecified LLM-to-controller interface, but comparable to PDDLLM. Score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>