Now I have enough calibration. Let me write the consolidated review.

**Bracket from Round 1:** The paper sits between the weak anchors (1.5–3.0, papers with no ImageNet results or major presentation flaws) and the strong anchors (7.6–8.0, top-tier theory/empirical contributions). The most relevant band is the middle band (3.5–7.5), where spiking transformer papers with varying soundness issues cluster.

**Narrowing from Round 2:** DISTA (4.50) is the closest anchor — it similarly proposes a spiking transformer attention mechanism with methodological gaps and no memory/energy measurements, but the current paper has stronger experiments (ImageNet results, multiple architectures). The Spike-driven Transformer V2 (5.67) had cleaner claims and more complete evaluation but was deemed incremental. SAF (4.00) had sounder theory but much weaker experiments. Comparing directly: this paper does better than SAF (4.00) and DISTA (4.50) on experimental breadth, but worse than Spike-driven Transformer V2 (5.67) on soundness and clarity of claims.

**Final Score:** 4.5 — the paper has plausible ideas and some real empirical support, but is undermined by overstated theoretical claims, an unacknowledged design shift (bidirectional → causal), absent memory measurements, and a parameter table inconsistency.

---

## Summary

This paper identifies two problems in spiking transformers — the limited locality of spiking self-attention (SSA) and its memory overhead — and proposes two modifications: LRF-SSA, which adds dilated depthwise convolutions to SSA to encourage local attention, and LRF-Dyn, which reformulates attention through neuronal charge-fire-reset dynamics to eliminate explicit attention-matrix storage. Experiments on ImageNet-1k and ADE20K show consistent accuracy improvements over SSA baselines across three spiking transformer architectures.

## Strengths

- **Consistent accuracy gains across multiple spiking transformer backbones on ImageNet.** Table 1 shows LRF-SSA and LRF-Dyn improve accuracy on Spikformer (+1.24% / +1.13%), QKFormer (+0.48% / +0.44%), and SDT-V3 (+0.92% / +0.82%) with negligible parameter increases (<0.2M). This demonstrates robustness of the core idea across different architectures.

- **Generalization to semantic segmentation.** Table 2 on ADE20K shows LRF-SSA and LRF-Dyn improve MIoU by 2.6% and 2.2% respectively over the SDT-V3 baseline, confirming the benefits extend beyond image classification to dense-prediction tasks.

- **Ablation isolating the role of the LRF module.** Table 3 on CIFAR-100 systematically varies the kernel count from "w/o LRF" to Ω≤5, and accuracy improves monotonically (77.86% → 78.64% for LRF-SSA), supporting the claim that the local receptive field operation drives the gains.

- **Qualitative receptive-field visualization.** Figure 5(a) presents effective-receptive-field heatmaps showing that both LRF-SSA and LRF-Dyn concentrate attention locally, resembling VSA patterns rather than the diffuse SSA patterns.

## Weaknesses

### Major

- **Theorems 1 and 2 are not valid mathematical results and should not be presented as such.** The paper states that VSA attention weights are proportional to exp(−βΔ) (Δ = Manhattan distance) and SSA weights to (α−βΔ)₊. These are empirical observations about the *tendency* of nearby tokens to have higher similarity, dressed up in theorem notation. VSA weights depend on learned query–key dot products, not solely on spatial distance, and the claimed exponential/linear forms are not derivable from the attention mechanism itself. The phrase "Theorems" overstates what is actually a heuristic characterization. These should be presented as empirical observations (as Figure 2 already does) without claiming formal theorem status. The proof references to Appendices C/D cannot salvage a premise that is not generally true.

- **LRF-Dyn replaces bidirectional self-attention with causal sequential processing without adequate justification or comparison.** Equation (11) sums over j = 1 to n−1, indexing tokens in order and accumulating only past tokens. This is a causal (unidirectional) attention mechanism, whereas standard self-attention in vision transformers is bidirectional. The ablation in Table 3 shows that "Causal SSA" (without LRF) drops from 77.86% to 74.30% on CIFAR-100 — a 3.56% loss. While LRF-Dyn partially recovers this (77.78% → 78.57% with LRF), there is no comparison against a non-causal version of the same neuronal-dynamics formulation. Consequently, it is unclear whether the gains come from the LRF module or from properties of the dynamics that happen to compensate for the causal restriction. The paper must either justify why causal attention is appropriate for vision tasks or compare against a non-causal variant.

- **The claimed memory reduction (49.4%) is not backed by empirical measurements.** The paper reports only theoretical storage complexity (O(d²) for SSA vs. O(kd) for LRF-Dyn) and a single sentence claiming 49.4% reduction for Spikformer-8-512. No actual peak GPU memory, inference-time footprint, or memory vs. sequence-length curves are reported. Figure 5(b) is described as comparing "memory usage, accuracy, and parameter efficiency" but the axes show Accuracy vs. Parameters, not memory. Without measured memory numbers, a central contribution of the paper is unsubstantiated.

- **The derivation linking LRF-SSA to LRF-Dyn is asserted, not derived.** The paper states that LRF-SSA (Eq. 8) "can be approximated" by the neuronal dynamics in Eq. (12), but never shows a formal equivalence or a bound on the approximation error. The terms 𝒜, Γ, Xₙ are defined ad hoc, the tridiagonal coupling matrix in Eq. (13) is not explained in terms of the attention computation, and the Fourier transform description in Eq. (15) appears without derivation. Without a clear guarantee connecting the dynamics to the original attention formulation, LRF-Dyn is effectively a new architecture rather than a memory-efficient implementation of LRF-SSA.

### Minor

- **The segmentation table (Table 2) contains a suspicious parameter entry.** The baseline SDT-V3 large model has 18.99M parameters, but the LRF-SSA large variant is listed with only 10.0M — less than the baseline, contradicting the claim that LRF-SSA adds parameters. The LRF-Dyn variant correctly shows 19.25M. This is likely a formatting/transcription error, but it undermines confidence in the table's accuracy.

- **The contribution of the LRF module is not isolated from added capacity.** LRF-SSA adds two dilated depthwise convolutions with batch normalization and a non-linearity. These could improve performance simply by adding model capacity, independently of the claimed "local receptive field" effect. The paper does not compare against SSA with equivalent extra parameters allocated elsewhere (e.g., additional linear layers or wider projections).

- **No statistical significance or variance reported.** All results appear to be single-run without standard deviations or confidence intervals, making it impossible to assess whether the reported gains (often <1%) are reliable.

### Trivial

- The notation in Equation (8) is ambiguous — 𝐕ʲᵏ is not defined before use.
- Some design choices (kernel size 3×3, dilation factors 3 and 5, number of dendrites n=8) are stated without ablation or citation.

## Nice-to-Haves

- Report actual GPU memory measurements (peak memory, inference footprint) for both SSA and LRF-Dyn across multiple sequence lengths.
- Provide an ablation controlling for added capacity: compare LRF-SSA against SSA with extra parameters allocated as additional linear layers.
- Add an experiment comparing LRF-Dyn against a non-causal variant of the same design (e.g., unrestricted KV accumulation).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Missing comparison with other efficient attention mechanisms (sliding-window, local attention)."* — The paper's scope is spiking transformers specifically; requesting comparisons with every linear-attention variant from the ANN literature is scope creep.
- *"Missing FLOPs/energy estimates."* — Welcome but not standard for a method paper focused on accuracy and memory.
- *"Missing related works"* — Cannot be externally verified; removed per policy.
- *"The attention-distribution histograms conflate removal of softmax with binarization."* — The paper's attribution to softmax removal is reasonable as a first-order analysis, and Figure 2 provides empirical grounding.
- *"Hyperparameter justification"* — Not every architectural choice needs independent ablation; the paper provides ablations for the key parameter (kernel count).
- *Strength about theoretical analysis* — Removed because the theorems are not valid as presented.
- *Strength about biological motivation* — Generic framing, not a specific evidence-backed strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Remove the "Theorem" framing** and present the distance-attention analysis as empirical observations (backed by Figure 2), not as formal results.
2. **Acknowledge and discuss the causal nature of LRF-Dyn** explicitly — state whether it is intended to be causal, justify why this is acceptable for vision tasks, and compare against a non-causal version.
3. **Measure and report actual GPU memory** (at least peak inference memory for one architecture at multiple resolutions) to substantiate the memory-reduction claim.
4. **Fix the segmentation table** — the 10.0M parameter entry for LRF-SSA large appears to be an error and should be corrected with an explanation.
5. **Add a control experiment** where SSA is augmented with the same number of additional FLOPs/parameters as LRF-SSA, to disentangle the locality benefit from the capacity benefit.

## Score and Decision

The paper addresses a real problem and shows consistent improvements across multiple architectures and tasks. However, the theoretical framing is overstated (Theorems 1–2 are not valid formal results), a fundamental design change (bidirectional → causal attention) is introduced without justification or proper controls, the central memory-reduction claim lacks empirical measurement, and the segmentation table contains a parameter inconsistency. These issues collectively mean the contribution does not hold up in its current form.

**Score: 4.5** — Below the acceptance threshold. A substantially revised version that removes the theorem overclaims, acknowledges and controls for the causal attention shift, reports actual memory numbers, and fixes the table inconsistency could be a strong candidate for resubmission.

**Decision: Reject**

---

### Calibration Anchors

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| BBldjKEBlJ | 3.00 | 1 (weak) | QuantFormer — a rejected paper with limited scope; this paper is stronger |
| N581Nje6fH | 1.50 | 1 (weak) | Long Horizon Decision Making — clearly weaker; poor experiments |
| qPwQj4Mf3u | 3.00 | 1 (weak) | Hopfield Encoding Networks — comparable rejection-tier quality |
| 4ymHtDAlBv | 2.33 | 1 (weak) | FSFC RNN — weaker methodology and experiments |
| qzZsz6MuEq | 6.60 | 1 (mid) | Spiking Vision Transformer with Saccadic Attention — stronger evaluation and cleaner claims; this paper is notably weaker |
| XrunSYwoLr | 7.00 | 1 (mid) | Spatio-Temporal Approximation (SNN conversion) — stronger theoretical grounding |
| 1SIBN5Xyw7 | 5.67 | 1 (mid) | Spike-driven Transformer V2 — cleaner contribution and more complete evaluation; this paper is worse on soundness |
| CwAY8b8i97 | 4.00 | 1 (mid) | SAF — sounder theory but much weaker experiments; comparable overall quality |
| Tzh6xAJSll | 7.60 | 1 (strong) | Scaling Laws for Associative Memories — far stronger theoretically |
| OvoCm1gGhN | 8.00 | 1 (strong) | Differential Transformer — stronger architecture with rigorous eval |
| aWXnKanInf | 8.00 | 1 (strong) | TopoLM — stronger on all dimensions |
| STUGfUz8ob | 7.60 | 1 (strong) | When can transformers reason — rigorous theory; not comparable domain |
| mjDROBU93g | 4.50 | 2 (narrow) | DISTA — similar tier with complementary weaknesses; this paper has better experimental breadth but worse theoretical soundness |
| PWtx9fJqM5 | 5.00 | 2 (narrow) | Linear Transformations in Attention — cleaner analysis but narrower scope |
| hpZ5zpudH8 | 4.20 | 2 (narrow) | SpikSSD — lower experimental strength |

**Round 1 bracket:** 3.5 – 6.0. **Round 2 narrowing:** 4.0 – 5.0, anchored best by DISTA (4.50). The paper is slightly above DISTA on experimental breadth (ImageNet results) but below on presentation clarity and claim accuracy, placing it at **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>