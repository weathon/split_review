# Neural Architecture Search by Learning a Hierarchical Search Space

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
Monte-Carlo Tree Search (MCTS) is a powerful tool for many non-differentiable search related problems such as adversarial games. However, the performance of such approach highly depends on the order of the nodes that are considered at each branching of the tree. If the first branches are not discriminative enough, i.e. they cannot distinguish between promising and deceiving configurations for the final task, the efficiency of the search is exponentially reduced. While in some cases the order of the branching is given as part of the problem (e.g. in chess the sequential order of the moves is defined by the game), in others, such as Neural Architecture Search (NAS), the visiting order of the tree is not important, and only the final architecture matters. In this paper, we study the application of MCTS to NAS for the task of image classification. We analyze several sampling methods and branching alternatives for MCTS and propose to learn the branching by hierarchical clustering of architectures based on their similarity. The similarity is measured by the pairwise distance of output vectors of architectures. Extensive experiments on two challenging benchmarks on CIFAR10 and ImageNet show that MCTS, if provided with a good branching hierarchy, can yield promising solutions more efficiently than other approaches for NAS problems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method for supernet sampling for neural architecture search using Monte-Carlo Tree Search (MCTS). After an initial phase of supernet training, the method uses similarity distances between architecture outputs and hierarchical clustering to build a search tree, then continue the supernet training by sampling from this tree using MCTS.

### Strengths
-The paper is overall well written.
-The methodology is well-explained and the contributions are clearly defined, the paper is well-placed in the literature.
-While not theoretically justified, the idea of learning the Monte-Carlo tree is promising.
-The experimental results are convincing on the ImageNet dataset.

### Weaknesses
 -The method still requires initial supernet training using uniform sampling before being able to build the tree, which is known to be computationally heavy.
-The overall contribution seems incremental, as it is mainly a new way to construct a Monte-Carlo tree for supernet sampling.
-For the experiment on the pooling dataset, the authors explain that this extremely small search space of 36 architectures is challenging because the initial supernet training shares weights between architectures with different pooling configurations. Given that the proposed method discriminates architectures by comparing the outputs after supernet pre-training, I wonder how the method is able to find a more efficient representation of the tree if the weights themselves are not optimal. Furthermore, the classical sampling methods (uniform, Boltzmann…) are unable to find the best architecture out of 36? How many samples are performed? The results, while in line with the results of [1], seem surprising and the paper could benefit from a more thorough explanation.
-There are several typos and the writing is overall unclear in Section 5.1.
-Is the Boltzmann sampling over UCT in Section 4.2 necessary? The UCT formula already offers a trade-off between exploration and exploitation. If it is necessary, then an ablation study could be useful.
-The following claim : “Different from other works such as Wang et al. (2021a) and Zhao et al. (2021b) that use the model accuracy directly for the tree design, the output vector provides more information for clustering architectures” seems unsupported.
-Building the search tree requires building a hierarchical clustering. As the authors use the pairwise distance matrix of all architectures in the search space over a mini-batch, the complexity of building this hierarchical clustering is O(n^2) complexity. For large search spaces, this could be very inefficient. A comparative complexity analysis of the proposed method would be welcome.

### Questions
The paper proposes an interesting idea, is mainly well-written and shows some good results on benchmark datasets. As written in the weaknesses section, there are several avenues for clarification and improvements on the paper.

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
2

### Summary
This paper challenges the commonly assumed node independence in Neural Architecture Search (NAS), which may limit both efficiency and performance. To address this, the authors propose a Monte Carlo Tree Search (MCTS) method incorporating a learned hierarchical tree structure, built with agglomerative clustering based on model output distances, to improve NAS effectiveness. Experiments are conducted on NAS benchmarks for CIFAR-10 and ImageNet image classification tasks.

### Strengths
* The paper introduces an approach by addressing node dependencies to improve NAS efficiency.
* Leveraging the UCT (Upper Confidence bounds applied to Trees) approach, the authors further utilize a learned tree structure to reduce the reliance on manually crafted search space designs.
* The paper provides ablation studies to analyze the effects of the proposed method in more depth.

### Weaknesses
 * The abstract may benefit from significant revision. Currently, it primarily highlights MCTS fundamentals and suggests general applicability, but the paper is focused on a NAS-specific task that utilizes MCTS and related techniques to enhance NAS performance. The abstract and introduction appear inconsistent in conveying the core contribution and scope.
* The rationale behind using model output distances to construct the tree structure and improve NAS is not clearly discussed, and the method itself lacks detail. This part should be the core of the paper, yet there is minimal explanation in the main text. Specifically, the method for calculating these distances, the choice of distance metric, and the impact of different metrics on the resulting tree structure are not addressed. Furthermore, the connection between these distances and the expected performance of the architectures is not clearly established. It's unclear how the semantic relationship between architectures, as defined by output distances, translates into an effective search strategy for high-performing models.
* While resource constraints may be a factor, it remains unclear whether the method scales well for large networks, which are particularly relevant in NAS applications. The experiments mainly validate that the learned tree provides slight improvements but do not assess scalability in larger search spaces. The paper lacks a discussion on the computational cost of constructing and utilizing the learned tree, especially in comparison to standard NAS approaches. It is not clear how the computational overhead of the clustering and tree construction impacts the overall efficiency of the proposed method, particularly for more complex search spaces. The experiments are limited to relatively small datasets and search spaces, making it difficult to extrapolate the findings to more realistic NAS scenarios.

Minor Comments
* Line 306: check around "Fig.3.4(a)"

### Questions
* How does this method compare with other state-of-the-art NAS techniques, such as those in the Neural Architecture Transfer (NAT) series?
* What insights or theoretical basis underlie the decision to use model output distances for improving NAS performance? (I already assume this will be addressed in a revision in my score.)

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a Neural Architecture Search (NAS) approach that leverages Monte Carlo Tree Search (MCTS) with a learned hierarchical search space. Instead of using a non-optimal, pre-defined hierarchical search order, this paper proposes to learn the branching by hierarchical clustering of architectures based on their similarity measured by the pairwise distance of output of architectures. The experiments on CIFAR10 and ImageNet demonstrate that the proposed approach yields better solutions than previous approaches.

### Strengths
This paper highlights the shortcomings of the previously used node independence assumption and demonstrates that too restrictive assumptions converge to worse solutions.

### Weaknesses
The weaknesses of this paper are the limited novelty, results not significant, and the unclear approach.

First, for the limited novelty and results not significant, this work improves previous works (Wang et al., 2021a; Zhao et al., 2021b) by replacing the model accuracy with the output vector. While the output vector provides more information for clustering architectures, the novelty is limited. Furthermore, the results only slightly outperform previous works (Su et al., 2021a; You et al. 2020; …), which is insignificant. In addition, making early tree nodes more discriminative is highly relevant to the partitioning or splitting problems in decision tree learning, which has been studied by many in the past (Costa and Pedreira, 2023).
Costa, V.G., Pedreira, C.E. Recent advances in decision trees: an updated survey. Artif Intell Rev 56, 4765–4800 (2023).

Second, the presentation has a lot of improvements, especially the approach. The proposed method is ambiguous and does not seem like MCTS. MCTS uses UCT to select child modes; however, the proposed method uses Boltzmann sampling with a UCB-like score as the parameter. The authors should justify whether this design follows the UCT foundations of balancing exploration and exploitation. 
Most importantly, using $Acc(a_i)/n_i$ in Eq. 4 is weird. From the definition, the first term in the formula is the average reward (Eq. 1 in Kocsis & Szepesvári, 2006). However, Eq. 4 further divides the accuracy by the visit count. Since the accuracy $Acc(a_i)$ is already considered the average reward, it makes no sense. If this is not a typo, the authors should justify the correctness of such a design.

### Questions
Questions related to the proposed MCTS procedure:
- As the tree is already constructed, does the algorithm still run selection from a single root node and then expand the known tree structure? Or does it just start sampling from the entirely constructed tree?
- The typical MCTS involves several phases (e.g., selection, expansion, simulation, backpropagation) per simulation, while it is unclear how the proposed procedures in Algorithm 1 are linked to these phases.
- It is mentioned that $C(a_i) = Acc(a_i)$ for architecture search in line 340. Does it mean that for supernet training, $C(a_i)$ is set to Eq. 4? It is unclear which parts use $Acc(a_i)$ or Eq. 4 in Algorithm 1.
- In Algorithm, $P_{train}$, $P_{search}$, and Eq. 5 are not defined.
- In line 358, it is mentioned that there is a warm-up period for uniform sampling, which is also not included in the typical MCTS routines (Kocsis & Szepesvári, 2006). As MCTS should already be able to balance exploration and exploitation, what is the purpose of adding such a warm-up period?
- In line 360, why is $C(a_i) < 1$ when nodes are visited?

Other comments related to typos and presentation issues:
- For Figure 1, it is difficult to understand why the subfigures "independent" and "joint" are drawn like this.
- For Figure 2, (b) and (c) use different styles to represent the tree structure, which should be normalized to the same.
- The section title "3.4 Sampling with conditional probabilities: Monte Carlo Tree Search" is confusing as this section does not seem to have any links to (the typical) MCTS.
- For Table 3, "the categorical vector representation" is not included in the discussion.
- Some terms are not consistently used, e.g., "Monte Carlo Tree Search" or "Monte-Carlo Tree Search"; "equation" or "eq." or "Eq.".
- Several typos, e.g., "Fig.3.4(a)", "and T the temperature term", "UTC".
- Placing Algorithm 1 in Appendix B lowers the readability. It would be more appropriate to include it in the main text, especially since the authors often refer to it with "see algorithm 1 in Appendix B".
- In Algorithm 1, the equations should be explicitly stated instead of mentioning "as in Eq. 1."

### Soundness
2

### Presentation
1

### Contribution
2
