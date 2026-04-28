# ConFIG: Towards Conflict-free Training of Physics Informed Neural Networks

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
The loss functions of many learning problems contain multiple additive terms that can disagree and yield conflicting update directions. For Physics-Informed Neural Networks (PINNs), loss terms on initial/boundary conditions and physics equations are particularly interesting as they are well-established as highly difficult tasks. To improve learning the challenging multi-objective task posed by PINNs, we propose the ConFIG method, which provides conflict-free updates by ensuring a positive dot product between the final update and each loss-specific gradient. It also maintains consistent optimization rates for all loss terms and dynamically adjusts gradient magnitudes based on conflict levels. We additionally leverage momentum to accelerate optimizations by alternating the back-propagation of different loss terms. The proposed method is evaluated across a range of challenging PINN scenarios, consistently showing superior performance and runtime compared to baseline methods. We also test the proposed method in a classic multi-task benchmark, where the ConFIG method likewise exhibits a highly promising performance. Source code is available at \url{https://tum-pbs.io/ConFIG}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Motivated by the discrepancy between the residual and data loss terms in Physics-Informed Neural Networks (PINNs), the authors propose a "conflict-free" gradient update for multi-task learning, such that the resulting optimization direction minimizes all individual loss terms, avoiding local minima induced by one loss term. Such optimization step is calculated by ensuring positive cosine similarity between the update direction and the individual gradients of each loss term and (in most cases) a uniform decay rate for all losses. The authors also propose a momentum-based algorithm to alleviate the computational costs.

### Strengths
1.  The experiments thoroughly evaluate the proposed method from various aspects and for different problems.
    - The effectiveness (in terms of accuracy) of both ConFIG and Momentum(M)-ConFIG algorithms is demonstrated compared to other gradient adjustment methods, loss weighting methods for PINNs, and Adam.
    - While M-ConFIG falls short of the original ConFIG, its performance in computation-constrained scenarios is well shown.
2. The motivating problem from PINNs is a significant obstacle to wider adoption of them, and the proposed algorithm paves the way for their application to more problems in Physics.
3. The paper is well-written and accompanied by a reasonable amount of experiments, maths, and pseudo-code.

### Weaknesses
1. Although the experiments are already extensive, the paper can benefit from experiments with other PDEs (e.g. KS, Turbulence) and boundary conditions (e.g. Neumann) from the studied loss weighting baselines.

### Questions
NA

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel method (ConFIG) to deal with multi-task problems, and specifically focus on the task of training physics-informed neural networks (PINNs). The main motivation behind the method is that multiple loss functions in their formulation (PDE residuals, boundary / initial conditions) often conflict and lead to suboptimal optimizations. To overcome this limitations, ConFIG ensures that the update direction is conflict free by maintaining a positive-dot product between the final direction and the individual loss-specific gradients. Additionally, the paper introduces a momentum-based version (M-ConFIG) which reduces computational efficiency while maintaining training efficiency. The proposed method is contrasted against other loss aggregation schemes on several PDE problems and a multi-task learning benchmark, and demonstrates improved performance over existing methods.

### Strengths
- The paper addresses the important issue of conflicting directions in gradient updates in the training of PINNs. The proposed approach is novel and seems to combine the best of other MTL methods that have been applied in the context of PINNs such as PCGrad and IMTL-G. The proposed formulation seems well-formulated and is theoretically sound. Further, the introduction of M-ConFIG as a method to accelerate training while avoiding the evaluation of all the individual gradients at every step is a great practical contribution. Additionally, the appendices on this aspect are also thorough and discuss the reason as to why using Adam with ConFIG wouldn't work.

- The experiments also reveal a better performance than other baselines across different PDE benchmarks. Moreover, the method also performs well when applied to the standard MTL CelebA benchmark revealing broader applicability. The experiments also showed better convergence when compared against computational time of other optimization schemes further improving the applicability.

### Weaknesses
 - The experiments that are peformed in the paper compare against other MTL aggregation schemes for the proposed benchmark problems. However, there are several challenging benchmark problems for PINNs that have been established in other works (such as PirateNets (Wang et al.), PINNacle (Hao et al.),  Expert's Guide to PINNs (Wang et al.)). Although, they do use other enhancements such as an improved network architecture / improved encodings / imposing causality, it would be interesting to see if these enhancements would further improve on the current state of the art results.

- The hyperparameter tuning and ablation studies in the paper could be more extensive. For instance, the authors claim that the learning rate was fixed to $10^{-4}$ for the long-training or the use of a $10^{-3} \to 10^{-4}$ decay. But they don't seem to study the influence of this chosen rate on the final relative L2 error that has been obtained. It would strengthen the position of the paper to study this aspect as well.

### Questions
In addition to the points raised in weaknesses, it would be good if the authors can address the following:
- It seems like this approach has been primarily studied in the context of forward problems. Have you performed any studies on inverse problems as well?
- Additionally, I'm curious how the more recent pre-print of Jacobian Descent for Multi-Objective Optimization (Quinton & Rey) ties in, and compares against your work. Again, they compare against several MTL aggregators and propose a new strategy that claims to avoid conflicts with any of the individual gradients.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the challenge of gradient conflicts in Physics-Informed Neural Networks (PINNs) and the tendency of optimization to get stuck in the local minima of specific loss terms. The authors highlight that the gradient magnitude of PDE residuals typically dominates that of initial and boundary condition losses, leading to biased final updates. Their proposed ConFIG method leverages a momentum-based approach that reduces computational costs by alternating the backpropagation of loss-specific gradients, ensuring conflict-free updates and improved convergence.

### Strengths
- The optimization of different loss functions in PINNs is critical, as it can influence whether PINNs succeed or fail in solving forward problems. The exploration of Multi-Task Learning (MTL) strategies for improving PINNs training is innovative and may inspire future methodologies.
- The problem setup and method are clearly explained, making the paper accessible and informative. The theoretical background is well-supported by proofs and discussions.
- The experimental design is good, but it needs some adjustments.
- Given the difficulty of training PINNs due to conflicting gradient directions and numerical issues, the ConFIG method can be a good direction for solving these problems.

### Weaknesses
 - The examples explored in this study are relatively simple and can be solved with standard methods like Adam. It would be insightful to evaluate the proposed approach on more complex, chaotic PDEs, such as the Kuramoto-Sivashinsky equation, which poses significant challenges due to its non-linear and chaotic behavior. The lack of evaluation on such systems limits the assessment of the method's robustness and general applicability. Specifically, the paper does not explore scenarios where the chaotic nature of the solution might lead to highly variable gradients, which could expose limitations of the proposed method.
- The study omits comparisons with certain MTL strategies, such as FAMO, which could provide further context to the method’s effectiveness in PINNs. Additionally, using only the CelebA dataset to demonstrate performance in MTL may not be comprehensive enough. The absence of comparisons with other state-of-the-art MTL techniques makes it difficult to ascertain the relative advantages of the proposed method. Furthermore, the choice of CelebA dataset, which is image-based, might not be directly relevant to the challenges encountered in PINN training, which involves solving differential equations.

### Questions
In addition to what I mentioned in weaknesses, I would like to know how this type of models can be compared to traditional methods to improve PINN training typically involves adjusting the weights for PDE residuals and loss terms for initial and boundary conditions in terms of convergence and performance.

### Soundness
3

### Presentation
4

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
The paper introduces a novel method, ConFIG (Conflict-Free Inverse Gradients), aimed at addressing gradient conflicts that arise during the training of Physics-Informed Neural Networks (PINNs). The primary challenge in training PINNs lies in the conflicting gradient directions from multiple loss terms, particularly those associated with initial/boundary conditions and the physics equations, which can impede learning and optimization.  The paper proposes the ConFIG method, which ensures that the final update gradient has a positive dot product with each loss-specific gradient, eliminating conflicts and enabling consistent optimization across all loss terms. The method adjusts gradient magnitudes dynamically based on conflict levels and maintains uniform optimization rates for all loss terms. The method provides a robust and conflict-free optimization framework for PINNs, and its application extends to multi-task learning, showcasing improved performance over existing methods.

### Strengths
The paper makes a notable contribution to the field of PINN training by addressing a fundamental challenge with an original and technically sound approach.

Originality: The ConFIG method introduces a novel solution to gradient conflict resolution in PINNs. It effectively adapts ideas from multi-task learning (MTL) and continual learning (CL) to address gradient conflicts, which is relatively unexplored in the PINN domain.

Quality: The paper demonstrates strong technical quality with rigorous mathematical proofs and comprehensive experimental validation across multiple benchmark problems. While the method’s effectiveness is well-supported, additional comparisons with state-of-the-art methods and scalability analysis would further bolster its quality.

Clarity: The paper is generally well-organized and clear, though certain sections, particularly those with heavy mathematical notation, could be simplified for broader accessibility. 

Significance: The method addresses a critical challenge in PINN training, with broad implications for fields like fluid dynamics, electromagnetics, and beyond.

### Weaknesses
The paper would significantly increase its rigor and relevance by including more comprehensive comparisons, and the detailed comments are 
1. Limited Benchmarking: The evaluation is narrow, focusing on standard PDEs like Burgers equations, without addressing more complex, real-world PDE challenges (e.g., multi-scale phenomena, high-dimensionality). It would be helpful if the authors could broaden the evaluation to include more diverse and complex PDEs, as seen in benchmarks like PINNacle (Hao et al., 2024), to demonstrate the robustness of ConFIG across a wider range of problems.

2. Comparison with Advanced Methods: The paper primarily compares ConFIG to basic methods (e.g., PCGrad, IMTL-G), without considering recent, more sophisticated approaches in PINN optimization. The authors are expect to include comparisons with advanced methods.

3. Scalability and Efficiency: The scalability of ConFIG, especially regarding the computational cost is not fully explored. It would be better if the authors could provide a detailed analysis of runtime and memory efficiency, particularly for large-scale or high-dimensional problems, to validate ConFIG’s scalability.

4. Ablation and Sensitivity Studies: There’s a lack of ablation studies to assess the impact of key hyperparameters like learning rate and gradient scaling. The authors could perform more ablation studies to better understand the effect of different components and configurations on ConFIG’s performance.

### Questions
1. What is the computational complexity of the pseudoinverse operation in ConFIG, and how does it scale with larger problem sizes?

2. It would be better if the authors could test ConFIG on high-dimensional or multi-scale PDE problems, as seen in benchmarks like PINNacle? If so, how does it perform?

3. The authors are expected to provide more insight into how sensitive ConFIG is to hyperparameters like learning rate and batch size? 

4. The authors are expected to evaluat ConFIG’s scalability and efficiency for large-scale industrial applications.

### Soundness
3

### Presentation
3

### Contribution
3
