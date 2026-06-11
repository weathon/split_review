Now I have all the information I need. Let me write the final review.

---

## Summary
This paper proposes Content-Aware Mamba (CAM) for learned image compression, introducing two mechanisms: (1) Content-Adaptive Token Permutation (CTP), which uses a learnable codebook to cluster latent tokens and reorder them so semantically similar tokens are contiguous; and (2) Global-Prior Prompting (GPP), which injects cluster-derived prompt vectors into the SSM output projection. The resulting CMIC model achieves competitive BD-rate savings of 15.91–21.34% over VTM-21.0 on Kodak, Tecnick, and CLIC datasets.

## Strengths
- **CTP is well-motivated, novel, and empirically validated.** The codebook-based clustering approach correctly identifies Mamba's rigid raster scan as limiting for image compression. Ablation (Table 2) shows CTP contributes ~1.8–2.4% BD-rate improvement over the vanilla single-scan Mamba baseline. Cluster visualizations (Fig. 10) demonstrate convincing semantic grouping — doors/windows (Kodim01), sky/clouds (Kodim21), feathers (Kodim23) — confirming tokens are grouped by content similarity as intended.

- **Competitive rate-distortion performance with favorable complexity.** CMIC achieves −15.91%, −21.34%, and −17.58% BD-rate on Kodak, Tecnick, and CLIC (Table 1), substantially outperforming prior Mamba-based methods (MambaVC by 7.51–10.09%, MambaIC by 2.17–6.48%). It uses 56% fewer parameters, 57% fewer FLOPs, and 78% less GPU memory than MambaIC, demonstrating the single-scan design with CTP/GPP is more efficient than multi-directional scan alternatives.

- **Components shown complementary through careful ablation.** Table 2 demonstrates CTP and GPP address orthogonal limitations: CTP alone yields −15.21% (Kodak), GPP alone yields −14.27%, and together −15.91%. The structural ablation (Table 4) validates CAM blocks over Conv (−12.89%), 2D Mamba (−14.13%), attention-only (−13.06%), and CAM-only (−14.68%) alternatives.

- **Content-adaptive clustering demonstrated quantitatively.** Table 5 shows only 23–26 out of 64 centroids are activated per image on average with high variance (90.91 on Kodak, 121.15 on CLIC), confirming the effective number of clusters adapts to image content. Throughput analysis (Table 3) shows CTP and GPP introduce only ~5% training overhead and ~4% decoding latency increase.

## Weaknesses

### Fatal
None.

### Major
- **GPP's claimed "non-causal" mechanism is overstated, and the key ERF evidence is weakened by a soft-clustering proxy.** GPP modulates the SSM output projection **C** (O_i = (C+P_i)h_i + Dx_i) rather than the hidden state recurrence (h_i = Āh_{i-1} + B̄x_i). Information in h_i remains strictly causal. The paper's language — "non-causal long-range modeling" (line 34), "relaxes the strict causal constraint" (line 183) — substantially overstates what the mechanism accomplishes. At inference, each token's prompt P_i depends only on that token's own features (via cosine similarity to fixed centroids), not on other tokens in the image. The actual mechanism is better described as cluster-conditioned output modulation using dataset-level priors. Furthermore, the ERF analysis in Fig. 9, presented as direct evidence for non-causality, explicitly uses "soft clustering" (§4.5, lines 299-301), whereas the deployed model uses hard clustering (argmax assignment, line 122). Soft clustering creates gradient pathways through the cluster assignment that do not exist with hard clustering, so the ERF patterns in Fig. 9(c)-(e) may overstate the effect present in the actual model. This framing issue affects the credibility of the paper's central narrative about breaking causality, though the underlying method (CTP + cluster-conditioned readout) remains useful and empirically validated.

### Minor
- **The SOTA claim in the abstract is slightly overbroad.** The abstract states CMIC "achieves state-of-the-art rate-distortion performance" without qualification, but Table 1 shows MLICv2 achieves −16.16% on Kodak vs. CMIC's −15.91%. CMIC leads on Tecnick and CLIC, so the claim should be qualified (e.g., "competitive or state-of-the-art on two of three benchmarks").

- **Within-cluster token ordering for CTP is unspecified.** The permutation π groups tokens by cluster (line 122) but does not specify ordering within each cluster. Since the SSM processes tokens sequentially, intra-cluster adjacency determines which token-to-token interactions can be exploited. This detail is needed for full reproducibility.

- **MS-SSIM evaluation is minimal.** Only two aggregate numbers (−7.34% vs. TCM-L, −3.87% vs. FTIC) are reported in prose (§4.3). A full BD-rate table for MS-SSIM would strengthen the evaluation, especially given the SOTA claim spans both MSE and MS-SSIM optimization.

- **Training-time behavior of K-Means clustering is not discussed.** Whether centroids converge, how assignment stability evolves, and whether the non-gradient K-Means updates interact well with gradient-based RD optimization are not addressed. This matters because unstable clustering would produce inconsistent permutations during training.

- **Entropy model modifications are not independently ablated.** The paper states (lines 248-249) that adding CAM to the entropy model yields negligible gains (details deferred to Appendix A.3.2), but the contributions of the depthwise convolution and gated MLPs (Fig. 3) are not isolated from the CAM contribution.

### Trivial
None.

## Nice-to-Haves
- Statistical significance or variance measures for BD-rate numbers, particularly relevant when differences vs. MLICv2 are small (0.25 pp on Kodak).
- Discussion of whether cluster centroids trained on Flickr2W transfer robustly to out-of-distribution images.
- Replace the soft-clustering ERF analysis (Fig. 9) with an analysis reflecting the actual hard-clustering mechanism, or clearly caveat the approximation.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic "Table 2 corrupted by parser"** — This is a parsing artifact in the review copy. The table is interpretable from context (row 1 is the baseline with no CTP/no GPP, despite the parser showing a checkmark).
- **Harsh Critic "no qualitative RD comparison in main text"** — The paper defers these to Appendix A.5, which is stripped in this copy. Cannot evaluate whether they exist.
- **Harsh Critic "no measure of variance / statistical significance"** — Demoted to Nice-to-Have. Single-run evaluation without CIs is standard practice in LIC benchmarking, and consistent margins across three datasets support the claims.
- **Harsh Critic "MambaVC's peak memory of 14.73 GB is surprisingly high"** — This is about another model, not a weakness of this paper.
- **Strength Finder "GPP provides lightweight and effective solution with ERF evidence" (unqualified version)** — The strength is retained but qualified; the ERF evidence uses soft clustering that differs from the deployed model.
- **Generic strengths about "important problem" or "well-written"** — Removed as superficial/not anchored in concrete evidence.

## Novel Insights
None beyond the paper's own contributions. The idea of using a codebook-based clustering for content-adaptive token reordering in SSM-based compression is a sensible synthesis of existing techniques (VQ-VAE-style codebooks + Mamba SSMs), applied effectively to a new domain.

## Suggestions
- **Reframe GPP honestly.** The real contribution is cluster-conditioned output modulation paired with content-adaptive token ordering — both are genuinely useful and empirically validated. Drop the "non-causal" framing and instead argue that GPP allows the SSM to use different readout strategies for different semantic regions, injecting a weak dataset-level prior that partially compensates for causal processing limits.
- **Specify within-cluster token ordering explicitly.**
- **Qualify the SOTA claim** in the abstract to reflect the Kodak result vs. MLICv2.
- **Replace or caveat the soft-clustering ERF analysis** in Fig. 9 to reflect the actual hard-clustering mechanism.

## Score and Decision

### Anchor Comparison (All Rounds)

**Round 1 anchors (bracketing):**
- `ReccFdn4zE.md` (avg 2.00) — Cross attention for oddly shaped data. Completely different domain and quality tier; not comparable.
- `LyJi5ugyJx.md` (avg 2.38, actually 9.20 — search anomaly) — Ignore; score is from a different query artifact.
- `WM5G2NWSYC.md` (avg 2.00) — Projected subnetworks. Very low quality; not comparable.
- `WoJzHQIIUk.md` (avg 1.50) — MinMax BNN. Very low quality; not comparable.
- `qi7udwV66M.md` (avg 4.25) — Zero-shot diffusion compression. Interesting idea but significant gaps; CMIC is clearly stronger.
- `gIrVoQEDQv.md` (avg 3.40) — Neural cellular automata for compression. Weaker contribution; CMIC is stronger.
- `aQ7qYnY2nF.md` (avg 4.00) — RL for video compression rate control. Different task; CMIC is stronger.
- `3d6awrrpUq.md` (avg 3.50) — Compressed-language models for JPEG. Different task; CMIC is stronger.
- `HKGQDDTuvZ.md` (avg 6.00) — **FAT for LIC.** Clean architectural contribution, SOTA results, no conceptual overstatements. CMIC has more novel core idea (CTP) but a Major framing issue (GPP causality). **CMIC is slightly below FAT.**
- `ulIW7Frjpn.md` (avg 4.75) — LLM entropy models. Novel but significant practical concerns. CMIC is stronger.
- `GSUNPIw7Ad.md` (avg 6.00) — Bridging compressed latents and MLLMs. Strong contribution; CMIC is roughly comparable but with the GPP framing issue.
- `dcG17rjJF9.md` (avg 5.67) — LLM for lossless compression. Different task; CMIC is comparable in quality.
- `Tv36j85SqR.md` (avg 7.20) — Lattice transform coding. Strong theoretical contribution. CMIC is clearly below.
- `VkWbxFrCC8.md` (avg 6.67) — RECOMBINER for INR compression. Strong contribution. CMIC is below.
- `kQCHCkNk7s.md` (avg 6.25) — AstroCompress benchmark. Different contribution type. CMIC is comparable or slightly below.
- `44cMlQSreK.md` (avg 7.20) — NeuroQuant for video coding. Strong contribution. CMIC is clearly below.
- `CxXGvKRDnL.md` through `fV0t65OBUu.md` (avg 8.00) — Various strong contributions. CMIC is clearly below.

**Round 2 anchors (narrowing):**
- `KgJwbsfN7G.md` (avg 4.80) — **MambaVC.** Direct predecessor applying SSMs to LIC. Rejected for limited novelty (straightforward application of VSS blocks), weak baseline comparisons, and insufficient SOTA comparisons. **CMIC is clearly stronger:** CTP is a genuinely novel mechanism designed for compression (not borrowed), baseline comparisons are comprehensive (13+ methods), RD performance is much better (−15.91% vs. −8.10% on Kodak), and ablation/analysis is thorough.
- `PQpvhUrA1C.md` (avg 5.75) — Autoregressive pretraining with Mamba in vision. Solid empirical contribution, accepted. CMIC has more architectural novelty but the GPP framing issue. **CMIC is comparable, slightly below.**
- `QBiFoWQp3n.md` (avg 4.60) — Architecturally aligned ConvNet vs. Mamba comparisons. Different contribution type. CMIC is stronger.
- `0A6f1b66pE.md` (avg 4.60) — Mamba for vision-language models. Different task. CMIC is stronger.
- `mb2ryuZ3wz.md` (avg 5.75) — Variable-length token representations. Different task. CMIC is comparable.
- `tFV5GrWOGm.md` (avg 6.00) — **ElasticTok.** Adaptive tokenization, clean contribution, all 6s. **CMIC is slightly below** due to the GPP framing issue.
- `ptCIlV24YZ.md` (avg 5.80) — Image clustering via rate reduction. Different task. CMIC is comparable.

**Bracket:** Round 1 placed CMIC between 4.5 and 6.0. Round 2 narrowed this: CMIC sits clearly above MambaVC (4.80) and below FAT/ElasticTok (6.00), closest to the Autoregressive Mamba pretraining paper (5.75) but with a framing weakness that pulls it slightly lower. **Final score: 5.5.**

The GPP causality overstatement and soft-clustering ERF mismatch constitute a genuine Major weakness in the paper's theoretical narrative, but the core contribution (CTP) is novel and well-validated, the empirical results are strong and comprehensively benchmarked, and the ablation analysis is thorough. With a rebuttal reframing GPP honestly, this paper would be a solid contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>