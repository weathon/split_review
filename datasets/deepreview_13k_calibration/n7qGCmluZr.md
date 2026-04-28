# PQMass: Probabilistic Assessment of the Quality of Generative Models using Probability Mass Estimation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
\spacehack{\vspace{-0.2cm}}
We propose a comprehensive sample-based method for assessing the quality of generative models. The proposed approach enables the 
estimation of the probability that two sets of samples are drawn from the same distribution,
providing a statistically rigorous method for assessing the performance of a single generative model or the comparison of multiple competing models trained on the same dataset. This comparison can be conducted by 
dividing the space into non-overlapping regions and comparing the number of data samples in each region.
The method only requires samples from the generative model and the test data. It is capable of functioning directly on high-dimensional data, obviating the need for dimensionality reduction. Significantly, the proposed method does not depend on assumptions regarding the density of the true distribution, and it does not rely on training or fitting any auxiliary models. Instead, it focuses on approximating the integral of the density (probability mass) across various sub-regions within the data space.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces PQMass, a likelihood-free approach for assessing the quality of generative models by comparing sample distributions without estimating probability densities. PQMass operates by dividing the sample space into non-overlapping regions, using chi-squared tests to measure the similarity between the distributions of real and generated samples in these regions. The method yields a p-value indicating whether samples from two sets arise from the same distribution. Authors argue that PQMass offers several advantages: it does not require auxiliary models or feature extraction, works across various data types, and scales to moderately high-dimensional data. Through experiments, authors aim to show that PQMass is effective in evaluating fidelity, diversity, and novelty in generated samples, providing a robust alternative for assessing generative models in machine learning.

### Strengths
- PQMass introduces a new, likelihood-free approach for evaluating generative models by comparing sample distributions without density estimation or feature extraction, which is a fresh alternative to traditional metrics like FID and MMD.

- The experiments are comprehensive, testing PQMass across various generative models, data types, and dimensions. The paper includes comparisons with established metrics, scalability tests, and ablation studies, which aims to show PQMass’s robustness, scalability, and ability to assess fidelity, diversity, and novelty effectively.

- PQMass offers a potentially practical, scalable solution for evaluating fidelity, diversity, and novelty in generative models across diverse, high-dimensional data domains, filling relevant gaps in current model evaluation techniques.

### Weaknesses
 - The use of L2 or L1 distance metrics may limit PQMass's effectiveness, especially when the data resides on a complex manifold. These metrics, which operate on raw data points, may not capture meaningful semantic or structural differences in such cases. For instance, in high-dimensional spaces, the Euclidean distance can become less informative due to the curse of dimensionality, potentially leading to inaccurate assessments of distribution similarity. This is particularly concerning when the underlying data distribution is highly non-uniform or concentrated on a lower-dimensional manifold within the ambient space.

- Experimental evaluation mostly focus on synthetic data or standard datasets like MNIST and CIFAR-10. While these datasets are useful for initial validation, they do not fully represent the complexities of real-world data. The performance of PQMass on these datasets may not translate to more challenging scenarios with higher dimensionality, complex dependencies, or noisy data. Testing on more complex, real-world datasets, such as those found in medical imaging or natural language processing, would strengthen PQMass’s claims about the practical applicability of the proposal.

- Although the paper briefly addresses other data types, it primarily evaluates PQMass on image data. The method's reliance on simple distance metrics may not be suitable for complex, structured data such as text or biological sequences, where the notion of distance is not straightforward. For example, in text data, semantic similarity is often more relevant than raw pixel-level differences. Expanding experiments to more complex, structured data and analyzing the impact of different distance metrics in these contexts would help to better validate PQMass performance.

### Questions
I would like to hear authors' opinions about the detailed weaknesses of their proposal.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a method for testing for the equality of two distributions from which two samples are obtained, by partitioning the sample space and comparing the multinomial vectors of counts of samples in each of the partitions via a chi-squared-distributed test statistic. The approach works for broad classes of data.

EDIT: Following the review/discussion period and (prospective) changes to the manuscript by the authors, I am increasing my score by 1.

### Strengths
The paper is well presented and understandable. A broad range of examples and simulations were presented demonstrating fairly broad applicability. The test statistic is a basic and well known statistical quantity, so the method is fast to implement.

### Weaknesses
Not clear if this is a weakness or a strength, but the proposed test is a well known, basic statistical test. The contribution of this paper, therefore, is to note that its easy to apply this test to a broad range of data types in order to detect a difference between the generating distribution of two samples. It's not clear if this is substantial enough a contribution for ICLR, though I do not wish to imply that substantial contributions need to involve complex methods.

Consistency Guarantees:
I'm not quite clear on or convinced about some of the claims being made.
* a) Proposition 1: Does the consistency here require any conditions on m and n as they approach -> infinity? E.g., what about their relative convergence rates (does m->infinity faster than n, for example). E.g. what if m/n -> K, where K=infinity, a finite constant, or zero. Presumably K=infinity or K=0 would break things and the test would no longer work (especially as you're sampling finite n_R samples).
* b) Proposition 1: Some clarification on the claim also needed here, as it's conditional on the n_R samples. E.g. if p = t_{\nu_p} and q = t_{\nu_q} (univariate t distributions with different degrees of freedom), and z_1 = -z_2, then you will never distinguish p and q under any rates of m, n -> infinity.
* c) Proposition 2: This proposition is ok, but really this situation won't happen, as the method explicitly requires that the z_i are taken from the set of (x_i, y_j), and so n_R is bound by m+n which are fixed and finite in this proposition (though the method will fail far before this as there will be no samples left to calculate the test statistic), as noted in the discussion. So how useful is Prop 2 in practice, particularly for small m+n?
* d) Proposition 2: "no information is lost by the PQMass statistic." would seem to be a bit of an overextension in light of the above point. But also because for n_R->\infty, the distribution of the statistic under the null would be a chi-squared distribution with infinite degrees of freedom. "No information is lost" only happens in this limit (as otherwise with a finite n_R, information can clearly always be lost), but how does your test statistic compare to its null distribution in this limit?

Practical implementation comments:
* a) As far as I can tell, you've only considered exactly balanced samples each time: m=n. While in some applications the user has control over both m and n, this will not be the case in many scenarios. So how well does the test perform when the two samples are imbalanced, including extreme cases?
* b) Using reference samples z_i randomly taken from the two distributions (x_i) and (y_i) has a long history, even when comparing samples from two MCMC samplers (or the same MCMC sampler twice, when considering convergence diagnostics; e.g. Sisson & Fan (2007). Statistics and Computing, 17, 357-367). So this approach is fine. However, a disadvantage of this is that when p and q differ only, say, by a small mode with low weight in the tail, then by sampling uniformly over the x_i and y_j, one is reasonably likely to miss samples in this mode, as the sampling will naturally favour repeated samples in areas of higher density, and hence the test will miss the obvious difference between p and q. (The examples in Section 3 seemed to consider equally weighted mixtures only ...). Hence the need to repeat the test multiple times with different z_i. Is there any argument to be made to reconsider this equal sampling of the z_i from (x_i) and (y_j), to ensure there is a greater spread over the space, rather than doubling (and tripling, and ...) down on high density regions?
* c) Figure 2: presumably when "this process" is repeated 500 (or 200?) times, this also means resampling the z_i? (Could be clearer in the caption.) But really, this histogram doesn't really seem to follow the red density. Suggest that the number of reps is increased here considerably if you're wanting to claim these distributions are the same. Also the y-axis label of "Frequency" seems to be incorrect, as the axis ticks aren't measured in counts.
* d) In the results in general, the empirical mean of the PQMass statistic (4) seems to be taken as "the statistic" for determining whether p=q (or p!=q). Is it obvious that this mean statistic has a chi-squared(n_R) distribution under the null? Each of the components of this statistic are chi-squared(n_R) (conditional on z_i) under the null, but is it obvious that they are independent from eachother? (chi-squared(m) + chi-squared(n) = chi-squared(m+n) if the two LHS distributions are independent). Certainly the alternative distributions are not the same for different z_i. So can this "mean PQMass statistic" actually be compared to the chi-squared null distribution in any meaningful way? Or is the use of the mean PQMass statistic merely limited to relative value comparisons? In which case, the paper should be clearer about all of this and tone down the chi-squared relevance.
* e) Section 4: Limitations. The method also appears to require independent samples (x_i), (y_i), otherwise the multinomial model does not hold. How likely is this in practice? In the MCMC comparisons in Table 1? Etc.


Typos:
* p.2 para 2, wrong parentheses surrounding reference list starting with Theis et al.
p.5. Algorithm step 1. "choice" -> "chosen"
p.6. Section 3.1. The number of test replicates here is 200, but in Figure 2 it's listed as 500. One of these must be wrong.
p.6. Table 1. D was previously the distance metric between two sample points (c.f. Section 2.2, Algorithm). Now D has switched to number of dimensions. Maybe separate the notation?

### Questions
See Weaknesses.

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
4

### Summary
The authors proposed a simple method for comparing the distribution $q$ of a generative model with the true data distribution $p$. The proposed method first discretizes the data space and then compare the proportion of data points in each region. Since this becomes a distribution comparison for a multinomial distribution, it can be tested using Pearson’s $\chi^2$ test. If the test indicates a difference between the two distributions, one can conclude that $p \neq q$, making this method a sufficient condition for identifying distribution differences. The authors demonstrated the effectiveness of the proposed method on synthetic data as well as datasets such as MNIST and CIFAR-10.

### Strengths
The strength of the proposed method is in its simplicity. After discretizing the data space, one only needs to count the data points in each region and calculate the test statistic. This makes the method computationally much more efficient compared to existing distribution comparison methods, such as MMD.

### Weaknesses
A weakness of this study is the limited comparison with other two-sample test methods. The authors simplified the problem by dividing the data space and reducing it to a multinomial distribution comparison. However, various other methods have been proposed for distribution comparison not only MMD and W2. For example, [Ref1] explores distribution comparison using classifiers and its application to GAN evaluation, while simpler approaches, like those using nearest neighbors, are also available [Ref2]. Although the simplicity of the proposed method is an advantage, comparing its performance with these existing distribution comparison methods would be essential for evaluating its practical utility. Furthermore, the choice of discretization method and the number of bins used in the proposed approach could significantly impact the test's sensitivity and power. The authors do not provide a clear guideline on how to select these parameters, which could limit the reproducibility and general applicability of the method. Specifically, the curse of dimensionality might make it difficult to choose an appropriate discretization strategy for high dimensional data, and the authors should address this limitation in more detail.

### Questions
What are the strengths or advantages of the proposed method compared to other distribution comparison techniques beyond MMD and W2?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The article proposes a new method for comparing samples from two distributions, providing a hypothesis test for whether they are identically distributed. The method introduces a Voronoi tessellation, dividing the data space into non-overlapping regions, and then assumes a multinomial likelihood describing the prevalence of observed data in each of the regions: this likelihood is then used to develop a hypothesis test as to whether each distribution has the same underlying probabilities of generating data in each region, which then implies equivalence of the distributions with some assumptions. Some theoretical results are derived to strengthen this argument. The method is then tested on several empirical problems.

### Strengths
The idea is pleasingly simple for a relevant contemporary challenge in stats/ML, and explained pretty clearly. The experimental results are strong and quite convincing, especially in higher-dimensional problems without an obvious feature representation.
The figure quality is high throughout, which is a good thing in general.
The experiments themselves are pretty thorough, as are the descriptions of the experiments, especially the astrophysics experiments that might be hard for a non-expert audience. The example detecting the small additive noise is nice in Appendix F.2. Demonstrating the method can find an effect invisible to the naked eye is good.

### Weaknesses
The very high figure quality has the probably unintended consequence that the resulting pdf file size is very large (>17MB), which makes it kind of a pain to handle by conventional means. If there were some way to reduce this without overly compromising readability, then that would be good. I suspect that you have one or two figures in the appendix that are unnecessarily high resolution when printed out, but I haven’t figured out which ones (possibly figures 17/18).

A few small language issues:

“Miscrepancy” line 356. I assume you meant “discrepancy”? English in general pretty good.
“The instrument has multiple sources of non-Gaussian additive noise, including… Gaussian noise” is kind of odd.

Figure design:

Figure 6 is hard to understand immediately. The claim about “strongly correlate” (line 446) does not jump out intuitively from the data plotted.

Some of the descriptions of the method’s properties are a little overly flattering:

You call this a “Likelihood-free method”... but, you do use a multinomial distribution.
Desiderata 1: “PQMass works with the intervals of pdfs, it does not make assumptions about the true underlying density field”. The cdf is defined by the pdf, and assumptions about one will imply assumptions about the other, so I don’t think this argument is particularly strong.

“These results show that, at least for “well-behaved” densities, no information is lost by the PQMass statistics”
Did you not say at the start that you didn’t make assumptions about the underlying density?
“No information is lost” in what sense? Clearly information is lost when you quantise. Is this claim meant in some asymptotic limit?

### Questions
Methodological questions:

Is there any particular reason that you pursued Pearson’s chi squared test ahead of Fisher’s exact test, which should be less vulnerable to small contingency cell counts, which could easily happen here with the randomised voronoi tessellation?

Choice of centres:

Is it really hard to do better than random? Some sort of relatively simple diversity measure would potentially get you quite far here.
“Sample the reference points from a uniform mixture of the empirical distributions of samples from p and q”

What if there are more samples available from one distribution?

What if one of the distributions is known to be more accurate representation of reality and therefore give a better coverage of realistic regions of probability space?

“Perform the test multiple times”? How many is necessary? What are the computation implications?

“This effectively marginalizes the choice of tessellation”: this comment makes me wonder whether a Bayesian formulation of the problem would work well, since you are effectively having sample the latent allocation of the points to reference centres vs cell populations. There will be analytical conjugate Bayes solutions to the multinomial distribution comparison too, so there should be no more pesky posterior sampling in addition to what is being done already.

Data balance between distributions:

What if there are unbalanced numbers of samples available from each distribution? This will be quite common, since in general distributions are not equally easy to sample from. This is especially true if comparing simulated data and real data, or complex vs simpler models. How would this influence the sampling of reference points?

Limitations: good for you for being open “if the number of samples is too small”. Do you have any idea how small? Does it scale with p in a demonstrable way?

### Soundness
3

### Presentation
3

### Contribution
3
