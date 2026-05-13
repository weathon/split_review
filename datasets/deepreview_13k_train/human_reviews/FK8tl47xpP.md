# Greedy Learning to Optimize with Convergence Guarantees

- Decision: Reject
- Scores: 6, 5, 6, 8

## Abstract
Learning to optimize is an approach that leverages training data to accelerate the solution of optimization problems. Many approaches use unrolling to parametrize the update step and learn optimal parameters. Although L2O has shown empirical advantages over classical optimization algorithms, memory restrictions often greatly limit the unroll length and learned algorithms usually do not provide convergence guarantees. In contrast, we introduce a novel method employing a greedy strategy that learns iteration-specific parameters by minimizing the function value at the next iteration. This enables training over significantly more iterations while maintaining constant GPU memory usage. We parameterize the update such that parameter learning corresponds to solving a convex optimization problem at each iteration. In particular, we explore preconditioned gradient descent with multiple parametrizations including a novel convolutional preconditioner. With our learned algorithm, convergence in the training set is proved even when the preconditioner is neither symmetric nor positive definite. Convergence on a class of unseen functions is also obtained, ensuring robust performance and generalization beyond the training data. We test our learned algorithms on two inverse problems, image deblurring and Computed Tomography, on which learned convolutional preconditioners demonstrate improved empirical performance over classical optimization algorithms such as Nesterov's Accelerated Gradient Method and the quasi-Newton method L-BFGS.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to use greedy learning to help scale L2O methods by avoiding memory constraints of unrolling, allowing to train for more iterations. The paper focuses on learning a linear operator preconditioning operator, minimizing the function value at subsequent iteration. The paper shows that such parametrisation, by virtue of generalising gradient descent, the iterations admit provable convergence guarantees, even on unseen data. Such preconditioner parametrization is shown to outperform classical optimization algorithms, such as NAG and L-BFGS, in experiments on two image inverse problems: image deblurring and Computed Tomography.

### Strengths
The theoretical part of the paper is well-written and provides a very clear story. The theoretical framework also provides a good starting point for further generalising analysis of L2O schemes, especially when moving to non-convex settings.

The proposed preconditioner learning is memory-efficient, fast, with convergence guarantees and empirical evidence on small problems.

### Weaknesses
Major:

Main weaknesses appear in the numerical section of this paper. Overall, the numerical section is very difficult to read, as it seems to mix the exact parameter choices with the rest of the explanations, further obfuscating everything. The various details seemed to have been mixed into a single soup of information - this should be summarised better. 

The numerical comparison seems to be missing the main evaluation - it is unclear whether the method actually generalises. Only a small example is portrayed, and no evaluation over the whole dataset is provided. It is not clear to me whether Figure 2 converges and Figure 6 diverges simply due to a different example being provided. Preferably there would also be some analysis of the initialisation question for the problems of consideration. 

There is also a summary/interpretation missing from the numerical section - it is not clear what the numerical results seem to be showing beyond efficiency over classical methods? Why are fully learned preconditioners bad? Is this observed for all problems? 

There also seems to be very little mentioned about the limitations of this approach - can this be expanded upon? Currently (at least to me), the question of computational costs behind hyperparameter tuning is not very clear. Also, memory footprint is unclear to me - the greedy approach needs to store a matrix for each step - thus linearly increasing memory requriement with T?

Minor: 

The method has only been illustrated on rather small scale problems (limited to 40x40 and 96x96) - it would be interesting to see whether same behaviour is observed on more realistic image sizes like 256x256 or 1024x1024. 

The paper is limited to convex problems, and while this is a good starting point I do believe that this is a significant weakness, especially given the interest in using L2O for optimization of non-convex problems. In the same vain, this approach (or at least the analysis) seems to be limited to differentiable functions.

### Questions
* Equation 2 seems to only vary the y over the whole space. I believe this should be rewritten to emphasise what kind of functions you expect to be varying over. I.e. y should be from some underlying distribution? Do regularisers get varied? Do operators get varied?
* Line 108, you seem to choose X to be a finite dim Hilbert space - what is the value of this? If X is finite dim, then practically there is not point in distinguishing it from Euclidean space or am I missing something?
* Proposition 2 - linear independence seems like a rather arbitrary assumption. Can anything be said when it does not hold?
* Equation 9 - this is a different regularizer from the one in equation 2, so worth using different notation for the two.
* Theorem 3 seems to assume that $x_t$ has to now be a bounded sequence, which seems to be a relatively strange assumption to appear in such a context. Can you explain why this is necessary?
* Random question to authors: do you believe that L2O can overcome the problems discussed in https://arxiv.org/pdf/2301.06148? 
* Section 6 - in this section what is Y? 
* Figure 3a - this is not reconstruction, but initialization presumably? 
* Figure 5 - where is the ground truth? Why is it only sinogram and reconstruction shown?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The submission introduces a "learning to optimize" algorithm that learns a sequence of fixed preconditioners to apply to gradient descent by fitting them greedily to maximize the one-step progress on a set of training problems. The paper presents convergence guarantees that the algorithm can fit and is guaranteed to converge when run for longer than trained on some problems that are not in the training set. The submission introduces multiple types of preconditioners and shows experimental results on deblurring and tomography problems.

### Strengths
The learning to optimize literature is still in development, and does not yet have well defined formalism or benchmark problems. As such, the goal of the paper as bringin formal guarantees to this setting is a new and relevant contribution to the community. The proposed algorithms show promising results on the experimental setup.

### Weaknesses
 **Safeguards.** The proposed algorithm still relies on hand-crafted a-priori knowledge of the optimization problem in the form of the maximum step-size that would work for all training problem, $\tau$. As such, it does not significantly differ from alternative approaches that require safeguarding or search within a predefined set that guarantees convergence. The reliance on a fixed, global step-size $\tau$ across all training problems and iterations is a significant limitation. It necessitates a conservative choice of $\tau$ to ensure convergence for the 'worst-case' training problem, potentially hindering performance on other, less challenging problems. This contrasts with adaptive methods that dynamically adjust the step-size based on local problem characteristics.

**Experimental validation.** The definition of train and test problems in the numerical experiments is not sufficiently transparent. If I understood it correctly, both problems are of the form $\|Ax-b\|^2$ but the training and test "samples" only differ in $x$ and $b$; the linear operator $A$ is fixed. This seems like an ``easy'' problem, as the goal of learning algorithm is to learn a preconditioner that approximates the inverse of $A^TA$, which is fixed across both training and test. The paper should make the distinction clear and highlight possible limitations. A more thorough experimental evaluation that tests the trained algorithm against other blurring operators, at least Gaussian blur with different parameters, would help make the claim that the learning algorithm can indeed generalize. The current setup, where only the data vector $b$ varies while the operator $A$ remains constant, does not adequately demonstrate the algorithm's ability to generalize to different problem structures. The algorithm might be learning a preconditioner that is highly specific to the fixed operator $A$, rather than learning a generalizable optimization strategy.

**Generalization guarantees.** The submission claims that the given algorithm "ensures convergence on unsees data" but the guarantees seem weak. Theorem 2 guarantees that there exists functions for which the given algorithm will work, but this is weaker than typical generalization guarantee. Translated to the classification setting, I would take to mean "there exists samples that were not in the training set that the algorithm classifies correctly", which is not a strong statement about the performance of the algorihm. Would it be possible to guarantee that the algorithm would work on all $1/\tau$ smooth problems, or to characterize that the preconditioner learned by the algorithm will lead to better performance on other problems if the train and test problems use the same operator $A$?

**Convolutional preconditioners** That the experimental results show a significant improvement in performance when used the learned convolutional preconditioner makes it unclear whether the benefit arises from the convolutional parameterization or the "learning to optimize" approach, and one could envision a BFGS-like algorithm using the convolutional structure. Although this is not my area of expertise, my understanding is that specialized approaches for deblurring using convolutional preconditioners exist, see for example [the work of Eboli et at.](https://arxiv.org/pdf/2007.01769). A discussion of, and a comparison with, specialized algorithms would be a welcome addition.

### Questions
## Smaller concerns

- **BGD assumption** Please correct me otherwise, but the "Better than Gradient Descent" (BGD) is assumed rather rather than proved, and theorem 2 both uses that $t \to \infty$ while requiring a final training iteration $T$. These two statements seem contradictory? 
- The BGD assumption seem unecessary for the unseen problem proof? A similar argument could be made without the $t \to \infty$ or BGD assumption if the preconditioner is PD. For a given training budget, the algorithm repeats the last learned preconditioner $G_{\theta_{T-1}}$, so it will eventually converge on any unseen function that is smooth relative to $G_{\theta_{T-1}}$ in the sense that $\nabla^2 f(x) \preceq [G_{\theta_{T-1}}]^{-1}$. This doesn't seem much weaker than the current proposition, which only guarantees that there exists a smoothness constant $\tilde L$ such that the algorithm will convergence on $\tilde L$-smooth functions.

- **Related work in optimization**: The discussion of related work in optimization only touches on L-BFGS and ignores relevant work that attempt to achieve a similar goal, "find a better step-size/preconditioner for the problem", but by running additional computation before/while solving the problem rather than by taking the learning to optimize approach. While the approaches are different, this literature should at least be acknowledged in a paragraph in the introduction as it shares a similar goal. Examples include a simple [Armijo line-search](https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-16/issue-1/Minimization-of-functions-having-Lipschitz-continuous-first-partial-derivatives/pjm/1102995080.full), 
[optimal diagonal preconditioners](https://arxiv.org/abs/2209.00809) for quadratic, 
[AdaGrad](https://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf) and [adaptive bound optimization](https://arxiv.org/abs/1002.4908) for convex non-smooth functions, [multidimensional Armijo](https://arxiv.org/abs/2306.02527) for smooth strongly convex functions, or [parameter-free methods in online learning](Coin Betting and Parameter-Free Online Learning).


## Questions

- Please clarify what is meant by "maintaining constant memory usage" and "memory is constant with increasing training iteration". My understanding of the algorithm is that the methods learns a different preconditioner for each iteration. This scales at least linearly with the number of training iterations. A more detailled explaination of where the memory is used and how it differs from the unrolling strategy would help.

- I don't understand Eq. 16. What is $B_k$? Equation (14) treats both $G_\theta$ and $B_k^t(\tehta)$ as equations of $\theta$, which makes 

## Minor

- Proposition 1 & 2 are missing the assumption that no entries of $\nabla f(x)$ is $0$. It is possible for the $j$th entry of $\nabla f(x)$ to be 0 while having $x[j] \neq x^*[j]$ where $x^* \in \arg\min_x f(x)$.

### Soundness
2

### Presentation
2

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
This paper proposed a novel L2O approach for inverse problems. To mitigate the computational challenges in current approaches in L2O, which are mostly based on unrolling, this paper investigate a greedy training approach which decouples the iterates leading to more efficient training. The proposed scheme provides an effective approach for training a preconditioner for gradient descent. Theoretical analysis demonstrate that the proposed preconditioned gradient descent converges under the BGD condition. A specialized parameterization using convolution has been proposed in the paper which is tailored for imaging applications. Numerical experiments on inverse problems have demonstrated superior performance over classical methods such as Nesterov's accelerated gradient and L-BFGS.

### Strengths
The greedy training approach is a novel and interesting scheme for L2O. Indeed, current L2O methods are mostly depending on unrolling several iterations, the proposed scheme is very timely for L2O area for scalability of training the optimizer.

The numerical performance of the proposed scheme on inverse problems is very impressive.

### Weaknesses
The theoretical part of the paper remains a concern. The convergence analysis relies on the BGD (better than gradient descent) assumption, which is not sufficiently justified. While the authors claim that the learned preconditioner satisfies this property, the BGD assumption is not a property that can be trivially assumed; it should depend on the specific parameter values learned during training. The fact that the learned preconditioner *can* satisfy this property does not mean that it *will* satisfy it in all cases, and this requires more rigorous justification. The convergence proof hinges on this assumption, making the theoretical guarantees weak. The claim in Corollary 1, which states convergence under certain conditions, is not sufficiently supported by the provided proof. The connection between Lemma 2 and Corollary 1 needs to be made more explicit, as it is not immediately clear how the continuity established in Lemma 2 directly leads to the convergence claim in Corollary 1. The reviewer still believes that showing the learned linear preconditioner is BGD is non-trivial and requires more than just stating that it can be satisfied by design. The "with Convergence Guarantees" part of the claimed contribution is still not fully convincing.

In terms of further development, the inability to learn iterative schemes that utilize memory of past iterates remains a significant limitation. While the authors' greedy approach allows for training over many iterations, it does so at the cost of losing the ability to model momentum or other memory-based optimization strategies. This is a clear advantage of unrolling-based methods that should be acknowledged more explicitly. The reviewer believes that a hybrid approach, combining the proposed greedy scheme with unrolling, could potentially yield better performance by leveraging the strengths of both methods.

In terms of experiments, while classical hand-crafted optimizers are included as baselines, the lack of comparison with other existing L2O methods is a significant oversight. The paper should include a comparison with state-of-the-art (truly) provably convergent methods, such as the one by Banert et al. [1].

### Questions
As mentioned above, please clarify the doubts regarding the theoretical analysis and include comparision with existing provable L2O schemes.

Meanwhile, the proposed scheme is tailored for inverse problems in imaging, particularly the convolutional parameterization of the preconditioner -- should this be make clearer in title/abstract/introduction?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes a provably convergent learning-to-optimize method based on preconditioned gradient descent. By considering gradient descent and regularizing the proposed algorithm such that it is majorized by and eventually becomes GD, they demonstrate significant speedups on various convex optimization problems, while maintaining provable convergence guarantees from GD. Moreover, the linear parameterization allows for convex solvers at each timestep which gives speedup compared to other L2O methods.

### Strengths
* The paper reads well and the theorems are very intuitive. Overall, a good submission to ICLR.
* The experiments are convincing and the details are very comprehensive. The speed of training is especially good due to the simple parameterization, and comparisons are made with the greedy training vs standard unrolled training.
* The clear structure of the learned kernels (e.g. Figure 1c, 5c) is good cause for further investigation towards optimal preconditioning for certain imaging problems.

### Weaknesses
 * The theory seems to require the knowledge of the maximum Lipschitz constant over all training examples in its regularization. How well does the method work when applied to problems with large or unknown constant?
* Related: finding the regularization parameter $lambda_T$ as in p.18 seems arduous. Is this done at every iteration $t$, and how many problems need to be solved to find $\lambda_t$? It seems also that the condition for choosing $\lambda_t$ gives that $G_\phi$ is positive definite, which is confusing with the initial claim that the method converges for non p.d. conditioners.
* While stepsize $\tau = 1/L$ does indeed give convergence for NAG, in practice, the smoothness is unknown and larger step-sizes can be taken while maintaining empirical convergence. Same for L-BFGS. Since the convergence profiles are quite similar, a proper comparison with differing parameters for NAG and L-BFGS would greatly help in ascertaining the role of interacting pixels in helping optimization.
* (l.327) Should this be (PC) instead of (PP)?
* How are the ground truths $x^*$ computed?
* While the linear parameterization should give minimal overhead, a wall-clock time comparison of test-time might be useful for further comparison.
* For quadratic problems, Tan et al. (2023b) consider the preconditioning $G = (A^* A)^{-1}$, which can be used to motivate the convolutional structure. How does the proposed method compare to perhaps a regularized version, say $(I + \delta^{-1} A^* A)^{-1} \approxeq I - \delta A^\dagger A^{*\dagger}$. I am not sure if this is available in standard libraries.
* The convolution-based preconditioner seems to generalize something called "Laplacian smoothing gradient descent" (Osher et al., 2022). Have the authors considered other possible instances of such linear preconditionings that may have better empirical performance?
* Related: perhaps a short reference to App. D.2 would be helpful in the main text, as the choice of full-image convolution is not motivated.
* (l.737) RHS of first inequality should be $g_{t,0}(\tilde{\theta})$, and $\nabla f_k$ on the second line. Proof of Thm 1 perhaps needs a short clarification on telescoping arguments (relating objective of $x_{t+1}$ in terms of $x_t$) since $x_t$ is not generated using GD, but the result should be the same.
* Prop 4 can be more proved more succinctly by noting the residual of $F$ is the average of residuals of $f_k$, which are non-negative, so $f_k^t - f_k^* \le N F_t - F^*$.
* Prop 5 can directly use coordinate projection and remove the elementary calculation: consider the convex function $\pi_i f$ and first-order optimality, clearly minimized at $x^*$ and with derivative equal to $[\nabla f]_i$.
* Proof of Lem 1: notation from $g_{t,\lambda_t}$ to $g_t(\cdot, \lambda_t)$. Inconsistency in the first inequality with definition of BGD: should be $g_t(\theta_t, \lambda_t) \le g_t(\tilde{\theta}, 0)$.
* Line 40: perhaps reference Theorem 1 here when claiming that the sums of the $f_k$ converge to the optimal values.

### Questions
* (l.327) Should this be (PC) instead of (PP)?
* How are the ground truths $x^*$ computed?
* While the linear parameterization should give minimal overhead, a wall-clock time comparison of test-time might be useful for further comparison.
* For quadratic problems, Tan et al. (2023b) consider the preconditioning $G = (A^* A)^{-1}$, which can be used to motivate the convolutional structure. How does the proposed method compare to perhaps a regularized version, say $(I + \delta^{-1} A^* A)^{-1} \approxeq I - \delta A^\dagger A^{*\dagger}$. I am not sure if this is available in standard libraries.
* The convolution-based preconditioner seems to generalize something called "Laplacian smoothing gradient descent" (Osher et al., 2022). Have the authors considered other possible instances of such linear preconditionings that may have better empirical performance?
* Related: perhaps a short reference to App. D.2 would be helpful in the main text, as the choice of full-image convolution is not motivated.
* (l.737) RHS of first inequality should be $g_{t,0}(\tilde{\theta})$, and $\nabla f_k$ on the second line. Proof of Thm 1 perhaps needs a short clarification on telescoping arguments (relating objective of $x_{t+1}$ in terms of $x_t$) since $x_t$ is not generated using GD, but the result should be the same.
* Prop 4 can be more proved more succinctly by noting the residual of $F$ is the average of residuals of $f_k$, which are non-negative, so $f_k^t - f_k^* \le N F_t - F^*$.
* Prop 5 can directly use coordinate projection and remove the elementary calculation: consider the convex function $\pi_i f$ and first-order optimality, clearly minimized at $x^*$ and with derivative equal to $[\nabla f]_i$.
* Proof of Lem 1: notation from $g_{t,\lambda_t}$ to $g_t(\cdot, \lambda_t)$. Inconsistency in the first inequality with definition of BGD: should be $g_t(\theta_t, \lambda_t) \le g_t(\tilde{\theta}, 0)$.
* Line 40: perhaps reference Theorem 1 here when claiming that the sums of the $f_k$ converge to the optimal values.

[1] Osher, S., Wang, B., Yin, P., Luo, X., Barekat, F., Pham, M., & Lin, A. (2022). Laplacian smoothing gradient descent. Research in the Mathematical Sciences, 9(3), 55.

### Soundness
4

### Presentation
3

### Contribution
3
