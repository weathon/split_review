Now I have enough anchors. Let me write the final review.

## Anchors retrieved

**Round 1 (bracketing):**
- `j0sq9r3HFv.md` (avg 2.50, weak band): LLM-based parameter extraction for neuroscience — only tangentially related.
- `BBldjKEBlJ.md` (avg 3.00, weak band): QuantFormer — neural-activity quantization, off-topic.
- `vw0NurJ7UX.md` (avg 3.00, weak band): PrefixQuant itself — closer to the substrate this paper builds on.
- `6Mdvq0bPyG.md` (avg 3.00, weak band): EfficientQAT — LLM quantization, adjacent.
- `ZadnlOHsHv.md` (avg 7.00, strong band, accept): **SpikeLLM** — the most topically similar accepted SNN-LLM paper. Reviewers explicitly raised "are activation quantization >=4 really spiking?" and "no on-chip sparsity/energy validation" — same critiques as here, but SpikeLLM has broader scope (up to 70B), explicit outlier story, and tied numbers to spike-driven quantization.
- `u438df0Uce.md` (avg 3.60, middle band, reject): **SpikeZIP** — referenced architecture; rejected for incremental novelty and unclear evidence; structurally similar but on vision.
- `GTzP2GC7NR.md` (avg 5.75, middle band, reject): **When SNN meets ANN** — ANN-to-SNN conversion with error analysis; similar theory + bias-shift + neuron-modification recipe, on ImageNet, more energy-aware than the paper under review.
- `6c4gv0E9sF.md` (avg 6.33, middle band, reject): SpikeBERT — direct-training SNN for language.
- `TopoLM.md`, `eW4yh6HKz4.md`, `TJo6aQb7mK.md`, `wg1PCg3CUP.md` (strong band): off-topic LLM quantization/topography papers.

**Round 1 bracket:** between 3.5 and 6.0 (closer in spirit to SpikeZIP/When-SNN-meets-ANN than to SpikeLLM).

**Round 2 (narrowing):**
- `u438df0Uce.md` (3.60): re-surfaced.
- `mtmqwhQiaG.md` (5.25, reject): Canonic Signed Spike — novel coding scheme but no LLM, similar incremental story.
- `JAnyCnK5In.md` (4.75, reject): Online SNN training.
- `mJ4mgYjDru.md` (4.60, reject): Discretized QIF neuron.
- `GTzP2GC7NR.md` (5.75): re-surfaced.
- `D4sQzdMvcG.md` (5.75, reject): **QAC: Quantization-Aware Conversion for Mixed-Timestep SNNs** — very close in conceptual setup, also rejected at 5.75.
- `OPSpdc25IZ.md` (6.00, accept): DS-LLM — orthogonal, less comparable.
- `lGUyAuuTYZ.md` (5.67, accept): BNN+SNN hybrid for CV.

Compared to QAC (5.75) and When-SNN-meets-ANN (5.75): both rejected SNN-conversion papers with stronger theory and broader vision-domain evaluations than the paper under review. The paper under review applies similar ideas to LLMs (a plus, scope-wise), but its evaluation undermines its own framing: T=1 is numerically identical to PrefixQuant and T>1 monotonically degrades, with no energy/sparsity measurement to recover the spiking story. That is materially worse on the "the contribution does what it claims" axis than QAC or When-SNN-meets-ANN.

Compared to SpikeZIP (3.60): SpikeZIP was rejected for similar "framing doesn't fully pay rent + incremental novelty" concerns on the vision side. The paper under review has cleaner calibration evidence (Table 4) but a sharper framing mismatch.

**Final bracket:** between 3.5 and 5.0, leaning ~4.0.

---

## Summary

The paper proposes a training-free "dual" ANN-to-SNN conversion pipeline for LLMs: start from a statically quantized LLM (PrefixQuant), replace the quantizer with an Integer Spiking (IS) neuron — a bias-shifted Multi-Hierarchical-Threshold neuron — such that, when $LT=2^n-1$, the summed spike output equals the quantization output, then learn only thresholds and initial membrane potentials per layer via a calibration objective derived from a layer-wise error bound (Theorem 3). Experiments are on LLaMA-2-7B and LLaMA-3-8B at W6A6 with $T\in\{1,2,4,8\}$.

## Strengths

- **Parameter-efficient calibration with strong recovery.** Table 4 shows threshold + $v(0)$ calibration (0.107K params/layer) achieves higher Avg. Acc. than full-weight calibration (202M params) on LLaMA-2-7B (67.65 vs 66.39) at $T=2$. Table 2 also shows uncalibrated SNNs collapse (LLaMA-3-8B $T=2$: 48.83 Acc, 29.97 PPL) and calibration recovers to 69.03/9.07 — close to the W6A6 quantized baseline (70.24/6.90). This is a genuine, well-supported result.
- **Training-free pipeline avoiding the conversion-friendly ANN bottleneck.** Section 3.2 / Figure 1(b): unlike conventional conversion that retrains a QCFS/ReLU-only ANN, this pipeline reuses PrefixQuant directly, which is a sensible scalability argument for LLM-scale conversion.
- **Robustness to learnable-parameter size.** Table 3: varying activation group size from 1 to 256 changes Avg. Acc. by under 2 points on LLaMA-2-7B at $T=2$, indicating the calibration is not finicky.

## Weaknesses

### Fatal
None — the framing/efficiency mismatch is severe but does not invalidate the calibration result; see Major.

### Major

- **The "spiking" framing is not supported by the results.** Theorem 2 / Remark 1 establish that when $LT=2^n-1$, the IS neuron at $T=1$ literally computes the quantization function, and Table 2's "Conversion, W6A6, T=1" row is digit-for-digit identical to PrefixQuant on both LLaMA-2-7B (70.17 / 75.70 / 45.99 / 74.41 / 77.26 / 5.76) and LLaMA-3-8B (71.11 / 78.04 / 48.32 / 75.13 / 77.64 / 6.90). The only regime in which the model is meaningfully spiking is $T>1$, but on every metric performance degrades monotonically with $T$ (LLaMA-2-7B PPL: 5.61 → 7.39 → 9.71 → 12.03; Avg. Acc.: 68.79 → 67.65 → 67.04 → 66.03). The paper's stated motivation in §1 and Contribution 3 — energy-efficient LLM deployment via SNNs — therefore goes unverified: there is no metric in the paper for which $T>1$ outperforms $T=1$.

- **No energy, sparsity, latency, or operation-count measurement.** The contributions specifically promise "potentially reduces the energy consumption of LLMs" (Contribution 3) and Section 1 frames the work around edge deployment, yet the paper reports no estimate of synaptic-operation counts, accumulate-only vs MAC ratios, activation sparsity, or neuromorphic-hardware latency. Without these, the paper's only supported quantitative claim is "approximately PrefixQuant-level accuracy at $T=1$, worse at $T>1$" — which is functionally a calibration-method claim, not a spiking-LLM claim. This is the headline metric for SNN papers and its absence is central, not peripheral.

- **Narrow experimental scope (single bit-width).** §4.1 explicitly fixes W6A6 across all experiments and Tables 2–4. The natural axis along which a quantization-emulating spiking neuron should earn its keep is lower precision (W4A4, W4A8, W3A8), where the IS neuron's multi-hierarchical thresholding would have more headroom to outperform plain static quantization. The current experimental setup forecloses the exact regime where the contribution would be most useful, and means the paper's "comparable to SOTA quantization" claim is established only at a precision where PrefixQuant already loses very little to FP16 (5.76 vs 5.47 PPL on LLaMA-2-7B).

- **Likely transcription / configuration problem in the DuQuant baseline.** In Table 2, DuQuant's row is identical across LLaMA-2-7B and LLaMA-3-8B (67.88 / 72.64 / 40.53 / 53.07 / 77.15 / 62.25 for the five accuracy columns), differing only in PPL (5.53 vs 6.27). That is implausible — two different models cannot produce the same five accuracy numbers under any normal evaluation. The ArcE = 53.07 figure for DuQuant is also dramatically below the ~74 of every other method in the table. Since DuQuant is one of only two quantization baselines, this materially affects the comparison's credibility and needs to be re-run.

### Minor

- **The IS neuron is acknowledged to be a minor variant of M-HT.** §3.2.2 explicitly attributes the neuron to Sun et al. 2022 / Wang & Zhang 2023 / Li & Zeng 2022 / Hao et al. 2024 and calls it "modified". The only modification visible in Eq. 8–10 is the additive bias $\alpha^k(t)\theta^k$ that allows negative-activation representation. Framing this as a core technical contribution is overstated; the genuine novelty is the pairing with PrefixQuant and the threshold/$v(0)$ calibration.

- **Theorem 3 does not constrain the design.** The bound multiplies $\prod_{\tau=k+1}^{K}\rho^\tau$ over 32 LLaMA blocks containing softmax, SiLU, RMSNorm, and activation-activation multiplications — Lipschitz constants for these blocks are large and input-dependent, and no empirical estimate of $\rho^k$ is provided. Remark 3 claims the theorem motivates calibration, but minimizing a single per-layer term inside a product of large constants does not, on its own, justify that the global error shrinks proportionally. The calibration objective is reasonable on its own terms; the theorem is decorative rather than load-bearing.

- **Unevenness-error narrative is asserted but not isolated.** §3.3 and Figure 3 describe unevenness error as the dominant degradation source at $T>1$, but Figure 3 compares ANN-vs-QANN MSE against ANN-vs-SNN MSE — not a clean decomposition into clipping, quantization, and unevenness error before and after calibration. The claim that calibration specifically targets unevenness error (vs. simply reducing whatever total SNN-vs-QANN gap exists) is not directly demonstrated.

- **Comparison framing in Table 4 understates the PPL gap.** §4.4 calls weight-calibration "comparable performance" to threshold-only calibration, but the weight baseline achieves PPL 6.37 on LLaMA-2-7B vs. 7.39 for the proposed method — a meaningful PPL gap that the text glosses over. The text emphasizes parameter count (0.107K vs 202.375M) but should at least acknowledge the PPL trade-off honestly.

### Trivial

- Table 2's row organization mixes LLaMA-2-7B and LLaMA-3-8B awkwardly — the LLaMA-2-7B "Conversion, W6A6, T=8" row sits adjacent to and is visually grouped with LLaMA-3-8B's "Baseline FP16" row, making the table harder to parse than necessary.

## Nice-to-Haves

- An empirical breakdown of clipping vs quantization vs unevenness error per layer, before and after calibration, on the same axis — this would directly substantiate the diagnostic claim in §3.3 and Remark 3.
- Sweep bit-widths (W4A4, W4A8, W3A8) to show where calibration's value grows.
- At least one direct comparison against a published SNN-conversion baseline at LLM scale, even if smaller-scale (the paper invokes SpikeZIP as the architectural source for spiking nonlinearities but does not compare against it numerically).
- Demonstrate one setting in which $T>1$ is preferable to $T=1$ (e.g., activation sparsity that maps to operation-count reduction on a sparse accumulator, or a low-bit equivalent precision $n$ achievable only with $T>1$).
- Report variance across seeds — at $T=1$, the gap between the proposed method and PrefixQuant on average accuracy is ~0.1 points (68.79 vs 68.70), which is plausibly within noise.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"SpikeZIP comparison is conspicuously missing" (harsh critic).** The paper does cite SpikeZIP and explicitly attributes its spiking-compatible non-linearities to You et al. 2024, but adding it as a numerical baseline would be a nice-to-have rather than a fatal omission — I've moved this to Nice-to-Have rather than keeping it as a Major weakness.
- **"Calibration recipe is too thin to be reproducible" (harsh critic, §3.4).** The paper states what is optimized ($\theta^k$, $v^k(0)$) and the calibration target. Specific optimizer/steps/sample-count details are reasonably appendix-grade and may have been stripped during parsing; not promoted.
- **"Abstract overclaims comparable performance" (harsh critic).** This is a real but minor framing issue — abstract phrasing is fixable in revision and has already been substantively captured in the Major "framing not supported" weakness; not duplicated as a separate criticism.
- **"Theorem 2 holds only when $LT = 2^n - 1$ which rarely holds" (harsh critic).** The paper itself flags this exactly (Remark 1) and proposes a practical setting $\alpha^k(t)=2^{n-j-1}$, $L=\lceil 2^{n-1}/T\rceil$ that gives approximate equivalence; the gap is what motivates the calibration step. This is candid disclosure rather than a flaw.
- **"Strength: theoretical analysis bounds conversion error" (strength finder).** Theorem 3's bound is too loose to constrain the design (32 LLaMA layers, large Lipschitz constants); the strength is downgraded in favor of the Minor weakness above.

## Novel Insights

None beyond the paper's own contributions. The calibration-of-thresholds-only result (Table 4) is a genuinely interesting parameter-efficiency observation: that adjusting ~100 scalar parameters per layer can recover most of a 200M-parameter weight calibration's accuracy at $T=2$. This is worth highlighting independently of the spiking framing.

## Suggestions

1. Reframe the paper around what the evidence supports: a parameter-efficient calibration method for low-bit statically quantized LLMs, with a spiking-compatible neuron formulation that incidentally admits an SNN implementation. The current "spiking LLM" framing is a hostage to the energy/sparsity story the paper does not deliver.
2. Add an energy/operation-count analysis — even a back-of-envelope synaptic-operation count under a sparse-accumulator assumption — to give $T>1$ a reason to exist within the paper.
3. Re-run the DuQuant baseline in Table 2; the LLaMA-2-7B and LLaMA-3-8B rows being identical accuracy-wise is almost certainly an error.
4. Add at least one lower-bit-width experiment (W4A4) to show the regime where the IS-neuron-as-quantizer formulation has more leverage than at W6A6.
5. Decompose conversion error empirically into clipping / quantization / unevenness components, before and after calibration, to substantiate the §3.3 diagnostic claim and tie the calibration target to the dominant error source.

---

**Axis-by-axis assessment.** *Originality:* Moderate — the IS neuron is acknowledged as a M-HT variant; the genuine novelty is the dual-pipeline framing + threshold-only calibration. *Importance:* Real — efficient LLM deployment is a meaningful problem. *Claim support:* The calibration claim is well-supported (Tables 2–4); the spiking-energy claim is not supported at all. *Soundness of experiments:* Limited — single bit-width, two models, no efficiency metric, a likely-erroneous DuQuant row. *Clarity of writing:* Generally clear; Table 2 organization is a stumble. *Value to community:* The calibration result is genuinely useful for the SNN-conversion sub-community; the broader spiking-LLM contribution is more aspirational than demonstrated.

## Score and Decision

Final placement: noticeably weaker than QAC and When-SNN-meets-ANN (both rejected at 5.75) because those papers' core claims were supported by their experiments, whereas this paper's central "spiking LLM" framing is contradicted by Table 2. Stronger than SpikeZIP (3.60) on calibration evidence and presentation. Lands at **4.0**.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>