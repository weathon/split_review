Now I have a comprehensive understanding of the paper. Let me write the final consolidated review.

## Summary

This paper proposes intervention as a fundamental goal for evaluating interpretability methods. It unifies four popular approaches (sparse autoencoders, Logit Lens, Tuned Lens, and probing) under an encoder-decoder framework enabling structured interventions, and introduces two evaluation metrics: intervention success rate and the coherence-intervention tradeoff. The authors benchmark these methods on GPT2-small, Gemma2-2b, and Llama2-7b across 10 token-level features (210 prompts), finding that lens-based methods outperform more complex approaches for simple concrete interventions, but that all methods degrade output coherence, often underperforming simple prompting.

## Strengths

1. **Clean unification of four interpretability methods under a single encoder-decoder framework (Section 3.1).** By formally defining forward and inverse mappings for each method (SAEs: learned dictionary + activation; Logit Lens: unembedding matrix; Tuned Lens: learned affine transformation on unembedding; probes: linear weights), the paper makes principled comparisons possible where previously methods had incompatible feature spaces. This formalization is directly useful for future work.

2. **Introduction of two concrete quantitative evaluation metrics that go beyond the field's typical qualitative demonstrations.** Intervention Success Rate (Section 3.2) and the Coherence-Intervention Tradeoff directly measure causal correctness and practical utility, rather than just reconstruction error or interpretability ratings. These metrics address a genuine gap in the interpretability evaluation literature.

3. **Non-trivial empirical finding that the simplest, least-trained method (Logit Lens) consistently achieves the highest intervention success across all three models.** Figure 2 shows Logit Lens dominating at comparable edit distances — a surprising result given that SAEs and probes require substantial training data and compute. The finding is robust in direction across model scales.

4. **Inclusion of an intervention-aware prompting baseline that quantifies the practical gap.** The coherence analysis (Section 4.3) compares all interpretability methods against prompting, showing that prompting often achieves higher coherence at comparable success rates. This sharply illustrates the real-world shortcoming of current interpretability-based steering.

## Weaknesses

### Major

1. **The prompting baseline comparison is fundamentally unfair, weakening the headline conclusion.** The paper states (line 158) that "only Llama2-7b was instruction-tuned out of the models evaluated, prompting was less successful for Gemma2-2b and infeasible for GPT2-small." Since Gemma2-2b has a widely available instruction-tuned variant (Gemma2-2b-it), comparing prompting against the base model — which cannot follow instructions — is a methodological mismatch. Two of three models literally cannot do the task asked of them. Yet the abstract and conclusion claim without qualification that "interventions… underperforming simpler alternatives, such as prompting" and "non-interpretability-based approaches, such as prompting, perform best overall" (lines 7, 241). This claim rests entirely on data from one model and should be explicitly scoped to instruction-tuned models. The paper's central comparative takeaway is materially less general than stated.

2. **No error bars, confidence intervals, or statistical testing for the main empirical results.** Figures 2–4 present curves without any measure of variance. With 210 prompts and 10 features, there is substantial room for variation, and the paper makes comparative claims (e.g., "Logit Lens outperforms all other methods across all models") without any statistical backing. For a paper whose central contribution is empirical benchmarking, this is a significant omission that makes it impossible to assess whether observed differences are meaningful or within noise. This also makes the results non-reproducible at the level of statistical rigor.

3. **The central explanation for poor SAE performance — feature label noise — is asserted without systematic verification.** Section 4.2 attributes SAE underperformance to "frequent mislabeling of the learned SAE features" and gives a single anecdotal example (coffee vs. beans), but provides no systematic error analysis: no human evaluation of label quality, no inter-rater agreement, no estimate of what fraction of features are mislabeled, and no attempt to filter to high-confidence labels and check whether results change. Since this is the paper's primary explanation for why SAEs underperform, the absence of evidence is a critical gap. Without it, reader cannot distinguish between "SAEs are genuinely worse for intervention" and "the labels used were noisy, but cleanly-labeled SAE features might work well."

### Minor

4. **The coherence metric measures linguistic fluency, not topical coherence, and is not validated.** The scoring prompt asks the evaluator to judge "grammar and comprehension, ignoring incomplete sentences" (line 92). This captures basic language quality and fluency, but the paper frames it as "coherence" — a different construct that also includes staying on topic and satisfying the prompt's intent. The ±1 buffer around the clean mean is a reasonable heuristic (line 128), and the qualitative examples support the main quantitative trends, but the metric's construct validity is imprecise. A small human correlation check (even 30–50 samples) would substantially strengthen this component.

5. **The pseudoinverse computation for Logit Lens and Tuned Lens is underspecified, and the large reconstruction error discrepancy is unexplained.** The paper mentions using a "low-rank pseudoinverse" (line 78) but does not describe the truncation criterion (SVD threshold, rank selection). Reconstruction error differs by four orders of magnitude across models (5e-5 for Llama2-7b vs. 0.52 for Gemma2-2b, Table 1) — this is mentioned but never explained or discussed in terms of how it might affect cross-model comparisons of intervention results.

6. **The hyperparameter α tuning process is not described.** The paper notes that α "must be tuned for each method, model, and sometimes even intervention feature" (line 81) but does not specify the tuning procedure: grid size, selection criterion, or whether α was chosen globally or per feature. Since normalized edit distance is used as a cross-method comparison axis (x-axis in Figures 2–4), the fairness of comparisons depends on whether α was tuned equally thoroughly per method.

7. **Which layer(s) were used for each method is not specified.** The formal description edits representation "at token position t and layer l" (line 82), but the paper never states which layer was chosen for each method or why. This matters because intervention at different layers can produce different effects, and the choice could systematically favor some methods over others.

8. **Claims about prompting "perform best overall" overreach the evidence even beyond the fairness issue.** The features tested are 10 concrete token-level words (e.g., "beauty", "coffee", "pink"). The paper notes this is an "upper bound" for "simple, easy-to-measure contexts" (Section 3.2), and later acknowledges that lens-based methods' "predefined, static features are limited and rudimentary" (line 231). However, the conclusion's sweeping "perform best overall" language (line 241) drops these qualifiers. The results would likely differ for abstract features (truthfulness, sycophancy, harmlessness) that cannot be prompted trivially and where Logit Lens has no direct handle. The paper's claims should match its acknowledged scope.

### Trivial

None.

## Nice-to-Haves

- The Intervened Token Probability metric (Section 3.2) is described but only briefly acknowledged in one line (line 155). Including it systematically in the main figures alongside binary success rate would add information about continuous effects.
- Adding a state-of-the-art instruction-tuned model to the set (e.g., Gemma2-2b-it, Llama3-8b) would make the prompting comparison fair and more informative.

## Removed Points

- **Intervened Token Probability "never used":** The critic claimed this metric is "mentioned in the text but never actually used in the experiments." This is factually incorrect — line 155 reports its magnitude for SAEs. **Removed.**
- **GPT2-small SAE reconstruction error (1.64) as an unaddressed concern:** The paper already acknowledges this (Section 4.2: "due to the large reconstruction error for GPT2-small, even with intervention, the edit distance is much greater than that needed for Logit lens and Tuned lens"). **Removed — already addressed.**
- **"Optimal intervention strength" undefined:** The paper defines it (line 197): "randomly chosen from the outputs where intervention succeeded and coherence was still relatively high." **Removed — reviewer missed the definition.**
- **Directional similarity speculation unsupported:** The paper states "We speculate" (line 210), which is appropriate language for a discussion section. Papers are permitted to offer plausible speculations. **Removed.**
- **Steering vector ChatGPT data bias:** The critic raises a speculative concern about ChatGPT-generated pairs having systematic bias. This is possible but no evidence is presented, and the probes achieve 100% train/test accuracy, suggesting the task is well-posed. **Removed.**
- **100% probe accuracy is "suspicious":** For a binary word-level classification with 200 examples of concrete token features, 100% accuracy is expected, not suspicious. **Removed.**
- **Coherence metric threshold unaddressed:** The ±1 buffer is a reasonable heuristic; the paper justifies it by showing reconstructed outputs match clean coherence (line 128). **Weakened to minor.**

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation that the paper itself does not already make.

## Suggestions

1. **Fix the prompting baseline:** Either (a) evaluate prompting on instruction-tuned variants of all models (e.g., Gemma2-2b-it, GPT2-small cannot follow instructions so exclude it from prompting comparisons), or (b) explicitly scope all prompting-related claims to instruction-tuned models only, removing unqualified statements from the abstract and conclusion.

2. **Add statistical grounding for the central empirical comparisons.** At minimum, report bootstrapped confidence intervals for the success rate curves in Figures 2–4 and include a statistical comparison (e.g., pairwise tests at key edit distances) to support comparative claims.

3. **Quantify SAE label quality.** Manually inspect a random sample of ~30 SAE features per model to establish a true labeling accuracy estimate, or show that filtering to only high-confidence Neuronpedia labels yields different results. Without this, the paper's main explanation for SAE underperformance is an untested hypothesis.

4. **Provide implementation details needed for reproducibility:** (a) which layer(s) were intervened on for each method/model; (b) the pseudoinverse computation details (SVD threshold); (c) α tuning protocol (grid, criterion, per-feature vs. global). These are standard methodological details, not trivial.

## Score and Decision

This paper addresses an important gap — systematic evaluation of interpretability methods as control mechanisms — and makes concrete contributions: a unifying framework, two evaluation metrics, and a broad empirical comparison across 4 methods, 3 models, and 210 prompts. The core findings about lens-based methods and intervention-induced coherence degradation are useful and credible within the paper's scope.

However, the headline claim about prompting "performing best overall" is substantially weakened by an unfair comparison (instruction-following task evaluated on non-instruction-tuned models for 2 of 3 models). The absence of any statistical testing (error bars, confidence intervals) is a significant gap for an empirical benchmarking paper. The central explanation for SAE underperformance (label noise) is asserted without systematic verification. These issues reduce confidence in the paper's strongest comparative conclusions but do not invalidate its core methodological contributions.

The paper would be strengthened substantially by addressing the prompting fairness issue, adding statistical grounding, and quantifying SAE label quality. I recommend conditional acceptance with major revisions addressing the above.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>