# Second-Order Forward-Mode Automatic Differentiation for Optimization

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 6, 3

## Abstract
This paper introduces a second-order hyperplane search, a novel optimization step that generalizes a second-order line search from a line to a $k$-dimensional hyperplane.
  This, combined with the forward-mode stochastic gradient method,
  yields a second-order optimization algorithm that consists of forward passes only, completely avoiding the storage overhead of backpropagation.
  Unlike recent work that relies on directional derivatives (or Jacobian--Vector Products, JVPs), we use hyper-dual numbers to jointly evaluate both directional derivatives and their second-order quadratic terms. As a result, we introduce forward-mode weight perturbation with Hessian information (FoMoH). We then use FoMoH to develop a novel generalization of line search by extending it to a hyperplane search. 
  We illustrate the utility of this extension and how it might be used to overcome some of the recent challenges of optimizing machine learning models without backpropagation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors present a new optimization method relying on forward mode automatic differentiation (AD). Namely, the authors propose to use second order directional derivatives computed along random directions to precondition stochastic estimates of the gradients obtained by forward mode automatic differentiation along these same random directions. The proposed Forward Mode Second-order Hyperplane Search (FoMoH) interpolates between using an approximate Cauchy stepsize (that is a Cauchy stepsize computed with a quadratic approximation of the objective) along a random direction and an approximate Newton step. The proposed method is shown to outperform a standard forward gradient descent on the Rosenbrock function, a logistic regression problem, and the MNIST image classification task with a CNN.

### Strengths
- The idea of exploiting second order directional derivatives is original and could be further explored.
- The proposed method shows clearly superior performance than a simple forward gradient descent.

### Weaknesses
Unfortunately the paper does not give justice to the potential of the main idea.
Improvements are necessary and possible:
- The method does not require introducing dual numbers. Computing second order directional derivatives can easily be done with nested forward mode autodiff:
```
import jax

def hqp(fun, w, v1, v2):
  def dir_der_v1(w):
    return jax.jvp(fun, (w,), (v1,))[1]
  return jax.jvp(dir_der_v1, (w,), (v2,))[1]
```
The above may be slightly slower than the implementation with dual numbers (the difference is probably minimal) but it is also much simpler to implement than having to adopt a new kind of automatic differentiation library. If one want the best possible implementation, then Taylor-mode automatic differentiation can also be used but again the benefits are really minor. Algorithm 1 is then unnecessarily complicated when it could be written in just K calls to the above function to define the approximate Hessian. Presenting the algorithm with a simple implementation that any user could recode in at most 50 lines of code in jax or pytorch would greatly improve the potential adoption of the method.
- Unfortunately, the proofs are not rigorous, nor are the claims.
  - Theorem 1 is a corollary of Theorem 2 so no need to present it. Also results like $\lim_{t \rightarrow +\infty} \theta_t = \theta^*$ are meaningless: we don't want to wait the time of the universe to see convergence. Rates like the ones provided in Theorem 2 are relevant.
  - In all claims, detail the setting: what algorithm is used, what is theta_t, what is the expectation taken against etc... You may not do that in the main text by lack of space but at least make sure that the appendix contains a result that details all assumptions.
  - The proof of theorem 2 is unfortunately not well detailed:
    - Please give a detailed proof that $\tilde \theta_{t+1} = \tilde \theta_t + P(\tilde \theta^* - \tilde \theta_t)$. We are dealing with quadratics so the proof should boil down to simple linear algebra. Avoid intuitive arguments, just write the equations one by one showing the results. I personally will refuse this paper to be accepted without detailed proofs.
    - Give a proper reference for the fact that the expectation of a projection matrix defined from Gaussian variables is the scaled identity
    - First line of last set of equations of the proof of theorem 2 should read $\tilde \theta_{t+1} - \tilde \theta^* = (1- K/D)(\tilde \theta_t - \tilde \theta^*)$
    - Please be rigorous when you write expectations. You need to detail each time with respect to which randomness you are taking the expectation. For example at one point you write $\tilde \theta_{t+1} = \mathbb{E}[\tilde \theta_t + P(\tilde \theta^* - \tilde \theta_t)]$ but so then $\tilde \theta_{t+1}$ is not random. Unless you meant $E[\tilde \theta_{t+1}] = $. Such lack of rigor is detrimental to the potential of the idea.
    - Section B.4 contains multiple errors:
      - Reaching a critical point does not imply that you reach a minimum unless you make additional assumptions like convexity.
      - Again be rigorous in the use of expectations, one usually use conditional expectations conditioned on the previous iterate for example.
      - The provided rate is clearly not linear. Consider rereading in details the reference for example.
- Second order methods may generally be very sensitive to the batch-size. It would be great to plot a sensitivity analysis of the method with the batch-size for e.g. a given learning rate.
- Consider another dataset than MNIST. MNIST is well known to be particularly easy and may not reflect potential challenges that the method can have.

### Questions
- First it would be great to revise the proofs to make them rigorous.
- Could you add a full mathematical definition of FoMoH-BP?
- What is the logistic regression model? I suppose it is not a regression but a classification problem first? Then if you use 7850 parameters it's probably not a simple linear model but some form of Multi-Layer Perceptron?
- Detail the CNN architecture used in the experiment.
- In the abstract, you mention alternative (orthogonal to be exact) methods for forward gradients. They are never compared in the experiments. It would be great to have them.
- By curiosity how can analog optical systems compute derivatives of intermediate functions to implement forward mode automatic differentiation? The reference provided by the authors does not mention AD, at least from its abstract.
- You mention "linesearch" in line 243 but there is no linesearch at all in the algorithm. What do you mean by linesearch?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a forward-mode-only optimization method that uses second order information on randomly sampled hyperplanes. 
The method makes use of (K^2 + K)/2 calls to a "double" forward-mode AD, implemented with hyper-dual numbers, computing along the way the Hessian projected onto the drawn plane. The paper presents theoretical results on convex and quadratic functions that also relates it to the Newton method, alongside some empirical validation on a test function and two learning problems.

### Strengths
- The significance of developing a preforming optimization method that does not rely on reverse-mode differentiation is very high, and the proposed method seems to make a concrete step in this direction 
- The paper is mostly well written and easy to follow, the notation is clear (although a few passages could be made clearer, see below)
- The work does a good job introducing the concept of dual and hyper-dual numbers, which I expect the community to benefit from 
-  The theoretical results clearly show the advantages of the proposed method over FGD, as well as the larger scale experiment.

### Weaknesses
 - One main promise of forward mode differentiation is to vastly decrease the memory requirement for large models, however the paper does not empirically quantifies the advantage of FoMoH in this regard. It would be nice to include memory footprint comparisons (as well as perhaps a table summarizing the runtime and memory complexity of key algorithms)
- I would have appreciated some larger scale experiment with transformer architectures, e.g. for fine-tuning LLMs, which could be an interesting application of the proposed method
- Some details could be better specified in the main paper:
    -  It is not entirely clear to me by reading the paper if the (hyper-)dual numbers allow for the computation of JVPs and bilinear hessian products by just "tracking the epsilons" while computing the function, or if one has actually to implement the above-mentioned operations (I think it's the first). One "implementation" example would help focus ideas.
    - I'm a bit confused about the origin of Equation (1) right. Do the expressions for the $\kappa$ come from manipulation of the resulting Taylor expansion or is it "set by design" (to mimic Newton updates)? In general, I would have appreciated some more details around lines 227 to 240
   - the learning rate scheduler seems like an important addition for empirical performance, some more details (e.g. which scheduler, how did you choose its hyperparamters) in the main paper would be welcomed.
   - some more discussion on relations between FoMoH-1d, FoMoH-BP and FGD would have been nice. For me it is not immediately clear why FoMoH-1d consistently underperforms FGD on the learning tasks and why FoMoH-BP consistently performs on par with BP.
  - what does BP stand for in the experiments? Is it plain (stochastic?) gradient descent or some other adaptive method?

### Questions
1. Is it correct to say that the method performs Newton steps in the sampled subspaces (assuming learning rate being 1)? If not, what's the relationship between the two?
2. the $\kappa_i$'s need not be positive, correct?
3. in the learning tasks, are also examples being smapled (i.e. mini-batch updates?). If so, is the proposed method sensitive to the mini-batch size?
4. Do you think the proposed method could be relevant also for forward-mode gradient-based hyperparameter optimization?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper investigates the effectiveness of the second-order differentiation in forward automated differentiation.
This paper and regards the forward propagation with dual number as the objective function applied second-order Taylor-series expansion to.
By using dual numbers, the proposed method estimates the Hessian matrix and applies the approximated Newton's method for the optimization.

### Strengths
1. This paper is well-written and easy to follow. Assumptions and mathematical expansions are explained in detail.
1. Experimental results demonstrate the proposed method is more efficient than baseline first-order methods in terms of iterations of parameter updates.
1. Convergence properties are proved in theory, and the proposed method is guaranteed to be consist with Newton's method.

### Weaknesses
1. I am not very sure that this paper addresses a new topic in machine learning.
The explanation of the proposed method seems to address general optimization problems but does not seem to focus on the problem in machine learning.
For examples, this paper does not explicitly address the difficulty of accessing the objective function due to large datasets like SGD, and not address the difficulty of non-convexity caused by nonlinear models.
Since I do not have much expertise in optimization theory or operations research, I cannot evaluate the novelty of this paper well in the context of optimization theory.
Even so, I doubt the proposed method is very novel because the used mathematical tools are fundamental and the addressed objective function does not seem very difficult.
Is the research problem specialized for machine learning problems? And, is the paper new even in the context of the optimization problem?


2. While this paper evaluates the convergence of the proposed method in terms of iterations, it does not evaluate the runtime of the proposed method.
The proposed method requires an inverse of Hessian matrices, and I think its computational cost can be high.
Does the overhead of the proposed method not increase the runtime in one iteration? If it does, the proposed method is still faster than baselines in terms of runtime until convergence?
To emphasize the practical usefulness of the proposed method, this paper needs the evaluation of runtime.

3. It is not clear that the proposed method is scalable for recent deep neural network model architectures.
(Fournier et al., 2023) seems to show that the first-order forward gradient method is applicable to ResNet18. Is the proposed method applicable to such modern architectures?

### Questions
1. Why is this paper suitable for publication as machine learning research? What is the difficult point of the optimization method in machine learning, and how does the paper address it? If the approximation of a second-order method using dual numbers is new, why has no literature in optimization theory or operations research discussed it?

1. Does not the overhead of the proposed method increase the runtime in one iteration? If it does, the proposed method is still faster than baselines in terms of runtime until convergence?

1. How is the scalability of the proposed method?

### Soundness
3

### Presentation
3

### Contribution
2
