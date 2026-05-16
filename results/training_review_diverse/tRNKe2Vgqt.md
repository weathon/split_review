Now I have all the information needed. Let me produce the consolidated review.

## Summary

MMWorld introduces a new multi-discipline, multi-faceted video understanding benchmark for evaluating MLLMs' world-model capabilities. It comprises a human-annotated subset (417 videos, 1,559 QA pairs across 7 disciplines and 61 subdisciplines) and synthetic subsets for modality-specific analysis (5,068 additional QA pairs). The work evaluates 12 MLLMs, finding that even the best model (GPT-4o) achieves only 62.54% accuracy, and reveals interesting divergences between model and human performance patterns.

## Strengths

- **Genuinely novel multi-discipline coverage**: MMWorld spans 7 broad disciplines and 69 subdisciplines (Art & Sports, Business, Science, Health & Medicine, Embodied Tasks, Tech & Engineering, Games), requiring domain expertise that prior video benchmarks (MVBench, Perception Test) do not cover. Table 1 substantiates this uniqueness.

- **Multi-faceted reasoning beyond perception**: The benchmark includes 7 reasoning types (explanation, counterfactual thinking, future prediction, domain expertise, temporal understanding, attribution understanding, procedure understanding) that go well beyond the perception-level or single-task evaluations in existing benchmarks. Concrete examples are provided in Figure 2.

- **First-party human annotations as the core asset**: Unlike benchmarks that repurpose existing datasets entirely, MMWorld's main subset is manually annotated and reviewed by humans, resulting in 1,559 carefully crafted QA pairs across diverse disciplines. This human-annotated set is the paper's strongest and most defensible contribution.

- **Comprehensive evaluation revealing large MLLM gaps**: 12 MLLMs (2 proprietary, 10 open-source) are evaluated with 3-run averages and standard deviations. The finding that GPT-4o achieves only 62.54% accuracy and several open-source models perform below random chance (Table 2) convincingly demonstrates that existing models lack the required world-modeling capabilities, establishing the benchmark's value for driving future progress.

- **Interesting human-model divergence finding**: The observation that models like GPT-4V can answer some expert-level questions that humans fail while stumbling on easier questions (Figure 4, Section 4.4) is a genuinely novel insight, though the strength of this finding is qualified by the noisy difficulty labels (see Weaknesses).

## Weaknesses

### Fatal
None.

### Major

- **Modality-specific evaluation is not properly controlled**: The paper claims the synthetic subsets allow "analyzing MLLMs within single visual or audio modalities" (Abstract, Section 3.2). However, the evaluation setup gives four of the five tested models (Video-Chat, ChatUnivi, Video-LLaMA, Otter) full multimodal input for both conditions—only Gemini Pro receives text-only input in the audio setting. The QA pairs are generated from single-modality content, but when multimodal models receive both audio and visual streams, there is no guarantee they are using only the intended modality to answer. The paper does not discuss this cross-modal leakage threat or attempt to control for it (e.g., muting audio for visual tests, blanking frames for audio tests). The conclusions about audio vs. visual perception abilities (e.g., "Video-Chat exhibited better audio perception than ChatUnivi") may reflect differential internal fusion strategies rather than genuine audio perception ability. This is a **methodological gap in the ablation study**—it does not invalidate the human-annotated core benchmark, but the claims about modality-specific analysis are not well-supported.

- **Difficulty-level analysis rests on only 3 annotators per question**: The four difficulty tiers (easy/medium/hard/expert) are defined by the performance of exactly 3 turkers per question. With n=3, a single annotator's guess shifts a question between categories, producing enormous variance. The paper draws conclusions about "different skill sets" between models and humans and claims models "can answer reasonable amount of difficult questions that humans completely fail" (Section 4.4), but the human difficulty labels are too noisy to support findings at this granularity. The turkers are also non-experts, so "expert"-level questions are simply those three random people all got wrong—not questions validated as requiring genuine expertise. This undermines the confidence in the human-MLLM comparison results, though the overall trend (some correlation, some divergence) is still suggestive.

- **The main results text contains a numerical inconsistency**: The abstract correctly states that GPT-4V achieves 52.3% accuracy (matching Table 2), and Table 2 shows GPT-4o at 62.54%. However, the contributions list (Section 1, bullet 3) states "Even the best performer, GPT-4o, can only achieve a 52.30% overall accuracy"—this number (52.30%) contradicts the actual table value (62.54%). This is not a parser artifact; it is a factual error in the paper's own summary of its results.

### Minor

- **No inter-annotator agreement reported for human annotations**: The paper describes a two-stage annotation process (Section 3.1) but does not report any inter-annotator reliability statistics (e.g., Cohen's kappa, agreement rates) for question creation or validation. This is a standard quality metric for benchmark papers and its absence makes it difficult to assess annotation consistency.

- **Synthetic dataset quality control is under-specified**: The automated pipeline generates 5,068 QA pairs, which constitute the majority of the benchmark. The paper states only that "Human evaluators were engaged to ascertain the reasonableness of automatically generated questions and answers" (Section 3.2). No details are given: number of evaluators, inter-annotator agreement, filter rate (what fraction were deemed unreasonable), or examples of rejected QAs. Since LLM-generated data is known to hallucinate, this gap reduces confidence in the synthetic subset's quality.

- **Error analysis is based on a very small sample**: The error analysis (Section 4.5, Figure 5) evaluates only 10 examples per error type across all models. With 70 total examples for seven error types across multiple models, the frequency distributions are at best anecdotal. No error bars or confidence intervals are reported. The paper does not draw strong conclusions from this analysis, but the figure's format implies quantitative frequency comparisons that are not supported by the data.

- **No discussion of cultural/geographic bias**: The benchmark title includes "World," and videos are sourced from YouTube under Creative Commons licenses and from Western-centric datasets (SportsQA, IKEA Assembly, Ego4D). The paper does not discuss cultural, geographic, or demographic coverage of its video selection, which is a relevant consideration for claims about world-model evaluation.

- **GPT-4 evaluator validation set is modest**: The GPT-4-as-evaluator method is validated on 189 examples (4.76% error rate). While this is acceptable, 189 represents only ~12% of the human-annotated QA pairs. A larger validation would be more convincing, especially given the diversity of question types and disciplines.

### Trivial
- The "temporal information" design principle (Section 3.1) is somewhat redundant with the overall goal of video understanding for world modeling; the paper's own examples do not compellingly demonstrate why this needed to be a separate criterion.
- The 53 videos sourced from existing datasets (SportsQA, IKEA Assembly, RT-1, Ego4D) inherit biases from those sources; the paper should note this briefly.

## Nice-to-Haves
- Show rule-based mapping results alongside GPT-4 evaluation results for consistency checking.
- Expand the limitations section in the conclusion to discuss annotation subjectivity, coverage gaps, and cultural biases in video selection, rather than focusing primarily on misuse risks.
- Provide a more detailed breakdown of why specific questions are "hard" (domain difficulty vs. video complexity vs. framing issues) beyond the turker-based difficulty tiers.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Abstract conflates total and human-annotated numbers**: The reviewer claimed the abstract's "1,910 videos" conflates with the human-annotated set. Upon verification, the abstract reports the total (1,910 videos, 6,627 QAs), and the introduction separately states "1,559 question-answer pairs" for the human-annotated set. The statistics table also cleanly separates these. No conflation exists; **removed as a misreading**.
- **Controlled synthetic subsets for isolating perception modalities (Strength Finder, Supporting Strength 2)**: Claims the synthetic subsets enable "controlled evaluation of single-modality perception." This conflicts with the verified weakness that the modality evaluation setup does not isolate modalities. **Removed — weakness wins**.
- **Detailed error analysis across seven failure categories (Strength Finder, Supporting Strength 4)**: Cited as a strength, but the error analysis is based on only 10 examples per type, which the reviewer correctly identifies as inadequate for quantitative conclusions. **Removed — weakness wins**.
- **Open-source release details not in main text**: The reviewer noted missing link/license, attributing this to the appendix. **Removed per missing-appendix rule**.
- **Katna footnote garbled sentence**: The reviewer noted a garbled sentence structure but acknowledged it is a parser artifact. **Removed per formatting-artifact rule**.
- **"The paper should cover Y / additional domains" type suggestions** that would turn the paper into a different, broader work: removed where they amount to scope creep.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight from the review process is that the paper's two most attention-grabbing auxiliary analyses (modality-specific perception and human-model skill comparison) are both methodologically weaker than the core human-annotated benchmark, yet these are precisely the analyses that the paper uses to argue for deeper conclusions about MLLM capabilities. This pattern—where the headline findings rest on shakier methodological ground than the core data contribution—is a recurring structure in benchmark papers and one that meta-reviewers should weigh carefully. The core contribution (a new multi-discipline, multi-faceted human-annotated video benchmark) is solid and independently valuable; the secondary analyses need either stronger controls or more cautious framing.

## Suggestions

1. **Fix the numerical inconsistency**: The contributions section states GPT-4o achieves 52.30% but Table 2 reports 62.54%. Correct this to match the table (62.54% for GPT-4o) or update the abstract/contributions to reflect whichever version is accurate.

2. **Acknowledge the modality experiment limitation explicitly**: Add a paragraph in Section 4.2 or 4.3 explaining that most models receive full multimodal input for both synthetic subsets, so the results reflect answerability from the intended modality rather than isolated modality perception. Discuss what cross-modal leakage is possible and why it is or is not a threat to the conclusions drawn.

3. **Hedge the difficulty-level conclusions or collect more annotators**: With only 3 annotators per question, the four-tier difficulty system is unstable. Either (a) collect more annotators, (b) report difficulty as a continuous score (fraction correct) rather than discrete buckets, or (c) clearly state in the main text that the difficulty labels are preliminary due to the small annotator pool and that the model-human comparison should be interpreted cautiously.

4. **Report inter-annotator agreement statistics** for the human annotation process and for the synthetic data quality control. This is standard practice for benchmark papers.

5. **Expand the error analysis or remove it**: With only 10 examples per type, the current presentation (showing frequency distributions with bars) implies more confidence than the data supports. Either sample many more examples (at least 50–100 per type) or reframe as a qualitative case study without quantitative frequency claims.

6. **Add a limitations paragraph to the conclusion** that covers benchmark-specific issues (annotation subjectivity, cultural/geographic coverage of videos, the modest size of the human-annotated subset for some disciplines) rather than focusing only on hallucination risks and misuse.

## Score and Decision

**Originality**: Good. The multi-discipline + multi-faceted reasoning combination is genuinely novel for video understanding benchmarks.  
**Importance of research question**: High. Evaluating MLLMs' world-model capabilities is timely and important.  
**Claims support**: Mixed. The core benchmark contribution is well-supported; the modality and difficulty analyses are not as well-supported as claimed.  
**Soundness of experiments**: Adequate for the main benchmark, with methodological gaps in the auxiliary experiments.  
**Clarity**: Generally clear, with minor inconsistencies (the GPT-4o number mismatch).  
**Value to the community**: Solid. The human-annotated subset fills a real gap, and the evaluation results are useful for benchmarking.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>