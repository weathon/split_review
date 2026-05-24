Now I have all the calibration data I need. Let me finalize my assessment.

**Round 1 bracket: 5.0–7.0**

**Round 2 narrowing:** UniHM clearly outperforms the 5.5-band anchors (3D Interacting Hands at 5.50 — limited novelty, marginal results; GenBot at 5.50 — different domain), and falls below the 7.0-band anchors (TraceVLA at 7.0 — 150K trajectories, 137 configurations, rigorous; Video Language Planning at 7.0 — strong algorithm + comprehensive experiments). It is most comparable to RoboFlamingo (6.50, accepted) and HAMSTER (6.00, accepted), with slightly less experimental polish than the former and a more novel technical contribution than the latter.

**Final score: 6.0, Accept**

Now let me write the consolidated review.

---

## Summary
UniHM is a unified framework for generating language-conditioned dexterous hand manipulation sequences from RGB-D observations. It combines three components: (1) a morphology-agnostic VQ-VAE tokenizer that maps heterogeneous hands (MANO, Shadow, Allegro, SVH, Leap, Panda) into a shared codebook via cross-hand distillation; (2) a VLM (Qwen3-0.6B) trained with a progressive masking curriculum to generate manipulation token sequences from language, target trajectories, and object point clouds; and (3) a physics-guided frame-wise Gauss-Newton refinement that enforces contact, generative, and temporal priors. The system trains solely on retargeted human-object interaction data (DexYCB, OakInk), eliminating the need for teleoperation. Benchmarks show consistent improvements over text-to-motion baselines, and real-world trials on a dexterous hand demonstrate higher success rates.

## Strengths
- **Morphology-agnostic tokenizer with cross-hand distillation (Section 3.2).** A shared VQ-VAE codebook combined with an encoder-distillation loss (Eq. 3) aligns heterogeneous hand morphologies without gradient disruption, enabling direct token reuse and cross-hand pose translation (Eq. 6). This is a genuine architectural contribution that directly supports the claim of scalable, hand-agnostic manipulation.

- **Consistent benchmark improvements (Tables 1, 2).** UniHM reduces MPJPE by 13–16mm on unseen DexYCB splits and by ~3–5mm on OakInk compared to the strongest baseline (MotionGPT3), with corresponding gains in FOL, FPL, and FID. The margins are substantial and hold across both seen and unseen test splits.

- **Physics-guided dynamic refinement (Section 3.4, Table 4).** The frame-wise Gauss-Newton optimization with contact, generative, and temporal energy terms (Eqs. 13–18) is mathematically well-specified. The ablation shows removing refinement increases MPJPE by ~4mm and FPL by ~3mm on seen data, confirming its role in improving physical plausibility.

- **Decoupled architecture (Section 3.3).** Separating CLIPort/PointSAM perception from VLM-based HOI generation is a sensible design. It allows fine-tuning only the smaller perception head under distribution shift, improving robustness without retraining the full model.

- **Validated ablation of each component (Table 4).** Removing depth input, masked training, or physical refinement each degrades performance meaningfully, confirming that all three design choices contribute to the final results.

## Weaknesses

### Major
- **Real-world evaluation lacks experimental rigor (Table 3).** Success rates are reported as single percentages per cell with no trial counts, no description of the robot platform, no object lists, no randomization protocol, and no variance. A result like "65% Grasp" carries little weight without knowing whether this is 13/20 vs. 65/100 trials, or what objects and initial conditions were used. The paper claims "extensive real-world cross-embodiment experiments" (Section 1) but the reported evidence is essentially anecdotal. This undermines what should be the paper's strongest selling point.

- **Baseline adaptation is insufficiently described.** The baselines (TM2T, MDM, FlowMDM, MotionGPT3) are general-purpose human motion generation models. The paper states their outputs are "post-processed with our physics-guided refinement to ensure a fair comparison" (Section 4.3), but never explains how these models were trained on DexYCB/OakInk hand-pose data, how they were adapted to output dexterous hand poses (vs. full-body human motion), or whether they had access to the same language annotations. Without these details, it is impossible to assess whether the comparison is genuinely fair or whether the baselines are operating at a structural disadvantage.

### Minor
- **"Open-world" is overclaimed.** The paper frames its contribution as "generalization to open-world tasks" (Figure 1, Section 1) and uses "open-world" language throughout, but the evaluation uses standard 80/20 train/test splits on DexYCB and OakInk. This is an object-instance generalization test, not an open-world one. The real-world experiments do test on some unseen objects, but still within a constrained lab setting. The framing should be calibrated to what was actually tested.

- **Some architecture details are under-specified.** The "Transfer function" labeled in Figure 2 is never defined in the text. While its role can be inferred from Eq. 9 (the VLM generating codebook indices that get decoded), the lack of explicit definition introduces avoidable ambiguity. The exact autoregressive generation mechanism of the VLM (token-by-token decoding, sequence length handling) could also be clearer.

- **No cross-morphology transfer experiment.** A key claimed contribution is the morphology-agnostic codebook enabling skill transfer across hands, yet there is no experiment isolating this effect (e.g., training the VLM on hand A and testing zero-shot on hand B). Adding such an experiment would directly validate a headline claim that currently rests on architectural design alone.

- **GPT-4o annotation quality and retargeting fidelity are unevaluated.** The automatic language annotation pipeline (Section 3.1) generates five instructions per sequence, but the paper never quantifies annotation quality or consistency. Similarly, Dex-Retargeting is used to map MANO poses to five robot hands, but no analysis of retargeting fidelity is provided. Both introduce unquantified noise into the training signal.

### Trivial
- Figure 2 labels a "Transfer function" component without a corresponding definition in the main text or a forward reference to Eq. 9.
- The paper's writing occasionally overstates claims relative to the evidence (e.g., "extensive real-world cross-embodiment experiments" given the limited reported data).

## Nice-to-Haves
- A cross-morphology zero-shot transfer experiment (train on MANO, test on Shadow/Allegro) would directly validate the morphology-agnostic codebook claim.
- Quantifying GPT-4o annotation quality (e.g., human evaluation of instruction relevance) and retargeting fidelity would rule out systematic corruption of the training signal.
- Reporting computational requirements (GPU hours, training time for the VLM and tokenizer) would aid reproducibility.
- Including HOIGPT or a language-conditioned DexGrasp baseline would position UniHM more precisely among recent hand-object methods.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh critic claim that VLM inference adaptation is unexplained:** REMOVED. The "Inference Stage" paragraph (Section 3.3) explicitly states: "At inference, a separate CLIPort module estimates these quantities from RGB-D observations, decoupling spatial perception from hand-object interaction... when the scene distribution changes, we fine-tune only CLIPort, which is smaller and less data-hungry, rather than the entire model." The paper already addresses this.

- **Harsh critic claim that "w/o Masked Training" is vaguely defined:** REMOVED. Section 4.4 explicitly describes the ablation: "Training starts with the teacher forcing the use of both language and ground-truth sequences, then gradually replaces a fraction p_t of ground truth with [MASK]." Eq. 10 formalizes the masking process. The ablation condition is adequately defined.

- **Harsh critic claim that physics refinement "does not explicitly enforce joint limits, collision avoidance, or physical dynamics":** REMOVED. The paper acknowledges these as limitations in the conclusion ("simplified energy terms for contact and friction"), and the optimization does incorporate contact (Eq. 13) and temporal smoothness (Eq. 15) terms. The harsh critic's framing as a fatal flaw is inconsistent with the paper's honest acknowledgment.

- **Strength Finder claim that real-world results "demonstrate the effectiveness of the dedicated tokenizer and VLM":** RETAINED but weakened. The real-world results directionally support this, but the limited experimental rigor means they should be treated as preliminary rather than conclusive.

- **Strength Finder claim about "consistent generalization to unseen objects and instructions":** RETAINED. The benchmark results in Tables 1 and 2 do show this consistently.

- **Harsh critic about HOIGPT positioning:** MOVED to Nice-to-Haves. The paper does discuss HOIGPT in related work, and the positioning is adequate though could be more precise.

- **Harsh critic about missing trial counts, platform, etc. in real-world evaluation:** RETAINED as a Major weakness. This is a genuine and important gap.

## Novel Insights
The unified tokenizer's use of encoder distillation (Eq. 3) to bypass the gradient discontinuity of the quantization step when integrating new hand morphologies is a genuinely clever design choice. Rather than attempting direct token alignment (which would be non-differentiable), the method first aligns encoder latent spaces continuously, then fine-tunes within the VQ-VAE pipeline. This staged approach for scalable cross-morphology integration could generalize to other multi-embodiment settings beyond hands.

## Suggestions
- Redesign the real-world evaluation with standard rigor: specify the robot platform, conduct at least 10–20 trials per condition with randomized object positions, and report means with confidence intervals. This would transform Table 3 from anecdotal to convincing.
- Add a paragraph detailing how the baselines were trained and adapted for the DexYCB/OakInk evaluation, including any data preprocessing, architecture modifications, and whether they used the same GPT-4o language annotations.
- Replace "open-world" terminology with more precise language ("held-out object generalization," "unseen object categories") to accurately reflect the experimental design.
- Define the "Transfer function" component explicitly, or remove the label from Figure 2 if it merely refers to the process already described in Eq. 9.

## Score and Decision

### Anchor comparison summary
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| HandsOnVLM (AJQuTFd9es) | 6.33 | R1 | Similar hand+VLM domain; UniHM more complete system, more experiments, but similar detail gaps |
| HAMSTER (h7aQxzKbq6) | 6.00 | R1 | Both hierarchical VLA designs; UniHM tackles harder problem (dexterous hand), similar real-world rigor |
| RoboFlamingo (lFYj0oibGR) | 6.50 | R1/R2 | More polished evaluation (CALVIN), thorough ablations; UniHM has real-world eval but less rigorous |
| 3D Interacting Hands (nTNElfN4O5) | 5.50 | R2 | UniHM clearly stronger — more complete system with real-world validation and larger contribution |
| TraceVLA (b1CVu9l5GO) | 7.00 | R2 | Significantly more comprehensive evaluation (137 configs + real robot); UniHM less polished |
| Video Language Planning (9pKtcJcMP3) | 7.00 | R2 | Stronger algorithmic contribution and more comprehensive experiments |

**Round 1 bracket:** 5.0–7.0.  
**Round 2 narrowing:** UniHM is clearly above the 5.50 anchors and below the 7.00 anchors. It is closest to RoboFlamingo (6.50) and HAMSTER (6.00). The real-world evaluation rigor weakness places it below RoboFlamingo; the stronger technical novelty (unified hand tokenizer, physics refinement) and harder problem setting place it slightly above HAMSTER. **Final score: 6.0.**

The paper addresses a timely problem, assembles interesting components, and demonstrates genuine improvements over baselines on standard benchmarks. The core weaknesses — under-rigorous real-world evaluation and insufficient baseline adaptation details — are significant but addressable in a revision. The technical contributions are real and the ablation studies validate the design choices. I recommend acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>