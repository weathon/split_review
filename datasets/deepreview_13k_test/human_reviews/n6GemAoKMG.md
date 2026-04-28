# EvA: Evolutionary Attacks on Graphs

- Decision: Reject
- Scores: 5, 5, 8, 5

## Abstract
Even a slight perturbation in the graph structure can cause a significant drop in the accuracy of graph neural networks (GNNs). Most existing attacks leverage gradient information to perturb edges. This relaxes the attack's optimization problem from a discrete to a continuous space, resulting in solutions far from optimal. It also restricts the adaptability of the attack to non-differentiable objectives. Instead, we propose an evolutionary-based algorithm to solve the discrete optimization problem directly. Our Evolutionary Attack (EvA) works with any black-box model and objective, eliminating the need for a differentiable proxy loss. This permits us to design two novel attacks that: reduce the effectiveness of robustness certificates and break conformal sets. We introduce a sparse encoding that results in memory complexity that is linear in the attack budget. 
EvA reduces the accuracy by an additional $\sim$11\% on average compared to the best previous attack, revealing significant untapped potential in designing attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new type of graph neural network (GNN) attack algorithm called Evolutionary Attack (EvA). EvA uses a genetic algorithm-based approach to directly optimize the graph structure in discrete space without the need for gradient information, making it adaptable to any black-box model and objective, including non-differentiable targets. By employing sparse encoding, EvA reduces memory complexity. Through adaptive mutation in genetic algorithms, it enhances higher performance. Experimental results show that EvA is more effective in reducing GNN accuracy than the SOTA methods, with an average accuracy decrease of about 11%. Furthermore, EvA has designed several new types of attacks and has shown high effectiveness in specific attack scenarios.

### Strengths
1. EvA does not rely on gradient information and can directly optimize in the discrete space. This innovative approach addresses some fundamental issues encountered by traditional gradient-based attack methods when dealing with graph-structured data, such as the need to relax discrete problems into continuous spaces and the reliance on non-differentiable objective functions.
2. The sparse encoding scheme significantly reduces the memory complexity of the attack, making it linearly related to the attack budget. This design not only improves the efficiency of the attack but also enables EvA to handle larger-scale graph data. Furthermore, by using batch evaluation methods, EvA can make more efficient use of computational resources, accelerating the optimization process, which is particularly important for large-scale graph data.
3. EvA does not require internal information of the model, which means it can be applied to black-box models, where we can only observe the input and output without access to the internal parameters. This feature greatly expands the scope of the attack method, enabling it to counter models that are commonly encountered in practice and protect their internal structure from being known to the outside world.

### Weaknesses
1.In the paper, it seems that the fitness function needs to be used frequently to analyze the population. The authors optimize the computation by using batched forward propagation and evaluating with the fitness function in one go. However, this also seems to require a significant amount of computational cost. It would be hoped that the authors conduct some experimental analysis comparing the time efficiency of EvA with SOTA attack methods.
2. In the experiments of this paper, the datasets used, such as CoraML, Citeseer, and PubMed, seem to be relatively small. When facing larger graphs, the computational cost of running the genetic algorithm will increase dramatically, and at this time, the performance of EvA may decline.
3. The layout of the article seems to have a few minor issues. For example, Fig. 2 is mentioned before Fig. 1 in the text.

### Questions
The paper proposes an effective attack method. However, I am curious if there are any specialized defense methods against this kind of genetic algorithm for adversarial attacks. If there are, it would make the work more comprehensive.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new method for attacking Graph Neural Networks (GNNs) using evolutionary algorithms. Unlike traditional gradient-based attacks, which can be limited by the need for differentiable objectives and may yield suboptimal results, EvA directly tackles the discrete optimization problem of modifying graph structures. This approach enables EvA to operate in a black-box setting, without requiring gradient information, and can therefore work with any model or objective, including non-differentiable ones.

### Strengths
1. EvA presents an innovative approach to attacking GNNs through an evolutionary algorithm, moving beyond the limitations of traditional gradient-based methods.

2. The method introduces new attack objectives, including reducing robustness certificates and conformal prediction sets, marking the first exploration of these targets within graph adversarial attacks.

### Weaknesses
1. Even the authors have mentioned the mitigation of efficiency issues, the evolutionary search strategy can still be computationally expensive, especially for large graphs, and may struggle with convergence in high-dimensional search spaces.

2. Evolutionary algorithms are well-studied in adversarial attack scenarios outside of graph applications. The novelty of applying essentially similar algorithms within the graph setting remains a question.

3. The datasets in this paper, such as Cora-ML, Citeseer, and PubMed, are widely used benchmarks for evaluating GNN models, but they are relatively small in terms of the number of nodes and edges. This aligns with my first concern and can limit the evaluation's applicability to real-world scenarios where graphs, such as social networks, protein interaction networks, or large-scale citation networks, have millions of nodes and edges.

### Questions
My major concerns are the scalability and the novelty.

### Soundness
2

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
5

### Summary
This paper proposes a new explore-and-exploit-based graph attack method. Unlike previous gradient-based methods, it no longer relies on approximate discrete optimization of the adjacency matrix. By eliminating the need to compute the gradients of a dense matrix, EVA significantly reduces the cost. Experimental results indicate a notable improvement compared to state-of-the-art methods.

### Strengths
1. The attack setting in this work is comprehensive, evaluating both local and global scenarios, and it selects a reasonably appropriate inductive setting.

2. Simple and effective with straightforward idea. Compared with gradient-based methods, e.g., PGD, PR-BCD, MetaAttack, EVA effectively reduce the cost.

### Weaknesses
## **Notations and mathematical expressions are unnecessarily complex**

EVA itself is a very simple method, and several improvements over the baseline-EVA (such as stopping the attack on nodes that are already misclassified) are not novel to this paper. However, the authors have chosen to use complex mathematical notation. Although this complexity does not hinder correctly understanding of the work, it creates unnecessary obstacles. Additionally, authors have chosen notations that is different from that used in this field, which I also believe is unnecessary. I think good writing should make it easier for readers to grasp the authors' ideas and methods, rather than trying to be distinctive in this regard.

## **Scalability**

The largest graph used in this work is PubMed. However, PRBCD can scale attack to ogb-arxiv, Products, and Papers 100M. Since one of the advantages of EVA is that it does not rely on computing gradients of the dense adjacency matrix, conducting experiments on larger-scale graphs would be more convincing.

### Questions
1. What is the time cost of EVA. Can authors provide some experiments to show this?

2. Can authors conduct experiments on larger graphs?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work tackles the problem of adversarial attack for Graph Neural Networks (GNNs). The authors propose approaching the problem through  an evolutionary-based algorithm to solve the adversarial optimization problem without using a relaxation to the continuous space nor using gradient-based methods.

### Strengths
- The tackled problem of adversarial attacks is very interesting and proposing alternative the the widely used gradient-based method is important.
- Attacking both the adversarial certificates and specially the conformal guarantees extracted from the Conformal prediction framework is very novel and interesting.

### Weaknesses
- The usage of Genetic Algorithms in attacking adversarial attacks is not novel from my opinion. Specifically, previous work [1] have discussed the subject and proposed a method based on that. While the authors refer to this work in their related work section as proposing to tackle the subject from an RL perspective, they omit the fact that they also proposed a genetic-based attack denoted  GeneticAlg (Section 3.2.3 in their paper).
- I would also expect empirical results comparing your slightly different approach to their approach. 


- In the experimental results, the authors evaluate only on the vanilla version of the models rather than considering adversarial defense methods. This latter therefore doesn’t confirm the effectiveness of the method as we are rather more interested in its performance when subject to the defense in comparison to the considered adversarial attacks. 


- While the authors discussed the memory complexity of the methods, it seems that they didn’t provide any details about the time complexity and specially in comparison to the considered attacks.  

—

[1] Adversarial Attack on Graph Structured Data. Dai & Al. - ICML 2018.

### Questions
- Would it be possible to provide more information about your data splits ? Why don’t you directly use the publicly available train/test splits (as they are provided for all the datasets you are considering)?
- Could you provide more details on the contrast of your proposed method to the method GeneticAlg [1] and also explain your claim about novelty of using Genetic Attacks. 
- Additionally, would be important to provide the experimental results comapring your method to the GeneticAlg [1]. 
- Could you provide the results when subject to adversarial defenses ? 
- Could you analyse the time complexity of your method in comparison to the considered attack baselines?

### Soundness
2

### Presentation
3

### Contribution
1
