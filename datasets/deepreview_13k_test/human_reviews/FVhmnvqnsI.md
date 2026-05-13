# Multisize Dataset Condensation

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
While dataset condensation effectively enhances training efficiency, its application in on-device scenarios brings unique challenges. 1) Due to the fluctuating computational resources of these devices, there's a demand for a flexible dataset size that diverges from a predefined size. 2) The limited computational power on devices often prevents additional condensation operations.
These two challenges connect to the ``subset degradation problem'' in traditional dataset condensation: a subset from a larger condensed dataset is often unrepresentative compared to directly condensing the whole dataset to that smaller size.
In this paper, we propose Multisize Dataset Condensation (MDC) by \textbf{compressing $N$ condensation processes into a single condensation process to obtain datasets with multiple sizes.}
Specifically, we introduce an ``adaptive subset loss'' on top of the basic condensation loss to mitigate the ``subset degradation problem''.
Our MDC method offers several benefits: 1) No additional condensation process is required; 2) reduced storage requirement by reusing condensed images.
Experiments validate our findings on networks including ConvNet, ResNet and DenseNet, and datasets including SVHN,  CIFAR-10, CIFAR-100 and ImageNet. For example, we achieved 5.22\%-6.40\% average accuracy gains on condensing CIFAR-10 to ten images per class.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the Multisize Dataset Condensation problem that can derive multiple subsets from the condensed images for supporting on-device scenarios. The authors identify “subset degradation problem” where the performance of a subset from condensed images is lower than directly condensing the full dataset to the target size. Subsequently, the authors propose “adaptive subset loss” where the most learnable subset is selected to update the subset, to alleviate the “subset degradation problem” for all subsets. Experimental results demonstrate that MDC works well for various datasets.

### Strengths
The paper presents a solution for DC named Multisize Dataset Condensation which is crucial for on-device scenarios. The proposed method outperforms baseline C significantly.

### Weaknesses
1. The synthetic samples within the subset seem to be fixed, which may not reflect “Multisize Dataset Condensation” correctly.

### Questions
I have several questions:
1. In Fig 2c, for baseline C, how to select subsets to calculate accuracy? Is it random? Let’s assume we have a subset of 2 images. Do we select 2 images from the condensed data randomly?
2. In basic condensation training (Sec 4.1), for each initialization the network is trained for 100 epochs. Is it the inner loop E?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method called Multisize Dataset Condensation (MDC) to compress multiple-size dataset condensation processes into a single process. The goal is to obtain a small synthetic dataset that is equally effective but much smaller in size. The authors introduce the concept of the Most Learnable Subset (MLS) and propose an adaptive subset loss to mitigate the "subset degradation problem" in traditional dataset condensation. The MDC method can reduce the condensing process and lower the storage consumption. The MDC achieves state-of-the-art performance on various models and datasets.

### Strengths
1. The proposed Multisize Dataset Condensation (MDC) method can effectively condense the N condensation processes into a single condensation process with lower storage and addresses the “subset degradation problem”.
2. The adaptive subset loss in the MDC method helps mitigate the “subset degradation problem” and improves the accuracy of the condensed dataset compared to the Baseline-C.
3. The concept of the rate of change of feature distance as a substitute for the computationally expensive “gradient distance” reduces computational overhead while capturing essential characteristics among subsets.

### Weaknesses
1. When the IPC (Inter-Process Communication) is small, there still exists a large accuracy gap between the proposed model and Baseline-A as shown in Figure 2 and Table 1.
2. The impact of the calculation interval (∆t) on the performance of the MDC method needs to be further analyzed to determine the optimal interval size.

### Questions
1. Can you provide the computational resource consumption and algorithmic complexity compared to Baseline-A, B, C, and other SOTA methods? It can help authors better understand the effects of algorithms in devices with limited computational resources.
2. Can you provide the values of hyperparameters such as λ and η in Formula 2?
3. The section on Visualization of MLS is currently difficult to understand. It would be helpful to provide more detailed and accessible explanations to ensure a clear understanding for readers.

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
This paper introduces the Multisize Dataset Condensation (MDC) method, aiming to address challenges associated with dataset condensation in on-device processing scenarios. The main innovation lies in the compression of multiple condensation processes into a single process to produce datasets of varying sizes. The authors combat the "subset degradation problem" with an "adaptive subset loss," ultimately enhancing the representation quality of condensed subsets. Experiments spanning various networks and datasets showcase the method's effectiveness.

### Strengths
Originality: This paper offers a unique approach to dataset condensation, aiming to cater to the specific needs of on-device scenarios. The proposal to compress N condensation processes into one is innovative.
Quality: The "adaptive subset loss" is a novel concept, targeting the "subset degradation problem." The method to select the Most Learnable Subset (MLS) is well-thought-out and complex.
Clarity: The paper is organized logically, and concepts are explained clearly. The use of terms like "adaptive subset loss" and "subset degradation problem" helps the reader understand the core issues being addressed.
Significance: The problem space being tackled (on-device training with dynamic computational resources) is relevant. Solving this issue can have substantial implications for real-world applications.

### Weaknesses
The paper explains three baselines for comparison. Compared to baseline A, the accuracy is not higher. Please explain the reason.
Is it possible to reach Baseline A's accuracies? 
Equation 7 is not that clear. How to calculate the distance between the full dataset and subset?

### Questions
Please see weakness.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel method to compress the condensation process into one process. It is different from the model compression or dataset compression, and this topic sound new to me. The definition of “subset degradation problem” is important in this domain. It will help the researchers to consider the problem. The experiments validate the effectiveness of the propose method.

### Strengths
1. The figures are beautiful and easy to understand.
2. The idea is novel. The process compression sound new to me since it is different from the model compression or dataset compression. 
3. The “subset degradation problem” is practical. Although I have find similar pattern in experiments, it is good to see it is officially and properly presented.
4. The experiment results are promising. It save the computational cost by N times.

### Weaknesses
1. It's not clear what's the purpose of baseline B. It looks like the results are only compared to baseline A and C.
2. It's not clear why the freezing is used in MLS selection. If adaptive is good, why not just use adaptive method to choose the subset?
3. Will the additional loss bring extra computational cost?

### Questions
See weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
