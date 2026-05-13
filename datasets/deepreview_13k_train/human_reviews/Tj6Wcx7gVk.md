# Probabilistically Rewired Message-Passing Neural Networks

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Message-passing graph neural networks (MPNNs) emerged as powerful tools for processing graph-structured input. However, they operate on a fixed input graph structure, ignoring potential noise and missing information. Furthermore, their local aggregation mechanism can lead to problems such as over-squashing and limited expressive power in capturing relevant graph structures. Existing solutions to these challenges have primarily relied on heuristic methods, often disregarding the underlying data distribution. Hence, devising principled approaches for learning to infer graph structures relevant to the given prediction task remains an open challenge. In this work, leveraging recent progress in exact and differentiable $k$-subset sampling, we devise probabilistically rewired MPNNs (PR-MPNNs), which learn to add relevant edges while omitting less beneficial ones. For the first time, our theoretical analysis explores how PR-MPNNs enhance expressive power, and we identify precise conditions under which they outperform purely randomized approaches. Empirically, we demonstrate that our approach effectively mitigates issues like over-squashing and under-reaching. In addition, on established real-world datasets, our method exhibits competitive or superior predictive performance compared to traditional MPNN models and recent graph transformer architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper has proposed a probabilistic rewiring methanism for GNN. Its improvement in expressive power has been verified with theory and experiments.

### Strengths
1. The method has been verified with both theory and experiments.

### Weaknesses
1. The computation overhead is also needed.
2. How does the expressiveness guarantee translate to practical performances?

### Questions
I wonder what is the performance gain over the overhead the method produces.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a probabilistic rewired message-passing network (PR-MPNN) to address the under-reaching and over-squashing problems of existing graph neural network (GNN) models. Specifically, PR-MPNN first uses a GNN to learn the priors over edges, and then it samples multiple adjacency matrices from the edge prior distributions using SIMPLE, a gradient estimator for k-subset sampling. The sampled adjacency matrices are combined with the original adjacency matrix to obtain the rewired graph, which is used in the downstream tasks. The paper also provides theoretical analysis to identify conditions under which the proposed method can outperform randomized approaches.

### Strengths
1. The proposed PR-MPNN model is simple yet effective. 
2. The paper provides theoretical analyses to prove that the proposed model is more effective in probabilistically separating graphs than randomized approaches such as dropping nodes and edges uniformly under certain conditions. 
3. Experimental results on both node classification and graph classification tasks indicate that PR-MPNN can achieve better or competitive performance compared with baselines.

### Weaknesses
1. The motivation for using $k$-subset constraint when sampling the adjacency matrix is not very clear. What are the advantages of using such constraints? Specifically, why is a $k$-subset constraint preferred over simply sampling edges independently with a learned probability? The paper should elaborate on the specific benefits of this approach in terms of the expressiveness and learning dynamics of the model.

2. The difference between the proposed PR-MPNN and previous works is not explicitly discussed in the related work section. The paper needs to clearly distinguish its approach from existing graph rewiring methods, especially those that also learn edge probabilities or use sampling techniques. A more detailed comparison with methods that use similar concepts, such as graph structure learning, would be beneficial.

3. The theoretical results indicate that PR-MPNN  is more effective in probabilistically separating graphs than randomized approaches under certain conditions. But how does this help PR-MPNN address the over-squashing problem? The paper should provide a more explicit connection between the theoretical analysis and the practical problem of over-squashing. It is not clear how probabilistically separating graphs directly translates to mitigating information loss due to over-squashing.

4. In the introduction section, the paper states that PR-MPNNs make MPNNs less vulnerable to potential noise and missing information. However, there are no empirical or theoretical results to validate such statements. The paper should provide evidence to support this claim, either through experiments that simulate noisy or incomplete graphs, or through theoretical analysis that demonstrates the robustness of PR-MPNNs to such perturbations.

5. PR-MPNN use SIMPLE to sample adjacency matrices. It seems to be an important component of the proposed model and the paper should provide an introduction to the SIMPLE method to make the paper self-contained. The paper should include a brief explanation of how SIMPLE works and why it is suitable for this task. This would make the paper more accessible to readers unfamiliar with this specific gradient estimator.

6. I also have some concerns regarding the experiments:

(1) In the “Baseline and model configurations” paragraph, the paper states that there are two ways to leverage the sampled adjacency matrices when using multiple priors. However, it is unclear which method is used in their experiments. The paper should explicitly state which method was used in the experiments and justify this choice.

(2) When answering Q2, why compare PR-MPNN with different baselines on different datasets? For example, the paper compares PR-MPNN with OSAN, GIN+POSENC, DropGNN on EXP, CSL and 4-CYCLES datasets respectively. Also, the statement “Concerning Q2, on the 4-CYCLES dataset, our probabilistic rewiring method consistently outperforms DropGNN” is inaccurate since PR-MPNN only achieve comparable performance with DropGNN in some cases. The paper should provide a consistent set of baselines across all datasets to ensure a fair comparison. The claims about the performance on the 4-CYCLES dataset should be revised to accurately reflect the experimental results.

(3) The results in Table 1 are quite confusing. What evaluation metric is used in these results? Why is it that on some datasets, such as OGBG-MOLHIV, a higher metric indicates better performance, while on others, such as ZINC and ALCHEMY,  a lower value is preferable? The paper should clearly state the evaluation metric for each dataset and explain why different metrics are used for different tasks. This would improve the clarity and interpretability of the results.

(4) There are no ablation studies to validate the effectiveness of each component of the proposed model. The paper should include ablation studies to demonstrate the contribution of each component, such as the learned edge priors, the $k$-subset sampling, and the SIMPLE gradient estimator. This would help to understand the importance of each part of the model.

7. In the conclusion section, the paper states that PR-MPNN “is competitive or superior to conventional  MPNN models and graph transformer architectures regarding predictive performance and computational efficiency”. However, there is no comparison between PR-MPNN and baselines regarding the computational efficiency in the main text. The paper should provide a detailed comparison of the computational cost of PR-MPNN with other models, including both training and inference time, to support the claim about computational efficiency.

### Questions
Please see the questions in the Weaknesses section.

### Soundness
3 good

### Presentation
2 fair

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
The work proposes a probabilistic rewiring technique that relies on differentiable k-subset sampling. The main motivation is that while current rewiring techniques rely on "arbitrary" heuristics (improving spectral gap, connecting nodes in the 2-hop), it would be ideal to *learn* such a rewiring. Further, the work proposes a way to study the expressive power -- in terms of WL -- for such a process. The work is evaluated on synthetic and real-world benchmarks.

### Strengths
The work is well-written and overall I found it interesting. I agree that learning a rewiring is intuitively something that should be preferred over arbitrary heuristics. I also appreciated that the work discusses techniques such as the Differentiable Graph Module, which in principle may seem similar.

### Weaknesses
(W1) I believe experimentally there could be a larger breadth of rewiring benchmarks, for instance comparing against "deterministic" rewiring techniques such as FOSR [1] and SDRF [2] would be valuable. Furthermore, adding a "random rewiring" GNN, i.e. DropGNN, would also be useful for the real-world tasks. 

(W2) The claim that the rewiring technique reduces over-squashing could be strengthened. At the moment this seems to be solely motivated by the empirical results in Figure 2 and Figure 4. It is not clear that edge removal alone can address over-squashing, as it might simply reduce information flow rather than alleviate bottlenecks. A more detailed analysis, potentially examining the impact on path lengths or effective resistance, would be beneficial to support this claim.

### Questions
(Q1) From Figure 1 and the paper overall, it seems like the rewiring technique is only removing edges and not adding any new edges not present in the original graph. Is this the case? 

(Q2) Regarding (W1), would it be possible to show results for existing deterministic rewiring techniques?

(Q3) Regarding (W2) and especially (Q1), it is not clear to me how the technique can reduce over-squashing if it is only able to remove edges. It would be important to clarify (Q1), and provide some theoretical evidence that it is indeed able to alleviate over-squashing. In general by removing edges, one is reducing the total effective resistance over the graph.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
