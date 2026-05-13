# GRADSIMCORE: GRADIENT SIMILARITY BASED REPRESENTATIVE INSTANCES AS CORESET

- Decision: Reject
- Scores: 1, 3, 3, 3

## Abstract
The rise in size and complexity of modern datasets and deep learning models have resulted in the usage of extensive computational resources and a rise in training time and effort. It also has increased the carbon footprint of training and fine-tuning models. One way to reduce the computational requirement is to extract the most representative subset (referred to as $\textit{coreset}$) that can substitute for the larger dataset. Coresets can thus replace huge datasets to train models and tune hyperparameters, especially in the early stages of training. This will result in a significant reduction of computational resource requirement and reduce carbon footprint. We propose a simple and novel framework based on the similarity of loss gradients for identifying the representative training instances as a coreset. Our method, dubbed as $\textit{GradSimCore}$, outperforms the state-of-the-art coreset selection algorithms on popular benchmark datasets ranging from MNIST to ImageNet. Because of its simplicity and effectiveness, our method is an important baseline for evaluating the effectiveness of the coreset selection algorithms. Anonymized codes for the proposed baseline are provided at https://anonymous.4open.science/r/GradSimCore-8884

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work the authors tackle the problem of coreset extraction from a dataset. This is a key problem in many scenarios from continual learning to meta-learning and HPO. The authors propose a simple technique where they identify samples that produce gradients that are closer to all the other samples (or N nearest samples) from the same class. They construct this representative set to be the coreset for the dataset. By controlling N, they can control the size of the coreset. They run experiments where they benchmark against the best result reported in an open-source library (deepcore) and show that at very low sizes of N, they perform slightly better.

### Strengths
The work is very simple and straight forward, particularly so for smaller datasets. Run the dataset through a model for a few epochs to stabilize the training, run every sample and measure the gradients of the last layer, measure a cross-similarity matrix and average it column-wise and sort.

### Weaknesses
This work falls short on several areas.
1. There are several assumptions made about the what an averaged gradient would imply or what it means for a sample to produce a gradient that is also closer to other samples, that need a more rigorous mathematical underpinning. It is not often clear or true that samples that produce noise-free gradients are the most representative. In fact, often the opposite is true and has been utilized in a lot of data sampling techniques from hard-negative mining to label softening, just to produce noisy gradients. This is also a reason why regularization techniques such as dropouts work. The authors assumption may only be true in cases where there are some stringent constraints on the loss manifold. The core idea of selecting samples based on the similarity of their gradients to other samples within the same class lacks a strong theoretical justification. The assumption that gradients closer to the average representativeness is not universally valid and requires more rigorous analysis. The authors need to provide a more in-depth explanation of why this approach is expected to work, especially given the existing literature on the importance of noisy gradients for effective learning.
2. The algorithm itself is tremendously computationally expensive. Quick back-of-the-envelope calculations indicate that for complete Imagenet dataset, most modern server-class instances will not be able to even hold the gradients in memory. Computationally, it will be more expensive to identify the coreset, than to run training on the entire dataset. The authors need to provide a more detailed analysis of the computational complexity of their method, including memory requirements and time complexity. The current description lacks the necessary detail to assess the practical feasibility of the approach, especially for large-scale datasets. Furthermore, the authors should consider the overhead of calculating the similarity matrix, which could be a bottleneck for larger datasets.
3. The experimentation is done on small datasets, in smaller models. From the results, it looks like their work only works at low-accuracy levels (or extremely low data sizes). In modern day ML, unless there is parity in accuracy (generalization performance), its not a practically usable model, no matter the constraints. Putting aside the pragmatism, the results show that the authors' approach does not apply at even relatively modest size of coreset. The experimental results are not compelling, as they are limited to small datasets and models. The authors need to demonstrate the effectiveness of their method on larger datasets and more complex models to establish its practical relevance. The current results do not provide sufficient evidence to support the claim that the proposed method is a viable alternative to existing coreset selection techniques. The lack of results at higher accuracy levels is also a major concern.

### Questions
The authors compare against deepcore library's best algorithm, but fail to mention which algorithm it is and what were settings used. This does not even convey the basic details. Will it be possible to make a more direct comparison?

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel coreset selection method, GradSimCore, to select the representative coreset from the original large dataset. The novel part of GradSimCore is its new metric to measure the importance of each example. To calculate the importance of an example, GradSimCore calculates and sums the cosine value between the gradient of this example on a certain model and the gradient of other examples on the same model as the importance value. The evaluation results on CIFAR10, CIFAR100, and ImageNet datasets show that GradSimCore outperforms methods implemented in DeepCore for most cases.

### Strengths
1. This paper proposes a novel metric to calculate the data importance based on the similarity of loss gradients.

2. The paper compares the proposed method with baselines implemented in DeepCore and shows that GradSimCore outperforms other baselines in most cases.

### Weaknesses
My major concerns on this paper are on the evaluation part.

The paper only compares the baselines implemented in DeepCore, which does not include some SOTA coreset selection baselines, like EL2N[1], CCS[2], and Moderate[3]. It is not convincing enough to demonstrate the effectiveness of the proposed method without comparing it with those SOTA baselines.

Besides, the evaluation data in Table 2,5,6 is kind of selective. The settings for all evaluations have “percentage of dataset” of less than 20%. It seems that GradSimCore’s performance drops a lot with a larger percentage of datasets (even with the reported data). It will be helpful to compare the coreset selection performance under various percentages of datasets to better demonstrate the effectiveness of GradSimCore.

### Questions
See weakness.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The use of gradients as indicators is not originally proposed in this article. The only good thing about this article is that it provides links to the code, beyond that I don't see any good things, whether it's typography, experiments, theoretical proofs, or methodology. I suggest that ICLR can access the GPT-4V interface and directly reject such low-quality submissions.

### Strengths
This article is that it provides links to the code

### Weaknesses
The use of gradients as indicators is not originally proposed in this article. The only good thing about this article is that it provides links to the code, beyond that I don't see any good things, whether it's typography, experiments, theoretical proofs, or methodology. I suggest that ICLR can access the GPT-4V interface and directly reject such low-quality submissions.

### Questions
No question! I suggest the author should not resubmit a manuscript like this again.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a core-set selection method based on the gradient-direction similarity (cosine distance) at the early phases of training (5-10 epochs). While the underlying idea (and its simplicity) is appealing and first experimental results are promising, the paper does not seem to be in a finalized form. I believe it requires a further iteration to establish the full potential of the method. Length and content-wise, it would fit a densely written 4-page workshop paper very well in preparation for a future main conference paper submission, e.g., for ICML or CVPR. Overall, I think this paper (in the current version) is not refined/detailed enough for the main conference and would require further experimental and comparative work to be competitive with other submitted papers.

Concretely,
1 while several approaches are discussed in related work, the proposed GradSimCore method is only compared to "DeepCore". 
2 also this "DeepCore" comparison is not very clear: it is stated that DeepCore is a library for coreset selection. To which algorithm in this library is the method compared to? 
3 the manuscript overall seems to be very stretched in the length to barely fill the length requirement of 9 pages. Tables are stretched; Algorithm 1 could fit half the width, The notation table is not necessary. Can be described at shorter length in text, Table 1 could also be described shorter in text. 

Content-wise, 
1. it is not clear if the method seen as a baseline (called as such in the discussion) or as a new state-of-the-art method (it beats the DeepCore comparison method across several datasets)
2. equation 3 seems to be the cosine similarity. It should be also called as such.
3. equation 4. Why is the expectation used here? Interpreting this (discrete) equation, a simple average 1/N sum would be sufficient and clearer
5. equation 5. How is the threshold chosen? Given the experiments (percentage of the datasets), it seems that the threshold is not used but the samples are rather sorted by f(x) score and the top x% samples are chosen

### Strengths
* efficient and effective core-set selection is an important direction that requires further approaches and more research.
* the method is overall intuitive and can be tested/implemented from the paper

### Weaknesses
1 while several approaches are discussed in related work, the proposed GradSimCore method is only compared to "DeepCore".
2 also this "DeepCore" comparison is not very clear: it is stated that DeepCore is a library for coreset selection. To which algorithm in this library is the method compared to?
3 the manuscript overall seems to be very stretched in the length to barely fill the length requirement of 9 pages. Tables are stretched; Algorithm 1 could fit half the width, The notation table is not necessary. Can be described at shorter length in text, Table 1 could also be described shorter in text.

Content-wise,
1. it is not clear if the method seen as a baseline (called as such in the discussion) or as a new state-of-the-art method (it beats the DeepCore comparison method across several datasets)
2. equation 3 seems to be the cosine similarity. It should be also called as such.
3. equation 4. Why is the expectation used here? Interpreting this (discrete) equation, a simple average 1/N sum would be sufficient and clearer
5. equation 5. How is the threshold chosen? Given the experiments (percentage of the datasets), it seems that the threshold is not used but the samples are rather sorted by f(x) score and the top x% samples are chosen

### Questions
1. which DeepCore method was GradSimCore compared to?
2. is this approach applicable to datasets that are gradually collected? I.e., by rejecting newly redundant collected samples that produce a low score? It seems from this version of the paper, that the sample-wise importance scores are calculated on the entire dataset first. Then afterwards, the subset of this dataset is identified. This seems to contradict the motivation of the paper of requiring smaller datasets that are more representative overall (Table 1)

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
