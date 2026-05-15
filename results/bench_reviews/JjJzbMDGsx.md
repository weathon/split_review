Here is my consolidated review:

## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight plug-in MLP that operates at decoding time to filter tokens from unintended language families in multilingual LLM generation. The method is motivated by a clear mechanistic analysis showing that output token embedding norms are biased toward high-resource languages (CJ, Latin), which partially explains why LLMs mix languages during generation. LCG is trained via norm-adjusted self-distillation — using the model's own debiased top-k/p predictions as pseudo-targets — and applies sparse, rule-based masking only when confusion is detected. Across Qwen3, Llama3.1, Gemma3, and GPT-OSS, LCG reduces language confusion by roughly an order of magnitude without degrading task BLEU or accuracy, while preserving most legitimate code-switching.

## Strengths

- **Mechanistic insight validated by experiments.** The analysis in §3.2 demonstrates a clear, measurable bias: high-resource language tokens disproportionately occupy the top 5% of output embedding norms (e.g., Qwen3-8B: 10.74% of CJ tokens vs. 0.14% of Low-Res tokens in the global top 5%). This decomposition of logits into norm × cosine similarity is clean, original, and directly motivates the norm-adjusted training signal.

- **Substantial and consistent confusion reduction across diverse architectures.** Table 3 shows order-of-magnitude reductions: Qwen3-30B CJ% drops from 1.0% to 0.0% and Latin% from 4.4% to 0.4%; Llama3.1-8B Latin% falls from 8.4% to 2.9%. These gains hold across no-think and thinking models, and across both FLORES and INCLUDE benchmarks, with BLEU/accuracy preserved or slightly improved.

- **Norm-adjusted self-distillation is shown to be essential via direct ablation.** The LCG-adjusted vs. LCG-unadjusted comparison (Table 3) consistently demonstrates that training with norm adjustment yields lower confusion (e.g., Llama3.1-8B Latin%: 5.7% → 2.9%). This experimentally validates that the norm-bias insight translates into a better-trained gate.

- **Sparse intervention preserves normal generation.** The intervention rate of 0.33–0.38% of tokens (with only 0.4% per-step inference overhead) makes the method practical for deployment. The code-switch analysis (86.7% preservation at human-validated confusion points, Table 5) credibly addresses the key trade-off between correction and natural multilingual behavior.

- **Outperforms existing baselines without retraining.** LCG substantially reduces confusion compared to ICL, greedy decoding, and ORPO (Figure 3), and avoids the accuracy degradation that ORPO causes (e.g., Qwen3-8B INCLUDE accuracy: 61.4 → 57.3 with ORPO vs. 61.76 with LCG).

## Weaknesses

### Fatal

None.

### Major

- **Potential overlap between FLORES+ training and evaluation data is not addressed.** The gate's training data (§5.1) includes the FLORES+ Dataset, and the evaluation (§5.2) uses FLORES+ (partitioned into FLORES-NO-LATIN and FLORES-WITH-LATIN). The paper provides no statement that the evaluation split is disjoint from the training data, no decontamination analysis, and no mention of held-out partitioning. While the risk is somewhat mitigated because (1) the gate learns to predict only 4 language families from hidden states (not memorize specific output tokens), (2) training uses norm-adjusted pseudo-targets rather than FLORES+ labels, and (3) the INCLUDE benchmark (independent of FLORES+) also shows strong confusion reduction — the lack of any explicit separation documentation undermines confidence in the core experimental results. This is a rigor issue that must be resolved for the paper to be accepted.

- **Missing hyperparameter disclosure for training.** Section 4.2 specifies that pseudo-targets are built from top-k/p filtering of norm-adjusted logits, but the values of *k* and *p* used during training are never reported. The inference-time values are given (§4.3, Rule #2: k=5/p=0.999 and k=20/p=0.95), but it is unclear whether these same values are used for training. This hurts reproducibility.

### Minor

- **Human-validated code-switch evaluation lacks methodological detail.** The claim that "LCG-adjusted allows the English code-switch in 86.7% of human-validated examples" (§5.3) is reported with no information about the number of examples annotated, number of annotators, inter-annotator agreement, or how confusion points were identified. As presented, this evidence is thin and should be expanded.

- **No analysis of how often intervention Rule #2 overrides the gate.** Rule #2 (§4.3) skips intervention when the gate's prediction is contradicted by high-confidence model output. The paper does not analyze how frequently this rule triggers or whether it lets through genuine confusion. This is a concrete failure mode worth characterizing.

- **Table 4 reports only CJ% for thinking models on Humaneval-XL.** Latin confusion in code generation is expected (programming keywords are Latin), but the paper should state this explicitly and/or report Latin% with explanation, rather than omitting it.

### Trivial

- None.

## Nice-to-Haves

- **Comparison against direct norm-adjusted sampling at generation time.** The critic suggests comparing against always sampling from norm-adjusted logits (`logits / ||e_i||`) as a drop-in replacement. The paper argues this would be insufficient (§3.2: "it can't be directly used for intervention"), but this is stated rather than demonstrated. Adding this baseline would cleanly isolate the contribution of the learned gate from the norm-adjustment idea.

- **Reporting LCB numbers.** The paper explains why it does not use LCB (§5.2: natural code-switching and unreliable detectors). However, reporting LCB results anyway, with appropriate caveats, would help anchor the evaluation to the existing literature.

## Removed Points

- **Criticism about Table 1 percentages summing >5%.** The reviewer misread the table header. It reports the *fraction of tokens within each language family* that have norms among the global top 5%. Across-families sums are not expected to equal 5% because they are per-family percentages. Removed (factually incorrect).

- **Criticism about missing appendix/proof content.** Removed per instructions (parser artifact).

- **Criticism about not using LCB as a requirement.** Weakened to a nice-to-have (scope creep beyond the paper's stated methodology).

- **Criticism about norm-adjusted sampling being a "methodological gap".** The paper already provides LCG-unadjusted vs. LCG-adjusted ablation showing norm adjustment's contribution to training. The suggested additional baseline is a nice-to-have, not a required experiment, especially since the paper argues (and the ablation supports) that norm adjustment alone is insufficient for intervention. Moved to nice-to-have.

## Novel Insights

Both reviewer-provided analyses converge on the same core assessment: the norm-imbalance insight is genuinely novel and well-supported, but the paper's main experimental results are clouded by a notable procedural oversight (lack of explicit training/evaluation data separation for FLORES+). The interesting tension is that while the harsh critic frames this as potentially fatal, the strength finder correctly points out that the INCLUDE benchmark provides independent validation — but neither reviewer fully explored this. The gate training uses self-distillation from model outputs, not FLORES+ gold labels, so the "contamination" mechanism would be about the gate seeing similar hidden states, not memorizing answers. This nuance matters: it makes the issue less severe than classic train/evaluation label leakage, but the paper still owes the reader a clear decontamination statement.

## Suggestions

1. **Provide a decontamination statement.** Explicitly state whether any FLORES+ sentences used for training overlap with the FLORES-NO-LATIN and FLORES-WITH-LATIN evaluation subsets. Report overlap counts or splits used. This is the single most important issue to address.

2. **Disclose training hyperparameters.** Report the k and p values used for pseudo-target construction in §4.2.

3. **Expand the human evaluation details.** Report the number of examples judged, number of annotators, and inter-annotator agreement for the 86.7% code-switch preservation claim.

4. **Add Rule #2 analysis.** Report how often Rule #2 prevents intervention, and in what fraction of those cases the gate's original prediction was correct.

## Score and Decision

I compare to the following calibration anchors retrieved from the corpus:

| Anchor Path | Avg Score | Comparison to this paper |
|---|---|---|
| q8fTgw8e5E.md | 6.00 (Accept) | Mechanistic analysis of translation heads; cleaner methodology but no practical intervention. LCG has stronger engineering contribution but a contamination concern that this anchor lacks. |
| RMT6CZquly.md | 4.00 (Reject) | Tokenizer plasticity study with mixed reviews. LCG has clearer novelty and stronger empirical validation. |
| sTfIhVn7TM.md | 4.00 (Reject) | Contrastive decoding method with excessive hyperparameters. LCG is better motivated and has fewer tunable knobs. |
| zCYXhSy9UH.md | 6.67 (Accept) | Strong benchmark paper; different contribution type (dataset vs. method). LCG is weaker methodologically due to contamination concern. |
| GFDSGlEks2.md | 4.67 (Reject) | Controlled contamination study with limited scope. LCG has broader impact and practical value. |
| jCkmwIN9kz.md | 3.33 (Reject) | Contamination detection with limited novelty. LCG is stronger. |
| QOWYX3Q2XS.md | 6.50 (Accept) | Multilingual evaluation framework. Different contribution; LCG is similarly practical but less methodologically rigorous. |

Positioned relative to these anchors, the paper sits above the typical reject (4.0) papers due to its clear mechanistic contribution and broad empirical validation, but below the strong accept (6.0+) papers due to the unresolved FLORES training/evaluation overlap concern and missing experimental details. The core ideas are solid; the main weakness is procedural rather than conceptual.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>