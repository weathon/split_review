Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces Content-Aware Mamba (CAM), a modification of Mamba-style state-space models for learned image compression, with two novel mechanisms: (1) Content-Adaptive Token Permutation (CTP), which reorders the token sequence by clustering feature-similar tokens together before the Mamba scan, prioritizing feature-space proximity over spatial adjacency; and (2) Global-Prior Prompting (GPP), which injects sample-specific global priors (derived from the clustering codebook) into the SSM output projection to relax the strict causal constraint. The resulting model, CMIC, achieves strong rate-distortion performance (BD-rate savings of -15.91%, -21.34%, -17.58% on Kodak, Tecnick, and CLIC against VTM-21.0) while maintaining computational efficiency far below prior Mamba-based LIC models.

## Strengths

1. **Well-diagnosed problem and targeted solutions.** The paper clearly identifies two concrete limitations of applying Mamba to image compression — content-agnostic scanning and strict causality — and proposes mechanisms (CTP and GPP) specifically designed to address each. This is not a generic application of Mamba to compression but a thoughtful adaptation with compression-specific designs.

2. **Ablation evidence cleanly isolates each component's contribution.** Table 2 shows CTP alone yields 1.8–2.4% BD-rate improvement, GPP alone yields 0.5–1.4%, and the combination achieves 2.7–3.6%, confirming both components are necessary and complementary. The component replacement ablation (Table 4) further shows CAM blocks outperform Conv, 2D Mamba, and attention-only alternatives with comparable parameter counts.

3. **Strong empirical results with convincing analysis.** CMIC substantially outperforms prior Mamba-based LIC models (MambaVC by 7.5–10.1%, MambaIC by 2.2–6.5%) while reducing parameters by 56%, FLOPs by 57%, and peak memory by 78% vs. MambaIC. The ERF visualizations (Figures 7–9) provide compelling evidence that CTP and GPP actually produce broader, content-adaptive receptive fields. The cluster visualization (Figure 10) demonstrates semantically meaningful groupings.

4. **High practical efficiency.** CMIC achieves strong RD performance at moderate complexity (69.11M params, 2.39 TFLOPs, 0.405s decode latency, 4.44GB peak memory), making it substantially more practical than the prior MambaIC (157.09M params, 20.32GB memory).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **"State-of-the-art" claim needs qualification.** The abstract claims "state-of-the-art rate-distortion performance," but Table 1 shows that on Kodak, MLICv2 achieves -16.16% BD-rate vs. CMIC's -15.91%. CMIC wins on Tecnick (-21.34% vs. -20.13%) and CLIC (-17.58% vs. -15.79%) and does so at lower complexity, so the overall claim is defensible but should be more precisely scoped (e.g., "competitive or superior to SOTA methods, with particular gains on high-resolution datasets").

2. **Gradient flow through the non-differentiable token permutation is not addressed.** The clustering uses argmax for hard assignments (Algorithm 1, line 152), which is non-differentiable. The centroid codebook is updated via EMA (non-gradient), and the paper notes the permutation is applied in the forward pass. However, it does not specify how gradients reach the feature encoder through this operation — whether via a straight-through estimator, treating the permutation as fixed during backward, or some other mechanism. Since the feature encoder produces the features being clustered, understanding this gradient path is important for reproducibility and for assessing whether the features are directly optimized to be clusterable. This is a common issue in clustering-based methods and can likely be addressed with a short clarification.

3. **"Relaxing strict causality" framing is slightly imprecise.** The paper states GPP enables "non-causal long-range modeling" (line 43) and "relaxes the strict causal constraint" (line 192). The state update equation h_i = Āh_{i-1} + B̄x_i remains strictly causal; what becomes non-causal is the output conditioning, because the prompt P is computed from all tokens via clustering. The ERF in Figure 9(c) showing non-zero activations after the anchor is consistent with this mechanism (gradients flow through the prompt generation network, not through the SSM state). This is a genuine contribution — the output at each step is informed by global priors — but the phrasing should be tightened to avoid implying the state transition itself becomes non-causal. The paper already provides enough detail for readers to understand the mechanism; this is primarily a presentation-cleanup issue.

4. **MS-SSIM comparison is incomplete.** The paper reports MS-SSIM BD-rate improvements over TCM-L (-7.34%) and FTIC (-3.87%) but does not provide a full table with all competing methods as is done for MSE. While the authors note that some competing methods are only optimized for MSE, a more complete MS-SSIM comparison table would strengthen the evaluation.

5. **Entropy model limitation not deeply discussed.** The paper mentions (Section 4.5) that "adding CAM to the entropy model yields negligible performance gains while increasing latency" (with details deferred to Appendix A.3.2). This is an interesting negative result that suggests a limitation of content-adaptive scanning in the entropy model context. A brief discussion of *why* this might be the case would strengthen the paper.

### Trivial

- The paper says the approach "avoids multi-directional scans" (line 41) but technically still uses a single 1D scan after content-adaptive permutation — this is clear from context but could be stated more precisely. No impact on results.

## Nice-to-Haves

- A full MS-SSIM BD-rate table (matching the MSE Table 1) would make the evaluation more complete.
- Examples where clustering is less effective (e.g., uniform textures, high-frequency regions) would help characterize limitations of the approach.
- The paper could briefly analyze why CAM helps the transforms but not the entropy model.

## Removed Points

The following points from the input reviews are removed with justification:

- **"GPP overstatement is a significant misinterpretation"** (Harsh Critic #1): Removed. The paper accurately describes that GPP relaxes causality by conditioning the SSM *output* on global priors. The state update remains causal, but the output incorporates information from the full image through the prompt. This is a genuine non-causal mechanism in the output, and the paper's phrasing ("relaxing strict causality") is reasonable. The ERF analysis in Figure 9 uses soft clustering (line 308), making gradient flow through the prompt network well-defined.

- **"Missing details about CAM block interaction with attention/conv"**: Removed. The paper clearly states (line 103) that "we first utilize window-attention to capture fine-grained local dependencies, while our proposed CAM blocks are introduced to enhance long-range modeling," and Figure 2 shows the architecture with staged Conv, Attention, and CAM blocks.

- **"Unclear whether P varies per token"**: Removed. The paper explicitly defines P = ΓU (line 186), where Γ is the one-hot assignment matrix, so each token receives its cluster's prompt vector.

- **"Missing rationale for cosine vs Euclidean"**: Removed. Cosine similarity is natural for L2-normalized features and the paper shows it works well. This is a standard design choice.

- **"Missing training hyperparameters"**: Removed. The paper provides learning rate, optimizer, λ choices, channel dimensions, block counts, cluster count, and window size (lines 198, 223). This is standard detail.

- **Generic strengths from Strength Finder about "importance of problem"**: Removed as generic/superficial.

- **Strength Finder's "ERF visualizations demonstrate CAM achieves global context"**: Verified and kept.

## Novel Insights

None beyond the paper's own contributions. The two input reviews largely agree on the paper's strengths and weaknesses, with the harsh critic's main concerns being either overstatements that don't survive verification against the paper text or relatively minor issues.

## Suggestions

1. Qualify the SOTA claim to acknowledge that CMIC is competitive with MLICv2 and DCAE, with particular strengths on high-resolution datasets and at lower complexity.
2. Add a sentence in Section 3.3 clarifying how gradients flow through the discrete token permutation (e.g., straight-through estimation or treating assignments as fixed during backward).
3. Tighten the GPP causality language (e.g., "enables the output to incorporate global information" rather than "non-causal modeling").
4. Include a full MS-SSIM BD-rate comparison table.
5. Add brief discussion of why CAM does not help the entropy model.

## Score and Decision

**Calibration Anchors:**
- **MambaVC** (KgJwbsfN7G.md, avg 4.80, Reject): First Mamba-based LIC, but novelty limited to applying existing VSS blocks. CMIC has substantially more novel contributions (CTP+GPP), better SOTA comparisons, and stronger results. **CMIC is clearly stronger.**
- **Spatial-Mamba** (iDe1mtxqK5.md, avg 7.00, Accept): Mamba architecture paper for general vision with structure-aware fusion. CMIC has comparable technical depth with stronger task-specific evaluation. **CMIC is comparable.**
- **Lattice Transform Coding** (Tv36j85SqR.md, avg 7.20, Accept): Theoretical contribution on lattice quantization for neural compression. CMIC has stronger empirical breadth but less theoretical depth. **CMIC is slightly weaker on theory, stronger on empirical validation.**
- **Idempotence** (Cy5v64DqEF.md, avg 7.50, Accept): Theory-driven compression paper with strong theoretical results. CMIC is more engineering-oriented. **CMIC is slightly lower on novelty but comparable on overall contribution.**
- **Test-time Adaptation for IC** (bsnRUkVn63.md, avg 6.00, Accept): Application-focused compression paper. **CMIC is stronger.**
- **CoINR** (ZWi6RpT4mJ.md, avg 3.50, Reject): Weak compression submission. **CMIC is far stronger.**
- **FV-NeRV** (hrXt6Fdl2P.md, avg 2.60, Reject): Very weak. **CMIC is far stronger.**

The paper makes a solid, well-evaluated contribution to learned image compression. The two proposed mechanisms (CTP and GPP) are novel, well-motivated, and empirically validated through comprehensive ablations and insightful visualizations (ERF, clustering). The empirical results are strong: CMIC significantly outperforms prior Mamba-based LIC models while being far more efficient, and is competitive with the best transformer-based methods. No fatal or major weaknesses exist; the identified issues are presentation refinements and a missing implementation detail. The paper is ready for acceptance pending minor revisions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>