# Gradient-Free Analytical Fisher Information of Diffused Distributions

- Decision: Reject
- Scores: 3, 3, 6, 6

## Abstract
Diffusion models (DMs) have demonstrated powerful distributional modeling capabilities by matching the first-order score of diffused distributions.
Recent advancements have explored incorporating the second-order Fisher information, defined as the negative Hessian of log-density, into various downstream tasks and theoretical analysis of DMs.
However, current practices often overlook the inherent structure of diffused distributions, accessing Fisher information via applying auto-differentiation to the learned score network. 
This approach, while straightforward, leaves theoretical properties unexplored and is time-consuming. 
In this paper, we derive the analytical formulation of Fisher information (AFI) by applying consecutive differentials to the diffused distributions.
As a result, AFI takes a gradient-free form of a weighted sum (or integral) of outer-products of the score and initial data.
Based on this formulation, we propose two algorithmic variants of AFI for distinct scenarios.
When evaluating the AFI’s trace, we introduce a parameterized network to learn the trace.
When AFI is applied as a linear operator, we present a training-free method that simplifies it into several inner-product calculations.
Furthermore, we provide theoretical guarantees for both algorithms regarding convergence analysis and approximation error bounds.
Additionally, we leverage AFI to establish the first general theorem for the optimal transport property of the diffusion ODE deduced map.
Experiments in likelihood evaluation and adjoint optimization demonstrate the superior accuracy and reduced time-cost of the proposed algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a way to approximate the Jacobian of the score function in a diffusion model without taking gradients. Based on expressing the Jacobian by a conditional covariance, the paper proposed some methods to estimate the Jacobian, the trace of the Jacobian,  and matrix-vector products with Jacobian. In the end of the paper, a criterion of whether the probability flow is an optimal transport map was also claimed.

### Strengths
This paper is clearly written. Core ideas are presented in a very readable manner, and there are no unnecessary complications.

### Weaknesses
While the clarity of writing in this paper is greatly appreciated, I regret to say that this paper has some major issues that resist a more positive evaluation.

1. The key result, Proposition 3 in the paper, is well-known. Most of the theory papers on diffusion contained a version of it, e.g., Benton et al., ICLR 2024 had exactly the same result.

2. Theorem 1 is wrong, and the proof in the appendix apparently did not prove it. Instead, it was only proved that positive semi-definiteness of some unknown matrix $C(t)$ implies the flow map is an optimal transport (which is yet incorrect; should be $C(t)C(T)^{-1}$). 

3. The analysis of the computational complexity of estimating trace by backpropagation did not take into account much more efficient trace estimators requiring only logarithmically many backpropagations, cf. Hutchinson estimator and its modern variants. 

4. Overall, the paper lacks technical depth or insight if viewed as a theory paper, due to the reason stated above. On the other hand, it lacks comprehensive experimental validation if viewed as an empirical paper. The proposed algorithm was only evaluated on a single task, and even in this task, it can be seen from Figure 5 that the proposed algorithm has worse detail (though taking less time).

### Questions
I have no particular questions.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides an analytical formula for the Fisher information, and uses jacobian-vector product tricks to obtain fast evaluation of likelihood evaluations. They use their formula to make a case for when, in fact, the diffusion ODE map /is/ the optimal transport map between two distributions. They have several experiments that use their approach for computing the negative loglikelihood (NLL) which appears to be correlated with high quality text-prompt/image generation.

### Strengths
This paper proposed a very natural solution to an otherwise computationally expensive problem.

### Weaknesses
The weaknesses of this paper are largely in the exposition, and in the sparsity of the literature review. 

On the writing, I strongly recommend having a native English speaker make a pass through the article if possible. There are many basic syntax errors throughout the text that ought to be corrected before submission.

The formula for the Hessian of a log-convolution of a density is well-known. This is a property that simply arises because this is a log-partition function, and the covariance appears when one takes two derivatives. 

I think the paper also tries to "do too much" by also trying to mention optimal transport maps --- I'm not sure what the connection is to this and other parts of the paper. I think this is also an interesting contribution to the field, but I'm not confident putting these ideas in the same work is best for clarity purposes.

### Questions
N/A

### Soundness
2

### Presentation
1

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
In this paper, 
1. the authors derive exact form of the Fisher Information (FI) matrix of the diffused target distribution in diffusion models context. 
2. Based on the formula, they propose an estimation of FI's trace by the trained diffusion model and an additionally trained model;
    - they also analyze its estimation errors,
    - they demonstrate the estimation makes speedup of the NLL computation.
3. Based on the formula, they propose an estimation of the matrix product of adjoint FI and certain vector only by the trained diffusion model;
    - they also analyze its estimation errors,
    - they apply the estimation to adjoint guidance sampling and show its effectiveness.
4. They provide a condition for the solution of a probability-flow ODE to become an optimal transport map.

### Strengths
- originality+
    - Focusing on the estimation of Fisher Information sounds novel and interesting at least for me.
- quality+
    - The paper is easy to follow, and the statements are clear, except for the theorem 1.
- significance+
    - Speedup of the NLL estimation would be useful even if it is not exact calculation. In addition, the AFI endpoint approximation seems also to be useful.

### Weaknesses
- clarity-
    - There were some unclear points. I will summarize them in the following questions.

### Questions
**Typo?**
1. In eq (1), $\alpha_t$ may be better to be replaced by $\alpha(t)$?
2. In eq (4), the symbol $s_\theta$ suddenly appeared without any explanation. I know it is related to $\epsilon_\theta$ and $\bar{y}_\theta$, but it would be better to leave some comments on them.
3. In eq (18), the symbol $h_\theta$ suddenly appeared without any explanation. I have no idea what this symbol stands for.

**Questions**
1. On JVP for trace, is it different from the Hutchinson's trace estimator?
2. On Proposition 7 and 8, the 2nd term and the 1st term of the errors seems to be related to data itself, and seems to be out of control, at least it cannot be reduced only with the improving its training. Does it cause any issue in practice?
3. In eq (20), I could not understand why the replacement $\sum_i w_i y_i y_i^\top \approx x_0 x_0^\top$ is valid.
4. In theorem 4, what distributions does this map define optimal transport between?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
A method for efficiently evaluating Fisher information is developed for diffusion models. The method is based on its analytic formula, which is derived by consecutive differentials to the diffused distributions. Due to the Gaussian nature of the diffusion process, the formula is expressed as a weighted sum of outer-products of the score and initial data, which is free from computing gradients. Based on the formula, an efficient algorithm for assessing trace of Fisher information matrix is developed using neural network learning. Another efficient algorithm is also proposed for using Fisher information as a linear operator for the adjoint optimization of  diffusion models. Several theoretical guarantees are provided for the algorithms. The analytical knowledge on Fisher information is also utilized for deriving a theorem that allows mapping deduced by the probability flow ordinary differential equation to possess the optimal transportation property.

### Strengths
Computing Fisher information matrix for high dimensional distributions is computationally very hard. This paper develops efficient methods to compute its summarized quantities without directly computing the matrix. Not only that, the authors manage to provide a theorem that guarantees the optimal transportation property of the probability flow ODE utilizing the analytical knowledge of the Fisher information.

### Weaknesses
Training cost of AFI-TM is not fully described. As for AFI-EA, adjoint guided sampling generally requires hyper-parameters. Since how the parameters were tuned is not written, it is unclear whether the obtained gain in the performance is actually due to AFI-EA or not.

### Questions
1. What are the minimum computational requirements for training AFI-TM?
2. What was the total wall-clock training time for AFI-TM?
3. For the adjoint guided sampling experiments, please provide details on:
    i) Specific hyperparameters tuned,
   ii) Hyperparameter ranges explored, 
  iii) Hyperparameter optimization method used, 
  iv) Computational budget for tuning

### Soundness
3

### Presentation
3

### Contribution
3
