# Training Over a Distribution of Hyperparameters for Enhanced Performance and Adaptability on Imbalanced Classification

- Decision: Reject
- Scores: 5, 3, 5, 6, 6

## Abstract
Although binary classification is a well-studied problem, training reliable classifiers under severe class imbalance remains a challenge. Recent techniques mitigate the ill effects of imbalance on training by modifying the loss functions or optimization methods. We observe that different hyperparameter values on these loss functions perform better at different recall values. We propose to exploit this fact by training one model over a distribution of hyperparameter values--instead of a single value--via Loss Conditional Training (LCT). Experiments show that training over a distribution of hyperparameters not only approximates the performance of several models but actually improves the overall performance of models on both CIFAR and real medical imaging applications, such as melanoma and diabetic retinopathy detection. Furthermore, training models with LCT is more efficient because some hyperparameter tuning can be conducted after training to meet individual needs without needing to retrain from scratch.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper is targeted at addressing the imbalanced image classification task. It reveals that the performance of existing methods trained using fixed hyper-parameters is sensitive to hyper-parameters, namely the highest precision is achieved with different hyper-parameter values at different recall. Targeted at learning a single model which can achieve consistently high performance across recall, it introduces the loss conditional training strategy which is originally proposed for image compression into image classification. This enables the hyper-parameters to flexibly tuned during inference. Extensive experiments on a few binary image classification datasets demonstrate the proposed method improves baseline methods focal loss and vector scaling loss consistently.

### Strengths
1. The paper presents a novel integration of loss conditional training (LCT) within the context of imbalanced image classification. While LCT itself is an existing technique, its application in this specific domain brings new insights, particularly in handling varying hyper-parameters to improve model adaptability and performance on diverse datasets.
2. The research demonstrates rigorous experimental validation. By applying the proposed method across multiple binary image classification datasets, the paper effectively highlights its potential in improving baseline performances. The objective function is thoughtfully designed, focusing on minimizing classification loss over a hyper-parameter distribution, which is both innovative and practical.
3. The paper is generally well-structured and presents its contributions clearly. The explanation of the objective function and its rationale is straightforward, aiding readers in understanding the methodology.
4. Given the widespread challenges posed by imbalanced datasets in image classification, the method’s capability to flexibly adapt post-training, as well as its empirical success on standard benchmarks, underscores its relevance and significance in the field.

### Weaknesses
1. While the application of LCT to imbalanced classification is a reasonable extension, the core technique—LCT—is not novel. The contribution could be viewed as incremental, leveraging existing methodologies without substantial innovation.
2. The choice of baselines seems outdated. To substantiate the method's efficacy, comparisons with more recent state-of-the-art techniques should be included：
SuperDisco: Super-class discovery improves visual recognition for the long-tail, cvpr2023
Balanced product of calibrated experts for long-tailed recognition, cvpr2023
Constructing balance from imbalance for long-tailed image recognition, eccv2022
3. The paper lacks sufficient details on the FiLM (Feature-wise Linear Modulation) module, which is critical for reproducibility. A clearer explanation and inclusion of implementation specifics are necessary. For instance, the paper does not specify the exact architecture of the FiLM layers, such as the number of layers, the activation functions used, or the dimensionality of the modulation parameters. This lack of detail makes it difficult to replicate the results.
4. The requirement for hyper-parameter input during inference could pose practical challenges. Providing a guideline for optimal hyper-parameter settings would be beneficial for practitioners and researchers aiming to apply this method. The paper does not offer any guidance on how to select the hyper-parameter during inference, which is a critical practical consideration. Without clear guidelines, users may struggle to effectively utilize the proposed method.
5. The method's inability to outperform VS-SAM in several settings is concerning. This raises questions about the generalizability and robustness of the approach. Furthermore, the observation from Table 4, where LCT without FiLM underperforms compared to the baseline, warrants a deeper analysis to understand the underlying reasons. The paper does not provide a sufficient explanation for why the FiLM layers are so critical to the performance of LCT, and why their absence leads to a degradation in performance compared to the baseline.

### Questions
1. Could the authors clarify how their approach extends beyond a straightforward application of LCT? Highlighting specific innovations or modifications would help in assessing the paper’s originality.
2. Could the authors provide more details on the FiLM implementation? 
3. The method relies on hyper-parameter inputs during inference. What guidelines or heuristics do the authors recommend for setting these parameters effectively?
4. The results in Table 4 indicate that without FiLM, LCT performs worse than the baseline. Could the authors provide an analysis of why FiLM is critical and why its absence degrades performance? Similarly, why does the method not consistently outperform VS-SAM?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper presents a method for training models on imbalanced datasets by using a distribution over loss hyperparameter values instead of a single value. The hypothesis is that by conditioning the model on different values of hyper-parameters, the model leads to different functions and thus, using a distribution of hyper-parameters leads to a more robust model. The method is evaluated on CIFAR and APTOS datasets.

### Strengths
* The paper is well-written, and the motivation is clear.

* The method is well-motivated and learning on imbalanced dataset is important.

### Weaknesses
 * Only binary classification is studied in the paper. It is not clear if the proposed method will work on multi-class classification or unsupervised learning.
* The datasets used in the experiments are very small. Experiments on more large-scale datasets are required (e.g. ImageNet).
*Only focal loss and VS loss are used as baselines. More extensive comparison against Sota methods for learning imbalanced datasets and long-tail learning.
* Hyper-parameter search space for focal loss and VS loss is very small, making the comparison somewhat unfair.
* It is not clear how pdf for sampling $\lambda$ is defined in section 4.3.
* Authors should run the method on different kinds of learning problems in different domains.
* Improvement on CIFAR and SIIM-ISIC datasets ARE very minor.
* Standard deviation is not mentioned in the result table. How many different seeds were used for each section?

### Questions
Why was the model trained for 500 epochs on cifar (section 5.1)? That's excessive for CIFAR.

Why do you need gradient clipping? Is the loss unstable?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper focuses on imbalanced classification. Authors focus on the hyper-parameter choices of imbalanced loss function and find no optimal solution for existing approach. Instead, the proposed method treating these hyper-parameters as a distribution and sample from it, combine with original data sample input as an additional input for training.

### Strengths
The idea of hyper-parameter sensitivity in imbalanced learning is new.

### Weaknesses
 - How is SAM trained with LCT? Since $\lambda$ is associated with each data sample, but SAM is an optimizer?
- How is $P_\Lambda$ calculated? Is it a small network or it is just a pre-defined distribution?
- Line 248-253 is vague in details. How is FiLM compute $\mu$ and $\sigma$? Does it just take one $\lambda$ in and output 2 values? Because without any constraints, these two values are directly applied on activation for linear transformation.
- I am still unclear about the hyper-parameter setting during training and testing. The paper mentions that each data sample is associated with a $\lambda$ sampled from $P_\Lambda$ during training, but it is not clear how this is handled during testing. Are multiple inferences performed with different $\lambda$ values, or is a single $\lambda$ chosen? This lack of clarity makes it difficult to understand the practical implications of the method.
- The experimental results lack sufficient explanation. For example, the paper does not provide a clear rationale for why LCT performs better or worse than other methods in specific scenarios. A more detailed analysis of the results is needed to understand the strengths and weaknesses of the proposed approach.

### Questions
- I am confused by LCT training part. My understanding is that LCT will point out the best hyper-parameter after training, and in inference we just use the best combination. But Sec. 4.3 claim we still need to evaluate with multiple values $\lambda$. So LCT is more similar to meta-learning, through its training paradigm, the model can generalize better?
- Given there is an underlying distribution over these hyper-parameters, could a VAE approach work as well?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper extends the Loss Conditional Training framework to address class imbalance issues, based on the observation that varying hyperparameters in the loss function results in different performance across evaluation metrics. The proposed method shows good performance and desirable properties on several datasets.

### Strengths
The paper extends the Loss Conditional Training framework to binary classification with class-imbalance setting. The extension is simple but seems useful.

### Weaknesses
1. It is unclear how the distribution of lambda during training and the lambda values to use in inference are chosen. More discussion is needed.

2. The proposed method seems a simple extension of existing method (Dosovitskiy & Djolonga, 2020).

3. The discussion on more general insight about the method is still unsatisfactory (when the proposed method will and will not work).

### Questions
1. Why does the paper focus solely on binary classification? Could the proposed method be extended to multi-class classification? What about class-balanced scenario?

2. The paper uses Focal Loss and VS Loss as examples of successful applications of the LCT framework. Why were only these two loss functions chosen? Are there more generalizable insights on which types of losses are or are not applicable? 

4. Have the authors considered alternative methods for conditioning the model on lambda (lines 248-253)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose a new approach to training binary classification models in severely imbalanced situations, using loss-conditioned training (LCT) to train a single model on a hyperparameter distribution, which consistently improves ROC curves and various other metrics. In addition, training models using the proposed approach are more efficient because some hyperparameter tuning can be done after training to suit individual needs without having to retrain from scratch. The proposed algorithm achieves good performance on both natural and medical images.

### Strengths
The research addresses a significant topic in the field by proposing a method to solve the imbalance problem in binary classification tasks. The proposed approach effectively tackles this challenge, as evidenced by comprehensive and valid experiments conducted across multiple datasets. The method demonstrates promising results, outperforming a large number of comparison methods. Overall, the study offers a valuable contribution by providing a robust solution to a prevalent issue, supported by thorough experimentation and strong comparative performance.

### Weaknesses
The authors propose training the model at multiple hyperparameter values, aiming to approximate the best performance of multiple models trained using a single loss function. However, this approach may be unfair to other baseline methods. It is unclear how the hyperparameters for the baseline methods were selected in the experiments. Providing details on this selection process would help ensure a fair comparison.

The novelty of the proposed method is not very clear. While the authors demonstrate the impact of optimal hyperparameters on model performance through a series of intuitive experiments, it remains uncertain whether the performance gains are simply due to increased randomness during training. Clarification on this point would strengthen the contribution.

Additionally, it appears that the LCT algorithm is only applicable to binary classification tasks. In real-world scenarios, multi-class classification is more common, and binary classification may be too simplistic for addressing imbalanced problems. The authors should consider extending their method to multi-class classification to verify its effectiveness in more complex settings.

The comparison methods used in the experiments seem to be somewhat outdated, such as Focal Loss and VS Loss. Including comparisons with more advanced algorithms like Gaussian Clouded Logit (GCL) Loss [1] and Dual Focal Loss [2] would enhance the study’s relevance and rigor.

The performance improvements reported seem negligible, and it is not clear whether they are attributable to the hyperparameter settings. Notably, the proposed LCT method appears to improve VS Loss more significantly, but the improvement over Focal Loss is minimal. An explanation for this discrepancy would be valuable.

Since the models’ results are based on multiple runs, performing statistical tests to compare the performance of different algorithms and reporting the standard deviations would provide more robust evidence of the method’s effectiveness.

Finally, information about the computational requirements for training the proposed method and its algorithmic complexity would be beneficial. This would help assess the practicality of implementing the method in real-world applications.

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3
