# Fit Like You Sample: Sample-Efficient Generalized Score Matching from Fast Mixing Diffusions

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5

## Abstract
Score matching is an approach to learning probability distributions parametrized up to a constant of proportionality (e.g. Energy-Based Models). The idea is to fit the score of the distribution (i.e. $\nabla_x \log p(x)$), rather than the likelihood, thus avoiding the need to evaluate the constant of proportionality. While there's a clear algorithmic benefit, the statistical cost can be steep: recent work by \cite{koehler2022statistical} showed that for distributions that have poor isoperimetric properties (a large Poincar\'e or log-Sobolev constant), score matching is substantially statistically less efficient than maximum likelihood. However, many natural realistic distributions, e.g. multimodal distributions as simple as a mixture of two Gaussians in one dimension---have a poor Poincar\'e constant. 

In this paper, we show a close connection between the mixing time of a \emph{broad class of} Markov processes with generator $\generator$ and stationary distribution $p$, and an appropriately chosen \emph{generalized score matching loss} that tries to fit $\frac{\smo p}{p}$. In the special case of $\smo = \nabla_x$, and $\generator$ being the generator of Langevin diffusion, this generalizes and recovers the results from \cite{koehler2022statistical}. This allows us to adapt techniques to speed up Markov chains to construct better score-matching losses. In particular, ``preconditioning'' the diffusion can be translated to an appropriate ``preconditioning'' of the score loss. Lifting the chain by adding a temperature like in simulated tempering can be shown to result in a Gaussian-convolution annealed score matching loss, similar to \cite{song2019generative}.  
Moreover, we show that if the distribution being learned is a finite mixture of Gaussians in $d$ dimensions with a shared covariance, the sample complexity of annealed score matching is polynomial in the ambient dimension, the diameter of the means, and the smallest and largest eigenvalues of the covariance---obviating the Poincar\'e constant-based lower bounds of the basic score matching loss shown in \cite{koehler2022statistical}. %This is the first result characterizing the benefits of annealing for score matching---a crucial component in more sophisticated score-based approaches like \citep{song2019generative, song2020score}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a general framework for designing generalized score matching losses with good sample complexity from fast-mixing diffusions. More precisely, for a broad class of diffusions with generator $\mathcal{L}$ and Pincare constant $C_P$, they can choose a linear operator $\mathcal{O}$ such that  the generalized score matching loss $E[\|\mathcal{O} p / p - \mathcal{O} p_{\theta} / p_{\theta}\|_2^2] / 2$ has a statistical complexity that is a factor $C_P^2$ worse than that of maximum likelihood. In addition, they analyze a lifted diffusion, which introduces a new variable for temparature and provably show statistical benefits of annealing for score matching. They apply their approach to sample from Gaussian mixture distributions.Their first result generalizes that of Koehler 2022.

### Strengths
The paper is well motivated and well written. It generalizes a previous paper on score matching (Koehler 2022) to generalized linear operator and correspondingly general score matching loss. The authors are also able to design a Markov chain termed CTLD based on the idea of anneling. Motivated by this chain, they are able to estimate the score function for Gaussian mixture distribution that has multiple modes and control the generalized score matching loss. The framework they propose is novel and quite interesting.

### Weaknesses
Several assumptions in the paper seem abit strong, and it would be good if the authors can elaborate a bit more on them. For the GMM application, it would be good to compare their result with the previous ones. Finally, I would love to see an experiment that supports their result, but the result itself is also interesting enough. Specifically, Assumption 1 and 2 of Theorem 2, while perhaps necessary for the proof, are quite restrictive and it's unclear how often they would hold in practice, especially when $\mathcal{O} \neq \nabla_x$ and not derived from CTLD. The paper would benefit from a discussion on the practical implications of these assumptions and how one might verify them in real-world scenarios. Additionally, while the authors mention that their results for GMMs improve upon existing bounds, a more direct comparison, detailing the specific scaling improvements, would be valuable. It would also be beneficial to see a discussion on the limitations of the proposed approach, especially in high-dimensional settings, and how it might compare with alternative methods for score matching. Finally, the lack of experimental validation makes it difficult to assess the practical performance of the method, and it would be beneficial to include some experiments, even on simple datasets, to demonstrate the effectiveness of the proposed approach.

### Questions
1. Assumption 1 and 2 of Theorem 2 seems pretty strong. Could the authors give an example where these assumptions hold when $\mathcal{O} \neq \nabla_x$ and not from CTLD? In general, how do we validate these assumptions?

2. What is $\mathcal{O}$ for CTLD? 

3. Maybe the authors can comment a bit on how Theorem 5 compares with the previous results, in particular, can the results of Koehler 2022 also be applied to get an upper bound?

4. Can we apply generalized score matching loss to diffusion sampling? Maybe the authors can comment a bit on the feasiblity of that.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study generalized score matching loss, that uses an arbitrary linear operator instead of $\nabla_x$ in the standard score matching objective. They generalize the result of  Koehler et al. (2022) to this setting. Concretely, they show that for a Markov process with stationary distribution $p$ proportional to $\exp(-f(x))$ and a generator $\mathcal{L}$ with Poincare constant $C_P$, one can choose a linear operator such that the error of the corresponding generalized score matching estimator (more precisely, the spectral norm of the covariance of limit distribution, assuming asymptotic normality) can be bounded in terms of $C_P$ and the error of MLE (more precisely, the spectral norm of the covariance of the limit distribution). In addition, they use generalized score matching with additional temperature variable for learning means of Gaussian mixtures with the same covariance matrix.

### Strengths
The results are new and non-trivial. The statements are clear, as well as comparison with results from prior works on score matching.

### Weaknesses
There are a few things that concern me. So far I'm not convinced that the paper is above the acceptance threshold. Please see the questions below.

Regarding Theorem 2: Could you please explain if there is any interesting technical contribution compared to Theorem 2 in Koehler et al. (2022)? The proof looks like a straightforward generalization of their proof to your settings, or did I miss anything important?

Regarding Theorem 5:

1) The estimator that you use here doesn't seem to be efficiently computable, is that correct? The score matching estimator for exponential families from Koehler et al. (2022) is efficiently computable (please correct me if I'm wrong), so their motivation to study it and compare with MLE is clear to me. What is the motivation of usage of your estimator for this problem if it is not efficiently computable? 

2) As I understood, you are interested in the regime $K \gg d$, so the fact that $C$ from your bound $\Vert \Gamma_{SM} \Vert_{OP} \le C \Vert \Gamma_{MLE}\Vert_{OP}^2$ does not depend on $K$ is important and nice. However, as you said in the footnote, $ \Vert \Gamma_{MLE}\Vert_{OP}$ may depend on $K$, so $K$ can appear in the end in the error, i.e. $\Vert \hat{\mu_i} - \mu^*_i \Vert$ 
may depend on $K$ even when the corresponding error for MLE doesn't. So it is not clear to me why this dependence on $K$ was important from the very beginning. 

If it was really important, then it would make sense to bound not 
$\Vert \Gamma_{SM} \Vert_{OP}$, but the largest diagonal entry of $\Gamma_{SM}$ in terms of the largest diagonal entry of $\Gamma_{MLE}$. In this case , if there is such a bound with a factor that does not depend on $K$, then it should imply a bound on $\Vert \hat{\mu_i} - \mu^*_i \Vert$ that does not depend on $K$ (as long as corresponding errors of MLE do not depend on $K$). Is it possible to derive such a bound?

3) There is no comparison with prior works on Gaussian mixtures. While you refer to some of these works in the paper, it is not immediately clear how your result is comparable with them. I think it makes sense to add such a comparison.

4) Can your approach be generalized to more general mixtures of Gaussians, when not all of them have the same covariance (but, say, when all covariances have condition number bounded by $O(1)$)?

And a minor thing:

In Definition 1, is it really fine to use linear operators between the spaces of *all* functions? E.g. in Lemma 1 you use adjoint operators and assume that the operators are between Hilbert spaces.

### Questions
Regarding Theorem 2: Could you please explain if there is any interesting technical contribution compared to Theorem 2 in Koehler et al. (2022)? The proof looks like a straightforward generalization of their proof to your settings, or did I miss anything important?

Regarding Theorem 5:

1) The estimator that you use here doesn't seem to be efficiently computable, is that correct? The score matching estimator for exponential families from Koehler et al. (2022) is efficiently computable (please correct me if I'm wrong), so their motivation to study it and compare with MLE is clear to me. What is the motivation of usage of your estimator for this problem if it is not efficiently computable? 

2) As I understood, you are interested in the regime $K \gg d$, so the fact that $C$ from your bound $\Vert \Gamma_{SM} \Vert_{OP} \le C \Vert \Gamma_{MLE}\Vert_{OP}^2$ does not depend on $K$ is important and nice. However, as you said in the footnote, $ \Vert \Gamma_{MLE}\Vert_{OP}$ may depend on $K$, so $K$ can appear in the end in the error, i.e. $\Vert \hat{\mu_i} - \mu^*_i \Vert$ 
may depend on $K$ even when the corresponding error for MLE doesn't. So it is not clear to me why this dependence on $K$ was important from the very beginning. 

If it was really important, then it would make sense to bound not 
$\Vert \Gamma_{SM} \Vert_{OP}$, but the largest diagonal entry of $\Gamma_{SM}$ in terms of the largest diagonal entry of $\Gamma_{MLE}$. In this case , if there is such a bound with a factor that does not depend on $K$, then it should imply a bound on $\Vert \hat{\mu_i} - \mu^*_i \Vert$ that does not depend on $K$ (as long as corresponding errors of MLE do not depend on $K$). Is it possible to derive such a bound?

3) There is no comparison with prior works on Gaussian mixtures. While you refer to some of these works in the paper, it is not immediately clear how your result is comparable with them. I think it makes sense to add such a comparison.

4) Can your approach be generalized to more general mixtures of Gaussians, when not all of them have the same covariance (but, say, when all covariances have condition number bounded by $O(1)$)?

And a minor thing:

In Definition 1, is it really fine to use linear operators between the spaces of *all* functions? E.g. in Lemma 1 you use adjoint operators and assume that the operators are between Hilbert spaces.

### Soundness
4 excellent

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of using score matching to learn the probability distribution in energy-based models.
In energy-based models, when we learn the probability distribution, we often encounter an intractable normalizing factor.
To avoid this intractable factor, one can use score matching instead.
However, score matching can be statistically less efficient.
This paper works on the connection between the mixing time of a broad class of continuous, time-homogeneous Markov processes with stationary distribution and generator, and the statistical efficiency of an appropriately chosen generalized score matching loss.

### Strengths
- The problem seems well-motivated.

### Weaknesses
 - The presentation is fairly technical and may pose challenges for readers who are not an expert in this particular area.



### Questions
Note:
- Theorem 2: What are $\Gamma_{SM}$ and $\Gamma_{MLE}$?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
