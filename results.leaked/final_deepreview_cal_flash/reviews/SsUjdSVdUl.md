Now I have a comprehensive calibration picture. Let me write the final review.

## Round 1 Bracket (explicit): 5.5 – 7.0

## Round 2 Narrowing

All anchors consulted across both rounds:

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| uMxiGoczX1 (Data-Driven Creativity) | 2.50 | R1 | Much weaker than Critique-RL |
| zEhTnQZB3D (Continual RL) | 2.33 | R1 | Much weaker |
| FaOeBrlPst (Explainable Rewards in RLHF) | 3.00 | R1 | Weaker |
| 9LAqIWi3QG (R3HF) | 3.00 | R1 | Weaker |
| YW79lAHBUF (In-Context RL) | 3.75 | R1 | Weaker |
| xThb6APBoG (Adapting Retrieval Models) | 4.00 | R1 | Weaker |
| EvRZ68ObgW (Controlling Over-optimization) | 3.75 | R1 | Weaker |
| F0GNv13ojF (Designing Effective RL Reward) | 5.17 | R1+R2 | Weaker; Critique-RL has clearer contribution and stronger results |
| cK7yrw5g5Q (Segmenting Text Rewards) | 5.25 | R1 | Weaker; Critique-RL has better motivation and broader evaluation |
| JEehcb48Vp (Critic-CoT) | 5.75 | R2 | Weaker; Critique-RL has stronger empirical support and clearer diagnostic analysis |
| GtpubstM1D (Advancing Math Reasoning) | 5.71 | R2 | Different focus (pre-training data), less relevant |
| BGnm7Lo8oW (Learning to Reason at Scale) | 5.50 | R2 | Different focus |
| cijO0f8u35 (Scaling Relationship) | 5.25 | R2 | Different focus |
| Tn5B6Udq3E (Hidden Reasoning Process) | 6.00 | R2 | Different focus (analysis, not method) |
| 38E4yUbrgr (RL Contemplation) | 6.00 | R2 | Similar topic; Critique-RL is comparable in quality with stronger task-specific evaluation |
| uvZDQvjULn (Bi-objective CLM) | 6.00 | R2 | Different focus |
| Sx038qxjek (CRITIC tool) | 6.50 | R2 | Comparable rigor; Critique-RL has deeper problem diagnosis but tool-based approach is more broadly applicable |
| pNkOx3IVWI (UltraFeedback) | 6.25 | R3 | Different focus (data); Critique-RL has stronger technical contribution |
| gkfUvn0fLU (Constrained RLHF) | 7.00 | R3 | Stronger theoretical grounding than Critique-RL |
| d94x0gWTUX (Tool-Augmented RM) | 7.33 | R3 | Stronger overall than Critique-RL |

**Final determination:** Critique-RL sits between the 5.17–6.25 papers (which it surpasses in contribution clarity and experimental depth) and the 7.0+ papers (which have stronger theoretical or cross-domain contributions). It is most comparable to the 6.0–6.5 tier: a solid empirical paper with a clear, well-motivated contribution and minor but addressable weaknesses.

**Final score: 6.5 | Decision: Accept**

Now writing the review.## Summary

This paper proposes Critique-RL, a two-stage reinforcement learning approach for training language models to critique model outputs (assess correctness and provide helpful feedback) without relying on human-annotated critique data or a stronger supervisor model. The key insight is that single-stage RL with indirect reward signals (based on actor refinement correctness) optimizes helpfulness but fails to improve discriminability (accurately judging whether a response is correct or not), leading to conservative or aggressive failure modes. Critique-RL addresses this by first optimizing discriminability with a direct rule-based reward (Stage I), then optimizing helpfulness via actor-refinement rewards while maintaining discriminability through explicit regularization (Stage II). Experiments on mathematical reasoning tasks with Qwen2.5-3B and Qwen2.5-7B show consistent improvements over SFT, STaR, Retroformer, and CTRL baselines across in-domain and out-of-domain datasets, with gains of 4–9% on accuracy and 10–20 points on discrimination accuracy.

## Strengths

1. **Clear diagnosis of the discriminability bottleneck (§4.1, Figure 3).** The paper identifies a genuine and non-obvious failure mode: RL with indirect reward signals (r_refine, r_correction, r_Δ) improves helpfulness but systematically fails to optimize the critic's ability to discriminate correct from incorrect responses, causing either conservative (refusing to change answers) or aggressive (over-correcting correct answers) behavior. This empirical finding directly motivates the two-stage design and is a valuable standalone contribution.

2. **Consistent and substantial performance gains (Table 1).** Critique-RL outperforms all baselines across three datasets and two model scales on both accuracy and discrimination. For Qwen2.5-7B on MATH: 58.40% Acc vs. CTRL 53.86% (+4.54); on GSM8K: 87.72% vs. CTRL 81.35% (+6.37). The Acc@Dis improvements are even more pronounced (e.g., 85.20 vs. CTRL 71.42 on MATH-7B), directly supporting the claim that discriminability is being effectively optimized.

3. **Well-designed ablation study (Table 3) validates the two-stage structure.** Removing Stage I or Stage II causes measurable degradation on both MATH and AQuA. Removing the discrimination regularization from Stage II (r_dis + KL to Stage I) also significantly hurts performance, confirming that both stages and the discriminability maintenance mechanism are necessary.

4. **Generalization to out-of-domain tasks (Table 4) and multiple architectures (Appendix).** The method transfers to unseen SVAMP and TheoremQA datasets and is validated on Llama3.2 and DeepSeek-R1-Distill-Qwen-7B, demonstrating robustness beyond the primary evaluation setting.

5. **Oracle-verifier analysis (Figure 5) disentangles helpfulness from discriminability.** When an external verifier handles discrimination, Critique-RL still outperforms baselines, showing that Stage II's helpfulness optimization is genuinely effective and that the two abilities are synergistic rather than independent.

## Weaknesses

### Fatal

None.

### Major

1. **No controlled single-stage RLOO baseline in the main results table.** The main comparison (Table 1) pits Critique-RL (RLOO) against Retroformer (PPO) and CTRL (GRPO), conflating the reward design with the RL algorithm. While the preliminary experiments in §4.1 do compare RLOO-like single-stage variants (r_refine, r_correction, r_Δ) and show they underperform, these results are only reported for GSM8K with a 3B model and are not carried into Table 1. The "w/o Stage I" ablation in Table 3 is not a clean single-stage baseline, because Stage II's objective already includes r_dis and KL regularization. A dedicated RLOO + r_refine baseline in the main table would cleanly isolate the contribution of the two-stage design. Without it, the reader must look across two separate experiment blocks to piece together the evidence.

2. **No variance or statistical significance reporting.** All results appear to be from single runs with no standard deviations, confidence intervals, or multi-seed averages. RL training is notoriously noisy, and the paper's central claims about the superiority of the two-stage design would be substantially strengthened by reporting variance across at least 3 seeds for the main experiments and key ablations. The consistency of improvements across tasks is suggestive but not a substitute for proper uncertainty quantification.

### Minor

1. **Retroformer and CTRL baselines are underspecified.** The paper states that these baselines use PPO and GRPO respectively and "leverage[] indirect outcome-based reward," but does not clarify whether the original reward designs from those papers were faithfully reproduced, or whether they were adapted to the same indirect rewards (r_refine, etc.) used in §4.1. If the latter, then the comparison is primarily about algorithm choice, not reward structure. A brief description of the reward functions used for each baseline would resolve this ambiguity.

2. **β₂ hyperparameter unreported.** In Stage II, β₁ is set to 0.2 (stated), but β₂ (the KL coefficient to the Stage I model) is not reported. The paper only mentions a "KL coefficient to 0.01" for general RL baselines. Since β₂ controls how aggressively the model can deviate from the discriminability-optimized Stage I policy, its value is important for reproducibility and understanding the method's sensitivity.

3. **Ablation limited to one model scale.** The ablation study (Table 3) is conducted only on Qwen2.5-3B with two tasks. While the results are internally consistent, ablations at the 7B scale would increase confidence that the two-stage structure remains beneficial as model capacity grows.

### Trivial

1. **RL algorithm not stated in §4.1.** The preliminary experiments use a generic "policy gradient" objective (Eq. 3) without specifying whether RLOO, REINFORCE, or another variant was used. The RLOO mention only appears in §5.1. Stating the algorithm earlier would help reproducibility.

2. **The "without stronger labeling" framing in the abstract could be slightly sharpened.** The method does not require human critique annotations, but still depends on an initial SFT dataset generated by a stronger instruct model (Qwen2.5-3B-Instruct) and on oracle correctness signals for the reward. This is transparently described in the paper but the abstract's phrasing could give a subtly different impression.

## Nice-to-Haves

- A brief discussion of the limitation that the reward signal depends on the availability of a verifier (oracle answer for math, learned reward model for open-ended tasks) would improve balance.
- Exploring sensitivity of the method to β₁ and β₂ (the two key hyperparameters in Stage II) would help practitioners apply the method.
- The iterative training results (Table 2) are interesting, but it would strengthen the paper to note whether the same iterative procedure was applied to the baselines, or to clarify that the comparison is specifically about how Critique-RL benefits from iteration.

## Removed Points

These points from the harsh critic were identified during verification and removed for the following reasons:

- **"Uncontrolled comparison of RL algorithms" (as a fatal confound):** The paper partially addresses this concern through the §4.1 preliminary experiments (Figure 3), which directly compare RLOO-like single-stage variants and show they underperform. The ablation in Table 3 further decomposes the contribution of each stage within the same algorithm. The remaining concern (that these are not in the main table) is captured in Major weakness #1.
- **"Introduction framing about 'without stronger labeling'":** The paper is transparent about using Qwen2.5-3B-Instruct for SFT data and oracle verifiers. This is a minor clarity issue, not a substantive weakness.
- **"Iterative training not applied to baselines":** The paper presents iterative training as a property of Critique-RL, not as a comparative claim against baselines. This is a nice-to-have enhancement, not a flaw in the evaluation.
- **"Paper does not discuss limitation that reward signal depends on verifier":** This is a valid observation but more of a completeness suggestion than a weakness; captured in Nice-to-Haves.
- Generic concerns from the Strength Finder about "the problem being important" — removed as generic/superficial. All retained strengths are concrete and grounded in specific evidence from the paper.

## Novel Insights

The reviews converge on a key observation that goes beyond the paper's own claims: the failure mode analysis in §4.1 (where indirect rewards fail to optimize discriminability, causing bifurcation into conservative or aggressive critique styles) provides a generalizable insight about RL for two-player interaction frameworks. This suggests that any method that optimizes critique models solely through downstream task reward (actor refinement accuracy) will inherit this discriminability bottleneck, and that the two-stage decoupling strategy may generalize to other multi-agent RL settings beyond the specific LLM critiquing application studied here.

## Suggestions

1. **Add an RLOO + r_refine baseline to Table 1** to directly isolate the effect of the two-stage reward design from the algorithm choice. If the improvement over this baseline is consistent, the argument for the two-stage approach is substantially cleaner.
2. **Report main results with at least 3 random seeds**, or provide a brief discussion of observed variance if single-seed reporting is a practical constraint.
3. **Report the value of β₂** and, if possible, a small sensitivity analysis to show how robust the method is to this hyperparameter.
4. **Clarify the Retroformer and CTRL implementations** — specifically, whether the original reward functions from those papers were used or whether they were replaced with the indirect rewards (r_refine, etc.) studied in §4.1.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>