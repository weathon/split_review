Now I have all the verification I need. Let me compose the final review.

## Summary

MMWorld introduces a multi-discipline, multi-faceted video understanding benchmark spanning seven broad disciplines (69 subdisciplines) with 1,910 videos and 6,627 QA pairs. The benchmark combines a human-annotated main subset (417 videos, 1,559 QA pairs) targeting multi-faceted reasoning (explanation, counterfactual thinking, future prediction, domain expertise, temporal understanding, attribution understanding, procedure understanding) with synthetic subsets isolating audio-only and visual-only perception. The paper evaluates 14 MLLMs and finds that even the best proprietary model reaches only 62.54% accuracy, with most open-source models performing far worse. The benchmark's core contribution—being the first video benchmark to simultaneously cover multi-discipline breadth and multi-faceted reasoning—is genuine and fills an identified gap.

## Strengths

- **Multi-discipline coverage is a genuine differentiator**: Table 1 shows MMWorld is the first video benchmark to check "Multi-Discipline"—it covers Art & Sports, Business, Science, Health & Medicine, Embodied Tasks, Tech & Engineering, and Games across 69 subdisciplines. Prior benchmarks (Perception Test, MVBench, Video-Bench) do not offer this breadth.

- **Multi-faceted reasoning beyond perception**: The benchmark includes counterfactual thinking, future prediction, explanation, domain expertise, temporal understanding, attribution understanding, and procedure understanding. Table 1 shows MMWorld is the only video benchmark covering all four of Explain., Counter., Future., and Domain.—prior benchmarks cover at most three of these.

- **Controlled synthetic subsets for modality isolation**: The automatic pipeline (Section 3.2, Figure 3) generates audio-only and visual-only QA subsets. Table 6 provides informative modality-specific comparisons (e.g., Video-Chat excels at audio perception, Gemini Pro at visual perception) that would be confounded in a single-modality benchmark.

- **Comprehensive model evaluation with interesting findings**: The evaluation of 14 MLLMs (4 proprietary, 10 open-source) reveals that Video-LLaVA-7B outperforms GPT-4V and Gemini Pro on Embodied Tasks and matches them on Art & Sports, suggesting spatiotemporal training data confers advantages that raw scale does not. This is a non-obvious finding.

## Weaknesses

### Major

- **Text–table inconsistency about model rankings undermines trust in the narrative**. The abstract states "GPT-4V performs the best with only 52.3% accuracy" (line 10). The contributions list says "Even the best performer, GPT-4o, can only achieve a 52.30% overall accuracy" (line 35)—but the table shows GPT-4o at 62.54%, not 52.30%. Section 4.3 (line 254) opens with "GPT-4V emerges as the top performer, closely followed by Gemini Pro," completely ignoring that GPT-4o (62.54%) and Claude-3.5-Sonnet (54.54%) both outperform GPT-4V (52.30%) in the very same table. This is not a single typo; the abstract, contributions list, and two discussion paragraphs all contain claims inconsistent with the results table. The abstract also says "2 proprietary and 10 open-source MLLMs" (12 total), but the table includes 4 proprietary and 10 open-source (14 total). These inconsistencies force the reader to question which results to trust and whether the analysis (e.g., comparisons to GPT-4V as the "best model") was actually written against the data presented. The benchmark contribution remains valuable, but the paper's reporting of its own results is unreliable in its current form.

- **The "expert" difficulty level is misleading and the human–model comparison is overstated**. Difficulty levels are defined solely by the performance of 3 non-expert turkers per question: "Expert" = 0/3 correct by these same turkers (Figure 4 caption, line 284). Calling this level "expert" conflates "hard for a handful of non-experts" with "genuinely requires domain expertise." The paper then claims (line 268) that MLLMs "can correctly answer expert-level questions that humans often get wrong." This overstates what the evidence supports. A more faithful claim would be that MLLMs sometimes answer questions that 3 non-expert raters all missed—which is interesting but different from showing models handle genuinely expert-level content. The underlying observation (different patterns of correctness) has value, but the framing needs adjustment.

### Minor

- **Per-type question counts are not reported**, making the per-reasoning-type accuracy comparisons (Figure 4) difficult to interpret. If some reasoning types (e.g., Procedure Understanding) have only a handful of examples, the per-type accuracy numbers become unreliable. The paper should report exact counts for each of the seven reasoning types in the human-annotated subset.

- **The error analysis methodology is underspecified**. The caption (Figure 5, line 323) says "For each error type, 10 examples were evaluated," but it is unclear whether this means 10 examples per model per type or 10 total across all models. With 7 error types and 14 models, the difference matters greatly. The sample size for a multi-model frequency comparison is not clearly stated and may be too thin to support the conclusions drawn.

- **Synthetic dataset quality is asserted but not quantified**. The paper states (line 174) that "human evaluators were engaged to ascertain the reasonableness of automatically generated questions and answers," but reports no inter-annotator agreement, no acceptance/rejection rate, and no validity statistics. Without these, the quality of the synthetic subsets used for modality ablation is hard to assess.

- **Minor model count inconsistency**: The abstract says "2 proprietary and 10 open-source MLLMs" (12 total), but Table 3 evaluates 4 proprietary and 10 open-source = 14 models. This further confirms that the narrative text was not updated to match the expanded evaluation table.

### Trivial

- None beyond those already noted in Minor (the presentation issues above are minor but substantive enough to list there).

## Nice-to-Haves

- The human study would be strengthened by either (a) using independent domain experts to define difficulty, or (b) renaming the difficulty levels (e.g., "Easy/Medium/Hard/Hardest for non-experts") to avoid overclaiming what "expert" means.
- Including a table with exact per-discipline video counts and per-type question counts would aid interpretation.
- Reporting acceptance rates or inter-annotator agreement for the synthetic dataset quality check would increase confidence.

## Removed Points

- **Criticism about "small size of human-annotated subset"** (417 videos, 1,559 QAs): This is a scope-appropriate size for a manually annotated benchmark spanning 7 disciplines. The paper does not claim to be the largest benchmark, and 1,559 manually curated QAs with two-stage review is a solid contribution. Keeping this as a weakness would punish the paper for not being something it never claimed to be. Moved to minor observation at most.

- **Criticism about benchmark not being large enough for statistical power per discipline**: This conflates "small" with "insufficient." The paper reports standard errors across 3 runs, which is the accepted practice in MLLM evaluation. No statistical claims are made that would require larger samples. Moved to Nice-to-Haves.

- **Criticism that the paper should report per-type question counts**: This is already listed as a Minor weakness rather than being removed entirely. Kept as Minor.

## Novel Insights

The reviews surface an interesting tension: the paper's core benchmark design (multi-discipline taxonomy, multi-faceted reasoning types, modality-controlled subsets) is genuinely novel and well-executed, but the textual reporting of evaluation results contains an unusually high concentration of inconsistencies—abstract, contributions list, and analysis text all contradict the results table. This suggests the evaluation was expanded (adding GPT-4o and Claude-3.5-Sonnet) after the main narrative was written, without corresponding updates to the text. The benchmark itself would be more valuable if the narrative were aligned with the actual results, because several interesting comparative claims (e.g., about Video-LLaVA's relative strengths against GPT-4V) hold for GPT-4V but shift or weaken when GPT-4o is considered. The human study design is also notable: the paper's most striking claim (MLLMs handle "expert-level" questions) rests on a definition of "expert" that is actually "hard for non-experts," which is a framing gap rather than a data gap—the data still shows interesting model–human disagreement patterns.

## Suggestions

1. **Align all narrative text with the results table**: The abstract, contributions, and Section 4.3 must be rewritten so that GPT-4o (62.54%) is correctly identified as the best model, GPT-4V's 52.30% is contextualized accordingly, and the abstract's model count (12→14) is corrected. Every comparison that currently uses GPT-4V as the reference point should be re-evaluated against GPT-4o.
2. **Rename "Expert" difficulty level** to something like "Hardest (for non-experts)" or "All-humans-missed" to accurately reflect the methodology, and adjust the claim that models handle "expert-level questions" accordingly.
3. **Report per-reasoning-type question counts** for the human-annotated subset in a table or figure.
4. **Clarify the error analysis sample size** and, if the sample is small, dial back the definitiveness of the conclusions.

## Score and Decision

The MMWorld benchmark is a solid contribution that fills a real gap in video understanding evaluation. However, the paper in its current form contains a cluster of textual inconsistencies that make its own results reporting unreliable. These issues are fixable (rewriting narrative text, adjusting difficulty naming, adding per-type counts), but they are not trivial: a reader cannot currently trust whether the authors' analysis was written against the data presented. The core benchmark contribution warrants acceptance, but only with the expectation that these reporting issues will be corrected.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>