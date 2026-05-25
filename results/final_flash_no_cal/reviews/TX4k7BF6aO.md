Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes ARPO, an RL algorithm for training multi-turn tool-using LLM agents. ARPO uses an entropy-based adaptive rollout mechanism that monitors token entropy after tool calls and adaptively branches sampling at high-entropy steps, combined with an advantage attribution estimation within the GRPO loss framework. Experiments across 13 benchmarks show ARPO consistently outperforms trajectory-level RL algorithms (GRPO, DAPO, REINFORCE++) while using significantly fewer tool calls during training.

## Strengths

1. **Empirically well-supported core idea**: The entropy-based adaptive rollout yields consistent gains over trajectory-level baselines across 13 benchmarks (Tables 1, 2) with two different model families (Llama3.1-8B, Qwen2.5-7B, Qwen3-8B/14B). The average improvement over GRPO is ~4% on the 10-task suite, and ~6% on deep search tasks. These results are substantiated by multiple independent metrics.

2. **Practical tool-call efficiency**: ARPO achieves higher accuracy while using roughly half the tool calls of GRPO during training (Figure 7a). This is a practically meaningful advantage for deployed agentic systems where API costs are a real constraint.

3. **Rollout diversity analysis provides supporting evidence**: The clustering analysis (54 vs. 48 clusters, Figure 7b) and Pass@3/Pass@5 scaling (Figure 6) show that ARPO produces more diverse trajectories, supporting the claim that adaptive branching broadens the exploration space.

4. **Empirical motivation from entropy analysis**: The preliminary experiments (Section 2, Figure 2) provide a clean, data-driven motivation for targeting tool-call steps — the entropy spikes after tool calls are visually clear and consistent across both search and Python tools, with search feedback producing larger effects.

5. **Clean integration with GRPO**: Rather than introducing an entirely new training objective, ARPO leverages the existing GRPO loss and shows how its importance-sampling ratios naturally differentiate shared and individual tokens from branching trajectories (Section 3.2). The comparison of hard vs. soft advantage settings (Figure 5) is a useful ablation that justifies the default choice.

## Weaknesses

### Fatal
None.

### Major

1. **The entropy comparison baseline conflates tool-induced uncertainty with natural reasoning drift.** The core branching signal ΔH_t compares post-tool-call entropy (H_t) to the initial entropy from the *first k tokens* of the trajectory (H_initial), rather than to the entropy *just before* the tool call. This means the branching signal captures the cumulative uncertainty shift from the start of generation, not the uncertainty specifically introduced by the tool result. Since the model's entropy can naturally drift during intermediate reasoning steps, this design conflates tool-induced uncertainty with other sources of entropy variation. The paper provides no justification for this design choice and no analysis of how the results would change with a more targeted baseline (e.g., comparing post-tool-call entropy to pre-tool-call entropy). This is the algorithm's central adaptive mechanism; a poorly specified signal weakens the claimed connection between entropy and the value of exploration. **(Section 3.1, Equation 2 and surrounding text)**

### Minor

2. **The complexity claim (O(n²) → O(n log n)) is poorly defined and unsubstantiated.** Section 3.1 states "assuming the global expansion size and the number of tokens per trajectory are n" — treating two independent quantities as a single variable. Trajectory-level rollout cost is linear in total tokens, not O(n²) as claimed. The paper provides no derivation, and the footnote "Neglecting the minor overhead from token-level entropy calculations" does not salvage an analysis that is mathematically inconsistent on its face. This does not affect the empirical results but erodes technical rigor. **(Section 3.1.4)**

3. **The advantage attribution estimation is presented as a larger contribution than it is.** The "soft advantage" setting (Section 3.2) retains the standard GRPO loss in full; the paper's contribution here is observing that GRPO's importance-sampling ratios naturally differentiate shared and individual tokens when trajectories share prefixes. This is a valid and useful analysis of how ARPO's rollout interacts with existing objectives, but it is not a new training objective or a fundamentally new credit-assignment method. The "hard advantage" setting is presented as an alternative but not used. The framing of "advantage attribution estimation" as a separate contribution inflates what is essentially a property of the rollout design interacting with GRPO. **(Section 3.2)**

4. **No statistical significance or variance reporting.** All results are single-run point estimates. Given the modest absolute gains (often 2–4% on individual tasks) and the small size of some benchmarks (e.g., AIME has only 30 problems), error bars or multiple seeds are needed to assess whether improvements are reliable. This is a standard expectation in empirical RL papers. **(Tables 1, 2)**

5. **No ablation isolating the entropy signal from the branching structure.** The paper does not compare entropy-based branching against random branching at the same frequency (e.g., branching at the same steps with probability sampled from ARPO's historical distribution). Without this control, it is unclear whether the benefit comes from the entropy signal specifically or from the branching structure itself (which could be triggered by any reasonable criterion). The efficiency claim (Figure 7a) similarly attributes lower tool-call usage to "entropy-based adaptive rollout" without isolating whether any adaptive branching would produce similar savings. **(Section 5.2, Figure 7)**

6. **The multi-tool reward bonus (r_M) is not ablated.** The reward function includes a 0.1 bonus for using both search and Python tools (Equation 5). It is possible that this bonus, rather than the rollout mechanism, drives some of the observed improvements (especially on deep search tasks where multi-tool usage is beneficial). An ablation controlling for the reward design would clarify the source of gains. **(Section 3.2, Equation 5)**

7. **The normalization procedure for ΔH_t is ambiguous and could affect results.** The paper states: "the normalization means summing all the values of ΔH and dividing by the vocab size V." Since H_initial and H_t are vectors of length k (one entropy per token position), summing the difference and dividing by V is an unusual normalization. Why divide by vocabulary size rather than by k? How does this choice affect the scale and distribution of branching probabilities? The paper provides no discussion. **(Section 3.1.2)**

### Trivial

8. **Main paper does not list the hyperparameter values used** (M, N, k, Z, α, β, τ). While the appendix may contain details (which are stripped from the review copy), these should be in the main text for a self-contained algorithm description.
9. **The formula P_t = α + β·ΔH_t can produce values outside [0,1]** without clipping being specified. This affects whether branching is ever triggered in practice and how τ is calibrated.
10. **The "pioneeringly quantify" language in the contribution list** overstates novelty — entropy in LLM reasoning has been studied in several of the paper's own citations (Wang et al. 2025b,c; Zheng et al. 2025b). The specific application to tool-use agents is valuable without needing this modifier.

## Nice-to-Haves

- **Compare to a non-entropy adaptive branching baseline** (e.g., branching at random steps or at fixed intervals controlled to match the same frequency). This would establish whether the entropy signal itself provides value over other branching triggers.
- **Control for tool-call budget** in the efficiency comparison: train GRPO with a limited tool-call budget to match ARPO's average usage, then compare performance, or compute performance-per-tool-call Pareto curves.
- **Report greedy decoding (temperature 0) results** alongside the current temperature 0.6 sampling for direct comparability with prior work that uses greedy evaluation.
- **Report Pass@3 and Pass@5 for baseline methods** (not just ARPO) to enable a complete comparison of sampling diversity.
- **Consider using pre-tool-call entropy as the baseline** for ΔH_t instead of initial trajectory entropy, to more directly measure tool-induced uncertainty.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The tool-use efficiency comparison is not controlled because ARPO's adaptive branching inherently uses fewer tool calls"** — This criticism conflates correlation with cause. The paper's claim is an empirical observation (ARPO achieves better accuracy with fewer tool calls during training), not a controlled causal claim. The comparison is fair: both methods are trained under the same compute budget and training steps. The fact that ARPO's design naturally produces lower tool usage is the finding, not a confound. Moved to nice-to-have as a suggestion for further attribution analysis.
- **"GRPO baseline may benefit from more samples"** — The paper fairly trains both GRPO and ARPO with the same 1k RL samples. The speculation that GRPO might close the gap with more data is unfalsifiable without evidence and does not invalidate the existing comparison.
- **"Missing related works"** — I cannot verify the existence of missing citations and following instructions, I do not include this.
- **"Missing appendix content, missing proofs"** — The appendix is stripped by the parser; these criticisms cannot be verified and are excluded per instructions.
- **"Formatting/style nitpicks"** — Parser artifacts are not author errors.
- **"The theoretical foundation is generic"** — The GPG Theorem (Section 3.3) is a formal statement that macro-action decomposition yields a valid policy gradient. While the reviewer argues it does not specifically justify entropy-based branching, the theorem provides necessary theoretical grounding for why partial rollouts (of any kind) are valid, which is a prerequisite for ARPO's approach. This is not a weakness — the paper does not claim the theorem justifies entropy specifically.

## Novel Insights

The most interesting observation emerging from the review is the tension in the entropy baseline design: ARPO's branching depends on comparing post-tool-call entropy to initial trajectory entropy, but the paper's own motivation (entropy spikes after tool calls) would more naturally support a comparison to pre-tool-call entropy. This discrepancy suggests the algorithm might be improved with a different baseline, and it also raises a question about whether the current design partially works because it captures a broader "uncertainty accumulation" signal rather than just tool-induced uncertainty. The cluster analysis showing more diverse rollout trajectories (54 vs. 48 clusters) is genuine evidence of behavioral diversity but doesn't directly confirm entropy guidance is the cause — a random-branching control at matched frequency would be the clearest test.

## Suggestions

1. **Fix or justify the entropy baseline.** Either switch to comparing post-tool-call entropy to pre-tool-call entropy (to isolate tool-induced uncertainty) or explicitly justify why the initial trajectory baseline is appropriate (e.g., by showing that intermediate reasoning steps have negligible entropy drift).
2. **Add a random-branching ablation** where branching occurs at the same steps and frequency as ARPO but triggered randomly rather than by entropy threshold. If ARPO outperforms this control, the entropy signal is validated.
3. **Report statistical significance** by running multiple seeds (at least 3) with standard deviations, especially for smaller benchmarks where individual point estimates are unreliable.
4. **Ablate the r_M multi-tool reward bonus** to separate the effect of reward design from the rollout mechanism.
5. **Remove or rigorously ground the complexity analysis.** If the intent is to discuss computational efficiency, use a standard measure (total tokens generated per rollout) and provide a clear derivation.
6. **Provide hyperparameter values and a basic sensitivity analysis** (at minimum, vary α or τ over a small range on one task) to demonstrate robustness.

## Score and Decision

The paper presents a novel, well-motivated, and empirically supported approach to step-level exploration in agentic RL. The core idea — using entropy at tool-call steps as a signal for adaptive branching — is sound and the results across 13 benchmarks are consistent and practically meaningful. The tool-call efficiency finding is a genuine practical advantage. However, the paper has several weaknesses that reduce its strength: the entropy baseline choice is unexamined and could dilute the signal, the advantage attribution framing overclaims, the complexity analysis is unsloppy, and key ablations (random branching control, r_M ablation, multiple seeds) are missing. These are addressable and do not invalidate the core contribution. The paper would benefit from revisions but is solid enough for acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>