Now I have enough calibration data. Let me finalize the review.

**Round 1 bracket**: 4.5–6.5 (clearly above 4.0 anchors like "Generating Robot Policy Code," comparable to 5.0–5.25 anchors like Instruct2Act and "Make a Donut," clearly below 7.0 anchors like M³PC).

**Round 2 narrowing**: Comparing against Instruct2Act (5.00, Reject) — CoRAL has better ablation design and a more novel architectural contribution (LLM as cost function architect), but Instruct2Act has real-world experiments and no internal contradictions. Comparing against "Make a Donut" (5.25, Reject) — similar level but "Make a Donut" has real-world validation. Comparing against M³PC (7.00, Accept) — M³PC is more technically rigorous with real-robot experiments and no evidence integrity issues. CoRAL sits around 5.0.

---

## Summary
CoRAL proposes a modular neuro-symbolic framework for contact-rich robotic manipulation that separates VLM-based perception (pose tracking via FoundationPose, physical parameter estimation via GPT-4o) from LLM-based reasoning (cost function generation and contact strategy formulation for an MPPI controller), with a memory unit for experience retrieval and two-level feedback loops for online adaptation. Experiments on 6 tasks in MuJoCo/RoboSuite simulation compare against VLA baselines and expert-designed cost baselines, with ablation studies isolating each component.

## Strengths
- **Well-designed ablation studies that cleanly isolate each component's contribution (Table 1).** Four ablation variants (w/o Memory, w/o Refinement, Unified VLM, w/o Pose Tracking) show interpretable degradation: the Unified VLM variant collapses from 4/10→0/10 on T1, and w/o Refinement drops from 4/10→0/10, demonstrating each module is necessary rather than redundant.
- **Novel use of LLM as cost-function architect, validated by expert baseline comparison.** Rather than using the LLM as a high-level planner, CoRAL has the LLM directly formulate MPPI cost function structure and weights (Eqs. 2–3). Table 1 shows LLM-generated costs approach expert FSM performance on hard tasks (T5: 9/10 vs. 10/10; T6: 7/10 vs. 9/10), while vastly outperforming single-stage expert design on sequential task T1 (4/10 vs. 0/10).
- **Quantitative evidence that LLM contact strategies transform search efficiency (Section 4.1.4).** On T6, the guided approach is 83.9% faster (32 vs. 199 steps) with 63.9% shorter end-effector paths (1.33 m vs. 3.69 m), providing concrete evidence that Eq. 3's contact point sampling meaningfully prunes the MPPI search space.
- **Inclusion of expert-designed cost baselines (both single-stage and FSM) provides a meaningful upper bound.** This contextualizes CoRAL's LLM-generated costs against what expert engineering achieves on the same controller infrastructure — stronger evaluation practice than typical.

## Weaknesses

### Fatal
None.

### Major
- **Figure 4 directly contradicts the text on a central adaptation claim.** Section 4.1.4 states mass was initialized at 2.0 kg with ground truth 0.1 kg and claims the estimate "converged remarkably close to their true values." However, Figure 4's y-axis ranges from 0.75 to 1.00 kg, showing corrected mass dropping from ~1.00 to ~0.85 kg — nowhere near the 0.1 kg ground truth and barely different from the initial value. This is the paper's primary evidence for online parameter adaptation, and the figure directly falsifies the text's characterization.

- **Baseline comparison is confounded by unacknowledged informational asymmetry.** CoRAL accesses: (1) known 3D object models M for FoundationPose (line 65: "known 3D geometric models of the objects"), (2) a physics simulator used by MPPI to roll out K=200 trajectories over H=50 steps (lines 117–118, 153), (3) force/torque sensor data from the physics engine (lines 130, 147), and (4) multiple GPT-4o API calls. The VLA baselines receive only RGB-D and proprioception from LIBERO checkpoints. CoRAL's claimed superiority over "fine-tuned" VLAs is substantially confounded by these advantages — particularly the physics simulator providing exact forward dynamics. The paper frames this as an architectural comparison without acknowledging the asymmetry. At minimum, this confound should be discussed; ideally, a VLA+MPPI ablation where the VLA provides cost functions to the same controller would isolate the architectural contribution.

### Minor
- **LLM-to-executable parsing pipeline is underspecified.** The paper describes LLM outputs (cost function structure, weights, contact regions with centers $c_j$, radii $e_j$, tangent vectors — Eqs. 2–3) but never describes how free-form LLM text is reliably converted into these structured mathematical objects. This is the critical link for reproducibility and assessing failure modes of the parsing step.
- **Only 10 trials per condition with no statistical reporting.** With n=10, the standard error for a proportion is ~15%. Differences of 1–2 successes (e.g., CoRAL 9/10 vs. Expert FSM 10/10 on T4) are within noise. No confidence intervals or statistical tests are reported.
- **Simulation-only evaluation despite sim-to-real framing.** The paper repeatedly invokes "sim-to-real gaps" (Section 4.1.4) and deployment in "unknown environments" as motivation, yet all experiments use a perfect simulator. The online adaptation mechanism has never been tested against actual model mismatch.

### Trivial
None.

## Nice-to-Haves
- Add at least 1–2 real-robot experiments to validate sim-to-real claims.
- Report computational cost analysis: GPT-4o API calls per task, planning latency per cycle, total task completion time breakdown.
- Analyze LLM failure modes: how often does the LLM generate poor cost functions or contact strategies?

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Strength Finder's claim about "online world-model correction through Figure 4"**: The Strength Finder claimed Figure 4 demonstrates parameter convergence to ground truth. Verification shows the figure directly contradicts this — mass converges to ~0.85 kg, not the stated 0.1 kg ground truth. This "strength" is invalid and was removed.
- **Criticisms about missing appendix content**: Appendix is stripped by parser; cannot verify.
- **Criticisms about missing related works**: Cannot verify existence of external works; removed per policy.
- **Generic formatting/style nitpicks**: Removed per policy.

## Novel Insights
The paper's most novel observation is that separating VLM perception from LLM reasoning produces dramatically better results than unifying them (Unified VLM ablation: 0/10 on nearly all complex tasks vs. 4/10–10/10 for the separated architecture). Combined with the finding that LLM-generated cost functions can approach expert-designed FSM performance while substantially outperforming single-stage expert costs on sequential tasks, this provides concrete evidence that the neuro-symbolic separation — not just using a large model — is the key architectural insight. The expert baseline comparison is also genuinely informative, revealing where LLM-generated costs still fall short and where they match expert engineering.

## Suggestions
- Fix or replace Figure 4 with an experiment matching the text (2.0→0.1 kg convergence), or accurately describe the experiment the figure depicts.
- Add a discussion paragraph acknowledging that CoRAL's informational advantages (physics simulator, known 3D models, force sensors) confound the VLA comparison, and consider adding a VLA+MPPI ablation.
- Specify the LLM-to-executable parsing pipeline in detail.
- Add statistical reporting (confidence intervals or standard deviations) for the 10-trial evaluations.

## Calibration Report

**All retrieved anchors across rounds:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| LARG2 | Q6HYM1EMu8 | 3.00 | 1 | CoRAL clearly stronger — more thorough architecture, better ablations |
| GRAIL | oyXoGJQlUf | 3.00 | 1 | CoRAL clearly stronger — addresses harder tasks with more complete evaluation |
| On Surprising Efficacy | I0To0G5J7g | 3.20 | 1 | CoRAL more novel in architecture but this paper has RL fine-tuning |
| From Appearance to Motion | wl1Kup6oES | 3.00 | 1 | CoRAL clearly stronger |
| Generating Robot Policy Code | WtHKqtHVXo | 4.00 | 1 | CoRAL stronger — better ablations, more tasks, expert baselines |
| LLM+A | cbVnJa4l2o | 4.00 | 1 | CoRAL stronger — more thorough evaluation, novel cost-function role |
| RePLan | gisAooH2TG | 4.25 | 1 | CoRAL stronger — better ablation design, expert baselines |
| LLMPhy | qGL6fE1lqd | 4.40 | 1 | CoRAL more relevant to robotics, better task diversity |
| Make a Donut | iTsHStJKcm | 5.25 | 1 | Comparable — has real-world experiments, CoRAL has better ablations but Figure 4 issue |
| On Evaluation of Gen Sims | s3sJenvY5H | 4.75 | 1 | Different focus, CoRAL more directly impactful |
| Instruct2Act | JWrl5pJCnl | 5.00 | 2 | Comparable — similar LLM+foundation model paradigm, CoRAL more novel but has Figure 4 issue |
| Foundation RL | epZV1nykll | 5.75 | 2 | Different approach, CoRAL comparable in ambition |
| Language Model Non-Myopic | OoNazl6T7D | 6.50 | 2 | Stronger paper — more rigorous, CoRAL comparable in novelty |
| M³PC | inOwd7hZC1 | 7.00 | 2 | Clearly stronger — real-robot experiments, no evidence integrity issues |
| Motion Control Hierarchical | MWHIIWrWWu | 6.25 | 2 | Stronger — real-robot, more rigorous |

**Round 1 bracket**: 4.5–6.5
**Round 2 narrowing**: Comparing to Instruct2Act (5.00), "Make a Donut" (5.25), and M³PC (7.00), CoRAL sits around 5.0. It is clearly above the 4.0 anchors (better ablations, more novel architecture, expert baselines) but has a significant Figure 4 contradiction and confounded baselines that hold it below the 5.75+ anchors. The paper has genuine architectural novelty and strong ablation design, but evidence integrity issues prevent a higher score.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>