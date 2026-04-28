# Implicit Neural Network on Dynamic Graphs

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
Recent works have demonstrated that graph convolution neural networks fail either to capture long-range dependencies in the network or suffer from over-smoothing issues. Several recent works have proposed implicit graph neural networks to remedy the issues. However, despite these issues being magnified in dynamic graphs, where the feature aggregation occurs through both the graph neighborhood and across time stamps, no prior work has developed implicit models to overcome these issues. Here we present IDGNN, a novel implicit neural network for dynamic graphs. We demonstrate that IDGNN is well-posed, i.e., it has a unique fixed-point solution. However, the standard iterative algorithm often used to train implicit models is computationally expensive in our setting and cannot be used to train IDGNN efficiently. To overcome this, we pose an equivalent bi-level optimization problem and propose a single-loop training algorithm. We conduct extensive experiments on real-world datasets on both classification and regression tasks to demonstrate the superiority of our approach over the state-of-the-art baseline approaches. We also demonstrate that our bi-level optimization framework maintains the performance of the standard iterative algorithm while obtaining up to 1600x speed-up.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents IDGNN, an Implicit Neural Network for Dynamic Graphs, aimed at overcoming the limitations of graph convolution neural networks (GCNs), such as over-smoothing and the failure to capture long-range dependencies, especially in dynamic settings. The authors introduce a novel bilevel optimization framework for training IDGNN, which shows superior performance on real-world datasets in both classification and regression tasks compared to state-of-the-art approaches. They also demonstrate a significant speed-up in training times without compromising performance.

### Strengths
1. IDGNN is the first method to tackle the dynamic graph problem via an implicit neural network, filling a gap in the literature.
2. The model outperforms state-of-the-art methods on various real-world datasets, and the authors provide experimental validation.

### Weaknesses
1. The discussion about IGNN being able to avoid over-smoothing seems heuristic. IGNN ensures that the representation of the network is convergent, but it does not prevent over-smoothing problems. The claim that implicit networks inherently avoid over-smoothing requires more rigorous justification, as convergence alone does not guarantee the preservation of distinct node representations. Specifically, the paper lacks a theoretical analysis demonstrating how the implicit formulation prevents node embeddings from becoming indistinguishable, a common symptom of over-smoothing.

2. The reasonableness of the assumption in Lemma 2 needs further explanation. For example, it says that Formula 3 has a unique embedding z, but which z in Formula 3 is referred to and under which conditions it is unique. The statement that a unique embedding z exists for Formula 3 is not sufficiently precise. It's unclear whether this uniqueness is guaranteed for any arbitrary initialization or only under specific conditions. The paper should explicitly state the conditions under which the fixed-point iteration in Equation 3 converges to a unique solution, and whether these conditions are always met during training.

3. In Lemma 2, ``let W_{j+k} denote M_{i}``. needs further explanation. The notation  ``let W_{j+k} denote M_{i}`` is confusing and requires clarification. It is not clear how the indices j, k, and i relate to each other, and how this mapping is defined when j+k exceeds the number of available matrices. The paper needs to provide a clear and unambiguous definition of how the matrices M_i are indexed and used in the context of Lemma 2.

4. Due to the question regarding Lemma 2, I am unable to determine the reasonableness of bilevel problem (8). (8) utilizes multi-block bilevel optimization for solving, and when solving (8), the paper makes extensive use of approximations without explaining their validity or drawbacks. The approximations used in solving the bilevel problem (8) lack sufficient justification. The paper does not provide a detailed analysis of the errors introduced by these approximations, nor does it discuss the potential impact on the convergence and optimality of the solution. Furthermore, the comparison with existing training methods is unclear, making it difficult to assess the advantages and disadvantages of the proposed approach. The paper needs to provide a more rigorous analysis of the approximation techniques and their implications.

5. Lack of experimental results on common datasets, such as QM9 and TUdataset.

### Questions
See weakness

### Soundness
2 fair

### Presentation
1 poor

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
The paper addresses the limitations of graph convolution neural networks (GCNs) in capturing long-range dependencies and oversmoothing issues in dynamic graphs.

The authors propose IDGNN, a novel implicit neural network for dynamic graphs, which overcomes these issues and has a unique fixed point solution.

To efficiently train IDGNN, the authors pose an equivalent bi-level optimization problem and propose a single-loop training algorithm, achieving up to 1600x speed-up compared to the standard iterative algorithm.

Extensive experiments on real-world datasets demonstrate the superiority of IDGNN over state-of-the-art baseline approaches in both classification and regression tasks. 

The paper also discusses the challenges in training implicit models and introduces an efficient bilevel optimization algorithm to overcome these challenges, resulting in improved computational efficiency during training. 

The contributions of the paper include proving the existence of fixed-point representations in dynamic graphs, designing an implicit model for general dynamic graphs, and developing an efficient training algorithm for IDGNN.

### Strengths
Originality:

The paper introduces IDGNN, a novel implicit neural network for dynamic graphs, which addresses the limitations of existing graph convolution neural networks (GCNs) in capturing long-range dependencies and oversmoothing issues.
The authors propose a bi-level optimization framework and a single-loop training algorithm to efficiently train IDGNN, which is a novel approach in the context of dynamic graphs.

Quality:

The paper provides a rigorous analysis of the proposed IDGNN model, demonstrating its well-posedness and unique fixed point solution.
Extensive experiments on real-world datasets are conducted to evaluate the performance of IDGNN, comparing it to state-of-the-art baseline approaches.

Clarity:

The paper clearly presents the motivation, challenges, and contributions of the research.
The authors provide detailed derivations and explanations in the Appendix to support their claims and ensure clarity. 

Significance:

The proposed IDGNN model and the efficient training algorithm have the potential to significantly improve the performance of dynamic graph neural networks, addressing the limitations of existing approaches. 

The experimental results demonstrate the superiority of IDGNN over state-of-the-art baseline approaches in both classification and regression tasks, highlighting its practical significance.

### Weaknesses
The paper lacks a comprehensive discussion on the limitations of the proposed IDGNN model and the potential challenges in its practical implementation.

The experimental evaluation could be further strengthened by including more diverse and challenging datasets, as well as comparing the performance of IDGNN with a wider range of state-of-the-art approaches.

The paper could benefit from providing more insights into the interpretability of the IDGNN model and how it captures the underlying dynamics of the dynamic graphs.

The clarity of the paper could be improved by providing more intuitive explanations and visualizations of the proposed model and its training algorithm.

The paper could provide more details on the computational complexity and scalability of the proposed single-loop training algorithm, particularly in large-scale dynamic graph scenarios.

### Questions
Can the authors provide more insights into the limitations of the IDGNN model and potential challenges in its practical implementation?

Could the authors consider including more diverse and challenging datasets in the experimental evaluation to further validate the performance of IDGNN?

It would be helpful if the authors could provide more details on the interpretability of the IDGNN model and how it captures the underlying dynamics of the dynamic graphs. 

Can the authors clarify the computational complexity and scalability of the proposed single-loop training algorithm, particularly in large-scale dynamic graph scenarios?

Could the authors provide more intuitive explanations and visualizations of the proposed IDGNN model and its training algorithm to enhance the clarity of the paper? 

It would be beneficial if the authors could discuss the potential applications and real-world use cases where IDGNN can be applied to address specific problems.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on graph learning for dynamic graphs. As the oversmoothing issues and the failure to capture long-range dependencies are more severe on dynamic graphs, the authors propose an implicit graph neural network model to mitigate the issues. To remedy the computationally expensive training issue, they propose a single-loop training algorithm by changing the original optimization problem to a bi-level optimization problem. The experimental results on both classification and regression tasks show the superiority of the proposed model in terms of both performance and efficiency.

### Strengths
1. The idea of using implicit GNNs for dynamic graphs is sound and the motivation to mitigate the dilemma between capturing long-range dependencies and suffering from oversmoothing problems is reasonable and interesting. 
2. The construction of the new equation for dynamic graphs in Eq (4) is good and the related theorems are sound. 
3. The performance of synthetic experiments directly supports the claim that the proposed method can avoid over-smoothing and still be effective in capturing long-range dependencies.

### Weaknesses
1. To me, the relation between Lemma 2 and the relationship between Lemma 2 and Eq (8) is not very clear. In Lemma 2, how does $M_i$ get involved in the formula about $z_j$. Additionally, Eq (8) suggests that the new constraint is only about the last timestamp. In this case, is it necessary to have Lemma 2 to arrive at Eq (8)? Why cannot directly iterate Eq (5) to have $\phi(z, W, V; G_i)$. I would like to see more explanations regarding these. 
2. The literature review may not be sufficient. As the paper focuses on implicit GNNs, I think the author may want to introduce and briefly discuss a few more recent implicit GNN works (e.g., CGS [1], EIGNN [2], USP [3]). Especially, USP seems to have a similar bilevel optimization problem, though it focuses on static graphs. 
3. The descriptions for the experiments are not very clear. As mentioned in Table 3, the memory usage and the runtime are reported as per batch. But how batches are formed for a single graph? Randomly select some nodes or use some sampling methods (e.g., neighbor sampling)?

### Questions
1. Although the convergence guarantee is a good thing to see, I am just curious whether this is necessary to make the implicit graph model work well. Based on my understanding, existing implicit GNNs all have this property. In contrast, implicit models in other areas seem not always have this theoretical guarantee (e.g., DEQ [1] and MDEQ). They empirically work well. 
2. Could you explain more about Hassian-vector Product as mentioned in the last paragraph of Sec 4? Can it be directly handled by a modern autodiff package? At least provide some reference materials in the appendix. 

Minor ones:
1. There is no Table 3 caption. Please fix it. 


References

[1] Deep Equilibrium Models. Shaojie Bai, J. Zico Kolter and Vladlen Koltun (NeurIPS 2019)

[2] Multiscale Deep Equilibrium Models. Shaojie Bai, Vladlen Koltun and J. Zico Kolter (NeurIPS 2020)

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new graph generative model for dynamic graphs based on implicit neural networks. The proposed method generalizes IGNN to the dynamic graphs, extending its capability to solve a broader range of problems. The well-posedness property has been shown for the proposed model. A bi-level optimization algorithm is developed for an efficient training of the proposed model. With the new training algorithm, the proposed model shows better performances on graph classification and regression tasks than baseline models.

### Strengths
- This is the first implicit model for dynamic graphs. The experimental results show that the implicit model for dynamic graphs can show better performances than non-implicit models.
- The proposed bi-level optimization algorithm can reduce the training time while having a competitive performance with the naive gradient descent algorithm.

### Weaknesses
 - The paper proposes an implicit model for discrete-time *cyclic* dynamic graphs. I assume that the cyclic property is added to obtain the implicit representation of graphs, but the datasets used in the experiments do not have the cyclic property.
    - Moreover, I doubt that the performance of the synthetic experiments comes from the implicit representation. Since the representation at time step $T$ is directly related to the representation at time step $1$, through the learning (back-propagation) process, the model can directly utilize the information at time step $1$ to infer the class label at time step $T$. Hence, it is unclear whether the long-range dependency is captured correctly or not. This is particularly concerning because the model's architecture seems to allow for direct information propagation from the initial time step to the final one, potentially bypassing the need to learn meaningful temporal dynamics. The experiments should include a more thorough analysis of the model's ability to capture long-range dependencies, perhaps by varying the temporal distance between relevant information and the prediction target.
- The main theorem seems a direct consequence of Gu et al. (2020).
- The claimed 1600x speed-up seems like an overstatement. Although the proposed algorithm achieves a 1600x speed-up for the Brain10 dataset, the improvement is much lower for the other datasets. Having said that, I found that the improvement from the other datasets is not insignificant (10x improvement is also great).
    - Moreover, it would be much more meaningful if there were any analysis on why the algorithm performs well on the Brain10 dataset. What characteristics of the dataset lead to such an impressive performance increase? The paper should provide a more detailed analysis of the computational complexity of both the proposed bi-level optimization and the naive gradient descent, specifically highlighting the factors that contribute to the observed speed-ups on different datasets. It would also be beneficial to explore the scalability of the proposed method with respect to the number of nodes and time steps.
- The representation of the manuscript can be improved further. Several notations are confusing, and a few terms are explained without having proper definitions. Here, I list some of them.
    - The notation $t$ is used for the depth of a layer and the time stamp of a graph (e.g., the first paragraphs of section 3). Although one may infer which t corresponds to which (based on location - superscript for layer and subscript for timestamp), it is difficult to follow the manuscript.
    - Transpose is denoted with superscript $T$, which is confusing with the timestamp T. Using \top latex command can alleviate the confusion.
    - Omega is not defined (Page 3, third line). I guess it means V
    - \ell in the equation on page 6 (where \nabla L(\omega) is defined) is not defined. So, I couldn’t follow the details after equation 8.
    - Please add references for datasets.
    - Use proper command for the citations. Use latex commands \citet and \citep for this.
    - Typo in the first sentence on Page 3 (l and d are both used to denote the dimension of the node attributes).
    - Typo in the matrix in Theorem 1 (the right-most column needs to be removed)

### Questions
- Why V in equation 2 is shared across time, and W is not?
- What makes the optimization ‘bi-level’? It would be better to have some additional background on the bi-level optimization methods.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
