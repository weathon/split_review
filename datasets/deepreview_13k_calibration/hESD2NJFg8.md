# Label-free Node Classification on Graphs with Large Language Models (LLMs)

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
In recent years, there have been remarkable advancements in node classification achieved by Graph Neural Networks (GNNs). However, they necessitate abundant high-quality labels to ensure promising performance. In contrast, Large Language Models (LLMs) exhibit impressive zero-shot proficiency on text-attributed graphs. Yet, they face challenges in efficiently processing structural data and suffer from high inference costs. In light of these observations, this work introduces a label-free node classification on graphs with LLMs pipeline, LLM-GNN. It amalgamates the strengths of both GNNs and LLMs while mitigating their limitations. Specifically, LLMs are leveraged to annotate a small portion of nodes and then GNNs are trained on LLMs' annotations to make predictions for the remaining large portion of nodes. The implementation of LLM-GNN faces a unique challenge: how can we actively select nodes for LLMs to annotate and consequently enhance the GNN training? How can we leverage LLMs to obtain annotations of high quality, representativeness, and diversity, thereby enhancing GNN performance with less cost?
To tackle this challenge, we develop an annotation quality heuristic and leverage the confidence scores derived from LLMs to advanced node selection. Comprehensive experimental results validate the effectiveness of LLM-GNN {on text-attributed graphs from various domains}. In particular, LLM-GNN can achieve an accuracy of 74.9\% on a vast-scale dataset \products with a cost less than $1$ dollar.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to combine Large Language Models(LLMs) and Graph Neural Networks(GNNs), leveraging their strengths. GNNs achieve promising performance when dealing with graph-structured data, while it needs abundant high-quality labels to ensure the performance. On the other hand, LLMs shows impressive zero-shot proficiency on text-attributed graphs, but it suffers from high inference costs and processing structural data. This paper suggests LLM-GNN, using LLM for annotation, providing training signals on GNN for further prediction. Moreover, the authors propose node selection strategy and confidence-aware annotation for efficient learning with high quality annotations.

### Strengths
- The proposed method is well-motivated.
- Each component supports motivation reasonably.
- Well written paper, it is easy to follow.

### Weaknesses
 - The performance gain is incremental, especially for Difficulty-aware active node selection (DA).
- Explanations about experiments are not enough, and some parts are unclear. Please refer to questions for details.
 - In Figure 2 or Figure 12, the trend of decreasing accuracy as the distance between nodes and cluster centers increases seems somewhat weak in average accuracy. Even in Table 2, when DA is added to traditional graph active selection and when DA is added to the use of PS, there are many cases where performance actually decreases. I acknowledge that tuning was not performed, but there are still too many cases where performance declines. While the authors said that grid search would improve the performance in a specific case, it seems necessary to perform more tuning across a broader range of cases to clearly demonstrate the effectiveness of DA.
- In Table 6, is it realistic to use labels in 1-shot example when we are considering the "Label-free" setting? Furthermore, how are the confidence scores determined in that example? More detailed explanation is required.
- In Figure 4, why do some methods show an increase in performance after a budget of 70, followed by a sharp decline? Could this be attributed to class-imbalance issues during the selection process?
- While there is an example in Figure 5, it would be beneficial to demonstrate on different datasets that LLM-GNN achieves competitive performance with GNNs trained on ground truth labeled data, while significantly reducing costs.

### Questions
- In Figure 2 or Figure 12, the trend of decreasing accuracy as the distance between nodes and cluster centers increases seems somewhat weak in average accuracy. Even in Table 2, when DA is added to traditional graph active selection and when DA is added to the use of PS, there are many cases where performance actually decreases. I acknowledge that tuning was not performed, but there are still too many cases where performance declines. While the authors said that grid search would improve the performance in a specific case, it seems necessary to perform more tuning across a broader range of cases to clearly demonstrate the effectiveness of DA.
- In Table 6, is it realistic to use labels in 1-shot example when we are considering the "Label-free" setting? Furthermore, how are the confidence scores determined in that example? More detailed explanation is required.
- In Figure 4, why do some methods show an increase in performance after a budget of 70, followed by a sharp decline? Could this be attributed to class-imbalance issues during the selection process?
- While there is an example in Figure 5, it would be beneficial to demonstrate on different datasets that LLM-GNN achieves competitive performance with GNNs trained on ground truth labeled data, while significantly reducing costs.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Given a text attributed graph without labels, the paper proposes a cost-effective method that combines LLMs and GNNs to annotate the labels in four steps. In the first step, the paper selects the nodes that should be annotated and terms it  as difficulty aware selection. It combines active learning (selection) techniques along with a difficulty score which is based on the distance from the center of a cluster. In the second step, annotations are created for the selected nodes using an LLM which also generates a confidence score. In the third step, nodes are pruned such that the confidence score of LLMs is high without significantly changing the diversity of nodes (via change in entropy). Finally, a GNN is trained on the graph to generate labels for other nodes.

### Strengths
- The idea of label-free annotation using LLMs on text attributed graphs is an interesting research direction introduced by the paper.

- The paper has experimented with different datasets and incorporated various existing techniques to come up with a cost-effective model.

- This paper appropriately balanced traditional graph active selection criteria with annotation quality by incorporating difficulty-aware active selection with post filtering to obtain training nodes from LLM.

### Weaknesses
 - Difficulty aware (DA) selection: According to the paper, LLMs annotation quality degrades when they have to annotate nodes which are away from the centers. It implies that the LLMs annotation quality would suffer in case of the diverse nodes (away from center).  However, GNNs accuracy will only improve if the nodes are diverse. Hence, difficulty aware selection i.e. use of c-density might not always help and, in fact, it may hinder in some cases. This is also evident from the results shown in Table 2 : Active_Selection_Methods and the corresponding  DA-Active_Selection_Methods show similar performance on average across different techniques (i.e., selection methods). Moreover, for at least 50% of the cases, the DA-method (row 2) performs poorly compared to the corresponding active learning method (row 1). The paper does not sufficiently address the potential for DA selection to introduce a bias towards less diverse, and potentially less informative, nodes. The reliance on cluster centers as a proxy for annotation quality may oversimplify the complex relationship between node position and the informativeness of its label for training a GNN.

- Though the accuracy from the LLM-GNN model is good (and of course, the model is efficient), it couldn't outperform LLM as a predictor (Table 3). This raises questions about the necessity of the GNN component, given that the LLM alone seems to achieve superior performance in some cases. The paper needs to provide a more compelling justification for the added complexity of the GNN, especially if it does not consistently improve upon the LLM's predictive capabilities.

- The methods are heuristics and do not have theoretical evidence. The lack of theoretical grounding makes it difficult to understand the conditions under which the proposed method will perform well, and when it might fail. This limits the generalizability of the approach and makes it challenging to compare with other methods that have theoretical guarantees.

### Questions
- Post-filtering (PS): How useful are the confidence scores generated by the LLMs (Appendix F.1, table 6)? Showing the mean and variance of confidence score for each dataset may help in understanding its impact on performance.

- Providing the number of nodes selected in each step in the experiment will also help in understanding the effects of the steps. For instance, could you please provide the number of selected nodes during active selection and DA-active selection? Also, what is the pruning ratio when applying PS? All this information can help in understanding the efficacy of the steps.

- PS-DA-methods have not performed well in most cases compared to DA-methods (Table 2). Any insights on this can help in understanding these steps better.

Minor Questions:

- Detail explanation on f_{act}(vi) is missing

- It is mentioned in page 5 that the detailed descriptions and full prompt examples are shown in Appendix D. However, it is missing any detailed descriptions.

Typos:

- Page 7: (4) Combing - supposed to be combining?

- Page 3: GNN modelson- models on (space missing)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study label-free node classification by combining LLMs with GNNs. Specifically, the proposed method first leverages LLMs to annotate a small portion of nodes, then uses GNNs with the pseudo-labels to classify the remaining large portion of nodes. The main challenges lie in how to actively select nodes and leverage LLMs to obtain reliable labels for those nodes. Three modules, including difficulty-aware active node selection, confidence-aware annotations, and post-filtering are proposed to tackle the challenges. Experimental results on text-attributed graphs demonstrate the effectiveness of the proposed method, especially compared with heuristically choosing annotated nodes.

### Strengths
1. The proposed method is among the first trials of combining LLMs with GNNs to solve a novel problem, i.e., label-free node classification.
2. The proposed method is clearly described and the paper is easy to follow in general.
3. The authors compare with various heuristic baselines and conduct analyses to demonstrate the efficacy of the proposed method.

### Weaknesses
1.	Though I acknowledge that the proposed method is a valid solution, the technical contribution of the paper is somewhat limited, especially considering that the three major components are largely based on heuristic observations, and the rest are based on existing LLMs and GNNs. It would make the paper stronger if some theoretical analyses could be provided for the proposed components.  
2.	The authors should more explicitly mention that their proposed method only works for text-attributed graphs rather than any general graph, e.g., in the abstract and introduction. Otherwise, the paper may have overclaiming issues.  
3.	In generating the initial node labels using LLMs, it seems that only the feature information is utilized and no structure is considered. Since it is well-known in the graph machine learning literature that both features and structures greatly affect the node labels, there exists a large room for improvement.    
4.	There are some missing related works regarding zero-shot node classification such as [1-2], which should be added.  
5.	I also wonder how different LLMs affect the model (the reported results are all based on GPT-3.5-turbo).

### Questions
See Weaknesses above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a novel approach called LLM-GNN for label-free node classification on graphs, which combines the strengths of Graph Neural Networks (GNNs) and Large Language Models (LLMs) while mitigating their limitations. It addresses the challenge of obtaining high-quality labels for graph-structured data by leveraging LLMs' zero-shot learning capabilities. LLM-GNN actively selects nodes for annotation by LLMs, generates confidence-aware annotations, and refines annotation quality through post-filtering. The approach achieves impressive results on a massive-scale dataset, OGBN-PRODUCTS, without the need for costly human annotations.

### Strengths
1. LLM-GNN presents an innovative approach to node classification on graphs by harnessing the complementary strengths of GNNs and LLMs. It acknowledges the challenges of obtaining high-quality labels and proposes a label-free solution, which is a significant contribution to the field of machine learning.
2. The paper demonstrates the cost-effectiveness of LLM-GNN by achieving high accuracy on a large dataset with annotation costs under 1 dollar. This cost-efficient approach is particularly relevant for real-world applications with resource constraints.
3. LLM-GNN offers a comprehensive methodology that not only utilizes LLMs for annotations but also considers active node selection, confidence-aware annotations, and post-filtering. This approach ensures the quality, representativeness, and diversity of annotations, addressing key challenges in label-free node classification.

### Weaknesses
1. Since LLMs generate annotations without access to ground truth labels, there is a risk of noisy annotations.  It would be better to investigate the robustness of LLM-GNN to noisy annotations and potential strategies for mitigating their effects. Specifically, the paper should explore the impact of different types of noise (e.g., random, systematic, label-dependent) on the performance of LLM-GNN. Furthermore, it should investigate techniques to reduce the impact of noisy annotations, such as label smoothing, robust loss functions, or data augmentation techniques that are tailored for noisy labels in graph data.
2.  LLM-GNN's performance is demonstrated on a specific dataset (OGBN-PRODUCTS), and while it achieves impressive results, its generalizability to other datasets or domains is not thoroughly explored in the paper. The effectiveness of the approach in different scenarios and with various types of graphs should be investigated to assess its broader applicability. For instance, the paper could explore the performance of LLM-GNN on graphs with different node feature types (e.g., numerical, categorical, multi-modal) or on graphs with varying structures (e.g., dense, sparse, hierarchical). Additionally, the paper should consider the impact of different graph sizes on the performance and scalability of LLM-GNN. 
3. There could be better with a detired comparison on the economic perspective. The paper should include a more detailed economic analysis by comparing the costs of LLM-GNN with traditional supervised learning methods and other label-free approaches. This analysis should consider not only the direct costs of LLM annotations but also the computational costs of training the GNN models with these annotations. Furthermore, the paper should discuss the trade-offs between the cost of annotations and the accuracy of the model.

### Questions
see the weakness

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
