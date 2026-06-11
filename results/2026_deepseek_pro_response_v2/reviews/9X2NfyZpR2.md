Now I have all the calibration data I need. Let me finalize.

## Calibration Summary

**Round 1 bracket:** 5.0–7.0. Below Anchor: the weak band (all ~3.0, reject) — TbLTA is clearly stronger. Above Anchor: the 8.0 band — TbLTA is clearly weaker (those are polished, near-consensus-accept papers).

**Round 2 narrowing:**

| Anchor | Avg Score | Decision | Comparison to TbLTA |
|--------|-----------|----------|---------------------|
| `sEARCNzhrP` (InterAct) | 5.00 | Reject | TbLTA stronger — more genuine novelty, new supervision paradigm |
| `IryGDUHxDE` (RISE) | 5.25 | Reject | TbLTA stronger — cleaner contribution, less novelty concern |
| `GQgPj1H4pO` (VSNLS) | 6.00 | Accept | Comparable — similar "first weak supervision for task" framing, similar single-dataset focus |
| `Bb21JPnhhr` (AntGPT) | 6.25 | Accept | TbLTA slightly below — AntGPT had SOTA on 3 benchmarks, more thorough eval |
| `f3CdjpPkSq` (ActSeq) | 6.50 | Accept | TbLTA slightly below — cleaner evaluation, more focused contribution |
| `dl34rOnbqJ` (Actions-to-Action) | 4.40 | Reject | TbLTA clearly stronger |
| `HEXtydywnE` (LASER) | 6.00 | Accept | Comparable quality, different task |

**Final score: 6.0.** TbLTA is a solid accept. The paper makes a genuinely novel contribution (first transcript-only LTA) with compelling results on Breakfast (beating all supervised methods). The major weakness (ablations on Top-1 oracle only) prevents a higher score but is addressable in revision and does not undermine the core contribution. The paper sits squarely with other 6.0-range accepted papers that introduce a new weak supervision paradigm with some evaluation limitations.

---

## Summary
This paper introduces TbLTA, the first framework for dense long-term action anticipation (LTA) trained exclusively from video transcripts — ordered action lists without temporal boundaries. The architecture combines an ATBA-based temporal alignment module for pseudo-label generation, cross-modal attention with pseudo-label-guided masking to ground video features in transcript semantics, CTC loss for transcript-level supervision, and a CRF-augmented anticipation decoder. Experiments on Breakfast, 50Salads, and EGTEA demonstrate that transcript-only supervision can approach and (on Breakfast at 30% observation) even exceed fully supervised methods, establishing the first transcript-based supervision baseline for LTA.

## Strengths
- **First transcript-only baseline for dense LTA, with decisive gap over prior weakly-supervised work.** Table 1 shows TbLTA (deterministic) achieves 29.03 MoC on Breakfast (30% obs), substantially exceeding WS-DA (Zhang et al., 2021) at 15.65 MoC — a method that still required frame-level labels for observed segments. This establishes transcript-only supervision as viable and far more effective than prior weak-supervision approaches.
- **Competitive with and occasionally superior to fully supervised methods on Breakfast.** The deterministic TbLTA (29.03 MoC at 30% obs) surpasses all fully-supervised baselines including ActFusion (28.45), FUTR (26.59), and Cycle Consistency (25.13), demonstrating that transcript-based supervision can capture procedural regularities effectively enough to rival dense annotation.
- **Cross-modal attention with pseudo-label-guided masking is well-motivated and empirically impactful.** The local cross-modal mechanism (Section 3.1, Eqs. 1-2) uses pseudo-labels to construct a binary mask restricting transcript-to-video attention to temporally relevant neighborhoods, with a gated residual update. Ablations (Table 4) show removing cross-attention drops Top-1 MoC by ~1.3 points on 50Salads and ~5.7 points on Breakfast, confirming the design's importance.
- **Well-structured multi-component loss with validated contributions.** The objective decomposes into alignment, segmentation, and anticipation groups (Eq. 3), each addressing distinct weak-supervision challenges. Ablations confirm CTC stabilizes pseudo-labels (~0.6-0.8 point drop when removed), CRF enforces temporal coherence at longer horizons (~4-5 point drop at extended horizons), and the self-supervised duration loss provides meaningful regularization (~3.3 point drop on Breakfast).
- **Transcript supervision benefits rare classes on EGTEA.** Table 2 shows TbLTA achieves 60.11 mAP on rare classes, surpassing supervised Anticipatr (55.10) and Timeception (59.70), suggesting high-level semantic supervision from transcripts can mitigate data imbalance.

## Weaknesses

### Fatal
None.

### Major
- **Ablation study is conducted exclusively on the Top-1 oracle metric, not on the deterministic variant that is the primary comparison point against baselines.** Section 4.3 explicitly states "All ablations are conducted on both Breakfast and 50Salads, and we report results using the Top-1 MoC metric" (line 231). The Top-1 protocol selects the best of K samples against ground truth — an oracle metric that inflates absolute numbers and potentially amplifies the apparent benefit of each component. Meanwhile, the deterministic variant (the one compared against supervised methods in Table 1) is never ablated. This means the reader cannot assess whether the components being ablated (CTC, cross-attention, CRF, duration loss) actually help the deterministic model. Since the stochastic-Mean variant shows no improvement or even degradation over the deterministic variant on 50Salads (19.11 vs 20.92), the gap between Top-1 and deterministic performance is not trivial. Ablation conclusions may not transfer to the model variant used in the main comparison.

### Minor
- **Missing implementation details affect reproducibility.** The binary local mask M construction for cross-attention — specifically the temporal neighborhood size and how it is determined from pseudo-labels — is not specified (line 130-131). The momentum buffer details for the duration loss (coefficient, initialization, interaction with progressive training schedule) are similarly absent. These are central enough to the method to warrant specification in the main paper.
- **EGTEA evaluation is narrow.** Table 2 compares against only two supervised baselines and restricts evaluation to verb prediction rather than the full verb-noun action recognition task, which weakens the evidence for the rare-class claim.
- **Breakfast advantage over supervised methods is not fully isolated from confounds.** TbLTA incorporates DistilBERT embeddings of action labels as an additional modality through cross-modal attention, while supervised baselines use only I3D visual features. The paper also benefits from ATBA pretraining and full-video access during training. Without ablations isolating the contribution of the language modality from the deterministic variant, the claim that transcript *supervision* rather than additional *features* drives the Breakfast advantage remains partially unsubstantiated. The 50Salads results (where TbLTA trails all supervised methods by 4-7 MoC points) further suggest the Breakfast result may be dataset-specific.

### Trivial
- **Qualitative results are limited to two examples** (Figure 3, one per dataset). While informative, they are insufficient to assess systematic failure modes, particularly the acknowledged duration estimation challenge.

## Nice-to-Haves
- Sensitivity analysis for the progressive three-stage training schedule.
- Per-class performance breakdowns on Breakfast and 50Salads to substantiate the claim that the duration loss helps for actions with concentrated duration statistics.
- Computational cost comparison between the proposed three-stage training and fully supervised alternatives, to contextualize the annotation-cost savings.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"The stochastic evaluation conflates oracle selection with model quality"** — Overstated framing. The paper clearly separates deterministic and stochastic variants in Table 1. The Top-1 metric follows established protocol (Abu Farha & Gall, 2019). The actual concern (ablations on Top-1 only) is retained as a Major weakness.
- **"The claim that the model achieves substantially higher accuracy by capturing multiple plausible futures is misleading"** — REMOVED. The stochastic Top-1 metric is standard in LTA literature; the paper explicitly labels these results as stochastic (*) and distinguishes them from deterministic.
- **"ATBA module's internal mechanics deferred entirely to external work"** — REMOVED per rules: the parser strips appendix/supplementary sections where these details exist.
- **"Table 3 (IAS) referenced but absent from main paper"** — REMOVED per rules: the parser strips appendix sections. Table 3 exists in the original submission's appendix.
- **"Table 1 bold/underline/gray annotation scheme is confusing"** — REMOVED as pure formatting nitpick.
- **"Abstract oversells being 'first' given Zhang et al. (2021)"** — REMOVED. Zhang et al. (2021) is semi/weakly-supervised (still uses frame-level labels for observed segments), so the claim that prior LTA was "fully supervised" is technically correct. The introduction (lines 70-76) correctly distinguishes the contribution.
- **"stochastic variant claim at lines 95-96 is misleading since CRF is not fundamentally stochastic"** — REMOVED. The CRF enables sampling multiple hypotheses, a standard approach for capturing uncertainty. The harsh critic is being pedantic about terminology.
- **"No discussion of computational cost"** — REMOVED as scope creep; moved to Nice-to-Haves.

## Novel Insights
None beyond the paper's own contributions. The paper's key insight — that transcript ordering alone can provide sufficient structure to train a dense LTA model through pseudo-label generation and cross-modal grounding — is its own novel contribution to the field.

## Suggestions
- Recomputation of key ablations (at minimum: w/o cross-att and w/o CRF) on the deterministic variant would substantially strengthen the paper by directly connecting ablation conclusions to the main comparative results in Table 1.
- The binary mask construction for cross-attention should be specified in the main paper (neighborhood radius, how it is derived from pseudo-labels), as it is a central architectural component.
- Reporting per-class performance on Breakfast and 50Salads, stratified by duration variance, would directly support the claim about the duration loss's mechanism and reveal whether overall gains are driven by a few easy classes.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>