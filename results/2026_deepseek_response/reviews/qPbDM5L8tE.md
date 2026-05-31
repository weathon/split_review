Now I have a good understanding of the calibration landscape. Let me compose the final review.

## Summary

CoRAL proposes a modular framework for contact-rich robotic manipulation that separates VLM (perception, parameter estimation) from LLM (reasoning, cost function design, contact strategy). The LLM generates MPPI cost functions and contact strategies in zero-shot, with a memory unit for experience reuse and an outer-loop adaptation mechanism that refines world model parameters mid-execution. Evaluated on 6 simulated manipulation tasks in MuJoCo/Robosuite against VLA baselines (OpenVLA-OFT, π0.5) and expert-designed cost baselines.

## Strengths

- **Clean ablation evidence for separation of VLM/LLM roles.** The "Unified VLM" variant (single model for both perception and planning) fails catastrophically — 0/10 on 4 of 6 tasks — while the full CoRAL achieves moderate to high success on those same tasks (Table 1). This directly supports the paper's core architectural claim and is one of the strongest pieces of evidence in the paper.

- **LLM-generated contact strategy dramatically reduces planning complexity.** On the "Flip with Wall" task (T6), the variant with the LLM's contact strategy is 83.9% faster (32 vs. 199 steps) and travels a 63.9% shorter path (1.33 m vs. 3.69 m) compared to receiving only a cost function with no contact bias. This is a compelling demonstration of how symbolic reasoning prunes the search space for a sampling-based planner.

- **Ablation studies isolate each component's contribution.** Every ablation (w/o Pose Tracking → 0/10 on 5/6 tasks; w/o Refinement → 0/10 on T1; w/o Memory → degradation across multiple tasks) cleanly demonstrates that each module serves a distinct and necessary function.

- **Explainability is a genuine architectural advantage.** The LLM can provide natural-language diagnoses of failures (e.g., adjusting cost function weights after diagnosing a poorly weighted plan), which black-box VLA policies cannot do.

## Weaknesses

### Major

- **Inconsistency in the parameter adaptation experiment (Section 4.1.4, Figure 4).** The paper states the evaluation world was initialized with a mass of **2.0 kg** vs. ground truth **0.1 kg** (a 20× error). Yet Figure 4 shows the "corrected mass" starting at **1.0 kg** and converging to **~0.85 kg** — 8.5× the true value. The y-axis range (0.75–1.00) excludes the ground truth of 0.1 entirely. The text claims estimates "converged remarkably close to their true values," which is contradicted by the figure data for mass. This undermines the central evidence for the claimed online parameter adaptation capability. The authors need to explain this discrepancy: is the figure mislabeled (e.g., showing a different experiment), is the text wrong about ground truth, or is the adaptation genuinely failing to converge?

- **Simulation-only evaluation does not support claims about real-world robustness.** The paper repeatedly claims robustness to "severe sim-to-real gap" and suitability for "deploying robots in unknown environments where accurate a priori physical models are often unavailable." All experiments are conducted in MuJoCo via Robosuite. Contact-rich manipulation is notoriously sensitive to simulator fidelity (friction, mass, contact dynamics). The reactive control term in Eq. (7) is described as addressing the sim-to-real gap, yet no real-robot experiments demonstrate this. The claims substantially exceed the evidence.

- **Thin statistical basis.** All success rates are reported as x/10 trials per condition, with no confidence intervals, error bars, or significance tests. The paper treats differences like 2/10 vs. 4/10 (memory ablation on T1) as meaningful, but with n=10, this difference is within sampling noise. While 10-trial evaluation is common in some simulation work, the paper makes strong quantitative claims (e.g., "memory boosted the success rate significantly") that require stronger statistical support.

### Minor

- **LLM prompts are not provided.** The method's central claim is that the LLM *generates* cost functions and contact strategies, but the prompt is not shown. The reader cannot assess whether the LLM is performing genuine reasoning or being hand-held with carefully structured prompts that enumerate available variables and cost primitives. This limits reproducibility and makes it hard to evaluate the method's true generality.

- **Memory retrieval mechanism is underspecified.** The paper states "the LLM embeds the current task into a latent semantic space" for retrieval (Eq. 1), but does not specify the embedding model, similarity metric, or retrieval threshold. A RAG-based memory system needs concrete implementation details to be reproducible.

- **Baseline comparison framing could be more balanced.** The paper frames the VLA baselines (OpenVLA-OFT, π0.5) as "state-of-the-art" comparisons, but these models are evaluated zero-shot on custom tasks outside their LIBERO training distribution, and unsurprisingly fail on contact-rich tasks. Against the expert-designed cost baselines (the appropriate comparison for a planning-based approach), CoRAL is competitive but not clearly superior — Expert (FSM) still outperforms CoRAL on 5/6 tasks. The narrative emphasizes outperforming VLA baselines but downplays the gap to expert cost functions.

### Trivial

- Figure 4's y-axis range (0.75–1.00) excludes the stated ground truth (0.1 kg), making the convergence claim impossible to verify from the figure as presented.

## Nice-to-Haves

- Real-robot validation on at least one contact-rich task to support the sim-to-real claims.
- Increase trial count to ≥30 with confidence intervals.
- Provide full LLM prompts in the supplement.
- Report wall-clock timing breakdown for LLM calls, MPPI planning, and overall latency.
- Failure mode analysis: why does CoRAL fail on the 6/10 unsuccessful T1 trials?

## Removed Points

- *Mass correction being "fabricated":* The harsh critic's characterization is too strong — the data is in the figure, it's just inconsistent with the text claims. The figure exists and shows corrected mass values; the problem is the mismatch between the figure and the text, not fabrication. This is properly captured above as a Major weakness.
- *Generic reproducibility complaints about missing appendix content:* The appendix was stripped by the parser; missing proofs/appendix content from the parser output is not the authors' fault. Removed per rules.
- *Strength Finder's generic strengths*: "Addresses an important problem," "targets an interesting question" — removed as generic/superficial.
- *Missing comparison to other LLM planners (SayCan, Code as Policies):* The paper does compare against VLMPC and IMPACT in Related Work and evaluates against VLA baselines. The scope is clear. Removed as scope creep.
- *Strength about "dedicated pose estimator shown to be non-negotiable":* This overlaps with the ablation evidence already captured. Merged into the ablation strength.

## Novel Insights

The two-reviewer synthesis surfaces a tension the paper does not fully address: the LLM-driven cost design is the most novel aspect of CoRAL, but the evidence that the LLM is genuinely *reasoning* about contact dynamics (rather than pattern-matching from training) is thin. The mass correction inconsistency is a concrete manifestation of this: if the LLM cannot correctly diagnose a 20× mass error, how much of the claimed adaptation is real? This is a sharper question than either reviewer alone raised.

## Suggestions

1. **Fix the mass correction experiment.** Either correct the figure to match the text, correct the text to match the figure, or run a cleaner experiment where the adaptation genuinely converges toward the true value. This is the single most actionable fix for improving credibility.

2. **Disclose LLM prompts in their entirety.** Without them, the paper's core novelty ("the LLM generates the cost function") remains a black box. Showing the exact prompt used for Task Formulation and Online Adaptation would resolve many reproducibility concerns at once.

3. **Scale back claims about real-world deployment.** Replace "severe sim-to-real gap" language with honest statements about the simulation-only scope. If real-robot experiments are planned for the future, state this clearly.

4. **Add statistical error bars.** Even with n=10, reporting standard deviation of completion times and perhaps bootstrapped confidence intervals for success rates would strengthen the quantitative evidence.

## Score and Decision

### Round 1 Bracket

Based on three bracketing queries for LLM-based contact-rich manipulation:
- **Lower band (avg < 3.5):** Papers like *Diff-Transfer* (3.40), *LARG2* (3.00), *GRAIL* (3.00) — rejected for weak evidence or overly narrow scope. CoRAL has stronger evidence and a clearer contribution than these.
- **Middle band (3.5–7.5):** Papers like *Generating Robot Policy Code for Contact-Rich Tasks* (4.00, sim: 0.80), *LLMPhy* (4.40, sim: 0.75), *Make a Donut* (5.25, sim: 0.75), *Zero-Shot Robotic Manipulation with Diffusion Models* (6.25, sim: 0.76).
- **Upper band (avg > 7.5):** Papers like *GenSim* (8.00), *Data Scaling Laws in Imitation Learning* (8.00) — these are broader in scope with extensive real-robot validation. CoRAL is clearly below this tier.

**Round 1 bracket: 3.5–6.0** (between the weak and middle anchors).

### Round 2 Narrowing

Within the bracket, I retrieved additional anchors:
- *Generating Robot Policy Code for Contact-Rich Tasks* (4.00) — the closest topical match. Like CoRAL, it uses LLMs for contact-rich tasks, but validates on a real robot. CoRAL has stronger ablations and task diversity but the mass inconsistency and simulation-only evaluation are liabilities. CoRAL is comparable to (slightly below) this paper overall.
- *LLMPhy* (4.40) — physical reasoning with LLMs, simulation only. Similar evaluation quality, but CoRAL has a more ambitious contribution. Comparable tier.
- *Make a Donut* (5.25) — zero-shot LLM planning with real-robot validation. CoRAL lacks real-robot experiments and has the mass inconsistency issue. CoRAL is below this anchor.
- *CrayonRobo* (5.20) — strong real-robot evaluation. CoRAL is below this.

CoRAL is comparable to *Generating Robot Policy Code* (4.00) and *LLMPhy* (4.40). The mass inconsistency and simulation-only evaluation prevent it from reaching the 5.25 level of *Make a Donut*.

### Anchor Papers Used

| Path | Avg Score | Round | Comparison to CoRAL |
|------|-----------|-------|---------------------|
| EODzbQ2Gy4.md (Diff-Transfer) | 3.40 | R1 | Weaker contribution; CoRAL is stronger |
| WtHKqtHVXo.md (Robot Policy Code) | 4.00 | R1, R2 | Closest topical match; CoRAL has better ablations but mass inconsistency |
| qGL6fE1lqd.md (LLMPhy) | 4.40 | R1, R2 | Comparable tier, CoRAL's contribution is more ambitious |
| iTsHStJKcm.md (Make a Donut) | 5.25 | R1, R2 | Stronger validation with real robot; CoRAL below this |
| c0chJTSbci.md (SuSIE) | 6.25 | R1 | Stronger overall; real-robot evaluation, thorough baselines |
| OI3RoHoWAN.md (GenSim) | 8.00 | R1 | Far stronger; extensive validation, broad scope |
| RQDuFF1rOn.md (Wonderful Team) | 3.67 | R2 | Weaker; CoRAL has clearer methodology and ablations |
| Aqfwhna1D7.md (CrayonRobo) | 5.20 | R2 | Stronger real-robot evaluation; CoRAL below |

### Final Score

**4.0**. The paper has a clear conceptual contribution and informative ablations, but the mass correction inconsistency in the core adaptation experiment undermines a central claim, and the simulation-only evaluation does not support the real-world robustness framing. The statistical basis is thin. These weaknesses are verifiable from the paper as written; they are not speculative.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>