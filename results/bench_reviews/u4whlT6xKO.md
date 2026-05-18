Here is the consolidated review:

---

## Summary

This paper introduces Divergent Chain of Thought (DCoT), a method that fine-tunes LLMs to generate multiple reasoning chains and select an answer in a single inference step. The authors show that DCoT instruction tuning consistently improves performance over standard CoT across model families (Phi, LLaMA-2) and scales (1.3B to 70B) on in-domain and out-of-domain reasoning tasks. They additionally claim that DCoT enables emergent self-correction — the later chain overrides an incorrect earlier chain — without external feedback.

## Strengths

- **Novel fine-tuning approach for multi-chain reasoning in one inference step.** The paper introduces a clean method: reformat training data so each instance bundles multiple (question, CoT) pairs, then fine-tune the model to generate k chains followed by a final answer. This is distinct from prior work like self-consistency or self-ensemble methods, which require separate inference passes. The paper shows that DCoT@1 (k=1) matches the CoT baseline, confirming that the multi-chain format does not harm single-chain performance.

- **Broad and rigorous experimental scope.** Evaluations span two model families (Phi 1.3B/2.7B, LLaMA-2 7B/13B/70B), six in-domain datasets covering diverse reasoning types (classification, span extraction, logic, conditional reasoning), four out-of-domain tasks (math, commonsense, symbolic), and BBH as a control. This sweep follows best practices from prior work (Wang et al., Yoran et al.) and provides solid evidence that the performance gains are not dataset- or model-specific.

- **Thoughtful BBH control experiment.** The authors specifically test whether DCoT could *harm* performance on tasks where even single-chain CoT is known to degrade results for smaller models. The finding that DCoT fine-tuning does not degrade BBH performance is a meaningful safety check.

- **DCoT integrates with existing CoT extensions.** The paper shows that DCoT can be combined with self-consistency to outperform CoT+self-consistency, demonstrating that the method is complementary rather than an alternative to existing techniques.

## Weaknesses

### Fatal
None.

### Major

- **The "self-correction" claim is overclaimed relative to the evidence.** The paper trains exclusively on *correct* CoTs (Section 3.3: "restrict the training data to those reasoning chains that lead to correct answers"), so the model never sees examples where some chains are correct and others are wrong, nor does it learn to explicitly detect errors. At inference, when the first chain is wrong and the second is correct, this is more parsimoniously described as "the model generates multiple correct-looking chains and one happens to be correct" than as "the model detects and corrects its first error." The paper acknowledges this in the Discussion (calling it a "side-effect"), yet still claims in the abstract and conclusion that DCoT "enables self-correction" and is "the first work to achieve self-correct ability in LLMs." This conflates a statistical side-effect of multiple sampling with deliberate revision. Prior work (Reflexion, Self-Refine) at least uses explicit verification steps or feedback loops; DCoT has no such mechanism. The manual analysis (Section 5.2) showing that the second chain "provides a different reasoning chain" establishes *diversity*, not correction. The paper does not analyze whether the model explicitly compares chains or whether the second chain acknowledges the first.

- **Missing ablation: training format is not controlled.** The CoT baseline trains on individual (question, single CoT) examples, while DCoT trains on (question, multiple CoTs) examples where multiple chains appear in context. The paper dismisses this as a "simple re-organization" (Discussion), but for the model these are different sequences with different positional dependencies and learning signals. The DCoT model sees multiple correct chains in the same context window, which could teach it to produce multiple plausible chains without teaching comparison or selection. The correct control — train a model on concatenated multiple CoTs but evaluate it on single-chain generation — is not performed. Without this, the claim that DCoT's gains come from its inference-time procedure (rather than from a training format that incidentally benefits multi-chain generation) is not fully substantiated.

### Minor

- **Best-k selection per dataset inflates headline results.** The paper reports "We run our DCoT with k ∈ [1,4] and select the best k for each dataset based on the dev set" (Section 4 Evaluation), then reports those best-k results as DCoT's main performance. While this is standard hyperparameter selection, the CoT baseline has no analogous tunable hyperparameter. Since the paper already reports DCoT@k for individual k values (via `\input{tables/dcot_k}`) and shows DCoT@1 ≈ CoT, the main results would be more transparent if they reported a fixed k (e.g., k=2) as the primary comparison, with the best-k results as supplementary.

- **The self-correction analysis does not distinguish "correction" from "ancillary correct generation."** The paper quantifies self-correction rates (gains up to 14 points) and qualitatively shows the second chain differs from the first. However, it does not measure what fraction of "self-corrections" are cases where the first chain was already partially correct, or where the second chain's reasoning explicitly acknowledges the first chain's error. Without comparing to an oracle baseline (e.g., forcing the model to commit to the first chain's answer after generating the second), the mechanism remains opaque.

- **Prompting experiments are dismissed without quantitative support.** The paper states that "the errors that are a result of the added complexity of this method almost completely offset the gains" for prompting-based DCoT, including GPT-4o. No quantitative results (e.g., accuracy rates, chain diversity statistics, error breakdowns) are reported for these experiments. While this is exploratory and the fine-tuning results are the main contribution, reporting even a small table would add credibility.

### Trivial
None.

## Nice-to-Haves

- **Statistical significance / confidence intervals.** The paper reports macro F1 but no confidence intervals or significance tests. Given the number of models and tasks, this would strengthen the reliability of the results.
- **Compute-matched comparison.** DCoT generates k chains per inference. A fair compute baseline would compare DCoT (k=2) against CoT with self-consistency using 2 samples, matching total output tokens. The paper discusses this conceptually but does not present a direct comparison.
- **Training with mixed-correctness data.** Training DCoT on data where some CoTs in the example are deliberately wrong and the final answer selects the correct one would directly test whether DCoT can learn genuine error detection and correction. This would likely produce stronger self-correction and could be a natural extension.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Not the first work to achieve self-correction"** — The harsh critic argues the claim is contradicted by the paper's own citations of Reflexion and Self-Refine. However, the paper's claim is specifically about self-correction *without external feedback or prompt optimization*, which Reflexion/Self-Refine do not achieve (they rely on external/oracle feedback or prompt engineering). The paper's novelty framing in its specific niche is defensible, though still overclaimed relative to the actual mechanism.

2. **"Missing related works"** — The rules forbid me from mentioning missing related works as I cannot verify them.

3. **"Tables not visible"** and **"Formatting issues"** — These are parser artifacts from \input commands being stripped; the original submission has these tables.

4. **"CoT baseline unfair comparison" exaggerated framing** — The harsh critic treats this as a "Structural" issue undermining the entire comparison. The paper does provide DCoT@1 ≈ CoT as a control, partially mitigating the concern. The remaining concern (training format) is kept as a minor weakness above.

5. **Criticisms about missing appendix content, hyperparameter details, or trivial implementation details** — These are nitpicks about reproducibility that the rules instruct me to remove.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Dial back the self-correction narrative.** Reframe DCoT's later-chain improvement as "beneficial side-effect of generating multiple divergent chains" rather than "self-correction." The paper's evidence supports diversity-based improvement, not error detection and correction. The claim "first work to achieve self-correct ability" should be dropped or sharply qualified.

2. **Add the training-format ablation.** Train a model on DCoT's concatenated multi-chain format but evaluate it with single-chain generation (k=1). If this model matches DCoT's performance, the gains come from training format, not inference procedure. If DCoT still outperforms, the mechanism claim is strengthened.

3. **Report results at k=2 as the primary comparison.** Since DCoT@1 matches CoT, the main result should emphasize k=2 (the minimal nontrivial case) without per-dataset tuning. Supplement with the best-k results.

4. **Include oracle-baseline analysis for self-correction.** On cases where the first chain is wrong and the final answer is correct, measure whether the model would perform worse if forced to output the first chain's answer. This would distinguish correction from independent correct generation.

5. **Report quantitative results from the prompting experiments.** Even a brief table showing GPT-4o's accuracy with DCoT prompting vs. standard CoT would substantiate the claim that prompting alone is insufficient.

## Score and Decision

**Anchor calibrations:** All anchors come from the calibration corpus.

| Anchor | Avg Score | Comparison to this paper |
|--------|-----------|--------------------------|
| "Large Language Models Cannot Self-Correct Reasoning Yet" (`IkmD3fKBPQ.md`) | 6.75 | Stronger methodology and more defensible claims about self-correction; this paper is weaker on both dimensions |
| "SuperCorrect" (`PyjZO7oSw2.md`) | 6.50 | Cleaner evidence chain and more rigorous evaluation; this paper has broader scope but weaker mechanistic support |
| "Flow of Reasoning" (`HHmnfVQagN.md`) | 5.75 | Comparable quality — both have interesting core ideas but overclaim and lack sufficient analysis |
| "LLMs have Intrinsic Self-Correction Ability" (`pTyEnkuSQ0.md`) | 5.25 | Similar quality band; this paper's idea is more novel but its claims are similarly overextended |
| "Mind Your Step" (`rpbzBXdo4x.md`) | 5.00 | Slightly weaker methodology but clearer framing; DCoT has broader experiments |
| "Critique Ability of LLMs" (`50P9TDPEsh.md`) | 4.67 | Both have interesting questions but insufficient evidence for central claims |
| "Improving AI via Novel Computational Models" (`NlY3XppPt3.md`) | 2.00 | This paper is substantially stronger in experimental scope, clarity, and contribution |

**Score rationale:** The paper presents a genuinely novel fine-tuning approach for multi-chain reasoning in a single step, backed by broad experiments across model families, sizes, and task types. The BBH control and DCoT@1 ≈ CoT baseline are thoughtful methodological choices. However, the self-correction narrative is overclaimed relative to the evidence (the model does not learn error detection), and a key ablation controlling for training format is missing. The core contribution — that fine-tuning on bundled multi-chain data yields performance gains — is solid, but the mechanistic explanation is not. Relative to the calibration anchors, the paper sits below the well-executed papers (6.5–6.75) and somewhat above the clearly flawed ones (4.25–5.0). A score of 5.0 reflects a paper with a real contribution undermined by overclaiming and insufficient mechanistic evidence.

**MY FINAL SCORE:** <pineapple>5.0</pineapple>

**MY FINAL DECISION:** <orange>Reject</orange>