# AIMing for Explainability in GNNs

- Decision: Reject
- Avg Score: 3.40
- Scores: 3, 3, 3, 5, 3

## Abstract
As machine learning models become increasingly complex and are deployed in critical domains such as healthcare, finance, and autonomous systems, the need for effective explainability has grown. Graph Neural Networks (GNNs), which excel in processing graph-structured data, have seen significant advancements, but explainability for GNNs is still in its early stages. Existing approaches fall into two broad categories: post-hoc explainers and inherently interpretable models. Their evaluation is often limited to synthetic datasets for which ground truth explanations are available, or conducted with the assumption that each XAI method extracts explanations for a fixed network. We focus specifically on inherently interpretable GNNs (e.g., based on prototypes, graph kernels) which enable model-level explanations. For evaluation, these models claim inherent interpretability and only assess predictive accuracy, without applying concrete interpretability metrics. These evaluation practices fundamentally restrict the utility of any discussions regarding explainability. We propose a unified and comprehensive framework for measuring and evaluating explainability in GNNs that extends beyond synthetic datasets, ground-truth constraints, and rigid assumptions, while also supporting the development and refinement of models based on derived explanations. The framework involves measures of Accuracy, Instance-level explanations, and Model-level explanations (AIM), inspired by the generic Co-12 conceptual properties of explanations quality (Nauta et al., 2023). We apply this framework to a suite of existing models, deriving ways to extract explanations from them and to highlight their strengths and weaknesses. Furthermore, based on this analysis using AIM, we develop a new model called XGKN that demonstrates improved explainability while performing on par with existing models. Our approach aims to advance the field of Explainable AI (XAI) for GNNs, offering more robust and practical solutions for understanding and interpreting complex models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a set of metrics for measuring explainability of GNNs inspired by the Nauta et al. co-12 properties. They also develop a variant of graph-kernel based GNNs enhancing explainability properties.

### Strengths
The idea of evaluating explainability from many different perspectives is (not novel but) sensible, and it's application to GNN explainability is potentially interesting.

The proposed approach seem to strike a good balance between different metrics.

### Weaknesses
My impression is that the authors made an attempt to adapt the co-12 properties from (Nauta et al., 2023), but partly failed to account for the specificities of of networked data and GNNs, and overlooked a number of formalization efforts already available in the literature.

Completeness (without): I(f(G\f(h(G)) != c) the formula is wrong, I
guess it should be I(f(G \ h(G)) != c). Also, this metric exists and
is called fidelity- (or sufficiency).

Consistency: this is poorly formalized, as IoU(h(G),h(G)) is 1 by
construction. You should clarify (and formally write) that this is
computed by picking explanations from a distribution (I guess).

Continuity: While this is sensible with low-level data (like pixels),
it's not necessarily sensible with discrete structures like graphs,
where the the ground truth could be a motif, and removing elements of
the motif could end up changing the label of the graph. Indeed,
measures like explanation fidelity (especially robust fidelity+),
encode the fact that removing elements that are part of the
explanation should have an impact on the prediction of the model (and
thus, on the resulting post-hoc explanation).

Contrastivity: the definition doesn't seem to fit the description in Table 1

For model-level metrics, correctness seems to be closer to a
(model-level) definition of robust fidelity+, but in this set of
metrics is somehow in contradiction with consistency in the
instance-level metrics. Also 

M3: Compactness - I am not sure this is about compactness, I would
rather talk about non-redundancy.

Talking about interpretable GNNs, the authors only focus on
prototype-based and kernel-based GNNs. However, the literature on
interpretable GNNs is much richer. For instance, all methods based on
attention are missing, e.g.:

Siqi Miao, Mia Liu, and Pan Li. Interpretable and generalizable graph learning via stochastic attention mechanism. ICML 2022.

Chris Lin, Gerald J Sun, Krishna C Bulusu, Jonathan R Dry, and Marylens Hernandez. Graph neural networks including sparse interpretability. arXiv, 2020.

Giuseppe Serra and Mathias Niepert. Learning to explain graph neural networks. arXiv, 2022.

This limits the relevance of the experimental evaluation. Additionally, only two explainers are evaluated, while  plenty of (more recent) explainers have been proposed in the literature.

Finally, the authors propose a SHAP-based approach to extract explanations from interpretable GNNs, which is fine. But post-hoc explainers can still be applied to interpretable GNNs, so it is not true that no  solution exists. The authors should show that their approach is better in extracting explanations from interpretable GNNs.

### Questions
Can you comment on my concerns about (some of) the properties you propose?

Can you comment on my concerns about the insufficient treatment of interpretable GNNs?

Can you comment on my concerns about the insufficient treatment of GNN explainers?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors focus on the problem of GNN explainability;

- Contribution 1 -- a framework for graph explainability, with 12 properties

- Contribution 2 -- XGKN, a new explanable GNN model based on random walks

### Strengths
- This paper tackles an important problem of GNN explainability
- The proposed method XGKN seems to provide some benefits against KerGNN (though see Questions)

### Weaknesses
 - It would be great if the authors put their work in the context of previous efforts, especially for C1
- Some questions about experiments

- In terms of contribution 1, there are previous efforts such as GraphFramEx that try to provide 
some properties and eval metrics for graph explainability. Although I understand AIM is not 
exactly the same, it would be great if the authors can elaborate on the differences and build their
insights over previous work instead of starting from scratch

- Personally I found it rather hard to compare XGKN and KerGNN by cross ref Figure 2 and Table 3
with Figure 4 and Table 4 that are 3 pages apart. But my understanding is that:

- Table 3 v Table 4 -- out of 6 benchmarks, 3 KerGNN is better and 3 XGKN is better -- it would be 
great if the authors can elaborate on why "XGKN outperforms its predecessor, KerGNN, delivering superior results"

- In terms of times to extract explanations -- the different is quite small and probably fall in the 
regime of implementation details -- it would be great if the authors can elaborate on why this difference
is fundamental, rather than some implication of implementation decisions.

- I didn't find a good way to compare Figure 2 and Figure 4 clearly and understand it; given the authors still
have 1 page left, I would enrich 4.2.2 and really compare these two methods clearly, tease apart different
datasets.

### Questions
1. In terms of contribution 1, there are previous efforts such as GraphFramEx that try to provide 
some properties and eval metrics for graph explainability. Although I understand AIM is not 
exactly the same, it would be great if the authors can elaborate on the differences and build their
insights over previous work instead of starting from scratch

2. Personally I found it rather hard to compare XGKN and KerGNN by cross ref Figure 2 and Table 3
with Figure 4 and Table 4 that are 3 pages apart. But my understanding is that:

- Table 3 v Table 4 -- out of 6 benchmarks, 3 KerGNN is better and 3 XGKN is better -- it would be 
great if the authors can elaborate on why "XGKN outperforms its predecessor, KerGNN, delivering superior results"

- In terms of times to extract explanations -- the different is quite small and probably fall in the 
regime of implementation details -- it would be great if the authors can elaborate on why this difference
is fundamental, rather than some implication of implementation decisions.

- I didn't find a good way to compare Figure 2 and Figure 4 clearly and understand it; given the authors still
have 1 page left, I would enrich 4.2.2 and really compare these two methods clearly, tease apart different
datasets.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The submission first proposes AIM metrics that cover Co-12 properties for evaluation of the Explainer of GNN Models. The authors then validate different existing GNN explainers with the proposed metrics. Moreover, the authors propose a new explainer approach based on Graph Kernel Networks (GKN). Basically, the idea of the proposed explainer is not very novel, that is a simple extention of existing GKN approaches. The thorough validation on different properties of explaination of an explainer of GNN is important.

### Strengths
1). The thorough validation on different properties of explaination of an explainer of GNN is important. Exisiting work does not discuss such different properties thoroughly. This is a good contribution of this submission.

2). The problem is important for XAI, espeicially for applications in important AI for sicience tasks, like drug discovery.

### Weaknesses
1). the idea of the proposed explainer is not very novel. The paper listed two other GKN approaches. On top of that, the new stuffs in this paper is not significant. Meanwhile, the performance improvement on AIM metrics over two other GKN approaches is not significant. 

2). The authors do not consider the OOD issue of the metrics that are discussed in the following papers:
Cooperative explanations of graph neural networks. WSDM’23.
TOWARDS ROBUST FIDELITY FOR EVALUATING EXPLAINABILITY OF GRAPH NEURAL NETWORKS.  ICLR’24.

3). The motivation is not well-written on the improvement over existing GKN approaches.

### Questions
as mentioned in weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose novel metrics for evaluating GNN explainer models, as well as a new interpretable GNN model based on KerGNN, called XGKN. The work is innovative and has great potential in the field of graph neural networks (GNNs). The authors have conducted extensive experiments to assess both their proposed metrics and the performance of their new model. However, there are several concerns that need to be addressed to improve the clarity and presentation of the paper.

### Strengths
The authors tackle an important problem in GNN interpretability and propose both a new model and metrics to evaluate it. The concept of XGKN and the proposed evaluation metrics are novel and relevant. Furthermore, the experimental evaluation is thorough, providing substantial support for the contributions.

### Weaknesses
1. Introduction Structure and Clarity:
   The logic in the introduction is somewhat unclear. The authors should clearly state their two main objectives: (1) to propose new evaluation metrics for GNN explainability, and (2) to introduce XGKN, a GNN model with inherent interpretability. After discussing the shortcomings of existing methods, the authors should introduce their model XGKN, explaining how it addresses the identified limitations. This should be followed by a clear explanation of the shortcomings of current evaluation metrics, leading to their motivation for proposing new metrics. Additionally, it would be helpful to move the related work to a separate section, so the introduction can focus more on the motivation and contributions. The current contribution section lacks clarity and should be more explicit about the novelty of the work.

2. Writing and Formatting Issues:
   There are numerous writing errors throughout the paper:
   - The caption for the tables is not formatted correctly. The captions should be placed above the tables.
   - In line 81, "GKN" should be "XGKN," as it refers to the authors' proposed model.
   - Line 140: A comma is missing after "as an explanation" and before "for the prediction."
   - Line 141: The correct notation should be "IoU(G1, G2)."
   - Line 142: The symbol "II" is introduced without explanation, and should be defined clearly when first mentioned.
   - Line 153: The formula should be written as "II(f(G \ h(G)) ≠ c)." 
   - Lines 156 and 159 use "G'" to represent different meanings. This inconsistency is confusing, and different symbols should be used to avoid ambiguity. Furthermore, "G'" appears again in line 374 without proper explanation.
   - Lines 160 and 213: The "G" font is incorrect; it should be italicized to represent "graph."
   - Line 238: There is a missing "a" before "GIN."

3. Formula and Notation Issues:
   - Line 160: The explanation for contrastivity is not clear. Contrastivity measures the distinguishability between explanations for different predictions. The authors should clarify their reasoning behind the current formula and explain how it relates to the concept of contrastivity as typically understood in the field. The current definition seems to focus on the difference in explanations for different predictions, but it's unclear how this is quantified and how it aligns with the broader notion of contrastivity.
   - In lines 149 and 167, the definitions of A1 and A2 rely on the explanation of ground truth. However, for real-world datasets where ground truth is not available, it is unclear how this would be handled. The authors could propose alternative metrics for cases without ground truth or discuss how their method could be adapted for such scenarios. The reliance on ground truth explanations limits the applicability of these metrics to scenarios where such information is available, and the paper needs to address how to handle cases where ground truth is not available.
   - Line 377: The meaning of "K" in the formula is not explained and should be clarified.

4. Figure and Table Organization:
   Figures 4 and Table 4 should be combined with Figure 2 and Table 3, respectively. This would allow for better comparison between the performance of the proposed method and existing methods, making it easier to assess improvements.

5. Overall Organization and Presentation:
   While the paper presents innovative ideas, the structure and presentation need significant improvement. It is recommended to first introduce the proposed method (XGKN), followed by the proposed metrics. In the experiments section, the authors should use their proposed metrics to evaluate both existing methods and their own. Additionally, the limitations of existing metrics should be clearly stated, and the authors should explain how their proposed metrics address these limitations.

### Questions
See in Weeknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose the adoption of the Co-12 properties previously developed in explanations for images into the graph domain.
The authors also claim that explainability for graphs is a rather under-studied issue, and that lacks standardized evaluation metrics.
After having defined those evaluation metrics, the authors propose a way to extract local explanations from previous explainable models and propose a new variant improving on self-explainability.

### Strengths
- The overall quality of the writing is good
- Challenging common assumptions in the literature, such as evaluation metrics, is useful for the community
- The visualization of results across different metrics (Fig. 1) is nice

### Weaknesses
The paper **substantially lacks references to previous works**, and **many claims central to the proposed contribution are contradicted by the literature**. For example:

1. line 14-15: the claim is not supported, as plenty of approaches evaluate post-hoc methods with metrics not requiring ground truth [1,2,3]
2. line 15-16: the contrasting approach to post-hoc methods is referred to as ante-hoc methods. The indicated ante-hoc methods (prototypes and graph kernels) constitute only a very limited perspective on the current state of the art in ante-hoc methods [1,4].
3. line 37: the claim is not supported, see [1,2,3,4]. XAI for GNNs is actually a very active field of research
4. line 51: the claim is not supported, see my point 2
5. line 60-61: the claim is not supported, as plenty of metrics are available for graph explanations [1,2,3,4]

### Questions
- Line 143 says "Explainers do not have to be deterministic". I wonder which kind of insights a human can extrapolate from a black-box when the explanation for a certain fixed output changes when the explanation is non-deterministic. Also, PGExplainer is indicated as a non-deterministic algorithm. However, once the explainer is trained, it is fully deterministic. Only the training of such an explainer is non-deterministic. This should be clarified in the text.

- The authors are proposing to evaluate graph explanation with a suite of 12 evaluation metrics. Such a high number of metrics, in my opinion, makes the assessment of different explainers difficult, making comparison hard.

- The proposed model is difficult to understand, and Figure 3 does not provide enough information. I would suggest annotating the figure with more detail and providing a more intuitive explanation.

- Some important implementation details for ensuring reproducibility are lacking, like how the Elbow method for obtaining explanation threshold is implemented. I suggest providing more details on this

### Soundness
1

### Presentation
1

### Contribution
1
