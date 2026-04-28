# Physics Informed Neurally Constructed ODE Networks (PINeCONes)

- Decision: Reject
- Avg Score: 3.60
- Scores: 3, 3, 3, 6, 3

## Abstract
Recently, there has been a growing interest in using neural networks to approximate the solutions of partial differential equations (PDEs). Physics-informed neural networks (PINNs) have emerged as a promising framework for parameterizing PDE solutions using deep neural networks. However, PINNs often rely on memory-intensive optimizers to attain reasonable accuracy and can encounter training difficulties due to issues such as stiffness in the gradient flow of the loss. To address these challenges, we propose a novel network architecture that combines neural ordinary differential equations (ODEs) with physics-informed constraints in the loss function. In this approach, the dynamics within a neural ODE are expanded to include a system of ODEs whose solution provides the partial derivatives governing our PDE system. We call this architecture PINECONEs: physics-informed neurally constructed ODE networks. We evaluate the approach using simple but canonical PDEs from the literature to illustrate its potential. Our results show that training requires fewer iterations than previous approaches to achieve higher accuracy when using first-order optimization methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A physics-informed method is introduced to model the temporal progression of PDEs. It decomposes a given PDE into a system of ODEs to be solved with Neural ODE subsequently. In comparison to PINN, the introduced method learns to simulate simple one-dimensional (transport and Burger's equations) more accurately by using first-order optimizers.

### Strengths
_Originality:_ The idea of converting a PDE into a set of ODEs to be solved with Neural ODE seems appealing, but I could not undertand the difference between PINECONE and other methods mentioned under the third bullet point of the related work section.

_Quality:_ The claims are partially supported by experimental results. For example, the superiority of PINECONE over PINN is demonstrated in two experiments. Other claims, such as memory and time efficiency, however, do not find evidence.

_Clarity:_ The manuscript is decently written and organized but would benefit from a clearer framing. For example, it remained unclear to me, whether ANODEs find application here (why are they introduced so explicitly) and what some functions and variables are doing (see questions below).

_Significance:_ The results point into a good direction but need more evidence. In the current state, I do not see how PINECONE finds a wide application and whether it contributes novel insignts to the community.

### Weaknesses
1. Unclear whether PINECONE is more efficient in training time and memory consumption. In particular, the application of Neural ODE is quite costly. How does this scale in equations where many ODEs must be solved to find a solution for a PDE? The manuscript does not provide a clear analysis of the computational overhead introduced by the Neural ODE solver, particularly in comparison to the direct optimization of a neural network in PINNs. The claim of efficiency needs to be substantiated with empirical evidence, especially considering the known computational cost of solving ODEs numerically within the training loop.

2. Few experiments on rather simple problems do not seem to be sufficient to demonstrate the superiority of PINECONE over PINN. For example [[1]](https://proceedings.mlr.press/v162/karlbauer22a.html) provides many benchmarks and models, also comparing PINN, which might give a good source for more comparisons. The experiments are limited to one-dimensional transport and Burger's equations, which are relatively simple PDEs. A more comprehensive evaluation should include more complex, higher-dimensional problems, and potentially problems with different boundary conditions to demonstrate the robustness of the method. The lack of experiments on more challenging problems makes it difficult to assess the practical applicability of PINECONE.

3. How does PINECONE compare to state-of-the-art methods? As reported in the related work section, there have been proposed numerous (if not hundreds) of modifications to PINN. A demonstration of how these modifications are applied to PINECONE would be of high value to assess whether PINECONE is also superior to more sophisticated PINN variants. Particularly, comparing against Lee & Parish as well as Rackauckas et al. (2021), cited under the third bullet point in related work, would be essential. In the end, it is crucial to assess the quality of PINECONE, how it compares to other methods, and where it actually strugles. The manuscript does not explore how PINECONE performs against advanced PINN techniques, such as those incorporating adaptive activation functions or more sophisticated loss functions. Without such comparisons, it is hard to determine if the observed improvements are due to the core idea of PINECONE or if they can be achieved by simply using more advanced PINN training techniques. The lack of comparison against these methods makes it difficult to assess the true contribution of PINECONE.

4. How do PINN and PINECONE perform and compare when both optimized with LBFGS? Does PINECONE benefit similarly to PINN from second-order optimization? The manuscript only presents results using first-order optimizers. It is well-known that PINNs can benefit significantly from second-order optimizers like LBFGS. It is important to investigate whether PINECONE also benefits from such optimization techniques and how the performance compares to PINNs when both are optimized using the same second-order method.

### Questions
1. In the loss function at the bottom of page 2, what does $s$ stand for, is it the time step and if so, would you mind using $t$ for comprehensibility? Also, what are the arguments to ODESolve?
2. Is the first line in Equation (7) missing an equals 0? That is $\partial u/\partial t + c\partial u/\partial x = 0$?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper combines Neural ODEs with PINNs to solve PDEs (PINECONE). The average of the outputs of neural ODEs are taken as candidate functions for PINN solutions. PINECONE demonstrates significantly faster speed and lower error compared to the original PINN.

### Strengths
1) Originality: PINECONEs provide a continuous solution like PINN, but replace FNN with an ANODE, and store the partial derivatives as system variables.
2) Clarity: The paper is well-written and easy to follow.

### Weaknesses
1) The major weakness is the soundness of technical claims and experiments.

* No enough baselines. In Section 1.5, the authors mentioned that some related works apply NODE solvers to PDE. But none of them are compared in experiments. It is crucial to compare against these methods to demonstrate the specific advantages of PINECONE over existing NODE-based PDE solvers. Without these comparisons, it's difficult to assess the true novelty and effectiveness of the proposed approach.
* No proper dataset. In Section 1.4, it is claimed that PINECONEs are more suitable for real-world data and high-dimensional PDEs. However, all experiments are about low-dimensional synthetic data. The lack of experiments on real-world or high-dimensional problems undermines the claims made about the method's applicability and scalability. The experiments should include datasets that reflect the complexity and dimensionality that the authors claim their method is designed to handle.

2) The significance of the result is another weakness.

* The number of iterations may be not a practical and fair measure. PINECONEs need less iteration to converge than PINNs, but the CPU time needed for one iteration is apparently different for these two models. The computational cost per iteration for PINECONEs, due to the Neural ODE integration, is likely to be significantly higher than that of PINNs. Thus, comparing only the number of iterations is misleading. A comparison of total training time would be more appropriate.
* The constraint of using a first-order optimizer is not necessary for simple PDEs such as Burger's equation. The PINN with L-BFGS is able to achieve high accuracy within a few numbers of iterations and with moderate memory. The choice of a first-order optimizer limits the potential performance of PINNs, especially for problems where higher-order optimizers are known to be effective. The authors should have included results with higher-order optimizers for PINNs to provide a more complete comparison.
* The overall accuracy of PINECONEs may be not satisfactory even in Burger's equation (Fig 2, up-right). It seems that PINECONEs can not learn a shock wave. The inability of PINECONEs to accurately capture the shock wave in the Burger's equation raises concerns about the method's ability to handle solutions with sharp gradients or discontinuities. This limitation needs to be addressed with more detailed analysis and potentially modifications to the method.

3) A minor weakness is some typos

* A missing $\tau$ in the arguments of $F$ in the RHS of Eq(4).
* The large equation in Section 2 paragraph 3 is not numbered, and it is hard to read. The position of the second $=$ is misleading.

### Questions
See points 1 and 2 in the Weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel architecture, called PINECONE, that combines the neural ordinary differential equation (neural ODE) with the physics-informed neural network (PINN). The experiments present that the new model improves training performance compared to the standard PINN; the proposed model requires fewer iterations and yields more accurate solutions for the target equations.

### Strengths
To the best of my knowledge, this is the first work that tries to combine the neural ODE with the PINN. The new formulation that extends the given neural ODE system with additional differential equations yields an efficient evaluation of derivatives with respect to the input. These derivatives can be used to update the model parameters, i.e., train the model, with the PINN loss. The experiments demonstrate that the proposed model outperforms the standard PINN model. This will be another variant to improve PINN, particularly for dynamics.

### Weaknesses
Despite the nice performance improvement presented through the experiments, I find that only two cases are insufficient to validate the model. A more comprehensive evaluation would include a wider range of partial differential equations (PDEs) with varying complexities and boundary conditions. For instance, testing the model on higher-dimensional PDEs or those with non-linear terms would provide a more rigorous assessment of its capabilities and limitations.

Additionally, I find that the manuscripts need to be further clarified with more elaborate explanations about the proposed formulation and its verification. Specifically, the paper claims that the calculation of neural ODE’s sensitivity w.r.t. the input is memory-efficient with the proposed formulation. However, the connection between the extended PINECONE system and the adjoint sensitivity method is not adequately explained. A more detailed derivation showing how the additional solutions (i.e., the derivatives) are used for training the model, particularly in the context of the adjoint method, would significantly improve the clarity of the paper.

Furthermore, there seems to be a discrepancy in the reported results. Sec 3.1 states "The PINECONE reaches the minimum error of the PINN at around iteration 2,700." However, the graph shows that it’s around 1,200. 

For the Burgers’ equation example, the presented performance of PINN is very different from what the original PINN paper shows. The paper mentions using the first-order optimization method instead of L-BFGS. While this might be a valid choice, it raises concerns about the fairness of the comparison. A more thorough analysis would involve comparing the performance of both models under the same optimization settings to ensure a fair evaluation.

### Questions
The paper claims that the calculation of neural ODE’s sensitivity w.r.t. the input is memory-efficient with the proposed formulation. I find that this is an important contribution yet not crystal clear. I guess this may relate to the adjoint sensitivity method proposed by the original neural ODE. A more clarification would be helpful. It would be better to elaborate more on how to solve the extended PINECONE system and how the additional solutions (i.e., the derivatives) are used for training the model.

Sec 3.1 states "The PINECONE reaches the minimum error of the PINN at around iteration 2,700." However, the graph shows that it’s around 1,200. Am I misinterpreting the graph?

For the Burgers’ equation example, the presented performance of PINN is very different from what the original PINN paper shows. I believe that it is because the first-order optimization method was used instead of L-BFGS, which was used in the original one. I’m not sure if this is a fair comparison.

Will the PINECONE architecture be able to handle data-driven discovery tasks as PINN does?

As minor comments, the following typos could be corrected:
- LBFGs
- In Sec 1.2, "... described by a neural network Eq. (3))."
- In Eq. (7), "$\frac{\partial{u}}{\partial{t}} + c\frac{\partial{u}}{\partial{x}}$"
- In Eq. (8), "... $\|| u_\theta|_{t=0} - \sin \||^2_2$ ..."
- In Sec 3.2, "... lowered to 1e-4 after 2,5000 iterations, …"

### Soundness
2 fair

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
This research describes a network architecture that integrates the neural ordinary differential equation (ODE) and physics-informed constraint loss. They evaluate the framework using the transport equation and Burger's equation, showing fewer training iterations and higher accuracy than original Physic Informed Neural Networks (PINNs).

### Strengths
This paper proposes an interesting framework.

### Weaknesses
(1) there are no theoretical results. 

(2) experimental results are very limited. The baseline PINN is not implemented well. For example, vanilla PINN works fine for Burger’s equation without any issue within a small number of iterations. The authors should provide a more detailed analysis of the PINN implementation, including the specific choice of activation functions, initialization strategies, and the precise formulation of the loss function. The lack of these details makes it difficult to assess the validity of the comparison. Furthermore, the claim that vanilla PINNs struggle with Burger's equation is not universally true, and depends heavily on the implementation and optimization strategy. 

(3) experimental results are with the vanilla machine learning training method. Better optimization algorithms for PINN have been developed. For example, you should use [1] to see if the claims still hold with more practical PINN training methods. Because low-dimensional problems can be solved with traditional PDE solvers such as FEM, PINN is not suitable for the cases where the vanilla machine learning training method is sufficient. Therefore, you need to see if the proposed method still makes sense for practical training methods such as [1] that allow PINN to scale well for practical problems.

### Questions
(1) Please provide more supportive information for the sentence: “Hybrid modeling frameworks that incorporate neural networks into scientific modeling problems have yielded impressive results.”

(2) Please conduct experiments using SDGD proposed in "Tackling the Curse of Dimensionality with Physics-Informed Neural Networks"

(3) In the experimental result, the authors said both networks have the same number of layers and identical widths. Please provide detailed information on the network configuration.

(4) What are the relationships and benefits of your methods relative to other PINN models? There are several PINN models, such as Augmented Physics-Informed Neural Networks (APINNs) and Extended Physics-Informed Neural Networks (XPINNs). There is no need to compare them in your experiments. But, the authors should mention these versions of PINNs and how the proposed approach fits in the ecosystem of PINNs in the related work section or conclusion.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Physics Informed Neurally Constructed ODE Networks (PINECONEs), a pipeline to combine the Neural ODE family with physics-informed loss. The authors evaluate this framework on transport equations and Burger’s equations, compared with PINNs. The proposed method shows faster convergence and better accuracy when using first-order optimization methods.

### Strengths
- A framework is proposed by combining Neural ODE architectures and physics-informed loss. 
- This paper is easy to follow.

### Weaknesses
 - The idea is not novel. There are already many works investigating the potential of combining neural differential equations with physics-informed loss [1,2,3]. 

 - The baselines are not sufficient. The proposed method is only compared with standard PINNs. There are many variants of the PINN family, which show better performance [4,5,6]. To convince the readers, I think more baselines are expected.

 - The proposed method is only tested on 1D problems. There are many successful implementations of PINNs in 2D and 3D cases [4,5,6], but this paper only investigates 1D systems.

### Questions
Please see my concerns in **Weaknesses**.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
