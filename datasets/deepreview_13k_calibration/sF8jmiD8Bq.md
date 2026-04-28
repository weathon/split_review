# Domain2Vec: Vectorizing Datasets to Find the Optimal Data Mixture without Training

- Decision: Reject
- Avg Score: 6.25
- Scores: 3, 8, 8, 6

## Abstract
The mixture ratio of data from different source domains significantly affects the performance of language models (LM) pretraining. In this paper, we introduce~\textsc{Domain2Vec}, a novel approach that decomposes any dataset into a linear combination of several ``Meta-Domains'', a new concept designed to capture key underlying features of datasets. \textsc{Domain2Vec} maintains a vocabulary of Meta-Domains and uses a Meta-Domain Classifier to decompose any given dataset into a domain vector that corresponds to a distribution over this vocabulary. These domain vectors enable the identification of optimal data mixture ratio for LM pretraining in a training-free manner under the \textit{\textbf{D}istribution \textbf{A}lignment \textbf{A}ssumption} (DA$^{2}$). Moreover, previous work could use \textsc{Domain2vec} to model the relationship between domain vectors and LM performance, greatly enhancing the scalability of previous methods without retraining as new datasets are introduced. Extensive experiments demonstrate that \textsc{Domain2Vec} finds data mixture ratios that enhance downstream task performance with minimal computational overhead. Specifically, \textsc{Domain2Vec} achieves the same validation loss on Pile-CC using only $51.5\%$ of the compute required when training on the original mixture of The Pile Dataset. Under equivalent compute budget, \textsc{Domain2Vec} improves downstream performance by an average of $2.72\%$. \textsc{Domain2Vec} serves as a strong and efficient baseline for data mixture optimization in LM pretraining, offering insights into improving data efficiency in large-scale models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a way to featurize datasets by computing their similarity to a set of "meta-domains", which are essentially the result of a k-means clustering of text embeddings. The authors then show how to use their featurizations / domain vectors to optimize dataset compositions, i.e., what weights to assign to the components of a combined dataset (such as arXiv, Wikipedia, etc.).

### Strengths
- The paper studies an important problem
- The proposed method is interesting and computationally efficient
- The paper is clearly written

### Weaknesses
My main reservation is that the proposed method offers little to no gains empirically. In particular, the authors conducted experiments where they trained language models on multiple different training sets and then measured the performance of the resulting models on a range of downstream tasks. I think this is a good experimental setup. Unfortunately, the results (Table 3) show that the proposed method offers little to no gains. In particular, the best Domain2Vec variant is worse than RegMix (0.483 vs 0.489) and worse than only training on Pile-CC alone (0.483 vs 0.487). The proposed method Domain2Vec is computationally cheaper than RegMix (9.7e16 flops vs 3.5e18 flops). But it is not clear that this difference is relevant because both flops counts are smaller than the cost of training the language model (6 N D gives 1.2e20 flops). Negative results do not necessarily mean that a submission must be rejected. But the paper should frame the results appropriately as negative and discuss the comparison to the aforementioned baselines more clearly.

In addition, the paper does not compare to state-of-the-art pre-training datasets such as RefinedWeb (https://arxiv.org/abs/2306.01116), FineWeb (https://arxiv.org/abs/2406.17557), and DCLM (https://arxiv.org/abs/2406.11794).

### Questions
- Line 65: small type (",,")
- Line 99: small typo ("to for vectorizing")

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a method for finding the mixing ratio of domains within a dataset. The method defines a concept of meta-domain that is represented as a vector that is a meta feature describing a domain. Given a dataset with some predefined domains, the method builds domain representations as a linear mixture of meta-domain vectors for each domain, then finds mixing ratios of domains as a function of domain vectors. The goal is to be more computationally efficient and scalable compared with prior works such as DoReMi. The paper relies on the Distribution Alignment Assumption (DA^2) that validation loss is minimized if the domain vector of training and validation sets align.

Section 2 introduces the Domain2Vec method. The method can be decomposed into the following steps:
- Construct vocabulary of meta-domains. A meta-domain, $D^*_j$, is a vector in the text embedding space. A vocabulary of 260 meta-domains is constructed from the centroids of KMeans in the embedding space of 5.2TBs of English, Chinese, and Code data.
- Create meta-domain classifiers. The method trains a text classifier that, given an input text, predicts the probability of it belonging to each meta-dataset. The classifier is a Qwen2-1.5B-base with a learnable head that is trained on 3k text samples from each meta-domain cluster.
- Define a domain vector and dataset vector. A domain vector, $v_i$, is an average of the probability vectors for text samples from a domain. A dataset is represented with a matrix of domain vectors, $V_{train}$.
- Compute the optimal mixing ratio $\bf{r}$ based on Eq. 5. That is, assuming the optimal mixing ratio is the one that maximizes the similarity between train and validation sets, and given the dataset matrix of the training set and domain vector of the validation set, the method finds the mixing ratio that maximizes the similarity between a mixed training set and the validation set.

---After rebuttal
Thank you for improving Eq 1. I recommend also fixing the minor issue of whitespace after thousand separator, e.g., in 3,000 and 1,000 on page 4. Maybe use {\small,}.

### Strengths
- The proposed method is ~3x more efficient than prior work, DoReMi.
- The method can efficiently adapt and scale as the number of domains within a dataset increases over time. In contrast, prior works would need to recompute the mixing ratios from scratch.

### Weaknesses
 **Clarity**
- Line 18-19: Please consider defining or providing an intuition for Distribution Alignment Assumption in the abstract. Otherwise, the abstract is unclear.
- The notation is not clearly defined, for example, the dimensionalities, what is a vector and what is a scalar, can only be guessed from the equations rather than being clearly defined. Specifically, in Equation 1, the dimensionality of $D_i^*$ is not explicitly stated, and it is unclear if $D_i^*$ represents a scalar, vector, or matrix. This lack of clarity makes it difficult to fully understand the mathematical formulation.
- Various concepts need to be clearly defined. For example, The meta-domain is not clearly defined and lines 118-119 are vague. Please consider clearly defining what is a vocabulary, features, and semantic features. Is a feature a vector? Is it an abstract concept? Is vocabulary a set of features? What is a semantic feature?
- On lines 56-57, the paper notes a downside of prior works as relying on a well-trained reference model which would imply the proposed method does not rely on such a model. However, the meta-domains rely on such a model as described in lines 134-147, specifically, `bge-small-en-v1.5` and `bge-small-zt-v1.5`. The meta-domain classifier also relies on a pretrained model, specifically, Qwen2-1.5B-base. Please consider clarifying the claim.

**Results**
- Table 3: The improvement in validation loss does not translate to any improvement in downstream performance. Specifically, the proposed method does not seem to be better than “Pile-CC only” that is a baseline with zero additional cost. It is unclear if the validation loss improvement is statistically significant and if the downstream performance is measured on a held-out test set.
- Figure 5: Please consider adding more baselines such as DoReMi, a simple 50-50 mix of Pile and C4, and a baseline that deduplicates this simple mix. The current figure only compares against the original data mixture, which is not a strong baseline.
 
**Minor**
- Line 80: missing period after “distinct features”.
- Please consider making a clear distinction between domains, $D_i$, and a training dataset, $D_{\text{train}}$. Right now the paper refers to both as datasets but defines a domain vector as a representation of $D_i$. So it makes more sense to also refer to it as a domain. Also the matrix $V_{\text{train}}$ can then be referred to as the dataset representation matrix or if flattened, a dataset vector. That way, the hierarchy of concepts, meta-domain, domain, and dataset, is more clearly separated.
- Line 162: belong -> belongs.
- There is a redundant space in all numbers with a thousand separate, right after the comma. Example: line 163, 3, 000. Please consider fixing this.
- Figure 2: the font size is too small, please consider reducing the columns/rows to the most important ones.
- Line 220: paer -> paper.
- Section 3.3 abuses the notation of $\mathcal{L}_\theta$ as it was previously defined as a function of $\bf{r}$ but now is a function of first $p, D_i^*$ and then just $\bf{p}$. Also, domain vector was previously denoted by $\bf{v}$ whereas now it is denoted by $\bf{p}$.
- Line 235: addictive -> additive.
- Line 267: what does “relative loss sizes” mean?

### Questions
- Figure 2: Please clarify how one would infer the claim on lines 172-173 from this figure that is “our classifier could reasonably distinguish some base features from different datasets.”.
- My understanding of Section 3.1 is that the proposed method relies on a predefined split of the dataset into domains. Is that correct? At the same time, the abstract says: “Domain2Vec … uses a Meta-Domain Classifier to decompose any given dataset into a domain vector that corresponds to a distribution over this vocabulary.”. This sentence could imply the method automatically identifies the domains. Please clarify the assumptions and requirements in the paper and particularly this sentence in the abstract.
- The notation of the loss in section 3.1 does not seem correct. Shouldn’t there be an additional inner argmin over $\theta$ given the mixing ratio $\bf{r}$? In other words, the model parameterized by $\theta$ will be different as one varies $\bf{r}$ but the Eq 4 would imply that it is independent.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces DOMAIN2VEC, a novel method for optimizing the data mixture ratio in LM pretraining by leveraging the concept of "Meta-Domains". DOMAIN2VEC decomposes datasets into a linear combination of these Meta-Domains, capturing essential features and maintaining a vocabulary for effective representation. By using a Meta-Domain Classifier, it generates domain vectors that facilitate the identification of optimal data mixtures without requiring retraining, based on the Distribution Alignment Assumption.

### Strengths
1. The authors decompose the dataset into domain vectors, representing attributes of datasets to balance its contributions, which introduces a training-free approach by for language models pretraining to find the optimal data mixture.

2. Experimental results indicate that DOMAIN2VEC can achieve better text generation capabilities and downstream task performance with lower computational costs.

3. This paper is well-written and provides detailed explanations from the theorical and practical aspacts.

### Weaknesses
1. The English requires further improvement and contains several minor errors. For example, line 80 is missing a period, and line 66 has an extra comma.

2. The authors claimed that "to the best of our knowledge, we are the first to propose DOMAIN2VEC, a novel concept for capturing the underlying features of datasets." There are works with similar ideas, particularly in the field of meta-learning, although they do not capsulate their approaches into the concept in the same way as this paper (e.g., `[1]`, `[2]`). The authors should discuss the relationship and differences between their work and these studies. Thus, I think it would be best to remove the statement of "the first".

Refs:

`[1]` Cross-Table Pretraining Towards a Universal Function Space for Heterogeneous Tabular Data.

`[2]` Dataset2Vec: Learning Dataset Meta-Features.

3. I have some doubts about the assumption. The authors state: "we introduce the Distribution Alignment Assumption (DA2), stating that lower validation loss can be achieved when the domain vector of training datasets aligns with the domain vector of the validation datasets." What if the domain vector of the training datasets is a subset of the domain vector of the validation datasets, or vice versa?

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Domain2Vec which decomposes data sets into meta-domain clusters from which data mixture ratios can be easily computed. The paper then uses their proposed strategy, DA2, to select better data mixtures than DoReMi.

### Strengths
The methodology is intuitive and easy to follow. The results demonstrate that the proposed method is effective.

### Weaknesses
The constructed meta-domains are heavily biased towards the initial data sources. This work collates 260 meta-domains over 100 sources containing English, Chinese, and Code. A practitioner in a distinctly different domain (e.g., German) may not be able to use the constructed domain2vec, and would have to first create their own domain2vec setup. This poses a type of chicken-and-egg problem on the usefulness of domain2vec. Furthermore, the reliance on k-means clustering for meta-domain discovery, while computationally efficient, may lead to suboptimal groupings that do not fully capture the semantic nuances of the data. The choice of k is also critical and may require extensive experimentation to determine the best value for a given dataset. The paper does not discuss the sensitivity of the results to different k values, which is a significant concern. The method also assumes that each data source can be represented as a mixture of these meta-domains, which may not always be true, especially if the source contains novel content not well represented in the initial meta-domain vocabulary.

### Questions
* How do we construct the vocabulary of meta-domains given a set of sources?
* How do we choose N, i.e., the number of points needed to get a confident probability vector? 
* When training the meta-domain classifier, is an arbitrary text belonging to a single meta-domain or can the arbitrary text also belong to multiple meta-domains? Is the meta-domain classifier a multi-class or multi-label problem? How do you handle precision/recall over long-tail meta-domains?
* Rather than fitting a meta-domain classifier, a simple baseline would be to leverage learned feature embeddings to automatically cluster the data into a set of meta-domains. How well would this perform versus the meta-domain vocabulary and the classifier?
* Ultimately, DA2 is trying to match two categorical probability vectors. Why use a Huber loss rather than, e.g., distributional measures (divergence, Wasserstein distance, etc.)?

### Soundness
3

### Presentation
2

### Contribution
2
