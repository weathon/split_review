## Summary

SpookyBench is a synthetic benchmark that encodes content (text, object images, dynamic depth scenes) exclusively through temporal motion patterns in binary noise frames, where individual frames contain no spatial information. The paper reports that while humans achieve ~98% accuracy, all 28 tested video-language models — spanning open-source (Qwen, InternVL, VideoLLaMA) and closed-source (GPT-4o, Gemini) systems from 2B to 78B parameters — obtain exactly 0% accuracy under both direct and chain-of-thought prompting. The finding is striking and, if robust, points to a genuine blind spot in current architectures.

---

## Strengths

1. **Benchmark design cleanly isolates temporal processing.** The opposing-motion encoding (Algorithms 1–2, Section 3) ensures that individual frames are uninformative noise; content is only recoverable through motion across frames. This is a genuinely novel evaluation paradigm — no existing benchmark completely eliminates spatial cues in this manner.

2. **Universal 0% across 28 diverse models is a compelling negative result.** Table 1 reports every tested model at exactly 0% accuracy with zero variance, including video-specialized architectures (TimeChat, InternVideo2.5) and massive models (InternVL2.5-78B, Qwen2.5-VL-72B). Both direct and CoT prompting fail. This breadth of coverage strongly suggests the limitation is not model-specific.

3. **Frame-rate control experiments rule out sampling confounds.** Section 4.3 (Tables 4–5) shows human accuracy degrades gracefully from ~96% at 20–30 FPS to 0% at 1 FPS, while all VLMs remain at 0% across every frame rate. This precludes the explanation that models simply need more temporal resolution.

4. **SNR metrics and binary threshold analysis provide quantitative characterization.** Section 3.3 defines four meaningful SNR measures (Basic, Perceptual, Temporal Coherence, Motion Contrast) and Figure 4 reveals a sharp threshold effect for text detection at ~2.5 dB SNR. These metrics help ground future analysis of why the failure occurs.

5. **Fine-tuning attempt addresses domain-missmatch concerns.** Section 4.4 reports fine-tuning two models on 400 SpookyBench videos for 10 epochs, with both still at 0% on the test set. While under-reported (see Weaknesses), the existence of this experiment strengthens the case that the failure is not merely distributional.

---

## Weaknesses

### Major

- **Fine-tuning experiment is insufficiently documented to support the "architectural inability" claim.** The paper claims the 0% test accuracy after fine-tuning "indicates a fundamental architectural inability," but does not report training accuracy, loss curves, or any metric showing the models were actually learning during training. Without these, it is impossible to distinguish between (a) the architecture genuinely cannot learn the task and (b) the training was simply ineffective (e.g., learning rate issues, the visual encoder unable to process binary noise patterns, or gradient problems). Training accuracy is a single critical number that would resolve this ambiguity. The paper also does not specify the test-set size (51 videos remain after reserving 400 for training) nor whether the test videos contain content categories unseen during training — both relevant to interpreting the result. This weakness is evidential rather than structural: the zero-shot results are robust and independently valuable, but the architectural claim exceeds the evidence provided.

### Minor

- **Framing overgeneralizes from motion-based figure-ground segregation to "temporal understanding."** The paper motivates SpookyBench with firefly communication and Morse code — discrete event-sequence temporal reasoning — but the benchmark tests continuous opposing motion of noise patterns, which is a motion perception / figure-ground segregation task. The content itself (words, object shapes) is static; motion makes it visible. This is a real and interesting form of temporal processing (motion-based content extraction), but it is not equivalent to understanding event sequences, causality, or temporal order. The title and abstract's "time blindness" framing implies a broader failure than the benchmark directly tests. A more precise characterization would strengthen the paper.

- **Small human sample limits the robustness of the human baseline.** Only 6 participants were evaluated (Section 4.2). While standard deviations are low and results are consistent, a larger and more diverse sample would increase confidence in the 98% accuracy figure, especially given that the gap between human and machine performance is central to the paper's contribution.

- **No systematic qualitative analysis of model outputs.** The paper states that models "attempted to extract information from individual frames" and fine-tuned models "mimicked training examples," but provides no examples or taxonomy of failure modes. A table of actual model responses would help readers understand *how* models fail (e.g., do they describe noise, hallucinate unrelated objects, or output silence?) and would concretely demonstrate "time-blindness" beyond the 0% accuracy figure.

- **Small evaluation set (451 videos).** While the paper notes more data can be generated, the current evaluation set is modest for a benchmark meant to challenge models. The fine-tuning split (400 train / 51 test) is particularly small for the test set, making the test accuracy less statistically reliable.

### Trivial

- The text in Section 5 has a duplicated paragraph (lines 321–331 repeat nearly verbatim).
- Figure 4 caption incorrectly repeats "SNR < 2.5 dB" for both the pink and yellow regions.

---

## Nice-to-Haves

- Report training accuracy and learning curves for the fine-tuning experiment (this is the single most impactful improvement).
- Test whether models can learn a simpler binary discrimination task (e.g., "does this video contain any content or is it pure noise?") before full content identification.
- Probe intermediate features to identify where the failure occurs (visual encoder, temporal pooling, or language head).
- Compare against a baseline where content is displayed as a flashing solid shape on a static noise background, to bound whether the failure is specific to motion-based encoding or more general.

---

## Removed Points

These points were flagged for removal; treat them with caution:

- **"Table 5 is redundant with Table 1."** — Table 5 reports VLM accuracy averaged across frame rates (all 0%), while Table 1 reports accuracy per model at full FPS. They serve different purposes; the overlap is intentional and not bloated.
- **"The SNR threshold analysis is not integrated into the main argument."** — The threshold analysis is presented as an observation about the stimuli's properties, not a core claim. The paper does not claim it explains model behavior; it is correctly scoped as a descriptive finding.
- **"No separate Limitations section."** — The paper includes an Ethics Statement that addresses limitations. The lack of a separately titled section is a formatting preference, not a substantive gap.
- **"No alternative training setups explored."** — This demands more experimental scope than is standard for a benchmark-introduction paper. A single fine-tuning attempt per model is acceptable as a preliminary investigation; the issue is lack of documentation, not lack of variants.
- **"Could use a larger training set for fine-tuning."** — The generator can produce unlimited data, but the current experiment is already informative. This is a nice-to-have, not a weakness.
- **"Criticism about random guessing baselines."** — The paper uses exact-match evaluation with accepted synonyms. Random guessing from the full vocabulary would indeed yield near 0%, but this is addressed by the flexible evaluation protocol (Section 4.1, Setup).
- **Strength Finder's generic strengths removed:** "addressed an important problem" (generic), "the problem is important" (generic), "well-written" (formatting-level praise without specific evidence). These lack concrete content anchors.

---

## Novel Insights

None beyond the paper's own contributions. The key insight — that VLMs universally fail to extract static content from motion-defined noise patterns while humans find the task trivially easy — is well articulated by the paper itself. The reviews do not surface a novel reinterpretation of this finding beyond what the authors state.

---

## Suggestions

1. **Report training accuracy for the fine-tuned models.** If training accuracy is near 100%, this would shift the interpretation from "architectural inability" to "poor generalization from small training set." If it is also 0%, this would strongly support the architectural claim. Either outcome is informative.

2. **Add a qualitative analysis of model outputs.** Show 5–10 representative model responses (e.g., "I see random noise," "a blurry image," actual correct guesses) in a table. This would make the failure mode concrete.

3. **Narrow the framing.** Replace "time blindness" with a more precise term like "motion-blindness" or "inability to extract static content from motion cues." Distinguish the benchmark's focus (motion-based figure-ground segregation) from event-sequence temporal reasoning.

4. **State the test-set size explicitly** (51 videos, derived from 451 total − 400 training) and clarify whether test-set categories overlap with training categories.

---

## Score and Decision

### Calibration

**Round 1 — Bracketing.** Searched for temporal video understanding benchmarks in three bands. Weak anchors (score < 3.5): Vinoground (3.00, withdrawn), Temporally-Grounded Lang Gen (3.33, withdrawn), NOAH (3.00, withdrawn). Middle anchors (3.5–7.5): TemporalBench (4.00, withdrawn), ConservationBench (4.00, rejected), VideoReasonBench (5.50, accepted), VCR-Bench (5.00, rejected). Strong anchors (>7.5): Embodied Nav Foundation Model (8.00), Generative Universal Verifier (8.00), Gaia2 (8.00). Initial bracket: **4.0–6.5**.

**Round 2 — Narrowing.** Searched within score bands (4.0–6.0 and 5.0–7.0) for more topically similar papers. ST-VLM (4.50, rejected), VidHal (4.50, rejected), VideoCogQA (4.50, rejected), VideoReasonBench (5.50, accepted), MMR-V (5.50, accepted), IV-Bench (6.00, accepted), AccidentBench (5.60, rejected).

**Anchor comparison:**
- *Vinoground* (3.00) — Natural video counterfactual benchmark; models get ~50% vs humans ~90%. SpookyBench's 0% finding is more striking and the synthetic design is more novel. **SpookyBench is clearly stronger.**
- *ConservationBench* (4.00) — Tests physical transformation reasoning across 34 models. Similar structure but less surprising result. **SpookyBench has a more novel design and more striking finding.**
- *VideoReasonBench* (5.50, accepted) — Complex video reasoning benchmark, 18 models. Larger dataset and more rigorous evaluation. **Comparable quality: SpookyBench has more novel design and more striking finding but smaller dataset and weaker fine-tuning documentation.**
- *MMR-V* (5.50, accepted) — Deep multimodal reasoning benchmark, 317 videos, 21 models. Strong human annotation, but conventional video content. **Comparable quality: SpookyBench has more novel design but less evaluation depth.**
- *IV-Bench* (6.00, accepted) — Image-grounded video reasoning, 966 videos, 28 models. Larger scale and more tasks. **Slightly weaker: SpookyBench has a more novel design but a smaller dataset and less thorough evaluation.**

**Final bracket narrows to 5.0–6.0.** The paper's novel design and striking finding place it above benchmarks scoring ~4.0, while the under-reported fine-tuning experiment and small dataset prevent it from reaching the 6.0 tier. Within this bracket, the paper is closest to VideoReasonBench and MMR-V (both 5.5, accepted).

### Final Score

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>