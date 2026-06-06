Now I have a clear picture of the paper. Let me draft the review before running calibration.Now let me run Round 1 calibration — bracketing pass.Let me read a couple of the most topically relevant anchors.**Round 1 bracket: 4–6.** RisoTTo is better than the Fox-TTS anchor (score 3.0) and comparable to A2-Flow/SpeechFlow anchors (5.5–5.75). Let me narrow within this bracket.Now I have enough calibration data for the final assessment.

**Round 1 bracket: 4–6**
**Round 2 narrowing:** RisoTTo sits between L3Speech (4.6, rejected) and MaskGCT (5.25, accepted). It has more convincing ablations than L3Speech but is weaker in scale and empirical quality than MaskGCT. The overclaiming issue and absent human evaluation are material. Final score: **4.5**.

---

## Summary

RisoTTo is a non-autoregressive (NAR) zero-shot TTS system that proposes three technically coherent techniques to close the quality gap with autoregressive (AR) models: Soft Alignment Generation (SAG), a flow-matching network that distills attention-based soft alignments without access to acoustic features at inference; an Invertible Encoder (IE) based on normalizing flow that models residual acoustic information as a Gaussian prior; and Prompt-Aware Lightweight Convolution (PAL), which adapts convolutional kernel weights from a speaker embedding. The system achieves striking efficiency (33M parameters, 0.89s latency for 10s speech) while remaining competitive on speaker similarity and broadly competitive on perceptual quality metrics.

---

## Strengths

- **SAG demonstrably outperforms standard NAR upsampling**: Table 1 shows SAG achieves 4.19 MOS vs. 3.85 (hard upsampling) and 4.07 (Gaussian upsampling), closely approaching the oracle "Attention" condition (4.24 MOS) that requires ground-truth mel at inference. This concretely validates the core alignment hypothesis.

- **IE outperforms VAE for residual modeling across two experiments**: Table 2 shows IE yields higher disentanglement from the context vector (MMD(c_s, z) = 2.613 vs. 1.941) and closer fit to the Gaussian prior (MMD(z,ε) = 0.207 vs. 0.611). Table 3 independently confirms: on LJSpeech, NAR+IE achieves 3.64 MOS vs. 3.51 for NAR+VAE and 3.38 for plain NAR.

- **PAL isolates a specific SECS contribution**: Table 5 shows removing PAL drops SECS from 0.673 to 0.638 while MOS barely changes (4.11→4.08), cleanly isolating PAL's targeted role in zero-shot speaker adaptation.

- **Highest SECS across all compared systems despite a fraction of their scale**: Table 4 reports RisoTTo SECS 0.668 (VCTK) and 0.651 (Seed-TTS), surpassing AR models (VALL-E 0.541, T5-TTS 0.613) and large NAR models (MaskGCT 0.637, F5-TTS 0.646), while using ~900h training data versus tens of thousands of hours for most competitors.

- **Compelling and well-documented efficiency advantage**: 0.89s latency and 33M parameters vs. 3.6s–6.9s and 220M–1048M for all competitors (Table 4). This is the paper's single strongest and most clearly documented contribution.

- **Systematic ablation validates each module's contribution**: Table 5 shows consistent, interpretable degradation for each removed module: −SAG hurts MOS most, −IE hurts WER most, −PAL hurts SECS most.

---

## Weaknesses

### Fatal
None.

### Major

- **The conclusion contradicts the empirical results**: The conclusion states "RisoTTo achieved better performance compared with representative zero-shot autoregressive TTS," but Table 4 shows T5-TTS (AR) outperforms RisoTTo on both VCTK MOS (4.21 vs. 4.14) and WER (4.91 vs. 5.51), and MaskGCT exceeds RisoTTo on MOS on both datasets and WER on Seed-TTS. The body of Section 4.3 correctly hedges: "While T5-TTS and MaskGCT outperform RisoTTo in terms of MOS and WER..." The title "Beyond Autoregressive Models" further amplifies this misrepresentation. The defensible claim—speaker similarity leadership and dramatic efficiency at competitive quality—is actually a more interesting and well-supported contribution than the overclaimed "beyond AR" narrative.

- **All perceptual quality claims rest on automated NISQA-MOS with no human evaluation**: Section 4 explicitly states NISQA-MOS is used "instead of human evaluation." The paper's central thesis is that NAR quality is now comparable to AR quality—precisely the type of claim that requires human perceptual validation. The key differences are small (e.g., RisoTTo 4.14 vs. MaskGCT 4.18 VCTK MOS) and across architecturally dissimilar systems (mel+HiFi-GAN vs. codec-token AR models), a setting where automated MOS correlation with human perception is weakest. The "comparable to AR" quality claim is the evidentiary centerpiece of the paper, and it is not adequately grounded.

### Minor

- **Logical inconsistency in the VAE posterior collapse explanation (Section 4.2)**: The paper claims "the VAE tends to produce a z that is too close to the prior, leading to posterior collapse." However, Table 2 shows the opposite: VAE's MMD(z,ε)=0.611 is higher than IE's 0.207, meaning VAE's z is actually *less* close to the Gaussian prior. The paper's own cleaner explanation appears later: IE is deterministic so it can be pushed close to the prior without information collapse. The initial "too close to prior" characterization of the VAE is inverted relative to the data and should be corrected.

- **PAL kernel reshaping is unexplained**: Section 3.4 states the 256-dim speaker embedding s is "reshaped" to a 3×8=24-element kernel for the text encoder and 17×8=136-element kernel for the mel decoder. No projection layer is described. If s is used directly, 232 of 256 dimensions are discarded for the text encoder kernel—a significant waste of speaker embedding capacity. Whether there is a projection (which would be the natural fix) is never specified.

### Trivial
None.

---

## Nice-to-Haves

- A small-scale human listening study (ABX or preference tests, even 50–100 pairings) comparing RisoTTo to T5-TTS and MaskGCT on the same utterances would substantiate or challenge the automated MOS comparisons and directly support the efficiency-quality tradeoff narrative.
- The training-inference mismatch from sampling z~N(0,1) at inference vs. the true posterior at training is acknowledged but not characterized empirically. Showing robustness of this approximation across diverse speakers/text lengths would strengthen the IE design argument.
- Characterizing SAG alignment quality on phonetically complex or long utterances (vs. hard upsampling) would make the mechanism claim more concrete and practically grounded.
- Discussion of prompt length sensitivity: PAL and cross-attention both assume a fixed 3-second segment. Robustness to shorter or variable-length prompts is unaddressed.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Training data scale disparity as a weakness** (Harsh Critic §3): RisoTTo uses ~900h vs. VALL-E's 60K hours and Emilia-scale data for F5-TTS/MaskGCT. By the hard rule on asymmetric comparison (the asymmetry favors the baselines, not the authors' method), this is not a weakness—it actually strengthens the contribution narrative. The fact that RisoTTo leads on SECS despite two orders of magnitude less data is a genuine finding.

- **Demo-page sourcing for VALL-E/T5-TTS/NaturalSpeech2** (Harsh Critic §3): The paper discloses this methodology explicitly and constrains comparison to the same VCTK utterances. The concern is noted but already addressed in Section 4.3, making it a minor acknowledged limitation rather than a hidden confound. The asterisked entries in Table 4 clearly flag these.

- **"Attention" oracle is not deployable** (Harsh Critic section on SAG): The paper explicitly discloses this uses the target mel-spectrogram: "Attention mechanism in Table 1 denotes soft alignment produced from attention mechanism with target mel-spectrogram." This is standard oracle upper-bound practice and not a misleading framing.

- **IE only validated on LJSpeech for Table 3** (Harsh Critic): The single-speaker controlled experiment for mechanism validation plus the zero-shot ablation (Table 5) is standard experimental design, not a gap. The zero-shot claim is directly evidenced by Table 5.

- **Small ablation sample sizes** (Harsh Critic): 30 samples (Table 1), 50 samples (Table 5) with CIs reported. This is within standard TTS ablation practice. The CIs are explicitly provided.

- **Strength "important problem / important research direction"** (Strength Finder generic framing): Removed per rule against generic importance-of-problem strengths not backed by specific paper content.

---

## Novel Insights

The most genuinely novel architectural insight in RisoTTo is the combination of two separate generative models addressing two *different* gaps in NAR TTS: flow matching for the alignment problem (SAG) and normalizing flow for the acoustic residual problem (IE). The IE design—pushing a deterministic encoder's output distribution close to a Gaussian prior so inference-time Gaussian sampling is a valid proxy—is a cleaner solution to the training-inference mismatch than VAE posterior sampling, because the determinism eliminates the information-collapse failure mode without constraining how much residual information is captured. The partial muddle in the VAE/IE comparison explanation (Section 4.2) obscures what is actually a clean and principled design choice that deserves clearer articulation.

---

## Suggestions

1. **Revise the conclusion and title** to remove "beyond autoregressive" and "better performance compared with representative zero-shot autoregressive TTS." The accurate framing—highest speaker similarity (SECS) with 7–38× lower latency and 7–32× fewer parameters, at broadly comparable perceptual quality—is a stronger, more defensible, and more interesting contribution.
2. **Add a human evaluation component**: Even a small crowdsourced preference study comparing RisoTTo vs. T5-TTS and vs. MaskGCT on 50–100 paired samples would substantially strengthen the "comparable to AR" quality claim.
3. **Correct the VAE posterior collapse argument** in Section 4.2 to be consistent with Table 2: the point is not that VAE's z is too close to the prior (the data shows it's farther), but that VAE's stochastic sampling limits how tightly z can be forced to the prior while retaining residual information.
4. **Clarify the PAL kernel extraction** in Section 3.4: state whether a learned projection from 256 to 24/136 dimensions is used, or explain the reshaping mechanism explicitly.

---

## Score and Decision

**Anchor comparison:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Fox-TTS | pWdkM9NNCA.md | 3.00 | R1 | Weaker than RisoTTo: simpler architecture, less ablation rigor |
| Simple-TTS | m4mwbPjOwb.md | 3.00 | R1 | Weaker: end-to-end approach without comparable novelty/ablation |
| L3Speech | RK3Gj9J5my.md | 4.60 | R2 | Comparable: both have evaluation weaknesses; RisoTTo has stronger ablations and cleaner contributions |
| MaskGCT | ExuBFYtCQU.md | 5.25 | R2 | Stronger than RisoTTo: large-scale, strong empirical results, accepted; RisoTTo has overclaiming and no human eval |
| A2-Flow | e2p1BWR3vq.md | 5.50 | R1/R2 | Slightly stronger average but rejected; RisoTTo has cleaner ablations but similarly no human evaluation |
| SpeechFlow | KpoQSgxbKH.md | 5.75 | R1 | Stronger: multi-task pre-training paradigm at 60K hours, broader scope |
| DiTTo-TTS | hQvX9MBowC.md | 6.25 | R2 | Stronger: accepted, rigorous analysis with domain-agnostic design |
| ControlSpeech | zAogQOIphH.md | 5.20 | R2 | Comparable in scope; RisoTTo has better ablation discipline |

**Round 1 bracket: 4–6.**
**Round 2 narrowing:** RisoTTo sits between L3Speech (4.6, rejected) and MaskGCT (5.25, accepted). The overclaiming conclusion, reliance on automated MOS without human evaluation, and small training data vs. competitors all weigh against acceptance. The genuine efficiency story, highest SECS, and clean ablations argue for the upper end of the bracket. Ultimately the paper is closer to the L3Speech/A2-Flow tier (4.6–5.5) due to the major framing issue and missing human evaluation — both fixable, but material weaknesses for a paper whose headline claim rests on a perceptual quality comparison. I place it at **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>