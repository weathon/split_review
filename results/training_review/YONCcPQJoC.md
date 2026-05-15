Now I have all the information I need to verify the reviewer claims against the paper. Let me write the consolidated review.

## Summary

This paper proposes fine-tuning LLMs to generate long-form documents (scientific news articles, Wikipedia entries) in a single pass by incorporating planning as auxiliary training tasks. The authors generate synthetic intermediate steps (summaries, outlines, key information) from existing full articles using Gemini Ultra, then fine-tune on a mixture of standard generation tasks and planning-augmented tasks. Experiments on SciNews and Wikipedia datasets show consistent ROUGE improvements over fine-tuning without planning (+2.5–4.4 RLsum) and positive human side-by-side evaluation results.

## Strengths

1. **Clean, practical approach to integrating planning into single-turn generation** — The idea of training with synthetically generated planning steps in a multi-task framework is simple to implement and clearly motivated. Table 1 shows consistent ROUGE gains across both datasets, and the best method (FT w/ I, Output w/ I) improves RLsum by +2.5 on SciNews and +4.4 on Wikipedia over the FT w/o I baseline. This validates that the planning-augmented training provides a measurable benefit.

2. **Synthetic data construction pipeline effectively addresses data scarcity** — The paper proposes a principled approach (Algorithm 1) that generates K candidate intermediate steps from each full article using Gemini Ultra, then selects the best via a scoring function combining length ratios and entailment scores. This allows constructing large-scale supervision for the auxiliary tasks without human annotation, which is a genuine practical contribution.

3. **Results generalize across two domains and two base models** — The method shows improvements on both SciNews (scientific journalism) and Wikipedia (encyclopedic articles), and holds when switching from Gemini 1.0 Pro to Gemini 1.5 Flash (Table 5), where the best mixture achieves +1.15 RLsum over the non-planning baseline. This strengthens the case that the approach is broadly applicable.

4. **Single-turn inference outperforms multi-turn inference** — Table 3 directly compares single-turn (generate intermediate steps + article in one call, then extract the article) against multi-turn (first generate outline, then generate article from outline + input). The single-turn approach achieves RLsum 46.61 vs. 43.73, a gain of +2.88. This supports the claim that the planning capability is internalized through fine-tuning rather than requiring iterative decomposition.

5. **Reasonably thorough ablation of training mixtures and inference modes** — Table 2 systematically tests six combinations of training tasks and inference strategies across both datasets. This provides useful guidance for practitioners on recipe selection and reveals that the two-task mixture (standard generation + planning-augmented generation) works best.

## Weaknesses

### Fatal
None.

### Major

1. **Human evaluation is too thin to serve as strong evidence for the headline claims about coherence, organization, and verifiability.** The human side-by-side evaluation (Sec. 5.5, Table 4) uses only **50 samples per dataset**. No confidence intervals, p-values, tie rates, number of raters, or inter-rater reliability metrics (e.g., Cohen's κ) are reported. The blinding procedure is described only as "randomly flipped" sides. With only 50 items, the dramatic W/L ratios on SciNews (7.75 for verifiability, 4.25 for coherence) are fragile — a handful of rater decisions could swing the result. The paper's central claim about improved organization and verifiability rests heavily on this evaluation, and in its current form it does not meet the rigor needed to support those claims.

2. **The synthetic data pipeline relies on Gemini Ultra (a stronger model) with no ablation controlling for teacher strength.** The entire pipeline (Sec. 4.2) uses Gemini Ultra (few-shot) to generate intermediate-step candidates. The fine-tuned model is Gemini Pro, which is weaker. The observed improvements could stem from the quality of the teacher's outputs rather than from the planning-auxiliary-task design itself. Without an ablation that either (a) uses Gemini Pro to generate the intermediate steps or (b) uses human-written intermediate steps where available, the attribution of gains to the proposed method is confounded. This is a significant methodological gap.

### Minor

3. **ROUGE is not well-suited for measuring the dimensions the paper emphasizes.** The paper claims improvements in coherence, organization, and verifiability, but the primary automatic metric (ROUGE) measures n-gram overlap with a reference. For open-ended long-form generation, ROUGE correlates weakly with human judgments of structure and organization. The modest +2–4% RLsum gains are consistent with superficial stylistic changes. The human evaluation is meant to fill this gap, but as noted above it is insufficiently rigorous.

4. **The scoring function for selecting intermediate steps is underspecified and unvalidated.** The sinusoidal scoring function g(·) is described as "derived from empirical observations" (Sec. 4.2) but the actual function is never given. The multiplicative combination LengthScore × EntailmentScore appears ad-hoc, and no validation is provided that these scores correlate with human-preferred outlines or summaries. This weakens confidence that the selected intermediate steps are actually the most useful for training.

5. **A failure case on Wikipedia is not discussed.** Table 2 shows that training with only the planning-augmented task ($x_i \rightarrow \bz_i \oplus y_i$) and inferring with $x_i \rightarrow y_i$ on Wikipedia yields a *significant drop* in ROUGE (RLsum 34.28 vs. baseline 41.28). The paper states that "models fine-tuned on the training mixture with intermediate steps consistently outperform" the baseline, but this single-task variant is a counterexample that goes unremarked. The omission weakens the thoroughness of the analysis.

6. **Training mixture ratios are not specified.** The paper does not state what fraction of training data comes from each task when using mixtures (e.g., $x_i \rightarrow y_i$ combined with $x_i \rightarrow \bz_i \oplus y_i$). This affects reproducibility.

7. **Limitations section is incomplete.** The limitations (Sec. 7) only mention the closed-book setting and RAG compatibility. It does not discuss the small human evaluation sample, the reliance on a stronger teacher model, the limitations of ROUGE for the claimed dimensions, or the Wikipedia failure case mentioned above.

8. **Auto SxS confound not discussed.** The automatic SxS evaluation uses Gemini Ultra as the judge — the same model used to generate the synthetic intermediate-step training data. This creates a potential evaluation bias favoring outputs that resemble Gemini Ultra's stylistic patterns. While the human SxS does not share this confound, the auto SxS results (W/L of 2.85 on SciNews, 1.20 on Wikipedia) should be interpreted with this in mind.

### Trivial
None.

## Nice-to-Haves

- Adding confidence intervals or paired bootstrap significance tests for the ROUGE results (Table 1) would clarify whether the modest gains are statistically reliable.
- An error analysis with case studies showing where the method improves versus fails would make the claimed benefits more concrete.
- A sensitivity analysis varying the number of candidates K or the scoring function would test robustness to noise in the constructed plans.

## Removed Points

These points were flagged for removal. Treat with caution:

1. **"The paper does not compare to STORM"** — The paper explicitly scopes itself as closed-book and states in Sec. 7 that it does not adopt a RAG setting, making STORM (which uses RAG) an apples-to-oranges comparison. Removed as scope creep.

2. **"Novelty over standard CoT fine-tuning is not articulated"** — The paper explicitly acknowledges similarity to CoT (line 23: "similar to the idea of Chain-of-Thought (CoT)") and positions its contribution as the application of this principle to long-form generation with synthetic planning data. The criticism conflates the underlying technique with the specific contribution. Removed as a strawman.

3. **"Related work does not list CoT fine-tuning"** — The paper discusses CoT, Zero-shot-CoT, ToT, and GoT in its related work section. The critic's request for a "CoT fine-tuning" baseline is an experimental comparison suggestion, not a missing citation. Removed as an experimental suggestion that belongs in Nice-to-Haves.

4. **"Missing appendix or proofs"** — The parser strips appendix/proof sections; these exist in the original submission. Removed per hard rule.

## Novel Insights

The reviews reveal an important tension that the paper does not fully resolve: the method's strength (leveraging a strong model to generate high-quality synthetic planning data) is also its key confound (gains may be driven by teacher quality rather than the planning paradigm). This is a recurring challenge in the synthetic-data-for-fine-tuning literature, and future work in this area should design experiments that decouple the effect of the teacher model from the effect of the training objective itself. A multi-level ablation (same teacher with/without planning structure, different teachers with same planning structure) would significantly strengthen the evidence.

## Suggestions

1. **Strengthen the human evaluation:** Increase the sample size, report tie rates and inter-rater agreement, and provide confidence intervals for the W/L ratios. Even a modest expansion (e.g., to 100–150 items per dataset) would substantially improve reliability.

2. **Add a teacher-model ablation:** Repeat the synthetic data construction pipeline using Gemini Pro (the same model being fine-tuned) instead of Gemini Ultra. If the gains shrink or vanish, it would indicate that teacher quality drives the improvement; if they persist, it would strengthen the claim that the planning structure itself is responsible.

3. **Discuss the Wikipedia failure case** and provide analysis of why training on $x_i \rightarrow \bz_i \oplus y_i$ alone degrades performance without the standard $x_i \rightarrow y_i$ task mixed in.

4. **Specify the scoring function g(·)** or at minimum provide the functional form, and include validation that the scoring correlates with human judgments of outline/summary quality.

5. **Disclose the training mixture ratios** used for multi-task training to improve reproducibility.

## Score and Decision

**Originality:** The approach of fine-tuning with synthetically generated planning steps in a single-turn framework is novel in its specific combination, though each component (planning steps, synthetic data, multi-task fine-tuning) builds on existing ideas.

**Importance of research question:** Long-form text generation is practically important, and simplifying multi-turn systems into single-turn generation with maintained quality would have real engineering impact.

**Support for claims:** The evidence is consistently positive but not as strong as it should be. The ROUGE gains are modest and the metric is not ideal for the claims. The human evaluation — the primary evidence for improved organization and verifiability — is too small-scale and lacks statistical rigor. The teacher-model confound is unaddressed.

**Soundness of experiments:** The experimental design is reasonable across datasets and models, but the gaps noted above (human eval rigor, teacher-model ablation, missing discussion of failure cases) prevent the evidence from being fully convincing.

**Clarity of writing:** The paper is clearly written and well-structured.

**Value to the community:** The method is practical and easy to implement. The paper would be useful to practitioners working on long-form generation, though the evidence for its advantages needs strengthening.

The paper presents a plausible and practical approach with consistently positive results. However, the evidence is not strong enough to fully support the headline claims. The two major weaknesses — thin human evaluation and unablated teacher-model confound — prevent the paper from making a fully convincing case. I judge it as borderline between weak accept and weak reject, and think the work would benefit substantially from revisions before acceptance at a competitive venue.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Weak Reject</orange>