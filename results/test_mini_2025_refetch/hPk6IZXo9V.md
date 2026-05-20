Now I have sufficient anchors to calibrate. Let me synthesize the final review.

My round-1 bracket placed the paper between 2.0 and 4.5. After reading the anchors, the most comparable paper is "Language Reconstruction with Brain Predictive Coding from fMRI Data" (avg 4.75, Reject) — that paper shared similar weaknesses (incoherent output, weak metrics) but had proper evaluation without the subject-pooling flaw. BELT-2 (avg 5.0, Reject) had mixed reviews but demonstrated much higher BLEU scores. "Aligning brain functions boosts decoding" (avg 4.25) also had small N but better-controlled evaluation. Neuro2Semantic is clearly weaker than all three.

Let me now produce the final consolidated review.

**Score: 3.5. Decision: Reject.**

Here are the anchors I've examined:

| Path | Avg Score | Round | Comparison to Neuro2Semantic |
|------|-----------|-------|------|
| hPk6IZXo9V.txt | **(this paper)** | — | — |
| b57IG6N20B.md (BrainCodec) | 6.60 | R1 | Much stronger: clean evaluation, multiple datasets, proper baselines |
| QzTpTRVtrP.md (LaBraM) | 7.33 | R1 | Much stronger: large-scale pretraining, rigorous evaluation |
| gp5dPMBzMH.md (BELT-2) | 5.00 | R1 | Stronger: higher BLEU scores, more tasks, still had methodological clarity issues |
| wJ6Bx1IYrQ.md (EEGPT) | 4.00 | R1 | Comparable but different scale; also rejected/withdrawn |
| 2hKDQ20zDa.md (PredFT) | 4.75 | R2 | Stronger: similar output quality issues but proper fMRI evaluation without pooling flaw |
| 3sfOGsBh85.md (CerebroVoice) | 4.75 | R2 | Stronger: proper dataset+benchmark contribution |
| GYAvwLviup.md (Align brain func) | 4.25 | R2 | Stronger: addressed cross-subject alignment directly, better-controlled evaluation |
| IAFStwZPNu.md (Brain's Bitter) | 5.67 | R2 | Much stronger: rigorous self-supervised learning, proper scaling analysis |

---

## Summary

Neuro2Semantic proposes a two-phase transfer learning framework for semantic text decoding from intracranial EEG (iEEG). Phase 1 trains an LSTM adapter to align iEEG signals with pre-trained text embeddings (text-embedding-ada-002) using contrastive + triplet loss. Phase 2 fine-tunes a pre-trained Vec2Text corrector to generate text from the aligned embeddings. The method is evaluated on pooled iEEG data from 3 subjects (~30 min total speech, 864 electrodes combined) across 6 naturalistic stories, using leave-one-trial-out cross-validation.

## Strengths

- **Two-phase ablation is informative**: Table 1 shows that the full model (BERT 0.1947) substantially outperforms either Phase 1 alone (0.0560) or Phase 2 alone (0.1001), providing direct evidence that both the LSTM alignment and the Vec2Text fine-tuning are necessary for the reported performance.
- **Zero-shot generalization evaluated**: Section 3.3 and Figure 3 test held-out stories (out-of-domain) and show Neuro2Semantic outperforms the baseline across BERT, BLEU, ROUGE, and 1-WER, suggesting the framework captures some generalizable semantic features rather than memorizing story-specific patterns.
- **Scaling analysis with data and electrodes**: Figure 4 demonstrates near-linear improvements with more training data and reasonable robustness to reduced electrode subsets (80% of electrodes sometimes matching 100%). This provides useful empirical findings about resource requirements.
- **Electrode selection via LLM encoding strength**: The method for selecting semantically responsive electrodes (Mistral-7B encoding strength, p<0.05) is a thoughtful preprocessing step grounded in neural encoding models.

## Weaknesses

### Major

- **Subject pooling invalidates data-efficiency claims**: The paper combines all electrodes from three subjects into a single 864-electrode dataset (Section 2.2, line 210-211): "we combined the electrodes from all three subjects into a single subject for all analyses, totalling 864 electrodes." The leave-one-trial-out cross-validation is over *trials*, not subjects, so the model trains on data from all subjects and is tested on trials that also include electrodes from all subjects. The claim that the method works "with as little as 30 minutes of neural data" conflates ~30 min total across 3 subjects (~10 min/subject). No per-subject or cross-subject evaluation is reported. Without this, the central claim about data efficiency for individual BCI applications is unsupported — we cannot tell whether the model exploits cross-subject patterns or would work with one subject's data alone. The paper acknowledges "cross-subject variability" as a limitation (Section 4.2) but does not identify this pooling issue as a structural constraint on what can be concluded.

- **Absolute performance is very low and overclaimed**: The full model achieves Word Error Rate of 0.966 (Table 1) — only 3.4% of words are correct. BLEU is 0.0789, ROUGE is 0.1387. These numbers indicate that reconstructed text is almost never verbatim. The BERT score (0.1947) is positive relative to the random baseline (-0.2452) but still modest in absolute terms. Given that Vec2Text can generate plausible-sounding sentences from any embedding, there is a real risk that the language model prior rather than neural-specific information drives much of the semantic content. The paper's framing ("remarkable performance", "significant improvements") is not calibrated to these magnitudes. The paper lacks a control with shuffled labels to estimate how much reconstruction is attributable to the corrector's bias alone.

- **Baseline comparison is weak and conflates contributions**: The baseline (Tang et al., 2023) was designed for fMRI, not iEEG, and does not use any pre-trained text embeddings. The reported "6× improvement" is expected — Neuro2Semantic's entire pipeline leverages powerful pre-trained components (text-embedding-ada-002, Vec2Text, Mistral-7B for electrode selection). An ablation comparing Neuro2Semantic to a simpler neural decoder (e.g., LSTM encoder + decoder trained end-to-end on iEEG-to-text, without the two-phase transfer design) would be far more informative. The headline result conflates the contribution of the proposed architecture with the contribution of off-the-shelf pre-trained models.

### Minor

- **Statistical testing is unreliable**: The leave-one-trial-out CV uses the last trial of each story (6 stories → 6 test points). The paired t-test over n=6 is unreliable. The paper should report confidence intervals or use bootstrapping. The error bars on the data scaling experiments are also large (Figure 4B), with some 80% electrode subsets matching 100% — this suggests high sensitivity to which electrodes are selected, not necessarily robustness.

- **Missing per-subject and per-story details**: The paper does not report the number of responsive electrodes per subject or per story, nor the distribution of electrode locations (cortical regions). This context is important for interpreting the scaling and generalization results, especially given the pooling issue.

- **Handpicked example reconstructions**: Figure 2B shows handpicked examples. While they illustrate the model's ability to capture coarse thematic content (e.g., "coat check robot" vs. "car keys to the valet"), the selection bias is unexplained. A random sample should be provided in the appendix.

- **No shuffled-label control**: The "Random" control uses randomly initialized LSTM adapter and corrector (Table 1), which is a sanity check but does not control for the language model prior. A better control would keep the corrector frozen (or pretrained) and shuffle the iEEG-to-embedding mapping to measure how much semantic content is truly driven by neural signals versus the corrector's inductive bias.

### Trivial

None.

## Nice-to-Haves

- Report per-subject performance, even if the model is trained on pooled data, to clarify how each subject contributes and whether the approach would work with a single subject.
- Include an internal baseline that uses the same pre-trained text embeddings but replaces Vec2Text with a simpler decoder (e.g., fine-tuned GPT-2) to isolate the benefit of the Vec2Text iterative refinement.
- Clarify the practical inference speed of the iterative Vec2Text refinement, as BCI applications generally require low latency.
- Add a qualitative comparison of a random subset (not handpicked) of reconstructions in the appendix.

## Removed Points

- **"Comparison to motor decoding is misleading"**: The paper mentions motor decoding (Willett et al., 2023; Metzger et al., 2023) as context about different approaches to speech decoding, not as a claim of comparable performance. The paper states "these approaches primarily focus on decoding motor intentions, which may not capture the full richness of linguistic semantic content" — a fair distinction, not a misleading comparison.
- **"30 minutes of data is ambiguous (total? per subject?)"**: The paper clearly states "In total, the task included about 30 minutes of speech" (line 208) — the ambiguity is about data efficiency per individual given the pooling, not about the numerical claim itself. This is subsumed under the subject pooling weakness.
- **"Rigorous cross-validation and statistical testing"** (from Strength Finder): The evaluation uses only 6 test points with a paired t-test, which is not rigorous. This strength conflicts with verified weaknesses and is removed.
- **"Scaling analysis shows robustness to reduced electrode coverage"** (partial): The large error bars actually indicate sensitivity, not robustness. The finding that 80% sometimes matches 100% could reflect redundancy among highly correlated channels, not general robustness. This strength is partially addressed in the minor weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension between the paper's ambitious framing and its weak evaluation design — the pooled-subject evaluation and lack of per-subject results prevent the paper from substantiating its core data-efficiency claims, while the weak baseline and modest absolute performance further undermine the significance claims. This collection of issues is well-recognized in the broader neural decoding literature and does not constitute a novel insight about this specific paper.

## Suggestions

1. **Add per-subject evaluation**: Re-analyze the data treating each subject separately. Report how much data per subject is needed for comparable performance. If per-subject results are substantially worse, this must be discussed as a limitation.
2. **Add a shuffled iEEG control**: Permute iEEG segments relative to their corresponding sentences and measure whether the corrector still produces semantically similar text. Without this, the contribution of neural signals to the reconstruction is unclear.
3. **Add a simpler neural baseline**: Train a single LSTM encoder-decoder (without the two-phase transfer) directly on iEEG-to-text to isolate the benefit of the pre-trained embedding pipeline from the proposed architectural design.
4. **Calibrate the language**: Replace "remarkable performance" and similar hyperbole with precise, metric-calibrated descriptions. At WER=0.966 and BLEU=0.0789, the appropriate framing is a proof-of-concept demonstration, not a high-performing system.
5. **Report confidence intervals via bootstrapping** instead of relying on paired t-tests with n=6.

## Score and Decision

**Initial bracket (Round 1):** Placed Neuro2Semantic between 2.0 and 4.5 based on broad retrieval of EEG/iEEG semantic decoding papers.

**Narrowing (Round 2):** Compared against "Language Reconstruction with Brain Predictive Coding" (avg 4.75, Reject) — that paper had similar output quality issues but a sounder evaluation without subject-pooling. Also compared against "Aligning brain functions boosts decoding" (avg 4.25, Reject) which had a similar small-N limitation but directly addressed cross-subject alignment. BELT-2 (avg 5.0, Reject) demonstrated much higher decoding performance. Neuro2Semantic is weaker than all of these because of the structural evaluation flaw (subject pooling) combined with very low absolute performance and an uninformative baseline comparison. The most appropriate score is between the weakest rejected papers (~2-3) and the borderline ones (~4-5), landing at 3.5.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>