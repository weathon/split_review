## Summary

The paper presents HYPOGENEAGENT, an LLM-driven framework that transforms cluster annotation and resolution selection in single-cell/Perturb-seq analyses into a quantitatively optimizable task. The method uses an LLM agent to generate GO-based hypotheses for each cluster, then computes intra-cluster agreement and inter-cluster distinctiveness from sentence embeddings of these hypotheses to derive a Resolution Score that identifies biologically meaningful clustering granularities. The authors validate their approach on a K562 CRISPRi Perturb-seq dataset, showing that their Resolution Score selects clustering resolutions that align with known biology better than traditional metrics like silhouette score and modularity.

## Strengths

- **Novel integration of LLM reasoning with clustering resolution selection**: The paper addresses a genuine gap in single-cell analysis—the subjective and heuristic nature of resolution selection—by proposing a principled, biology-aware optimization criterion. This is a creative and timely contribution that bridges unsupervised clustering with automated functional annotation.

- **Well-defined, interpretable metrics**: The intra-cluster agreement (ICS) and inter-cluster distinctiveness (ICD) metrics are clearly defined, intuitive, and grounded in semantic similarity of LLM-generated hypotheses. The Resolution Score combining these two components provides a single objective function for resolution optimization.

- **Comprehensive ablation studies on prompt design and model selection**: Stage 1 experiments systematically compare different LLM backbones (GPT-4o, GPT-o3, GPT-5, Gemini variants), embedding methods (OpenAI, SapBERT, Nomic), prompt designs (general vs. hypothesis), and temperature parameters. This provides useful guidance for practitioners deploying similar systems.

- **Demonstration on both gene-expression and perturbation levels**: The method is applied to two distinct clustering tasks (GEX-level and perturbation-level), showing versatility across different data modalities within the Perturb-seq framework.

## Weaknesses

### Fatal
None.

### Major

- **Limited validation scope**: The method is tested on only one dataset (K562 CRISPRi Perturb-seq from Replogle et al. 2022). While this is a well-established benchmark, a single dataset is insufficient to demonstrate generalizability across different cell types, tissues, experimental conditions, and sequencing technologies. The paper acknowledges this limitation but does not provide any additional validation.

- **No quantitative comparison of biological relevance against baselines**: The paper claims that HYPOGENEAGENT selects resolutions that "exhibit alignment with known pathway compared to classical metrics," but this claim is supported only by qualitative visual inspection of UMAP plots and box plots. There is no quantitative metric (e.g., enrichment of known perturbation-gene associations, overlap with curated cell-type markers, or agreement with ground-truth labels) that directly compares the biological validity of clusters selected by HYPOGENEAGENT versus those selected by silhouette score, modularity, or functional enrichment. The comparison in Section 4.4 merely shows that different methods select different resolutions, not that HYPOGENEAGENT's choice is biologically superior.

- **The Resolution Score's weight parameter w is arbitrarily chosen**: The authors set w = 1/3 based on "a small grid search" that "found to give a stable ordering of resolutions across data sets." However, only one dataset is tested, and the sensitivity analysis in Figure S5 shows that different clusters respond differently to w. The choice of w directly affects the optimal resolution, and the paper does not provide a principled way to select this hyperparameter or demonstrate that the method's conclusions are robust to reasonable variations in w.

- **Computational cost and scalability are not addressed**: The method requires running an LLM (GPT-o3, a costly model) on every cluster at every resolution, generating up to 5 hypotheses per cluster. For a dataset with 10 resolutions and up to 20 clusters per resolution, this could require 200+ LLM calls. The paper does not report API costs, runtime, or discuss how this scales to larger atlases (e.g., Human Cell Atlas with millions of cells and hundreds of clusters). The authors acknowledge "LLM dependence and cost" as a limitation but provide no analysis.

### Minor

- **The comparison with functional enrichment analysis (Section 4.4.3) is confusing**: The authors apply their own ICS/ICD/Resolution Score metrics to the enrichment results, which essentially tests whether the enrichment analysis agrees with HYPOGENEAGENT. This is circular reasoning—it does not validate HYPOGENEAGENT against an independent standard. A more meaningful comparison would be to assess whether the clusters selected by HYPOGENEAGENT yield more specific, non-redundant, or biologically validated enrichment terms compared to clusters selected by other methods.

- **The paper does not report whether the LLM-generated hypotheses are factually correct**: While the Stage 1 experiments validate that GPT-o3 can recover known GO terms for curated gene sets, there is no evaluation of whether the hypotheses generated for the actual Perturb-seq clusters are accurate. The authors could have manually inspected a subset of cluster annotations or compared them against known perturbation mechanisms from the original Replogle et al. study.

- **The "calibrated confidence scores" are not validated**: The paper treats the LLM's self-reported confidence scores as calibrated, but there is no evidence that these scores correlate with actual prediction accuracy beyond the Stage 1 analysis (Figure S3). The confidence scores are used in the hypothesis ranking but not in the Resolution Score computation, which relies only on the text embeddings.

### Trivial
- The paper contains a stray figure (Figure 1 in Section 4.4.3) that appears to be from an unrelated study about vitamin D3 effects on TH17 cells, likely a parser artifact from the PDF extraction.

## Nice-to-Haves

- Validation on at least 2-3 additional datasets (e.g., a different cell line, a tissue atlas, or a different Perturb-seq library) would substantially strengthen the generalizability claims.
- A quantitative comparison metric, such as the overlap between HYPOGENEAGENT-selected clusters and known ground-truth cell types or perturbation effects, would provide a rigorous evaluation.
- An analysis of the computational cost (API calls, time, cost in USD) and a discussion of how the method could be made more efficient (e.g., by using a cheaper LLM or sampling resolutions adaptively) would be valuable for practitioners.

## Novel Insights

None beyond the paper's own contributions. The core insight—using LLM-generated functional annotations to define a resolution selection criterion—is novel and well-motivated, but the paper does not reveal unexpected biological findings or methodological principles that transcend the specific implementation.

## Suggestions

1. **Add quantitative validation**: Compare the biological relevance of clusters selected by HYPOGENEAGENT against those selected by silhouette score, modularity, and functional enrichment using a quantitative metric. For example, compute the average pairwise semantic similarity of known ground-truth labels within clusters, or measure the enrichment of known perturbation-gene associations in the selected clusters.

2. **Test on additional datasets**: Apply the method to at least one more Perturb-seq dataset (e.g., from a different cell type or targeting a different biological pathway) and one scRNA-seq atlas dataset to demonstrate generalizability.

3. **Provide a principled approach to selecting w**: Either show that the optimal resolution is robust to w in a reasonable range (e.g., 0.2–0.5), or propose a data-driven method for selecting w (e.g., by maximizing the gap between the best and second-best resolution scores).

4. **Report computational costs**: Include a table showing the number of API calls, total tokens processed, runtime, and estimated cost for the full analysis. Discuss strategies for reducing cost (e.g., using a cheaper model for initial screening, or only running the agent on a subset of resolutions).

5. **Clarify the comparison with functional enrichment**: Either remove Section 4.4.3 or reframe it as a consistency check rather than a validation. If the goal is to compare methods, use an independent evaluation metric that does not rely on the same LLM-based scoring.

## Score and Decision

The paper presents a novel and well-motivated approach to a genuine problem in single-cell analysis. The method is clearly described, and the ablation studies on prompt design and model selection are thorough. However, the validation is limited to a single dataset, and the claimed superiority over traditional methods is not supported by quantitative evidence. The paper would benefit from additional validation and a more rigorous comparison framework. Given these limitations, the paper is at the borderline of acceptance—it has a clear contribution but requires stronger empirical support.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>