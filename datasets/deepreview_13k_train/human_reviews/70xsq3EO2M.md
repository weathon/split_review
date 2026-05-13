# Learning Ante-hoc Explanations for Molecular Graphs

- Decision: Reject
- Scores: 5, 6, 8, 3, 3

## Abstract
Explaining the decisions made by machine learning models for high-stakes applications is critical for transparency. This is particularly true in the case of models for graphs, where decisions depend on complex patterns combining structural and attribute data. We propose EAGER (Effective Ante-hoc Graph Explainer), a novel and flexible ante-hoc explainer designed to discover explanations for graph neural networks, with a focus on the chemical domain. As an ante-hoc model, EAGER inductively learn a graph predictive model and the associating explainer together. We employ a novel bilevel iterative training process based on optimizing the Information Bottleneck principle, effectively distilling the most useful substructures while discarding irrelevant details. As a result, EAGER can identify molecular substructures that contain the necessary and precise information needed for prediction. Our experiments on various molecular classification tasks show that EAGER explanations are better than existing post-hoc and ante-hoc approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors propose to learn an edge weighting scheme together with a graph neural network where the edge weights serve as explanation of the graph neural network. The combined training of the explainer and the GNN minimizes an Information Bottleneck objective to reduce the size of the explanations while maximizing the predictive performance of the GNN learner. Empirical experiments on suitably preprocessed datasets suggest that the method, called EAGER, works well in practice.

### Strengths
- The paper is well structured and introduces all relevant concepts and steps
- Ante-hoc explainers -- in this case subgraphs on which the GNN model is allowed to learn solve several of the problems of instance based post-hoc explanations of graphs
- the overall architecture seems simple and elegant

### Weaknesses
 - It remains unclear from the presentation whether indeed subgraphs are used or whether the explainer computes an edge weight that just scales down edge attributes during training and/or inference. In the latter case, explanations would be not much helpful, I fear.
- The edge weighting approach to arrive at a subgraph(?) is not expressive enough to capture many phenomena that are taking place in graphs. See question below.
- It remains unclear how to control the size of the explanations/subgraphs

### Questions
# Statement
I am terribly sorry about my lapse. There is really no excuse for posting the wrong review here and then not reacting to multiple questions here. I have changed it now, but please, ignore my questions and comments, as there is really no time left to act on them. I accept full responsibility and am truly sorry. 

# Questions

- Can you please be more precise about the usage of the edge weights in training and inference? Is $\alpha$ in Algorithm 1 a hard threshold that removes all edges with weight $<\alpha$? How to choose this?
- Assuming thresholding takes place: Is precision at 10 or ROC a good evaluation measure? In this case, I assume that one has no influence on the amount of edges that is selected by the explainer.
- Assuming no thresholding takes place: How can you ensure that the GNN after edge weighting only uses information of high weight edges, as claimed in the introduction. In this case, it seems that message passing uses all existing edges of the graph and may also reweight low weight edges from the explainer with suitable parameters.
- Furthermore both p@10 and ROC at some point require to select a threshold. Does this imply that the user needs to know/set the size of the explanations that they want to get?
- The explainer model seems to weight edges independently of graph topology, just based on attributes of the edge and the two incident nodes. This, however, implies that such an explainer cannot distinguish e.g. a C-C edge on a six-cycle from a C-C edge on a three-cycle. Hoever, it seems, that this is the case in Figure 1c. Are you using some particular preprocessing to add this information?

# Minor issues and typos
- l75 We introduces
- l203 two distributions are keps
- Algorithm 1 / Section 3.4.2 use inconsistent notation. While in Alg.1 $\alpha$ appears as threshold parameter, it appears as a tradeoff parameter in a different place. I suggest to rename one of the alphas and to consistently use the same sybmol for the threshold parameter in Alg.1 and Sec.3.4.2

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Summary:

The paper proposed EAGER - an ante-hoc graph explanation method by optimizing the information bottleneck principle via a bilevel optimization process.

### Strengths
Strengths:

1. An ante-hoc graph explanation model is an crucial topic.
2. Introducing a bilevel optimization method is interesting.

### Weaknesses
Weaknesses:
1. My primary concern is about the efficiency of the proposed method, particularly given its dual role as both an explanation method and a Graph Neural Network for predicting molecular properties. The efficiency of this method is crucial for its practical application. The authors should thoroughly discuss the computational complexity of their method in the main section of the paper and include experiments on running time. Currently, the assessment of running time is relegated to the appendix and only tested on a relatively small synthetic dataset. This is insufficient to demonstrate the method's efficiency effectively. More comprehensive testing on larger and more diverse datasets is necessary to establish a clearer understanding of the method's performance in real-world scenarios.
2. The effectiveness of the target Graph Neural Network (GNN) model significantly influences the quality of explanations provided. In prior research, particularly with post-hoc explanation methods, it is common practice to maintain a consistent target model across different methods to ensure fair comparisons with baseline approaches. However, due to the unique architecture of the proposed method, it does not use the same GNN classifier as the one employed in the baseline methods. This discrepancy could compromise the fairness of direct comparisons between the proposed method and other baselines, as the underlying GNN model differences might affect the outcome independently of the explanation method's effectiveness.
3. The datasets currently used in the study are relatively small. To more effectively demonstrate the capabilities of the proposed method in classification tasks, it would be beneficial to employ larger datasets, such as HIV or PCBA. Utilizing these more extensive datasets could provide a more robust evaluation of the method's performance.
4. Figure 3 lacks clarity. A more detailed illustration is required to effectively display each component of the process. The figure should aim to distinctly outline and explain the functionalities of each part, ensuring that the figure conveys the intended information clearly and accurately.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes EAGER (Effective Ante-hoc Graph Explainer), an innovative framework designed to produce explainable predictions in graph neural networks (GNNs), particularly for molecular classification tasks. By utilizing the Information Bottleneck (IB) principle and bilevel optimization, EAGER jointly learns a GNN and its explainer, producing both accurate and interpretable predictions. The authors present competitive results across various datasets, demonstrating EAGER's superior performance compared to both ante-hoc and post-hoc explainers.

### Strengths
1. Introduces a novel ante-hoc approach that optimizes explainability alongside prediction, addressing limitations of post-hoc methods.

2. Successfully applies a theoretically sound adaptation of the Information Bottleneck principle within GNNs for robust feature selection.

3. Shows empirical advantages over baselines in accuracy, explainability, and reproducibility across synthetic and real-world datasets.

4. Offers substantial evaluation, including interpretability benchmarks, ablation studies, and reproducibility analyses.

### Weaknesses
1. Complex Training Process: The bilevel optimization, though effective, is computationally intensive and requires significant training time compared to other models.

2. Limited Practical Validation: EAGER’s application is restricted to curated datasets; more real-world, large-scale evaluations could better demonstrate its adaptability.

3. Reliance on Specific Hyperparameters: Model performance is sensitive to hyperparameter settings, notably in the inner and outer loop parameters of bilevel optimization.

4. Interpretability Metrics: Just for suggestion, it would be better to have more real-world datasets. For those lacking a ground truth explanation, the fidelity score could be considered.

### Questions
1. Could you elaborate on the rationale for including the average AUC in Table 3? Is averaging the model’s performance across diverse datasets meaningful or informative in this context?

2. Are there plans to include newer baselines in future evaluations? For instance, the addition of MixupExplainer (2023) might provide useful insights for comparing EAGER's performance with recent advances in explainability.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces EAGER, an ante-hoc graph explainer that generates interpretable explanations for graph neural network (GNN) predictions. EAGER uses the Information Bottleneck (IB) principle within a bilevel optimization framework to learn compact, discriminative subgraphs that are closely tied to the model’s prediction. In the process, EAGER assigns influence values to edges, which are incorporated into the graph to create an influence-weighted GNN. This approach ensures that the explanations are jointly learned with the model, providing consistent and reproducible insights into the model's decision-making.

### Strengths
1. This ante-hoc approach avoids the limitations of post-hoc explainers, which often provide inconsistent explanations due to their black-box nature.

2. The paper incorporates edge features directly into the explanation process, which is particularly beneficial for domains like molecular graphs, where edge information is critical.

### Weaknesses
1. Lack of Novelty.
This paper primarily consists of a combination of methods from other studies. The model’s unique methodology is not clearly emphasized. For example, in the Information Bottleneck principle, the iterative algorithm from [1] is used as-is. Moreover, in the explainer and predictor sections, except for simple tricks like permutation invariance, the method of PGExplainer [2] is used directly.

- [1] Tishby, Naftali, Fernando C. Pereira, and William Bialek. "The information bottleneck method." arXiv preprint physics/0004057 (2000).
- [2] Luo, Dongsheng, et al. "Parameterized explainer for graph neural network." Advances in neural information processing systems 33 (2020): 19620-19631.

2. Lack of Distinction from Existing Ante-Hoc Models.
The paper does not present advantages that differentiate it from existing ante-hoc models. For example, it does not explain how the bilevel training approach provides any benefits over GSAT, which uses variational bounds. Furthermore, it lacks an explanation of advantages compared to other GNN models that generate predictions and explanations simultaneously, such as CAL [3] and OrphicX [4].

- [3] Sui, Yongduo, et al. "Causal attention for interpretable and generalizable graph classification." Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2022.
- [4] Lin, Wanyu, et al. "Orphicx: A causality-inspired latent variable model for interpreting graph neural networks." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

3. Need for Fidelity Score in Explanation Evaluation.
In addition to calculating explanation AUC, it is necessary to utilize the Fidelity score [5], which is widely used. It is recommended to assess explanations based on the difference in predicted labels between graphs with and without explanations.

- [5] Yuan, Hao, et al. "On explainability of graph neural networks via subgraph explorations." International conference on machine learning. PMLR, 2021.

4. Limited Baselines.
The baselines in this paper are relatively limited in terms of the explainer models used for comparison. 
CAL [6] and OrphicX [7] are models that predict labels based on important explanatory subgraphs. It would be beneficial to include these as additional baselines for both explanation and classification performance.

- [6] Sui, Yongduo, et al. "Causal attention for interpretable and generalizable graph classification." Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2022.
- [7] Lin, Wanyu, et al. "Orphicx: A causality-inspired latent variable model for interpreting graph neural networks." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

### Questions
Since it uses bilevel optimization, learning might be unstable. Could you show the training curve for loss and accuracy?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents EAGER, a method for producing subgraph explanations for graph neural networks in an *ante hoc* manner. In this method, the input graph is first passed to an explainer network, which learns an edge weight for each edge, where the edge weight reflects the importance/influence of that edge for final prediction. These edge influences are used to modify the input graph (simply scaling the adjacency matrix), which is then passed to the predictor network, which finally predicts the output label. The loss functions are based on information bottlenecking, which uses mutual information to maximize the usefulness of the subgraph explanation for prediction, and minimize the size of the subgraph itself.

In order to train both networks, a meta-learning approach is taken (i.e. bi-level training), where the predictor is trained for several iterations using training data, and the resulting gradients from training the predictor is then used to perform gradient descent on the explainer (using the support dataset).

The EAGER method is based on an existing approach, GSAT, which also uses bi-level training to produce an explainer and predictor network. In contrast with GSAT, which approximates the mutual information between the input graph and the subgraph explanation in the loss using a variational approach, EAGER approximates mutual information using the divergence between their representations.

The experimental results focus on three molecular classification tasks, where the predictive task is to classify molecules with lactam or benzoyl groups. The ground-truth explanations are these lactam or benzoyl groups. The authors show that compared to GSAT (and some *post hoc* explainer methods like PGExplainer), EAGER is able to accurately identify the ground-truth edges in the lactam or benzoyl groups as explanations, and is competitive with other methods or better.

### Strengths
### Many references and explanations to previous works

One of the major strengths of this manuscript is the thoroughness when citing other relevant works. I found it very easy to find relevant literature from the citations, and it was easy to understand the contributions of each of those works, even though I don’t have a background in information bottlenecks for interpretability. I also found it easy to understand how this work (EAGER) differs from previous related works (i.e. what the marginal contributions of EAGER are). I wish all papers in AI/ML were this thorough in references and describing what the marginal contributions are.

### Good evaluations of the accuracy of the explanations

For the datasets where the accuracy of the explanations were evaluated, the evaluations were decently thorough. The accuracy of the explanations was shown by measuring the accuracy of edges which were weighted properly. It was also very informative to see the distribution of edge weights given to the proper ground-truth (i.e. lactam or benzoyl) edges compared to the other background edges, comparing EAGER and GSAT. This figure is particularly compelling, in my opinion.

### Weaknesses
### Experimental results on explainability are on very easy tasks with identical explanations

The three datasets used in this work to evaluate the accuracy of the explanations are all very easy tasks. All three are based on identifying lactam and/or benzoyl groups in small molecules. The predictive task itself is already extremely simple (a neural network isn’t even needed, technically). More importantly, the correct explanation for every single input graph is going to be the same (i.e. a lactam group or a benzoyl group). That is, there is very little to no variation in the explanations between input graphs.

In contrast, real-world tasks on molecules are likely going to be far more complex (e.g. classify molecules based on solubility or toxicity or drug-like properties). In these real-world tasks, the explanations will be far more diverse compared to the datasets/tasks evaluated here. The current evaluation is limited to a very narrow scope of molecular classification, where the ground truth explanations are essentially the same across all inputs. This does not adequately demonstrate the method's ability to handle more complex scenarios where explanations might vary significantly between different input graphs, or where the predictive task requires a deeper understanding of molecular properties beyond the presence of a specific functional group.

Furthermore, the accuracy of explanations from EAGER were only evaluated on these few easy datasets. EAGER is technically a general graph-explainability method, and even though the manuscript is presented as being focused on molecules, it would be very informative to see how it performs on non-molecular graphs. After all, there’s technically nothing that’s preventing EAGER or GSAT from being evaluated on general graphs. Even if this work were to entirely be focused on molecules, it will be crucial to evaluate this method’s performance on more difficult molecular tasks with more diverse explanations. As of now, the predictive tasks are too simple and the correct explanation for every example is the same, which severely limits the evaluation of this method for any reasonable task.

There are other experiments on other molecular datasets, but the results shown are limited to predictive performance, and there are no other results on explainability.

### Unclear details on technical contributions

The writing/flow of the paper is not very clear. The technical details are rather lacking. In particular, the main technical contribution in this paper seems to be the way $I(S, G)$ is calculated in the information-bottleneck loss (paragraph beginning at line 212). However, the exact way this quantity is computed is never really described. The paper mentions an approximation in representation space, but it lacks a clear mathematical definition of how this approximation is implemented. The description should include the specific operations performed on the representations to estimate the divergence, and how this divergence is then used to update the edge weights in the explainer network. Without these details, it is difficult to assess the novelty and validity of the proposed approach.

Algorithm 1 is also included to walk through the EAGER algorithm, but it only describes the bi-level meta-learning approach at a high level, and includes the neural-network architecture backbone. It doesn’t sufficiently describe how the loss is computed. Later equations also define the bi-level optimization in terms of the inner and outer loop, but the losses themselves, $\ell^{tr},\ell^{sup}$, are never defined in the paper. The algorithm description should include the specific loss functions used for both the inner and outer loops, as well as how the gradients are computed and propagated. The lack of clarity on these points makes it hard to reproduce the results and understand the core mechanism of the method.

Since the computation of the loss is the major technical novelty of this paper, more details need to be shown describing this development, as well as the previous attempts. Since this paper’s method (EAGER) is most related to GSAT, the related work should describe the variational approach used in GSAT (at least briefly), and many more details should be given for how EAGER is different. The section on bilevel optimization in related works, incidentally, seems not particularly useful.

On a side note, it is not clear what the purpose of Section 3.3.1 is.

### Limited marginal contribution

The marginal technical contribution of this paper seems to be an improvement on GSAT, where one of the terms in the information-bottleneck loss is computed differently (instead of relying on a variational bound). This marginal technical contribution is not huge, but could still be useful if it leads to large improvements overall, or if there are interesting properties (relative to GSAT) stemming from the difference in how the loss is computed. However, the paper does not provide a rigorous analysis of the theoretical properties of this new approximation, such as its convergence or its relationship to the true mutual information. Without such analysis, it is hard to assess the significance of the technical contribution.

The marginal empirical contribution would ideally provide evidence of consistent improvements, or experiments showing unique technical insights into the method. However, this paper’s empirical contributions are also a bit limited. There are only a handful of very related and easy tasks evaluated (as mentioned above), which are focused on molecules. Together, both the technical and empirical results are somewhat limited.

### Many grammatical/writing issues

There are also many grammatical issues and other typographical errors throughout the manuscript. These are minor blemishes which are not a big issue, but should be fixed regardless. Here is a *very* non-comprehensive list:

- “The main idea is to find [the] most relevant information” (line 183)
- Equation 2 is missing parentheses in the “exp”
- “two distributions are [kept] constant (line 203)

### Questions
### How is $I(S, Y)$ calculated?

The main text says that this is calculated by computing the cross-entropy loss with respect to the labels. Why is the cross entropy a measure of I(S, Y)?

### How is $I(S, G)$ calculated?

The main text mentions an approximation in representation space, but how exactly is this quantity computed?

### How does Equation 2 minimize the objective in Equation 1?

Although Tishby et. al. (2000) proposed this reformulation, it would be great to have some intuition about why these reformulation minimizes the objective function.

### What is the definition of the loss functions $\ell^{tr}$ and $\ell^{sup}$?

The bi-level optimization is key, but the procedure is only described at a very high level (the equations on page 6 only show how the meta-learning is done in general, but not what the losses are. Additionally, what is $\theta^{*}$ exactly?

### How is $\alpha$ related to $\beta$?

Equations 1 and 2 feature the hyperparameter $\beta$, which trades off between predictability and explainability (i.e. compactness of $S$). But Algorithm 1 and Table 2 show $\alpha$ as a hyperparameter (i.e. learning rate), which is meant to do a similar trade-off. What is the relationship between these two hyperparameters? Can Table 2 be replicated to show the same results by tuning $\beta$ instead of $\alpha$?

On a related note, why is $\alpha$ described as a "threshold parameter" in Algorithm 1?

### Soundness
2

### Presentation
1

### Contribution
2
