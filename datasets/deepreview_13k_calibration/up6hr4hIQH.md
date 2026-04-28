# Towards Robust Fidelity for Evaluating Explainability of Graph Neural Networks

- Decision: Accept
- Avg Score: 6.00
- Scores: 3, 5, 8, 8

## Abstract
Graph Neural Networks (GNNs) are neural models that leverage the dependency structure in graphical data via message passing among the graph nodes. GNNs have emerged as pivotal architectures in analyzing graph-structured data, and their expansive application in sensitive domains requires a comprehensive understanding of their decision-making processes --- necessitating a framework for GNN explainability. An explanation function for GNNs takes a pre-trained GNN along with a graph as input, to produce a `sufficient statistic' subgraph with respect to the graph label. A main challenge in studying GNN explainability is to provide fidelity measures that evaluate the performance of these explanation functions. This paper studies this foundational challenge, spotlighting the inherent limitations of prevailing fidelity metrics, including $Fid_+$, $Fid_-$, and $Fid_\Delta$. Specifically, a formal, information-theoretic definition of explainability is introduced and it is shown that existing metrics often fail to align with this definition across various statistical scenarios. The reason is due to potential distribution shifts when subgraphs are removed in computing these fidelity measures. Subsequently, a robust class of fidelity measures are introduced, and it is shown analytically that they are resilient to distribution shift issues and are applicable in a wide range of scenarios. Extensive empirical analysis on both synthetic and real datasets are provided to illustrate that the proposed metrics are more coherent with gold standard metrics. The source code is available at 
\href{https://trustai4s-lab.io/fidelity}{https://trustai4s-lab.io/fidelity}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzes the inherent limitations of prevailing fidelity metrics and proposes a robust class of fidelity measures.
The contributions are mainly about the relevant theoretical analysis

### Strengths
- Sufficient theoretical discussions regarding prevailing fidelity metrics are introduced in the paper

### Weaknesses
 - The paper is poorly structured. The theoretical analysis took up too much space, and many of the derivations can be moved into the appendix. In the meantime, the discussion for the motivation of Fidelity measures is too limited.  Experimental results are also too limited.
- I hope the paper can better justify why the proposed fidelity metrics are ideal, and especially discuss their differences and relations with respect to the existing explainable GNN methods. Such discussions are lacking
- It is not apparent that why technical theoretical results are special for graphs. Many definitions and discussions seem to relate to general machine-learning problems. Can they be applied to data beyond graphs? If so, why the paper restrict the scope to graphs?

### Questions
- Can the proposed fidelity measures be applied to data beyond graphs? If so, why the paper restrict the scope to graphs?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The present work studies existing fidelity metrics to quantify performance of GNN explanation methods. Through a theoretical analysis, the authors find that existing fidelity metrics are not well-behaved for a wide set of scenarios without special properties due to the OOD nature of explanation subgraphs. To address this, the authors proposed modified fidelity metrics where explanation subgraphs are transformed to approximate the underlying data distribution and hence obtain more accurate approximations of predictions from trained GNN models, which, the authors argue, provide well-behaved proxy fidelity metrics.

### Strengths
-	Addressing a fundamental aspect of GNN explainability, i.e., how well current metrics evaluate GNN explanation methods. This is a crucial topic.
-	Theoretical and empirical analysis to show that the widely accepted fidelity metrics are not well behaved for a wide range of scenarios without special properties. 
-	Innovative proposal to transform sampled explanation subgraphs closer to the distribution of graphs in the training set for a well-behaved measure of fidelity.

### Weaknesses
The authors mention that current fidelity metrics are not well behaved because optimized models learn how to approximate the (graph) data distribution when making predictions and explanation subgraphs are rarely part of the dataset on their own, resulting in (potentially) poor estimates of predictions for explanation subgraphs. To address this, the authors design fidelity metrics which add/remove edges such that the explanation subgraphs approximate the training data distribution during evaluation of fidelity. I have three questions regarding this:
1.  What are the authors’ thoughts on how the nature of explanations should be? I think intuition says that explanation subgraphs should indeed be OOD w.r.t. the data distribution, after all, we’re looking for *sub*graphs that stand out (can be predictive on their own). Do authors generally think that the field should be moving to finding IID explanation subgraphs (if this is possible)?
2.  It appears that the OOD aspect is addressed in the proposed fidelity metrics. However, it seems to me that the sampling when computing fidelity metrics means that these metrics are not actually measuring fidelity of the actual explanation subgraph (but down/up-sampled versions of it). Why/how can we say that these fidelity metrics actually correspond to the explanation subgraphs themselves when these metrics measure fidelity *not* exactly for the explanation subgraphs?
3. A different direction could be to accept that predictions for OOD subgraphs are not as accurate and compute fidelity metrics and compare explanations for subgraphs with the same sparsity level, as is done in https://proceedings.neurips.cc/paper/2021/file/2c8c3a57383c63caef6724343eb62257-Paper.pdf What are the authors’ thoughts on this?

The authors have done a great job at studying how fidelity metrics are not well behaved for a wide range of scenarios, which is a crucial question in GraphXAI. I, however, have some questions regarding their solution to the OOD issue of explanation subgraphs, specifically, my question 2. If this (and other concerns) are addressed, I am open to updating my score.

### Questions
Could you elaborate on why proving that the proposed fidelity metrics are monotonically increasing in p means that they are monotonically increasing with the mutual information?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper points out a crucial problem in evaluating the explainability of Graph Neural Networks (GNNs) that the subgraph is distributed differently from the training graphs. Recognizing the limitations of conventional fidelity metrics ($Fid_+$, $Fid_-$, and $Fid_\Delta$) in capturing genuine model explainability due to the potential distribution shifts, the authors introduce an information-theoretic definition of explainability, carefully design and propose a straight forward evaluation methods by adopting sampling. They use 4 datasets and two tasks in the experimental part. They show that the proposed method is more consistent to ground truth ones.

### Strengths
1. The research problem is significant in the graph learning domain. They show that the existing evaluation method is heavily affected by distribution shifting problem, which is overlooked by existing methods. The proposed evaluation method has the potential to set new standards in the evaluation of GNN explainability.
2. The paper provides strong theoretical analysis and empirical verification.
3. The paper provides a simple and effective method with solid theoretical foundation.

### Weaknesses
I  have a minor concern that the proposed evaluation method is not deterministic and more time consuming comparing to the original fidelity measurement.

Minor typos. 

1. In the introduction, "nodes presenting atoms" should likely be "nodes representing atoms".
2. In the introduction, "subgraph of the input which satisfies two conditions" shoule be "subgraph of the input that satisfies two conditions"
3. In Section 3, "low error probability" should be "a low error probability", "with error close"-> "with an error close", " has Bayes error rate" -> " has a Bayes error rate"

### Questions
1. Why the proposed method fails with GIN on Tree-grid?
2. How to select $alpha_1$ and $alpha_2$?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tackles the crucial challenge of evaluating the fidelity of explanations provided by Graph Neural Networks (GNNs). Given the increasing importance of GNNs in sensitive sectors, understanding their decision-making process is paramount. Traditionally, fidelity metrics like $Fid_+$, $Fid_-$, and $Fid_\Delta$ have been utilized to measure the correctness of these explanations. The intuition behind these metrics is to assess the change in model predictions when certain subgraphs, deemed important for predictions, are masked out or removed. However, the authors spotlight potential issues with these metrics, chiefly the distribution shift when subgraphs are removed. An information-theoretic framework for GNN explainability is presented, highlighting the misalignment of prevalent surrogate fidelity metrics with their proposed fidelity measure. As a solution, a novel class of fidelity measures that are robust to distribution shifts is introduced. The paper validates these measures through empirical analysis on synthetic and real datasets, demonstrating that the new metrics align more closely with ground truth explanations.

### Strengths
Originality: The paper effectively spotlights an overlooked issue in the field of explainable graph learning, bringing to the fore the inherent shortcomings of widely accepted evaluation methodologies. The introduction of robust evaluation metrics grounded in information theory provides a fresh perspective on the problem.

Quality: The paper maintains high standards in its methodological approach. It's evident that thorough theorical analysis and experiments has been done.

Clarity: Overall, the paper is well organized that logically from identifying the problem, proposing a theoretical framework, and then introducing new evaluation metrics. It would be better if the authors can use a figure to clearly illusrate the differences between original fidelity and the proposed ones. 

Significance: This research is timely and significant. Given the increasing number of papers on explainable GNNs. The routinely adopted metric is problematic and maybe misleading.  The paper's proposed fidelity metrics could play a important role in the literature.

### Weaknesses
1. The proposed metrics are not easy to understand until reading the algorithm in appendix. 

2. Only small scale datasets are adopted to evaluate the proposed metrics. 

3. It is unclear why we need to consider the rate of convergence in fidelity measurements.

### Questions
1. On Page 5, the authors claims that the convergence ratio of fidelity is 1/2. What does that mean in practice?  Does the proposed metric provide better convergence rate?

2. The paper focus on graph classification problem. But in the experiment, there are two node classification datasets, how can this method be applied for node classification task?

3. is OOD problem unique to graph? Or it also affects other domains, like images and natural languages.

4. Are there computational complexities or scalability concerns with the new metrics, especially when dealing with large real-world graphs?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
