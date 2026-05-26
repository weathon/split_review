Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual text. Let me construct the final consolidated review.

## Summary

The paper introduces Language Confusion Gate (LCG), a lightweight plug-in module that dynamically masks tokens from disallowed language families during LLM decoding, without modifying the base model. LCG uses a two-layer MLP trained via norm-adjusted self-distillation on the model's own debiased predictions. The method is motivated by analysis showing that language confusion is infrequent, correct-language tokens rank among the top candidates, and token embedding norm imbalance biases sampling toward high-resource languages. Evaluated across Qwen3, Llama3.1, Gemma3, and GPT-OSS on FLORES+, INCLUDE, and Humaneval-XL, LCG reduces language confusion by roughly an order of magnitude while preserving task performance and legitimate code-switching, with only 0.4% latency overhead.

## Strengths

1. **Order-of-magnitude confusion reduction across multiple models and datasets** — On FLORES-NO-LATIN, LCG-adjusted reduces CJ confusion from 1.0%→0.0% and Latin confusion from 4.4%→0.4% on Qwen3-30B, and from 3.0%→0.4% (CJ) and 8.4%→2.9% (Latin) on Llama3.1-8B (Table 3). Similar large reductions hold on the INCLUDE dataset (e.g., Qwen3-30B CJ% from 2.21→0.11) and on thinking models (Table 4). This directly supports the central claim of drastic confusion reduction.

2. **Task performance is preserved** — On FLORES-NO-LATIN, BLEU scores remain stable or improve slightly (Qwen3-30B: 13.2→13.4, Llama3.1-8B: 11.3→12.3; Table 3). On INCLUDE, accuracy changes by at most ±1.4%. For thinking models, Pass@1 and Pass@10 on Humaneval-XL are essentially unchanged (Table 4). This shows the intervention does not degrade quality.

3. **Legitimate code-switching is largely preserved** — LCG-adjusted permits English tokens at 86.7% of human-validated code-switch points (Section 5.3). On FLORES-WITH-LATIN, post-intervention code-switch rates remain comparable to reference rates (e.g., Qwen3-8B: 46.34%→25.90% vs ground-truth 38.36%; Table 5). This distinguishes the method from a naive language constraint.

4. **Outperforms existing baselines by a large margin** — Figure 3 shows LCG-adjusted achieves far lower confusion rates than ICL, greedy decoding, and ORPO tuning on Qwen3-8B and Llama3.1-8B. Unlike ORPO, LCG does not degrade INCLUDE accuracy (e.g., ORPO drops accuracy from 61.4→57.3 on Qwen3-8B; LCG maintains 61.8). This demonstrates clear superiority over prior intervention strategies.

5. **Extremely low overhead for deployment** — The gate adds only 0.4% to per-step latency (15.95 ms→15.99 ms for Qwen3-30B, Section 6) and intervenes on only 0.33–0.38% of tokens (Section 5.3). This supports the claim that LCG is a practical plug-in solution.

6. **Norm-adjusted self-distillation ablation validates the core training innovation** — Table 3 consistently shows LCG-adjusted outperforms LCG-unadjusted (e.g., Llama3.1-8B Latin%: 5.7% vs 2.9%; Qwen3-8B Latin%: 6.2% vs 2.0%; Qwen3-30B CJ% on INCLUDE: 0.22% vs 0.11%).

## Weaknesses

### Fatal
None.

### Major
None. No weakness identified verifiably undermines the paper's core claims.

### Minor

1. **Missing training hyperparameters for reproducibility** — The paper specifies (k=5, p=0.999) and (k=20, p=0.95) for the *intervention rules* (Section 4.3), but does not state the k and p values used during *training* to create pseudo-targets via top-k/top-p filtering (Section 4.2). The two-layer MLP architecture (hidden dimension, activation function) is also not specified. These details are needed for exact reproducibility.

2. **Code-switch preservation experiment is underspecified** — The paper reports 86.7% preservation based on "human-validated examples" (Section 5.3) but provides no details on: number of examples evaluated, number of annotators, annotation instructions, or inter-annotator agreement. Without this information, the strength of this evidence is unclear.

3. **FLORES-NO-LATIN evaluation languages create ambiguity for CJ confusion** — The paper describes FLORES-NO-LATIN as partitioned from five target languages including Chinese (Section 5.2), and reports CJ confusion on this subset (Table 3). The evaluation languages for FLORES+ are stated as Arabic, Hebrew, Korean, Thai (implicitly excluding Chinese), but it is not explicitly stated that Chinese-origin examples were excluded from the CJ confusion calculation. While the evaluation setup as described is consistent, this ambiguity should be resolved with a clear statement.

4. **Latin confusion metric on FLORES-NO-LATIN may include some false positives** — The assumption that any Latin character in a FLORES-NO-LATIN response is an error (Section 5.2) does not account for legitimate proper nouns, loanwords, or technical terms (e.g., "iPhone", "Python") that a model might correctly produce even when the reference transliterates them. The paper's code-switch analysis partially addresses this, but the false-positive rate is not quantified. The relative improvement from LCG remains informative, but absolute numbers should be interpreted cautiously.

5. **Small Pass@1 decreases on thinking models reported without variance** — In Table 4, Qwen3-8B drops from 83.81→83.13 and GPT-OSS from 85.88→84.56 after applying LCG. The paper describes these scores as "maintained," but no confidence intervals, standard deviations, or significance tests are provided. Given the Humaneval-XL sample size (164 problems × 10 repetitions), these drops may be within noise, but the paper should acknowledge this.

6. **ORPO baseline comparison lacks hyperparameter details** — The paper states that ORPO was trained using a "multilingual dataset" with "synthesized samples with language confusion as rejected samples" (Section 5.3, Figure 3), but does not report learning rate, number of epochs, ORPO β parameter, or the data construction process. Without these details, the comparison—which shows ORPO underperforming LCG—is not fully reproducible, and it is unclear whether ORPO was reasonably tuned.

### Trivial
None.

## Nice-to-Haves

- **Confidence intervals or error bars** on confusion rates and task metrics in Tables 3 and 4 would strengthen the statistical claims, given the low absolute rates where a few examples can shift percentages.
- **Failure analysis**: The paper could benefit from a few qualitative examples where LCG incorrectly masks a correct token or fails to mask a confusion token, to help readers understand the method's limitations.
- **Scalability discussion**: The paper notes the gate adds 0.4% overhead but does not discuss whether the MLP size scales with the model's hidden dimension (and thus with model size), which is relevant for deployment on larger models.

## Removed Points

The following points raised in the inputs were removed with justification:

- **"Norm analysis pattern has been noted previously"** — The paper does not claim this as a novel discovery; it presents the analysis to motivate the method. Requesting a causality proof (does norm bias cause confusion?) is scope creep beyond what the paper needs to establish for its contribution.
- **"No LCB results"** — The paper provides a clear rationale for not using LCB (some queries require code-switching, detector unreliability). Requesting LCB results is scope creep; the paper's chosen evaluation methodology is valid.
- **"Comparison with neuron suppression (Nie et al., 2025) and post-hoc smoothing (Ji et al., 2025)"** — A direct comparison is not straightforward (these methods modify model weights or operate differently), and the paper already provides a reasonable related-work discussion. Requesting new experiments is beyond reasonable scope.
- **Criticisms about appendix content, missing proofs, or formatting artifacts** — The parser strips supplementary material; these are not author errors.
- **"Could the metric be measuring a proxy?" style speculation** — The harsh critic's general concern about Latin confusion false positives is retained (Weakness 4), but framing it as a fatal validity issue is disproportionate given the paper's own partitioning strategy and the relative-informativeness of the numbers.

## Novel Insights

None beyond the paper's own contributions. The key insight—that token embedding norm imbalance creates a systematic bias favoring high-resource languages, and that norm-adjusted self-distillation can train a lightweight gate to predict permissible language families—is well articulated by the authors.

## Suggestions

1. Explicitly state in Section 5.2 that Chinese target-language examples are excluded from CJ confusion evaluation, to resolve the ambiguity about FLORES-NO-LATIN.
2. Report the training hyperparameters (k and p values for pseudo-target creation, MLP hidden dimension and activation) in Section 4.2 for full reproducibility.
3. Provide basic annotation statistics (number of examples, number of annotators, agreement rate) for the code-switch preservation experiment.
4. Add a brief acknowledgment of the potential false-positive issue for Latin confusion on FLORES-NO-LATIN (proper nouns, loanwords) and, if feasible, estimate the false-positive rate via a small manual sample.
5. Report standard deviations or confidence intervals for the main results in Tables 3 and 4, or at minimum note the lack of such statistics as a limitation.

## Score and Decision

The paper presents a well-motivated, practical, and empirically strong solution to language confusion in multilingual LLMs. The method is lightweight, model-agnostic, and demonstrates consistent improvements across multiple model families and tasks without degrading performance or eliminating legitimate code-switching. The weaknesses are all minor—clarity issues, missing reproducibility details, and under-specified sub-experiments—none of which threaten the paper's core claims. The contribution is solid and the results are compelling.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>