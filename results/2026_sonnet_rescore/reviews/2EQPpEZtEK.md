Now I have a full picture of the paper. Let me write the final consolidated review.

---

## Summary

DiSTAR is a zero-shot TTS framework that operates entirely in a discrete RVQ code space, coupling a causal autoregressive language model (which drafts a patch-level sketch) with a LLaDA-style discrete masked diffusion transformer (which performs parallel intra-patch infilling). This avoids continuous-latent instabilities while inheriting LM-style discrete controllability. On two standard benchmarks (LibriSpeech-PC test-clean and SeedTTS test-en), DiSTAR-medium (0.3B) achieves the lowest WER among all compared systems and the highest SMOS in listener evaluation. A training-time stochastic RVQ layer truncation scheme enables test-time bitrate/compute control without retraining.

---

## Strengths

- **State-of-the-art WER**: DiSTAR-medium achieves 1.66% on LibriSpeech test-clean and 1.32% on SeedTTS test-en (Table 1), the lowest among all systems including human (1.80%, 1.47%), demonstrating exceptionally robust intelligibility from the AR+discrete-diffusion design.
- **Highest subjective speaker similarity (SMOS)**: In listener evaluation (Table 2), DiSTAR achieves SMOS 3.31, above E2TTS (3.29), CosyVoice 2 (3.07), and FireRedTTS (2.36), showing the discrete code space preserves timbral fidelity perceptually despite lower objective SIM than E2TTS.
- **Test-time controllability via RVQ layer pruning**: The stochastic layer truncation training (Section 3.4) enables zero-retraining test-time trade-offs. Figure 2 demonstrates that speaker similarity rises monotonically from 0.58 (2 layers) to 0.64 (9 layers) while WER bottoms near 6 layers, providing a practical bitrate-quality dial.
- **Competitive parameter efficiency**: DiSTAR-base (0.15B) achieves 1.90% WER and 4.29 UTMOS on LibriSpeech (Table 1), outperforming DiTAR (0.6B, 2.39% WER) in robustness at less than one-quarter the parameter count — a concrete indication of representational efficiency in the discrete space.
- **No duration predictor**: DiSTAR dispenses with forced alignment and duration predictors (Section 3.1.2), simplifying the training pipeline relative to several baselines while achieving stronger robustness metrics.

---

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled NFE difference in the central DiTAR comparison**: Table 1 pits DiSTAR (NFE=24) against DiTAR (NFE=10) — a 2.4× difference in diffusion iterations, favoring DiSTAR. Because diffusion quality generally improves with more NFEs (up to saturation), the headline WER advantage (2.39% → 1.66% on LibriSpeech) and the SIM gap cannot be attributed to the discrete-domain design choice alone. Neither ablation (DiSTAR at NFE=10; DiTAR at NFE=24) is provided. Since the paper's central thesis is that operating in discrete RVQ space yields better stability and quality than DiTAR's continuous approach, this confound materially weakens the core claim.

- **DiTAR absent from the subjective evaluation (Table 2)**: The system DiSTAR most directly claims to surpass does not appear in Table 2. The listener study compares DiSTAR against FireRedTTS, CosyVoice 2, E2TTS, and F5TTS — none of which is the paper's primary motivating competitor. The CMOS result (0.22 vs. 0.00 human) therefore cannot be interpreted relative to DiTAR. This structural asymmetry — DiTAR in Table 1 but not Table 2, while the other systems are in Table 2 but not Table 1 — means no single table gives a complete comparative picture, and the subjective evaluation cannot validate the paper's main claim.

- **Ablation study does not isolate the key architectural contribution**: Table 3 only varies decoding temperature settings (sampling vs. greedy, $T_{\text{time}}$, $T_{\text{layer}}$). No experiment removes or replaces the masked diffusion component with a simpler intra-patch decoder (e.g., single-pass prediction or a lightweight AR), compares overlapping vs. non-overlapping windows, or ablates the stochastic RVQ layer truncation, factorized embeddings, or codebook transplant initialization. The central design question — *does discrete masked diffusion within each patch actually help over a simpler intra-patch decoder?* — is left unanswered.

### Minor

- **CMOS above human (0.22 ± 0.13 vs. 0.00) reported without any discussion**: This is an anomalous result — synthesized audio rating above matched human recordings on naturalness is extraordinary. The paper summarizes it in one sentence ("The same trend is observed in the objective predictor UTMOS and in CMOS listening tests") without acknowledging that it is surprising, without describing the human reference material, and without any analysis of ceiling effects or prompt-domain matching. Whether this reflects a genuine quality achievement or a property of the evaluation design (e.g., read-speech references that are not well-matched to the synthesis domain), the paper must address it explicitly.

- **Abstract overclaims speaker similarity**: The abstract states DiSTAR "surpasses state-of-the-art zero-shot TTS systems in robustness, naturalness, and **speaker/style consistency**." However, E2TTS achieves SIM 0.70–0.71 on both benchmarks, higher than DiSTAR-medium's 0.66–0.67 (Table 1). DiSTAR leads on subjective SMOS, but the objective claim of universally surpassing speaker similarity is not supported. Section 4.2 attributes this to "reduced sensitivity to high-frequency artifacts in the reference prompt," but no supporting evidence is provided for this attribution.

- **No actual latency/throughput data despite "inference cost close to DiTAR" claim**: The abstract and introduction state that DiSTAR maintains "inference cost close to its continuous counterpart DiTAR." Given the NFE difference (24 vs. 10), this claim is not self-evident. Section 4.4 discusses RVQ layer pruning but provides no wall-clock latency, RTF (real-time factor), or FLOPs comparison. A model can be smaller in parameters yet more expensive at runtime if it runs many more diffusion steps.

### Trivial

- The paper introduces three separate inference heuristics (layer-wise temperature shaping, position-wise temperature shaping, hybrid sampling) to address a "tail-first bias" discovered post-hoc. The paper honestly acknowledges this as a training/inference mismatch (Section 3.4: "in principle, the greedy/sample schedule is a hyperparameter; we adopt a simple half-half scheme to avoid over-tuning"), but the necessity of three compensatory fixes suggests the masking objective does not fully resolve the positional confidence issue during training.

---

## Nice-to-Haves

- An apples-to-apples comparison with DiTAR at the same NFE (e.g., both at NFE=10 and NFE=24) would be the single most impactful addition to substantiate the paper's core thesis.
- A controlled domain-shift experiment (e.g., evaluating both DiSTAR and DiTAR on out-of-domain prompts) would directly validate the claimed brittleness of continuous systems under distribution shift, which is currently asserted but not evidenced.
- Adding DiTAR to Table 2 (or a dedicated CMOS/SMOS comparison with DiTAR) would complete the evidential chain for the subjective naturalness claim.
- A minimal ablation replacing masked diffusion with a simple one-shot intra-patch predictor would isolate the contribution of the iterative decoding within patches.
- A brief analysis of why CMOS exceeds human (e.g., checking whether the human reference prompts are lower-quality read-speech) would clarify whether this is a meaningful finding or an evaluation artifact.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Harsh critic: "claimed advantages never demonstrated experimentally"** — Partially retained as Major #1 (NFE confound) and merged with the DiTAR comparison issue; the broader version of the claim (asserting optimization fragility comparisons must be shown) is outside the paper's stated scope and is removed.
- **Harsh critic: tail-first bias as "structural fatal flaw"** — Demoted to Trivial. The paper acknowledges it honestly and the heuristics demonstrably work (Table 3). It is a design tension, not a failure.
- **Strength Finder: "Design simplicity via implicit timing modeling"** — Removed as somewhat generic; the no-duration-predictor observation is already captured under Strengths above.
- **Strength Finder: "Effective decoding heuristics"** — Removed as a primary strength and merged into context. The heuristics work but exist to fix a bias; promoting them as a key strength conflicts with the verified Trivial weakness about their necessity.

---

## Novel Insights

The central novel observation — threading LLaDA-style discrete masked diffusion into the intra-patch slot of a DiTAR-style blockwise AR system — is genuinely elegant: it reuses the codec's own quantization space for both training and inference, avoiding the continuous-latent distribution mismatch, while the stochastic RVQ layer truncation provides a bitrate-quality dial that has no obvious analog in continuous systems. The reviewer synthesis suggests an underexplored insight: because the discrete code space supports greedy decoding (Section 3.4, Table 3 — greedy WER 1.91% vs. sampling 2.11%), DiSTAR may be the first patchwise AR+diffusion TTS system for which greedy decoding is competitive. This has practical implications for deterministic, latency-sensitive deployment that the paper does not fully develop.

---

## Suggestions

1. Re-run Table 1 with DiTAR at NFE=24 *or* DiSTAR at NFE=10 — whichever is feasible — and report both, so the NFE axis is separated from the continuous vs. discrete axis.
2. Add DiTAR to Table 2 (subjective evaluation). Even a pilot listener study with a subset of samples would close the most important evidential gap.
3. Add a short ablation replacing the masked diffusion refiner with a single-pass prediction head to isolate its contribution.
4. Include a brief analysis section for the CMOS > human result: describe the human reference source and check whether it is domain-matched to the synthesis condition.
5. Replace the qualitative claim in Section 4.2 ("reduced sensitivity to high-frequency artifacts") with either a quantitative artifact analysis or soften it to a hypothesis.
6. Report RTF or wall-clock latency per second of generated audio for DiSTAR and, if possible, DiTAR, to substantiate the "comparable inference cost" claim.

---

## Evaluation on Key Axes

- **Originality**: Moderate-high. The discrete masked-diffusion-within-patch formulation is a genuinely novel combination in TTS, though it assembles established components (DiTAR patchwise AR, LLaDA masked diffusion). The stochastic RVQ truncation trick is novel.
- **Importance of research question**: High. Zero-shot TTS with controllable inference is an active, practically important problem; addressing the brittleness of continuous-latent systems is well-motivated.
- **Claims well supported**: Moderate. WER and SMOS claims are well supported. The core comparative claim over DiTAR is confounded by NFE. Speaker similarity claims in the abstract are overclaimed relative to objective SIM.
- **Soundness of experiments**: Moderate. Benchmark evaluation is standard and thorough. Ablation is narrow and does not isolate the main architectural contribution. The NFE confound is a genuine methodological gap.
- **Clarity of writing**: Good. Formulation is precise, design choices are clearly motivated. The CMOS anomaly and the SIM discrepancy in the abstract are exceptions where clarity breaks down.
- **Value to community**: High if the NFE confound is resolved. As written, it demonstrates strong practice and introduces useful ideas (test-time RVQ pruning, discrete masked diffusion for TTS), but the central comparative claim is not fully established.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>