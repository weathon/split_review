Here is my final consolidated review.

---

## Summary

The paper proposes **LoRA-Mixer**, a framework that places mixture-of-experts LoRA adapters on the attention/SSM projection layers (Q, K, V) rather than on the FFN layers, and introduces a **Routing Specialization Loss (RSL)** that combines a load-balancing auxiliary loss with an entropy regularization term. The framework supports joint training of adapters and routers, as well as plug-and-play routing over frozen, publicly-sourced LoRA modules. Experiments across 15 benchmarks and three base model architectures (LLaMA3-8B, Mistral-7B, Falcon-Mamba-7B) show consistent improvements over baselines including MoLE, MixLoRA, and LoRAHub.

## Strengths

1. **Consistent performance gains across diverse architectures and tasks (Table 2)**: LoRA-Mixer outperforms strong baselines on nearly all 7 benchmarks × 3 base models (LLaMA3-8B, Mistral-7B, Falcon-Mamba-7B). Gains are meaningful (e.g., +3.79% GSM8K, +2.90% CoLA, +3.95% ARC-C on LLaMA3-8B over the best baseline). The inclusion of Falcon-Mamba (a pure SSM architecture) demonstrates the method's architecture-agnostic design.

2. **Plug-and-play reuse of public LoRA modules (Table 3)**: Using five LoRAs downloaded from LoRAHub with only 2K additional training samples for the router, LoRA-Mixer on Flan-T5 outperforms a single LoRA on four of five GLUE tasks. This is a practically relevant capability.

3. **Cross-model transferability (Table 5)**: Routing parameters trained on Mistral-7B transfer to LLaMA3-8B without any fine-tuning, improving GSM8K (0-shot: 59.13 vs. 57.92) and ARC-C (79.14 vs. 78.65). This validates the claim that routing learned via RSL captures input semantics in a model-agnostic way.

4. **Data efficiency of RSL (Table 9)**: At 2K training samples, RSL outperforms the standard auxiliary loss by +1.97 points (79.26 vs. 77.29). The gap persists (though narrows) at 8K and 10K, supporting the claim that the loss helps in low-data regimes.

5. **Input-aware specialization visualization (Figure 4)**: The expert activation heatmaps clearly show that RSL produces differentiated per-task expert activations (e.g., Expert 2 activated ~38% on GSM8K vs. ~15% on Medical), while the auxiliary loss alone produces near-uniform activation.

## Weaknesses

### Fatal
None.

### Major

1. **RSL sign inconsistency (Section 3.3, Eq. 5 vs. textual description)**: The RSL loss is defined as $\mathcal{L}_{\text{RSL}} = \alpha \sum \bar{p}_i \bar{f}_i - \lambda \mathbb{E}[\mathcal{H}(p(x))]$. The entropy term is subtracted. Since $\mathcal{H}(p) = -\sum p_i \log p_i \geq 0$, minimizing this loss *maximizes* $\mathcal{H}$ (making routing distributions more uniform), which is the opposite of promoting specialization. Yet the text repeatedly claims that RSL "suppresses overly flat distributions," that "minimizing $\mathcal{H}(p(x))$ reduces token-conditional uncertainty," and that RSL "promotes expert differentiation." The gradient derivation in Eq. (9) is internally consistent with Eq. (5), so the math is coherent with itself — but the textual interpretation contradicts the math. This is not a trivial typo: the paper's central theoretical claim about what RSL does cannot be evaluated from the current text. The empirical results (Figure 4) show that RSL does produce more peaked distributions than the auxiliary loss alone, suggesting the implementation may use $+\lambda \mathcal{H}$ (which would match the text). The authors must clarify the intended sign, correct the equations if needed, and explain how the stated loss produces the observed behavior. *This is the single most significant weakness and must be resolved for the paper to be assessable.*

### Minor

2. **Missing ablation of expert placement (projection vs. FFN)**: The paper claims that placing LoRA experts on projection layers is better than placing them on FFN layers (the standard practice in prior LoRA-MoE work). However, there is no controlled ablation comparing otherwise identical setups where experts are placed on projection layers vs. FFN layers under the same RSL loss. The baselines (MoLE, MixLoRA) use different losses and architectures, so the contribution of placement alone cannot be isolated.

3. **No parameter counts in the main text**: The abstract and introduction prominently claim that LoRA-Mixer uses "48% of the trainable parameters of existing methods," but the main text contains no table or calculation of parameter counts for any method. The only reference is to Appendix A.4 (stripped by the parser). A headline quantitative claim should be verifiable from the main text itself.

4. **Several performance degradations are under-discussed**: (a) Table 3: LoRA-Mixer underperforms simple LoRA on QQP (84.75 vs. 85.55) with no discussion. (b) Table 4: LoRA-Mixer drops 10.38 points on RTE compared to LoRA-LEGO (61.47 vs. 71.85), which is a severe degradation on a specific task. The paper's claim of "outperforms on three of four tasks" is technically correct but obscures this failure. (c) Table 5: The transferred LoRA-Mixer drops 2.56 points on ARC-E compared to the base LLaMA3-8B (85.89 vs. 88.45). Acknowledging these patterns would strengthen the paper's credibility.

5. **No statistical significance reported**: All experiments are run three times with the average reported, but no standard deviations or confidence intervals are provided. Given the modest gaps in some comparisons (e.g., Table 9 at 8K: 79.75 vs. 79.48, gap of 0.27), it is unclear which differences are meaningful.

6. **RSL ablation shows inconsistent benefit at larger data sizes (Table 9)**: At 4K data, w/o RSL (79.14) outperforms w/ RSL (78.77). At 6K, the gap is essentially zero (79.41 vs 79.37). The paper defers explanation to Appendix A.16. While the low-data benefit is clear, the claim that RSL remains beneficial at scale is weakly supported.

### Trivial
None.

## Nice-to-Haves

- **Computational overhead analysis**: Adding experts to every projection layer increases per-token compute even with sparse top-K activation. Reporting FLOPs or inference latency relative to baselines would improve the paper.
- **Expert granularity analysis**: How does performance change with the number of experts per layer? Do different layers benefit from different numbers of experts?
- **Cross-model transfer expansion**: The current experiment (Mistral→LLaMA3, 3 tasks) is narrow. Additional source-target pairs would strengthen the transferability claim.

## Removed Points

- **"Parameter efficiency claim is unsubstantiated because Appendix A.4 is stripped"**: The instructions note that the parser strips appendix content from all papers; the parameter counts exist in the original submission. However, the separate criticism (weakness #3 above) that the main text itself lacks parameter counts is valid and retained.
- **"The comparison with GMoE/DS-MoE/AESL is confounded by L_preserve"**: The routing-loss comparison in Table 8 uses the same training data and LoRA parameters, and L_preserve is a regularization on expert weights (not routing loss). The paper states "the only difference is the routing loss." This criticism speculates about a confound without evidence and is removed.
- **"Missing related works"**: The instructions forbid mentioning missing related works as I cannot verify them externally.
- **Strength Finder strengths about "important problem" and generic framing**: Removed as generic/superficial per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the RSL sign inconsistency as an important finding that was not apparent from the paper alone. The interaction between the harsh critic's mathematical analysis and the empirical results (Figure 4 showing the method works despite the apparent sign issue) highlights a genuine tension in the paper that requires author clarification.

## Suggestions

1. **Resolve the RSL sign issue**: Clarify whether Eq. (5) should have $+\lambda \mathbb{E}[\mathcal{H}]$ (which would make minimization equivalent to entropy minimization, matching the text) or whether the text description of "minimizing $\mathcal{H}(p(x))$" is incorrect. If the implementation uses a different sign than what is written, correct both the equation and the gradient derivation (Eq. 9). Explain how the stated loss produces the peaked distributions shown in Figure 4.

2. **Add a main-text table with parameter counts** for all compared methods, explicitly showing the claimed 48% reduction.

3. **Add an ablation comparing projection-layer experts vs. FFN-layer experts** under the same RSL loss to isolate the architectural contribution.

4. **Discuss the failures honestly**: Add analysis for the RTE drop (Table 4), QQP underperformance (Table 3), and ARC-E degradation (Table 5).

5. **Report standard deviations** across the three runs.

## Score and Decision

**Round 1 — Bracketing**: Three queries on "LoRA mixture of experts multi-task adaptation" with band filters:
- Low band (score < 3.5): Retrieved papers avg 2.50–3.33 (clearly flawed, rejected)
- Middle band (3.5 < score < 7.5): Retrieved papers avg 4.00–5.50 (mixed quality, some accepts)
- High band (score > 7.5): Retrieved papers avg 8.00 (not topically relevant to LoRA-MoE)

Initial bracket: **4.5–6.0**.

**Round 2 — Narrowing**: Queries on "LoRA routing loss specialization multi-task fine-tuning" and "mixture of experts routing loss entropy regularization PEFT" within (4.0, 6.0):
- MoSE (4.50, Reject): LoRA-Mixer has clearer novel contributions and broader experiments → **LoRA-Mixer is stronger**
- mtLoRA (5.50, Accept Poster): Stronger theoretical grounding, cleaner presentation → **LoRA-Mixer is slightly weaker** due to the RSL sign confusion
- DPSL (5.00, Reject): Comparable contribution level → **LoRA-Mixer has clearer gains**
- Expert Divergence Learning (5.50, Accept Poster): Strong paper, different setting → **roughly comparable quality**

**Final score anchored at 5.0.** The paper has solid empirical contributions (consistent gains across architectures, plug-and-play reuse, cross-model transfer) but the RSL sign inconsistency is a significant unresolved issue that prevents a higher score. Without this problem, the paper would sit at 5.5–6.0. The score of 5.0 reflects a paper with genuine contributions that needs a substantive clarification on its central theoretical formulation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>