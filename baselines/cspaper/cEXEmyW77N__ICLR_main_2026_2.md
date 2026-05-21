---
job_id: b9eeae85-cdf2-43e2-9d7a-405e646c92d2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: cEXEmyW77N.pdf
paper: Structurally Human, Semantically Biased: Detecting LLM-Generated References with Embeddings and GNNs
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining representation learning, graph learning, and LLM analysis, with a concrete graph classification problem and embedding-based detection setup.

## Minimum Quality
Pass ✅. The paper contains the expected research components, including abstract, introduction, related work, methodology, experiments, results, discussion, and conclusion, and it provides substantial empirical evidence despite several methodological and presentation limitations.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious text targeting automated review systems in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies whether LLM-generated bibliographies can be distinguished from human reference lists using induced citation graphs and textual semantics. Using paired citation graphs for 10,000 focal papers from SciSciNet, the authors compare structure-only descriptors, graph-level aggregated title embeddings, and GNNs with node features, and conclude that topology alone weakly separates GPT-generated from ground-truth reference graphs, while semantic embeddings make the distinction much easier. The paper also includes random field-matched baselines and a robustness check with Claude Sonnet 4.5 and alternative embedding models.

## Strengths
The paper asks a timely and reasonably important question. As LLMs are increasingly used to suggest references, understanding whether their outputs are structurally human-like but semantically biased is relevant for automated literature review, citation recommendation, and research integrity tooling.

The empirical setup is broad and, in several respects, careful. The paired-graph construction around the same focal papers is a sensible design choice because it reduces variation from paper-specific topic differences. The scale is also nontrivial, 10,000 focal papers and roughly 275k references, which is larger than the toy-scale analyses that often populate this area.

I appreciated the progression from simple to more expressive models. The move from interpretable structural summaries, to graph-level embedding aggregation with RF, to GNNs, makes the central empirical finding easy to follow. The main result is also fairly crisp: coarse topology is not enough, semantics is. That is a useful takeaway even if the modeling ingredients themselves are standard.

The random baseline is better than a naive randomization. In Section 3, the field-matched reshuffling preserves out-degree and broad field distributions while disrupting latent citation structure. This is not perfect, but it is a meaningful control and the temporal/subfield robustness checks at least indicate the authors thought about easy objections.

Figure 2 is one of the paper’s more convincing pieces of evidence. In particular, the overlap of ground-truth and GPT clouds in Figure 2(b), 2(d), and 2(e), contrasted with the random baseline collapsing toward sparse low-clustering regions, does support the claim that the LLM-generated graphs are not trivially random and do reproduce some realistic multivariate structural couplings. This is stronger than only showing one-dimensional histograms.

Table 1 and Table 2 together tell a coherent story. Table 1 shows that structural descriptors separate human/LLM graphs from random ones very well, but barely separate GPT from ground truth, while Table 2 shows a large jump once semantic embeddings are used. Even without buying every interpretation, the empirical contrast between the two tables is clear and informative.

The paper includes useful robustness checks. The Claude replication, the OpenAI/SPECTER comparison, and the random-vector control all help support that the signal is not purely a dimensionality artifact. I also found the cross-generator experiment interesting, because it suggests at least part of the learned signal is shared across generators rather than tied to one specific model family.

## Weaknesses
1. **The novelty is more in the problem framing and dataset construction than in the modeling, and the paper sometimes oversells the methodological contribution.**  
The core technical pipeline is standard: graph descriptors, summed embeddings with RF, then standard GCN/GAT/GIN/GraphSAGE. That is not a deal-breaker by itself, but the paper occasionally reads as if the main contribution is a graph-learning method, when it is really an empirical study plus a detection benchmark. I think the paper would be stronger if it were more explicit and modest about this. Right now, the contribution is interesting, but methodologically incremental.

2. **The structural conclusion, “topology alone does not distinguish GPT from human graphs,” is stronger than what the actual structural feature space justifies.**  
Section 4 only uses a very small descriptor family: degree centrality, closeness, eigenvector centrality, clustering coefficient, and edge count, aggregated with simple statistics. That is a coarse summary of graph structure, not “citation topology” in any rich sense. Figure 2 indeed shows strong overlap under these summaries, but this could simply mean these particular low-order descriptors are insufficient. It does not establish that higher-order motifs, assortativity, community structure, ego-network signatures, graphlets, spectral features, or direction-aware citation patterns would also fail. Because the paper converts all graphs to undirected simple graphs in Section 3, it also discards one of the most meaningful aspects of citation networks, namely directionality and temporal asymmetry. So the claimed lesson should be narrowed from “structure alone fails” to “these coarse undirected structural summaries fail.”

3. **The comparison between RF on aggregated embeddings and GNNs does not isolate what exactly the GNN is buying.**  
Table 2 reports RF accuracy of \(0.8346 \pm 0.0063\) for ground truth vs GPT using summed title embeddings, while Table 3 reports around 93% test accuracy for GNNs with embedding node features. That looks impressive, but it is not an apples-to-apples comparison. The RF sees one summed vector per graph, while the GNN sees node-level embeddings, focal node context, graph size, and connectivity. As a result, the gap cannot be attributed specifically to graph reasoning. A stronger ablation would compare against order-invariant set models, mean/sum pooled MLPs over node embeddings, or a non-message-passing graph classifier with access to the same node-level inputs. Without that, the paper’s narrative risks crediting “structure + semantics” when the real gain may come from finer-grained node-level semantic access alone.

4. **There are likely confounds in the semantic detection setup that are not disentangled.**  
The paper argues that the distinguishing signature is semantic bias, but there are several plausible shortcuts that remain uncontrolled. For example, Section 3 states that about 6% of GPT-generated suggestions point to papers published after the focal paper, which is already a non-human artifact. It is unclear how much of the embedding-based separability is driven by topical-semantic bias versus easier metadata-correlated cues reflected in the text space, such as recency, venue style, title length, or broad field lexical priors. Figure 3 shows separation in embedding space, but that figure alone does not identify the cause of separation. Since the central scientific claim is about “semantic fingerprints,” the paper should do more to separate semantics from correlated bibliometric artifacts.

5. **The embedding aggregation and node-feature specification are underspecified in places, which matters for reproducibility and interpretation.**  
In Section 5, the graph-level embedding is formed by summing node embeddings. Since graphs vary in size and the generated/ground-truth graphs are size-matched only after node removal, sum pooling can still couple graph representation magnitude to residual size/composition effects. The paper does not clearly justify why sum is preferable to mean or normalized sum here, nor whether feature normalization is applied before RF. Similarly, Figure 3 discusses cosine and Euclidean graph-wise diagnostics, but the exact formulas for “mean focal with reference,” “mean reference with reference,” and “focal vs. sum of references” are never written explicitly in the main paper. For a paper making subtle semantic claims, this lack of formal definition is frustrating.

6. **The GNN structural feature construction is conceptually awkward and may bias the results.**  
Section 6 says each node receives a five-dimensional feature vector consisting of degree centrality, closeness centrality, eigenvector centrality, clustering coefficient, and the graph’s total number of edges, with edge count being a graph-level feature copied to every node. This is an odd design choice. Replicating a graph-global scalar across all nodes is not inherently wrong, but it blurs node and graph information and can encourage the GNN to act as a graph-size detector rather than a learned local-structure model. If the paper wants to test whether message passing adds structural power, this construction muddies the interpretation. At minimum, the rationale should be much clearer.

7. **The mathematical and formal exposition is thinner than it should be for a graph-learning paper.**  
There is no central theorem here, which is fine, but the paper still leans heavily on mathematically defined quantities. The main text never formally defines the graph-level feature map used by RF, even though the conclusions hinge on it. The appendix gives node-level formulas for \(C_D(v)\), \(C_C(v)\), \(C_E(v)\), and \(C(v)\), but the main paper should state the actual graph representation, something like  
\[
\phi(G) = \big[\operatorname{mean}(C_D), \operatorname{median}(C_D), \operatorname{IQR}(C_D), \ldots \big],
\]
rather than vaguely referring to “summary statistics” and “maxima-to-mean ratios.” The same applies to the semantic diagnostics and pooled embeddings. This is not a fatal correctness problem, but it weakens technical precision.

8. **Some experimental reporting choices are confusing and weaken the presentation.**  
Table 3 is hard to parse because each model appears in two unlabeled rows, evidently Accuracy and F1, but the formatting forces the reader to infer that. This should be explicit. Likewise, Figure 4 reports validation-accuracy distributions over 500 hyperparameter settings, while the main conclusions rely on test performance in Table 3. The two are both useful, but the presentation oscillates between “transparent sweep distributions” and “best test result” without a very clean bridge between them. I also found parts of the figure captions too interpretive, especially Figure 2, where the caption occasionally reads more like argumentation than description.

9. **The literature positioning is narrower than it should be, especially around citation-integrity detection and graph-based anomaly detection in scholarly networks.**  
The Related Work section mostly frames the paper against LLMs as research assistants and prior work by the same line of literature on LLM-generated bibliographies. What is missing is stronger engagement with adjacent work on suspicious/manipulated citation detection, miscitation detection, and text-rich graph learning for scholarly integrity tasks. That matters because the paper’s empirical setup is essentially a citation-integrity detection problem on attributed graphs. Better positioning against that literature would help clarify what is actually new here, and what is inherited from earlier graph-based anomaly detection ideas.

10. **External validity remains limited.**  
The dataset is restricted to SciSciNet papers with specific metadata availability constraints, Q1 journals, and focal papers between 1999 and 2021. The generation setup is also intentionally limited to parametric retrieval without external search. That is a legitimate design decision, but it narrows what can be concluded. The paper sometimes writes as if it has diagnosed “LLM bibliographies” broadly, whereas the actual result is about two model families under one constrained prompting-and-matching pipeline. I would like to see the claims tightened accordingly.

## Questions
1. The main claim is that “semantic fingerprints” distinguish LLM-generated bibliographies. Can the authors quantify how much of this effect remains after controlling for basic bibliometric covariates such as publication year, venue prestige, title length, number of authors, and overlap with the focal paper’s year/field? A matched analysis or a residualized classifier would increase my confidence that the signal is genuinely semantic rather than metadata-correlated.

2. Can the authors provide a stricter ablation for the 93% GNN result in Table 3? In particular, please compare against at least one non-graph model that has access to the same node-level embeddings, for example a DeepSets-style model or pooled node-embedding MLP. This would clarify whether message passing is truly helping, or whether the improvement over Table 2 mainly comes from avoiding graph-level sum compression.

3. In Section 5, why was **sum pooling** chosen for graph-level embeddings instead of mean pooling, normalized sum, or attention pooling? Since graph size and node composition vary, a clearer justification and a direct ablation would be helpful.

4. In Section 6, what is the rationale for copying the graph-level edge count onto every node as a node feature? Did the authors try removing that feature, or alternatively using graph-level readout features outside the node feature matrix? This choice affects how I interpret the structure-only GNN results.

5. Could the authors clarify the exact formulas for the Figure 3 diagnostics? The text refers to “mean of focal with reference,” “mean of reference with reference,” and “focal vs. sum of references,” but these are not formally defined in the main paper. Writing them explicitly would improve reproducibility.

6. Since the graphs are converted to undirected simple graphs in Section 3, did the authors try retaining directionality or temporal ordering? Citation graphs are inherently directed and time-respecting, so it would be valuable to know whether the “structure alone” conclusion survives in a more faithful graph representation.

7. The paper reports that about 6% of GPT suggestions cite future papers. If those nodes are removed, or if all comparisons are restricted to temporally valid references only, how much does the embedding-based separability change? This would help disentangle easy artifacts from subtler semantic patterns.

8. Relatedly, Figure 2 supports the claim that the chosen structural descriptors overlap strongly between GPT and ground truth, but have the authors tried richer structural baselines, such as motif counts, graphlet features, or spectral summaries? A negative result there would make the structural claim much stronger.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard caution around deployment. The paper studies LLM-generated bibliographies and possible detection mechanisms, but it does not introduce an obviously harmful dataset release, human-subject protocol, or unsafe deployment recipe that would by itself warrant formal ethics review.

## Soundness Rating
3: good. The empirical study is substantial and the main directional claims are supported, but several confounds and under-specified design choices prevent me from calling the evidence airtight.

## Presentation Rating
2: fair. The paper is readable overall, but the exposition is uneven, some tables/figures are confusingly formatted, and important feature definitions are too implicit.

## Contribution Rating
3: good. The problem framing, scale, and main empirical takeaway are useful to the community, even though the modeling is largely built from standard components and the broader positioning could be stronger.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a clear and interesting empirical message, good scale, and useful robustness checks, and I think that is enough to put it slightly on the positive side. That said, the work overstates what can be concluded about “topology” versus “semantics,” does not fully isolate why the GNNs help, and needs better positioning and sharper technical specification.

## Reviewer Confidence
4: confident. I am familiar with graph representation learning and citation-network modeling, and I checked the technical setup carefully, though I did not independently verify every appendix experiment.