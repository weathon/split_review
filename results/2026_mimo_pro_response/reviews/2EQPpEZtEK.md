Now I have all the information I need. Let me finalize the review and scoring.

## Summary

DiSTAR is a zero-shot TTS framework that operates entirely in discrete RVQ code space, coupling an autoregressive language model (which drafts block-level sketches) with a LLaDA-style masked diffusion transformer (which infills each patch in parallel). The paper claims state-of-the-art robustness, naturalness, and speaker/style consistency, with practical advantages including variable bitrate via RVQ layer pruning and elimination of duration predictors.

## Strengths

- **Novel and well-motivated hybrid architecture**: The combination of AR drafting with masked diffusion infilling in fully discrete RVQ space is a genuinely novel contribution that cleanly avoids the optimization fragility of continuous latent diffusion while retaining patch-level parallelism. The decomposed generator is mathematically formulated (Equations 1–2) and cleanly motivated.

- **Strong WER with parameter efficiency**: DiSTAR-medium (0.3B) achieves WER 1.66% on LibriSpeech-PC and 1.32% on SeedTTS, outperforming DiTAR (0.6B, the continuous counterpart) at 2.39% and 1.78% — better quality with half the parameters (Table 1). This is a clear, concrete result demonstrating the value of the discrete approach.

- **Variable bitrate via stochastic layer truncation**: Training with randomly dropped top RVQ layers (ℓ ~ Unif{0,…,L−1}) enables test-time pruning without retraining. Figure 2 shows speaker similarity degrades gracefully from 0.64 (9 layers) to 0.58 (2 layers), providing a practical quality-compute trade-off lever absent from most competing systems.

- **Diagnosis and mitigation of tail-first bias**: Section 3.4 identifies a specific artifact in masked diffusion decoding over temporal sequences — later patch positions receive overconfident predictions early in decoding — and provides principled mitigation (position-wise temperature shaping). Table 3 shows these improve WER from 2.11% to 1.91%, a meaningful contribution to the community's understanding of discrete masked diffusion in sequential domains.

- **Best subjective scores on SeedTTS**: Table 2 shows DiSTAR achieves the highest SMOS (3.31 ± 0.25) and CMOS (0.22 ± 0.13) among all compared systems, including F5TTS, E2TTS, CosyVoice 2, and FireRedTTS.

## Weaknesses

### Fatal
None

### Major

- **Overclaimed "style consistency"**: The abstract claims SOTA "speaker/style consistency," but the only similarity metric (SIM in Table 1) measures speaker identity via WavLM embeddings, not style (prosody, rhythm, emotion). Moreover, DiSTAR's SIM is *not* the best — E2TTS achieves 0.70/0.71 on LibriSpeech/SeedTTS versus DiSTAR-medium's 0.67/0.66. The SMOS improvement over E2TTS (3.31 vs. 3.29) is within typical annotator error bounds (±0.25 vs. ±0.19). The paper provides no metric that specifically measures style consistency, yet this is a headline claim in both the abstract and contributions section.

- **Inconsistent baseline sets between objective (Table 1) and subjective (Table 2) evaluations**: Table 1 compares against IndexTTS, E2TTS, F5TTS-v1, DiTAR. Table 2 replaces IndexTTS and DiTAR with FireRedTTS and CosyVoice 2. This makes it impossible to directly assess whether subjective gains track objective ones. Notably, E2TTS has the best SMOS among baselines (3.29) but the worst WER (2.20 on SeedTTS), suggesting evaluation dimensions may not be tightly correlated and making the aggregate "SOTA" claim harder to evaluate.

- **No latency or throughput measurements despite efficiency being a central motivation**: The paper emphasizes patch-level parallelism and claims inference cost is "close to" DiTAR (Section 1, last paragraph), but provides no wall-clock time, real-time factor, or latency comparisons. Different NFE budgets across systems (E2TTS/F5TTS: 32, DiSTAR: 24, DiTAR: 10) further complicate any efficiency comparison. Given that overcoming AR throughput limitations is presented as a key motivation, this is a significant gap.

### Minor

- **Multiple inference heuristics with no sensitivity analysis**: The decoding pipeline includes 5+ tuned parameters (T_layer=0.8, T_time=0.95, hybrid sampling 50/50 split, top-k=50, top-p=0.9, repetition penalty every 4 patches). Table 3 only ablates the temperature shaping pair vs. vanilla, not individual contributions. Without sensitivity analysis, it is unclear how robust these choices are across domains/languages or how much each contributes. This matters for reproducibility and for practitioners tuning the system.

- **Missing key ablations**: No ablation on (a) AR vs. diffusion module contribution, (b) overlapping vs. non-overlapping patches (S < P vs. S = P), (c) number of historical patches for conditioning, or (d) NFE sensitivity. The NFE=24 choice appears fixed with no sweep showing quality degradation at fewer steps — directly relevant to the efficiency argument.

- **Small objective margins without variance estimates**: DiSTAR-medium vs. F5TTS-v1 on SeedTTS is 1.32% vs. 1.35% WER (0.03% absolute). Without confidence intervals or significance tests on objective metrics (the paper provides CIs only for subjective metrics), it's unclear whether these small differences are meaningful. The LibriSpeech gap is larger (1.66 vs. 2.02), which is more convincing.

- **Non-monotonic WER in RVQ layer pruning (Figure 2)**: WER dips at 6 layers (1.88), rises at 8 (2.04), then drops at 9 (1.98). This non-monotonicity somewhat complicates the narrative that "upper RVQ layers primarily encode acoustic detail" and that WER is insensitive to layer count.

### Trivial
None

## Nice-to-Haves
- An NFE sensitivity sweep (24→16→8→4) would directly support the efficiency claims.
- Using identical baseline sets in Tables 1 and 2 would make the evaluation story much clearer.
- Per-heuristic ablation in Table 3 would help practitioners reproduce and extend the decoding strategies.
- Latency/real-time factor comparisons, at minimum against DiTAR (the paper's own continuous counterpart), would substantiate the efficiency narrative.

## Removed Points
These points are flagged to be removed, treat them with caution.
- The harsh critic's framing that inference heuristics are "ad-hoc" and fundamentally undermine the approach overstates the issue. The paper acknowledges the tail-first bias, provides a principled explanation, and the mitigations are lightweight. The concern about sensitivity is valid but was demoted to Minor with actionable fix (per-heuristic ablation).
- Concerns about English-only evaluation — while expanding to multilingual would strengthen the paper, English-only evaluation on established benchmarks is standard practice in TTS research and does not constitute a fundamental flaw.

## Novel Insights

The paper's most interesting technical observation is the identification and diagnosis of "tail-first bias" in masked diffusion over temporal sequences — the phenomenon where later patch positions receive overconfident predictions early in decoding due to causal context. This is a genuinely novel artifact specific to applying masked diffusion to sequential (rather than spatial) data, and the paper's mitigation strategies (position-wise temperature shaping) are creative. The finding that discrete code space enables rich decoding control — including functional greedy decoding — is a useful contribution to the TTS community's understanding of the discrete vs. continuous design space. The variable-bitrate capability through stochastic layer truncation is a practical and distinctive feature not commonly seen in competing systems.

## Suggestions
- Add an NFE sensitivity sweep to directly support the efficiency claims.
- Use the same baseline set in both objective (Table 1) and subjective (Table 2) evaluations.
- Replace or supplement "style consistency" claims with a style-specific metric, or soften the language to "speaker similarity."
- Add latency/real-time factor measurements, at least for DiSTAR vs. DiTAR.
- Provide per-heuristic ablation in an expanded Table 3.

---

## Calibration Report

**All retrieved anchors across rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Uj0h13lVrR.md | 1.00 | 1 | GFlowNet paper, completely different topic — weak reject |
| gwZ90hFSL2.md | 1.00 | 1 | Cross-lingual robot NLP, unrelated — weak reject |
| 5lUdTogEL3.md | 1.00 | 1 | Person re-identification, unrelated — weak reject |
| m4mwbPjOwb.md | 3.00 | 1 | Simple-TTS (latent diffusion TTS) — simpler approach, less convincing results than DiSTAR |
| pWdkM9NNCA.md | 3.00 | 1 | Fox-TTS (flow-matching TTS) — similar topic, rejected with uniform 3s, weaker results |
| UFwefiypla.md | 3.00 | 1 | DM-Codec (speech tokenization) — related topic, rejected for limited novelty |
| Qn4HEhezKW.md | 5.00 | 1 | Diffusion language models scaling — related methodology, accepted |
| ExuBFYtCQU.md | 5.25 | 1,2 | **MaskGCT** (masked generative codec TTS) — highly relevant, similar approach but less novel than DiSTAR, accepted |
| zAogQOIphH.md | 5.20 | 1 | ControlSpeech (zero-shot TTS + style control) — related, accepted with mixed reviews |
| WzrkZeDxrM.md | 4.25 | 1 | DLPO (RL for diffusion TTS) — related, rejected |
| hQvX9MBowC.md | 6.25 | 1,2 | **DiTTo-TTS** (DiT-based TTS) — directly relevant, thorough ablations but limited novelty criticism, accepted |
| ofzeypWosV.md | 6.40 | 1,2 | **CLaM-TTS** (codec LM for zero-shot TTS) — highly relevant, strong results on 100K hours, accepted |
| GTk0AdOYLq.md | 5.75 | 1,3 | DiffAR (diffusion AR for speech) — related methodology, accepted |
| 71mqtQdKB9.md | 6.60 | 1,3 | SEDD (discrete diffusion LM) — related methodology, rejected with mixed scores |
| tyEyYT267x.md | 8.00 | 1 | SAR models (AR+diffusion interpolation) — similar paradigm but for language, strong accept |
| WNvvwK0tut.md | 6.50 | 2 | Scaling MDMs on text — related methodology, accepted |
| ngp5jzx5oK.md | 4.33 | 2 | Speaker-specific latent features — related topic, rejected |
| E1DGY1FXef.md | 4.75 | 2 | Abstract style prompts for TTS — related topic, rejected |
| n6YVISFrcN.md | 4.25 | 2 | TTS evaluation methodology — related topic, rejected |
| St7k6NJKn1.md | 3.50 | 2 | Deepfake speech detection — peripherally related, rejected |

**Round-1 bracket: 5.5 – 6.5**

DiSTAR is clearly above the rejected TTS papers at 3.0-4.75 (Simple-TTS, Fox-TTS, DLPO) which had weaker results and/or less novelty. It is comparable to MaskGCT (5.25) but with a more novel architecture and cleaner empirical story. It is slightly below CLaM-TTS (6.40) and DiTTo-TTS (6.25) due to the overclaimed style consistency, inconsistent baseline reporting, and missing latency measurements — weaknesses that CLaM-TTS and DiTTo-TTS did not share to the same degree.

**Round-2 narrowing: 5.5 – 6.5 confirmed**

The key anchor comparison is with MaskGCT (5.25): DiSTAR's AR+diffusion hybrid in discrete space is more architecturally novel than MaskGCT's two-stage mask-predict, and DiSTAR's evaluation (while imperfect) is more convincing than MaskGCT's (which had a reviewer giving it 3 for "limited novelty"). The comparison with CLaM-TTS (6.40) and DiTTo-TTS (6.25) provides the upper bound — both had cleaner evaluation and more extensive ablations.

**Final score: 6.0** — DiSTAR is a solid, novel contribution with strong empirical results (best WER on both benchmarks, best SMOS, variable bitrate feature) but is held back by overclaimed consistency, inconsistent baseline reporting, missing latency data, and insufficient ablations. It sits squarely between MaskGCT (5.25) and CLaM-TTS/DiTTo-TTS (6.25-6.40).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>