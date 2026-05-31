## Summary

DiSTAR is a zero-shot text-to-speech framework that couples an autoregressive (AR) Transformer with a masked discrete diffusion model operating entirely in a Residual Vector Quantization (RVQ) code space. Unlike prior continuous-latent AR+diffusion approaches (e.g., DiTAR), DiSTAR drafts coarse patch-level summaries autoregressively then refines within-patch RVQ tokens in parallel via LLaDA-style masked diffusion, achieving blockwise parallelism while jointly modeling RVQ time-depth dependencies. Additional contributions include stochastic layer truncation for test-time compute/bitrate control, RVQ-aware temperature shaping, and a hybrid greedy-sample decoding strategy that improves stability.

---

## Strengths

- **Novel and well-motivated architecture:** DiSTAR is, to the reviewer's knowledge, the first system to combine AR sketching with masked discrete diffusion operating end-to-end in an RVQ code space for TTS. The design choice is clearly motivated by the known failure modes of continuous-latent diffusion (optimization instability, domain sensitivity) and single-codebook AR (exposure bias, depth-ignorance). The formalism in Section 3 is clean and the key equations (2, 3) follow from first principles.

- **Strong empirical robustness:** DiSTAR-medium (0.3B) achieves the lowest WER on both evaluated benchmarks—1.66% on LibriSpeech-PC and 1.32% on SeedTTS-en—outperforming DiTAR (0.6B, 2× larger) at 2.39%/1.78%, F5TTS at 2.02%/1.35%, IndexTTS at 2.57%/1.92%, and E2TTS at 2.74%/2.20%. This represents a meaningful and consistent advantage on a concrete measure of synthesis robustness.

- **Impressive subjective results:** DiSTAR achieves CMOS of +0.22 and SMOS of 3.31±0.25 on SeedTTS-en, outperforming CosyVoice 2, E2TTS, F5TTS, and FireRedTTS by non-trivial margins (CosyVoice 2 CMOS −0.04; F5TTS CMOS +0.01). Beating human reference on CMOS in a wild-corpus benchmark, while also winning SMOS, is a notable result.

- **Practical test-time controllability:** Stochastic layer truncation during training enables variable-bitrate and variable-compute inference without any retraining. Figure 2 shows monotone improvement in speaker similarity as more RVQ layers are used (0.58→0.64), while WER is largely insensitive to depth beyond six layers—an interpretable trade-off curve.

- **Parameter efficiency:** DiSTAR-medium (0.3B) achieves better WER than DiTAR (0.6B) and is parameter-competitive with F5TTS (0.3B), demonstrating that discrete representations do not sacrifice efficiency.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **No inference speed or real-time factor (RTF) comparison.** A central claim of DiSTAR is blockwise parallelism that reduces latency relative to fully-AR systems. Section 4.4 discusses compute in terms of RVQ layers used but never reports wall-clock RTF or latency figures. DiSTAR uses NFE=24 versus DiTAR's NFE=10—a 2.4× increase in diffusion steps—raising a legitimate concern about whether net latency is actually competitive. Without RTF numbers the efficiency narrative is unsupported.

2. **No direct ablation between discrete and continuous representations.** The core contribution over DiTAR is operating in discrete rather than continuous latent space. The paper argues that discrete space avoids optimization instability and domain sensitivity, but offers no controlled ablation (same architecture, same data, same codec bitrate) comparing discrete vs. continuous RVQ to verify this claim empirically. Cross-system differences in codec, training data subsets, and model size conflate representation choice with other variables.

3. **Speaker similarity not state-of-the-art.** E2TTS leads on SIM in both benchmarks (0.70/0.71 vs. DiSTAR-medium's 0.67/0.66), and F5TTS is competitive (0.68/0.68). The paper asserts "SIM on par with the best alternatives," but 0.67 vs. 0.70 is a 3-point gap that is attributable to the discrete bottleneck. The paper credits the advantage to "reduced sensitivity to high-frequency artifacts," but this hypothesis is not tested.

### Minor

1. **Codec parameters excluded from model count.** The codec (MAGICODEC-derived, ~0.3B) is not counted in the 0.15B/0.3B parameter totals, while it is unclear whether competing systems' codecs are also excluded. This makes the parameter count comparison potentially misleading.

2. **Subjective and objective baselines differ.** Table 2 (subjective) includes CosyVoice 2 and FireRedTTS but not DiTAR—the most natural continuous-latent counterpart. Table 1 includes DiTAR but not CosyVoice 2. Ideally the same baselines would appear in both tables, especially since DiTAR is the direct comparison.

3. **UTMOS is not best.** DiSTAR never wins UTMOS (IndexTTS leads on LibriSpeech at 4.35 vs. 4.27; DiTAR leads on SeedTTS at 4.15 vs. 4.05). The paper does not discuss this divergence between subjective CMOS and objective UTMOS.

4. **Tail-first bias explanation is speculative.** The paper attributes this decoding artifact to non-autoregressive training making later positions easier but provides no ablation confirming this. The same heuristics (temperature shaping, hybrid decoding) are presented without ablating each individually.

### Trivial
None.

---

## Nice-to-Haves

- An RTF comparison table (DiSTAR-base, DiSTAR-medium, DiTAR, F5TTS) under matched hardware would substantially strengthen the efficiency claim.
- An ablation of each decoding trick (layer temperature, position temperature, hybrid sampling) independently to clarify their individual contributions.
- A controlled comparison swapping only the representation (discrete vs. continuous) within the DiSTAR architecture, holding codec rate, model size, and training data fixed.

---

## Novel Insights

DiSTAR makes the non-obvious observation that masked discrete diffusion (LLaDA-style) applied at the intra-patch level in RVQ space can resolve the depth-axis dependencies of multi-codebook codecs in a single bidirectional Transformer pass, without the optimization difficulties associated with continuous-latent diffusion. The stochastic layer truncation trick—uniformly randomizing how many RVQ tiers are visible during training—elegantly converts a fixed-topology discrete model into a variable-compute system at no retraining cost. The empirical finding that upper RVQ layers primarily encode acoustic detail (speaker timbre) rather than linguistic content, evidenced by WER bottoming out around 6 layers while SIM continues improving to 9 layers, is a clean and interpretable result that may generalize to other codec-based TTS systems.

---

## Suggestions

- Report RTF (or tokens/sec) for each model size alongside NFE count, and compare with DiTAR and F5TTS under the same hardware.
- Add a single-row ablation removing discrete representation (replacing with continuous latents under the same patch-AR + diffusion architecture) to isolate the contribution of the RVQ discrete space.
- Include DiTAR in the subjective evaluation table for a fair head-to-head comparison of the two paradigms.
- Ablate each decoding heuristic independently in Table 3 to clarify which tricks actually matter.

---

## Score and Decision

DiSTAR is a well-executed work that achieves state-of-the-art synthesis robustness and strong naturalness on two standard benchmarks. The architecture is genuinely novel for the TTS domain, the motivation is clear, and the results—especially WER and CMOS—are convincing. The primary gaps are the missing RTF comparison (efficiency claim unverified), absence of a controlled ablation on the discrete vs. continuous design axis, and the persistent speaker similarity deficit relative to E2TTS. These are meaningful but not fatal; the submission represents a solid contribution to the zero-shot TTS community.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>