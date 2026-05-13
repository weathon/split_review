# Accelerating Data Generation for Neural Operators via Krylov Subspace Recycling

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Learning neural operators for solving partial differential equations (PDEs) has attracted great attention due to its high inference efficiency.
However, training such operators requires generating a substantial amount of labeled data, i.e., PDE problems together with their solutions.
The data generation process is exceptionally time-consuming, as it involves solving numerous systems of linear equations to obtain numerical solutions to the PDEs.
Many existing methods solve these systems independently without considering their inherent similarities, resulting in extremely redundant computations.
To tackle this problem, we propose a novel method, namely \textbf{\underline{S}}orting \textbf{\underline{K}}rylov \textbf{\underline{R}}ecycling (\textbf{SKR}), to boost the efficiency of solving these systems, thus significantly accelerating data generation for neural operators training.
To the best of our knowledge, \modelname{} is the first attempt to address the time-consuming nature of data generation for learning neural operators.
The working horse of \modelname{} is Krylov subspace recycling, a powerful technique for solving a series of interrelated systems by leveraging their inherent similarities.
Specifically, \modelname{} employs a sorting algorithm to arrange these systems in a sequence, where adjacent systems exhibit high similarities.
Then it equips a solver with Krylov subspace recycling to solve the systems sequentially instead of \mbox{independently}, thus effectively enhancing the solving efficiency.
Both theoretical analysis and extensive experiments demonstrate that \modelname{} can significantly accelerate neural operator data generation, achieving a remarkable speedup of up to 13.9 times.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, authors proposed an iterative method called Sorting Krylov Recycling (SKR) to boost the efficiency of solving systems of linear equations, thus accelerating data generation for neural operators training. The proposed method leverages the power of Krylov subspace recycling and a sorting algorithm to arrange interrelated systems in a sequence, where adjacent systems exhibit high similarities. 
The effectiveness of the SKR method was demonstrated through both theoretical analysis and extensive experiments. The SKR performance was compared with other state-of-the-art methods, such as GMRES, and by considering the impact of different preconditioning techniques on the convergence rate and computational efficiency. The results indicate that SKR can deliver impressive acceleration, reducing the wall clock time by factor of up to 13.9 and requiring up to 30 times fewer iterations.

### Strengths
- Paper is well-written and overall easy to follow, with additional useful materials in appendices. 
- Extensive experiments and nice ablation studies to illustrate the impact of different components of the proposed algorithm
- The code and the reproducibility details are useful for other researchers to leverage the developments for their data driven PDE solvers, or benchmark their ongoing/future studies on related topics.

### Weaknesses
 - It would have been nice if authors provided more elaboration on the results for different types of PDEs, in particular for Poisson equation, for which the SKR and GMRES perform comparably to some extent. 
- In addition to time and iteration count, what about the numerical accuracy of their solvers w.r.t the grid resolution? Also, how can one interpret the slopes of plots indicating tolerance vs time and tolerance vs interations?

### Questions
- One general question for me was whether this approach can be used beyond neural operators, and can be used for any data driven PDE solvers? I did not quite understand the necessity of using NO to generate PDE, and it would be great if authors could elaborate on this.
- For many problems such as Poisson equation the resulting matrix, A, is symmetric and using iterative solvers for symmetric case (such as CG solver) could significantly help speed up the process. with that being said, could authors modify the algorithm by using symmetry property to make it perform better for symmetric matrices?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses a fundamental challenge in the training of Neural Operators (NOs) for solving Partial Differential Equations (PDEs) by introducing a novel algorithm called Sorting Krylov Recycling (SKR). The primary challenge is the time-consuming and computationally expensive process of generating labeled data for training NOs, which involves solving numerous systems of linear equations. The proposed SKR algorithm is designed to improve the efficiency of solving these systems and significantly accelerate data generation for NOs training.

### Strengths
Innovative Algorithm: The SKR algorithm is a novel and innovative approach to accelerate the generation of training data for NOs, focusing on the efficient resolution of linear systems. It addresses a fundamental challenge in the field of data-driven PDE solvers.

Efficiency Improvement: The paper demonstrates that SKR can achieve a remarkable speedup in the generation of training data, with a potential acceleration of up to 13.9 times. This significant efficiency improvement has the potential to reduce computational costs in the training of NOs.

Real-World Relevance: The need for efficient data generation for NOs is of practical importance, especially in scientific domains where PDEs play a crucial role, such as climate modeling, fluid dynamics, and electromagnetism.

### Weaknesses
Complexity: While SKR is a promising algorithm, the paper does not discuss its potential complexities or challenges in practical implementation. It is essential to evaluate the algorithm's feasibility and usability in real-world scenarios.

Application Scope: The paper primarily focuses on the problem of generating training data for NOs. It would be beneficial to discuss broader applications or scenarios where SKR could be applied beyond this specific context.

Generalization: The paper does not extensively discuss the generalizability of the SKR algorithm to different types of PDEs or scenarios. It is important to assess whether SKR is applicable in a wide range of PDE-related problems.

### Questions
Could you provide more details about the specific types of PDEs or problems where the SKR algorithm is expected to have the most significant impact in terms of efficiency improvement?

The paper mentions that SKR can achieve a remarkable speedup. Are there specific parameters or settings that are critical for achieving this speedup, and are there scenarios where the speedup might be less pronounced?

Have you considered potential challenges or limitations in implementing the SKR algorithm in practical applications, and are there strategies to address these challenges?

Beyond the context of generating training data for NOs, are there other domains or problems where SKR's approach of optimizing linear system solutions could be applied effectively?

How does the SKR algorithm handle variations in the complexity of PDEs, and does it exhibit consistent efficiency improvements across different levels of complexity?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method, SKR, to speed up the process of repeatedly solving a given PDE with different parameters (e.g. initial conditions, boundary conditions, right-hand side, etc.). This scenario arises when generating data to train neural operators, as this process effectively entails solving the same PDE multiple times with different input parameters. Solving a PDE often involves a potentially very large linear system, which can be solved using Krylov methods. SKR leverages the fact that the same PDE is solved across samples with different parameters to accelerate the data generation process, thanks to Krylov subspace recycling and a specific sorting algorithm.

### Strengths
This work addresses the important problem of data generation for NO training. The idea relies on the well-known Krylov subspace recycling method and, to the best of my knowledge, has not been previously proposed.

### Weaknesses
The paper does not discuss the aspect of parallelism, which raises concerns about the fairness of the benchmark. More specifically, in the traditional setting, PDE solves are independent of each other. Consequently, data generation can be achieved by splitting the PDE systems to solve across different MPI processes to reduce the cost and achieve faster data generation. However, in the SKR setting, the PDE solves are no longer independent, which undermines the claimed advantage of SKR over the classical approach. The lack of discussion regarding parallelization strategies, particularly in the context of large-scale data generation, is a significant oversight. The paper should explicitly address how the proposed method scales with increasing problem size and how it compares to standard parallel PDE solvers. Furthermore, the benchmark should include a comparison against a parallel implementation of the baseline GMRES method to provide a fair assessment of the proposed method's performance. The current evaluation appears to only consider a sequential implementation of the baseline, which is not representative of real-world usage in large-scale data generation scenarios.

### Questions
Is there a plan to add support for widely used PDE software such as Firedrake, FEniCS, etc.? This would enable data generation for neural operator training with just a few lines of code using SKR in high-level languages like FEniCS or Firedrake, enhancing the method's dissemination.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses lengthy workload required for generating data for neural operators, which are one class of typical machine learning models used as surrogate models for solving partial different equations. The key idea of the paper is the use of Krylov subspace recycling method, a technique for solving a series of interrelated systems. Together with the sorting algorithm based on inherent similarities, the proposed method greatly accelerates the data generation process.

### Strengths
The main advantage of the paper is an oriented way of generating dataset based on Krylov subspace recycling method, whose validity is supported by rigorous theoretical analysis. The paper reveals common features of (generating process of) NO datasets. The proposed method is evaluated with a wide range of its variants and the reduction in the computational cost is shown significant for most of the cases.

### Weaknesses
Although the reduction in the computational workload of SKR is significant, it is still not clear to me that SKR is a better choice as a generator for NO dataset, since the paper lacks evaluation of the dataset generated by SKR in the context of training NOs. One of my questions in this regard is:
How does the performance of NO instances (e.g. FNO, DeepONet) trained on datasets generated by SKR compare to those trained on their original datasets? 
Speaking from the practical aspect, it might be also beneficial for readers if the authors could give run-time comparison of SKR to parallelized solvers.

The presentation of the paper does not look clear to me. The followings are a couple of examples that made it difficult for me to understand the paper
* In Section 3.1 ”The data points for these PDEs in the parameter space of the NO inputs are relatively dense” : How did the authors withdraw this conclusion? Compared to what PDEs are the inputs dense?
* Table 5 (and its caption) is entirely confusing and hard to understand.
* Caption in Figure 9 “Specifically, when the parameters of the neural operator are closely matched in Helmholtz equations” : how do you compare the parameters of NO to Helmonltz equations?

### Questions
See the weeknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
