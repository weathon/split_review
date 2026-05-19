Now I have all the evidence needed to write the final review. Let me synthesize everything.

---

## Summary

This paper proposes Simi-Mailbox, a post-hoc calibration method for GNNs that groups nodes by both neighborhood representational similarity (computed via logit dot products) and confidence, then applies group-specific temperatures. The motivation is that existing GNN calibration methods (CaGCN, GATS) fail to properly adjust confidence across different levels of neighborhood similarity. The paper validates this via analysis showing that nodes with similar neighborhood topology and confidence share similar calibration errors (lower variance), and empirically demonstrates state-of-the-art ECE on 15 out of 16 configurations across diverse datasets and architectures.

## Strengths

- **Novel identification of a genuine failure in prior GNN calibration methods**: Section 4 and Figure 1 concretely show that CaGCN and GATS systematically fail to adjust confidence in low-neighborhood-similarity regions, with CaGCN showing a 16.34% gap between accuracy and calibrated confidence for low-similarity nodes in the highest confidence bin. This is a specific, verified finding that goes beyond generic criticism.

- **Strong empirical performance**: Table 2 shows Simi-Mailbox achieves the best ECE on 15 of 16 configurations across GCN and GAT architectures, including first-time sub-1% ECE on Cora (GCN) and sub-0.8% on PubMed and Coauthor CS. These are concrete, sizable improvements over existing methods.

- **Scalability demonstrated on large graphs**: Tables 3 and 4 show that Simi-Mailbox maintains ECE below 1% on Arxiv and Reddit while reducing calibration runtime by up to 182 seconds compared to GATS, supporting the claim of practical deployability.

- **Empirical grounding of the grouping intuition**: Table 1 shows that variance of calibration error within neighborhood-similarity sub-intervals (0.52 for CoraFull GCN) is substantially lower than node-wise variance (6.47), providing direct quantitative support for the claim that nodes with similar topology and confidence share analogous calibration errors.

## Weaknesses

### Fatal
None.

### Major

- **Unvalidated correspondence between the analysis similarity measure and the method's similarity measure**: The motivating analysis (Section 4, Eq. 4) defines neighborhood prediction similarity as the *discrete label-based* fraction of neighbors sharing the same predicted label: $s(i) = \sum_{j\in\mathcal{N}_i} \mathbb{1}[\hat{y}_i = \hat{y}_j] / |\mathcal{N}_i|$. The method (Section 5.2, Eq. 6) defines neighborhood affinity via a *continuous logit-based* representational similarity: $\mathcal{M}^{simi}(i) = \frac{1}{|\mathcal{N}_i|}\sum_{j\in\mathcal{N}_i} \sigma(z_i^\mathsf{T} z_j)$. The variance analysis in Table 1 (which grounds the method's design) also uses the label-based $s(i)$ measure. The paper never demonstrates that the two measures capture the same topological property or that groups formed by the logit-based measure recover the calibration-error patterns observed with the label-based measure. This is a logical gap in the paper's evidentiary chain from motivating observation to implemented method.

### Minor

- **Underspecified hyperparameters with no sensitivity analysis**: The method requires the number of clusters $N$ (for KMeans) and the regularization weight $\lambda$ (for $\mathcal{L}_{simi}$). Neither value is reported anywhere in the paper, nor is any ablation or sensitivity study provided. This makes reproduction difficult and leaves open the question of how robust the method is to these choices. The paper also contains an ambiguous phrase ("optimal calibration models are selected based on the lowest validation ECE on the training set," line 184) that appears to conflate training and validation sets.

- **No variance or statistical significance reported**: All ECE results in Tables 2 and 3 are single point estimates with no error bars, standard deviations, or indication of multiple runs. Given that some improvements are small fractions of a percent (e.g., CoraFull GCN: CaGCN 2.73 vs. Simi-Mailbox 2.64), it is impossible to assess the significance of the results. Multiple runs with standard deviations are needed to establish reliability.

- **Motivating analysis limited to one dataset**: The detailed analysis in Section 4 (Figure 1, Table 1) is conducted only on CoraFull with GCN. While this is sufficient to illustrate the identified failure patterns, showing the analysis on at least one additional dataset would strengthen the claim that this is a general problem rather than a dataset-specific artifact.

- **Missing experimental comparison against relevant grouping-based calibration methods**: The Related Work section (line 31) cites multicalibration (Hébert-Johnson et al., 2018) and semantic partitioning (Yang et al., 2023) as grouping-based calibration works. Since Simi-Mailbox is itself a grouping-based method, a comparison or clear justification for their exclusion would help isolate the contribution. (That said, these are general ML calibration methods not designed for graph data, so the omission is understandable but worth noting.)

### Trivial

- The paper states "the optimal calibration models are selected based on the lowest validation ECE on the training set" (line 184) — this appears to be a writing error; the intended meaning is the lowest ECE on the validation set.

- The method uses the sigmoid of raw logit dot products in $\mathcal{M}^{simi}(i)$ without discussing sensitivity to logit magnitudes. While min-max normalization of the resulting mailbox values is applied before clustering, the raw dot product can be sensitive to output scale.

## Nice-to-Haves

- **Ablation on the auxiliary loss $\mathcal{L}_{simi}$**: How much does the $\lambda$ regularization contribute versus using KMeans grouping with cross-entropy alone?
- **Comparison against a baseline that groups by confidence bins only** (without the similarity dimension) to isolate the benefit of adding topology.
- **Correlation analysis** between the label-based similarity $s(i)$ and the logit-based similarity $\mathcal{M}^{simi}(i)$ to validate the connection between analysis and method.
- **Quantitative subgroup evaluation**: Reporting per-similarity-level ECE for all methods would strengthen the qualitative Figure 3.
- **Comparison of alternative grouping criteria** (e.g., by degree, by homophily ratio) to show that the chosen (similarity + confidence) pairing is the most effective.

## Removed Points

These points from the harsh critic are flagged to be removed; treat them with caution:

1. **Speculation about TS performance on Reddit**: The critic asked "whether TS alone (single temperature) also achieves near-perfect calibration on this dataset" as a hypothetical. TS results are reported in Table 3 (the critic simply does not have access to the numerical values). This is not a verifiable weakness.

2. **"Improved runtime should be contextualized"**: The paper reports runtime in seconds (Table 4), which is standard. The critic's request for further "contextualization" without specifying what is needed is too vague to retain.

3. **Criticism that the abstract claim is too strong and only supported for two methods on one dataset**: The paper uses CoraFull as an illustrative analysis (standard practice in ML papers) and then validates generality experimentally across 10 datasets. The scope is clearly stated. This criticism is overblown.

4. **Suggestion that the variance analysis "risks being somewhat circular"**: The analysis validates that grouping by neighborhood similarity + confidence reduces variance — that is precisely the claim being tested. It is not circular; it is self-consistent. The critic's suggestion to compare against alternative grouping criteria is a nice-to-have, not a weakness.

## Novel Insights

The two reviewers complement each other usefully: the harsh critic correctly identifies a real gap between the paper's analysis measure and its method measure that the strength finder's positive framing glosses over. Conversely, the strength finder accurately identifies that the paper's empirical results are genuinely strong — 15/16 SOTA is not noise. The intersection of these views suggests the paper's contribution is real but the argument connecting motivation to method needs a missing link (correlation analysis between the two similarity measures). Neither reviewer identified this as fatal, and neither did the paper itself; this is a gap that the meta-review can surface as the single most actionable improvement.

## Suggestions

1. **Validate the similarity measure connection**: Run a correlation analysis between $s(i)$ (label-based) and $\mathcal{M}^{simi}(i)$ (logit-based) on at least 2-3 datasets to confirm the method's grouping captures the same topological variation that the motivating analysis relies on. This is the single highest-leverage improvement.

2. **Report hyperparameter values and add sensitivity analysis**: Disclose the values of $N$ and $\lambda$ used in experiments, and include a figure showing how ECE varies with $N$ (e.g., 2 to 20) and $\lambda$ (e.g., 0 to 1) on at least two datasets.

3. **Add variance over multiple runs**: Report mean and standard deviation over 5-10 independent runs for all main results. This is especially important for the small-margin improvements.

4. **Fix the ambiguous wording** on line 184 about "lowest validation ECE on the training set."

## Score and Decision

The paper presents a well-motivated, novel calibration method with strong empirical evidence across diverse settings. The core weakness is the unvalidated link between the analysis measure and the method measure, but this is addressable (not fatal), and the empirical results strongly suggest the method works regardless. The paper makes a clear contribution to GNN calibration.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>