# Probabilistic Hash Embeddings for Temporal Tabular Data Streams

- Decision: Reject
- Scores: 8, 3, 5, 5

## Abstract
We study temporal tabular data-streams (TTD) where each observation has both categorical and numerical values, and where the universe of distinct categorical items is not known upfront and can even grow unboundedly over time. Such data is common in many large-scale systems, such as user activity in computer system logs and scientific experiment records. Feature hashing is commonly used as a pre- processing step to map the categorical items into a known universe, before doing representation learning (Coleman et al., 2024; Desai et al., 2022). However, these methods have been developed and evaluated for the offline or batch settings. In this paper, we consider the pre-processing step of hashing before representation learning in the online setting for TTD. We show that deterministic embeddings suffer from forgetting in online learning with TTD, leading to performance deterioration. To mitigate the issue, we propose a probabilistic hash embedding (PHE) model that treats hash embeddings as stochastic and applies Bayesian online learning to learn incrementally with data. Based on the structure of PHE, we derive a scalable inference algorithm to learn model parameters and infer/update the posteriors of hash embeddings and other latent variables. Our algorithm (i) can handle evolving vocabulary of categorical items, (ii) is adaptive to new items without forgetting old items, (iii) is implementable with a bounded set of parameters that does not grow with the number of distinct observed items on the stream, and (iv) is efficiently implementable both in the offline and the online streaming setting. Experiments in classification, sequence modeling, and recommendation systems with TTD demonstrate the superior performance of PHE compared to baselines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the temporal tabular data streams (TTD), where each observation has both categorical and numerical values and the universe of distinct categorical items is not known upfront and can even grow unboundedly over time. As pointed out by the paper,  feature hashing is commonly used as a preprocessing step in this case but currently such a method is only considered for the offline or batch settings.
In this paper, the authors give a new stochastic method called probabilistic hash embedding (PHE) which applies Bayesian online learning to learn incrementally with data. The paper then shows that PHE is useful in the downstream inference algorithm implementation. Finally, the paper gives an empirical evaluation which demonstrates the advantage of the proposed method.

### Strengths
- The technical contribution of this paper is solid. The paper gives a stochastic method for feature embedding, which is based on the Bayesian online learning method while in the previous works that is only considered in the offline or batch settings. This is interesting to me. In addition, the paper also gives a theoretical explanation that shows the advantage of the stochastic embedding method compared to the deterministic embedding method.

- The paper gives a detailed experiment comparison, which demonstrates the advantage of the proposed method.


- The writing of the paper is good and the presentation is clear.

### Weaknesses
I am not an expert in the related field, hence currently I do not see some important weakness in this paper.

### Questions
N/A

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper discusses the problem of learning with temporal tabular data streams. The challenge in this setting is that the vocabulary of categorical data, and the relevance or meaning of categorical data fields can change over time. A fixed embedding of those categorical features, which is typical in offline methods, does not address those challenges in an online setting.

The paper proposed a new bayesian method, called probabilistic hash embedding (PHE), that is able to incrementally learn those embeddings based on the input data observed so far. The final goal is to learn an ML model in the TTD stream setting, exploiting the PHE.

The paper runs experiments to show the advantage of their method with respect to other different ways to update the categorical embeddings.

### Strengths
The work addresses an important problem. Tabular data is the most common source of data, and in an online setting, the changes in the vocabulary of categorical features and their meaning are an important problem. 

The paper provides an extension to existing prior methods that use a fixed unified embedding for the categorical features, which are not updated over time. I believe that the method proposed by the authors to update those embeddings, based on the input data, is original and significant.

### Weaknesses
I found Section 3 unclear and very hard to follow. The mathematical notation is often imprecise, and it is hard to understand what the paper is trying to accomplish. This is one of the paper's main weaknesses, making it hard to appreciate its contribution, and to understand the algorithm presented in the paper. This is the main reason for my final score.

I will give several examples:

In line 182, the hash function is defined to be a number. This is problematic because a hash function should map an input (e.g., a categorical feature) to a numerical index, not just be a single number. It's unclear how this single number is used to index into the embedding matrix.

E is a $B \times d$ matrix. What does it mean for a matrix E to be Gaussian with a diagonal covariance(see footnote 3)? A matrix cannot be Gaussian distributed; it's the elements of the matrix that can be. The footnote should clarify whether each element of E is sampled from a Gaussian with a diagonal covariance, and if so, what is the mean and variance of this Gaussian distribution.

What is the approximation in Equation (1)? Why does the expectation become probability? The transition from an expectation to a probability is not clearly justified. It's unclear what distribution the expectation is taken over, and why this expectation is equivalent to the probability term that follows. This needs a more rigorous explanation.

The discussion 209-215 seems to be out of place. It is not possible to follow comments like "only a few embeddings need to be updated online" since the update is not discussed in Section 3.2. In particular,  Lines 209-215 for the paragraph "Discussion" seem completely unrelated to Section 3.2

Section 3.3 discusses how PHE can be used in conjunction with Deep Kalman Filter. However, Deep Kalman Filter is also never presented or discussed. The paper assumes the reader is familiar with Deep Kalman Filters, which is not appropriate. A brief explanation of the Deep Kalman Filter and how it interacts with the PHE is needed.

In line 224, the function $f_{\theta_z}$ is defined as a set of a vector and a matrix.  A normal distribution $\mathcal{N}$ has two parameters $\mathcal{N}(\mu, \Sigma)$. In lines 223, and 227, what does it mean $\mathcal{N}(z \mid 0,I)$? It is not clear what the mean and covariance are in this context. Is $z$ a vector? If so, what is its dimensionality? Is $I$ an identity matrix? If so, what is its dimensionality?

In lines 234-235, it is written that the "Observation of other tasks is generated similarly beside the hash-embedding [...]$. This is the first time that the word "task" appears in the paper. What is a task? The concept of a task is not defined, and it's unclear how it relates to the rest of the paper.

In Lines 245: also assume that $q_{\theta}()$ is a Gaussian distribution implemented as a recurrent neural network. What does this mean? How can a neural network output a distribution? Is it outputting the parameters of the Gaussian distribution? This needs to be clarified.

How can the covariance $\Sigma_{\lambda}$ have the same dimensionality $B \times d$ than the vector $\mu_{\lambda}$? How is the covariance $\mu_{\lambda}$ diagonal as written in Lines 243. The dimensionality mismatch between the covariance matrix and the mean vector is a significant issue. A covariance matrix should be a square matrix, not a matrix of the same shape as the mean vector. Also, the claim that the covariance is diagonal is not consistent with its dimensionality.

Why is the covariance $\Sigma_{i,\phi}$ a vector in line 247. Covariance matrices are not vectors. This is a fundamental error in notation.

I would add a reference for Kalman Filters in line 228.

In line 254, is maximizing the ELBO equivalent to maximizing the marginal likelihood? Also, there are no references for these known techniques as ELBO, structured variational inference. The paper should cite the relevant literature on ELBO and variational inference.

Section 3.4, which is supposed to be theory, only contains a simple example, using simplifying assumptions. Although the paper contains a lot of equations and it is mathematical dense, it has no formal proposition/lemma/thm. It is unclear what Section 3.4 is trying to achieve. I believe theoretical results should be summarized in a formal statement (as a theorem).

---- 

For the experimental section, there is no comparison with the baseline from previous work. Does this mean that there exists no method in the literature that can be applied in your experimental setting (even if it has low performance?), even ones that do not use unified embeddings?

Since this is an important problem, and in the real world, there are indeed applications where categorical data is used without prior knowledge of the vocabulary size (e.g., advertisement), it seems peculiar that no comparison with previous work appears in the paper. A comparison with previous work would also strengthen the paper since it would further motivate the importance of solving this problem in the context of the existing literature.

---

Usually, hash functions are chosen using a random seed. Why are the methods from prior work that use hashing tricks deterministic, as written in Lines 117-119?

### Questions
See Weaknesses for Question on Section 3.

In Section 3, I would recommend clearly stating the assumption, maybe summarizing all the random variables and functions used in the paper using a table, with the correct dimensionality.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a probabilistic hash embedding (PHE) model for handling temporal tabular data-streams (TTD) with both categorical and numerical features, addressing the challenges of unbounded growth and evolving categorical items. The PHE model adapts to new items without forgetting old ones, maintains a fixed parameter size, and efficiently supports incremental learning in both offline and online settings. Experimental results show that PHE outperforms baseline methods in classification, sequence modeling, and recommendation tasks.

### Strengths
The research ideas are clear.
The experiments are extensive.

### Weaknesses
1. The transitions between paragraphs are quite abrupt, with a lack of logical connections, making some parts difficult to understand. Could the logical structure be further refined?
2.In the “Related Work” section, is the relevance of temporal and recommendation models to the research topic truly that strong? Additionally, could the practical shortcomings of these models be discussed in more detail?
3.There are some minor writing errors. For instance, the formula in line 232 should be numbered.
4.In the “Experiment Overview” section, could you elaborate on the detailed setup of the experiments? Additionally, it is worth noting why the five curves in Figure 5 (Right) exhibit very similar trends.
5.In Table 2, could there be more comprehensive comparisons regarding memory usage?

### Questions
1. The transitions between paragraphs are quite abrupt, with a lack of logical connections, making some parts difficult to understand. Could the logical structure be further refined?
2.In the “Related Work” section, is the relevance of temporal and recommendation models to the research topic truly that strong? Additionally, could the practical shortcomings of these models be discussed in more detail?
3.There are some minor writing errors. For instance, the formula in line 232 should be numbered.
4.In the “Experiment Overview” section, could you elaborate on the detailed setup of the experiments? Additionally, it is worth noting why the five curves in Figure 5 (Right) exhibit very similar trends.
5.In Table 2, could there be more comprehensive comparisons regarding memory usage?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In the paper, the memory efficiency of data stream machine learning is addressed by proposing a hash table for open vocabulary categorical features, which is learned by Bayesian online learning.

The main idea of the paper is to replace a deterministic hash table by a probabilistic one (PHE), in which each cell is a probability distribution and is updated by calculating the posterior distribution. Properties of PHE follow from the theory of online Bayesian learning, notably in each step, the posterior distribution is the same whether learned online or at once, based on all samples so far. In my opinion, this is the key idea, however it is hidden in Appendix D starting at line 1030. Furthermore, no reference is given to the theorem (or hidden and I did not spot).

The idea of using Bayesian online learning in a probabilistic hash table is nice, useful, and up to my knowledge novel.

In practice, I am a bit uncertain about the importance of the hash table size, especially in light of the large language models. More motivation, including data and vocabulary sizes, would be necessary. Data in the experiments are definitely small in this sense.

Unfortunately, the paper is not well written, very hard to follow the presentation jumping back and forth between main paper and Appendix. While the very simple hand picked two-value example is worked out in much detail showing forgetting can occur with partial hash collision (which is not a surprise in my opinion), several important details are not worked out at all. For example, a detailed Bayesian update for the same example would be more enlightening than the deterministic analysis. Specific suggestions are
-    Moving key technical details from the appendix into the main text;
-    Adding a worked example of the Bayesian update to complement the deterministic analysis;
-    Reorganizing the content to reduce the need to jump between main text and appendix.

Most importantly, the Bayesian update step is only hinted for Deep Kalman filters. In equation (2) an independence assumption is used but its validity is not verified. In general, for Bayesian online learning, assumptions on the distribution are necessary, otherwise the posterior calculation for the update requires the knowledge of the entire past data. For the different regression applications, there is not even a sketch on how the update is calculated.  Please add the following technical description:
-    Justify the independence assumption in equation (2).
-    Specify the distributional assumptions required for the Bayesian online learning updates.
-    Provide at least a high-level sketch of how the updates are calculated for the different regression applications.

Minor question: why can we assume the latent time variable z (line 222) is Gaussian?

While the goal of the paper is to close to the upper bound of the collision-free hash and the experimentations show good results in this sense, I am not convinced whether competitive models are used for the tasks. For example, is Deep Kalman filter recommendation competitive to state-of-art recommenders? Why was it selected? Is it because the update is feasible to compute? This is not explained in the paper. Please justify your choice of Deep Kalman filters and other baseline models.

For example, some specific state-of-the-art recommender systems could be included as baselines include ADDVAE, SLIM, or even simple traditional ones as knn, also using some evaluation framework such as https://github.com/enoche/MMRec.

Minor typo: line 978 e(2) and not e(1).

### Strengths
- The idea of mitigating hash collision by Bayesian online learning is nice and up to my best knowledge new
- Works well in experiments
- Source code in supplement, expected to be fully reproducible upon acceptance

### Weaknesses
 - May technical details are missing from the paper, most notably the various versions of the Bayesian online learning step with the underlying assumptions on the distribution
- Paper is difficult to read, reader has to switch back and forth between main text and Appending. A simple example is worked out in much detail on why deterministic hash forgets in case of a partial collision (no big surprise), but there is no similar example that illustrate how the Bayesian update mitigates the effect of a collision.
- The selection of base regressors and recommender methods are not really explained, why for example deep Kalman filters?
- The data used in the experiments are small, for a better motivation some real large data sets would be necessary.

### Questions
Does the applicability of PHE depend on the base machine learning method?

How can one compute the Bayesian update of the hash embedding, what assumptions are necessary on the distributions?

Can you list some real data sets and applications where the size of the embedding really matters, especially considering the huge size of the large language models?

### Soundness
2

### Presentation
1

### Contribution
3
