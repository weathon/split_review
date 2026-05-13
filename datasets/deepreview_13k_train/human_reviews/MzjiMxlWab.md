# Learning Multi-Faceted Prototypical User Interests

- Decision: Accept
- Scores: 6, 8, 5

## Abstract
We seek to uncover the latent interest units from behavioral data to better learn user preferences under the VAE framework. Existing practices tend to ignore the multiple facets of item characteristics, which may not capture it at appropriate granularity. Moreover, current studies equate the granularity of item space to that of user interests, which we postulate is not ideal as user interests would likely map to a small subset of item space. In addition, the compositionality of user interests has received inadequate attention, preventing the modeling of interactions between explanatory factors driving a user's decision.
To resolve this, we propose to align user interests with multi-faceted item characteristics. First, we involve prototype-based representation learning to discover item characteristics along multiple facets. Second, we compose user interests from uncovered item characteristics via binding mechanism, separating the granularity of user preferences from that of item space. Third, we design a dedicated bi-directional binding block, aiding the derivation of compositional user interests.
On real-world datasets, the experimental results demonstrate the strong performance of our proposed method compared to a series of baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work propose to learn multi-faceted prototypical user interests based on VAE framework. The proposed method is technically sound, although it can be viewed as a natural extension based on MacridVAE, which limits the technical contribution somehow. The paper is well written and easy to follow, related work is well discussed and the extensive experiments and ablation studies verify the model performance.

### Strengths
1. This paper is well motivated to solve the multi-facet user interest modeling problem based on VAE framework. The proposed method is well motivated and presented.
2. This paper is well written and easy to follow, especially the related work and limitation discussion in preliminaries.
3. Extensive experiments are conducted, with state-of-the-art methods as baselines. The results demonstrate the improvement.

### Weaknesses
1. In real world recommender systems, different product categories will have different facets, in total, it can reach up to thousands of facets in the recommendation space, especially when we want to do whole website recommendation. It's unclear how this method can handle and scale to large scale product facets. Specifically, the method's reliance on a fixed number of facets per category may become a bottleneck when dealing with the long-tail of less popular categories, which may have unique and numerous facets. The paper does not address how the model would adapt to these varying facet granularities and the computational overhead associated with maintaining such a large number of facets.
2. This work can be viewed as an incremental upon MacridVAE, which limits the technical novelty contribution. While the paper introduces multi-faceted modeling, the core architecture and training procedure appear to be heavily influenced by MacridVAE, raising concerns about the extent of the innovation. The paper needs to more clearly articulate the specific technical differences and demonstrate how these differences lead to substantial improvements beyond what could be achieved with a straightforward extension of MacridVAE.
3. The performance on large scale (millions of users and items) datasets is unclear. The experiments are conducted on relatively small datasets, and it remains to be seen whether the proposed method can maintain its performance when scaled to datasets with millions of users and items. The paper lacks a discussion of the potential challenges in scaling the model, such as increased computational costs and memory requirements, and how these challenges might be addressed.
4. How to leverage product knowledge/other knowledge source to automatically choose #facets should be discussed to make it applicable in real world applications. The paper does not provide a clear methodology for determining the optimal number of facets for each category. This is a critical issue for real-world deployment, where manual selection of the number of facets is impractical. The paper should explore methods for automatically determining the number of facets, potentially by leveraging product knowledge or other external knowledge sources.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presented a new approach to uncover latent user interests for recommender system. Specifically, it proposed FACETVAE which tries to align user interests with multi-facted item characteristics and prototype-based user representation. It tries to separate granularity of user preferences from that of item space. WIth a dedicated bi-directional binding block, it demonstrates better recommendation performance compared to other baseline VAE approaches.

### Strengths
1. The paper is well organized and written.
2. The paper is well motivated.
3. The paper proposed a mathematically solid approach and demonstrated its clear strength over baselines.

### Weaknesses
The proposed approach has worse complexity than baseline MacridVAE. For real-world recommendation problems with huge spaces of users and items, the approach seems less applicable. Specifically, the multi-faceted clustering step, while offering a richer representation, introduces additional computational overhead that scales linearly with the number of items, which could become a bottleneck in large-scale scenarios. Furthermore, the bi-directional binding block, while effective, also adds to the overall computational cost compared to MacridVAE's simpler architecture. The paper does not provide a detailed analysis of the time complexity of each step, making it difficult to assess the practical scalability of the proposed method.

### Questions
1. For Table 1, what is the number of clusters and the number of parameters for the baseline MacridVAE? 

2. Is it possible to report the performance with respect to the number of parameters, and computation time across the baselines and the proposed approach? That seems to be able to give readers a better understanding of accuracy and efficiency.

3. In Table 2, why is the number of prototypes fixed to 12 instead of other numbers? Can the best F and J have different trends with different number of prototypes?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes FACETVAE to align user interests with multi-faceted item characteristics. The paper puts forward low-level and high-level user interests and introduces a bi-directional binding block to learn compositional user interests. Rich experimental results demonstrate the  good performance of FACETVAE.

### Strengths
- This paper is well motivated and the idea of learning multi-faceted prototypes is interesting.

- The paper conducts comprehensive experiments that encompass various aspects such as prediction performance, visualizations, parameter studies, and case studies.

- The authors have made their code and dataset publicly available.

### Weaknesses
1. The proposed method is somehow incremental and is a combination of existing techniques. This work is based on an existing work that learns prototypical representation of items and users that seperate items into different groups. This work further incorporates disentangled representation learning to explore item representations of various aspects of items, which has been also considered in previous works. The main difference appears to be  the combination of these various aspects.
2. Figure 2 is confusing because it takes explicit user-item interaction in an rating form. However, the paper is designed based on implicit user-item interaction. This misleads the reader on the output form and training strategy of the proposed method.
3. Would it be better to include item attribute information in prototype learning as auxiliary information? Without low-level attributes as input, the so-called low-level user interest about a facet might also be a composite feature of some facets. This could result in the difference in meaning between the two levels of interests not being clear.
4.  More qualitative analysis and case studies about on how learned latent representations corresponds to different aspects of characteristics may help to better evaluate the interpretability of the model. For example, more details on how the "latent interest" corresponds to explicit interests 1, 2, and 3 in Table 4 would be appreciated.

### Questions
Please refer to the weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
