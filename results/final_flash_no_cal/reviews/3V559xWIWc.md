## Summary

This paper identifies a training-inference mismatch in tree-based speculative decoding: existing draft model training (EAGLE, HASS) uses sequence-level objectives that neglect the tree structure used at inference. It proposes two fixes: (1) TALF, a tree-aware loss that aggregates cross-entropy over all nodes of a target-model-generated tree, improving calibration on lower-ranked tokens; and (2) SALF, a dynamic tree construction algorithm with a provably monotonic early-stopping criterion that reduces drafting overhead. Combined, SALF&TALF achieve 15.6–39.4% and 6.5–24.4% end-to-end wall-clock speedups over EAGLE-2 and HASS across three LLMs and five benchmarks, under both greedy and non-greedy sampling.

## Strengths

1. **Well-motivated diagnosis drives the method.** Figure 2 cleanly demonstrates that prior training (EAGLE, HASS) under-calibrates the draft model on lower-ranked tokens, which constitute >10% of tree nodes during inference. TALF specifically addresses this, improving accuracy by ≈5% and reducing ECE by ≈0.05 on ranks 2–5 (Figure 2(b)). The diagnostic-to-solution narrative is clear and empirically grounded.

2. **TALF consistently improves draft quality (τ) regardless of tree construction method.** Across beam search, optimal tree search, and SALF, TALF raises mean τ over EAGLE-2 by 11.7–12.9% and over HASS by 3.5–7.3% (Table 2). This shows that the benefit of tree-aware training is not contingent on a particular drafting algorithm.

3. **SALF is a principled early-stopping rule with a theoretical guarantee.** Theorem 1 proves that the sum of probabilities of nodes selected for expansion monotonically decreases over drafting iterations. SALF operationalizes this to stop when further gains fall below a threshold, yielding 14.4% higher end-to-end speedup than optimal tree search despite a modest τ reduction (Table 2, TALF row). The algorithm is clearly specified (Algorithm 2) and supported by sensitivity analysis (Table 4).

4. **Consistent speedups across diverse settings.** SALF&TALF outperform both baselines on every combination of 3 LLMs × 5 benchmarks × 2 temperatures (Table 1). The relative improvements are especially pronounced for the stronger target model (DeepSeek-R1-Distill-Llama-8B) and under non-greedy sampling, where draft-target alignment is hardest.

5. **Clean component ablation.** Table 2 orthogonally varies loss function (EAGLE-2 / HASS / TALF) and tree construction (beam search / optimal / SALF), cleanly isolating each contribution. Parameter sensitivity for TALF top-k (Table 3) and SALF threshold th (Table 4) is provided.

## Weaknesses

### Fatal
None.

### Major
None. The weaknesses below are all addressable and do not invalidate the core contribution.

### Minor

1. **Generation quality is asserted but not empirically verified.** The abstract and conclusion claim speedups come "without any generation quality degradation." While standard SpD theory (rejection sampling, tree attention) guarantees distribution preservation in principle, the paper does not explicitly state its verification protocol, nor does it provide empirical confirmation (e.g., perplexity on held-out text, task accuracy comparison between target-only and SpD outputs, or a distributional divergence measure). This is standard practice in the SpD literature (the baselines also rely on the same theoretical guarantee), so it is not a fatal gap, but it should be documented and ideally backed by a brief empirical check to satisfy readers unfamiliar with the guarantee.

2. **Training-tree / inference-tree mismatch acknowledged but not discussed.** TALF trains on trees built by the *target* model, while inference trees are built by the *draft* model using its own probability estimates. The paper correctly notes the computational rationale for this design (§3.2: "prohibitively high computational cost" of dynamic construction per epoch), but does not discuss whether the fixed target-model trees produce a training distribution representative of what the draft model will encounter at inference. A brief analysis or argument (e.g., "the target model's tree subsumes the draft model's high-probability nodes, so the mismatch is mild") would strengthen the paper.

3. **No variance/confidence intervals for speedup measurements.** Table 1 and Table 2 report speedups without standard deviation, confidence intervals, or number of runs. Wall-clock timing is subject to system noise, especially for the modest absolute differences (e.g., 2.91× vs. 3.09× on Llama2-7B greedy). Reporting variance would increase confidence that improvements are statistically stable.

4. **Omission of regression loss not ablated.** TALF drops the regression loss ℒ_reg used by EAGLE and HASS. The paper claims "training solely on the token probability distributions across multiple nodes was sufficient" (§3.2), but provides no controlled comparison showing the effect of adding or removing ℒ_reg. An ablation row in Table 2 would cleanly answer whether the regression loss is neutral, harmful, or helpful under TALF.

5. **Time-budgeted training for DeepSeek model introduces a confound.** For DeepSeek-R1-Distill-Llama-8B, EAGLE, HASS, and TALF were trained for equal wall-clock time (24 hours) rather than equal epochs. The paper notes this is "defensible as a fair comparison regarding the training cost," but the three loss functions may converge at different rates. If one method would improve more with additional epochs, the comparison could be biased. The trade-off should be discussed more explicitly.

6. **Verification procedure not explicitly stated.** The paper references tree attention (Miao et al., 2024) and rejection sampling (Leviathan et al., 2023; Chen et al., 2023) in related work (§5) and describes verification generically in §2.1, but does not explicitly state which acceptance/rejection rule was used in the experiments. Stating "we use the standard rejection sampling verification as in Leviathan et al. (2023), which guarantees exact preservation of the target distribution" would close this gap.

### Trivial

None that survive filtering.

## Nice-to-Haves

- **Add a direct comparison to the SpecExec public implementation** rather than a re-implemented "optimal tree search" baseline. This would strengthen the external validity of the SALF comparison.
- **Provide sensitivity analysis for the SALF threshold th on additional target models** (beyond DeepSeek-R1-Distill-Llama-8B in Table 4) to substantiate the claim that th=0.6 gives "more consistent performance improvements." Currently the choice is justified only qualitatively.
- **Explore adaptive or model-specific tuning of th** — the paper already mentions this as future work.

## Removed Points

These points were raised by input reviewers but are removed or downgraded per the filtering criteria:

- **"Speculative-fatal framing of missing quality evaluation"** — The harsh critic framed the missing quality validation as a "structural gap" that makes the "central premise... unsubstantiated." This overstates the issue: standard SpD theory guarantees distribution preservation when proper rejection sampling is used, and the baselines (EAGLE-2, HASS) similarly do not re-verify quality empirically. The weakness is valid but minor, not fatal. The critic's characterization has been demoted accordingly.
- **"Missing related works"** — Not included, per instructions.
- **"Reproducibility concerns about undisclosed hyperparameters"** — The paper provides detailed hyperparameters in §4.1 and Appendix D. This concern is not grounded.
- **"Formatting/style nitpicks"** — All removed per instructions.

## Novel Insights

The key insight that emerges from the reviews more clearly than from the paper alone is the *interaction between the two contributions*: TALF improves calibration on lower-ranked tokens, which makes SALF more effective (fewer wasteful nodes are pruned) — as evidenced by the smaller τ drop when SALF is applied on top of TALF (6.3%) versus EAGLE-2 (6.2%) or HASS (2.4%) in Table 2. This suggests TALF and SALF are synergistic: better calibration reduces the need for deep tree expansion, which is exactly where SALF cuts overhead. The reviewers did not fully articulate this; it emerges from cross-referencing the component ablation.

## Suggestions

1. **Add one sentence stating the verification protocol** (standard rejection sampling as in Leviathan et al., Chen et al., using tree attention) and a brief note that this theoretically guarantees the target distribution. Optionally provide a one-paragraph empirical check (perplexity on a held-out set or pass@1 match) to make the "no quality degradation" claim fully transparent.
2. **Add a brief paragraph discussing the training-tree / inference-tree mismatch** — acknowledging it, explaining why the fixed target-model trees are a reasonable proxy, and noting any limits.
3. **Report variance** for the main speedup results (Table 1), at minimum the range over 3 runs or an estimate of system noise.
4. **Add an ablation row** in Table 2 for "TALF + regression loss" to show the effect of the omitted ℒ_reg.
5. **Acknowledge the epoch-vs-time confound** for the DeepSeek model more explicitly and discuss whether the three methods converge at different rates.

## Score and Decision

The paper makes two well-motivated, clearly described contributions, supported by thorough experiments across multiple models and tasks. The weaknesses are real but minor — they concern documentation and additional analysis, not the validity of the core results. The paper is a solid contribution to the speculative decoding literature.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>