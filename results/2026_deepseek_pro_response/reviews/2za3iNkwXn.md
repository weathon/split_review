## Summary

This paper investigates how compression (quantization, distillation, pruning) affects the reasoning capabilities of large reasoning models (LRMs) through two complementary approaches: comprehensive performance benchmarking of compressed DeepSeek-R1 variants across four reasoning datasets, and fine-grained mechanistic interpretation that adapts difference-of-means and attribution-patching to compute per-linear-module weight importance scores. The main findings are: (1) weight count affects knowledge memorization more than reasoning, (2) the MLP up-projection in the final layer emerges as critically important in distilled LRMs, and (3) current quantization methods overly compress final-layer modules and gate projections, and protecting just ~2% of these weights can substantially improve 3-bit quantized performance.

## Strengths
- **Comprehensive multi-method benchmarking across compression paradigms**: The paper evaluates 40+ experimental configurations spanning dynamic quantization (2.51/1.73/1.58-bit), distillation (four R1-distilled models), pruning (SparseGPT, AlphaPruning at multiple sparsity levels), and four PTQ methods (AWQ, GPTQ, GPTAQ, ANY4/3 at 4-bit and 3-bit) across four reasoning benchmarks of varying difficulty (AIME 2024, FOLIO, Temporal Sequences, MuSiQue). This breadth, presented in Tables 1 and 2, goes well beyond prior work that typically evaluates only one or two methods on simpler benchmarks.

- **Fine-grained mechanistic interpretation at the per-linear-module level**: Unlike prior interpretability work that measures only layer-wise contribution, the paper adapts difference-of-means (to extract per-module steering vectors) and attribution-patching (to compute per-module importance scores) for each of the seven linear components (q, k, v, o, gate, up, down) across all layers. This enables a genuinely more granular analysis of which specific weights matter for reasoning — a core question in compression research. The heatmap visualizations (Figures 2, 3) make these patterns interpretable at a glance.

- **Causal validation through two complementary ablation experiments**: Table 3 shows that selectively quantizing only `32_up` (the final-layer MLP up-projection identified as most important) causes a 16.3-point average accuracy drop — substantially more than quantizing other components. Table 4 demonstrates that protecting final-layer MLP modules (~2% of weights) in 3-bit AWQ raises average accuracy by 6.57 percentage points. These experiments close the loop between interpretation and actionable findings.

- **Cross-model generalization of the final-layer up_proj finding**: The `32_up` outlier is observed in both R1-Distill-Llama-8B (Figure 2) and R1-Distill-Qwen-7B (Figure 4), suggesting the finding is not an artifact of a single architecture.

- **Clear conceptual framework**: The definition of relative importance and the principled decision to track only decreases in importance shift (Section 2.3) makes the heatmap interpretation unambiguous — the justification that increases merely offset decreases due to normalization is logically sound.

## Weaknesses

### Fatal
None.

### Major
- **The protection experiment is a single data point, yet it supports one of the paper's three headline claims**: The protection experiment (Section 5.2, Table 4) consists of exactly one configuration — protecting final-layer MLP in 3-bit AWQ on R1-Distill-Llama-8B. No control condition is tested (e.g., protecting a random set of modules of equal parameter count) to establish that the gain is specifically due to the correctness of the importance scores rather than simply having more bits anywhere. The second identified bottleneck (gate projections) is not tested for protection. No cross-model validation is performed (e.g., on Qwen-7B). The abstract and introduction elevate this to a headline result and claim it "greatly surpass[es] the state-of-the-art," yet the "23.17%" figure is the gain against the single worst-performing 3-bit baseline (ANY3 on Llama-8B, 29.4 avg), not the best. The comparison against the best-performing 3-bit baseline on the same model yields a more modest 4.77% improvement. While the heatmap analysis in Figures 3, 6, and 7 provides supporting qualitative evidence, the quantitative validation is insufficient to support the strength of the claim made.

- **The connection between the benchmarking half (Section 3) and the interpretability half (Sections 4–5) is asserted rather than demonstrated**: The paper's thesis is that mechanistic interpretability explains compression effects, but the two halves remain largely separate. There is no quantitative analysis linking importance-shift magnitude to benchmark degradation — for example, across models or compression levels, do larger importance shifts in critical modules correlate with larger accuracy drops? The paper would be substantially stronger if it closed this loop rather than presenting the two analyses side-by-side.

### Minor
- **Evaluation protocol inconsistency weakens the R1 vs. compressed-R1 comparison**: Table 1 evaluates original R1 and dynamically quantized R1 variants with a single pass (marked †), while all other models are averaged over three passes. The 2.51-bit R1 scores 84.8 avg vs. 83.1 for original R1 — i.e., the compressed model appears to outperform the original. The paper attributes this to "over-parameterization" (Takeaway 3.1) but does not discuss how single-pass variance could explain the difference. While this does not undermine the paper's main conclusions (the degradation pattern across bit-widths is clear regardless), it weakens the specific claim that 2.51-bit R1 reaches "close-to-R1 performance" with precision.

- **The interpretability pipeline has unexamined failure modes**: The chain is GPT-4o annotates reasoning-behavior spans → difference-of-means extracts steering vectors → attribution-patching (first-order Taylor approximation) computes importance scores. The paper defers annotation robustness to a stripped appendix. The 120-instance annotation set is small and no sensitivity analysis is performed (e.g., how do importance scores vary under instance subsampling?). No comparison against full activation patching (a more expensive but reliable method) calibrates trust in the linear approximation. The decision to zero out increases in relative importance (Section 2.3) is well-motivated but means the analysis cannot detect modules that genuinely become *more* important after compression.

- **The 1_up anomaly in Table 3 is noted but unexplained**: 1_up, ranked last overall, produces the lowest AIME 2024 score (6.7), contradicting the ranking. The paper acknowledges this ("except for 1_up, which incurs the lowest accuracy on AIME 2024") but offers no explanation. This raises concerns about whether the importance scores are reliable across all modules.

- **The distillation-vs-knowledge claim in Takeaway 3.3 is partially conflated**: The claim that "distillation compresses knowledge retention more than reasoning" rests partly on comparing Qwen-32B vs. Llama-70B MuSiQue scores (Table 1), which could reflect pre-training data differences between model families rather than distillation effects alone.

### Trivial
- The four reasoning behaviors (backtracking, uncertainty estimation, example testing, adding knowledge) are taken from prior work but never defined or illustrated in the main text. A reader unfamiliar with Venhoff et al. (2025) cannot evaluate whether these categories are meaningful.
- The paper would benefit from a limitations section explicitly acknowledging the small annotation dataset (120 instances), the linear approximation in attribution patching, and the narrow scope of the protection experiment.

## Nice-to-Haves
- Close the loop between benchmarking and interpretability by showing that importance-shift magnitude correlates with benchmark degradation across models or compression levels.
- Expand the protection experiment to include controls (random module protection, gate-projection protection, both) and run it on at least one additional model family (e.g., Qwen-7B).
- Report variance for benchmark evaluations and bootstrap confidence intervals for importance scores from the 120-instance annotation set.
- Calibrate the attribution-patching approximation against full activation patching for a subset of modules.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic claim: "The core benchmarking comparison is confounded (evidential)" framed as fatal**: The single-pass vs. three-pass discrepancy is a real limitation, but it does not invalidate the core claims — the degradation pattern across compression levels is clear regardless. Demoted to Minor.
- **Harsh Critic claim: "No test on gate projections / no cross-model generalization" for protection experiment**: Valid points but subsumed under the broader Major weakness about the protection experiment being a single data point.
- **Harsh Critic claim: "GPT-4o annotation reliability not verified"**: The paper states robustness is demonstrated in Appendix G (stripped); we cannot verify but cannot assume absence. Merged into the Minor weakness about the interpretability pipeline rather than treated as a standalone fatal flaw.
- **Harsh Critic claim: "Takeaway 3.1 is a truism"**: This is a judgment about significance, not a factual error. The takeaway has empirical support. Removed.
- **Harsh Critic claim: "Section 4.3 overstates — low relative importance in backbone doesn't mean backbone weights are irrelevant"**: The paper's claim is that important weights of the distilled model are "primarily the result of distillation with SFT," which is a reasonable interpretation of the importance-shift analysis. Removed.
- **Harsh Critic claims about missing non-R1 generalization evidence / missing appendix proofs**: The paper references appendices for these (standard practice). Removed per hard rules.
- **Strength Finder claim: "Practical guidance for future compression research"**: Too generic and speculative. Removed.
- **Strength Finder claim about importance of the problem**: Generic framing, not a concrete contribution. Already captured in the summary.

## Novel Insights
The paper's most genuinely novel observation is the identification of the final-layer MLP up-projection (`32_up`) as the single most important weight module for reasoning in distilled LRMs, validated both destructively (quantizing it causes a 16.3-point average drop across benchmarks, far more than comparable modules) and constructively (protecting it during quantization yields substantial recovery). This is a specific, falsifiable finding that is not obvious from prior work and has direct implications for compression algorithm design. The cross-architecture replication in both Llama and Qwen families strengthens its generality.

## Suggestions
- Run the R1 baselines with the same 3-pass protocol used for other models, or at minimum report single-pass variance estimates to contextualize the 2.51-bit vs. original R1 comparison.
- Add a control condition to the protection experiment (e.g., protect a random set of modules with equal parameter count) to isolate the contribution of the importance scores.
- Include a brief definition and one example of each reasoning behavior in the main text to make the paper self-contained.

## Score and Decision

**Round 1 bracket**: The paper sits between "The Super Weight" (4.60, Reject) and "Mechanistically analyzing fine-tuning" (6.67, Accept), with initial bracket 4.6–6.5.

**Round 2 narrowing**: Compared against "LLM Pruning and Distillation in Practice" (5.00, Reject), "PALMBENCH" (5.80, Accept), "The Cost of Scaling Down Large Language Models" (6.00, Accept), and "Compressing LLMs: The Truth is Rarely Pure and Never Simple" (6.75, Accept). The current paper is more ambitious and broader than the 5.00 anchor (adds mechanistic interpretability, covers 3 compression paradigms), but has methodological gaps (single-data-point protection experiment, disconnected halves, evaluation protocol inconsistency) that the 6.00–6.75 anchors do not have. It is most comparable to PALMBENCH (5.80) in being a comprehensive benchmarking study, but the current paper's headline claims outrun its evidence more than PALMBENCH's do.

**Final score: 5.5**, situated between the rejected 5.00 papers and the accepted 5.80–6.00 papers. While the paper makes genuine contributions (comprehensive benchmarking, novel fine-grained interpretability findings, causal validation), the protection experiment — one of three headline claims — is too narrow to support the strength of claim made, and the two halves of the paper remain quantitatively disconnected.

**Anchor comparison summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| PrefixQuant | 3.00 | R1 | Current paper is substantially stronger in scope and contribution |
| LLM Compression with Convex Opt. | 3.00 | R1 | Current paper is substantially stronger |
| The Super Weight in LLMs | 4.60 | R1 | Current paper is broader (3 compression paradigms + interpretability vs. one finding + method) |
| LLM-Codebook | 4.75 | R1 | Current paper has broader evaluation and more novel findings |
| Distributional reasoning in LLMs | 5.00 | R1 | Current paper is broader and more actionable |
| LLM Pruning and Distillation in Practice | 5.00 | R2 | Current paper is more ambitious (interpretability + benchmarking) |
| PALMBENCH | 5.80 | R2 | Similar in benchmarking rigor; current paper adds interpretability but has weaker validation |
| The Cost of Scaling Down LLMs | 6.00 | R2 | Cleaner methodology and more focused claims; current paper is more ambitious but less rigorous |
| Mechanistically analyzing fine-tuning | 6.67 | R1 | Cleaner narrative, tighter methodology; current paper is weaker |
| Compressing LLMs (LLM-KICK) | 6.75 | R2 | Stronger methodology, cleaner narrative, better-supported claims |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>