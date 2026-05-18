Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes a metric-learning framework for detecting LLM-generated texts. The approach trains a lightweight metric network on same-context triplets (two LLM responses, one human response) on top of frozen MPNet embeddings, using the triplet loss to pull LLM responses closer while pushing LLM and human responses apart. The authors also release four new benchmark datasets (NQ, SQUAD, SciQ, Wiki) totaling over 85,000 prompt-response triplets. The best architecture achieves F1 scores of 0.87–0.95 across same-corpus, out-of-corpus, and paraphrased settings, with training times of seconds per epoch.

## Strengths

- **Novel adaptation of metric learning to LLM-text detection.** The paper adapts triplet loss (Schroff et al., 2015) with a same-context constraint specifically designed for this problem — positive pairs are two LLM responses to the same prompt, negatives are human responses. This is a principled and clearly motivated departure from both supervised classifiers and internal-access methods (Section 3.2).

- **Computational efficiency is demonstrated quantitatively and is genuinely impressive.** The full-text model trains in 8 seconds per epoch on 51,250 triplets (batch size 2,048) on a T4 GPU, and the sentence model in ~3 minutes. By contrast, finetuning DistilBERT takes 70 minutes per epoch and RoBERTa 125 minutes (Section 5). This directly supports the paper's core claim of balancing cost and performance.

- **Strong detection performance within the scoped setting.** The full-text model achieves F1 scores between 0.87 and 0.95 across same-corpus, out-of-corpus, and paraphrased settings (Figure 4). The approach demonstrably works well when the context is known and a fresh LLM reference can be generated.

- **Release of four new benchmark datasets.** The paper constructs and will release datasets from NQ (56,845 instances), SQUAD (18,813), SciQ (4,419), and Wiki (2,071) with prompt-triple structure, filling a gap in available resources for this task (Section 4).

- **No requirement for internal LLM access.** Unlike DetectGPT or watermarking, the method only needs the ability to prompt an LLM to obtain a reference response (Section 1, 2). This directly addresses the accessibility gap the paper targets.

- **Robustness to paraphrasing is explicitly tested.** The same-corpus-with-paraphraser setting (Section 5) merges original and paraphrased training data and tests on paraphrased-only data, with results showing maintained F1. This demonstrates the learned representations are not brittle to surface-form variation.

## Weaknesses

### Major

- **The evaluation lacks the most directly relevant baseline: a simple supervised classifier on the same frozen MPNet embeddings.** The only comparison is a raw distance threshold on MPNet outputs. The paper dismisses supervised methods by noting that "a deep classifier of 20 layers and over 12 million parameters could not converge" (line 32, 126), but this is a specific deep architecture, not a general failure of supervised approaches. A straightforward logistic regression, SVM, or shallow MLP trained on the same MPNet embeddings would be a natural and lightweight supervised baseline. Without this comparison, the reader cannot evaluate whether the triplet-based metric learning adds meaningful value beyond what standard classification on the same representation achieves. This gap undermines the core claim that the metric learning approach is a *better* way to balance cost, accessibility, and performance. The paper shows the full-text model often outperforms the raw MPNet threshold, but by margins that can be thin, and the question of "does metric learning beat a trivial supervised alternative on the same features?" is left unanswered.

- **The context-dependency requirement is a significant practical limitation that the paper scopes itself to but does not fully reckon with.** The method requires (1) exact knowledge of the prompt that produced the text under investigation and (2) unrestricted online access to the generative LLM at decision time to produce a fresh reference (line 15, 90). The paper acknowledges this in the conclusion as future work (line 144: "develop methods that can effectively reconstruct contexts from any texts"), and the first contribution explicitly states "for known contexts" (line 21). However, in most realistic use cases — detecting AI-written student essays, anonymous forum posts, or scientific abstracts — the prompt is not available. The framing "does not require access to any LLMs' internal computations" (line 21) is accurate but the method substitutes one form of access (internal distributions) for another (online generative access at test time), which is also frequently unavailable or costly. This narrows the deployability of the method considerably relative to the problem space the paper motivates.

### Minor

- **No measures of variance are reported despite 10 runs.** The paper states that all models are "tested in 10 runs" (line 128) and shows bar charts in Figure 4, but no standard deviations, confidence intervals, or error bars are presented. Given the small size of some datasets (SciQ: 4,419, Wiki: 2,071) and the fact that the sentence model's performance varies substantially across settings (best on NQ, worst elsewhere), this omission makes it difficult to assess the reliability and statistical significance of the reported improvements.

- **Dataset artifacts may inflate reported performance.** Human responses come from Wikipedia (NQ, SQUAD) and curated scientific explanations (SciQ, Wiki) — sources that are stylistically distinct from typical conversational or student writing. The LLM responses were generated with explicit length prompts ("please answer using at least five sentences"), potentially creating formulaic, verbose outputs. The paper acknowledges length filtering (line 110) but does not perform any content-based analysis (e.g., formality, vocabulary diversity, syntactic patterns) to ensure the detection task is driven by genuine LLM-vs-human differences rather than by surface-level artifacts of the data collection procedure.

- **The "first work" novelty claim is insufficiently contextualized.** The paper states "to our knowledge, this is the first work that utilizes metric learning in detecting LLM-synthesized contents" (line 38). Even if literally true, the paper does not discuss prior use of similarity-based, contrastive, or distance-learning approaches for synthetic text detection under different names. This makes it hard for readers to assess how the proposed approach relates to adjacent work that may not explicitly call itself "metric learning."

### Trivial

- None.

## Nice-to-Haves

- **Ablation on the triplet formulation.** The paper uses a specific triplet structure (anchor and positive: both LLM; negative: human, all from the same context). Experiments testing variants (e.g., anchor=human, or triplets not constrained to same context) would clarify why the same-context constraint is essential.
- **Error overlap analysis.** An analysis of which cases the raw MPNet baseline gets wrong and the trained metric network gets right (or vice versa) would strengthen the argument that the metric network contributes beyond the embedding features.
- **Cost-benefit comparison at deployment scale.** The paper emphasizes training speed but does not account for the cost of generating LLM references at inference time. A discussion of total cost (generation + inference) vs. alternatives would be informative.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing related works on accessible detection methods (e.g., GLTR, perplexity-based methods).** The reviewer claims the paper omits discussion of existing accessible methods. However, the paper discusses supervised classifiers on embeddings (line 32) and explicitly addresses finetuning-based approaches (line 127). The paper's scope is metric learning, not a survey of all detection methods. Removed per the "do not mention missing related works" rule.
- **Claim that the paper's framing is "misleading."** The paper's first contribution explicitly states "detects LLM responses for known contexts" (line 21) and Section 3.3 clearly describes the test-time requirement of generating an LLM reference from the context (line 90). The paper is transparent about its assumptions, so the charge of misleading framing is removed.
- **Criticism about the cost of generating LLM references at scale.** This is a natural consequence of the approach that the paper already acknowledges (generative access is needed). It's a reasonable consideration but belongs in Nice-to-Haves, not Weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's clear internal validity (the method works as described within its scoped setting) and its incomplete external evaluation (missing the most natural supervised baseline). The insight this juxtaposition yields is that the paper's contribution would be much easier to assess if it had established what incremental value metric learning provides over a trivial classifier on the same frozen features — a standard that is not met here but that is straightforward to address.

## Suggestions

1. **Add a simple supervised baseline on the same frozen MPNet embeddings.** Train a logistic regression classifier (or SVM, or 1–2 layer MLP) on the MPNet embeddings using the same train/val/test splits. Report F1 and compare directly with the full-text and sentence models. If the metric network outperforms this baseline, the contribution is clear. If it does not, the paper needs to articulate what other advantages it offers (e.g., threshold interpretability, zero-shot adaptation to unseen prompts).

2. **Report standard deviations or confidence intervals for the 10 runs.** Add error bars to Figure 4 or a table with exact numbers and variance. This is essential for evaluating whether the reported improvements are meaningful.

3. **Include at least one experiment that relaxes the known-context assumption.** Even a simple diagnostic — e.g., using a paraphrased or partially observed prompt — would give readers a sense of how fragile the method is when the context assumption is violated. This would directly address the main practical limitation of the work.

4. **Analyze dataset artifacts.** Report basic linguistic statistics (e.g., Flesch readability, type-token ratio, average sentence length difference) for human vs. LLM responses in each dataset. This would help assess whether the detection task is harder or easier than it would be in a more natural deployment setting.

## Score and Decision

The paper proposes a genuinely novel application of metric learning to LLM-text detection, with impressive training efficiency and reasonable performance within its scoped setting. However, the evaluation contains a serious gap: the only baseline is a raw distance threshold on MPNet embeddings, and the dismissal of supervised methods is based on a specific deep architecture rather than the obvious simple alternative (e.g., logistic regression on the same frozen features). Without this comparison, the incremental value of metric learning over a trivial supervised approach is unclear, which undermines the paper's central claim. Combined with the significant practical limitation of requiring known contexts and online generative access at test time, and the absence of variance reporting, the paper in its current form does not provide sufficient evidence that its approach advances the state of the art over what a simpler pipeline could achieve. Substantial revision — particularly the addition of proper baselines — would be needed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>