Now I have sufficient calibration data. Let me synthesize the final review.

## Summary

CoRAL proposes a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation. The core idea is to use a VLM (GPT-4o) for physical parameter estimation, an LLM to generate MPPI cost functions and contact strategies, and a reactive controller with online adaptation and memory-based experience reuse. Instead of treating the LLM as a high-level planner or perceptual guide, CoRAL directly grounds LLM reasoning in the mathematical structure of the control objective.

## Strengths

- **Novel and clean architectural contribution**: Using an LLM to generate the structure and weights of an MPPI cost function (rather than just high-level plans or perceptual guidance) is a genuine advance. The LLM outputs explicit cost terms (e.g., $w_d, w_c, w_u$) and contact strategies that are directly used by the controller, creating a well-principled link between symbolic reasoning and optimal control.

- **Zero-shot outperformance over fine-tuned VLA baselines on contact-rich tasks**: Table 1 shows CoRAL achieves 7–9/10 on the most physically demanding tasks (T4: Push with Constant Force, T5: Flip Box, T6: Flip with Wall), while OpenVLA‑OFT and π₀.₅ both score 0/10 on T4 and T6 despite being fine-tuned on LIBERO. This is a non-trivial finding — the VLA paradigm's reliance on imitation learning from static datasets is genuinely insufficient for tasks requiring explicit physical reasoning.

- **Online adaptation loop is empirically essential**: The "w/o Refinement" ablation drops from 4/10→0/10 on T1, 10/10→3/10 on T3, and 7/10→2/10 on T6 (Table 1). This convincingly shows that the outer-loop LLM diagnosing failures and correcting the world model is critical for multi-stage and long-horizon tasks.

- **LLM-guided contact strategy dramatically prunes search space**: On T6, the guided agent is 83.9% faster (32 vs. 199 steps) with a 63.9% shorter path (1.33 m vs. 3.69 m) compared to unguided MPPI (Section 4.1.4). This provides concrete evidence that the symbolic contact strategy makes a long-horizon contact problem computationally tractable.

- **Memory unit provides measurable benefit**: The "w/o Memory" variant is consistently worse — e.g., T1 drops from 4/10→2/10, T5 from 9/10→7/10, and completion times increase across the board (Table 1). This validates the practical value of experience reuse.

- **Explainability is a genuine architectural feature**: The LLM's natural-language failure diagnosis (Section 4.1.4) is not a wrapper but flows directly from the modular design. Unlike black-box policies, CoRAL can articulate *why* a plan failed and *what* it is correcting, which is valuable for debugging and trust.

## Weaknesses

### Fatal
None.

### Major

1. **The Unified VLM ablation does not isolate the benefit of role separation.**  
   The "Unified VLM" variant replaces both FoundationPose *and* the separate LLM with a single VLM prompt. Its catastrophic failure (0/10 on most tasks) could be driven entirely by the loss of a dedicated pose estimator — which the paper itself calls "a critical and non-negotiable component" — rather than by merging perception and reasoning. A proper ablation would keep FoundationPose constant and compare (a) one VLM call for both physical parameter estimation *and* cost generation vs. (b) separate VLM (parameters) + LLM (costs). As designed, this experiment does not cleanly support the paper's claim about role separation (Section 4.1.3, Table 1).

2. **The human‑designed FSM baseline outperforms CoRAL, and the claimed benefit of reduced tuning effort is not measured.**  
   On the two hardest tasks (T1, T6), the Expert (FSM) baseline achieves 8/10 and 9/10 while CoRAL achieves 4/10 and 7/10 (Table 1). On simpler tasks (T2–T5), CoRAL matches but does not beat the single-stage expert. The paper argues that CoRAL reduces manual effort, but zero quantitative evidence is provided — no person-hours, no iteration counts for prompt engineering, no comparison of effort required. Without this, a reader cannot evaluate the practical trade-off. A system that is both weaker *and* slower than an expert's hand-tuned cost function needs to show *some* compensating advantage beyond the architectural novelty.

3. **Small sample size (10 trials per condition) with no statistical measures.**  
   With binary success metrics and 10 trials, the 95% binomial confidence interval for, e.g., 4/10 spans approximately 12%–74%. Differences like 2/10 vs. 4/10 (the claimed memory benefit on T1) are not statistically significant. The paper draws strong conclusions about component criticality ("dramatic performance drop") from these noisy numbers without error bars, confidence intervals, or hypothesis tests. This undermines the reliability of every quantitative comparison.

### Minor

1. **Sensor asymmetry between CoRAL and VLA baselines limits the comparison's interpretability.**  
   CoRAL uses real-time force/torque feedback in its reactive control term (Equation 7), while OpenVLA‑OFT and π₀.₅ receive only RGB images and language. The paper's claim that "even fine-tuning an end-to-end policy is insufficient for scenarios that demand explicit physical modeling" (Section 4.1.1) overstates what can be concluded, since the baselines lack force-sensing entirely. This does not diminish CoRAL's real achievement, but the comparison conflates the absence of a sensor modality with a failure of the end-to-end paradigm.

2. **The memory module is under-specified.**  
   The paper states that retrieval works via "latent semantic space" and "sufficiently similar" experience (Section 3.2), but does not define the embedding space, similarity threshold, maximum memory size, or what happens on retrieval failure. Similarly, the reactive control term (Equation 7) uses a gain matrix $K_f$ whose values are not given. These details matter for reproducibility.

3. **Explainability is shown via a single anecdote, not systematic evaluation.**  
   The natural-language diagnosis example (Section 4.1.4) is illustrative, but the paper claims explainability as a contribution without measuring it — no user study, no correctness rate of LLM diagnoses, no comparison to VLA introspection methods.

4. **The mass-correction plot (Figure 4) shows one trajectory.**  
   While the online parameter adaptation mechanism is compelling, a single illustrative trajectory does not tell the reader how often the LLM successfully corrects parameters vs. hallucinating worse values.

### Trivial
None.

## Nice-to-Haves

- **Statistical grounding**: Report success rates with binomial confidence intervals, or run more trials (e.g., 50+) on at least the two hardest tasks. Report variance of completion times.
- **Ablation that isolates role separation**: Keep FoundationPose for both variants, compare one VLM call for both parameter estimation and cost generation vs. separate VLM + LLM calls.
- **Failure-case breakdown**: For the 6/10 failed T1 trials, categorize whether failure was due to incorrect parameter estimation, poor cost function design, planner limitations, or controller overshoot.
- **Effort quantification**: Report how many person-hours or LLM API calls were needed to design prompts vs. designing the expert FSM cost functions.
- **Real-robot validation**: The most compelling next step would be a physical robot performing the same tasks, since the paper repeatedly invokes sim-to-real robustness.

## Removed Points

- **Criticism about the appendix being stripped (Limitations section)**: The paper references Appendix A.3.2 for limitations details. The critic notes this section is absent but acknowledges it is not the authors' fault. Per hard rule: remove weaknesses about missing appendix sections.
- **Strength Finder's claim that role separation is "empirically essential" as proven by the Unified VLM ablation**: This strength directly conflicts with a verified weakness (the ablation is confounded). Per rules: when a strength and weakness disagree, the weakness wins.
- **Critic's point about "catastrophic failure" language regarding Unified VLM**: The description is factually correct (0/10 results) but the interpretation is addressed in the Major weakness above.
- **Critic's point that the paper fails to discuss whether the gap to human-designed costs is acceptable**: This is subjective framing — the paper does discuss this (Section 4.1.2: "narrows the gap... substantially reducing manual tuning effort"). The critic's desired framing is a judgment call, not a factual issue.

## Novel Insights

The reviews surface an interesting tension that the paper does not fully confront: CoRAL's strongest results (beating VLA baselines by a wide margin) come from tasks where the baselines lack force sensing entirely, while its weakest results (being outperformed by human-designed cost functions) come from direct comparisons on the same sensing and control architecture. This suggests that the value of LLM-generated cost functions may lie less in surpassing expert-tuned costs and more in (a) providing a viable starting point when no expert is available, and (b) enabling online adaptation that can recover from initial modeling errors — capabilities that the paper partially demonstrates but does not cleanly isolate. The real contribution may be the adaptation loop rather than the initial cost generation, a hypothesis the paper could test by comparing initial LLM costs against random/seeded cost baselines.

## Suggestions

1. **Fix the Unified VLM ablation**: Keep FoundationPose in both conditions. Compare (a) one VLM call for both physical parameter estimation and cost generation vs. (b) separate VLM (parameters) + LLM (costs). This would cleanly test the role-separation claim.
2. **Add binomial confidence intervals or run more trials** on T1 and T6 to provide statistical support for the claimed component benefits.
3. **Quantify the human effort** required to design the expert FSM costs (person-hours, iterations) so readers can evaluate the practical trade-off CoRAL offers.
4. **Add a baseline that provides force feedback to the VLA methods** (or at minimum, discuss the sensor asymmetry transparently) to make the VLA comparison more interpretable.

## Score and Decision

**Calibration anchors (all paths from retrieval batch; compared to CoRAL):**

| Anchor | Avg Score | Comparison to CoRAL |
|--------|-----------|---------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WtHKqtHVXo.md` | 4.00 | Similar topic (LLM + contact-rich). CoRAL has more comprehensive evaluation, better ablation design, and a novel architectural contribution. CoRAL is clearly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/iTsHStJKcm.md` | 5.25 | Both use LLMs + MPC for manipulation. Comparable in evaluation breadth and novelty. CoRAL has stronger ablation studies but weaker VLA comparison interpretability. Roughly similar tier. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lFYj0oibGR.md` | 6.50 | RoboFlamingo has stronger benchmark results on CALVIN and more thorough empirical analysis. CoRAL has a more novel architecture but weaker evaluation. CoRAL is a step below this. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/h7aQxzKbq6.md` | 6.00 | HAMSTER features real-robot validation and broader evaluation. CoRAL's evaluation is simulation-only and less rigorous. CoRAL is somewhat weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gkDRrvqeWF.md` | 5.50 | NaVILA (VLA for navigation) also has mixed evaluation scores. CoRAL's topic is different but the evaluation quality is comparable. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Cf8HBieRzL.md` | 3.50 | UniContact focuses on contact synthesis and has much weaker evaluation. CoRAL is substantially stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/N581Nje6fH.md` | 1.50 | Very weak paper with major clarity issues. CoRAL is in a completely different league. |

**Score rationale**: CoRAL introduces a genuinely novel architectural idea and demonstrates clear advantages over VLA baselines on contact-rich tasks. However, the evaluation has three significant issues — a confounded key ablation, the absence of statistical grounding, and no quantification of the claimed "reduced effort" benefit. The paper sits between the 5.25 anchor (similar quality, comparable limitations) and the 6.00+ anchors (more rigorous evaluation or real-robot validation). The idea is strong enough to warrant publication with revisions, but the current evidence does not fully support all claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>