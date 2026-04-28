# Views Can Be Deceiving: Improved SSL Through Feature Space Augmentation

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
Supervised learning methods have been found to exhibit inductive biases favoring simpler features. When such features are spuriously correlated with the label, this can result in suboptimal performance on minority subgroups.
Despite the growing popularity of methods which learn from \textit{unlabeled} data, the extent to which these representations encode spurious features is unclear. In this work, we explore the impact of spurious features on Self-Supervised Learning (SSL) for visual representation learning. We first empirically show that commonly used augmentations in SSL can cause undesired invariances in the image space, and illustrate this with a simple example. We further show that classical approaches in combating spurious correlations, such as dataset re-sampling during SSL, do not consistently lead to invariant representations. 
Motivated by these findings, we propose \ours to remove spurious information from these representations during pretraining, by regularizing later layers of the encoder via pruning. 
We find that our method produces representations which outperform the baselines on several benchmarks, without the need for group or label information during SSL.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the impact of spurious features on Self-Supervised Learning (SSL) in visual representation learning. It starts by demonstrating that commonly used augmentations in SSL can inadvertently introduce undesired invariances in the image space, highlighting this issue with a simple example. The authors also examine classical approaches to mitigating spurious correlations, such as dataset re-sampling during SSL, and find these methods inconsistent in leading to invariant representations.

To address these challenges, the paper proposes a novel method called "LATE TVG," which aims to remove spurious information from representations during pretraining. This is achieved by regularizing later layers of the encoder via pruning. The authors present empirical evidence showing that LATE TVG produces representations that outperform baselines on several benchmarks. Notably, their method does not require group or label information during SSL, marking a significant advantage over traditional approaches.

The paper provides a thorough examination of the pitfalls of inductive biases in supervised learning, particularly when dealing with minority subgroups and spurious correlations. The proposed solution, LATE TVG, is a promising step towards more robust and fair SSL models, showing effectiveness in various benchmarks without relying on group or label information.

### Strengths
**1. Originality:**
The paper introduces a novel method, "LATE TVG," to mitigate the influence of spurious correlations in Self-Supervised Learning (SSL) for visual representation learning. This approach is original in its utilization of later layer regularization via pruning to enhance the robustness of SSL models. Unlike conventional methods that often rely on re-sampling or require group or label information, LATE TVG innovatively ensures invariant representations without such dependencies. The idea of addressing undesired invariances introduced by common augmentations in SSL is a creative combination of existing concepts in a unique problem formulation.

**2. Quality:** The empirical evidence presented in the paper is of high quality, showcasing the effectiveness of LATE TVG through comprehensive benchmarks. The authors provide a detailed analysis of the pitfalls of standard augmentations in SSL and demonstrate the superiority of their method over traditional approaches. The experiments are well-designed and executed, offering convincing support for the proposed solution. The quality of the research is further underscored by the rigorous testing on various benchmarks, which highlights the method's robustness and generalizability.

**3. Clarity and Significance:** The paper is clearly written, with a well-structured format that guides the reader through the problem statement, methodology, and findings. The significance of the work is evident, as it addresses a critical challenge in SSL—ensuring fairness and robustness in visual representation learning. By providing a solution that does not require group or label information during SSL, the paper makes a useful contribution to the field, potentially leading to more equitable and effective machine learning models.

### Weaknesses
 **1. Scalability and Efficiency:** The paper introduces the LATE TVG method, which involves regularizing later layers of the encoder via pruning. While this approach is novel, the scalability and computational efficiency of the method in large-scale settings are not thoroughly addressed. Pruning, especially in deeper layers, can be computationally intensive and may not scale well with very deep networks or extremely large datasets. The paper lacks a detailed analysis of the computational overhead introduced by the pruning mechanism, particularly in terms of FLOPs and memory requirements, which are critical for practical applications.

**2. Domain Generalization:** Although the paper demonstrates the effectiveness of LATE TVG across several benchmarks, it primarily focuses on visual representation learning. The generalizability of the method to other domains or types of data, such as text or audio, is not explored. It remains unclear whether the proposed pruning strategy would be effective in different modalities where the nature of spurious correlations and feature representations can vary significantly. The paper does not discuss potential modifications or adaptations that might be needed to apply LATE TVG to non-visual data.

**3. Comparison with State-of-the-Art:** While the paper shows that LATE TVG outperforms traditional methods, it does not provide an extensive comparison with the latest state-of-the-art methods in SSL that address similar challenges. Without this context, it's difficult to gauge the relative progress made. The paper needs to include a more thorough comparison with recent techniques that explicitly target spurious correlations or aim to improve robustness in SSL, providing a more comprehensive understanding of the method's competitive standing.

### Questions
Here are some questions and suggestions for the authors:

**1. Clarification on Scalability and Efficiency:**
- Question: Could you provide more details on the computational efficiency and scalability of the LATE TVG method, especially when applied to very large datasets or extremely deep networks?
- Suggestion: It would be beneficial if the authors could include a section discussing the computational complexity of their method, possibly comparing it with other SSL methods in terms of training time and resource utilization.

**2. Long-Term Effects of Pruning:**

- Question: Pruning, especially in later layers, might have long-term effects on the learning capabilities of the network. Have you investigated how the pruning process affects the network's ability to learn new tasks or adapt to new data over time?
- Suggestion: Providing insights or conducting experiments on the long-term effects of pruning could offer a more nuanced understanding of the method's robustness and adaptability.

**3. Robustness to Adversarial Attacks:**

- Question: How robust is the LATE TVG method to adversarial attacks, given that it focuses on mitigating spurious correlations?
- Suggestion: Including experiments or discussions on the method's robustness to adversarial examples could highlight another dimension of its efficacy, particularly in security-sensitive applications.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper explores the impact of spurious correlations on Self Supervised Learning (SSL) for visual representation learning. The paper discusses how inductive biases in supervised learning favor simpler features, and when these features are spuriously correlated with the labels, it can result in suboptimal performance, especially for minority subgroups. The paper aims to investigate the extent to which SSL representations rely on spurious features for prediction.

The paper empirically demonstrates that common augmentations used in SSL can introduce undesired invariances in the image space, which may be problematic. It also finds that traditional approaches, such as dataset re-sampling during SSL, do not consistently lead to invariant representations. To address these findings, the paper proposes a new approach called LATETVG, which removes spurious information from SSL representations during pretraining by regularizing later layers of the encoder through pruning. LATETVG is shown to produce representations that outperform baselines on various benchmarks without requiring group or label information during SSL.

### Strengths
The strengths of the paper are as follows:

Theoretical Insights: By analyzing simpler cases (Section 3.3), the paper provides theoretical arguments that offer a deeper understanding of how common augmentations used in Self Supervised Learning (SSL) pre-training affect the model's reliance on spurious features for downstream linear classifiers. 

Experimental evaluation of Spurious Feature Learning: The paper empirically explores the extent of spurious feature learning in self-supervised representations, focusing mainly on downstream worst-group performance. It demonstrates that traditional techniques for avoiding spurious correlations, such as re-sampling the training set with group information, do not consistently lead to improved core feature representations. This empirical analysis exposes the limitations of existing approaches and motivates the need for novel solutions.

LATETVG: The paper introduces LATETVG, a novel approach designed to correct biases introduced by augmentations. LATETVG modifies the views of samples in the representation space, effectively improving worst-group performance in downstream tasks on four datasets. This contribution presents a practical solution to the problem of spurious correlations in SSL pre-training, resulting in better core feature learning.

### Weaknesses
The paper is missing references to some important works on spurious feature learning:

1. Salient ImageNet: How to discover spurious features in deep learning?
2. WILDS: A Benchmark of in-the-Wild Distribution Shifts


Most of the results given in the paper are using smaller datasets. I believe the analysis of Section 4 could have been carried out a large number of publicly available SSL trained models. I would have liked to see some results using models trained on large datasets. 

To evaluate the performance of models, the authors could have used more challenging datasets such as:
1. FOCUS: FOCUS: Familiar Objects in Common and Uncommon Settings
2. Hard ImageNet: Segmentations for objects with strong spurious cues
3. WILDS: A Benchmark of in-the-Wild Distribution Shifts

Most of the results seem to be on relatively simpler datasets.

### Questions
Why is the analysis of Section 4 limited to simpler datasets and no results are provided for the datasets discussed above?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of spurious correlations in self-supervised learning, in particular, contrastive learning. The paper first formally shows, in a toy setting, that ensuring the groups are balanced is not sufficient to ensure a spurious correlation is not learnt. This is then confirmed empirically as well. The paper then presents the new method to remedy this: "LATE-LAYER TRANSFORMATION-BASED VIEW GENERATION". This involves conducting magnitude pruning for the later layers of the network to remove dependence on spurious. This method is able to improve worst-group accuracy on some popular datasets to study spurious correlations in supervised learning.

### Strengths
1. The problem of spurious correlations has not been studied for SSL before and is of importance, considering the lack of group / label information in SSL can make this hard to remedy. 

2. The conclusion that balancing the data may not be effective for remedying spurious correlations is extremely interesting. 

3. The method proposed is effective in remedying worst-group accuracy despite other standard methods like group balancing failing.

### Weaknesses
1. The intuition / reasoning behind the choice to prune the later layers to forget the spurious feature is not well-explained / discussed sufficiently.


### Questions
1. The problem of spurious correlations in SSL is actually equivalent to **feature suppression** studied first here: https://proceedings.neurips.cc/paper/2021/hash/628f16b29939d1b060af49f66ae0f7f8-Abstract.html. It will be useful to discuss the equivalence of this problem as well as other relevant literature. 

2. In supervised learning, the models trained on Waterbirds etc. are initialized from ImageNet pretrained weights. Is that the case here as well? 

3. Experiments on some larger scale datasets provided in packages such as WILDS (https://wilds.stanford.edu/) or SpuCo (https://spuco.readthedocs.io/en/latest/) can strengthen the empirical success of the method.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors explore the self-supervised learning (SSL) in visual representation learning. They emphasize the impact of spurious features on model efficacy. Spurious features are those that are only correlated with the label for specific subsets of data, potentially leading to suboptimal results, especially for minority subgroups. This study delves into the extent to which SSL representations depend on such spurious features and introduces an innovative approach known as LATETVG to alleviate their impact during the pretraining phase.

### Strengths
* The introduced method effectively reduces spurious correlations and enhances the performance of downstream tasks across multiple datasets.

* The author presents a clear depiction of the prevalent issues with SSL arising from spurious features.

### Weaknesses
 * The paper's structure and content are not easy to follow. Specifically, the use of symbols like alpha, beta, and gamma appears to be overloaded, making it challenging to distinguish between the connectivity and the P matrix. The lack of clear definitions for these terms and their relationships makes the theoretical arguments difficult to parse. The reader is left to infer the precise meaning of each symbol in different contexts, which creates ambiguity and hinders understanding.
* It's unclear how the correlation in Table 1 is computed. It seems spurious attributes and core features are not defined for real data. Specifically, the method used to quantify the connectivity error rates is not sufficiently detailed, making it difficult to reproduce the results. Without a clear definition of spurious and core features in real-world datasets, the reported correlations lack a solid foundation and raise questions about their validity and interpretability. The paper should provide a concrete methodology for identifying and defining these attributes in the context of real-world data.
* The theoretical foundation leans heavily on Spectral Contrastive Learning, yet it is not used in the experimental section. This disconnect between theory and practice raises concerns about the relevance of the theoretical analysis. The paper does not adequately explain how the theoretical insights derived from Spectral Contrastive Learning translate into the practical implementation of the proposed method. The absence of empirical validation of the theoretical claims makes it difficult to assess the practical implications of the theoretical framework.
* The presentation would benefit significantly from the inclusion of an algorithmic representation of the proposed Late TVG method, enhancing its comprehensibility for readers. The current description lacks the necessary detail for readers to implement the method. A clear, step-by-step algorithm would greatly improve the clarity and reproducibility of the work.

### Questions
* Which training parameters were utilized in the LaterTVG method?
* How do the authors identify spurious features? The paper does not provide clear definitions distinguishing between spurious attributes and core features.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
