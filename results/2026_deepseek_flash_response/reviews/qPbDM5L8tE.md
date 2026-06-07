Now I have all the calibration data I need. Let me produce the final consolidated review.

## Summary

CoRAL proposes a modular neuro-symbolic framework for contact-rich robotic manipulation. It integrates a VLM for perception (object pose tracking via FoundationPose, physical parameter estimation), an LLM for high-level reasoning (generating MPPI cost functions, contact strategies, and online adaptation), with a reactive controller and memory unit. The system operates zero-shot without task-specific training data. Evaluated on 6 simulated manipulation tasks (10 trials each), CoRAL achieves reasonable success on contact-rich tasks where end-to-end VLA baselines fail.

## Strengths

- **LLM-generated cost function structure (§3.2, Eq. 2).** Unlike prior work (IMPACT, VLMPC) that uses VLMs only for perceptual guidance or sub-goal identification, CoRAL has the LLM generate the mathematical structure and weights of the MPPI cost function itself. This elevates the LLM from a perceptual guide to a high-level strategist that directly shapes the optimal control problem — a genuinely different design point.

- **Quantitative evidence for LLM-guided contact strategy efficiency (§4.1.4).** In the "Flip with Wall" ablation, providing the LLM's contact strategy makes the planner **83.9% faster** (32 vs. 199 steps) and yields a **63.9% shorter end-effector path** (1.33 m vs. 3.69 m). These are concrete, compelling results that directly tie the LLM's symbolic output to measurable planner improvement.

- **Ablation evidence for VLM/LLM role separation (§4.1.3, Table 1).** The Unified VLM variant (single multimodal prompt for both perception and planning) collapses to 0/10 on 4 of 6 tasks. While not perfectly clean (confounding prompt design with role separation), this provides reasonable support for the architectural claim.

- **Online world-model correction demonstrated (§4.1.4).** The outer-loop adaptation drives an overestimated mass toward ground truth over time, providing direct evidence that the system can diagnose misestimated physical parameters from execution failures and correct them mid-task.

- **Memory unit shows measurable gains on the hardest task (Table 1).** On T1 (Push+Pick Board), the memory module doubles the success rate from 2/10 to 4/10 and cuts completion time from 212 s to 162 s.

## Weaknesses

### Major

- **The VLA comparison is structurally uninformative and the framing is misleading.** CoRAL and the VLA baselines (OpenVLA-OFT, π_0.5) operate with vastly different information access and engineering support. CoRAL uses known 3D object models (FoundationPose), a full physics simulator (MuJoCo) as its planning world, a reactive controller with real-time force feedback, and GPT-4o to generate cost functions. The VLA baselines are monolithic RGB+language policies fine-tuned on LIBERO and evaluated zero-shot on custom tasks. The paper claims CoRAL "significantly outperforms" (line 193) these baselines, but this is the expected outcome of comparing an engineered pipeline against an out-of-distribution policy. The comparison tells us little about the scientific merit of CoRAL's approach. On the two tasks where VLAs do well (T2, T3 — closer to LIBERO's distribution), CoRAL matches but does not outperform. The paper should lead with the human-expert comparison, where the evidence is more informative but less flattering.

### Minor

- **Statistical evidence is thin.** All results are based on 10 binary trials per condition with no confidence intervals or significance tests, yet the paper uses "significantly" repeatedly (lines 193, 230). For a 4/10 success rate, the 95% binomial CI spans roughly [12%, 74%]. Key claims about differences between conditions (e.g., memory vs. no-memory on T1: 4/10 vs. 2/10) are well within sampling noise.

- **Explainability is claimed as a contribution but not evaluated.** The abstract and introduction list explainability as a core contribution (lines 9, 26, 29), but the paper provides only one anecdotal example of the LLM diagnosing a failure. There is no user study, no human preference evaluation, no comparison against the explainability of any baseline. Either the claim should be evaluated or scaled back.

- **The human-expert FSM baseline consistently outperforms CoRAL, and the gap is understated.** Expert FSM beats CoRAL on every task, often by wide margins (T1: 8/10 vs. 4/10; T6: 9/10 vs. 7/10). The paper frames this as "narrowing the gap" (line 197), but 4/10 vs. 8/10 is a large gap. There is no analysis of *why* the LLM cost functions are worse — whether the wrong weights, missing cost terms, or structural errors — which would be the most informative analysis for the research direction.

- **FoundationPose's requirement of known 3D CAD models for all interactable objects is a significant limitation not prominently discussed.** The system cannot operate zero-shot in genuinely novel environments where CAD models are unavailable. The paper notes this implicitly (line 65: "known 3D geometric models of the objects") but does not flag it as a limitation in the main text.

- **Prompt engineering details are omitted.** The method depends entirely on prompt-crafting for GPT-4o to generate cost functions, contact strategies, and diagnose failures. Without the prompts (which may be in the stripped appendix), the core LLM reasoning steps are not reproducible, and it is impossible to assess whether results are driven by the approach or by prompt engineering.

- **Two LIBERO benchmark tasks are mentioned (line 151) but never identified.** The paper does not specify which tasks correspond to LIBERO, making it impossible to evaluate how CoRAL compares on standardized benchmarks.

### Trivial

- The mass correction figure (Fig. 4) has a possible description discrepancy: the text mentions initializing with 2.0 kg (line 220), but the figure caption describes a y-axis ranging from 0.75 to 1.00 kg. This may be a parser artifact in the extracted caption.

## Nice-to-Haves

- A comparison against classical MPC (without LLM) with the same information access would isolate the LLM's contribution more cleanly than the current VLA comparison.
- Reporting per-control-cycle latency would help assess real-time feasibility.

## Removed Points

The following points from the reviews were removed with justifications:

- *"The Unified VLM ablation conflates model change with role separation"* — Removed. Both conditions use GPT-4o; the difference is whether it processes a single multimodal prompt (VLM role) or a text-only prompt (LLM role). The ablation tests the claimed architectural separation reasonably. While prompt engineering confounds are possible, they are speculative rather than demonstrated.
- *"The w/o Pose Tracking ablation is a straw man"* — Removed. The paper is testing whether the VLM can substitute for a dedicated pose estimator, which is a natural question to ask about a claimed VLM capability. Confirming that VLMs are bad at precise geometric tracking (as the ablation shows) is not a weakness of the paper.
- *"Mass correction figure shows corrected value still 8.5x the true mass"* — Removed. The figure is a parser-stripped image; the extracted caption may not accurately represent the visual content. Cannot verify from available information.
- *Strength Finder: generic strengths* — Removed strengths that are generic ("important problem", "timely topic") with no specific evidence.
- *Various nitpicks about reproducibility, missing appendix content, formatting* — Removed per filtering rules (parser artifacts, appendix stripping).

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely surface known tensions in LLM-for-robotics evaluation (fair baselines, statistical rigor) without generating genuinely novel observations beyond what the paper itself presents.

## Suggestions

1. **Reframe the evaluation to lead with the human-expert comparison.** The VLA baselines should be secondary or moved to a supplementary section. The paper's actual contribution is about substituting LLM-generated costs for expert-engineered ones — this comparison should be the primary axis of evaluation, with an honest discussion of where and why the LLM falls short.

2. **Provide failure analysis.** Analyze what the LLM gets wrong in its generated cost functions: wrong weights? missing terms? structural errors? This diagnostic analysis would be far more valuable than the current VLA comparison.

3. **Add statistical grounding.** Report binomial confidence intervals, run more trials, or at minimum stop using "significantly" without statistical backing.

4. **Either evaluate explainability or scale back the claim.** A user study, human preference ranking, or quantitative comparison against baseline explainability would substantiate the claim.

5. **Identify which tasks are from LIBERO** and discuss how CoRAL compares on those standardized benchmarks.

## Score and Decision

**Round 1 bracket:** [4.5, 6.5] — Based on comparison against calibration anchors:
- "Generating Robot Policy Code..." (4.00, Reject): CoRAL is clearly stronger (more tasks, better ablations, more novel architecture).
- "Make a Donut" (5.25, Reject): CoRAL has closed-loop adaptation vs. open-loop plans, more task diversity — slightly stronger.
- "LLMPhy" (4.40, Reject): CoRAL addresses a harder problem with more evaluation axes — stronger.
- "HAMSTER" (6.00, Accept): HAMSTER has real robot + human evaluation but simpler tasks; CoRAL has more novel architecture but weaker experiments. Comparable, but HAMSTER's stronger evaluation pushes it slightly higher.

**Round 2 narrowing:** Inspected full reviews of HAMSTER (6.00, Accept), Instruct2Act (5.00, Reject), SuSIE (6.25, Accept) as topically similar anchors. CoRAL is stronger than Instruct2Act (harder problems, more novel architecture) but weaker than SuSIE (no real-world experiments, weaker baselines, no benchmark results).

**Final calibration:** CoRAL sits between Instruct2Act (5.00) and HAMSTER (6.00). The uninformative VLA comparison and thin statistics are significant evaluation flaws that prevent it from reaching HAMSTER's level. The genuine novelty of the architecture (LLM-generated cost functions + outer-loop adaptation) suggests it merits a score above Instruct2Act.

**Calibration anchors used:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Generating Robot Policy Code... | WtHKqtHVXo.md | 4.00 | 1 | CoRAL clearly stronger (more tasks, ablations, novel architecture) |
| LLMPhy | qGL6fE1lqd.md | 4.40 | 1 | CoRAL stronger (harder problem, better evaluation) |
| Instruct2Act | JWrl5pJCnl.md | 5.00 | 2 | CoRAL somewhat stronger (harder tasks, more novel contributions) |
| Make a Donut | iTsHStJKcm.md | 5.25 | 1 | CoRAL slightly stronger (closed-loop adaptation, more task diversity) |
| HAMSTER | h7aQxzKbq6.md | 6.00 | 2 | CoRAL comparable but HAMSTER has stronger evaluation (real robot, human eval) |
| SuSIE | c0chJTSbci.md | 6.25 | 2 | CoRAL weaker (no real-world, no benchmark results, weaker baselines) |

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>