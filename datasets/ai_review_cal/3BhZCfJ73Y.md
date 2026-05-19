- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8
Now I have everything I need. Let me synthesize the final review.

## Summary

This paper introduces Adaptive Prompt-Tailored Pruning (APTP), the first prompt-based pruning method for text-to-image (T2I) diffusion models. APTP learns a prompt router and a set of architecture codes that allocate different computational capacity to different prompts, enabling per-prompt specialization while preserving batch parallelism on GPUs. The prompt router is trained using contrastive learning and optimal transport to prevent code collapse. Experiments on Stable Diffusion V2.1 with CC3M and COCO target datasets show that APTP outperforms a weight-norm pruning baseline at similar or lower compute budgets, and the learned expert routing exhibits semantically meaningful specialization (e.g., harder prompts like text/humans get routed to higher-capacity experts).

## Strengths

1. **First prompt-based pruning framework for T2I that preserves batch parallelism.** The paper introduces a genuinely novel formulation: dynamic per-prompt capacity allocation without sacrificing GPU batch processing. The contrastive learning + optimal transport framework is technically sound, and the design choice of applying contrastive loss to the Gumbel-sigmoid outputs (e') rather than raw embeddings is well-motivated (lines 163–166).

2. **Consistent quantitative gains over the weight-norm pruning baseline.** APTP outperforms weight-norm pruning across two target datasets (CC3M and COCO) and two budget levels on FID, CLIP, and CMMD. On CC3M, APTP (0.66 MACs) uses 21% fewer MACs than the Norm baseline while showing "a large gap" in all metrics (Section 4.1). On COCO, APTP (0.78) reduces latency by 22.5% while preserving CLIP score and outperforming Norm pruning at similar cost.

3. **Semantically meaningful expert specialization.** Analysis of the prompt router's assignments (Section 4.2) reveals that different experts specialize in distinct topics (cityscapes, animals, interiors). Critically, the highest-capacity expert receives prompts involving text and humans — categories empirically known to be challenging for SD 2.1 — demonstrating that APTP automatically discovers harder inputs and allocates more compute to them.

4. **Ablation study validates each component.** The component ablation (Table 4, Section 4.3) cleanly shows: contrastive learning alone fails (code collapse), adding optimal transport dramatically improves FID (to 10.22), and distillation further refines performance. This provides clear evidence that all proposed design choices are necessary.

5. **Optimal transport formulation prevents code collapse.** The paper identifies a key failure mode (all architecture codes collapsing to one) and solves it with an equipartition-constrained optimal transport assignment (Eq. 7–9). The ablation confirms that without OT, the router assigns most prompts to a single expert, degrading quality.

## Weaknesses

### Fatal

None.

### Major

1. **Baseline comparison is insufficient to fully support the central claim.** The paper argues that prompt-based pruning is more suitable than static pruning for T2I models, yet the only static pruning baseline is weight-norm pruning (Li et al., 2017) — a generic technique from the CNN pruning literature. The paper itself discusses SPDM (Fang et al., 2023) in related work as a structural pruning method specifically designed for diffusion models (line 42), but does not compare against it. Without at least one diffusion-specific pruning baseline, the reader cannot determine whether APTP's gains stem from its prompt-based allocation mechanism or simply from using a more sophisticated pruning procedure than the simple weight-norm baseline. This directly weakens support for the paper's central thesis that "prompt-based pruning outperforms static pruning for T2I models."

2. **Training cost is not reported, undermining the practical motivation.** The paper frames APTP for "resource-constrained organizations" (Sections 1, 3) that fine-tune on proprietary target data before deployment. Yet it provides no information about the computational cost of the pruning stage itself (GPU-hours, iteration count for the pruning phase, wall-clock time). APTP requires joint training of the prompt router, architecture codes, and sub-networks using the denoising objective — this constitutes non-trivial overhead. Without knowing this cost, a practitioner cannot assess whether APTP is actually more practical than fine-tuning a static pruned model.

### Minor

1. **No error bars or variance reported.** All metrics (FID, CLIP, CMMD) are reported as single numbers. Given that the pruning process involves Gumbel noise and stochastic optimization, reporting variance across seeds is necessary to assess whether the observed improvements are reliable. This is a common standard in ML evaluation.

2. **Missing implementation details for reproducibility.** Several details are absent: (a) the specific Sentence Transformer variant used (only "pretrained frozen Sentence Transformer model" is stated, line 71); (b) the architecture (dimensions, layers) of the architecture predictor; (c) the numerical value of the Gumbel temperature γ (only "set appropriately," line 126); (d) the numerical value of the optimal transport regularization strength ε (only "set to a small value," line 97). These details matter for reproducing the results.

3. **Hyperparameter sensitivity not explored.** APTP introduces four hyperparameters (N, λ_cont, λ_res, λ_distill) plus the number of experts. Only one value is reported for each. The number-of-experts ablation (Section 4.3) is a good start, but sensitivity to the loss weights (especially λ_cont = 100, which is large) is not examined.

4. **Test-time distribution shift not discussed.** During inference, the router switches from optimal transport to cosine similarity (line 115). Since the equipartition constraint is only enforced during training, a skewed test-time prompt distribution could cause the actual compute budget to deviate substantially from the target T_d. This is a real limitation worth acknowledging.

### Trivial

1. **No dedicated limitations section.** The paper lacks a limitations paragraph. While the Conclusion summarizes contributions, important limitations (test-time budget deviation on skewed distributions, training overhead, dependence on prompt diversity in the target dataset) are not explicitly acknowledged.

## Nice-to-Haves

- A comparison to SPDM (or another diffusion-specific static pruning method) would substantially strengthen the paper's central claim.
- Convergence curves comparing APTP and the baseline would clarify the training efficiency.
- Reporting GPU-hours for the pruning + fine-tuning stages would help practitioners assess practicality.
- An ablation of the contrastive loss applied to e vs. e' (to justify the design choice \S 3.2.2) would add methodological depth but is not essential.

## Removed Points

- **"BK-SDM should be compared"**: BK-SDM is an architecture design method (block removal + distillation for a one-size-fits-all architecture), not a pruning method that operates on arbitrary target datasets. The paper's setting (pruning a pretrained model on a target dataset) is fundamentally different from BK-SDM's approach, making this comparison not directly applicable. Removed as scope creep.

- **"Comparison is not iteration-matched (30k vs 50k)"**: The paper states "APTP and Norm pruning reach their final performance after about 30k and 50k iterations" — meaning both were trained to convergence and evaluated at their respective best points. APTP converging faster is a strength, not a weakness. Removed as it misunderstands the paper.

- **"The gap between APTP and weight-norm pruning could largely reflect the weakness of the baseline"**: This is speculative framing. The underlying concern (limited baselines) is retained as Major weakness #1, but the speculative conclusion is removed.

- **"Missing appendix content / proofs"**: The parser strips appendices; these exist in the original submission. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any novel perspective that the paper itself does not articulate.

## Suggestions

1. Compare against at least one diffusion-specific static pruning method, such as SPDM (Fang et al., 2023), to substantiate the claim that prompt-based pruning improves over static pruning for T2I models.
2. Report the training cost (GPU-hours for the pruning + fine-tuning stages) and clarify the practical regime in which APTP is advantageous.
3. Add error bars (or results across multiple seeds) for the main comparison tables and the ablation study.
4. Specify the missing implementation details: Sentence Transformer variant, architecture predictor dimensions, Gumbel temperature γ, and OT regularization strength ε.
5. Add a brief limitations discussion addressing test-time budget deviation on skewed prompt distributions, training overhead, and sensitivity to target dataset diversity.
