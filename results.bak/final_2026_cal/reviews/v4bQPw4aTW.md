Now I have all the information I need. Let me synthesize the review. My round-1 bracket was [4.5, 6.5]. After reading anchors at scores 4.00, 4.80, 5.50, 6.00, and the paper in full, I can place this paper at 5.5.

Let me write the review.

## Summary

This paper tackles inference-time inefficiency in Best-of-N alignment, where a fixed budget of N samples is allocated uniformly to every prompt regardless of difficulty. The authors propose AdaBoN, a two-stage adaptive algorithm that first explores each prompt with a small budget to estimate its reward distribution (via Gaussian KDE), then greedily allocates the remaining budget across prompts to maximize cumulative maximum reward. The method requires no training, works out-of-the-box for any LM-RM pair, and minimizes latency through its two-stage design (only two serial calls to the LM). Empirical results across 12 LM-RM pairs, 3 datasets, and 50 batches per setting show consistent improvement over uniform allocation, with median Batch Win Rates of 0.54–0.62 and budget savings of ~20–25%.

## Strengths

- **Comprehensive empirical evaluation**: AdaBoN is tested across 12 LM-RM pairs (4 LMs × 3 RMs), 3 datasets (AlpacaEval, HH-RLHF, PKU-SafeRLHF), and 50 independently-sampled batches per dataset. Table 1 shows median BWRs consistently above 0.50 across all 12 pairs, with several pairs reaching 0.60+. Table 2b reports that for several LM-RM pairs, 100% of batches achieve BWR > 0.50. This breadth convincingly supports the claim that AdaBoN "consistently and often significantly outperforms the uniform allocation."

- **Model-agnostic and training-free**: Unlike Damani et al. (2024), which requires training a separate MLP for each LM-RM pair, budget value, and domain, AdaBoN uses only test-time Monte Carlo estimation and KDE with an automatic bandwidth selector. The paper evaluates all 12 LM-RM pairs with the same procedure and hyperparameters (d=0.75B), demonstrating genuine plug-and-play usability.

- **Latency-efficient two-stage design**: The paper explicitly motivates two-stage allocation by minimizing latency — only two serial calls to the base LM are needed (exploration, then batch generation after allocation). This is a principled design choice that respects real-world deployment constraints.

- **Performance scales with batch size**: Figure 3 shows average BWR increases monotonically as batch size K grows from 3 to 20 for all 12 LM-RM pairs. For some pairs (e.g., Qwen-Mistral), the gain exceeds 0.15 BWR. Table 14 shows that for Mistral with any RM, BWR > 0.50 rises to 100% of batches at K=20.

- **Robust to hyperparameter choice**: Table 3 (referenced in Section 4.3) shows that fixing d=0.75B incurs minimal drop in median BWR compared to tuning d ∈ {0.60B, 0.70B, 0.75B, 0.80B}. This reduces the tuning burden for practitioners.

## Weaknesses

### Fatal

None.

### Major

- **No empirical comparison with the most directly related prior work (Damani et al., 2024)**: The paper acknowledges that Damani et al. study the same allocation problem and lists them as the most closely related work, but provides no experimental comparison. The stated reasons (no existing implementation, computationally prohibitive at full scale) are legitimate, but the authors could have performed a reduced-scale comparison (e.g., 1–2 LM-RM pairs, one dataset, one budget). Without any head-to-head comparison, it is difficult for readers to assess whether AdaBoN's test-time-only approach offers practical advantages over the trained auxiliary model approach in the regime where both methods could plausibly apply. The paper's claim that Damani et al. "does not observe significant improvements for large inference budgets" (Section 1.1) partially mitigates this — since the two methods target different regimes (small-batch/large-budget vs. large-batch/small-budget), the absence of comparison is more justifiable than it first appears — but the gap remains.

### Minor

- **Modest effect sizes in a narrow regime**: Median BWRs of 0.54–0.62, while consistent, are not dramatic. The ESTs (~148–153 vs. B=120) suggest ~20–25% budget savings. More importantly, the exploration budget d=0.75B consumes 75% of total compute, meaning AdaBoN only reallocates the remaining 25% adaptively. This limits both the potential gain and practical efficiency improvement. The paper acknowledges this regime (K=5, B=120) is deliberately chosen, but the narrow operating range constrains the contribution's significance.

- **Computational overhead of Monte Carlo estimation not analyzed**: Line 4 of Algorithm 2 uses m=1024 MC samples per prompt per remainder value j to estimate V_{i,j}. The total is K × (B-d)K × m = 5 × 150 × 1024 ≈ 768K MC draws per batch. While cheap relative to LM calls, the paper omits any discussion of this overhead.

- **Limited sensitivity analysis of the KDE assumption**: The paper compares Gaussian KDE against MLE fits of Gaussian/Skew-Normal (Table 16 in Appendix K.3) and finds KDE performs best. However, there is no analysis of KDE's robustness to multimodal, heavy-tailed, or highly discrete reward distributions. The paper acknowledges this as a limitation (Section 5) but does not probe the boundary conditions where KDE might break down.

- **No discussion of RM overhead in inference budget**: The budget is counted purely in LM queries. Each LM call requires a subsequent RM call, and RM compute is non-negligible. While consistent within the paper's framing, this could mislead practitioners who care about total latency/compute.

### Trivial

- The EST computation caps the sum at 2B (noted in Section 4.3). This should be stated more prominently in the metric definition.

## Nice-to-Haves

- Reporting average reward improvement magnitude alongside win rate would help gauge practical significance. The BWR tells *how often* AdaBoN wins but not *by how much*.
- An ablation comparing AdaBoN against a simpler adaptive heuristic (e.g., allocate all remaining budget to the prompt with the highest sample maximum) would help isolate whether the KDE+greedy machinery is necessary.
- A histogram showing the distribution of per-prompt allocation differences vs. uniform would give insight into AdaBoN's behavior.

## Removed Points

These points were flagged for removal by the filtering rules. They are recorded here for completeness but should not carry weight in the evaluation.

- **"Two-stage uniform baseline needed"**: The critic argued that a two-stage uniform baseline is required to isolate adaptivity's effect. This is invalid — a two-stage procedure that explores with d samples then uniformly allocates remaining (B-d)K samples is mathematically equivalent to single-stage uniform with B samples per prompt (the max of 120 iid samples is the same regardless of when they are drawn). The improvement over single-stage uniform is thus correctly attributed to adaptive allocation.
- **"Latency claim overstated (second call not parallelizable)"**: The critic claimed the second LM call cannot be parallelized across prompts. This is factually incorrect — batches of samples with different allocation sizes per prompt can be parallelized simultaneously.
- **"Unspecified decoding parameters"**: The paper states "we use the standard generation function from Hugging Face, and thus use the default decoding strategy for all LMs." This is sufficient for a paper at this level.
- **"Only two-stage structure causes gains"**: See first point above.
- **Generic formatting/style nitpicks**: Not relevant.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a reduced-scale comparison with Damani et al. (2024)**: Even a single LM-RM pair, one dataset, and one budget value would significantly strengthen the evaluation. If the computational cost is truly prohibitive, clearly state this and provide an analytical comparison of the two methods' trade-offs.

2. **Add a two-stage uniform baseline**: Despite the mathematical equivalence argument above, adding an explicit two-stage uniform baseline would preempt the concern and make the evaluation airtight.

3. **Report an effect size metric alongside BWR**: The average difference in cumulative max reward (or a normalized version) would help readers gauge whether AdaBoN's wins are close or decisive.

4. **Analyze the computational overhead**: Include a brief runtime analysis showing that the KDE+MC+greedy steps are negligible compared to the LM call cost.

5. **Report standard errors in the main tables**: The box plots show distributions, but Table 1 and Table 2 would benefit from error bars or confidence intervals for the median BWR across batches.

## Score and Decision

Score calibration (all rounds):

| Round | Anchor ID | Avg Score | Comparison |
|-------|-----------|-----------|------------|
| R1 | RAs8XzpNzQ | 3.00 | A solvable model of inference-time scaling — purely theoretical, no LLM experiments. AdaBoN is substantially stronger. |
| R1 | JMmljf895g | 3.00 | Not-a-Bandit — different problem (drafter selection), lower relevance. |
| R1 | fZJvPuadUT | 4.00 | Optimal Stopping vs BoN — similar topic, clean theory but weaker empirical eval (fewer model pairs, missing baselines). AdaBoN is stronger. |
| R1 | a6CVQpjbXq | 4.80 | Best-of-Majority — strong theory but narrow empirical scope (math only). AdaBoN has broader empirical evaluation. |
| R1 | GqZYGOYuF2 | 5.50 | Zero-Overhead Introspection — adaptive test-time compute, similar quality level, different approach. Comparable. |
| R1 | qOyF214xmg | 8.00 | Transducing Language Models — unrelated topic, much higher tier. |
| R2 | ctspw4CqbS | 6.00 | Plan and Budget — more dramatic improvements, theory+practice. AdaBoN is slightly weaker due to modest effect sizes. |
| R2 | aC2ku2uKcB | 4.50 | Sequential Reward Filtering — interesting theory but concerns about assumptions. AdaBoN is stronger. |
| R2 | 5mGGqfDtbR | 4.50 | Multi-path reasoning on a budget — clean theory, modest empirical relevance. AdaBoN is stronger. |

Round-1 bracket: [4.5, 6.5]. Round-2 narrowing: the paper sits above anchors at 4.00–4.80 and below the anchor at 6.00, placing it at approximately 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>