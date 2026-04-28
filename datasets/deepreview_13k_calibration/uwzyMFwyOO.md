# Learning Latent Graph Structures and their Uncertainty

- Decision: Reject
- Avg Score: 5.60
- Scores: 3, 5, 8, 6, 6

## Abstract
Within a prediction task, Graph Neural Networks (GNNs) use relational information as an inductive bias to enhance the model's accuracy. As task-relevant relations might be unknown, graph structure learning approaches have been proposed to learn them while solving the downstream prediction task. In this paper, we demonstrate that minimization of a point-prediction loss function, e.g., the mean absolute error, does not guarantee proper learning of the latent relational information and its associated uncertainty. Conversely, we prove that a suitable loss function on the stochastic model outputs simultaneously grants (i) the unknown adjacency matrix latent distribution and (ii) optimal performance on the prediction task. Finally, we propose a sampling-based method that solves this joint learning task. Empirical results validate our theoretical claims and demonstrate the effectiveness of the proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tackles the latent structure learning on graph structured data and demonstrate that minimizing prediction function does not guarantee a calibrated model with rigorous theoretical justifications. The author proposes a sampling-based optimization using Maximum Mean Discrepancy (MMD) between output distributions and shows the effectiveness of joint learning tasks.

### Strengths
1. The theoretical results of the paper are fully-justified although the reviewer didn't check every details of the proof. 
2. The paper proves the feasibility of minimizing joint distribution discrepancy of (A<X) leads to both optimal point predictions and latent distribution calibration

### Weaknesses
1. The paper does not focus on graph-specific optimization techniques. It seems that no matter how strcuture of {x} is generated, the consluion of the theoretical results always applied. In the proof of injectivity for example, the graph structure is modeled as a linear projection with continuous value 
2. The paper oversimplifies the graph structures, for example, continuous adjacency matrices and bernouli distribution in experiments, which makes the practical impact of the paper quite limited in my opinion. The use of independent Bernoulli distributions for adjacency matrices, while mathematically convenient, fails to capture the complex dependencies and structural properties inherent in real-world graphs. This oversimplification undermines the practical relevance of the experimental results.
3. The contribution and proposed algorithm needs to be justified on more data modality with latent structure given that the paper seldomly uses property of the graph structure in its optimization. I would like to see the paper remove the focus on graph structures and verify the effectiveness in different domains such as image/audio etc.

### Questions
1. Why the inindependent bernouli distribution is used in experiment for adjacency matrix A? In reality, the graph structures follows (1) Erdős–Rényi Model (2) Barabási–Albert Model (BA Model). 
2. Maybe I missed somewhere, what is the feature distribution $P(X)$ used in experiments?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors point out the limitation of current point-prediction methods, which cannot guarantee the calibration of the distribution of adjacency matrix $A$.
Therefore, the authors propose a sampling-based learning method for joint optimization.

### Strengths
1. The uncertainty issue of graph structure learning is important.
2. Theoretical analysis and proofs are provided.

### Weaknesses
1. Section 4 has no analysis specifically related to the adjacency matrix $A$, which contradicts contribution 1. Maybe $A$ is input into $L$ or $x$, but the analysis in Section 4 could be applied to any scenario and cannot bring any insights for the community of graph learning. The core issue is that while the method aims to learn a distribution over adjacency matrices, the theoretical analysis does not explicitly consider the structural properties of these matrices, such as sparsity, degree distribution, or connectivity patterns. The analysis treats $A$ as a generic latent variable, failing to leverage the unique characteristics of graph structures. This lack of specificity undermines the claimed contribution to graph structure learning.

2. Similarly, the methodological contribution in Section 5 is also universal and seems unrelated to GSL or GNNs. The proposed sampling-based learning method, while potentially useful, does not incorporate any graph-specific inductive biases or constraints. It could be applied to any problem involving the learning of a distribution over latent variables, without any modification. This generality, while not inherently negative, diminishes the contribution to the specific field of graph structure learning, as it does not address the unique challenges and opportunities presented by graphs.

3. Lack of experimental results on real datasets compared with GSL baselines. The absence of experiments on real-world graph datasets makes it difficult to assess the practical relevance and effectiveness of the proposed method. Without comparisons to existing graph structure learning baselines, it is unclear whether the method offers any advantages over existing approaches. The synthetic experiments, while useful for validating theoretical claims, do not fully capture the complexities of real-world graph data and the challenges associated with learning graph structures in practical applications.

### Questions
1. Why MMD? And why not KL or JS divergence? Lines 247-251 are insufficient. Please give reasons why the theory is not feasible or experimental gaps.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the Graph Structure Learning (GSL) problem, sometimes referred to as the ‘Latent Graph Learning’ problem, which concerns co-learning the graph structure and GNN weights for downstream prediction. The paper reveals issues with point-predictor losses with regards to the learning of the latent graph structure, and proposes a sampling based approach to overcome such issues.

### Strengths
I believe this work to be the first to consider the calibration aspect of the latent graph structure, which is an interesting point.

A primary supporting argument for GSL methods is that the learned graph is itself useful for interpretability purposes. But most (all?) approaches make little effort to (i) show an instance where this is actually useful beyond a nice visualization or (ii) discuss why we should believe this underlying graph corresponds to some real object.

This work seems to address address (ii).

### Weaknesses
 **Motivation**

As best I can understand, the paper attempts to address (ii), but without addressing (i), i.e. the motivation of the entire effort. Why should anyone care in the first place? 

The authors attempt to provide high-level applications, e.g., “Examples include e.g., social interactions where links can intermittently be present, traffic flows affected by road closures and temporary detours, and adaptive communication routing. It follows that a probabilistic framework is appropriate to accurately capture the uncertainty in the learned relations whenever randomness affects the graph topology.”

But it is not clear to me how GSL is/would be actually used in these applications, why uncertainty over such an inferred latent graph is important in these applications, nor why calibrated uncertainty measures of the latent graph are important.

&nbsp;


**Gaps in Related Work**

There are large gaps in related work on graph structure learning, e.g. using unrollings and/or Bayesian Neural Network. For recent work see Graph Structure Learning with Interpretable Bayesian Neural Networks, which addresses learning graphs with uncertainty estimates. Link at the bottom.

&nbsp;


**Extension to Real Data**

As the underlying network topology is rarely ever observed, how do we evaluate whether our estimate of it (along with the corresponding uncertainty/calibration) is good in a real data setting? The only way I can think of is by using it to make downstream predictions on labels we do observe, i.e. marginalizing it out and evaluating the resulting posterior predictive.


&nbsp;


**Minor Comments**

In Eqn (1) and (2) it may make sense to place A \sim P^{\theta)_A above \hat{y} = f_{\psi}(x, A). This is more standard in the probabilistic community which often views this model as a data-generating process:  A must be sampled first before it can be used as an input for f.

&nbsp;

Graph Structure Learning with Interpretable Bayesian Neural Networks, https://openreview.net/forum?id=2noXK5KBbx

### Questions
Listed in my above comments, namely addressing motivation (if the downstream prediction is the same, why do we care at all about GSL producing high fidelity graph estimates?) and extensions to real data.

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
3

### Summary
This paper aims to calibrate the latent distribution of graphs for predicting outcomes of interacting entities. To this end, the paper considers a dissimilarity measure, which can be f-divergence, Stein variational gradients, or maximum mean discrepancy, between two predictive distributions. Then, the paper demonstrates that minimizing this measure ensures success of calibration under certain conditions where conventional point-wise approaches fail. For practical implementation, the dissimilarity measure is considered with maximum mean discrepancy computed over finite samples. The experiments focus on validating the proposed theorem.

### Strengths
- This paper first explores calibrating graph structure learning by minimizing the dissimilarity measure between two distributions.
- The theoretical analysis shows how the proposed method can be beneficial in cases, such as when  $f^{\ast} = f_{\psi}$, where the proposed method succeeds while conventional methods fail.
- The authors show that proposed method can be useful by incorporating variance reduction techniques and addressing the complexity.
- The experiments validate the theorems from several perspectives.

### Weaknesses
I have no concerns about the methods or their theorem. However, my overall concerns stem from the experiments.

- **Lack of baselines.** The experiments only provide the outputs of the proposed method and validate the theorem. However, they do not provide experiments for showing how conventional approaches fail in contrast, such as their shortcomings in estimating the underlying graph distribution. This limits the emphasis on the advantages of the proposed method.

- **Lack of benchmarks.** The experiments focus on synthetic benchmarks with limited scope, which limits highlighting the benefits of the proposed method. Are there no conventional benchmarks, such as node classification benchmarks, that could better highlight the benefits in practice?

- **Lack of uncertainty analysis.** In my understanding, the ultimate goal is to model output $y$ uncertainty by calibrating the latent distribution for graphs. However, the experiments lack analysis of the capability to model this uncertainty.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
(After reading the revised version, I increased my score from 5 to 6.)

This paper addresses the problem of jointly learning the latent adjacency matrix $A$ and a node inference task via a function $f(A, x)$. It considers a family of predictive models $P_{y|x}^{\theta, \psi}$, where one component learns the distribution $P(A)$ and another models the inference task $f$. The paper shows that optimizing a pointwise loss does not necessarily ensure proper learning of the distribution over $P(A)$. To address this, the authors propose a new loss formulation based on a distribution dissimilarity metric that guarantees learning both the latent graph structure and the inference function for the considered class of functions and settings. The methodology provides one example of how to optimize such a loss by choosing Maximum Mean Discrepancy (MMD) as the dissimilarity metric. The authors then develop a method to optimize the proposed MMD loss and provide empirical experiments to show that their approach successfully learns both the distribution $P(A)$ and the inference function $f$

### Strengths
1. The paper is well-structured and clearly written, with a logical flow that guides the reader through the problem, methodology, and results on the synthetic experiment.

2. The paper provides a comprehensive treatment of the problem, carefully addressing its assumptions and hypotheses.  It thoroughly discusses the implications and limitations of each assumption and hypothesis, and it empirically verifies what happens when the assumptions are violated. 

3. The proposed loss function is principled, built on a solid theoretical foundation.

### Weaknesses
1. Motivation. 
The motivation for the joint learning task is not clearly articulated. The paper’s main result highlights cases where successfully solving one task does not imply solving an unrelated task (i.e., learning the distribution of a latent random variable). However, the primary cited motivation for learning the graph distribution is to improve performance on a downstream task. If the downstream task can already be solved, it is unclear why learning the distribution over a latent graph would then be necessary. In summary, the authors should provide a practical setting where their proposed joint learning task and loss function would be called for.

2. Contribution. The paper's main theoretical contribution appears to be the observation that optimizing for task $X$ (achieving optimal point prediction) does not inherently lead to solving subtask $Y$ (learning the distribution over the latent adjacency matrix). This outcome is somewhat expected, given that the problem formulation lacks any dependencies linking subtask $Y$ to task $X$. A more specific formulation that establishes an explicit connection between the two tasks might provide a stronger foundation for the contribution.

3. Scope of the experiment. The experiments are limited to a small synthetic dataset with a small number of nodes ($N = 12$), a fixed feature dimension ($d = 4$), and fixed graph sparsity. The paper does include an experiment with more nodes ($N = 116$); however, the authors note that beyond this number, the number of free parameters becomes prohibitive. A more extensive empirical section showing how training with the proposed loss scales with the number of nodes, the feature dimension, and the graph sparsity (of the ground truth) would strengthen the presentation and provide more insight into the limits and applications of the proposed loss.

Relevant citations
Xingyue Pu, Tianyue Cao, Xiaoyun Zhang, Xiaowen Dong, and Siheng Chen. Learning to learn
graph topologies. In Advances in Neural Information Processing Systems, pages 4249–4262,
2021.
Ruoyu Li, Sheng Wang, Feiyun Zhu, and Junzhou Huang. Adaptive graph convolutional neural
networks. In Proceedings of the AAAI Conference on Artificial Intelligence, 2018.

Antonio Ortega, Pascal Frossard, Jelena Kovacevic, José MF Moura, and Pierre Vandergheynst. 
Graph signal processing: Overview, challenges, and applications. Proceedings of the IEEE,
106(5):808–828, 2018.

Minor
 
1. (68) typo 
2. (128) Missing end of sentence 
3. (275) typo substituhte

### Questions
1. Why is the problem of learning the distribution of a latent random variable (the adjacency matrix) relevant in cases where the inference task can be perfectly solved? Some settings where sampling the graph, evaluating edge probability or explainability should be put forward to better ground the contribution.

2. Where does $P_x*$ comes from? There is no discussion around $X$ being a random variable in the problem setting, and it's relation (if any) to $p(A)$. Currently, it may seems like $A$ and $X$ are assumed to be independent, which seems unlikely?

3. Why is there no baselines presented in the experiment section? For example, Anees Kazi et al. (2022) could have been presented to highlight the importance of the proposed joint learning formulation. 

4. Aren't most GNN architecture not injective and would violate the injective constraint from Theorem 5.2?

### Soundness
4

### Presentation
3

### Contribution
2
