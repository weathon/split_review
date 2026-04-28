# Jointly-Learned Exit and Inference for a Dynamic Neural Network

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
Large pretrained models, coupled with fine-tuning, are slowly becoming established as the dominant architecture in machine learning. Even though these models offer impressive performance, their practical application is often limited by the prohibitive amount of resources required for \textit{every} inference. Early-exiting dynamic neural networks (EDNN) circumvent this issue by allowing a model to make some of its predictions from intermediate layers (i.e., early-exit). Training an EDNN architecture is challenging as it consists of two intertwined components: the gating mechanism (GM) that controls early-exiting decisions and the intermediate inference modules (IMs) that perform inference from intermediate representations. As a result, most existing approaches rely on thresholding confidence metrics for the gating mechanism and strive to improve the underlying backbone network and the inference modules. Although successful, this approach has two fundamental shortcomings: 1) the GMs and the IMs are decoupled during training, leading to a train-test mismatch; and 2) the thresholding gating mechanism introduces a positive bias into the predictive probabilities, making it difficult to readily extract uncertainty information. This leads to significant performance improvements on classification datasets and enables better uncertainty characterization capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an early-exit dynamic neural network architecture, JEI-DNN, that augments a backbone with lightweight, trainable gates and intermediate classifier that are jointly optimized. The gates are trained through a surrogate binary classification task, focusing on the optimization for assigning the most cost-effective early-exit classifier for each input. The results are presented on the cifar and svhn datasets for the T2T-ViT backbone.

### Strengths
- Analysing the conformal intervals for the early exiting classifiers is interesting and it's promising to see the proposed method yields better uncertainty characterisation.
- The ablation study in 8.6 clearly shows the merits of learnable GMs versus other design choices.
- Figure 2 a) and b) very clearly show the early exiting patterns for the method and competing approaches.

### Weaknesses
 - It is unclear what the major contribution of the paper is. The use of learned early exiting gates and intermediate classifiers, trained jointly with the backbone is common practice for many early exiting architectures. After all the approximations described in 4.1, the loss term for the gating modules turnes into the common practice of summing the losses of independent binary early-exiting classifiers. The main task loss is similarly aligned with prior work from Han et al. (2022b).

- Constructing surrogate binary targets for the learned gates is also common, e.g. FrameExit by Ghodrati et al. CVPR 2021.

- Figure 2a) The fact that samples do not exit at all from the first few early exiting layers in JEI-DNN is puzzling and I am wondering if it is due to the choice of specific hyperparameters that prevent early exiting from these layers. As can be seen, the accuracy of the IM at layer 5 & 6 is far higher that the overall performance. It is conceivable that a good accuracy higher than the green dashed line is still achievable by the earlier classifiers at least for a proportion of samples. Is there any hyperparamer that could potentially give more control into the exiting pattens of JEI-DNN?


- All the results in the paper are limited to the T2T-ViT backbone. The authors should show the efficacy of their method for a larger variety of backbones, preferably to models that are established in the early exiting literature such as MSDNet, DenseNet, etc.

- Comparison of the accuracies among T2T-Vit and MSDNet architectures in Fig 5 seem unfair. Most of the gain in accuracy comes because of the more powerful transformer-based backbone and not because of the efficacy of the early exiting approaches. In fact, MSDNet and RANet show more robust early exiting results compared to the results reported for T2T. E.g. MSDNet retains the original accuracy of the model after almost 50% compression. The performance of the proposed JEI-DNN approach in comparison drops very rapidly even with 25% compression.

- The method is only evaluated on three small-scale datasets: CIFAR10 & 100, SVHN. The authors should consider expanding the evaluation to ImageNet.

### Questions
- The assumption that a sample exited at a gate at layer $l$ should also exit from any late stage gate seems against the prevalent view of $overthinking$:
"Overthinking is computationally wasteful, and it can also be destructive when, by the final layer, a correct prediction changes into a misclassification." by Kaya et al. ICML 2019.
How did you make this assumption?

### Soundness
2 fair

### Presentation
2 fair

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
This submission introduces JEI-DNN, an early-exit model approach that can be applied on top of off-the-shelf backbones for image classification. The proposed methodology appends light-weight classifiers and trainable gates along the depth of a frozen backbone model and jointly optimises them with a custom and insightfully designed loss function. As a result, a better speed-accuracy trade-off is provided compared to several baselines considering both learnable and non-parametric exit policies, while offering improved prediction uncertainty.

### Strengths
-The submission studies a very interesting problem, focusing on the emerging inference setting of input-dependent computation via early-exiting. 

-The manuscript offers a beautiful formulation of the examined task and provided solution, that can benefit the community as a principled definition of early-exit models. Additionally, the discussion of the manuscripts findings presents useful insights that can guide practitioners and inspire future research in the direction of EE models.

-Most design choices in the adopted solution are well motivated and backed by practical insights.

-The presented results indicate that the proposed method is effective and achieves a superior speed-accuracy trade-off to a wide set of baselines approaches.

### Weaknesses
 -A few technical aspects of the paper remain unclear. Specifically, the use of the min operator between two terms in Eq.8 is not fully justified in the manuscript, nor experimentally verified by a relevant ablation. The manuscript states that the min operator is used to ensure that the sum of probabilities does not exceed 1, however, it does not explain why a simple normalization (dividing by the sum) cannot be used, or why the min operator is the best choice among other possible alternatives. The lack of justification for this specific design choice weakens the overall contribution.

-The proposed methodology is only evaluated on frozen-backbone CNNs. Although this a practical sub-category of EE-models, further evaluation on end-to-end EE models (jointly training the backbone and exits), which are shown to achieve superior speed-accuracy trade-off would increase the contribution of the paper. The current evaluation limits the applicability of the proposed method to a specific scenario, and it is not clear how the method would perform in a more general setting.

-Although the proposed approach is compared with a wide set of baseline, ImageNet experiments are omitted, rendering the presented results less convincing. The lack of experiments on ImageNet, which is a standard benchmark for image classification, makes it difficult to assess the effectiveness of the proposed method in a more realistic and challenging scenario. The presented results are therefore less compelling and the generalizability of the method remains unclear.

### Questions
1. What is the role of the second (1-sum) term in Eq.8 ? Potentially, its use could be validated through an ablation experiment.

2. How would the method perform on end-to-end trainable early-exit models? Would the training of the gates affect the convergence of the overall model? Should the method be considerably adjusted to be applicable in this setting? 

3. Is the proposed approach equally effective on the most commonly used ImageNet-1K benchmark?

Minor Comments:
Sec3: The term "IC-Only training" is widely used in the community (including the cited survey paper) to denote "Intermediate-classifier only training", rather "than inference cost-only training" as stated in the manuscript

Post-Rebuttal Edit: Following the clarification on Q1 and additional results included in the updated version of the manuscript for Q2 and Q3, I am increasing my score from 6(=BA) to 8(=A).

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to jointly learn the backbone parameters and the exiting strategies in a dynamic multi-exit model. Intermediate classifiers are constructed in a pre-trained backbone, and exiting gates are built as a binary classification head. The joint learning problem is formulated as a bi-level optimization problem. Experiments on several small datasets demonstrate that 1) a better trade-off between accuracy and efficiency is achieved; and 2) a better estimation of uncertainty (calibration of classification confidence) is achieved.

### Strengths
1. The studied problem is of great interest;

2. The motivation is clear;

3. The proposed method is technically sound;

4. The literature review is comprehensive;

5. The experiments show the effectiveness in both accuracy-efficiency tradeoff and calibrated confidence.

### Weaknesses
1. **Lack of experiment on more advanced architectures**. Why did the authors select a T2T-ViT to construct the early-exiting model? Straightforwardly, the joint learning procedure can be directly applied in mature multi-exit models, such as the compared MSDNet, RANet, and the cited Dynamic Perceiver.  To my understanding, Dynamic Perceiver is the most recent work in this field, achieving SOTA performance in dynamic early exiting. The choice of T2T-ViT, while a valid transformer, does not showcase the method's applicability to state-of-the-art dynamic exiting architectures. The paper should demonstrate the method's effectiveness when integrated with architectures specifically designed for early exiting, which often incorporate specialized mechanisms for feature sharing and exit placement.
    
2. **Overclaiming contributions**. Based on the above point, the contribution of this paper should not include a new architecture. It is recommended to summarize the contribution as the joint learning procedure only. I believe this would already be significant enough if the learning method is shown effective on more SOTA architectures and on the ImageNet dataset. The current framing of the contribution implies an architectural novelty, which is not supported by the presented experiments. The core contribution lies in the joint learning strategy, and this should be the primary focus.

3. **Lack of experiments on ImageNet**. To my understanding, the learning approach does not need to be applied in a downstream task on the toy small-scale datasets. Experiments on ImageNet would be more convincing. The experiments on small datasets, while useful for initial validation, do not adequately demonstrate the scalability and effectiveness of the proposed method on large-scale, real-world datasets. ImageNet, with its large number of classes and images, is a standard benchmark for evaluating image classification models, and its absence is a significant limitation.

4. **Presentation**. It is recommended to use figures to clearly show the motivation and the method pipeline. The current presentation lacks visual aids to clarify the method's motivation and implementation details. A clear diagram illustrating the joint learning process and the interaction between the backbone, intermediate classifiers, and exiting gates would greatly enhance the paper's clarity.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper describes a novel mechanism to add trainable early exits (EEs) to a pre-trained neural network. It addresses a common concern of the majority of previous works, where the train procedure and the test procedure of the EEs were mismatched (e.g., jointly training all the early exits during training while thresholding their outputs during test). 

In the proposed framework, each EE is associated to a probabilistic gate, and everything is trained jointly with a bilevel optimization problem, where the outer problem is defined over the gates and the inner problem over the EEs. The system is trained to also minimize execution time by training the gates to select the first exit having good accuracy for each pattern.

They also propose a novel conformal prediction (CP) strategy for EE networks, where different thresholds are selected for each exit (since each exit will observe a different subset of values at inference times).

### Strengths
The topic of the paper is important, since the method described can be used to reduce inference time (hence, power consumption) of any pre-trained model. The paper is generally well written and easy to read, although some additional visualization could be useful (see below). Results are relatively comprehensive, although I am concerned by the transfer learning from a large dataset (ImageNet) to a smaller, fundamentally similar dataset (CIFAR, also see below).

### Weaknesses
I find it hard to fully understand the method before reading through the entire paper. In particular: (a) the abstract has no mention of the paper's contributions; (b) the "Contributions" also does not explain how the method works; (c) there is no visual schema of the model; (d) some important details are described very late, for example "Gate design" is part of the experimental section but it is a crucial design decision. Overall it is understandable, but I think some minor reorganization and some additional visual descriptions (maybe a shortened pseudo-code?) can significantly help the reader.

On the novelty, I think a few methods could be added and discussed more. For example, the zero-time waste model (cited in the paper) has a geometric ensemble of the early exits which is very similar to their gating probability, if I understand correctly. As another example, differentiable branching (https://ieeexplore.ieee.org/document/9054209) considers a trainable exit strategy that also combines the EEs and that can be trained end-to-end with the rest of the network. Some of these methods can be also added to the experimental comparison.

Concerning the last point, I am curious about transfer learning from a large, generalist dataset (ImageNet) to a small dataset which is basically in the same domain (CIFAR-10). Would it not make more sense to test directly on ImageNet? Improvements would be directly comparable with the original pre-trained model.

### Questions
Apart from the topics discussed above, I have a general question about the bilevel task. Can you clarify why this is needed? There are techniques to train probabilistic blocks (e.g., reparameterization, score function estimators), which would allow to train all blocks simultaneously, or I am missing something? Also, what is the overall training time of your model compared to the alternatives?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
