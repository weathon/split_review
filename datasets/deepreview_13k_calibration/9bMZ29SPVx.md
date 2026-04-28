# A CLIP-Powered Framework for Robust and Generalizable Data Selection

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Large-scale datasets have been pivotal to the advancements of deep learning models in recent years, but training on such large datasets invariably incurs substantial storage and computational overhead.  Meanwhile, real-world datasets often contain redundant and noisy data, imposing a negative impact on training efficiency and model performance. Data selection has shown promise in identifying the most representative samples from the entire dataset, which aims to minimize the performance gap with reduced training costs. Existing works typically rely on single-modality information to assign importance scores for individual samples, which may lead to inaccurate assessments, especially when dealing with noisy or corrupted samples. To address this limitation, we propose a novel CLIP-powered data selection framework that leverages multimodal information for more robust and generalizable sample selection. Specifically, our framework consists of three key modules—dataset adaptation, sample scoring, and selection optimization—that together harness extensive pre-trained multimodal knowledge to comprehensively assess sample influence and optimize the selection results through multi-objective optimization. Extensive experiments demonstrate that our approach consistently outperforms existing state-of-the-art baselines on various benchmark datasets. Notably, our method effectively removes noisy or damaged samples from the dataset, enabling it to achieve even higher performance with less data. This indicates that it is not only a way to accelerate training but can also improve overall data quality. The implementation will be made publicly available soon.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a CLIP-based multimodal data selection framework that enhances the robustness and generalizability of data selection by leveraging both image and text information. Firstly, the paper trains an adapter to transfer pretrained knowledge to the target data. Then, the similarity between the image and text is used to calculate the sampling score for subset selection. The authors evaluate their results in various popularly datasets, obtaining state-of-the-art results in almost all of them.

### Strengths
1. The method performs more robustly compared to other baseline data selection methods in various popularly datasets.
2. The algorithm is easy to understand and to follow.
3. The writing of this paper is overall great.

### Weaknesses
Some details and motivation should be explained further.
1. The method requires training an adapter with data from the training dataset for data selection. If the noise ratio is high (such as 50%), wouldn't it be a better option not to use an adapter?
2. Does the Actual Selection Costs in Appendix G include the training time for the Adapter? Is the comparison fair?
3. From the ablation experiment, it can be seen that selection loss has a significant impact on the final result. So, what is the sensitivity of this parameter?

### Questions
The authors should take the above questions into consideration: the utilization of the adapter, the comparison, and the parameter.
1. The method requires training an adapter with data from the training dataset for data selection. If the noise ratio is high (such as 50%), wouldn't it be a better option not to use an adapter?
2. Does the Actual Selection Costs in Appendix G include the training time for the Adapter? Is the comparison fair?
3. From the ablation experiment, it can be seen that selection loss has a significant impact on the final result. So, what is the sensitivity of this parameter?

### Soundness
3

### Presentation
3

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
This paper argues that current image data selection methods are limited because they are unimodal. It proposes a multimodal method that uses the category texts from pretrained CLIP to complement images for more robust and generalized data selection. The proposed framework consists of three modules (1) dataset adaptation that integrates image and text adapters to transfer prior knowledge to the target data; (2) sample scoring that calculates the semantic alignment and diversity scores based on the multimodal features, measuring the image-text alignment as well as the local pattern variability; (3) Selection optimization that uses the two scores to select semantically representative and diverse samples, and introduces selection optimization to efficiently identify the ideal data subsets given an expected selection ratio through a multi-objective optimization strategy.

Post discussion comments:
The authors have addressed my concerns. With the additional clarifications and material, the paper is in much better shape. I am keeping my score at 8, which correctly reflects the quality of this work.

### Strengths
The idea of exploiting multimodal features from the CLIP model is interesting and plausible. 

The proposed method is simple, which is a strength in my opinion. 

The method is also efficient and is able to control the alignment, diversity and selection ratio in a multiobjective optimization efficiently. 

The paper is well written and easy to follow. 

The results are good.

### Weaknesses
The proposed method relies on a pretrained CLIP and hence any biases in the CLIP model will propagate to the selected dataset. This is a significant limitation as CLIP models, despite their impressive performance, are known to exhibit biases related to various factors such as demographics and object representations. These biases can lead to skewed data selection, potentially reinforcing existing societal biases or creating new ones in downstream tasks. The method optimizes for alignment and diversity, but it's unclear if this optimization inadvertently amplifies or mitigates biases present in the original dataset. For instance, if certain categories are overrepresented or underrepresented in the CLIP training data, the selection process might exacerbate this imbalance. It is crucial to understand whether the proposed method has any indirect effect on bias in the dataset, and if so, to what extent.

Is it possible to control bias in the dataset or in the subsequent models that are trained on the selected dataset? The paper does not discuss any mechanisms for bias mitigation, which is a critical oversight. The Straight-Through Estimator (STE) used in the selection optimization could potentially cause convergence issues, especially given the non-differentiable nature of the selection process. While the method is presented as efficient, the potential for instability during optimization needs to be addressed. The variable d (sample wise parameter) can be easily confused with d (feature dimension). Consider changing one of them. Also, I don’t see d in Fig. 1. Is “w: N x 1” the sample wise parameter d? Or am I missing something?

The caption of Tab.3 needs to be corrected. You can also merge Tab.3 with Tab.2.

### Questions
See above.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel CLIP-based data selection method leveraging multimodal information with an SGD optimization module. The experiments on several benchmarks show evident improvements over existing approaches.

### Strengths
- Connecting the text and image information for the dataset selection is novel. The proposed CLIP-based method implements the idea well. 
- The SGD-based selection optimization with multi-objective is interesting. It is different from the existing sampling strategies with combinational optimization. 
- Sufficient experimental results show the effectiveness, including different datasets, different settings, and different model architectures.

### Weaknesses
 - The work relies on two adapters to project the CLIP features to the dataset-specific embedding space. The adapter training is based on perfect data. In fact, under the setting of noisy or corrupted data, this ideal data is inaccessible. Therefore, the experiments would be problematic. In Lines 514-515, the authors depict "is essential for effectively transferring the model’s generalization ability to target datasets". It seems the adapter has a large influence on the performance.  Will using the *imperfect* data to fine-tune the adapter degrade the method's effectiveness? This needs to be discussed.

- The class label in this work plays a role as a prototype, while previous work also uses prototypes. They [a] often use the average image features as the prototype and calculate the Euclidean distance between the embedded image and the corresponding prototype, similar to SAS (Eq. 1). Besides, they also use this distance to filter noisy labels [b]. Intuitively, we can use the average image feature to replace the text feature in Eq. 1 of the proposed method. Therefore, it is essential to discuss these results to convey to readers that introducing text is significant.  

- MoSo is NeurIPS'23 rather than NeurIPS'24. Therefore, methods from 2024 have not been compared, e.g., [c]. Besides, some typical methods good at low sampling ratios are missing, e.g., [d].

- Typo: the symbol for the learnable parameter in Figure 2 should be $\mathbf{d}$ rather than $\mathbf{w}$.

### Questions
- The text-image alignment is like using CLIP to measure the difficulty in learning the data. Noisy data or corrupted data are difficult to learn. However, will the selection also filter some important yet difficult data?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a CLIP-powered framework for data selection that addresses the limitations of traditional single-modality data selection methods by incorporating multimodal information. This framework utilizes a pretrained vision-language model (CLIP) to integrate image and text modalities, thereby enhancing data selection accuracy and robustness. The framework is built on three modules: Dataset Adaptation, Sample Scoring, and Selection Optimization. It leverages both semantic alignment and diversity scores to refine sample selection, removing redundant and noisy data to improve training efficiency and performance on benchmark datasets. Experiments demonstrate the method's superior performance in generalization and robustness compared to existing state-of-the-art approaches, especially in noisy environments.

### Strengths
1. Originality: The use of multimodal data via CLIP for data selection is innovative and distinguishes this work from single-modality approaches.
2. Quality: The methodology is backed by rigorous experiments, with a well-defined scoring system for sample selection (SAS and SDS).
3. Clarity: Visualizations effectively depict the advantages of multimodal selection over traditional methods.
4. Significance: This framework has broad applications, as it improves dataset quality and model robustness, potentially benefiting various domains using machine learning.

### Weaknesses
1. Complexity: While effective, the Selection Optimization module’s complexity might hinder its application to extremely large datasets without computational resources.

2. Generality: The framework is primarily tested on vision-based datasets; extending it to text or mixed-modality datasets may reveal further limitations. Future work could focus on enhancing the framework’s versatility across other modalities​

### Questions
1. Could the authors provide more detail on the computational efficiency of the Selection Optimization module for very large-scale datasets?
2. Has the framework been tested on datasets with high modality imbalance (e.g., more text than images), and how does it handle such scenarios?
3. For real-world noisy datasets, could the authors provide more information on how they define and quantify "noisy" samples?

### Soundness
3

### Presentation
3

### Contribution
3
