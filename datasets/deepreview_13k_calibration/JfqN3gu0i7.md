# The optimality of kernel classifiers in Sobolev space

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Kernel methods are widely used in machine learning, especially for classification problems. However, the theoretical analysis of kernel classification is still limited. This paper investigates the statistical performances of kernel classifiers. With some mild assumptions on the conditional probability $\eta(x)=\mathbb{P}(Y=1\mid X=x)$, we derive an upper bound on the classification excess risk of a kernel classifier using recent advances in the theory of kernel regression. We also obtain a minimax lower bound for Sobolev spaces, which shows the optimality of the proposed classifier. Our theoretical results can be extended to the generalization error of overparameterized neural network classifiers. 
To make our theoretical results more applicable in realistic settings, we also propose a simple method to estimate the interpolation smoothness of $2\eta(x)-1$ and apply the method to real datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers estimating classifiers in the interpolation Sobolev RKHS. They have two theoretical contributions: (a) the lower bound on the excess risk and (b) the upper bound of the same at the t-th iterate. They apply this results to a neural network which can be approximated by a neural tangent kernel. The optimal rate depends on the smoothness of the optimal classifier, larger smoothness leading to faster convergence. They propose a truncation strategy for estimation of the smoothness, which when applied to real datasets corraborates the estimated smoothness with the difficulty of the dataset.

### Strengths
The paper is well written and easy to follow. The main results seem novel for the setup considered. The association of the estimated smoothness to the difficulty of the datasets is interesting.

### Weaknesses
see questions.

### Questions
-- Not very clear how the arrived results compare against the existing work on NTK. Would be interesting to understand that to appreciate the impact of the contributions
-- It is not very clear about the impact of this work from an application front. The experiments to real datasets are restricted to estimation of the smoothness. Some insights would be helpful in this regard. How to enforce learning estimators constrained with a requirement on the smoothness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work shows the minimax optimality of kernel classifiers in Sobolev spaces and extends the theory to neural network classifiers through the connection between neural networks and neural tangent kernels. The paper also shows the error rate depends on the data smoothness. Thus the paper proposes a practical approach to estimate such data smoothness, helping us understand how hard it will be to model the data accurately.

### Strengths
* Studying the optimality of kernel classifiers is a fundamental problem in machine learning. 
* The theory in this paper has the potential to guide the practice of kernel learning and neural networks.

### Weaknesses
The primary concern regarding this paper is that the established minimax optimality for kernel classifiers relies on the gradient flow algorithm, which is mainly based on the L2 loss and is not commonly used in practical applications of building kernel classifiers. While the minimax rate is established, its optimality is only proven in an asymptotic sense, leaving a considerable gap between theory and practical usage. This approach is natural in the existing work when building the minimax rate for kernel classification, but not for the kernel classification. The paper's contribution would be more significant if the theoretical framework were based on widely used classifiers, such as SVM and logistic regression.

A similar issue arises with the application of kernel classifier theory to neural networks, particularly those employing the L2 loss for fitting. Despite the L2 loss being effective in various neural network scenarios, the paper would benefit from incorporating theories that utilize loss functions more prevalent in practice.

An additional point of concern is that the paper's main theoretical underpinnings are based on unpublished works, specifically referenced as https://arxiv.org/abs/2305.07241. The validity and proofs presented in that work have not been verified in this review.

### Questions
After estimating the smoothing parameter, can we further gain some insight into the optimal steps in the gradient flow algorithms? It would be helpful if some numerical studies can be performed to support this.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper shows that a variety of kernel regression methods known as spectral algorithms achieve optimal convergence rates for binary classification when the conditional probability function $\eta$ stems from a Sobolev space. The authors also apply this theory to neural tangent kernels. Finally, the paper provides a simple (but not theoretically analyzed) method for estimating the smoothness of the conditional probability function $\eta$ from a data set, which is applied to standard image classification data sets.

### Strengths
The paper has a relatively clear message, and I think the paper is relatively well-written. I guess that the upper bound on the convergence rate in Theorem 2 should be a relatively direct corollary from Fischer and Steinwart (2020) in the special case of ridge regularization, but the authors formulate a more general result for spectral algorithms that also holds for gradient flow. The lower bound in Theorem 1 nicely complements the upper bound. While the square loss is not very common for classification, it is still noteworthy that optimal rates can be achieved with any loss.

### Weaknesses
The application to the NTK looks nice, but I have some concerns that Assumption 3 cannot be verified for a good $\alpha_0$, see the major comments below.

While the smoothness assumption on $f^*$ seems less natural to me in the classification setting, the authors provide interesting experiments that appear to show that this assumption is appropriate. However, I have doubts that the proposed (and not theoretically justified) estimator can really estimate what it is supposed to estimate, see the major comments below.

Overall, the aforementioned concerns hold me back from recommending acceptance at the moment, but I am ready to adjust my score if these concerns can be addressed.

### Questions
**Questions**:
(1) Does ridge regularization also qualify as a spectral algorithm? And what about gradient descent?

(2) Could the results be generalized to multi-class classification? I am also wondering about other loss functions, but the Brier score should be trivial and the log-loss should require additional modifications.

**Major comments**:
(3) Before Corollary 1: While NTKs are dot-product kernels on the sphere, they are not in general dot-product kernels outside of the sphere. For example, from Eq. (15) we have $K_{ntk}(0, 0) = 1$, which means that $K_{ntk}$ cannot be a dot-product kernel. On the other hand, I also don't see why you would need it to be a dot-product kernel for Corollary 1.

(4) In Theorem 2, you seem to implicitly assume that $\alpha_0 = 1/\beta$, see the text before Eq. (14) in the appendix. Please state this in the theorem. Moreover, it is not clear to me that this would also hold in the setting of Corollary 1 for general domains. In the special case of the sphere, this could be fixed at least for very similar network architectures because then the RKHS of the NTK is known to be a Sobolev space, see for example the proof of Theorem G.5 in https://arxiv.org/abs/2305.14077

(5) I am not fully convinced by the proposed smoothness estimator. For example, assume that the target function $f^*: \mathbb{R}^2 \to \mathbb{R}$ has different degrees $s_1$ and $s_2$ of (Sobolev) smoothness in dimensions $1$ and $2$. Then, I would expect the eigenvalues to decay at different rates depending on the direction that the eigenfunctions are more refined in, such that the eigenvalues in a plot as in Figure 1 (a) wouldn't lie on a single line but in between two lines corresponding to $s_1$ and $s_2$. Linear regression would then estimate a smoothness between $s_1$ and $s_2$, but in terms of interpolation spaces, the function would still only lie in the interpolation space with the lower smoothness. (This could be checked by just plotting the $p_j$ on the image data sets.) 

Perhaps this issue could be "fixed" by performing linear regression on top of $\tilde p_j := \sup_{k \geq j} p_k$, which would try to filter out the "upper line" in the plot, but also potentially it could be more susceptible to noise. (Judging from the plots, perhaps it could be a good heuristic to automatically set the threshold in a way that only those $p_j$ are included that are larger than the maximum in the right half of the plot.) Another idea for the estimator would be to stay closer to the definition of interpolation spaces and work with (approximations of) the interpolation space norms of the regression function, maybe something like finding an "elbow" in $s \mapsto y^\top (K + \lambda I)^{-1} K^s (K + \lambda I)^{-1} y$.

Besides the mixed smoothness case, another important case is the "manifold assumption" case where $\mu$ is supported on a submanifold, and which is a popular assumption for image data sets. I am wondering whether the estimator can be trusted in this case.
Another potential test case is what happens if the classes are well-separated and non-noisy, i.e., with $\eta(x) \in \{1, -1, \text{undefined}\}$. This is arguably close to the situation for MNIST. Can the estimator find out that the function is arbitrarily smooth?
In general, it would be interesting to see whether the rates predicted by the theory and the simple estimation method hold up in a practical setting.
(I'm brainstorming a bit here, it is not necessary to try everything in order to address my comment.)

**Minor comments**:
- p. 1: Use \operatorname{sign} or something like this to set the sign operator in non-italic font. (same for later)
- "trained via the gradient flow" -> "trained via gradient flow"
- Sec 1.1 i) "bounded by $...$" there should be a constant $C$ or an O-notation in there.
- Please don't use all-caps for author names in citations (STEINWART & SCOVEL, 2007).
- p. 3: "Recently, Deep" -> "Recently, deep"
- "gained incredible success" -> "achieved incredible success" or so?
- "Another reason we choose" -> "Another reason why we choose"?
- "spectra algorithm" - should this be "spectral algorithms"? (also further below)
- Same paragraph (last paragraph of Sec. 1): When you say "Another reason ... NTK kernel ..." it seems that this is essentially the same reason as before, just formulated in more detail.
- Sec 2.3: Mention that it is gradient flow on the least-squares loss?
- Assumption 3 could be formulated more clearly: $\alpha_0$ always exists because $\alpha = 1$ is always admissible by the bounded kernel assumption. Moreover, $\alpha_0 > 0$ trivially because of the way that $\alpha_0$ is defined. So here, I think Assumption 3 should be a definition (something like "We define the embedding index $\alpha_0$ as ..."), unless you want to require $\alpha_0 < 1$.
- p. 6: "minimax optimality of kernel classifier" -> "minimax optimality of kernel classifiers"
- p. 6: "source condition 1" -> "source condition (Assumption 1)"
- "Assumption 1, 2, and 3" -> "Assumptions 1, 2, and 3"?
- In Theorem 2: "Assumption 1, 2, and3" -> whitespace is missing
- "of the neural network classifier" -> "of neural network classifiers"
- Eq. (14): The last layer should use the matrix $W^L$, not $W^{(L, p)}$. (The latter notation seems to be a remnant of the mirrored initialization notation, which you do not adopt in the other parts of Eq. (14).)
- The "mirrored initialization" seems to be already older and known as "antisymmetric initialization trick": http://proceedings.mlr.press/v107/zhang20a.html
- The citation Hui (2020) is missing the second author M. Belkin.
- The sentence before Proposition 1 is not ended by a period.
- Before corollary 1: I think the eigenvalue decay shouldn't be $\beta = d(d-1)$, maybe you meant $\beta = d/(d-1)$?
- p. 7: "ground true function" -> "ground-truth function"  (also in the conclusion)
- p. 8, paragraph "Estimation of $s$ in regression": There is nothing sensible after the $\in$ symbol 
- Related work: The authors could (briefly) mention/discuss other classes of assumptions that can be made in the classification setting, see e.g. https://projecteuclid.org/journals/electronic-journal-of-statistics/volume-12/issue-1/Improved-classification-rates-under-refined-margin-conditions/10.1214/18-EJS1406.full

**Summary of discussion**:
I missed an assumption in the NTK part, now I am not concerned about its correctness anymore. The smoothness estimator is still not reliable in general, which means that the experiments cannot fully support the appropriateness of the Sobolev assumption, but the authors acknowledge the limitations. In conclusion, I am changing my score from 5 to 6.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors investigate the statistical performance of kernel classifier, and establish, under rather standard assumptions in Theorem 1 and 2, respectively, upper and lower bounds on the classification excess risk (over Sobolev spaces), showing the optimally of the proposed classifier.

The proposed theoretical analysis is then applied to (deep) neural network (NN) models, to establish some generalization error bound of a fine-tuned NN model in the over-parameterization regime.

An intuitive approach is also proposed in Section 5 to estimate the key smoothness parameter with respect to the kernel.

### Strengths
This paper focuses on the fundamental problem of kernel learning and, if I understand correctly, improves some previous efforts such as Kerkyacharian & Picard (1992).

The obtained results (Theorem 1 and 2) are rather strong, in that Theorem 1 and 2 together show the minimax rate optimality of the proposed kernel spectral classifier.

The authors establish an interesting connection between the proposed theoretical analysis to NTK and deep neural networks in Corollary 1.

### Weaknesses
I am not an expert in the theory of kernel learning and I personally find this paper a bit difficult to digest. I assume some other audiences from the (theoretical) AI/ML community may have the same impression.
I think this paper can be improved in terms of presentation. See my detailed comments below.

I the following questions and/or comments for the authors:

1. Page 3: "Therefore, the framework of spectra algorithm" -> spectral algorithm. Similarly for the first sentence in Page 5.
2. Page 5: "bounded domain with smooth boundary $\mathcal{X} \subseteq R^d$" should be $\mathcal{X} \subseteq \mathbb{R}^d$ here?
3. I do not understand Assumption 3 and the notations therein, could the authors clarify this?
4. The proof of Theorem 1-2, Corollary 2, and the appendix should be re-organized for better readability.
5. I do not understand the statement of "width m and the sample size n are sufficiently large" in Corollary 1: should Corollary 1 be understood as asymptotic statements as $m,n \to \infty$? I am a bit confused since in many DNN and NTK literature, one must have $m \gg n$ for the NTK to accurately approximate the DNN behavior. Also, can the results in Corollary 1 be compared to existing results in NTK kernel literature?
6. I do not understand the connection between the min kernel discussed above Equation (17) and the NTK.

### Questions
I the following questions and/or comments for the authors:

1. Page 3: "Therefore, the framework of spectra algorithm" -> spectral algorithm. Similarly for the first sentence in Page 5.
2. Page 5: "bounded domain with smooth boundary $\mathcal{X} \subseteq R^d$" should be $\mathcal{X} \subseteq \mathbb{R}^d$ here?
3. I do not understand Assumption 3 and the notations therein, could the authors clarify this?
4. The proof of Theorem 1-2, Corollary 2, and the appendix should be re-organized for better readability.
5. I do not understand the statement of "width m and the sample size n are sufficiently large" in Corollary 1: should Corollary 1 be understood as asymptotic statements as $m,n \to \infty$? I am a bit confused since in many DNN and NTK literature, one must have $m \gg n$ for the NTK to accurately approximate the DNN behavior. Also, can the results in Corollary 1 be compared to existing results in NTK kernel literature?
6. I do not understand the connection between the min kernel discussed above Equation (17) and the NTK.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
