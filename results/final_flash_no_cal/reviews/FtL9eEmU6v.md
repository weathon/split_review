## Summary

EditBench introduces a benchmark for evaluating LLMs on instructed code editing, constructed from real-world developer interactions collected via a custom VSCode extension used by ~500 developers. The dataset comprises 540 problems (109 core, translated across 5 natural languages), with evaluations of 40 models. The paper's key claims are that real-world editing data yields a task distribution fundamentally different from existing synthetic benchmarks, and that contextual information (highlighted code, cursor position) significantly affects performance. The benchmark includes multi-lingual instructions, diverse libraries (74 unique imports), and four edit categories (feature addition, modification, bug fixing, optimization).

## Strengths

- **Genuinely real-world provenance, backed by concrete evidence.** The data collection methodology (Section 3.1) — a VSCode extension used by 458 developers in their daily workflows, yielding 2672 accepted edits — is a clear differentiator from prior edit benchmarks. Tables 1 and 2 provide concrete evidence that EditBench's instruction length, code context length, and underspecification differ substantially from CanItEdit, EditEval, and Aider Polyglot. This is not a superficial claim; the paper quantifies the difference.

- **Ablation study provides direct causal evidence for the importance of context.** Table 3 convincingly shows that adding highlighted code improves pass@1 for 5 out of 7 top models, with performance varying by up to ~8% depending on context combination. This validates the paper's central methodological design choice and demonstrates that the benchmark genuinely tests context-dependent reasoning rather than simple instruction following.

- **Multi-lingual and multi-library diversity is well-documented.** Table 1 shows EditBench spans 5 natural languages (vs. 1 in all prior edit benchmarks). Figure 3 documents 74 unique imports in Python problems — roughly 3× Aider Polyglot (25) and 4× CanItEdit (16) and EditEval (15). These are concrete, quantified claims backed by data.

- **Granular category analysis reveals non-uniform model competencies.** Figure 5 shows that different models excel in different edit categories (e.g., qwen3-coder-flash's top category is bug fixing while claude-sonnet-4's is feature modification), and the average gap between easy and hard problems is 59.3%. This demonstrates richer diagnostic value than a single aggregated score.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No inter-annotator agreement reported for test harness creation.** The paper describes a careful two-review process (Section 3.3) but provides no quantified measure of inter-annotator reliability (e.g., agreement rate, Cohen's Kappa). Given that the test harnesses define the ground truth against which all 40 models are measured, and that interpreting ambiguous real-world instructions is inherently subjective, this is a gap. The paper would be strengthened by reporting agreement statistics on a held-out subset to demonstrate that the ground truth is reproducible beyond the specific annotation team.

- **Full-file regeneration evaluation protocol is in tension with the paper's ecological validity framing.** The paper motivates EditBench by invoking real-world tools (Copilot Edit, Cursor) where models edit a highlighted region. Yet the evaluation (Section 5) asks models to "edit the entire file by regenerating the entire code context." While the paper is transparent about this design choice, and full-file generation is standard in existing editing benchmarks (Aider Polyglot), the paper's explicit appeal to real-world interaction modality makes the mismatch worth addressing. The authors should either justify why full-file regeneration is appropriate for measuring editing ability, or evaluate using a more targeted protocol.

- **Difficulty split is relative to the model pool, not an intrinsic property of problems.** The easy/hard split (Section 5.1) is defined by the number of models (k=20) that solve a problem from the specific 40-model set. This is a common practice but the paper refers to these as "hard problems" in a way that could be misinterpreted as an intrinsic difficulty measure. The finding that hard instructions are shorter and have longer highlighted code is interesting, but may partially reflect which problems happened to stump the specific model set evaluated.

- **Correlation analysis with Aider Polyglot is based on only 17 shared models (r=0.24, p=0.06).** The paper interprets this as evidence that EditBench captures a "unique set of difficult edit tasks." While the low r is suggestive, 17 data points provides limited statistical power. The paper reports the p-value transparently, but the claim of capturing a "unique" signal would be strengthened by either a larger overlap in evaluated models or additional correlation evidence.

- **Curation yield is not characterized.** From 2672 accepted edits, the paper filters to 109 core problems. The paper describes what was removed (trivial, stylistic, ambiguous, similar) but does not characterize the distribution of the raw data (e.g., fraction of problems that were trivial vs. ambiguous vs. interesting). This makes it hard for readers to assess whether the benchmark preserves the distributional properties of real-world editing or selectively tests only the "hard tail."

### Trivial
- The limitations section is brief and could more directly address the concerns about test harness subjectivity and evaluation protocol mismatch that this review identifies.
- The paper says "when possible" for temperature 0 but does not specify which models did not support temperature 0 and how they were handled.

## Nice-to-Haves

- A formal inter-annotator agreement study on a random sample of test harnesses (even on a subset of the 109 core problems).
- An explicit analysis comparing the distribution of the raw 2672 responses to the final 109 core problems (e.g., instruction length, edit type, code length before and after filtering).
- Releasing anonymized original survey data to enable analysis of selection effects, if privacy constraints allow.
- Reporting confidence intervals or significance tests for the category-level comparisons in Figure 5.
- A diff-based or highlighted-region replacement evaluation setting alongside the full-file generation results.

## Removed Points

These points from the reviewer inputs were identified as problematic and removed (with justification):

1. **"Test harness creation introduces circularity because annotators were given model-generated solutions."** — The paper states annotators *generated* example solutions using models "to give insight into possible solutions" (Section 3.3). The test harnesses consist of unit tests that verify functional correctness, not output similarity. Annotators were explicitly instructed to create tests "generalizable to different potential implementations." Using model outputs as a reference tool during annotation is standard practice and does not create circularity unless the test harness directly checks against model outputs, which the paper does not claim or imply.

2. **"The paper misrepresents the correlation analysis: r=0.24 should be described as 'not statistically significant' rather than 'weakly correlated'."** — This is factually incorrect. r=0.24 is a weak correlation by any standard effect-size interpretation. The paper reports both r and p transparently and does not claim statistical significance. The strength of correlation (weak) and its statistical significance (p=0.06, not significant at 0.05) are separate statements; the paper makes no error here.

3. **"The optimal context setting being model-dependent undermines the claim that one setting is 'best.'"** — The paper runs a full ablation (Table 3) and transparently reports that different models respond differently to context. The standard setting (highlighted code only) was chosen because it performs best on average across models — this is a defensible methodological choice for a benchmark's standard configuration, not a weakness.

4. **"The 4% yield from 2672 to 109 is very low."** — The paper filters sequentially: 2672 → ~1700 (Python/JS only) → ~470 (after removing trivial/stylistic/ambiguous/similar) → 109 (with test harnesses). The yield from ~470 interesting problems to 109 with test harnesses (~23%) is reasonable for a curated benchmark where test harness creation is labor-intensive. The framing of "4%" is misleading because it ignores the multiple filtering stages, each of which the paper documents.

5. **"Missing confidence intervals for category-level comparisons."** — While these would be nice, single-run evaluation on static benchmarks without confidence intervals is standard practice in the LLM code generation literature. This is not a weakness specific to this paper.

## Novel Insights

The most interesting insight from the review synthesis is that the **filtering procedure itself creates an underexplored tension** in the paper's contribution narrative: the paper celebrates "messy, ambiguous" real-world data as the key differentiator, but then removes ambiguous problems during curation and uses full-file generation (rather than targeted editing) during evaluation. The paper would benefit from explicitly acknowledging this tension and analyzing whether the final benchmark preserves the properties it claims to value. A second noteworthy observation is that the ablation study (Table 3) reveals *model-dependent* context sensitivity — some models (e.g., o3-mini, qwen3-coder) consistently *lose* performance when given highlighted code. This is a more nuanced finding than the headline "context is important" and deserves deeper analysis, as it suggests that different models may have different architectural or training-based strategies for integrating contextual information.

## Suggestions

1. Report inter-annotator agreement statistics on a random subset of test harnesses to quantify ground-truth reliability.
2. Consider adding an evaluation setting that uses targeted-region replacement (matching how tools like Cursor and Copilot Edit actually work) as a secondary configuration, and analyze how results differ from full-file generation.
3. Characterize the raw data distribution (2672 responses) to show how the final 109 core problems relate to the full distribution, addressing the selection effect concern.
4. Rename the "easy"/"hard" split to "commonly solved"/"rarely solved" or similar to avoid implying intrinsic difficulty.
5. Expand the limitations section to directly address test harness subjectivity and evaluation modality choices.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>