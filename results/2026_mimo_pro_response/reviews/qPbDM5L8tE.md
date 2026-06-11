## Summary
CoRAL proposes a modular framework for zero-shot contact-rich robotic manipulation that separates VLM-based perception from LLM-based reasoning, with the LLM generating MPPI controller cost functions and contact strategies. A RAG-based memory unit retrieves past successful experiences, and an online adaptation loop refines world model parameters and plans mid-execution. The framework is evaluated on six tasks in MuJoCo simulation against VLA baselines and expert-designed cost baselines, with ablation studies isolating each architectural component.

## Strengths
- **Well-designed ablation study isolating architectural components**: Table 1 systematically removes pose tracking, memory, refinement, and role separation. The progressive degradation is stark — e.g., T6 (Flip with Wall): 7/10 → 5/10 w/o memory → 2/10 w/o refinement → 0/10 w/o pose tracking or with unified VLM. Each ablation targets a specific design decision, providing strong evidence for the necessity of each module.
- **Novel LLM→MPPI cost function generation**: Unlike prior work where LLMs provide high-level plans translated to actions, CoRAL has the LLM generate the mathematical structure of the MPPI cost function (Eq. 2) and contact strategies (Eq. 3) directly. The contact strategy ablation on T6 demonstrates 83.9% faster execution (32 vs. 199 steps) and 63.9% shorter end-effector paths, providing concrete evidence this grounding is effective.
- **Expert-designed cost baselines provide meaningful upper bound**: Including both single-stage and FSM expert baselines allows assessment of how close LLM-generated costs come to carefully engineered solutions. CoRAL approaches the FSM expert on T5 (9/10 vs. 10/10) and narrows the gap on T6 (7/10 vs. 9/10).
- **Consistent memory module benefits**: The memory unit improves both success rates and completion times across all tasks — e.g., T1: 2/10→4/10 with 212s→162s, T4: timing improvement from 109s→52s, T6: 5/10→7/10 with 164s→106s.
- **Competitive on simple tasks validates generality**: CoRAL matches VLA baselines on standard pick-and-place (T2: 10/10, T3: 10/10), suggesting the architecture is not overly specialized and the added complexity does not degrade simpler scenarios.

## Weaknesses

### Fatal
None

### Major
- **Small sample size with no statistical analysis undermines quantitative claims**: All results are based on 10 trials per task with binary outcomes. With N=10, a success rate of 4/10 (T1) has a 95% binomial CI of roughly [0.12, 0.74], and differences like 2/10→4/10 for the memory ablation are well within noise bounds. The paper calls the memory effect "significant" (Section 4.1.3) but reports no variance, confidence intervals, or significance tests. This makes it difficult to evaluate which ablation effects are genuine — these ablations are the paper's primary evidence for its architectural claims.
- **Simulation-only evaluation limits the contribution's impact for contact-rich manipulation**: The entire evaluation is in MuJoCo/Robosuite, where force/torque data is perfectly available from the physics engine, object geometries are exactly known, and there is no real noise or sim-to-real gap. The reactive control augmentation (Eq. 7) assumes clean force feedback. For a paper whose central contribution targets contact-rich tasks and claims to address scenarios "where accurate a priori physical models are often unavailable" (Section 4.1.4), at least a proof-of-concept real-world demonstration would substantially strengthen the claims.

### Minor
- **Somewhat unfair VLA baseline comparison**: The VLA baselines (OpenVLA-OFT, π₀.₅) were fine-tuned on LIBERO pick-and-place demonstrations and evaluated on custom contact-rich tasks (T1, T4, T5, T6) they were never trained on. The paper explicitly states tasks were "designed to be difficult for purely vision-based, collision-avoidant planners" (line 155). While the zero-shot framing partially justifies this, the more informative comparison is against Expert-designed costs, where CoRAL still underperforms the FSM on the hardest tasks (T1: 4/10 vs. 8/10, T6: 7/10 vs. 9/10). The paper should more clearly characterize this gap.
- **Figure 4 text/figure discrepancy**: Section 4.1.4 describes initializing with "severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg)" but Figure 4's y-axis ranges from 0.75–1.00 kg with corrected mass starting at 1.00. These cannot both be correct and need clarification.
- **Known 3D geometric models required**: FoundationPose requires "known 3D geometric models of the objects, M" (line 65) as input, limiting applicability to scenarios with CAD models or 3D scans. This is not discussed as a limitation.
- **Memory retrieval underspecified**: The RAG mechanism (Eq. 1) is described at a high level — "the LLM embeds the current task into a latent semantic space" — but the paper does not specify the embedding method, similarity threshold for retrieval vs. new generation, or how cost functions and strategies are serialized. This affects reproducibility.

### Trivial
- The limitations section defers most discussion to an appendix, making it difficult to assess the authors' awareness of key limitations without supplementary material.

## Nice-to-Haves
- Systematic evaluation of VLM physical parameter estimation accuracy across all objects and randomized conditions (not just a single mass correction example).
- Concrete timing data: how long does a single LLM API call take, and how does total task time break down?
- Discussion of safety constraints or validation of LLM-generated cost functions for real-robot deployment.
- Clearer labeling of which tasks (T2, T3) are from LIBERO vs. custom-designed.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **"Dependency on proprietary LLM API"** — Valid implementation choice, not a methodological flaw. The harsh critic's concern about API costs/latency is practical, not scientific.
- **"Missing related works"** — Cannot verify existence of claimed missing works; removed per rules.
- **"Reproducibility concerns about model existence"** — All cited models/tools treated as existing per rules.

## Novel Insights
The most novel architectural insight is the direct grounding of LLM reasoning into the MPPI cost function structure — rather than having the LLM produce high-level plans that another module must translate, the LLM generates the mathematical cost terms and contact strategy biases that directly shape the control optimization. The contact strategy ablation (83.9% faster execution, 63.9% shorter paths on T6) provides strong evidence this grounding is meaningful, not just symbolic. The hierarchical ablation also reveals an important architectural lesson: role separation (VLM for perception, LLM for reasoning) is not optional — collapsing them into a single model causes near-total failure on complex tasks.

## Suggestions
- Run at least 50 trials per condition and report confidence intervals to make ablation results statistically credible.
- Include a baseline using the same MPPI controller with simpler/heuristic cost functions (e.g., scripted costs or a smaller model) to isolate the LLM's specific contribution from the MPPI architecture.
- Add at least a proof-of-concept real-world experiment, even on one task, to demonstrate sim-to-real viability.
- Clarify Figure 4 vs. the text description of the mass correction experiment.

## Calibration Report

**Round 1 bracket: 5.0–6.0**

**All anchors retrieved across rounds:**

| Anchor Paper | Avg Score | Round | Comparison to CoRAL |
|---|---|---|---|
| Generating Robot Policy Code for Contact-Rich Tasks (WtHKqtHVXo) | 4.0 | R1 | Very similar topic; rejected for ad-hoc approach, weak baselines. CoRAL is clearly stronger with systematic ablations. |
| LARG2 (Q6HYM1EMu8) | 3.0 | R1 | LLM reward generation; rejected for poor writing, no baselines, no ablation. CoRAL clearly stronger. |
| Online Self-Improvement for Foundation Models (I0To0G5J7g) | 3.2 | R1 | Foundation models for robotics; rejected despite one 10-score. Mixed reviews. |
| Zero-Shot Manipulation with Diffusion Models (c0chJTSbci) | 6.25 | R1 | Accepted. Real-world + simulation demos. Stronger generalization evidence. Above CoRAL. |
| Video Language Planning (9pKtcJcMP3) | 7.0 | R1 | Accepted. 3 real hardware platforms, video generation planning. Clearly above CoRAL. |
| Residual-MPPI (gVnJFY8nCM) | 6.25 | R1 | Accepted. MPPI-based, real game env + MuJoCo. Reviewers wanted better baselines. Comparable. |
| HAMSTER (h7aQxzKbq6) | 6.0 | R1 | Accepted. Hierarchical VLA, real-world demos. Simpler tasks but real-world present. |
| CORN: Contact-based Object Representation (KTtEICH4TO) | 4.75 | R1 | Borderline accepted (1,5,5,8). Contact-rich manipulation. |
| Automated Rewards via LLM Progress (lvDHfy169r) | 5.75 | R2 | Rejected. LLM reward generation, SOTA on Bi-DexHands but rejected. |
| Eureka: Human-Level Reward Design (IEduRUO55F) | 6.25 | R2 | Accepted. Closest conceptual match — LLM generating reward functions. 29 envs, real-world pen spinning. Stronger than CoRAL. |
| Video2Policy (RhfYIJux9d) | 5.5 | R2 | Rejected. LLM reward + simulation. |
| GenBot (fZZ4ubttru) | 5.5 | R2 | Rejected. Generative simulation for robot learning. |
| RePLan (gisAooH2TG) | 4.25 | R2 | Rejected. VLM replanning. Less systematic than CoRAL. |
| Instruct2Act (JWrl5pJCnl) | 5.0 | R2 | Rejected. LLM mapping instructions to robot actions. |
| ManiBox (VEdeDd13gx) | 5.25 | R2 | Rejected. Simulation-only grasping. |
| MeMo: Modular Controllers (VZTFUtldbC) | 4.75 | R2 | Rejected. Modular robot controllers. |

**Narrowing to final score:** CoRAL's novel LLM→MPPI cost function generation and thorough ablation study place it clearly above rejected LLM-for-robotics papers (scores 3.0–5.5). However, simulation-only evaluation with only 10 trials and no statistical analysis place it below accepted papers in this space (Eureka 6.25, Residual-MPPI 6.25, HAMSTER 6.0) which typically include real-world validation and/or larger-scale experiments. The paper sits at the boundary: 5.0 represents a borderline paper with genuine architectural contributions that needs more rigorous empirical validation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>