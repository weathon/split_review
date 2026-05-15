Here is the consolidated final review:

---

## Summary

This paper introduces RiTTA, a framework for studying event relation modeling in Text-to-Audio (TTA) generation. The authors construct a taxonomy of four relation categories (Temporal Order, Spatial Distance, Count, Compositionality) with 11 sub-relations, create a synthetic benchmark by blending seed audio clips from 25 event categories, propose a multi-stage evaluation metric (MSR-RiTTA) that checks presence, relation correctness, and parsimony, and fine-tune Tango on the synthetic data to improve relation modeling. The paper identifies a genuine gap — existing TTA models largely ignore inter-event relations — and provides a structured starting point for future work.

## Strengths

- **Structured relation taxonomy**: The paper defines four main relation categories and 11 sub-relations (Table 2) spanning temporal, spatial, and compositional dimensions. This provides a clear organizational framework that has been absent in prior TTA work and can serve as a foundation for future research.

- **Empirical demonstration of a real gap**: Through systematic benchmarking of seven TTA models on the proposed dataset, the paper shows that even the best model (Tango 2) scores below 1% on both presence accuracy and relation correctness (mAPre=0.02%, mARel=0.04%). This concretely demonstrates that relation modeling is an unsolved problem, validating the paper's motivation.

- **Conceptually clean multi-stage metric**: The MSR-RiTTA framework decomposes evaluation into presence, relation correctness, and parsimony stages (Section 3.4). Averaging across detection thresholds (inspired by COCO mAP) is sensible. The metric generates richer signal than global FAD/KL scores, and the paper shows these metrics can produce different rankings (Table 5), supporting the need for relation-aware evaluation.

- **Fine-tuning shows the benchmark enables improvement**: Fine-tuning Tango on the synthetic dataset yields consistent improvements across relation metrics relative to the baseline (Table 8), demonstrating the benchmark's utility as a training resource even if absolute scores remain low.

## Weaknesses

### Fatal

None.

### Major

1. **Evaluation metric is not validated** (Sections 3.4, 5.3). The MSR-RiTTA metric depends on a "finetuned PANNS" model to detect audio events from generated audio, but the paper reports no accuracy, precision, or recall of this detector on the synthetic test set, and provides no human evaluation to establish correlation with human judgment. Since all quantitative conclusions — the finding that existing models fail, the ranking of methods, the improvement from fine-tuning — flow through this instrumentation, the lack of validation is a significant gap. It is possible that detector failures (e.g., domain mismatch between PANNS training data and the benchmark's synthetic audio) inflate or deflate reported scores in unknown ways. The paper should, at minimum, report per-class detection accuracy on the test set and conduct a human listening study on a sample of generations.

2. **Synthetic ground truth is a simplified proxy, but the paper overclaims scope** (Sections 3.3, 5.1, Abstract, Conclusion). Ground truth audios are created by linearly blending or concatenating isolated event clips, producing clean event boundaries and no acoustic interaction (e.g., masking, reverberation, frequency overlap). The abstract and conclusion claim the corpus covers "all potential relations in real-world scenarios," but linear blending of two clean clips is far from the acoustic complexity of real overlapping, interacting events. This overclaim is misleading; the paper would be better served by honestly characterizing the benchmark as a simplified initial testbed.

3. **Fine-tuning results are too weak to support the conclusion that "audio events relation can indeed be modelled by TTA methods"** (Section 5.4, Table 8, line 241). Even after fine-tuning, absolute scores remain extremely low (e.g., mAPre ~1.97%, as referenced in the reviewer's critique). The claim that relation modeling "can indeed be modelled" requires demonstrating practically meaningful correctness, not just a statistically significant improvement over a near-zero baseline. The improvement shows the benchmark can drive optimization, but the conclusion oversells the practical result. The paper should temper this claim and add error analysis (e.g., are failures in generation or detection?).

4. **Benchmark scale is limited** (Tables 2–4). The audio event corpus contains only 25 event types, each instantiated with 5 seed audios. All 11 sub-relations involve exactly two audio events (except Count, which involves up to 3). The benchmark is a proof-of-concept rather than a comprehensive evaluation suite. The paper's framing as a "benchmark" is reasonable, but the limited coverage should be explicitly discussed as a limitation rather than claiming comprehensiveness.

### Minor

1. **Missing comparison to WavJourney on the benchmark** (Section 2, Section 5). WavJourney is discussed in related work as a compositional TTA approach but is not included as a baseline. Even if its post-mixing design differs, evaluating it on the benchmark would clarify whether the failure to model relations is inherent to single-model diffusion methods or more general. This is not a fatal omission but weakens the empirical scope.

2. **Lack of clarity on audio blending implementation** (Section 3.3, line 114). The paper states that "combining two audio signals simply involves linearly adding them together" as a general claim, but for temporal relations (before, after), concatenation — not addition — is required. The implementation of temporal blending (e.g., gap between clips, overlapping edges) is not specified, which affects both reproducibility and the evaluation of temporal detection.

3. **No relation-specific architectural modification in fine-tuning** (Section 4). The fine-tuning uses the standard diffusion NLL loss without any relation-aware objective (e.g., contrastive loss for temporal order). While this is not required, it limits the methodological contribution of the fine-tuning component to a standard fine-tuning recipe on synthetic data.

4. **Threshold range selection for mAMSR** (Section 3.4, line 167). The detection thresholds are uniformly sampled from [0.5, 0.8] with step 0.1. This range and step size are stated without justification. While following COCO-style averaging is reasonable, the specific range should be motivated.

### Trivial

- Figure 2 (GPT-4 prompts) is placed mid-sentence in the PDF, making it hard to follow the text flow.
- The text at line 241 has a doubled phrase: "improves its improves its."

## Nice-to-Haves

- A human listening study on ~100 samples per sub-relation, measuring inter-annotator agreement and correlation with MSR-RiTTA scores.
- Comparison to WavJourney as an additional baseline on the benchmark.
- Per-class detection accuracy of PANNS on the synthetic test set, broken down by event category.
- Inclusion of overlapping audio events (beyond the clean non-overlapping constraint) for a more realistic Spatial Distance evaluation.
- A relation-aware loss (e.g., temporal order contrastive loss) in the fine-tuning pipeline.

## Removed Points

These points were assessed and removed with justification:

- *"Missing related works"* → Removed per instruction; I cannot verify existence of unmentioned works.
- *"Only 5 GPT-4 prompts per relation is minimal diversity"* → Removed. 5 diverse linguistic expressions per relation is a reasonable starting point for an initial benchmark; the generation strategy can trivially scale.
- *"Parsimony penalty can dominate the score"* → Removed. With ws=0.1, the penalty is mild (score ~0.9 for one extra event, ~0.82 for two). The reviewer's concern is not supported by the paper's design.
- *"Presence is scored even if events occur at wrong times"* → Removed. This is by design: Stage 1 checks presence regardless of timing, and Stage 2 evaluates temporal correctness. This is a deliberate multi-stage decomposition, not a flaw.
- *"Threshold selection 0.5–0.8 with step 0.1 is arbitrary"* → Removed. Following COCO mAP-style threshold averaging is standard practice; the exact range selection is a minor design choice.
- *"Why Tango 2 fine-tuning failed is not explained"* → Removed. The paper notes this in one sentence; analysis would be nice but is not a required explanation.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the authors themselves do not already discuss, though the severity of the metric validation gap is more sharply articulated by the critics than by the paper.

## Suggestions

1. **Validate the evaluation metric**. Add per-class PANNS detection accuracy on the test set and a small human listening study (50–100 examples per relation) to measure correlation between MSR-RiTTA scores and human judgment. Without this, the quantitative results remain uninterpretable.

2. **Tone down scope claims**. Replace "covering all potential relations in real-world scenarios" with "covering a range of basic relations as a first step." Honest scoping makes the paper's actual contributions (taxonomy, benchmark infrastructure) stand stronger.

3. **Add error analysis for fine-tuning**. Break down whether low mARel scores reflect (a) failure to generate the correct events, (b) failure to order/blend them correctly, or (c) detector failure. A confusion matrix would clarify the bottleneck.

4. **Include WavJourney as a baseline**. Even if its design is different, evaluating it on the benchmark would provide an informative comparison and strengthen the empirical scope.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>