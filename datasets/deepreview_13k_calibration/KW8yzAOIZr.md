# To Tackle Adversarial Transferability: A Novel Ensemble Training Method with Fourier Transformation

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Ensemble methods are commonly used for enhancing robustness in machine learning. However, due to the ''transferability'' of adversarial examples, the performance of an ensemble model can be 
seriously affected even it contains a set of independently trained sub-models. To address this issue, we propose an efficient data transformation method based on a cute  ''weakness allocation'' strategy, to diversify non-robust features.
Our approach relies on a fine-grained analysis on the relation between non-robust features and adversarial attack directions.
Moreover, our approach enjoys several other advantages, e.g., it does  not require any communication between sub-models and the construction complexity is also quite low.
We  conduct a set of  experiments to evaluate the performance of our proposed method and compare it with several popular baselines. The  results suggest that our approach can achieve significantly improved robust accuracy over most existing ensemble methods, and meanwhile preserve high clean accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a Fourier-based ensemble training method to counter adversarial transferability by diversifying non-robust frequency components across sub-models. Using random noise and targeted attack transformations, the method achieves improved robustness and competitive accuracy on datasets like CIFAR-10, outperforming current ensemble techniques.

### Strengths
- The use of Fourier transformations to manipulate frequency components for adversarial robustness is innovative and less explored in ensemble methods.
- The proposed method addresses the transferability of adversarial attacks more effectively by diversifying non-robust features across sub-models.
- Unlike simultaneous training methods, the approach’s independent training of sub-models reduces GPU memory requirements and simplifies the training pipeline.

### Weaknesses
 - The proposed targeted-attack transformation method, while effective, introduces a layer of complexity to the training pipeline. By replacing specific non-robust frequency components in the data with adversarially targeted features, the transformation becomes computationally intensive and intricate to implement, especially when scaling to larger datasets or real-time applications. This additional complexity may limit the ease of adoption for other researchers or practitioners looking to implement this technique without substantial computational resources.
- The experiments are primarily conducted on smaller architectures, like ResNet-20, with limited exploration on larger or more complex models. Without extensive testing across a variety of architectures, it’s unclear whether the proposed Fourier-based transformations are universally effective or if they are more suitable for specific model types.

### Questions
Refer to the weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Ensemble training is a commonly used technique to enhance a model's adversarial robustness. However, recent studies suggest that this approach may not be as effective, as adversarial examples can often affect multiple sub-models due to a phenomenon called "transferability." This limitation arises because all sub-models are typically trained on the same dataset, leading them to share similar vulnerabilities. To address such issue, the author propose an effective data transformation framework to improve the diversity of training
data used by different sub-models for robust ensemble training. In the end of the paper, they present empirical results demonstrating the effectiveness of their method against common adversarial attacks, while also maintaining clean accuracy.

### Strengths
- The proposed framework is innovative, intuitively reasonable, and easy to understand. 
- The method comes with solid theorical backing
- The experiments are comprehensive and well-supported their findings

### Weaknesses
 - The paper's readability is poor. I’ve provided specific feedback in the following sections and strongly recommend improvements in clarity and structure.
- The ensemble learning with proposed method still shows limited competitiveness with adversarial training, which restricts its practical applicability. Although the appendix shows that this method maintains higher clean accuracy than popular adversarial training (AT) methods, it still falls significantly short in robust accuracy compared to these approaches.


### Questions
Here are few questions and suggestion I want to provided for your paper:

1. No detailed explanation of the feature extractor. In Definition 3.1, you provide a detailed definition of what a "useful detail extractor" is. However, the feature extractor itself is only given as $θ: X → \mathcal{R}^k$. Based on the information provided, I can't see how it differs from a standard classification model. I hope you can add more details to improve the readability of the paper

2. $\hat{y}$ is not an appropriate mathematical symbol in my opinion. $\hat{y}$ is typically used to denote the prediction of y by convention, but in your paper, you are using it to denote the one-hot vector of y, which is quite confusing.

3. In your Definition 3.2, I am confused by the second formula you provided. The first formula indicates that the feature extractor is robust if the expectation $ y^t \cdot \theta(A(x)) > \frac{1}{k} $, but the second formula does not contain $y^t$ at all. I'm not sure whether I misunderstood your formula or if there is a mistake here.

4. The format of your formula 8 doesn’t seem correct to me. The equation is broken in the middle, leaving part of it followed after the plain text and the other part in equation mode.

5. I am curious how you find the "high-amplitude frequency features" from your image. I think I am having this question since I didn't understand how your feature extractors work.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes an ensemble training approach to tackle the adversarial transferability problem by leveraging Fourier transformation and a weakness allocation strategy to diversify non-robust features across sub-models. The authors introduce a novel data transformation framework involving frequency selection and frequency transformation, aiming to improve the ensemble model’s robustness against adversarial attacks without sacrificing clean accuracy. Experimental results show that their method, particularly the FDT-hybrid, outperforms several existing ensemble methods in robust accuracy on benchmark datasets like CIFAR-10 and CIFAR-100​.

### Strengths
1. The paper addresses a critical challenge in adversarial machine learning, focusing on enhancing ensemble robustness without excessive overhead.
2. The frequency-based approach for diversifying non-robust features is innovative and leverages insights from signal processing.
3. Experimental results are thorough, showcasing improved robustness across various adversarial attacks and comparison with multiple baseline methods.

### Weaknesses
1. The paper’s complexity may hinder reproducibility, especially given the intricate weakness allocation and frequency transformation processes. The specific implementation details of the frequency selection and transformation, particularly how the Fourier transform is applied and how the frequency components are manipulated, are not sufficiently detailed. This lack of clarity makes it difficult for other researchers to replicate the results without significant effort in reverse-engineering the methodology.
2. The dependency on specific frequency thresholding could limit adaptability across different datasets or tasks. The paper does not provide a clear methodology for determining optimal frequency thresholds for new datasets. The chosen thresholds, τ1 and τ2, are critical hyperparameters, and the lack of a systematic approach to setting them could lead to suboptimal performance when applying the method to datasets with different statistical properties than those used in the experiments. The paper needs to address how these thresholds should be adapted to datasets with different image resolutions or feature distributions.

### Questions
1. Could the authors elaborate on how the choice of frequency thresholds (τ1 and τ2) affects robustness and clean accuracy?
2. Is the computational efficiency of the proposed approach scalable to larger models or more complex datasets, given the Fourier transformations applied?

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
4

### Summary
This paper introduces a data transformation method aimed at improving the adversarial robustness of ensemble models. Instead of reducing the influence of non-robust features, the authors propose to reduce the transferability of attacks by increasing the diversity of non-robust features. The robust and non-robust features are identified by frequency selection. The weakness set is allocated to sub-models for training to increase diversity. Through the experiments on various datasets, the results demonstrate the superiority of the proposed method over other baselines.

### Strengths
1. This paper is well-written and easy to follow.
2. The motivation of diverse non-robust features seems natural for a better trade-off between clean and robust accuracy.
3. The comparison with other baselines shows the effectiveness of the proposed method.

### Weaknesses
1. The motivation of amplitude-based selection is not well explained. There is no theoretical or empirical evidence to support this design in this paper.
2. There is no ablation study to verify the effectiveness of all the components, such as weakness set allocation, amplitude-based selection, new dataset construction, etc.
3. The results of baselines seem strange. For example, the results in Table 2 differ from those in Table 1 of TRS.

### Questions
1. Please clarify the motivation of amplitude-based selection.
2. Please provide more ablation studies of the proposed method.
3. Please clarify the difference in the result in Table 2.

### Soundness
2

### Presentation
3

### Contribution
2
