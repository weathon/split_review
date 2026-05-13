# Data Valuation for Graphs

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
What is the worth of a node? We answer this question using an emerging set of data valuation techniques, where the value of a data point is measured via its marginal contribution when added to the (training) dataset. Data valuation has been primarily studied in the i.i.d. setting, giving rise to methods like influence functions, leave-one-out estimation, data Shapley, and data Banzhaf. We conduct a comprehensive study of data valuation approaches applied to graph-structured models such as graph neural networks in a semi-supervised transductive setting. Since all nodes (labeled and unlabeled) influence both training and inference we construct various scenarios to understand the diverse mechanisms by which nodes can impact learning. We show that the resulting node values can be used to identify (positively and negatively) influential nodes, quantify model brittleness, detect poisoned data, and accurately predict counterfactuals.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work conducts a comprehensive study in a semi-supervised transductive setting. In this setting, the paper highlights the insufficiency of the setting adopted by existing works, which ignores the influence of unlabeled nodes. The paper empirically shows that taking both labeled and unlabeled nodes into consideration will lead to a more effective valuation.

### Strengths
The paper summarizes and connects different valuation methods in a clear way.

The idea of considering unlabeled data in the semi-supervised transductive setting is interesting and makes much sense.

The experiments show that the overlooked data valuation methods, such as data models, perform quite well across different downstream tasks of data valuation. This is important for future research in this field.

### Weaknesses
My primary concern is that the motivation is not well supported by evidence. The paper starts with the motivation that we should consider the influence of unlabeled data (e.g., line 016).  Also, in line 084, the authors claim that ”we can find unlabeled nodes which have greater influence than many training nodes.” However, I could not find much empirical support in the experiments. This claim should be backed up with comparative experiments. Specifically, the paper lacks a direct comparison showing instances where unlabeled nodes demonstrably have a higher influence score than a significant portion of labeled nodes. The current experiments do not isolate and highlight such cases, making the central claim difficult to verify.

I find the setting part, like the “Learning signal vs. Overall signal” section, difficult to digest. It would be great if it could be expanded with concrete examples (a tiny set of nodes, some are used to train the model, some are used for inference, etc). For instance, a step-by-step walkthrough of how the learning signal and overall signal are computed for a small graph with 3-4 nodes, including both labeled and unlabeled nodes, would greatly improve clarity. The current description is too abstract and lacks the necessary grounding in concrete examples.

In Figure 1, the coloring of nodes is not used in the subsequent and might not be so meaningful in this diagram. Defining them here seems redundant and distracting. Using real numbers in this example might assist in illustrating the idea. The current use of colors is not only confusing but also a missed opportunity to make the concept more intuitive. A numerical representation of influence, even in a toy example, would be more effective.

### Questions
Although methods like Data Shapley consider the coalition of nodes and can somehow capture the correlation between nodes, removing points based on individual score ranking does not seem to consider this. I wonder if this is the best we can do with the individual node scores and I am curious how the group influence/contribution plays in this context.

For Average class-wise values, what does a high in-class influence imply (e.g., in terms of prediction robustness)?

What is the intuition behind the improved performance of LOO when facing a larger distribution shift (Fig.6(b))?

This work looks into semi-supervised transductive settings, but I am curious if similar conclusions can be drawn in the context of supervised learning (e.g., which methods are more accurate than others).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work conducts a benchmark study of data valuation methods on graph neural networks. This work does not introduce new data attribution methods but focus on evaluation. The methods being evaluated include several generic data valuation methods (leave-one-out, Data Shapley, Data Banzhaf and Datamodels), as well as recent methods tailored for graphs. The results show that Data Banzhaf and Datamodels perform the best.

### Strengths
This paper conducts a comprehensive evaluation of existing data valuation methods for graph neural networks. This includes a reasonably large set of methods, and a variety of evaluation metrics. The visualization of influential nodes also provides helpful insights.

### Weaknesses
1. Overall, this paper lacks technical novelty as it only focuses on evaluating existing methods.

2. A major contribution claimed by this paper is the application of data valuation methods to the graph setting. However, most of the generic data valuation methods studied in this paper, such as leave-one-out, Data Shapley or Data Banzhaf, are not restricted to i.i.d. settings by design and can be straightforwardly applied to graph neural networks with proper choice of utility function. So the incremental novelty of generalizing these methods from a feedforward NN to a GNN is no significantly larger that that from a CNN to a ResNet.

3. The computation cost for the evaluated methods is not reported, which is a very important metric.

4. The experimental setups are simple GNNs on what have been considered as toy datasets by the GNN community.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a comprehensive study of existing data valuation techniques on graphs. It finds that datamodel and data Banzhaf outperforms other method (including graph-specific valuation). The authors also show the potential of using node values for various applications.

### Strengths
S1. This paper offers a thorough introduction to data valuation and valuation for graphs.

S2. It evaluates various valuation techniques on semi-supervised node classification in several different downstream tasks.

### Weaknesses
W1. It is unclear whether removing nodes from a graph can be considered as a valuation for node itself, given that message passing depends on edges as well. Node classification accuracy can change even if keeping the node itself and only remove edge(s) from the graph (e.g., how poisoning attacks are done on graphs). Essentially I think these valuation is measuring the values of a node and its associated edges, rather than just the value of **a node**.

W2. As a paper that focuses on comprehensive study of existing methods, I would like to see more analyses on why some methods offer good valuation while some don't, especially for PCW which is the only one method that designed for graphs. The current section 4 is more like describing all results, without many insightful analyses or discussion to dig deeper into the results, which should be the key but missing contribution of this paper to the field. The analysis should explore the underlying mechanisms of why certain methods fail, going beyond just reporting performance metrics. For instance, a deeper dive into how PCW's graph-specific design impacts its performance compared to methods designed for i.i.d data would be beneficial.

W3. There are quite a lot of figures and heatmaps in the paper. I would suggest the authors to add necessary legends and figure captions into the paper for better clarity. It is also unclear why different circles have a very different sizes in Figure 9. Furthermore, in Figure 6, several baseline methods such as SHAP, PCW, and PCWP have very similar coloring, making it difficult to distinguish between them without careful inspection. This lack of visual clarity hinders the interpretability of the results.

W4. I think the paper could be further strengthened if it includes a dedicated section to discussion the lessons learned and what actions the community should take for precise valuation for graphs.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This is a benchmark paper on data valuation for graphs. It summarizes and compares different data value notions, whether to predict the estimation of data value, and different sampling methods.

### Strengths
- The summarization and survey of previous data valuation methods are clear and detailed.

- The experiments and evaluation are sufficient and intriguing.

### Weaknesses
 - The analysis of the experiment results does not match the illustrated figures. See questions.

- No running time is provided. I'm concerned about how the sampling subset number affects the value estimation and running time, considering that 50,000 subsets is quite a large number, even for small graphs.

### Questions
- What's the main challenge of applying game-theoretic data notions to graphs? Do we need any specific designs for the graph besides customizing the influence function?

- In Fig. 3, it seems that in subgraphs 5&6, DM does not outperform other methods. Can you clarify that?

- It's interesting to control the average size of coalitions. What about controlling the upper bound of size, e.g., to 500, since in experiments, we only remove the top 500 nodes?

- Did you make any adaptations from Chi's PC-Winter to the transductive setting? How do you exclude the effect by the test node that has already been seen during training?

### Soundness
3

### Presentation
3

### Contribution
2
