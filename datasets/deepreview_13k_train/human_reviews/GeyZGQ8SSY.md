# Learning-Augmented Learning of Gaussian Mixture Models

- Decision: Reject
- Scores: 5, 3, 6, 3

## Abstract
Gaussian mixture models (GMMs) is one of the most fundamental methods to identify and extract latent structure in complex datasets. Unfortunately, well-known hardness results require that any algorithm for learning a mixture of $k$ multivariate Gaussian distributions in $d$-dimensional space requires both runtime and sample complexity exponential in $d$, even if the Gaussians are reasonably separated. To overcome this barrier, we consider settings where algorithms are augmented with possibly erroneous ``advice'' to help learn the underlying GMMs. In particular, we consider a natural predictor that can be easily trained through machine learning models. Specifically, our predictor outputs a list of $\beta$ possible labels for each sample from the mixture such that, with probability at least $1-\alpha$, one of the labels in the list is the true label, for a fixed constant $\alpha$. We show that to estimate the mixture up to total variation distance $\tilde{\mathcal{O}}(\varepsilon)$, we can use $k\cdot\text{poly}\left(d,\log k,\frac{1}{\varepsilon}\right)$ samples from the GMM, provided that $\beta$ is upper bounded by any fixed constant. Moreover, our algorithm uses polynomial time, thus breaking known computational limitations of algorithms that do not have access to such advice.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper considers the setting of "learning-augmented" algorithms where the sample/computational efficiency of algorithms is improved through the presence of predictions/advice from machine learning models, analogous to the settings of "expert-advice" considered in online learning. The paper proposes algorithms for estimation a Gaussian-mixture model in total-variation distance in the presence of a possibly erroneous list of labels for each sample. The proposed algorithms are polynomial-time and have sample-complex linear in the number of classes and polynomial in dimension $d$. The algorithms rely on seperability assumptions either on the means or the spectrum of the covariances.

### Strengths
- The general direction of ``learning-augmented" algorithms is promising.
- The paper is well-written apart from certain consistency issues described in the ``weaknesses" section.
- The paper includes numerical verifications of the proposed algorithm's efficacy.

### Weaknesses
 - I believe there are certain definitional and consistency issues that need to be addressed. Firstly, from Definition 2.4 it is not clear whether the list of labels correspond to a fixed-known list of means and covariances. From the use of Theorem 3.4 in Algorithm 3 it is clear that this is not the case but this should be transparent in Definition 2.4. Specifically, the definition should clarify whether the provided labels are associated with a fixed set of parameters (means and covariances) or if they are simply a list of class assignments without a direct correspondence to the underlying model parameters. This ambiguity makes it difficult to understand the precise nature of the 'advice' provided to the algorithm and how it relates to the true parameters of the Gaussian mixture model.
- Second major issue is in Definition 3.1 which defines only when $d_{param}$ is upper bounded. This definition isn't sufficient to understand what the lower-bound on $d_{param}$ means in Lemma 3.1. Does it mean that none of the conditions in definition 3.1 are satisfied? The definition should explicitly state what constitutes a lower bound on $d_{param}$, rather than implicitly suggesting it through the negation of the upper bound conditions. For example, does a lower bound imply a minimum separation between means or a minimum eigenvalue for the covariance matrices? The lack of clarity here makes it challenging to assess the scope and applicability of Lemma 3.1.
- The proofs are not self-contained and require going through the details of existing works such as Diakonikolas et al. (2017, 2020). This reliance on external proofs makes it difficult for the reader to verify the correctness of the results without significant effort. While referencing existing work is acceptable, the key steps and adaptations of those proofs to the specific context of this paper should be clearly outlined to ensure the paper is self-contained and accessible.

### Questions
- How would the results change if the number of classes in not known before-hand?
- In Algorithm 3, why is the list-decoding parameter represented as $\frac{1}{\beta}$ ?
- What is the explicit dependence of the sample-complexity on $\beta,\alpha$?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors provides an algorithm for estimation of a GMM up to total variation distance $\epsilon$  that scales linearly with the number of components - this is possible by exploiting auxiliary information which provides a list of labels which has the correct one with probability 1-\alpha. In some sense, the authors claim that this paper breaks the exponential in components lower bound on GMM parameter estimation.

### Strengths
The paper is well-written

### Weaknesses
The problem is highly fabricated. There is absolutely  no motivation provided to study this problem - in which use case can such a scenario  occur and why should anybody care about a mixture of gaussian study where the number of components is not a constant? It would be great if the authors can provide some motivating examples/ experiments on real world datasets where the number of components is large enough to actually see a difference.

The authors mention that they can use "heuristic such as kmeans++ to cluster the initial data, and use the resulting
centers to form a predictor for the second half of the data”. However such a heuristic does not provide confidence signals to the labels - I am confused regarding this statement with respect to kmeans++. Can the authors explain how kmeans++ or other heuristics could be used to generate the list oracle with confidence signals, as this connection is not immediately clear?

From the example provided in lines 111-123, it seems a robust algorithm for learning mixture of Gaussians will be sufficient - why is this not the case for the general problem? Specifically, the example seems to suggest that if we have some data that is close to the true means, then a robust algorithm should be sufficient to learn the true parameters. The paper does not clearly explain why this is not the case for the general problem, and what specific aspect of the general problem makes it so much harder.

Theorem 1.1 states guarantees in terms of the Total Variation distance which is different from parameter estimation that has been proved in Moitra and Valiant - is there a reference which says that large TV distance always implies large parameter distance. Why is the result not stated in terms of parameter distance directly is very confusing to me - why is this left to the reader when the authors claim parameter estimation as one of their goals.  Can the authors please restate their main result directly in terms of parameter distance?

In a paper, theorem statements cannot be theorems from other papers (even if cited) - Theorem statements are always main contributions of the paper.  Can the authors clearly distinguish between their novel theoretical contributions and existing results they are building upon - perhaps make different sections including preliminaries?

### Questions
Please see above

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
The paper presents an informed strategy for learning a Gaussian mixture model. Given a set of $n$ datapoints sampled from a mixture of $k$ Gaussians, it is assumed that an oracle provides, for each point $i$, a list $P_i$ of $\beta$ possible class labels so that with probability at least $1-\alpha$ the correct label appears in the list. The mixture is then estimated in polynomial time in $n$ up to total variation distance $\tilde{\mathcal O}(\varepsilon)$ if $n=k\\,\text{poly}(d,\ln k,\varepsilon^{-1})$.

### Strengths
The algorithm proposed in the paper exemplifies how even possibly corrupted and partial information on the label of data points sampled from a Gaussian Mixture Model can help to construct a Mixture that is close in total variation distance to the true one in polynomial time, as long as the dataset size is large enough. The actual generation of the lists of candidate Gaussians is based on the result in Theorem 3.4, i.e., on a strategy proposed by [Ivkov and Kothari](https://arxiv.org/abs/2206.10942), the main subsequent manipulations being related to the measure of the distances between the generated Gaussians and possible its merging. Nevertheless, the criteria used for merging and the size of the dataset required for the success of the strategy (e.g., having enough points to sensibly sample each class) are under analytical control, which guarantees the statement of the main contribution of the paper.

### Weaknesses
A weakness of the paper is the fact that, as the authors state, the strategy very heavily relies on the fact that the objects under analysis are *Gaussian* mixtures. To my understanding, the robustness of the strategy when the underlying mixture is not composed by Gaussian clouds is not obvious. An additional weakness of the paper is, in my opinion, its not outstanding clarity and, at some points, its lack of precision (see the *Questions* section below). This weakness might be fixed after an adequate revision.

I list below some comments and observations.

- It appears there is a broken sentence in Definition 2.4, "for which $x_i$...?".
- In Definition 3.1 it should be clarified that at least one of the conditions has to hold. Also, the relative-Frobenius closeness relation has to be fixed (there is a very curious typo...)
- In the pseudocode for ```Algorithm 1```, do the authors mean at line 4 "for $i,j\in[|\mathcal L|]$"? The pseudocode is not very clear in expressing what the output is: shouldn't it be the list $\{\mathcal G_a\}_{a}$ of grouped pairs? Is the new list $\mathcal L$ made of a single representative for each group (to make then sense of Observation 3.5)?
- In the pseudocode for ```Algorithm 2```, $\mathcal P$ never appears to be used after initialization except to be returned. Also, the authors use the notation $\mathcal P_i$ and $P_i$: please make the text more precise.
- In Lemma 3.8, what is $\gamma$? In Algorithm 3 it seems to be put equal to $\frac{1}{2}$ and never updated. From comparison with the Appendix, this quantity seems to be related to the oracle error rate (in particular, an upper bound to it).
- The ratio behind the choice for $\Delta$ in line 3 of Algorithm 3 stems, from my understanding, from the proof of Lemma 3.8, and similarly the numerical prefactor appearing in Lemma 3.9: could the authors give an intuition behind them? Also, Algorithm 3 refers to $\tilde P_i$ which is, I suppose, the oracle input: is this correct? Moreover, step 13 in Algorithm 3 evokes the ```RobustGaussian``` algorithm in Theorem B.5: I think it would be convenient to mention, at least briefly, this step in the main text and give a proper reference.
- Typo at line 474 (sentence starts with "finds").
- I would like the authors to clarify a little bit more how the generation of the list of Gaussians in the numerical experiment has been performed. From what I understand, the authors neglected the Frobenius separation criterion: is this correct? Also, are numerical experiments performed in $d=2$? Do the authors have a numerical estimate of the decay rate in $n$ of $d_{\rm TV}$ between the ground truth and the reconstructed GMM as $n$ grows?

On a more general question, as the algorithm is fed by a dataset of "oracle-labeled points" I was wondering how the performance of the algorithm would compare with the training error in a "standard" multiclass classification strategy by using, for example, a cross-entropy loss on the dataset by assigning to each datapoint $\boldsymbol x_i$ a label $\boldsymbol y_i=(y_{ij})_{j\in[k]}$ having components $y_{ij}=\frac{1}{\beta}$ if $i\in \tilde P_j$ and zero otherwise (see, e.g., the high asymptotic analysis in [Loureiro et al. (2021)](https://proceedings.neurips.cc/paper/2021/hash/543e83748234f7cbab21aa0ade66565f-Abstract.html) for the case $n\sim d$). Would this strategy be feasible if one is only interested in the correct labeling of the data points (and not in the reconstruction of the mixture)? How would this approach compare with the proposed one?

As a side note, the paper refers to the additional information exploited by the proposed algorithm to achieve its performance as *learning* provided. To my understanding, the fact that the input predictor is provided by some machine learning strategy plays essentially no role in the results: maybe a more suitable name for the manuscript would have been *Oracle-augmented* more than *Learning-augmented*.

### Questions
I list below some comments and observations.

- It appears there is a broken sentence in Definition 2.4, "for which $x_i$...?"
- In Definition 3.1 it should be clarified that at least one of the conditions has to hold. Also, the relative-Frobenius closeness relation has to be fixed (there is a very curious typo...)
- In the pseudocode for ```Algorithm 1```, do the authors mean at line 4 "for $i,j\in[|\mathcal L|]$"? The pseudocode is not very clear in expressing what the output is: shouldn't it be the list $\\{\mathcal G_a\\}_{a}$ of grouped pairs? Is the new list $\mathcal L$ made of a single representative for each group (to make then sense of Observation 3.5)?
- In the pseudocode for ```Algorithm 2```, $\mathcal P$ never appears to be used after initialization except to be returned. Also, the authors use the notation $\mathcal P_i$ and $P_i$: please make the text more precise.
- In Lemma 3.8, what is $\gamma$? In Algorithm 3 it seems to be put equal to $\frac{1}{2}$ and never updated. From comparison with the Appendix, this quantity seems to be related to the oracle error rate (in particular, an upper bound to it).
- The ratio behind the choice for $\Delta$ in line 3 of Algorithm 3 stems, from my understanding, from the proof of Lemma 3.8, and similarly the numerical prefactor appearing in Lemma 3.9: could the authors give an intuition behind them? Also, Algorithm 3 refers to $\tilde P_i$ which is, I suppose, the oracle input: is this correct? Moreover, step 13 in Algorithm 3 evokes the ```RobustGaussian``` algorithm in Theorem B.5: I think it would be convenient to mention, at least briefly, this step in the main text and give a proper reference.
- Typo at line 474 (sentence starts with "finds").
- I would like the authors to clarify a little bit more how the generation of the list of Gaussians in the numerical experiment has been performed. From what I understand, the authors neglected the Frobenius separation criterion: is this correct? Also, are numerical experiments performed in $d=2$? Do the authors have a numerical estimate of the decay rate in $n$ of $d_{\rm TV}$ between the ground truth and the reconstructed GMM as $n$ grows?

On a more general question, as the algorithm is fed by a dataset of "oracle-labeled points" I was wondering how the performance of the algorithm would compare with the training error in a "standard" multiclass classification strategy by using, for example, a cross-entropy loss on the dataset by assigning to each datapoint $\boldsymbol x_i$ a label $\boldsymbol y_i=(y_{ij})\_{j\in[k]}$ having components $y_{ij}=\frac{1}{\beta}$ if $i\in \tilde P_j$ and zero otherwise (see, e.g., the high asymptotic analysis in [Loureiro et al. (2021)](https://proceedings.neurips.cc/paper/2021/hash/543e83748234f7cbab21aa0ade66565f-Abstract.html) for the case $n\sim d$). Would this strategy be feasible if one is only interested in the correct labeling of the data points (and not in the reconstruction of the mixture)? How would this approach compare with the proposed one?

As a side note, the paper refers to the additional information exploited by the proposed algorithm to achieve its performance as *learning* provided. To my understanding, the fact that the input predictor is provided by some machine learning strategy plays essentially no role in the results: maybe a more suitable name for the manuscript would have been *Oracle-augmented* more than *Learning-augmented*.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the following problem.
Given samples from a mixture of $k$ $d$-dimensional Gaussians with labels, we would like to return another mixture of $k$ Gaussians such that the total variation of them is at most $\epsilon$.
Here, the label comes with each sample indicating that which component in the mixture the sample is drawn from and the label may not be correct.
Moreover, we assume that the components in the mixture are well-separated.

The result replies on the ROBUSTGAUSSIANS algorithm from (Diakonikolas et al., 2020) which considers the setting of learning mixtures of Gaussians with corrupted samples.
In this paper, the authors exploit the similarity between these two settings and apply ROBUSTGAUSSIANS algorithm to their problem.

The authors show that we need $poly(dk/\epsilon)$ samples to achieve the goal.

### Strengths
The paper studies an interesting problem of learning mixtures of Gaussians with extra information. Also, the authors manage to show the polynomial sample complexity.

### Weaknesses
It seems that the key component is derived from a previous result (Diakonikolas et al., 2020). 
The rest involves using the labels to ensure that the conditions in the previous result hold, allowing us to apply it.
I am not sure if there are fundamentally new techniques introduced.

### Questions
.

### Soundness
2

### Presentation
2

### Contribution
2
