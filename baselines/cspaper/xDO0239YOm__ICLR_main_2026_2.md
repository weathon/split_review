---
job_id: 3f846bb3-8695-4504-8a79-e116d63f384d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: xDO0239YOm.pdf
paper: HypoGeneAgent: Hypothesis Language Agent for Gene-Set Cluster Resolution Selection Using Perturb-Seq Datasets
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as an ML-for-biology submission centered on LLM agents, embedding-based semantic scoring, and hyperparameter selection for clustering.

## Minimum Quality
Pass ✅. The paper contains the expected core sections and presents a complete, reviewable research narrative, although there are substantial issues in methodology, experimental validation, and clarity that affect the final score rather than triggering desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes HYPOGENEAGENT, an LLM-based framework for selecting clustering resolution in Perturb-seq analysis by turning cluster annotation into an optimization problem. The method asks an LLM to generate up to five GO-style hypotheses per cluster, embeds the generated texts, and computes an intra-cluster agreement score and an inter-cluster distinctiveness score, which are combined into a resolution score used to pick the clustering granularity. The empirical study includes a prompt/model benchmark on curated GO biological process gene sets and an application to one public K562 CRISPRi Perturb-seq dataset, with comparisons to silhouette score, modularity, and enrichment-based summaries.

## Strengths
1. The paper addresses a real pain point in single-cell and Perturb-seq analysis, namely that clustering resolution selection is often heuristic and intertwined with subjective downstream biological interpretation. Framing resolution selection through the lens of semantic coherence is a reasonable and interesting problem formulation.

2. The overall pipeline is easy to understand at a high level. In particular, **Figure 2** gives a useful end-to-end schematic of the workflow, connecting candidate clusterings, LLM-based annotation, text embeddings, and final resolution scoring. Even though some implementation details remain underspecified, the conceptual decomposition is clear.

3. The paper attempts to separate two intuitions that practitioners often use informally, internal cluster coherence and external distinction across clusters, into explicit quantities. The decomposition into ICS and ICD is simple and practically interpretable.

4. The authors do include some effort toward prompt/model selection rather than treating the LLM backend as a black box. The Stage 1 benchmark on curated GOBP sets is a reasonable preliminary step before deployment to the Perturb-seq setting.

5. I appreciated the attempt to compare against non-LLM baselines that are actually used in practice. The discussion around silhouette and modularity at least acknowledges that conventional clustering metrics do not directly encode biological interpretability.

6. There is some value in the side-by-side prompt illustration. **Figure 1** helps clarify what changed between the “general-analysis prompt” and the “hypothesis prompt,” and why the latter is necessary for computing within-cluster agreement over multiple candidate descriptions.

## Weaknesses
1. **The core evaluation is too narrow for the scope of the claims.**  
   Nearly all of the main biological conclusions rest on a single dataset, the K562 CRISPRi Perturb-seq dataset from Replogle et al. This is stated in **Section 4.2** and reinforced throughout **Section 4.3**. For a paper making broad claims about “fully automated, context-aware interpretation pipelines” and “general methodology” in the abstract and conclusion, one cell line, one perturbation setting, and one clustering setup is not enough. This matters because the proposed score is tightly coupled to the semantic behavior of an LLM on a specific kind of marker list. Without testing on additional Perturb-seq datasets, additional cell types, or at least a second public single-cell benchmark, it is impossible to know whether the method is robust or simply tuned to a favorable case.

2. **The paper does not establish a convincing ground truth for “best resolution,” so the central claim is under-supported.**  
   The main argument is that HYPOGENEAGENT selects biologically meaningful resolutions better than silhouette and modularity. But in the main paper, the evidence is mostly that the score peaks at \(r=0.4\) for GEX and \(r=0.5\) for perturbation-level clustering, and that these UMAPs “look clear” or seem “in agreement with known pathway.” This is qualitatively argued in **Section 4.3** around **Figure 3** and **Figure 4**, but not quantitatively demonstrated. There is no direct external evaluation against known perturbation labels, pathway memberships, held-out annotations, or recovery of expected gene modules. A resolution score can always produce an optimum, but that does not mean the optimum is biologically correct. This is the scientific bottleneck of the paper.

3. **The proposed metric is partly circular and risks rewarding linguistic redundancy rather than biological validity.**  
   In **Section 3.4**, \(\mathrm{ICS}_k\) is defined as the average cosine similarity between the top hypothesis \(h_{k1}\) and the lower-ranked hypotheses \(h_{k2},\ldots,h_{k5}\). If the same model generates all five candidates under one prompt, then high ICS may simply reflect that the model paraphrases itself consistently. That is not equivalent to the underlying cluster being biologically coherent. In other words, the score measures self-consistency of an LLM more than consistency of the data. This matters a lot because the paper interprets ICS as evidence that “the cluster is internally coherent and biologically robust,” which is a much stronger statement than what the metric actually guarantees.

4. **There are mathematical and notation inconsistencies in the metric definitions, and they are not minor.**  
   In **Table 1** on **Page 4**, \(\mathrm{ICS}_{h,k}\) is described as “Cosine distance” whereas the text below defines \(\mathrm{ICS}_k = \frac{1}{4}\sum_{h=2}^{5}\mathrm{sim}(h_{k1},h_{kh})\), explicitly using cosine similarity. Similarly, \(\mathrm{ICD}_k\) is described in the table as a cosine distance, but the formula in **Section 3.4** defines it as a mean pairwise similarity. Then the text says “A lower \(\mathrm{ICD}_k\) therefore implies that cluster \(k\) is well separated,” which only makes sense if \(\mathrm{ICD}_k\) is indeed a similarity, not a distance. This inconsistency is more than cosmetic, because the meaning of the score flips depending on whether one uses similarity or distance. The authors should rewrite the definitions cleanly, for example by choosing one convention and using it everywhere:
   \[
   \mathrm{ICS}_k = \frac{1}{H-1}\sum_{i=2}^{H} \cos(e(h_{k1}), e(h_{ki}))
   \]
   \[
   \mathrm{ICD}_k = \frac{1}{C-1}\sum_{\ell \neq k} \cos(e(h_{k1}), e(h_{\ell 1}))
   \]
   \[
   \mathrm{RS}_k = w\,\mathrm{ICS}_k + (1-w)(1-\mathrm{ICD}_k)
   \]
   where \(e(\cdot)\) is the text embedding function and \(H\) is the number of returned hypotheses actually present. Right now the notation and prose do not line up reliably.

5. **The definition of the final resolution score is underspecified at the partition level.**  
   The paper defines \(\mathrm{RS}_k\) for each cluster in **Section 3.4**, but the optimization problem in practice is over a resolution \(r\), not a single cluster. The reader has to infer from **Figure 3a** and **Figure 4a** that the authors summarize cluster-level scores across clusters at a given resolution, apparently using a box plot and choosing the highest median. But this aggregation rule is never explicitly defined as a formal objective such as
   \[
   \mathrm{RS}(r) = \mathrm{median}_{k \in \mathcal{C}(r)} \mathrm{RS}_k
   \quad \text{or} \quad
   \mathrm{RS}(r) = \frac{1}{|\mathcal{C}(r)|}\sum_k \mathrm{RS}_k .
   \]
   That missing definition matters because different aggregations can yield different selected resolutions, especially when the number of clusters changes substantially with \(r\). A method paper should not leave the actual optimization target implicit in the figure caption.

6. **The choice of the weighting parameter \(w\) is inconsistent and suggests post hoc tuning.**  
   In **Section 3.4**, the paper states “We adopt \(w=\frac{1}{3}\).” However, in the perturbation-level experiment on **Page 7**, the text for **Figure 4a** says the resolution score uses \(w=\frac{1}{2}\). This is a serious reproducibility and methodology issue. If different tasks use different weights, then the method is not fixed as claimed in **Section 4.2** (“selected a single prompt/model/embedding configuration and held it fixed for all downstream analyses”). If the weight was changed between GEX-level and perturbation-level evaluation, the reason should be explicit and justified. Otherwise this reads like silent objective retuning to get a nicer peak.

7. **Stage 1 benchmarking is weakly connected to Stage 2 claims.**  
   The Stage 1 study on curated GOBP sets mostly measures cosine similarity between generated text and reference text. But the Stage 2 use case does not have such reference descriptions, so the benchmark only loosely validates the downstream application. Also, the benchmark itself is not summarized in any proper table in the main paper, only in supplementary figures and narrative descriptions in **Section 4.3**. As a result, it is hard to judge how strong the model-selection evidence really is. If the point is to justify GPT-o3 plus the hypothesis prompt plus the selected embedding model, the paper should provide a compact main-paper results table with medians, confidence intervals, and sample counts rather than prose like “thinking LLMs perform better.”

8. **The empirical comparisons to traditional methods are not fair enough to support “exceeded traditional metrics.”**  
   In **Section 4.4**, the silhouette and modularity baselines are discussed mostly through qualitative “elbow” behavior in **Figure 5**, and the enrichment baseline in **Figure 6** is described somewhat informally. There is no rigorous downstream criterion by which one can conclude that HYPOGENEAGENT is better. For example, if the authors believe \(r=0.4\) is superior to the silhouette-selected \(r=0.5/0.6\) or the modularity-selected \(r=0.7\), they should quantify that superiority using external biological labels, perturbation recovery, or overlap with known pathways. Right now, the baseline comparison is largely rhetorical.

9. **The visual evidence in the main figures is weaker than the text suggests.**  
   In **Figure 3b** and **Figure 4b**, the selected UMAPs at \(r=0.4\) and \(r=0.5\) are shown as qualitative support for the chosen resolutions. But UMAP separation is not a reliable validation of clustering quality, and the plots themselves do not demonstrate that these resolutions are preferable to nearby alternatives. Showing only one selected UMAP per setting is not enough. If the authors want to make a visual argument, they need side-by-side plots for neighboring resolutions, plus quantitative cluster sizes and perhaps marker consistency. As presented, the figures mainly show that the data can be partitioned, not that the selected partition is optimal.

10. **The only explicit results table in the main paper, Table 1, is not a results table at all, and it introduces confusion rather than clarity.**  
    The paper lacks a conventional quantitative results table in the main text. The one table present, **Table 1**, is a definitions table. That would be fine, except the table itself contains incorrect or inconsistent terminology, as noted above, using “distance” where the equations use similarity. Since the paper depends heavily on these metrics, having the central table misaligned with the formal definitions undermines confidence in the implementation details.

11. **Key implementation details are missing from the main paper, making the method hard to evaluate as science rather than as a demo.**  
    Several choices are pushed to the appendix or omitted. Examples include the exact size of gene signatures passed to the LLM, how ties or fewer than five hypotheses are handled in \(\mathrm{ICS}_k\), whether confidence scores \(c_{ki}\) are used anywhere in the final score, how retrieval snippets are selected and truncated, and how many API calls or repeats were run per cluster. The confidence scores are prominently introduced in **Section 3.3**, but then disappear from the metric definitions, which raises the obvious question of whether they matter at all. This matters because the paper’s main claim is about an “agent” with calibrated confidence, yet the scoring machinery seems to ignore those calibrations.

12. **The paper’s positioning against prior work is incomplete.**  
    The related work cites GeneAgent and several broad AI-for-science works, but it does not sufficiently discuss earlier work on LLM-based gene-set summarization or agentic interpretation of transcriptomic clusters. That omission makes the novelty claim feel overstated. The main contribution seems to be the specific use of semantic agreement for resolution selection, which is a narrower and more incremental claim than the paper’s framing suggests.

13. **Presentation quality is below the bar for a paper whose credibility depends on precise definitions.**  
    There are many grammar and wording problems throughout the main text. Some examples: the abstract has multiple broken constructions, **Section 3.2** lists pipeline items without enough explanation, **Section 4.4.3** is written in a very informal way, and several sentences are hard to parse. This would be survivable in a purely empirical paper with overwhelming results, but here the contribution is a metric definition. When the writing is this loose, it becomes difficult to tell what exactly was computed.

## Questions
1. What is the exact partition-level objective optimized over resolutions? Please provide the precise formula used to collapse \(\{\mathrm{RS}_k\}_k\) into a single score for each resolution \(r\), and state whether you use the mean, median, or another statistic.

2. Why is \(w=\frac{1}{3}\) in **Section 3.4** but \(w=\frac{1}{2}\) for the perturbation-level experiment in **Figure 4a**? Was this changed after inspecting the results, or was there a predefined reason for using different weights across settings?

3. Can you provide an external quantitative validation of the selected resolutions, beyond UMAP appearance and narrative biological plausibility? For example, recovery of known perturbation groups, pathway consistency against held-out labels, or enrichment overlap against curated references would significantly increase confidence.

4. How exactly are the top marker genes chosen for each cluster, and how many genes are passed to the LLM? This is central to the behavior of the method but is not specified clearly in the main paper.

5. What happens when the agent returns fewer than five valid hypotheses, duplicate hypotheses, or very generic hypotheses? How are \(\mathrm{ICS}_k\) and \(\mathrm{RS}_k\) computed in those cases?

6. The paper emphasizes calibrated confidence scores \(c_{ki}\), but the main scoring formula does not use them. Did you try a confidence-weighted variant, such as
   \[
   \mathrm{ICS}_k^{(w)} = \frac{\sum_{i=2}^{H} c_{ki}\,\cos(e(h_{k1}),e(h_{ki}))}{\sum_{i=2}^{H} c_{ki}}?
   \]
   If not, why introduce calibration so prominently?

7. Can you include a compact quantitative table in the main paper summarizing Stage 1 model/prompt selection and Stage 2 resolution selection outcomes, including uncertainty across runs? Right now the evidence is spread across prose and supplementary plots.

8. Please clarify whether the retrieval component was enabled in all experiments and what exact resources/snippets were exposed to the model. Since the method is partly retrieval-augmented, this has a large effect on factuality and reproducibility.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond ordinary caution about the use of proprietary LLM APIs and reproducibility. I do not see a primary ethics issue that requires formal escalation based on the main paper.

## Soundness Rating
2: fair. The idea is plausible, but the technical definitions contain inconsistencies and the empirical evidence does not adequately support the paper’s broader claims.

## Presentation Rating
2: fair. The high-level story is understandable, but the writing, notation, and method specification are too loose for a metric-driven paper.

## Contribution Rating
2: fair. The problem framing is interesting, but the actual contribution feels preliminary, narrowly validated, and not yet strong enough for ICLR in its current form.

## Overall Rating
2: Reject, not good enough. The paper has an interesting premise and a potentially useful direction, but the current version is undermined by unclear metric definitions, inconsistent objective specification, limited empirical validation, and insufficient evidence that the chosen resolutions are actually better in an external biological sense.

## Reviewer Confidence
4: confident. I am confident in the assessment, though it is still possible I missed some implementation detail because several important parts of the method are not clearly specified in the main paper.