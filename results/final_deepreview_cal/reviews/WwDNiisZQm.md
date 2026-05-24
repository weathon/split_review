Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper presents Content-Aware Mamba (CAM), an SSM-based architecture for learned image compression that addresses two key limitations of vanilla Mamba when applied to images: (1) rigid raster-scan ordering that fails to group semantically related but spatially distant tokens, and (2) strict causality that prevents each token from accessing global context. CAM introduces Content-Adaptive Token Permutation (CTP), which uses codebook-based cosine K-Means clustering to reorder tokens by feature similarity, and Global-Prior Prompting (GPP), which injects sample-specific global statistics into the SSM output projection via a cluster-tied prompt dictionary. The resulting CMIC model achieves state-of-the-art BD-rate reductions of 15.91%, 21.34%, and 17.58% over VTM-21.0 on Kodak, Tecnick, and CLIC respectively, while maintaining competitive computational complexity.

## Strengths

- **Content-Adaptive Token Permutation is well-designed and empirically validated.** CTP uses a shared, learnable codebook of centroids updated via EMA-based K-Means to cluster latent tokens, then reorders the 1D scan sequence so that feature-space neighbors become contiguous. Ablation (Table 2) shows CTP alone yields BD-rate reductions of 2.0%, 2.4%, and 1.8% on Kodak, Tecnick, and CLIC. Cluster visualizations (Fig. 10) confirm that semantically related regions (sky, feathers, building edges) are grouped together, directly supporting the method's core claim.

- **Global-Prior Prompting demonstrably relaxes causality without multi-directional scans.** GPP ties a prompt dictionary to the clustering centroids and modulates the SSM output matrix **C** with sample-specific global priors. ERF visualizations of a single Mamba layer (Fig. 9, column c vs. b) show that GPP produces non-zero activations beyond the causal scan position — direct evidence of non-causal information flow. The approach avoids the 4× computational cost of multi-directional scanning while still yielding 0.5–1.4% BD-rate improvements.

- **Comprehensive and convincing experimental validation.** The paper benchmarks against 14+ methods including VTM-21.0 and SOTA learned codecs (MLIC++, FTIC, HPCM, DCAE, etc.) across three standard datasets (Table 1, Figs. 4–6). Complexity analysis (Table 1) shows CMIC uses 56% fewer parameters, 57% fewer FLOPs, and 78% less peak memory than MambaIC while achieving better RD performance. Multiple ablation dimensions are covered: component contributions (Table 2), structural alternatives (Table 4), cluster count (Table 6), throughput (Table 3), and activation statistics (Table 5).

- **Effective Receptive Field analysis provides compelling qualitative evidence.** Fig. 7 shows CMIC's analysis transform has a substantially broader global receptive field than CNN-, Transformer-, and existing Mamba-based LIC models. Per-image ERF maps (Fig. 8) demonstrate that high-influence regions align with semantically meaningful structures, confirming content-adaptive behavior.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Gradient flow through the clustering step is acknowledged but not fully explained.** The paper correctly notes that centroid updates use a "non-gradient update process" (line 129) and that the prompt dictionary mapping 𝒜(·) is differentiable (line 186). However, it does not explicitly discuss how gradients propagate through the hard permutation step: the permutation is an index-based reordering that leaves token vectors unchanged, so gradients flow normally through the SSM while the clustering operates as a detached auxiliary module. Adding a sentence to clarify this would preempt reader confusion. The method is sound — this is a presentation gap, not a methodological flaw.

### Trivial

- **Table 2 contains a labeling error.** The first two rows both display "✓" in the CTP column with empty GPP, but show different BD-rate values (−13.26% vs. −15.21% on Kodak). From context (the text states the baseline uses a "vanilla single-scan Mamba block" and that adding CTP yields a 2.0% improvement), the first row is almost certainly the baseline row with both CTP and GPP disabled. This is a formatting artifact that should be corrected to avoid confusion.

## Nice-to-Haves

- The claim that Mamba's strict causality is "misaligned with the non-causal nature of images" (Section 1) could be stated more precisely — the actual issue is the limitation of unidirectional scan for joint spatial context modeling, which is what the method addresses.
- Reporting MS-SSIM results for Mamba-based baselines (MambaVC, MambaIC) is noted as omitted because those methods only optimize for MSE, but a sentence confirming this earlier would help readers.
- A brief note on expected behavior under perceptual metrics (LPIPS, etc.) would manage reader expectations, though the paper's MSE/MS-SSIM scope is standard for the field.

## Removed Points

These points were flagged for removal — treat them with caution:

- **"Non-differentiable clustering is a methodological gap / fatal flaw" (from harsh critic):** Removed from Major tier. The paper explicitly discusses the non-gradient nature of the K-Means update (lines 129, 186) and notes that the token permutation preserves token identity (only positions change), so gradients propagate normally. The mechanism is sound; the paper's description is adequate though could be expanded slightly (retained as Minor).
- **"Missing MS-SSIM for Mamba-based methods is a significant omission":** Removed. The paper explicitly states these competing methods are "only optimized for MSE" (Section 4.3), which is a reasonable justification.
- **"Training overhead of clustering needs quantification":** Removed. The paper states the 5 K-Means iterations account for "only 5% of each step's training time" and provides throughput numbers in Table 3 (23.19 → 22.05 samples/s), which is sufficient quantification.
- **Various phrasing/precision nitpicks about motivation and GPP mechanism description:** Moved to Nice-to-Haves as stylistic suggestions, not weaknesses.

## Novel Insights

The paper's ERF-based non-causality analysis (Fig. 9) is a genuinely illuminating diagnostic tool. By computing the ERF of a single SSM layer and ablating CTP and GPP individually, the authors produce visual proof that (a) vanilla Mamba exhibits strict raster-scan causality (zero activation beyond the anchor position), (b) GPP alone introduces non-zero activations in semantically meaningful regions beyond the causal boundary, and (c) CTP reshapes the ERF away from raster-scan patterns toward content-correlated regions. This layered visualization technique is a methodological contribution in itself and could be adopted by future SSM-for-vision papers to diagnose causality and content-adaptivity.

## Suggestions

- Add one sentence in Section 3.3 clarifying that the hard permutation is an index-based reordering preserving token vectors, so gradients propagate through the SSM normally.
- Fix Table 2 by adding an explicit baseline row (both CTP and GPP empty, value −13.26% on Kodak) and relabeling the CTP-only row with the correct value (−15.21% on Kodak).

## Score and Decision

**Round-1 bracket:** The paper sits clearly above MambaVC (4.80, rejected for limited novelty and weak comparisons) and in the range of Spatial-Mamba (7.00, accepted), Lattice Transform Coding (7.20, accepted), and AuxT (7.50, accepted). Initial bracket: 6.5–8.0.

**Round-2 narrowing:** CMIC is stronger than Spatial-Mamba (7.00) — it introduces two genuinely novel mechanisms vs. one fusion operation, has more comprehensive compression-specific experiments, and the ERF visualizations provide direct mechanistic evidence. CMIC is comparable to AuxT (7.50) — both have well-motivated innovations with strong empirical validation; AuxT has deeper theoretical analysis of energy compaction, while CMIC has broader component coverage (two complementary mechanisms, more ablation dimensions). CMIC is comparable to LTC (7.20) — LTC has stronger theoretical depth, CMIC has stronger practical demonstration and more thorough benchmarking. CMIC lands solidly at **7.5**.

**Anchor references:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| MambaVC (KgJwbsfN7G) | 4.80 | 1 | CMIC is dramatically stronger: genuine novelty vs. straightforward VSS application, comprehensive SOTA comparisons vs. only ConvVC/SwinVC, SOTA results vs. modest gains |
| Spatial-Mamba (iDe1mtxqK5) | 7.00 | 1 | CMIC is stronger: two mechanisms vs. one, compression-specific design, more comprehensive experiments including complexity, ERF, and clustering analysis |
| LTC (Tv36j85SqR) | 7.20 | 2 | Comparable quality: LTC has deeper theory, CMIC has broader empirical validation and more immediate practical impact |
| AuxT (U67J0QNtzo) | 7.50 | 2 | Comparable quality: both well-motivated innovations with thorough experiments; CMIC has two complementary mechanisms, AuxT has novel energy-compaction analysis |

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>