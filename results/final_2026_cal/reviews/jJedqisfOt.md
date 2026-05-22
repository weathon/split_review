Now I have a comprehensive calibration picture. Let me produce the final review.

---

## Summary

This paper identifies two problems in Spiking Self-Attention (SSA) for SNN-based transformers: (1) SSA lacks locality bias compared to VSA, causing a performance gap, and (2) SSA incurs high memory overhead from storing attention matrices. It proposes LRF-SSA, which adds two dilated depthwise convolutions to SSA to inject local bias, and LRF-Dyn, which reformulates attention as a causal recurrent update inspired by neuronal dynamics to eliminate explicit attention-matrix storage. Experiments on ImageNet classification and ADE20K segmentation show consistent accuracy gains (+0.4% to +1.24% on ImageNet, +2.2% to +2.6% MIoU on ADE20K) with minimal parameter overhead, and LRF-Dyn reduces storage complexity from O(d²) to O(kd).

## Strengths

- **Well-motivated problem with quantitative diagnosis.** Section 4.1 and Figure 2 provide concrete evidence: only 20.31% of SSA's attention mass falls within Manhattan distance <5 (vs. 76.68% for VSA), and SSA's attention entropy is H=0.5637 vs. VSA's H=0.1777. This directly quantifies the locality deficit that motivates the paper.

- **Consistent accuracy gains across three architectures and two tasks.** Table 1 shows LRF-SSA improves accuracy on Spikformer (+1.24%), QKFormer (+0.44-0.48%), and SDT-V3 (+0.51-0.92%) on ImageNet with <0.2M extra parameters. These gains extend to ADE20K semantic segmentation (+2.2-2.6% MIoU in Table 2), a more challenging dense prediction task where the locality bias matters more.

- **Memory reduction through recurrent reformulation.** LRF-Dyn reduces storage complexity from O(d²) to O(kd) (k=8 dendrites). The paper reports 49.4% memory reduction for Spikformer-8-512 while maintaining accuracy (+1.13%), addressing a real deployment bottleneck for SNN transformers that prior work did not tackle.

## Weaknesses

### Major

1. **Causal sequential bias of LRF-Dyn is unexamined.** Equation 11 reformulates attention as a causal update — token n only attends to tokens 1 through n-1, imposing an arbitrary raster-scan ordering on 2D spatial positions. The paper does not discuss whether this breaks translation equivariance, test different orderings, or analyze when/why the causal bottleneck matters. Table 3 provides critical evidence: naively forcing SSA to be causal (Causal SSA) drops CIFAR-100 accuracy from 77.86% to 74.30% (−3.56%), yet LRF-Dyn (also causal) reaches 78.57%. The paper presents this result without explaining *how* LRF-Dyn's specific recurrent formulation (Eqs. 12-13) overcomes the causal information loss, or acknowledging the ordering dependence as a limitation. Understanding this recovery mechanism is essential for trusting the method in other settings.

2. **Theoretical analysis (Theorems 1-2) is not properly grounded.** Theorem 1 claims α_{ij}^{ssa} ∝ (α − βΔ)_+ — that SSA attention weights decay linearly with Manhattan distance — and α_{ij}^{vsa} ∝ exp(−βΔ). These forms are asserted without derivation or justification. SSA computes q_i·k_j on binary spike vectors; the result depends on feature similarity, not just spatial distance. Theorem 2's entropy ordering (Eq. 10) involves an α_i term that is not defined in the main text. As presented, these theorems lack the explicit assumptions needed to evaluate their validity and do not convincingly support the paper's claims about why LRF-SSA works. The paper would be better served by relying on the empirical evidence (which is already fairly strong on its own).

### Minor

3. **Memory reduction claims lack systematic measurement.** The "49.4% reduction" is stated only once in prose for Spikformer-8-512 (Section 6.2). There is no table of actual GPU memory consumption (in MB) across all model configurations. Asymptotic complexity (Table 1's SR column) is not a substitute for concrete measurements, especially since both LRF-SSA and LRF-Dyn add parameters (dilated convolutions, dendrite weights) that consume some memory themselves.

4. **No multiple seeds or uncertainty estimates.** All results are single runs. Gains of 0.4-1.24% could be within run-to-run noise. This is particularly important for the CIFAR-100 ablation (Table 3) where some gaps between variants are small (e.g., 78.64% vs 78.57%).

5. **Missing experimental details.** The number of simulation timesteps T for ImageNet is not stated. Hyperparameters (learning rate, batch size, optimizer, epochs) are absent. This harms reproducibility.

6. **Fourier formulation in Eq. 15 is unexplained.** Equation 15 introduces a Fourier-domain computation (F^{-1}{F(K) * F(X)}) that is distinct from the recurrence in Eq. 12. The connection is not explained, and the paper never mentions using FFT in experiments. It is unclear whether this formulation was actually implemented.

### Trivial

7. The biological framing (multi-dendritic neurons, charge-fire-reset) is somewhat decorative — Eqs. 12-13 describe a linear recurrence without spike generation, threshold, or reset. The method's value does not depend on the biological analogy.

## Nice-to-Haves

- An ablation comparing LRF-Dyn's specific recurrent formulation (Eqs. 12-13) with a simpler learnable-scalar variant of A and Γ, to isolate whether the structured multi-dendritic form matters.
- Energy consumption estimates (MACs vs. spike-driven operations) to accompany the memory analysis.
- A description of how the effective receptive field (ERF) in Figure 5 is computed.

## Removed Points

These points from the inputs were removed or demoted per the filtering rules:

- **"Overstated novelty — local convolutions already exist in ANN transformers"** (Harsh Critic): The paper's contribution is specifically about spiking transformers where SSA has unique constraints (binary activations, no softmax). ANN analogy does not invalidate the SNN contribution. **Removed**.
- **"Biological analogy is misleading"** (Harsh Critic's Issue 4): The paper frames the dynamics as "inspired by" biology, which is standard in the SNN field. The core insight is the recurrent computation, not biological fidelity. **Demoted** from a separate weakness to Trivial item 7.
- **"Could be catastrophic for non-image data"** (Harsh Critic): The paper scopes itself to vision tasks. Speculation about set-structured data is outside scope. **Removed**.
- **"Table 1 storage complexity inconsistency"** (Harsh Critic): Different baselines (SDT-V1 vs. others) use different SSA versions, so their SR columns differ by design. Not an inconsistency. **Removed**.
- **"Theoretical analysis should be removed entirely"** (Harsh Critic, implicit): This is an opinion, not a specific weakness. The actual problem (unjustified claims) is captured in Major weakness 2. **Removed**.
- **Strength Finder's "theoretical characterization" strength**: The theory is not rigorous enough to count as a genuine strength. **Removed**.

## Novel Insights

None beyond the paper's own contributions. A genuinely novel insight would require deeper analysis of *why* LRF-Dyn's recurrence recovers performance despite the causal bottleneck — the data in Table 3 suggests this recovery is real, but the paper does not explain it.

## Suggestions

1. **Address the causal issue directly.** Study how different token orderings (raster, Hilbert, random) affect LRF-Dyn's performance on ImageNet or at least CIFAR-100. If the model is robust to ordering, state this; if not, discuss the limitation and when the causal bias is acceptable (e.g., for image patch sequences where spatial smoothness already imposes a weak ordering).

2. **Either properly ground the theorems or remove them.** If Theorem 1 makes claims about the *average* or *expected* attention weight as a function of distance, state the averaging assumptions explicitly and show how they would hold under the model's spike distributions. Otherwise, drop the theoretical framing and let the strong empirical evidence stand on its own.

3. **Report actual GPU memory consumption** in a systematic table covering all model configurations (Spikformer, QKFormer, SDT-V3 at each scale), for baseline SSA, LRF-SSA, and LRF-Dyn.

4. **Run at least 3 seeds** for the main ImageNet results and the CIFAR-100 ablation, reporting mean and standard deviation.

5. **State the simulation timestep T** used for ImageNet experiments, along with learning rate, batch size, optimizer, and epoch count.

6. **Clarify the relationship between Eq. 12 and Eq. 15**, or remove Eq. 15 if it was not implemented.

## Score and Decision

**Calibration Report:**

*Round 1 (bracketing, 3 queries on "spiking transformer self-attention SNN"):* Weak anchors (score<3.5): O3CuUy5XAX (3.00), 6c2h6mZVfu (2.67). Middle anchors (3.5-7.5): ZsvGCzpaVD (6.00), 9z9mgVpXyE (4.50), r6fNn987rr (4.00), XX8jHAbWoy (4.00). Strong anchors (>7.5): kkBOIsrCXh (8.00, different field). Round-1 bracket: [3.5, 6.0].

*Round 2 (narrowing, 2 queries):* L5llQD0nMf / TP-Spikformer (4.50, accept) — similar quality level with clear contribution but limitations; the current paper has stronger architectural novelty but weaker experimental rigor. 9z9mgVpXyE (4.50, reject) — comparable; both have a focused contribution but notable gaps. 78glEsQB0v / SMixer (5.00, accept) — stronger experimental validation and clearer efficiency analysis. 7Brnh0aNFn / Spiking Discrepancy Transformer (6.00, accept) — stronger across all dimensions.

Comparisons: Better than SF-PE (2.67) and SpikingLLM (4.00). Comparable to TP-Spikformer (4.50) and the Positional Encoding paper (4.50). Weaker than SMixer (5.00) and RAT SNN (6.00) due to the unexamined causal issue and missing experimental rigor.

*Final score:* **4.5** — borderline paper with a clear architectural contribution that is held back by the unanalyzed causal bias in LRF-Dyn, weak theoretical framing, and missing experimental details.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>