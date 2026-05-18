Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes that training VLMs on receiver behavior (likes, comments, replay graphs) improves their content understanding abilities. The authors collect BLIFT (730k images/videos with behavioral annotations from Reddit and YouTube), fine-tune LLaMA-Vid on behavior prediction tasks to produce Behavior-LLaVA, and evaluate across 46 tasks over 26 benchmarks. The core empirical finding — consistent improvement over the base model and the Ad-LLaVA content-only control — is well-supported. The BLIFT dataset itself is a significant resource for the community.

## Strengths

1. **Large-scale behavioral dataset (BLIFT).** The paper collects and releases 730k images and videos paired with real user behavior (likes, comments, replay graphs, upvotes) from Reddit and YouTube. This is orders of magnitude larger than lab-collected perception datasets (e.g., SALICON's 10k images) and is a valuable community resource (Section 3, Table 1).

2. **Ad-LLaVA control disentangles content from behavior.** The paper trains Ad-LLaVA on the same BLIFT videos and images (with scene descriptions) but without behavior labels. Ad-LLaVA performs comparably to the base LLaMA-Vid, while Behavior-LLaVA outperforms both. This controlled ablation (Section 3, line 163) provides meaningful evidence that the improvement is attributable to the behavioral signal, not merely exposure to more video content.

3. **Consistent improvements across a broad evaluation suite.** Across 46 tasks spanning image, video, text, and audio (26 benchmarks), Behavior-LLaVA improves over LLaMA-Vid in both zero-shot and fine-tuned settings. Gains are notable on complex high-level tasks: up to 43–87% on video understanding (Table 2), and Behavior-LLaVA matches supervised memorability SOTA while using only 25% of the training data (Table 4). The trend is highly consistent — Behavior-LLaVA improves on nearly every task.

4. **Zero-shot transfer to non-visual modalities.** Behavior-LLaVA, trained only on image/video behavior, shows 19.5% improvement on audio summarization and text sentiment analysis (Section 4, Table 6), indicating that behavioral signals impart modality-agnostic content understanding.

## Weaknesses

### Major

1. **The causal claim is not fully isolated from the "more text tokens" confound.** The paper argues that behavior *content* drives improvement. Behavior-LLaVA receives behavior strings (comments, likes) as additional text tokens during training. The Ad-LLaVA control removes behavior but still provides scene descriptions — so it controls for exposure to more *video content*, but not for the presence of additional *language tokens* in the training objective. The improvement could partially reflect a richer language modeling objective (more tokens to predict) rather than anything specific about behavior. A control where behavior strings are randomly shuffled (preserving token length and distribution but destroying content signal) would cleanly separate these explanations. Without it, the paper's strongest causal interpretation — "behavior contains signals about content" — remains plausible but incompletely proven. The paper would be strengthened by acknowledging this distinction more explicitly rather than presenting Ad-LLaVA as a complete causal control.

2. **Zero-shot memorability results rest on near-floor absolute numbers.** On memorability (Table 4), Behavior-LLaVA improves from 0.02–0.13 (LLaMA-Vid) to 0.07–0.21, while human consistency is 0.61–0.78. The paper reports 160–350% relative improvements, which are mathematically correct but inflate the apparent practical significance of moving from near-random to still-very-low absolute performance. The paper should be more careful to distinguish relative improvement on these tasks from the fine-tuned results (where 25% data matches full-data SOTA — a genuinely strong result). This does not undermine the paper's contribution but the framing overstates what the zero-shot numbers convey.

### Minor

3. **Perception vs. action ablation is confounded by dataset scale.** The paper compares Behavior-LLaVA trained on BLIFT (730k samples) vs. Salicon10k (10k samples) and finds perception behavior gives smaller gains. The paper briefly acknowledges the scale confound (line 57: "We posit that one reason for this could be due to the scale"), but contribution point 3 (line 57) still draws a conclusion about perception vs. action behavior without sufficiently caveating the 73× difference. A proper ablation would hold dataset size constant (e.g., subsample BLIFT to 10k). As presented, the comparison tells us more about data scale than about inherent utility of perception vs. action signals.

4. **No error bars or statistical significance for any result.** Given 46 tasks and evaluation protocols that may have stochastic variation (especially in fine-tuned settings where margins are as small as 0.86% on Ekman-6, Table 3), the absence of confidence intervals or multi-run estimates makes it difficult to assess which improvements are reproducible vs. within noise. This is a standard concern and should be addressed with at least a few representative multi-run experiments.

5. **GPT-4V-as-judge for dense captioning is unvalidated.** The paper uses GPT-4V to evaluate dense captions on correctness, detail, and quality (Section 4), but reports no human correlation. Given that Behavior-LLaVA shows a *decrease* in correctness but improvements in detail/quality (line 376), it is unclear whether GPT-4V's preferences align with human judgments or whether the model is trading factual accuracy for more vivid (potentially hallucinated) details learned from comment data. A small-scale human evaluation would substantially strengthen this analysis.

6. **"Free lunch" claim is overstated.** The abstract describes behavior-data improvements as "essentially free-lunch," but the paper describes extensive curation effort: NSFW filtering, TF-IDF deduplication, minimum word counts, >10k view thresholds, manual category exclusion, and more (Section 3). This is not cost-free. The core insight — that behavior data is cheaper to collect at scale than lab-collected perceptual data — is valid and interesting without the "free lunch" rhetoric.

### Trivial

- The title says "LLMs" but the paper works with VLMs. The paper correctly frames itself around vision-language models throughout, so this is a minor mismatch.
- Minor British/American spelling inconsistency ("Behaviour" vs. "Behavior") in a few places (e.g., line 49, line 352, line 378), though the paper predominantly uses "Behavior."

## Nice-to-Haves

- A control with shuffled/permitted behavior strings to fully isolate the behavioral content signal from extra language tokens.
- Error bars for at least the fine-tuned results with small margins (e.g., emotion benchmarks).
- Small-scale human evaluation to validate the GPT-4V dense captioning judgments.
- Brief discussion of distributional biases from the heavy filtering pipeline (e.g., >10k view threshold, top-comment selection) and how these might affect generalizability.
- Ethics/consent discussion around use of public Reddit/YouTube comments, even if brief.

## Removed Points

These points were flagged by reviewers but are removed as per meta-review guidelines:

- *Reproducibility concern about missing hyperparameters*: The paper discloses the key hyperparameter (1:1 sampling ratio, 2.2 epochs, line 154–158). Removed per rule on trivial reproducibility nitpicks.
- *Criticism about "not yet released" / unverifiable models/references*: All cited models, datasets, and benchmarks are assumed to exist per guidelines. Removed.
- *Generic strength about "addressing an important problem" (from Strength Finder)*: Dropped per rule requiring specific, citable content in strengths.
- *Typos/formatting/style nitpicks not related to scientific content*: Removed per hard rules.

## Novel Insights

The paper's most interesting finding is that *action-level* behavior (likes, comments) — which is cheap, abundant, and noisy — appears to transfer to high-level content understanding tasks (emotion, persuasion, memorability) more effectively than the perception-level signals (saliency) that prior work has relied on. This turns a practical observation (action data scales better) into a structured hypothesis about the nature of behavioral supervision: perhaps the semantic richness of natural language comments carries more content-relevant signal than fixation heatmaps, even at much smaller scale. The paper does not fully prove this (the scale confound prevents it), but it provides enough evidence to be genuinely thought-provoking for the community. The finding that behavior-training transfers to *audio* and *text* tasks despite being trained only on images and videos is a striking emergent property worth deeper investigation.

## Suggestions

- Add a control experiment with permuted/shuffled behavior strings (same token length, no content signal) to distinguish the effect of behavioral content from additional language-modeling tokens.
- Reframe the zero-shot memorability results with clear caveats about absolute performance levels; lead with the fine-tuned results (25% data matching SOTA) which are the stronger contribution.
- Acknowledge the perception-vs-action scale confound more prominently and either subsample BLIFT to match SALICON size or temper the conclusion.
- Provide at least 3-run averages with standard deviations for a representative subset of the fine-tuned evaluations (especially the emotion benchmarks where margins are <5%).
- Validate the GPT-4V captioning evaluation with a small human study on 50–100 samples.

## Score and Decision

The paper makes a genuine contribution: a large-scale behavioral dataset and a carefully executed demonstration that training on receiver behavior improves VLM performance across an impressively broad suite of tasks. The Ad-LLaVA control, extensive evaluation, and consistent improvements provide solid evidence for the core empirical claim. The weaknesses — incomplete causal isolation, confounded ablations, absence of error bars — are real but addressable and do not invalidate the contribution. This is a solid paper that would be strengthened by the suggested revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>