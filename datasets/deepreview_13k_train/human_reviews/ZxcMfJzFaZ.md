# Boosting Adversarial Robustness with CLAT: Criticality Leveraged Adversarial Training

- Decision: Reject
- Scores: 6, 3, 6, 5, 6

## Abstract
Adversarial training (AT) is a common technique for enhancing neural network robustness. Typically, AT updates all trainable parameters, but such comprehensive adjustments can lead to overfitting and increased generalization errors on clean data. Research suggests that fine-tuning specific parameters may be more effective; however, methods for identifying these essential parameters and establishing effective optimization objectives remain unclear and inadequately addressed. We present CLAT, an innovative adversarial fine-tuning algorithm that mitigates adversarial overfitting by integrating "criticality" into the training process. Instead of tuning the entire model, CLAT identifies and fine-tunes fewer parameters in robustness-critical layers—those predominantly learning non-robust features—while keeping the rest of the model fixed. Additionally, CLAT employs a dynamic layer selection process that adapts to changes in layer criticality during training. Empirical results demonstrate that CLAT can be seamlessly integrated with existing adversarial training methods, enhancing clean accuracy and adversarial robustness by over 2% compared to baseline approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper tackles the important issue of adversarial vulnerability of neural networks. Instead of updating all parameters during adversarial training, CLAT focuses on layers that predominantly learn non-robust features, identified by a "criticality index." This selective focus is designed to improve adversarial robustness, can be used with on top of standard adversarial training approaches. The paper offers detailed results on multiple architectures and also evaluated under both white-box and black-box adversarial attacks

### Strengths
- CLAT presents an alternative to traditional adversarial training, which requires updating the entire network, and can be used on top of any adversarial training method
- The analysis is detailed and covers many network architectures 
- The method is evaluated on various attacks and also includes the strong attacks such as Auto Attack
- The ablation study and the overhead analysis is good and useful

### Weaknesses
 - I am unclear about the problem statement and objective. Because, in the Adversarial domain, there are two main adversarial training challenges: (1) the trade-off between clean and adversarial accuracy and (2) adversarial overfitting, and there are methods that cater to either or both, but the evaluation criteria are different. For ex, for trade-off we need to check how clean acc and adv acc are impacted, and for the latter, we need to report both the peak and final accuracy scores, highlighting the impact of overfitting. 
- The concept of robust and non-robust features is important in the paper, and needs more context and explanation. What is the criteria to differentiate, and further an empirical example or analysis will provide more clarity. Additionally, the theoretical explanation behind the criticality index would benefit from more intuition. Is the motivation based on the paper [Robustness via curvature regularization, and vice versa], that small curvature correlated to higher robustness? How does this relate to criticality or non-robust features? The main focus of the paper about critical layers and its criterion is unclear to me.
- The paper uses multiple terms—such as "weakness," "robust-critical layers," "sensitive layers," and "non-robust features". This variation makes it difficult to understand the precise characteristics, need consistent definitions. Also are we talking about NR layers (weights) or features, there's multiple usages of these terms.
- Since CLAT fine-tunes layers that supposedly learn non-robust features (which aid clean accuracy), one would expect that this selective fine-tuning might reduce clean accuracy, however the clean accuracy improves as well ? I am curious to understand more on this.
- Line 430: Additional intuition or analysis is needed to support this claim. What architectural properties might influence these findings? Additionally, is there a discernible pattern to the critical layers? Identifying such patterns could provide valuable insights into what different layers learn and how this understanding could be leveraged to improve robustness further.

### Questions
- Could you elaborate on different hyperparameters and how they were chosen? Ex. the 5% threshold for selecting critical layers. Is there any consideration for adjusting the percentage based on the depth or structure of the network?
- Robust/Non-Robust - is it only layer wise, or also makes sense to see sub-networks or neuron-wise? Introduction could use more context
- Results - (related to point 1 in weaknesses), if the the paper claims to address overfitting in adversarial training, it would be essential to compare CLAT with explicit overfitting reduction techniques like AWP (Adversarial Weight Perturbation) or SWA (Stochastic Weight Averaging). Including metrics such as best vs. final accuracy scores for these methods would help demonstrate whether CLAT effectively mitigates overfitting.
- Computational overhead on bigger and more complex datasets? (other than CIFAR)
-  Line 461 - Did not understand the hypothesis for the behavior of Figure 3. Please elaborate with supporting evidence. Further, how is the behavior on clean accuracy? In general, the ablation study is interesting, but the claims and intuitions presented would benefit from more supporting evidence to strengthen their validity.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a **Criticality-Leveraged Adversarial Training (CLAT)** method to enhance adversarial robustness by keeping certain parts of the neural network fixed and only fine-tuning the layers that are fragile in terms of robustness. Experiments are conducted across various datasets and neural network structures.

### Strengths
1. The explanation of the concept is clear.

2. The presentation in the experimental section is well-organized and easy to follow.

### Weaknesses
1. This method is cumbersome as it requires inputting both clean and adversarial images to compute the difference.

2. In Section 3.1, numerous mathematical tools are introduced but ultimately seem unnecessary, as the final objective function minimizes the initial starting point. This makes much of the content in Section 3.1 redundant.

3. Experiments are conducted only on the CIFAR dataset with CNN structures. The experimental design should be expanded to include both small- and large-scale datasets, as well as ViT models.

### Questions
1. Some tables could use bold font to highlight the best results.

2. To demonstrate the effectiveness of the proposed Layer Criticality Index, an ablation study on fine-tuning different critical layers with small or large $C_{f_i}$ values would be helpful.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents an adversarial-finetuning algorithm that selectively updates specific parameters in a deep network. The algorithm relies on iteratively finding `critically vulnerable' parameters and then leveraging variants of adversarial training to robustly train deep networks. The fraction of critical parameters is often less than 4% of the total network, leading to better regularization and reduced overfitting. The paper presents empirical results for a variety of adversarial training approaches, as well as several ablation studies.

### Strengths
1. The CLAT formulation expands upon existing intuition of constraining the local lipschitz constant of layers as an adversarial defense, by restricting the number of trainable layers. The idea of using smarter regularization to reduce overfitting is quite interesting, and proves to be useful in the settings that the paper describes.

2. The results and ablations are quite thorough, and support the claims in the paper. I especially appreciate the results in Fig. 2 for clearly showing the advantages and disadvantages of CLAT over just pure adversarial training.

### Weaknesses
Some possible improvements are listed below:

1. The criticality metric is essentially an estimate of the ratio of local lipschitz constants across layers. While the use of the metric as a way to rank layers by vulnerability is interesting, it would be better to use standard terminology here rather than coming up with new ones. I also suggest adding a discussion comparing other lipschitz regularization approaches used as an adversarial defense.

2. The paper mostly conducts experiments on CIFAR-10/100 which are generally standard in the field of robustness. However, an experiment on ImageNet or a dataset of similar size and complexity would be a valuable addition. One hypothesis to test is if a dataset of additional complexity also requires a similar number of CLAT parameters. This would also further strengthen the claims from Table 8 which suggests that criticality is an architecture-specific phenomenon.

3. Another ablation that I find would be useful is to track the change in critical layer distributions across training. Since the algorithm re-identifies critical layers every 10 epochs, does the distribution change significantly over training? Specifically, are critical layers more prominent in earlier or later layers as training progresses. This may help further reduce the hyperparameter exploration required for CLAT.

4. Finally, a comparison of epoch wall-time for PGD-AT versus PGD-AT + CLAT would be interesting.

Overall, the results are quite interesting and encouraging, but I would appreciate it if the authors addressed other lipschitz regularization approaches for adversarial defense in the draft.

Minor nit: The plots often have very thin lines close to each other. I suggest increasing the line thickness and fontsize in the figures to make them more clear.

### Questions
1. What was the reasoning behind approximating $\frac{\partial F(x')}{\partial x'}$ with a uniform vector in Eq. 5?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method to address adversarial overfitting issues by optimizing only the parameters in critical layers during adversarial training, instead of all parameters. The authors argue that this approach can effectively alleviate the problem. Specifically, they identify critical layers as those that exhibit a stronger tendency to learn non-robust features or demonstrate higher sensitivity to adversarial input perturbations compared to other layers in the model. The authors empirically demonstrate the effectiveness of their method through experiments conducted on CIFAR10 and CIFAR100 datasets.

### Strengths
The numerical experiments in the paper yield promising results, and the method's general applicability is validated across multiple models. The approach presented in this paper is intuitive, and the writing is clear and easy to understand.

### Weaknesses
The method proposed by the authors appears to be empirically feasible but lacks theoretical justification. I have certain reservations about the authors' approach, as it appears to be not much different from simply reducing the learning rate. Notably, the authors have fix the maximum number of epochs in their experimental setup, rather than training until convergence, which deviates from conventional practices. If the method merely prevents the model from learning to fit, in order to achieve the so-called mitigation of overfitting, I question the significance of this paper. The core issue is that the paper does not provide a clear explanation of why optimizing only critical layers should inherently lead to better generalization, or why this approach is superior to other regularization techniques. The selection of critical layers is also not rigorously justified, and the criteria used for identifying these layers may be sensitive to the specific architecture or dataset used, thus limiting the general applicability of the method.

### Questions
I suggest the authors further investigate the performance of the model after increasing the number of epochs, as well as compare the performance of the model after reducing the learning rate. Additionally, I recommend including the performance of the model without adversarial training in the table, to facilitate comparison for the readers.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work studies the adversarial robustness of image classification models. It focuses on improving adversarial robustness through fine-tuning the parameters of selected layers. Specifically, it first proposes to identify robustness-critical layers by the (approximate) curvature of loss landscape. During fine-tuning, it only updates the parameters in the robustness-critical layers, while keeping the rest fixed.

### Strengths
1. The idea of identifying and fine-tuning robustness-critical layers is interesting and less studied before. It has the potential of improving the trade-off between accuracy and robustness through reducing the over-regularization of adversarial training.

### Weaknesses
1. The paper uses the term "adversarial overfitting" without a clear definition. It is confusing because there exists phenomena such as "robust overfitting" [1] and "catastrophic overfitting" [2]. The authors should clarify if they are proposing something new or just referring to either of them. If latter, I would suggest the authors to avoid the creation of new term and adopt the existing. 
2. The motivation of the proposed method is weak. The paper could benefit from a more in-depth discussion of how updating critical layers, instead of all, mitigates adversarial overfitting. 
3. Technically, the fine-tuning loss proposed in section 3.2 is similar to the loss function of TRADES.
4. 10-step PGD without restart is too weak so the conducted adversarial evaluation using it is unreliable. It is therefore unable for me to judge the soundness of the results e.g. in the Tab. 1. 
5. It has been demonstrated that data augmentation methods such as IDBH [3] and generative models [4] are effective in mitigating overfitting in adversarial training. It could enhance the strength of the proposed method if it improves the performance when combined with them.

### Questions
Please refer to the above.

### Soundness
3

### Presentation
2

### Contribution
2
