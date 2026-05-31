Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper introduces QueryCAD, a method that uses a Vision-Language Model (VLM) to iteratively refine CAD scripting code by generating and answering binary verification questions about rendered 3D objects, then producing textual feedback for code correction. Alongside the method, the authors present CADPrompt, a benchmark of 200 3D objects with natural-language prompts and expert-annotated CADQuery code. Results across GPT-4, Gemini 1.5 Pro, and CodeLlama show that QueryCAD consistently improves the geometric quality (Point Cloud distance, Hausdorff distance) and success rate of generated objects compared to the 3D-Premise baseline and the no-refinement baseline.

## Strengths

- **First dedicated benchmark for CAD code generation with quantitative evaluation.** CADPrompt provides 200 objects with natural language prompts, expert-written Python/CADQuery code, and stratification by complexity and difficulty. This fills a clear gap: prior work relied on qualitative evaluations or small case studies. The benchmark enables reproducible, multi-metric comparisons across models and refinement methods, and is a substantive community resource.

- **Consistent improvements over the prior SOTA baseline across multiple VLMs.** On GPT-4 few-shot, QueryCAD reduces Point Cloud distance from 0.137 (3D-Premise) to 0.127 and improves success rate from 91.0% to 96.5% (Table 1). Similar or larger improvements hold for GPT-4 zero-shot, Gemini zero-shot and few-shot, and CodeLlama. The improvement pattern is directionally consistent across all three models (geometric distances + success rate), which strengthens the case that the method provides genuine benefit rather than incidental API noise.

- **Model-agnostic feedback transfers to non-multimodal models.** QueryCAD improves CodeLlama (which has no vision capability) by using GPT-4 to generate the QA feedback. Success rate rises from 64.5% to 70.0% (zero-shot) and 67.0% to 73.5% (few-shot), demonstrating that the "assess and reason" feedback is not tied to the target model's modality.

- **Ablation study supports the key design choices.** On a 100-example subset (Table 2), removing reference images increases Point Cloud distance from 0.126 to 0.153, and switching from few-shot to zero-shot QA generation raises it to 0.141. These controlled comparisons validate the necessity of both visual input and few-shot examples.

- **Oracle baseline provides useful context.** The geometric-solver baseline (accessing ground-truth geometry) upper-bounds the task. QueryCAD approaches these oracle numbers without ground-truth access (e.g., GPT-4 few-shot: 0.127 vs. 0.103), which helps calibrate reader expectations about the headroom available.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical significance or uncertainty quantification for any comparison.** The key improvements in Table 1 are modest in magnitude (e.g., Point Cloud distance 0.127 vs. 0.137 for GPT-4 few-shot) relative to the interquartile ranges (~0.14). The paper reports only median and IQR, with no confidence intervals, bootstrap estimates, or significance tests. Furthermore, the ablation (Table 2, n=100) shows that zero-shot QA generation achieves *higher* success rate (98.0%) than the full QueryCAD (97.5%) — the trend on one metric reverses. Without quantifying uncertainty, the reader cannot determine whether the reported advantages reflect a reliable effect or fall within random variation, especially given the stochasticity of VLM outputs. This weakens the paper's central claim that QueryCAD "sets a new state-of-the-art."

2. **Evaluation metrics conflate compilation success with geometric quality.** For failed compilations, the paper assigns the maximum possible distance (√3) and IoGT=0 (Section 5). This means the distance metrics simultaneously encode both whether the code compiled and how accurate the object shape is. Since success rate differences between methods are ≤5% in most comparisons, small changes in the number of failures can mechanically shift the distance numbers without reflecting any change in the geometric quality of successful objects. Reporting distances computed *on successful objects only* is necessary to separate these effects and should be provided as a supplementary analysis.

### Minor

1. **No analysis of the intermediate pipeline outputs.** QueryCAD's claimed mechanism is that the VLM generates relevant validation questions, answers them correctly by inspecting rendered images, and then produces actionable feedback. The paper provides zero analysis of any of these intermediate steps: (a) what kinds of questions are generated and are they relevant to actual deviations? (b) how accurate are the VLM's answers (by human judgment on a sample)? (c) does the resulting feedback text explicitly reference a detected issue and a corrective action? Without this, the mechanism is an untested hypothesis — the pipeline could succeed for reasons unrelated to the QA loop (e.g., the prompt structure itself acting as a useful exemplar for refinement). The ablation removing images is suggestive but does not validate the full claimed mechanism.

2. **The 3D-Premise baseline consistently reduces success rate relative to no refinement.** For GPT-4 few-shot, the Generated baseline achieves 96.0% success rate, but 3D-Premise drops to 91.0% (Table 1). A similar pattern appears for GPT-4 zero-shot (92.0% → 91.5%) and Gemini (85.0% → 83.5%/81.5%). The paper never addresses why the prior SOTA refinement method *worsens* compilability. This matters because it raises the possibility that QueryCAD's advantage over 3D-Premise comes partly from avoiding this degradation rather than from positive improvement of object quality. An analysis of the failure cases (what 3D-Premise breaks and why) would substantially strengthen the argument.

3. **The ablation is run on only 100 examples with no uncertainty characterization.** The finding that removing images or switching to zero-shot QA hurts performance is based on a single 100-example subset. As noted above, the zero-shot QA condition achieves a *higher* success rate (98.0%) than the full method (97.5%), and without confidence intervals these numbers cannot be reliably interpreted. The ablation would be more informative with bootstrap intervals or multiple runs.

### Trivial

- **Inconsistent improvement percentage between abstract and contributions.** The abstract claims a "5.0% improvement in success rate," while the contributions list says "5.5% increase in successful object generation" (lines 5 vs. 36). These appear to refer to the same metric but use different numbers.

## Nice-to-Haves

- Run the pipeline with multiple random seeds / API calls and report variance, especially for the key comparisons in Table 1.
- Provide per-example analysis showing where QueryCAD helps and where it hurts (failure case study).
- Report distances on successful objects only as a supplementary decomposition to separate success-rate effects from geometric-quality effects.
- Show examples of generated questions and answers with human-judged accuracy to validate the claimed mechanism.

## Removed Points

These criticisms were found to be factually incorrect, based on misreading the paper, or otherwise invalid:

- **"Figure 2 caption does not explain the X icon."** The caption explicitly states: *"The X icon denotes situations wherein GPT4 generated code did not compile"* (line 148). Removed as factually wrong.
- **"3D-Premise baseline description is vague / no example prompts."** The paper states it uses the same prompts from the original cited work, which is standard practice for reproducing baselines. Removed.
- **"Reference images described as optional but used in main experiments."** The paper describes images as an optional *design choice* ("We optionally include..."), which is consistent with the ablation testing their effect. Removed.
- **"Difficulty split is circular."** The difficulty is measured by the number of model configurations (6 total) that compile on initial generation — a standard empirical approach to characterize data difficulty, not circular. Removed.
- **"The paper should discuss possibility that QA feedback induces focus on surface-level features."** This is pure speculation without supporting evidence. Removed.
- **"Strengthening the Paper on Its Own Terms" section items** that overlapped with kept weaknesses have been merged; remaining suggestions (multiple runs, statistical tests) appear in Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard tension between a genuinely useful benchmark contribution and an evaluation whose rigor does not fully match the strength of the claims, but this is a common observation rather than a novel insight.

## Suggestions

1. Add bootstrapped 95% confidence intervals (or similar) for all main table entries. This is the single highest-leverage improvement: it would let readers assess whether the reported improvements are reliable given the large IQRs.
2. Decompose distance metrics into "successful-only" and "all" variants to separate the effect of improved compilability from improved geometric accuracy on successful objects.
3. Provide a human-annotated analysis of the intermediate QA outputs for a sample of ~20-30 examples: what questions were generated, were answers accurate, did feedback reference specific issues. This would validate the claimed mechanism.
4. Add a discussion of why 3D-Premise reduces success rate compared to the no-refinement baseline, and analyze whether QueryCAD's advantage partly comes from avoiding this degradation.

## Score and Decision

The paper makes two contributions: CADPrompt (the first quantitative benchmark for CAD code generation, which is a clear community asset) and QueryCAD (a method that shows consistent improvement over the prior SOTA). The evaluation has real methodological gaps — no uncertainty quantification, metrics that conflate two effects, and no intermediate analysis of the pipeline — but none of these invalidate the core findings. The benchmark in particular is a solid contribution that the community can build on. The paper would benefit substantially from tightening the evaluation, but the work as presented meets the bar for acceptance.

**Originality:** 6/10 — the QA-based feedback loop is novel, though the individual components (self-debug, VLM-based refinement) are known.  
**Importance of research question:** 7/10 — automated CAD code refinement is a meaningful problem with practical relevance.  
**Claims supported:** 5/10 — the claims are directionally supported but the lack of significance testing and metric conflation weaken confidence in the exact magnitudes.  
**Soundness of experiments:** 5/10 — reasonable coverage of models and baselines, but the statistical foundation is missing.  
**Clarity of writing:** 7/10 — clearly organized and the method is well explained.  
**Value to the community:** 8/10 — CADPrompt is a useful benchmark; the method provides a solid baseline for future work.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>