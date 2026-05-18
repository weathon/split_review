Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual content. Let me compose the final review.

## Summary

This paper proposes TC-MoE, which expands the MoE expert space by multiplying each original expert with the ternary set {−1,0,1}, creating three variants: the original (E¹), the negated output (E⁻¹), and a zero-output expert (E⁰). This expansion requires only router-level overhead (growing from N to 2N+K experts in the router). The paper also introduces custom load-balancing and reward losses suited to the expanded space. Experiments on 100B-token pretraining show ~0.8–1.2% average accuracy improvements over Top-K baselines while reducing activated expert counts by ~7–9%.

## Strengths

1. **Novel and well-motivated idea.** The ternary expert expansion is conceptually clean. The paper identifies two genuine limitations of Top-K routing (unnecessary activations, lack of negative weights) and provides empirical evidence for both in Figure 1. The proposed mechanism addresses both simultaneously without modifying the routing algorithm itself — a different approach from prior work on routing modification.

2. **Ablation study confirms component contributions.** Table 3 explicitly decomposes the method: {0,1} alone (+0.52% accuracy, −0.19 activated experts), {−1,1} alone (+0.29%, no efficiency gain), and the full {−1,0,1} achieving the best overall results. This demonstrates that both E⁻¹ (improving accuracy via negative weights) and E⁰ (improving efficiency via zero-cost skips) contribute meaningfully, and that the full ternary set outperforms either subset.

3. **Consistent results across multiple settings.** Improvements are demonstrated on two datasets (RedPajama, FineWeb), three model scales (tiny, base, fine-grained base), and nine evaluation benchmarks. The budget-controlled comparison (Figure 3) shows TC-MoE consistently outperforming Random drop and Top-P across different activation budgets, not just at one operating point.

4. **Insightful analysis of learned router behavior.** Figures 6 and 8 show that the model spontaneously learns interpretable patterns — E⁰ activated more in shallow layers, E⁻¹ more in deeper layers — with stable ratios across training. This provides evidence that the router genuinely leverages the expanded space in a structured way rather than learning trivial patterns.

## Weaknesses

### Fatal
None.

### Major

1. **No variance estimates or multiple runs.** All results in Table 1 are single-point estimates. The reported improvements (0.7–1.2% average accuracy) are modest, and for 100B-token training runs, run-to-run variance could be non-negligible. Without standard deviations or multiple seeds, it is difficult to assess whether the observed differences are statistically significant. This is the single most consequential weakness in the evaluation.

### Minor

2. **Missing standard training configuration details.** The paper does not report batch size, learning rate schedule, optimizer, warmup steps, or total number of training steps. While the architecture is specified (Table 2), the training setup is only partly described ("100B tokens on RedPajama/FineWeb"). These are standard details that aid reproducibility.

3. **No sensitivity analysis for the reward factor α₂.** The reward loss (controlled by hyperparameter α₂) is a key component for the efficiency-effectiveness trade-off. The paper does not sweep α₂ or analyze how sensitive results are to this choice. A brief sweep (e.g., Table 1 results for a few α₂ values with corresponding accuracy and activated expert counts) would demonstrate that the trade-off is controllable and not brittle.

4. **Reward loss interaction with load balance loss is not analyzed.** The paper introduces two auxiliary losses (ℒ_{aux} and ℒ_{rwd}) but does not discuss how they interact. Since ℒ_{rwd} explicitly promotes E⁰ activation while ℒ_{aux} ignores E⁰, there could be regimes where the reward loss dominates and degrades task performance, or where the load balance loss counteracts the reward loss. A brief discussion or empirical check would strengthen the method section.

5. **Router computational cost claimed but not quantified.** The paper states the extra routing cost is "negligible compared to the overall computational cost of the MoE block" but provides no FLOPs breakdown. For the fine-grained model with N=64 and K=4, the router logit matrix grows from 64×d to (2×64+K)×d = 132×d. A brief numerical comparison (e.g., router FLOPs as a fraction of total MoE FLOPs) would ground this claim.

6. **Load balance deviation on out-of-distribution data not discussed.** Figure 7 shows near-perfect balance on pretraining data but a noticeable spread on ARC-Easy (8.5%–15%). The paper calls this a "slight deviation" but does not discuss whether this would be problematic for distributed inference or whether the load balance loss generalizes poorly to distribution shift.

### Trivial
None.

## Nice-to-Haves

- **Comparing against Expert Choice routing** (Zhou et al., 2022) as an additional efficiency-oriented baseline would be informative. However, TC-MoE is framed as an *expert space expansion* method that keeps the routing algorithm unchanged, whereas Expert Choice modifies the routing mechanism. These are orthogonal approaches, so the omission is not a fatal gap. A comparison would strengthen claims of overall efficiency but is not required to validate the core contribution.
- **A control experiment** that forces a zero-cost placeholder expert without the ternary expansion (to isolate the effect of E⁻¹ beyond the forced E⁰ trick) would further cleanly separate the contributions of the two expert types. The existing ablation (Table 3) partially addresses this by comparing {0,1} vs {−1,0,1}, but a direct control would be tighter.
- **Analysis of when E⁻¹ helps vs. hurts** — e.g., what fraction of E⁻¹ activations yield larger positive contributions than the corresponding E¹ would have provided.

## Removed Points

These points from the input reviews were evaluated against the paper and removed:

1. **"Missing the most relevant baseline: Expert Choice routing" (framed as fatal/critical)** — The paper explicitly states its contribution is orthogonal to routing-modification methods: *"Unlike previous studies...that focus on modifying the routing scheme, we explore an alternative direction by expanding the expert space."* TC-MoE keeps Top-K routing and expands the expert space; Expert Choice keeps the expert space and changes routing. Comparing against it would be informative but is not required to validate the paper's core claim. Demoted to Nice-to-Have.

2. **"Eq. 7 load balance loss uses 1/(KT)" (framed as a technical concern)** — The formula uses a normalization that differs from some prior work (e.g., Switch Transformer). However, different MoE implementations use different normalizations, and the paper does not claim to follow any specific prior convention. This is a stylistic/design choice, not an error. Removed.

3. **"Missing layer count for Base model"** — Table 2 (an image in the paper) likely provides this information. The parser strips images, so this is an artifact of the review format, not a paper omission.

4. **Criticisms about baselines not being "carefully optimized" or hyperparameters not being tuned per task** — This is speculative; there is no evidence in the paper that baselines were poorly tuned.

5. **"Figures 4/5 add limited new insight"** — This is a subjective opinion rather than a weakness. The figures directly support the claim about alleviating unnecessary activations.

6. **Strength Finder claims about the paper addressing an "important problem" or having "clear motivation"** — These are generic/superficial strengths without specific concrete evidence tied to the paper's content. Removed.

## Novel Insights

The most interesting finding across the reviews is that the harsh critic's central concern (missing Expert Choice baseline) is largely a scope mismatch: the critic evaluates the paper as a routing-improvement method, but the paper's actual contribution is an *expert space expansion* that keeps the routing algorithm fixed. The ablation study (Table 3) serves as a partial counterargument — it shows that even {−1,1} alone (which changes nothing about routing or efficiency) yields +0.29% accuracy, confirming that the ternary expansion itself provides value independent of the efficiency gains from E⁰. This distinction is important: TC-MoE's primary novelty is in providing the router with a richer action space through parameter-sharing expert variants, not in designing a new routing algorithm. The evaluation should be judged against this framing.

## Suggestions

1. **Report variance.** At minimum, run 3 seeds for the primary comparison (base model on RedPajama) and report mean ± std. If computational constraints make multi-seed runs infeasible at 100B tokens, state this explicitly and note it as a limitation.
2. **Add a sensitivity sweep for α₂** showing how accuracy and average activated experts vary across a range of reward factor values.
3. **Include standard training configuration details** in the experimental setup (batch size, LR schedule, optimizer, number of steps).
4. **Provide a FLOPs breakdown** of the router vs. expert FFN computation to quantify the "negligible" overhead claim.
5. **Add a brief discussion** of the interaction between ℒ_{aux} and ℒ_{rwd}, and the out-of-distribution load balance behavior observed on ARC-Easy.

## Score and Decision

This paper presents a novel, well-motivated, and clearly explained idea. The core contribution — expanding the expert space through ternary multiplication — is technically sound and the method is lightweight. The ablation study effectively decomposes the contributions of each expert type. The main weakness is the lack of variance estimates, which makes the modest reported improvements harder to assess. The paper would be strengthened by addressing the minor issues above, but the core contribution is valid and the evidence is directionally consistent across multiple settings.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>