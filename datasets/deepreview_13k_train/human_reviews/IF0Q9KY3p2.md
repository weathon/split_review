# Implicit Bias of Mirror Descent for Shallow Neural Networks in Univariate Regression

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
We examine the implicit bias of mirror flow in univariate least squares error regression with wide and shallow neural networks. For a broad class of potential functions, we show that mirror flow exhibits lazy training and has the same implicit bias as ordinary gradient flow when the network width tends to infinity. For ReLU networks, we characterize this bias through a variational problem in function space. Our analysis includes prior results for ordinary gradient flow as a special case and lifts limitations which required either an intractable adjustment of the training data or networks with skip connections. We further introduce \emph{scaled potentials} and show that for these, mirror flow still exhibits lazy training but is not in the kernel regime. For networks with absolute value activations, we show that mirror flow with scaled potentials induces a rich class of biases, which generally cannot be captured by an RKHS norm. A takeaway is that whereas the parameter initialization determines how strongly the curvature of the learned function is penalized at different locations of the input space, the scaled potential determines how the different magnitudes of the curvature are penalized.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the implicit bias of mirror flow on shallow univariate neural networks in the standard parameterization. The authors show that the networks are in the lazy regime (only the second layer weights move non-negligibly), and characterize the representation norm in two different regimes. In the "unscaled" regime, the mirror map plays a minor role, only through its Taylor expansion around 0, leading to an NTK-like implicit bias similar to GD. In the "scaled" regime, where the potentials are rescaled by width, a richer implicit bias arises involving the corresponding Bregman divergence, which is no longer a RKHS norm.

### Strengths
The paper is well written, and the obtained implicit bias results for scaled potential is quite interesting as it involves new norms that have not been used before in the context of neural networks, to my knowledge.

### Weaknesses
The significance is unclear: while the obtained norms are interesting, it is unclear if mirror flow is a relevant method in the study of neural networks. The lazy training regime suggests that it may be good to reframe the paper more generally outside of neural networks (which in practice are often in non-lazy regimes), for instance mirror descent on random features models, which could be of interest to the statistical learning and kernels community more broadly. The analysis is also somewhat incremental over existing implicit bias results. Specifically, the paper's analysis of the lazy regime, while technically sound, largely reproduces known results for gradient descent in the neural tangent kernel (NTK) limit. The extension to scaled potentials, while introducing Bregman divergence-based norms, still operates within a lazy training framework, limiting its applicability to more practical, feature-learning scenarios. The connection between the derived implicit bias and practical performance of neural networks remains tenuous, making the overall impact somewhat limited.

### Questions
* Given that the networks are in lazy regimes and similar to random feature models, is the setting related to this paper on random feature models with Lp penalties on the weights? https://arxiv.org/abs/2103.15996

* Do you have a sense of whether such mirror flow analyses extend to feature learning regimes, e.g. by switching to a mean-field parameterization? What would be the resulting implicit bias?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper establishes various implicit biases for wide shallow networks trained via mirror flow in the context of univariate regression which roughly fall into two categories: (i) parameters do not move far from initialization while asymptotically minimizing risk (ii) the asymptotic solution (asymptotic with respect to time) can be characterized via a variational problem.

### Strengths
Characterizing the asymptotic solution of mirror flow via a variational problem is interesting.

### Weaknesses
The work only considers univariate models.


minor comment:
Considering the work only deals with mirror flow, I believe the title should be remedied to "Implicit bias of Mirror Flow ...".

### Questions
1) All the convex potentials bake in the initial parameter $\hat \theta := \theta_0$. I wonder how much of the implicit bias results are affected by the choice of $\hat \theta$. If $\hat \theta$ was arbitrary (or any point other than $\theta_0$), how do the lazy training results change (i.e. is it still true that the parameters do not move far from initialization)? Of course when the coordinate function $\phi(x) = \frac 1 2 x^2$ (i.e. GF), the choice of $\hat \theta$ does not matter but for $\phi(x) = x^2 + x^4$, the mirror flow update explicitly penalizes movement away from $\hat \theta$ and hence it less clear whether lazy training should occur. 

2) Why is the mirror flow update scaled by $\eta$? Do similar results hold if $\eta$ is dropped?

3) Is the restriction to the univariate case only needed for the variational characterization of the asymptotic solution? 
(i.e. can the univariate requirement be dropped for establishing lazy training results and risk minimization?)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the implicit bias of mirror flow in univariate two-layer networks in the lazy regime. For a broad class of potential functions, they show that the implicit bias at the limit of infinite width is similar to the implicit bias of mirror flow. They also provide a characterization of this implicit bias in function space which generalized prior results. Moreover, they introduce scaled potential functions, where training is in the lazy regime but not in the kernel regime, and characterize its implicit bias.

### Strengths
The implicit bias of mirror descent/flow has been studied mostly for linear models. Here, the authors extend our understanding of mirror flow to the case of univariate two-layer networks in the lazy regime, and also give a more precise characterization of the implicit bias in function space for gradient flow in this setting. I think that the contribution is of interest to the implicit bias community, and continues two lines of work: the works on the implicit bias of mirror descent, and the works on the implicit bias of univariate shallow networks.

I believe that the contribution is significant and hence recommend acceptance.

### Weaknesses
It would be nice to extend Theorem 2 beyond Assumption 1, which restricts the class of potential functions covered here, and also to relax the many assumptions in Theorem 8. Specifically, Assumption 1 requires the potential to be a sum of functions of the difference between the current and initial parameters, which is a strong constraint. It would be beneficial to explore if similar results can be obtained for more general potential functions, such as those that depend directly on the parameter values without the shift by the initial value. Similarly, the assumptions in Theorem 8, while necessary for the proof, limit the applicability of the result. For instance, the requirement of a specific initialization scale and the boundedness of the parameter space might not hold in all practical scenarios. Relaxing these assumptions would significantly broaden the scope of the theorem and make it more useful for a wider range of problems.

### Questions
In both Theorem 2 and Theorem 8:
“with high probability over the random parameter initialization,
there exist constants C_1, C_2 such that …”. It sounds like the constants C_1,C_2 may depend on the initialization (which also depends on n). Did you mean to write “there exist constants C_1, C_2 such that w.h.p. over the initialization …”?

### Soundness
4

### Presentation
4

### Contribution
3
