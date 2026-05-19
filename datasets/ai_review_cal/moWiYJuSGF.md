- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces World-Model-Augmented (WMA) web agents, the first work to incorporate world models into LLM-based web navigation. The key technical novelty is a **transition-focused observation abstraction**: instead of predicting full HTML/accessibility trees, the world model predicts natural language descriptions of only the changed elements between consecutive observations (using Hungarian matching for element alignment). At inference time, the agent samples action candidates from a frozen policy model, uses the trained world model to simulate the next observation for each candidate, and selects the action with the highest estimated reward from a value function. Experiments on WebArena (3.5pp improvement over CoT with GPT-4o, 5.3× speedup vs. tree search) and Mind2Web (new SOTA) demonstrate the approach's potential, particularly its cost and time efficiency relative to tree-search methods.

## Strengths

- **Novel transition-focused observation abstraction validated by ablations.** The Hungarian algorithm-based diffing combined with free-form natural language summaries of changes (Section 4.2.2, Figure 3) is a well-motivated solution to the problem of long, repetitive HTML observations. The ablation (Table 5, row 3) directly shows this abstraction yields 16.4% SR vs. 7.8% when predicting the full accessibility tree — a 2.1× improvement — proving the abstraction is material, not cosmetic.

- **Concrete and substantial efficiency gains over tree-search agents.** The paper documents a 5.3× speedup (140.3s vs. 748.3s per task) and 6.8× reduction in API cost over the tree-search baseline (Koh et al., 2024) (Table 4, Section 5.3). These are exact, reproducible numbers from a direct comparison against the most relevant inference-time search baseline.

- **Clean preliminary analysis motivating the approach.** The two preliminary studies (Section 3) directly measure (i) that current LLMs fail to predict action outcomes (~55% accuracy, barely above chance) and (ii) that providing the true next observation improves action selection accuracy from ~49% to up to 73% (38% relative improvement). This evidence grounds the core claim that world models can help, rather than assuming it.

- **Systematic ablation studies isolating each component.** The paper ablates the role of the simulated next state in value estimation, fine-tuned vs. prompted world models, the observation abstraction itself, and the choice of value function (Tables 5, 6, Section 5.4). Each variant is evaluated on the same 200-instance subset, providing a reproducible decomposition of the method's contributions.

## Weaknesses

### Fatal

None.

### Major

- **Value function trained on Mind2Web, applied to WebArena without discussion of domain transfer.** The paper states (Section 5.1, "Value function", line 212): "We fine-tune Llama-3.1-8B-Instruct to predict rewards using data from Mind2Web, where rewards (as training objective) are calculated based on the progress toward the goal, i.e. $t / (len(\tau))$." This same value function is used for WebArena evaluations in the main results (Table 1). WebArena uses a different reward structure (binary success/fail at task completion) and a different environment. The paper does not discuss whether or why this transfer is valid, nor does it report the value function's prediction accuracy on WebArena data. While the ablation in Table 6 shows the fine-tuned value function modestly outperforms a prompted GPT-4o-mini on WebArena (which partially mitigates the concern), the core experimental design should be clarified — either by explicitly justifying the transfer, reporting cross-domain prediction accuracy, or training/evaluating a WebArena-specific value function.

- **Overstated framing of WebArena results relative to Tree search.** The paper claims "superior cost and time efficiency" (Section 5.3, line 240) and writes that WMA "outperforms strong baselines (i.e. Tree search agent) with reduced cost and time" (Conclusion, line 303). However, on the per-site breakdown, WMA achieves lower success rates than Tree search on 4 of 5 sites (Shopping: 10.1 vs. 15.4; CMS: 18.8 vs. 25.0; Gitlab: 22.0 vs. 26.0; Map: 22.3 vs. 27.8; only Reddit is tied at 30.0). The overall SR is 16.6% vs. 19.2%. The efficiency advantage is real and valuable, but the paper should frame this honestly as a performance-efficiency trade-off (competitive accuracy at substantially lower cost) rather than implying overall superiority. The relative improvement framing (+29.7% vs. +28.0% over CoT) further obscures the modest absolute gap.

### Minor

- **Synthetic instruction generation process for WebArena training data is underspecified.** The paper generates 870 synthetic user instructions and 14K training instances (Section 5.1, lines 190–194) but does not describe the LLM prompt used to generate these instructions, nor does it discuss potential overlap or contamination with the 812 test tasks. Without this information, it is difficult to assess whether the world model's generalization is fairly evaluated or whether the training distribution inadvertently mirrors test tasks. The authors should provide the generation prompt and report lexical/task overlap statistics.

- **Preliminary analysis uses perfect next states but the real system uses imperfect world model predictions.** The second preliminary analysis (Section 3.2, Figure 2) shows LLMs benefit from access to the *true* next state. However, the actual world model produces imperfect simulations (as shown in the error analysis: 42% counterfactual, 26% low competence). The paper does not acknowledge this gap or quantify how much benefit is retained under realistic (noisy) simulations. The subsequent ablations partially address this by showing the full system works, but the logical leap from "perfect next state helps" to "imperfect world model will also help" should be explicitly discussed.

- **Additional cost of world model inference not reported.** The cost comparison (Table 4) compares WMA's total cost to Tree search's, but does not break down WMA's cost into its components: the policy model calls, world model calls (k per step), and value function calls. Reporting this breakdown would help readers understand where the efficiency gains come from and whether the world model itself is cheap enough to deploy.

- **Observation abstraction step uses an additional LLM call that is not ablated.** The abstraction pipeline (Section 4.2.2) uses an LLM to convert the structured diff list (UPDATED/DELETED/ADDED) into free-form text. It is unclear whether this natural-language conversion is necessary, or whether the world model could be trained directly on the structured diff list. This step adds both cost and potential variability.

### Trivial

None.

## Nice-to-Haves

- **Statistical significance for WebArena results.** The absolute improvements on WebArena are small (3.5pp for GPT-4o). Reporting confidence intervals or significance tests would strengthen the claim that the improvement is reliable. (Single-run evaluation on large benchmarks is standard in this field, so this is not a weakness, but would be a nice addition.)

- **World model prediction accuracy metric.** Beyond the error analysis, reporting how often the generated abstracted observation matches the ground-truth next observation (via human or automated evaluation) would help calibrate expectations about the method's upper bound.

- **Safety discussion of counterfactual imagination errors.** The error analysis reveals 42% of errors involve fabricating non-existent elements. The paper could briefly discuss whether such errors could lead to poor action selection in safety-critical scenarios and how they might be mitigated (e.g., confidence calibration).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Check concurrent work on the 'first to pioneer' claim"** — The harsh critic acknowledges this is not a flaw. Pure speculation, not a weakness.
- **"Potential for spurious correlations between instructions and page patterns in world model training"** — Speculative concern without evidence.
- **"Binary classification foil selection might be trivially distinguishable"** — The results show ~55% accuracy (near chance), so this is empirically not a problem; the critic themselves acknowledges it's not a major issue.
- **"Statistical significance missing"** — Moved to Nice-to-Haves; single-run benchmark evaluation is standard practice in the field.
- **"Generalization to unseen environments"** — Scope creep; testing on two different benchmarks (WebArena and Mind2Web, with different observation formats) is already a form of generalization.
- **"Discussion of safety"** — Moved to Nice-to-Haves; the error analysis already exists.
- **"Absence of statistical tests"** — Repeated point, merged.
- **"Reproducibility: hyperparameters, training logs, complete appendix"** — Standard practical limitations in conference submissions.
- **Strength Finder strengths about "addressing an important problem" and "important research question"** — Generic/superficial; removed as they are not specific to this paper's concrete evidence.

## Novel Insights

None beyond the paper's own contributions. The review surfaces no observation about the work that the paper itself does not articulate.

## Suggestions

1. **Clarify the value function training used for WebArena.** State explicitly whether the same Mind2Web-trained value function is used for all WebArena results, and provide evidence that its reward predictions correlate with WebArena outcomes (e.g., by evaluating prediction accuracy on held-out WebArena data or showing a calibration plot). Alternatively, train a WebArena-specific value function and compare.

2. **Reframe the WebArena vs. Tree search comparison.** Replace claims of "superior" efficiency with "competitive accuracy at substantially lower cost." Report the per-site breakdown in the main comparison table and explicitly acknowledge where and why WMA underperforms Tree search.

3. **Provide the synthetic instruction generation prompt** in the appendix, along with an analysis of lexical/task overlap between the synthetic training set and the 812 WebArena test tasks.

4. **Break down the inference cost** into policy model calls, world model calls (k per step), and value function calls, so readers can assess the marginal cost of the world model component.

5. **Acknowledge the gap between perfect and imperfect next-state simulation** more explicitly in Section 3.2, and cite the error analysis as partial evidence for what types of imperfections matter most.
