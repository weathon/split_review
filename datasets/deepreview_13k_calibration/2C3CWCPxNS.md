# Preconditioning for Physics-Informed Neural Networks

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
Physics-informed neural networks (PINNs) have shown promise in solving various partial differential equations (PDEs). However, training pathologies have negatively affected the convergence and prediction accuracy of PINNs, which further limits their practical applications. In this paper, we propose to use condition number as a metric to diagnose and mitigate the pathologies in PINNs. Inspired by classical numerical analysis, where the condition number measures sensitivity and stability, we highlight its pivotal role in the training dynamics of PINNs. We prove theorems to reveal how condition number is related to both the error control and convergence of PINNs. Subsequently, we present an algorithm that leverages preconditioning to improve the condition number. Evaluations of 18 PDE problems showcase the superior performance of our method. Significantly, in 7 of these problems, our method reduces errors by an order of magnitude. These empirical findings verify the critical role of the condition number in PINNs' training. The codes are included in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper defines the condition number as a metric for the difficulty and ill-posedness of the PINN training problem. The main argument is that the condition number is problem-dependent and almost algorithm-independent, therefore the problem must be alleviated by pre-codnitioning. They also support their theory with numerical examples on 16 PDE problems.

### Strengths
1. The idea and the theoretical standing of the paper is sound; the pre-conditioning of linear solvers has been studied for decades in numerical computation literature and is proven effective.

2. The suite of experiments does support the hypotheses made in the introduction under many difficulty conditions such as time-dependency, non-linearity, irregular geometry, discontinuity, etc.

3. The research and writing sequence is right; the work does start by defining and making the case for an underlying problem, showing that it exists in the first place, and then proposes a solution.

3. The implementation is made available and the work includes a detailed appendix.

### Weaknesses
1. The main turn-off of the work is its lack of scalability to higher-dimensional PDEs. One major part of the "complex problems" defined in Hao et al. (2022) is its high-dimensional PDE category, which seems left behind altogether in this work. The key advantage and promise of PINNs, compared to mesh-based/FEM/etc counter-parts, is their ability to generalize to higher-dimensional problems. This ability is unfortunately tainted by the need for the creation of a mesh in the proposed solution. On the second page, the authors make the assumption of d<=4 for the practicality of the proposed solution. This is a significant limitation of the work, and narrows its applicability to situations where FEMs can be expected to already be applicable. The reliance on mesh-based preconditioning inherently limits the method's advantage over traditional numerical solvers for higher-dimensional problems, where mesh generation becomes computationally expensive and memory-intensive. The authors should acknowledge that the proposed preconditioning method might not be suitable for problems with more than 4 dimensions, and that alternative preconditioning strategies should be explored for higher-dimensional problems.

2. Most of the experiments in the paper are done with 5 random seeds. This sample size is inadequate for reliable and significant conclusions. The statistical significance of the results is questionable with such a small number of trials, especially when dealing with stochastic optimization methods like those used in training PINNs. The variability in performance due to random initialization and training data sampling could be significant, and 5 trials may not be enough to capture this variability. This makes it difficult to draw strong conclusions about the effectiveness of the proposed preconditioning method. A more robust experimental design with at least 10-20 random trials would be more appropriate for establishing the statistical significance of the results.

3. The Poisson example in Figure 2a is overly simplistic. Since this is the basis for the paper, I wish the underlying problem was a bit more challenging and representative of the real-world problems than a 1-d Poisson problem. The 1D Poisson equation is a very basic linear problem and does not fully demonstrate the challenges that PINNs face in more complex scenarios, such as non-linear PDEs or PDEs with complex geometries. The condition number analysis might not be as insightful for such a simple problem, and the results might not generalize well to more complex PDEs. A more challenging example, such as a 2D or 3D Poisson equation with non-constant coefficients or a more complex boundary condition, would be more appropriate to demonstrate the practical relevance of the proposed condition number analysis.

### Questions
1. In Figure 1.a, why does the iterations axes start at 500? It looks like PCPINN is getting a head-start, which seems unfair to the other methods.

2. Figure 2b only shows 3 PDE problems of the Wave, Burgers, and the Helmholtz equations. Could the authors explain why more of the 16 considered problems were not included in this experiment?

3. Here are a few typos in the paper:

    * In the title of Section 3.2, "Condition" is misspelled as "Contion".

    * On Page 5, there is a minor grammatical error two lines under Equation 9: "closely enough" should better be replaced with "close enough".

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a way to alleviate the ill-conditioning of pinns training, proposing a metric to assess ill-conditioning. They provide theoretical results on the relationship between their metric and converge of the method, as well as numerical results illustrating how their approach behaves  on a PINN benchmark.

### Strengths
The paper is clear and reads well.

### Weaknesses
I have lots of concerns regarding the correctness and depth of the mathematical results.

First off, the 'condition number' you define looks nothing like a condition number. This is a well defined concept in the literature, it is not possible to define it however you like. Moreover, the supremum is taken on a dependant variable so it is not clear for me what is actually varying here.

The central theorem 3.6, which connects their 'condition number' to how the neural network approaches the solution looks nothing like a result one would obtain in the linear case. If one takes a look at the proof in the appendix, we can see how the condition number of the problem is artificially put in the theorem, making the theorem entirely vacuous. Not to mention the strenuous assumptions.

In section 4, "Training PINNs with a Preconditioner" they do not use a NN, $u$ just becomes a vector that is learned: no autograd, just finite differences, no neural networks. This formulation of the problem is very similar to finite elements, and using ILU preconditioning in this context is not new.

Eq 11. Have you simply replaced u_theta with the target u to obtain the result you were expecting? I could be wrong but i think this is a mistake.

Many more flaws in the paper, but this is already sufficient for me to advise for a clear rejection.

### Questions
I have no questions at the moment.

### Soundness
1 poor

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new way to spot and fix issues during the training of physics-informed neural networks (PINNs) using something called the condition number. The authors say that PINNs, which are deep learning models that use physical rules, can sometimes face problems. These problems might make the PINNs work less accurately or not learn well.

To solve these problems, the authors suggest a special algorithm. This algorithm uses the condition number from a specific matrix to make PINNs learn better and make fewer errors. In simple terms, they tweak the problem a bit using a matrix to make it easier for the PINN to handle. This tweak helps the PINNs learn faster and be more accurate.

The authors tested their new algorithm on 16 different problems, like some common equations. They also checked how their method stands against other top methods. Their results show that their new algorithm works better in terms of learning speed, accuracy, and how much computer power it needs.

Key points of the paper:

The authors present a new way to spot and fix issues in PINNs using the condition number.
They use a special algorithm that makes use of this condition number to help PINNs learn better.
They prove that their method works well by testing it on 16 problems and comparing it with other top methods.
In summary, this paper adds a lot to the understanding of physics-informed neural networks. It gives a new method that could make these networks work better in many different situations.

### Strengths
First, the authors describe the challenges that PINNs encounter. They note that even though PINNs are helpful for complex equations, there are hurdles that hinder their effectiveness. This discussion leads to their innovative solution for enhancing PINNs.

Then, they present their fresh approach. They employ the condition number from a specific matrix to assess the training of PINNs. This number is a known tool for gauging the reliability of systems. By adjusting the problem using a matrix, they enhance the performance of PINNs.

Finally, they evaluate their approach using 16 different mathematical problems. They compare their technique with other well-known methods. The outcomes indicate that their method is superior in several aspects. Furthermore, they offer detailed observations and visual representations to underscore the success of their approach.

### Weaknesses
1. Lack of thorough analysis of computational complexity and scalability of the preconditioning algorithm.
2. Insufficient comparison with other preconditioning methods in the literature.
3. Inadequate analysis of sensitivity to hyperparameters and initialization schemes.
4. Lack of theoretical analysis or empirical evidence to support the use of the condition number as a metric for diagnosing and rectifying training pathologies in PINNs.

### Questions
How does the condition number of the Jacobian matrix of the residual function help diagnose and rectify training pathologies in PINNs?

What is the significance of the proposed approach for solving complex partial differential equations (PDEs)?

 What are the implications of the proposed approach for computational efficiency and scalability?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the training of PINN is discussed from the perspective of the condition number. The condition number is a constant that is considered in the research area of numerical analysis and this number links the residual of the equation to the accuracy of the solution. The authors propose to employ this number to quantify the trainability of a problem. Also, the authors propose a method of preconditioning, which is a method to reduce the condition number for ill-conditioned problems.

### Strengths
This is probably the first paper to consider condition numbers for PINNs. The effects of the condition number on the error and the convergence of PINNs are theoretically investigated.

### Weaknesses
Condition numbers have long been studied in the field of numerical analysis. The most famous are those for systems of linear equations, but nonlinear equations in infinite dimensional space have also been considered (e.g., W. C. Rheinboldt, On Measures of Ill-Conditioning for Nonlinear Equations, Math. Comput., Vol. 30, pp. 104--111, 1976.) The formulation of PINNs is also a nonlinear equation in an infinite-dimensional space, so the novelty of this paper is questionable.

In addition, the proposed preconditioner is exactly the same as that for classical numerical methods. I suppose that if the proposed preconditioner is to be used, it would be better to use the classical numerical method instead of PINNs.

### Questions
1) PINN is said to perform worse than classical numerical methods when the problem under consideration is defined on a low-dimensional domain. Therefore, it is preferable to apply the proposed method to high-dimensional problems (e.g., 10-dimensional problems); however, when applied to high-dimensional problems, the proposed method is expected to be affected by the curse of dimensionality. Does the proposed preconditioner scale to such high-dimensional problems?

2) A preconditioner based on the domain decomposition method was proposed for PINNs [1]. What are the advantages of the proposed method compared to this method?

[1] Alena Kopaničáková, Hardik Kothari, George Em Karniadakis, Rolf Krause, Enhancing training of physics-informed neural networks using domain-decomposition based preconditioning strategies, arXiv:2306.17648

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
