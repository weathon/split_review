Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes CompA, a collection of two expert-annotated benchmarks (CompA-order and CompA-attribute) for evaluating compositional reasoning in audio-language models (ALMs), and CompA-CLAP, a two-stage fine-tuning method that combines composition-aware hard negatives with a novel modular contrastive learning objective. The CompA benchmarks fill an important gap: existing audio retrieval benchmarks are insufficient for evaluating compositionality, as demonstrated by the paper's finding that ALMs are largely insensitive to word order on standard benchmarks. CompA-CLAP achieves substantial improvements on CompA-order (group score rising from 11.50 to 33.85 over the authors' own CLAP baseline) while maintaining performance on standard retrieval and classification tasks. However, performance on CompA-attribute remains near or below random chance for all models.

## Strengths

1. **First dedicated benchmark for compositional reasoning in audio-language models.** Prior work in compositionality has focused nearly exclusively on vision-language models (Winoground, NegCLIP, CREPE). The paper correctly identifies that no systematic study of compositionality exists in the audio space (Section 1), and the CompA benchmarks — with 400 (order) and 200 (attribute) expert-annotated instances using majority real-world audio from AudioSet — directly address this gap. The paper demonstrates convincingly (Fig. 1, Section 2.1) that standard retrieval benchmarks like Clotho and AudioCaps are insufficient for evaluating compositionality because CLAP's performance degrades by only 0.04 R@1 when word order is shuffled.

2. **Demonstrably effective method for improving order understanding.** CompA-CLAP raises the group score on CompA-order from 11.50 (CLAP ours) to 33.85 (Table 2). Ablations confirm the contribution of both training stages: removing hard negatives drops the order group score from 33.85 to 20.20, and removing modular contrastive drops it to 21.25. The improvement on CompA-order is substantial and represents a genuine advance in audio compositional reasoning.

3. **Performance retention on standard benchmarks.** CompA-CLAP maintains competitive performance on text-to-audio retrieval (AudioCaps R@1: 36.1) and zero-shot classification (ESC-50: 89.1%, US8K: 85.7%) despite being fine-tuned specifically for compositionality (Table 1). This is non-trivial and demonstrates that compositional reasoning can be improved without catastrophic forgetting.

4. **Methodological innovations to address data scarcity.** The paper proposes a template-based synthetic audio-caption creation method that generates ~251k compositional training audios and ~110k real compositional pairs (AudioSet-CompA), overcoming the acute scarcity of compositional audio data noted in Section 3.1. The use of GPT-4 to generate semantically valid hard negatives and the modular contrastive loss that does not require existing compositional audio-caption pairs are practical contributions.

## Weaknesses

### Fatal

None.

### Major

None. The paper's most significant weakness — poor performance on CompA-attribute — is openly acknowledged by the authors (line 279: "all models, including CompA-CLAP, perform worse than our random baseline on CompA-attribute").

### Minor

1. **Attribute binding remains essentially unsolved.** CompA-CLAP achieves a group score of 15.13 on CompA-attribute, marginally above the authors' own CLAP baseline (14.75) and below the random baseline (16.67). The improvement is ~0.4 percentage points and, despite tiny reported standard deviations, is not practically meaningful. The paper's broad claim (abstract) that "CompA-CLAP significantly improves over all our baseline models on the CompA benchmark" does not adequately differentiate between the large, convincing gains on CompA-order and the essentially null result on CompA-attribute. The introduction's claim of "10%-28%" improvement does not hold for most attribute metrics (e.g., attribute text improves by 4.4%, attribute group by 2.6%).

2. **Baseline comparison partially confounded by text encoder choice.** The authors' CLAP uses Flan-T5-large as the text encoder rather than RoBERTa used by prior CLAP variants. While the main comparison (CLAP ours → CompA-CLAP) controls for this, the paper attributes the large gap between CLAP (ours) and CLAP-LAION on CompA-order (group 11.50 vs. 5.50) to "the better dataset and encoder" without isolating the encoder's contribution. An ablation initializing CompA-CLAP from a RoBERTa-based CLAP would strengthen the claim that the method itself, not just the encoder upgrade, drives the improvement.

3. **Synthetic training data quality is not validated.** The modular contrastive learning stage generates 251k synthetic audios by concatenating/overlaying single-event snippets from a pool of 500k, using template-based captions. The paper does not report any human evaluation or automated quality check (e.g., sound event detection accuracy) to confirm that these synthetic compositions sound natural, contain the intended acoustic events, or that the template captions are linguistically diverse. Given that the method is evaluated partly on real-world audio (CompA-order), this creates uncertainty about how well the synthetic training distribution matches the test distribution.

4. **The "10%-28%" improvement claim is imprecise.** Verifying this claim against Table 2: CompA-CLAP vs. CLAP (ours) improvements range from 2.6% (attribute group) to 194% (order group). Only CompA-order text (20.6%) falls cleanly within the stated range. While approximate ranges are acceptable in narrative text, the discrepancy between the stated range and the actual numbers across most metrics is noticeable.

### Trivial

- The paper states "All scores have been averaged for 3 runs on 3 random seeds" but the standard deviations for CompA-CLAP in Table 2 are extremely small (≤0.20), which is unusual for a 200–400 instance benchmark. A brief explanation of how variance is computed would be helpful.

## Nice-to-Haves

- **Validation of synthetic training data:** A small human rating study or sound event detection analysis on the 251k synthetic audios would increase confidence that the training data captures the intended compositional structure.
- **Qualitative failure analysis on CompA-attribute:** Understanding why the model fails at attribute binding — does it systematically prefer one type of misbinding? — could guide future work.
- **Ablation of Kpos/Kneg:** The paper fixes Kpos, Kneg ≤ 7; analysis of how performance varies with the number of compositional granularities would inform practical usage.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Random baseline error for CompA-attribute" (Harsh Critic, Critical Issue #1):** The critic claimed the random group score for CompA-attribute should be 50% rather than the reported 16.67%. This is **factually incorrect**. For a 2-pair instance, the group score requires **all four** inequalities from both the text and audio scores to hold simultaneously (Eqs. 4-6). Under i.i.d. random similarities, this requires that {s(C0,A0), s(C1,A1)} are the two largest among four values — probability = 1/6 ≈ 16.67%. The paper's math is correct; the critic confused the individual text/audio scores (25% each) with the more stringent group score. The critic's downstream claims that "the model performs far below chance" and "has learned an inverse mapping" are based on this mathematical error and are unfounded.

2. **"The paper does not discuss potential transfer from VLM compositionality methods to audio" (Section-by-Section note).** This is a scope-creep request. The paper already discusses NegCLIP and CREPE as inspiration. Requiring explicit adaptation of VLM methods to audio in a first-of-its-kind paper is beyond reasonable expectations.

3. **"The paper does not discuss potential train-test distribution gap" (Section 3 note on synthetic audios).** The paper explicitly states that CompA-attribute uses WavJourney-generated audios validated by experts (Section 3.3). The limitation is noted. This is covered by weakness #3 above in a more precise form.

4. **"Reproducibility details for GPT-4 prompting" note:** The paper states GPT-4 prompts would be in the appendix. Missing appendix content is a parser artifact, not an author error.

## Novel Insights

The reviews surface one genuinely novel insight beyond the paper's own contributions: the **asymmetry between order understanding and attribute binding** in audio-language models appears to be substantially larger than what has been observed in vision-language models. In the VLM literature (Winoground, NegCLIP), models typically struggle roughly equally with both phenomena. The fact that CompA-CLAP achieves a 33.85 group score on CompA-order (3× the CLAP baseline) but remains at chance (15.13, below random 16.67) on CompA-attribute suggests that **audio attribute binding may be a fundamentally harder problem** — possibly because acoustic attributes (source, quality, pitch) are perceptually more entangled in the audio signal than visual attributes are in images, making contrastive representation learning less effective for disambiguation. This insight is worth stating explicitly and could motivate dedicated architectural solutions for attribute binding in audio.

## Suggestions

1. **Scope the claims precisely.** Replace "improves compositional reasoning" in the abstract and intro with a two-part claim: "substantially improves order understanding (group score 11.50→33.85 on CompA-order) while attribute binding remains an open challenge." This is far more honest and still impressive.

2. **Acknowledge and discuss the order/attribute asymmetry explicitly.** The paper presents this as a uniform failure, but the contrast between order and attribute performance is the most interesting finding in the results. A dedicated analysis of why modular contrastive learning succeeds for order but not attribute would strengthen the paper considerably.

3. **Add an ablation varying the text encoder** (e.g., RoBERTa vs. Flan-T5) in the hard-negative training stage. This would directly address concerns about whether the encoder upgrade or the method itself drives improvements.

4. **Run a small human evaluation on the synthetic training data** (e.g., 100 samples rated by 2 annotators) to validate that the template-based concatenations/overlays produce recognizable compositional audio. This is a quick experiment that would significantly increase confidence in the training methodology.

## Score and Decision

**Originality:** 7/10 — First systematic study of audio compositional reasoning; novel modular contrastive loss.
**Importance of research question:** 8/10 — Compositional reasoning is a well-recognized limitation of contrastive models; extending this to audio fills a clear gap.
**Claims support:** 6/10 — Strong evidence for order understanding; the 10-28% improvement claim and abstract framing overstate the attribute results.
**Soundness of experiments:** 7/10 — Benchmarks are well-designed and expert-annotated; encoder confounding and lack of synthetic data validation are minor concerns.
**Clarity:** 7/10 — Generally well-written; the random baseline calculation is correct but could be explained more explicitly to prevent misinterpretation.
**Value to community:** 8/10 — CompA benchmarks are likely to become a standard evaluation for audio compositionality; the method provides a strong baseline for future work.

The paper makes a genuine contribution through its carefully constructed benchmarks and a method that convincingly improves order understanding. The primary weakness is not a methodological flaw but an overclaim: the paper's framing implies broader compositional reasoning gains than the evidence supports, since attribute binding remains at chance. However, the paper openly acknowledges this limitation in its Results section. The benchmark contribution alone is valuable enough to merit acceptance, as it provides the community with a much-needed evaluation tool. The modest methodological contribution on the attribute side does not invalidate the substantial contribution on the order side.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>