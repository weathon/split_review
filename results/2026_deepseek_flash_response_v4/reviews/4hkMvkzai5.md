Now I have sufficient calibration. Let me produce the final review.

## Summary

DeCodec proposes a neural audio codec that learns to disentangle mixed speech+background audio into orthogonal subspaces dedicated to speech and background sound, while further decomposing speech into semantic and paralinguistic components via HuBERT-guided semantic guidance. The key technical innovations — a Subspace Orthogonal Projection (SOP) module and a Representation Swap Training (RST) procedure — are designed to achieve this hierarchical disentanglement within a single codec framework. The paper demonstrates that this single model can be applied to reconstruction, speech enhancement, one-shot voice conversion, and downstream ASR/TTS without task-specific fine-tuning.

## Strengths

- **Joint SOP+RST mechanism validated by ablation (Table 4).** Neither SOP alone (Ablation-1: SDR-B = −13.15 dB) nor RST alone (Ablation-2: SDR-B = −10.67 dB) achieves decoupling, but their combination (Ablation-3) jumps to SDR-B = 0.49 dB and SDR-S = 7.90 dB. This step-function improvement directly supports the core claim that both components are jointly necessary.

- **Strong speech enhancement results on the DNS Challenge (Table 2).** DeCodec achieves the highest BAK scores (4.13 no-reverb, 3.99 real recordings) among all SE baselines — including dedicated discriminative and diffusion models — despite SE not being its primary training objective. The causal variant (DeCodec-c) also matches or exceeds the non-causal SELM on OVL and SIG scores, which is notable for streaming applications.

- **Semantic guidance yields measurable ASR benefit (Table 4).** Adding SG on top of SOP+RST reduces downstream ASR WER* from 41.9% to 25.8%, confirming that the hierarchical speech decomposition into semantic and paralinguistic components is operational and beneficial.

- **Novel combination of capabilities in a single codec.** To the reviewer's knowledge, DeCodec is the first codec to simultaneously perform reconstruction, speech enhancement, one-shot voice conversion on noisy speech, and provide controllable representations for downstream ASR/TTS. While individual capabilities exist in prior work, the unification is novel.

## Weaknesses

### Major

- **Reconstruction comparison (Table 1) confounded by bitrate and training-data mismatch.** DeCodec operates at 8.0 kbps (4.0+4.0) against baselines at 2.0–6.0 kbps, giving a roughly 1.3–4× bitrate advantage that trivially favors higher SDR. Additionally, baselines use official checkpoints trained on clean/diverse audio, while DeCodec trains on 700h of mixed speech+noise specifically designed for its decoupling objective. The paper presents the SDR advantage as evidence of capability ("ensure the performance of complete signal reconstruction while decoupling representations") without acknowledging these confounds. At minimum, the text should clearly state that the comparison is not controlled for bitrate or training conditions. More importantly, SpeechTokenizer at 4.0 kbps achieves better WER (1.82 vs. 1.92) than DeCodec at 8.0 kbps on clean speech — a meaningful result that the paper downplays as "only slightly worse."

- **The theoretical justification for RST (Section 3.6) does not hold.** The mean-value-theorem argument attempts to prove that Zs is independent of background sound information. The logic is: from Eq (15)–(16), ∂Dec/∂Zn|_ξ (Zn₂−Zn₁) ≈ n₂−n₁, and since the left side depends on Zs₁ through ξ while the right side does not, Zs₁ must be independent of n₁. This is not a valid inference: the MVT guarantees existence of some ξ for each specific pair (Zn₁, Zn₂), but ξ can depend on Zs₁ in arbitrarily complex ways while still satisfying the equation. The conclusion "Zs₁ must be independent of n₁" does not follow. Furthermore, the entire chain uses "≈" (approximate equality from loss minimization that never perfectly holds), so even a correct MVT argument would only show approximate independence under idealized assumptions. The paper overclaims theoretical rigor here; the decoupling claim should rest on empirical evidence rather than flawed mathematics.

- **"Angular matrix" (Section 3.4) is undefined and not a standard concept.** The paper states: "When the covariance matrix YY^T satisfies the angular matrix, indicating that the encoder extracts sufficiently diverse embeddings with different feature channels being mutually independent, we can obtain P_S P_N^T = 0." The term "angular matrix" is never defined, cited, or referenced, making the SOP module's claimed theoretical grounding opaque. Since SOP is one of the paper's two key innovations, this lack of clarity is a substantive gap.

### Minor

- **Table 4 leaves WER* blank for Ablation-1 and Ablation-2.** If these configurations produce severely degraded representations that prevent ASR, the paper should explicitly state this rather than leaving the cell empty.

- **Number of RVQ layers K_s and K_n and codebook sizes are not specified anywhere in the paper,** limiting reproducibility. The paper mentions K_s and K_n in Section 3.5 but never gives their values.

- **Adding SG degrades BGS decoupling substantially.** SDR-B drops from 0.49 (Ablation-3, SOP+RST) to −1.11 (DeCodec-c, SOP+RST+SG) — a relative drop of 326% — yet the paper describes this as "a slight decrease in SDR." This should be discussed more candidly as a trade-off between decoupling quality and semantic-paralinguistic decomposition.

- **No computational cost comparison is provided,** despite the Introduction claiming "computational efficiency via feature selection rather than differential extraction" as a core advantage. DeCodec uses two encoders, two parallel RVQ streams, and a decoder — this likely increases computational cost relative to both standard codecs and dedicated SE models. The efficiency claim is unsupported.

- **No direct empirical validation of representation disentanglement** (e.g., t-SNE/PCA visualization of S vs. N subspaces, probe classifiers predicting BGS type from Zs, or cross-correlation analysis) is provided. The evidence for decoupling is entirely indirect (SDR-B improvements and SE performance).

### Trivial

None.

## Nice-to-Haves

- Matched-bitrate reconstruction comparisons or rate-distortion curves
- Retraining/fine-tuning baselines on the same noisy training data
- Empirical disentanglement validation (probe analysis, representation visualization)
- Background sound extraction as a standalone evaluated task
- Specification of K_s, K_n, codebook sizes

## Removed Points

The following points from the inputs were removed with justification:

- *Harsh Critic's claim that "SOP alone actively harms reconstruction":* The paper already acknowledges this, stating that SOP or RST alone is "insufficient to achieve effective decoupling."
- *Strength Finder's claim of a "formal theoretical argument" for RST:* Retained as a weakness instead, since the theoretical argument is invalid.
- *Strength Finder's claim about "orthogonality constraint grounded in subspace formalism":* Weakened because the "angular matrix" concept is undefined.
- *Various speculative criticisms about missing appendix content:* The parser strips these from all papers; they exist in the original submission.
- *Formatting/style nitpicks:* These are parser artifacts, not author errors.
- *Critique about sample-wise vs. subspace orthogonality:* While technically valid, this is addressed by the joint SOP+RST training that operates at the distribution level.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the reconstruction evaluation.** Either (a) train/fine-tune baselines on the same noisy data and match total bitrate, or (b) present Table 1 as contextual evidence that the codec functions adequately (not as a competitive result) and clearly acknowledge the bitrate disparity.

2. **Remove or substantially revise Section 3.6.** The attempted MVT proof does not work. Replace it with direct empirical evidence of disentanglement: probe classifiers trained on Zs to predict BGS type, cross-correlation analysis between Zs and Zn, or t-SNE/PCA visualizations of the subspaces.

3. **Define "angular matrix" or replace the term with a precise mathematical description** of the covariance condition needed for the SOP derivation.

4. **Specify all missing architectural details:** K_s, K_n, codebook sizes, total parameter count, and inference runtime.

5. **Report WER\* for Ablation-1 and Ablation-2** in Table 4 and explain why ASR fails in those configurations.

6. **Discuss the SDR-B degradation from SG more honestly** as a design trade-off rather than a "slight decrease."

## Score and Decision

**Calibration Summary:**

| Anchor Paper | Score | Round | Comparison |
|---|---|---|---|
| USC: Universal Semantic Disentangled Privacy-preserving Speech (Id2JMVSQHZ) | 4.80 | R1, R2 | DeCodec is stronger — its speech/BGS decoupling is a genuinely novel contribution, whereas USC applies known disentanglement to privacy |
| DC-Spin: Speaker-invariant Speech Tokenizer (OW332Wh9S5) | 4.75 | R2 | DeCodec is stronger — more novel contribution and better empirical grounding |
| RepCodec: Speech Representation Codec (LfDUzzQa3g) | 5.50 | R1, R2 | Comparable — RepCodec has cleaner evaluation but less novelty |
| Vec-Tok Speech (C53xlgEqVh) | 5.20 | R2 | Comparable scope, DeCodec has stronger technical novelty |
| Codec-LM Co-design (KCVv3tICvp) | 5.00 | R1, R2 | DeCodec is stronger — more novel technical contribution |
| GenSE: Generative SE via LMs (1p6xFLBU4J) | 6.00 | R2 | GenSE has cleaner evaluation but less novelty; accepted despite its own limitations |

**Round 1 Bracket:** 4.0–6.5

**Narrowing:** Comparison with the six anchors above places DeCodec above the 4.75–4.80 papers (stronger contribution), comparable to the 5.0–5.5 papers, and below the 6.00 accepted paper (which had cleaner evaluation). Within this bracket, DeCodec's evaluation issues (bitrate mismatch, flawed proof, data mismatch) are more significant than RepCodec's and Vec-Tok Speech's issues, while its contribution is stronger than USC's and DC-Spin's.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>