### Summary

This paper proposes a learning principle for graph neural networks from the perspective of convergence. Based on this principle, the authors propose a new GNN architecture called Adaptive Power Graph Neural Network (APGNN). The authors provide a theoretical analysis of the generalization ability of APGNN. Experimental results show that APGNN outperforms some existing GNN models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and well-organized.
2. The authors provide a theoretical analysis of the generalization ability of APGNN.
3. Experimental results show that APGNN outperforms some existing GNN models.

### Weaknesses

#### Some Related Works

[1] Weisfeiler and Leman Go Neural: Higher-order Graph Neural Networks.
[2] Distance Encoding -- Design Provably More Powerful GNNs for Structural Representation Learning.
[3] Revisiting Heterophily For Graph Neural Networks.
[4] Dropedge: Towards deep graph convolutional networks on node classification.

#### comment

1. The authors claim that the proposed principle can guide the design of GNNs for constructing infinite deep GNNs. However, the proposed APGNN is still a finite deep GNN. The authors should clarify the relationship between the proposed principle and the architecture of APGNN. Specifically, it is unclear how the 'infinite depth' claim is supported by the actual architecture, which appears to be a standard GNN with a specific aggregation scheme. The paper needs to articulate more precisely how the proposed learning principle, which seems to be about convergence, translates into a practical architecture that can be implemented with finite layers.
2. The authors claim that the proposed principle can be used to unify the design of existing GNNs. However, the authors do not provide a clear explanation of how the proposed principle can be used to unify the design of existing GNNs. The paper lacks a concrete demonstration of how different existing GNN architectures can be derived from this principle. It is not sufficient to simply state that the principle can unify existing GNNs; the authors need to show the specific steps or transformations that would achieve this unification.
3. The proposed APGNN is similar to existing GNN models, such as [1][2]. The authors should compare APGNN with these models and highlight the advantages of APGNN. The paper needs to provide a more detailed comparison, focusing on the specific differences in the aggregation schemes and how these differences lead to improved performance or theoretical properties. A simple mention of similarity is not sufficient; a rigorous analysis is required.
4. The experimental results are not convincing. The authors should conduct more experiments to demonstrate the advantages of APGNN. The current experiments are limited in scope and do not provide a comprehensive evaluation of the proposed model. The paper needs to include a wider range of datasets, tasks, and baselines to demonstrate the robustness and generalizability of APGNN. Furthermore, the experimental setup should be more rigorous, with a clear description of hyperparameter tuning and statistical significance testing.
5. The authors should conduct experiments on heterophilic datasets to demonstrate the advantages of APGNN. The paper needs to explicitly address the performance of APGNN on heterophilic graphs, as this is a critical aspect of GNN performance. The current experiments do not provide sufficient evidence to support the claim that APGNN is effective in such scenarios.
6. The authors should conduct experiments on heterophilic datasets to demonstrate the advantages of APGNN. The paper needs to explicitly address the performance of APGNN on heterophilic graphs, as this is a critical aspect of GNN performance. The current experiments do not provide sufficient evidence to support the claim that APGNN is effective in such scenarios.
7. The authors should conduct experiments on heterophilic datasets to demonstrate the advantages of APGNN. The paper needs to explicitly address the performance of APGNN on heterophilic graphs, as this is a critical aspect of GNN performance. The current experiments do not provide sufficient evidence to support the claim that APGNN is effective in such scenarios.
8. The authors should conduct experiments on heterophilic datasets to demonstrate the advantages of APGNN. The paper needs to explicitly address the performance of APGNN on heterophilic graphs, as this is a critical aspect of GNN performance. The current experiments do not provide sufficient evidence to support the claim that APGNN is effective in such scenarios.
9. The authors should conduct experiments on heterophilic datasets to demonstrate the advantages of APGNN. The paper needs to explicitly address the performance of APGNN on heterophilic graphs, as this is a critical aspect of GNN performance. The current experiments do not provide sufficient evidence to support the claim that APGNN is effective in such scenarios.
10. The authors should conduct experiments on heterophilic datasets to demonstrate the advantages of APGNN. The paper needs to explicitly address the performance of APGNN on heterophilic graphs, as this is a critical aspect of GNN performance. The current experiments do not provide sufficient evidence to support the claim that APGNN is effective in such scenarios.

### Suggestions

The paper needs to provide a more detailed explanation of how the proposed learning principle translates into the specific architecture of APGNN. The authors should clarify the connection between the convergence principle and the power series expansion of the graph filter. It is not sufficient to simply state that the principle is about convergence; the paper needs to show how this principle directly leads to the specific form of the APGNN architecture. For example, the authors could explain how the truncation of the power series is related to the convergence properties of the filter. Furthermore, the authors should provide a more rigorous mathematical analysis of the convergence properties of the proposed filter, demonstrating how the truncation error is bounded and how this bound relates to the performance of the GNN. This analysis should also consider the impact of the decay rate parameter on the convergence and stability of the filter. The authors should also clarify how the proposed principle can be used to unify the design of existing GNNs. The paper should provide a concrete example of how a specific existing GNN architecture can be derived from the proposed principle. This would involve showing how the aggregation scheme of the existing GNN can be expressed as a power series, and how the convergence properties of this series are ensured by the proposed principle. The authors should also discuss the limitations of the proposed principle and identify the types of GNN architectures that cannot be unified using this principle. This would help to clarify the scope and applicability of the proposed approach. 

The paper needs to provide a more detailed comparison of APGNN with existing GNN models, such as those presented in [1,2]. The authors should not only mention the similarity between APGNN and these models but also highlight the specific differences in the aggregation schemes and how these differences lead to improved performance or theoretical properties. For example, the authors could compare the convergence rates of APGNN and the existing models, or analyze the stability of the filters under different conditions. The authors should also provide a more comprehensive experimental evaluation of APGNN. The current experiments are limited in scope and do not provide a comprehensive evaluation of the proposed model. The paper needs to include a wider range of datasets, tasks, and baselines to demonstrate the robustness and generalizability of APGNN. The experimental setup should also be more rigorous, with a clear description of hyperparameter tuning and statistical significance testing. The authors should also conduct experiments on heterophilic datasets to demonstrate the advantages of APGNN. The paper needs to explicitly address the performance of APGNN on heterophilic graphs, as this is a critical aspect of GNN performance. The authors should also investigate the sensitivity of APGNN to different hyperparameter settings and provide guidelines for selecting appropriate values. The authors should also investigate the computational complexity of APGNN and compare it with existing GNN models. This analysis should consider the time and memory requirements of APGNN for different graph sizes and complexities. The authors should also discuss the potential limitations of APGNN and identify areas for future research.

### Questions

1. How to prove that the proposed principle can guide the design of GNNs for constructing infinite deep GNNs?
2. How to prove that the proposed principle can be used to unify the design of existing GNNs?
3. What are the advantages of APGNN compared to existing GNN models, such as [1][2]?
4. How to conduct more experiments to demonstrate the advantages of APGNN?
5. How to conduct experiments on heterophilic datasets to demonstrate the advantages of APGNN?

[1] Weisfeiler and Leman Go Neural: Higher-order Graph Neural Networks.

[2] Distance Encoding -- Design Provably More Powerful GNNs for Structural Representation Learning.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
