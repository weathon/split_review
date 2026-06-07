Here is my final consolidated review.

---

## Summary

Blueprint-Bench introduces a benchmark for evaluating spatial intelligence by requiring AI models to convert apartment photographs into 2D floor plans. The task is cleverly motivated: photographs are in-distribution for multimodal models but floor plan reconstruction is not explicitly trained for, making failures harder to dismiss as modality mismatch. The paper evaluates LLMs (via SVG generation), image generation models (direct pixel output), and agentic systems (Docker container with iterative refinement) on 50 apartments with ~20 images each, using an automated scoring pipeline based on room connectivity graphs and size rankings.

## Strengths

- **Novel and well-motivated task design**: The paper explicitly contrasts with ARC by keeping the input modality (photographs) in-distribution while making the output task (floor plan reconstruction) out-of-distribution. This framing makes failure harder to dismiss as a modality mismatch and isolates spatial reasoning as the bottleneck. The analogy to ARC is apt and the motivation is clearly stated.

- **Precise formatting rules enabling clean automated scoring**: The nine pixel-level rules (Section 2.1) — wall colors, line widths, red dot specifications, color restrictions — are sufficiently unambiguous that the scoring algorithm can robustly extract connectivity graphs and size rankings via standard CV techniques (HSV filtering, flood-fill segmentation) without human annotation. This makes the evaluation reproducible and scalable.

- **Multi-faceted scoring with transparent weights**: The composite score combines six components (50% edge overlap, 20% degree correlation, 10% density, 10% room count, 5% door count, 5% door orientation) with weights stated explicitly, and the paper documents which alternative approaches were tried and rejected (LLM-based extraction, shape-based metrics), demonstrating methodological awareness.

- **Cross-architecture comparison on a single task**: Evaluating LLMs, image generation models, and agentic systems under a shared evaluation protocol is a genuinely useful contribution. The paper goes beyond aggregate scores to trace agent behavior (e.g., Codex never looked at its output before submitting), providing diagnostic insight into why iterative refinement failed.

- **Open-source commitment**: Code is released, community submissions are welcomed, and the dataset sample is public (with the majority held private to prevent overfitting).

## Weaknesses

### Major

1. **Human baseline is far too thin to support the paper's central claim.** Only one human was tested, on 12 of 50 apartments (24%). The conclusion that "human performance remains substantially superior" (abstract) and that "all models remain substantially below human performance" (Figure 7 caption) rests entirely on this single data point (score 0.547 vs. random 0.322). With N=1, no confidence intervals can be estimated and the result is uninformative for a benchmark paper making strong human-vs-AI comparative claims. The paper further acknowledges that the metric penalizes humans on size ranking and speculates that an alternative metric would increase the gap — but this is post-hoc speculation, not evidence. A benchmark claiming to reveal a "significant blind spot" relative to human ability needs a proper human study (multiple participants, all 50 apartments).

2. **Inconsistent model naming and categorization between figures and tables.** Multiple mismatches suggest carelessness in data reporting:
   - **"Claude Code (Opus 4.1)"** is categorized as **"Image model"** in the Figure 5 table (line 121 of the parsed file), whereas the abstract describes it as an agent system and the figure legend codes it as a dotted bar (agents). The model is simultaneously an "image model" in the table and an agent in the visual legend.
   - **"CodeX (GPT-6)"** in Figure 5 (line 122) becomes **"Codex (GPT-5)"** in Figure 7 (line 159) — the GPT version changes from 6 to 5 across figures, and this is never explained.
   - **Error bars**: Figure 5 caption states "Error bars show standard deviation." Figure 7's embedded image alt-text says "Error bars show 2.5 standard deviation" while its text caption says "Error bars represent standard deviation." Two different scalings are used without justification.
   - **Claude model naming** varies across the paper: "Claude 4 Opus" (abstract), "Claude Opus 4.1" (Figure 5 table), "Claude Code (Claude 4.5)" (appendix figure alt-text). It is unclear whether these are the same or different models.
   
   These inconsistencies undermine confidence in the reliability of the reported numerical results. If model names and even model versions change between figures, a reader cannot be sure which system actually produced which score.

3. **Claim of statistical significance without any supporting evidence.** Section 3 states that GPT-5, Gemini 2.5 Pro, GPT-5-mini, and Grok 4 "statistically perform better than the random baseline" but provides no p-values, test statistics, confidence intervals, or description of the test used. With only 50 apartments and the visible variance in error bars, this claim is entirely unsupported. For a benchmark paper that makes significance claims, this is a basic methodological gap.

### Minor

4. **"Random baseline" is a misnomer and its behavior across subsets is not explained.** The baseline is described in Section 2.2 as "generating typical floor plans using LLMs and image generation models without any image input" — this is a *no-visual-information* baseline that leverages LLM priors about apartment layouts, not a random process. The headline finding that "most models perform at or below a random baseline" depends on the specifics of this constructed baseline. Additionally, the baseline score changes from 0.279 (Figure 5, all 50 apartments) to 0.322 (Figure 7, 12-apartment subset) without explicit acknowledgment that the baseline model was re-evaluated on the subset. While inferable from context, this should be clearly stated.

5. **Size-ranking cascading penalty acknowledged but unquantified.** The paper explicitly notes (Section 2.4) that labeling rooms by size rank rather than type means a single size-ranking error propagates into the connectivity score, but no ablation is performed to separate the two. Without quantifying how much of the reported scores (and especially the human-AI gap) is driven by this structural property of the metric rather than genuine spatial errors, the results are hard to interpret. This is a known confound that the paper could have addressed with a simple ablation.

6. **Output modality confounds spatial intelligence with instruction-following.** LLMs generate SVG code (introducing a code-generation failure mode), image generation models output pixels directly, and agents operate in a Docker container. The paper acknowledges in Section 2.4 that "Blueprint-Bench should test spatial intelligence, not instruction following" but does not separate the two. The observation that GPT-4o and NanoBanana scored poorly "primarily due to poor instruction following" (Section 3) confirms that the metric conflates format adherence with spatial understanding. This makes cross-architecture comparisons fundamentally apples-to-oranges.

7. **Undefined term "epochs".** Results are described as "averaged across epochs and apartments" (Figure 5 and Figure 7 captions) but "epochs" is never defined. It is unclear whether this means multiple random seeds, multiple runs with different temperatures, or something else entirely. This matters for understanding the error bars and the precision of the reported scores.

8. **No error-type breakdown.** The paper reports only aggregate similarity scores. An analysis of whether models fail at room count estimation, connectivity reconstruction, size ranking, or door detection would be far more informative than a single number. This is the highest-leverage analytical improvement available within the paper's existing framework, and its absence limits the benchmark's diagnostic value.

### Trivial

9. Model naming is not fully consistent across the paper (e.g., "Grok-4" in the abstract vs. "Grok 4" in tables).

## Nice-to-Haves

- Sensitivity analysis on the scoring weights (why 50% for edges and only 5% for doors?).
- Ablation removing the size-ranking component to quantify the cascading penalty.
- Reporting per-apartment difficulty variance and analysis of what correlates with it (number of rooms, apartment size, etc.).

## Removed Points

The following points raised by the critics were removed:

- "Missing comparison to BLINK, CV-Bench, VSR" — removed per instruction: the system cannot require missing related work citations without external knowledge of the reviewer's domain.
- "No discussion of whether photographs follow real-estate conventions" — speculative; the paper acknowledges images are from apartment listings.
- "Fatal structural metric flaw invalidates the paper" — downgraded. The cascading penalty and confounds are acknowledged limitations, not invalidations. The metric still measures something meaningful, even if imperfectly. However, these remain real weaknesses (listed above as Minor #5 and #6).
- "Random baseline invalidates the central claim" — downgraded from fatal to Minor (#4). The baseline is properly described as "worst-case" in the methods section; calling it "random" in results is imprecise but does not invalidate the finding that most models struggle even compared to a no-visual-input baseline.
- Generic strengths from the Strength Finder ("addressed an important problem," "well-motivated" without specificity) — removed as superficial.
- Formatting and style nitpicks — removed per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Expand the human baseline** to at least 3–5 participants on all 50 apartments. This is critical for the paper's strongest framing claim.
2. **Fix all labeling inconsistencies**: ensure model names and versions are identical across abstract, text, tables, and figures. Explain why Figure 5 and Figure 7 use different error bar scalings.
3. **Provide proper statistical tests** (e.g., bootstrap confidence intervals or paired permutation tests) for any claim that a model "statistically" outperforms the baseline.
4. **Clarify the "random baseline"**: rename it to "no-visual-input baseline" and explicitly state that its values differ across subsets because the baseline model was re-evaluated.
5. **Add error-type breakdown**: report room count accuracy, connectivity accuracy, size ranking accuracy, and door detection accuracy separately.
6. **Define "epochs"** clearly in the main text.
7. **Ablate the size-ranking component** from the metric to quantify the cascading penalty and its effect on relative rankings.

## Score and Decision

**Score: 4.0**
**Decision: Reject**

**Calibration:** I compared this paper against three anchor papers retrieved from the human-review corpus:

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| On Inherent 3D Reasoning of VLMs in Indoor Scene Layout Design | uBhqll8pw1.md | 4.00 (5,5,3,3) | 1 & 2 | Similar evaluation-only benchmark in spatial/indoor domain. Blueprint-Bench has a more novel task (photos→floor plan vs. furniture layout) and clever automated scoring, but comparable evaluation weaknesses (limited dataset scope, no error analysis). Both papers share similar score profiles. |
| FoREST: Frame of Reference Evaluation | 9Y6QWwQhF3.md | 4.25 (5,6,3,3) | 1 & 2 | Spatial reasoning benchmark with synthetic data and a method contribution. Blueprint-Bench's realistic dataset is a strength but it has no method contribution and thinner analysis. Roughly comparable overall quality. |
| SPACE: Does Spatial Cognition Emerge in Frontier Models? | WK6K1FMEQ1.md | 6.75 (5,8,8,6) | 1 | Clearly stronger in every dimension: 15 tasks grounded in cognitive science, proper human baselines, extensive model evaluation. Blueprint-Bench does not reach this bar. |
| DivScene: Benchmarking LVLMs for Object Navigation | G6DLQ40VVR.md | 6.25 (8,6,5,6) | 2 | More polished benchmark with large-scale dataset (4,614 scenes), method contribution, and thorough experiments. Blueprint-Bench is notably weaker. |

**Round 1 bracket:** 4.0 – 5.5. **Round 2 narrowing:** The closest comparators (On Inherent 3D Reasoning at 4.00, FoREST at 4.25) define the upper bound; Blueprint-Bench's labeling inconsistencies and unsupported statistical claims prevent it from reaching even FoREST's level. I place it at 4.0.

**Rationale:** The paper has a genuinely interesting core idea and a functional automated scoring pipeline, which are real contributions. However, the human-vs-AI comparison that drives the paper's strongest claims rests on N=1 data on 24% of the apartments. The inconsistent model naming and error bar descriptions between figures suggest data quality problems. The claim of statistical significance is made with no supporting test. These are not minor gaps — they affect the paper's central interpretive claims. The benchmark itself (dataset, task, code) has value, and a revised version that fixes the baselines, standardizes the reporting, and tones down unsupported claims could be a useful contribution. In its current form, the evidence does not support acceptance at a top venue.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>