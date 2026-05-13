# From Logits to Hierarchies: Hierarchical Clustering made Simple

- Decision: Reject
- Scores: 3, 5, 3, 3, 5

## Abstract
The structure of many real-world datasets is intrinsically hierarchical, making the modeling of such hierarchies a critical objective in both unsupervised and supervised machine learning. Recently, novel approaches for hierarchical clustering with deep architectures have been proposed. In this work, we take a critical perspective on this line of research and demonstrate that many approaches exhibit major limitations when applied to realistic datasets, partly due to their high computational complexity. In particular, we show that a lightweight procedure implemented on top of pre-trained non-hierarchical clustering models outperforms models designed specifically for hierarchical clustering. Our proposed approach is computationally efficient and applicable to any pre-trained clustering model that outputs logits, without requiring any fine-tuning. To highlight the generality of our findings, we illustrate how our method can also be applied in a supervised setup, recovering meaningful hierarchies from a pre-trained ImageNet classifier.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a method to map from the logit space output from a pretrained clustering network to convert its output into a hierarchical structure. They demonstrate that by building on existing foundation models and non-hierarchical clustering methods, this simple method can outperform bespoke deep hierarchical clustering methods.

### Strengths
It is valuable to have strong baselines for complex methods, even when those methods are simple.

The paper is generally well written.

### Weaknesses
1. Experiments are too restricted. In the introduction, the authors state that much real-world data is hierarchical, such as taxonomic data. However, they barely run experiments on datasets that possess hierarchical labels. CIFAR-10 does not have hierarchical labels, and so it is unclear how the authors evaluated it for dendritic purity, etc. As far as I am aware, Food101 doesn't either. CIFAR-100 only has one intermediate level in its hierarchy. They refer to the datasets used as being challenging, but I don't think it is appropriate to describe CIFAR-10 as such when we have models achieving >99% accuracy on it. They refer to CIFAR-100 and Food101 as having a large number of classes, but given that models are routinely trained on IN-1k (1,000 classes), IN-21k (21,000 classes), iNaturalist (10,000 classes), and 100 classes is quite small in comparison to these datasets. For work that is benchmarking a relatively simple method, I think it is important that the authors benchmark on more complex and more real-world datasets such as iNaturalist or BIOSCAN-5M from the taxonomic labelling perspective, or even non-image modalities for [more comprehensive analysis]. For a method that trains in 5 minutes on IN-1k, I do not think the authors can justify not exploring larger datasets and demonstrating the methodology works well at scale, both in terms of its performance and execution time. Even worse though, quantitative IN-1k results are not shown (i.e. in Table 1).

2. Baselines are inadequate. What is being proposed in the paper is a method for mapping from logits to a hierarchy, harnessing a couple of methods (TEMI and TURTLE) which can map from the embeddings of pretrained encoder (CLIP and DINOv2) to logits for clusters.
(2a.) The authors introduce the flexibility in their algorithm to consider multiple aggregation operations, but only consider summation ($Λ=\Sigma$). This leaves the question of what is the best aggregation operation unclear.
(2b.) Moreover, the paper leaves open the question of whether this is a *good* methodology of mapping from the TEMI or TURTLE outputs to a hierarchy. They present one method for this mapping, but there are no comparators given for it. For example, what if you used agglomerative clustering to cluster the TEMI or TURTLE logits? Does the L2H method beat this obvious baseline?
(2c.) The L2H-TEMI/TURTLE methods presented have the benefit of building on pretrained foundation models, whereas the competing methods are trained from scratch. Hence it would perhaps be more appropriate to compare against alternative methods for producing clusters from the embeddings of pretrained models, for instance [Lowe et. al. (2024)](https://arxiv.org/abs/2406.02465) investigate methodologies for doing this. [That paper concludes that the best way to cluster embeddings from a pretrained model is UMAP with >5 dims for dimensionality reduction, followed by Agglomerative clustering. So although they don't analyze hierarchical embeddings, the methodology they recommend is actually hierarchical and should serve as a useful baseline for this paper.]

3. Algorithm 1 (which is in a sense the main output of the work) is not adequately well written.
    - The same variable, $s$, is used for both the step number and the score.
    - Some variables are defined in the text of the paper, and used in the algorithm without definitions in the algorithm itself. The algorithm should stand alone without needing to read the rest of the paper to understand it. $f_θ$ is defined and never used, whilst $g_θ$, $g^m_θ$, $K$, $Λ$ are used and never defined.
    - argmin yields a single index, not a set, so it is unclear why the authors use an $\in$ symbol in $G^*\in \text{argmin}_{G\in \mathrm{G}} s(G)$, etc. Perhaps this is to cover the edge case of ties..? But this unnecessarily adds confusion to the notation.
    - $K$ is not updated in the outer loop, so the inner loop at L173 refers to cluster indices that no longer correspond to unmerged clusters.

**Typos and minor points**
- L311 Agglomerative clustering is abbreviated as Agg, but as far as I can see, this abbreviation is never used.
- The methodology for several things is only given in the appendix (e.g. agglomerative clustering), but nowhere in the main text does it let the reader know this or where in the appendix one might find these details (which a reader otherwise may well assume are omitted from the text entirely).
- There are a couple of places where a word is repeated (e.g. L271 "Appendix Appendix")
- L730 The text says it is giving the aggregation function, $Λ$, but the equation is the score function
- L734 "possiblle"
- L341 British English "modelled" contrasts with the American English used in the rest of the text
- Some references are cased incorrectly, e.g. key reference "Deepect" -> DeepECT
- Some references don't include publication details, e.g. Bengio (2014)
- Some references cite arXiv versions of papers where peer-reviewed versions are available (which should generally be preferred for citations) e.g. Karthik (2021b)
- Most references don't have links to the paper being cited, which should ideally be present for the convenience of the reader in the modern, digital era. DOIs can be made clickable simply by importing the doi package in main.tex (and don't need a URL field also present in the bibtex)
- One reference has mojibake: Nguyen (2024) "Identification of distinct subgroups of sj&#xf6;gren’s disease"

### Questions
Q1. Why is IN-1k not included in Table 1?

Q2. What is the input to the agglomerative clustering baseline? Is it the raw pixel values of the images?

Q3. Is the performance of L2H-TEMI on flat clustering metrics identical to the performance of TEMI? Similarly for (L2H-)TURTLE.

Q4. Did you really train the auto-encoder for DeepECT from scratch on CIFAR-10/100 in 25 minutes on a single CPU core...? This seems rather unlikely, but it does appear to be what the paper claims.

Q5. In Fig 2, why is there a space between woman and otter but not between palm tree and sunflower? The two pairs are equally far from each other.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a new algorithm for generating hierarchies based on logits of pre-trained models. The new method outperforms other deep clustering techniques both in terms of performance and runtime.

### Strengths
The methods elegantly bypass the standard O(N^2) complexity required for standard agglomerative clustering

The model outperforms the other baselines both in terms of runtime and clustering performance.

The paper is well written and easy to follow.

### Weaknesses
I'm concerned that the suggested models received a better starting point. If I understand correctly, the pre-trained models know better how to cluster to the starting 10/100/101 clusters. It would benefit this work if there would be an ablation study that demonstrated the good results caused by the suggested algorithm and not by the pre-trained models.

The suggested algorithm is generic, how does it perform on non-vision-based clustering tasks?
How does it perform compared to other (more) deep hierarchical models?
I hope to see a broader comparison, with more than two models for deep custring and on various clustering tasks aside from vision.

The runtime comparison is not 100% fair, in my opinion, since L2H utilizes pre-trained models. 
The pre-trained models already know how to cluster the leafs, while other models need to learn it.

### Questions
Do other methods assume a starting division to K clusters?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors provide a simple and fast hierarchical clustering method, which works well in the case of many-class problems. It works on the pretrained representation in the logits space. The method is a version of aglomerative clustering which can be based on a chosen standard clustering backbone. The paper is well written. The idea is simple and can be easily applied even to large datasets.

### Strengths
The paper is clearly written, the experiments are properly conducted and shows that the method outperforms other hierarchical approaches. The idea is nice as it uses as a backbone a non-hierarchial clustering method.

### Weaknesses
The novelty of the approach is rather limited, the method is in fact a shallow clustering approach applied in the representation space. Consequently, since in training the representation the knowledge of classes was used, it is hard to say how the method would deal in the case when the model did not know the proper classes beforehand. In particular a test of themodel on a few common unsupervised representations on ImageNet is necessary (for example given by SimClr or MaskedAutoEncoders).

### Questions
It is necessary to validate the approach on representation space constructed by unsupervised models.

### Soundness
3

### Presentation
3

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
The authors propose a new hierarchical clustering algorithm that leverages a pre-trained flat clustering models.
The key observation is that the logits of those model encode class similarity.

### Strengths
- The paper is well-written and easy to read.
- The authors compare their method with three related methods. 
- The authors provide the pseudo code of their algorithm.

### Weaknesses
The contribution is rather limited and incremental. It is well known that the logits encode class similarity, and have been frequently used to reconstruct classification hierarchy. Examples for previous work with similar observation:
- https://arxiv.org/abs/2007.06068
- https://dl.acm.org/doi/abs/10.1145/3491102.3501823

The evaluation is based on two pre-trained image clustering models, TURTLE and TEMI.
This limits the generalizability of the results, as these are not the same backbones used for the other baselines.

Minor presentation remarks:
- Provide full names of the acronyms NMI and ARI
- datapoints => data points

### Questions
Did you consider using the logits of standard image classification models (e.g. a ResNet trained to classify ImageNet)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a simple method for hierarchical clustering based on pre-trained non-hierarchical models. Specifically, the method performs on top of (non-hierarchical) pre-trained models, which uses the logits output by the pre-trained models to iteratively compute clusters in a fine-to-coarse manner. The authors verify the effectiveness of the method on four datasets, including CIFAR-10, CIFAR-100, Food-101 and ImageNet1K.

### Strengths
The proposed method is simple.
The proposed method looks effective from the experimental results.

### Weaknesses
 + The paper presents some challenges in clarity, particularly in the methods section, which may hinder reviewers from fully understanding how the proposed method operates. For example,
  - The terms "clusters" and "groups" seem to be used somewhat interchangeably, which can lead to confusion regarding their meanings. It would be helpful for the authors to clarify the distinctions between these terms in the context of the paper. Specifically, it's unclear if 'clusters' refer to the initial output of the pre-trained model or to intermediate groupings during the hierarchical process, and how these relate to the final 'groups'.
  - it should number the equations and reference specific formulas in the algorithm table to illustrate the execution process of the proposed method more effectively. Currently, the algorithm description lacks precise references to the mathematical operations, making it difficult to follow the exact steps of the method.

+ The authors assert that the proposed method does not require fine-tuning of the pre-trained model. However, it would be helpful to clarify how the logits are generated for different datasets. For example, in a network trained on ImageNet1K, the output is 1000-dimensional. If we are now clustering on CIFAR-10, does this imply that its logits are also 1000-dimensional? In other words, does this mean that the number of clusters at the finest-level hierarchy is 1,000? This point is crucial for understanding the method's applicability across different datasets and the relationship between the pre-trained model's output space and the resulting hierarchy.

+ In the context of hierarchical clustering, determining the number of hierarchies is crucial. I would appreciate further explanation on how this is accomplished within the proposed method. It's not clear how the algorithm decides when to stop merging clusters and how the depth of the hierarchy is determined. This needs to be explicitly addressed in the paper.

+ Regarding line 190, where $s(G)$ represents the sum of the probabilities of samples belonging to $G$, it seems that if $G$ has more samples, its $s(G)$ value would naturally be larger. This raises the question of whether the relatedness between clusters is sensitive to the number of samples, which may not align with our intuitive understanding. The paper should provide a more detailed analysis of the impact of cluster size on the similarity metric and how this is addressed in the method.

### Questions
Please refer to the weakness section.

### Soundness
2

### Presentation
1

### Contribution
2
