# Exploring Pointwise Similarity of Representations

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Representation similarity measures have emerged as a popular tool for examining learned representations.
Many existing studies have focused on analyzing aggregate estimates of similarity at a global level, i.e. over a set of representations for N input examples.
In this work, we shed light on the importance of investigating similarity of representations at a local level, i.e. representations of a single input example.
We show that peering through the lens of similarity of individual data points can reveal previously overlooked phenomena in deep learning.
Specifically, we investigate the similarity in learned representations of inputs by architecturally identical models that only differ in random initialization.
We find that while standard models represent (most) inputs similarly only when they are drawn from training data distribution, adversarially trained models represent a wide variety of out-of-distribution inputs similarly, thus indicating that these models learn more "stable" representations.
We design an instantiation of such a pointwise measure, named Pointwise Normalized Kernel Alignment (PNKA), that provides a way to quantify the similarity of an individual point across distinct representation spaces.
Using PNKA, we additionally show how we can further understand the effects of data (e.g. corruptions) and model (e.g. fairness constraints) interventions on the model's representations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel measure for comparing the similarity of latent spaces, with a special focus on its locality property instead of a global one. By independently computing intra-space distances with respect to a specific set of reference points, the authors relate these vectors using the angles between them, assuming a known correspondence between the two sets. The paper then proceeds with three major applications of the method and their validation: i) correlating the measure's similarity output with classification errors on ResNets, ii) out-of-distribution detection, and iii) studying the geometric effects of debiasing techniques on GloVe embeddings.

### Strengths
- The paper presents an interesting approach to comparing the similarity of latent spaces and well-motivates its importance;
- The applications proposed, particularly relating to classification errors and out-of-distribution detection on ResNets and the effects of debiasing on GloVe embeddings, are noteworthy;
- The experimental setup appears robust, providing valuable insights that can be considered useful contributions to the field;
- The supplementary material is extensive and also contains the code, enhancing reproducibility;

### Weaknesses
 - The method explanation lacks some clarity. Multiple readings were necessary due to references to the use of yet-to-be-introduced concepts such as "neighborhood" and "reference points". I think there's also some mismatch between the method presentation and the general take that the neighborhoods of each point are important to their representation since the reference points are never restricted or searched in the neighbors.
- Despite the valuable insights from the experiments, their current setting might not be general enough, limiting broader application and significance. For example, the relationship between PNKA and model disagreement on specific data points is limited to only a cross-training setting, without considering other possible variations such as architectural ones. This is something I would expect in a more theoretical work. The reported results are convincing, but, as commendably acknowledged by the authors themselves in the discussion section, the variation in architecture/tasks is not enough to validate the robustness of the proposed claims;
- There is a noticeable overlap in methodology with cited prior work, particularly Moschella et al. Although the paper frames its method as a kernel method application, it bears a strong resemblance to the direct application of cosine similarity between relative encodings, a technique already explored in the mentioned work. This overlap reduces the novelty of the method but doesn't impact its interesting applications;

### Questions
- as described in the weaknesses section, I would ask the authors to please clarify the "neighborhood" concept and its relationship with the reference points;
- In the current manuscript form, I'm recommending a weak reject. However, I'm willing to increase the score if either the lack of variety in experiments or the relationship with previous work is addressed since the former would improve the experimental contributions while the latter the theoretical ones;

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
the submission proposed a point-wise normalized kernel alignment for measuring the similarity of a pair of vector representations that are produced by two trained neural networks on a single data point. The core concept which the proposed similarity score draws inspiration from is the assumption that similar vector representations should have similar neighbours, so we can directly measure the similarity of neighbours of the same point in two representation spaces. 

Through experiments, they showed that trained models are likely to disagree on points with representations that are not so similar, and robust models are likely to agree more since they produce similar representations.

### Strengths
1. the proposed similarity score is well-motivated, and easy to implement.

2. the experiments show evidence of the effectiveness of the proposed score.

### Weaknesses
I have several questions regarding the usefulness of the proposed scores.

1. if the assumption is that the neighbours of a single point in two representation spaces matter in the construction of useful similarity scores, then I think an easy and effective approach would be Jaccard distance, and its variants that take distances into consideration.  I wonder how the proposed approach compares to Jaccard distance.

2. it seems natural that models tend to disagree on misclassified data points, so if that is the case, we would then only need to look at the misclassified points as the unstable points rather than using the proposed similarity score to determine the unstable ones?

3. since the comparison is now conditioned on a single data point along with its reference points, when two models are presented to us, how do we determine which model to use? The submission mentioned transfer learning as a use case, but it seems relatively non-trivial to me in terms of how we use the score in selecting the better pre-trained model to transfer from.

### Questions
n/a

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes new similarity measure between two representation spaces. The main idea of the new measure lies in assessing similarity locally, i.e., by comparing neighbourhoods of points between representation spaces.

### Strengths
The development of reliable similarity measures between representations is important and ongoing direction in the modern deep learning. Authors suggest studying similarity from the perspective of neighbourhoods of points and examine the proposed measure in various experiments.

### Weaknesses
My main concern is that authors propose a new metric which is build on CKA and CKA is known to have pitfalls (i.e. [1]). Thus, the very important part of suggesting a new metric is studying the pitfalls of the new measure and understanding the differences from the existing metrics. In the current version of the paper I did not see such investigation.

Also, for the similarity measure, it is important to understand the context in which we are using them. Authors argue that studying neighbourhoods might make sense, but does not discuss in which context it is important. For example, authors show that PNKA as CKA also shares such properties as the invariance to orthogonal transformations and to isotropic scaling, but again sometimes it can be beneficial, sometimes not, depends on the context.

Thus, deeper understanding of pitfalls and studying application areas are important to prevent careless use of the new metric by the community.

### Questions
In general, I would like to see the additional analysis as mentioned in the Weaknesses part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
