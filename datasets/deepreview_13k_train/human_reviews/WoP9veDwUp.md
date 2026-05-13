# Variance-Reduced Meta-Learning via Laplace Approximation

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Meta-learning algorithms aim to learn a general prior over a set of related tasks to facilitate generalization to new, unseen tasks. This is achieved by estimating the optimal posterior using a finite set of support data. However, this estimation is subject to high variance due to the limited amount of support data for each task, which often leads to sub-optimal generalization performance. In this paper, we address the problem of variance reduction in gradient-based meta-learning and define a class of problems particularly prone to this. Specifically, we propose a novel approach that reduces the variance of the gradient estimate by weighing each support point individually by the variance of its posterior over the parameters. To estimate the posterior, we utilize the Laplace approximation, which allows us to express the variance in terms of the curvature of the loss landscape of our meta-learner. Experimental results demonstrate the effectiveness of the proposed method and highlight the importance of variance reduction in meta-learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a new gradient-based meta-learning algorithm that is able to decrease the variance of the learned parameters. Taking a Bayesian perspective, it weights each of the support data points by the variance of the posterior that it induces over the parameters, approximated using a Laplace Approximations. Experiments show improvements in meta-learning ODEs w/o substantially increasing computation time, but is inconclusive for a real-world physics simulation problem.

### Strengths
# Originality and significance #

As far as I know, this paper is the first application of the Laplace Approximation to GBML. The results are promising, so I think this work would be relevant to the community.

# Clarity #

The paper is written very clearly and is straightforward to understand. The authors explain some of the assumptions made.

# Quality #

The proposed algorithm is simple and straightforward, with approximate (but incomplete) mathematical backing.  A good diversity of problems and baselines are used in the experiments, and the experimental results are promising.

### Weaknesses
1. The experiments do not contain ablations in certain axes. The problem dimensionality is varied, but the model dimension (the network architecture) is not. Specifically, the number of layers and the number of neurons per layer are not explored, which could significantly impact the performance of the proposed method. This is a critical omission, as the expressiveness of the network is a key factor in meta-learning performance, and the authors' claim about the network's ability to model the task distribution as a Gaussian in parameter space relies on this expressiveness.
2. The assumptions of the algorithm is not clear. The variance calculation implicitly assumes that $\theta_0$ is deterministic, but is that reasonable given that it depends on previous parameter updates (which are not deterministic)? Furthermore, the algorithm's reliance on the Laplace approximation, which assumes a unimodal posterior distribution, might not hold in practice, especially with complex task distributions. The validity of this approximation needs to be further justified, particularly in the context of the stochastic nature of the meta-learning process.

### Questions
1. The standard errors for the Omnipush results are large compared to the differences in algorithms' performances. Have you tried increasing the number of trials to reduce it?
2. How do the results vary when the model architecture varies, e.g. when the number of parameters in the neural network increases?
3. Is there a proof of the claim made in the first paragraph of page 5?

### Soundness
3 good

### Presentation
4 excellent

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
The paper considers improving gradient-based meta-learning from the perspective of approximate bayesian inference. Here the authors show that vanilla MAML’s adaption can be seen as aggregating Gaussian-approximated posterior distribution over each support example with the same covariance matrix. Instead of using the same covariance, the authors apply Laplace approximation so that different support examples have its own covariance matrix (which is the Hessian of the example’s negalive log-likelihood). The proposed method LAVA then uses the Hessian-weighted individual-example-adapted parameters as the final adapted model parameters. The authors show that this new approach reduces the variance of the parameter estimates. Experimentally, results are shown over 3 few-shot regression tasks which demonstrate the performance advantage of LAVA over existing meta-learning methods.

### Strengths
- The idea of aggregating individual example’s posterior distribution in the context of meta-learning is to my knowledge novel.
- The connection between MAML (which the authors argue treats each example’s posterior covariance as equal) and LAVA (which allows Laplace approximation in individual example’s posterior) is novel and insightful.

### Weaknesses
Although I find the paper’s proposed idea interesting, I find the choice of technical language, explanation, and the experimental results a bit lacking in its current form for publication:

- **Method is computationally too expensive**.
    - Despite the authors performing an analysis in Figure 6 and 7 showing the time cost of 1 inner step of LAVA is comparable to 6 inner steps of CAVIA, it is important to note that this relationship depends on (and should be linear to) the dimensionality of the adaptable parameter space of LAVA, as the Hessian computation takes $O(d)$ backprops where $d$ is the dimension of $\theta$. If we choose the number of adaptable parameters to be larger (for example, 100 context parameters in the image classification task in the original CAVIA paper), the computation and time cost of LAVA would be much greater than CAVIA. Specifically, the computation of the full Hessian matrix requires $d$ Hessian-vector products, each necessitating a separate backpropagation pass. This leads to a computational complexity that scales linearly with the dimensionality of the adaptable parameter space, posing significant challenges for scaling to higher-dimensional problems.
    - Given the worse computation requirement of LAVA compared to CAVIA and MAML, I believe it is necessary for the authors to further discuss and investigate possible techniques for computation savings. For example, instead of computing and storing the Hessian, it is conceivable to use techniques such as 1) only performing Hessian vector products (which only takes constant back props to compute) and 2) using conjugate gradients to approximately find the (inverse Hessian, vector) product. These explorations are necessary for the scaling of the proposed method. Purely scaling up the non-adaptable parameters while keeping the number of adaptable parameters to a very small number (e.g. $<10$) may not provide sufficient performance in the case of LAVA on real world problems.
- **Evaluating on problems with higher inherent dimensions** The three few-shot experiments are all internally parameterized by a small number of parameters ($<10$), which might make it appropriate consider LAVA which could adapt a correspondingly small number of context parameters. However, for real world parameters, the inherent problem dimensions could be much higher or unknown. The current experiments in the paper haven't demonstrated the ability of LAVA to handle such problems. For instance, in image-based tasks, the dimensionality of the input space is inherently high, and directly adapting model parameters in this space would be computationally infeasible. It would be beneficial to see how LAVA performs when adapting a lower-dimensional latent representation of the input, or when applied to tasks where the inherent dimensionality is not known a priori.
- **Evaluating on another model architecture.** All the three few-shot experiments are performed using the same 3 layer 64 hidden unit MLP architecture. It is useful to also demonstrate that the proposed method can perform well for other architectures (different computation blocks, depths, and widths). For example, evaluating LAVA on a convolutional neural network (CNN) for image-based tasks or a recurrent neural network (RNN) for sequence-based tasks would provide a more comprehensive understanding of its generalizability.
- **Comparing gradient-based meta-learning methods under the same number of inner-problem backprops used**. In the experiment section, the authors have reported performances of different baseline gradient-based meta-learning methods. However, it’s not clear to me whether all these methods are restricted to using 1 inner steps (the same as LAVA). If so, I want to highlight that LAVA’s single inner adaptation update step requires number of backprops proportional to the adaptable parameter dimension, while the other methods only need 1 backprop per single inner adaptation step. Thus, for fairness, the authors should also allow the other baseline methods to use the same number of backprops by allowing them to take more inner adaptation steps (preferably during meta-training, at least during meta-test). This might improve the performances of some of the baseline methods. A more equitable comparison would involve normalizing the computational budget across all methods, ensuring that each method is allowed the same number of gradient computations during both meta-training and meta-testing.
- **Unsatisfying explanation on the lack of performance on Mini-imagenet**. In Table 4 in the Appendix, the authors compare LAVA with other meta-learning methods on Mini-Imagenet (arguably the most commonly used few-shot meta-learning benchmark) and find the performance to be worse than many other methods. The authors give an explanation that the few-shot classification classification are inherently discrete problems that do not suffer as extensively from the task overlap. However, this claim seems incorrect to me, as observing a single image, label pair from a few-shot classification task is also insufficient to determine what the rest of the classes are in the task. Thus there is also task overlap according to the authors’ definition. Besides, it’s only unclear how the discreteness of the labels would play a role in this, as the learning parameters $\theta$ are in a continuous space. The authors should provide a more rigorous explanation for the observed performance discrepancy on Mini-Imagenet, potentially exploring factors such as the suitability of the Laplace approximation in discrete output spaces or the impact of the chosen architecture on performance.
- **choice of technical language**
    - **Assumption 1**. It is a bit unclear how to define the optimal $\theta_{\tau}^*$. To my understanding, the right-hand side of Equation (6) should not guarantee to be the best possible $\theta$ in the space $\Theta$ for the task $\tau$. Instead, it makes more sense use $\theta_{\tau}^*$ to denote the one-step gradient adapted model parameters over an infinite number of support examples sampled from the task $\tau$. (In fact this is what has been shown in Appendix A.2). However, if more than one gradient steps are taken, the unbiasedness (and thus Assumption 1) would no longer be true. A more precise definition of $\theta_{\tau}^*$ is needed, along with a clarification of the conditions under which Assumption 1 holds.
    - **Assumption 2**. The notation $f_	au(x)$ is defined without exactly specifying what its output means until Assumption 2. Besides, in the interpretation of Assumption 2, the authors mention an alternative formulation is that the conditional task-distribution have a non-zero “covariance”. However, I believe this terminology should be changed to “having a non-singleton distribution support”.
- **Equation 9 is incorrect without additional assumptions**. We notice that the single-example posterior terms on the right hand side is each proportional to product of the example likelihood and the prior $\propto p(y_i \mid x, \theta) p(\theta)$. Hence the product on the right hand side of Equation 9 would be proportional to the product of $N$ prior probabilities $p(\theta)^N$. In contrast, the left hand side of Equation 9 is still proportional to only $p(\theta)$, making the prior weighted more heavily on the right hand side of (9). A way to fix this is to introduce the uniform prior assumption earlier than Equation (9) instead of after.
- **The explanation of the variance reduction is a bit lacking**. Equation (12) formulates a variance reduction problem. However, the current writing misses the connection to its use of Assumption (1) which would imply that the estimators $Z$ under different values of $\{W_i\}$ would have the same expectation. Without clearly specifying this, the variance reduction problem seems out of place and unmotivated.

### Questions
- On page 5, it was mentioned that “Consequently, it is possible to shape the posterior distribution $p(\theta | x, y)$ to be normal”. It’s not clear to me how this would be possible for general neural network predictive models. Can the authors further explain this?
- How many context parameters (adaptable inner loop parameters) are used in the MiniImagenet experiment? How long would the training take compared to other methods on this application?
- Why are the dotted prior curves sometimes different for the same column in Figure 5 in the Appendix?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors characterized task overlap for GBML, and proposed a solution to address high variance in GBML, which reduced the variance of the gradient estimate by weighing each support point individually by the variance of its posterior over the parameters.

### Strengths
The idea is of task-overlap is good, which is demonstrated in Figure 1.

The idea of aggregating of parameters is good and new.

The experiments on the toy example, sine function regression, contain good discussion about the variance reduction.

### Weaknesses
 **The presentation can be further strengthened.**

* The notation keeps changing, which is very unclear. Please make notation clear and consistent.
* The type of reference, eg. in-text reference, needs to be checked.
* Eq 1. is not clear. It is better to rewrite the objective.

**Please reconsider the assumptions and Proposition 1.**
* Eq 3. is unclear, as $D_{\tau}^{Q}$ is just one realisation of $D_{\tau}$. It seems that the authors miss another expectation there given that the authors claim that the uncertainty comes from data points.
* Meanwhile, the authors claim that $D$ is a collection of all tasks, is it finite or countable infinite? Are there any uncertainty in the generating process of tasks themselves?
* In theory, it is even difficult to have a local solution of MAML's objective. To ensure it, we often need additional assumptions. The assumption 1 and the paragraph underneath do not make sense from a theoretical aspect though the authors try to provide some theory. 
* The definition of $h_\psi$ on page 5 is problematic as covariance needs to be positive semi-definite.
* I do not understand why the authors need to have Proposition 1 if it is a well-known result.



**From the experiments in Appendix, it seems that the method does not work well on mini-ImageNet.**

### Questions
Why does the proposed method perform worse than MAML on mini-ImageNet?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the 'task overlap' problem, which enlarges the variance for posterior parameter estimate in GBML. A new approach, LAVA is proposed to alleviate this issue.

### Strengths
S1. This work identifies the task overlapping issue for GBML.

S2. To overcome the challenge of task overlapping, this work proposes a Hessian aided task adaption, and further employs Laplace approximation, variance reduction, as well as stabilized Hessian for efficiently solving it.

### Weaknesses
W1. Task overlapping needs more examples. Because this is the core to this work, it is beneficial to provide more real-world examples Current sinusoidal example appears to be oversimplified and not convincing enough.

W2. This work can benefit from additional experiments in real-world scenarios. It seems that on the only real-world dataset, omnioush, the proposed algorithm is not the most competitive.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
