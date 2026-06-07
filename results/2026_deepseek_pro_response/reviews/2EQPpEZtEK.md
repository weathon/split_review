Now I have all the anchors I need. Let me synthesize the final review.

**Calibration comparison across rounds:**

| Anchor | Avg Score | Round | Comparison to DiSTAR |
|---|---|---|---|
| MaskGCT | 5.25 | R1 | DiSTAR stronger: more novel architecture, better results, not just combining existing methods |
| DiffAR | 5.75 | R2 | DiSTAR clearly stronger: multi-speaker zero-shot vs single-speaker, 50K hrs vs LJSpeech, stronger baselines |
| DiTTo-TTS | 6.25 | R2 | DiTTo-TTS has richer ablations; DiSTAR has more architectural novelty. DiTTo-TTS slightly ahead on evaluation rigor |
| CLaM-TTS | 6.40 | R1/R2 | Similar: novel idea + evaluation gaps. CLaM-TTS slightly more thorough ablations but DiSTAR more architectural novelty |
| HALL-E | 6.40 | R1/R2 | Similar: novel idea + evaluation concerns. HALL-E's MReQ is more complex; DiSTAR's AR+MDM coupling is cleaner |

**Round 1 bracket**: 5.25–6.50  
**Round 2 narrowing**: DiSTAR lands at **6.0** — above DiffAR (5.75) and MaskGCT (5.25), comparable but slightly below DiTTo-TTS (6.25) and CLaM-TTS/HALL-E (6.40), primarily due to missing architectural ablations.

---

## Summary
DiSTAR introduces a zero-shot TTS framework that couples an autoregressive (AR) language model with discrete masked diffusion, operating entirely in the discrete RVQ code space. The AR model produces block-level conditioning sketches, and a bidirectional masked diffusion Transformer infills intra-block tokens in parallel using iterative demasking. The framework supports test-time controllability through RVQ layer pruning and multiple decoding strategies.

## Strengths
- **Clean architectural integration of AR sketching with discrete masked diffusion.** The design is coherent and well-specified: overlapping-patch aggregator, causal AR LM producing conditioning sketches, and bidirectional masked-diffusion Transformer for parallel intra-patch infilling — all in the same discrete RVQ space. Specific engineering choices (trainable scalar gate for conditioning stability, factorized embedding parameterization, embedding initialization from codec codebooks) are well-motivated and described in concrete detail (Sections 3.2–3.4).
- **Test-time bitrate/compute control via stochastic layer truncation.** Training with randomly dropped upper RVQ layers enables inference-time pruning without retraining. Figure 2 provides clean empirical validation: speaker similarity improves monotonically with more RVQ layers (0.58→0.64) while WER saturates around 6 layers (1.88%). This is a practical contribution with clear deployment implications.
- **Strong subjective evaluation results.** Table 2 shows DiSTAR leading all baselines on both SMOS (3.31 ± 0.25) and CMOS (0.22 ± 0.13) in human listening tests, outperforming CosyVoice 2, F5TTS, E2TTS, and FireRedTTS on both naturalness and speaker similarity. These results are independent of training-data concerns that affect the objective comparisons.
- **Identification and mitigation of tail-first bias in masked diffusion decoding.** The paper diagnoses a specific failure mode — overconfident predictions for later positions in temporally-structured masked diffusion — and proposes lightweight countermeasures (layer-wise and position-wise temperature shaping, hybrid sampling). Table 3 confirms these improve both WER (2.11→1.99) and speaker similarity (0.626→0.640).

## Weaknesses

### Fatal
None.

### Major
- **Missing architectural ablations for the core thesis.** Section 4.3 ("Ablation Study") tests only decoding hyperparameters (temperature shaping, greedy vs. sampling). None of the following architectural choices — which together constitute the paper's claimed contribution — are ablated: (a) contribution of the AR sketcher (what happens if the masked diffusion model operates without it?); (b) masked diffusion vs. a simpler intra-patch decoder; (c) overlapping vs. non-overlapping patches. The paper notes that patch size and CFG ablations are in appendices (lines 213–214), but these are not the critical ablations needed to validate that the AR + masked-diffusion coupling is responsible for the reported gains rather than other factors (data scale, codec quality, model capacity). This is the paper's most significant gap.
- **The DiTAR baseline comparison is confounded.** DiTAR's numbers are explicitly taken from its original paper (marked ♦ in Table 1), meaning DiTAR was trained on different data than DiSTAR. Additionally, DiTAR uses NFE=10 while DiSTAR uses NFE=24 — a significant compute difference. The abstract's claim of "inference cost close to its continuous counterpart DiTAR" (line 31) is unsubstantiated by any latency or FLOP measurement. While the other three baselines (IndexTTS, E2TTS, F5TTS-v1) lack ♦ markings and are consistent with the "All models are trained on Emilia" statement in Section 4.1, the DiTAR comparison — which is the most direct architectural predecessor — is not controlled.

### Minor
- **WER beating codec resynthesis and human baselines is not discussed.** DiSTAR-medium achieves lower WER than both RVQ resynthesized audio and human reference on both benchmarks (e.g., LibriSpeech: DiSTAR 1.66% vs. RVQ resynth 1.83% vs. Human 1.80%). While speaker similarity remains comparable (0.67 vs. 0.66), this phenomenon — a generative model producing more intelligible speech than the ground-truth signal — warrants explanation or characterization. The paper does not address it.
- **Decoding heuristics lack sensitivity analysis.** The three inference adjustments (T_layer=0.8, T_time=0.95, 50/50 hybrid sampling) are presented as fixed values without ablation over these specific hyperparameters. The paper acknowledges the hybrid schedule is "a hyperparameter" (line 146) but does not characterize sensitivity.
- **Different baseline sets in objective vs. subjective evaluations.** Table 1 (objective) includes IndexTTS and DiTAR but not FireRedTTS or CosyVoice 2; Table 2 (subjective) includes FireRedTTS and CosyVoice 2 but not IndexTTS or DiTAR. Only E2TTS and F5TTS appear in both tables, preventing cross-validation between objective metrics and human judgments for several baselines.
- **Subjective evaluation protocol details are sparse.** Table 2 reports standard errors but the paper does not specify the number of raters, their qualifications, or how samples were presented.
- **Diversity claims lack quantitative support.** The abstract claims "rich output diversity" and the decoding section discusses diversity-determinism trade-offs, but no diversity metric (e.g., variance of WavLM embeddings across multiple generations) is reported.

### Trivial
- The relationship between Eq. 1 (per-token AR factorization) and Eq. 2 (masked diffusion training objective) would benefit from an explicit note clarifying that Eq. 1 is the conceptual factorization that the patch-level model approximates.
- It is unclear whether the reported DiSTAR parameter counts (0.15B, 0.3B) include or exclude the ~0.3B parameter RVQ codec. If excluded, the total system parameter count changes the comparison against DiTAR (0.6B).

## Nice-to-Haves
- A direct ablation removing the AR sketcher (masked diffusion only, conditioned on text and prompt) would directly test the paper's central architectural claim.
- Latency, throughput, or FLOP measurements to support the "inference cost close to DiTAR" claim.
- A diversity metric to substantiate the abstract's diversity claim.
- Sensitivity analysis over the decoding heuristic hyperparameters (T_layer, T_time, hybrid split ratio).

## Removed Points
These points are flagged to be removed — treat with caution.

- **Harsh Critic CI #1: "All models are trained on Emilia" refers only to DiSTAR variants.** The literal text says "All models are trained on Emilia" (line 172) in the Datasets paragraph of Experimental Settings. The ♦ marking on DiTAR explicitly flags it as an exception. The three other baselines lack ♦, consistent with retraining. The critic's reading that this sentence describes only DiSTAR variants is not supported by the text.
- **Harsh Critic CI #1: NFE difference "undermines the entire evaluation."** The NFE difference (24 vs. 10) is real, but NFE counts mean different things for continuous diffusion vs. discrete masked diffusion. The DiTAR comparison is imperfect but not worthless. Retained as Major with appropriate caveats.
- **Harsh Critic CI #2: Beating codec resynthesis on WER is a "red flag" indicating the model is "not faithfully cloning."** The SIM scores are comparable (0.67 vs. 0.66), directly contradicting the claim that speaker characteristics are lost. The phenomenon is interesting and merits discussion but is not evidence of evaluation failure. Retained as Minor.
- **Harsh Critic CI #4: Decoding heuristics are "ad hoc patches" and were "tuned on the evaluation set."** The paper identifies a real phenomenon, explains its likely cause, and proposes mitigations. Temperature shaping and hybrid sampling are standard decoding techniques. The paper states the hybrid split is 50/50 "to avoid over-tuning" (line 146). No evidence of test-set tuning. The "ad hoc" framing is removed; the lack of sensitivity analysis is retained as Minor.
- **Strength Finder: "Greedy decoding that outperforms sampling on robustness."** Table 3 shows greedy+shaping (WER=1.91) beats baseline sampling (WER=2.11), but sampling+shaping (WER=1.99) nearly matches it. The claim overstates the finding but the underlying result is still useful.
- **Strength Finder: "Embedding initialization that bootstraps from the codec."** This is a practical implementation detail, not a contribution-level strength. Folded into the architectural integration strength.

## Novel Insights
The paper's observation of a "tail-first bias" in masked diffusion decoding over temporally-structured sequences — where later positions receive higher confidence because they can attend to more preceding context during non-autoregressive training — is genuinely interesting and not, to my knowledge, previously characterized in the TTS literature. While the paper treats it as a problem to be mitigated, the phenomenon itself may be a general property of masked diffusion over causal sequences and could motivate further study.

## Suggestions
- The strongest path to strengthening the paper is adding a minimal architectural ablation: train a DiSTAR variant without the AR sketcher (masked diffusion only, conditioned on text and prompt) and report the performance gap. This single experiment would directly validate or refute the core thesis.
- For the WER-vs-resynthesis phenomenon, add a brief discussion paragraph characterizing what the model is doing (e.g., producing more canonical pronunciations, reducing artifacts present in the original). This turns a potential weakness into an interesting finding.
- Report at minimum the number of raters and a brief description of the subjective evaluation protocol.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>