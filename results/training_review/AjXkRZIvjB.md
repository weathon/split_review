Here is my consolidated review.

---

## Summary

The paper introduces GSM-Symbolic, a template-based benchmark that generates diverse variants of GSM8K questions by sampling names, numbers, and conditions, enabling distributional evaluation rather than a single accuracy metric. Through experiments on 25 state-of-the-art models, the authors find that performance varies substantially across instantiations, degrades with increasing clause count, and collapses catastrophically (up to 65%) when a single irrelevant clause (GSM-NoOp) is added — a failure that in-context shots largely fail to fix. The work provides a useful methodological tool and striking empirical evidence that LLM mathematical reasoning remains brittle.

## Strengths

- **GSM-Symbolic enables distributional performance analysis.** By generating 50 variants per template, the paper shows that all 25 models exhibit non‑negligible variance (12–15% gaps between worst and best instances) and that original GSM8K accuracy falls on the right tail for 21/25 models — concrete evidence that single-point metrics can be misleading and that data contamination may be inflating reported scores (Figure 1, Section 4.1).

- **GSM-NoOp exposes a catastrophic, general failure on irrelevant information.** Adding a single clause that is semantically relevant but mathematically inconsequential drops accuracy by up to 65% (Phi‑3‑mini) and substantially degrades even o1‑preview. The demonstration that providing 8 shots of the *same* question variant (NoOp‑Symb) fails to recover performance for several models is a genuinely striking result that goes beyond prior work like GSM‑IC (Figures 5a/b, Section 4.4).

- **Controlled difficulty manipulation reveals a consistent, monotonic pattern.** By systematically adding or removing clauses (M1 → Symbolic → P1 → P2), the paper shows that all models shift leftward with increasing difficulty and variance grows concurrently — a clean behavioral result that holds across open and closed models (Figure 4, Section 4.3).

- **Large‑scale, multi‑model evaluation with disentangled ablations.** The study covers over 20 open models (2B–27B) plus GPT‑4o, o1‑preview, etc., totaling ~500 evaluations. Ablating name‑only vs. number‑only changes reveals that models are far more robust to name changes than to numerical changes, disentangling sources of fragility in a way earlier benchmarks (GSM‑Plus, GSM1K) did not (Figure 3, Section 4.2).

## Weaknesses

### Fatal
None.

### Major
None. The weaknesses below are substantive but addressable and do not invalidate the paper's core claims.

### Minor

- **Arithmetic difficulty confound in the number‑change variance experiments (Sections 4.1, 4.2).** When numerical values are sampled from ranges like 5–100 (for x, y, z) and 100–500 (for total), the resulting instantiations differ in arithmetic complexity: some require single‑digit addition, others multi‑digit subtraction with borrowing. The paper attributes the observed variance and leftward shift to fragile reasoning, but some portion of the variance could simply reflect varying computational difficulty. The name‑only condition partially controls for this (names don't change difficulty), and the overall pattern remains suggestive, but the conclusion that variance *implies* reasoning fragility is weaker than claimed without controlling for digit count, carries, or number of arithmetic operations. The paper would benefit from either a controlled analysis or a clear acknowledgment of this confound.

- **No statistical significance tests for key comparisons.** The paper relies entirely on visual histograms and bar charts without reporting standard deviations, confidence intervals, or significance tests for: (a) the difference between GSM8K and GSM‑Symbolic averages across 50 datasets, (b) the shift in means across difficulty levels, or (c) the effect of NoOp‑shot interventions. Given that the central argument hinges on the *existence and nature* of performance variance, the absence of any quantitative significance statement makes it difficult to judge whether reported differences are meaningful or within sampling noise. This is straightforward to address and would strengthen the paper.

- **NoOp‑shot analysis is presented selectively, and the central claim is stronger than the evidence supports.** The paper claims (in the contributions list and figure captions) that the NoOp performance drop "cannot be alleviated by in‑context shots." However, the NoOp‑shot experiments (Figures 6b, 6c) only show results for **4 of 25 models**. Figure 6c further shows that Gemma‑2B and Mistral‑7B *do* improve substantially on NoOp‑Symb shots, even though they perform worse on GSM and GSM‑Symbolic. The paper mentions this as "a very notable observation" but does not analyze the discrepancy or report how many of the 25 models show recovery. The claim "cannot be alleviated" is too strong given these exceptions; it should be qualified (e.g., "cannot be alleviated for most models" or "fails to recover performance across the board, with a few notable exceptions").

- **Template selection criteria are not specified.** The paper generates 100 templates from the 1319 GSM8K test examples but does not state how these 100 were selected (random, stratified by operation type, covering specific difficulty ranges, etc.). Selection bias could affect representativeness, and the omission limits reproducibility.

### Trivial

- **P2 difficulty level introduces a qualitatively different operation.** The P2 condition adds a discount clause requiring multiplication, which is a different type of operation than the additive clauses in other levels. The paper's footnote acknowledges that clause count does not perfectly track reasoning steps, but the qualitative shift in operation type is not discussed. This does not undermine the overall difficulty trend but should be noted.

## Nice-to-Haves

- **Control for arithmetic complexity in the number‑change experiments** (cluster by digit count, carries, etc., and test whether variance persists within clusters of equal complexity).
- **Full reporting of NoOp‑shot results for all 25 models** (e.g., a table or heatmap showing performance across conditions).
- **Qualitative analysis of error patterns on GSM‑NoOp** (e.g., what fraction of errors are false subtractions vs. false multiplications, and which NoOp statement types are most damaging).
- **A companion table reporting mean ± std for all conditions and models** to complement the histograms.
- **Statistical tests** (paired t‑test or Wilcoxon for GSM8K vs. GSM‑Symbolic; ANOVA or repeated‑measures test across difficulty levels; Levene's test for variance comparisons).

## Removed Points

These points were identified in the reviewer inputs but are **not included** in the main weaknesses above because they violate the review guidelines:

- **"Abstract overstates findings as definitive rather than tentative."** The abstract says *"We hypothesize that this decline is due to the fact that current LLMs are not capable of genuine logical reasoning"* — the word "hypothesize" is present, and the contributions list uses appropriately tentative language ("suggests deeper issues"). The criticism is factually inaccurate about what the paper claims.

- **"Data contamination hypothesis not explored further (perplexity checks, probing)."** The paper presents data contamination as *one possible explanation* ("One explanation for this could be data contamination") and does not assert it as a proven finding. Requesting further investigation is a reasonable suggestion for future work, not a weakness of what is presented.

- **"Difficulty levels do not control reasoning chain steps exactly."** The paper already addresses this with a footnote in Section 4.3 acknowledging that "adding or removing a clause does not always result in an exact increase or decrease of one in the number of required reasoning steps."

- **Several generic or scope‑creep suggestions** (fine‑tuning on NoOp data, testing more model families, adding confidence intervals for single‑run evaluations where that is not the norm). These are moved to Nice‑to‑Haves where applicable.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel interpretation that the paper itself does not already articulate.

## Suggestions

1. **Acknowledge the arithmetic‑difficulty confound explicitly** in Sections 4.1–4.2. Either control for it (cluster by digit count / carries) or note it as a limitation. This would strengthen rather than weaken the paper by showing methodological awareness.
2. **Qualify the NoOp‑shot claim.** Replace "cannot be alleviated by in‑context shots" with "cannot be alleviated for most models" or add a sentence quantifying exceptions. Show a table or figure covering all 25 models for the NoOp‑shot conditions.
3. **Add basic significance tests** for the three main comparisons (GSM8K vs. GSM‑Symbolic, difficulty levels, NoOp‑shot interventions). Even simple paired t‑tests and variance comparisons (Levene's test) would substantially increase confidence in the claims.
4. **Report how the 100 templates were selected** from the GSM8K test set. A single sentence describing the selection procedure would suffice.
5. **Include a small table of mean ± std** for key conditions across all models so readers can make precise comparisons that the histograms alone do not support.

## Score and Decision

This paper makes a solid empirical contribution. GSM‑Symbolic is a genuinely useful methodological tool, the scale of evaluation (25 models, ~500 evaluations) is commendable, and the GSM‑NoOp result is impactful. The weaknesses identified above are real but addressable: none invalidate the core findings, and they stem primarily from incomplete reporting rather than flawed methodology. The paper would benefit from revisions to sharpen its interpretive claims and add quantitative rigor.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>