Now I have a clear calibration picture. Let me write the final review.

**Calibration bracket reasoning:**

- **Round 1 bracketing**: Weak anchors at ~3.0 (STFormer, etc.) are far below this paper; strong anchors at 7.5+ (Differential Transformer, etc.) are far above. Initial bracket: **5.0–6.5**.
- **Round 2 narrowing**: Compared against SDT-V2 (5.67, Accept-poster), LMUFormer (5.75, Accept-poster), DISTA (4.5, Reject), Zero Memory (5.75, Reject), S-TLLR (5.0, Reject). The paper is clearly stronger than DISTA and S-TLLR, comparable to SDT-V2 and LMUFormer. It has slightly less evaluation breadth than SDT-V2 but a more interesting core mechanism (neuron dynamics reformulation). **Final score: 5.5**.

---

# Consolidated Review

## Summary

This paper identifies two key limitations of Spiking Self-Attention (SSA) in spiking transformers — weak local modeling and high memory overhead — and proposes LRF-Dyn, a mechanism that (1) injects local receptive fields into SSA via dilated depth-wise convolutions to improve locality, and (2) reformulates the attention computation as charge–fire–reset neuronal dynamics to eliminate explicit storage of large attention matrices, reducing memory complexity from O(d²) to O(kd). Experiments on ImageNet classification (three architectures, two scales) show consistent accuracy gains of 0.4–1.24% at negligible parameter cost, and a 49.4% memory reduction is reported on Spikformer-8-512.

## Strengths

1. **Clear problem diagnosis grounded in empirical evidence.** Figure 2 provides a direct quantitative comparison of VSA vs. SSA attention distributions: VSA concentrates 76.68% of attention within Manhattan distance 5 (entropy H=0.1777), while SSA is nearly uniform (20.31% within distance 5, entropy H=0.5637). This empirical mismatch concretely motivates the need for improved local modeling and goes beyond prior work that merely notes a performance gap without isolating the cause.

2. **Consistent accuracy gains across multiple spiking transformer backbones.** Table 1 shows that both LRF-SSA and LRF-Dyn improve accuracy on Spikformer, QKFormer, and SDT-V3 at two model scales each (e.g., +1.24% on Spikformer-8-512, +0.48% on QKFormer-512, +0.92% on SDT-V3-S). The gains are modest but consistent, demonstrating broad architectural compatibility — no prior local-enhancement method for spiking transformers shows this level of cross-architecture generalization.

3. **Memory reduction via a principled neuronal-dynamics reformulation.** LRF-Dyn reformulates the attention KV-aggregation as a recurrent charge–fire–reset process, reducing inference-time memory complexity from O(d²) (storing the KV product matrix) to O(kd) (storing membrane potentials). The 49.4% memory reduction on Spikformer-8-512 (Fig. 5b) is a concrete efficiency improvement that simultaneously preserves or improves accuracy. This is a genuine advance over prior spiking transformers that require storing large QK or KV matrices.

4. **Ablation isolating the LRF contribution.** Table 3 systematically varies the number of LRF convolution kernels and shows monotonic accuracy improvement (from 77.86% w/o LRF to 78.64% with Ω≤5 for LRF-SSA), cleanly attributing the gains to the local receptive field module.

## Weaknesses

### Fatal
None.

### Major

1. **Parameter count in the segmentation table is anomalous.** In Table 2, the SDT-V3 + LRF-SSA large variant is listed at "10.0 + 1.4" = 11.4M backbone parameters, while the SDT-V3 baseline large variant has 18.99 + 1.4 = 20.39M. Meanwhile, Table 1 (ImageNet) consistently reports ~19.25M for the same LRF-SSA large variant. If correct, the 10.0M figure would make the segmentation comparison unfair (much smaller model vs. larger baseline). Most likely this is a typo/formatting artifact (should be 19.0), but as presented it undermines the credibility of the segmentation results. The authors must clarify this discrepancy in the rebuttal.

2. **Missing efficiency metrics beyond memory.** The paper claims efficiency benefits (motivated by edge deployment), yet reports no FLOPs, energy consumption estimates, or inference runtime. For an SNN paper whose contribution explicitly targets "high memory overhead during inference," the absence of any efficiency measurement beyond theoretical complexity and a single memory-usage bubble chart (Fig. 5b) weakens the practical claims. The comparison to other memory-efficient attention mechanisms (linear attention, Performers) is also absent from the experiments.

### Minor

1. **Theorems 1 and 2 are not effectively connected to the method.** The theorems assert specific functional forms (exponential decay for VSA, linear decay for SSA) and an entropy ordering, but these are presented as observations rather than derivations from the SSA/VSA mechanisms. The paper does not verify that the empirical distributions in Fig. 2 actually fit these parametric families (exp vs. piecewise-linear). The entropy ordering in Theorem 2 follows straightforwardly from the mixing in Eq. 9 and does not require a theorem. Since the paper's core claims are empirically supported, the theorems add little and risk over-claiming rigor.

2. **The "Causal SSA" baseline in Table 3 is not defined.** The ablation compares LRF-Dyn against "Causd SSA" (likely "Causal SSA") with a much lower accuracy (74.30% vs. 77.86% for standard SSA). The paper does not explain what this baseline is, how it was implemented, or why the gap is so large. Since LRF-Dyn is itself causal (Eq. 11), comparison against a causal variant is sensible, but the reader cannot assess whether the implementation is faithful.

3. **Eq. 15 (Fourier transform formulation) is introduced and never used again.** The mention of Fourier transforms in the overall architecture section (§5.3) appears without motivation and is not referenced in any experiment. This appears to be a dangling formulation that should either be connected to practice or removed.

4. **Memory reduction claim (49.4%) lacks a component breakdown.** The paper states this figure for Spikformer-8-512 but does not specify which memory components are included (attention matrix only vs. total inference memory including parameters, activations, etc.). A per-component breakdown would contextualize the improvement.

### Trivial
- "Causd SSA" in Table 3 is likely a typo for "Causal SSA."

## Nice-to-Haves
- Comparison against other memory-efficient attention mechanisms (linear attention variants such as Performer) in the SNN context would usefully contextualize the memory–accuracy trade-offs.
- Reporting training details (epochs, batch size, hardware) for the segmentation experiments would help reproducibility.
- A discussion of why LRF-Dyn's accuracy is sometimes slightly below LRF-SSA (e.g., 74.51% vs. 74.62% on Spikformer-8-512) would clarify the accuracy–memory trade-off.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that theoretical analysis proofs are "deferred to an appendix that is not available."** Per guidelines, missing appendix content is a parser artifact; the appendix exists in the original submission. The content-based criticism (that the theorems are not derived from first principles) is retained as Minor weakness #1.
- **Harsh critic's claim about the parameter-count discrepancy being "structural" and "compromised."** The discrepancy is real and flagged as Major weakness #1, but the severity characterization as "fatal" or "structural" is excessive given that Table 1 provides consistent parameter counts (~19.25M), suggesting a typo/formatting artifact. The criticism is demoted from Fatal to Major.
- **Strength Finder's generic strengths** (e.g., "This paper addressed an important problem") were removed.
- **Strength Finder's claim about segmentation "finer-grained outputs"** — while Fig. 4 shows qualitative results, the quantitative improvement (+2.2%) depends on the parameter discrepancy in Table 2, so this strength is partially contingent on resolution of the anomaly.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the Table 2 parameter discrepancy.** The 10.0M figure for the LRF-SSA large variant is inconsistent with the 19.25M reported in Table 1. If it is a typo, correct it; if the segmentation backbone differs from the classification backbone, explain the difference. A fair controlled comparison at matched model size would significantly strengthen the segmentation results.

2. **Add energy and runtime measurements.** Report FLOPs, estimated energy consumption (following standard SNN estimation protocols), and/or wall-clock inference time for at least one representative model scale. This would substantiate the efficiency claims and address a notable gap in the current evaluation.

3. **Remove or substantiate Theorems 1 and 2.** Either connect the theorems to derivations from the softmax vs. linear dot-product mechanism, or replace them with a simpler qualitative discussion. The empirical attention histograms (Fig. 2) already carry the argument effectively.

4. **Define the "Causal SSA" baseline clearly** in the ablation table, or re-run the comparison against a standard SSA causal variant with documented implementation details.

5. **Provide a memory-usage breakdown** for the 49.4% reduction claim, specifying which memory components are included.

## Score and Decision

**Calibration anchors across all rounds:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `/human_reviews/1SIBN5Xyw7.md` (Spike-driven Transformer V2) | 5.67 | R1/R2 | Similar domain and quality level. SDT-V2 has broader evaluation (4 tasks) but more incremental architecture. Our paper has a more interesting core mechanism (neuron dynamics reformulation) but evaluates on fewer tasks and has modest gains. **Comparable quality.** |
| `/human_reviews/mjDROBU93g.md` (DISTA) | 4.50 | R1 | Much weaker: CIFAR-only results, no ImageNet, trained for 1000 epochs. Our paper is clearly stronger. |
| `/human_reviews/Sf4ep9Udjf.md` (P-SPIKESSM) | 6.75 | R1/R2 | Stronger paper: more novel SSM+SNN combination, state-of-the-art results on long-range tasks. Our paper is less novel and has less impressive absolute results. **Our paper is weaker.** |
| `/human_reviews/XrunSYwoLr.md` (Spatio-Temporal Approximation) | 7.00 | R1/R2 | Stronger: first training-free SNN conversion for Transformers, solid theoretical guarantees. Our paper is less novel. |
| `/human_reviews/oEF7qExD9F.md` (LMUFormer) | 5.75 | R2 | Similar quality. LMUFormer has impressive efficiency results on speech tasks but more incremental design. **Comparable quality.** |
| `/human_reviews/yqIJoALgdD.md` (Zero Memory SNN Training) | 5.75 | R2 | Similar score but rejected due to presentation and evaluation issues. Our paper has clearer presentation and broader validation. |
| `/human_reviews/vlQ56aWJhl.md` (S-TLLR) | 5.00 | R2 | Weaker: rejected due to insufficient novelty validation and questionable claims. Our paper has clearer contributions. |
| `/human_reviews/wPK65O4pqS.md` (STFormer) | 3.00 | R1 | Far weaker: withdrawn/rejected. |
| `/human_reviews/OvoCm1gGhN.md` (Differential Transformer) | 8.00 | R1 | Far stronger: oral paper with clear mechanism and strong results. |

**Round-1 bracket**: 5.0–6.5 (between weak SNN anchors at ~3.0 and strong anchors at 7.5+).

**Narrowing**: The paper is comparable to accepted posters SDT-V2 (5.67) and LMUFormer (5.75), clearly better than rejected papers DISTA (4.5) and S-TLLR (5.0), but not as strong as P-SPIKESSM (6.75) or Spatio-Temporal Approximation (7.0). The core contribution (LRF + neuronal dynamics reformulation) is interesting and validated across multiple architectures, but the gains are modest, the evaluation lacks efficiency metrics, and there is an unresolved parameter count anomaly in Table 2. The paper sits at the boundary between marginal and strong accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>