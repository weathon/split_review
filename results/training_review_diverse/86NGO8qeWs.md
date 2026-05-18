Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper makes two contributions: (1) **CompA**, a pair of expert-annotated benchmarks (CompA-order and CompA-attribute, 400+200 instances) in the Winograd twin-sentence format that test compositional reasoning in audio-language models (ALMs), and (2) **CompA-CLAP**, a two-stage fine-tuning method combining composition-aware hard negatives with a novel modular contrastive loss to improve compositional reasoning. The benchmarks reveal that existing ALMs perform near or below random chance on compositional understanding, and CompA-CLAP substantially improves over baselines on CompA-order (e.g., group score from 5.50% to 33.85%) while largely retaining performance on standard retrieval and classification benchmarks.

## Strengths

- **First systematic benchmark for compositional reasoning in ALMs.** CompA-order and CompA-attribute are carefully designed with expert annotation, real-world audio (90%+ from AudioSet Strong), and a Winoground-style evaluation that directly tests whether models can match the right caption to the right audio when only composition differs. Human performance (87.4% group on CompA-order) vs. all existing models near or below random proves the gap is real and severe — a clear and valuable finding.

- **CompA-CLAP produces meaningful and controlled improvements.** The proposed two-stage training boosts group score on CompA-order from 11.50% (CLAP-ours) to 33.85%, and improves over all baselines on every metric on both benchmarks (Table \ref{tab:compa-results}). These gains come with minimal degradation on standard retrieval (Table 1: AudioCaps/Clotho R@1 changes within ±0.4) and zero-shot classification (ESC-50: 90.2→89.1, US8K: 86.1→85.7), showing the fine-tuning does not sacrifice general capability.

- **Ablation study validates each component.** The paper includes ablation rows ("- Hard Negative" and "- Modular Contrastive") in Table 3, confirming that removing either stage degrades performance, with the full model achieving the best results.

- **Tackles data scarcity with a scalable synthetic approach.** The modular contrastive framework generates ~251k training audios from single-event snippets and their labels, providing a practical solution to the acute lack of compositional audio-text pairs in existing datasets.

## Weaknesses

### Major

- **Asymmetric loss formulation is not discussed and likely explains the systematically poor audio scores.** In both stages, hard negatives appear only in the audio-to-text direction (ℓ^{a-2-t}, Eq. 5 and Eq. 7) and are absent from the text-to-audio direction (ℓ^{t-2-a}, Eq. 4 and Eq. 6). Concretely:

  - Stage 1, Eq. 4 (ℓ^{t-2-a}): denominator = Σⱼ exp(t_i^⊤ a_j / σ) — *no hard negatives*
  - Stage 1, Eq. 5 (ℓ^{a-2-t}): denominator = Σⱼ exp(a_i^⊤ t_j / σ) + Σₖ exp(a_i^⊤ t_{i_k}^{hard} / σ) — *includes hard negatives*
  - Stage 2, Eq. 6 (ℓ^{t-2-a}): denominator = Σⱼ exp(t_i^⊤ a_j / σ) — *no hard negatives*
  - Stage 2, Eq. 7 (ℓ^{a-2-t}): denominator = Σⱼ exp(a_i^⊤ t_j / σ) + Σₖ exp(a_i^⊤ t_{i_k}^{neg} / σ) — *includes hard negatives*

  Crucially, ℓ^{t-2-a} (text→audio) contributes to the **audio score** (given a caption, select the correct audio), while ℓ^{a-2-t} (audio→text) contributes to the **text score** (given an audio, select the correct caption). The loss asymmetry therefore directly maps to the observed performance gap: text scores are consistently higher than audio scores, and on CompA-attribute even CompA-CLAP's audio score (22.52) remains below random (25.0). The paper never discusses this asymmetry or its potential consequences. The authors should either explain the design rationale, investigate whether adding hard negatives to the text-to-audio direction resolves the deficiency, or acknowledge this as an explicit limitation.

- **Evaluation metrics for three-pair instances are not defined.** The paper states that 100 out of 400 CompA-order instances have three audio-caption pairs (C₂, A₂) where events occur simultaneously (line 87). However, Section 3.4 defines the text, audio, and group scores (Eqs. 1–3) only for the two-pair case. How these metrics extend to three-pair instances is never specified, making it impossible for readers to verify the reported random baselines (text=19.70, audio=19.70, group=16.67) or reproduce the evaluation. This is a missing technical specification that must be provided.

### Minor

- **Confounding of architectural/data improvements with novel loss contributions.** The "CLAP (ours)" baseline already replaces RoBERTa with Flan-T5-large and uses CompA-661k, outperforming CLAP-LAION on CompA-order text score by 9.75 points (33.75 vs. 24.0). The proposed two-stage fine-tuning adds a further 6.95 points. While the ablations in Table 3 isolate the marginal contribution of each stage *starting from the stronger CLAP (ours)*, the paper does not ablate whether applying the novel losses to the original CLAP-LAION (with RoBERTa) would produce similar gains. The majority of the overall improvement over the literature baseline comes from architecture/data choices, and a reader cannot fully disentangle the contributions. An additional ablation using the original CLAP architecture would clarify this.

- **Synthetic training-to-real transfer is not analyzed.** The modular contrastive data concatenates/overlays short AudioSet Strong snippets with template-generated captions — audios where events are strictly sequential or perfectly overlaid with no natural acoustic interaction. While the aggregate CompA improvements suggest transfer, there is no per-instance analysis (by event distinctness, background noise level, or number of acoustic events) to establish whether the gains concentrate on test cases that resemble the synthetic training distribution. The paper offers only qualitative observations (line 281) about when the model performs better or worse.

- **AudioSet-CompA annotation details are sparse.** The 110k-pair dataset is central to the hard-negative training stage, but the paper provides only that "two human annotators evaluated and corrected GPT-4 captions." No inter-annotator agreement, correction workload statistics, or quality metrics are reported. These details would help establish the reliability of this resource.

### Trivial

- **"Marginally better than random chance" (abstract) is imprecisely stated.** On most baseline models, the audio and group scores are *below* random (e.g., CLAP-LAION group = 5.50 vs. random 16.67 on CompA-order). Characterizing this as "marginally better" is too generous; "near or below random" would be more accurate.

## Nice-to-Haves

- Provide the GPT-4 prompts used for hard-negative generation and template creation, along with a small validation set for generated text.
- Report a breakdown of the synthetic modular training data by number of events (2/3/4) and construction type (concatenation vs. overlay).
- Expand the benchmark with more instances and provide confidence intervals accounting for benchmark sampling variance (not just seed variance from 3 runs).

## Removed Points

- **Criticism about models "not yet released" or "cannot be independently verified":** None present in the original review. The paper provides a project page URL.
- **Notation inconsistency gripe about t_i vs. t^{pos}_{i_k}:** The notation in Eq. 4 (stage 1) is internally consistent — there are no t^{pos} in stage 1. The real issue is the *asymmetry of hard-negative inclusion*, which is covered in Major weakness #1 above.
- **Criticism that below-random audio scores "fundamentally undermines" compositional reasoning claims:** The paper's core claim is that CompA-CLAP *improves* over baselines (which is supported). The claim is comparative, not absolute. The paper also explicitly acknowledges the limitation (line 279). The asymmetry concern is serious but does not invalidate the comparative result.
- **Criticism about the synthetic data being artificial:** This is an inherent property of the approach, not a flaw. The paper is transparent about the synthetic nature of the modular data. The reasonable remaining ask (per-instance analysis) is retained as a Minor weakness.

## Novel Insights

The most valuable analytical observation across the reviews — and one the paper itself does not make — is that the **hard-negative inclusion asymmetry maps directly onto the evaluation asymmetry**: ℓ^{a-2-t} (which gets hard negatives) drives the text score (above random), while ℓ^{t-2-a} (no hard negatives) drives the audio score (below random on CompA-attribute). This is not a side note; it is a plausible structural explanation for the paper's most puzzling result. If this connection holds, it suggests the audio-score deficiency may be a consequence of an asymmetric training design choice rather than an inherent limitation of the approach. Investigating this would substantially strengthen the paper.

## Suggestions

1. **Address the loss asymmetry.** Add hard negatives (or the modular negatives) to the ℓ^{t-2-a} direction in both stages, or provide a principled justification for why they are intentionally excluded from one direction only. Report whether this resolves the audio-score deficiency on CompA-attribute.
2. **Define the 3-pair evaluation metric.** Specify how text, audio, and group scores extend to instances with three audio-caption pairs, and how the random baselines (19.70, 16.67) are derived.
3. **Add an ablation that starts from the original CLAP-LAION architecture.** Apply the hard-negative and modular contrastive stages to the original CLAP (with RoBERTa and LAION-630K) to isolate the value of the loss formulations independent of the architecture/data improvements.
4. **Add per-instance analysis on CompA test sets.** Categorize instances by acoustic similarity, number of events, and whether events are present in AudioSet, and report accuracy per category to establish where synthetic-to-real transfer succeeds and fails.

## Score and Decision

This paper addresses a genuine and underexplored problem — compositional reasoning in audio-language models — and provides two valuable contributions: carefully designed benchmarks and a method that delivers real improvements. The weaknesses are significant but addressable: the most serious (asymmetric loss formulation and undefined 3-pair metrics) can be resolved in a revision. The benchmarks alone are a standalone contribution that advances the field. I recommend acceptance conditional on addressing the two Major weaknesses.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>