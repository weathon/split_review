Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces an automated method for refining CAD code generation using VLMs. The approach works by having a VLM generate binary verification questions about the object described in the prompt, answer them using rendered images of the generated 3D object, and then produce corrective feedback based on mismatches. Alongside the method, the paper presents CADPrompt, a benchmark of 200 natural language prompts paired with expert-written CAD code and ground-truth 3D objects. Results on GPT-4, Gemini, and CodeLlama show consistent improvements in geometric metrics and compilation success rate over the prior 3D-Premise baseline.

## Strengths

- **First dedicated benchmark for CAD code generation (CADPrompt):** The paper introduces a curated set of 200 prompts with expert-verified code and ground-truth STL objects, stratified by complexity and compilation difficulty. This fills a clear gap — prior work relied on qualitative assessments or small-scale examples. The dual-annotation and expert-review process for 65 ambiguous cases demonstrates careful curation (Section 4, Table 1 statistics).

- **Consistent improvement over 3D-Premise across VLMs and settings:** In Table 1, the proposed method applied to GPT-4 few-shot reduces Point Cloud distance from 0.137 to 0.127 (7.3% relative) and increases success rate from 91.0% to 96.5% compared to 3D-Premise. For Gemini zero-shot, Point Cloud distance improves from 0.150 to 0.138. The direction of improvement is consistent across GPT-4 and Gemini in both zero-shot and few-shot settings.

- **Operates without ground-truth or human-in-the-loop:** Unlike the geometric solver baseline (which requires ground-truth geometry) and prior refinement methods (which require human feedback), the proposed method is fully automated and only requires the prompt and rendered images of the generated object. Section 6 correctly notes this practical advantage.

- **Model-agnostic feedback demonstrated on CodeLlama:** The method improves CodeLlama few-shot success rate from 67.0% to 73.5% and reduces Point Cloud distance from 0.224 to 0.185 (Table 1), even though CodeLlama lacks multimodal capabilities — GPT-4 is used to generate the feedback. This supports the claim that the refinement mechanism transfers across models.

- **Ablation study isolates key components:** Table 2 shows that removing reference images worsens Point Cloud distance from 0.126 to 0.153, and switching from few-shot to zero-shot QA generation increases it to 0.141. This confirms that both visual input and structured QA examples contribute to the method's effectiveness.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation conflates compilation success with geometric accuracy.** The paper assigns the maximum possible point cloud distance (√3) and zero IoGT to any non-compiling code (Section 5.2: "When computing these distances, we assign the maximum distance of two points within a unit cube, i.e., √3, and an IoGT value of zero to any data point where the code fails to compile."). This means that a method which converts non-compiling cases into compiling-but-mediocre ones will mechanically improve on the reported metrics, even if its geometry for already-compiling cases is worse. Since VQCAD improves the success rate (e.g., GPT-4 few-shot: 96.5% vs 3D-Premise 91.0%), some portion of the reported geometric improvement may be an artifact of this penalty structure. The paper does not report metrics conditional on successful compilation, making it impossible to assess how much of the headline improvements come from genuine geometric refinement versus simply converting previously-failed cases. This directly affects interpretation of the claimed 7.30% reduction in Point Cloud distance.

- **Prompts for all VLM calls are withheld, preventing independent reproduction.** The method chains four to five distinct VLM calls (initial code generation, question generation, answer generation, feedback generation, code refinement). The behavior at each step is highly sensitive to prompt wording. The paper provides no exact prompts, no example questions from the few-shot set $E_q$, and no description of how the geometric solver's numerical feedback is formatted as text for each model. Given that prompt engineering can drastically alter VLM outputs (especially for structured tasks like code generation), the method is not reproducible as described. This is a significant methodological gap.

### Minor

- **No statistical significance testing; reported differences may be noise.** Improvements in Table 1 are reported as medians with IQRs. The IQRs overlap substantially: for GPT-4 few-shot, Generated has Point Cloud distance 0.155 (IQR 0.140) and VQCAD has 0.127 (IQR 0.135). For IoGT, differences are in the third decimal place (0.939 vs 0.944) with overlapping IQRs (~0.03). Without confidence intervals, paired tests (e.g., Wilcoxon signed-rank), or per-object improvement/degradation counts, it is unclear whether the observed differences reflect genuine improvement or sampling variability.

- **Geometric solver baseline is called an "upper limit" but behaves inconsistently.** For CodeLlama, the geometric solver feedback *worsens* all metrics compared to the Generated baseline (e.g., zero-shot: success rate drops from 64.5% to 55.5%; Point Cloud distance rises from 0.237 to 0.280). The paper states the geometric solver "serves as an upper limit for CAD code refinement" (Section 5.1), yet on CodeLlama it is clearly not an upper bound. The paper does not explain how the numerical geometric feedback is formatted for CodeLlama (a text-only model) nor why feedback conveying "precise geometric differences" would degrade performance. This inconsistency is never acknowledged.

- **Ablation does not isolate the QA mechanism.** The ablation (Table 2) tests removing reference images and switching to zero-shot QA generation, but it does not test a simpler variant: provide the image and prompt the VLM directly to "identify discrepancies and suggest code fixes" (i.e., a prompt-only refinement without structured QA generation). This makes it impossible to determine whether the two-step QA process adds value over a direct visual inspection prompt. The 3D-Premise baseline is also omitted from the ablation table, so the marginal benefit of the QA mechanism over the prior state-of-the-art is not quantified.

- **5.0% vs 5.5% success-rate inconsistency between abstract and introduction.** The abstract (line 5) reports "a 5.0% improvement in success rate" while the introduction (line 36) reports "a 5.5% increase in successful object generation." The correct value from Table 1 is 5.5 percentage points (96.5% - 91.0%).

- **Self-verification hallucination risk not addressed.** The feedback loop relies on the VLM correctly answering its own verification questions. If the VLM hallucinates that a feature exists or answers incorrectly, the feedback will be misdirected. The paper instructs the model to respond "Unclear" when uncertain (Section 3.3), but provides no evaluation of how often this occurs or whether the answers are correct. A human-judged spot-check on question relevance and answer accuracy is needed.

### Trivial

- **Underspecified notation in geometric solver equations.** The concatenation operator $\oplus$ in Equations (5) and (6) is not explained — it is unclear how 26 numerical values (13 categories × 2 objects) are formatted as textual feedback for the LLM.

## Nice-to-Haves

- **Report metrics conditional on successful compilation** (alongside the current penalized values) to separate geometric quality from compilation-rate effects. This is the single most impactful addition.
- **Disclose exact prompts** for all VLM calls in an appendix, including the few-shot questions $E_q$.
- **Conduct a paired significance test** (e.g., Wilcoxon signed-rank) between VQCAD and 3D-Premise on per-object metrics, and report the number of objects improved vs. degraded.
- **Add an ablation variant** that replaces the two-step QA with a direct "describe discrepancies and fix" prompt to isolate the value of structured verification.
- **Report a human evaluation** on a sample of 30–50 objects: (1) whether generated questions are relevant to the prompt, (2) whether VLM answers are correct.

## Removed Points
- *Criticism about question relevance or "not like other 3D works" comparisons that are generic.* Removed: not a concrete weakness.
- *Complaint about CodeLlama not having 3D-Premise baseline.* Removed: 3D-Premise requires multimodal capabilities; the paper correctly notes this is inapplicable.
- *Missing related works.* Removed per instruction: I cannot verify existence of missing references.
- *Formatting nitpicks and completeness concerns about appendix sections.* Removed per instruction: parser strips appendix content.

## Novel Insights

The reviews surface an interesting tension: the paper's framing depends on the claim that QA-structured feedback is superior to direct visual inspection, yet neither the ablation nor the qualitative analysis directly tests this hypothesis against a simple "look and fix" prompt baseline. This is a recurring pattern in VLM self-refinement papers — the extra complexity of structured reasoning chains is assumed beneficial, but the controlled comparison that would validate that assumption is rarely performed. The real threat is not that VQCAD fails (it likely does help, as the convergent evidence across models suggests) but that the *specific mechanism* may be over-engineered relative to a simpler alternative. A well-designed comparison between the proposed QA pipeline and a direct refinement prompt with equivalent image access would strengthen or reframe the contribution significantly.

## Suggestions

- **Above all:** report all geometric metrics *conditional on successful compilation* alongside the current penalized versions. Without this, the core quantitative claims cannot be properly interpreted.
- **Disclose all prompts** (or at minimum the question generation and feedback generation prompts) and the few-shot question examples $E_q$. Without these, the work is not reproducible.
- **Add a significance test** (e.g., paired Wilcoxon signed-rank on 200 per-object comparisons) to verify that the reported differences are not noise.
- **Add an ablation** that replaces the QA pipeline with a single VLM prompt: "Here is the image of the generated object and the specification. Identify discrepancies and output code fixes." Compare this to the full method to quantify the value of structured QA.
- **Analyze failure cases** — for the ~3.5% of GPT-4 few-shot objects where VQCAD fails to compile or degrades geometry, show what went wrong (e.g., question misinterpretation, introduced syntax errors).

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>