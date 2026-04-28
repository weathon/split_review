# Backpropagation-free training of neural PDE solvers for time-dependent problems

- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 6, 6, 5, 6

## Abstract
Approximating solutions to time-dependent Partial Differential Equations (PDEs) is one of the most important problems in computational science. Neural PDE solvers have shown promise recently because they are mesh-free and easy to implement. However, backpropagation-based training often leads to poor approximation accuracy and long training time. In particular, capturing high-frequency temporal dynamics and solving over long time spans pose significant challenges. To address these, we present an approach to training neural PDE solvers without backpropagation by integrating two key ideas: separation of space and time variables and random sampling of weights and biases of the hidden layers. We reformulate the PDE as an Ordinary Differential Equation (ODE) using a neural network ansatz, construct neural basis functions only in the spatial domain, and solve the ODE leveraging classical ODE solvers from scientific computing. We demonstrate that our backpropagation-free algorithm outperforms the iterative, gradient-based optimization of physics-informed neural networks with respect to training time and accuracy, often by 1 to 5 orders of magnitude using different complicated PDEs characterized by high-frequency temporal dynamics, long time span, complex spatial domain, non-linearities, shocks, and high dimensionality.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose training neural PDE solvers by variable separation and random sampling of neural network weights. The neural network ansatz is utilized for the spatial domain, and the system evolving in time is solved by classical ODE solvers. Extreme learning machines and adaptive sampling techniques (SWIM) are applied for better training efficiency. An SVD layer is introduced to improve the condition number of the associated ODE. It is claimed that the proposed method outperforms PINN by 1 to 5 orders of magnitude in time efficiency and accuracy, for PDEs including Advection, Euler-Bernoulli, Nonlinear diffusion, and Burgers'.

### Strengths
- The writing is clear and detailed.
- The experiments are rich in problem types, specific difficulties, and baseline comparisons.

### Weaknesses
 - Meaning no offense, but I think researchers in AI4PDE with more AI background will think of this work as a huge step backward. The essence of deep neural networks is their surprisingly good performance in approximating high-dimensional functions, and the efficiency of backpropagation in implementing neural networks with huge amounts of parameters. Surely there are still issues even if we can obtain the gradients cheaply, but zeroth-order optimization, according to my personal judgment, cannot be the solution because it will only scale poorly.
- For the experiments, the spatial dimension is 1 or 2, and small in range. It would be interesting to see some results for problems huge in space.

### Questions
I hope to confirm with the authors that if you claim supremacy in any metric of the proposed method compared to traditional FEM solvers?

### Soundness
2

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
4

### Summary
The authors present a method of solving PDEs by parameterizing solutions fields with neural networks whose parameters depend on time. The integration scheme solves for the last layer cofficents. The basis functions, induced by the inner parameters, are generated via a data driven or data agnostic way.

### Strengths
- The presentation is clear and the literature review is thorough and provides a good introduction.
- The method shows strong performance on the chosen benchmarks

### Weaknesses
 - The paper should consider add more backgrounds about the random-sampling methods of neural network weights. Without back-propagation, how does this random-sampling of weights influence the final solution of the proposed method? As can be seen in Table 2, the standard deviations of your proposed method is relatively larger than PINNs, although the accuracy is significantly better. Specifically, it is unclear how the distribution of the randomly sampled weights affects the stability and convergence of the solution. A more detailed analysis of the weight sampling strategy, including the specific distributions used and their impact on the final solution, is needed. For example, do different distributions (e.g., uniform, Gaussian) lead to different solution characteristics, and how does the variance of the chosen distribution influence the observed standard deviations in the results?
- The paper should add some ablation studies to provide more insight about each component of the proposed method. For example, the necessity of the SVD layer, the influence of number of hidden neurons. It is not clear if the SVD layer is crucial for the method's performance or if it primarily serves to improve the condition number of the ODE system. Furthermore, the paper lacks an investigation into the impact of the number of hidden neurons on the accuracy and computational cost. A systematic study varying the number of hidden neurons and evaluating the corresponding performance would be beneficial. This should also include an analysis of the computational cost associated with increasing the number of hidden neurons.
- It would add more practicabillity of the proposed method by providing more detailed comparisons between ELM-ODE and SWIM-ODE. Is one strategy better than another, or one should choose between these two strategies based on the PDE to tackle? The current paper does not provide clear guidance on when to use ELM-ODE versus SWIM-ODE. A comparative study that highlights the strengths and weaknesses of each approach, perhaps in the context of different types of PDEs (e.g., linear vs. nonlinear, parabolic vs. hyperbolic), would be valuable. It is also unclear whether one method is more computationally efficient or robust than the other.

### Questions
What is the n-width of the problems considered (as given by the spectral decay of the snapshot matrix)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a method for training neural PDE solvers without backpropagation, which aims to improve efficiency in solving time-dependent partial differential equations (PDEs). The authors integrate two main ideas: separating space and time variables and randomly sampling weights and biases in hidden layers. By reformulating the PDE as an ordinary differential equation (ODE) using neural networks for spatial components, they leverage traditional ODE solvers for time evolution. The approach is benchmarked against standard backpropagation-based Physics-Informed Neural Networks (PINNs). It shows improvements in accuracy and speed on complex PDEs involving non-linearities, high-frequency temporal dynamics, and shocks.

### Strengths
1. The authors propose a backpropagation-free method that leverages random sampling techniques like Extreme Learning Machines (ELM) and Sampling Where It Matters (SWIM) to address the inefficiencies of traditional backpropagation, especially for complex time-dependent PDEs.

2. The paper reports significant speed gains in training time, with improvements of up to 5 orders of magnitude over standard PINN approaches.

3. Specialized handling of boundary conditions and separation of variables for time-dependent PDEs are some of the contributions that could impact future neural PDE solvers.

4. The authors demonstrate extensive benchmarking across a range of PDEs with different challenges, showing superior performance in terms of speed and accuracy.

5. The paper is well-written and easy to follow.

### Weaknesses
The authors have mentioned the limitations of their method and share possible directions to follow in future work.

### Questions
Could the authors clarify the absence of experiments involving higher-dimensional PDEs? Given the introduction’s emphasis on the limitations of mesh-based methods—particularly their impracticality in complex domains and high-dimensional spaces—it would be valuable to see examples where the proposed method effectively addresses these challenges. Higher-dimensional cases are particularly relevant to machine learning applications, where scalability in complex domains is critical.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a backpropagation-free training algorithm for a neural partial differential equation solver, utilizing the Extreme Learning Machine (ELM) framework. The method reformulates the partial differential equation (PDE) as an ordinary differential equation (ODE) problem through the separation of variables, which is then solved using classical ODE solvers. Numerical experiments show that the proposed method outperforms traditional PINNs in both test accuracy and training speed.

### Strengths
- Significantly lower relative error compared to PINNs
- Substantially faster training speed than PINNs
- Achieves both improvements without backpropagation while retaining a mesh-free approach

### Weaknesses
- The experiments are insufficient to fully support the authors' claims.
- The paper lacks theoretical contributions.
- The proposed method has a limited range of applications, which restricts its overall contribution.

### Questions
1. Experiments.
- The boundary conditions are approximated using a boundary-compliant layer. For instance, in the case of periodic BC, the authors approximate $\sin(kx)$ and $\cos(kx)$ by applying a linear transformation to the basis function. However, this raises the question: what advantage does the proposed method offer compared to just using $\sin(kx)$ and $\cos(kx)$ as basis functions, or P1, P2 basis functions in FEM? A numerical comparison in this scenario would be helpful.
- It appears that $C(t)$ is calculated by multiplying the pseudo inverse of feature matrix $[\Phi(X),1]$, where $X$ contains all the collocation points. In cases of high dimensionality $d>>1$ where $N>>1$ to cover the entire domain, there may be significant computational demands. Further discussion and experiments on the computational cost in high-dimensional settings would be needed.

2. Theoretical contributions
- Does ELM possess a universal approximation property? If so, can this be generalized to the neural PDE solver setting?

3. Limited applications
- As the authors mention, the method cannot be applied to grey-box or inverse problem settings. Given this, what advantage does the mesh-free nature provide?
- If the pseudo-inverse calculation for $[\Phi(X),1]$ becomes computationally expensive, especially in high-dimensional problems, what practical benefit does mesh-free implementation offer?
- Overall, what advantages does the proposed method offer over mesh-based approaches? In many cases presented in the paper, mesh-based methods achieve superior test accuracy with shorter training(computing) times.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to use a hybrid framework consisting of a neural network ansatz and a classical ODE solver to solve typical time-dependent PDEs. Specifically, the neural network ansatz features separation of spatial and temporal variables, and the parameters of this network is randomly sampled rather than trained with back propagation. Numerical experiments are conducted to verify the high accuracy and reduced training time of the proposed method.

### Strengths
- The proposed method is novel and provides a distinct method to solve time-dependent PDEs other than classical numerical methods and PINNs.
- The experiment results show that te proposed method outperforms PINNs by orders of magnitude of accuracy; the accuracy is even comparable to classical numerical solvers.
- The authors also provide techniques to satisfy boundary conditions and improve the condition number of the associated ODE.

### Weaknesses
- The paper should consider add more backgrounds about the random-sampling methods of neural network weights. Without back-propagation, how does this random-sampling of weights influence the final solution of the proposed method? As can be seen in Table 2, the standard deviations of your proposed method is relatively larger than PINNs, although the accuracy is significantly better. 
- The paper should add some ablation studies to provide more insight about each component of the proposed method. For example, the necessity of the SVD layer, the influence of number of hidden neurons.
- It would add more practicabillity of the proposed method by providing more detailed comparisons between ELM-ODE and SWIM-ODE. Is one strategy better than another, or one should choose between these two strategies based on the PDE to tackle?

### Questions
Is the proposed method able to handle PDEs with higher-order time derivatives?

### Soundness
3

### Presentation
3

### Contribution
3
