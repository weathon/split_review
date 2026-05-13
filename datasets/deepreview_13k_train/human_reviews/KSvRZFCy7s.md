# Differentially Private Low-dimensional Synthetic Data from High-dimensional Datasets

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
Differentially private synthetic data provide a powerful mechanism to enable data analysis while protecting sensitive information about individuals. However, when the data lie in a high-dimensional space, the accuracy of the synthetic data suffers from the curse of dimensionality. In this paper, we propose a differentially private algorithm to generate low-dimensional synthetic data efficiently from a high-dimensional dataset with a utility guarantee with respect to the Wasserstein distance. A key step of our algorithm is a private principal component analysis (PCA) procedure with a near-optimal accuracy bound that circumvents the curse of dimensionality. Unlike the standard perturbation analysis, our analysis of private PCA works without assuming the spectral gap for the covariance matrix.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a differentially private algorithm to generate low-dimensional synthetic data with theoretical utility guarantees over the accuracy of the resulting data. Proof-of-concept experiments are given on MNIST, demonstrating the approach can yield synthetic data that provides reasonable utility on downstream tasks.

### Strengths
This paper attempts to tackle and important problem which I agree has not been solved by existing DP literature. The theoretical analysis is rigorous and thorough and I have limited criticisms if this is pitched primarily as a theory paper. With that being said, I'm not convinced the most interesting problems in DP synthetic data create are theoretical at this stage.

### Weaknesses
My main criticism is that it is unclear how a practitioner looking to use this approach would know whether their data fits the regime in which the utility theorems hold. In particular, the experiments are very limited and in my view provide little information into the practical utility of the approach to most real-world datasets.  For instance it is very unclear that the inferences about the impact of choosing a smaller d' would generalize to other data. In my view the experiments need to be extended to a much wider set of datasets and downstream tasks. Currently the only evaluation is on the accuracy of a prediction, but one of the main benefits of sharing synthetic data is that in principle it could be used for a large stream of data analysis tasks, beyond training ML models (e.g. descriptive stats and regression tasks).

Related to my previous point, why is this the appropriate baseline approach in Figure 2? I would like to see this compared to training the classifier with DP-SGD directly without ever creating the synthetic data for instance and a classifier trained without DP. If the argument is that this approach lends itself to multiple training and analysis tasks, then a broader set of tasks should be included in the experiments. 

Finally, I would encourage the authors to include further intuition and descriptions of the algorithms in surrounding text to make the paper more readable. Currently the paper explains what each part of the algorithm does but I feel it lacks explanation of why this is a good idea.

### Questions
Why was such a high privacy budget chosen in the experiments? Did you try other values and how did this change the results?

How were hyper-parameters chosen in the experiments?

Have you thought about whether statistical inference is feasible from the output of your algorithm?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of generating low-dimensional synthetic datasets under the constraint of differential privacy (DP) accurately with respect to the Wasserstein distance. Their algorithms are computationally efficient and make no assumptions on the distribution of the underlying data. They provide both (primarily) theoretical and empirical results to demonstrate their findings.

Their algorithms is decomposed into a few steps. Private PCA followed by projections of data. Then they have an adaptation of the work from He et al (2023). The adding back the private mean vector to shift the subspace correctly.

### Strengths
1. The writing of this paper is quite good. The paper was easy enough to follow, and the results were cleanly written.
2. Working in low-dimensions is an important theme for computational and sample efficiency, so their work makes sense in that regime.
3. They don't require the data to have large eigenvalue gaps, so it is general enough by itself.

### Weaknesses
1. The expected Wasserstein distance is $poly(d)$. The second term is still alright if we have enough samples, but the third terms is the one that concerns me. When $d$ is large, the third terms does not really help a lot, especially when $d'$ is not too small. That said, the second term becomes too large if $d'$ is large, so there seems to be quite a trade-off over there.
2. More empirical evaluation would have been nice for this venue. I understand that this is mainly a theoretical work, but given that it might have very practical applications, more experimental work would have made sense.
3. The empirical accuracy is not significant when $\varepsilon$ is small, even when as small as $1$, although it does better than a direct application of the work from He et al (2023).

### Questions
1. Where are the empirical comparisons with He et al (2023) shown in the paper?
2. At the bottom of page 2, what are $\delta_{X_i}$ and $\delta_{Y_i}$? Should define them somewhere earlier.
3. How does the accuracy improve when the data is actually low-dimensional? It could be approximately low-dimensional, like in Singhal and Steinke (2021) or it could be exactly low-dimensional. How would the results change?
4. How do your results compare with the **lower bounds** on DP synthetic data generation?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
it is known that the expected utility loss of $\varepsilon$-DP synthetic dataset in 1-Wasserstein distance is $\Omega((\varepsilon n)^{-1/d})$. However, if the data lies in a $d'$-dimensional subspace, then one can construct DP synthetic data with $\tilde{O}((\varepsilon n)^{-1/d'})$ utility bound. However, the the previous work's algorithm (Donhauser et al., 2023) has runtime complexity of $O(d^{d'}n + poly(n^{d/d'}))$. 

In this work, the authors propose a polynomial-time algorithm for low-dimensional synthetic. The authors also claim that it has a better utility bound that that in Donhauser et al., 2023.

Mainly, the proposed algorithm employs (1) private PCA to project the data to a low-dimensional subspace and (2) hierarchical partition, where Laplacian noise is added to the count in each subregion in order to create a synthetic probability measure..

### Strengths
- The authors proposed a polynomial-time algorithm for DP synthetic data that can be more accurate than previous methods if the data is lying in a low dimensional subspace.
- The value of $d'$ can be chosen adaptively by looking at the singular values of the privatized covariance matrix.
- Privacy and utility analysis of the algorithm are provided.

### Weaknesses
 - The experimental against the full-dimension algorithm is convincing, but I also would like to see how it perform against the method of Donhauser et al. (2023), especially when the authors claim that their method is more accurate than that of the previous work.
- There should be a discussion on the $\sqrt{\sum_{i>d'}\sigma_i(M)}$ term, especially when $d'$ is unknown (which occurs in most use cases). How do we make sure that this term does not dominate the rest of the error bound? Specifically, it is unclear how the algorithm would perform if the singular values decay slowly, or if there is no clear gap in the singular value spectrum to select an appropriate $d'$.

Right now, I am mainly focusing on the soundness of the paper, but I am not fully convinced that the proposed method performs *strictly* better than that of Donhauser et al. (2023). Also see Questions below.

### Questions
- In the Conclusion, the authors claim that Donhauser et al. (2023)'s accuracy rate is $(\varepsilon n)^{-1/(d'+1)}$. I skimmed the said paper and couldn't found the exact bound. Can the authors point me to where the said bound is located?
- I think the upper bound can be used to find an "optimal" value of $d'$ by comparing $\sqrt{\sum_{i>d'}\sigma_i(\hat{M})}$ and the rest of term (we also might have to take the bias of $\sigma_i(\hat{M})$ into account. Can the authors make some comments on this approach?

Minor comments:  
- In Algorithm 1: "Let $\overline{X}$ be the mean value of the dataset". Is this the original or the synthetic dataset?
- Continuing from above, if it is the mean of the original dataset, can't we just save the privatized mean from the Linear Projection step and add it back after Low-dimensional Synthetic Data? This would help save the privacy budget by $\varepsilon/4$.
- In Algorithm 1, I see two mechanisms with privacy budget $\varepsilon/2$, and two with $\varepsilon/4$. I am not sure if I am interpreting this correctly since total privacy budget is larger than $\varepsilon$.
- In Algorithm 2, the definition of $\boldsymbol{A}_{ij}$ when $i>j$ is missing.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method to generate DP synthetic data that projects the data into a low-dimensional linear subspace, generates synthetic data there, and projects it back. Projecting to a low-dimensional subspace improves the dimension dependency of the accuracy if the data actually lies close to that subspace. The paper proves a Wasserstein distance accuracy guarantee, and conducts a single experiment on an image dataset.

### Strengths
The paper is fairly easy to understand, despite being theory-heavy. Using PCA in this way to get around the curse of dimensionality in DP synthetic data generation is novel to my knowledge.

### Weaknesses
## Major Issues
The Laplace mechanism should be introduced in the paper, and its privacy guarantee should be stated. The parameter of the Laplace mechanism should be $\frac{\Delta_1}{\epsilon}$ for $\epsilon$-DP, where $\Delta_1$ is the $L_1$-sensitivity (Dwork and Roth 2014, Definition 3.3). The paper uses the Laplace mechanism to release $\bar{X}$ in Algorithms 1 and 3 with $\Delta_1 = \frac{1}{n}$. However, if the data is $d$-dimensional, the $L_1$ sensitivity of $\bar{X}$ is $\frac{d}{n}$, so it looks like Algorithm 1 does not have the advertised privacy bound. The incorrect sensitivities are used in the accuracy analysis (for example equation C.7), so they are unlikely to be just typos.

The "private covariance matrix" and "private linear projection" steps in Algorithm 1 should have $\epsilon / 4$, not $\epsilon / 2$. This is because the composition theorem for differential privacy requires that the privacy budget is split among the different mechanisms used. Since there are four mechanisms used in Algorithm 1, each should have a privacy budget of $\epsilon/4$ to achieve $\epsilon$-differential privacy for the whole algorithm.

## Minor Issues
The paper should mention that the experiment considers the image labels to be public information in the experiment, so they don't have privacy protection. This is an important detail that needs to be made explicit, as it affects the interpretation of the results. The lack of privacy for the labels should be clearly stated to avoid any confusion about the scope of the privacy guarantees.

The generated images look very poor compared to images showcased in the DP-MERF paper (Harder et al. 2021) for MNIST. As the datasets are different, it would be good to compare with DP-MERF on the dataset used in the paper. This would provide a more meaningful comparison and help to contextualize the performance of the proposed method. The current lack of comparison makes it difficult to assess the practical value of the approach.

### Questions
- You claim that the Wasserstein distance bound gives accuracy guarantees for many machine learning algorithms. How strong are these guarantees in practice? For example, what is the accuracy guarantee for the SVM in the experiment of the paper (if there is one)?
- What is the accuracy of the SVM on the real data, without DP?
- Assuming that the data lies close to a low-dimensional linear subspace (instead of a more general manifold) sounds very restrictive. Do you have some idea on what settings would this assumption be realistic in?
- Is $\sigma_i(M)$ the $i$-th largest eigenvalue in Theorem 1.2, or is the order something else?
- How could $d'$ chosen in practice?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
