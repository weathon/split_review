# Reformulating Strict Monotonic Probabilities with a Generative Cost Model

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
In numerous machine learning contexts, the relationship between input variables and predicted outputs is not only statistically significant but also strictly monotonic. Conventional approaches to ensuring monotonicity focus primarily on construction or regularization methods. This paper establishes that the problem of strict monotonic probability can be interpreted as a comparison between an observable revenue variable and a latent cost variable. This insight allows us to reformulate the original monotonicity challenge into modeling the latent cost variable and estimating its distribution. To address this issue, we introduce a generative model for the latent cost variable, called the Generative Cost Model (\textbf{GCM}), and derive a corresponding loss function. We further enhance the estimation of latent variables using variational inference, which reformulate our loss function accordingly. Lastly, we validate our approach through a numerical simulation of quantile regression and several experiments on public datasets, demonstrating that our method significantly outperforms traditional techniques. The code of GCM is available in https://github.com/iclr-2025-4464/GCM.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper models a conditional monotonic distribution as a marginalization over latent variables. The key idea is to modify the monotonic modeling problem into modeling an element-wise cumulative distribution function (over a cost variable C). To actually model the latter, the authors introduce a latent variable modeling problem and solve it via a standard importance-weighted likelihood estimate with or without an additional ELBO term. The paper presents improved results in two experiments over a variety of baselines.

### Strengths
- Clean reformulation of the monotonic problem into a classification over a latent variable.
- Well-motivated techniques to solve the problem.
- Comparison against a variety of baselines.

### Weaknesses
No confidence intervals in the results tables. It's not clear that the improvement achieved by GCM is large enough (even over the simple MLP) to justify the much more complicated modeling procedure.



### Questions
- How wide are the confidence intervals for each of the metrics? Just do standard bootstrap if possible and report please.
- Why introduce the extra prior $p_\theta(Z)?$ Also, why is the prior different from $\pi(Z)$?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel approach to model strict monotonic probabilities. Without loss of generality, it considers the binary classification formulation $y|x, r\sim Bernoulli(y;G(x,r))$, where $G(x,r)$ is a function that is monotonic in $r$. The target is to learn the function $G$. Instead of directly learning $G$, the paper introduces a cost variable $c$ and reformulates $G(x,r)$ as an integration $\int_{c<r} p(c|x)d c$. The paper then introduces a generative cost model to approximate the conditional distribution $p(c|x)$.

### Strengths
The paper tackles an interesting problem of modeling monotonic probabilities. The problem itself is important, and the reformulation proposed by the paper is unique. Extensive experiments are conducted to support this new method.

### Weaknesses
The paper lacks theoretical results on the finite sample efficiency of the proposed algorithm. For the experiment design, an important setup that requires strict monotonicity is quantile regression, where the conditional quantile should be monotonic in the quantile argument. It would be interesting to see experiments designed for it and a comparison with the existing benchmarks.

### Questions
No additional questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes the Generative Cost Model (GCM) to enforce strict monotonicity by modeling a latent cost variable, using variational inference and importance sampling. This approach avoids architectural constraints and outperforms traditional methods on synthetic and real datasets.

### Strengths
The paper seems to present a novel approach to formulate the problem of strict monotonic probability, it provides convincing theoretical analysis and emprical results.

### Weaknesses
The paper lacks empirical validation across diverse, high-dimensional real-world datasets, limiting the demonstrated generalizability of the Generative Cost Model (GCM). Specifically, the current evaluation primarily relies on synthetic datasets and a limited number of real-world datasets, which may not fully capture the complexities and nuances of real-world monotonic relationships. The absence of experiments on datasets with a large number of features or instances makes it difficult to assess the scalability and robustness of the proposed method. Moreover, the code was not provided in the supplementary materials to assess the reproducibility of the results. This lack of code hinders the ability of other researchers to verify the claims made in the paper and build upon the proposed approach. Furthermore, the assumption of conditional independence between the latent variable z and revenue r given x, while simplifying the model, may not hold in many real-world scenarios, potentially limiting the model's flexibility and accuracy. The paper does not adequately explore the implications of this assumption or provide sufficient justification for its use.

### Questions
1. Can the authors provide additional justification or empirical validation for the assumption of conditional independence between the latent variable z and revenue r given x, as this assumption may affect model flexibility in real-world applications?

2. Could the authors elaborate on the computational efficiency of the Generative Cost Model (GCM) compared to traditional monotonic models, especially when applied to high-dimensional datasets? How does the computational time compare to the benchmarks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a latent variable model capturing both a monotonic part and a part that need not be monotonic. They give some background, and then propose a loss function for a variational training with neural nets.

### Strengths
It is an interesting problem and their construction is quite novel and creative.

### Weaknesses
The objective function and implementation leaves a lot of details missing and unexplained. The paper does not inspire confidence in the method.

Line 063 may not be quite right; p_theta(x,r) cannot be ignored in the evidence unless you drop the dependence on theta. Maybe rework the setup / explanation a bit, this shouldn’t be a big issue.

Line 101 equivalent to what?

Line 150 consider the machinery within https://arxiv.org/abs/2301.11695 and also the separate line of work on normalizing flows that all involve e.g. invertibility, monotone transformations, etc.

Line 210 (0,1) should be {0,1}

Line 189 should **y** and r have the same dimension?

Line 289 elementwise

Line 304 looks like it would suffer from high variance since pi(z) is fixed but p(z|x) depends on x.

Line 323 the combination of losses looks a little suspicious.

Line 323 Note that IWAE (Burda) is equal to ELBO (Jordan et al) for IWAE number of samples set to one; why is adding ELBO to IWAE sensible? Shouldn’t pi be something else and then no ELBO? Please expand, this is unconvincing.

Line 324 it seems like this doesn’t really match the beta vae setup; it would if you put a beta in front of the kl in line 318. What is this doing?

Table 1 does not seem to match appendix C for any value of the parameters, what is missing? Please add details.

Line >= 378 how did you set all of the parameters?

Line 698 affect

### Questions
Overview with some questions embedded:

Lines 054-059 could be clearer with a graphical model diagram. Edit: there is one later, nice.

Line 063 may not be quite right; p_theta(x,r) cannot be ignored in the evidence unless you drop the dependence on theta. Maybe rework the setup / explanation a bit, this shouldn’t be a big issue.

Line 101 equivalent to what?

Line 150 consider the machinery within https://arxiv.org/abs/2301.11695 and also the separate line of work on normalizing flows that all involve e.g. invertibility, monotone transformations, etc.

Line 210 (0,1) should be {0,1}

Line 189 should **y** and r have the same dimension?

Line 289 elementwise

Line 304 looks like it would suffer from high variance since pi(z) is fixed but p(z|x) depends on x.

Line 323 the combination of losses looks a little suspicious.

Line 323 Note that IWAE (Burda) is equal to ELBO (Jordan et al) for IWAE number of samples set to one; why is adding ELBO to IWAE sensible? Shouldn’t pi be something else and then no ELBO? Please expand, this is unconvincing.

Line 324 it seems like this doesn’t really match the beta vae setup; it would if you put a beta in front of the kl in line 318. What is this doing?

Line 378 how about some ablations of alpha and beta terms? Edit: there are some in appendix C.

Table 1 does not seem to match appendix C for any value of the parameters, what is missing? Please add details.

Line >= 378 how did you set all of the parameters?

Line 698 affect

### Soundness
2

### Presentation
2

### Contribution
3
