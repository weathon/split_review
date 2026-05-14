Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

---

## Summary

This paper proposes Steady Thought (ST), a thought-level preference optimization framework to mitigate the "under-thinking" phenomenon in Large Reasoning Models—where models frequently abandon promising reasoning paths by switching thoughts unnecessarily. ST operates in three stages: (1) entropy-based thought segmentation of model responses, (2) forced thought completion via logit suppression of switch-triggering tokens, and (3) fine-grained preference optimization (STPO) that treats the forced completion as chosen and the original switched trajectory as rejected. Experiments across three model scales (1.5B, 8B, 14B) and four benchmarks (MATH500, AIME 2024, GSM8K, LiveCode) demonstrate accuracy improvements of up to 5.3% with token reductions of 19–39%.

## Strengths

- **Novel problem framing.** The paper formalizes under-thinking as a preference optimization problem at the thought level (Section 2.1), moving beyond global token suppression to a more selective mechanism that penalizes abandoning promising thoughts while preserving productive exploration. This is a conceptually clean and well-motivated advance over prior work (NoThink, NOWAIT, SEAL) that applies suppression indiscriminately.

- **Strong and consistent empirical results across scales and tasks.** Table 1 shows ST improves Qwen3-8B average accuracy by 3.12% while reducing tokens by 23.6%; on the 1.5B model, a 1.9% accuracy gain with 24.9% token reduction. Crucially, gains transfer to LiveCode (OOD, +5.3% accuracy, −19.0% tokens for Qwen3-8B), indicating the method teaches transferable reasoning patterns rather than dataset-specific heuristics.

- **Convincing behavioral evidence for the claimed mechanism.** Table 8 (Appendix C) quantifies that ST reduces invalid switches (T→F) much more than valid switches (F→T). For the 1.5B model on AIME 2024, valid switches actually increase by 69.4%, directly refuting the alternative hypothesis that ST merely produces shorter but shallower reasoning. Figure 2 further confirms deeper commitment via increased final-thought proportion.

- **STPO effectively addresses length bias in preference data.** Table 4 demonstrates STPO outperforms DPO (84.4% vs. 82.6% on MATH500) with substantially shorter outputs (2809 vs. 4273 tokens), validating the SimPO-inspired length-normalized formulation for the thought-level setting.

- **Practical data construction cost.** Appendix E reports only ~36M tokens on a single A100 for the 1.5B model, making the approach feasible for research adoption.

## Weaknesses

### Fatal

None.

### Major

- **Entropy threshold selected on evaluation benchmarks (test-set optimization).** Section 4.4.3 (Table 3) and Appendix D (Table 9) select the entropy threshold based on downstream accuracy and token count on MATH500 and AIME 2024—the same benchmarks used for final evaluation. While the threshold is a single scalar and adjacent values show modest differences (~1–2 pp accuracy), this constitutes hyperparameter tuning on test data. Best practice would use a held-out validation split from the training distribution (omni-math). The OOD LiveCode results partially mitigate this concern by providing independent evidence, but the reported MATH500 and AIME 2024 metrics should be interpreted as potentially optimistic by a small margin.

- **Missing ablation isolating thought-level conditioning.** The training method comparison (Table 4) evaluates SFT, DPO, and STPO, but none of these baselines uses the same chosen/rejected pairs without thought segmentation (e.g., SimPO on full original vs. full completion responses). Without this, the added value of conditioning on the shared thought prefix (Q, T_i) rather than simply training with shorter preferred responses remains unquantified. The NTS/NIS/NVS analysis (Table 8) provides indirect evidence that the mechanism works as intended, but a direct ablation would substantially strengthen the contribution claim.

### Minor

- **Quality of forced completions beyond final-answer correctness is unverified.** Section 3.2 generates chosen responses by suppressing switch-token logits and filters them by final-answer correctness. The paper does not analyze whether the intermediate reasoning in these forced completions is coherent, logically sound, or merely happens to reach the right answer through superficial steps. Low-quality completions would inject noise into the preference signal. Showing a few completion examples or a stepwise coherence evaluation would address this.

- **Thought-level training/inference gap not directly tested.** STPO trains the model on artificially segmented contexts (Q, T_i) where T_i is an explicit thought prefix. During normal autoregressive decoding, no such explicit boundary is provided. While the empirical results (accuracy gains, selective switch reduction) suggest the learned preference transfers to natural generation, a direct analysis (e.g., probing whether the model's internal representations at entropy-spike boundaries shift after ST training) would strengthen the mechanistic claim.

### Trivial

- **Segmentation evaluation reports precision (85%) but not recall** (Appendix F). Reporting recall against the LLM-based segmentation reference would give a more complete picture of segmentation quality.

- **Table 1 caption** states "two large reasoning models" while the text discusses three (1.5B, 8B, 14B). The 14B results appear only in prose; ensuring all three models appear in the main results table would improve clarity.

## Nice-to-Haves

- **Adaptive switch suppression.** The predefined token list for thought completion (Table 5) is large (100+ tokens) and hand-curated. A learned or adaptive suppression mechanism would reduce reliance on manual engineering and improve cross-model transfer.

- **Validation-set-based threshold selection.** Re-running threshold selection on a held-out split of omni-math would eliminate the test-set tuning concern and produce more reliable reported numbers.

- **Completion quality case studies.** Including 2–3 side-by-side examples of forced completions with commentary on reasoning quality would help readers assess the training signal's reliability.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"The steadiness score is an unnecessary abstraction"** — This is a stylistic objection. The steadiness score (Section 2.1) provides a formal bridge from the under-thinking phenomenon to the Bradley-Terry preference framework. Whether the formalism is "necessary" is a matter of taste; it does not constitute a weakness.

2. **"PCT metric is ambiguous / a lower PCT could mean fewer correct intermediate thoughts overall, not necessarily better switching decisions"** — The paper explicitly addresses this through the NTS/NIS/NVS analysis in Appendix C (Table 8), which decomposes switches by type (valid vs. invalid) and directly tests the mechanism. The main text (Section 4.4.2) cites Appendix C for this purpose. The concern is already addressed.

3. **"Appendix C not cited in the main text"** — Factually incorrect. Section 4.4.2 states: "We further discuss the benefits that ST brings to the model through thought-level preference optimization in the Appendix C."

4. **"14B model absent from Table 1"** — The parsed PDF text shows a garbled Table 1 with no data rows visible (parser artifact). The original submission likely contains the full table. Even if the table only shows two models in the original, this is a presentation detail, not a substantive weakness.

5. **"Test-set optimization renders the main experimental evidence invalid"** — Overstated. The threshold differences are modest (adjacent values differ by ~0.8–2 pp accuracy), all threshold settings beat baselines, and LiveCode (OOD) provides independent corroboration. The concern is real (see Major weaknesses) but does not "invalidate" the evidence.

6. **"The paper provides no argument or experimental evidence that the thought-context training signal translates to improved switching behavior under standard sampling"** — Overstated. The empirical results (Table 1 accuracy + token reduction) and the detailed switch-type analysis (Table 8) constitute evidence of translation to standard sampling. The mechanism may not be proven, but evidence exists.

## Novel Insights

The paper's most distinctive insight is the decomposition of under-thinking into a preference between two trajectory types sharing a common thought prefix—commit vs. switch—and the demonstration that preference optimization at this granularity can selectively suppress invalid switching while preserving (and in hard cases even enhancing) valid exploration. Table 8's finding that valid switches increase by 69.4% for the 1.5B model on AIME 2024 while invalid switches decrease is a compelling empirical phenomenon that challenges the default assumption that efficiency measures necessarily trade off against exploration. This granular, switch-type-aware perspective on reasoning efficiency is a useful lens beyond the specific method proposed.

## Suggestions

- **Add a SimPO-on-full-responses baseline** (using the same chosen/rejected pairs but without thought segmentation) to Table 4. This is the most direct way to isolate the value of thought-level conditioning and would address the major ablation gap.

- **Report threshold sensitivity on a held-out validation split** rather than on MATH500/AIME 2024 directly. Even a small held-out subset of omni-math would resolve the test-set tuning concern.

- **Include 2–3 forced-completion examples** with brief commentary on reasoning coherence, even if only in the appendix, to give readers confidence in the training signal quality.

- **Report segmentation recall** alongside the 85% precision in Appendix F for completeness.

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Decision | Comparison to Steadythought |
|--------|-----------|----------|-----------------------------|
| LCPO (`8xSU8Oscvg`) | 5.00 | Accept (Poster) | Closest comparator. Both use preference optimization for LRM length reduction. ST has more novel framing (thought-level vs. full-response), broader model coverage, deeper mechanism analysis (switch-type decomposition), and improves accuracy rather than just maintaining it. ST's test-set threshold tuning is a methodological concern not present in LCPO. Overall ST is stronger. |
| OptimalThinkingBench (`N5kWa3sRJt`) | 5.33 | Accept (Poster) | Benchmark paper with different contribution type. Both have strong motivation around under-thinking. ST's methodological concern (test-set tuning) is more serious than the benchmark's concerns (dataset bias, lack of formal definitions), so ST scores comparably or slightly below. |
| PALU (`msKQYIfgVm`) | 5.00 | Reject | Both frame reasoning efficiency as optimization. PALU was rejected despite strong theoretical framing due to limited model evaluation, hyperparameter sensitivity, and evaluation concerns. ST has broader model coverage and more thorough behavioral analysis. ST is stronger. |
| TBO (`esXvdhwUQ5`) | 3.50 | Reject | Also has test-distribution tuning as a criticism plus other issues (implausible numbers, limited baselines). ST is clearly stronger on experimental rigor and contribution clarity. |
| PREMISE (`gFSQNmBXx1`) | 2.67 | Reject | Prompt-only method with weaker baselines and outdated datasets. ST is substantially stronger. |

ST sits above the borderline. Compared to LCPO (accepted at 5.00), ST offers more novelty in framing, stronger accuracy improvements, better mechanism analysis, and OOD generalization evidence. The test-set threshold tuning is a legitimate concern but affects only one scalar hyperparameter with modest inter-threshold variance, and the OOD LiveCode results provide independent corroboration. The missing thought-level conditioning ablation is addressable and does not threaten the core empirical story given the switch-type decomposition evidence.

**Originality:** Good. Thought-level preference optimization for under-thinking is a novel framing that advances beyond prior global-suppression methods.

**Importance:** High. Under-thinking is a recognized and practically significant problem in deployed LRMs; methods that improve both accuracy and efficiency have clear value.

**Claim support:** Mostly strong, with two caveats noted above (test-set tuning, missing ablation). The behavioral evidence (Table 8, Figure 2) is particularly persuasive.

**Soundness:** Acceptable but imperfect. The core pipeline is sound; the threshold selection procedure and ablation gaps are shortcomings that should be addressed but do not undermine the central findings.

**Clarity:** Good. The three-stage framework is clearly described, and the figures effectively communicate the phenomenon and results.

**Value to community:** Moderate-to-high. The thought-level preference optimization paradigm and the switch-type analysis framework are likely to influence follow-up work on reasoning efficiency.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>