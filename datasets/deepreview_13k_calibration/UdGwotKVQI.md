# Certified Defense on the Fairness of Graph Neural Networks

- Decision: Reject
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
Graph Neural Networks (GNNs) have emerged as a prominent graph learning model in various graph-based tasks over the years. Nevertheless, due to the vulnerabilities of GNNs, it has been empirically proved that malicious attackers could easily corrupt the fairness level of their predictions by adding perturbations to the input graph data. In this paper, we take crucial steps to study a novel problem of certifiable defense on the fairness level of GNNs. Specifically, we propose a principled framework named ELEGANT and present a detailed theoretical certification analysis for the fairness of GNNs. ELEGANT takes {\em any} GNNs as its backbone, and the fairness level of such a backbone is theoretically impossible to be corrupted under certain perturbation budgets for attackers. Notably, ELEGANT does not have any assumption over the GNN structure or parameters, and does not require re-training the GNNs to realize certification. Hence it can serve as a plug-and-play framework for any optimized GNNs ready to be deployed. We verify the satisfactory effectiveness of ELEGANT in practice through extensive experiments on real-world datasets across different backbones of GNNs, where ELEGANT is also demonstrated to be beneficial for GNN debiasing.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This works aims to formulate the problem of certified defense on the fairness. To achieve this goal, the certified robustness analysis is applied to the certified fairness against input perturbations. More specifically, the analysis about certified fairness defense is conducted on node attributes and graph structures. Experiments are conducted on three real-world datasets.

### Strengths
1. This work focuses on an important problem of fairness on graph-structured data. Many real-world applications such as financial analysis and social network analysis requires the fairness to be guaranteed.
2. The authors propose a novel problem of certified fairness defense to avoid the attacks on the fairness. 
3. The analysis in certified fairness defense is solid. And surprisingly, the certified fairness method empirically improve the fairness.

### Weaknesses
Overall, the reviewer feel the strengths outweigh the weaknesses. However, several concerns would be highly suggested to be addressed.
1. The certified fairness defense is an application of certified robustness by changing the accuracy metric to the fairness metric in the analysis. This is quite straightforward. Hence, the contributions in theoretical analysis is somewhat limited.
2. For certified robustness methods, they improve the robustness because of the adversarial training stage of the trained model. For this proposed method, bias is decreased without explicit way to improve the fairness. It is highly suggested to conduct some further theoretical analysis for this interesting phenomenon. 
3. Experiments on large graphs with none-synthetic edges are suggested.

### Questions
Please refer to the weakness. 

In addition. for certified adversarial robustness methods, they generally are only applicable to the evasion attack, where the perturbations are only conducted on the test samples. For the proposed method, can it defend the poisoning attack?

### Soundness
3

### Presentation
3

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
This paper introduces ELEGANT, a framework for certifiable defense on the fairness of GNNs against adversarial perturbations in node attributes and graph topology. ELEGANT aims to serve as a plug-and-play module that can be applied to any optimized GNN model without altering the underlying structure or requiring retraining. The paper's contributions include a formal problem formulation, algorithmic design leveraging randomized smoothing, and extensive experiments to validate the approach across real-world datasets.

### Strengths
- The authors provide comprehensive experimental validation across multiple real-world datasets, demonstrating the generalizability and effectiveness of ELEGANT across different GNN architectures.
- The paper is well-written, with clear explanations of the methodology and experimental setup.

### Weaknesses
 - The setting, though well-defined theoretically, may lack practical applicability in real-world scenarios. The assumptions about the perturbation budgets and fairness certification requirements may not always align with practical needs, which could limit the framework’s deployment in real-life applications. The practical feasibility of maintaining certified fairness under realistic conditions could be further substantiated.
- The Monte Carlo estimation and probabilistic guarantee calculation introduce added complexity to the certification process. While theoretically sound, this approach could pose challenges in implementation, especially in large-scale networks. Further simplification or performance analysis would strengthen the practical value of the proposed solution.

### Questions
Please refer to the weakness.

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
4

### Summary
This paper proposes a fairness certification framework for Graph Neural Networks (GNNs) based on randomized smoothing. The corresponding framework, ELEGANT, provides a certain level of fairness guarantee for node classification under certain perturbation budgets.

### Strengths
- Paper is well-written and fluent.

- The considered research problem is a novel and important one.

- The paper provides theoretical guarantees for fairness certification.

### Weaknesses
 - The analysis in this paper is developed on existing randomized smoothing works, where certified evaluation has already been studied for both discrete and continuous data. This paper combines such works and reframes the problem from fairness aspect, which I believe limits its novelty in terms of analysis strategy.

- As also explained in the paper, fairness improvements observed in the Experimental Results and Conclusions are probably just a by-product of the applied noise, thus there is not of sufficient contribution from the bias mitigation aspect. 

- The proposed scheme cannot be directly used with fairness metrics that require ground-truth labels. However, the Authors claim that "Here bias is measured with $\Delta_{SP}$ and we have similar observations on $\Delta_{EO}$" without explaining how they used ELEGANT for the certification of $\Delta_{EO}$ (this metric requires ground-truth label information). Also, throughout the paper they never mention this limitation.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a framework called ELEGANT, which is designed to guarantee GNNs to be fair, even if they’re under attack within certain limits of budgets. What’s appealing about this framework ELEGANT is that it works with any GNN model as a plug-and-play method, meaning it doesn’t require re-training or making assumptions about the structure of the GNNs. This kind of flexibility and ease of use might make it a valuable tool, and it has the potential to inspire others in the field to build on its ideas.

### Strengths
(1) The theoretical analysis is laid out in a detailed and step-by-step manner, walking through the certification on node attributes and graphs with rigor. This could be helpful for readers trying to follow along. 

(2) Unlike most existing certification methods, which don’t address fairness in GNNs, this framework is specifically aimed at fairness issues. This should be considered a significant step for the field, where fairness is a major concern but often gets sidelined. 

(3) Since ELEGANT is a re-training-free, drop-in solution for GNNs, it could be easy for researchers to try it out and see the impact. Its flexibility and practicality make it stand out, and it might encourage more work along these lines. 

(4) The authors evaluated the proposed framework on a solid selection of datasets and GNN models. Their experiments are thorough and show strong evidence of the effectiveness of this proposed approach.

### Weaknesses
(1) The general theoretical results in A.9 could use a clearer introduction earlier in the paper, to make it easier for interested readers to gain details about the theorems.

(2) There’s a mention of constraints on node attributes and graph structure that are supposed to be “unnoticeable,” but it’s not clear why these are necessary. Specifically, the notion of 'unnoticeable' needs to be rigorously defined in the context of graph perturbations. What constitutes an unnoticeable change in node attributes or graph structure? Is it based on a specific distance metric, or a perceptual threshold? Without a clear definition, it's difficult to assess the practical implications of these constraints.

(3) Are there any assumptions about the types of graphs that the framework applies to? For instance, does it matter if they’re directed or undirected, or weighted or unweighted? Furthermore, how does the framework handle graphs with heterogeneous node and edge features, or dynamic graphs that evolve over time? The current discussion seems to assume a relatively simple graph structure, and it's unclear how well the approach would generalize to more complex scenarios.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
