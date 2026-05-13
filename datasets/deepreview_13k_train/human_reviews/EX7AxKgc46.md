# Improved Generalization of cGAN using Vicinal Estimation and Early Stopping

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
The problem of generating high-dimensional distributions has been known as a difficult problem in machine learning due to the Curse of Dimensionality: the higher the dimensionality is the more the empirical data deviates from its original distribution even for a large number of samples. Along with the Curse of Dimensionality, the generalization of conditional density estimation (CDE) suffers from so-called Lack of Conditional Samples: the number of data for each conditional density is usually much smaller than the number of samples or no data is avaiable for some conditional densities. To overcome these difficulties, we introduce the concept of Vicinal Estimation (VE) which is shown to be useful in estimating conditional densities. With VE we propose a conditional Generative Adversarial Network (cGAN) model and analyze theoretically that the generalization error of our model is independent of the dimensionality of the output. We also show that our theoretical analysis holds in practice through experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of learning a conditional distribution with a continuous input and potentially high-dimensional output, using a variant of a generative adversarial network (GAN) with a "vicinal estimation" mechanism to address the sparsity of observed labels in the label-space. The paper first provides theoretical guarantees showing that the proposed approach (together with an early stopping mechanism) learns the true conditional distribution in $2$-Wasserstein distance and then provides a toy experiment in which the proposed method is demonstrated to learn a synthetic conditional distribution more efficiently than a baseline cGAN.

### Strengths
The vicinal estimation (VE) approach seems novel in the setting of conditional generation. The paper presents precise theoretical guarantees supporting the proposed method. The synthetic data experiment is clearly explained and its results are quite precise and illustrative.

### Weaknesses
1. I suggest removing "and Early Stopping" from the title of the paper, as (a) this is hardly discussed in the paper and (b) it seems to be a direct adaptation of Yang & E (2021) to the conditional setting rather than a really novel contribution.

2. Eq. (1): In this sentence, $p$ should be quantified more carefully; there are obvious counterexamples (e.g, when $p$ is a single point mass) for which this statement, as written, is false.

3. I found it counterintuitive that $X$ is used for the label and $Y$ is used for the generated image. While this makes sense in terms of the inputs and outputs of a cGAN, it conflicts with much more common settings in the ML literature (e.g., image classification, where $X$ is the image and $Y$ is the label), causing me to be confused through much of the paper until I went back and re-read the beginning of Section 3. I don't necessarily suggest changing this (especially if it is consistent with other paper on conditional generative modeling), but perhaps it is worth adding a sentence to explicitly point out this possible point of confusion.

4. Section 4: The notation in here seemed unnecessarily complicated. Isn't $q_x$ simply the conditional distribution of $X'$ given $X$. Why introduce a new notation rather than simply writing it as such? If I understand correctly, later parts could be written much more readably (e.g., in Lemma 1, $m_{\tilde q}(x') = \mathbb{E}[X|X']$ and $d_{\tilde q}(x') = \sqrt{\mathbb{E}[||X - \mathbb{E}[X|X']||^2|X']}$, etc.). The introduction of $q_x$ and the subsequent notation using $m_{\tilde q}$ and $d_{\tilde q}$ obscures the underlying simplicity of the conditional expectation and variance, making the analysis harder to follow.

5. Just before Eq. (11), a minor wording suggestion: "a VE vanishes the conditional information" -> "a VE reduces the conditional information"

6. Theorem 1: Isn't $||\tilde q^L||_\infty = L^{-d_x} ||\tilde q^1||_\infty$? If so, perhaps explanding this would make the statement it a bit more intuitive. The current presentation of the theorem does not clearly highlight the relationship between the scaling factor $L$ and the resulting bound, leaving the reader to infer this relationship.

7. Although the work is intended to be theoretical, it would be strengthened by any discussion of real-world relevance (e.g., describing some applications where the proposed vicinal estimation approach might be useful). Experiments on real-world data would further strengthen the paper. The absence of real-world validation leaves a gap in demonstrating the practical utility of the proposed method.

### Questions
1. Just before Eq. (11)
> uniform auxiliary distributions on $\mathcal{X}'$ erase completely the information of labels in the data

If I understand correctly, what really matters here is how much information about $X$ is preserved by $X'$, rather than the particular distribution of $X'$. For example, doesn't any distribution of $X'$ that is independent of $X$ completely the information of labels? Or is there some reason the uniform distribution is special here?

2. Just after Lemma 1
> Note that the quantities $m_{\tilde q}(x′)$ and $d_{\tilde q}(x′)$ only depend on the auxiliary distribution $q$, not on the distribution $p$.

I found this sentence confusing, as $m_{\tilde q}(x′)$ and $d_{\tilde q}(x′)$ depend on the inverse auxiliary distribution $\tilde q$, which is related to the auxiliary distribution $q$ in a way that depends on $p$ (namely, through Eq. (10)). Perhaps this was a typo (i.e., "auxiliary distribution $q$" should have been "inverse auxiliary distribution $\tilde q$")? Even so, I don't really understand the point of this sentence.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article studies the generalization property of conditional GANs to estimate conditional probabilities p(y|x). By adding conditional data samples with Vicinal estimation and using 1-layer neural network discriminator, the proposed model is able to achieve a Wasserstein error which does not grow with the dimension of y. As long as the dimension of of x is small, it overcomes the curse-of-dimensionality when the dimension of y is large.

### Strengths
This article makes a creative combination of 2 existing ideas: one based on 1-layer neural network discriminator based on Barron space and early stopping in learning to achieve dimension-free generalization. The other idea is based on vicinal estimation to define a new training loss to increase effective number of samples.

### Weaknesses
The theoretical results are somehow not very clear, making it hard and inconsistent to understand how the whole idea is connected to the Wasserstein-2 error used in the evaluation of cGANs. I would suggest a clearer explanation in the rebuttal phase.

- What is the functional space of the discriminator D(y,x) in eq. 5, and how is it related to the W-1 distance in eq. 6? I suppose you are assuming the (y,x) -> D(y,x) is Lipschitz, but for the W-1 distance, we only need y -> D(y,x) to be Lipschitz for any x. 
- The tilde D_alpha(y,x’) defined in eq 14, is it also Lipschitz? I do not see why this is so (even based on eq. 22) and it seems to be inconsistent to your previous definition. 
- What is the definition of tilde p_{x,y} and p(x’) in eq. 20? Is p(x’) an empirical distribution as in eq. 7? It seems not to be the case according to theorem 2 and 3. Then I am confused of the over-all setting if you are the true distribution p(x’) of x’ in your training loss. 
- Do you need to assume that the kernel is characteristic in Theorem 3 ? It is not clear what are the above conditions in Theorem 5. Please make it clearer. Could you also explain why there is no d_y in the statement of Theorem 5?

Minor: 

- Why did you introduce a RKHS regulation in the loss V’ in eq. 18? What would happen if there is no regulation?
- What is y used for in eq. 25 ? I do not see it to appear on the right hand side. 
- How do you get the optimal scale of ||tilde q||_inf after eq. 33 ?

### Questions
-	What is the functional space of the discriminator D(y,x) in eq. 5, and how is it related to the W-1 distance in eq. 6? I suppose you are assuming the (y,x) -> D(y,x) is Lipschitz, but for the W-1 distance, we only need y -> D(y,x) to be Lipschitz for any x. 
-	The tilde D_alpha(y,x’) defined in eq 14, is it also Lipschitz? I do not see why this is so (even based on eq. 22) and it seems to be inconsistent to your previous definition. 
-	What is the definition of tilde p_{x,y} and p(x’) in eq. 20? Is p(x’) an empirical distribution as in eq. 7? It seems not to be the case according to theorem 2 and 3. Then I am confused of the over-all setting if you are the true distribution p(x’) of x’ in your training loss. 
-	Do you need to assume that the kernel is characteristic in Theorem 3 ? It is not clear what are the above conditions in Theorem 5. Please make it clearer. Could you also explain why there is no d_y in the statement of Theorem 5?

Minor: 

-	Why did you introduce a RKHS regulation in the loss V’ in eq. 18? What would happen if there is no regulation?
-	What is y used for in eq. 25 ? I do not see it to appear on the right hand side. 
-	How do you get the optimal scale of ||tilde q||_inf after eq. 33 ?

### Soundness
2 fair

### Presentation
2 fair

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
The paper deals with the problem of sampling from the conditional distribution of $Y$ given $X=x$, based on a sample of size $N$ denoted by $(X_1,Y_1),\ldots, (X_N,Y_N)$. The Vicinal Estimation method is introduced that, roughly speaking, consists in replacing the original problem by that of estimating the conditional distribution of $Y$ given $X'=x'$, where $X'$ is a random label artificially generated from a conditional distribution $q(.|X = x)$. The main contribution of the paper is theoretical: it provides an upper bound on the distance between the learned conditional density and the true conditional density. Taking the set of discriminators to be equal to a subset in the Barron space, it is shown that it is possible to get an error that behaves itself as $N^{-1/(6+2d_X)}$, where $d_X$ is the dimension of the set of the labels $X$.

### Strengths
1. Studies an important problem. 
2. Obtains a new bound on the error of conditional sampling

### Weaknesses
1. Section 4, which is one of the most important ones is poorly written. The definition of the generator that is analyzed is not given in full detail. In particular, neither the set of the discriminators nor the set of the generators involved in the min-max problem of the GAN are clearly specified. In addition, it is not clear in Eq 19 what is understood by $\tilde p_{X,Y}(y|x')$.  The description of the GAN training procedure lacks crucial details, specifically regarding the optimization process. The text states that $\tilde D$ is trained to maximize $\hat V'(G,\tilde D)$ and $G$ is trained to minimize $\hat V(G,\tilde D)$, but it fails to specify the sets over which these maximizations and minimizations are performed. For instance, it is unclear whether the maximization over $\tilde D$ is with respect to parameters $a$, $w$, $b$ or some other set of parameters. Similarly, the set of generators over which the minimization is performed is not defined clearly. This lack of precision makes it difficult to understand the exact nature of the optimization problem being solved.
2. Section 5 is very dense and hard to read. The results are quite technical so it is impossible to say whether they are plausible or not without checking the proofs line by line. Given the limited time I had to review the paper, I could not check the proofs provided in the supplementary material. I believe that it would be much better for such a paper to be submitted to a journal, where more space may be used for stating the main theorems and providing some explanations and intuitions, as well as more time could be left to the reviewers for checking the details of the proofs.
3. It seems that the results of the paper do not imply that the vicinal estimation method is better than the vanilla cGAN. Indeed, the fact that the rate of convergence does not depend on the dimension of Y might very well be a consequence of the choice of the set of discriminators. In particular, it is well known that the lower bound (1) is due to the fact that the set of discriminators defining the $W_1$ (which is a lower bound on $W_2$) -- the set of 1-Lipschitz functions -- is too large.  Replacing this set by an RKHS with a bounded kernel leads to the dimension independent rate $N^{-1/2}$. Furthermore, the paper defines the conditional density $\tilde p$ corresponding to the vicinal estimation (VE) in Eq (9), which is valid for joint distributions that admit a density with respect to the Lebesgue measure. However, the empirical distribution $p_{X,Y}$ is not absolutely continuous with respect to the Lebesgue measure. Therefore, the corresponding VE should be defined without relying on densities. The current definition is not mathematically rigorous and needs to be addressed.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper improves conditional GAN learning using Vicinal Estimation.

### Strengths
The idea to introduce a auxiliary distribution is interesting.

### Weaknesses
I was still confused about how the auxiliary distribution helps after reading the paper, because I'm not familiar with related works. The paper does not clearly articulate the specific mechanism by which the vicinal estimation addresses the challenges of conditional GANs, particularly the issue of limited conditional samples. The explanation of how the auxiliary distribution provides 'sufficiently many conditional samples' is not intuitive, and the connection to the curse of dimensionality is not explicitly made. The paper needs to provide a more detailed explanation of how the vicinal distribution is constructed and how it differs from the original conditional distribution, and why this difference is beneficial. The lack of clarity makes it difficult to assess the true contribution of the proposed method.

### Questions
The idea to use an auxiliary distribution is similar to importance sampling, are they related somehow?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
