Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes **Agentic Reinforced Policy Optimization (ARPO)**, an RL algorithm for training multi-turn LLM-based agents that use external tools (search engine, web browser, code interpreter). The core idea is to use an entropy-based adaptive rollout mechanism that branches sampling at high-uncertainty tool-call steps, moving beyond trajectory-level RL which treats entire tool-use trajectories as flat sequences. A pilot study shows that token entropy spikes after tool calls, motivating partial sampling at those points. ARPO also introduces advantage attribution estimation (hard vs. soft) to distinguish shared and diverged token segments. Experiments across 13 benchmarks (math, knowledge QA, deep search) show ARPO consistently outperforms GRPO, DAPO, and Reinforce++ on both Llama3.1-8B and Qwen2.5-7B, while using fewer tool calls during training.

## Strengths

1. **Well-motivated entropy-based adaptive rollout mechanism** (Section 3.1, Equation 2): The paper identifies a real phenomenon — token entropy spikes after tool-use steps — and designs a concrete branching strategy (P_t = α + β·ΔH_t with threshold τ) that targets high-uncertainty decision points for additional exploration. This directly addresses a genuine limitation of trajectory-level RL for multi-turn tool-use.

2. **Consistent and broad empirical superiority over trajectory-level RL** (Table 1): ARPO outperforms GRPO, Reinforce++, and DAPO on all 10 mathematical and knowledge-intensive reasoning benchmarks for both Llama3.1-8B (average 55.3 vs. 51.1 for best baseline) and Qwen2.5-7B (58.3 vs. 56.5). The pattern is consistent across diverse dataset types, and the gains hold for two different model families, demonstrating robustness.

3. **Strong deep search results with 1k RL samples** (Table 2): ARPO achieves 43.7% average on GAIA with Qwen3-14B compared to 36.9% for GRPO and 25.2% for GPT-4o, using only 1k training samples. The comparison against GRPO under identical RL fine-tuning conditions (same data, same backbone) is fair and shows clear gains (e.g., GAIA: 43.7 vs. 36.9 for 14B; 38.8 vs. 32.0 for 8B).

4. **Rollout diversity evidence** (Figure 7b): ARPO produces 54 distinct DBSCAN clusters vs. 48 for GRPO with greater intra-cluster compactness, providing direct evidence that the branching mechanism broadens the solution space during training.

5. **Pass@K scaling** (Figure 6): Clear scaling from Pass@1 to Pass@5 on GAIA (43.7%→63.2%), HLE (10.0%→24.0%), WebWalkerQA (36.0%→54.5%), and xBench-DS (35.0%→59.0%), showing that the expanded sampling space translates into reliable gains with repeated sampling.

## Weaknesses

### Fatal

None.

### Major

1. **Missing ablations of the branching mechanism itself**: The paper does not compare the entropy-based branching against simpler alternatives — such as (a) random branching with the same probability, (b) fixed-ratio branching (branch at every tool step), or (c) a version that simply allocates the same total rollout budget to more trajectory-level samples without branching. Since the entire claimed advantage of ARPO hinges on the entropy-based criterion being better at targeting useful exploration, the absence of these ablations is a significant gap. The paper references "more ablation and scaling analyses" in Appendix A.2 (stripped by parser), but the most critical comparisons (random/fixed-ratio branching) are standard enough to warrant main-paper treatment.

2. **No variance or statistical significance reported for main results** (Table 1, Table 2): All results are reported as single-point estimates without standard deviations, confidence intervals, or multi-seed runs. Several differences are small (e.g., Qwen2.5-7B: ARPO 58.8 vs. GRPO 59.0 on HotpotQA; ARPO 78.8 vs. GRPO 78.0 on MATH500) and could fall within per-run noise. Without error bars, the reader cannot assess the reliability of the reported improvements.

3. **The "half the tool-call budget" claim is supported by only one experiment** (Figure 7a): The efficiency comparison shows ARPO vs. GRPO on Qwen2.5-7B for a single training run, with no replication, no other model (e.g., Llama3.1-8B), and no other dataset. The abstract and conclusion state this as a general result, but it has not been established as a robust phenomenon. Further, the paper measures training-time tool calls but does not report test-time tool-call budgets or compare methods at matched tool-call counts to confirm the efficiency-accuracy trade-off is genuine.

### Minor

4. **Theoretical foundation is a notational restatement** (Section 3.3, Equation 6): The Generalized Policy Gradient Theorem simply redefines token groups as macro actions and applies standard policy gradient. The paper acknowledges it "encompasses the traditional Policy Gradient Theorem as a specific instance," which is accurate, but this does not provide new convergence guarantees, optimization insights, or justification for why entropy-based branching specifically is beneficial. The claim that it provides "a robust theoretical foundation" overstates its contribution.

5. **The pilot entropy study is descriptive, not validated** (Section 2, Figure 2): The observation that entropy spikes after tool calls is visually clear but rests on qualitative inspection of a single figure. No quantitative comparison (e.g., average entropy before vs. after tool calls with confidence intervals, or a statistical test) is provided to support the claim that search feedback introduces "more uncertainty than Python feedback."

6. **No error bars for Figure 5** (hard vs. soft advantage): The comparison between hard and soft advantage estimation shows a single learning curve per condition, making it impossible to assess whether the apparent advantage of the soft setting is reliable.

### Trivial

None.

## Nice-to-Haves

- Compare ARPO against step-level/segment-level RL baselines (e.g., Guo et al. 2025, Li et al. 2025g) if applicable in the agentic tool-use setting.
- Provide a case study showing a concrete trajectory where branching discovers a correct path that trajectory-level sampling misses.
- Analyze test-time tool-call counts, not just training-time counts, to better substantiate the efficiency claim.

## Removed Points

- **"Deep search comparison is fundamentally unfair (prompted methods vs. fine-tuned)"** — The paper includes a direct comparison against GRPO (RL fine-tuned under identical conditions) within the RL-based method rows of Table 2. The prompted methods (Vanilla RAG, Search-o1, etc.) are provided as supplementary context, not as the primary comparison. The main claim is about beating trajectory-level RL, and that comparison is fair.
- **"Soft advantage estimation is simply standard GRPO without modification"** — The paper acknowledges this explicitly ("While we retain the original GRPO loss formulation") and explains that the distinction arises from the rollout mechanism, not the loss function. This is not a weakness; it is a design choice.
- **"Hierarchical reward r_M may incentivize unnecessary tool calls"** — The bonus r_M = 0.1 is conditioned on the answer being correct ("If Format is Good & Acc. > 0"), so it does not incentivize unnecessary tool calls independent of correctness. This is speculative and not supported by evidence.
- **"Missing comparison against step-level RL methods (Guo et al. 2025, Li et al. 2025g)"** — These methods are cited in the related work. Comparing against every related method is neither feasible nor required for the paper's stated scope. Moved to nice-to-have.
- **"Claims about 'pioneeringly quantify' are overblown"** — Style concern; entropy analysis in RL is well-cited in the paper's own references. The paper does cite prior entropy-based RL work.
- **"Hyperparameters α, β, τ are unspecified"** — Values may be in the stripped appendix; also, this is a reproducibility nitpick that does not threaten the core claims.
- **Various presentation, formatting, and scope-creep criticisms** — Removed per review discipline guidelines.

## Novel Insights

Beyond the paper's own contributions, a genuinely novel observation emerges from the contrast between the two reviewers: the harsh critic correctly identifies that the paper's strongest claim (half the tool-call budget) rests on the thinnest evidence (one training run, one model), while the paper's most defensible contribution (consistent gains over trajectory-level RL across 13 datasets) is undercut by the lack of error bars. This tension — a potentially strong empirical result presented without the statistical rigor needed to confirm it — is the paper's central unresolved issue. The entropy-based rollout idea is intuitively appealing, but whether the entropy criterion itself drives the gains, versus simply providing more rollouts at critical points, remains unproven.

## Suggestions

1. **Run ablations of the branching mechanism**: Compare ARPO against (a) random branching at the same average rate, (b) fixed-ratio branching (branch at every tool step), and (c) a version that allocates the partial sampling budget to additional full trajectories instead. This would directly test whether the entropy-based criterion provides value beyond simply increasing the number of rollouts at tool-use steps.

2. **Report standard deviations over 3+ seeds**: At minimum for the main results (Table 1, Table 2), to establish whether the reported gains are statistically meaningful.

3. **Substantiate the efficiency claim**: (a) Repeat the tool-call comparison on at least one additional model (e.g., Llama3.1-8B) and one additional dataset; (b) report test-time tool-call budgets; (c) compare ARPO and GRPO at matched tool-call budgets to show the efficiency-accuracy trade-off more rigorously.

4. **Tone down the "half the tool-call budget" claim** to reflect the limited evidence supporting it, or provide the additional experiments needed to support it.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>