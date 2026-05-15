I've now read the paper thoroughly and cross-checked every claim from both reviewers against the paper. Let me now produce the consolidated review.

---

## Summary

Critique-RL proposes a two-stage online RL method for training language models to critique and refine outputs without requiring a stronger supervisor. The key insight — supported by training dynamics analysis — is that indirect outcome-based rewards alone fail to build discriminative critics (they become overly conservative or aggressive). The solution decouples the problem: Stage I explicitly optimizes discriminability via direct rule-based rewards, and Stage II introduces refinement rewards while preserving discriminability through an auxiliary reward and KL regularization. Experiments across multiple model scales (3B–7B) and math reasoning tasks demonstrate consistent improvements over existing RL-based critic training methods (Retroformer, CTRL) with strong OOD generalization.

---

## Strengths

- **Clear diagnostic contribution (Figure 3 / §4.1):** The paper provides a well-executed training dynamics analysis showing that indirect reward signals (r_refine, r_Δ, r_correction) produce critics that optimize either helpfulness or conservatism but fail to develop discriminability, leading to a training bottleneck. The visualization of Acc@Dis stagnating or collapsing while helpfulness metrics improve is a genuine empirical insight that motivates the two-stage design.

- **Principled two-stage solution with strong ablations (Table 3):** The decoupling of discriminability (Stage I) and helpfulness (Stage II) is conceptually clean and directly addresses the diagnosed failure modes. The ablation study confirms that removing Stage I, removing Stage II, or removing the discrimination-aware regularization in Stage II all cause performance drops, demonstrating that both stages and the regularization are necessary.

- **Comprehensive and consistent empirical results (Table 1, Table 4):** On Qwen2.5-7B MATH, Critique-RL achieves 58.40% Acc@Refine and 85.20% Acc@Dis, outperforming CTRL (53.86%, 71.42%) and Retroformer (52.34%, 68.03%). Gains persist across three in-domain datasets, two OOD datasets (SVAMP, TheoremQA), and multiple model scales (3B, 7B). The OOD generalization without additional fine-tuning is a meaningful demonstration of the method's robustness.

- **Practical utility demonstrated through multiple lenses:** The paper validates the method's value through iterative refinement (Figure 4), iterative training (Table 2), inference-time compute scaling (Figure 1 right), and oracle-verifier analysis (Figure 5), showing the critic is useful across several real-world deployment scenarios.

---

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Algorithm confound weakens the headline comparison (Table 1):** Critique-RL uses RLOO as its base RL algorithm, while Retroformer uses PPO and CTRL uses GRPO. Because these RL algorithms can differ in stability, sample efficiency, and final performance, it is unclear how much of the observed gain over baselines stems from the two-stage reward design versus the choice of base RL algorithm. The paper partially mitigates this concern: Figure 3 compares different reward formulations under the *same* policy-gradient algorithm, and the ablation study (Table 3) varies reward designs within a fixed framework. However, the main comparison in Table 1 — which the paper's central claims rest on — does not control for algorithm choice. A fairer comparison would run Retroformer and CTRL's reward designs using RLOO, or report Critique-RL using the baselines' native algorithms.

- **Motivating claim in §4.1 is slightly overstated given limited evidence:** The paper concludes that indirect reward signals "cannot develop effective critique models" based on a single model (Qwen2.5-3B), a single dataset (GSM8K), 500 training steps, and a specific KL penalty. The baselines in Table 1 (Retroformer, CTRL) *do* achieve meaningful improvements over the No Critic baseline using indirect rewards — just not as much as Critique-RL. The claim would be better stated as "indirect rewards alone lead to suboptimal discriminability and limit final performance" rather than suggesting they categorically fail.

- **Iterative training protocol is underspecified (§5.3, Table 2):** The paper states that iterative training involves alternately conducting Stages I and II again, but does not specify whether the actor model is updated between iterations, how the RL dataset changes across iterations, or what "Iteration 2, Stage I" concretely entails (e.g., does it restart from the SFT checkpoint, or build on Iteration 1 Stage II?). This makes the iterative training result difficult to interpret or reproduce.

### Trivial

- The training dynamics in Figure 3 show only 500 steps on a single dataset/model combination. While sufficient to illustrate the failure modes, the analysis does not address whether baseline curves would eventually recover under longer training or different KL tuning.

---

## Nice-to-Haves

- A baseline that runs RLOO with the best indirect reward (e.g., r_refine) from the SFT initialization would isolate the effect of the two-stage design from the RL algorithm choice. This could be added in a rebuttal.

- Confidence intervals or bootstrap-based significance tests for the main accuracy numbers would strengthen confidence in margins as small as 1–2 percentage points, though this is not standard practice in LLM benchmarking.

- A direct comparison of a single-stage RL variant that combines r_refine and r_dis from the start (with the same KL penalty) versus the two-stage approach would quantify the benefit of staging rather than assuming it is necessary. The ablation "Stage II w/o discrimination" partially addresses this, but a clean single-stage variant with both rewards simultaneously would be more informative.

- Analysis of the parsing function f(x,y,c): how often does the critic's output fail to parse, and could parsing errors affect discriminability metrics?

---

## Removed Points

The following points from the reviewers were considered and removed:

- **Abstract "misleading" about gain percentages:** The abstract reports gains of 9.02% and 5.70%. The harsh critic noted these are relative to "No Critic" rather than the strongest baseline. The paper also states Critique-RL outperforms baselines, and the abstract does not claim these gains are relative to baselines. Reporting improvement over a no-critic baseline is standard practice. **Removed as a nitpick.**

- **Compute-scaling equivalence insufficiently explained:** The paper states in §6 that "performing K× response-critique-refinement sampling is more compute-efficient than conducting 3K× parallel sampling responses." This is brief but adequate given that the main contribution is the training method, not the inference scaling analysis. **Removed as a trivial presentation point.**

- **Oracle verifier analysis is speculative:** The paper states that "the optimization of discriminability in our method also implicitly contributes to the improvement of helpfulness." This is a reasonable interpretation supported by Figure 5 data showing Critique-RL outperforms baselines even when an oracle verifier is provided. **Removed — not a weakness; the paper appropriately presents this as an interpretation, not a proven claim.**

- **No variance estimates/significance tests:** The harsh critic noted the absence of statistical tests. This is standard in the field for LLM benchmark evaluations; many anchor papers at the same venues lack them. **Moved to Nice-to-Haves.**

- **Missing baselines (RLOO with indirect rewards, single-stage combined rewards):** These are reasonable suggestions but go beyond what is needed to support the paper's claims, given the existing ablation study. **Moved to Nice-to-Haves.**

---

## Novel Insights

Beyond the paper's own contributions, the review process highlights an important methodological consideration for this line of work: the interaction between RL algorithm choice and reward design creates a confound that makes it difficult to attribute performance gains solely to the reward structure. This is a broader issue in the RL-for-LLMs literature — as different papers adopt different base algorithms (PPO, GRPO, RLOO, REINFORCE, etc.), cross-paper comparisons become harder to interpret. The field would benefit from standardized evaluation protocols where reward designs are evaluated under a common algorithmic backbone.

---

## Suggestions

- For the camera-ready version, clarify the iterative training protocol in §5.3: state whether the actor is fixed or updated between iterations, and specify how the RL dataset is constructed for Iteration 2.
- Soften the language in §4.1 and the abstract from "cannot develop effective critique models" to "lead to suboptimal discriminability" to better align with the full evidence.
- If feasible within the rebuttal period, run one additional experiment: Retroformer/CTRL reward designs using RLOO as the base algorithm, to demonstrate that the two-stage reward design benefits hold even when algorithm choice is controlled. Even reporting this for one model/dataset would address the most significant remaining concern.

---

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Decision | Comparison to Critique-RL |
|---|---|---|---|
| Critique-Coder (tsuxIeLUsz) | 5.50 | Accept (Poster) | Similar domain (RL for critique training, code). Critique-RL has a stronger diagnostic contribution, more comprehensive evaluation (OOD, iterative, multiple scales), and cleaner two-stage design. Critique-RL is slightly stronger. |
| RFTT (lHbhzxiVI9) | 5.00 | Accept (Poster) | Two-phase RL with functional tokens for math reasoning. Well-executed but limited baselines. Critique-RL has stronger diagnostics, ablations, and more comprehensive evaluation. Comparable or slightly stronger. |
| RefCritic (qgMvotqkXd) | 4.00 | Reject | Very similar approach (dual reward for critic: correctness + refinement). Critique-RL has clearer two-stage decoupling, more thorough ablations, OOD evaluation, and iterative training results. Clearly stronger. |
| DeepCritic (wyCnT4BUsT) | 4.67 | Reject | Two-stage critic training (SFT+RL). Critique-RL uses RL in both stages and provides a diagnostic of *why* two stages are needed (discriminability collapse). Critique-RL is stronger. |
| Critique-GRPO (5FzN1nM20e) | 4.50 | Reject | Integrates critique into GRPO for self-refinement. Qwen-only, incremental novelty. Critique-RL has a more principled decoupling of discriminability/helpfulness and broader evaluation. Clearly stronger. |
| Mirror-Critique (he7BMZwm8t) | 3.00 | Withdrawn/Reject | SFT+RLVR for verifier training. Many methodology and presentation issues. Critique-RL is substantially stronger across all dimensions. |
| Zero Rewards (Fuhmh86Ckv) | 2.50 | Withdrawn/Reject | Single task, single model, very narrow. Not comparable in scope or quality. |

Critique-RL is clearly stronger than the rejected papers in this space (RefCritic, DeepCritic, Critique-GRPO, Mirror-Critique) and comparable to or slightly stronger than the accepted posters (Critique-Coder, RFTT). The paper makes a genuine contribution — a clear diagnostic finding and a principled solution — supported by comprehensive experiments. The remaining weaknesses (algorithm confound, slightly overstated claims, underspecified iterative protocol) are addressable and do not threaten the core contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>