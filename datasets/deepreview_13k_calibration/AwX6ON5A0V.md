# On Gaussian Mixture Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 3, 6

## Abstract
We investigate the sample complexity of Gaussian mixture models (GMMs).  Our results provide the optimal upper bound, in the context of uniform spherical Gaussian mixtures.  Furthermore, we highlight the relationship between the sample complexity of GMMs and the distribution of spacings among their means.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the sample complexity of learning the parameters of mixtures of (spherical) Gaussians (of equal variance), showing that the distribution of spacing between the means influences the sample complexity.

The proof uses the standard method of moments: first estimate the empirical moments, then compute (an estimate of) the coefficients of the parameter polynomials (whose roots are the means), and finally compute (an estimate of) the means.



Some minor typos:

Page 1
- Title is missing, currently showing Formatting Instructions for ICLR 2024 Conference Submissions
- The paper should point out that in Equation (0.1), weights $\omega_i$ are be non-negative, in addition to sum to 1.
- If the parameters of the mixtures ~all~ **are** well separated, it can be shown that...

Page 5
- “imperial moments we obtain in equation 1.3” should be empirical moments.

Page 9
- References 6 and 7 are the same.

Throughout
- Left (double) quotes should use `` instead of '' when typesetting in $\LaTeX$, so that we get “this” instead of ”this” (note the left quote).

### Strengths
The upper bounds generalize previous results of 2 Gaussians by Hardt and Price to $k$ (spherial) Gaussians (of equal variance), and matches their lower bounds.

Section 0.1 explaining Pair Correlation, with the two examples without and with consecutive gaps, is helpful to understanding to this central concept for the main result. Besides, identifying the role of the Pair Correlation of means is itself a contribution, explaining the dependence of sample complexity to distribution of parameters (means).

### Weaknesses
Works only for the mixture of spherical Gaussians of equal variance, and for the mean zero case, depends on a new parameter of pair correlation of means, which limits applications of this result. The restriction to spherical Gaussians with equal variance is a significant limitation, as real-world data rarely conforms to such a strict assumption. Furthermore, the requirement that the mixture has a mean of zero, while addressable through data centering, adds a preprocessing step that may not always be desirable or feasible. The dependence on the pair correlation of means, while insightful, introduces a hyperparameter that is not easily interpretable or controllable, further limiting the applicability of the results. The analysis does not consider the impact of potential outliers in the data, which could significantly affect the moment estimates and consequently the parameter recovery. The theoretical analysis also assumes perfect knowledge of the number of components, which is often unknown in practice, and the impact of misspecifying this parameter is not explored. The paper also lacks a discussion on the computational complexity of the proposed method, which is crucial for practical applications. While the method uses the standard method of moments, it is not clear how the computational cost scales with the number of components, the dimension of the data, and the sample size.

### Questions
Besides theoretical interests, may the authors suggest applications of the results, considering their limitations (works only for the spherical case of equal variance, and depends on pair correlation of means)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors look at the problem of learning mixture of Gaussians. There are two points of view for studying this problem. The first is to learn the mixture in total variation distance. The second one which is taken in this paper is to learn the mixture probabilities, means, and covariance matrices up to certain desired precision. The authors claims to give better than existing bounds for this parameter estimation problem. I found the paper is extremely ill-presented and very confusing to read.

The main contribution seems to be an algorithm for the uniform spherical case, where each mixture probability is the same and the standard deviation is 1.

### Strengths
I think the problem is well-studied and important in the community.

### Weaknesses
 - The results are described in a very confusing manner all over the paper. To quote: "... assume that we have gaps of length $\varepsilon$ between consecutive means in our mixture. However, these gaps are isolated, meaning that if $\mu_{n+1}-\mu_n=\varepsilon$, then the
adjacent gaps are significantly larger:  $\mu_{n+2}-\mu_{n+1}>>1$, and  $\mu_{n}-\mu_{n-1}>>1$". What does this mean? On the one hand, you are saying consecutive gaps are small. But immediately after that you are saying certain gaps are significantly large.

-Are you considering the univariate or the multivariate Gaussian case? In equation 0.1 you are saying covariance matrix whereas in the our contribution paragraph, you are saying $\sigma_i=1$ which corresponds to the univariate case. This is very confusing to read.

- Furthermore, the main contribution seems to be an algorithm for the uniform mixture of spherical Gaussians, which seems rather limited and incremental. Also is it already covered by the prior work? See my comment for Questions.

- Now I'll come to the *main weakness* of the paper. The presentation is extremely poor and unprofessional. For example the paper don't even have a title and section title for the starting section. One cannot simply expect reviewers to spend time on a paper where the authors themselves have not spend much time.

### Questions
You are saying the main contribution is an algorithm for the case $\omega_i = \frac{1}{k}$ and $\sigma_i = 1$. I though Hard and Price already show that the tight sample complexity is $\Theta(\Sigma^{-12})$ which in this case would be $\Theta(1)$.

Considering the above fact, why is your result interesting? What am I missing here?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors aim to establish the sample complexity of $k$-component Gaussian mixture models (GMMs), that is, to find the optimal number of samples necessary to achieve mixture parameter estimation within some tolerance $\epsilon$ from the true parameters. By using the method of moments, they figure out that a relationship between the sample complexity of one-dimensional GMMs with mean zero and variance $\sigma^2$ and the distribution of spacings among their means. Via that relationship, the author arrives at the sample complexity of $\epsilon^{-2}$.

### Strengths
1. Originality: The sample complexity of $k$-component Gaussian mixture models is novel but limited to one-dimensional setting.

2. Quality: All results in the paper are associated with theoretical guarantee. The authors intepret their results well.

### Weaknesses
1. Clarity: the presentation of the paper is poor due to the following reasons:
- The title of the paper is missing.
- The abstract does not summarize the paper well. In particular, the authors should highlight that the sample complexity is established in one-dimensional setting.
- At the beginning of the paper, it is too general to say that GMMs have been extensively studied in the field of machine learning. The authors should specify the applications of GMMs in that fields, and cite relevant papers.
- There are some undefined notations, e.g. $\sigma_i$ in the contribution paragraph.
- The corollaries are presented without any theorems introduced before, which makes no sense.
- In the main text, I suggest that the authors should only provide a proof sketch in a separate section and then leave the full proofs in the supplementary material. This would help improve the cohesiveness of the paper.

2. The sample complexity of GMMs derived in the paper is limited to one-dimensional setting. Moreover, the variance of each Gaussian distribution is assumed to be one, which is quite restricted.

3. When discussing about the parameter estimation of GMMs, the authors should involve more relevant papers, not only those using the method of moments but also other methods like Maximum Likelihood, namely [1], [2], [3], [4] and [5].

4. The paper lacks a simulation study to empirically verify their theoretical results. I believe that such numerical experiments would significantly strengthen the paper.

5. The authors should include a discussion paragraph at the end to conclude the paper, discuss about the limittaions of their current technique, and its ability to extend to more general settings of GMMs.

### Questions
1. In Corollary 0.1, is the variance $\sigma^2$ of the whole mixture or an individual Gaussian distribution?

2. In Section 0.1, the authors should define the notation $\Omega(\sigma)$, and do not assume that readers will understand.

3. In the Gaussian mixture models, when the mixture weights are generalized to depend on the covariates $X$, namely softmax weights (see [1]), can the current techniques be applied to those settings?

4. In Theorem 0.3, is the mean zero and variance one assumptions for simplicity or necessary for the proof to hold true?

5. What are the main challenges of deriving the sample complexity of GMMs in high-dimensional settings?

6. In equation (4.2), Is the term $\hat{P}'(x)$ always different from zero?

7. The 'Corollary' should be renamed as 'Proposition'.

8. In equation (0.1), the weights $\omega$ need to be non-negative.

**References**

[1] H. Nguyen. Demystifying Softmax Gating Function in Gaussian Mixture of Experts. In NeurIPS, 2023.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the problem of sample complexity for learning mixtures of $k$ univariate, equal-weighted, standard Gaussians.
The authors devised an algorithm that takes $n$ samples from such a mixture and returns $k$ estimated means,
They showed that if $n > \frac{C}{\epsilon^2}$ where $C$ is a factor depending on the separation of means, all estimated means have an additive error of $\epsilon$.
Note that when the separations of the means are constant, the factor $C$ is a constant. 
When the separations of the means are $\sim \epsilon$, the factor can be $\frac{1}{\epsilon^{2k-2}}$ and hence the final sample bound is $\frac{1}{\epsilon^{2k}}$.
The main idea of the proof is moment based.
The authors consider the polynomial whose roots are the means of the mixture and expand the coefficients in terms of the moments by Hermite polynomials.
Then, one can use samples to estimate the coefficients and solve the polynomial with the estimated coefficients.
Hence, the roots are supposed to be close to the true roots which are the means.

### Strengths
- The result achieves the optimal rate and explains the connection between the sample complexity and the separations of the means.

### Weaknesses
 - The proofs are mostly calculations.
I believe most of the lemmas are not fundamentally novel or can be easily follow from previously known results.
This paper appears to primarily reiterate known results and may be somewhat remote from making a substantial contribution.
For example: Aren't Lemma 2.1 and 2.2 the Hermite polynomial expansion?
The authors may also want to cite the paper "Optimal estimation of Gaussian mixtures via denoised method of moments" by Yihong Wu, Pengkun Yang.
Even though the problem definitions are not exactly the same, there is discernible overlap in the techniques employed to address the underlying challenges.


- The paper may need some work to polish it.
For example: 
Make the title a bit more informative, start the section number from 1 instead of 0 and other numbering systems...

### Questions
Notes:
- In (0.1): I think $\omega_i$ also needs to be $\geq 0$.
- In (1.2): The authors may want to introduce Hermite polynomials before (1.2). Also, should $\mathcal{M}_d$ be $\mathcal{M}_m$?
- References: [6] and [7] are the same.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies estimating the mean parameters of a equi-weighted mixture of $k$ Gaussians with unit variance: $\Gamma = \frac{1}{k} \sum_{i=1}^k \mathcal{N}(\mu_i, 1)$. The paper gives an upper bound on the sample complexity to estimate the mean parameters within an error of $\epsilon$. The results are interesting and novel. The paper can be improved by correcting some mistakes and fixing several typos.

Notation: 
* $\mu_1, \dots, \mu_k$ are the means to be estimated
* $M_m$: m'th moment of the mixture
* $P_m = \sum_{i=1}^m \mu_i^m$
* $e_m$: elementary symmetric polynomials of mean parameters
* $P(x) = \Pi_{i=1}^k (x-\mu_i)$ is a polynomial whose roots are the mean paramters

Some key points
* We can write $P_m = f(M_1, \dots, M_m)$ for some function f
* We can write $e_m = g(P_1, \dots, P_m)$ for some function g

How to estimate $\mu_1, \dots, \mu_k$ from a sample drawn from $\Gamma$?
* Compute empirical moments $\hat M_m$
* Plugin estimate $\hat P_m = f(\hat M_1, \dots, \hat M_m)$
* Plugin estimate $\hat e_m = f(\hat P_1, \dots, \hat P_m)$
* Form the polynomial $\hat P(x) = \sum_{i=1} \hat e_i x^i$.
* The roots of this polynomial yield estimates of the means

The authors show that if the means are well-separated, then given $\log(1/\delta) \epsilon^{-2}$ samples, with probability $1 -\delta$, $|\hat \mu_i - \mu_i | \leq c \epsilon$ where $c$ depends on $k, var(\Gamma)$ and a mean-separation metrics $\Pi_{i \neq m} (\mu_m - \mu_i), m \in [k]$. On a high-level, the proof 
* ties together $\hat M$ and $M$ (previously known)
* then bounds $\hat P_m - P_m$
* then bounds $\hat e - e$
* then gives root difference bounds between $\hat P(x), P(x)$ from real analysis literature

### Strengths
The results are interesting and novel.

### Weaknesses
There are several mistakes and typos which make this theoretical paper hard to read.

*   Update the title, currently it is a placeholder from ICLR formatting instructions.
*   page 2 second line: Why is it $3k-2$ parameters? I understand $3k-1$ (due to the fact that weights need to sum up to 1).
*   What Corollary 0.1 a corollary to? Rename it to a Proposition?
*   Sentence below equation (0.2): make it tighter, maybe $\Omega(\epsilon^\ell)$.
*   Theorem 0.3: first line: mean does not seem to be 0? There are some other places as well where the mean is stated to be 0.
*   Equation (1.2): $\mathcal{M}_d$ should be $\mathcal{M}_m$?
*   Sentence below eq (1.3): The variance of $x^m$ is not $\sigma^{2m}$. You seem be missing a constant?
*   Senetence above Lemma 2.1: imperial → empirical
*   Lemma 2.1 last line: less than "or equal to" $2i-1$.
*   Eq (2.9): maybe write one/two steps more to explain it.
*   Eq (3.2): left hand side should have a factor of $n$. Right hand side should have $j-1$ in the exponent, not $j$. Also say that $e_0 = 1$. Ditto for Definition 3. 
*   I believe, some constants in the proofs need to be changed because of the above mistake.
*   Lemma 3.1: The statement is missing "with probability at least $1-\delta$".
*   Eq (3.4): Is the $K$ used here defined before?
*   Line below eq (3.5): $i\geq m$?
*   Proof 3: Second display, last inequality: explain how to derive this. I am not sure if this is true for small $n$.
*   Proof 4.: In the first line, $p$ should be $P$.
*   Eq (4.2): How to handle the case where the denominator is $0$?
*   Display above eq (4.4): How is $|\hat P'(x)$ bounded by $\Pi_{j\neq m} (\mu_m - \mu_j)$ here?
*   There are duplicates in References.

### Questions
Comments/questions/typos

* Update the title, currently it is a placeholder from ICLR formatting instructions.
* page 2 second line: Why is it $3k-2$ parameters? I understand $3k-1$ (due to the fact that weights need to sum up to 1).
* What Corollary 0.1 a corollary to? Rename it to a Proposition?
* Sentence below equation (0.2): make it tighter, maybe $\Omega(\epsilon^\ell)$.
* Theorem 0.3: first line: mean does not seem to be 0? There are some other places as well where the mean is stated to be 0.
* Equation (1.2): $\mathcal{M}_d$ should be $\mathcal{M}_m$?
* Sentence below eq (1.3): The variance of $x^m$ is not $\sigma^{2m}$. You seem be missing a constant?
* Senetence above Lemma 2.1: imperial → empirical
* Lemma 2.1 last line: less than "or equal to" $2i-1$.
* Eq (2.9): maybe write one/two steps more to explain it.
* Eq (3.2): left hand side should have a factor of $n$. Right hand side should have $j-1$ in the exponent, not $j$. Also say that $e_0 = 1$. Ditto for Definition 3. 
* I believe, some constants in the proofs need to be changed because of the above mistake.
* Lemma 3.1: The statement is missing "with probability at least $1-\delta$". 
* Eq (3.4): Is the $K$ used here defined before?
* Line below eq (3.5): $i\geq m$?
* Proof 3: Second display, last inequality: explain how to derive this. I am not sure if this is true for small $n$.
* Proof 4.: In the first line, $p$ should be $P$.
* Eq (4.2): How to handle the case where the denominator is $0$?
* Display above eq (4.4): How is $|\hat P'(x)$ bounded by $\Pi_{j\neq m} (\mu_m - \mu_j)$ here?
* There are duplicates in References.

I have not checked a few proofs: Lemma 2.2, Proof 3.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
