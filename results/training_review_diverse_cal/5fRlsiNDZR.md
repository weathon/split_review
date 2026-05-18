Now I have all the information needed to produce the final consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper introduces FARV, a unit-based vocoder for Video-to-Speech (V2S) synthesis that fuses facial image embeddings (from FaRL) with HuBERT acoustic units to improve speaker identity preservation. The method leverages a shared unit vocabulary between the frontend encoder and vocoder to mitigate domain gaps, and demonstrates competitive intelligibility against existing V2S methods. The paper's core novelty lies in integrating visual speaker information into the vocoder stage of a two-stage V2S pipeline.

## Strengths

1. **Novel and practical integration of facial embeddings into a unit-based vocoder for V2S.** FARV is, to the paper's account, the first vocoder for V2S that fuses pretrained FaRL facial embeddings with acoustic units to preserve speaker characteristics that standard unit-HiFiGAN neglects. This design choice directly targets a known limitation of unit-based vocoders — that HuBERT units encode content but discard speaker identity. The 100% gender classification accuracy achieved by FARV's embedding (Table 6) provides direct evidence that the facial information injects useful speaker cues into the representation.

2. **Strong intelligibility results against diverse baselines.** In Table 1, FARV ranks among the top-2 across all metrics (ESTOI, MCD, LSE-C, LSE-D, WER) on both LRS3-TED and LRS2-BBC when compared against a range of V2S methods, including those using additional speaker embeddings or textual supervision. This demonstrates that the method achieves competitive content recovery using only visual input during training and inference.

3. **Well-demonstrated advantage of unit-based vocoders for frontend adaptation.** The paper provides a clean empirical demonstration (Table 4, Figure 3) that mel-based HiFiGAN suffers severe degradation when applied to V2S frontend predictions in a zero-shot manner, while unit-based vocoders (including FARV) maintain much more stable performance. This is a genuine practical insight — the shared unit vocabulary eliminates the frequency-domain mismatch that plagues mel-based approaches. Table 5 further shows that HiFiGAN requires explicit fine-tuning on frontend outputs to recover, while FARV does not.

4. **Dataset adaptation analysis with relative drop rates.** The paper provides a clear analysis (Table 3, Figure 2) comparing zero-shot vs. fine-tuned performance across datasets, showing that FARV has lower drop rates than unit-HiFiGAN and mel-based alternatives. This goes beyond a single comparison and demonstrates robustness.

## Weaknesses

### Fatal
None.

### Major

1. **Unfair comparison in the main V2S evaluation (Tables 1 and 2) conflates in-domain training with facial embeddings.** FARV is trained (fine-tuned from LJSpeech) on the evaluation datasets LRS3-TED and LRS2-BBC, while the unit-HiFiGAN/ReVISE baseline used in the main comparison is explicitly not fine-tuned on those datasets (the paper states at line 158: "we utilize only the Unit-HiFiGAN model trained on LJSpeech without finetuning it on LRS2-BBC and LRS3-TED for this analysis"). The paper justifies this by arguing fine-tuning hurts unit-HiFiGAN quality, but this justification conflates two variables: (a) the addition of facial embeddings, and (b) access to in-domain, multi-speaker training data. The proper baseline to isolate the contribution of facial embeddings is unit-HiFiGAN fine-tuned on the *same* LRS3/LRS2 data without facial embeddings. The paper does provide some evidence in a different setting — Table 3 shows FARV outperforming fine-tuned unit-HiFiGAN on LRS2 and VoxCeleb2 with ground-truth inputs — but this is not in the V2S frontend evaluation setting, and does not cover LRS3, which is the primary evaluation dataset for Tables 1 and 2. This is a structural issue with the paper's central evidence for speaker preservation.

2. **Missing ablation to isolate the facial embedding contribution within the same architecture.** The paper never trains a version of FARV without the facial embedding (e.g., zeroing out e_I or removing the FaRL encoder) on the same training data. The closest comparison is against unit-HiFiGAN trained on LJSpeech, which differs in both architecture and training data. A controlled ablation — FARV without FaRL trained on LRS3/LRS2 — would directly measure what the facial input adds. Without it, the improvement in speaker preservation metrics (Table 2, Table 3) is attributable to a combination of in-domain multi-speaker training data and the facial embedding, rather than to the facial embedding alone. The embedding capability experiment (Table 6) partially addresses this by showing facial information helps classification, but this is a proxy task, not the actual synthesis task.

### Minor

3. **The embedding capability experiment (Table 6) uses an ambiguous "unit embedding."** The paper states that the linear classifier takes "the output of unit embedding as input." For FARV, the architecture produces both e_U (acoustic unit embedding before fusion) and p_AV = e_I ⊕ e_U (fused multimodal representation). The paper does not specify which is used. If it is p_AV (the fused representation), then comparing FARV's "unit embedding" against unit-HiFiGAN's unit embedding compares a multimodal representation against a unimodal one — making the 100% gender accuracy unsurprising and not isolating whether the *fusion mechanism itself* contributes to synthesis quality. This does not invalidate the paper's claims but weakens the specificity of the evidence.

4. **"Zero-shot" claim for frontend adaptation (Contribution 3) is somewhat softened by dataset exposure.** The paper claims FARV can be adapted to a frontend encoder "even in a zero-shot manner" — meaning without fine-tuning on frontend predictions. However, FARV has been trained on the target dataset (LRS3-TED) with ground-truth acoustic units from the same video corpus, so it has observed the dataset's speakers and acoustic distributions. This is not "zero-shot" in the strongest sense (unseen dataset/speakers). The claim is specifically about zero-shot adaptation to the frontend encoder's *output distribution*, which is legitimate, but the phrasing "zero-shot" without this caveat could mislead readers. The paper would benefit from clarifying this distinction.

5. **Missing reproducibility details for FaRL and image preprocessing.** The paper does not specify which FaRL model variant is used (e.g., ViT-B vs. ViT-L), how the "visual frame cropped from the input video" is selected (random frame, first frame, centered frame?), or the cropping methodology. These details are necessary for reproducing the results. This is a standard reproducibility concern that should be addressed.

### Trivial
None.

## Nice-to-Haves

- Statistical significance / confidence intervals across multiple runs for all metrics would strengthen confidence in the reported scores.
- An ablation where the FaRL embedding is zeroed out or replaced with a constant at inference time (within the same trained FARV model) would provide a simple additional check that the facial embedding is actively used.
- Comparison against a speaker-embedding-conditioned unit-HiFiGAN (e.g., using a pretrained audio speaker embedding like d-vector instead of FaRL) would further help disentangle the benefit of visual speaker information specifically.

## Removed Points

The following weaknesses from the Harsh Critic were removed or downgraded:

- *Criticism about "low-level metrics (ESTOI, MCD) relevance to perceptual speaker identity being unclear"* — The paper uses ESTOI/MCD for intelligibility, not speaker identity. SECS/EER is used for speaker preservation, which the critic acknowledges is appropriate. This is a generic observation, not a weakness. **Removed.**

- *Criticism framing the zero-shot frontend adaptation issue as a stronger fault than it is* — The critic's phrasing suggests the term "zero-shot" is used "inconsistently." In context (Section 4.3.2), the paper is clear that the comparison is about adapting to frontend encoder outputs, not to new datasets. The term is used consistently within that framing. **Downgraded** from the critic's implied severity to a Minor weakness (point 4 above).

- *Criticism about missing statistical significance / confidence intervals* — Largely standard across speech synthesis papers where single-run evaluation is common. This is a nice-to-have, not a weakness. **Moved to Nice-to-Haves.**

- *The Strengths Finder's claim about "state-of-the-art intelligibility"* — Retained but reframed as "strong" rather than "state-of-the-art" since the comparison in Table 1 includes methods with different supervision levels.

## Novel Insights

The Harsh Critic's most insightful contribution is identifying the structural confound in the main V2S evaluation — the fact that FARV receives in-domain multi-speaker training data in addition to facial embeddings, while the baseline does not. This is not a superficial oversight; it cuts to the interpretability of the paper's central claim about speaker preservation. The critic correctly notes that the paper's evidence would be much stronger with a controlled baseline (unit-HiFiGAN fine-tuned on LRS3/LRS2 without facial embeddings). However, the critic underweights the supporting evidence from Table 3 (where both models are fine-tuned on the same data) and Figure 2 (drop rates), which partially mitigate the concern. The net insight is that the paper's experiments are directionally supportive but not crisply controlled, and the missing ablation is the single largest gap.

## Suggestions

1. **Add a controlled baseline to Tables 1 and 2:** Fine-tune unit-HiFiGAN on exactly the same LRS3-TED (and LRS2-BBC) training data and recipe as FARV, but without facial embeddings. Compare FARV against this baseline in the V2S evaluation setting. This would isolate the contribution of facial information from the confound of in-domain training data.

2. **Add an ablation within FARV:** Either train a version of FARV without the FaRL encoder on the same data, or at inference time ablate the facial embedding (zero out e_I) within the already-trained FARV. Report the change in SECS, EER, and NISQA-MOS.

3. **Clarify the embedding capability experiment:** Specify whether the linear classifier in Table 6 uses e_U (unit embedding before fusion) or p_AV (fused multimodal representation). If it uses p_AV, add a comparison using e_U alone from FARV to enable an apples-to-apples comparison with unit-HiFiGAN.

4. **Clarify the "zero-shot" terminology** when discussing frontend adaptation (Section 4.3.2). State explicitly that the model has been trained on the target dataset's ground-truth data but not on frontend predictions, to avoid ambiguity.

5. **Add reproducibility details:** Specify the FaRL model variant (e.g., ViT-B/16), how the facial frame is selected from each video (e.g., first frame, center frame, random), and the cropping procedure.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>