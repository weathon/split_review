Now I have a comprehensive picture. Let me write the final review.

## Summary of Calibration

### Anchor List

| Anchor | Avg Score | Round / Query | Comparison |
|--------|-----------|---------------|------------|
| Fox-TTS (pWdkM9NNCA) | 3.00 | R1-topic-low | Only one baseline; much weaker evaluation than DiSTAR |
| Simple-TTS (m4mwbPjOwb) | 3.00 | R1-topic-low | Limited evaluation, less thorough than DiSTAR |
| DM-Codec (UFwefiypla) | 3.00 | R1-topic-low | Codec-focused, different scope |
| MaskGCT (ExuBFYtCQU) | 5.25 | R1-topic-mid / R2-WER | Most comparable — similar scope and evaluation depth, but DiSTAR has stronger novelty and weaker evaluation controls |
| DiTTo-TTS (hQvX9MBowC) | 6.25 | R1-topic-mid / R2 | More thorough ablations and comparisons than DiSTAR |
| CLaM-TTS (ofzeypWosV) | 6.40 | R1-topic-mid | Stronger evaluation and presentation than DiSTAR |
| Towards Codec-LM (KCVv3tICvp) | 5.00 | R2-narrow | Rejected; similar evaluation fairness concerns |
| Enhancing ZS-TTS (bAdSmSR10C) | 5.50 | R2-narrow | Rejected; evaluation reliability concerns |
| ZS-TTS Cont. Streams (RK3Gj9J5my) | 4.60 | R3/WER | Rejected; different task, limited comparison |
| Do Not Mimic (v9LjNopQ6W) | 4.75 | R3/WER | Rejected; different task, small evaluation |
| MaskGCT (repeat) | 5.25 | R3/WER | See above |

### Round-1 Bracket
The paper was bracketed between 4.0 and 6.0 after round 1. It is substantially stronger than the low-band (3.0–3.25) papers which had minimal baselines and limited evaluation. It sits below DiTTo-TTS (6.25) and CLaM-TTS (6.4) which have more thorough evaluation and ablations. Its closest comparison is MaskGCT (5.25) — similar scope, similar level of empirical support but with different weakness profiles (MaskGCT had more novelty concerns, DiSTAR has more evaluation fairness concerns).

### Round-2 Narrowing
Searching within 4.0–6.5 confirmed the bracket. Towards Codec-LM Co-design (5.0, rejected) shares similar evaluation fairness issues. Enhancing Zero-shot TTS (5.5, rejected) had evaluation reliability concerns. None of the weakness-anchored queries returned papers with the same specific combination of weaknesses.

### What low-band anchors failed at, and does this paper share those failures?
Fox-TTS (3.0) failed primarily on insufficient baselines (only one comparison). Simple-TTS (3.0) failed on limited evaluation. DiSTAR does NOT share these failures — it has multiple strong baselines and a thorough evaluation across objective and subjective metrics. However, DiSTAR shares a *partial* failure mode with these papers: the baseline comparisons are not demonstrably fair (cited vs. reproduced scores, different NFE). But the degree is much less severe. DiSTAR's evaluation is far more comprehensive than the low-band anchors.

### Final Score Rationale
The paper presents a genuine technical contribution (coupling AR + masked diffusion in discrete RVQ space) with competitive empirical results. However, three major weaknesses — (1) baseline comparison fairness not controlled, (2) missing the most directly comparable system (DiTAR) from subjective evaluation, and (3) insufficient ablations to attribute gains to the hybrid design — prevent the paper from being a clear accept. The paper oversells some results (e.g., "SIM on par" when it is consistently lower than E2TTS/F5TTS). Score 5.0 reflects a solid technical core held back by evaluation gaps that need substantial revision.

---

## Final Review

## Summary

DiSTAR introduces a zero-shot text-to-speech framework that operates entirely in a discrete RVQ code space, coupling an autoregressive language model (drafting block-level tokens) with a masked diffusion transformer (infilling within each patch). The method achieves patch-level parallelism without forced alignment or duration predictors, and supports controllable bitrate/compute via RVQ layer pruning. On standard benchmarks (LibriSpeech-PC, SeedTTS test-en), DiSTAR attains the best WER among compared systems while showing competitive speaker similarity and naturalness. The technical design is well-motivated and the discrete-space formulation provides practical advantages (EOS termination, stable LM training, interpretable decoding heuristics).

## Strengths

1. **Strong robustness (WER) across two zero-shot TTS benchmarks.** Table 1 shows DiSTAR-medium (0.3B) achieves the lowest WER among all compared systems on both LibriSpeech-PC (1.66%) and SeedTTS test-en (1.32%), outperforming F5TTS (2.02%/1.35%), E2TTS (2.74%/2.20%), and DiTAR (2.39%/1.78%). The gap over DiTAR on LibriSpeech (1.66 vs. 2.39) is substantial and supports the claim that the discrete formulation benefits intelligibility.

2. **Competitive subjective results with DiSTAR at the top of included systems.** In the subjective evaluation (Table 2), DiSTAR achieves the highest SMOS (3.31±0.25) among FireRedTTS, CosyVoice 2, E2TTS (3.29±0.19), and F5TTS (3.08±0.20), with a positive CMOS of 0.22±0.13 relative to human.

3. **Parameter-efficient design.** DiSTAR-base (0.15B) attains WER of 1.90% on LibriSpeech-PC, surpassing IndexTTS (0.5B, 2.57%) and DiTAR (0.6B, 2.39%) with fewer parameters. Table 1 provides direct evidence for this efficiency.

4. **Controllable bitrate and compute at inference without retraining.** Stochastic layer truncation during training (Section 3.4) enables on-the-fly RVQ layer pruning at test time. Figure 2 quantifies the quality-compute trade-off across 2–9 layers, allowing adaptive deployment.

## Weaknesses

### Major

1. **Baseline comparisons are not conducted under controlled conditions.** Table 1 marks DiTAR scores with ♦ indicating they are "reported in DiTAR paper" — i.e., cited, not reproduced. The paper does not clarify whether the scores for IndexTTS, E2TTS, and F5TTS were obtained in the same evaluation environment or cited from their respective papers. Since WER is highly sensitive to ASR choice, prompt construction, and decoding parameters, comparisons mixing cited and self-evaluated scores are unsafe without verification. Furthermore, DiTAR uses NFE=10 while DiSTAR uses NFE=24, confounding method with compute budget. This undermines the paper's central robustness claim.

2. **Subjective evaluation omits the most directly comparable system (DiTAR).** Table 2 includes FireRedTTS, CosyVoice 2, E2TTS, and F5TTS, but not DiTAR — the continuous-domain counterpart sharing the same patchwise AR-diffusion paradigm. Since one of the paper's main claims is that the discrete formulation avoids the fragilities of continuous latents, the absence of DiTAR from the listening test means the paper cannot convincingly demonstrate that the discrete approach yields better perceptual quality. The reader cannot tell whether DiSTAR's subjective advantage is due to the discrete formulation or simply because it is a different/better system.

3. **Insufficient ablations to attribute gains to the hybrid design.** The ablations focus on decoding strategies (temperature shaping, greedy vs. sample) and RVQ layer pruning, but never isolate the core architectural contribution. The paper does not compare against:
   - A version without the AR drafter (pure masked diffusion over the whole sequence)
   - A version without the masked diffusion refiner (AR LM with a simple MLP head or parallel decoding)
   - DiTAR with matched NFE (to control for compute)
   
   Without these controls, it is unclear whether the performance stems from the AR+diffusion coupling, from the specific discrete formulation, from the large custom codec (0.3B params, 50k hours data), or from the higher inference compute (24 vs. 10 NFE).

4. **Discrepancy between speaker similarity claims and data.** The paper states that "DiSTAR yields SIM on par with the best alternatives." However, Table 1 shows DiSTAR-medium SIM (0.67/0.66 on LibriSpeech/SeedTTS) is *consistently lower* than E2TTS (0.70/0.71) and F5TTS (0.68/0.68) on both benchmarks. While the subjective SMOS is higher (3.31 vs. 3.29 for E2TTS), the objective SIM metric directly contradicts the "on par" characterization. This factual inaccuracy in the text should be corrected.

### Minor

5. **Marginal WER improvement on SeedTTS.** The WER gap between DiSTAR-medium (1.32) and F5TTS (1.35) on SeedTTS test-en is only 0.03 percentage points — likely not statistically significant. No confidence intervals or significance tests are reported anywhere in the paper, making it impossible to assess whether the observed differences are reliable.

6. **SMOS confidence intervals overlap substantially.** DiSTAR SMOS (3.31±0.25) overlaps with E2TTS (3.29±0.19) and even F5TTS (3.08±0.20). The CMOS confidence intervals also overlap with zero for most baselines. The language around "surpasses" and "state-of-the-art" is stronger than the data support in several categories.

7. **No wall-time or FLOPs comparison.** The paper claims "inference cost close to DiTAR" but provides no runtime measurements (RTF, wall-clock time, or FLOPs). Given the different NFE counts (24 vs. 10) and model sizes, this claim is unsubstantiated.

8. **No limitations section.** The paper lacks a dedicated discussion of limitations. Important caveats include: dependence on a large custom codec (0.3B parameters), training on 50k hours (much more data than some baselines), the ad-hoc nature of the three decoding heuristics, and the reliance on 24 diffusion steps.

### Trivial

9. Equation (1) writes the likelihood as a product over individual codes, while generation proceeds patch-wise. A clarifying remark noting this distinction would be helpful.

## Nice-to-Haves

- Add DiTAR to the subjective evaluation (Table 2). This is the single most informative comparison for the paper's thesis.
- Reproduce all key baselines (DiTAR, F5TTS, E2TTS) in the same evaluation environment with matched NFE, or clearly mark which scores are cited and discuss potential confounds.
- Add ablations that isolate the hybrid design: (a) pure AR baseline, (b) pure diffusion baseline, (c) DiTAR with matched NFE and data.
- Report confidence intervals or significance tests for WER and SIM comparisons.
- Compare the custom RVQ codec reconstruction quality against codecs used by baselines (e.g., EnCodec for DiTAR) to rule out codec quality as a confounding factor.
- Provide wall-time or FLOPs comparison to substantiate the "inference cost close to DiTAR" claim.

## Removed Points

These points are flagged for removal; treat them with caution:

- **"Equation (1) factorization doesn't match patch-wise generation"** — The equation states the standard autoregressive factorization in terms of individual codes. This is mathematically correct as the general form; the patch-wise structure is a computational approximation. Minor notation imprecision, not a weakness.
- **"λ(1−n/N) not clearly defined (N appears later)"** — N IS defined in the preceding paragraph as "the total number of the decoding steps." This is a reviewer misreading.
- **"Cut Cross Entropy mentioned but not explained"** — The paper states "Further details are provided in the Appendix B.1." The appendix was stripped by the parser; this information exists in the original submission.
- **"Unfair comparison where asymmetry favors baselines"** — The harsh critic notes an asymmetry but the rule says to remove criticisms where asymmetry favors the baseline (not the author's method).
- **"Pure formatting/style nitpicks"** — Various minor presentation suggestions that are parser artifacts or below the evaluation bar.
- **Redundant "missing appendix" criticism** — The appendix was stripped by the parser.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful methodological scrutiny (baseline fairness, ablation completeness) but do not generate novel scientific insights about the method or the problem.

## Suggestions

1. **Control the evaluation environment**: Reproduce DiTAR, F5TTS, and E2TTS in your own pipeline with the same ASR (Whisper-large-v3), same prompt selection, and same evaluation script. Report NFE-matched comparisons (DiSTAR at 10 NFE or DiTAR at 24 NFE) to separate method from compute.
2. **Add DiTAR to the listening test**: This is the single most important missing baseline. Without it, the discrete-vs-continuous claim is unsupported.
3. **Add architectural ablations**: Compare against a pure AR version (replace diffusion head with causal prediction over the flat patch) and a pure diffusion version (condition directly on text+history without AR summarizer). This would directly test whether the coupling provides value beyond either component alone.
4. **Correct the "SIM on par" claim**: Acknowledge that objective SIM is lower than E2TTS and F5TTS, and explain why subjective SMOS differs from objective SIM.
5. **Report uncertainty**: Add confidence intervals (bootstrap) or significance tests for all key metrics.
6. **Add runtime analysis**: Report RTF or wall-clock time for DiSTAR vs. baselines.
7. **Add limitations section**: Discuss dependence on the custom codec, training data scale, decoding heuristics, and NFE requirements.

## Score and Decision

**Round-1 bracket**: 4.0–6.0. The paper is substantially stronger than low-band anchors (3.0–3.25) which had minimal baselines, but has weaker evaluation controls than DiTTo-TTS (6.25) and CLaM-TTS (6.4). Its closest comparison is MaskGCT (5.25), which had similar evaluation concerns but was accepted.

**Round-2 narrowing**: Searched within 4.0–6.5. Towards Codec-LM Co-design (5.0, rejected) and Enhancing Zero-shot TTS (5.5, rejected) share similar evaluation fairness concerns. DiSTAR has stronger novelty than these papers but comparable evaluation gaps.

**What the low-band anchors failed at**: Insufficient baselines (only 1 comparison), minimal evaluation. DiSTAR does not share this failure — it has multiple baselines and thorough evaluation. However, it does share a partial failure mode: the baseline comparisons are not demonstrably fair across all systems.

**Final score rationale**: The paper has a genuine technical contribution and competitive empirical results. However, three major weaknesses — uncontrolled baseline comparisons, missing the most directly comparable system (DiTAR) from subjective evaluation, and insufficient ablations — collectively weaken the evidential basis for the core claims. The paper also contains a factual inaccuracy ("SIM on par") and lacks uncertainty quantification. These issues require substantial revision. Score 5.0 reflects a solid technical core that is not yet convincingly validated.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>