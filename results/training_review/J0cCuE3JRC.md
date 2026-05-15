Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper proposes Bag of Features for Link Prediction (BFLP), a non-neural model that combines five classical structural similarity indices (Common Neighbors, Jaccard, Salton, Sørensen, Adamic-Adar) with dataset-specific domain features derived from node attributes, and feeds them to an XGBoost classifier. The central claim is that this simple feature-engineering approach matches or outperforms 13 GNN baselines across six benchmark datasets, including the OGBL-COLLAB benchmark.

## Strengths

- **Empirically strong results that challenge the GNN narrative**: BFLP achieves top performance on CITESEER, PHOTO, COMPUTERS, and OGBL-COLLAB (where it reportedly scores 53.49 Hits@50 against the previous GNN-based best of 50.90), directly supporting the paper's hypothesis that current GNNs may not be leveraging neighborhood and feature information as effectively as simpler models. These results are consistent with theoretical expressivity concerns raised in prior work (Xu et al., 2019; Morris et al., 2019).

- **Clear and well-motivated research question**: The paper identifies a genuine gap — the disconnect between GNNs' theoretical expressivity limits (tied to the WL test) and the pervasive assumption that they universally outperform classical methods on link prediction. The hypothesis is clearly stated and the experimental design directly targets it.

- **Honest discussion of limitations**: The paper acknowledges that domain features must be customized per dataset and that no general rule exists for this step, and it proposes a potential future direction (using GNNs to learn domain feature vectors). This self-critical framing is valuable.

- **Practical computational profile**: The paper reports concrete runtimes (30 minutes for OGBL-COLLAB, up to 18 hours for COMPUTERS) and the 𝒪(|𝒱|·k³) complexity, giving practitioners useful information about the trade-offs.

## Weaknesses

### Major

- **GNN baseline results are sourced from prior work without confirming identical experimental conditions**: The paper compares BFLP against 13 GNN models and reports baseline numbers from Li et al. (2023) — a survey/benchmark paper — rather than re-running the GNNs under the same splits, negative sampling, masking protocols, and repetitions used for BFLP. For CORA/CITESEER/PUBMED, the paper follows splits from Zhao et al. (2022); for COMPUTERS/PHOTO, splits from Guo et al. (2022). Whether Li et al. (2023) used exactly these splits is not verified. Since the paper's central claim is that BFLP matches or beats GNNs, this uncontrolled comparison significantly weakens the evidence. While this practice is not uncommon in ML, it is a critical issue here because the headline claim depends entirely on it. For OGBL-COLLAB the concern is partially mitigated by standardized OGB splits, but for the other datasets it remains unresolved. This is the single most important weakness in the paper.

### Minor

- **Domain features are insufficiently specified**: The paper states that "domain features leverage similarity measures derived from the node features" (Section 3.2) and that they are "the relevant similarity measure between the node features" (Section 2.2), but it never specifies what similarity measure(s) are actually used (e.g., cosine similarity, dot product, Euclidean distance) or how they are computed. The ablation study (Table 6) treats "domain features" as a single block, but a reader cannot reproduce or adapt this component without knowing what it is. The customization of domain features across datasets is acknowledged as a limitation, but the paper should document exactly what was done for each dataset.

- **Adaptation to OGBL-COLLAB is not described**: The paper notes (Section 4.1) that "Since OGBL-COLLAB is dynamic and weighted, we needed to adjust our features in this dataset to adapt our method to this context," but provides no description of what adjustments were made. Since the OGBL-COLLAB result is one of the paper's strongest selling points, this omission makes the experiment unreproducible and undermines the reader's ability to interpret the comparison.

- **No standard deviations or confidence intervals in the text**: While the tables (rendered as images) may contain standard deviations, the paper does not discuss statistical significance anywhere. Given that results are reported over 10 or 5 repeated splits, this information is essential for assessing whether BFLP's improvements over GNN baselines are meaningful. The reader cannot tell, for instance, whether BFLP's lead on CORA is 1 percentage point with small variance or 5 points with large variance.

### Trivial

- The connection between the WL test and link prediction is stated rather than argued. The paper cites the standard GNN expressivity literature (Xu et al., 2019; Morris et al., 2019) but does not explain why limitations in *graph isomorphism testing* specifically imply limitations in *link prediction*. This makes the motivation feel generic. The argument can be tightened without changing the experiments.

- "Computationally efficient" is claimed in the conclusion and ablation discussion, but no runtime comparison with GNN training/inference is provided. The reported 18-hour runtime for COMPUTERS may or may not be competitive depending on the GNN being compared.

## Nice-to-Haves

- **Include simple ML baselines**: The paper could compare BFLP against simpler baselines using the same features (e.g., logistic regression, random forest) to isolate the value added by XGBoost over the combination of features alone.

- **Feature importance analysis**: Since XGBoost provides built-in feature importance, showing which structural or domain features drive performance per dataset would give useful insight.

- **Re-run GNN baselines under identical conditions** (acknowledged as a major weakness above; this would need to be done for acceptance, not just a "nice-to-have"). Listed here only to clarify what the paper is missing.

## Removed Points

- **"Method section entirely absent"** — This is an overstatement. The structural features (five similarity indices) are defined with full formulas in Section 2.2. Section 3.2 describes the two categories of features and the overall approach. The domain features are underspecified, but the method is not "entirely absent." This is better captured as a minor weakness (domain features insufficiently specified).

- **"Missing related work citations (Lichtenwalter et al., 2010; L. Li et al., 2018)"** — Per instructions, missing related works are not to be mentioned as weaknesses, as this cannot be verified without external sources.

- **"Variety of formatting/style nitpicks"** — Removed per hard rules.

- **"WL test motivation is too loose"** — This criticism misunderstands the literature: the GNN expressivity papers (Xu et al., 2019; Morris et al., 2019) are about GNNs in general, not just graph isomorphism, and the paper's use of this connection to question GNN superiority in link prediction is standard and reasonable.

- **Strength: "Comprehensive and fair experimental design"** — Dropped because it conflicts with the verified weakness about uncontrolled GNN baseline comparisons, which undermines the fairness claim.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective that the paper's authors have not already stated or implicitly acknowledged. The main value of the reviews is in identifying the severity of the uncontrolled baseline comparison, which the paper's "honest discussion" does not address.

## Suggestions

1. **Re-run all GNN baselines under identical conditions** (same splits, negative sampling, masking, and number of repetitions as BFLP). This is the single most impactful thing the authors can do to support their claim. If this is infeasible, the paper should explicitly acknowledge the limitations of citing external baseline numbers and consider reframing the contribution as a competitive baseline rather than a "beats GNNs" claim.

2. **Specify the domain features precisely**: For each dataset, state exactly what similarity measure(s) on node features were used, how many domain features were generated, and any preprocessing applied. This is essential for reproducibility.

3. **Describe the OGBL-COLLAB feature adaptation**: Provide a clear account of how the structural and domain features were adjusted for the dynamic, weighted setting.

4. **Report standard deviations and, ideally, statistical significance** for all metrics and all datasets.

5. **Replace "computationally efficient" with concrete runtime comparisons** against the GNN baselines on the same hardware, or qualify the claim to avoid misleading readers.

## Score and Decision

The paper tackles a worthwhile question and provides empirical evidence that is suggestive but not fully convincing in its current form. The core idea is solid and the results on OGBL-COLLAB are genuinely interesting. However, the uncontrolled comparison against GNN baselines — the central pillar of the paper's contribution — is a significant evidential gap that undermines the headline claim. Additionally, the domain features and OGBL-COLLAB adaptation are underspecified, harming reproducibility. These issues can be addressed, but they are substantial enough to prevent acceptance in the current submission.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>