# Parameter Expanded Stochastic Gradient Markov Chain Monte Carlo

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Bayesian Neural Networks (BNNs) provide a promising framework for modeling predictive uncertainty and enhancing out-of-distribution robustness (OOD) by estimating the posterior distribution of network parameters. Stochastic Gradient Markov Chain Monte Carlo (SGMCMC) is one of the most powerful methods for scalable posterior sampling in BNNs, achieving efficiency by combining stochastic gradient descent with second-order Langevin dynamics. However, SGMCMC often suffers from limited sample diversity in practice, which affects uncertainty estimation and model performance. We propose a simple yet effective approach to enhance sample diversity in SGMCMC without the need for tempering or running multiple chains. Our approach reparameterizes the neural network by decomposing each of its weight matrices into a product of matrices, resulting in a sampling trajectory that better explores the target parameter space. This approach produces a more diverse set of samples, allowing faster mixing within the same computational budget. Notably, our sampler achieves these improvements without increasing the inference cost compared to the standard SGMCMC. Extensive experiments on image classification tasks, including OOD robustness, diversity, loss surface analyses, and a comparative study with Hamiltonian Monte Carlo, demonstrate the superiority of the proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new SGMCMC method using the idea of parameter expansion to improve the diversity of samples. Specifically, the weight and bias terms in neural networks are reparameterized using a sequence of matrix multiplication. The upper bound on the differences between two consecutive time steps is given. The experiments consider distribution shifts and of-distribution detection on CIFAR datasets.

### Strengths
- The paper studies an important problem in SGMCMC, which is to improve sample diversity.
- The method is simple and the algorithm is easy to implement in practice. 
- The empirical results show improvement over existing SGMCMC methods.

### Weaknesses
 - The main concern I have is the motivation of the proposed method. It is unclear why parameter expansion can solve the sample diversity issue. The paper did not explain the intuition and only explain it through Theorem 3.2. However, the theorem did not provide a convincing motivation either. Specifically, it's not clear how the implicit preconditioning achieved through parameter expansion differs fundamentally from simply using a larger step size, and why this specific form of preconditioning is beneficial for sample diversity.
- In Theorem 3.2, c and d have similar effects as the step size. I believe the values of c and d cannot be too large to achieve good convergence. If so, how is it different from using larger step sizes? Also, does Theorem 3.2 include the standard SGMCMC as a special case? In experiments, the authors use c=0,d=0 to refer to the standard SGMCMC, but the formulation in Eq.9 suggests c,d>=1. The theoretical analysis needs to clarify the relationship between the proposed method and standard SGMCMC, and the practical implications of the parameters c and d.
- Another main concern is that the required additional memory and computation will increase significantly. For an m by n W, we now will have c m by m and d n by n matrices, which at least increases O(c+d) costs. The paper needs to provide a more detailed analysis of the computational and memory overhead, especially in the context of large neural networks, and discuss strategies to mitigate these costs.
- In experiments, the proposed method did not compare with SGMCMC methods that aim to improve sample diversity, such as cyclical SGMCMC. It is crucial to compare against other state-of-the-art methods designed for improving sample diversity to properly evaluate the contribution of the proposed method.
- Fig 1 seems to show that EP can find modes but cannot converge to the target distribution, as the bottom left region seems to have more density. The paper should address this issue and provide a more detailed analysis of the convergence properties of the proposed method, especially in multi-modal distributions.
- Is the proposed parameter expansion implemented upon cyclical SGMCMC? This is because results in Fig 3 and 4 suggest so. Also, the authors use the cycle index in several figures. However, it is not explicitly mentioned anywhere in the paper whether PX-SGMCMC is built upon cSGMCMC. The paper needs to clearly state whether the proposed method is combined with cyclical SGMCMC and justify this choice.
- The empirical performance does not match typical benchmarks. E.g. err 29% on C100 where the neural network with the same architecture typically can achieve <20%. The paper should clarify why the reported performance is lower than typical benchmarks and discuss the limitations of the experimental setup.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors address the issue of limited sample diversity when using Stochastic Gradient Markov Chain Monte Carlo (SGMCMC) for posterior sampling in Bayseian Neural Networks (BNNs). They propose a novel expanded parametrization (EP) of neural networks that relies on a decomposition of the network weights for producing diverse sample weights. They provide theoretical and empirical validation of the proposed approach.

### Strengths
The paper is well structured and the writing is easy to follow. The approach is fairly practical, easy to adopt for general neural network architectures and circumvents the need for high compute resources associated with running multiple chains. Moreover, the theoretical analysis on the gradient flow of EP and the corresponding bound on distance between consecutive samples provides interesting insights on the relation between the induced network “depth”, maximum singular value of the matrices and exploration during sampling. The empirical evaluations clearly demonstrate the strength of the proposed approach for robustness to distribution shifts, ood performance and further validate the theoretical bound.

### Weaknesses
 * One of the weaknesses, as noted in the paper, is the additional overhead introduced by the EP. Since the sample diversity depends on the depth of the EP, this could potentially be prohibitive when dealing with large networks. Specifically, the expanded parameterization increases the number of parameters, which could lead to higher memory consumption and computational costs during sampling. This is especially concerning for very deep networks or those with a large number of channels, where the parameter increase could be substantial. The paper mentions that the parameter increase is less pronounced in convolutional networks, but it would be helpful to have a more detailed analysis of the overhead in different network architectures and sizes. 
* The authors note that one of the reasons why less principled deep ensembles perform better than SGMCMC is better sample diversity. It would be helpful to see how the proposed approach compares to deep ensembles.

### Questions
* Have the authors tried comparing the proposed method to one of the meta-learning approaches proposed for increasing sample diversity (Gong et al., 2019; Kim et al., 2024)?
* Do the authors have any ideas on modifying the EP design to address computational overhead? For instance, I’m curious to know if introducing low-rank constraints in these matrices significantly impact the results?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose an approach to enhance sample diversity in SGMCMC for Bayesian neural networks.  Their approach is based on decomposing the weight matrices of each BNN layer into a product matrices.  They provide theoretical justification for this approach by showing that the euclidean distance between consecutive samples depends on the number of matrices used in the product construction.  They validate their approach on toy data and several classification tasks.  their results show empirical correspondence to the derived theorem, and show their method helps to provide robustness to distribution shifts, can enhance OOD detection and increase sample diversity.

### Strengths
the paper is clearly written and easy to read.  it is impressive that the authors provide theoretical justification for their proposed parameter expanded SGMCMC by showing that the expected euclidean distance between parameters is bounded above by a quantity depending on the depth of the weight matrix parameterization.  

the authors provide a few variants of EP for different architectures showing that it can be extended beyond linear layers in theory and in practice (as justified by their latter experiments).  they provide extensive experimental/empirical results that show their proposed parameterization can enhance sampling quality in BNNs.  they examine several properties like robustness to distribution shift, out of distribution detection, and show their method also provides improvements even when data augmentation is used.  the number of experiments and their coverage of standard questions readers/researchers might be interested in is both comprehensive and extensive.

### Weaknesses
in section 3, it might be useful to hold the reader’s hand more and expand on lines 168-174 in a way that makes statements about the preconditioning aspect more precise and perhaps easier to visually parse.  for example i am not sure what was meant by the preconditioning producing `extraordinary directions of gradient steps.’

the authors remark about increased parameter counts during training, but it might be helpful to see wallclock times as well as burn in times.  maybe it is possible that drawing single samples is slower, but the enhanced training dynamics lead to a smaller burn in period, which could be another plus for the parameter expanded neural network layers if that difference were sufficiently large.

I am confused about the variables introduced in Eq.11 — in particular, it could be helpful to see how they relate to $r$ for the langevin dynamics of the classic unaltered network.

while fig.2 shows that the maximum singular value increases while the minimum singular value decreases, how does the condition number change?

### Questions
I am confused about the variables introduced in Eq.11 — in particular, it could be helpful to see how they relate to $r$ for the langevin dynamics of the classic unaltered network.

while fig.2 shows that the maximum singular value increases while the minimum singular value decreases, how does the condition number change?

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
In this paper, the authors studied sampling strategy used in Bayesian Neural Networks (BNNs), and proposed a new approach to enhance sampling diversity in stochastic gradient Markov chain Monte Carlo (SGMCMC). which is one of the most commonly used sampling methods in BNNs. Their proposed approach , known as PX-SGMCMC, can better explore the target parameter space by decomposing the weight matrices int o a produce of matrices. While doing this decomposition, their approach does not increase sampling cost compared against the original SGMCMC. They evaluated PX-SGMCMC on image data, and show that  PX-SGMCMC can indeed achieve more diverse samples, leading to outperformance in uncertainty characterization and robustness.

### Strengths
In general, this paper is well-structured and the writing is in good quality. It's great that the authors provided detailed mah derivations for their approach, and to my best knowledge, the proof is sound. 
In term of originality, because sample diversity can significantly influence the methods such as SGMCMC, I believe the idea from this paper is well motivated. And the authors provided comprehensive evaluations on multiple image datasets and it is impressive that the PX-SGMCMC can achieve better sample diversity.

### Weaknesses
The main concern is how this work is distinguished from the prior work on SGMCMC. Because there are many prior methods (such as the cited work in the Related Work section), I would hope to better understand their unique contributions to this topic. Specifically, while the paper motivates the need for improved sample diversity, it does not clearly articulate how the proposed parameter expansion method fundamentally differs from existing techniques that also aim to enhance exploration in the parameter space. For example, methods that meta-learn the diffusion and curl matrices, or those that employ cyclical step size schedules, also target improved exploration. The paper needs to more clearly delineate the specific mechanism by which the proposed method achieves this, and why this mechanism is novel compared to the existing literature. It is not sufficient to simply state that the method modifies the parameterization; a deeper explanation of the implications of this modification on the sampling dynamics is needed. Furthermore, the paper should discuss the potential limitations of the proposed method, such as the increased memory cost, especially for deep networks, and how this cost scales with network size and depth. A more thorough analysis of the computational trade-offs is required to fully assess the practical applicability of the method.

### Questions
1. How to interpret the different colors shown as the distribution modes? It shows a color scale but I don't know what the values indicate.
2. What do the authors think are the possible ways of reducing the computational costs for PX-SGMCMC? The answer does not have to be concrete, it just will be interesting to know conceptually how to optimize the cost in this case.

### Soundness
3

### Presentation
3

### Contribution
2
