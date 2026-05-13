# A Normalizing Flows based Difference-of-Entropies Estimator for Mutual Information

- Decision: Reject
- Scores: 3, 3, 5, 5, 8, 5

## Abstract
Estimating Mutual Information (MI), a key measure of dependence of random quantities without specific modelling assumptions, is a challenging problem in high dimensions. We propose a novel mutual information estimator based on parametrizing conditional densities using normalizing flows, a deep generative model that has gained popularity in recent years. This estimator leverages a block autoregressive structure to achieve improved bias-variance trade-offs on standard benchmark tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explores block neural autoregressive normalizing flows (B-NAF) for estimating the mutual information (MI) between two continuous random variables, denoted X and Y, from samples. The idea is to decompose MI as the difference between H(X) and H(X|Y), respectively denoting the entropy of X and the conditional entropy of X given Y. The observes that the (conditional) entropy is a direct by-product of density estimation with the KL divergence as $H(X) = \inf_{q} \mathbb -{E}_{p(x)}[\log q(x)] $. By exploiting the autoregressive nature of B-NAF we can jointly estimate H(X) and H(X|Y) with one B-NAF network.

### Strengths
- Using normalizing flows, in particular autoregressive flows, to do MI estimation is a novel idea to the best of my knowledge.
- Empirical results demonstrate that the proposed method can achieve good results on simple benchmarks.

### Weaknesses
 - Presentation: Overall I do not find the paper very well-written. The problem is not well-motivated and it remains unclear under which setting the proposed approach can be of practical usefulness. Section 2 spans from page 2 to page 6 and does not contain original results in my opinion. In contrast, section 3 is very short and is more difficult to read whereas it is probably the most important part of the paper. Figures are very hard to read with almost 19 coloured lines on each plot -- it is unclear to me what is the value of such plot for the reader and message of the paper. Finally there is no conclusion or discussion of future work, potential impact, weaknesses or whatsoever of the paper. 
- Soundness: Overall I have trouble to really understanding the practical relevance of estimating MI from samples as this ends up being equivalent to density estimation. It is thus very sensitive to the choice of model class and, in my opinion, inspecting MI depends as much on the model class chosen than on the samples. This is particularly true for higher dimensional problem where density estimation becomes intractable without strong modelling assumptions. I agree my statement is strong and there may exist certain usecases where estimating MI with minimal modelling assumptions can be relevant, however the paper fails to motivate such use cases and to demonstrate the value of the proposed approach for such settings. 
- Novelty: Normalizing flows perform density estimation while providing both density evaluation and sample generation. It is also clear and well known that the MI can be estimated by sampling and evaluating p(x, y) (potentially by exploiting Bayes' rule to decompose p(x,y) into factors). Thus I do not find the idea presented in this paper very novel and I can imagine many researcher have already used NF to estimate MI when they felt it was a useful value to look at.

### Questions
I do not understand why you couldn't simply learn a B-NAF (implicitly decomposing p(x, y) as p(x), p(y|x)) with standard MLE of the joint distribution of x, y. What is the gain of alternating between two optimization problem whereas directly solving density estimation with the right architecture would do the same job. Can you provide some motivation and why don't you compare to that more natural approach?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a training regime for a block neural autoregressive flow (B-NAF) for difference-of-entropies (DoE) estimation of mutual information using a single normalizing flow (as an alternative to the naive implementation with two flows). The paper evaluates the method on several synthetic mutual information estimation tasks.

### Strengths
- Originality: to the best of my knowledge, simultaneous estimation of conditional and unconditional density using a single normalizing flow with application to mutual information estimation has not been explored in literature before.
- Quality: good narrative flow, generally consistent mathematical notation, clear figures. The paper is self-contained: the authors provide an extensive introduction to normalizing flows and mutual information estimation, including relevant prior work.

### Weaknesses
 - Clarity: the proposed method is not presented with great clarity, and even after multiple reads I am not sure I understand _completely_ what the authors are proposing, and how it is motivated. In particular, it is not clear to me where the Eq. (11) comes from, and what the terms in it are precisely. The paragraph following Eq. (11) seems key to understand the idea, but is extremely dense and hard to parse. Authors repeatedly use the word "deactivate" (weights/sub-network), but don't explain precisely what it means. Algorithm 1 does not seem to optimize a part of the flow: $f_1$ (both losses only involve $f_2$). I suggest the authors shorten the Section 2 significantly (by e.g. moving parts to the appendix, or leaning more on prior work), and use the space to expand the Section 3, being more precise and clear when introducing and motivating their method.
- Significance: the benefit of using a single flow (as proposed, i.e. NDoE, BNAF) instead of two flows (BNAF) is not clear from the results presented. While authors claim that "proposed model achieved better performance across different dimensionalities and sample sizes", looking at Figures 2-5 I see, at most, a marginal improvement of NDoE, BNAF over BNAF, and often no improvement at all. The significance would be clearer if authors quantified the (relative/absolute) improvement in text, and provided an argument as to why it's significant (avoiding phrases like "_slight_ bias"). Moreover, authors only report results on synthetic data in the main text: if experiments were run on real data, authors should at least summarize the findings in the main text. Finally, in the conclusion authors say that they "plan to evaluate our method in view of downstream applications that require computation of mutual information" -- expanding the introduction to include a paragraph on what the most important applications of mutual information estimation are would further showcase significance.

### Questions
- Where does Eq. (11) come from precisely? Why does it not include the derivative of $f_2$ w.r.t $y$?
- How do we train $f_1$ using Algorithm 1?
- What do authors mean when they say "deactivate the off-diagonal weights" in Algorithm 1?
- What can authors say about the computational cost of the method compared to e.g. BNAF, i.e. training separate flows?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper expands on the difference-of-entropies (DoE) mutual information (MI) estimator
proposed by David McAllester and Karl Stratos in 2018.
In contrast to the original work, the authors use normalizing flows to model $p(X)$ and $p(X \mid Y)$,
which makes the estimator consistent.
Additionally, a clever trick is proposed to enable the estimation of $p(X)$ and $p(X \mid Y)$ via a single model.
This is achieved through the usage of the block autoregressive flows.
The paper includes comprehensive experimental results that highlight the practical advantages and disadvantages of the approach.

### Strengths
1. The paper is overall well-written, the motivation behind the DoE estimator and autoregressive models is presented clearly.
1. The idea of modelling two distributions via one flow model is interesting
   and is reminiscent to a similar technique successfully used in MINDE [1].
1. The scale of the final comparison (the number of other NN-based estimators featured) is truly commendable.
   This allows for a better assessment of the advantages of the proposed approach.
   The authors also provide a comprehensive analysis of the results.
1. Overall, the proposed method achieves better results compared to other NN-based approaches.

### Weaknesses
1. Despite the strength №3,
   the set of benchmarks used to evaluate the estimators is very limited and can be considered outdated.
   The authors employ some simple tests from (Czyż et al., 2023),
   but do not consider the distributions which might pose a real challenge to flow-based approaches due to the manifold-like structure:
   the Swiss Roll embedding and the spiral diffeomorphism.
   Additionally, in (Butakov et al., 2024) and in [2], several complex and high-dimensional image-like datasets
   with tractable MI have been proposed.
   Although the authors conduct a number of tests on the MNIST dataset, checking that selected properties of MI also hold for their estimator,
   the work would still benefit greatly from image-like tests for which the ground truth value of MI is available.
1. Although I clearly see that the DoE estimator combined with two expressive enough flow models is consistent,
   a rigorous proof still has to be provided in order to show that the same holds for using only one model;
   please, see the questions.
1. Combining the proposed estimator with a dimensionality reduction technique during the tests with MNIST seems unfair.
   If the proposed estimator fails to estimate MI between images
   (which definitely might happen due to certain limitations of the generative models used),
   this should be clearly represented as a limitation of the method.
1. The major limitation of the proposed method in its current form is that it is only applicable to continuous distributions,
   whereas critic-based methods (MINE, InfoNCE, ...) work with any types of distributions out-of-the-box.
   The authors should address this limitation properly in their manuscript.
   I also suggest dedicating a separate paragraph to all the limitations of the proposed method.

**Minor:**

1. The novelty of this work is limited due to the main ideas behind the DoE estimator being explored in (McAllester & Stratos, 2018).
1. The authors do not compare their method to other approaches based on generative models,
   such as [1] and (Ao & Li, 2022; Duong & Nguyen, 2023; Butakov et al., 2024).
1. The first plot in Figure 16 features a dashed line, which is misleading.
   For this particular test, there are no clues which ratio we should expect to see,
   as the information about $X$ can be distributed non-uniformly among the rows.
   Moreover, the test itself is ill-posed, as $I(X;X) = I(X;Y) = +\infty$ in this particular case;
   I, however, acknowledge that the test is borrowed from the work of Song & Ermon (2020).
1. Due to the source code being absent from the supplementary materials, the reproducibility can be questioned.

### Questions
1. As only $p(X)$ and $p(X \mid Y)$ are modeled,
   why can not we always use the original values of $y$ to condition the corresponding flows for $x$?
   Is there any need to assume continuity of $Y$ and apply transformations to $Y$ alongside $X$?
   If the answer is "no", then the method could be generalized to any type of $Y$ (including discrete or mixed distributions),
   provided that $p(X)$ and $p(X \mid Y)$ still exist.
1. What is the difference between "NDoE, BNAF" and "BNAF"?
   Do I understand correctly that in "BNAF", $H(X)$ and $H(X \mid Y)$ are approximated via two separate flows?
1. How were the confidence intervals obtained?
1. NDoE, Real NVP is mentioned in Figure 5, but absent from the actual plot. Why?
1. There seem to be some minor issues with notation in Theorem B.1.
   Firstly, in the statement, $T$ is applied to $(y,x)$, but in the proof, the order is reversed:
   $U$ is applied to $(x,y)$.
   Of course, this is still perfectly valid; however, it introduces some unnecessary confusion.
   Secondly, from the notation $V = (T_1, \overline{T})$ it is not obvious that
   $\overline{T} \colon \mathbb{R}^{2n} \to \mathbb{R}^n$ (which, I assume, is implied here).

   Additionally, it seems that this theorem can be easily extended to the case of $X$ and $Y$ being of different dimensionalities.

   I kindly ask the authors to address my concerns regarding this theorem.
1. In Corollary B.2, $q$ is not defined.
   The role of $f = (f_1, f_2)$ is also not explained properly
   (as for the current state of the corollary, this can be any block-triangular normalizing flow).
   Please, clarify.
   I also suggest addressing the following notation conflict: $g$ in Corollary B.2 and on lines 742--743
   is not the same as on lines 751-755.
1. It might be due to the previously mentioned issues,
   but the following claim lacks rigorous backing:
   "Corollary B.2 suggests that given enough expressive power of our neural network architecture,
   we can (train?) the network to both approximate $H(X \mid Y)$ and $H(X)$".
   As we do not choose $g$ in Corollary B.2, it is not obvious that it is possible to achieve $\forall x,y \;\; g(y, f^x(x)) = f^x(x)$.
   Please, address my concerns and provide a more formal bridge between Corollary B.2 and the claim in question.

**Additional references:**

[1] Giulio Franzese et al. MINDE: Mutual information neural diffusion estimation. *Proc. of ICLR 2024.*

[2] Lee K., Rhee W. A Benchmark Suite for Evaluating Neural Mutual Information Estimators on Unstructured Datasets. *Proc. of NeurIPS 2024.*

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose using a version of DoE estimators to create an unbiased version of parameterizing normalizing flows to estimate mutual information. They do this by deactivating certain parts of the network to estimate each of the two entropy terms. They demonstrate their method across a variety of synthetic distributions with different transformations.

### Strengths
The current method can be flexibly parameterized any type of normalizing flows with a conditional dependence for MI estimation. Theory wise, everything is quite clear and intuitive.

### Weaknesses
Currently, the experiments test against a lot of baselines, but don't particularly highlight their main contribution in terms of the addition of the DoE estimator (given that a normalizing flows for MI estimation paper exists). The main comparison experimentally is with standard BNAF, and the results for that aren't fully convincing of the advantages of the method. One simple way to add an additional comparison is to have a standard RealNVP without the NDoE portion, for an apt comparison. Alternatively, adding DoE to some of the other baselines presented (while cutting down on the total number, as the error bars are quite hard to read with that many baselines, many of which do not contribute particularly to the argument) would also be good. Also, you may want to consider presenting some of the baselines in a table instead (perhaps in the appendix).
The abstract doesn't seem to contain your main contribution here, which can be quite confusing.

Some of the charts seem to be missing a baseline (e.g. NDoE, RealNVP in Figure 5 and Figure 9), which I presume is due to the line in the text where it is stated that NDoE, Real NVP failed to achieve realistic results in the Sparse Gaussian case. Is this something due to the RealNVP, or did the NDoE part also affect it? Is there some intuition or explanation for why this happened?
Is there a reason for not including a standard RealNVP approach (without the NDoe) in the baselines?

### Questions
Some of the charts seem to be missing a baseline (e.g. NDoE, RealNVP in Figure 5 and Figure 9), which I presume is due to the line in the text where it is stated that NDoE, Real NVP failed to achieve realistic results in the Sparse Gaussian case. Is this something due to the RealNVP, or did the NDoE part also affect it? Is there some intuition or explanation for why this happened?
Is there a reason for not including a standard RealNVP approach (without the NDoe) in the baselines?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a novel method for the estimation of mutual information between arbitrary, continuous random variables, extending the range of estimators from the literature. The key idea stems from the seminal work by McAllester & Stratos (2018), in which mutual information is cast as an optimization problem by noting that entropy and conditional entropy can be estimated as infimum of cross-entropies computed with an approximation density.

Such density, in the presented work, is obtained by the application of normalizing flows, that transform a base normal distribution into an arbitrary distribution, which is used in the optimization problem discussed above. The authors clearly indicate how to use recent advances in the theory and practice of normalizing flow to build an approach that is computationally cheap, by means of an amortization approach. Indeed, they can estimate mutual information, and the elements described above (entropy and conditional entropy) with a single network.

A large number of synthetic experiments complement the presented methodology, illustrating the advantages of the proposed method when compared to a number of alternatives from the literature. Such experiments include cases in which the original Gaussian distributions are transformed by means of non-linear functions. Furthermore, the appendix contains additional experiments including self-consistency tests, as done previously in the literature.

### Strengths
* Section 2.1 is very clear, and contains a good summary of known results from McAllester & Stratos (2018) in sections 5.1 and 5.2, setting the stage for a much advanced parametrization of the two optimization problems of estimating cross entropies to obtain estimates of entropy and conditional entropy, by means of an amortized, flow-based approach. I think this is an original idea which displays good performance in practice.

* Section 2.2 is also very clear and didactical, motivating the need for efficient variants of the base normalizing flow approach, which can be costly from the computational perspective. Ultimately, a block autoregressive formulation is what the authors used for MI estimation. I really like, again, the clear and didactical approach to explain the “amortization technique” to activate part of the flow network to obtain estimates of the various quantities required to solve the optimization problem in Equation 3.

* Despite some questions (see below), the experimental section is very thorough (including also the results presented in Appendix C, which complement substantially the standard benchmark results in the main part of the paper).

### Weaknesses
 * Expression at line 37 is the equivalent of equation 7 in McAllester & Stratos (2018), which is a difference of entropies. The authors anticipate equation 14 in McAllester & Stratos (2018), which instead involves cross-entropies as upper bounds of the entropy and conditional entropy. I think this can be easily clarified in the paper, as the authors correctly characterize their expressions as the infimum of cross entropies that they translate to a variational problem.

* Section 1.1 offers a detailed overview of alternative MI estimators, but misses one important approach that has appeared prior to the last reviewed method from Butakov et al (2024), namely the MINDE estimator proposed in Franzese et al., “Mutual information neural diffusion estimator”, ICLR 2024, which also targets arbitrary, high-dimensional continuous distributions, making it a good candidate for comparison in the experimental evaluation.

* Experiments in section 4 rely only on synthetic data, which is a necessity to gain access to ground-truth MI, and to perform a comparative analysis among methods. The authors build upon prior benchmark studies, and propose a series of synthetic random variables sampled from Gaussian distributions with varying dimensionality, and having access to various sample sizes. They also consider one non-linear transformation by applying a cubic function to one of the variables. While in all such cases, the proposed method performs well, I am curious to understand why (also by looking at experiments in Appendix C, including additional transformations) the proposed method struggles with highly non-linear transformations. If on the one hand, the authors claim that the superiority of the proposed method in the Gaussian case might be “likely be due to the fact that the base distribution is itself Gaussian” (line 409), when this is not the case, does it mean that normalizing flows struggle with arbitrary distributions? This should not make sense right? So what is the problem, which is exacerbated by an high MI regime?

* One last question on the experiments is in order. Recent work, such as Kong et al, “Interpretable Diffusion via Information Decomposition”, ICLR 2024, Franzese et al. “Mutual information neural diffusion estimator”, ICLR 2024, illustrate some practical applications in which mutual information estimation can be instrumental. Have the authors attempted at estimating MI between complex distributions such as $X \sim \text{image data}$ and $Y \sim \text{Text embeddings}$? This question is important to fully grasp the potential impact of MI estimators that can be useful in the machine learning community for a variety of purposes.

### Questions
I do not have more questions than those discussed in the weaknesses. Apart from missing one reference that I saw recently, and some questions on the experiments, this is a nice work, in my opinion.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new difference of entropies estimator for mutual information (MI). The estimator uses a block autoregressive flow and shows good performance on benchmarks.

### Strengths
- Good summary of exisiting methods
- Clearly written
- Promising performance on benchmarks

### Weaknesses
 - Robustness of results to different hyperparameter settings could be explored in more depth
- Figures are hard to read and not colorblind friendly
- Minor: Reference section deserves revision; many inconsistencies

### Questions
- How do methods compare when using half or double the parameter count?
- Have you considered alternative ways of reporting the results? The plots feel very crowded and are hard to discern.

### Soundness
3

### Presentation
3

### Contribution
3
