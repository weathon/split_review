# Characterizing ResNet's Universal Approximation Capability

- Decision: Reject
- Scores: 6, 8, 3, 8

## Abstract
Since its debut in 2016, ResNet has become arguably the most favorable architecture in deep neural network (DNN) design. It effectively addresses the gradient vanishing issue in DNN training, allowing engineers to fully unleash DNN's potential in tackling challenging problems in various domains. Despite its practical success, an essential theoretical question remains largely open: how well can ResNet approximate functions? In this paper, we show that ResNet with bottleneck blocks (b-ResNet) can approximate any $d$-dimensional monomial with degree $p$ to any accuracy $\epsilon>0$ with $\mathcal{O}(dp\log (p/\epsilon))$ number of weights and we extend the results to polynomials, smooth functions, continuous functions. This is a factor of $d$ reduction in the number of training weights compared with the classical results for ReLU feedforward networks. Our results reveal that a continuous-depth network generated via a dynamical system possesses significant approximation capabilities even if its dynamics function is realized by a shallow ReLU network with absolute constant neurons. Furthermore, our achievability result is order-optimal in terms of $\epsilon$ as it matches the generalized lower bound. Besides, we apply ResNet can approximate a special function class based on Kolmogrovo Superposition Theorem with $\mathcal{O}(d^4\epsilon^{-1})$ tuning weights to overcome the curse of dimension. This work adds to the theoretical justifications for ResNet's stellar practical performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims to provide a theoretical understanding of the expressive power of Resnets. The authors study this question w.r.t. function approximation. They first start with d-dimensional monomials of degree p, then they study smooth functions that are differentiable up to degree r, and they also provide a class of lower bounds. Their main results are to derive bounds on the number of tunable weights needed or sufficient for the function approximation. The authors' results showcase the benefits of ResNets compared to ReLU nets in terms of necessary tunable weights. 

The main idea behind the results is to show a connection between ResNets and their feedforward counterparts. The authors show that ResNets can be viewed as a sparse FNN. The authos also provide specific constructions that show how to approximate classes of functions mentioned before with a bounded (and they provide the bounds) number of tunable weights.

### Strengths
+well-motivated question about the theoretical properties of ResNets

+clean results in that the bounds are interesting

### Weaknesses
Overall i like the paper however, I find the most important weakness to be w.r.t. novelty and technical innovation.

-the main concern is that many of the ideas/constructions upon which the paper relies to prove their results have been known in prior works. This is the case with the proposed lower bound for example. The most interesting observation I would say is the implementation of quadratics "x^2" and product "xy" using ResNets, but I don't find this contribution enough for ICLR.

### Questions
Q: A related interesting question is about the depth-width tradeoffs for ResNets. Perhaps this is something that follows from your work on just the tunable weights, but as far as I can tell it's not obvious. Given that there are many results for FNNs and their depth/width tradeoffs,  I believe it is important to highlight this too.

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
The paper studies approximation properties of residual networks under usual assumptions. Given a function space, input dimension, and a precision requirement, upper and lower bounds on the number of parameters of a ResNet architecture are studied. These bounds are derived to ensure the function family parameterized a ResNet architecture is dense in the function space under the supremum norm. By extending a result by Yarotsky (2017), a lower bound for the size of a ReLU network which approximates a multivariate product function is first derived. Since there is always a ReLU network which represents a ResNet, a lower bound in ReLU networks also serves as a lower bound for ResNets. As the family of multivariate product function is a subset of polynomials, the lower bound derived is also applicable to polynomials. Then, upper bounds are derived for monomials, which is smaller by a factor of input dimension d compared to the upper bound on the family of ReLU networks. Next, the bound is extended to polynomials and the Sobolev space. The bound is also smaller by a factor of d compared to the one on ReLU networks. Finally, it was shown that any continuous piecewise linear function can be approximated by a ResNet with width $(d+1)$ when the depth $L$ is large enough. Then, the authors argue that ResNets can approximate any continuous function. A relation between ResNets and dynamic systems is also studied. By limiting the regularity of the outer function of the Kolmogorov representation of a continuous function, the authors show that any function in this special family can be approximated by ResNets in the uniform norm.
In addition to the above theoretical results, the authors also demonstrate the approximation ability of ResNets by changing their size in computer simulation where mean squared error is used to measure the approximation capability.

### Strengths
- Originality: Most existing approximation bounds are derived for networks without skip connections. Hence, the proposed upper and lower bounds are novel in the sense that they are tailored to the ResNet architecture.

- Quality and clarity: This paper gives a comprehensive presentation on the approximation properties of ResNet. The background knowledge is well-organized, and the theoretical results are presented in a flow that is easy to follow and understand.

- Significance: ResNet is an important architecture and understanding its approximation limitations and abilities is crucial.

### Weaknesses
1. The upper bounds for monomial and polynomials (Theorem 3 and 4) in this paper are not surprising in the sense that any layer in a ReLU network can be configured to implement a d-dimensional identity function if the width is sufficiently large. Since a $d$-dimensional identity function can be represented by a layer of $2d$ ReLU units, a smaller upper bound (for approximating monomials) by a factor of $d$ is expected. The upper bound given in Theorem 5 is the same as the bound given in Theorem 1 by Yarotsky (2017). Although this is for ResNet, it is not surprising using the above argument. The large constant d is also hidden in the big O notation. This piece of result can be more interesting if the authors can show the dependency on d explicitly and demonstrate that it is also some factors of reduction similar to case of monomials. 

2. For the lower bound (Theorem 2), it is not very useful given the product function is limited. The authors give a comprehensive discussion but the result extending this bound to the space of continuous functions is missing. It is good to discuss existing results, but a comparison is expected.

3. In Theorem 6, the upper bound for approximating continuous functions grows with the input dimension given that the width is bounded by $(d+1)$, provided the depth is sufficiently large. Such dependency on the input dimension is usually not friendly given that many neural networks in applications directly work on raw data. A dimension-independent bound (reference below) can be derived when the number of pieces in the continuous piecewise linear function is known.

>Chen, Kuan-Lin, Harinath Garudadri, and Bhaskar D. Rao. "Improved bounds on neural complexity for representing piecewise linear functions." Advances in Neural Information Processing Systems 35 (2022): 7167-7180.

4. On the other hand, the depth is not explicitly given in the theorem, which even reduces the significance of the statement. It would be clearer if the authors could explain this missing part in the discussion following Theorem 6.

5. The function space considered in Theorem 8 is very limited. Such a space is even smaller than the space used by Theorem 4.1 in the following paper.

>Montanelli, Hadrien, and Haizhao Yang. "Error bounds for deep ReLU networks using the Kolmogorov–Arnold superposition theorem." Neural Networks 129 (2020): 1-6.

6. In the above paper, the space of functions is defined based on the refinement levels of the inner functions which can be used to bound the Lipschitz constant of the outer functions. However, Theorem 8 directly limits the Lipschitz constant of the outer function. This assumption is unrealistic, and it avoids the main difficulty in approximating the outer function.

6. Since the approximation quality is measured by the uniform norm, it seems not reasonable to measure the mean squared error. Measuring the maximum error could be more convincing.

### Questions
1. In the second paragraph after Proposition 1, can one of the $\alpha_i$ be 0?

2. It would be clearer if the authors can state that this paper only discusses bounds under the uniform norm. Would it be possible to derive tighter bounds under $L^2$ norm for ResNet?

3. The variable d is missing in the last sentence of Theorem 3.

4. Theorem 5. There is a ResNet R that can … A word is missing.

5. The paragraph following Theorem 5, please clarity that the bound is nearly tight up to a log factor of epsilon.

6. The statement after “Thus” of Theorem 6 is incomplete.

7. The last paragraph on page 7. Can you provide some references to justify why ResNet has superior optimization performance? Do you mean by the ability to improve representation? Are there any guarantees?

8. The authors claim that experiment results show the exceptional approximation capability of ResNet for learning complex functions. Can you evaluate the trained ResNets using the maximum errors?

9. It would be clearer if the authors can emphasize in the conclusion that the class of smooth functions is a limited class.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to extend e Lin & Jegelka (2018) which shows that ResNet with single-neuron can approximate any step function to approximate any CPwL function. Thus ResNet can become an optimal approximator.

Reviewer's concern is mostly the relationship between the submission with [1] (seems not cited and discussed in the paper). All the two papers are based on spline approximation and result in an O(1) channel ResNet. From the reviewer's perspective, it's essential to discuss different dependencies of dimension and differences in the structure before the paper is accepted.

The reviewer is open to increasing the score if this problem can be resolved during the interactive review process of ICLR. 

[1] Oono, Kenta, and Taiji Suzuki. "Approximation and non-parametric estimation of ResNet-type convolutional neural networks." International conference on machine learning. PMLR, 2019.

### Strengths
Solid and well-written paper, construct a practical resnet with optimal apprxoimaton ability.

### Weaknesses
See above. missing literature and the comparison to the previous work.

### Questions
See above

### Soundness
3 good

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors clearly and correctly derive quantitative universal approximation guarnatees for the ResNet architecture.  Furthermore, they exhibit a class which can be efficiently approximated (i.e. without the curse of dimensionality) using the ResNet model.

### Strengths
The results are very interesting, definitely publishable, and I will likely be using/quoting them myself in the near future ;).  Thanks for the very nice contribution :)

Personally: I was looking for such a result in the literature, so I must say I'm happy its added.  Good work!

### Weaknesses
 **1) Lack of Explanation in the "Perspectives on the Curse of Dimensionality" paragraph need clarification/explanation/motivation.**

The way this section is written leaves the reader, not familiar with constructive approximation in the dark, thinking some "magic is happening" where "there be dragons".  Worry not!, here is how to fix this issue:

1. the curse of dimensionality is not only something that MLPs experience, but every (reasonable) class of function approximators which are uniformly approximating in the Lipschitz ball on some compact subset of a metric space.  Indeed, this is due to metric entropy limitations and the result is essentially due to Kolmogorov [1].  I think the authors should add 1 sentence at the end of page 2 to explain how this is a **generic** problem, and that the reader should expect this to **always** be the case.

2. By the same token as (1), above, the reason which people consider speacialized classes of functions as a viable way to circumvent the curse of dimensionality is again rooted in metric entropy number arguments.  Indeed, [1] or even [2] show that the metric entropy (which is a non-linear notion of comprehensibility of a function class), or even linear notions such as Kolmogorov linear widths, are not cursed by dimensionality for smooth classes.  Indeed, the metric entropy of the unit ball in $C^k$ wrt the uniform topology is $\Theta(\varepsilon^{-r/d})$ so one can expect that the optimal (non-linear) approximator can achieve such rates.  These ideas should be communicated to the reader atop page $3$ so that it does not seem that consider "special functions classes" is a "magic trick" :)

Fyi, the relationship between linear and non-linear measures of compressibility (the above which I mention) are given by Carl in their wonderful paper [3].

3. There similar reason justified why the MLPs with super expressive activation in the following paragraph.  Namely, due to the (near) discontinuity of these classes, as a function of their parameters.  See [4].  So again, there is a simple, conceptual explanation for why these approaches work, but also why they should not be employed (since beating the curse of dimensionality in this way is only possibly by models whose input-output relation changes chaotically if the training data is perturbed only a tiny bit, since minor parameter changes result in dramatically different functions.  For instance, this is very clear in Theorem 1 of [5].

I strongly feel that, points 1-3, should be communicated to the reader.  Albeit more conclusively due to the page limitations, if one even considers embarking on a meaningful discussion on the curse of dimensionality, and why/how it can be beaten.  More critically, the authors should, in such a discussion, highlight the reproductions of beating it; namely: the choice between an unstable model class (in its parameters) or a restriction of the functions which can be effectively approximated.


-----

**2) Suboptimal Rates Due to Polynomial Approximation and Not Quantization**

The proof strategy is akin to [6] (or its quantitative version in Proposition 53 - [7]) where one first approximates polynomials using the network class (here ResNet and in those papers deep but narrow MLPs), then one concludes by relating the polynomials to the target function being approximated (e.g. via quantitative Stone-Weirestrass theorems using Bernstein polynomials).  However, due to the "triangle inequality"-based argument these rates are suboptimal compared to the more modern quantization-based arguments of [8] which are possible for structures with recurrence/depth like MLPs ResNets.  For this reason, the rates which the authors derive are suboptimal by an exponential factor of $1/2$.

For example, in Theorem 3.3 [9], the author exhibits the existence of an MLP with ReLU activation achieving the optimal (with the optimality given, for example, by Theorem 3.1 [9] ) depth of $\mathcal{O}(\varepsilon^{-r/(2d)}$ is required to approximate any function in the unit ball of $H^r$ (as opposed to the current manscript's ResNet guarantee of $\tilde{\mathcal{O}}(\varepsilon^{-r/d})$.

** 3) Minor Comment(s)**

Some figures, e.g. Figure 6 in the appendix, seem not be expored as pdf or eps files making them pixelated.  Please fix this.

### Questions
1. Can you please incorporate the discussion I added above, in the weaknesses.  I think the explanation of the curse of dimensionality is not satisfactory nor insightful, but it can be made 100% by adding the above points.

2. Why not deploy the quantization argument of [8] instead of approximating polynomials as in [6] (or its quantitative version in Proposition 53 of [7])?  

That said, changing this is not feasible/worth it at this point, so I think its appropriate if the authors comment on this point.  Since, it is at the core of providing rates in their main results.  


-- Reused references as Weaknesses section - In respective order -- 

[6] Kidger, Patrick, and Terry Lyons. "Universal approximation with deep narrow networks." In Conference on learning theory, pp. 2306-2327. PMLR, 2020.

[7] Kratsios, Anastasis, and Léonie Papon. "Universal approximation theorems for differentiable geometric deep learning." The Journal of Machine Learning Research 23, no. 1 (2022): 8896-8968.

[8] Shen, Zuowei, Haizhao Yang, and Shijun Zhang. "Optimal approximation rate of ReLU networks in terms of width and depth." Journal de Mathématiques Pures et Appliquées 157 (2022): 101-135.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
