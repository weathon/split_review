Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper investigates using Minimum Bayes Risk (MBR) decoding with LLM judges to improve instruction-following LLMs. In the first part, the authors show that MBR decoding with Prometheus-2-7B as a reference-based utility metric consistently outperforms greedy decoding, best-of-N decoding, and MBR with lexical/embedding metrics across five LLMs (7B–70B) on AlpacaEval 2.0 and MT-Bench. In the second part, they show that iterative DPO self-training on MBR-selected outputs allows greedy decoding to match or exceed the test-time MBR performance, eliminating the quadratic inference cost of MBR decoding.

## Strengths

- **MBR decoding with an LLM judge yields substantial and consistent gains across diverse model scales.** Tables 1 and 2 show average improvements of +3.6% on AlpacaEval 2.0 and +0.28 on MT-Bench across five LLMs (7B to 70B). The gains are positive for every model tested, and a small 7B judge (Prometheus-2-7B) improves models up to 10× larger — a practically significant finding.

- **MBR decoding consistently outperforms best-of-N decoding across multiple judge models.** Table 3 compares MBR and BoN across five different LLM judges (Prometheus-2-7B, Prometheus-2-8x7B, JudgeLM-7b, JudgeLM-33b, Llama3-70b-Instruct) and five base models. MBR beats BoN in every configuration, often by a wide margin (e.g., Llama3-70b-Instruct: MBR +0.41 vs BoN +0.06 on MT-Bench). This provides strong evidence that reference-based evaluation via pseudo-references is more effective than reference-free scoring.

- **Iterative DPO self-training on MBR-selected outputs allows greedy decoding to match or exceed the test-time MBR performance.** After three rounds, the 13B DPO-MBR model achieves 15.3% on AlpacaEval 2.0 and 6.75 on MT-Bench, surpassing the base SFT model with MBR decoding (13.6% and 6.31). This demonstrates that MBR's gains can be internalized without paying the quadratic inference cost — a practical advance over prior work limited to machine translation.

- **Clean ablation isolating DPO vs SFT for self-training.** Table 4 (right subtable) shows that SFT self-training on MBR-selected outputs yields at most +1.57% on AlpacaEval, while DPO self-training yields +3.68%, isolating preference learning as the key mechanism.

- **Quantification of inference-time cost savings.** Figure 3 shows MBR self-trained models achieve >10× throughput over MBR decoding at test time (25 vs ~2 samples/second), making the gains practically accessible.

## Weaknesses

### Fatal
None.

### Major

- **No statistical significance or variance reporting.** All results in Tables 1–4 and the self-training tables are point estimates without confidence intervals, standard errors, or multiple-run statistics. MT-Bench has only 80 samples, and improvements of 0.1–0.3 on a 1–10 scale (e.g., Llama2-7b: greedy 5.72 → MBR 6.10) may fall within measurement noise. Without error bars or bootstrap intervals, the reader cannot assess the robustness of the reported gains. This is the most significant evidential gap in the paper.

### Minor

- **Self-training experiments start from weak SFT baselines, limiting generalizability.** The SFT models trained on 3000 UltraChat samples (AlpacaEval 5.18% for 7B, 8.24% for 13B) are far below the official chat model performance used in Section 3 (14.4% and 19.0%). The paper justifies this choice ("retain full control over the training procedure"), but it leaves open whether the same self-training gains would hold from stronger starting points. The official chat models are already available and could have been included as an additional starting condition.

- **Missing ablations in DPO self-training.** The paper does not compare DPO on MBR-selected pairs against (a) DPO on random pairs from the candidate set, or (b) DPO on oracle-selected pairs (upper bound from an external strong model). The existing comparison (DPO-MBR vs DPO-BoN) is informative, but without these controls it is unclear how much of the gain comes from MBR's selection mechanism vs. simply using DPO at all.

- **Data size not controlled in self-training comparisons.** The paper compares *dpo*-3-MBR (trained on 9000 prompts via DPO) against *sft*-full (trained on 12000 prompts via SFT) and concludes that MBR-selected data is more beneficial. While the conclusion is plausible, the comparison conflates training objective (DPO vs SFT), data size (9000 vs 12000), and data selection strategy. A controlled comparison with equal data sizes would be stronger.

- **No human evaluation.** The paper relies entirely on automated LLM-as-a-judge benchmarks (AlpacaEval 2.0 with GPT-4o, MT-Bench with GPT-4o). While these correlate with human judgments (as the paper cites), a small-scale human preference study would strengthen the claim that MBR decoding improves "instruction-following" rather than just scores on these particular benchmarks. This is standard practice in the field and not unique to this paper, but it remains a limitation.

### Trivial

- **Temperature choice (t=0.3) not clearly justified.** The analysis in Figure 1 (right) shows performance increasing with temperature up to roughly t=0.5–1.0 and dropping after t=1.0, yet the main experiments use t=0.3. Gains at t=0.3 may be conservative (which works in the paper's favor), but the choice deserves a brief explanation.

- **Per-category analysis shows near-zero gains in some categories.** Figure 2 (category breakdown) shows that several categories (e.g., coding, math) have gains within one standard error of zero, yet the text says "improves across a wide range" without qualifying the small effect sizes in reasoning categories. The paper partially addresses this by noting the higher bar for correctness in reasoning tasks, but the presentation could be more precise.

## Nice-to-Haves

- Applying the MBR self-training procedure to the official chat models (e.g., Llama2-7b/13b-chat, Llama3-8b/70b-Instruct) would substantially increase confidence that the results generalize beyond scratch-trained SFT models.
- Evaluating on a benchmark that does not use LLM-as-a-judge (e.g., IFEval with verifiable constraints) would break the reliance on automated judges and provide complementary evidence.
- A deeper analysis of *why* MBR outperforms BoN would strengthen the paper — specifically, an ablation using an oracle reference-free judge to distinguish the "averaging effect" from the "reference-based evaluation effect."

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Circular evaluation framework" (as a fatal issue).** The harsh critic claimed that using LLM judges for both supervision (Prometheus-2) and evaluation (GPT-4o on AlpacaEval/MT-Bench) creates a "closed loop." This is overstated: Prometheus-2 and GPT-4o are different models, AlpacaEval and MT-Bench are standard, widely-validated benchmarks, and the paper cites their correlation with human judgments. The concern about no human evaluation is retained as a minor weakness, but the framing as a "circular" or "fatal" flaw is not supported. The critic also ignores that AlpacaEval 2.0 uses length-controlled win rates specifically to mitigate the length/style gaming concern.
- **"SFR-Embedder baseline's poor performance is predictable."** Including baselines that do not work is standard practice. The paper acknowledges exploring dense embedders for MBR is novel, and a negative result is informative.
- **"Temperature choice suboptimal, gains might be underestimated."** If t=0.3 is suboptimal relative to the peak in Figure 1, then the reported gains are conservative, which strengthens rather than weakens the paper's claims. This is not a weakness.
- **"Beam search and Longest decoding degrade performance."** These are findings reported by the paper, not weaknesses.
- **Formatting/style nitpicks and missing appendix content.** The parser strips these; they do not exist in the original submission.
- **Missing related works.** Cannot confirm without external knowledge.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a pattern of analysis that the paper itself does not already articulate.

## Suggestions

1. **Add confidence intervals or bootstrap estimates** for all main results (Tables 1–4). For MT-Bench in particular (80 samples), report the 95% confidence interval and state whether the gains are significant.
2. **Include a controlled ablation for DPO self-training:** compare DPO on MBR-selected pairs against DPO on random pairs and DPO on oracle-selected pairs, with matched data sizes and training rounds.
3. **Apply MBR self-training to at least one official chat model** (e.g., Llama3-8b-Instruct) to show that the distillation procedure works from stronger baselines, not just from scratch-trained SFT models.
4. **Provide a small-scale human evaluation** on a subset of AlpacaEval (e.g., 100 examples) to validate that the automated gains correspond to human preferences.
5. **Clarify the choice of t=0.3** in light of the analysis in Figure 1 showing peak performance at higher temperatures.

## Score and Decision

This paper makes a solid empirical contribution to an important problem (improving instruction-following through LLM judge supervision). The experiments are broad: 5 base models, 5 judge models, multiple utility metrics, and both inference-time and self-training settings. The core findings are well-motivated and the results are consistent. However, the lack of statistical significance reporting is a real evidential gap, and the self-training results would benefit from stronger baselines and cleaner ablations. The paper is above the acceptance threshold but requires revisions to address these gaps.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>