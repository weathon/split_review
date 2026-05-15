Now I have a thorough understanding of the paper and have verified the reviewer claims against the text. Let me produce the consolidated review.

## Summary

The paper proposes Density-Based Pruning (DBP), which extends SSP-Pruning to web-scale multimodal datasets by making the per-cluster pruning rate proportional to a cluster "complexity" measure (product of intra-cluster and inter-cluster distances). Applied to LAION-CAT-440M and DataComp Medium with a pipeline of deduplication → CLIP-score filtering → DBP, the method reports strong results: outperforming a full-dataset OpenCLIP-ViT-B/32 baseline while using substantially less training compute, and achieving state-of-the-art ImageNet zero-shot accuracy on the DataComp Medium benchmark.

## Strengths

- **Novel and principled extension of SSP-Pruning.** DBP replaces the fixed cluster-balancing ratio of SSP-Pruning with a per-cluster pruning rate that depends on an intuitive complexity measure (product of intra- and inter-cluster distances). This cleanly addresses the limitation that different concepts have different information densities. The paper provides direct comparisons showing DBP outperforms SSP-Pruning across all tested cluster-balancing ratios (Fig. 5, right) and on LAION-CAT-440M (Table laion280_cbp_vs_ssp_pruning).

- **Demonstrated compute savings with maintained or improved accuracy.** On LAION-CAT-440M, the DBP-112M model (27.7% of the data/compute) achieves strong ImageNet zero-shot accuracy. The paper shows this model outperforms the full LAION-CAT-440M baseline on ImageNet, VTAB, and ImageNet distribution-shift tasks while using only 27%–41% of the training cost (Fig. 1). This substantiates the claim that smaller, well-pruned datasets can match or exceed larger ones.

- **New state-of-the-art results on DataComp Medium.** The method achieves top ImageNet zero-shot accuracy on the DataComp Medium leaderboard and outperforms the previous best (T-MARS) on three of four task families (ImageNet, VTAB, Retrieval). This demonstrates that the pipeline transfers to a raw, unfiltered web-scale benchmark.

- **Systematic hyperparameter ablations on a development set.** All DBP hyperparameters (number of nearest neighbors for inter-cluster distance, softmax temperature, number of k-means clusters, cluster balancing ratio) are ablated on LAION-50M with clear results presented in Fig. 7, providing practical guidance for adoption.

- **Exploration of embedding modalities.** The paper compares image embeddings (DINOv2-L/14, CLIP-B/16), caption embeddings (CLIP-B/16, Sentence-BERT), and multimodal BLIP ITM embeddings, finding DINOv2-L/14 works best — an actionable finding for practitioners.

## Weaknesses

### Fatal

None.

### Major

- **Inconsistent numerical claims across the paper.** The abstract and conclusion claim a "1.1 p.p." improvement over "the LAION-trained OpenCLIP-ViT‑B/32 model," and the Fig. 1 caption reports 64.1% vs 63.0% (a 1.1 p.p. gap). However, Section 5.1 states that "training on the 112M subset outperforms OpenCLIP‑B/32 on ImageNet (65.44% vs 62.92%)," which is a 2.52 p.p. gap. The paper offers no explanation for this discrepancy or what each baseline refers to (e.g., the official OpenCLIP release vs. a model trained by the authors). This inconsistency erodes confidence in all reported numbers and must be resolved.

### Minor

- **Headline comparison conflates the effects of CAT pre-filtering and DBP.** The abstract foregrounds a comparison against the "LAION-trained OpenCLIP-ViT‑B/32 model" trained on raw LAION-400M, while the method starts from LAION-CAT-440M — a dataset already filtered via caption complexity, action, and text-spotting. Although the paper *does* include a CAT-440M baseline (green line in Fig. 1) and states DBP outperforms it, the headline framing obscures that a non-trivial portion of the gap over raw LAION-400M is due to the CAT pre-filtering, not DBP alone. Reframing the headline claim around the controlled CAT-440M baseline would give readers a more accurate picture of DBP's marginal contribution.

- **Missing ablation isolating DBP on DataComp Medium.** The DataComp pipeline combines deduplication (SemDeDup), CLIP-score filtering, and DBP. The paper achieves SOTA with this combined pipeline, but there is no controlled comparison on DataComp (e.g., dedup+CS vs. dedup+CS+DBP with the same training budget and embeddings) that would attribute the gain to DBP. The LAION ablations provide indirect evidence, but a direct DataComp ablation is needed to substantiate the SOTA claim cleanly.

- **Hyperparameter tuning on a proxy setting.** All hyperparameter ablations (Fig. 7) are conducted on LAION-50M with only 5 training epochs, whereas the final LAION-CAT-440M experiments use 32 epochs and the DataComp experiments use a fixed seen-examples budget. The paper does not verify whether the optimal values (τ=0.1, l=20, k=500, balancing ratio=0) transfer to these larger-scale, longer-training settings. While the proxy approach is practical, a sensitivity check on the final setting would strengthen confidence.

- **Thin evidence for the "longer training helps retrieval/distribution-shift" analysis.** The claim that retrieval and distribution-shift tasks benefit more from longer training is supported by only one comparison point (training the 166M subset with two different numbers of seen examples). A sweep across dataset sizes would make this more convincing.

### Trivial

None.

## Nice-to-Haves

- A qualitative example showing clusters with high vs. low complexity and the corresponding number of samples kept per cluster would help readers build intuition for the method.
- A histogram of cluster complexity Cⱼ across the 500 clusters would show whether the measure actually varies meaningfully.
- A comment on why DINOv2 (a vision-only encoder) outperforms multimodal embeddings for clustering multimodal data would be informative for practitioners.

## Removed Points

- **Quadratic program formulation in commented-out block**: The harsh critic flags that the QP objective (Eq. 1) is inside an `\iffalse` block. Per the instructions, the parser strips these sections from all papers; they exist in the original submission. **[Removed per parser artifact rule]**
- **"Only the 112M model is highlighted"**: The paper shows results for 84M, 112M, 166M, and 222M in Fig. 1. The text highlights 112M as the best, but the full range is displayed. **[Factually inaccurate — data for multiple subset sizes is presented in the figure.]**
- **"The 1.1 p.p. claim is based on an uncontrolled comparison"**: The paper includes the CAT-440M baseline and explicitly states it outperforms it (line 217). The comparison against raw OpenCLIP is an *additional* asymmetric comparison, not the sole basis of the paper's claims. The asymmetry favors the baseline (more training data) and per the rules, such points should be removed. However, the *framing* concern about the headline is kept above as a minor weakness. **[Overstated — the CAT-440M baseline is present and acknowledged.]**
- **"The main result is invalid"**: This is hyperbolic. The core contribution (DPB improves over SSP-Pruning and achieves strong results with less compute) is supported by controlled comparisons. The framing issue and numerical inconsistency are real but do not invalidate the paper. **[Hyperbolic characterization removed; the substantive concerns about framing and inconsistency are kept above.]**

## Novel Insights

The reviews converge on an important tension: the paper's DBP method is genuinely novel and the ablations against SSP-Pruning are clean, but the headline numbers are double-reported (1.1 p.p. vs. 2.52 p.p.) and the abstract's marquee comparison juxtaposes a CAT-filtered starting point against a raw-data baseline without sufficiently highlighting that asymmetry. The harsh critic correctly identifies that the marginal gain over the controlled CAT-440M baseline is more modest than the paper's 1.1 p.p. headline suggests, but overstates the severity — the paper does include the CAT baseline, and the compute-efficiency achievement (matching/besting a larger-dataset model with far less compute) remains impressive even when measured against CAT-440M. None of the weaknesses are fatal; they all concern presentation, framing, or missing ablations that the authors could address in a revision.

## Suggestions

1. **Clarify the numerical inconsistency.** Report a single, consistent set of numbers for the headline result. State explicitly which baseline (OpenCLIP official release vs. author-trained) the comparison refers to, and which subset size and metric produce each number.
2. **Reframe the headline around the controlled CAT-440M comparison.** State DBP's improvement over LAION-CAT-440M (the direct baseline) upfront, then note the additional comparison against raw OpenCLIP to contextualize compute savings.
3. **Add a DataComp ablation** isolating DBP's contribution from deduplication and CLIP-score filtering, using the same embeddings and training budget.
4. **Verify key hyperparameters** (τ, l, k) with a sensitivity check under the full 32-epoch training schedule rather than relying solely on the 5-epoch proxy.

## Score and Decision

The paper makes a genuine contribution — DBP is a sensible, novel improvement over SSP-Pruning, validated on LAION and DataComp with careful ablations. The main issues are presentation (inconsistent numbers, framing that conflates CAT pre-filtering with DBP's own contribution) and a missing DataComp ablation. These are addressable in revision and do not undermine the core contributions. The paper is a solid, above-threshold submission.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>