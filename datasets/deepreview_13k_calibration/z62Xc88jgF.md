# Neural functional a posteriori error estimates

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 8, 6, 6

## Abstract
We propose a new loss function for supervised and physics-informed training of neural networks and operators that incorporates a posteriori error estimate. More specifically, during the training stage, the neural network learns additional physical fields that lead to rigorous error majorants after a computationally cheap postprocessing stage. Theoretical results are based upon the theory of functional a posteriori error estimates, which allows for the systematic construction of such loss functions for a diverse class of practically relevant partial differential equations. From the numerical side, we demonstrate on a series of elliptic problems that for a variety of architectures and approaches (physics-informed neural networks, physics-informed neural operators, neural operators, and classical architectures in the regression and physics-informed settings), we can reach better or comparable accuracy and in addition to that cheaply recover high-quality upper bounds on the error after training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose a loss function for training PINNs with theoretically guaranteed error bounds. Experiments are done for verifying their claims.

### Strengths
1. By the theory from functional a posteriori error analysis, using Astral loss gives theoretical guarantee that the output of neural network is the exact solution in the sense that their distance is zero in some function space.

2. Astral loss can be computed explicitly for common PDE problems. The authors use elliptic equation as an example.

3. Some experiments are done to compare Astral loss with the commonly used residual loss using different models/equations.

### Weaknesses
1. Although the use of this type of loss in this setting might be new, this work does not prove any new theoretical results.

2. That being said, experiment is a very important component in this paper, however, I find the evaluation metric of the solution very interesting. More specifically, let $u$ be the output of neural networks and $u^*$ be the exact solution. The test error is usually computed using relative $L^2$ norm (See for example [1][2]), i.e.
$$|| u - u^*||_2^2 / ||u^*||_2^2 = \int|u - u^*|^2dx / \int |u^*|^2 dx.$$
However, in Figure 4, when evaluating solutions, the mean error is computed using equation (15), the energy norm. 

(i). why not using the relative $L^2$ norm? How does Astral loss perform if the evaluation is done in $L^2$?

(ii). The a posteriori error bound is in the energy norm, i.e. 
$$L(u, w_L) \leq |||u-u^*||| \leq U(u, w_U).$$
so I would naturally expect Astral loss to achieve fairly small error in this energy norm, but this does not necessarily imply the solution is "better". Equations can be solved in different spaces. In fact, I think the space $L^2$ is more commonly used when people study existence and uniqueness of PDE solutions. 

(iii). There could be a relation between the energy norm and $L^2$ norm. More explanation is needed for the specific choice of the evaluation metric since it differs from the previous literature.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method for training neural networks that provide solutions to PDEs (including PINNs, Neural Operator networks, and vanilla surrogate models). The idea is to upper bound the error of the predicted solutions and incorporate this upper bound into the training loss of the neural network. Constructing the the upper bound on the solution error is non-trivial and requires expert knowledge, but this provides a way of incorporating domain knowledge into the model.

### Strengths
- The paper is well-written and easy to follow. Figures are clear and informative.
- The paper addresses a method for computing error bounds on solutions to PDEs, a challenge of high interest to the ML for physics community.
- Experiments support the claims.

### Weaknesses
 - It seems like this approach will have limited applicability. The first limitation is that the U function must be specified by the practitioner, but this is addressed in the paper, seems reasonable, and is a way to incorporate domain knowledge. The bigger issue is that in most scenarios, I imagine that predicting the error certificates is at least as difficult (and usually more difficult) than predicting the solution. This is particularly concerning because the error certificate $w_U$ is meant to provide a rigorous upper bound on the error, which requires a high degree of accuracy in its own prediction. If the surrogate model struggles to produce accurate error certificates, the resulting error bounds will be loose and potentially uninformative, limiting the practical utility of the method.

- My intuition is that the error certificate w_U can be thought of as an *explanation* of how the solution emerges. For example, the certificate could explain the predictions of a day-ahead weather forecast model by providing the evolution of the weather variables over the intermediate time steps. When a good certificate can be generated, the practitioner can feel confident that the solution is correct (with hard error bounds!), but otherwise the error bounds will be loose and the practitioner will not have much confidence in the solution. This all seems desirable, but I wonder if there exists a large set of problems for which the surrogate model can produce good solutions but not produce good certificates?

There are some minor typos throughout:
- Figure 1: should approximate solution u by u^tilde?
- Section 2.1 "deep learning is to"

### Questions
- My intuition is that the error certificate w_U can be thought of as an *explanation* of how the solution emerges. For example, the certificate could explain the predictions of a day-ahead weather forecast model by providing the evolution of the weather variables over the intermediate time steps. When a good certificate can be generated, the practitioner can feel confident that the solution is correct (with hard error bounds!), but otherwise the error bounds will be loose and the practitioner will not have much confidence in the solution. This all seems desirable, but I wonder if there exists a large set of problems for which the surrogate model can produce good solutions but not produce good certificates?

There are some minor typos throughout:
- Figure 1: should approximate solution u by u^tilde?
- Section 2.1 "deep learning is to"

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new loss function for supervised and physics-informed training of neural networks and operators that incorporates a posteriori error estimate. The trained model can guarantee the approximation error as this is done by the new loss function aiming at minimizing the theoretical posterior error estimate. The later has been established for a number of PDEs.

### Strengths
1.  It is a novel idea to adopt the theoretical  functional a posteriori error estimates for the learning objective. The functional a posteriori error estimate was initially established in the conventional finite element method analysis for PDE.

2. The entire framework has been clearly described (at least I can follow the main stream of the paper, although I am not the expert in this particular area).

3. The paper is well motivated with the goal to mitigate neural PDE solvers' inability guarantee good accuracy in practice.

### Weaknesses
Although this is a viable approach in a guaranteed way to produce reliable neural PDE solvers, the application could be limited, e.g., in the case for the problems where there is no theoretical posteriori estimates available.

### Questions
Not sure why the full GitHub repository is not made available for review.

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
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper brings "functional a posteriori error analysis" from the mathematics community to machine learning. Similar to Hillebrecht et al and many others, the goal is to obtain error certificates, i.e, some formal statement on the upper bound of the error produced by physics-informed neural networks. In functional a posteriori error analysis, the upper bound of the error depends on approximate solution, data, and additional fields that can potentially tighten the bound. This work builds on this direction and proposes a loss function Astral. Experiments show that in an unsupervised setting, Astral outperforms one baseline (Li et al).

### Strengths
I note that I am not an expert in the related domain of the paper. Hence, I requested area chairs for additional reviewers. My score reflects that I am ignorant in this field and do not want to reject papers.

There are many papers on certifiable machine learning, where the goal is to analyze the error, traditionally from generalization theory like PAC-Bayes bounds. For physics-informed neural networks, I think there might be meaning in investigating practical techniques to upper bound the error.

What this paper provides is perhaps the idea of bringing "functional a posteriori error analysis", which can be interesting to certain parts of the community.

### Weaknesses
On the other hand, I would have preferred if the presentation of the paper was more kind to readers. For example:

The introduction provides minimum information about astra -- only that it is a loss function with certain benefits like more robustness over residuals and variational losses. In my view, there should be a high-level description of (a) what motivates this specific loss function, and (b) what exactly is this loss function. There should also be reasoning behind it at a high level. It is difficult to grasp the concept and also get interested otherwise. I think the paper can also be more kind to the readers by defining certain terminology before using them, e.g., majorants, posterior error, priori error, etc.

I found section 2.3 to be difficult to parse. The paper states several equations without explaining them in sufficient depth. For example, in equation (9), I did not understand where the definition of astral is from. The paper states "It is possible to derive" but at least in the appendix, these derivations should be shown. Equation 12 is also similar. I could not understand the derivation from equation 9 to equation 12. There should also be sufficient reasoning "why", for example, equation 12 is a good measure of the predicted solution.

### Questions
My questions for clarification are embedded in the comments above.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
