- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 8, 6, 6
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

MME-RealWorld introduces a large-scale (29,429 QA pairs), high-resolution (avg. 2000×1500 pixels), fully human-annotated benchmark for evaluating multimodal LLMs across 43 subtasks in 5 real-world domains (OCR, remote sensing, diagrams/tables, autonomous driving, monitoring). The paper evaluates 29 models and finds none exceed 60% accuracy, demonstrating that the benchmark is substantially more challenging than existing ones. A Chinese variant (abbr-CN, 5,917 QA pairs) is also constructed, avoiding translation artifacts by selecting Chinese-native images and collecting additional Chinese-specific content.

## Strengths

1. **Largest fully human-annotated MLLM benchmark.** The comparison table shows 29,429 QA pairs vs. the next largest human-annotated benchmarks (MME: 2,374, MMBench: 3,217) — an order of magnitude larger. This is the paper's primary concrete contribution and is well-supported.

2. **Highest average image resolution among comparable benchmarks.** The reported average resolution (2000×1500 ≈ 3,007,695 pixels) substantially exceeds the next highest (MME at 1161×840). The paper also notes a maximal resolution of 42 million pixels. This is a genuine differentiator for evaluating high-resolution understanding.

3. **Consistent evidence of difficulty via model performance.** LLaVA-1.5-7B achieves only 24.9% accuracy on this benchmark vs. 76.0% on MME. No evaluated model exceeds 60% overall accuracy (Tab. 1), clearly separating models in a regime where many benchmarks are saturating (80-90%). This difficulty claim is supported by model data.

4. **Chinese variant avoids translation artifacts.** Unlike prior Chinese benchmarks that machine-translate English QA pairs (e.g., MMBench-CN), abbr-CN is constructed by selecting images without English text and collecting additional Chinese-specific images (Section 3.3), with professional human translation. This explicitly addresses the "question-image mismatch" and "translation mismatch" problems documented in the paper.

5. **Fine-grained error analysis beyond average accuracy.** The analysis of "E" answer frequency (Fig. 5) and confusion matrices (Fig. 6) reveals distinct behavioral patterns: larger models bias toward choosing "E" (conservative strategy), smaller models toward option "A", and InternVL-2 exhibits a uniquely uniform error distribution. This goes beyond reporting averages to characterize model behavior.

6. **Comprehensive evaluation scope.** The paper evaluates 24 open-source and 5 proprietary MLLMs across 43 subtasks in 5 domains, providing per-domain breakdowns for both perception and reasoning tasks.

## Weaknesses

### Fatal
None.

### Major

1. **Missing human performance baseline despite prominent "human difficulty" claims.** The paper repeatedly states the benchmark is "extremely challenging even for humans" (abstract), "most questions are even hard for humans" (line 33), and tasks "are difficult even for humans" (line 30). The title itself frames scenarios as "Difficult for Humans." However, **no human accuracy numbers are reported anywhere in the paper.** The annotation process involved 25 annotators and 7 experts who answered questions during annotation (line 33: "requiring multiple annotators to answer and double-check the results"), so a human accuracy rate on at least a subset could have been computed and reported. Without this, the central claim that the benchmark's difficulty derives from human-level challenge rather than from annotation artifacts, poorly designed questions, or the 5-option multiple-choice format is unsubstantiated. The paper's evidence for difficulty relies entirely on model accuracy comparisons (models <60% on this benchmark vs. 80-90% on others), which is suggestive but conflates benchmark difficulty with model capability. This is the single most impactful weakness — it is fixable (compute and report human accuracy from existing annotation data) but undermines a headline claim as written.

2. **No inter-annotator agreement statistics reported.** The paper states that annotations are "cross-checked by at least two professional multimodal researchers to ensure accuracy and prevent annotation errors caused by human bias" (line 180) and that "most questions are even hard for humans, requiring multiple annotators to answer and double-check the results" (line 33). However, no agreement metrics (e.g., Cohen's κ, Fleiss' κ) are reported. Without this, the reader cannot assess how much individual annotator subjectivity affects the ground-truth answers, particularly for the hardest questions. Given that the paper explicitly states questions require multiple annotators to answer, understanding the level of agreement is important for assessing benchmark quality. This is a standard expectation for human-annotated datasets at this scale.

### Minor

1. **Effect of image compression for proprietary models is acknowledged but not quantified.** The paper notes (line 240) that closed-source models impose resolution limits (e.g., Claude 3.5 Sonnet: 8K/5MB; GPT-4o/Gemini-Pro: 20MB), forcing image compression that "restricts the input of some high-quality images." This is a valid concern that could disproportionately affect tasks with very large images (e.g., remote sensing at 139MB). While the paper lists this as one of three possible reasons for performance patterns, it does not quantify the effect — e.g., by testing a subset of images that fit within the proprietary model limits without compression, or by analyzing whether the performance gap between closed-source and open-source models narrows on lower-resolution subsets. This would strengthen the conclusions about model capability vs. resolution constraints.

2. **No analysis of performance as a function of image resolution or object size.** Given the emphasis on high resolution being critical (a key design goal), the paper would benefit from analyzing how model accuracy varies with image resolution and the relative size of the queried object. This would directly support the claim that high resolution matters for these tasks, rather than relying on cross-model comparisons with different architectures. The 1/10 object-area constraint (line 178) is a design choice whose intended effect could be verified.

3. **No discussion of potential data leakage from public dataset images.** The paper collects images from public datasets and the internet (line 122: "existing high-resolution datasets," line 127: "over 70,000 public remote sensing images"), some of which may have appeared in MLLM training data. While the paper creates new QA pairs manually (mitigating this), the issue is not acknowledged. An explicit discussion of leakage risks and mitigations would strengthen the paper.

### Trivial

- Minor typo on line 20: "stituations" → "situations."
- Figure reference on line 34 uses `\label{label:teaser_task}` which seems to be a duplicate/misreference (the correct label appears to be `\ref{fig:teaser_tasks}` or `\ref{label:teaser_task}` — the figure has both `\label{fig:teaser_tasks}` on line 17 and `\label{label:teaser_task}` on line 80, which may cause confusion).

## Nice-to-Haves

- Analyze whether the 5-option multiple-choice format inflates apparent difficulty relative to open-ended generation, and discuss the implications for real-world applicability.
- Add confidence intervals or variance estimates for model accuracies to determine which performance differences are statistically significant.
- Condense the computation efficiency analysis (Section 4.3, lines 405-407), which is tangential to the benchmark contribution, to make room for the human baseline and resolution analysis.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Object area 1/10 rule not validated."** — Removed because the paper does not claim to validate this rule empirically; it is a stated design principle. The criticism is speculative about whether this "makes questions artificially hard," which goes beyond what the paper asserts.

2. **"MathVista/MM-Vet comparison is speculative."** — Removed because the paper's observation that these benchmarks are "naturally challenging" due to math and multi-step reasoning is a reasonable qualitative characterization, not an empirical claim requiring proof.

3. **"Multiple-choice format may overestimate difficulty."** — Removed because it is speculative and unsupported by evidence. The paper does not claim its format is equivalent to open-ended QA.

4. **"No confidence intervals or variance estimates for model accuracies."** — Removed because single-run accuracy reporting is the standard in this evaluation paradigm. Not a meaningful weakness in isolation.

5. **"No analysis of whether [format] overestimates difficulty relative to open-ended QA."** — Same as point 3.

6. **Strength Finder's "largest fully human-annotated benchmark"** — Kept; this is the paper's strongest verified claim. (Not removed; listed here for completeness of tracking.)

## Novel Insights

None beyond the paper's own contributions. The reviews surface the missing human baseline as the primary gap but do not generate novel observations about the benchmark's methodology or results that the paper itself does not articulate.

## Suggestions

1. **Add human accuracy numbers.** Compute human accuracy from the annotation process (the paper notes that annotators answered questions during verification). Report aggregate human accuracy, ideally per domain, and use this as a ceiling for model comparison. This directly validates the paper's most prominent claim and is the single highest-value addition.

2. **Report inter-annotator agreement statistics.** Compute and report Cohen's κ or Fleiss' κ to substantiate the claim that cross-checking ensures quality.

3. **Quantify the resolution compression effect.** Run a controlled experiment on a subset of images that fit within proprietary model limits without compression, and compare performance against the compressed versions. Report whether the rankings change meaningfully.

4. **Add a resolution/object-size analysis.** Analyze how model accuracy correlates with image resolution and the relative size of the queried object to directly support the claim that high resolution is the source of difficulty.

5. **Acknowledge and discuss data leakage risk.** Add a brief paragraph in the limitations section discussing the potential for images from public datasets to overlap with MLLM training data and why the manual QA construction mitigates this.
