# Provable Robustness of (Graph) Neural Networks Against Data Poisoning and Backdoors

- Decision: Reject
- Scores: 6, 6, 8, 6

## Abstract
Generalization of machine learning models can be severely compromised by data poisoning, where adversarial changes are applied to the training data. This vulnerability has led to interest in certifying (i.e., proving) that such changes up to a certain magnitude do not affect test predictions. We, for the \textit{first} time, certify Graph Neural Networks (GNNs) against poisoning attacks, including backdoors, targeting the node features of a given graph. Our certificates are white-box and based upon $(i)$ the \textit{neural tangent kernel}, which characterizes the training dynamics of sufficiently wide networks; and $(ii)$ a novel reformulation of the bilevel optimization problem describing poisoning as a mixed-integer linear program. Consequently, we leverage our framework to provide fundamental insights into the role of graph structure and its connectivity on the worst-case robustness behavior of convolution-based and PageRank-based GNNs. We note that our framework is more general and constitutes the \textit{first} approach to derive white-box poisoning certificates for NNs, which can be of independent interest beyond graph-related tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel framework, QPCert, for certifying the robustness of GNNs, against data poisoning and backdoor attacks. This work leverages the NTK for white-box certification and reformulates the poisoning problem as a MILP to provide formal guarantees for GNNs. The authors explore this certification's effectiveness across various GNN architectures and benchmark datasets, and also analyze the effect of graph structure on robustness, presenting insights for architectural choices in GNNs with robustness considerations.

### Strengths
The paper is generally well-organized and thorough, with sections on methodological background, detailed steps in QPCert’s derivation, and clear experimental results. Extensive experiments are conducted across multiple GNN architectures and datasets. The analysis includes diverse attack scenarios and perturbation models, highlighting the framework’s adaptability and utility.

### Weaknesses
Although the focus is on feature perturbations, robustness against graph structure modifications is a critical issue for GNNs. Future work on structural robustness would greatly enhance the scope and impact of this framework.

On the assumption on large Width: The reliance on the NTK’s emight limit applicability to smaller, practical network sizes.

Given the MILP reformulation, computational costs may scale poorly with large datasets,

### Questions
No questions

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a white-box certification framework, QPCert, for evaluating the robustness of neural networks, specifically Graph Neural Networks (GNNs), against data poisoning and backdoor attacks. This framework, grounded in Neural Tangent Kernel (NTK) theory, reformulates poisoning detection as a mixed-integer linear program (MILP), enabling robustness certificates against node feature perturbations in GNNs. Thexperimental results to validate QPCert's effectiveness.

### Strengths
1. This paper studies an interesting problem: the certified robustness against data poisoning and backdoor attacks.
2. The extensive theoretical analysis is provided.
3. The paper is well written.

### Weaknesses
1. While the theoretical analysis is promising, the empirical evaluation could be strengthened to more comprehensively demonstrate the effectiveness of the proposed certification method. Currently, only one attack, APGD [1], is considered in the experiments. Since certification methods aim to provide provable guarantees against all attacks within a specific threat model, it would be beneficial for the authors to clarify how their certification framework addresses the threat models of other commonly studied attacks, such as graph poisoning and backdoor attacks [2, 3, 4]. Specifically, the evaluation should include a broader range of attacks, including those that manipulate graph structure or node features in more complex ways, to better assess the practical robustness of the proposed method. This would provide a more insightful discussion of the method’s robustness and scope of applicability, beyond specific attack evaluations.
2. It appears that the Neural Tangent Kernel (NTK) approach is currently limited to specific GNN architectures such as GCN, SGC, and GraphSage, which could restrict the broader applicability of the proposed method. It would be helpful if the authors could discuss any challenges or limitations in extending their method to other GNN architectures, such as those employing attention mechanisms or more complex aggregation functions, or clarify why these specific GNNs were chosen as representative examples. Additionally, outlining potential directions for adapting the approach to other types of GNNs, including those with non-linear output layers or batch normalization, could strengthen the paper's discussion and broaden its scope.
3. The proposed method addresses node feature perturbation attacks, yet structural perturbations are often more prevalent and impactful in real-world scenarios. It would strengthen the paper if the authors could discuss the challenges in adapting their method to structural perturbations, such as edge additions or removals, or clarify their focus on feature perturbations. Additionally, a comparison of the practical implications of feature versus structural perturbations in real-world applications, including a discussion of the relative ease of implementation and potential impact of each type of attack, would provide valuable insights into the method's scope, limitations, and potential future directions.

### Questions
1. Please add more experiments against some realistic graph poisoning and backdoor attacks.
2. Please discuss applying the proposed method to more advanced GNNs.
3. There are some works that study clean-label (graph) backdoor attacks [1, 2], can the proposed method be applied to this attack?

[1] Clean-Label Backdoor Attacks.

[2] A clean-label graph backdoor attack method in node classification task.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
I'm rating this paper as "8: accept, good paper".

Summary: the paper proposes a certification against white-box and backdoor attacks, by making use of Graph NTK and the fact that for sufficiently wide networks the network is throughly understood given the input data and the neural tangent kernel.

### Strengths
- Clear writing
- Elegant ideas to make the bi-level optimisation feasible and tracktable

### Weaknesses
-


### Questions
- In line 369 it is mentioned that: "... We note as we are the first work to study white-box certificates for clean-label attacks on node features in graphs in general, there is no baseline prior work. ...". Even if there are no baselines for white-box attacks, aren't the certificates for black-box baselines still applicable? Specially because these methods are different in, e.g., their relaxation which may differently affect their performance and one cannot presume superiority of certificate in black-box versus white-box setting?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors leverage the Neural Tangent Kernel (NTK) to capture the complex training dynamics of GNNs and reformulate the bilevel optimization problem describing poisoning as a mixed-integer linear program. This allows them to provide white-box certificates for GNNs and neural networks in general, which was previously an unsolved problem.

### Strengths
- Provide a comprehensive theoretical analysis to support the methodology 
- Very inspiring to leverage NTK to defend the adversarial and backdoor attacks
- Reformulated the bilevel optimization problem describing poisoning as a mixed-integer linear program

### Weaknesses
 - this paper only considers the scenario where the adversaries manipulate the node features, but there are plenty of graph attack works that manipulate the graph structure and the node features at the same time. Could the method in this paper be leveraged for poisoned data with both graph structures and node features manipulated?
- The experiments only compare the GNNs with MLP. Could authors provide some adversarial/backdoor defense baselines? While the comparison with MLPs demonstrates the positive impact of QPCert, it does not adequately illustrate the extent of QPCert's effectiveness.
- In Figure 2, MLP consistently has the lowest accuracy when evaluated in the PL task, but MLP can have a better performance than some GNNs in Figure 3 (PU and BU tasks) when perturbation budges are large. Could the author explain what factors lead to these differences?

### Questions
the same as weaknesses

### Soundness
3

### Presentation
3

### Contribution
4
