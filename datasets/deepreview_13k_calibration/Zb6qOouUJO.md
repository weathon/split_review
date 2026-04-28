# Efficient Fully Single-Loop Variance Reduced Methods for Stochastic Bilevel Optimization

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Stochastic Bilevel Optimization (StocBO) has gained traction given its unique nested structure, which is increasingly popular in machine learning areas like meta-learning and hyperparameter optimization. A recent innovation by Dagreou et al. provided a unified single-loop framework for finite-sum StocBO. This presented the SABA method, a SAGA-type approach, achieving an iteration complexity of $\mathcal{O}({(m+n)^{3/2}}/{T})$ and a memory cost of $\mathcal{O}((m+n)(d+p))$. In this context, $m$ and $n$ symbolize the finite sum counts for the outer and inner-level tasks, while $d$ and $p$ describe their parameter dimensions. However, a drawback surfaces with memory consumption, especially with significantly large values of $m$ or $n$.
In response to this, we present the SBO-LSVRG, an adept solution inspired by Loopless-SVRG (LSVRG). This avant-garde method not only achieves the desired iteration complexity but also substantially trims the memory cost to a leaner $\mathcal{O}(d+p)$. To our awareness, this paper pioneers in illustrating, from a theoretical lens, the application of LSVRG to bilevel optimization, particularly in non-convex realms. Furthermore, our variance-reduced method, SBO-LSVRG, excels with an optimal convergence speed. Comprehensive experiments validate the efficiency of our proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the problem of bilevel optimization, and introduce  a new method named SBO-LSVRG. This method achieves the SOTA iteration complexity with a lower memory cost. The experiments confirms the effectiveness of the proposed method.

### Strengths
1. The paper is well-organized, and easy for readers to follow.
2. This paper can obtain SOTA complexity with lower memery cost. The rigorous proof is provided.

### Weaknesses
1. The novelty is limited. This paper mainly follows Dagreou et al. (2022). Therefore, the theoretical contribution is limited. It is better if the authors could highlight the challenges in the analysis.
2. Some assumptions made in the paper seems quite strong, would it hold in practical scenarios?

### Questions
1. Can the proposed method handle non-convex or non-strongly convex lower-level problems, which are common in many real-world applications?
2. This paper investigate the iteration complexity of the proposed method, how about the sample compexity?
3. Is the rate obtianed in this paper optimal in terms of $\epsilon$, $m$ and $n$?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work provides a study for stochastic bilevel optimization and provided a fully single-loop stochastic bilevel algorithm using an idea from Loopless-SVRG. Compared to SABA, another fully single-loop stochastic optimizer via SAG, the proposed SBO-LSVRG method achieves a similar sample complexity but with less cost in memory and space. The algorithm and analysis are also applied to minimax problem as well. Experiments are provided to demonstrate the effectiveness.

### Strengths
1.	The motivation is clear and the study on fully single-loop bilevel method is very important given its simple structure and implementation. Applying the idea from loopless-SVRG is a good contribution, and the authors have done a good job in the algorithmic design and literature review. 

2.	The proposed algorithm achieves the same sample complexity as SABA, the best fully single-loop stochastic bilevel method, but with much less memory cost. In terms of the performance, it seems the method can be more efficient than SABA.

### Weaknesses
1. Applying the idea of L-SVRG in bilevel optimization sounds a little bit incremental. However, I feel that some challenges such as the probabilistic selection step and the proof of variance reduction may introduce some new analysis and designs. I strongly suggest that the authors can explicitly point them out instead of just saying “This approach is far from trivial”. Specifically, the probabilistic selection mechanism in Algorithm 1, where $x_{k+1}$ is updated with probability $p$ and $\tilde{x}$ with probability $1-p$, warrants a more detailed explanation. How does this probabilistic update contribute to the overall convergence and stability of the algorithm? Furthermore, the proof of variance reduction, particularly in the context of bilevel optimization, could be elaborated. A clearer articulation of these aspects would strengthen the paper's contribution.

2. The comparison miss an important baseline as show here: it proposes a single-loop SARAH-based bilevel optimizer named SRBA, which achieves a near-optimal $(n+m)^{1/2}\epsilon^{-1}$ sample complexity. It would be good to have a comparison here. Specifically, how does the proposed method's performance compare to SRBA in terms of convergence rate and computational efficiency, especially when dealing with large datasets where $m$ or $n$ is significantly large? A direct comparison in the experimental section would provide valuable insights into the practical advantages of the proposed algorithm.

### Questions
Overall, I think this work has provided some interesting approach based on the idea from L-SVRG. I like the method and give 6. However, I cannot give higher score given several questions regarding the novelty clarification and the missing baseline. The questions and suggestions can be found in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a single-loop algorithm inspired by L-SVRG solving (finite-sum) stochastic bilevel optimization problem with an iteration complexity of $\mathcal{O}((m+n)^{3/2}/T )$ and a memory cost of $\mathcal{O}(d + p)$. The main contribution is reducing the memory cost from $\mathcal{O}((m+n)(d+p))$ to $\mathcal{O}(d + p)$ but achieving the same iteration complexity compared with the state-of-the-art algorithms.

### Strengths
Originality: In this paper, the authors considered using L-SVRG for problems with a nested structure and proposed a method for solve stochastic bilevel optimization problem based on it. 

Quality: Compared with SABA, their approach reduced the memory cost significantly. 

Clarity: The overall structure and presentation of the paper is clear. 

Significance: This research provide lower memory cost without affecting iteration complexity for stochastic bilevel optimization and other related problems.

### Weaknesses
1. In Contribution (c), the authors stated "We establish the link between our method and related areas, such as federated learning and minimax optimization, and we provide a theoretical analysis for both of these areas." However, I don't see any theoretical analysis about federated learning. It is only in the future work section.

2. From my perspective, the novelty of the paper is limited. The only improvement is reducing cost memory by using a different variance reduction technique. The core algorithmic structure remains similar to existing bilevel optimization methods, and the application of L-SVRG, while effective for memory reduction, doesn't introduce a fundamentally new approach to solving the bilevel problem itself. The reduction in memory cost is certainly valuable, but the algorithmic contribution feels incremental rather than transformative.

3. The plots in the paper are hard to read. For example, in figure 2, what is the x-axis of the plots. It is better to provide some plots in terms of running time. The lack of clear axis labels and the absence of running time comparisons make it difficult to assess the practical implications of the proposed method. The plots should clearly show the convergence behavior with respect to a standard metric like running time, which is more informative than an abstract oracle complexity measure.

### Questions
1. In Theorem 1, the authors stated "This result leads to the convergence rate $\mathcal{O}(\epsilon^{−1})$, which is optimal in stochastic bilevel optimization. " I think this result is for general stochastic bilevel optimization problem. But in this paper, the authors considered a finite-sum version of it, which is easily than the general version. The convergence rate could be potentially improved. It would be more convincing if the authors point out more related references.

2. In Corollary 1, the authors stated "the rate under nonconvex conditions remains unclear. We initially introduce a rate of $\mathcal{O}(n^{2/3}\epsilon^{−1})$". But the authors did not state what kind of convergence criteria do they consider here? Can you provide more references related to the single-level result here?

3. In Corollary 2, do you assume $F$ is convex? Or it could be possibly non-convex. If it is non-convex, how do you get the rate $\mathcal{O}(n^{2/3}\epsilon^{-1})$?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the stochastic bilevel optimization problem and proposes a new fully single-loop method using the LSVRG to approximate the gradient. Also, theoretical analysis and experiments are presented to show the superiority of the proposed method.

### Strengths
1. This paper is well-written and easy to follow. 
2. The proposed is novel and the theoretical analysis and experiments are presented to show the superiority of the proposed method.

### Weaknesses
1. More experiments are expected, such as meta-learning, and poison attack. I think hyperparameters selection and data hyper-cleaning are somewhat similar, experiments on other applications are expected.
2. Some O(1) sample complexity methods should be compared, e.g. SUSTAIN[1]
3. The proposed method seems can not effectively solve the large-scale problem. Can the author give some results on the large-scale datasets?
4. The convergence analysis is based on the PL condition. An analysis on a more general case is expected.

### Questions
1. Can the author explain the relation between the gradient estimation of the proposed method and other hypergradient methods?
2. Why the complexity of SVRB is different from VRBO in Table 1? I think they have the same complexity since they all use STORM. 
See other questions in weakness.

On page 4, below Equation (4), the sentence is not correct.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
