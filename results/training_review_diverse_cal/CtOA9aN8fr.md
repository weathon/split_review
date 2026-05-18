Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes Density-Based Pruning (DBP), an extension of SSP-Pruning for web-scale multimodal datasets. The key idea is that different concept clusters in a dataset have different complexities, so they should be pruned at different rates. DBP uses a cluster complexity measure (inter-cluster distance × intra-cluster distance) to determine how many samples to keep from each cluster, then solves a quadratic program to satisfy the target size. Experiments on LAION show that training on a 112M DBP-pruned subset outperforms the OpenCLIP-ViT-B/32 baseline (65.44% vs. 62.92% ImageNet zero-shot) with 27.7% of the compute. On DataComp Medium, it achieves a new state-of-the-art ImageNet zero-shot accuracy and competitive results across 38 evaluation tasks.

## Strengths

- **Significant data efficiency gains**: Training on a 112M subset produced via deduplication + DBP from LAION-CAT-440M outperforms the full OpenCLIP-ViT-B/32 model (trained on LAION-400M) on ImageNet zero-shot by 1.1 p.p. while using only 27.7% of the training compute (Fig. 1, Section 5.1). Critically, the paper also shows DBP-pruned datasets outperform training on the *full* LAION-CAT-440M dataset at 27%–50% of the compute, isolating the method's value from the upstream CAT filter.

- **New state-of-the-art on DataComp Medium**: DBP achieves a new SOTA on the DataComp Medium benchmark for ImageNet zero-shot accuracy and outperforms T-MARS on three of four task families (ImageNet, VTAB, Retrieval), as shown in Table 1 (Section 5.2).

- **Principled concept-specific pruning**: DBP replaces SSP-Pruning's fixed cluster balancing ratio with a complexity-aware allocation (inter-cluster distance × intra-cluster distance, Eq. 1–2). Ablations on LAION-50M (Fig. 4 right) show DBP consistently outperforms SSP-Pruning across all cluster balancing ratios, and the best result is obtained without any balancing—demonstrating that the complexity measure genuinely captures informativeness.

- **Thorough hyperparameter analysis**: The paper provides systematic ablations on LAION-50M for number of nearest neighbors, cluster balancing ratio, temperature, and number of clusters (Fig. 7), with clear justification for final choices.

- **Generality across model scales**: DBP outperforms CLIP-score filtering for CLIP-S/32, CLIP-B/32, and CLIP-L/14 (Section 5.3, Table 2), showing the method is not tied to a single architecture.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Headline comparison conflates multiple filtering stages.** The abstract's claim of "outperform[ing] the LAION-trained OpenCLIP-ViT-B/32 model on ImageNet zero-shot accuracy by 1.1p.p." attributes the gain to the overall pipeline (CAT + SemDeDup + DBP), not DBP alone. The paper *does* include the fairer internal baseline (LAION-CAT-440M full training, green line in Fig. 1) where DBP-pruned subsets clearly win, which is the more important comparison. However, the abstract and introduction do not distinguish between these two comparisons, potentially misleading readers about what fraction of the gain comes from DBP versus the upstream CAT filter and deduplication. The authors should restructure the headline claim to foreground the comparison against CAT-440M (the controlled baseline) and relegate the OpenCLIP comparison to an end-to-end system result.

- **No random subsample baseline on the large-scale LAION experiment.** On LAION-DeDup-280M, DBP prunes to 84M–222M and shows that 112M outperforms the full CAT-440M dataset. However, the paper does not report the result of taking a *random* subsample of the deduplicated dataset at the same size (e.g., a random 112M from 280M). Existing work (including DataComp) has shown that random subsampling can itself improve performance in certain settings. The SemDeDup-280M baseline partially addresses this concern (showing DBP-112M beats the full 280M deduplicated dataset), and the LAION-50M experiments include DBP vs. CLIP-score and SSP-Pruning comparisons. But for the headline large-scale result, a random-subsample control would cleanly isolate the benefit of DBP's selection from the effect of using less data. This is the single most impactful missing experiment.

- **Quadratic program formulation is not visible in the main text.** The method section (Section 3) describes the QP conceptually ("sample as close as possible to P_j while honoring the dataset constraints") but the actual optimization problem (Eq. 3 in the extracted text) is enclosed in an `\iffalse` block that would not appear in the compiled PDF. While the problem is a standard constrained least-squares minimization and the solver (`qpsolvers`) is cited, the full formulation should be presented explicitly in the paper. Readers should not need to reverse-engineer the QP from a conceptual description.

- **DataComp SOTA claim needs qualification.** The paper correctly notes (Section 5.2) that T-MARS still leads on ImageNet distribution shifts (62.3 vs. 62.1). The abstract's phrasing—"a new state-of-the-art ImageNet zero-shot accuracy"—is appropriately qualified, but some passages (e.g., "beat the current state of the art reported in the literature in most categories") are less precise. Given small margins (0.2–0.5 p.p.), the authors should also report whether any results come from single runs and note the lack of variance estimates.

- **Optimal number of clusters may not transfer from LAION-50M to LAION-280M.** The hyperparameter k=500 is selected on LAION-50M (Fig. 7d) and used without verification on the 5.6× larger LAION-DeDup-280M. The paper does not discuss whether optimal k scales with dataset size or should be re-tuned. A brief discussion or sensitivity check would strengthen the method's practical guidance.

- **Cost of the pruning pipeline itself is not reported.** A major selling point is reduced training cost, but the paper does not report the compute required for the pruning pipeline: embedding ~280M images with a DINOv2-L/14 model, running k-means on 500 clusters, and solving the QP. While this cost is plausibly small relative to full CLIP training, it should be quantified.

### Trivial

- Fig. 1 caption refers to "LAION-400M" while the text uses "LAION-CAT-440M" as the starting point. The relationship between these numbers should be clarified in the caption.

## Nice-to-Haves

- On the LAION-50M experiments, training the 30M DBP subset for 45 epochs closes the gap to the full 50M dataset (Fig. 5 left). A similar experiment on the large-scale 112M DBP subset—training for more epochs to match the total examples seen by the 166M model—would directly test the hypothesis that retrieval/distribution-shift tasks primarily benefit from more iterations rather than more data.

- The analysis shows DINOv2-L/14 embeddings outperform CLIP and BLIP embeddings for clustering (Fig. 5 right). A brief discussion of whether this advantage could come from data overlap (DINOv2 was trained on LVD-142M, which may overlap with LAION) would be a useful caveat.

## Removed Points

These points were flagged for removal; treat them with caution:

- **Wrap-figure formatting issues (Harsh Critic's "Other Observations" bullet 3)**: Removed as a formatting artifact.
- **"The paper's analysis... is useful but qualitative" (Harsh Critic's "Other Observations" bullet 1)**: The paper provides quantitative evidence (0.9 p.p., 0.8 p.p., etc.) for the claim, not just qualitative reasoning. This criticism is partially inaccurate.
- **"The paper does not discuss potential data contamination from the DINOv2 encoder"**: The calibration data does not confirm this is a standard concern for this paper type. This is speculative and moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally new perspective on the method that the authors themselves do not already articulate.

## Suggestions

1. **Add a random-subsample control on LAION-DeDup-280M.** Report ImageNet zero-shot accuracy for a random 112M subset (and potentially 166M) drawn from LAION-DeDup-280M. This is the single most important experiment to isolate DBP's contribution from the effect of simply using less data.

2. **Restructure the headline claim.** In the abstract and introduction, lead with the controlled comparison (DBP-pruned subset beats full CAT-440M training at lower compute) and present the OpenCLIP comparison as an end-to-end system result. This would avoid any perception of cherry-picking baselines.

3. **Present the QP formulation explicitly in the main text.** At minimum, state the objective (minimize squared deviation from target cluster sizes) and constraints (total size N, box constraints 1 ≤ x_j ≤ M_j). Currently this is inside a commented block.

4. **Report the compute cost of the pruning pipeline.** Provide GPU-hours for: embedding the full dataset with DINOv2-L/14, k-means clustering, and QP solving. This is needed to give a complete picture of the cost savings.

5. **Add variance or multi-seed results for the DataComp Medium comparisons**, since the margins over T-MARS are small (0.2–0.5 p.p.). Even noting that runs were single-seed would help readers calibrate confidence.

## Score and Decision

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**