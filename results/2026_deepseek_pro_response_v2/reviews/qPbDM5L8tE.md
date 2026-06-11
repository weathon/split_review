Now I have strong comparative anchors. Let me summarize my calibration:

- **Make a Donut (5.25)**: LLM generates subgoals, differentiable-physics MPC executes. CoRAL is stronger — it has nested feedback loops with online adaptation (vs. open-loop LLM plans), contact strategy guidance, stronger ablations (Unified VLM collapse), and better baselines.

- **Plan-Seq-Learn (6.67)**: LLM decomposes tasks, motion planner sequences, RL learns low-level control. CoRAL is comparable but slightly weaker — PSL has more extensive evaluation (25+ tasks, 4 benchmarks, 85%+ success), while CoRAL's central cost-function claim is undersupported. CoRAL's architecture is more innovative (LLM authors cost functions) but this is precisely what's least well-demonstrated.

- **GenSim (8.0)**: Thorough evaluation in sim and real, well-supported claims. CoRAL is clearly weaker.

CoRAL sits between Make a Donut and Plan-Seq-Learn. The major cost-function weakness pulls it below PSL. Final score: **6.0**.

Now let me write the final review.

## Summary
CoRAL is a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation. It decouples perception (VLM estimates physical parameters, FoundationPose tracks 6-DoF poses) from reasoning (LLM generates MPPI cost functions and contact strategies), and wraps these inside nested feedback loops: a fast inner MPPI control loop with reactive augmentation, and a slow outer loop where the LLM diagnoses failures and refines its world model. A memory unit stores successful episodes for retrieval. Experiments on six simulated tasks (including two LIBERO benchmarks) compare CoRAL against OpenVLA-OFT, π₀.₅, human-designed cost baselines, and four ablations.

## Strengths

- **Decisive evidence for separated VLM/LLM roles**: The Unified VLM ablation (collapsing perception and planning into a single multimodal prompt) fails catastrophically — 0/10 on T1, T3, T5, T6 and 1/10 on T4 — while the full separated architecture achieves 4/10, 10/10, 9/10, 9/10, and 7/10 on those same tasks (Table 1). This stark, consistent gap directly validates the paper's central architectural hypothesis.

- **Isolated demonstration that LLM contact strategies prune the search space**: On T6 (Flip with Wall), the contact strategy ablation compares LLM-guided sampling against uninformed random sampling using the same MPPI controller and cost function. The guided strategy achieves an 83.9% reduction in planning steps (32 vs. 199) and a 63.9% shorter end-effector path (1.33 m vs. 3.69 m). This cleanly isolates the contact strategy's contribution.

- **Online physical parameter correction demonstrated**: Section 4.1.4 and Figure 4 show the LLM-driven outer loop correcting a deliberately biased internal world model through iterative refinement, converging toward true mass and friction values. This demonstrates a capability — explicit, interpretable self-correction — that end-to-end VLA policies cannot provide.

- **Refinement loop is decisive on long-horizon tasks**: On the multi-stage T1 (Push and Pick Cutting Board), removing the online refinement loop drops success from 4/10 to 0/10 (Table 1), showing the outer loop is sometimes the difference between any success and none.

- **Well-structured task suite**: The six tasks cover distinct capability axes — multi-stage reasoning (T1), baseline pick-and-place (T2, T3), force control (T4), and environment-as-tool (T5, T6) — with randomized masses, friction, and dimensions across 10 trials each.

## Weaknesses

### Fatal
None.

### Major

- **The cost function contribution is asserted rather than isolated or demonstrated**: The paper's headline claim is that the LLM "formulates the structure of the MPPI controller cost function itself" (Section 2). Yet Eq. 2 is explicitly flagged as "only an illustrative example" — no concrete LLM-generated cost function is shown for any task. The contact strategy ablation on T6 isolates C₀, showing the LLM's contact guidance matters. But there is no parallel ablation that isolates J₀ (e.g., using the LLM's cost function with uninformed contact sampling, or comparing against a simple hand-crafted cost). Without this, we cannot distinguish whether the LLM's cost function design is genuinely contributing sophisticated reasoning or whether the MPPI controller plus contact strategy is doing most of the work. The paper needs to either show and analyze the actual cost functions produced, or run an ablation that disentangles J₀ from C₀.

### Minor

- **Small sample sizes without statistical characterization**: All evaluations use n=10 trials per task with no confidence intervals or statistical tests reported. Several key comparisons involve small absolute differences — the memory module boosting T1 from 2/10 to 4/10, or CoRAL at 7/10 vs. Expert FSM at 9/10 on T6 — where the 2-trial gap could plausibly be noise. Reporting Clopper-Pearson confidence intervals would let readers assess which comparisons are reliable.

- **Online adaptation mechanism underexplained**: Section 3.4 describes the LLM receiving logged episode data and refining parameters or cost weights, but the prompt structure, the specific information in E_t, and the LLM's diagnostic reasoning process are not described in enough detail for a reader to understand how the adaptation works in practice. The parameter correction experiment (Figure 4) uses a deliberately extreme initialization (2.0 kg vs. 0.1 kg ground truth), leaving open how the system performs under more realistic levels of initial error.

- **Contact strategy biasing implementation unspecified**: Eq. 3 defines candidate contact points, and Section 3.2 (line 99) states these "bias the initial control perturbations to explore actions that bring the end-effector closer to the LLM-proposed contact regions." But the actual mechanism — whether through modified sampling distributions, auxiliary cost terms, or some other approach — is never specified. This makes Section 3.2 not fully reproducible.

- **Computational latency not broken down**: CoRAL is substantially slower than VLAs on shared tasks (45–106s vs. 5–13s for T2–T3 in Table 1). While the limitations section acknowledges "computational latency," it does not decompose where time is spent (VLM inference, LLM inference, MPPI rollouts, control loop), which would help readers understand the bottleneck.

### Trivial

- **Figure 4 description inconsistent with text**: The text in Section 4.1.4 describes a parameter correction scenario with initial mass estimate of 2.0 kg converging toward ground truth of 0.1 kg, while Figure 4's caption describes a correction from 1.00 kg to ~0.85 kg. These appear to be different experiments; clarifying which experiment Figure 4 corresponds to would avoid confusion.

- **K_f feedback gain matrix untuned**: Eq. 7 introduces a feedback gain matrix K_f for reactive control augmentation, but how K_f is designed or tuned is never discussed.

## Nice-to-Haves

- The paper could benefit from discussing whether the framework could be deployed on a real robot; all current experiments are in MuJoCo simulation. A discussion of sim-to-real considerations beyond the reactive term in Eq. 7 would strengthen practical relevance.
- Breaking down computational latency by component (VLM, LLM, MPPI) would help readers assess practical deployability.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"VLA baselines are evaluated unfairly" (from Harsh Critic)**: REMOVED per hard rule — the asymmetry favors the baseline (VLAs had LIBERO fine-tuning; CoRAL is zero-shot). The comparison is valid for the paper's claim about zero-shot generalization to contact-rich tasks. The speed disadvantage is retained separately as a minor weakness.
- **"Missing engagement with LLM-generated reward/cost function literature (Eureka, Text2Reward)" (from Harsh Critic)**: REMOVED per hard rule — we cannot verify existence of specific related works beyond what the paper cites. Do not mention missing related works.
- **"Explainability example deferred to appendix" (from Harsh Critic)**: REMOVED per hard rule — the appendix is stripped in this format; the original submission includes it. Weaknesses about missing appendix content are not valid.
- **Strength Finder "SOTA baselines with fair evaluation"**: Dropped as a standalone strength — the VLA comparison is a legitimate baseline choice but is not the paper's most compelling contribution. The comparison evidence is captured in the broader evaluation picture.
- **"N_retry persistent failures undefined" (from Harsh Critic Section-by-Section Notes)**: The paper does define N_retry = 15 as the trigger threshold; what is slightly vague is the exact progress criterion. The concern is too minor to list separately.

## Novel Insights
The reviewers did not surface genuinely novel observations beyond the paper's own contributions. The most interesting meta-observation is that the Unified VLM ablation provides the strongest evidence for the paper's thesis — the complete collapse of a merged perception-and-reasoning model is more convincing than the comparison against VLAs — and this should arguably be the paper's headline result rather than the VLA comparison.

## Suggestions

- Run an additional ablation on at least one task (ideally T1 or T6) that isolates the LLM's cost function J₀: use the LLM's contact strategy C₀ but substitute a simple hand-crafted cost function (e.g., distance-to-target + control regularization). Compare this against the full CoRAL with LLM-generated J₀. This would directly address the major weakness.
- Show concrete examples of LLM-generated cost functions for 2-3 tasks with qualitative analysis of which terms proved useful.
- Report Clopper-Pearson confidence intervals on success rates in Table 1.
- Specify the sampling biasing mechanism in Section 3.2 (how candidate contact points from Eq. 3 modify MPPI sampling).
- Clarify which experiment Figure 4 depicts, or align its values with the text description (2.0→0.1 kg vs. 1.0→0.85 kg).

## Score and Decision

### Calibration Anchors

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Diff-Transfer | EODzbQ2Gy4 | 3.40 | R1 (low) | Different approach, CoRAL is clearly stronger |
| Online Self-Improvement | I0To0G5J7g | 3.20 | R1 (low) | Different domain; CoRAL has stronger evaluation |
| GRAIL | oyXoGJQlUf | 3.00 | R1 (low) | LLM for symbolic action rules; CoRAL more sophisticated |
| From Appearance to Motion | wl1Kup6oES | 3.00 | R1 (low) | Vision pre-training; not comparable |
| Generating Robot Policy Code | WtHKqtHVXo | 4.00 | R1 (mid) | LLM for contact-rich code; CoRAL much stronger architecture and evaluation |
| Make a Donut | iTsHStJKcm | 5.25 | R1+R2 (mid) | LLM subgoals + MPC; CoRAL has online adaptation and stronger ablations |
| CORN | KTtEICH4TO | 4.75 | R1+R2 (mid) | Contact-based RL; different paradigm |
| LLMPhy | qGL6fE1lqd | 4.40 | R1 (mid) | LLM physical reasoning; CoRAL more complete system |
| Instruct2Act | JWrl5pJCnl | 5.00 | R2 (mid) | LLM → Python code; CoRAL more sophisticated |
| GenBot | fZZ4ubttru | 5.50 | R2 (mid) | Generative simulation; CoRAL has stronger ablations |
| Plan-Seq-Learn | hQVCCxQrYN | 6.67 | R2 (high) | LLM+RL for long-horizon; PSL has broader eval, CoRAL more innovative LLM use |
| Video Language Planning | 9pKtcJcMP3 | 7.00 | R2 (high) | Video+language planning; stronger evaluation |
| GenSim | OI3RoHoWAN | 8.00 | R1 (high) | LLM generates sim tasks; well-supported claims, real robot; CoRAL clearly weaker |

**Bracket**: Round 1 placed CoRAL in 5.0–7.5. Round 2 narrowed to 5.5–6.5. CoRAL is clearly stronger than Make a Donut (5.25) — it has online adaptation, nested feedback loops, and stronger ablations. CoRAL is slightly weaker than Plan-Seq-Learn (6.67) — PSL has broader evaluation (25+ tasks, 4 benchmarks) and its central claims are well-supported, whereas CoRAL's headline cost-function contribution is undersupported. CoRAL is substantially weaker than GenSim (8.0).

**Final Score**: 6.0 — a borderline accept with real contributions (modular architecture, contact strategy guidance, online adaptation) but a significant gap in demonstrating the central cost-function claim.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>