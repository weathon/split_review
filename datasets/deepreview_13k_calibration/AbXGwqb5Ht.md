# Implicit regularization of deep residual networks towards neural ODEs

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Residual neural networks are state-of-the-art deep learning models. Their continuous-depth analog, neural ordinary differential equations (ODEs), are also widely used. Despite their success, the link between the discrete and continuous models still lacks a solid mathematical foundation. In this article, we take a step in this direction by establishing an implicit regularization of deep residual networks towards neural ODEs, for nonlinear networks trained with gradient flow. We prove that if the network is initialized as a discretization of a neural ODE, then such a discretization holds throughout training. Our results are valid for a finite training time, and also as the training time tends to infinity provided that the network satisfies a Polyak-Łojasiewicz condition. Importantly, this condition holds for a family of residual networks where the residuals are two-layer perceptrons with an overparameterization in width that is only linear, and implies the convergence of gradient flow to a global minimum. Numerical experiments illustrate our results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper shows that an implicit regularization of deep residual networks towards neural ODEs still holds after training with gradient flow. In particular, this is shown for both large depth (via gradient clipping in finite time) and large time limits (assuming PL condition). Along the way, interesting aspects of the problem are discussed and the results are demonstrated numerically on simple simulations as well as on CIFAR10.

### Strengths
The derived results and the neural ODE limits seem rather interesting. The theoretical analyses seem rigorous and their discussions are quite thorough, though I haven't read the proofs in detail. It could be that I have missed a similar related work in the literature, but I do think this seems to be an important contribution, and thus could spark interesting future work on implicit regularization as well as furthering understanding of residual networks via the toolbox of ODEs. Besides, the paper is, in general, very well written, and nicely presented.

### Weaknesses
- One of the key drawbacks is requiring weight-tying or weight sharing. While results with weight-tied networks don't look bad, still this would have been nice to take care of. It is unclear how much this constraint limits the practical applicability of the results. The authors should clarify if the weight-tying is strictly necessary for the ODE limit to hold, or if there are alternative initialization schemes that could achieve a similar result without weight sharing. Specifically, it would be helpful to understand if the proof strategy fundamentally relies on this assumption, or if it's a technical convenience that could be relaxed with further analysis. The current presentation leaves the reader wondering about the necessity of this constraint and its implications for broader use cases.

- The other issue is that the linear overparameterization $m > c_1 n$ would, in practice, be somewhat unreasonable and is thus a bit of a stretch. While the authors mention this might be a norm in the literature, the practical implications of such a constraint should be further discussed. It is not clear how this assumption affects the empirical performance of the model, and whether the theoretical results hold for more realistic scenarios with fewer parameters. The authors should provide more insights into the sensitivity of their results to this parameter, and whether there are any known techniques to mitigate the need for such a large overparameterization. It would be beneficial to see a discussion on the trade-offs between theoretical guarantees and practical feasibility.

### Questions
Please see above. Besides:


- Would it be possible to extend the approach to incorporate layer normalization?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper shows that the dynamics of a residual connection converges that to of an ODE. 

First, the authors show that under certain conditions (like the boundedness of the Frobenius norms of the weight matrices) for finite training time as the depth of the network tends to infinity the dynamics of a resnet converge to that of an ODE. This is assuming that the model is trained with clipped gradient descent. 

Since here the authors show that the Frobenius norm of the different of the weight matrices is upper bounded by a value that is O(exp(T)), the to show the result for when both T→ \infty and L → \infty, the authors also assume that residual network satisfies a PL condition. 

Therefore, the authors show that under these condition as T→ \infty and L→ infty, the dynamics of a residual network tend to an ODE and converges to a function that interpolates the training data.

### Strengths
The paper is very well written and easy to follow, where the results and their implications are clearly stated.

The authors show weights of a resnet convert to an ODE while considering the dynamics of the network as well, which is new and interesting. 

Given that the result shows that the dynamics of the resnet architecture converges to that of an ODE, and therefore as the authors mention one can utilize existing generalization bounds for neural ODEs etc can under certain conditions now be applied to resnets, given the results that has been shown by the authors.

The authors also show that their results/assumptions hold very well on their synthetic dataset.

For the cifar dataset, the authors show that their results hold when using smooth activations and the dynamics may deviate from neural ODE if one uses a non-smooth activation like ReLU.

### Weaknesses
The results are under the condition that the resnet is trained under clipped gradient flow, which is often not used in practice. While the authors acknowledge that this is a technical assumption to facilitate the proof, the practical implications of this constraint should be further explored. Specifically, it is unclear how the magnitude of the clipping threshold affects the convergence behavior and the final performance of the model. Furthermore, the assumption of a Polyak-Lojasiewicz (PL) condition, while useful for theoretical analysis, may not hold in practice for complex datasets, and the paper does not provide sufficient justification for its applicability in the scenarios considered. It would be beneficial to see an analysis of how the violation of the PL condition affects the convergence to the ODE limit.

For the experiments on cifar, the authors show the plot of a random coefficient and its value as one goes deeper into the layer. However, it would be more beneficial to see the difference in Frobenius norm of the weight matrices as well. This would give a more complete picture of how the weights evolve across layers and whether the smoothness assumption is indeed satisfied in practice.

### Questions
For the experiments on cifar, the authors show the plot of a random coefficient and its value as one goes deeper into the layer. However, it would be more beneficial to see the difference in Frobenius norm of the weight matrices as well.

### Soundness
4 excellent

### Presentation
4 excellent

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
The paper establishes a connection between deep residual networks and neural odes.  Prior works have attempted to provide a theoretical framework for the same, but they come with several shortcomings -- like considered only simplified models with linear activations. The authors train the neural network with gradient flow and show that in the limit of $L \rightarrow \infty$, the network converges to a discretization of neural ode.

### Strengths
1. Most prior works in this domain make simplifying assumptions which prevents their analysis from being directly applicable to practical models. The authors overcome those assumptions

### Weaknesses
N/A

### Questions
N/A

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper establishes that initialising the network with an ODE results in preserving smoothness of weights throughout training.  The authors do this through the framework of Polyak-Łojasiewicz condition.

### Strengths
Pros:

- (Significance) It is an important result that shows the impact of initial conditions on the training of ResNets; furthermore, it is crucial that while the paper is mostly theoretical, the settings the authors propose are realistic and can generalise to the practical ResNet models.  I also checked the derivations and could not find any problems with them. 

- (Quality) The paper is well written, with thoroughly addressing the reproducibility aspects (through both derivations and the experiments)

- (Clarity) The paper is clearly written, with great attention to detail

- (Originality) While the notion of interpretation of ResNets as a discretisation of (Neural) ODEs has been a widely-discussed topic, it has not been analysed in the opposite direction. The authors address an intriguing question of whether every ResNet corresponds to a (Neural) ODE and show, to my knowledge, previously undocumented, impact of initial conditions on whether the ResNet can be presented as a discretisation of an ODEs

### Weaknesses
Cons:

-  (Significance elements) There are some limitations to the analysis, which are related to implicit generalisation to the convolutional and other sparse scenarios (see questions below).


### Questions
Q 1: It seems to me that both fully-connected and convolutional neural networks would be the particular cases where the ODE parameter matrices A, V, W are considered sparse (some or most of the entries are fixed to zero and the rest are optimised according to Equation (5)). The experiment, depicted in Figure 3, suggests that results in Theorem 4 might be expanded to the more generic sparse scenarios.  Might be good if the authors could confirm this observation.

Q2: If it happens that the weights are initialised randomly, for every finite depth of the neural network (as there’s finite time and finite depth), there could be still a Lipschitz-continuous function (ii) over that set (as locally Lipschitz function on a compact set is Lipschitz as per, e.g. https://faculty.etsu.edu/gardnerr/5510/cspace.pdf ). However, what’s appearing in Figure 3 appears to go beyond literal application of Theorem 4: not only the function is compact but also it appears that the Lipshitz constant is preserved to be small during the optimisation. 

Q3: Another interesting aspect is that  it would be intuitive to see smaller Lipshitz constant could be beneficial for out-of-distribution recognition. I wonder if the authors could clarify on this aspect? To what extent would the proposed derivation generalise for higher-than-two layers of multilayer perceptrons?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
