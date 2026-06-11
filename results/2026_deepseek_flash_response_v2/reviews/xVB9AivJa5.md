Now I have a solid calibration. Let me compile the final review.

**Round 1 bracket:** The paper sits between the weak anchors (~3.0-4.25) and the strong anchors (~6.25-6.75). The most similar paper is SPACE (6.75, Accept), which is clearly more comprehensive and better validated. The paper is stronger than FoREST (4.25, Reject) and "On Inherent 3D Reasoning" (4.00, Reject) due to its more creative task design and cross-architecture comparison. Initial bracket: **4.0 – 6.0**.

**Round 2 narrowing:** Compared to MANGO (6.25, Reject), which had thorough evaluation (hundreds of QAs per maze) but less task novelty, Blueprint-Bench has more creative task design but weaker evaluation rigor. Compared to "A little less conversation" (4.33, Reject), Blueprint-Bench has stronger novelty. The paper sits above the 4.0-4.5 cluster but below the 6.0+ cluster. Narrowed to **4.5 – 5.5**.

**Final score: 5.0** — the paper has a genuinely creative task design and important cross-architecture comparison capability, but the misleading "random" baseline and unvalidated scoring metric substantially weaken its central quantitative claims. This is a borderline reject that needs major methodological revision.

---

## Summary

Blueprint-Bench introduces a benchmark for evaluating spatial reasoning in AI models by requiring them to convert apartment photographs into 2D floor plans. It evaluates LLMs (via SVG code generation), image generation models (via direct image output), and agent systems on 50 apartments, using a scoring algorithm based on room connectivity graphs and size rankings. The key finding is that most models perform at or below a "random" (no-visual-input) baseline, with the best models (GPT-5, Gemini 2.5 Pro at 0.42) substantially below human performance (0.547).

## Strengths

1. **Task design that isolates spatial reasoning by keeping input in-distribution**: Unlike ARC and similar benchmarks that use alien input modalities, Blueprint-Bench uses photographs (well within training distribution) but requires an output transformation (floor plans) that models were not explicitly trained for. This provides a cleaner test of whether generalist models possess genuine spatial intelligence rather than testing distribution mismatch (Section 1, lines 15-18).

2. **First numerical framework enabling cross-architecture comparison**: The benchmark provides the first numerical comparison of spatial reasoning across LLMs, image generation models, and agents on the same task (Section 1, lines 37-39; Section 2.2). This fills a genuine gap—image generation model announcements (GPT Image, Nano Banana) lacked numerical benchmarks entirely.

3. **Non-obvious negative result on agent-based approaches**: Agent evaluation with trace analysis (Section 3, lines 175-179, Figure 8) reveals that neither Codex CLI nor Claude Code outperformed single-pass generation, despite having iterative refinement capabilities. The trace analysis showing Claude Code's false confidence ("Each room is fully enclosed" when it wasn't) provides qualitative insight beyond surface-level scores.

4. **Transparent documentation of scoring design choices and limitations**: Section 2.3 specifies the six-component weighted similarity metric with justifications, and Section 2.4 candidly discusses why alternatives (LLM-based extraction, shape similarity metrics) were rejected, including specific failure modes observed.

5. **Nuanced analysis of scoring artifacts affecting the human baseline**: The paper acknowledges (lines 149-151) that all humans correctly inferred connectivity, but the size-ranking-based scoring penalized them for misordering room sizes. This self-awareness about the metric's limitations strengthens the paper's credibility.

## Weaknesses

### Fatal
None.

### Major

1. **Misleading "random baseline" that is not random**: The paper's central claim ("most models perform at or below a random baseline" — Abstract, line 9; Section 3, line 112) is anchored to a baseline described as "generating typical floor plans using LLMs and image generation models without any image input" (line 69). This is not random—it embeds strong architectural priors about apartment layouts (typical room counts, connectivity patterns, size relationships). A model performing "at or below" this baseline means the visual input *hurts* performance compared to relying on priors alone, which is a different (and less severe) finding than "no better than random chance." The paper does not specify how many floor plans were generated per apartment, how they were aggregated across models, or what the variance looks like. It is referred to as "random" throughout (Figure 5 caption, Figure 7 caption, Section 3) despite not being random. This fundamentally affects how the paper's headline quantitative result should be interpreted.

2. **Scoring methodology has a structural confound that is acknowledged but unquantified**: Room IDs are assigned strictly by size rank (1=largest, 2=second largest, etc.), so a small error in size ordering cascades into apparent connectivity errors. The paper acknowledges this (Section 2.4, lines 99-100: "the penalty of making a mistake in the size ranking causes additional penalties when scoring the connectivity") but does not quantify its effect on the overall scores. The benchmark's composite scores conflate size estimation accuracy with connectivity accuracy in an unknown way. Without validation (e.g., synthetic perturbations of ground-truth floor plans, correlation with human judgment), the leaderboard cannot be reliably interpreted as cleanly measuring "spatial intelligence." The paper's own observation that all humans got connectivity correct but were penalized on size ranking (lines 149-151) inadvertently demonstrates this problem: the metric systematically under-reports true spatial understanding.

### Minor

1. **No statistical tests reported for claimed significance**: The paper states that GPT-5, Gemini 2.5 Pro, GPT-5-mini, and Grok 4 "statistically perform better than the random baseline" (line 112) but reports no p-values, confidence intervals, or correction for multiple comparisons. Given the per-apartment variance visible in the appendix figures, this claim is unsupported.

2. **Human baseline critically underspecified**: The paper says only "we gave the task to a human" (line 69) with no information about number of participants, their background/instructions, time limits, or whether they followed the same 9 rules. Human performance is the reference standard (Figure 7), yet the human evaluation procedures are opaque.

3. **Extraction pipeline accuracy not reported**: The extraction algorithm (HSV filtering, flood-fill segmentation, door detection, Section 2.3) is described but no accuracy metrics are provided. Errors in extraction compound with model errors, yet the pipeline's own error rate is unknown.

4. **Instruction-following confound**: The paper acknowledges (Section 2.4, lines 104-108) that models failing the formatting rules are penalized in ways that may not reflect spatial intelligence. GPT-4o and NanoBanana's low scores (0.15 and 0.18) are attributed to "poor instruction following" (line 138), but the benchmark design cannot cleanly separate rule adherence from spatial reasoning. The paper acknowledges this trade-off but does not resolve it.

5. **Number of epochs unreported**: The paper aggregates "across epochs and apartments" (lines 116, 152) but never specifies how many repetitions were used per apartment per model, which is needed to interpret error bars and variance.

### Trivial

1. **Model categorization inconsistency in Figure 5 table**: Claude Code (an agent) is listed as "Image model" in the table (line 121), while CodeX is correctly listed as "Agent" (line 122). Several LLMs (GPT-5, Gemini 2.5 Pro, etc.) are also categorized as "Image model" despite generating SVG code through an LLM pipeline. The categorization scheme is unclear.

## Nice-to-Haves

- Validate the scoring function with synthetic perturbations (controlled room size changes) showing that scores degrade monotonically with perturbation magnitude
- Construct a proper random baseline (randomized room counts/connectivity/sizes) to compare against the LLM-generated "no-image" baseline
- Analyze what apartment characteristics (room count, irregular layouts) correlate with difficulty across models
- Report per-model compute cost or API call budget

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The dataset (50 apartments) is too small for a benchmark"** (Harsh Critic, Critical Issue #3): 50 apartments with ~20 images each is a moderate size for an initial benchmark, and many benchmarks in this area operate at this scale. The real issue is the lack of statistical tests (kept above as Minor weakness #1), not the raw count. Absorbed into Minor weakness about missing statistical tests.
- **"The paper's claim about enabling comparisons between image models and their underlying LLMs is circular"** (Harsh Critic, Overall Assessment): The paper does compare GPT-5 with GPT Image and Gemini 2.5 Pro with Gemini 2.5 Flash, so the comparison exists. The criticism is factually incorrect. Removed.
- **"No discussion of cost or compute budget"** (Harsh Critic, Missing Parts): Minor omission, not a validity-affecting weakness.
- **"Dataset not released in full"** (Harsh Critic, Section 2.1): The paper explicitly states they keep most data private to prevent overfitting (line 71, 203), which is standard practice for benchmarks. Per hard rule: do not question release status of cited entities.
- **"Cherry-picked example of Nano Banana solving geometry"** (Harsh Critic, Abstract/Introduction): This is framing context in the introduction, not a core claim. The paper's contribution does not depend on this example. Removed as nitpick.
- **Missing appendix details** (Harsh Critic, various): The parser strips appendix content from all papers; these criticisms cannot be verified. Removed per hard rule.
- **"The paper does not describe how the 50 apartments were selected"** (Harsh Critic, Section 2.1): The dataset source (apartment listings) is stated. For a benchmark, this is adequate.

## Novel Insights

The most interesting observation emerging across the reviews is that the paper's central interpretive framing—that models perform "at or below random"—is held hostage by the baseline construction. Meanwhile, the genuinely robust finding (agents with iterative refinement not outperforming single-pass, despite having the same workflow as humans) is underexplored. The reviews also surface that the size-ranking cascade is a real confound, but the paper's own analysis of how this affected the human baseline (all humans got connectivity right but were penalized on size rankings) inadvertently serves as the strongest internal evidence that the metric needs validation—it shows the metric systematically under-reports spatial understanding even for perfect connectivity inference.

## Suggestions

1. **Rename the "random" baseline to "no-visual-input baseline"** and properly characterize its construction: how many samples per apartment, across which LLMs, with what variance. Compare this against a true random baseline (randomized room counts, connectivity, sizes) to isolate the contribution of architectural priors.
2. **Validate the scoring metric** by: (a) generating synthetic floor plans with controlled perturbations and showing monotonic score degradation, or (b) having human raters judge which of two outputs is closer to ground truth and measuring agreement with the scoring function.
3. **Report statistical significance tests** (bootstrap confidence intervals, permutation tests) for all model comparisons against baselines, with correction for multiple comparisons.
4. **Specify the human evaluation protocol**: number of participants, their expertise, instructions given, and whether the 9-rule format was enforced.
5. **Report extraction pipeline accuracy** on a held-out validation set of manually labeled floor plans.
6. **Clarify the model categorization scheme** in the results table—the current labels ("Image model" for Claude Code and GPT-5) are confusing.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `WK6K1FMEQ1.md` (SPACE) | 6.75 | 1, 2 | More comprehensive (15 tasks), better validated, grounded in cognitive science. This paper is clearly weaker. |
| `uBhqll8pw1.md` (3D Reasoning) | 4.00 | 1, 2 | Narrower dataset, overclaimed 3D reasoning. This paper is somewhat stronger. |
| `9Y6QWwQhF3.md` (FoREST) | 4.25 | 1, 2 | Narrower scope (frame of reference only). This paper has more creative task design. |
| `eUkbTUsDgs.md` (LLM-AAI) | 4.33 | 2 | Uses embodied 3D environment but "toy" setup. Comparable quality; this paper has stronger novelty. |
| `a7eIuzEh2R.md` (MANGO) | 6.25 | 2 | More thorough evaluation (hundreds of QAs per maze) but less novel task. This paper is somewhat weaker. |
| `UiLtbLsiPU.md` (ET-Plan-Bench) | 4.50 | 1 | Similar scope benchmark. This paper has comparable contribution. |

**Round 1 bracket:** 4.0 – 6.0  
**Round 2 narrowing:** Above the 4.0-4.5 cluster (FoREST, 3D Reasoning, LLM-AAI) but below the 6.0+ cluster (SPACE, MANGO)  
**Final score: 5.0**

The paper has a genuinely creative task design and the cross-architecture comparison is a real contribution. However, the misleading "random" baseline naming and the unquantified scoring confound substantially weaken the central quantitative claims. The paper needs major methodological revision—particularly validation of the scoring function and proper baseline characterization—before its conclusions are adequately supported. The qualitative findings (agents failing to improve despite iteration) are robust and interesting, but they do not compensate for the unvalidated quantitative framework.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>