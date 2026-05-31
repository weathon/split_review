Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

The paper introduces M-Longdoc, a benchmark of 851 QA samples across 180 multimodal documents averaging 210.8 pages each—far exceeding prior benchmarks in document length—along with an automated evaluation framework using multiple judge models. It also proposes a retrieval-aware tuning approach that fine-tunes Qwen2-VL-7B on both relevant and distractor pages to improve robustness to noisy retrieval contexts, reporting consistent but modest improvements over the untuned baseline.

## Strengths

1. **Document length dramatically exceeds prior benchmarks.** Table 1 shows M-Longdoc averages 210.8 pages and ~121K tokens per document, versus 47.5 pages and ~2K tokens for the next largest benchmark (MMLongBench). This directly fills a gap in evaluating models on realistic long-document scenarios.

2. **Two-stage verification pipeline ensures question quality.** The data construction (Section 3) uses automated checks (80.1% pass rate) followed by expert human verification (80.9% of those pass), yielding a rigorous filtering process. Expert annotators are appropriately matched to domain (Ph.D. students for academic, professionals for finance/product).

3. **Automated evaluation achieves strong correlation with human judgments.** The paper reports a Pearson correlation of 88.9% (p<0.001) between aggregated judge-model scores and human annotator scores on 100 samples (Section 4.4), demonstrating that the automated framework is a reasonable proxy for human evaluation at scale.

4. **Consistent improvements across all domains and question categories.** Table 5 shows Qwen2-VL with retrieval-aware tuning outperforms the untuned baseline on every domain (Academic, Product, Finance) and every question type (Text, Figure, Table), with the improvement being uniform rather than concentrated in one area.

5. **Alternative-settings analysis demonstrates the necessity of multimodal inputs.** Table 6 shows removing image inputs drops figure-based scores from 3.83 to 3.37 and table-based scores from 3.62 to 3.38, while using only rendered page images is suboptimal compared to extracted text+images—supporting the paper's multimodal design choices.

## Weaknesses

### Major

- **No ablation isolating the retrieval-aware design from standard SFT.** The main results (Table 5) compare Qwen2-VL-7B untuned (3.84) vs. the tuned version (4.02), but there is no control condition trained on gold-page-only data (without distractors). The improvement (~4.7% relative) could come entirely from supervised fine-tuning on the high-quality training corpus (which the paper itself scores at 4.82/5 on a subset), rather than from the retrieval-aware distractor component specifically. Without this ablation, the central methodological claim—that the *retrieval-aware* design drives improvement—is not supported. This is the single most important missing experiment.

### Minor

- **Evaluation framework validation is limited.** The 88.9% Pearson correlation with human judgments is computed on only 100 samples from the same set used in the preliminary study. The paper does not report: (a) inter-judge agreement among the three judge models, (b) variance of scores across judges, (c) stability of the evaluation across different random subsets, or (d) whether the judge models (presumably the proprietary models) overlap with the evaluated models, which could introduce bias. While the approach is reasonable, the validation is not yet sufficient for a benchmark that aims to rank models.

- **Reproducibility gaps in the training procedure.** Section 5.3 specifies epochs, batch size, learning rate, and LoRA parameters, but does not specify: how many distractor pages are provided during training (the "N" in Figure 6), how distractors are selected (from the same document or others, random or retrieval-based, whether their modality distribution is controlled), or whether the gold page is always guaranteed to be in the top-N. These details are essential for reproducing the method's core component.

- **Method novelty is incremental relative to prior work.** The paper explicitly acknowledges being "inspired by" RAFT (Zhang et al., 2024) and MuRAG (Chen et al., 2022), which also train generators on both relevant and irrelevant retrieved contexts. The claimed novelty—"first to directly address the retrieval setting for multimodal long documents" (line 6)—is a narrow domain application rather than a methodological advance, and the experiments do not demonstrate that the multimodal long-document setting introduces unique challenges requiring a solution beyond straightforward adaptation of these existing approaches.

- **Training data quality verification relies on an untested assumption.** The paper states (line 282) that human verification is omitted for the training corpus because "majority of the automatically verified samples also satisfied human verification," citing the benchmark set's 80.9% agreement rate. However, this rate was measured on the benchmark set, not the training set, and the two sets may have different properties (different documents, no human filtering). The training answers score 4.82/5 on the automated evaluation—suspiciously near-ceiling—which may reflect judge-model self-bias rather than genuine human-judged quality.

- **No statistical significance reported for main results.** Given the moderate benchmark size (851 questions, broken into subcategories of ~280), the observed differences between models (e.g., 3.84 vs. 4.02) may or may not be statistically meaningful. Confidence intervals or significance tests would strengthen the claims.

### Trivial

- The improvement magnitude is modest (~4.7% relative, or 0.18 points on a 5-point scale). The paper's framing using a placeholder (`\performanceincrease{}`) prevents readers from immediately assessing the effect size.

## Nice-to-Haves

- Reporting inter-judge agreement and variance across judge models would strengthen confidence in the evaluation framework.
- An analysis of failure cases of the tuned model (where does it still struggle?) would contextualize the improvements and guide future work.
- Statistical significance or confidence intervals for the main results would help readers assess whether differences are reliable, although this is not yet standard practice in all LM benchmarking papers.

## Removed Points

- **Placeholder formatting complaints (`\performanceincrease{}`, etc.):** These are parser artifacts from the PDF extraction; the original submission contains the actual values. Removed per rules that parser artifacts are not author errors.
- **Criticism that the benchmark "scale is small" (851 questions):** This is generic; for a specialized, human-verified benchmark over documents averaging 210 pages, 851 questions is a reasonable starting size. Demoted as a one-size-fits-all criticism.
- **Criticism that the preliminary study "uses only 100 samples and two models":** This study is explicitly preliminary and scoped as such; it is used to motivate the method, not to draw definitive conclusions. Removed as a scope-creep criticism.
- **Strength about "consistent and substantial improvements" (from Strength Finder):** The improvement is consistent but modest (~4.7% relative). The word "substantial" overstates the evidence; rephrased in the strengths list above to "consistent but modest."

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective not already present in the paper's framing.

## Suggestions

1. **Add the critical ablation:** Train the same model on the same corpus but *without* distractor pages (gold-page-only context). If tuned⁻distractor performs similarly to the full method, the retrieval-aware design is not contributing. If it performs worse, the paper has a genuine finding.
2. **Specify distractor selection details:** Number of distractors, selection strategy (random vs. retrieval-based, same-document vs. cross-document), and whether the gold page is always included.
3. **Strengthen evaluation validation:** Report inter-judge agreement, score distributions, and correlate with human judgments on a held-out set (not the same 100-sample subset used to motivate the design).
4. **Clarify judge model identities:** State which specific models serve as judges and whether they overlap with the evaluated models, to address potential self-bias concerns.
5. **Tone down the method novelty claims** or provide stronger evidence that the multimodal long-document setting requires a solution beyond a straightforward adaptation of RAFT/MuRAG.

## Score and Decision

The paper's benchmark contribution—both the dataset and the evaluation framework—is solid and fills a genuine gap (documents an order of magnitude longer than prior benchmarks, with open-ended questions). The method contribution, however, is weakly supported: the key ablation (retrieval-aware design vs. standard SFT) is missing, the improvement is modest, and the novelty is incremental. The benchmark alone is a worthwhile contribution that justifies acceptance, but the method claims need substantial strengthening.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>