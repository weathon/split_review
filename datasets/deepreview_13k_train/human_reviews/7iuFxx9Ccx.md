# Resource Efficient Test-Time Training with Slimmable Network

- Decision: Reject
- Scores: 5, 6, 5, 8

## Abstract
Test-Time Training (TTT), an innovative paradigm for enhancing a model's generalization in a specific future scenario, commonly leverages self-supervised learning to adapt the model to the unlabeled test data under distribution shifts. However, previous TTT methods tend to disregard resource constraints during the deployment phase in real-world scenarios and have two fundamental shortcomings. Firstly, they are obligated to retrain adapted models when deploying across multiple devices with diverse resource limitations, causing considerable resource inefficiency. Secondly, they are incapable of coping with computational budget variations during the testing stage. To tackle these issues, we propose a resource-adaptive test-time training framework called SlimTTT, which allows for the seamless switching of different sub-networks for adaptive inference. Furthermore, we discover that different width of sub-networks can capture different views of images and these views are complementary and beneficial to the ones created by data augmentation, which is widely used in TTT. To utilize these views, we introduce Width-enhance Contrastive Learning (WCL), Logits Consistency Regularization (LCR) and Global Feature Alignment (GFA) to promote representation consistency at both feature and prediction space in a self-supervised manner, enabling networks of different widths to excel in TTT tasks. Our proposed method, SlimTTT, has achieved state-of-the-art (SOTA) results across a variety of adaptation methods and four different datasets with varying backbones. Remarkably, despite a significant reduction in computational complexity - over 70% less than the current SOTA method - SlimTTT continues to deliver competitive performance, rendering it highly conducive for adoption in practice.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed to leverage slimmable networks in the scenario of test-time training to allow the model to meet different resource budgets during test-time training. The paper proposed width-enhanced contrastive learning which is to conduct contrastive learning among different network width to learn different representations. The proposed method shows better performance than previous	works at different resource budgets

### Strengths
1.	The paper has a clear explanation about the background and objectives of this work. 
2.	The proposed method shows better performance than previous works at different resource budgets.

### Weaknesses
1.	It seems that this work is pretty much slimmable network, but just in the setting of test-time training. I don’t see what are the unique challenges in applying slimmable networks in the test-time training? The test-time training seems to be the same as training-time training, but just without labels. Then the problem seems to be how to apply slimmable networks in the un-supervised setting, which has been studied in previous works [1].
2.	The motivation that different sub-networks could capture different image features has been studied in [2].
3.	In Table 1, the other methods should also use ResNet-50 with different widths to have a fair comparison.
4.	This work finetuned the pre-trained slimmable networks on ImageNet and ImageNet-C, what about other works?
5.	In Table 5, why is the training cost is comparable or even faster than TTT++ and TTAC? The proposed method needs to forward and backward multiple times, I am assuming it should be more training expensive.


### Questions
Please see the weakness part

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a varying resource constraint setting for Test-Time training approaches and proposes an architecture based on the Slimmable Network (Yu et al., 2018). The primary assumption made for the targeted varying resource constraints setting is the dynamically changing computational budget (hardware-based computational constraints or dynamic resource allocation to the algorithm) during inference. Slimmable neural network architectures are specifically designed to provide adaptive accuracy-efficiency trade-offs during model inference on various devices with different budgets of computational resources. In this paper, the authors utilize Width-enhanced Contrastive loss and Logit Consistency Regularization for maintaining consistency between the subnetworks in both features and logits space. Further, the paper also introduces an ensembling strategy based on dynamically changing resources to boost the performance of the architecture. The pipeline for the proposed framework can be summarized in 3 modules 1) Source Training Phase: The pretrained backbone is trained on the source dataset with the primary training objective with an additional auxiliary self-supervised learning task. 2) Target Training Phase:  for this phase, the paper proposes maintaining feature consistency between differently augmented views obtained by both slimmable network structure and data augmentation and adds another learning objective of Logits Consistency Regularization where an augmented version of the sample is sent to the largest network for obtaining a pseudo label which is further used to maintain prediction consistency among all the sub-networks. 3) In the last phase, the paper makes use of the predictions available from different slimmable networks to create an ensemble version of the predictions for boosting prediction performance. 

The paper provides empirical results on four widely used benchmarks (ImageNet-C, CIFAR10-C, CIFAR10.1, and CIFAR100-C) with different backbones (ResNet, Mobilienet, and ViT) for four settings of switchable widths in Slimmable Network (1.0×, 0.75×, 0.5×, 0.25×). The reported results highlight an improvement over the compared baselines and show the computation cost comparison via reporting the FLOPs with prediction accuracies. The paper also provides ablation experiments for highlighting the impact of various components in the design of the proposed framework.

### Strengths
* The paper highlights an important issue of dynamically changing resource constraints in test-time training settings for deploying models in the real world. The paper utilizes the architecture of slimmable networks to address this issue, making test-time training approaches to incorporate adaptive accuracy-efficiency trade-offs during model inference on various devices with different budgets of computational resources.

* The paper proposes the WCL, LCR, and GFA for exploiting the slimmable network to ensure consistency between multiple views captured by the architecture. The proposed design choices are sufficiently backed up by suitable ablation experiments. Moreover, as an additional advantage, the paper reports the slimmable network for TTT to be effective when compared with other baselines on the same computation budget.

* The paper presents a detailed empirical study with various backbones (3 backbones) and datasets (4 benchmarks) along with different settings of Switches in Slimmable Network (4 in number), with required performance comparison over the computation cost for fair comparison making the results more reliable.

### Weaknesses
 * One of the primary claims of the paper is the varying inference budget during the inference (also highlighted as Challenge II in Figure 1). Since the paper targets a practical setting of dynamic resource allocation during inference, it is imperative to consider experiments where the available compute changes frequently during inference (test time training). It would be interesting to monitor the sensitivity of the performance in those settings since different parameters of the model will be updated based on the available compute. Low-performance sensitivity on dynamically changing resources will make the method more reliable for practical use cases. Moreover, it’ll promote future research to address the challenges faced in such a setting. Specifically, the paper should investigate the impact of frequent switches in computational resources on the model's performance, as this is a key aspect of the claimed contribution. The current evaluation does not fully capture the challenges of a truly dynamic environment where resource availability fluctuates rapidly and unpredictably. This could involve simulating scenarios with varying resource availability at different time steps during the test phase, and analyzing the model's performance under these conditions. Furthermore, it's important to understand if the model's performance degrades over time with frequent resource switches due to error accumulation.

* The proposed framework highly depends on the source domain training however, the training cost and the convergence rate comparison for various architecture is missing from the paper. It would be good to add a comparison of training times/ convergence rates of the proposed architecture to make the approach more transparent for real-world deployment use cases. This is crucial for assessing the practical applicability of the method. The paper should provide a detailed analysis of the computational overhead associated with training the slimmable network, including the time required for convergence and the resources needed for training each sub-network. This analysis should include a comparison of the training time and convergence rates for different architectures used in the experiments (e.g., ResNet, MobileNet, ViT). Without this information, it is difficult to evaluate the overall efficiency and practicality of the proposed approach.

### Questions
Minor suggestions:
* It would be better to update the caption of Table 3 to highlight the explanation of numbers presented in red for easier readability. 
* While making the comparison with existing methods, it would be good to highlight the dependency on the availability of the source dataset. Adding another column for a clear distinction between TTA and TTT approaches will make the paper more transparent.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors identify two main shortcomings of existing TTT methods: resource inefficiency during deployment across devices and an inability to handle computational budget variations during testing. To address these, the authors propose SlimTTT, a resource-adaptive test-time training framework. They introduce techniques like Width-enhance Contrastive Learning (WCL), Logits Consistency Regularization (LCR), and Global Feature Alignment (GFA) to promote representation consistency. SlimTTT is reported to achieve state-of-the-art results across various adaptation methods and datasets, with a significant reduction in inference complexity. My main concerns lie on the motivation of SlimTTT and its evaluation protocols.

### Strengths
The proposed method properly integrates Width-enhance Contrastive Learning, Logits Consistency Regularization, and Global Feature Alignment and thus achieves significant performance improvement compared with prior source-free unsupervised domain adaptation methods, such as SHOT. 

The findings of “different width of sub-networks can capture multiple views of the same input data, possessing a talent for enhancing TTT performance” is interesting and provides new insights.

### Weaknesses
The motivation for slimmable TTA does not convince me. As all TTA methods are inference-time methods and the adapttion+inference is often conducted on the same device, in Table 1, the computational resource consumption comparison should include both training (GPU memory, wall-clock time) and inference, rather than only #Model Params and Flops during inference. I mean, for a resource-limited device, whether a TTA method can be run is determined by the training resource request, rather than inference.

In Table 1, ResNet-50(1.0$\times$)+TENT+ImageNet-C@56.89 is evaluated in an online manner (to my knowledge). So if SilmTTT is evaluated in an offline manner, the comparison would be unfair.

Does the proposed SlimTTT work well in the online setting? I am curious about the online performance and TTA efficiency (training+inference) comparisons with compared methods.

Comparisons with more resource-efficient TTA methods (perfectly under the online setting) are preferred, such as EATA [Efficient Test-Time Model Adaptation without Forgetting. ICML 2022].

### Questions
For all compared methods, are they evaluated in online or offline setting?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces SlimTTT, a resource-efficient approach for test-time training. The author proposed a practical scenario of TTT under resource constraints. To address such a challenge, the method utilizes slimmable network that can flexibly switch between different widths of sub-networks for adaptive inference and requires no retraining. The method includes width-enhanced contrastive learning, logit consistency regularization, and global feature alignment to promote representation consistency among sub-networks, in both feature and prediction spaces. The method is demonstrated by the experiment against other TTT methods by the adaption to corrupt samples on several datasets. It can achieve superior performance in the same resource constraint and can be generalized with several different backbones.

### Strengths
1. Proposed a new challenge of resource constraint in such a field, which fits in with realistic demands as a result.

2. Proposed a test-time training method for slimmable neural network. 

3. Comprehensive experiments that support the methodology and each sub-module of it.

4. The framework considered comprehensively every part of an image classification pipeline.

### Weaknesses
1. The definition "Efficient" is vague in the title, that the model result of your method in inference is efficient, but not during the training process（it actually costs more time as claimed in your experiment). Does the efficiency come from utilizing the slimmable models and you proposed a TTT method for them？

2. There are some basic assumptions that should be explained.

3. The purpose of the TTT is to generalize the model when a distribution shift occurs, as your experiment proves by using corrupt samples. This logical correlation can be straightly pointed out.

### Questions
1. In some works about explainable networks, the grad-cam result shows what the model is focusing on and indicates the semantical feature that is used to make decisions. Does the bigger-width network contain the attention information of smaller networks well in all these backbones? If not, is the bigger network always better?

2. In some cases of classification, one class can include several visual patterns (eg. some datasets have coarse classes like “vehicle ” including items that do not look exactly the same.) Will these have an impact if you align all networks to the supernet, as it may focus on several instance-level features? I'm also curious if this will have a bigger impact on the contrastive learning that expands the positive data with the different representations from 2 sizes of model.

3. There seems to be a paradox between the purpose of consistency and the ensemble of results in 3.4, if the difference between all subnets to the super net is lowered, will they intend to focus on the same feature? Though it improves the performance, I'm not fully understanding the reason.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good
