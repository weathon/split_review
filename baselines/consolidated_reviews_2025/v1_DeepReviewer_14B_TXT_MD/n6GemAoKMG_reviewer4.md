### Summary

This paper introduces a novel evolutionary-based algorithm for performing attacks on graph neural networks. The proposed approach directly addresses the discrete nature of graph perturbations, avoiding the relaxation of the adjacency matrix used in gradient-based methods. The method is model-agnostic and can be applied to any black-box model, broadening its applicability. The paper also introduces two new attack objectives that target robustness certificates and conformal prediction sets, expanding the scope of adversarial attacks on graphs. The experimental results demonstrate that the proposed method outperforms existing state-of-the-art attacks, achieving an additional ~11% reduction in accuracy on average. The paper's contributions include a new attack method, novel attack objectives, and a demonstration of its effectiveness, highlighting the potential for further research in this area.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel evolutionary-based algorithm for performing attacks on graph neural networks, which is a significant contribution to the field of adversarial machine learning.
2. The proposed approach directly addresses the discrete nature of graph perturbations, avoiding the relaxation of the adjacency matrix used in gradient-based methods.
3. The method is model-agnostic and can be applied to any black-box model, broadening its applicability.
4. The paper introduces two new attack objectives that target robustness certificates and conformal prediction sets, expanding the scope of adversarial attacks on graphs.
5. The experimental results demonstrate that the proposed method outperforms existing state-of-the-art attacks, achieving an additional ~11% reduction in accuracy on average.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the adversary has full knowledge of the graph structure and node labels. This assumption may not always hold in real-world scenarios, potentially limiting the practical applicability of the attack.
2. The method relies on multiple forward passes through the model, which can be unrealistic in some attack scenarios due to query limitations or computational costs.
3. While the paper demonstrates the effectiveness of EvA, it does not extensively explore potential defenses against these evolutionary attacks.

### Suggestions

The paper's reliance on full knowledge of the graph structure and node labels is a significant limitation that needs to be addressed. In many real-world scenarios, an attacker might only have access to a partial or noisy version of the graph. The authors should explore the robustness of their method under such conditions. For example, they could investigate how the attack performance degrades when a certain percentage of edges or node features are randomly removed or perturbed. Furthermore, it would be beneficial to analyze the sensitivity of the attack to different types of graph perturbations, such as adding or removing edges, or modifying node attributes. This analysis would provide a more comprehensive understanding of the attack's limitations and its applicability in practical settings. The authors could also consider incorporating techniques to handle incomplete or noisy graph information, such as using graph reconstruction methods or robust optimization techniques.

The computational cost of the proposed method, due to multiple forward passes, is another area that requires further investigation. While the paper mentions that the method is model-agnostic, the practical feasibility of applying it to large-scale graphs or complex models is questionable. The authors should provide a detailed analysis of the computational complexity of their approach and compare it with existing black-box attack methods. It would be helpful to explore techniques to reduce the number of forward passes required, such as using more efficient search strategies or approximating the model's behavior. Additionally, the authors should consider the impact of query limitations on the attack performance. In some scenarios, the attacker might only have a limited number of queries available, which could significantly affect the effectiveness of the attack. The authors should investigate how the attack performance varies with different query budgets and propose strategies to optimize the attack under such constraints.

Finally, the paper should explore potential defenses against the proposed evolutionary attack. While the authors mention that they leave this for future work, it is crucial to understand the potential vulnerabilities of the proposed method and how they can be mitigated. The authors could investigate the effectiveness of existing defense mechanisms, such as adversarial training or graph regularization, against the proposed attack. Furthermore, they could explore the development of new defense strategies specifically tailored to counter evolutionary attacks. This would provide a more complete picture of the attack's impact and its potential for real-world applications. The authors should also consider the possibility of adaptive attacks, where the attacker iteratively refines the attack based on the model's defenses. This would provide a more realistic assessment of the attack's robustness and its potential for circumventing defenses.

### Questions

1. How does the performance of EvA degrade if the adversary has only partial knowledge of the graph structure or node labels?
2. Can the authors provide a more detailed analysis of the computational complexity of EvA compared to other black-box attack methods?
3. What are the potential defenses against EvA, and how effective are they in mitigating the attack?

### Rating

6

### Confidence

3

**********
