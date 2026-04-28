# Denoising Diffusion Causal Discovery

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 3, 6, 6

## Abstract
A common theme across multiple disciplines of science is to understand the underlying dependencies between variables from observational data. Such dependencies are often modeled as Bayesian Network (BNs), which by definition are Directed Acyclic Graphs (DAGs). Recent advancements, such as NOTEARS and DAG-GNN, have focused on formulating continuous DAG constraints and learning DAGs via continuous optimization. However, these methods often have scalability issues and face challenges when applied to real world data. In this paper, we propose Denoising Diffusion Causal Discovery (DDCD), a new learning framework that leverages Denoising Diffusion Probabilistic Models (DDPMs) for causal structural learning. Using the denoising objective, our method allows the model to explore a wider range of noise in the data and effectively captures both linear and nonlinear dependencies. It also has reduced complexity and is more suitable for inference of larger networks. To accommodate potential feedback loops in biological networks, we propose a k-hop acyclicity constraint. Additionally, we suggest using fixed-size bootstrap sampling to ensure similar training performance across varying dataset sizes. Our experiments on synthetic data demonstrate that DDCD achieves consistent competitive performance compared to existing methods while noticeably reducing computation time.  We also show that DDCD can generate trustworthy networks from real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the causal discovery problem by reformulating it into a denoising diffusion process problem. It proposes three frameworks, the linear model, the nonlinear model, and the smooth model. Under the linear model, the authors show the equivalence of the denoising objective to the objective of the structural equation model. Furthermore, the author proposes the k-hop DAG constraints to enforce DAG structures within k-hops of the nodes. This method speeds up the computation by only checking the DAG of local neighbors. The paper compares the proposed method with several baselines including DAGs and the proposed method shows improvement in SHD score.

### Strengths
The scalability of the directed graph discovery procedure is an important and yet challenging problem. This paper addresses the issue by proposing a k-hopDAG constraint, which greatly reduces the computation time. 

The simulation results indicate that the proposed method works well under the nonlinear structure.

### Weaknesses
It is unclear why formulating the causal discovery problem as a diffusion process is needed and how it can make the estimation scalable. It seems that the major trick that can make the estimation procedure scalable is the k-hop DAG constraint, which reduces the algorithm's runtime. However, under the k-hop framework, the DAG structure is no longer guaranteed. It is not clear if a graph with cycles can be uniquely identified under this framework.

It is also concerning that the benefits of the diffusion process are not clearly demonstrated. While the authors claim it helps with optimization, there is no clear evidence of this. The experiments only show a small improvement in convergence speed, and it is not clear if the method converges to a better solution. The paper lacks a comparison of the quality of the graph recovery between the proposed method and a baseline without the diffusion process. This makes it difficult to assess the true impact of the diffusion process on the final results.

Furthermore, the k-hop DAG constraint, while potentially speeding up computation, introduces a significant limitation. The paper does not provide a theoretical analysis of the impact of this constraint on the final graph structure. The experiments show that the number of DAG violations can be reduced, but the scale of the x-axis in Figure 6 suggests that violations are still significant, especially for small k values. The paper lacks a rigorous argument for how generalizable the algorithm is, and there is no guarantee that the method will converge to a valid DAG in the worst-case scenario.

### Questions
a. It would be great to add more recent baselines, e.g., Bello et al., 2022; Deng et al., 2023, to the simulations.

b. It is not clear why Equation (13)-(14) is equivalent to Equation (4), as $Y$ has an additional term $E_1$.

c. In the experiment section, it states that the number of nodes ranging from 20 to 5000 are tested, but only results of 20 and 100 are reported. How does the method perform when the number of nodes increases beyond 100?'

d. The first term of  Equation (16) is 
$\|(X−f_2(f_1(X)W))+(Y_t−Y_tW)−diag(\sqrt{1−\bar\alpha_t})Z(I−W)\|_F^2$. I am a bit confused here. Why is it not the decomposition of two terms $\|(X−f_2(f_1(X)W))\|_F^2+\|(Y_t−Y_tW)−diag(\sqrt{1−\bar\alpha_t})Z(I−W)\|_F^2$?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposes a new Denoising Diffusion Causal Discovery (DDCD) framework that leverages Denoising Diffusion Probabilistic Models for causal discovery under additive noise setting.

### Strengths
- This work proposes a denoising optimization as effective as Notears [1].

### Weaknesses
 - There is also some similar work that used the diffusion model to learn causality under ANM [2]. What is the difference compared with it?
- This work seems only applicable in the Gaussian noise setting, can it be extended to the non-Guassian setting?
- Why the diffusion can help improve the causal discovery compared with the other Notears-based method. Can you offer some theoretical guarantee for it?
- Besides, whether will the nonlinear loss function (16) identify the true causal structure since it is just a combination of the linear loss of $Y$ and the nonlinear loss of $X$ without theoretical guarantee.
- The proposed "k-hop DAG constraint" aiming to replace the acyclic constraint seems to lack theoretical analysis and the result of real-world experiments does not appear to outperform the Regdiffusion.
- In lines 39-40, PC and LiNGAM are not Score-based approaches.

### Questions
See the weakness above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The study introduces the Denoising Diffusion Causal Discovery (DDCD) framework, which enhances causal structural learning by integrating denoising diffusion probabilistic models (DDPMs). DDCD captures both linear and nonlinear dependencies in causal structures. It employs a k-hop DAG constraint to preserve acyclicity while allowing feedback loops that are common in biological networks. Additional techniques like bootstrap sampling and gradient clipping improve scalability. 
The experiments tested DDCD on synthetic (scale-free and Erdős-Rényi) and real-world datasets (myocardial infarction complications and yeast gene networks). DDCD outperformed baseline models (e.g., NOTEARS, DAG-GNN) with lower structural Hamming distance and higher true positive rates, successfully identifying meaningful causal structures in both synthetic and real-world data.

### Strengths
The main strength of this paper is its seeming efficiency on large networks due to the fixed-size bootstrap sampling. The DDCD framework captures nonlinear relationships, making it effective for complex real-world applications on both simulated and biological data.

### Weaknesses
The inclusion of nonlinear denoising steps increases computational demand which can be exacerbated by the data-intensive need of a diffusion model. The performance could also be affected by fine-tuning needs of the diffusion-related parameters. This may not be trivial in practice. What would you recommend to identify the right hyperparameters? How do you define the threshold values and k-hop constraints to prevent overfitting in densely connected real-world networks?

### Questions
The questions stated above: 

What would you recommend to identify the right hyperparameters? 

How do you define the threshold values and k-hop constraints to prevent overfitting in densely connected real-world networks?

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
This paper proposes a novel method for causal discovery based on the principles of denoising diffusion. First, it demonstrates that the objective function of a linear Structural Equation Model (SEM) can be transformed into the form of a denoising diffusion model, thereby enabling causal discovery using this methodology. Next, the paper introduces an approach to nonlinear causal discovery by applying the denoising diffusion framework to intermediate variables that are nonlinearly transformed from the original variables. To address the issue of variable scale adjustment, the authors propose a method that smooths the process using the activation function of a Multilayer Perceptron (MLP). Additionally, they incorporate a modified version of the NOTEARS constraint - relaxed to a k-hop condition - into the denoising diffusion process, aiming to better approximate a Directed Acyclic Graph (DAG). Through experiments with synthetic data, the method demonstrates the ability to estimate causal graphs with high accuracy and efficient computation, outperforming traditional causal discovery methods that handle a large number of variables. The approach is further validated with real-world data, showing that it produces results consistent with domain knowledge.

### Strengths
The paper successfully presents a natural approach by transforming the objective function of SEM into the form of denoising diffusion. It further extends this concept to nonlinear causal discovery by naturally deriving a model similar to VAE. Moreover, the relaxation of the strict DAG constraint from NOTEARS to a k-hop DAG constraint is smoothly incorporated into the denoising diffusion model. Experimental results using synthetic data demonstrate that the proposed method outperforms traditional approaches in terms of both accuracy and computational efficiency. Additionally, experiments with real-world data further validate the effectiveness of the proposed method.

### Weaknesses
This paper is generally well-structured and easy to understand, and the proposed method shows great promise. However, there is room for improvement in the evaluation of the method. The most significant issue lies in the assessment of the DAG property. Since the proposed method introduces a relaxed k-hop DAG constraint rather than enforcing a strict DAG structure, a more careful evaluation is needed to understand how this relaxation impacts the DAG nature of the estimated causal graph. While the Structural Hamming Distance (SHD) between the estimated graph and the ground truth DAG is provided, this metric alone is insufficient to assess how well the DAG constraint is being maintained (or violated). Evaluating the number of loops that occur, for example, could provide more insight. Additionally, allowing loops might enable better handling of feedback loops in real-world data, so evaluating the DAG property in this context is crucial. Including such evaluations could greatly enhance the persuasiveness of the paper.

### Questions
Is it possible to provide a quantitative evaluation of how well the DAG constraint is maintained (or violated) in the synthetic data experiments?

### Soundness
3

### Presentation
4

### Contribution
4
