Now I have enough information. Let me compile the final review.

## Calibration Analysis

**Round 1 Bracketing:**
- Low band (< 3.5): GroupMamba (3.00), NCA compression (3.40) — the current paper is clearly above these
- Middle band (3.5–7.5): MambaVC (4.80), Autoregressive Mamba (5.75), Spatial-Mamba (7.00)
- High band (> 7.5): Progressive Diffusion Compression (8.00), Oscillatory SSM (8.00) — the current paper is clearly below these

**Bracket: between 5.5 and 7.0**

**Round 2 Narrowing:**
- MambaVC (4.80): Direct predecessor; the current paper has substantially more task-specific innovation (CTP, GPP) vs. "just apply VSS block." Clear improvement.
- Autoregressive Mamba (5.75): Good but straightforward pretraining recipe. Current paper has more architectural novelty.
- Spatial-Mamba (7.00): Novel SASF mechanism for general vision. Current paper is comparable but the gradient-flow gap pulls it slightly below.
- Lattice Transform Coding (7.20): Stronger theoretical contribution.

**Final score: 6.5** — Above MambaVC (4.80) and Autoregressive Mamba (5.75); comparable to but slightly below Spatial-Mamba (7.00) due to the gradient-flow documentation gap.

---

## Summary

The paper introduces Content-Aware Mamba (CAM) for learned image compression, replacing Mamba's rigid raster scan with content-adaptive token permutation (CTP) via codebook-based clustering, and mitigating strict causality via global-prior prompting (GPP). The resulting CMIC model achieves strong BD-rate reductions over VTM-21.0 (−15.91% Kodak, −21.34% Tecnick, −17.58% CLIC) while reducing parameters by 56% and peak memory by 78% vs. MambaIC.

## Strengths

- **Content-adaptive token permutation with clear empirical validation.** CTP groups semantically related tokens regardless of spatial position. Figure 10 shows cluster membership aligns with visual content (red doors, feathers, sky), and Table 2 confirms CTP alone reduces BD-rate by 1.8–2.4% across datasets. This directly addresses the paper's central problem of content-agnostic raster scans.

- **Global-Prior Prompting demonstrably relaxes strict causality without multi-directional scans.** Figure 9 shows that GPP introduces non-causal activations beyond the raster-scan boundary, and Table 2 shows GPP alone yields 0.5–1.4% BD-rate improvement. The ablation study (Table 2) establishes complementarity: CTP+GPP together achieve 2.7–3.6% total BD-rate improvement over the vanilla-Mamba baseline.

- **State-of-the-art RD performance with substantial efficiency gains.** Table 1 reports CMIC outperforms all prior Mamba- and Transformer-based LIC models on Kodak, Tecnick, and CLIC, while using 56% fewer parameters, 57% fewer FLOPs, and 78% less peak memory than MambaIC. The controlled ablations (Tables 2–4, all trained on Flickr2W) confirm these gains are not artifacts of cross-dataset comparisons.

- **The clustering mechanism introduces negligible overhead.** Training throughput drops from 23.19 to 22.05 samples/s (Table 3), and decoding latency increases by only 4% (0.387s → 0.405s), confirming practical deployability.

- **ERF analysis convincingly demonstrates content-adaptivity.** Figures 7–9 show CMIC's effective receptive field is substantially larger than CNN, Transformer, and prior Mamba-based models, and that high-influence regions align with semantically meaningful structures (hair, feathers, shoreline) in a per-image adaptive manner.

## Weaknesses

### Major

None.

### Minor

- **Gradient flow through the clustering/permutation is not specified.** The paper uses a hard argmax assignment (Algorithm 1, line 4) and a discrete permutation, then cites VQ-VAE as inspiration. VQ-VAE uses a straight-through estimator, but the paper never states whether this is employed, whether gradients are blocked, or whether some other mechanism is used. The centroids are updated via non-gradient EMA; the linear projection $\mathcal{A}$ in GPP is the only differentiable path from the clustering to the loss. This omission matters for reproducibility: if gradients are blocked at the argmax, the feature encoder receives no direct supervision to produce cluster-friendly representations, and the claimed *learned* content-adaptivity is weaker than implied. The paper's empirical results are unlikely to be invalidated by this detail (the model works), but the authors must clarify the gradient routing.

- **The "2D Mamba" ablation (Table 4) is not clearly defined.** The paper states "substitute with Conv block and 2D Mamba blocks" but does not specify whether the 2D Mamba uses 4-direction scanning or a single raster scan. Without this, the claim that CTP+GPP "avoids quadrupling computational cost" cannot be directly verified from this ablation.

### Trivial

- None.

## Nice-to-Haves

- A brief limitations paragraph (e.g., acknowledging that clustering is unsupervised and may not be optimal for compression) would strengthen the paper's completeness.
- An ablation comparing cosine K-means vs. Euclidean K-means or a simpler grid-based grouping would further justify the cosine-based design choice.
- The paper could be more explicit about why the prompt dictionary is preferable to a fully learnable prompt pool (the current explanation is brief).

## Removed Points

These points were removed from the inputs after verification against the paper text, following the filtering rules:

1. **Cross-dataset comparison fairness (Harsh Critic Critical Issue 2):** Concern that Table 1 baselines used different training data. *Removed because:* (a) this is standard practice in LIC evaluation; (b) the paper's controlled ablations (Tables 2–4, trained on Flickr2W) are the primary evidence for the contribution; (c) the reviewer acknowledged the claim "may still be true" and the evidence is "weaker than presented" but not invalid. The harsh critic's own controlled-ablation analysis shows the real evidence is strong.

2. **Missing limitations discussion:** *Moved to Nice-to-Haves* — a useful addition but not a weakness of the paper as submitted.

3. **"Quadrupling computational cost" not demonstrated with a multi-directional baseline.** The paper does compare against "2D Mamba" in Table 4; the issue is that the configuration of that baseline is underspecified (now addressed as a Minor weakness about definition clarity, not a separate computational-cost claim issue).

4. **Strength Finder generic strengths** (e.g., "this paper addressed an important problem"): *Removed* — these are superficial and not specific to the paper's evidence.

5. **Strength about codebook-based clustering with EMA being training-stable:** *Retained* (it is specific and backed by Table 3 throughput numbers).

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface a synthesis or observation that the paper itself does not already articulate.

## Suggestions

1. **Clarify gradient flow.** Add a 2–3 sentence paragraph explaining how gradients pass through the argmax assignment and permutation. If a straight-through estimator (as in VQ-VAE) is used, state it explicitly. If gradients are blocked, discuss why the model still learns useful features.

2. **Define the "2D Mamba" ablation explicitly.** State whether it uses 4-direction scanning or a single scan, so the comparison with CTP+GPP's single-scan approach is interpretable.

3. **Include a brief limitations discussion** to improve completeness (e.g., unsupervised clustering may not be optimal for compression; K=64 is dataset-specific).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>