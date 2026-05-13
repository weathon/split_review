# Interpretable and Convergent Graph Neural Network Layers at Scale

- Decision: Reject
- Scores: 3, 6, 6, 3, 8

## Abstract
Among the many variants of graph neural network (GNN) architectures capable of modeling data with cross-instance relations, an important subclass involves layers designed such that the forward pass iteratively reduces a graph-regularized energy function of interest. In this way, node embeddings produced at the output layer dually serve as both predictive features for solving downstream tasks (e.g., node classification) and energy function minimizers that inherit desirable inductive biases and interpretability. However, scaling GNN architectures constructed in this way remains challenging, in part because the convergence of the forward pass may involve models with considerable depth.  To tackle this limitation, we propose a sampling-based energy function and scalable GNN layers that iteratively reduce it, guided by convergence guarantees in certain settings.  We also instantiate a full GNN architecture based on these designs, and the model achieves competitive accuracy and scalability when applied to the largest publicly-available node classification benchmark exceeding 1TB in size.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies how to scale unfold GNNs to large-scale graph benchmarks while maintaining acceptable computational and memory overheads, aligning with common GNN alternatives. Specifically, the authors integrate offline subgraph sampling into the energy function to propose a novel sampling-based energy function and derive convergence guarantees for the novel objective, demonstrating its theoretical feasibility. The authors also empirically demonstrate the effectiveness of MuseGNN constructed using the subgraph sampling-based energy function across datasets of widely varying sizes.

### Strengths
1. This article is well-organized.
2. The author has presented sufficient theoretical proof to ensure the convergence of the novel sampling-based energy function during training.
3. The proposed MuseGNN framework achieves state-of-the-art performance on the largest graph benchmark IGB-full.

### Weaknesses
1. The paper emphasizes \textbf{Interpretable} in the title and illustrates the explanality of energy minimizers. The key concern is the energy minimization is not aligned with the common concept of GNNs interpretation. For example, some of existing works of interpretable GNNs highlight neighborhood structure leading to the node label classification. The superficial conclusion of node embedding information stemming from the node itself or neighbors makes no sense to the real interpretable applications. 
2. In addition, the absence of case study to validate the explanations provided by the energy function raises questions about one of the paper's main claims.
3. The incorporation of the energy minimization into GNNs is not novel. The Dirichilet energy of node embeddings, i.e., the second term in Eq.(2), has been extensively studied in graph domains and GNNs. For example, it has been used to analyze over-smoothing issue in [1]. Following this work, several novel GNNs to optimize this energy function have been proposed. The constraint of closeness to base model embedding, i.e., the first term of Eq. (2), has been implicitly included in models like SIGN [2], SAGN [3], DAGNN[4].

### Questions
1. Please address the previous concerns.
2. Present more results about ablations on $\gamma$, i.e. results on IGB-full, the dataset where traditional GNNs with sampling technique obviously suffer a significant performance degradation, to further demonstrate the effectiveness of $M$.
3. In Proposition 3.1, what is the definition of l(M)? What is the purpose of this proposition?
4. According to my understanding, the main novelty of this paper is to incorporate the shared summary embedding matrix $M$ into energy to facilitate controllable linkage between the multiple embeddings that may exist for a given node appearing in different subgraphs (Because the Formula 6 is a commonly used technique for large-scale training). But existing ablation on $\gamma$ are not sufficient to demonstrate the general effectiveness of this additional constraint term.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A sampling-based energy function and scalable GNN layers, MuseGNN, is proposed. Convergence guarantees (under certain assumptions) are provided. Experiments on the large dataset IGB-full and MAG240M demonstrate the scaleability of MuseGNN and its competitive performance with GATs (combined with neighbourhood sampling).

### Strengths
- The background of unfolding GNNs, related energy functions, etc. is well explained.
- Advantages of the proposed offline sampling approach are discussed that also enable a convergence analysis.
- Assuming that there exists a unique solution, a theoretical convergence analysis derives a convergence rate of $O(1/\sqrt(t) + \exp(-Ck))$.
- The method enables training on very large graphs and achieves state-of-the-art performance on IGB-full.

### Weaknesses
 - Novelty: What are the practical benefits of the proposed sampling method over neighbourhood sampling?
- MuseGNN is integrated into the energy function and thus a less general approach than neighborhood sampling, which can be applied to most message passing GNNs.
- In comparison to GAT with neighbourhood sampling, the proposed MuseGNN requires a few more training epochs. Also the performance of GAT with neighbourhood sampling is often competitive. 
- Significance intervals are not provided for GAT with neighbourhood sampling on the very large graphs, yet, they are computed for the proposed MuseGNN. The reasoning by the authors are long run times. However, GAT with neighbourhood sampling is reported to be slightly faster than MuseGNN. Thus, significance intervals should also be attainable in this case. Without them, the statement that MuseGNN achieves a new state of the art is not actually accurate.
- The convergence analysis relies on the strong assumption of a unique solution.


Minor points:
- The discussed concept of interpretability seems of minor relevance, as it does not relate to explaining how trained GNNs solve a task. It actually refers more to a concept of consistency over samples. What should the practical benefit of this be?

### Questions
-What are the limitations of neighborhood sampling that require the development of the proposed offline sampling scheme? From a practical point of view, what are the actual disadvantages of NS that motivate the development of MuseGNN?
-Please add significance intervals for GAT with neighbourhood sampling for GAT (NS) and SAGE (NS) and GCN (NS). 
- What are the number of training epochs for GCN (NS)?
- What are the actual training and inference times for the baselines and MuseGNN? This is also a relevant question because the sampling schemes themselves could take different amounts of time.
- What are the memory requirements of MuseGNN versus the baselines?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Unfold GNNs are those whose forward pass iteratively reduces a graph-regularized energy function of interest. The node embeddings of unfolded GNNs serve as both predictive features and energy function minimizers. This paper proposes a sampling-based energy function and designs a scalable unfolded GNN (MuseGNN). The authors also theoretically analyze the convergence behavior of MuseGNN.

### Strengths
1. This paper is well-structured and well-written. I really enjoy reading this paper.
2. The proposed method makes sense to me.
3. The experiment results are good compared to the baselines.

### Weaknesses
1. Lack of comparison with representative sampling-based GNNs, such as [a, b].
2. The authors did not conduct experiments on datasets that can illustrate the importance of unfolded GNNs.

### Questions
Please see "weakness".

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors of the paper present a new approach to address the scalability issues of Graph Neural Networks (GNNs) when constructed with sampling-based energy functions. The paper also discusses the motivation behind unfolded GNNs, their advantages in terms of interpretability, and the challenges of scaling such models. It introduces the MuseGNN model, which addresses these challenges by incorporating efficient subgraph sampling into the energy function design. It demonstrates increased performance over the baselines on large-scale node classification tasks.

### Strengths
1. The paper introduces a novel approach to address the scalability challenges faced by GNNs. The incorporation of offline subgraph sampling into the energy function design is a unique and innovative concept.

2. The paper provides a theoretical analysis of the convergence properties of MuseGNN, when γ is set to 0.

3. The paper includes experimental results showing that MuseGNN performs competitively in terms of accuracy and scalability, especially on large graphs exceeding 1TB in size. This demonstrates the practical feasibility of the proposed approach in large scale graphs.

### Weaknesses
1. One notable weak point of the paper's experimental evaluation is its limited comparison to a rather outdated set of baseline models. While the paper does present compelling results in terms of the proposed MuseGNN's performance, the absence of more contemporary and diverse baseline models hinders the thorough assessment of the method's competitiveness and applicability in the current research landscape. Graph neural networks have seen significant advancements in recent years, resulting in a multitude of state-of-the-art models and techniques that offer superior performance across various graph-related tasks. Focusing solely on older and limited baseline models (GCN, GraphSage, GAT) from the past can potentially lead to a skewed perspective of MuseGNN's relative performance in the current state of the art. A more comprehensive comparison against a broader range of modern baseline models would provide a more accurate and up-to-date assessment of the strengths and weaknesses of MuseGNN. I provide some example papers [1,2,3] that can be used as baselines below. Moreover, in the ogb leaderboard https://ogb.stanford.edu/docs/leader_nodeprop/#ogbn-arxiv there are many new baselines.

2. Another weak point in the paper lies in its motivation and justification for employing unfolded GNNs, especially for those who may not be well-versed in this specific research area. While the paper briefly discusses the benefits of using unfolded GNNs and emphasizes their role in enhancing explainability by distinguishing the relative importance of node features and graph structure in predictive tasks, the argument remains somewhat vague and underdeveloped. The paper primarily suggests that the use of unfolded GNNs can help reveal whether node features or graph structure hold more significance for predictions. However, it lacks a more thorough and nuanced discussion of why this is an important aspect to investigate, and how this contributes to the broader field of graph-based machine learning or the potential practical implications.

### Questions
1. Could the authors provide more context on their choice of limited and older baselines for comparison? Are there more recent or relevant methods that could have been included for a more comprehensive evaluation?

2. The paper claims that using unfolded GNNs enhances explainability, but the argument remains somewhat abstract. Can the authors provide specific instances or use cases where this enhanced explainability has a direct impact on decision-making or model interpretability?

3. Can the authors elaborate on the practical scenarios where distinguishing the importance of node features and graph structure is particularly valuable? How might this knowledge influence real-world applications, and can the paper provide more concrete examples?

4. The paper would benefit from a more comprehensive and well-structured explanation and rationale for the concept of unfolded GNNs.

I am more willing to increase my score, if the authors properly address the above concerns.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes a novel architecture for graph data. It extends the "unfolded GNN" line of research, where GNNs are formulated by an outer loss function to be minimized, and an inner energy function which is minimized layer-by-layer. In this inner energy function, a "base model" (e.g., an MLP over the nodes) is defined, and the graph layer is defined as a balance between deviating from this base model and smoothing the signal over the graph. 

To scale it up, in the proposed MuseGNN the authors combine the idea of sampling subgraphs from the original graph with the unfolded GNN model. A new unfolded model is defined by running the original unfolded model on each subgraph, augmented by an additional regularization term that enforces similarity across subgraphs of the nodes' representations.

They show several convergence analyses on the model of different types. On the experimental side, they show the model is able to achieve better results on very large datasets with slightly higher training time than the baselines.

### Strengths
The paper is well written and easy to follow. The idea is described clearly. The model is a combination of two known ideas (unfolded GNNs and subgraph sampling), but it is complemented by a good theoretical analysis and good experimental results. Overall, this is an interesting contribution for the field.

### Weaknesses
The biggest weakness of the paper is that the authors keep saying that the model is "interpretable" (e.g., "while maintaining the interpretability attributes of an unfolded GNN"), but this is never truly motivated. The idea is that a user can look at the difference between the base model and the true output to understand whether the prediction was done by looking at the features or at the graph's structure, but this is a very weak notion of "interpretability". In addition, the authors are never showing examples of this.

I have not found any analysis on the memory of the approach, which requires storing predictions and auxiliary embeddings for multiple subgraphs. In addition, the authors should provide an ablation study on the number of subgraphs that are chosen.

In the related works, several papers have proposed subgraph-based GNNs to improve the expressiveness of standard message-passing. Can you compare your approach, either methodologically or experimentally?

### Questions
Based on the listed weaknesses:
1. Add a true explainability analyis or remove most of these claims.
2. Add an analysis of the memory required by the model.
3. Add some ablations on the number of chosen subgraphs.
4. Improve the related works section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
