# Imbalanced data robust online continual learning based on evolving class aware memory selection and built-in contrastive representation learning

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
Continual Learning (CL) aims to learn and adapt continuously to new information while retaining previously acquired knowledge. Most state of the art CL methods currently emphasize class incremental learning. In this approach, class data is introduced and processed only once within a defined task boundary. However, these methods often struggle in dynamic environments, especially when dealing with imbalanced data, shifting classes, and evolving domains. Such challenges arise from changes in correlations and diversities, necessitating ongoing adjustments to previously established class and data representations. In this paper,  we introduce a novel online CL algorithm, dubbed as Memory Selection with Contrastive Learning (MSCL), based on evolving intra-class diversity and inter-class boundary aware memory selection and contrastive data representation learning. Specifically, we propose a memory selection method called Feature-Distance Based Sample Selection (FDBS), which evaluates the distance between new data and the memory set to assess the representability of new data to keep the memory aware of evolving inter-class similarities and intra-class diversity of the previously seen data. Moreover, as the data stream unfolds with new class and/or domain data and requires data representation adaptation, we introduce a novel built-in contrastive learning loss (IWL) that seamlessly leverages the importance weights computed during the memory selection process, and encourages instances of the same class to be brought closer together while pushing instances of different classes apart. We tested our method on various datasets such as MNIST, Cifar-100, PACS, DomainNet, and mini-ImageNet using different architectures. In balanced data scenarios, our approach either matches or outperforms leading memory-based CL techniques. However, it significantly excels in challenging settings like imbalanced class, domain, or class-domain CL. Additionally, our experiments demonstrate that integrating our proposed FDBS and IWL techniques enhances the performance of existing rehearsal-based CL methods with significant margins both in balanced and imbalanced scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a storage sample selection strategy based on feature distance, which evaluates the distance between new data and the memory set to assess the representability of new data. And based on this, contrastive learning loss is introduced to leverages the importance weights computed during memory selection process. Experiments on different online incremental learning setting demonstrate the effectiveness of the proposed method.

### Strengths
1.	The proposed FDBS and IWL is of great importance and applicable for the different online incremental learning setting. 
2.	Adequate and reasonable proof of derivation.
3.	Expensive experiments are conducted in different datasets.

### Weaknesses
1.	The overall paper is well written, however, some details need a little more attention. Such as the title is too long, a little difficult to understand the point of this paper.
2.	From the title and abstract of the paper, it looks like your method is supposed to work for all settings of online incremental learning, so it should achieve the best performance so far for different settings, but for experiments with balanced datasets, it looks like OnPro[1], GSA[2], and OCM[3] have achieved much better experimental results with the same resnet18 and M=5K methods, so you should add the latest methods into it to make your experiments more convincing

### Questions
Please refer to the strengths and weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a online Continual Learning (CL) algorithm named Memory Selection with Contrastive Learning (MSCL), aiming to adaptively learn and retain knowledge in dynamic environments with imbalanced data. The proposed framework, MSCL, addresses the challenges arising from changes in correlations and diversities of data by continually adjusting previously established class and data representations. The core of MSCL lies in its two main components: Feature-Distance Based Sample Selection (FDBS) and Built-in Contrastive Learning Loss (IWL). The method has been tested on various datasets such as MNIST and Cifar-100. The results show that in balanced data scenarios, MSCL either matches or outperforms leading memory-based CL techniques, marginally. Additionally, the integration of FDBS and IWL enhances the performance of existing rehearsal-based CL methods in both balanced and imbalanced scenarios.

### Strengths
* Novel framework for online continual learning. The paper introduces Memory Selection with Contrastive Learning (MSCL), a novel framework specifically designed for online continual learning in dynamic environments with imbalanced data, shifting classes, and evolving domains.

* The paper tackles real-world challenges associated with non-stationary data streams, such as imbalanced data across classes and domains, and the need for ongoing adjustments in class and data representations.

### Weaknesses
 * Lack of visualizations that show how data points are distributed in the feature space leaves the reader without a clear, visual understanding of how the Feature-Distance Based Sample Selection (FDBS) method operates.

* There is no discussion of the computational cost of the algorithm. 

* Lack of discussions on the framework's applicability and performance in large-scale scenarios, which remain unaddressed in the current version of the paper.

### Questions
* There is no discussion of the computational cost of the algorithm. There are a few steps in the framework including: 1. Memory Management, 2. Feature Space Mapping, 3. Distance Calculation, 4. Importance Weight Calculation that can add to the computational cost hence overhead of the framework at each step. For example, the FDBS method involves managing a memory set, which includes calculating distances in the feature space and selecting representative samples. The size of the memory set and the dimensionality of the feature space can influence the computational cost and runtime efficiency for this step. The same applies to other steps.

* The authors mentioned Split ImageNet-1k in section 5. Experiment as one of the benchmarks but there are no mention of this dataset in the result section. 

* The above comment raises another question: The authors acknowledge the substantial difficulties encountered when dealing with imbalanced data across various classes and domains, citing works by Wu et al. (2019) to underscore this challenge. However, the evaluations suffices to mid-sized datasets. This raises questions about the framework's applicability and performance in large-scale scenarios, which remain unaddressed in the current version of the paper.

* By continuously refining the feature space and adjusting the memory set based on incoming data, the method aims to adapt to changes in the data distribution. However, the paper could provide more details on how the method performs in scenarios with rapid changes in data distribution and whether there are any limitations in its adaptability.

* Lack of visualizations that show how data points are distributed in the feature space leaves the reader without a clear, visual understanding of how the Feature-Distance Based Sample Selection (FDBS) method operates.

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
The paper introduces a novel Continual Learning (CL) algorithm, Memory Selection with Contrastive Learning (MSCL). It focuses on adapting to imbalanced data, shifting classes, and evolving domains. MSCL uses Feature-Distance Based Sample Selection (FDBS) to assess the representability of new data in memory, maintaining awareness of evolving inter-class similarities and intra-class diversity. Additionally, it incorporates a contrastive learning loss (IWL) that encourages similar class instances to be closer while pushing different class instances apart. Experimental results show that MSCL excels in challenging scenarios, enhancing existing CL methods in both balanced and imbalanced data settings.

### Strengths
1. This paper considers the setting of IMBALANCED DATA ONLINE CONTINUAL LEARNING that most online continual learning methods do not address.
2. Experimental results indicate that the proposed feature-distance-based sample selection and IWL are effective.
3. This paper conducts extensive experiments.

### Weaknesses
1. The proposed method appears to be more general rather than specifically tailored to the task of online continual learning with imbalanced data. The core mechanisms, such as feature-distance based sample selection and contrastive learning, are not inherently designed to address the unique challenges of imbalanced data streams in an online setting. While these techniques can be beneficial, the paper lacks a clear explanation of how they are specifically adapted or optimized for imbalanced online continual learning, rather than being a general approach applicable to various scenarios.
2. Computing the distance of all samples at each time step is time-consuming, which may not be practical for efficient online continual learning. The computational overhead of calculating feature distances for all samples in the current batch against all samples in the memory buffer at each step could become a bottleneck, especially with large datasets or limited computational resources. This could hinder the real-time applicability of the method in practical online learning scenarios.
3. The method focuses on identifying samples with high intra-class variance and high inter-class similarity, potentially causing the model to overemphasize challenging extreme cases, whereas most samples exhibit low intra-class variance and high inter-class variance (class dissimilarity). This selection strategy might lead to a memory buffer that is not representative of the overall data distribution, potentially biasing the model towards outliers and neglecting the more common and representative samples. This could negatively impact the model's generalization performance on typical data instances.
4. Typically, continual learning experiments provide accuracy changes for each incremental step. It would be beneficial to observe the accuracy changes for each task. This would provide a more granular understanding of the model's performance and its ability to retain knowledge of previous tasks while learning new ones. The current evaluation lacks this level of detail, making it difficult to assess the model's behavior at each stage of the continual learning process.
5. The baseline methods used for comparison seem somewhat outdated, with the most recent one dating back to 2022. The field of continual learning is rapidly evolving, and the use of older baselines might not provide a fair comparison against the current state-of-the-art methods. This makes it difficult to ascertain the true novelty and effectiveness of the proposed method in comparison to contemporary approaches.

### Questions
typos. As a result, they face significant challenges in presence of imbalanced data in class and domain Wu et al. (2019)Liu et al. (2022). Ye et al. (2022) introduce a novel approach for quantifying dataset distribution shifts across two distinct dimensions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
