Now I have verified the paper's content thoroughly. Let me compose the final consolidated review.

---

## Summary

This paper proposes the first sentence-level multilingual visual speech recognition (VSR) system using a single model. To manage the computational cost of large-scale visual data, the authors introduce **visual speech units** — discretized tokens obtained by quantizing visual features from a multilingual self-supervised model (mAV-HuBERT, trained on 5,512 hours of audio-visual data across 9 languages). Pre-training is framed as unit-to-text translation with a curriculum that progressively masks out audio inputs, transitioning from audio-visual to purely visual inputs. Fine-tuned on continuous features, the single model achieves comparable word error rates across English, Spanish, Italian, French, and Portuguese alongside a ~12× speedup in pre-training time.

---

## Strengths

- **First single-model sentence-level multilingual VSR.** The paper is the first to demonstrate that a single model can recognize five languages from silent video, with results that are competitive against language-specific monolingual systems (Table 7). This is a genuine step forward for the field.
- **Dramatic efficiency gains from visual speech units.** The compression of raw video (61,952 bits/frame) to 10-bit discrete tokens (0.016% of original size) yields a ~12× speedup in pre-training (6.6 hours vs. 52.5 hours, Table 3), while also enabling larger batch sizes. This practical speed–accuracy trade-off is well-demonstrated.
- **Curriculum learning is convincingly shown to be critical.** Ablation (−Curriculum, Table 5) causes catastrophic degradation (e.g., English WER from 24.4% to 35.6%, Portuguese from 27.2% to 42.3%), establishing that progressive masking from audio-visual to visual inputs is essential for stable VSU-based pre-training.
- **mAV-HuBERT clearly benefits multilingual modeling.** Table 2 shows that the multilingual backbone dramatically outperforms English-only AV-HuBERT on non-English languages (>10% absolute WER reduction), justifying the investment in a multilingual self-supervised model.
- **Analysis of visual speech units provides useful insights.** The speaker verification experiment (Table 4) shows that discretization suppresses speaker information (EER rises from 19.42% for continuous visual features to 32.74% for VSUs), and the phoneme-viseme mapping (Figure 2) offers qualitative evidence that units capture linguistic content.

---

## Weaknesses

### Fatal
None.

### Major

- **The comparison against monolingual SOTA (Table 7) is not a controlled test of the proposed method's contribution.** The proposed multilingual model is trained on 4,545 hours of data (including additional English sources LRS3, VoxCeleb2, AVSpeech with automatic labels) and uses a stronger backbone (mAV-HuBERT vs. smaller models in prior work). Better non-English results could simply reflect more training data or a more powerful encoder, rather than the VSU pre-training strategy. A controlled comparison — training a counterpart method on the same data with the same backbone — is needed to attribute gains to the VSU pipeline. The paper's "state-of-the-art" claim (abstract, contribution 5) is overstated given this confound.

- **The key ablation (Table 5, −Unit Pretraining) shows only modest improvements that may not be statistically meaningful.** The full model improves over direct fine-tuning of mAV-HuBERT by approximately 1–2 WER points on non-English languages, while English WER *degrades* (e.g., 24.4 vs. 24.0). No statistical significance or variance estimates (multiple seeds) are reported. With margins this small, it is unclear whether VSU pre-training provides a genuine benefit or whether results are within noise. The core claim that "VSU pre-training enables effective multilingual VSR" rests on fragile evidence here.

### Minor

- **The comparison baseline in Table 6 (English-only AV-HuBERT) is weak for demonstrating the VSU pipeline's value.** The fact that a multilingual model (mAV-HuBERT + VSU) outperforms an English-only model on non-English languages is expected and mostly reflects the multilingual backbone, not the VSU pre-training. The more informative comparison (mAV-HuBERT fine-tuned directly) is deferred to Table 5, where gains are modest. This framing somewhat overstates what Table 6 demonstrates.
- **The curriculum schedule (linear masking from 10%–70% of training) is not ablated or justified.** Given that the curriculum is central to the method and its removal causes catastrophic failure, exploring other schedules (exponential, constant) would strengthen the paper's understanding of why this particular schedule works.
- **The language embedding is added during pre-training but never ablated.** It is unclear how much of the multilingual capability comes from the language embedding vs. the model's implicit multilingual modeling. The paper does not test whether the model actually uses the embedding to switch languages or simply memorizes language-specific patterns.
- **No held-out language evaluation.** Testing on a language unseen during VSR training (e.g., German from mTEDx) would provide stronger evidence of genuine multilingual generalization rather than memorization of five language-specific mappings.

### Trivial

- **The "six times larger bits" framing** (Introduction) compares raw pixel bits to raw audio bits, which is accurate for input data size but not how VSR systems internally process features (which use compact front-end representations). This is a minor motivational framing issue, not a technical error.

---

## Nice-to-Haves

- Evaluate with a held-out language not seen during VSR training (e.g., German from mTEDx) to test cross-lingual generalization.
- Ablate the visual speech unit token size (e.g., 500, 2000) to understand sensitivity.
- Ablate the language embedding to measure its contribution.
- Report results over multiple seeds with variance estimates for main tables.
- Provide qualitative VSR output examples per language showing common error patterns (homophene confusions).
- Test on LRS2 (English) to verify English performance is not dataset-specific.
- Visualize the progressive masking schedule and how validation loss evolves during pre-training.

---

## Removed Points

*These points were flagged as invalid during verification and should be treated with caution:*

- **"The −Unit Pretraining still uses mAV-HuBERT as a frozen feature extractor"** — The paper clearly states this is direct fine-tuning of mAV-HuBERT, not a frozen extractor. Removed as factually wrong.
- **"it is unclear whether the model uses language identity during pre-training or only during fine-tuning"** — Section 3.2 and the architecture description (Section 4.2) clearly describe the language embedding being added during pre-training. Removed as the paper addresses this.
- **"−Curriculum dramatic drop weakens the claim that VSUs alone are sufficient for linguistic modeling"** — The paper never claims VSUs alone suffice without curriculum; the curriculum is a core part of the proposed method. Removed as a strawman.
- **"The paper would benefit from comparing against a multilingual baseline trained from scratch with continuous features"** — The −Unit Pretraining ablation (Table 5) is exactly this comparison. Removed as already addressed.
- Criticisms about missing appendix content — The parser strips supplementary sections; the original submission contains them. Removed per hard rules.
- Criticisms about Whisper accuracy not being analyzed or 350k steps with one iteration — These are observations rather than substantive errors; the model demonstrably works.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the authors themselves do not already acknowledge or address (e.g., the curse of multilinguality, the modest gains on English, the need for curriculum learning).

---

## Suggestions

1. **Tone down the "state-of-the-art" claim** in the abstract and conclusions. The paper's genuine contribution is demonstrating *the first single-model multilingual VSR* with competitive results and massive efficiency gains — that is already strong without claiming SOTA on every language.
2. **Add variance estimates** (multiple seeds) for the key ablation (Table 5) to establish whether the 1–2 WER improvements are statistically significant.
3. **Include a controlled baseline** where the same mAV-HuBERT backbone is used to train a monolingual system for each language on matched data, so the "curse of multilinguality" explanation can be quantitatively demonstrated rather than invoked post-hoc.
4. **Ablate the language embedding** to measure its contribution to multilingual performance.
5. **Replace or supplement Table 6's baseline** (English-only AV-HuBERT) with the mAV-HuBERT direct-finetuning baseline already present in Table 5, to avoid confounding backbone quality with VSU effectiveness.

---

## Score and Decision

**Originality:** Moderate. First to do sentence-level multilingual VSR with a single model, but the individual components (AV-HuBERT, speech units, curriculum learning) are adapted from prior work.

**Importance:** Moderate to high. Multilingual VSR is a real, underexplored problem, and the efficiency gains are practically valuable.

**Claims supported:** Partially. The efficiency gains and curriculum necessity are well-supported. The benefit of VSU pre-training over simpler alternatives is weakly supported (modest gains, no significance testing, English degradation). The SOTA claim is overstated.

**Soundness:** Adequate but with notable gaps — uncontrolled comparison in Table 7, missing variance estimates, no language embedding ablation, no held-out language test.

**Clarity:** Generally well-written and structured. The method is clearly described.

**Value to community:** Moderate. The efficiency gains and the demonstration that a single multilingual VSR model is feasible are useful contributions. The paper opens a direction rather than closing it.

**Overall assessment:** The paper has genuine contributions — particularly the efficiency gains and the first demonstration of single-model multilingual VSR — but the central claim that VSU pre-training is beneficial is only weakly supported by the controlled ablation, and the SOTA claim is inflated by an uncontrolled comparison. The method is novel enough and practical enough to merit publication, but the claims should be tempered.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>