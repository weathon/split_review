Now let me search for calibration anchors.**Round 1 bracket: 5.0 – 7.0** (DiSTAR is stronger than the reject-band TTS papers, comparable to DiTTo-TTS at 6.25, but with real experimental gaps)

Now let me narrow within that range.Now I have enough to write the final review. Let me compile everything.

**Anchor summary across all rounds:**
- Round 1: Simple-TTS (3.0, Reject), Fox-TTS (3.0, Reject), CLaM-TTS (6.40, Accept), DiTTo-TTS (6.25, Accept), DiffAR (5.75, Accept), SAR Diffusion (8.0, Accept)  
- Round 2: MaskGCT (5.25, Accept), CLaM-TTS (6.40, Accept), VALL-E 2 (5.00, Reject), DiffAR (5.75, Accept)

**Bracket**: 5.5 – 6.5. DiSTAR produces SOTA WER numbers and novel integration of AR+discrete masked diffusion for RVQ speech, but has real methodological gaps (NFE confound vs. DiTAR, DiTAR absent from subjective eval, CMOS anomaly undiscussed, thin ablations). It is stronger in results than MaskGCT (5.25) and VALL-E 2 (5.00), comparable to but somewhat weaker in evidence quality than CLaM-TTS (6.40) due to the specific comparison gaps. **Final score: 6.0**.

---

## Summary

DiSTAR is a zero-shot TTS system that couples a causal autoregressive language model with a discrete masked diffusion Transformer operating entirely in the RVQ code space. Rather than working in continuous latents (as DiTAR does), it drafts patch-level RVQ codes autoregressively and then refines each patch via iterative masked demasking, achieving blockwise parallelism and joint modeling of temporal and depth dependencies in multi-codebook speech representations. The system also introduces stochastic RVQ layer truncation during training, enabling test-time bitrate/compute control without retraining.

---

## Strengths

- **SOTA WER on both benchmarks**: DiSTAR-medium achieves 1.66% WER on LibriSpeech test-clean and 1.32% on SeedTTS test-en (Table 1), the lowest among all compared systems, demonstrating strong robustness and intelligibility.
- **Best subjective naturalness and similarity**: In human evaluation (Table 2), DiSTAR leads on both SMOS (3.31 ± 0.25) and CMOS (0.22 ± 0.13) over E2TTS, F5TTS, CosyVoice 2, and FireRedTTS.
- **Controllable inference via stochastic RVQ layer truncation**: Trained with randomly dropped top-k RVQ layers (Section 3.4 / Figure 2), the model gracefully degrades at test time — speaker similarity rises from 0.58 to 0.64 as layers are retained while WER stays near 2%, offering an explicit compute-quality trade-off without retraining.
- **Parameter efficiency relative to comparable systems**: DiSTAR-medium (0.3B) achieves SOTA robustness versus DiTAR (0.6B, NFE=10), suggesting the discrete RVQ pipeline achieves high quality at smaller model scale (though this comparison is confounded by NFE — see weaknesses).

---

## Weaknesses

### Fatal
None.

### Major

- **The DiTAR vs. DiSTAR comparison is confounded by a 2.4× NFE difference** (DiSTAR NFE=24, DiTAR NFE=10 per Table 1), and this is never controlled for or acknowledged. DiSTAR's headline WER improvements over DiTAR (2.39% → 1.66% on LibriSpeech, 1.78% → 1.32% on SeedTTS) could be partially or wholly attributable to the higher number of decoding steps, not the discrete-domain design. The paper does not show DiTAR at NFE=24, nor DiSTAR at NFE=10, making the primary comparative claim not directly supported by the evidence presented.

- **DiTAR is excluded from the subjective evaluation** (Table 2). The paper's strongest evidence table — where DiSTAR achieves CMOS 0.22 and SMOS 3.31 — simply omits the system the paper is most directly competing with. Since the motivation of the paper centers on outperforming DiTAR, the subjective evaluation cannot answer the core question the paper raises. The baselines in Tables 1 and 2 are partially non-overlapping (DiTAR appears only in Table 1; FireRedTTS/CosyVoice 2 appear only in Table 2), leaving no single table that gives a comprehensive comparison picture.

- **The CMOS-above-human result (0.22 vs. 0.00) is reported without any analysis or acknowledgment of its anomalous nature**. A synthesized system outperforming human recordings in a naturalness listener study is extraordinary and either reflects a meaningful finding or a characteristic of the human reference recordings used (e.g., domain/recording condition mismatch). The paper treats this result as routine: "leads on SMOS" (Section 4.2). This result needs explicit examination — was the human reference speech drawn from a matched domain? Were ceiling effects considered?

- **The ablation study (Table 3) does not isolate the central architectural contributions**. The only ablation compares decoding temperature configurations (sampling vs. greedy, different $T_\text{time}$ / $T_\text{layer}$ values). No ablation removes or replaces the masked diffusion module (e.g., with a single-pass decoder), isolates the effect of overlapping vs. non-overlapping windows, examines the stochastic layer truncation, or evaluates the factorized embedding or codebook transplanting initialization. For a paper whose primary contribution is architectural, the question "does discrete masked diffusion help over a simpler intra-patch decoder?" is not answered.

### Minor

- **No actual inference latency or throughput data is provided**, despite the abstract claiming DiSTAR "maintains the inference cost close to its continuous counterpart DiTAR." With DiSTAR at NFE=24 vs. DiTAR at NFE=10, this claim is not self-evident from parameter counts alone. Model size alone (0.3B vs. 0.6B) does not determine wall-clock inference cost when diffusion steps differ by 2.4×.

- **The abstract's claim of surpassing SOTA in "speaker/style consistency" is not fully supported**. On objective SIM, E2TTS leads on both benchmarks (0.70–0.71 vs. DiSTAR's 0.66–0.67). DiSTAR leads only on the subjective SMOS. The paper attributes the SIM gap to "reduced sensitivity to high-frequency artifacts in the reference prompt" (Section 4.2), but this is asserted without any supporting experiment.

### Trivial

- **Three post-hoc decoding heuristics (layer/time temperature shaping + hybrid sampling) are needed to address a training/inference mismatch** (tail-first bias). This is acknowledged honestly, but the three-heuristic fix is presented without ablating the individual contribution of each; Table 3 only shows combined outcomes. A per-heuristic ablation would make the analysis more informative.

---

## Nice-to-Haves

- An apples-to-apples comparison with DiTAR at matched NFE (both at NFE=10 and NFE=24) would directly test whether the discrete-domain design confers genuine advantages.
- Direct experimental evidence for the claimed brittleness of continuous systems under distribution shift (e.g., evaluating both DiSTAR and DiTAR on prompts outside the Emilia training domain) would either validate or falsify the paper's primary motivation.
- Analyzing what accounts for the CMOS > human result — e.g., characteristics of the human reference recordings, annotator criteria — would transform an anomalous finding into a meaningful insight.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "the claimed disadvantages of DiTAR are asserted but never demonstrated"** — While valid as a nice-to-have, this is largely scope creep. The paper's scope is to propose and evaluate DiSTAR; demonstrating prior-system failures would strengthen motivation but is not required. DEMOTED to Nice-to-Haves.
- **Harsh critic: "tail-first bias as a structural flaw"** — The paper openly acknowledges this issue and addresses it. The heuristics do measurably improve quality (Table 3). The absence of a per-heuristic ablation is a minor gap, not evidence of a fundamental design failure. DEMOTED to Trivial.
- **Strength Finder: "Parameter efficiency relative to DiTAR"** — The model size comparison (0.3B vs 0.6B) is real but partially undermined by the NFE confound. Retained as a strength but qualified.
- **Strength Finder: "Design simplicity via implicit timing modeling"** — This is generic praise that rewords what the paper already claims as a design goal, not a grounded empirical strength. REMOVED.
- **Harsh critic: asymmetric baseline set across tables** — While the overlap issue is real and flagged above as a Major weakness, the separate complaint about "no single comprehensive table" is a presentation concern rather than a methodological flaw. Merged into the DiTAR Major weakness.

---

## Novel Insights

The paper's most genuinely novel observation is that operating in the discrete RVQ code space allows an EOS-token-based stopping criterion, eliminating the duration predictor without sacrificing intelligibility — and that stochastic RVQ layer dropping during training naturally yields test-time bitrate/compute controllability with no additional training. The integration of LLaDA-style discrete masked diffusion into a patch-wise AR TTS framework is a clean and well-motivated design choice. However, the paper's core thesis — that discrete space confers robustness/stability advantages over continuous-latent AR+diffusion — is better treated as a hypothesis than a finding, because the experimental evidence to distinguish "discrete space helps" from "more NFE helps" is not present.

---

## Suggestions

1. **Run DiTAR and DiSTAR at matched NFE (both at 10 and 24)** and report both in Table 1. This is the single highest-impact experiment for the paper's central claim.
2. **Include DiTAR in the subjective evaluation** (Table 2). If reproducing DiTAR is infeasible, a note explaining why would suffice, but the absence as-is is an evidential gap.
3. **Discuss the CMOS > human result explicitly**: verify whether human reference recordings are from a matched domain, and acknowledge the anomaly.
4. **Add an ablation removing the masked diffusion module** (e.g., replace with a one-pass predictor or a small NAR Transformer) to show it contributes beyond what a simpler intra-patch decoder would achieve.
5. **Report real-time factor or latency measurements** to support the efficiency claim in the abstract.

---

## Score and Decision

**Anchor papers (all rounds):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| m4mwbPjOwb (Simple-TTS) | 3.00 | 1 | Much weaker: minimal novelty, poor results |
| pWdkM9NNCA (Fox-TTS) | 3.00 | 1 | Much weaker: rejected TTS with limited contribution |
| GTk0AdOYLq (DiffAR) | 5.75 | 1 | Somewhat weaker: AR diffusion for speech, solid but narrower contribution |
| hQvX9MBowC (DiTTo-TTS) | 6.25 | 1&2 | Comparable: TTS without domain-specific factors, accepted; similar comparison gaps |
| 71mqtQdKB9 (Discrete Diffusion LM) | 6.60 | 1 | Slightly stronger: solid theoretical and empirical contribution, cleaner evaluation |
| tyEyYT267x (SAR Diffusion) | 8.00 | 1 | Much stronger: AR+discrete diffusion with clean ablations, unanimous 8s |
| ofzeypWosV (CLaM-TTS) | 6.40 | 2 | Comparable: RVQ codec TTS, similar unresolved central claim issue, accepted |
| ExuBFYtCQU (MaskGCT) | 5.25 | 2 | Weaker: similar masked-codec TTS approach, less novel combination, accepted |
| 0bcRCD7YUx (VALL-E 2) | 5.00 | 2 | Weaker: codec LM TTS, no major new architecture, rejected by most |

**Round 1 bracket**: 5.0–7.0  
**Round 2 narrowing**: DiSTAR is clearly above MaskGCT (5.25) — the results are stronger and the architectural contribution more specific. DiSTAR is comparable to CLaM-TTS (6.40) in overall tier: both have SOTA results, both have an unresolved central comparison gap. DiSTAR's NFE confound and missing subjective DiTAR comparison are slightly more damaging than CLaM-TTS's missing ablation, but DiSTAR's empirical results (SOTA WER, positive CMOS vs. human) are arguably stronger. Net: DiSTAR sits at **6.0** — just below CLaM-TTS, comfortably above MaskGCT/VALL-E 2.

**Originality**: Moderate-good — adapting LLaDA-style discrete masked diffusion to RVQ TTS in the DiTAR framework is a natural but non-obvious combination.  
**Research question importance**: High — zero-shot TTS at scale is an important problem.  
**Claims support**: Moderate — WER claims are well-supported; robustness/stability claims vs. DiTAR are not.  
**Experiment soundness**: Moderate — SOTA numbers but comparison confounded by NFE and asymmetric tables.  
**Clarity**: Good — paper is clearly written.  
**Value to community**: Good — strong benchmark results and the RVQ layer pruning feature are useful practical contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>