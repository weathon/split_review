# Neural Evolutionary Kernel Method: A Knowledge-Based Learning Architechture for Evolutionary PDEs

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Numerical solution of partial differential equations (PDEs) plays a vital role in various fields of science and engineering. In recent years, deep neural networks (DNNs) have emerged as a powerful tool for solving PDEs. DNN-based methods exploit the approximation capabilities of neural networks to obtain solutions to PDEs in general domains or high-dimensional spaces. However, many of these methods lack the use of mathematical prior knowledge, and DNN-based methods usually require a large number of sample points and parameters, making them computationally expensive and challenging to train. This paper aims to introduce a novel method named the Neural Evolutionary Kernel Method (NEKM) for solving a class of evolutionary PDEs through DNNs based kernels. By using operator splitting and boundary integral techniques, we propose particular neural network architectures which approximate evolutionary kernels of solutions and preserve structures of time-dependent PDEs. Mathematical prior knowledge are naturally built into these DNNs based kernels through convolutional representation with pre-trained Green functions, leading to serious reduction in the number of parameters in the NEKM and very efficient training processes. Experimental results demonstrate the efficiency and accuracy of the NEKM in solving heat equations and Allen-Cahn equations in complex domains and on manifolds, showcasing its promising potential for applications in data driven scientific computing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel approach called Neural Evolutionary Kernel Method (NEKM) for solving time-dependent semi-linear Partial Differential Equations (PDEs). The authors leverage a combination of operator splitting, boundary integral techniques, and Deep Neural Networks (DNNs) to construct evolutionary blocks that approximate solution operators. NEKM incorporates mathematical prior knowledge into each block, utilizing convolution operations and nonlinear activations tailored to the specific PDEs under consideration. This approach offers several noteworthy contributions:

1. **Efficiency and Generalizability**: The use of boundary integral techniques is a standout feature of NEKM, allowing for a reduced requirement of network parameters and sampling points. This not only improves training efficiency but also relaxes the regularity assumptions on solutions. The capacity to apply NEKM to problems in complex domains and on manifolds showcases its versatility and potential real-world applicability.

2. **Compatibility with Time Discretization Schemes**: NEKM can be effectively combined with time discretization schemes that possess structure-preserving properties, such as energy stability. This demonstrates the adaptability of the method to diverse mathematical contexts.

3. **Treatment of Singular Boundary Integrals**: The paper introduces a method for computing singular boundary integrals that arise from fundamental solutions. This addition contributes to the overall training efficiency and robustness of NEKM.

The empirical validation of NEKM is conducted through testing on heat equations and Allen-Cahn equations in complex domains and on manifolds. The results demonstrate the method's high accuracy and its capacity to generalize across various domains.

In summary, the paper presents an innovative and promising approach, NEKM, which addresses the solution of time-dependent semi-linear PDEs. The combination of mathematical prior knowledge, boundary integral techniques, and DNNs provides a compelling method that improves training efficiency, generalizability, and adaptability to different mathematical scenarios. The successful testing on various equations and domains underscores the method's potential significance in the field of mathematical modeling and scientific computing.

### Strengths
The strengths of the paper "Neural Evolutionary Kernel Method (NEKM) for Solving Time-Dependent Semi-Linear PDEs" include:

1. **Innovative Approach**: The paper introduces a novel approach, NEKM, which combines operator splitting, boundary integral techniques, and Deep Neural Networks (DNNs) to address the solution of time-dependent semi-linear Partial Differential Equations (PDEs). This innovation offers a fresh perspective on tackling complex mathematical problems.

2. **Efficiency Improvement**: NEKM leverages boundary integral techniques to reduce the need for extensive network parameters and sampling points. This not only enhances the efficiency of training but also relaxes regularity assumptions on solutions. This efficiency improvement is a significant advantage in solving real-world problems.

3. **Generalizability**: The paper demonstrates that NEKM can be applied to problems in complex domains and on manifolds, showcasing its generalizability across different mathematical contexts. This broad applicability enhances its potential usefulness in a wide range of scientific and engineering applications.

4. **Compatibility with Time Discretization Schemes**: NEKM's compatibility with time discretization schemes that possess structure-preserving properties, such as energy stability, is a valuable feature. This adaptability makes it easier to integrate NEKM into existing mathematical frameworks.

5. **Treatment of Singular Boundary Integrals**: The paper provides a method for computing singular boundary integrals that arise from fundamental solutions. This contribution adds to the method's efficiency and robustness, making it more practical for real-world applications.

6. **Empirical Validation**: The authors validate the NEKM approach through rigorous testing on heat equations and Allen-Cahn equations in complex domains and on manifolds. The high accuracy demonstrated in these tests underscores the practical utility of NEKM.

7. **Mathematical Rigor**: NEKM incorporates mathematical prior knowledge into its framework through convolution operations and nonlinear activations. This mathematical rigor ensures that the method is well-founded and theoretically sound.

8. **Interdisciplinary Relevance**: The paper's focus on solving complex mathematical problems with machine learning techniques has broad interdisciplinary relevance, as it can find applications in various fields, including physics, engineering, and computational science.

Overall, the strengths of the paper lie in its innovative approach, efficiency improvements, generalizability, compatibility with existing mathematical schemes, and the rigorous empirical validation of the proposed method. These qualities make NEKM a promising addition to the field of mathematical modeling and scientific computing.

### Weaknesses
While the paper on "Neural Evolutionary Kernel Method (NEKM) for Solving Time-Dependent Semi-Linear PDEs" offers several strengths, there are also some potential weaknesses to consider:

1.  **Complexity**: The proposed NEKM method, while innovative, is complex in its approach, involving the integration of operator splitting, boundary integral techniques, and Deep Neural Networks. This complexity might make it challenging for practitioners who are not well-versed in all of these areas to implement and understand. The reliance on both Green's functions and neural network approximations adds layers of abstraction that could hinder practical adoption.

2.  **Computational Resources**: The paper does not extensively discuss the computational resources required for training and applying the NEKM method. Deep learning methods often demand significant computational power, which could be a limitation for some users, particularly those without access to high-performance computing resources. The training of Green's functions, in particular, may introduce bottlenecks that are not clearly addressed.

3.  **Limited Real-World Use Cases**: While the paper demonstrates NEKM's effectiveness in solving specific mathematical problems, it remains largely theoretical. More real-world use cases and practical applications in various domains would strengthen the paper's relevance and utility. The current examples, while illustrative, do not fully demonstrate the method's applicability to complex engineering or scientific problems.

4.  **Interpretability**: The paper discusses the use of neural networks, which are often seen as "black-box" models. While the paper addresses some interpretability challenges, it might not provide a complete solution to the interpretability issues associated with deep learning approaches. The integration of mathematical knowledge, while beneficial, does not fully mitigate the challenge of understanding the inner workings of the neural network components.

5.  **Algorithm Complexity**: The proposed method involves a combination of different techniques, such as boundary integral representation and neural networks. This may make the implementation and understanding of NEKM challenging for some users, potentially limiting its widespread adoption. The need to handle singular boundary integrals also adds to the complexity of the implementation process.

6.  **Empirical Validation Scope**: While the paper includes empirical validation on heat and Allen-Cahn equations, the scope of the empirical validation might be limited. A more extensive range of test cases across different scientific and engineering domains would strengthen the method's generalizability. The current validation does not fully explore the method's performance across a wide variety of PDE types.

7.  **Scalability**: The paper does not explicitly address the scalability of the NEKM method. As the complexity of problems increases, it remains to be seen whether NEKM can efficiently scale to handle more complex and larger-scale scenarios. The computational cost associated with larger domains and longer time scales is not fully explored.

8. **Comparison to Existing Methods**: The paper lacks a comprehensive comparison of the NEKM method with existing approaches for solving similar problems. Such comparisons would help to better assess the relative strengths and weaknesses of NEKM. A more detailed analysis of how NEKM compares to methods like PINNs in terms of accuracy, computational cost, and ease of implementation is needed.

In conclusion, while the NEKM method offers several promising advantages, such as efficiency improvements and generalizability, it also has some potential limitations, including complexity, computational resource requirements, and the need for more extensive real-world applications and validation. These weaknesses should be considered when evaluating the method's suitability for specific applications.

### Questions
1. Can you provide more insight into the computational resources required for training and applying the NEKM method? What kind of hardware and software infrastructure is necessary for its practical implementation?

2. The NEKM method is quite complex, involving a combination of operator splitting, boundary integral techniques, and neural networks. How user-friendly and accessible is the implementation for researchers and practitioners who may not be experts in all these areas?

3. The paper mentions empirical validation on heat and Allen-Cahn equations. Are there plans to expand the empirical validation to a broader range of mathematical problems or real-world applications to further assess the generalizability of NEKM?

4. How does NEKM address the interpretability challenge often associated with deep learning methods? Can you provide more details on how NEKM helps users understand and trust its results, especially in cases where interpretability is critical?

5. The paper mentions combining NEKM with time discretization schemes that possess structure-preserving properties. Could you elaborate on specific scenarios or use cases where this combination has proven to be advantageous?

6. NEKM proposes the treatment of singular boundary integrals arising from fundamental solutions. Can you discuss the impact of this addition on the overall efficiency and robustness of the method in practical applications?

7. In the real world, problems often scale in complexity. How does NEKM address the scalability challenge, especially when dealing with larger and more complex scenarios beyond the examples provided in the paper?

8. The paper does not include a comprehensive comparison of NEKM with existing methods for solving similar problems. Could you share insights into how NEKM performs in comparison to other approaches, and in what scenarios it may have a comparative advantage?

9. Are there any specific plans or ongoing research aimed at addressing some of the potential weaknesses or limitations identified in the paper, such as making the method more accessible or broadening the scope of empirical validation?

10. How do you envision the practical adoption of NEKM in various scientific and engineering domains? Are there specific industries or areas where NEKM is expected to have a significant impact, and if so, what are the next steps for its real-world application?

These questions aim to seek further clarification and insights from the authors regarding the NEKM method and its potential applications and improvements.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to tackle solving partial differential equations (PDEs) traditionally solved by numerical methods with deep neural networks (DNNs). The authors address the challenges of solving PDEs with DNNs that a majority of these methods do not use any mathematical or physical parameters and require a large amount of parameters to tune. The authors propose the Neural Evolutionary Kernel Method (NEKM) to solve a type of evolutionary PDEs with DNN based kernels. The core idea is to incorporate pre-trained Green's functions. NEKM is an alternating two-step procedure that first analytically or numerically solves a nonlinear ODE to obtain a flow map and then numerically integrate the related linear PDE with a convolutional kernel.

### Strengths
- Nice abstract that motivates the need for PDEs in science and engineering problems and use of numerical methods to solve them.
- The paper and abstract are well-written.
- Incorporating ideas from numerical methods, e.g., Green's function, boundary conditions and energy stability is very nice. In particular, I like to the discussion in subsection 2.2 on energy conservation and would like more details in the Appendix.
- The generalization and use of the pre-trained Green's function is nice.
- The computational savings of defining the Green's function on the boundary rather than the interior domain is nice. For other boundary integral representations for conservation laws, see Hansen, et. al, "Learning physical models that can respect conservation laws", ICML 2023 (https://arxiv.org/abs/2302.11002).
- Nice high dimensional simulations in Figures 6-7.
- Generalizability to different manifolds and boundary conditions.

### Weaknesses
 - The authors should define earlier what they mean by evolutionary PDEs.
- Connection to other kernel operator methods such as the Fourier Neural Operator (FNO) should be considered. It is only briefly discussed in one sentence of related work with a majority on the PINNs literature. In particular, in the related works, the authors discuss in detail how boundary conditions are incorporated into Physics-Informed Neural Networks (PINNs). The related in Neural Operator community should be discussed, such as how to incorporated boundary conditions into Neural Operators in Saad et. al, "Guiding continuous operator learning through Physics-based boundary constraints", ICLR 2023.
- The method only works on semi-linear PDEs. This is actually a very strong assumption and limitation. The authors should discuss the extension to nonlinear PDEs. Specifically, how would the operator splitting approach extend to fully nonlinear equations where a closed-form solution for the nonlinear part is not available. 
- Evaluation: the method is only tested on the simple linear heat/diffusion equation and Allen-Cahn equations. The heat equation is smooth and parabolic and very easy for numerical methods to solve. It would be nice to test hyperbolic problems with shocks, e.g., in the GPME benchmarking framework in Hansen, et. al, "Learning physical models that can respect conservation laws", ICML 2023.
- The method seems to have strong limitations if the first step requires an analytical or numerical solution to the ODE. 
- In particular, the authors should clarify this in the last paragraph of the introduction. I don't understand where the nonlinear ODE is coming from in step 1 and then how there is "numerically integration" for the related linear PDE. Typically, in numerical methods a (non)linear PDE is first discretized in space and then the resulting semi-discrete form of the ODE is discretized in time. The authors should clarify what they mean here. It is unclear how the operator splitting is actually implemented and how the method handles the coupling of the linear and nonlinear parts, especially if the nonlinear part does not have a closed-form solution.
- I think some of the equation details of BINet in the related work should be moved to an appendix or background section.
- Care should be taken with the discretization because this adds a first order error into the scheme. For example, the first equation should not be discretized with the 1st order accurate Forward Euler without even citing the method. This is an explicit method and there are necessary bounds on $\Delta t$/$\tau$ to ensure numerical stability.  See Krishnapriyan et. al, "Learning continuous models for continuous physics", 2023 (https://arxiv.org/pdf/2202.08494.pdf) on how the time discretization matters in NeuralODE and the 4th order RK4 is advantageous but even that scheme without being careful about the numerics can lead to convergence issues. The authors should clarify the specific time discretization scheme used and justify why it is appropriate for the problem.
- Ideally the method and presentation wouldn't need to be separated into separate cases for linear equations or not.
- It seems like the method depends too strongly on the BINet method and the authors should better differentiate the novelty between the two.
- The exposition of the method in Section 2 isn't too clear and some of the details can be moved to an appendix.
- The unique features of the NEKM subsection seems like it could be incorporated with the contributions subsection in the intro.
- Label x and y axis in Figure 3.
- Another major weakness in the evaluation is just comparing to the exact solution and no other baseline methods, especially to related neural operator based methods.

### Questions
- Does the method only work on semi-linear PDEs? If so, this is a bit limiting and the authors should discuss the extension to nonlinear PDEs.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents the Neural Evolutionary Kernel Method (NEKM) for solving semi-linear time-dependent PDEs. NEKM distinguishes itself by utilizing operator splitting and boundary integration, enabling efficient network architectures. The method is demonstrated to be effective and stable in solving classic PDEs, such as the heat equation and the Allen-Cahn equation.

### Strengths
NEKM can be combined with time discretization schemes that preserve energy stability, which is crucial for modeling physical systems.
The method incorporates an evolutionary kernel, which inherently preserves the structure of the problem.

The method incorporates an evolutionary kernel, which inherently preserves the structure of the problem.

### Weaknesses
While NEKM is claimed to work in complex domains, the paper primarily provides examples in small and relatively simple domains. It would be beneficial to demonstrate its performance in more complex and realistic domains, similar to the level in the referenced paper (https://arxiv.org/pdf/2309.00583), including real-world scientific and engineering geometries.

The paper lacks references to related work that adopts neural networks only at the spatial level while using time discretizations to evolve spatial fields over time. Including references to papers like "Evolutional deep neural network (Physical Review E 2021)," "Implicit Neural Spatial Representations for Time-dependent PDEs (ICML 2023)," and "Neural Galerkin Scheme with Active Learning for High-Dimensional Evolution Equations" could help provide context and comparisons.

The paper does not provide information about the computational cost and scalability of NEKM compared to classical numerical methods, especially for larger 3D problems. It would be valuable to include performance comparisons in terms of computational efficiency.

### Questions
My biggest confusion and concern is the relationship between this paper (Lin et al., 2023a) as well as (Lin et al., 2023b). Those paper also use a convolution representation of the solutions using Green's functions. What exactly is the author's contribution except working with time-dependent problems?

The paper focuses on semi-linear PDEs, but it would be interesting to know if NEKM can be extended to handle nonlinear PDEs. Clarification on the limitations and potential extensions of the method for nonlinear problems would be beneficial.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a neural network-based algorithm, namely the Neural Evolutionary Kernal Method (NEKM), for solving evolutionary PDEs. The method involves the operator splitting technique and the idea of boundary integral network. Specifically, the method pre-trains a neural network representation of the Green function and then solves the evolutionary PDE by applying the Green function block and kernel function block alternatingly with an ODE solver. Experiments on the heat equation and Allen-Cahn equations are conducted to demonstrate the performance.

### Strengths
- The paper is well-written and easy-to-follow.
- The proposed method is interesting and mathematically grounded.
- Experimental results seem strong.

### Weaknesses
 - It seems the method heavily relies on the closed form formula of the fundamental solution $G_0$. The numerical error of the integration involving $G_0$ seems troublesome. Specifically, while asymptotic expansions and integration by parts are mentioned, the paper lacks a detailed analysis of how these techniques are applied to handle the singularity of $G_0$ in practice. The specific form of the asymptotic expansion used, the order of approximation, and the criteria for determining when to apply integration by parts are not discussed. This makes it difficult to assess the robustness of the method with respect to the numerical integration of the singular kernel. Furthermore, the method's reliance on a known fundamental solution limits its applicability to PDEs where such solutions are readily available.
- The experimental results of Allen-Cahn equation is not compared with the exact one or any other method. While the authors mention comparisons in the appendix, these are not directly presented in the main text, making it difficult to evaluate the method's performance against existing numerical techniques for this specific equation. The lack of a direct comparison with established methods, such as finite difference or finite element methods, makes it hard to gauge the relative advantages and disadvantages of the proposed approach.
- Some minor issues: Figure 12 is too small.

### Questions
- Now that the Green function $G$ is computed by pre-training a neural network, the error of this step may propagate to solving the time evolutionary PDE. Was this problem an issue in the experiments? How accurate should the numerically approximated Green function be so as not to affect the performance?
- As mentioned in the paper, the possible singularity of $G_0$ may demand special handling. But the form of $G$ is generally unknown. How can the singularity appearing in $G$ be dealt with?
- Energy stsability is claimed as one of the contributions. Is this only empirically observed or grounded with some particular design?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
