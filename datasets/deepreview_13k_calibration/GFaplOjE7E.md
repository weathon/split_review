# On Choice of Loss Functions For Neural Control Barrier Certificates

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
The design of controllers with correctness guarantees is a primary concern for safety-critical control systems. 
A Control Barrier Certificate (CBC) is a real-valued function over the state space of the system that provides an inductive proof of the existence of a safe controller. 
Recently, neural networks have been successfully deployed for data-driven learning of control barrier certificates. 
These approaches encode the conditions for the existence of a CBC using a rectified linear unit (ReLU) loss function. 
The resulting encoding, while sound, tends to be conservative, which results in slower training and limits scalability to large, complex systems. 
Can altering the loss function alleviate some of the problems associated with ReLU loss and lead to faster learning?

This paper proposes a novel encoding with a Mean Squared Error (MSE) loss function, which allows for more scalable and efficient training, while addressing some of the theoretical limitations of previous methods. 
The proposed approach derives a validity condition based on Lipschitz continuity to formally characterize safety guarantees, eliminating the need for a post-hoc verification. 
The effectiveness of the proposed loss functions is demonstrated through six case studies curated from the existing state of the art.
Our results provide a compelling argument for exploring alternative loss function choices as a novel approach to optimizing the design of control barrier certificates.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors address the challenging problem of synthesizing a neural network controller and barrier certificate simultaneously which certifies safe behavior of the closed-loop system under unknown dynamics. The authors propose an MSE loss and validity condition which can practically achieve state-of-the-art performance in terms of training time and network parameter scalability over previous methods.

### Strengths
- The formulation is practical in the sense that it does not assume much structure at all about the dynamics and control other than they are in state-feedback and uses a weaker definition of CBC than previous papers by not requiring incremental decrease in the level sets.

- The algorithm and verification are technically sound and implementable given the required Lipschitz constants and lead to favorable results over existing approaches in their experimental settings of systems up to 6 dimensions.

### Weaknesses
 -The paper’s formulation and technical results are similar to that of Nejati 2023.

- The validity of the algorithm depends on obtaining valid upper-bounds for the Lipschitz constants L_x and L_u. This seems to be non-trivial unless they are known analytically.

- I don’t think the MSE loss is well-motivated as a contribution and there is not enough justification other than smoothness. Once a performance objective is added to the loss, the CBC MSE loss does not behave like a constraint and will compete with the performance in possibly undesirable ways (related to my questions below).

- The author’s claim that their method is more scalable to higher-dimensions. I will agree that it is scalable wrt to the network size, however I think there are significant scalability issues in state and control dimension in requiring an epsilon-net (Eq (6) on the state-space and and requiring sampled-based estimates for Lipschitz constants L_x and L_u. Often-times large networks aren’t required for direct state-feedback of 6-dimensional problems and more appropriate for perception-based controllers not currently supported by this framework.

### Questions
-I don’t totally understand the motivation of the MSE loss. The ReLU-type loss is meant to mimic a constraint and be active only when the constraint e.g. B(x) <= -\eta is not satisfied. However, it seems that MSE loss tends to push B(x) towards the boundary of the safe level set so that B(x) = -eta. It’s not clear how this will affect the overall landscape of the learned barrier function or why this is desirable besides smoothness of the loss. Typically a smooth performance objective is included in the loss anyways, which would end up competing adversarially with your CBC MSE loss.

- The control problem formulation is kind of strange to me. Algorithm 1 certainly trains a controller to avoid the unsafe region, but what is the controller trying to achieve otherwise? Shouldn’t there be some performance objective such as stability to a fixed point or reaching a terminal set? The setting in the paper would make more sense to me if we are already given a controller and want to learn a barrier function B to certify its behavior rather than learning one from scratch. If a performance objective is added to the algorithm, it might be hard to trade-off that additional loss with your MSE which is always going to be non-zero if B is a continuous function.

- Using spectral normalization to enforce the Lipschitz of B and k is quite conservative. Have you tried using more sophisticated Lipschitz parameterizations (see below)?

Pracht 2022: Almost-Orthogonal Layers for Efficient General-Purpose Lipschitz Networks
Wang 2023: Direct Parameterization of Lipschitz-Bounded Deep Networks

### Soundness
3

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
3

### Summary
This paper leverages a Mean Squared Error (MSE) loss function for constructing neural CBF and claims that their approach gives which more scalable and efficient training. The proposed approach uses Lipschitz continuity to provide safety guarantees. Numerical results are provided to justify the effectiveness of the proposed method.

### Strengths
1. This paper is quite original, and I haven't seen similar ideas before.

2. Numerical study on six different cases is definitely a plus.

3. The paper is written well, and the idea is quite simple and easy to follow.

4. The idea of using Lipschitz analysis to derive control barrier functions is interesting.

### Weaknesses
I am not sure how significant the result is. It seems that the authors use Lipschitz constant to guarantee stability. So the authors are using the spectral norm bounds for Lipschitz constants and then derive certificates based on that? I almost feel that the study is not that complete given the facts that there are so many results on Lipschitz networks which are completely ignored by this work. It seems that one can immediately strengthen the results in this paper by connecting the results to the large body of literature on Lipschitz networks. Some sampled results on Lipschitz networks are provided below, and there are actually many more papers.

Miyato et. al: Spectral normalization for generative adversarial networks. ICLR 2018.

Fazlyab et.al: Efficient and accurate estimation of lipschitz constants for deep neural networks. NeurIPS 2019

Li et. al. Preventing gradient attenuation in Lipschitz constrained convolutional networks. NeurIPS 2019.

Pauli et. al: Training robust neural networks using Lipschitz bounds. IEEE LCSS 2021.

Trockman, A. and Kolter, J. Z. Orthogonalizing convolutional layers with the Cayley transform. ICLR 2021.

Singla, S. and Feizi, S. Skew orthogonal convolutions. ICML 2021.

Meunier et.al: A dynamical system perspective for Lipschitz neural networks. ICML 2022

Xu et. al. Lot: Layer-wise orthogonal training on improving l2 certified robustness. NeurIPS 2022

Prach et. al. Almost-orthogonal layers for efficient general-purpose Lipschitz networks. ECCV 2022.

Araujo et al: A unified algebraic perspective on Lipschitz neural networks. ICLR 2023

Wang, R. and Manchester, I. Direct parameterization of lipschitz-bounded deep networks. ICML 2023.

Wang et al: On the scalability and memory efficiency of semidefinite programs for Lipschitz constant estimation of neural networks. ICLR 2024.

Pauli et. al: Novel quadratic constraints for extending LipSDP beyond slope-restricted activations. ICLR 2024.

Prach et. al: 1-Lipschitz Layers Compared: Memory Speed and Certifiable Robustness. CVPR 2024.


This paper almost completely ignores the large body literature on Lipschitz networks. It seems to me that the proposed approach can be significantly strengthened by connecting to these papers. It is also unclear to me whether the key to the improvement is the MSE loss or just the control of Lipschitz constants.

### Questions
1. Are the authors using the spectral norm bounds for Lipschitz constants and then derive certificates based on that? Have the authors considered more advanced methods for Lipschitz continuity?

2. Can the authors justify whether the MSE loss or the Lipschitz continuity lead to the improvements? Maybe some baselines that use advanced Lipschitz continuity properties without using MSE loss can be added for comparison?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
An important problem in control theory is to prove that a system can reach a desired condition while avoiding unsafe conditions.  This problem has been formulated using a variety of methods in the past, including constrained optimization, optimal control and dynamic games, and with the use of control Lyapunov and control barrier functions. The challenge in using control Lyapunov or control barrier functions is in the generation of the function itself:  generally these are hand-tuned functions inspired by the linearization of the system and the constraints, and can be hard to construct, and the result is often quite conservative.  Over the last decade, new methods for generating control Lyapunov and control barrier functions have been developed using neural networks.  The idea has been to use the dynamics model and the barrier function conditions to train a neural-network representation of the function and the resulting control policy.  Early work demonstrated that neural networks could learn these conditions, but failed to provide a proof over the state space of the system.  In more recent work, ReLU neural networks have been used to represent the barrier function, and a proof of its applicability over the state space generated by employing formal verification tools based on Satisfiability Modulo Theory (SMT) and the piecewise linear structure of the network.  The conditions for existence of a control barrier function are encoded in the ReLU loss function, and the proof of applicability of the state space can be slow to obtain through the training of this network, which suffers from the curse of dimensionality, resulting in scalability limitations.  

The current paper replaces the ReLU loss function in this last step with a mean squared error (MSE) loss function.  Lipschitz continuity conditions of the system and the neural networks implementing the control barrier function are then sufficient to prove the applicability of the control barrier function over the state space, removing the need for a formal verification procedure using SMT tools.  Dynamic system examples ranging from 2D to 6D demonstrate that this new loss function results in computation of a barrier function and resulting control law faster than previous methods.

### Strengths
The key idea here is a good one, and the paper builds on previous work to automate the generation of control barrier functions.  The new MSE-based loss function works better than the ReLU-based loss function featured in previous work, and the paper employs Lipschitz continuity assumptions to generate a proof that the barrier function can be used across a region of states, not just at the sample points used for training.  This speeds up the process because the formal verification used in the ReLU-based loss function work is not needed.
The benchmark examples are adopted from the previous work, and allow a direct comparison with previous work.

### Weaknesses
(1) The gridding of the state space into Lipschitz-constant-dependent neighborhoods of training points is a potential downside of this approach -- it seems that it could limit the scalability and remove some of the benefits of using a barrier function.  The authors should include a more detailed discussion of how the training scales with the dimension of the dynamic system, as the number of training points is exponential in this dimension.  Specifically, how does the required number of training points scale with the Lipschitz constant of the system dynamics and the neural network?  The paper should also address the practical implications of this exponential scaling, such as memory requirements and training time, for higher-dimensional systems.

(2) The presentation of the paper is quite poor.  First, the paper presents results using a discrete time control system, whereas the original work on which CBCs (Prajna) are based is presented for continuous systems.  This should be clarified and that the results carry over directly should be confirmed.  Second, the ReLU(.,.) and MSE(.,.) functions are not defined.  In Alg 1 L_{MSE} references L_i functions in equations (7)-(9) that do not exist.  Lipschitz continuity of neural networks is not defined.  There are small typos throughout the paper. The lack of precise definitions makes it difficult to assess the correctness of the proposed method. For example, the specific form of the loss function and how it relates to the barrier function conditions is not clearly laid out, and the reader must infer this from the text.  The paper should include a clear, self-contained description of the mathematical framework.

(3) There is not much physical intuition given in the paper:  why are the inverted pendula examples harder to verify?  Why is the inverted pendulum example not symmetric wrt theta and thetadot?  What is the dependence on the network architecture, and how were the specific architectures used in the examples chosen?   Also, these systems are small enough that there are analytically-determined barrier functions for at least some of them.  How do the computational results compare?  Finally, how is eta chosen, and is it decreased over the course of training?

### Questions
See questions in weaknesses above.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a Mean Squared Error (MSE)-based loss function for training Neural Control Barrier Certificates (NCBCs) to enhance safety-critical control. By reformulating CBC conditions with MSE, it achieves smoother gradients and better convergence, eliminating the need for post-hoc verification. Experiments confirm improved scalability, stability, and robustness in multiple control scenarios.

### Strengths
The MSE loss function allows for smoother gradients and faster convergence, which enhances scalability and enables the NCBCs to handle higher-dimensional systems and more complex neural network architectures.
By satisfying validity conditions through training, the MSE-based approach removes the need for further verification, simplifying the process and making it more computationally efficient.

### Weaknesses
1. The primary contribution is the replacement of the ReLU loss with Mean Squared Error (MSE) for smoother convergence in Neural Control Barrier Certificates (NCBCs). The novelty is low.
2. Algorithm 1 is very confusing and not well-written. B3 = B? What is B3 and why?
3. The presentation is poor. 
4. the algorithm relies heavily on Lipschitz constants (isn't that loose?)
5. the attached code only includes the pendulum examples.

### Questions
See weakness

Any intuition for Theorem 8? It's just math proofs there, and it's a bit hard for readers to digest.

The verification relies heavily on Lipschitz constants, the upper/lower bounds. From my experience, this Lipschitz bound is usually extremely loose, especially when the input region is not small. Did the authors encounter this issue? 

What do sections 5.3 and 5.4 mean? Is it to pick an inverted pendulum as an illustration example? 

The experiment settings in Section 5.2 miss many hyperparameters, the code only contains the pendulum examples.

### Soundness
3

### Presentation
2

### Contribution
2
