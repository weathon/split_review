# IO-LVM: Inverse optimization latent variable models with applications to inferring and explaining paths

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Learning representations from solutions of constrained optimization problems (COPs) with unknown cost functions is challenging, as models like (Variational) Autoencoders struggle to capture constraints to decode structured outputs. We propose an inverse optimization latent variable model (IO-LVM) that constructs a latent space of COP costs based on observed decisions, enabling the inference of feasible and meaningful solutions by reconstructing them with a COP solver. To achieve this, we leverage estimated gradients of a Fenchel-Young loss through a non-differentiable deterministic solver while shaping the embedding space. In contrast to established Inverse Optimization or Inverse Reinforcement Learning methods, which typically identify a single or context-conditioned cost function, we exploit the learned representation to capture underlying COP cost structures and identify solutions likely originating from different agents, each using distinct or slightly different cost functions when making decisions. Using both synthetic and actual ship routing data, we validate our approach through experiments on path planning problems using the Dijkstra algorithm, demonstrating the interpretability of the latent space and its effectiveness in path inference and path distribution reconstruction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work proposes a method titled inverse optimization latent variable model (IO-LVM). This latent-variable model can model the space of solutions of constrained optimization problems. The authors test the idea on ship routing data. Here, the model learns the latent space representing transition costs of different agents in the data. Then, COP solver provides paths based on the sampled transition costs.

### Strengths
- The results show that the learned latent space captures the space of paths well. IO-LVM captures nuances such as big ships not passing through Oresund Straight even when it's the shortest path purely based on the data.

### Weaknesses
 - This is not my area of expertise, so I may not be the best judge of it, but the paper was hard for me to understand.
- The experiments are done on problems with few dimensions. If I understand correctly, the latent learned latent space has only 2 or 3 dimensions. The method would be more convincing if there were experiments with more dimensions, e.g. discrete decision problems.
- The experiments are specific to paths generation. This objective is quite general, but in the experiments, the mapping from Y to X is essentially the shortest path finding algorithm.

###### writing
230 and 286: direct graph: should it be "directed" graph?

### Questions
1. Why do you think 2 or 3 dimensions is enough to capture the dimensionality of underlying cost functions? Is that because only 2 or 3 factors come into play in your examples, like 3 different agents in the synthetic paths setting, and size/weight of the ship in the real trajectories dataset?
2. Quantifying how well the model captures the ship width would be interesting. I'm curious whether you can learn a mapping from $z$ to the weight of the ship if that data is available.
3. What could be other applications of this method apart from paths sampling? Could this be applied to discrete decision problems from [Perturbed Optimizer paper](https://arxiv.org/pdf/2002.08676)?

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
3

### Summary
I found the rebuttal to be convincing, so I raised my score.  
---

-The paper’s central motivation is that VAEs (or generative models in general) will generate infeasible paths.  I don’t think this is really validated experimentally in the paper.  
  -While the proposed method is neat, it’s not clear to me that it justifies the substantial added complexity.  


notes from reading paper: 
  -Learning representations from solutions of constrained optimization problems (COPs) with unknown cost functions is challenging.  A VAE may fail to capture the constraints.  
  -Paper proposes inverse optimization latent variable model.  Latent space model of COP costs, which are then reconstructed via a COP solver.  Leverage gradients of a Fenchel-Young loss through deterministic solver.  
  -Synthetic and actual ship routing data.  Validate on Dijkstra path planning problems.  
  -Fenchel-Young loss is defined as gap between the score function and the score function under a regularized solution based on the score vector.  Using a linear cost function, we have a loss which is minimized only if the regularized solution and the given solution are the same.  
  -Map x to latent space z, then to unconstrained space y, then to constrained space x.

### Strengths
The problem of learning generative models of optimal paths is interesting.

### Weaknesses
-The paper’s central motivation is that VAEs (or generative models in general) will generate infeasible paths.  I don’t think this is really validated experimentally in the paper.  The authors claim that VAEs do not explicitly model constraints, but this is not a sufficient justification for the proposed method. The experiments should demonstrate empirically that VAEs fail to produce feasible paths in the specific problem settings considered. Without this, the motivation for the added complexity is weak.
  -While the proposed method is neat, it’s not clear to me that it justifies the substantial added complexity. The need to integrate a pre-defined planning algorithm, such as Dijkstra's, introduces a significant computational overhead and limits the applicability of the approach to problems where such algorithms are readily available and efficient. The authors should provide a more thorough analysis of the computational cost and scalability of their method compared to simpler alternatives.


### Questions
-Is it possible to use the algorithm to learn optimal trajectories even when trained on sub-optimal data?  I think this aspect could be interesting.

### Soundness
3

### Presentation
3

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
The paper proposes IO-LVM, a solution to constrained optimization problems (COPs) with unknown cost functions that leverages VAE and Fenchel-Young loss to learn an informative latent representation of graph paths. IO-LVM is evaluated on synthetic and real-world ship path datasets and can disentangle a dataset's factors of variations, denoising observed paths, and predicting optimal paths for unseen data.

### Strengths
- Training a neural generative model with COP solvers is to my knowledge novel and interesting.
- The paper shows that the trained VAE's latent embeddings capture meaningful details about the data-generating process, such as the agent index and ship width.
- The paper presents a comprehensive ablation and qualitative analysis of simple pathfinding problems.

### Weaknesses
 - The motivation behind the paper's research direction could be stated better. The introduction elaborates on IO-LVM's interesting capabilities in detail, but none of them are practically relevant in their current state. Further elaborating on how they can lead to effective solutions for real-world problems would make the paper stronger.
- The paper leans too heavily on qualitative analysis over quantitative analysis. Only one table of results compares against baselines, and IO-LVM's performance gain is only meaningful on the synthetic dataset's Spearman metric. It is also unclear what different Jensen-Shannon divergence values tell us about a model's predictive and reconstructive abilities. Having additional quantitative metrics, preferably interpretable ones, would be beneficial.
- The proposed experiments are relatively simple. Given that IO-LVM's latent space clusters agent ID variable significantly better for the simpler synthetic paths datasets compared to the ship width variable for the more complicated Ships dataset, I question whether IO-LVM will scale well to more complicated problems.

### Questions
- For the Ships dataset, why do you think having just two latent dimensions was sufficient? Is this related to the fact that the problem is fairly simple?
- Do you know of any other metric aside from Jensen-Shannon divergence and Spearman's rank correlation that can better highlight IO-LVM's advantage?
- What other problems aside from path explaining do you think IO-LVM can be applied to with small modifications?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces a novel approach called Inverse Optimization Latent Variable Model (IO-LVM), designed to learn interpretable latent representations of cost functions underlying constrained optimization problems (COPs) based on observed decisions, specifically in path-planning tasks. Traditional methods struggle with structured outputs or assume a single underlying cost function, limiting their ability to e.g. learn from multiple agents making decisions. IO-LVM overcomes this by using a low-dimensional latent space that captures varying cost structures, utilizing a Fenchel-Young loss and a COP solver for gradient estimation. This approach enables tasks like clustering paths, denoising, and path prediction for new start-target pairs, demonstrated on synthetic and real-world ship routing data. Overall, the model is rather interpretable and flexible, which makes it a robust tool for complex path inference and for understanding agent-specific behaviors in path planning.

### Strengths
- The preliminary section is clear and well-written.
- The method section is very well presented and easy to understand.
- The beta ablation (table 1) makes sense.

### Weaknesses
 - The coefficient $\beta$ is presented as "introduced" in this work to trade off the reconstruction of the data and how Gaussian the latent distribution is. In the original VAE paper [Kingma and Welling, 2014], this coefficient is indeed 1. To my knowledge, setting this coefficient to less than 1 is not new and is rather well-known in the VAE community because the encoder learning signal from the KL is much stronger than from the reconstruction loss. Examples include the beta-VAE paper [Higgins et al., 2017] that you also mentioned, and most VAE implementations (e.g. https://github.com/AntixK/PyTorch-VAE). It seems that introducing this coefficient as something new is an inaccuracy.
- Most figures from the experiment section are hard to interpret by someone who isn't familiar with the tasks used for demonstration.
- Comparison with baselines (especially PO) is hard to make sense of and does not seem very significant (table 2).

### Questions
1. As mentioned above, the comparison with baselines is hard to interpret. How significant are IO-LVM results compared to PO?
2. Are latent spaces always of dimension 2 in the paper? How has experimenting with higher dimensions looked? What is the conclusion of needing such low-dimensional spaces?

### Soundness
3

### Presentation
4

### Contribution
3
