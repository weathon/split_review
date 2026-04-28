# Graph Neural Preconditioners for Iterative Solutions of Sparse Linear Systems

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
Preconditioning is at the heart of iterative solutions of large, sparse linear systems of equations in scientific disciplines. Several algebraic approaches, which access no information beyond the matrix itself, are widely studied and used, but ill-conditioned matrices remain very challenging. We take a machine learning approach and propose using graph neural networks as a general-purpose preconditioner. They show attractive performance for many problems and can be used when the mainstream preconditioners perform poorly. Empirical evaluation on over 800 matrices suggests that the construction time of these graph neural preconditioners (GNPs) is more predictable and can be much shorter than that of other widely used ones, such as ILU and AMG, while the execution time is faster than using a Krylov method as the preconditioner, such as in inner-outer GMRES. GNPs have a strong potential for solving large-scale, challenging algebraic problems arising from not only partial differential equations, but also economics, statistics, graph, and optimization, to name a few.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Authors propose use Graph Neural Network (GNN) as a general-purpose preconditioner. They offer a convergence analysis for flexible GMRES. A new effective training data generation is proposed to training GNN. They develop a scale-equivariant GNN as the preconditioner. A novel evaluation protocol proposed by authors is being for general-purpose preconditioners.

### Strengths
* Authors pay their attention to the problem which is linked to using neural networks (in particular, GNN) as the preconditioner. In this sense, the preconditioner is a nonlinear operator and, using a standard preconditioned solver with this preconditioner is not correct. In this case, the convergence theory is broken. They concentrate on flexible GMRES and present an original convergence analysis. 
* Authors propose original scheme of data generation. Suggested sampling is linked with eigen-subspace of the $\mathbf{A}$.
* Of course, the idea of using GNN as the preconditioner is not novel. Authors offer a fresh approach to normalize $\mathbf{A}$. This prevents the potential division-by-zero issue that can arise in the standard normalization of GCN. The major innovation of the architecture is its scale-equivariance, i.e. the input space of the neural network is restricted.
* Proposed architecture is checked on the SuiteSparse matrix collection https://sparse.tamu.edu (square, real-valued 867 matrices (not spd-matrices) from 50 application areas, whose count of non-zero elements is less than 2M. To compare with classical methods such as ILU, AMG, and GMRES author propose two novel metrics.

### Weaknesses
 * Authors use $\ell_1$ residual norm as the training loss. Is it possible to use $\ell_2$ norm or others as the training loss?
* Authors compare their architecture with classical methods(GNP, ILU, AMG, Jacobi, and GMREs). It will be good to compare their approach and metrics with the existing general-purpose preconditioners which are used GNN as the preconditioner. See for example, https://proceedings.mlr.press/v202/li23e/li23e.pdf, https://arxiv.org/pdf/2405.15557.
* Are there exist some constraints to use this approach for SPD-matrices?
* Why is not the full GitHub repository made available for review?
* Why do the authors only assume the ground truth solution $\mathbf{x} = 1$?

### Questions
See weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a novel approach using Graph Neural Networks (GNNs) as general-purpose preconditioners for solving large, sparse linear systems. The authors present an empirical evaluation of their method, showing that it outperforms traditional preconditioning techniques like ILU and AMG in terms of construction time and execution efficiency, especially for ill-conditioned matrices. The method is tested on a diverse set of over 800 matrices, suggesting significant advantages in robustness and performance compared to existing methods.

### Strengths
- **Innovative Approach:** The use of GNNs as preconditioners is a fresh perspective that leverages recent advancements in machine learning.

- **Empirical Validation:** The extensive evaluation on a wide range of matrices provides strong evidence of the proposed method's effectiveness across various problem domains.

- **Robustness:** The proposed method demonstrates high robustness with a low failure rate compared to traditional preconditioners, particularly in handling ill-conditioned problems.

- **Theoretical Contributions:** The paper includes a convergence analysis for the flexible GMRES method, which adds valuable theoretical insights to the practical implementation.

### Weaknesses
 - **Scalability Concerns:** While the paper demonstrates robustness, it lacks a thorough analysis of scalability, particularly concerning the computational cost and memory requirements of GNNs when applied to significantly larger matrices. The paper does not discuss how the GNN architecture and training process scale with increasing matrix dimensions, which is critical for practical application to large-scale problems. Specifically, the paper should address the growth in computational complexity and memory footprint as the size of the matrix increases, and how this impacts the feasibility of the proposed method for very large sparse systems. It is unclear if the GNN's performance will degrade with larger matrices, and what the practical limitations are in terms of matrix size.

- **Dependence on Training Data:** The effectiveness of the GNN-based preconditioner appears to be highly dependent on the training data's quality and diversity. The paper does not sufficiently explore the potential impact of biases or limitations in the training data on the generalization performance of the GNN. For instance, it is not clear how the GNN would perform if the training data does not adequately represent the characteristics of the matrix being preconditioned. The paper should include a more detailed analysis of the training data generation process and its influence on the GNN's performance, including the potential for overfitting or underfitting due to specific training data distributions.

- **Limited Theoretical Foundation:** Although the empirical results are promising, the theoretical grounding of the proposed method could be strengthened. While the paper includes a convergence analysis for the flexible GMRES method, it does not provide a comprehensive theoretical analysis of the GNN's ability to approximate an effective preconditioner. Specifically, the paper lacks a theoretical justification for why the proposed GNN architecture is suitable for learning preconditioners, and how the learned preconditioner relates to the optimal preconditioner. Further theoretical analysis is needed to understand the convergence properties of the proposed method under various conditions, and to establish bounds on the approximation error.

### Questions
1. How does the proposed preconditioner handle matrices outside the tested conditions, particularly in real-world applications?

2. Could you elaborate on the training data generation process? How might biases in the training set affect the performance of the GNN?

3. What are the implications of your findings for future research in preconditioning techniques, especially concerning adapting the GNN for a wider array of problems?

### Soundness
3

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
3

### Summary
This paper proposes a GNN-based approach to preconditioning Krylov solvers, offering a novel alternative to traditional algebraic preconditioners. Unlike conventional methods, the GNN-based preconditioner (GNP) approximates the matrix inverse without relying on additional information, making it adaptable and robust across a wide range of matrices. GNP demonstrates predictable training costs, good robustness, and, in some cases, faster convergence than traditional preconditioners like ILU and AMG, which are often hampered by unpredictable construction times and structural limitations.
The contributions:
1. Convergence analysis for FGMRES, a widely used but theoretically underexplored method.  
2. New approach to training the neural preconditioner, focusing on effective training data generation by sampling from the bottom eigensubspace of  A to enhance training performance. 
3. Scale-equivariant GNN to serve as the preconditioner, addressing the challenge of varying input scales in the training data by enforcing an inductive bias that maintains scale-equivariance. 
4. Novel evaluation protocol to test the preconditioner broadly, evaluating across over 800 matrices from 50 diverse application areas in the SuiteSparse collection.

### Strengths
1. Introduces a GNN-based preconditioner (GNP) as a novel, general-purpose alternative to traditional methods, approximating the matrix inverse without additional problem-specific information.
2. Offers stable and consistent training times, unlike traditional preconditioners with unpredictable construction times due to matrix irregularities.
3. Contributes a convergence analysis for FGMRES.
4. Tests GNP on over 800 matrices from 50 application areas.

### Weaknesses
Sometimes both Iter-AUC and Time-AUC do not give good "weight" for the final residual accuracy. A method that reaches a lower final residual can be underrepresented if it converges more gradually, while a method with fast early convergence but a higher final residual might appear more favorable. This is a critical limitation, especially when the absolute accuracy of the solution is paramount. The AUC metrics, by their nature, prioritize the area under the convergence curve, which can obscure the importance of achieving a specific, low residual. For instance, a method that quickly reduces the residual to a moderate level but then plateaus might score higher than a method that converges more slowly but ultimately reaches a much lower residual, even though the latter is more desirable in many practical applications. This can lead to misleading conclusions about the effectiveness of different preconditioning strategies.



### Questions
1. Since neither Iter-AUC nor Time-AUC specifically prioritizes the final residual accuracy, have you considered including a metric that directly measures the final residual? For applications where achieving a specific residual threshold is crucial, this could provide a more balanced evaluation. If not, what are your thoughts on this?
2. Iter-AUC and Time-AUC capture different aspects of convergence (iteration efficiency and time efficiency, respectively). In cases where these metrics might conflict (e.g., one method scores well on Iter-AUC but poorly on Time-AUC), how would you recommend interpreting the results?

### Soundness
2

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
The authors focus on the task of preconditioning linear systems which remains one of the most important problems in scientific computing and applied maths. The authors use a machine learning approach and propose using graph neural networks as a general-purpose preconditioner.

### Strengths
- Preconditioning is a relevant problem and discovering new preconditioners for novel applications is resource-demanding
- The paper tackles a large number of test matrices and compares with SOTA black box preconditioners

### Weaknesses
 - The authors state their result as probably novel. Have they not found anything similar in the literature? I would like them to discuss the difference to the work USING FGMRES TO OBTAIN BACKWARD STABILITY IN MIXED PRECISION by Arioli and Duff, which they have done in the revised version.
- I am not a fan of presenting the results as best performer but it could be that the other methods are really close and this method only outperforms slightly and is terrible for the other problems. I would like to see actual  numbers or convergence plots.

- For the training data generation at the beginning of 2.2, is this really meaningful? You cannot sample the whole of $\mathbb{R}^n$ to run the problem forwards as also given possible ill-conditioning of $A$ approximating the inverse is difficult. Is this the reason the authors then switch to Arnoldi? This is the basis for many Krylov solvers and it is not clear what the advantage of the machine learning approach his if we have to do Arnoldi anyways?
- How about the sharpness of the Gershgorin estimates? These are not necessarily sharp.
- Do the authors really observe convergence of GMRES in 10 iterations to $10^{-6}$?
- AMG works better for symmetric problems, for nonsymmetric matrices PyAMG comes with better approaches for nonsymmetric problems such as the AIR approach.

### Questions
- For the training data generation at the beginning of 2.2, is this really meaningful? You cannot sample the whole of $\mathbb{R}^n$ to run the problem forwards as also given possible ill-conditioning of $A$ approximating the inverse is difficult. Is this the reason the authors then switch to Arnoldi? This is the basis for many Krylov solvers and it is not clear what the advantage of the machine learning approach his if we have to do Arnoldi anyways?
- How about the sharpness of the Gershgorin estimates? These are not necessarily sharp.
- Do the authors really observe convergence of GMRES in 10 iterations to $10^{-6}$?
- AMG works better for symmetric problems, for nonsymmetric matrices PyAMG comes with better approaches for nonsymmetric problems such as the AIR approach.

### Soundness
3

### Presentation
3

### Contribution
2
