Here is my synthesized final review.

---

## Summary

This paper introduces M-Longdoc, a benchmark of 851 question-answer samples over multimodal documents averaging 210 pages (substantially longer than any existing benchmark), requiring open-ended reasoning rather than extractive answers. It also proposes a retrieval-aware tuning framework that includes distractor pages during fine-tuning to make models more robust to noisy retrieved context, and an automated evaluation framework using multiple judge models that achieves 88.9% Pearson correlation with human annotators.

## Strengths

- **Benchmark documents are an order of magnitude longer than existing ones**: M-Longdoc averages 210.8 pages and ~121K tokens per document, compared to the next-longest benchmark (MMLongBench) at 47.5 pages (Table 1). This directly addresses a genuine gap — real-world business, legal, and academic documents are routinely hundreds of pages long.

- **Open-ended, reasoning-heavy questions go beyond extractive spans**: Questions require explanatory answers that draw on multimodal content (e.g., explaining *why* a trend occurs using both a bar chart and associated text), unlike prior benchmarks that largely ask for short extractive spans.

- **Automated evaluation framework shows high correlation with human judgment**: A pilot study on 100 samples reports an 88.9% Pearson correlation (p<0.001) between the multi-judge aggregate and human annotators (Section 2.4). This enables scalable, reproducible evaluation of open-ended answers without requiring reference responses.

- **Rigorous data construction with multi-stage verification**: Questions pass both an automated checklist (80.1% acceptance) and human verification by domain experts (80.9% of those accepted). Documents are sourced from after January 2024 to mitigate data contamination.

- **Preliminary study reveals specific weaknesses of current models**: The study documents multimodal bias (lower scores on figure/table questions vs. text) and susceptibility to irrelevant context even with retrieval augmentation — a useful empirical finding in its own right.

## Weaknesses

### Fatal
None.

### Major
- **No ablation isolating the retrieval-aware component from standard fine-tuning.** The experiments compare tuned Qwen2-VL (with distractor pages) only against the *untuned* Qwen2-VL (Table 3). There is no comparison against standard supervised fine-tuning on the same question-answer pairs *without* distractor pages. The reported improvement of ~4.7% relative could be entirely due to in-domain fine-tuning rather than the retrieval-aware noise. Without this control, the central claim about the retrieval-aware component's effectiveness is not established. (The benchmark contribution stands independently, but the tuning method's contribution is unsubstantiated as submitted.)

### Minor
- **Results are demonstrated on only one tuned model.** The paper acknowledges that LLaVA-OneVision could not be tuned due to "training instabilities" (line 313), but this limits the generality of the approach. Without results on at least one additional model architecture, readers cannot assess whether the tuning procedure is broadly applicable or specific to Qwen2-VL.

- **Distractor selection strategy is underspecified for reproducibility.** The method description (Section 4, Figure 6 caption) states that training includes "potentially irrelevant pages" alongside the gold evidence, but does not detail how distractors are selected (random? from same document? same domain? how many distractors per example?). This is critical for reproducibility.

- **Retrieval quality (recall) is not reported.** The setup uses top-5 pages from ColPali. The model's absolute accuracy is upper-bounded by whether the gold evidence page appears in those five retrieved pages. Without reporting retrieval recall (e.g., Recall@5), it is impossible to distinguish model weaknesses from retrieval failures. This does not affect the *relative* comparison (tuned vs. untuned use the same retrieval), but it weakens the interpretation of absolute scores.

- **\performanceincrease{} placeholder is left unfilled.** The abstract, Section 5.1, and conclusion all contain "\performanceincrease{}" instead of the actual computed improvement (~4.7% relative, calculable from Table 3). While the number is derivable, the placeholder makes the submission appear incomplete.

- **No statistical significance or confidence intervals.** The gain of 0.18 on a 5-point scale over 851 questions may be statistically significant, but the paper does not report any significance testing or confidence intervals to support the claim that the improvement is "significant."

### Trivial
- The \trainsize{} and \datasize{} macros are also unfilled (likely style-file templates), leaving the actual training corpus and benchmark sizes unspecified in the extracted text.

## Nice-to-Haves
- Qualitative examples showing where the tuned model corrects a baseline error and where it still fails would help illustrate what behavior the tuning induces.
- LoRA hyperparameter sensitivity analysis (rank, alpha) — standard reporting but not essential.
- Large-scale expansion of the benchmark (851 questions is modest compared to DocVQA's 50k).
- Per-judge agreement statistics (e.g., Fleiss' kappa) beyond the aggregate Pearson correlation.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"First" claim is overly strong due to MuRAG and RAFT.** — The paper qualifies the claim with "to our knowledge" and specifies "multimodal long documents." MuRAG (Chen et al., 2022) addresses multimodal knowledge retrieval (not specifically long document settings) and RAFT (Zhang et al., 2024) is text-only. The claim is appropriately scoped. REMOVED: strawman.

- **LoRA hyperparameters not analyzed.** — This is a generic nitpick. Picking rank=64, alpha=32 is standard LoRA practice; exhaustive hyperparameter sweeps are not required for a systems/empirical paper. REMOVED: generic nitpick.

- **No qualitative examples of success/failure.** — Nice-to-have, not a weakness. REMOVED to Nice-to-Haves.

- **Missing related works.** — As per policy, I do not have external sources to verify this. REMOVED.

- **Formatting/style/typo nitpicks.** — These are parser artifacts. REMOVED.

- **Reproducibility concerns about undisclosed hyperparameters or training details beyond what's already provided.** — Batch size, learning rate, epochs, LoRA rank, temperature are all reported. No significant details are missing. REMOVED.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a critical methodological gap (missing SFT ablation) but do not offer a genuinely novel observation about the field beyond what the authors already present.

## Suggestions

1. **Add the critical ablation**: Fine-tune Qwen2-VL on the same training corpus but with only the gold evidence page (no distractors). Compare this "SFT without distractors" condition to the reported "w/ Retrieval Tuning" result. If the gap is small or zero, the retrieval-aware claim is unsupported and should be scaled back; if large, it validates the core contribution.

2. **Report retrieval recall**: Compute and report Recall@5 of the gold evidence page on the benchmark, broken down by question category. This contextualizes all generator scores and helps the community understand where the bottleneck lies (retrieval vs. generation).

3. **Either add a second tuned model** (attempt tuning on LLaVA-OneVision or a more stable variant like InternVL2 or Phi-3-Vision, documenting any failures) or explicitly qualify the claims as "demonstrated on Qwen2-VL."

4. **Replace the \performanceincrease{} placeholder** with the actual computed number (~4.7% relative improvement).

5. **Specify the distractor selection strategy** in Section 4 to enable reproducibility.

## Score and Decision

**Originality**: 7/10 — The benchmark is a clear advance in scale (210 pages vs. ~50); the tuning method is simple but well-motivated.  
**Importance of research question**: 8/10 — Long multimodal document understanding is practically important and under-studied.  
**Claims well-supported**: 5/10 — The benchmark and evaluation framework are well-validated; the tuning method's central claim is not (missing ablation, single model).  
**Soundness of experiments**: 6/10 — Benchmark construction is rigorous; tuning experiments lack a crucial control.  
**Clarity**: 7/10 — Well-structured but marred by unfinished placeholders (\performanceincrease{}).  
**Value to community**: 8/10 — A longer, more realistic benchmark for multimodal document QA fills a clear gap.

The benchmark and evaluation framework represent a genuine contribution. The tuning method is interesting and shows promising results, but the missing ablation prevents attribution of the gain to the retrieval-aware component. This is fixable in revision and does not invalidate the benchmark contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>