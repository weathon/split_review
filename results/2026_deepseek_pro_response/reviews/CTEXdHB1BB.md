Now I have a good calibration picture. Let me finalize the review.

**Calibration summary:**

| Anchor | Score | Round | Comparison to CANON |
|--------|-------|-------|---------------------|
| BGnm7Lo8oW (Reasoning at Pre-Training Scale) | 5.50 | R1 | CANON is clearly stronger — more comprehensive experiments, cleaner theoretical contribution, consistent gains across models/tasks |
| 6UQaXJm53B (DfPO) | 5.25 | R1 | CANON is clearly stronger — fewer theoretical gaps, broader empirical validation |
| mMPMHWOdOy (WizardMath) | 8.00 | R1 | WizardMath is stronger — dramatic 10+ point gains, multi-scale experiments up to 70B. CANON has more modest gains (1.9–5.2 points) |
| cfKZ5VrhXt (COPO) | 7.33 | R2 | COPO has stronger theory (regret bound). CANON has broader experiments and cleaner core idea. CANON is comparable but slightly weaker on theory. |
| gkfUvn0fLU (Constrained RLHF) | 7.00 | R2 | Comparable quality. CANON has broader experiments, Constrained RLHF has a more novel problem framing. Both have practical limitations. |

**Round 1 bracket:** 6.0–7.5

**Round 2 narrowing:** CANON sits between Constrained RLHF (7.00) and COPO (7.33). Given CANON's stronger empirical breadth but weaker theory compared to COPO, and its comparable quality to Constrained RLHF with fewer practical limitations, I place CANON at **7.0**.

Now let me write the final review.

## Summary
This paper introduces CANON, an advantage estimation method for RLVR that splits sampled responses into two groups based on a target metric (e.g., entropy, response length) and computes separate inter-group and intra-group advantages. The key insight is that DR.GRPO decomposes exactly into an equally weighted sum of these two components (Eq. 7), and biasing the weighting toward inter-group or intra-group advantage systematically steers the model toward exploitation or exploration without imposing hand-crafted directional priors. Experiments across three LLMs and multiple math/logic benchmarks show that inter-group advantage improves math performance while intra-group advantage benefits complex logic reasoning, and scheduling between them (CANON-Dynamic) achieves balanced gains. Applying CANON to response length yields a superior Pareto frontier in the performance–efficiency trade-off.

## Strengths
- **Clean theoretical decomposition of DR.GRPO (Eq. 7):** The proof that DR.GRPO is exactly the unweighted average of CANON's inter-group and intra-group advantages when μ=0.5 is elegant and provides a principled foundation for the method. This is not a mere reformulation — it exposes structure that DR.GRPO conflates, which the paper then exploits by varying μ.
- **Selective amplification verified by ablation (Table 4):** Table 4 shows that direct numerical scaling (A = A × 2) degrades logic performance (25.1 vs 26.2) while CANON-Inter and CANON-Intra improve math and logic respectively. This cleanly demonstrates that regrouping matters beyond simply amplifying the advantage signal.
- **Consistent gains across three model families and two task categories:** Table 2 shows CANON-Dynamic outperforming DR.GRPO on Qwen2.5-Math-7B, Qwen2.5-Math-1.5B, and Llama3.1-8B across both math reasoning and high-complexity logic tasks. The pattern is consistent across model scales (1.5B to 8B) and architectures (Qwen and Llama).
- **Pareto-dominant efficiency results:** Table 3 and Figure 4c show CANON-Eff's Pareto frontier dominates all efficiency baselines. The stability of CANON-Eff across α values — contrasted with Length Reward (+), which collapses from 54.8 to 22.5 when its coefficient moves from 0.004 to 0.005 — is a practically significant finding.
- **Mechanistic training dynamics analysis:** Figure 2 tracks six metrics over training, revealing that CANON-Inter drives rapid reward increase and entropy decrease (exploitation), while CANON-Intra promotes exploration (higher entropy, more reflection, crossing into positive reflection gains late in training). Figure 6 further shows CANON-Dynamic achieves both positive rethinking gains and high training reward.
- **Hierarchical control via single scalar μ:** Figure 5 shows that varying μ ∈ [0.0, 1.0] produces a monotonic ordering of entropy trajectories, demonstrating genuine tunable control over the target metric without handcrafted penalties.

## Weaknesses

### Fatal
None.

### Major
- **Single-run reporting with no statistical evidence:** All results (Tables 1–4, Figures 2, 5, 6) are from single training runs with no error bars, standard deviations, or multi-seed averages. RL training is high-variance and advantage estimation methods are sensitive to random seed. While we acknowledge the enormous computational cost of multi-seed LLM RL training, the headline gains (e.g., 1.9 points on math, 5.2 points on XLarge logic) could partially reflect seed variance. The consistent pattern across multiple benchmarks and models partially mitigates this concern, but the paper would be substantially stronger with even one multi-seed comparison on the main result.

### Minor
- **CANON-Dynamic radar chart uses model-specific scheduling:** Figure 3 uses Cosin-First-Inter-Later-Intra for Qwen-7B and Llama-8B but First-Inter-Later-Intra for Qwen-1.5B. The paper acknowledges this (line 208: "A specifically designed strategy is acceptable for better performance in practice"), but it weakens the claim of a single principled solution. However, Table 2 shows that the model-agnostic First-Inter-Later-Intra schedule also beats DR.GRPO across all three models, so the core claim remains supported.
- **Asymmetric α-weighting in Eq. 9 is unmotivated:** The inter-group advantage weights the baseline reward mean for one group but the individual reward for the other (Eq. 9). The paper provides no justification for this asymmetry or discussion of alternative symmetric weighting schemes.
- **Mixed evaluation metrics conflated into a single aggregate:** The "overall" math score averages Avg@10 (for AIME/AMC) with Pass@1 (for other benchmarks), making the aggregate hard to interpret and directly compare across methods.
- **Theoretical results are motivational rather than foundational:** Theorem 1 establishes that inter-group advantage magnitude exceeds DR.GRPO under equal group sizes, and Theorem 2 shows CANON doesn't amplify independent conditions. Neither provides performance guarantees, convergence properties, or regret bounds. This is acceptable for an empirical paper but limits the theoretical contribution.
- **Per-token entropy computation not described:** Entropy is the primary grouping metric, but the paper does not specify how per-token entropy is computed (token-level, averaged over sequence, logits vs. probabilities), which matters for reproducibility.

### Trivial
- The abstract's claim that CANON "consistently outperforms prior methods across three LLMs" is slightly overstated — Clip-Cov beats CANON-Inter on individual benchmarks (AIME 25, GSM8k), and CANON-Inter loses to DR.GRPO on AIME 25. The overall trend is in CANON's favor, but "consistently" is not strictly accurate at the per-benchmark level.
- Different training datasets used for Llama vs. Qwen models in Section 5.2 (35k simpler dataset vs. 45k) introduce a confound when comparing across models in Table 2, though within-model comparisons remain valid.

## Nice-to-Haves
- A negative control experiment: grouping by a known-uninformative metric (e.g., random noise) would strengthen the argument that CANON works through amplifying meaningful metric signals specifically.
- An ablation comparing symmetric vs. asymmetric α-weighting in Eq. 9 would clarify whether the asymmetric design is necessary.
- A limitations section acknowledging the reliance on choosing a good grouping metric, the restriction to domains with verifiable rewards, and computational overhead of sorting.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"CANON-Dynamic is not a single method — it requires per-model trial-and-error"** (Harsh Critic): The paper clearly shows that the model-agnostic First-Inter-Later-Intra schedule beats DR.GRPO across all models in Table 2. The per-model selection only applies to the radar chart Figure 3 and the paper transparently reports all schedules for all models. This criticism overstates the problem.
- **"Intra-group advantage is itself a directional prior"** (Harsh Critic): The paper's claim is that CANON does not *presuppose* which direction of the metric is beneficial — the inter-group comparison discovers this from data. The intra-group advantage rewards correct answers in the worse-performing group, which encourages exploration but does not impose a directional prior on the metric itself. The criticism misinterprets the paper's framing.
- **"The paper does not discuss whether prior methods can achieve comparable results when their hyperparameters are tuned as extensively"** (Harsh Critic): The efficiency experiments in Section 5.3 explicitly sweep hyperparameters for all baselines (Length Reward (+) at 4 settings, Length Reward (*) at 3 settings), so this claim is factually incorrect.
- **"Denser sampling of CANON's hyperparameter could make its frontier appear smoother"** (Harsh Critic): This is speculative nitpicking. The Pareto dominance is clear from the reported points regardless of interpolation smoothness.
- **"The DR.GRPO baseline is also μ=0.5 in the CANON framework, so the comparison is within the CANON framework rather than against truly independent baselines"** (Harsh Critic): This is the whole point of the paper — showing that DR.GRPO is a suboptimal special case. The paper also compares against ReMax, R++, RLOO, GRPO, Entropy Adv, and Clip-Cov as independent baselines.
- **Figure 5 legend garbled by parser** (Harsh Critic): This is a parser artifact, not an author error.

## Novel Insights
The paper's insight that DR.GRPO implicitly averages an inter-group and intra-group comparison across an unlabeled partition — and that making this partition explicit by grouping on a target metric unlocks tunable control — is genuinely novel. The observation that inter-group and intra-group advantages map cleanly onto exploitation vs. exploration dynamics (Figures 2, 5, 6) provides a mechanistic understanding that was not obvious a priori. The finding that CANON-Eff is stable across α values while length-penalty baselines exhibit catastrophic collapse under coefficient changes (54.8 → 22.5) is a practically significant insight about the brittleness of hand-crafted directional priors vs. metric-aware regrouping.

## Suggestions
- Run at minimum 2–3 seeds for the core CANON-Inter vs. CANON-Intra vs. DR.GRPO comparison on Qwen2.5-Math-7B and report means with standard deviations. Even one additional seed would substantially strengthen the evidence.
- Replace or supplement the model-specific radar chart (Figure 3) with results using a single model-agnostic schedule (First-Inter-Later-Intra) across all models to demonstrate transferability.
- Add a brief description of how per-token entropy is computed (token-level logits averaged? sequence-level?) for reproducibility.
- Justify the asymmetric α-weighting in Eq. 9 or add a symmetric alternative as an ablation.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>