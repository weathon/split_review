## Summary

LoRA-Mixer proposes placing mixture-of-experts (MoE) on the *projection layers* (Q/K/V) rather than on FFN blocks, combined with a Routing Specialization Loss (RSL) that adds token-level entropy regularization to standard load-balancing losses. The framework supports joint training and plug-and-play reuse of downloaded LoRA modules. Evaluated across 15 benchmarks on LLaMA3-8B, Mistral-7B, and Falcon-Mamba-7B (an SSM), it outperforms LoRAHub, MoLE, MixLoRA, and other routing-loss baselines across most tasks.

## Strengths

- **Projection-layer MoE placement is a distinctive architectural choice.** Unlike prior LoRA-MoE work that replaces FFN blocks (MixLoRA) or attaches parallel branches (MoLE), LoRA-Mixer places LoRA experts on the attention projection matrices (Q/K/V), which Figure 1 and Equation 4 clearly illustrate. The output feeds directly into the attention or SSM module, making the intervention architecture-agnostic. This is validated by strong results on Falcon-Mamba-7B (a pure SSM), which prior Transformer-specific frameworks cannot handle.

- **RSL provides a principled and empirically validated improvement over standard auxiliary losses.** The derivation in Section 3.3 (Equations 5–9) shows that RSL introduces a token-level gradient signal ($\log p_i(x)$) that standard auxiliary losses lack. Table 8 directly validates this: under identical 2k-sample training data and LoRA parameters, RSL outperforms GMoE, DS-MoE, and AESL by substantial margins (e.g., +3.77% on SST-2, +6.86% on HumanEval).

- **Broad and well-structured evaluation.** The paper tests across 15 benchmarks covering medical QA, commonsense reasoning, NLP, math, and coding, on three different base architectures (Transformer ×2, SSM ×1). Tables 2, 3, 4, and 7 show consistent improvements over baselines. The inclusion of Falcon-Mamba is especially informative and demonstrates genuine architecture-agnostic capability.

- **Cross-model transfer and plug-and-play reuse are demonstrated concretely.** Table 5 shows Mistral→LLaMA router transfer improves 2 of 3 tasks without fine-tuning. Table 3 shows that LoRA-Mixer can compose five frozen LoRAs downloaded from LoRAHub using only 2k additional data, outperforming single LoRA on 4 of 5 GLUE tasks.

- **Expert load analysis (Figures 3–4) supports the RSL design narrative.** Figure 3 shows balanced per-expert loads (15%–18%), and Figure 4 shows that RSL produces task-specific activation peaks (e.g., Expert 1 at ~35% for Medical) while the w/o-RSL baseline yields flat distributions. This directly supports the claim that RSL achieves both balance and specialization.

## Weaknesses

### Major
- **The "48% of trainable parameters" claim in the abstract and introduction is unsubstantiated in the main text.** No table or calculation shows which baselines are included in the denominator, how many experts/ranks are used by each method, or how the router size is accounted for. The paper points to Appendix A.4 and A.7, but a claim this precise and prominent in the abstract should have supporting evidence in the main text. A simple parameter-count comparison table is needed.

### Minor
- **No variance or confidence intervals reported.** The paper states "all experiments are run three times and the average reported," but no table includes standard deviations. Given the large claimed gaps (e.g., Table 8: RSL 57.32 vs. AESL 50.46 on HumanEval), the absence of error bars makes it impossible to assess whether these differences are statistically significant or within run-to-run noise.

- **Cross-model transfer claim overreaches the evidence.** Table 5 tests only 3 tasks, and one of them (ARC-E) actually degrades (85.89 vs. 88.45). Calling the routing "extremely robust and transferable" requires more tasks, more source/target model pairs, and ideally an analysis of what the router actually learns that transfers.

- **The 4K data-point anomaly in Table 9 is visible but unexplained in the main text.** With RSL, average performance at 2K is 79.26 but drops to 78.77 at 4K (below the w/o-RSL baseline at 4K). The paper defers the explanation to Appendix A.16. While the appendix is beyond the review scope, this non-monotonic behavior is concerning enough that it deserves at least a brief comment or hypothesis in the main text.

- **The preservation loss (L_preserve, Equation 11) is defined and included in the total loss (Equation 12) but never mentioned in any experiment.** It is unclear whether $\beta$ was set to zero or what value it took in the reported results. Clarifying whether this term was used and why would improve completeness.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment that isolates projection-layer MoE from FFN-layer MoE (same experts, same router, same training data) would strengthen the core architectural claim.
- Reporting results for multiple random seeds (not just averaged) would enhance trust in the numbers, especially for the routing-loss comparison in Table 8.
- More details on the number and training source of LoRA experts used in each experiment (which domains, what rank) would improve reproducibility.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Unclear LoRA baseline in Table 2" / "unfair comparison"**: Removed. The "LoRA" row standardly denotes single-task LoRA. Comparing multi-task LoRA-Mixer against single-task LoRA favors the baseline (single-task LoRA does not share capacity), making this a conservative, not unfair, comparison.
- **"Large gains on BoolQ/HellaSwag/PIQA are suspicious"**: Removed. MoE composition over multiple LoRA experts is expected to outperform single LoRA. The critic provides no concrete evidence these gains are implausible; the speculation is ungrounded.
- **"RSL vs. AESL gap on HumanEval is implausible"**: Removed. Different routing losses can produce large differences in low-data regimes (2k samples) — that is the paper's claim, not an anomaly. No evidence is provided that such a gap is impossible.
- **"'Serial attention routing' framing is misleading"**: Removed. The paper explicitly states LoRA-Mixer is "applied to the linear projection layers *in serial* with the Attention and SSM modules" (Figure 2 caption). This usage is accurate, not misleading.
- **"Preservation loss is a dead branch"**: Demoted to minor and rephrased (see above). The strong claim that it was "never used" is unverifiable without the appendix.
- **"Missing appendix content" (hyperparameter choices, ablation on K, etc.)**: Removed per hard rule — the parser strips appendix sections from all papers; they exist in the original submission.
- **"Omitted MoLA and other baselines"**: Removed per rule — the reviewer cannot independently verify missing related work.
- **"Attention-centric framing for SSMs"**: Removed. The paper explicitly discusses "attention or state-transition mechanisms" and includes SSM results, so it does not over-claim.
- **"Falcon-Mamba has no attention"**: Removed. The paper is explicit about supporting SSMs.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a parameter-count comparison table** in the main text that specifies for each method (LoRAHub, MoLE, MixLoRA, LoRA-Mixer): number of experts, rank per expert, router size, and total trainable parameters. This would directly substantiate the "48%" claim (or correct it if inaccurate).

2. **Add standard deviations** to all tables, or at minimum to Tables 2, 8, and 9 where the largest claims are made.

3. **Tone down the "extremely robust and transferable" claim** for cross-model transfer (Table 5), and either add more tasks or reframe as preliminary evidence of transferability.

4. **Briefly address the 4K anomaly in Table 9** with a hypothesis in the main text (e.g., overfitting of the router at intermediate data scales, or a known property of the training set composition).

5. **Clarify whether $\beta$ (preservation loss coefficient) was used** in the reported experiments, and if so, what value it took. If it was set to zero, state that explicitly.

## Score and Decision

**Calibration anchors used across rounds:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| b2ZbMyFCja (MoL) | 2.50 | R1 | Lower — fewer baselines, narrower eval |
| ZiBDVotA7g (Gated LoRA) | 3.00 | R1 | Lower — narrower scope, no SSM eval |
| YXvPS2uebR (Rank-efficient MoE) | 2.00 | R1 | Lower — limited novelty, insufficient baselines |
| O0BRg90v1Y (MIDAS) | 2.67 | R1 | Lower — different problem setting |
| BqyPLOkxFY (Cross-layer MoE Routing) | 5.00 | R1 | Comparable — both accepted-level work with minor issues |
| MpeyjgWbKt (Coupling Experts & Routers) | 6.67 | R1 | Higher — cleaner experiments, stronger theoretical grounding |
| v5qb8BG18G (Continuous Rerouting) | 4.00 | R1 | Lower — narrower analysis |
| zNqc0li5Dl (ReMix) | 4.00 | R1 | Lower — similar LoRA-MoE routing topic but weaker eval |
| VKGTGGcwl6 / qOyF214xmg / oBXfPyi47m / kkBOIsrCXh | 8.00 | R1 | Not relevant — different topics |
| yAIosXyiOy (MoSE) | 4.50 | R2 | Lower — similar multi-task LoRA-MoE but less architectural novelty |
| L3RSb9yTlL (mtLoRA) | 5.50 | R2 | Slightly higher — better diagnostic analysis, but also incremental novelty |
| x9tSyvnD8o (Mixture of Thoughts) | 4.00 | R2 | Lower — different problem |
| 3lskwxB653 (Routing Manifold Alignment) | 4.50 | R2 | Comparable — both improve routing; this one is narrower in scope |
| wrqYMYazm0 (Expert Divergence Learning) | 5.50 | R2 | Comparable — similar level of contribution, both have evaluation concerns |
| fMdJAcQNSD (Dirichlet-Prior Shaping) | 5.00 | R2 | Comparable — rejected but similar strengths/weaknesses profile |
| FNuvMnGAm8 (Similarity Preserving Routers) | 5.00 | R2 | Comparable — also improves routing, rejected |

**Round 1 bracket:** [4.5, 6.0]

**Round 2 narrowing:** The paper is clearly above ReMix (4.00) and MoSE (4.50) due to its more distinctive architectural contribution (projection-layer MoE), broader evaluation (15 benchmarks, 3 architectures including SSMs), and demonstrated cross-model transfer. It is comparable to Expert Divergence Learning (5.50, Accept) and Dirichlet-Prior Shaping (5.00, Reject) — all three propose routing improvements with solid evaluations but have issues (modest gains / unsubstantiated claims / missing error bars). It falls below Coupling Experts and Routers (6.67, Oral), which has cleaner experiments and stronger theoretical grounding. The main weakness keeping it from a higher score is the unsubstantiated "48%" parameter claim and missing error bars.

**Final score:** 5.0

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>