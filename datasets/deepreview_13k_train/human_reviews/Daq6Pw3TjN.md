# Wolf2Pack: The AutoFusion Framework for Dynamic Parameter Fusion

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
\lipsum[1]

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper concentrates on a very interesting problem: how to fuse two types of distinct model parameters pretrained for two different tasks into one model that can simultaneously solve two tasks. By applying permutation on different parameters and unsupervised  learning on unlabeld data, this paper provide an autofusion method and achieves good performance.

### Strengths
Although I am not an expert in this domain, I believe these strengths should be acknowledged:

+ The paper presents a clear and convincing motivation, effectively setting the stage for the proposed work. 
+ There is a notable degree of innovation in the methodology, and the authors have thoroughly reviewed prior approaches, clarifying how their contributions advance the state-of-the-art. 
+ The results achieved by the proposed method are impressive, consistently outperforming baselines across a variety of experimental settings, which underscores its effectiveness. 
+ Additionally, the paper provides detailed theoretical proofs that reinforce the validity and soundness of the approach. 
+ The writing is also commendable, as the paper reads smoothly and is relatively accessible, making it easier for readers to grasp complex concepts. 

Overall, this work shows promise in advancing the field and could be a valuable addition to the literature.

### Weaknesses
 - Line 225: The sentence appears to be incomplete because it begins with a conditional clause (“If we attempt to…”), which typically requires a main clause to complete the thought. In English, when a sentence starts with “If,” it sets up an expectation that there will be a following statement explaining the result, purpose, or consequence of the condition.

- To further demonstrate the effectiveness of the proposed fusion method, more complex tasks and datasets should be considered, such as detection and segmentation tasks with VOC, COCO, or ImageNet datasets, respectively. In this paper, the evaluation is limited to the classification task on two relatively simple datasets (MNIST and CIFAR-10), which is insufficient to validate the robustness of the approach and may render the work less substantial. I will update my final score if the authors can provide more experimental results on some complex tasks and datasets.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces AutoFusion, a framework that fuses distinct model’s parameters (with the same architecture) for multi-task learning. The key idea is to leverage Mena et al. (2018) to make permutation matrix in Re-basin differentiable, thus allowing end-to-end training. Experimental results demonstrate clear improvement over baseline methods.

### Strengths
- It leverages Mena et al. (2018) to make permutation matrix in Re-basin differentiable, thus allowing end-to-end training.
- It achieves clear improvement over baseline methods on MINST and CIFAR.

### Weaknesses
 __Experiments could be improved__

- an analysis of model similarity is needed.
- baselines of fine-tuning the model (trained on one task) on the multi-task jointly are needed. They will provide a good reference even though they are not consider as fair comparisons.
- LoRA fine-tuning could be considered as a fair baseline. As the proposed model learns a permutation matrix per layer, which essentially can be considered as low-rank fine-tuning. Thus, adding comparison to LoRA fine-tuning would provide additional insights.
- In section 4.3, it only compares to weight interpolation on different distributions. Please add comparisons to Git Re-Basin and Zipit (similar to section 4.1)
- experiments on larger dataset (like ImageNet) using transformer based architectures would provide more convincing evidences.

__The paper needs a major revision in writing.__

- The introduction could be improved. It is not usual to have half of the introduction to summarize contributions. It would be better to add more lines on the loss function and unsupervised setup and reduce the space for contributions.

- Figure 1 could be improved. Please adding explanation what each animal represents in the caption.

- Please avoid overusing equations. For example, eq. 1-4 could be in text for better readability. Eq. 7 and 8 could be combined. Eq. 9 and 10 need more explanation about M, U and insights behind. Eq. 11 could be in text.

- Figure 2 is too busy. Math equations make it difficult to read.

- Line 209: “in the absence of pre-trained parameters”. Are parameters in Model A and B pre-trained? This is confusing.

- Line 215: “However, this assumption of high similarity falls apart when the models to be merged are trained for different tasks.” Please demonstrate this by real examples and measure the similarities for different tasks.

- Section 3.1 could be written in a more straightforward manner. It simply leverages differentiable Sinkhorn operator in prior works Mena et al. (2018) and Pena et al. (2023). The error bound is nice to have, but not directly related to the key idea of the paper.

### Questions
please refer to items in weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors aim to merge models independently trained with different initializations. Specifically, the authors employ the Sinkhorn operator to convert the problem of finding a discrete permutation matrix into a differentiable problem that can be directly optimized using gradient descent algorithms.

### Strengths
1. The visualization of the method is good.
2. The application of the Sinkhorn operator is innovative in the field of deep model fusion.

### Weaknesses
1. It would be beneficial to list the number of optimized parameters of each methods.
2. Lacking related work or experimental results to substantiate the claim in lines 215-218 that "However, this assumption of high similarity falls apart when the models to be merged are trained for different tasks. During merging, we must not only align parameters with similar functions but also strive to retain parameters with distinct functions, enabling the fused model to perform various tasks simultaneously."
3. The manuscript lacks a related work section. The introduction is insufficient and fails to provide a comprehensive overview of the existing literature and context for the study. The author could further discuss why the absence of a shared pre-trained initialization poses a challenge to multi-task model merging.
4. It would be beneficial to compare the results of the model merging techniques with the ensemble method and knowledge distillation method, as demonstrated in [1].
5. In lines 351-353, Git Re-Basin archives the best results for Task B, while AutoFusion is highlighted.

### Questions
1. For models trained independently rather than fine-tuning from a shared pre-trained checkpoint, the task-specific models reside in different loss basins. Consequently, linear weight interpolation is expected to yield the worst performance in this scenario. Nonetheless, in Table 4.1, for MLP models on two disjoint MNIST subsets, weight interpolation surpasses both Git Re-Basin and ZipIt. Could the authors please provide an explanation for this?
2. Can the proposed method scale to larger models such as vision transformers used in [1]?

[1] Kinderman et al. Foldable SuperNets: Scalable Merging of Transformers with Different Initializations and Tasks. http://arxiv.org/abs/2410.01483

### Soundness
3

### Presentation
1

### Contribution
2
