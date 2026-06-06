Now I have a clear picture. Let me finalize my calibration:

**Anchor comparisons:**
- "LLM as Decision Makers" (3.75): CoRAL is clearly stronger — better ablation design, more comprehensive experiments, clearer architecture
- "Generating Robot Policy Code" (4.00): CoRAL is somewhat stronger — more sophisticated architecture, better ablation, but the Figure 4 issue is a significant concern
- "LLMPhy" (4.40): Comparable — both have LLM + physics simulator integration; CoRAL has broader task coverage but the Figure 4 contradiction
- "Make a Donut" (5.25): CoRAL is below — Make a Donut has real robot experiments and no figure/text contradictions

**Round 1 bracket:** 4.0–5.5

**Round 2 narrowed to:** 4.0–4.5 — CoRAL sits between "Generating Robot Policy Code" (4.00) and "LLMPhy" (4.40), with the Figure 4 issue pulling it down. I assess CoRAL at **4.5** — it has enough genuine contributions (clean ablations, contact strategy gains, conceptual advance of LLM-as-cost-designer) to edge above the 4.00 anchor, but the Figure 4 contradiction on a key claim and missing IMPACT/VLMPC comparisons prevent it from reaching the 5+ range.

---

## Summary
CoRAL proposes a modular neuro-symbolic framework for contact-rich robotic manipulation where an LLM acts as a high-level strategist by directly formulating MPPI cost functions and contact strategies, while a separate VLM handles physical parameter estimation and FoundationPose provides 6-DoF pose tracking. The architecture features nested feedback loops (inner MPPI re-planning, outer LLM-driven adaptation) and a RAG-based memory unit for experience reuse. Experiments on six contact-rich tasks in simulation compare against end-to-end VLA baselines, human-expert-designed cost baselines, and four component ablations.

## Strengths
- **Genuine conceptual advance — LLM as cost-function designer for MPPI**: Rather than using LLMs/VLMs as perceptual guides or subgoal proposers (as in prior work IMPACT, VLMPC), CoRAL has the LLM directly formulate the mathematical structure and weights of the MPPI cost function (Section 3.2, Eq. 2). The LLM determines which cost terms to include and their relative weights based on task semantics. This grounds commonsense reasoning directly in the optimal control formulation, which is a meaningful conceptual step beyond existing hybrid approaches.
- **Well-designed ablation study that isolates each architectural component**: The four ablations in Table 1 each remove exactly one component, producing interpretable degradations: Unified VLM fails near-totally on complex tasks (0/10 on T1, T5, T6), w/o Pose Tracking yields 0/10 on most tasks, w/o Refinement drops T1 from 4/10 to 0/10, and w/o Memory reduces T1 from 4/10 to 2/10. This provides clean causal evidence for each module's individual contribution to the overall system.
- **Compelling quantitative evidence for contact strategy guidance**: The targeted T6 ablation comparing LLM-guided vs. random contact sampling yields an 83.9% reduction in planning steps (32 vs. 199) and a 63.9% shorter end-effector path (1.33 m vs. 3.69 m). These are large-effect, well-measured results that directly validate the claim that symbolic contact strategies (Eq. 3) intelligently prune the action search space for long-horizon contact problems.

## Weaknesses

### Fatal
None.

### Major
- **Figure 4 contradicts the paper's central claim about online parameter adaptation (Section 4.1.4)**: The text states the mass estimate was initialized at 2.0 kg against a ground truth of 0.1 kg and claims the agent's belief "converged remarkably close to their true values." Figure 4 shows initial mass at 1.00 kg (not 2.0 kg), converging to approximately 0.85 kg on a y-axis that ranges only from 0.75 to 1.00. The ground truth of 0.1 kg is not even on the scale, and 0.85 kg is over 8× the claimed true value. Either the figure was generated from a different experimental setup than the text describes, or the convergence claim is false. The w/o Refinement ablation in Table 1 provides indirect evidence that the outer loop contributes to performance, but the claimed mechanism — accurate parameter convergence — is not substantiated by the figure presented. This directly undermines the paper's evidence for its online adaptation capability.
- **No comparison to the most directly related methods (IMPACT, VLMPC)**: Section 2 discusses IMPACT and VLMPC — methods that similarly combine VLMs/LLMs with motion planners or MPC — and claims CoRAL "significantly advances this paradigm." Yet neither appears as a baseline in Table 1. Without comparing against methods that also integrate foundation models with model-based control, the paper cannot substantiate its claim that having the LLM design cost functions (rather than identify subgoals or generate cost maps) yields practical benefits over these existing integrations.

### Minor
- **VLA comparison asymmetry inflates the apparent contribution**: CoRAL has access to a MuJoCo physics simulator, known 3D object models, and an MPPI controller rolling out 200 trajectories over a 50-step horizon at every timestep — infrastructure entirely unavailable to the end-to-end VLA baselines (OpenVLA-OFT, π₀.₅). The human-expert cost baselines (which share the same MPPI infrastructure) provide a fairer comparison; there, CoRAL underperforms the Expert FSM on every task. The abstract and introduction emphasize the VLA comparison, which overstates the contribution relative to a fair within-infrastructure evaluation.
- **No isolated evaluation of VLM physical parameter estimates**: The entire pipeline depends on GPT-4o estimating mass and friction coefficients from RGB-D images (Section 3.1), but the paper provides no evaluation of whether these estimates are usefully accurate or better than reasonable defaults. The outer loop can correct errors, but the baseline accuracy of the VLM's physical reasoning is never established.
- **"Explainability" claim is undersupported**: The paper repeatedly claims explainability as a headline contribution (abstract, introduction, Section 4.1.4), but supports it with only a single qualitative anecdote about the LLM outputting a natural-language diagnosis of a cost-weighting failure. No systematic evaluation is provided.

### Trivial
- **Missing prompt details affect reproducibility**: The prompts used for the three LLM calls (physical parameter estimation, task formulation, online adaptation) are not provided, making the core LLM behavior difficult to reproduce.
- **No confidence intervals on success rates**: With only 10 trials per task, differences of 1–2 trials (e.g., memory ablation on T3: 10/10 vs. 9/10) are consistent with noise. Binomial confidence intervals should be reported.

## Nice-to-Haves
- Showing what cost functions the LLM actually produces across the six tasks (e.g., a table of cost terms and weights per task) would let the reader judge whether the LLM generates meaningfully different structures or just minor variations on the Eq. 2 template.
- Including an IMPACT or VLMPC baseline on at least a subset of tasks would situate the contribution against the most direct competitors.
- A table comparing VLM-estimated physical parameters (mass, friction) against ground truth across randomized trials would clarify whether the VLM provides useful initialization.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *"The LIBERO benchmark tasks are mentioned but Table 1 does not clearly identify which tasks these are"* — The paper identifies T2 and T3 as standard pick-and-place tasks from the LIBERO suite (lines 151, 155). This is sufficiently clear.
- *"The Unified VLM ablation conflates role separation with fundamentally different prompting strategy"* — This is speculative; we cannot verify from the paper that a differently-prompted unified VLM would perform better. The ablation as presented is valid evidence for the claimed architecture choice.
- *"Limitations are deferred to appendix"* — Per review guidelines, appendix-stripping is a parser artifact; the original submission includes these sections. Not a paper weakness.
- *"Missing appendix figures/proofs"* — Parser artifact; removed per guidelines.

## Novel Insights
The paper's most interesting insight is the elevation of the LLM from a perceptual guide or subgoal proposer to a *cost-function designer* — having the LLM directly output the mathematical terms and weights of the optimal control objective rather than intermediate representations. This is a genuinely different way to connect language-model reasoning to model-based control. The contact strategy mechanism (Eq. 3) provides a concrete instantiation of how symbolic LLM outputs can prune continuous action spaces, and the 83.9% planning-step reduction demonstrates this works in practice. However, the paper does not empirically verify that this specific design choice (LLM-as-cost-designer vs. LLM-as-subgoal-proposer) drives the benefits over prior hybrid approaches, since it does not compare against methods like VLMPC that represent the subgoal-proposer alternative.

## Suggestions
- Fix or explain the Figure 4 discrepancy. If the figure is correct, retract or substantially qualify the claim about converging "remarkably close" to true values. If the text is correct, regenerate the figure so it matches the described experimental setup (initial mass 2.0 kg, convergence toward 0.1 kg).
- Add an IMPACT or VLMPC comparison, even on a subset of tasks, to substantiate the claim of advancing beyond prior hybrid LLM-planner integrations.
- Include the prompts used for the three LLM calls, at minimum in summarized form in an appendix.
- Report binomial confidence intervals for success rates given the small sample size (10 trials).

---

**Calibration anchor summary:**
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| GRAIL | oyXoGJQlUf | 3.00 | R1 (weak) | CoRAL is stronger — more sophisticated architecture with real experimental validation |
| LARG2 | Q6HYM1EMu8 | 3.00 | R1 (weak) | CoRAL is stronger — more complete system with ablation studies |
| Generating Robot Policy Code | WtHKqtHVXo | 4.00 | R1+R2 (mid) | CoRAL has stronger architecture and ablation, but Figure 4 issue is a liability this paper doesn't have |
| LLMPhy | qGL6fE1lqd | 4.40 | R1+R2 (mid) | Comparable — both combine LLM with physics simulators; CoRAL has better ablation, LLMPhy avoids contradictory figures |
| LLM as Decision Makers | NkYCuGM7E2 | 3.75 | R2 (mid) | CoRAL is clearly stronger — much better experimental design and clarity |
| Make a Donut | iTsHStJKcm | 5.25 | R1+R2 (mid) | CoRAL is weaker — Make a Donut has real robot experiments and no figure/text contradictions |
| GenSim | OI3RoHoWAN | 8.00 | R1 (strong) | CoRAL is much weaker — GenSim has novel task generation, comprehensive evaluation |

**Round 1 bracket:** 4.0–5.5  
**Round 2 narrowing:** CoRAL lands at 4.5 — above "Generating Robot Policy Code" (4.00) due to stronger architecture and ablation design, but below "Make a Donut" (5.25) due to the Figure 4 contradiction, missing nearest-method baselines, and simulation-only evaluation.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>