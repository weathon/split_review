Now I have thoroughly read the paper and analyzed all reviewer claims against the actual paper content. Let me produce the final consolidated review.

---

## Summary

This paper observes that real-world graphs contain a mixture of homophilic and heterophilic nodes, and that applying a single global filter (even a learnable one) is suboptimal. The authors provide a theoretical motivation using a mixed-pattern CSBM model, then propose Node-MoE, a framework that uses a Mixture-of-Experts architecture to blend different spectral filters per node. A gating model takes node features and neighbor-difference features to assign weights, and multiple ChebNetII experts with different initializations provide diverse filters. Experiments on 7 benchmark datasets show that Node-MoE achieves the best average rank (1.29), outperforming strong baselines including single ChebNetII (rank 3.86).

## Strengths

1. **Empirical demonstration that graphs exhibit mixed structural patterns**: Using node homophily histograms (Figure 1) and community-level homophily analysis (Figure 2), the paper shows that datasets like Cora and Chameleon each contain nodes spanning a wide range of homophily values, and that different communities within the same graph show substantially different homophily levels. This evidence directly motivates why a single global filter is insufficient.

2. **Theoretical motivation via mixed-pattern CSBM (Theorem 1)**: The paper extends the CSBM to model graphs with both homophilic and heterophilic patterns and proves that (i) a global low-pass filter incurs a loss lower-bounded by \(\frac{R(q_1-p_1)}{2(q_1+p_1)}\|\boldsymbol{\mu}-\boldsymbol{\nu}\|(1+o_d(1))\) on heterophilic nodes, while (ii) oracle node-wise filtering achieves linear separability with probability \(1-o_d(1)\). This provides a clean theoretical rationale for pursuing node-wise filtering.

3. **Strong empirical results with best average rank**: In Table 1, Node-MoE achieves the best average rank (1.29) across 7 datasets, outperforming all baselines including ChebNetII (3.86), GCNII (5.43), GloGNN (5.43), and GMoE (6.57). The largest gains appear on heterophilic datasets (Chameleon: +2.50%, Squirrel: +5.19%), which is precisely where a single learnable filter would struggle most.

4. **Interpretable gating behavior**: Analysis on Chameleon (Figures 3-4) shows that one expert learns a low-pass filter, the other a high-pass filter, and the gating model assigns higher weight to the high-pass filter for low-homophily (heterophilic) nodes and higher weight to the low-pass filter for high-homophily nodes. This directly confirms that the gating model learns to match filters to node patterns as intended.

5. **Well-designed gating mechanism validated by ablation**: The gating model uses a composite input \([X, |AX-X|, |A^2X-X|]\) with a GIN backbone, motivated by the need to capture neighborhood pattern differences and community structure. The ablation (Figure 6) shows this design significantly outperforms a simple MLP gating baseline, and the Top-1 gating variant achieves comparable performance to soft gating while maintaining single-expert efficiency.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by evidence, and no flaw invalidates them.

### Minor

1. **Claims of "significant" improvement are not backed by statistical tests.** The paper states that Node-MoE "significantly outperforms" ChebNetII, but Table 1 shows modest deltas on several datasets: Cora (Δ = 0.67%, stds overlapping), PubMed (Δ = 0.65%), Actor (Δ = 0.61%). On PubMed, GCNII (90.17) actually exceeds Node-MoE (89.58). Without pairwise significance tests (e.g., t-tests or confidence intervals over the 3 runs × 10 splits), the reader cannot distinguish genuine gains from random variation. The average-rank argument is meaningful, but the specific "significant outperformance" claim is not rigorously supported. The paper should report p-values or confidence intervals for the key comparisons.

2. **Gap between the theoretical motivation and the learned gating mechanism.** Theorem 1 shows that *oracle* node-wise filtering (where pattern labels are known) achieves linear separability. The proposed Node-MoE must learn these assignments without pattern labels via a gating model that uses \([X, |AX-X|, |A^2X-X|]\) and a GIN. The paper acknowledges this challenge (Section 3: "without ground truth on node patterns"), but does not analyze when or whether the gating model can recover the oracle assignments, nor quantify how misassignments degrade performance. A small-scale simulation on synthetic CSBM graphs comparing oracle filtering to Node-MoE's learned assignment would directly bridge this gap and substantially strengthen the paper.

3. **Limited ablation of architectural choices.** Only the filter smoothing loss weight \(\gamma\) is systematically ablated (on two datasets). The number of experts (2, 3, 5) is mentioned in settings but not analyzed — e.g., does performance saturate at 2 experts, or do more experts help on harder datasets? The Top-K gating uses \(k=1\) exclusively; it is unclear whether \(k=2\) or \(k=3\) would improve performance at modest computational cost. A broader sweep over these design dimensions would strengthen confidence in the framework's robustness.

4. **Expert diversity shown on only one dataset.** The filter analysis (Figure 3) demonstrating that experts learn distinct low-pass and high-pass filters is presented only for Chameleon. While compelling, the paper does not verify that experts remain diverse across datasets or random seeds. Mode collapse is a well-known risk in MoE, and additional evidence (e.g., filter similarity metrics on CiteSeer or Squirrel) would substantiate that the differentiated initialization + smoothing loss reliably prevents it.

5. **No computational complexity comparison.** The paper claims Top-1 gating achieves "similar efficiency to a single expert," but provides no wall-clock time, FLOPs, or parameter count comparisons. The gating model is a GIN (not a lightweight MLP), which adds overhead. Reporting training/inference time per epoch for soft gating, Top-1 gating, and the single ChebNetII baseline would make the efficiency claim concrete.

### Trivial

- **Gating input design not benchmarked against alternatives.** The composite input \([X, |AX-X|, |A^2X-X|]\) is motivated heuristically. While it outperforms MLP-based gating, the paper does not compare against alternative encoding schemes (e.g., degree-normalized differences, random-walk features). A brief comparison would clarify whether the specific choice matters or whether any pattern-sensitive encoding works.

## Nice-to-Haves

- A small-scale CSBM simulation experiment that compares oracle node-wise filtering to Node-MoE's learned gating, to directly bridge Theorem 1 and the proposed method.
- Results on one additional large-scale dataset (e.g., ogbn-products) to further test scalability.
- An ablation where all experts are initialized identically, to isolate the benefit of the MoE structure itself from the benefit of diverse starting points.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism that "node-wise filtering" is a misleading term because experts are global and only gating weights are node-specific.** This misreads the paper's contribution. In an MoE framework, each node receives a distinct convex combination of expert filters; the effective filter applied to each node is different. This *is* node-wise filtering in the practical sense. The paper clearly describes the gating mechanism in Section 3.2 and does not misrepresent it. [Reason: Strawman weakness; the paper's framing is accurate and standard for MoE work.]

2. **Criticism about the choice of experts all being ChebNetII (framed as a weakness rather than a design choice).** The paper deliberately selects ChebNetII as the expert backbone because of its efficient learnable filters, and differentiates experts via initialization. This is a defensible design choice within the paper's scope. The relevant question — whether experts remain diverse — is already kept as a minor weakness above. [Reason: The underlying concern (expert diversity) is already captured in the minor weaknesses section.]

3. **Criticism about reporting filter analysis only on Chameleon.** This is already captured in minor weakness #4 above with more precision. [Reason: Duplicate.]

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs do not contribute novel observations about the paper that the paper itself does not already state.

## Suggestions

1. **Add statistical significance testing.** For the primary comparison (Node-MoE vs. ChebNetII) and Node-MoE vs. the overall best baseline on each dataset, report p-values from paired t-tests or Mann-Whitney U tests over the 30 runs (3 runs × 10 splits) to substantiate the "significantly outperforms" claim. Alternatively, report effect sizes and confidence intervals.

2. **Add a CSBM simulation experiment.** Generate synthetic graphs under the mixed-pattern CSBM (Definition 1), compare oracle node-wise filtering to Node-MoE's learned gating, and report how well the gating model recovers the ground-truth pattern assignments (e.g., via accuracy or mutual information). This would directly close the theory-method gap.

3. **Report wall-clock time or FLOPs.** Add a table or paragraph comparing training/inference time per epoch for Node-MoE (soft gating, Top-1 gating) vs. ChebNetII, to substantiate the efficiency claim for Top-K gating.

4. **Expand ablation studies.** Report performance for different numbers of experts (2, 3, 5) on at least two datasets, and consider adding a brief analysis of \(k=2\) in Top-K gating. Show expert filter responses on at least one additional dataset (e.g., CiteSeer or Squirrel) to verify that experts remain diverse.

## Score and Decision

**Originality:** The paper adapts MoE to node-wise spectral filtering in GNNs, which is a reasonably novel combination. The theoretical CSBM analysis with mixed patterns is a clean contribution.

**Importance:** The problem — graphs with mixed homophilic/heterophilic patterns — is well-motivated and practically relevant. Node-wise filtering is a natural direction.

**Claims:** Generally well-supported by experiments, though the "significant outperformance" claim needs statistical backing. The theory-motivation gap is acknowledged but not fully closed.

**Soundness:** The experiments are standard and the analysis (Figures 3-4) convincingly shows the gating model works as intended. Weaknesses are in completeness (ablation scope, significance testing), not correctness.

**Clarity:** The paper is well-written and the framework is clearly explained.

**Value:** The framework is simple, flexible, and achieves strong empirical results. The analysis of gating behavior provides useful insights.

The paper makes a solid contribution. The core claim — that node-wise filtering via MoE outperforms single-filter approaches — is supported by the best average rank across 7 datasets and the interpretable gating analysis. The weaknesses are matters of rigor and completeness, not fundamental flaws. With the suggested additions (statistical tests, broader ablations, complexity comparison), the paper would be significantly stronger. In its current form, the contribution stands and warrants acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>