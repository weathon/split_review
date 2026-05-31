Now let me perform calibration searches to determine the appropriate score.Round 1 bracket: **5.5–7.5**. MambaVC (directly compared in paper) scored 4.8 and was rejected; CMIC clearly surpasses it in every metric. Spatial-Mamba at 7.0 is an accepted Mamba-for-vision paper. Let me narrow within this range.Now I have enough to write the final review. Key comparisons:
- **MambaVC** (4.8, Rejected): CMIC is a direct successor that significantly outperforms it on every metric
- **FAT** (6.0, Accepted): Comparable LIC paper with single frequency-aware attention contribution; CMIC has two well-motivated components, stronger performance, and a better efficiency story
- **Spatial-Mamba** (7.0, Accepted): More fundamental architectural change to SSMs for general vision

CMIC sits between FAT (6.0) and Spatial-Mamba (7.0). It is stronger than FAT in novelty depth and empirical results, but the minor overstatement of SOTA and GPP mechanism imprecision keep it from reaching 7.0. Final score: **6.5**.

---

## Summary
Content-Aware Mamba for Image Compression (CMIC) proposes a novel Mamba-based learned image compression framework with two key innovations: Content-Adaptive Token Permutation (CTP), which reorders latent tokens via VQ-VAE-style codebook clustering to group semantically similar tokens before the SSM scan; and Global-Prior Prompting (GPP), which injects sample-specific, cluster-derived prompt vectors into the SSM output projection to condition each token's readout on global image statistics. The combined model achieves state-of-the-art BD-rate savings on Tecnick (−21.34%) and CLIC (−17.58%) over VTM-21.0, is near-SOTA on Kodak (−15.91%), and substantially reduces parameter count, FLOPs, and memory compared to prior Mamba-based LIC competitors.

## Strengths

- **CTP demonstrably improves content-adaptive redundancy capture, with well-ablated gains.** Table 2 isolates CTP-only BD-rate gains of ~2.0% (Kodak), ~2.4% (Tecnick), and ~1.8% (CLIC), and Figure 10 confirms that clusters learn semantically coherent visual patterns (red doors in Kodim01, feather textures in Kodim23), directly supporting the claim that feature-space proximity is prioritized over Euclidean order.

- **Efficiency story over MambaIC is compelling and practically significant.** Table 3 and Section 4.4 document that CMIC achieves 56% fewer parameters (69.1M vs. 157M), 57% fewer FLOPs (2.39T vs. 5.56T), 39% lower decoding latency, and 78% lower peak memory compared to MambaIC, while outperforming it on all three datasets. This is the paper's most striking result.

- **ERF analysis provides multiple layers of supporting evidence.** Figure 7 shows globally wider ERFs than all competing models. Figure 8 reveals per-image content-adaptive activation patterns aligned with semantic structure (hair, shoreline, aircraft). Figure 9 isolates GPP's non-causal effect and CTP's feature-space ERF restructuring in a single Mamba layer—directly linking mechanism to behavior.

- **The adaptive cluster count is an empirically grounded claim.** Table 5 reports that images activate on average only 23–26 of 64 codebook entries (variance ≈91–121), and Table 6 confirms K=64 is near-optimal, showing the codebook is neither saturated nor underutilized.

- **CTP and GPP are complementary and additive.** Table 2 confirms that the joint gain (~2.7–3.6% BD-rate) exceeds the sum of the individual gains in the right direction, with no evidence of interaction artifacts.

## Weaknesses

### Fatal
None.

### Major

- **Partially overclaimed SOTA on Kodak.** Table 1 clearly shows MLICv2 achieves −16.16% on Kodak versus CMIC's −15.91%—a 0.25% gap in MLICv2's favor. Section 4.3 states "Our CMIC model achieves superior performance, reducing BD-rate by 15.91%, 21.34%, and 17.58% on the Kodak, Tecnick, and CLIC datasets" without acknowledging this shortfall. The abstract similarly claims "state-of-the-art rate-distortion performance" without qualification. Given that CMIC uses 18% fewer parameters (69.1M vs. 84.3M) and fewer FLOPs (2.39T vs. 2.78T) than MLICv2, a brief acknowledgment of the Kodak gap—contextualized against the large efficiency advantage—would render the claims honest and still compelling.

### Minor

- **GPP is described as "relaxing strict causality" and "encoding global priors during the scan process," but the mechanism only modifies the output readout matrix C, not the state update.** As shown in the SSM equations (Section 3.4), the state update h_i = Ā h_{i−1} + B̄ x_i remains strictly causal; GPP inserts a sample-specific offset into O_i = (C + P)h_i + Dx_i. The ERF visualization in Figure 9(c) shows GPP does introduce non-zero activations beyond the causal boundary, so the *effect* is real, but it works by conditioning how the hidden state is *read*, not by modifying what information the hidden state *stores*. The description should be more precise: GPP provides globally conditioned output scaling, not bidirectional state communication. This is a conceptual imprecision, not a structural flaw—the ablation evidence supports GPP's utility regardless.

- **The non-differentiable clustering and its gradient flow implications are not discussed in the main body.** Token permutation is determined via argmax (non-differentiable), and codebook updates are EMA-based (Algorithm 1, outside the gradient graph). The paper notes the mapping A(·) is differentiable and trained end-to-end, but does not address whether early-training feature diffuseness could lead to uninformative cluster assignments that degrade SSM training before the codebook stabilizes. The appendix reportedly covers stability, but the main body should include at least a brief discussion of this training dynamics concern, since it is a real design choice distinct from standard VQ-VAE usage.

### Trivial

- **Table 2 has a rendering artifact** (both rows 1 and 2 appear to have CTP=✓; row 1 should be CTP=✗, GPP=✗ based on the text). This is a PDF parser issue, not an author error, but the camera-ready table should disambiguate with explicit ✗ marks to avoid confusion.

## Nice-to-Haves

- A direct quantitative measurement of the CTP mechanism's core premise would strengthen the paper: reporting the average feature-space cosine distance between consecutive token pairs under raster scan vs. CTP-permuted scan would make the "feature-space proximity" claim verifiable rather than assumed.

- Section 4.3 mentions that CAM in the entropy model yields "negligible performance gains while increasing latency" but defers the evidence to the appendix. A single sentence explaining *why* CAM does not help in the entropy model (e.g., local serial context makes global clustering less relevant) would preempt reviewer concern about incomplete methodology.

- Per-image analysis correlating BD-rate gain with number of activated clusters (Table 5) would provide direct quantitative support for the claim that content-heterogeneous images benefit more from CTP—the clustering visualization (Figure 10) already moves in this direction.

- Per-bitrate or per-image analysis of GPP's specific contribution (e.g., whether it helps most at low bitrates where global context is more compressed) would help readers understand when to apply GPP versus simpler baselines.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Section 3.3 — codebook initialization in raster order is inconsistent with the paper's motivation."** Removed because EMA over many batches makes initialization irrelevant to the final codebook quality; this is acknowledged in the paper. Retaining it would be a nitpick.

- **Harsh Critic: "Table 2 is a structural error requiring correction."** Demoted to Trivial (parser artifact per hard rules); the text unambiguously describes the ablation setup, so this is a presentation clarification, not a methodological error.

- **Harsh Critic: "The ERF visualization does not rule out that high-gradient regions naturally attract large gradients in any expressive model."** Removed—this is speculative-conjecture criticism ("alternative hypothesis not ruled out") without a specific anchor showing CMIC's ERF pattern is explainable by architecture expressiveness alone. The comparison against FTIC and TCM-L in Figure 8 does provide the relevant counterfactual.

- **Harsh Critic: "The comparison with FTIC/TCM in ERF should use same images."** Removed—Figure 8 explicitly compares CMIC, FTIC, and TCM-L on the same Kodak images; the harsh critic's objection is factually incorrect.

- **Strength Finder: "CMIC achieves state-of-the-art performance, outperforming all methods"** — Partially dropped because MLICv2 outperforms CMIC on Kodak; retained only as qualified (SOTA on Tecnick and CLIC, near-SOTA on Kodak).

- **Harsh Critic: "MambaC vs. MambaIC naming inconsistency."** Removed as trivial formatting/consistency nitpick.

## Novel Insights

The paper's most genuinely novel observation—supported by Figure 9 and Table 2—is that CTP and GPP address orthogonal failure modes of Mamba: CTP reshapes *which tokens interact* (fixing scan order), while GPP reshapes *how the hidden state is read* (partially fixing causality). Their empirical complementarity (additive BD-rate gains with no saturation) suggests these two axes of content-awareness are nearly independent, which has broader implications for designing adaptive SSMs beyond LIC. The clustering visualization further shows that the codebook spontaneously learns semantically consistent cross-image representations (edges, saturated textures, smooth backgrounds), suggesting that VQ-VAE-style codebooks can encode perceptually meaningful priors even when trained purely on a rate-distortion objective.

## Suggestions

1. In Section 4.3, explicitly acknowledge that MLICv2 leads on Kodak by 0.25%, and immediately contextualize this with CMIC's efficiency advantage (18% fewer parameters, fewer FLOPs). This one sentence would make the SOTA framing defensible.
2. In Section 3.4, revise the description of GPP to accurately state that it "provides globally conditioned output scaling" rather than claiming it modifies the causal state update or "relaxes strict causality" in the strong sense. The ERF evidence in Figure 9(c) is sufficient to justify the practical benefit without overstating the mechanism.
3. Add a brief paragraph in Section 3.3 or 4.5 discussing the training dynamics of the non-differentiable permutation—specifically how EMA stabilization ensures the codebook converges before CTP degrades SSM gradient flow in early training.

---

## Score Calibration

**Round 1 anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| KgJwbsfN7G (MambaVC) | 4.80 | R1 | CMIC directly surpasses; rejected for low novelty of plug-in Mamba |
| iDe1mtxqK5 (Spatial-Mamba) | 7.00 | R1 | Accepted; more fundamental SSM redesign, not LIC-specific |
| AL1fq05o7H (Mamba original) | 6.25 | R1 | Different scope |
| PQpvhUrA1C (AR-Mamba Pretrain) | 5.75 | R1 | Different task |
| HKGQDDTuvZ (FAT-LIC) | 6.00 | R2 | Accepted LIC paper; CMIC stronger in novelty and performance |
| mb2ryuZ3wz (Variable tokens) | 5.75 | R2 | Accepted; different modality |
| bsnRUkVn63 (TTA-IC) | 6.00 | R2 | Accepted; narrower scope than CMIC |
| foKwWau15m (CMC-Bench) | 6.00 | R2 | Rejected; benchmark paper, different contribution type |

**Round 1 bracket:** 5.5–7.5  
**Round 2 narrowing:** FAT (6.0) is the closest topical anchor (LIC + SOTA comparison + ablation). CMIC is stronger than FAT: two well-motivated novel components vs. one; better performance gains; explicit efficiency story; richer mechanistic analysis. The minor SOTA overstatement and GPP imprecision are addressable. CMIC is above 6.0 but below Spatial-Mamba (7.0) due to narrower scope (LIC only) and the real-but-minor weaknesses. Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>