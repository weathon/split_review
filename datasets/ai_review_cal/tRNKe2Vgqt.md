- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6
Now I have a clear picture of the paper and can verify each reviewer claim. Let me produce the final consolidated review.

## Summary

This paper introduces MMWorld, a video question-answering benchmark spanning seven broad disciplines (69 subdisciplines) with seven types of multi-faceted reasoning (explanation, counterfactual thinking, future prediction, domain expertise, temporal understanding, attribution, procedure). The benchmark includes a human-annotated subset (417 videos, 1,559 QA pairs) and a larger synthetic subset for modality-specific analysis. The authors evaluate 12 MLLMs and find that even the strongest model (GPT-4o) achieves only 62.54% accuracy, with several video-specialized models scoring below random chance. The benchmark is the first to combine multi-discipline coverage with multi-faceted reasoning types in the video domain.

## Strengths

- **First benchmark combining multi-discipline coverage with multi-faceted reasoning in video.** Table 1 shows MMWorld is the only benchmark among eleven compared that simultaneously covers multi-discipline, multi-task, all four multi-faceted reasoning types (Explanation, Counterfactual Thinking, Future Prediction, Domain Expertise), and first-party annotation. No prior benchmark (MVBench, Perception Test, Sports-QA, etc.) achieves this combination.

- **Rigorous evaluation reveals a genuinely challenging testbed.** Table 2 reports GPT-4o at 62.54% and GPT-4V at 52.30%, while Otter (14.99%), LWM (15.39%), and Video-LLaMA-2 (14.03%) all fall below the 26.31% random baseline. This quantitatively validates that MMWorld presents a difficult benchmark not saturated by existing models, confirming the need for such a resource.

- **Demonstrates that open-source Video-LLaVA outperforms proprietary models on spatiotemporally heavy disciplines.** Table 2 shows Video-LLaVA achieves 63.17% on Embodied Tasks (vs. GPT-4V 55.48%, Gemini 43.59%) and ties GPT-4V on Art & Sports. Figure 3 shows it also leads on Temporal Understanding. This finding—that models have divergent skill sets along discipline and reasoning dimensions—is a direct consequence of MMWorld's design and was not visible in prior video benchmarks.

- **Synthetic subsets enable controlled modality-specific analysis.** Section 3.2 and Table 3 provide dedicated QA pairs isolating audio-only and visual-only perception. Results reveal meaningful differences (e.g., Video-Chat's audio advantage over ChatUnivi, traced to its Whisper module) that would be confounded in a holistic benchmark.

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent and contradictory claims about the top-performing model across abstract, introduction, and body text.** The abstract states "GPT-4V performs the best with only 52.3% accuracy" (line 10). The introduction's contribution list says "the best performer, GPT-4o, can only achieve a 52.30% overall accuracy" (line 35)—mixing up the model name and using the wrong accuracy. Section 4.3 (line 254) also claims "GPT-4V emerges as the top performer." Yet Table 2 plainly shows GPT-4o at **62.54%**, with GPT-4V at 52.30%. These three statements all contradict the table and each other. This is not a minor typo; it severely undermines the paper's presentation of its own headline result. The table data is correct, but the text surrounding it needs systematic correction before the paper can be considered credible.

### Minor

- **Small human-annotated subset limits per-subdiscipline reliability.** The main human-annotated set contains 417 videos across 69 subdisciplines—roughly 6 videos per subdiscipline. While the broad coverage is commendable, per-subdiscipline or per-reasoning-type accuracy figures should be interpreted cautiously. The paper does not transparently acknowledge this limitation.

- **Missing inter-annotator agreement for human annotations.** No inter-annotator agreement metric (e.g., Cohen's κ) is reported for the human-annotated subset. This is a standard quality indicator for benchmark construction and its absence makes it difficult to assess annotation consistency.

- **Synthetic dataset quality control not substantiated.** The paper states (line 174) that "human evaluators were engaged to ascertain the reasonableness" of automatically generated QAs, but provides no numbers: how many questions were reviewed, what fraction passed/failed, and what the failure modes were. Without these numbers, the quality of the synthetic data is opaque.

- **Error analysis conditioned on GPT-4V's mistakes.** The error study (line 318) uses "the same questions that triggered errors in GPT-4V" and poses them to other models, then reports error-type frequencies. This design ensures the distribution is conditioned on GPT-4V's error profile, making the reported frequencies unrepresentative of each model's overall error distribution. The paper calls it "a simple test" but should more clearly caveat the interpretability.

- **Human-MLLM difficulty comparison lacks quantitative correlation analysis.** The paper (line 268) claims "some correlation" between human difficulty levels and MLLM accuracy but does not compute a correlation coefficient (e.g., Spearman's ρ) or confidence intervals. The qualitative interpretation that "MLLMs present different skill sets" is interesting, but the evidence base is thin without a quantitative statistic.

- **Multi-faceted reasoning results (Figure 3) shown without error bars or significance tests.** Given the small per-category sample sizes, many observed differences between models may not be statistically significant. Statistical testing is absent throughout the paper.

- **Audio modality ablation for Gemini Pro is uninformative.** The paper explicitly notes (Table 3 caption) that Gemini Pro receives "only providing the question" for the audio setting—no audio input at all. Its 24.45% average (below random's 32.44%) is a no-information baseline, not a measure of audio perception. The paper is transparent about this, but including it as an "audio" result without a clearer caveat is misleading.

- **No dedicated limitations section.** The conclusion briefly mentions potential misuse risks but does not acknowledge the benchmark's limitations (small human-annotated subset, potential GPT-4V bias in synthetic data, thin per-subdiscipline coverage) in a structured way.

### Trivial
- Line 36 has a typo ("stll").
- The "Missing Parts" suggestion about dataset release/license details is not verifiable—the paper's references suggest they exist.

## Nice-to-Haves

- **Report prompts used for query generation and QA generation** in the automatic pipeline (Section 3.2) to improve reproducibility.
- **Provide the distribution of question types across the seven reasoning categories** beyond what is shown in the figures, so readers can assess balance.
- **Report the fraction of automatically generated QAs approved/rejected by human evaluators** to substantiate synthetic dataset quality.
- **Add statistical significance tests** (or at least effect size discussion) for key model comparisons.

## Removed Points

- **"No distribution of question types provided":** The paper states "The detailed distribution and examples are shown in Figure~2" (line 142). Since we cannot verify the figure, this criticism is unsubstantiated from the text alone.
- **"Perception Test description is dismissive":** Subjective tone judgment about a related-work paragraph; not a substantive weakness.
- **"First-party annotation unclear":** The meaning is clear from context (annotations done by benchmark authors). This is a minor terminology nitpick.
- **"Missing appendix, proofs, references":** These are stripped by the PDF parser; they exist in the original submission.
- **"Not all models are competitive on this benchmark":** Including weaker baselines is standard practice for characterizing benchmark difficulty. If anything, this strengthens the paper's claim that the benchmark is challenging.
- **Strength: "Synthetic dataset enables controlled modality-specific analysis"** — kept in strengths but over-claimed by the Strength Finder; the audio analysis has genuine utility despite the Gemini Pro limitation.
- **Strength Finder's generic claims about "addressing an important problem"** — dropped as lacking specific evidence.
- **"Missing related work"** — cannot confirm without external sources.

## Novel Insights

The reviewers surface a genuine tension in the paper: the benchmark's design and experimental findings are solid and useful (the multi-discipline + multi-faceted combination is genuinely novel), but the paper's presentation of its own headline result (which model is best and at what accuracy) is inconsistent across abstract, introduction, and body. This suggests the paper was revised to include newly available models (GPT-4o, Claude-3.5-Sonnet) without a corresponding update to the surrounding text. No deeper methodological insight emerges beyond what the paper itself provides.

## Suggestions

1. **Fix the top-performer inconsistency immediately.** Abstract, introduction, Section 4.3, and Table 2 must all agree. GPT-4o is the top performer at 62.54% (from Table 2). Update the abstract to say "GPT-4o achieves 62.54%, with GPT-4V at 52.30%," and fix the introduction bullet's accuracy number.
2. **Add inter-annotator agreement** for the human-annotated subset and report the synthetic data quality control pass rate.
3. **Acknowledge the benchmark's scope limitations** explicitly in a limitations subsection: the human-annotated set is small for fine-grained analysis; per-subdiscipline results should be interpreted cautiously.
4. **Either drop Gemini Pro's "audio" results or reframe them** as a question-only baseline rather than an audio perception measure.
5. **Add a correlation coefficient** (Spearman's ρ) for the human difficulty comparison.
6. **Sample errors randomly across all models** for the error analysis, rather than conditioning on GPT-4V's errors, or clearly label the current analysis as a case study.
