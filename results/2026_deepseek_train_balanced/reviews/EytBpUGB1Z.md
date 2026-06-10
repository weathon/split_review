Now let me produce the final review.

## Summary

This paper identifies "retrieval heads" — a sparse set of attention heads (≈5% of all heads) in transformer LMs that are causally responsible for retrieving information from long contexts. Through systematic experiments across 4 model families (LLaMA, Yi, Qwen, Mistral) at 6 scales (7B–34B), the authors show that: (1) these heads are universal and sparse; (2) they exist inherently in pretrained models before long-context training; (3) they are dynamically activated based on context; and (4) pruning them collapses retrieval performance while pruning random heads does not. The paper also connects retrieval heads to chain-of-thought reasoning.

## Strengths

- **Cross-model breadth confirming universality and sparsity**: The paper tests across 4 model families, 6 model scales, and 3 post-training variants (continued-pretraining, chat fine-tuning, sparse upcycling). Section 3/Figure 3 shows that ~5% of attention heads meet the retrieval threshold in every model studied, while 45–73% have a retrieval score of 0. No prior work has demonstrated this degree of consistency across such a wide range of architectures and scales.

- **Causal evidence through controlled pruning**: Section 4.1 (Fig. 7) shows that masking the top retrieval heads (≈5% of all heads) drives NIAH performance below 50%, while pruning the same number of random non-retrieval heads has negligible effect. This controlled comparison provides strong evidence that these heads are necessary for accurate retrieval, not just correlated with it.

- **Quantitative evidence for intrinsic nature**: Figure 6 reports Pearson correlations >0.8 between the retrieval scores of base models and their continued-pretraining/chat/upcycled variants, while cross-family correlations are <0.1. This quantifies the claim that retrieval heads emerge during initial pretraining and persist through context-extension training — a non-obvious finding.

- **Stability of detection methodology**: Appendix Figures 13–14 show that the ranking of top retrieval heads stabilizes with increasing detection iterations, and varying needle size from 10 to 100 tokens does not change detection results. These diagnostics strengthen confidence that the retrieval score is a reliable metric, not an artifact of experimental setup.

- **Clear differentiation from induction heads**: Section 1 explicitly distinguishes retrieval heads from induction heads (Olsson et al., 2022) on two grounds — scale (7B–34B vs. <1B) and targeted capability (long-context factuality, QA, and CoT vs. in-context learning). This prevents the work from being dismissed as a rediscovery and clarifies what is novel.

## Weaknesses

### Fatal
None.

### Major

- **CoT reasoning analysis conducted on a single model**: The paper claims retrieval heads "strongly influence chain-of-thought reasoning" (abstract) and devotes Section 4.3 to this claim, yet all CoT experiments use only Mistral-7B-Instruct-v0.2. This is inconsistent with the paper's emphasis on universality across model families and scales. The interaction between instruction tuning and retrieval head behavior is not analyzed, and it remains unclear whether the finding generalizes to base models or other architectures. The paper's strongest downstream claim rests on a single data point, which is a meaningful evidential gap for a paper that otherwise demonstrates breadth.

- **The 0.1 threshold for classifying "retrieval heads" lacks sensitivity analysis**: A head is classified as a retrieval head if its average retrieval score exceeds 0.1 (line 53). The paper offers no analysis of how the set of identified heads changes with threshold variation (e.g., 0.05 or 0.2), nor whether the key results (sparsity percentages, causal pruning outcomes) are robust to reasonable threshold adjustments. While the distribution in Figure 3 suggests the qualitative sparsity story would survive modest shifts, the central quantitative claim ("only 3% to 6% of heads achieve a retrieval score above 0.1") relies on this specific cutoff, and the lack of sensitivity analysis is a meaningful gap.

### Minor

- **Detection methodology captures only literal token-level copy-paste**: The retrieval score is defined by exact token matching (the generated token must match the token at the maximally-attended position in the needle). The paper acknowledges this limitation (line 49: "although we detect retrieval heads by copy, in practice, their functionality goes beyond copy-paste") and partially addresses it with the ExtractQA experiments (Section 4.2), but the detection pipeline itself may systematically miss heads that perform retrieval through paraphrase or semantic matching. The paper could more prominently discuss what kinds of retrieval mechanisms might be missed by a pure copy-pate detector.

- **No confidence intervals or variance estimates**: Key numerical results (F1 drops of 9.2% and 23.1% in ExtractQA, NIAH success rates, correlation coefficients) are reported as point estimates without variance. While single-run evaluation is common in large-scale interpretability work, the reliability of comparisons would be improved by reporting variability across runs or contexts.

- **The "causal" framing overstates what ablation evidence alone establishes**: Property (5) in the abstract labels the findings as "causal," but the evidence is based on ablation (pruning), which demonstrates *necessity* — not the full causal mechanism. This is a standard limitation of ablation studies; the paper would benefit from using "necessary for" rather than "causal," which implies a stronger mechanistic account.

### Trivial

- The interaction between retrieval heads and "attention sink" tokens (line 95) is mentioned in passing but not analyzed. Given the prominence of the attention sink phenomenon, a brief analysis would be a natural addition.

## Nice-to-Haves

- Extend the pruning baselines to compare against "high overall attention mass but low retrieval score" heads rather than purely random heads, to confirm that the pruning effect is specific to retrieval functionality and not just to any head that attends strongly.
- Include a table in the main text listing the number of layers and heads per layer for each model studied.

## Removed Points

These points were raised by reviewers but removed after cross-checking against the paper:

- **"Mistrial" typo (line 113)**: This is a PDF parser artifact; the original submission would not have this error. Removed per hard rule on formatting artifacts.
- **"Threshold justification is circular"**: The paper's justification (0.1 "reflects the minimal level of retrieval activity necessary for a head to be considered specialized") is a threshold choice, not circular reasoning. The lack of sensitivity analysis (kept as a Major weakness) is the real concern.
- **"Induction heads overlap not empirically investigated" and "prefix-matching pattern not tested"**: These ask the paper to address questions outside its stated scope. The paper explicitly distinguishes retrieval heads from induction heads on scale and capability focus (Section 1), not on mechanistic identity. Scope creep removed.
- **"Mistral v0.1 vs v0.2 comparison confounds architecture with training"**: The paper makes a straightforward empirical observation (sliding window attention fails NIAH, full attention passes) to motivate why full attention is important. This is not a controlled experiment claim and the criticism misreads the intent of the passage.
- **"Missing appendix or proofs"**: Appendices are frequently stripped by the parser; the paper is an empirical analysis, not a theory paper requiring proofs.
- **Reproducibility nitpicks about trivial implementation details**: Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs surface complementary perspectives (harsh critic focuses on evidential gaps in the strongest claims; strength finder highlights the breadth of empirical support) but do not produce a genuinely new synthesis beyond what the paper itself provides.

## Suggestions

1. **Extend the CoT analysis to at least one additional model family** (e.g., a LLaMA-2 variant) to validate the claim that retrieval heads influence reasoning across architectures. This is the single most impactful fix.
2. **Add a sensitivity analysis** showing how the set of identified retrieval heads changes with the threshold (e.g., 0.05, 0.1, 0.15, 0.2) and whether the pruning results hold at these alternative thresholds.
3. **Tone down the "causal" framing** in the abstract to "necessary for" or "causally implicated in," which more precisely reflects the ablation evidence.
4. **Report variance or confidence intervals** for the key downstream task results where feasible.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>