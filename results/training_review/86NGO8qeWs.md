## Summary

This paper identifies an important gap — compositional reasoning in audio-language models (ALMs) — and proposes two contributions: (1) **CompA**, a benchmark suite with CompA-order (400 instances, real-world AudioSet audios) and CompA-attribute (200 instances, synthetic audios) to evaluate whether ALMs understand event ordering and attribute-binding, and (2) **CompA-CLAP**, a two-stage fine-tuning method that combines composition-aware hard negatives with a modular contrastive learning objective. On CompA-order, CompA-CLAP achieves a group score of 33.85 vs. random 16.67 and far outperforms all baselines (best baseline CLAP-LAION: 5.50). On CompA-attribute, the improvement over baselines is marginal (group 15.13 vs. random 16.67), and the model's audio retrieval direction is below chance.

## Strengths

- **First systematic study of compositional reasoning in ALMs.** The paper correctly identifies that existing audio-retrieval benchmarks (Clotho, AudioCaps) do not test compositionality (Fig. 1 shows only ~0.04 R@1 drop after word shuffling, and most captions have a single acoustic event). The CompA benchmark directly fills this gap. This is a timely and well-motivated contribution.

- **Expert-annotated benchmark with real-world audios for order understanding.** CompA-order uses >90% real-world audio from AudioSet Strong, annotated by four subject-matter experts. The Winoground-inspired paired-instance format cleanly isolates compositional reasoning from other retrieval abilities. The human baseline of 87-90% confirms the task is meaningful.

- **Significant improvements on CompA-order.** CompA-CLAP achieves a group score of 33.85 on CompA-order, far exceeding all baselines (CLAP-LAION: 5.50, CLAP (ours): 11.50). Both ablations confirm that the hard-negative stage and the modular contrastive stage each contribute substantially (removing either drops group score from 33.85 to ~20-21).

- **Novel modular contrastive loss that overcomes data scarcity.** The template-based approach to constructing compositional audios from single-event snippets and generating multi-granularity positives/negatives is clever and addresses a genuine bottleneck (lack of compositional audio-caption pairs). The method does not require pre-existing compositional pairs.

- **Retention of standard benchmark performance.** CompA-CLAP performs on par with vanilla CLAP on text-to-audio retrieval, audio-to-text retrieval, and zero-shot classification (Table 1), showing that compositionality fine-tuning does not sacrifice general capability.

## Weaknesses

### Fatal
None. While several issues are serious, none individually invalidates the core contributions beyond repair.

### Major

1. **Missing verification of train/test disjointness from AudioSet Strong.** CompA-order test instances, the AudioSet-CompA training dataset (≈110k pairs), and the modular contrastive training pool (≈500k single-event snippets) are **all drawn from AudioSet Strong**. The paper provides no statement that the test instances are disjoint from the training data. If any audio (or snippet that appears in a test audio) was also used in the training pool or AudioSet-CompA, the evaluation is contaminated and the claimed improvements are artifacts. This must be explicitly confirmed before any results can be trusted. This is the single most serious weakness.

2. **CompA-attribute performance is below random on the audio retrieval direction, substantially weakening the central claim.** CompA-CLAP's group score on CompA-attribute is 15.13 vs. random 16.67, and its audio score is 22.52 vs. random 25.0. The model systematically prefers the *wrong* audio more than 75% of the time. While the paper acknowledges this ("worse than our random baseline…leaves plenty of room for improvement"), the abstract and introduction still claim that CompA-CLAP "significantly improves compositional reasoning." The headline claim of "10%-28% improvement on the CompA benchmark" conflates the strong CompA-order results with the near-negligible CompA-attribute results (where the best improvement over baselines is ~2.6% relative on group score). Given that attribute-binding is one of the two compositional abilities the paper claims to address, this gap is significant.

3. **The "10%-28%" improvement claim is imprecise and potentially misleading.** The paper states that "CompA-CLAP outperforms all our baselines on the CompA benchmark by 10%-28%." However, the improvement on CompA-attribute group score over CLAP (ours) is only ~2.6%. The 10-28% range does not cleanly match any single metric in Table 2. This claim blurs the distinction between the strong CompA-order results and the much weaker CompA-attribute results.

### Minor

1. **No justification for the asymmetric loss formulation.** In both training stages, hard negatives (Stage 1) and generated negatives (Stage 2) are only added to the audio-to-text loss (ℓ^{a→t}), not the text-to-audio loss (ℓ^{t→a}). This asymmetry is not discussed or justified. Since the evaluation measures both directions (text score and audio score), treating them asymmetrically in training could explain why the audio score on CompA-attribute is especially weak.

2. **No ablation isolating the text encoder change.** The paper replaces RoBERTa with Flan-T5-large (citing prior work) and trains its own CLAP on CompA-661k. The resulting CLAP outperforms CLAP-LAION by "0.15%-4.67%" on retrieval and "11.85%-23.8%" on CompA. Without an ablation that keeps the text encoder fixed, it is impossible to attribute these gains to the compositionality-focused data/training versus the stronger text encoder.

3. **Quality of LLM-generated hard negatives and synthetic modular audios is not analyzed or validated.** GPT-4 generates the hard negative captions, but no analysis is provided of whether these are genuinely "hard" (plausible but compositionally different) versus semantically implausible and easily rejected. Similarly, the modular training uses concatenated/overlaid audio snippets without any evaluation of whether the resulting mixtures sound natural or preserve the intended compositional relationships. If the synthetic audios are unrealistic, the model may learn shortcuts that do not transfer to real-world compositional reasoning.

4. **No statistical significance tests on standard retrieval benchmarks (Table 1).** While CompA results (Table 2) include standard deviations across 3 seeds, the retrieval and zero-shot results in Table 1 do not. Given that CompA-CLAP's scores are very close to CLAP (ours) on these benchmarks (e.g., T-A R@1 AudioCaps: 36.1 vs. 35.9), it is unclear whether the minute differences are meaningful or noise.

### Trivial

- The number of hard negatives K per audio is not explicitly stated.
- The templates and preposition list used for caption generation are not provided.
- The pool construction in "More details in \ref{subsubsection:template}" references a subsection that appears to be in the (stripped) appendix.
- The modular contrastive training caps positives/negatives at 7 without justification.

## Nice-to-Haves

- **Direction bias analysis for CompA-order.** It would strengthen the benchmark to report whether lower-performing models systematically prefer one ordering (e.g., always "A then B") regardless of the correct answer, which would indicate prior bias rather than failed compositionality.
- **Adapt NegCLIP to audio** as a stronger baseline, to contextualize CompA-CLAP's improvements relative to the best-known VLM compositional reasoning method.
- **Per-attribute breakdown on CompA-attribute** to identify which attribute types (source, qualitative, etc.) drive the failures.
- **Human evaluation of modular synthetic audio quality** to assess whether the training mixtures sound natural.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Modular contrastive learning claim about not requiring compositional pairs is misleading because it requires single-event snippets"** — This is a misreading. The paper's claim is precise: it does not require *compositional audio-caption pairs*. Single-event snippets are trivially available and are clearly described as the building blocks. This is not misleading.
- **"The paper glosses over CompA-attribute failure"** — The paper explicitly states in Section 4: "However, all models, including CompA-CLAP, perform worse than our random baseline on CompA-attribute, which leaves plenty of room for improvement." The paper does not gloss over this.
- **"The shuffling experiment is weak evidence"** — The paper also provides noun-distribution analysis (Fig. 3.1), so this criticism omits supporting evidence.
- **Various pure formatting nitpicks** about figure placement, section numbering, and whitespace — these are artifacts of PDF extraction.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the train/test overlap concern (which the paper should have addressed), and the asymmetric loss pattern is worth noting, but neither constitutes a novel observation about the field that the authors themselves did not identify.

## Suggestions

1. **Explicitly confirm train/test disjointness.** State that no audio file (or snippet) in CompA-order or CompA-attribute appears in AudioSet-CompA or the modular training pool. Provide a quantitative check (e.g., by file hash, by timestamp overlap analysis, or by citing the specific split methodology used from AudioSet Strong).

2. **Restructure the narrative around CompA-attribute.** Either (a) present CompA-attribute as a challenging diagnostic that current methods do not solve (framing it as a finding rather than a success), or (b) include additional experiments or analyses that explain why the audio retrieval direction fails and whether the modular training can be improved to address it. The abstract and introduction should not claim "significantly improves compositional reasoning" without caveat.

3. **Provide ablations to isolate contributions.** Add an ablation comparing Flan-T5 vs. RoBERTa as the text encoder with the same training data, to separate the encoder effect from the compositionality-specific training. Justify the asymmetric loss or provide a symmetric variant.

4. **Add statistical significance** to Table 1, at minimum for the close-call comparisons (CompA-CLAP vs. CLAP on retrieval benchmarks).

5. **Analyze hard negative quality** with examples showing whether GPT-4-generated negatives are truly hard (i.e., plausible but compositionally different) versus trivially distinguishable.

## Score and Decision

This paper tackles an important, underexplored problem and offers both a benchmark and a training approach that shows clear improvements on the order-understanding front. The CompA benchmark alone is a valuable resource for the community. However, the missing train/test disjointness verification is a serious methodological gap — until resolved, the evaluation results cannot be fully trusted. Combined with the below-chance performance on attribute-binding audio retrieval and the imprecise headline claims, the paper as submitted does not convincingly establish its contributions. The work could become a strong paper with major revisions addressing the data overlap concern, providing a more honest and nuanced discussion of CompA-attribute, and adding the requested ablations.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>