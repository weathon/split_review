Now I have all the information needed. Let me cross-reference the reviewer claims against the actual paper text and produce the final consolidated review.

## Summary

This paper proposes Auto-CEI (Automatic Curriculum Expert Iteration), a method that simultaneously improves LLM reasoning and aligns assertive vs. conservative response behavior (i.e., avoiding both "hallucination" and "laziness"). The core idea is that the number of reasoning steps (CoT length) serves as a proxy for problem difficulty and the LLM's capability boundary. Auto-CEI uses expert iteration with a length-dependent reward function that compensates "I don't know" responses that occur after sufficient reasoning while penalizing short refusals. A curriculum mechanism automatically adjusts the reward threshold via hill-climbing to push the LLM to reason longer before refusing, optimizing an objective function that balances precision and refusal rate. Experiments on BoardgameQA (logical reasoning), MATH (mathematics), and Blocksworld (planning) with Llama-3.1-8B show improvements over SFT, Vanilla EI, R-Tuning variants, and RLKF (DPO).

## Strengths

1. **Novel and well-motivated method design.** The combination of length-based reward shaping with curriculum-driven expert iteration is original. The paper grounds its approach in computational theory (relating step count to complexity) and shows that the method's behavior—refusal rate tracking error rate as response length increases—is consistent with the underlying assumption. This is verified empirically in Figure 2.

2. **Consistent advantage on the composite objective.** In Table 1, Auto-CEI achieves the highest objective function *f* on BoardgameQA (0.817 vs. 0.789) and MATH (0.575 vs. 0.552), and ties for highest on Blocksworld (0.896) against the strongest baselines. This shows the method reliably finds a better precision–refusal trade-off than alternatives.

3. **Curriculum component is empirically necessary.** The ablation study (Table 2) demonstrates that removing the curriculum ("No Curriculum") degrades accuracy and increases refusal rate across all three benchmarks (e.g., BoardgameQA accuracy drops from 59.70% to 56.10%, IDK rises from 29.37% to 34.43%). This isolates the curriculum's contribution and confirms it is responsible for pushing the capability boundary.

4. **Diverse evaluation across reasoning domains.** The paper tests on logical reasoning, mathematics, and planning—three qualitatively different reasoning types—lending credibility to the claim that the approach generalizes beyond a single task family.

5. **Reduction of over-conservatism.** The method starts from R-Tuning (which is deliberately over-conservative) and demonstrably reduces laziness: on Blocksworld, IDK rate drops from 57.51% (SFT+R-Tuning) to 18.30% (Auto-CEI) while improving accuracy from 38.54% to 74.78%.

## Weaknesses

### Fatal
None.

### Major

1. **Improvements over the strongest baseline are modest and not uniform across individual metrics.** Auto-CEI consistently achieves the highest *f* value, but the gains over EI+R-Tuning are small (e.g., +0.028 on BoardgameQA, +0.023 on MATH) and precision is actually slightly lower than EI+R-Tuning on MATH (55.63% vs. 55.80%) and Blocksworld (91.53% vs. 93.95%). The claimed "10–24% boost in precision" (abstract, line 47) is only true relative to Vanilla EI, which has no refusal behavior; against the strongest baseline (EI+R-Tuning), precision improvements are 0–5%. The paper should be precise about which comparison supports this claim.

2. **No variance or statistical significance reported.** All numbers in Table 1 and Table 2 are point estimates without standard deviations, confidence intervals, or multi-seed runs. Given the modest margins on *f* (e.g., +0.028), it is plausible that these differences fall within natural variation. This is the single biggest evidential gap and should be addressed before claims of "superior" performance can be confidently assessed.

3. **The precision–refusal trade-off is only evaluated at fixed λ for baselines.** The objective *f* uses λ=0.2 for all methods in Table 1, but this is an arbitrary point on the precision–IDK curve. The paper varies λ only for Auto-CEI (λ=0.5 in the ablation) and does not show Pareto frontiers for the baselines. Without this, it is unclear whether Auto-CEI genuinely dominates the trade-off or merely outperforms at the chosen λ.

### Minor

1. **The central assumption (CoT length ≈ difficulty) is validated only indirectly.** The paper provides theoretical grounding and shows that error rates increase with response length (Figure 2), which is consistent with the assumption. However, a more direct validation—e.g., a scatter plot of problem difficulty vs. average correct-step length, or human-annotated difficulty vs. step count—would strengthen the method's motivation. As presented, the assumption is plausible but not rigorously verified.

2. **Precision–IDK trade-off framing conflates two effects.** Auto-CEI both (a) improves reasoning robustness (via EI) and (b) adjusts refusal behavior (via the curriculum). The improvement in *f* could partly come from better reasoning alone (reducing the need to refuse) rather than from better alignment. The paper acknowledges this (the curriculum ablation helps isolate it) but does not fully disentangle the two effects. A breakdown showing how much of the *f* gain is from improved reasoning vs. better refusal calibration would be informative.

3. **Limited analysis of refusal quality.** The paper reports refusal rate but does not analyze whether the refusals are sensible ("I don't know" after genuine failed reasoning) or generic. A manual spot-check or automatic quality score (e.g., does the refusal come after a plausible reasoning attempt?) would strengthen the claim about alignment quality.

4. **BoardgameQA uses GPT-4-generated CoT for "unknown" questions.** This introduces a potential distributional mismatch: the training data contains GPT-4 reasoning traces for problems that are labeled "unknown" by the dataset's formal logic, but the model is evaluated on its own generations. The paper does not discuss or control for this.

5. **Hyperparameter sensitivity is underexplored.** The reward shape parameters *c₁* and *c₂* are derived from the initial policy's distribution. No analysis shows how sensitive results are to this initialization (e.g., if *c₁* were set manually instead). The hill-climbing step size *d* is also not ablated.

### Trivial
None.

## Nice-to-Haves

- **Pareto frontier analysis:** Show precision vs. IDK rate across varying λ for *all* methods, not just Auto-CEI. This would demonstrate dominance rather than pointwise superiority.
- **Full fine-tuning comparison:** The paper uses LoRA (rank 128). A comparison with full fine-tuning would show whether the method's benefits are specific to the parameter-efficient setting.
- **Computational cost reporting:** The paper acknowledges runtime cost in limitations but does not quantify it (number of EI rounds, total training time vs. baselines).
- **Reward shape ablation:** Test a step function instead of the sigmoid-shaped reward to see if the smooth transition matters.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Central assumption not validated; never provides empirical evidence"* — **Removed.** The paper does provide empirical evidence: Figure 2 shows that error rates of SFT/EI grow exponentially with response length and that Auto-CEI's refusal rates track those error rates. This is indirect but real empirical support. The critic's stronger claims about "never" providing evidence are factually inaccurate.

- *"Method specification is incomplete; pseudocode omits crucial details"* — **Removed.** The paper describes the resampling distribution (softmax with temperature τ, lines 178–179), hill-climbing details (step size *d*, domain *[μ−2σ, μ+2σ]*, stopping criterion, lines 205–206), and temperature setting (initial SFT accuracy, capped [0.4, 0.7]) in the main text. The pseudocode is concise but the text provides the missing detail.

- *"Baselines limited and not contemporary; missing PRM, confidence-based abstention, test-time scaling"* — **Removed.** These methods address different problems (per-step process rewards, selective prediction, inference-time scaling) and are not directly comparable to a post-training alignment method for refusal-aware reasoning. The paper's baselines (SFT, EI, R-Tuning, EI+R-Tuning, RLKF/DPO) are appropriate for the claimed contribution.

- *"Missing related work on abstention/selective prediction"* — **Removed.** The paper's scope is reasoning hallucination and laziness mitigation, not general selective prediction. The cited works on R-Tuning and RLKF are directly relevant to the refusal-aware setting.

- *"No discussion of computational cost"* — **Removed.** The limitations section (line 382) explicitly states: "our method might require a long time for optimisation as it requires running Expert Iteration multiple times."

- *"Paper does not discuss distributional mismatch from GPT-4 CoT for BoardgameQA"* — **Kept and downgraded to Minor #4.** The concern is valid but the paper does mention that GPT-4 is used to generate CoT for unknown problems (line 217), so it is acknowledged; however, the potential mismatch is not analyzed.

- *"Formatting/style nits about wrapfigure"* — **Removed.** Parser artifact; irrelevant to paper quality.

- *"LoRA vs full fine-tuning not compared"* — **Moved to Nice-to-Haves.**

- *"The resampling concatenation is unusual and not justified"* — **Removed.** The paper justifies this explicitly (line 179): "Since resampling also kills instances that waste some of the exploration data, we concatenate…to form the new training dataset."

## Novel Insights

Beyond the paper's own contribution, the most insightful observation from the review process is that the paper's two main weaknesses (modest gains over the strongest baseline and no variance reporting) interact to make the evidential case weaker than it first appears. The method is conceptually elegant—using a simple scalar (length) as a proxy for a complex latent variable (capability boundary)—but the empirical validation would need to be tighter (with confidence bounds and a dominated trade-off curve) to fully establish that this simplicity does not come at the cost of robustness. The tension between wanting a method that is general (works across tasks) and needing measurements that are statistically rigorous is a recurring pattern in LLM post-training papers.

## Suggestions

1. **Report 3+ seeds with standard deviations** for the main results. Without this, the modest *f* improvements are unconvincing.
2. **Provide a Pareto frontier of precision vs. IDK rate** for all methods by varying λ or equivalent hyperparameters. This would directly address whether Auto-CEI dominates the trade-off.
3. **Clarify the "10–24% boost in precision" claim** by specifying the reference baseline and showing that the improvement is meaningful after accounting for statistical noise.
4. **Add a direct validation of the step-count assumption**, such as a correlation plot between problem difficulty (e.g., correctness rate across LLMs or human annotation) and average correct CoT length on the benchmarks used.

## Score and Decision

The paper proposes a novel and well-motivated method for a practically important problem (balancing LLM assertiveness and conservativeness in reasoning tasks). The core methodology is sound, the curriculum ablation confirms the key design choice, and results are consistent (higher or tied *f* across three diverse domains). However, the empirical case is weakened by (a) the lack of variance reporting, which is critical given the modest margins; (b) the absence of a Pareto analysis across the trade-off; and (c) imprecise claims about the magnitude of improvements. These are addressable weaknesses, not structural flaws. The paper's contribution is genuine and the method is clearly described.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>