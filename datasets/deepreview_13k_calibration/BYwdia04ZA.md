# Measuring similarity between embedding spaces using induced neighborhood graphs

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Deep Learning techniques have excelled at generating embedding spaces that capture semantic similarities between items. Often these representations are paired, enabling experiments with analogies (pairs within the same domain) and cross-modality (pairs across domains). These experiments are based on specific assumptions about the geometry of embedding spaces, which allow finding paired items by extrapolating the positional relationships between embedding pairs in the training dataset, allowing for tasks such as finding new analogies, and multimodal zero-shot classification. In this work, we propose a metric to evaluate the similarity between paired item representations. Our proposal is built from the structural similarity between the nearest-neighbors induced graphs of each representation, and can be configured to compare spaces based on different distance metrics and on different neighborhood sizes. We demonstrate that our proposal can be used to identify similar structures at different scales, which is hard to achieve with kernel methods such as Centered Kernel Alignment (CKA). We further illustrate our method with two case studies: an analogy task using GloVe embeddings, and zero-shot classification in the CIFAR-100 dataset using CLIP embeddings. Our results show that accuracy in both analogy and zero-shot classification tasks correlates with the embedding similarity. These findings can help explain performance differences in these tasks, and may lead to improved design of paired-embedding models in the future.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a new metric, Nearest Neighborhood Graph Similarity (NNGS), designed to evaluate the similarity between embedding spaces by examining the structural similarity of induced neighborhood graphs. The authors use Jaccard similarity to assess overlap between nearest neighbors in paired embeddings. In doing so, NNGS enables comparisons across domains or modalities (e.g., text and image). NNGS is validated on two experimental case studies using analogies and GloVE embeddings, as well as CLIP embeddings on CIFAR100.

### Strengths
Generally, the paper is structured well, which as a result makes it fairly straighforward to follow the train of throught.
Moreover, I believe that the authors did a good job providing some crucial theoretical fundamentals in support of NNGS across section 3, which offers some interesting insights on respective measure bounds, e.g. for two independent point clouds and variations thereof.

### Weaknesses
Unfortunately, I am currently strongly advocating for rejection, as the paper as several large issues alongside lack of clarity in different important parts. I have ordered these based on their importance to me.

One major problem with this work is the lack of meaningful experiments, both with respect to their setup, as well as their breadth and depth.

* Testing a metric on two small-scale case studies is simply insufficient. To understand if NNGS holds any relevant benefits over NNGS, a much larger array of tests should be conducted. What happens when the metric is applied e.g. on CLIP, but with a more out-of-distribution dataset? How do insights hold when moving to larger, higher-dimensional variants? How does it transfer to other language-based similarity tasks? And for the one application to GloVe embeddings, the authors report a single correlation value, without any additional visualization, explanation of discussion of differences.

* Moreover, the application of CLIP on just CIFAR-100 is insufficient. For one, CIFAR-100 operates in much lower resolution than the training data used for CLIP. While still applicable, insights do not necessarily transfer. At the same time, the experimental design is problematic; relying on CLIPs sensitivity to template changes can fall victim to the known bag-of-words nature in CLIP (c.f. e.g. Yuksekgonul et al. 2022, https://arxiv.org/abs/2210.01936). At the same time, the differences in correlation to CKA, particularly given that experiments were conducted on just one dataset, are insignificant.

* The authors insufficiently compare and contrast against other similarity measures (of which there are many) - both in their discussion of related works, and more importantly, their experimental case studies. Why simply focus on CKA, when SVCCA, PWCCA (Morcos et al. 2018, https://arxiv.org/pdf/1806.05759), ContraSim (Rahamim et al. 2023, https://arxiv.org/pdf/2303.16992), Brain-Score, RSA or metrics like GULP (https://arxiv.org/pdf/2210.06545) or a simple mean cosine similarity between clusters are all possible similarity measures to relate against performance changes. 

In turn, this makes it unclear why NNGS should be preferred over other distance-based similarity measures. This also holds when looking at the theoretical motivation: there is no free lunch. By avoiding the explicit reliance of point distances, NNGS in return disregards relative relations between neighbouring points in a k-Neighbourhood, which in turn raises the question on whether this is a desired property or not.

* The authors for example note that "NNGS has two additional parameters when compared to CKA: the neighborhood size k, and the distance metric used to induce the neighborhood graph. In datasets with more than one cluster, these parameters can be manipulated to find similarities at different scales and in different situations." But in CKA, one can simply adjust the utilized kernel to adapt to different situations. Moreover, isn't the dependence on different scales and situations used as the motivating factor for NNGS over CKA, as e.g. noted in L108-111? It is not entirely clear to me why NNGS should, again, be preferred?

Similarly, there are several other elements of the provided motivation that remain unclear to me:

* L328: "Although theoretically the value of σ in CKA with an RBF kernel plays the same role, it is easier to find suitable values for k than to σ. >>> But why? This is very handwavy, arbitrary reasoning. Sigma is simply a hyperparameter to tune like k.

* L329: "In special, we observe that even very small values of σ were innefective to find local changes in the point clouds." >>> But in these cases, CKA does allow for simple changes in the underlying kernel to much better account for particular point cloud structures, no?

Finally, the actual novelty is also limited: The Jaccard similarity is exactly defined as a distance over vertices' graph neighbourhoods. The singular novelty in this work is thus the application to a graph induces by some distance function; with works such as Sobal et al. 2024 (https://arxiv.org/pdf/2407.18134) having already investigated the use of distance-induced graphs for e.g. contrasive learning.

Also a smaller, nitpicky issue: The paper uses in parts weird formulation throughout, such as "datablob"; which I assume refers to clusters?

### Questions
See weaknesses. I am currently strongly advocating for rejection; but would be willing to raise my score if the authors significantly extend their experimental study, and provided convincing arguments regarding the novelty of the proposed NNGS.

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
3

### Summary
This paper proposes a novel method, namely “Nearest Neighbor Graph Similarity (NNGS)”, to evaluate the similarity between paired embedding spaces. Through case studies of the Glove and CLIP models, this paper validates the effectiveness of NNGS, showing a correlation between similarity and task-specific accuracy such as analogy calculation and cross-modal zero-shot classification. These findings can help to understand the reasons behind performance differences in these tasks and provide directions for improving the design of paired embedding models.

### Strengths
1.	Introduces a novel metric, NNGS, for evaluating similarity between paired embedding spaces.
2.	NNGS excels in identifying similar structures across different scales, which is challenging for traditional kernel methods like CKA.

### Weaknesses
1.	NNGS is based on Jaccard similarity, therefore it is non-differentiable and cannot be used for end-to-end learning of structurally similar representations, limiting its use to measuring the similarity between paired embeddings of items. This significantly restricts its applicability in scenarios where the goal is to optimize the embeddings themselves for structural similarity. The lack of differentiability prevents the integration of NNGS into gradient-based learning frameworks, which are the cornerstone of modern deep learning.
2.	This paper uses the K-nearest neighbor algorithm, which has high computational complexity when used on large-scale points, requiring high hardware computing resources. The computational cost of finding the K-nearest neighbors for each point scales poorly with the size of the dataset, making it impractical for very large embedding spaces. Furthermore, the memory requirements to store the distance matrix can also become a bottleneck.
3.	NNGS is constrained by KNN because KNN is sensitive to outliers in the data, which may affect its performance. Outliers can disproportionately influence the local neighborhood structure identified by KNN, leading to inaccurate similarity measures. This sensitivity is a significant concern, particularly in real-world datasets where outliers are common.
4.	the choice of k is crucial, and in high-dimensional spaces, the performance of KNN may also deteriorate. The changing the value of k implies in a modification of the locality of the similarity measure. Although NNGS demonstrates good performance, there is a lack of detailed discussion on how to select the value of k and other parameters. The paper does not provide a clear methodology for selecting the optimal k, and the impact of different k values on the final NNGS score is not thoroughly explored, especially in the context of high-dimensional embeddings where the notion of proximity becomes less intuitive.
5.	Figure 1 illustrates the relationship between NNGS and the number of selected k-nearest neighbors, indicating that NNGS increases as k increases; this contradicts the comparison with the last two columns of Table 1.
6.	In Line 290, the reference to Table 1 is incorrectly labels as Table 3.3.

### Questions
1.	In Figure 1, the relationship expressed on the same curve represents the variation of NNGS with the number of selected k nearest neighbors, indicating that as the number of k nearest neighbors increases, NNGS also increases. This contradicts the data in the last two columns of the first row in Table 1. Could you please explain this discrepancy?
 
2.	From Equation 7, it can be seen that c = k/(n - 1),  where k is controlled by c. So, how to choose c?
 
3.	In section 3.1, how is the existence of a one-to-one correspondence proven in real-world scenarios? Can the authors provide relevant theoretical or empirical support for this assumption?

### Soundness
3

### Presentation
3

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
This paper proposes a new metric, named NNGS, to evaluate the similarity between paired item representations. NNGS is based on the structural similarity between the nearest-neighbors of induced graphs. Two case studies in analogy and zero-shot classification tasks demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper introduces a new metric that assesses the similarity between paired item representations by examining the structural similarity within the neighborhoods of induced graphs.
2. The effectiveness of the proposed method is demonstrated in two scenarios: analogy tasks and zero-shot classification tasks.

### Weaknesses
1. The methods discussed in the related work section are insufficient. For instance, only GloVe and CLIP are mentioned for semantic word embeddings and cross-modal embeddings, respectively. A broader range of relevant methods should be included, such as BLIP and Flamingo, to provide a more comprehensive review. Furthermore, the discussion lacks depth regarding the specific mechanisms of these models and how they relate to the proposed NNGS metric. For example, the related work should discuss how the embedding spaces of different models might influence the structural similarity of nearest-neighbor graphs.
2. The quality of the figures does not meet the standards expected at top conferences like ICLR. For example, Figures 5 and 6 contain overlapping text, which significantly impacts readability and clarity. The overlapping text makes it difficult to discern the data points and their relationships, hindering the interpretation of the results. Additionally, the figures lack detailed axis labels and legends, which are crucial for understanding the presented data.
3. The comparison is limited to CKA, a method proposed in 2019. To strengthen the evaluation, more recent methods should be included for comparison. The choice of CKA as the sole baseline limits the scope of the evaluation. It is essential to compare the proposed method against more recent and state-of-the-art techniques to demonstrate its superiority or at least its competitive performance. The evaluation should also consider methods that are specifically designed for comparing graph structures or embedding spaces, which would be more relevant to the proposed NNGS metric.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
2
