# MgNO: Efficient Parameterization of Linear Operators via Multigrid

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
In this work, we propose a concise neural operator architecture for operator learning. Drawing an analogy with a conventional fully connected neural network, we define the neural operator as follows: the output of the $i$-th neuron in a nonlinear operator layer is defined by $\mathcal O_i(u) = \sigma\left( \sum_j \mathcal W_{ij} u + \mathcal B_{ij}\right)$. Here, $\mathcal W_{ij}$ denotes the bounded linear operator connecting $j$-th input neuron to $i$-th output neuron, and the bias $\mathcal B_{ij}$ takes the form of a function rather than a scalar. Given its new universal approximation property, the efficient parameterization of the bounded linear operators between two neurons (Banach spaces) plays a critical role. As a result, we introduce MgNO, utilizing multigrid structures to parameterize these linear operators between neurons.  This approach offers both mathematical rigor and practical expressivity. Additionally, MgNO obviates the need for conventional lifting and projecting operators typically required in previous neural operators. Moreover, it seamlessly accommodates diverse boundary conditions. Our empirical observations reveal that MgNO exhibits superior ease of training compared to CNN-based models, while also displaying a reduced susceptibility to overfitting when contrasted with spectral-type neural operators. We demonstrate the efficiency and accuracy of our method with consistently state-of-the-art performance on different types of partial differential equations (PDEs).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new neural network architecture based on analogies between convnets and the multigrid method (these analogies have been previously identified with an architecture called MgNet). The authors prove a universality theorem for a network whose neurons are operators and use this theorem to motivate a neural operator which is a deep network with neurons being (elliptic) operators implemented via multigrid. Numerical experiments show competitive performance against existing neural operator architectures.

### Strengths
- The paper is very clearly written, the ideas are solid and the numerics are strong. I like the spirit of an architecture where neurons become operators: this appears very natural and the right thing to do.

- Using a multigrid (or in general multiscale) representation of operators is also the right thing to do. Similar ideas go back to efficient wavelet approximations of operators of Beylkin, Coifman, and Rokhlin. It is nice to see this done explicitly and clearly it yields strong performance.

- The experiments are very well executed.

### Weaknesses
 - Many of the ideas might have already been present in MgNet; it would be nice to see a comment.

- It is not clear to me what (9) is stating since you don't state the typical values of c. How should we use / interpret (9)?

- The motivation via exact encoding of boundary conditions is sound but I would also say quite easy to implement with other neural operators. For example the FNO by default works on the torus but via zero padding could be easily adapted to Neumann or Dirichlet boundaries (though not as easily as MgNO).

### Questions
- Why is there no comparison with FNO in Figure 7 (Helmholtz)? It might be nice to compare / combine with https://arxiv.org/pdf/2301.11509
- The sentence "Regarding our training setup, we adopted a meticulous approach." is strange.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a concise neural operator architecture designed for operator learning. This architecture draws inspiration from a conventional fully connected neural network, with each neuron in a nonlinear operator layer being determined by a bounded linear operator connecting input and output neurons, in addition to a function-based bias term. To address the efficient parameterization of these bounded linear operators within the architecture, the authors introduce MgNO (Multigrid Neural Operator). MgNO utilizes multigrid structures to effectively model and approximate these linear operators, eliminating the need for conventional lifting and projecting operators while accommodating diverse boundary conditions. Numerical experiments highlight the advantages of MgNO over CNN-based models and spectral-type neural operators, demonstrating improved ease of training and reduced susceptibility to overfitting.

### Strengths
1. The authors introduced a novel formulation for neural operators that characterizes neuron connections as bounded linear operators within function spaces. This eliminates the need for traditional lifting and projecting operators, simplifying the architecture.

2. The MgNO architecture, which leverages multigrid structure and multi-channel convolutional form, efficiently parameterizes linear operators while accommodating various boundary conditions. This approach enhances both accuracy and efficiency.

3. Empirical evaluations demonstrate superior performance of MgNO across multiple partial differential equations (PDEs), including Darcy, Helmholtz, and Navier-Stokes equations. This indicates the effectiveness and versatility of the proposed approach.

### Weaknesses
The limitations and drawbacks of the proposed methods are not explicitly mentioned

### Questions
1. The proposed method may not scale well to larger datasets or more complex problems. Any remark for this?

2. Is it possible to extend the universal approximation theorem to encompass general Banach spaces for X and Y?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new neural operator architecture that does not require lifting and projecting operators. It uses multigrid structures (V-cycle multigrid) to parameterize the linear operators between neurons. Then this paper proves the universal approximation of their proposed parameterization and uses experiments to show the efficiency and accuracy of the method.

### Strengths
The neural operator proposed in this paper uses the multi-scale method to get a better parameterization of the weights. It is applied to the spatial domain hence it seems like it won't significantly increase the complexity. From the experimental results, MGNO works quite well compared to other models, which provides convincing evidence that MGNO can be useful.

### Weaknesses
1. I am confused about the discretization of the input. It seems like the input still needs to be discretized (Eq.(6)) and the multigrid is applied to the spatial domain. Then I suppose the performance and the efficiency of MGNO are affected by the mesh size $h=1/d$. The performance of MGNO with respect to $d$ is missing in the paper.

2. What about the parameterization with multi-channel inputs? Can this V-cycle be applied to multi-channel inputs? If there is no easy extension, I believe the significance of this work is compromised.

### Questions
1. What is the dependence of $n$ with $\epsilon$ in Theorem 3.1?
2. Why are the approximation capabilities so important? It might be a necessary condition for neural operators to learn but is definitely not sufficient. In my understanding, FNO is good at working with different resolutions which probably is not caused by its approximation capability.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce a novel formulation for neural operators and establish (in Theorem 3.1) the corresponding universal approximation property.

The authors then propose a multi-grid-based parameterization of linear operators, called MgNO, that can be efficiently parameterized and naturally accommodates various boundary conditions.

Numerical results are provided on several popular PDEs, including Darcy, Helmholtz, and Navier-Stokes equations, with different boundary conditions, showing the superiority in prediction accuracy and efficiency of the proposed approach.

### Strengths
The paper provides novel insights and novel methodology of neural operators.
The numerical results on different popular PDEs with various boundary conditions look compelling.

### Weaknesses
I do not see particular weakness for this paper. See below for some comments.

### Questions
I do not have specific questions but the following general comments for the authors:

1. just being curious, can something similar to Theorem 3.1 be said about deep networks as defined in Section 3.2? How the network depth may play a role here?
2. it would be helpful to discuss also the limitation of the proposed approach.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
