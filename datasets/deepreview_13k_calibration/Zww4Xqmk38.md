# Tree-based Ensemble Learning for Out-of-distribution Detection

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 8, 3, 5

## Abstract
\noindent
Being able to successfully determine whether the testing samples has similar distribution as the training samples is a fundamental question to address before we can safely deploy most of the machine learning models into practice. In this paper, we propose TOOD detection, a simple yet effective tree-based out-of-distribution (TOOD) detection mechanism to determine if a set of unseen samples will have similar distribution as of the training samples. The TOOD detection mechanism is based on computing pairwise hamming distance of testing samples' tree embeddings, which are obtained by fitting a tree-based ensemble model through in-distribution training samples. Our approach is interpretable and robust for its tree-based nature. Furthermore, our approach is efficient, flexible to various machine learning tasks, and can be easily generalized to unsupervised setting. Extensive experiments are conducted to show the proposed method outperforms other state-of-the-art out-of-distribution detection methods in distinguishing the in-distribution from out-of-distribution on various tabular, image, and text data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the fundamental question of determining whether testing samples have a similar distribution to training samples, which is crucial for the safe deployment of machine learning models. The authors propose a mechanism called TOOD detection, which is a simple and effective tree-based method for detecting out-of-distribution (TOOD) samples. The TOOD detection mechanism works by computing the pairwise hamming distance of tree embeddings of the testing samples. These embeddings are obtained by fitting a tree-based ensemble model using in-distribution training samples. The authors highlight that their approach is interpretable and robust due to its tree-based nature. Additionally, the method is efficient, flexible across various machine learning tasks, and can be applied to unsupervised settings. The paper presents extensive experiments to demonstrate the superiority of the proposed method compared to other state-of-the-art out-of-distribution detection methods. The experiments cover tabular, image, and text data, showing the effectiveness of the approach in distinguishing between in-distribution and out-of-distribution samples.

### Strengths
Novel approach: The paper introduces a new mechanism, TOOD detection, which offers a novel perspective on addressing the problem of determining whether testing samples have a similar distribution to training samples by a tree based ensemble method. From my personal knowledge, tree structures and ensemble methods are seldomly studied in OOD detection, making the considered direction an interesting line of works. 


Effective methodology: The proposed TOOD detection mechanism based on computing pairwise hamming distances of tree embeddings proves to be simple yet effective in distinguishing in-distribution from out-of-distribution samples. The approach demonstrates superior performance compared to other state-of-the-art methods in extensive experiments across various data types.

Interpretable and robust: The authors highlight the interpretability and robustness of their approach, attributed to its tree-based nature. This characteristic allows for better understanding and trust in the detection process, making it easier to analyze and interpret the results.

Flexibility across machine learning tasks: The paper emphasizes the flexibility of the proposed approach, indicating that it can be applied to various machine learning tasks. This versatility makes it applicable to a wide range of scenarios, adding practical value to the research.

Generalizability to unsupervised setting: The authors state that their method can be easily generalized to unsupervised settings, which is beneficial in scenarios where labeled data is scarce or unavailable. This adaptability enhances the applicability of the proposed approach.

### Weaknesses
The authors define OOD in the abstract, but such a definition may violate the main stream of the community. In my view, telling the difference between two distributions is more related to two sample test. While in OOD Detection,  we typically assume the ID and OOD distribution has been mixed, thus we need to tell data as ID and OOD cases instance/point wise. I think such a setting is more difficult than two sample test, making OOD detection remain a challenging task in the literature. It will be great if the authors can discuss about it. 

The paper is not clearly written. I am not sure if the proposed tree based method uses original features in the input space or embedding feature given by the pretrained classifier. If the former is true, I am not sure if the tree based methods have enough capability to fit complex classification tasks such as CIFAR classification. Also, the computational complexity will be high (even built upon the high dimensional embedding features). If the latter is true, I am not sure if the learned embedding features are good enough in OOD detection, especially considering the reliance of strong assumptions in their theoretical analysis (see also in the below questions).

A related question is about the strong assumption in Theorem 1. In the input space, especially for the complex image classification task, it is obviously not true. In the embedding space, since model cannot perfectly separate ID and OOD cases, it is still a strong assumption. Therefore, I cannot fully understand why the tree based method is superior over previous works such as distance based methods (KNN), MSP, Energy, among many others. 

Why ensemble method can facilitate OOD detection, the theoretical analysis does not cover such an issue, meanwhile heuristic explanation and empirical evaluation  are not sufficient. Therefore, I think the authors should discuss more about why ensembling is critical for the suggested tree based methods. 

The authors make another strong assumption that the calibration failures, which is the main cause of why DNNs fail in OOD detection, will not occur for tree based methods. I am not sure if it is true in the real world, and more evaluation and ablation should be provided. 

More discussion about the hyper parameter setting and the choice of evaluation datasets should be discussed here. More experiments about hard OOD detection and wild OOD detection are also of the interest in the literature.

### Questions
Please see the Weaknesses above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study presents a novel scoring function for mismatch detection. For each test input, the position of its terminal node in a set of classification trees is recorded. Then the authors use the hamming distance between two location vectors to quantify the similarity of two sample points.

### Strengths
- The proposed detection method is novel and interesting.
- There is diversity in the experimental setup, considering OOD detection on multiple data types.
- Theoretical analysis is provided.

### Weaknesses
 - This method is not valid for high-dimensional inputs.
- There are no experiments on ImageNet benchmark.
- The results of the theoretical analysis are for a single classification tree model, not for a random forest.

### Questions
1. For image classification, does the input $x$ refer to an image or a feature vector obtained from a pre-trained feature extractor? 
2. Do the hyper-parameters used in training the tree models (such as tree depth, the number of terminal nodes, and the minimal size of terminal nodes) have any effect on OOD Detection results?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a tree-based ensemble learning approach for out-of-distribution (OOD) detection. The method involves calculating the Hamming distance for the tree embeddings obtained from a random forest trained on in-distribution data. The authors offer a comprehensive theoretical analysis of this method to substantiate their proposal. Additionally, empirical experiments are conducted on synthetic datasets and benchmark datasets to validate its effectiveness.

### Strengths
The strengths of this paper can be summarized as follows:

1. **Experimental Results:** The experiments demonstrated the proposal's strong performance across various synthetic and benchmark datasets.

2. **Clarity and Presentation:** The paper is meticulously structured, and the ideas presented are easily comprehensible, ensuring accessibility for readers.

### Weaknesses
While this paper exhibits several strengths, it also presents several weaknesses, which are outlined as follows:

1. **Limitation 1**: The idea that "out-of-distribution data may exhibit smaller Hamming distances among themselves" hinges on the assumption that the support of training and testing distributions does not overlap in each dimension. However, this assumption raises doubts as it prohibits anomalies from occurring in only one dimension. For instance, consider a scenario where in-distribution data lies within a hypercube $[0,1]^d$. If out-of-distribution data appears only along one dimension, say as values much greater than 1 in the first dimension while remaining within [0,1] for all other dimensions, the Hamming distance could be large, not small. This contradicts the core assumption.

2. **Limitation 2**: The central idea appears to implicitly assume that labels are distributed uniformly across different classes. Consider a binary classification scenario where the major class has a significantly higher probability than the minor class, and the labels are determined by whether $x_{i} < s_{i}$. In such cases, the Hamming distance of the embedding of in-distribution test data may be small among them, primarily because most of the samples reside in the same leaf as the major class.

3. **Regarding Experiments**: It is advisable to present the experimental results in the format "mean ± std" due to the inherent randomness of random forests.

4. **Regarding Related Work**: Decision tree learning and random forests should be traced back to the works of Quinlan (1979), Breiman et al. (1984), and Breiman (2001).

### Questions
See Weaknesses #1 and #2.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on a method called TOOD detection, which aims to improve out-of-distribution (OOD) detection in tree-based machine learning models. The paper evaluates this method on various types of data, including tabular, image, and text data. It also compares TOOD detection with existing state-of-the-art OOD detection methods and claims to show favorable or comparable performance. The paper includes mathematical validation to support its methodology and presents preliminary results that indicate the effectiveness of TOOD detection.

### Strengths
The paper is comprehensive and covers several types of data, making it widely applicable.
It provides rigorous theoretical results to mathematically validate its model.
The paper compares its method to existing diverse techniques, providing a benchmark for its effectiveness.
Preliminary results are promising, indicating the potential impact of the research.
The paper addresses the issue of OOD detection based on the new approach, tree-based algorithms, which is a significant problem in machine learning.

### Weaknesses
It only compares their models with kernel-based baselines for efficiency analysis. More comprehensive comparisons are necessary.

The "Comparison with State-of-the-Arts" section does not provide the comparison between TOOD and the recent models. 

As shown in Figure 7, the proposed model may not be effective in high-dimensional cases.

### Questions
Please see the Weakness and Strengths sections.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
