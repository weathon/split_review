Now I have a thorough understanding of the paper and the reviews. Let me synthesize the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor

- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now write the full review.

---

Here is my analysis of which criticisms to keep/remove:

**Criticisms to REMOVE entirely (moved to Removed Points):**
1. t-SNE "only two statements" criticism — The paper explicitly chooses RAVDESS because "the linguistic content remains constant across utterances with different emotions" (line 210). This is intentional experimental design, not a limitation. The criticism fundamentally misunderstands why this dataset was chosen.
2. "textual attention correlating with intensity/pitch undercuts claim" — The paper explicitly addresses this at line 267: "Note that textual attention exhibits fairly high similarity with acoustic features as polar words are often pronounced with emotional emphasis." This is the paper's own observation, not an oversight.
3. "U-shaped pattern is surprising and not discussed" — The paper discusses this pattern at line 227: "Wav2Vec2 shows a U-shaped pattern, with the best performance in the middle layers and the final layers being unable to decode transcription."
4. "soundness of experiments" questioning due to missing appendix — parser artifact.

**Criticisms to WEAKEN:**
1. "Probe textual latents for more acoustic features" — The paper already probes for mean intensity, mean pitch, gender, and speaker ID (4 acoustic features, line 183). Requesting more (speaking rate, voice quality) is nice-to-have, not a core gap.
2. β per-layer criticism — Standard practice for layerwise analysis. Optimizing β per layer would be unusual and could introduce confounds.

**Criticisms to KEEP:**
1. Structural framing issue (textual ≠ ASR-needs) — Genuine and substantive
2. Incomplete probing (no probing of z^acoustic for textual features beyond CTC) — Valid
3. Missing standard VIB ablation — Valid and methodologically important
4. No mutual information estimate between latents — Valid

Now my final synthesis.## Summary

This paper proposes a two-stage Variational Information Bottleneck (VIB) framework to disentangle neural speech representations into two components: Stage 1 compresses hidden states to predict ASR transcriptions (yielding "textual" latents), while Stage 2 compresses the same hidden states to predict a downstream task (emotion or speaker ID) conditioned on the frozen textual latents (yielding "acoustic" latents). The framework is evaluated on emotion recognition and speaker identification using Wav2Vec2 and HuBERT models, with probing experiments validating disentanglement and layerwise analyses revealing how fine-tuning shifts the textual/acoustic balance across model layers.

## Strengths

- **Novel layerwise analysis revealing how fine-tuning shifts the textual-acoustic tradeoff.** The paper traces how each model layer contributes textually and acoustically to emotion recognition (Section 6, Figure 4, right panel). It shows that fine-tuning Wav2Vec2 for ASR causes a sharp decline in acoustic contribution in the final layers while textual contribution increases — a concrete, previously undemonstrated insight into how supervised speech models reallocate information during adaptation. This is the paper's most clearly supported contribution.

- **Strong probing evidence that the two latent sets are functionally separated on the tested dimensions.** The sanity-checks (Section 5.1, Figure 3) show that textual latents perform at chance on pitch, intensity, gender, and speaker ID classification, while acoustic latents perform at chance on CTC-based transcription (WER=100). These negative results are clean and rule out gross leakage between the two representations.

- **Competitive downstream performance despite aggressive compression.** VIB models (d=128) match or exceed probing baselines on emotion recognition and speaker identification across multiple model sizes (Table 1). For example, HuBERT-Large VIB achieves 66.1% emotion accuracy vs. 57.3% probing, and Wav2Vec2-FT-Large VIB achieves 99.6% speaker ID vs. 98.5% probing. This demonstrates that compression does not harm task performance — a necessary condition for practical utility.

- **Modality-agnostic design with low overhead.** The framework requires only a pair of tasks (ASR + target) and applies to any speech model without architectural modification, distinguishing it from prior work tied to specific model families (e.g., Prosody2Vec's HuBERT-specific quantization module).

## Weaknesses

### Major

- **The claimed "textual vs. acoustic" distinction is not fully supported by the method's design.** Stage 1 is trained with a CTC objective that only preserves information *necessary for accurate character/word decoding* — not all textual content. Stage 2 is conditioned on these ASR-relevant latents with an information penalty, so it encodes *anything* the target task needs that Stage 1 did not capture. This "anything" could include acoustic features (pitch, prosody), but it could equally include *textual semantic features* that are helpful for the downstream task but not required for ASR (e.g., word-level sentiment, pragmatic cues like sarcasm marked by word choice). The paper defines "textual" as "what can be transcribed as text" (line 6), but the method only captures what is *needed* for transcription, which is a proper subset. The paper does not probe the acoustic latents for textual features beyond CTC transcription (e.g., word polarity, sentiment category from content), leaving this alternative explanation untested. This is the most consequential weakness because it means the headline claim of "textual/acoustic disentanglement" may be overstated — the method is better described as separating "ASR-relevant from target-task-relevant information."

- **Missing ablation: single-stage VIB without conditioning on textual latents.** The paper compares the two-stage VIB against a probing classifier trained on full hidden states (no compression). This tests the effect of compression, but not the effect of the *conditional disentanglement structure*. A standard single-stage VIB trained directly on the target task (without access to z^textual) would reveal whether the two-stage conditional design provides any benefit over VIB regularization alone. Without this baseline, the framework's claimed advantage from disentanglement cannot be separated from the general advantages of information bottleneck compression.

- **No direct measure of dependency between the two latent sets.** The paper does not report mutual information, correlation, or any other direct measure of statistical dependence between z^textual and z^acoustic. The probing experiments provide indirect evidence (negative results on certain held-out tasks), but these cannot rule out the presence of shared information that is not captured by the specific probe tasks used. A direct dependency measure would substantially strengthen the disentanglement claim.

- **The acoustic latents are not probed for textual features beyond CTC.** The paper probes z^acoustic for transcription via CTC (finding WER=100, i.e., random), but does not probe for word-level sentiment, semantic category, or any other text-derived feature relevant to emotion recognition. If z^acoustic encodes "fine" as a sentiment-ambiguous word or "sad" as a negative-polarity word — information that is textual in nature but not strictly needed for character-level ASR — this would undermine the claim that z^acoustic is acoustic-only. This is the most directly actionable of the probing gaps.

### Minor

- **The feature attribution analysis (Section 7) is preliminary and lacks quantitative baselines.** The dot-product analysis between attention scores and acoustic/sentiment features is interesting but is not compared against any baseline (e.g., random attention, attribution from a non-disentangled VIB model). The paper acknowledges this ("beyond the scope of this work," line 260), but the section as presented does not provide strong evidence for the claimed attribution capability. The Integrated Gradients comparison mentioned in the text is never quantitatively compared to the attention scores.

- **The probing baselines in Table 1 are classifiers on full hidden states without compression.** While stated as probing, the baseline architecture is identical (including the attention pooling layer and classifier), making this a fair comparison of VIB compression vs. no compression. However, the probing classifiers for the sanity checks (Section 5.1) use linear probes, while the Table 1 baselines use the same architecture as VIB — this creates a slight asymmetry in what "probing" means.

### Trivial

- The β schedule (linearly increased from 0.1 to 1.0) is used for all layerwise analyses without per-layer tuning. While standard practice, the paper could note whether the U-shaped transcription pattern for Wav2Vec2 (Section 6) is robust to different β values.

## Nice-to-Haves

- **Standard VIB ablation** (single-stage, no conditioning) to isolate the value of the conditional structure.
- **Probing z^acoustic for word-level sentiment or semantic categories** to close the most significant evidential gap.
- **Mutual information estimate** between z^textual and z^acoustic.
- **Privacy-relevant demonstration**: show that suppressing z^acoustic degrades speaker ID but preserves emotion recognition, or vice versa.
- **Sensitivity analysis of β** on both task accuracy and probe-based disentanglement metrics.

## Removed Points

- **t-SNE uses only two identical statements (Critic's Issue 2 sub-point).** Removed because the paper explicitly chooses RAVDESS because "the linguistic content remains constant across utterances with different emotions" (line 210). This is deliberate experimental design, not a flaw — the experiment tests whether acoustic latents cluster by emotion when text is fixed, which is exactly the right test.

- **"Textual attention correlating with intensity/pitch undercuts the claim of disentangled attribution."** Removed because the paper itself acknowledges this at line 267: "Note that textual attention exhibits fairly high similarity with acoustic features as polar words are often pronounced with emotional emphasis." This is the paper's own observation, not an oversight.

- **"U-shaped pattern is surprising and not discussed."** Removed because the paper does discuss it at line 227, noting the pattern and its relationship to model fine-tuning.

- **"Probe textual latents for more acoustic features (speaking rate, voice quality)."** Weakened to nice-to-have. The paper already probes for 4 acoustic features (mean intensity, mean pitch, gender, speaker ID); the existing set provides meaningful coverage.

- **"Using the same β for all layers undermines the layerwise comparison."** Weakened to trivial. Using consistent hyperparameters across layers is standard practice for layerwise analysis; per-layer β tuning would introduce confounds.

## Novel Insights

None beyond the paper's own contributions. The layerwise finding (fine-tuning for ASR shifts the later layers from acoustic to textual dominance) is the most novel observation, but it is well-described in the paper itself.

## Suggestions

1. **Reframe the contribution** around "separating ASR-relevant from target-task-relevant information" rather than "textual vs. acoustic." This is more precise and avoids overclaiming. If the authors want to maintain the textual/acoustic framing, they must probe z^acoustic for textual features beyond CTC transcription (e.g., word polarity, semantic categories derived from ground-truth transcripts) and show they cannot be decoded from z^acoustic.

2. **Add a standard VIB ablation**: train a single-stage VIB for the target task without conditioning on z^textual. Compare its accuracy and probe-based disentanglement to the two-stage version.

3. **Report a direct dependency measure** between z^textual and z^acoustic (e.g., estimated mutual information or squared correlation).

4. **Add probing of z^acoustic for word-level sentiment** (e.g., using ground-truth transcripts and a sentiment lexicon). This directly tests whether z^acoustic carries textual semantic information beyond ASR-level character decoding.

5. **Add a baseline to the feature attribution analysis**: compare attention-based attribution scores against a null distribution (random attention) or against attribution from a non-disentangled model.

6. **Consider a privacy-preservation demonstration** that concretely shows the practical value of the disentanglement (e.g., blocking z^acoustic degrades speaker ID while preserving emotion performance).

**Overall:** The paper presents a clean, well-motivated framework and provides interesting layerwise analyses. However, the headline claim of textual/acoustic disentanglement is partially unsupported — the method demonstrably separates ASR-relevant from target-task-relevant information, but whether the latter is truly *acoustic* (rather than textual information not required for ASR) is not adequately tested. The missing probing experiments and ablation are addressable and would substantially strengthen the paper. In its current form, the contribution is solid but the central claim is broader than the evidence justifies.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>