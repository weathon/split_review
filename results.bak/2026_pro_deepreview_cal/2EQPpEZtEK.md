Now I have a thorough understanding of both the paper and the calibration anchors. Let me compile the final review.

---

## Summary
DiSTAR proposes a zero-shot text-to-speech framework that operates entirely in a discrete residual vector quantized (RVQ) code space, coupling an autoregressive language model (AR) drafter with a masked diffusion transformer infiller. The AR module produces patch-level sketches, and the masked diffusion model completes each patch in parallel, achieving blockwise parallelism while jointly modeling RVQ layer-time dependencies without forced alignment or a duration predictor. The method supports variable bitrate via RVQ layer pruning at inference time, and achieves state-of-the-art word error rates on LibriSpeech (1.66%) and SeedTTS (1.32%) benchmarks alongside top-ranked subjective naturalness.

## Strengths
- **Leading word error rates.** DiSTAR-medium achieves the lowest WER among all compared systems on both LibriSpeech-PC test-clean (1.66%) and SeedTTS test-en (1.32%), outperforming strong baselines including F5TTS (2.02%/1.35%) and DiTAR (2.39%/1.78%) — Table 1.
- **Strong subjective results.** In listening tests, DiSTAR obtains the highest SMOS (3.31 ± 0.25) and the only positive CMOS (0.22 ± 0.13) among evaluated systems including E2TTS, F5TTS, CosyVoice 2, and FireRedTTS — Table 2.
- **Effective inference-time controllability.** RVQ layer pruning yields a smooth trade-off: speaker similarity rises from 0.58 (2 layers) to 0.64 (9 layers) while WER remains stable around 1.9–2.1%, confirming controllability without retraining — Figure 2 and §4.4.
- **Simplified pipeline.** DiSTAR dispenses with explicit duration predictors and forced alignment (§3.1.2), yet achieves competitive or better quality than systems that rely on these components.
- **Flexible decoding strategies.** Table 3 demonstrates clear trade-offs: greedy decoding yields lowest WER (1.91%), while sample-based decoding with per-layer temperature shaping yields highest speaker similarity (0.640), giving users fine-grained control over the diversity–determinism spectrum.
- **Novel architectural coupling.** The tight integration of AR drafting with masked diffusion entirely over discrete RVQ tokens, with patch-level parallelism, represents a genuinely new point in the TTS architecture design space, distinct from both purely AR discrete approaches and continuous diffusion pipelines.

## Weaknesses

### Fatal
None.

### Major
- **Missing internal AR-only baseline.** The paper's core architectural claim is that coupling an AR drafter with a masked diffusion infiller yields advantages over purely AR generation in the discrete RVQ space. Yet there is no ablation that replaces the masked-diffusion module with a standard autoregressive head over the same RVQ tokens, keeping the model size, training data, and AR backbone identical. External baselines (IndexTTS, E2TTS, F5TTS, DiTAR) differ in representation type (continuous vs. discrete) and training protocol, so they cannot isolate the benefit of the AR+masked-diffusion coupling itself. Without this controlled comparison, the contribution of the specific architectural choice—as opposed to the RVQ representation, training data scale, or engineering details—remains unvalidated. This is a structural gap in the experimental design that weakens the paper's central claim.

### Minor
- **Efficiency claims unsupported by timing data.** The paper repeatedly asserts "comparable or lower computational cost" (abstract, §1, §4.2), but reports only NFE counts (24 for DiSTAR vs. 10 for DiTAR) and parameter counts. No inference latency, FLOPs, throughput, or wall-clock measurements are provided. An NFE comparison across discrete vs. continuous diffusion is not directly meaningful since per-step cost differs substantially. The efficiency claim should either be backed by measurements or appropriately tempered.

- **Missing key discrete-token baselines in objective evaluation.** VALL-E 2 and CosyVoice 2 are prominent discrete RVQ-based TTS systems and natural comparison points. CosyVoice 2 appears only in the subjective test (Table 2) while VALL-E 2 is absent entirely. Their omission from the objective metrics (Table 1: WER, SIM, UTMOS) makes it harder to situate DiSTAR precisely within the discrete-model landscape.

- **Subjective superiority not statistically established.** Table 2 reports SMOS for DiSTAR as 3.31 ± 0.25 vs. E2TTS at 3.29 ± 0.19 — confidence intervals overlap substantially. CMOS comparisons similarly lack significance testing. While DiSTAR is clearly competitive, the paper's claim of "state-of-the-art" across all three axes (robustness, speaker similarity, naturalness) overreaches relative to the statistical evidence presented.

- **Inference heuristics lack robustness characterization.** The temperature-shaping and hybrid sampling strategies (§3.4) are presented as part of the method's contribution, but Table 3 only compares T=1 against the chosen constants (T_layer=0.8, T_time=0.95). No sensitivity analysis across a realistic range of hyperparameter values is provided. The 50/50 sampling-greedy split is described as chosen "to avoid over-tuning" but not varied experimentally. This leaves unclear whether the method would require dataset-specific retuning for new domains.

### Trivial
- The "tail-first bias" diagnosis (§3.4) is stated as an observation without supporting empirical evidence (e.g., confidence curves or per-position confidence plots), which would strengthen the motivation for the temperature heuristics.

## Nice-to-Haves
- A long-form synthesis evaluation (utterances 30+ seconds) would substantiate the claimed mitigation of AR exposure bias across many patch steps.
- An NFE sweep or Pareto frontier comparing DiSTAR against DiTAR and F5TTS on a common hardware setup would clarify the true cost/quality trade-off.
- Reporting variance or confidence intervals for the objective metrics (WER, SIM, UTMOS) in Table 1, especially for RVQ layer pruning in Figure 2 where point estimates are reported without error bars.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh critic: "embedding initialization mismatch."** The critic questioned whether the 16-dimensional codebook vectors can fill only 16 channels of a larger d-dimensional embedding. The paper clearly states (§3.4): "transplanting the first 16 channels from the corresponding codebook of the RVQ codec. The remaining d−16 channels are sampled i.i.d. from a Gaussian." This is unambiguous — the codebook provides 16 values, and remaining dimensions are randomly initialized. No mismatch exists.
- **Harsh critic: "no evaluation of long-form synthesis."** The paper claims blockwise mitigation of exposure bias (§1) but only evaluates on short LibriSpeech/SeedTTS utterances. This is a genuine limitation but is appropriately categorized as a nice-to-have rather than a weakness, since the paper's core claims are about zero-shot quality on standard benchmarks, not long-form synthesis specifically.
- **Strength Finder: "Simplified pipeline without forced alignment or duration predictor."** Retained — this is a genuine strength confirmed in §3.1.2.
- **Strength Finder: "Patch-level parallelism via AR-plus-masked-diffusion coupling."** Retained as the architectural novelty strength.
- **Harsh critic: "overstates fragility of continuous representations."** The introduction's discussion of continuous-latent weaknesses (§1, lines 21-26) is a motivating argument, not a central claim. While broad, it is not factually wrong and properly scopes the paper's motivation. Removed as a meta-critique of rhetorical framing rather than a substantive issue.

## Novel Insights
The review process surfaces an interesting tension in evaluating hybrid AR-diffusion architectures: the field's standard baseline practices (comparing against published external systems with different representations, data scales, and training recipes) make it genuinely difficult to attribute gains to specific architectural choices. DiSTAR exemplifies this — its results are clearly strong, but the evidence that the AR+masked-diffusion coupling *specifically* drives the improvement (rather than the RVQ representation, the training recipe, or the inference heuristics) is indirect. This pattern appears across multiple TTS papers in the calibration set (CLaM-TTS, MaskGCT) and suggests that the community would benefit from establishing conventions for internal architectural baselines, akin to what is expected in NLP architecture papers.

## Suggestions
- The highest-impact addition would be an AR-only baseline: train the causal LM to directly predict next RVQ tokens (with an appropriate delay pattern) using the same data, model capacity, and training budget. Report WER, SIM, and inference steps for both greedy and sampled decoding. This single experiment would directly answer whether the masked-diffusion infiller provides benefit over a purely AR approach in the same discrete space.
- Either provide actual inference latency/FLOP measurements or soften the efficiency claim to say "comparable parameter count" rather than "comparable or lower computational cost." The current NFE=24 vs. NFE=10 comparison across discrete/continuous paradigms does not support the claim.
- Add an ablation sweeping T_layer ∈ {0.6, 0.7, 0.8, 0.9, 1.0} and T_time ∈ {0.85, 0.90, 0.95, 1.0} to characterize sensitivity and demonstrate the heuristics are not narrowly tuned.

## Score and Decision

### Calibration anchors compared:

| Paper | Avg Score | Round | Comparison to DiSTAR |
|-------|-----------|-------|---------------------|
| MaskGCT (ExuBFYtCQU) | 5.25 | R1 | DiSTAR has stronger results, more novel architecture (AR+masked-diffusion coupling rather than two-stage mask-predict), and better-controled evaluation |
| DiffAR (GTk0AdOYLq) | 5.75 | R1 | DiSTAR is far more comprehensive: multi-speaker zero-shot, large-scale training (50K hrs), many strong baselines vs. single-speaker with weak baselines |
| DiTTo-TTS (hQvX9MBowC) | 6.25 | R1/R2 | DiSTAR has stronger objective results and a more distinctive architectural contribution (discrete RVQ AR+MD vs. continuous latent DiT); both share missing-internal-baseline concerns |
| CLaM-TTS (ofzeypWosV) | 6.40 | R2 | Most comparable anchor: discrete codec LM for zero-shot TTS with novel probabilistic RVQ. DiSTAR has better WER, more comprehensive subjective evaluation, and at least equal architectural novelty |
| Continuous AR + GMM-VAE (cuFzE8Jlvb) | 6.67 | R2 | Strong anchor with genuine novelty. DiSTAR achieves better absolute metrics (WER, SIM) on larger-scale benchmarks and provides more inference-time controllability |
| Beyond Auto-Regression (uZ5K4HeNwd) | 7.00 | R2 | Different domain (LLM text generation); broadly comparable in novelty and evaluation quality |
| Interpolating AR and Discrete Diffusion (tyEyYT267x) | 8.00 | R1 | Stronger theoretical contribution and cleaner evaluation; DiSTAR lacks this level of analytical depth |

**Round-1 bracket:** 5.25–8.0, narrowed to 6.25–7.0 based on closest TTS anchors.
**Round-2 narrowing:** DiSTAR sits above the best TTS-specific anchor (6.67) due to stronger empirical results and a genuinely novel architecture, but below the 8.0 tier due to the missing internal baseline and unsupported efficiency claims. Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>