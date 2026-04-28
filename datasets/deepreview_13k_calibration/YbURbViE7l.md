# GOttack: Universal Adversarial Attacks on Graph Neural Networks via Graph Orbits Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Graph Neural Networks (GNNs) have demonstrated superior performance in node classification tasks across diverse applications. However, their vulnerability to adversarial attacks, where minor perturbations can mislead model predictions, poses significant challenges. This study introduces GOttack, a novel adversarial attack framework that exploits the topological structure of graphs to undermine the integrity of GNN predictions systematically. 

By defining a topology-aware method to manipulate graph orbits, our approach can generate adversarial modifications that are both subtle and effective, posing a severe test to the robustness of GNNs. We evaluate the efficacy of GOttack across multiple prominent GNN architectures using standard benchmark datasets. Our results show that GOttack outperforms existing state-of-the-art adversarial techniques and completes training in approximately 55% of the time required by the fastest competing model, achieving the highest average misclassification rate in 155 tasks. 
This work not only sheds light on the susceptibility of GNNs to structured adversarial attacks but also shows that certain topological patterns may play a significant role in the underlying robustness of the GNNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents GOttack, an adversarial attack framework targeting Graph Neural Networks (GNNs) through manipulation of graph orbits to maximize misclassification rates in node classification tasks. GOttack leverages topological properties, specifically graph orbits, to systematically alter graph structure with minimal changes, showing superior efficiency and effectiveness compared to other adversarial methods across multiple datasets and GNN architectures.

### Strengths
1. Provides comprehensive experimentation across various datasets, GNN models, and defense mechanisms, demonstrating GOttack’s robustness.
2. The idea of using graph orbits learning is interesting.
3. According to the presented results, the proposed method has better time efficiency than baselines.

### Weaknesses
1. It is unclear why existing methods, which rely on direct node feature manipulation or edge modifications, do not account for topological impact. Could the authors provide specific examples of how these approaches might implicitly consider topology and clarify what unique advantages GOttack offers by explicitly leveraging topology?

2. Orbit discovery is extremely time-consuming, which could limit the practical applicability of the method in real-world settings. Although the orbit discovery on graphlets is performed as a pre-processing step, it would be helpful for the authors to discuss scenarios where the graph structure updates dynamically. Additionally, considering large-scale graphs (e.g., OGB-arxiv) may require significant computational resources. Providing empirical runtime comparisons on such large-scale datasets and discussing potential strategies for dynamic graphs would strengthen the discussion on scalability.

3. The proposed method appears to rely heavily on specific orbit structures (e.g., orbits 15 and 18). Could the authors elaborate on the selection of these specific orbits and clarify whether the effectiveness of the method would hold if these particular structures were not present in the target graph?

4. PRBCD is designed for the scalable graph adversarial attack, but the experiments are mainly on small-scale datasets. Evaluating on some large-scale datasets, such as Reddit and ODB-arxiv, would provide a more robust assessment of the scalability claims, especially in comparison with GOttack.

### Questions
1. In line 286, why GOattack works with k=5-node graphlets?
2. Please give the time used in orbit discovery to better show the efficiency of the method. 
3. Does the used time of GOattack presented in Table 4 includes the preprocessing phase (i.e., orbit discovery)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes GOttack, a first-of-its-kind local attack on GNNs via structure perturbations, that leverages graph orbits to narrow down the search space. That is, via topological analysis, a short list of nodes is created for the targeted node. This shortlist is then used to generate the perturbations. The authors validate the efficacy of their method on 5 graphs, 3 GNNs, and, additionally, four GNN defenses.

### Strengths
1. The authors propose a new angle on the adversarial attack problem for structure perturbation using insights from topology.
1. The found perturbations transfer well between different GNN architectures.
1. The paper is well structured and (except for some details) it is easy to follow.
1. The empirical verification not only assesses misclassification rates but also uses explainers for qualitative insights.

### Weaknesses
 1. The attack is an indirect attack using a surrogate (i.e., non-adaptive [1]). This severe limitation should be discussed prominently in the text. Moreover, GOttack seems to transfer evasion attacks to the poisoning setting and the attack is not evaluated against adaptive attacks (except for GCN; e.g. directly attack  GSAGE/GIN with PRBCD and not the GCN surrogate).
 1. I had a hard time following some of the discussion Section 4.2 since it is not clear when numbers are general constants or tailored to the example in Figure 2.
 1. The attack does not seem scalable due to the required preprocessing (see question below).
 1. The authors do not properly discuss scalable attacks on GNNs. For example, the authors compare with PRBCD but ignore its properties in their discussion. For example, the argument on ll. 517-519 does not necessarily apply to PRBCD. Also, the statement that PRBCD was of quadratic scalability seems wrong/imprecise (Section B.2).
 1. The topological analysis is independent of the node features, implicitly assuming that they are somewhat different to ensure attack efficacy.
 1. The evaluated defenses are not state-of-the-art [1].

I am willing to increase my score if especially the first two weaknesses are properly addressed.

Minor:
 1. It is not clear why Metattack is mentioned in the related work, but there is no further discussion about the differences.
 1. The bilevel nature of poisoning attacks (eq. 2) usually arises from the fact that one wants to contrast predictions of the model trained on the clean data and perturbed data. The inner maximization is usually rather considered part of the loss.
 1. The authors might want to note that the reliability of GNN explanations is debated [2,3]

### Questions
1. Have the authors tried to scale to larger graphs? E.g., OGB arXiv, Products, or Papers100M (as PRBCD does)?
1. Is $\mathcal{G}\_{g p} = \mathcal{G}\_{s'}$ in Definition 2
1. Are orbits 15 and 18 special regardless of the number of nodes? If so, could the authors please elaborate a bit more?
1. Why do the authors focus on very small budgets 1..5? Usually, the budget is made relative to the degree of the attacked node.
1. How is the preprocessing of Gottack included in the times reported in Table 4?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The work tackles the problem of adversarial attack for Graph Neural Networks (GNNs). The authors propose a new “universal” attack to the graph topology through graph orbits, denoted GOttack. The paper identify that nodes from a certain part of the structure (specifically from the concept of orbits) are rather more vulnerable to attacks and consequently would be good targets. The main key of the method is the proposed trade-off between attack success rate and the time-complexity.

### Strengths
- The paper is well motivated and well written.
- The method is targeting the complexity challenge of attack adversarial attack, which is something that is very sparse in current literature as the majority of the work rather evaluate from an attack perspective (lower attack accuracy) rather than the time complexity — making sometimes their method not possible in some practical settings.
- Evolving the concept of graph orbits and graphlets in the perspective of adversarial attack is novel. Specifically, the theoretical analysis in Theorem 1 is very interesting.

### Weaknesses
The main weakness of the paper is related to the experimental part. Specifically the following points:
- The authors only consider RGCN, GCN-Jaccard, GCN-SVD and MediaGCN as a defense method to attack. Recent work have clearly shown the failure of these defense in defending (specifically targeted attacks). I would rather consider adding other benchmarks such as GCNGuard [1] and specifically the newly presented GCORN [2]. The choice of defense mechanisms is crucial, and the current selection does not represent the state-of-the-art in robust GNNs. This raises concerns about the practical relevance of the attack method, as it may not be effective against more sophisticated defenses. A more comprehensive evaluation should include defenses that are known to be more resilient to adversarial attacks, such as those based on certified robustness or adversarial training.
- The Budgeted attack results are rather focusing on the GCN, GIN and GraphSage and ignores the defense methods. Typically in the adversarial litterature, we are rather interested in the attack success rate when subject to the defense method, as by definition the original models are rather known to be vulnerable to attacks. The evaluation should primarily focus on the attack's effectiveness against defended models, as this is the most relevant scenario for assessing the attack's practical impact. Evaluating against undefended models provides limited insight into the attack's true capabilities.
- Small note: While I understand that you provide the std values for the success rate in the appendix, it would have been much easier to include them also on the main paper’s tables. 

Additionally, from the theoretical perspective:
- The theoretical insights presented in Theorem 1 are very interesting. It would be great to also validate the claims experimentally. One first experimental setting would be to consider the effect of choosing nodes in the orbits 15 and 18 and other orbits to see the effect of the hitting times. The lack of empirical validation for the theoretical claims is a significant gap. The paper should provide experimental evidence to support the theoretical findings, specifically regarding the relationship between orbit selection and attack effectiveness. This would strengthen the paper's claims and provide a more complete understanding of the proposed method.

### Questions
- Please provide the attack success when subject to the defenses proposed in [1] and [2], as they will allow the user to judge the real validity of the method.
- The theoretical analysis doesn’t seem to take into account the node features ? Could you please clarify on that
- Is it possible to provide empirical results validating the claims in Theorem 1? Refer to my proposed setting in the Weakness section, otherwise I am open to any other proposition.
- Is your framework also adaptable to node-feature based adversarial attacks ? As it seems you refer to it in general attack formulation in Section 2 (mainly Eq. 1).

I am willing to raise my score if the some of the previous question were answered.

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
4

### Summary
This paper presents GOttack, an adversarial attack framework that manipulates graph orbits to disrupt Graph Neural Networks (GNNs) with subtle yet effective modifications. GOttack outperforms existing methods by achieving the highest misclassification rates while reducing training time by 45% across multiple GNN architectures and benchmark datasets. The study highlights the vulnerability of GNNs to structured attacks on graph orbits.

### Strengths
- This work proposed an interesting approach for attacking GNNs using the concept of graph orbits.
- Authors offered some insights into the effectiveness of GOttack.
- Authors have compared GOttack with several attack methods, including PRBCD.

### Weaknesses
 - The improvement over attack baselines is not very convincing. In Table 2, GOttack outperforms the baselines by less than 1% in many cases—an improvement smaller than the standard deviation reported in Appendix D. This raises concerns that GOttack may not consistently outperform these baselines, as using a different random seed could potentially alter the ranking of attack methods in Table 2.
- GOttack underperforms compared to attack baselines in most cases when the budget exceeds 1, as shown in Tables 9–13.
- GOttack appears ineffective on heterophilic graphs, as suggested by the homophily assumption in line 256 and the empirical results in Appendix D.
- Some recent and more effective defense methods are missing from the experiments. The authors only consider defense methods published before 2021, while several more powerful approaches have been proposed in the past two years. For example, GARNET [1] and SG-GSR [2] have shown stronger results than the defense methods included in this work.

### Questions
- What is the runtime of the preprocessing stage?
- How large of a graph can GOttack scale to?
- In Table 2, why is there a significant difference (over 30%) between GOttack-GCN and GOttack-GSAGE on BlogCatalog?

### Soundness
3

### Presentation
2

### Contribution
2
