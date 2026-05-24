Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight two-layer MLP that operates as a plug-in at decoding time to reduce language confusion in LLMs. LCG is trained via norm-adjusted self-distillation, leveraging the finding that token embedding norm imbalance biases models toward high-resource languages. It dynamically masks tokens from inappropriate language families while preserving legitimate code-switching. Evaluation across Qwen3, Llama3.1, Gemma3, and GPT-OSS on FLORES, INCLUDE, and HumanEval-XL shows confusion reductions of 4–45× with <0.4% overhead and no degradation in task accuracy.

## Strengths

1. **Novel mechanistic finding with direct practical application.** Section 3.2 demonstrates that token embedding norm imbalance biases models toward high-resource languages (Table 1: Qwen3-8B has 10.74% CJ tokens vs. 0.14% Low-Res tokens in the top-5% of embedding norms), and norm adjustment reveals correct-language tokens in top-10. This finding is well-supported and directly motivates the training procedure.

2. **Norm-adjusted self-distillation is cleanly ablated.** Table 3 compares LCG-unadjusted vs. LCG-adjusted across four models. The adjustment consistently reduces confusion further (e.g., Llama3.1-8B Latin% drops from 5.7% to 2.9%; Qwen3-8B Latin% drops from 6.2% to 2.0%), validating that the norm-adjustment component provides genuine signal improvement beyond vanilla self-distillation.

3. **Preserves legitimate code-switching, a nuanced requirement.** Unlike rule-based or retraining methods that penalize all language mixing, LCG retains 86.7% of human-validated code-switch tokens (Section 5.3), and post-intervention code-switch rates remain above the Claude Sonnet 4 reference and near ground-truth answer rates (Table 5). This directly addresses the practical challenge raised in Section 3.3.

4. **Genuinely lightweight and practical.** The gate adds 0.4% overhead (15.95ms → 15.99ms per step) and is compatible with speculative decoding. The plug-in design means no base-model retraining, and the sparse intervention rate (0.33–0.38% of tokens) ensures negligible impact on normal generation.

5. **Broad evaluation coverage.** Results span four no-think models (Qwen3-30B, Qwen3-8B, Llama3.1-8B, Gemma3-12B) and three thinking models (Qwen3-8B, Qwen3-30B, GPT-OSS) on separate benchmarks appropriate to each regime, demonstrating generalizability.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison to the most directly relevant decoding-time baselines.** The paper cites Nie et al. (2025) — neuron suppression at inference time — and Ji et al. (2025) — post-hoc smoothing that identifies and suppresses Chinese tokens during decoding — as prior methods that operate at decoding time without retraining (Section 2). These are the closest prior approaches to LCG's setting. The paper evaluates against ICL, greedy decoding, and ORPO (training-based), but not against Nie et al. or Ji et al. Without this comparison, it is impossible to assess whether LCG improves upon existing plug-in interventions or simply underperforms them. The paper's claim of advancing beyond "some require model retraining" (Section 2) leaves the state-of-the-art among the retraining-free methods unestablished.

### Minor

2. **No statistical uncertainty or variance reported.** All confusion rates, BLEU scores, and accuracy figures are reported as point estimates (e.g., CJ% 4.5% → 0.1%, BLEU 12.1 → 12.1). Given the low base rates of confusion (many values below 1%), these differences could be within noise. No confidence intervals, bootstrap estimates, or significance tests are provided. This is especially relevant for the thinking-model results (Table 4), where absolute reductions are tiny (e.g., Qwen3-30B CJ% 0.12% → 0.00%).

3. **Training hyperparameters (k/p values) for pseudo-target construction are not specified.** Section 4.2 defines pseudo-targets using `S_{k,p}(logits_adjust)` (top-k/top-p filtering on norm-adjusted logits) but never states the specific k and p values used during training. The intervention rules (Section 4.3) use (k=5, p=0.999) and (k=20, p=0.95), but it is unclear whether these same values are used for training. This under-specifies the training procedure.

4. **Norm-adjustment-immune confusion cases not quantified.** The paper explicitly acknowledges (Section 3.2) that norm adjustment "cannot fully explain language confusion" and gives examples (English-Chinese, low-resource vs. low-resource). For these cases, norm-adjusted top-k/p may still contain only wrong-language tokens, making pseudo-targets incorrect. The paper does not measure (a) how often this occurs, or (b) how LCG performs specifically on such cases. While the aggregate results are positive, the scope of confusion types that the method can address is not characterized.

5. **Human evaluation for code-switch preservation lacks detail.** Section 5.3 reports that LCG allows English code-switch tokens in 86.7% of "human-validated examples," but the number of examples, annotation process, and inter-annotator agreement are not described. This makes it difficult to assess the reliability of this important claim.

### Trivial

6. **Wording inconsistency: "infrequent" in the abstract vs. Table 3 results.** The abstract states "language confusion is infrequent," yet Qwen3-8B has 12.1% Latin confusion (per-response rate on FLORES-NO-LATIN, Table 3). The paper later reports a token-level intervention rate of 0.38%, so the intended meaning is token-level infrequency, but the abstract is ambiguous.

## Nice-to-Haves

- Reporting results on a filtered subset of the Language Confusion Benchmark (LCB) (removing queries that require natural code-switching) would enable direct comparison to prior LCB-based quantitative results. The paper's rationale for not using LCB (Section 5.2) is reasonable, but a supplemental LCB analysis would strengthen comparability.
- An error analysis of gate predictions (false positives where a legitimate token is masked, false negatives where an erroneous token is allowed) would help characterize gate behavior.
- A sensitivity analysis of the k/p parameters used in pseudo-target construction would demonstrate robustness.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Paper does not acknowledge within-script confusion limitation"** — REMOVED. The paper explicitly states this in Section 6: "the current approach is limited by its script-level granularity… cannot resolve more nuanced confusion between languages that share the same script (e.g., Spanish vs. English) or between two different low-resource languages." The harsh critic claimed this was unacknowledged, which is factually wrong.

2. **"LCB rationale is thin and unsupported"** — REMOVED. The paper provides a clear, explicit rationale with two concrete reasons (Section 5.2). Even if one disagrees with the choice, this is a methodological preference difference, not an error or omission.

3. **"Section 2 claim of outperforming 'other approaches' is unsubstantiated"** — REMOVED. The paper does not claim to outperform all approaches in Section 2. It says "Our work addresses these gaps" — specifically retraining requirement and inability to distinguish legitimate code-switching. The outperformance claim is made only for training-based methods (ORPO) in Section 5, which is supported by experimental data.

4. **"Section 3.2 claim about English-Chinese confusion is without evidence"** — REMOVED from weaknesses tier. The paper presents this as a conceptual limitation of the norm-adjustment view, not as a quantitative finding. It's an honest acknowledgment of scope, not an unsupported claim.

## Novel Insights

The reviews collectively surface one genuinely novel observation not spelled out in the paper: the self-distillation training procedure depends on norm adjustment to produce correct pseudo-targets, but for confusion types where norm adjustment does not help (same-script confusion, both-high-norm confusion), the training signal is inherently degraded. This means LCG may work best for the subset of confusion caused by norm imbalance, and its effectiveness for other confusion types is currently untested. This is a useful framing of the method's implicit scope that the authors could explicitly characterize in a revision.

## Suggestions

- Add experimental comparisons to the neuron-suppression method of Nie et al. (2025) and the post-hoc smoothing of Ji et al. (2025) — these are the most directly comparable decoding-time interventions. Without this, the paper's claim of advancing the state-of-the-art among plug-in methods cannot be evaluated.
- Specify the k/p values used for pseudo-target construction during training. If they differ from the intervention-rule values, explain the choice.
- Add confidence intervals (e.g., bootstrap estimates) for confusion rates, especially for thinking-model results where base rates are below 1%.
- Quantify the fraction of confusion cases where norm-adjusted top-k/p does not contain the correct language, and report LCG's performance on this subset explicitly.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>