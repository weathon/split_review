# Error Slice Discovery via Manifold Compactness

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
Despite the great performance of deep learning models in many areas, they still make mistakes and underperform on certain subsets of data, i.e. error slices. Given a trained model, it is important to identify its semantically coherent error slices that are easy to interpret, which is referred to as the error slice discovery problem. However, there is no proper metric of slice coherence without relying on extra information like predefined slice labels. The current evaluation of slice coherence requires access to predefined slices formulated by metadata like attributes or subclasses. Its validity heavily relies on the quality and abundance of metadata, where some possible patterns could be ignored. Besides, current algorithms cannot directly incorporate the constraint of coherence into their optimization objective due to the absence of an explicit coherence metric, which could potentially hinder their effectiveness. In this paper, we propose manifold compactness, a coherence metric without reliance on extra information by incorporating the data geometry property into its design, and experiments on typical datasets empirically validate the rationality of the metric. Then we develop Manifold Compactness based error Slice Discovery (MCSD), a novel algorithm that directly treats risk and coherence as the optimization objective, and is flexible to be applied to models of various tasks. Extensive experiments on the current benchmark and case studies on other typical datasets demonstrate the effectiveness of our algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies ERROR SLICE DISCOVERY issue. In the paper, the authors mainly proposed the concept of manifold compactness and a coherence metric. The proposed optimization objective can be applied to models of various tasks. The authors also conduct many experiments to demonstrate the effectiveness of the method.

### Strengths
The authors mainly proposed the concept of manifold compactness and a coherence metric.

### Weaknesses
The paper is difficult to understand and follow as the source code is not provided.

The dimensions of all variables are not provided clearly, making the paper difficult to understand.

What’s the physical meaning of the second term in (2)? What’s the optimization solution for (2)?

There are not enough comparison methods.

What are the main advantages of the proposed method compared with the existing works?

### Questions
1. The dimensions of all variables are not provided clearly, making the paper difficult to understand.
2. What’s the physical meaning of the second term in (2)? What’s the optimization solution for (2)?
3. There are not enough comparison methods. 
4. What are the main advantages of the proposed method compared with the existing works?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper focuses on error slice discovery, where error slices refer to specific data subsets on which the model underperforms. It first proposes a new evaluation metric, manifold compactness, which does not rely on external information such as predefined slices or metadata attributes. Furthermore, the paper leverages manifold compactness to design a new error slice discovery algorithm, which can be flexibly applied across various task models.

### Strengths
1. This is a relatively new and interesting field that merits further exploration.
2. The organization and writing of this paper are reader-friendly.
3. Extensive case studies support the authors' views, accompanied by new metrics and algorithms.

### Weaknesses
1. Although extensive case studies support the authors' viewpoints, the lack of theoretical analysis is regrettable.
2. There is no analysis of time and space complexity. For a dataset of size $n$, constructing a graph requires at least $O(n^2) $ and solving Equation 2 takes $O(n^3)$. In fact, as seen in Table 8, efficiency is indeed a drawback. The authors might consider explaining why this efficiency loss is worthwhile.
3. The paper suggests that Euclidean distance is inferior to manifold, but this may be misleading. In fact, constructing the k-nearest neighbors graph still depends on Euclidean distance. Additionally, because distance variance lacks bounds, it is more sensitive to samples, especially if the sample features are not normalized. Therefore, the superiority of manifold compactness over variance may not be fully convincing. Consider adding a new distance-based measure. Different manifold constructions and distance calculations are also anticipated.
4. The algorithm is divided into multiple parts, and an end-to-end model would be more desirable.

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
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, authors propose manifold compactness, a coherence metric that does not depend on additional information, by incorporating data geometric properties into its design. And experiments are conducted on typical datasets to empirically validate the reasonableness of the metric. Authors then propose an method (MCSD), which directly considers risk and coherence as optimization objectives.

### Strengths
The authors show the results of many experiments.

### Weaknesses
There are a number of problems that the author needs to address, as detailed in the Questions section.

1. The example given by the author on page 4 is not convincing. The author claims that monotonicity can be used as a criterion for determining whether a measure of the semantics of slices is good, yet I do not think this is sufficient. Suppose I propose a measure that uses the difference between the number of elements in the cluster and the total number of elements as the measure, in which case the slices, as shown in Figure 3, would result in a positive increase in the value of the measure for each further slice, with a consistent trend with the measure proposed by the authors. Clearly, this arbitrarily proposed measure is not superior. Therefore, the authors need to further clarify the example. 
(e.g. Provide step-by-step details on how Figure 2c is generated, or clarify the relationship between the optimization variables w and g and how they relate to generating a new space)

2. Some key details are missing. The variables involved in the optimization objective appear to be w and the binary classifier g; how does this generate an new space? How do you generate the picture that the authors show in Figure 2c? If my understanding is wrong, please let me have further information.


3. The author mentions in line 273 that the w obtained by solving Eq. 2 is used to train the slice function g. Are the training samples obtained using w already the desired samples? Does this result in a meaningless slice function g?
(e.g. Clarify the purpose of training g if w already identifies the desired samples)


4. Does the slicing function obtained by the authors give the same output results from the same input data in each slicing? If so, does multiple slices require re-solving Eq. 2 and re-training the slice function g? I think the desired slicing result can already be obtained before training the slicing function g, does this mean that training the slicing function is meaningless? Can the authors clarify this?

5. What is the difference between Eq. 2 and a clustering method? Equation 2 seems to be a clustering method as well. 
(e.g. Discuss how the proposed method specifically addresses the goals of error slice discovery in ways that clustering alone may not )

6. In line 71, the authors describe the coherence method of past methods as only indirectly joining the optimization process. However, the authors' method also seems to be a two-step optimization process: i.e., first optimize the clustering and then optimize the slicing function g. If I have misunderstood, please clarify further.

7. The authors need to clarify further in the Section 1 what is the reason for proposing this method. The current motivation of the authors for proposing the method seems to be somewhat weak.

### Questions
1. The example given by the author on page 4 is not convincing. The author claims that monotonicity can be used as a criterion for determining whether a measure of the semantics of slices is good, yet I do not think this is sufficient. Suppose I propose a measure that uses the difference between the number of elements in the cluster and the total number of elements as the measure, in which case the slices, as shown in Figure 3, would result in a positive increase in the value of the measure for each further slice, with a consistent trend with the measure proposed by the authors. Clearly, this arbitrarily proposed measure is not superior. Therefore, the authors need to further clarify the example.
(e.g. Provide step-by-step details on how Figure 2c is generated, or clarify the relationship between the optimization variables w and g and how they relate to generating a new space)

2. Some key details are missing. The variables involved in the optimization objective appear to be w and the binary classifier g; how does this generate an new space? How do you generate the picture that the authors show in Figure 2c? If my understanding is wrong, please let me have further information.


3. The author mentions in line 273 that the w obtained by solving Eq. 2 is used to train the slice function g. Are the training samples obtained using w already the desired samples? Does this result in a meaningless slice function g?
(e.g. Clarify the purpose of training g if w already identifies the desired samples)


4. Does the slicing function obtained by the authors give the same output results from the same input data in each slicing? If so, does multiple slices require re-solving Eq. 2 and re-training the slice function g? I think the desired slicing result can already be obtained before training the slicing function g, does this mean that training the slicing function is meaningless? Can the authors clarify this?

5. What is the difference between Eq. 2 and a clustering method? Equation 2 seems to be a clustering method as well. 
(e.g. Discuss how the proposed method specifically addresses the goals of error slice discovery in ways that clustering alone may not )

6. In line 71, the authors describe the coherence method of past methods as only indirectly joining the optimization process. However, the authors' method also seems to be a two-step optimization process: i.e., first optimize the clustering and then optimize the slicing function g. If I have misunderstood, please clarify further.

7. The authors need to clarify further in the Section 1 what is the reason for proposing this method. The current motivation of the authors for proposing the method seems to be somewhat weak.

### Soundness
2

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
The paper identifies error slices within data subsets using manifold compactness and measures the similarity of certain features in the error samples based on the level of manifold compactness. This approach focuses on detecting error slices that have both high risk (high error rate) and high coherence, making these slices easier to interpret and understand.

### Strengths
1. It provides a different perspective for measuring error slices, and this metric does not require predefined slice label information.
2. An algorithm called MCSD is proposed, which directly uses model risk and coherence as optimization objectives.
3. The experimental data is thorough and demonstrates the effectiveness of the proposed method across multiple datasets.

### Weaknesses
The further explanation of the experiments is missing. More information pls see Questions.

1. In the first paragraph of the problem definition on page 2: Does $\mathcal{Y} \times \mathcal{Y}$ represent the Cartesian product of two sets? If so, one should represent the predicted label, and the other should represent the true label. Why are both symbols $\mathcal{Y}$?

2. The method proposed by the authors provides greater interpretability and feature similarity consistency when identifying error subsets, as shown in the visualization results of the CELEBA dataset in Figure 4. However, why does the ACC of the error slices identified by MCSD outperform the SOTA methods by such a large margin? Besides this specific similar feature, what other factors could lead to poor performance of the sliced subsets?

3. Why does Table 4 only compare the MCSD method with the Spotlight method?

4. I have some concerns about the metric proposed by the authors. The expected trend in the experimental data is that as ACC increases, the Comp result should also increase. Why do Tables 2, 3, and 5 not follow this trend? Perhaps I am missing something—do the authors provide any further explanation?

### Questions
1. In the first paragraph of the problem definition on page 2: Does $\mathcal{Y} \times \mathcal{Y}$ represent the Cartesian product of two sets? If so, one should represent the predicted label, and the other should represent the true label. Why are both symbols $\mathcal{Y}$?

2. The method proposed by the authors provides greater interpretability and feature similarity consistency when identifying error subsets, as shown in the visualization results of the CELEBA dataset in Figure 4. However, why does the ACC of the error slices identified by MCSD outperform the SOTA methods by such a large margin? Besides this specific similar feature, what other factors could lead to poor performance of the sliced subsets?

3. Why does Table 4 only compare the MCSD method with the Spotlight method?

4. I have some concerns about the metric proposed by the authors. The expected trend in the experimental data is that as ACC increases, the Comp result should also increase. Why do Tables 2, 3, and 5 not follow this trend? Perhaps I am missing something—do the authors provide any further explanation?

### Soundness
2

### Presentation
3

### Contribution
3
