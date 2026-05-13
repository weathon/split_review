# Conserve-Update-Revise to Cure Generalization and Robustness Trade-off in Adversarial Training

- Decision: Accept
- Scores: 5, 6, 6, 5

## Abstract
Adversarial training improves the robustness of neural networks against adversarial attacks, albeit at the expense of the trade-off between standard and robust generalization.
To unveil the underlying factors driving this phenomenon, we examine the layer-wise learning capabilities of neural networks during the transition from a standard to an adversarial setting. Our empirical findings demonstrate that selectively updating specific layers while preserving others can substantially enhance the network's learning capacity. We therefore propose CURE, a novel training framework that leverages a gradient prominence criterion to perform selective conservation, updating, and revision of weights. Importantly, CURE is designed to be dataset- and architecture-agnostic, ensuring its applicability across various scenarios. It effectively tackles both memorization and overfitting issues, thus enhancing the trade-off between robustness and generalization and additionally, this training approach also aids in mitigating "robust overfitting". Furthermore, our study provides valuable insights into the mechanisms of selective adversarial training and offers a promising avenue for future research.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper focuses on the trade-off between standard and robust generalization. To this end, this paper proposes CURE that leverages a gradient prominence criterion to perform selective conservation, updating, and revision of weights, which can tackle both memorization and overfitting issues.

### Strengths
The problem authors focused on is very interesting.

### Weaknesses
1. Experimental results in Fig. 2 cannot support authors' claim that ".. cause reduced performance on both data due to overwriting of learned information..". Specifically, just a comparison of accuracy in Fig. 2  cannot reflect the overwriting of learned information. Authors should design new solid experiments to support this conclusion. For instance, analyzing the change in feature representations or using metrics that directly quantify the forgetting of previously learned information would be more convincing than just observing a drop in accuracy. The current evidence is insufficient to claim that the observed accuracy drop is due to overwriting, rather than a simple shift in the learned feature space.
2. Authors did not clarify how to disentangle robust and non-robust features, which still presents a significant challenge. Hence, Fig.3 is in doubt. The visualization in Figure 3, while potentially illustrative, lacks a clear methodology for disentangling robust and non-robust features. Without a well-defined process for identifying and separating these features, the interpretation of Figure 3 remains subjective and open to question. The authors should provide a concrete method for feature disentanglement, or at least acknowledge the limitations of their visualization in the absence of such a method.
3. I wonder why "a subset with the most significant impact on accuracy" equals to the subset of weights that "contribute more to the joint distribution of both natural and adversarial accuracy." Can you prove it or explain it? The connection between the impact on accuracy and the contribution to the joint distribution is not clearly established. The authors need to provide a more rigorous justification for this claim, possibly through mathematical derivation or a more detailed explanation of the underlying assumptions. The current explanation is not sufficiently convincing.
4. A algorithm flowchart will help readers better understand how weights are updated in each epoch. In each epoch, are different or same subsets of weights updated? It is unclear how the weight selection process evolves over training epochs. A flowchart would clarify the dynamic nature of weight updates, specifically whether the same or different subsets of weights are updated in each epoch. This is crucial for understanding the adaptive behavior of the proposed method.
5. What does "sample∼U(0,1)<r" in Eq. 7 mean? The meaning of the stochastic sampling in Equation 7 is not clearly explained. The authors should provide a more detailed explanation of how this sampling process contributes to the overall algorithm and why a uniform distribution is chosen for this purpose.
6. Experimental results cannot verify the effectiveness of the proposed CURE method, since authors just conducted experiments on resnet18 and resnet34. Please conduct more experiments on more classic DNNs. The experimental evaluation is limited to only ResNet18 and ResNet34. To demonstrate the general applicability of the proposed method, experiments on a wider range of architectures, including more classic DNNs, are necessary.

### Questions
In this paper, many conclusions are not supported authors' experimental results, i.e., we cannot infer these conclusions just based on existing experimental results.
Thus, many conclusions in Section 3 are over-claimed.
Details are stated in weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel approach to improving the adversarial robustness of DNNs while maintaining the performance on natural samples. The authors first conduct empirical studies to discover that updating weights in all layers in AT may be not good for the generalization of DNNs in both natural and adversarial samples. Thus, they propose an adaptive method to selectively update a subset of weights in the DNN. The proposed method is simple but empirically effective.

### Strengths
This paper presents a simple yet effective method of improving both robustness and generalization of DNNs.

This study discovers some interesting phenomena, e.g., updating middle layers is beneficial to standard and robustness generalization, and adversarial training increases the similarity between features of different layers.

The paper is well-written and easy to follow.

### Weaknesses
- The authors frequently use the terms “overwritten” and “learning” when describing weight updates. However, the distinction between these two concepts remains unclear. Specifically, what criteria are used to determine whether a weight update constitutes “overwriting” of previously learned features versus “learning” of new information? For instance, in Figure 2(a), the accuracy drop is used to infer conclusions about “overwritten” and “learning.” However, it is not immediately obvious how the magnitude of the accuracy drop directly correlates to one or the other. A more precise, quantifiable definition of these terms would significantly improve the clarity of the paper. Furthermore, does a drop in natural accuracy always imply overwriting of features? 
- In Section 2, the methodology involves re-initializing and updating the weights of selected layers. While this provides an interesting perspective, it is worth considering an alternative approach: directly fine-tuning these layers with adversarial examples without re-initialization. Re-initializing weights, especially in shallow layers, may lead to a significant drop in performance because the network is essentially learning from random noise. In contrast, fine-tuning would allow the network to adjust its existing knowledge, potentially leading to a more nuanced understanding of the interplay between natural and adversarial examples. It would be valuable to see a comparison between these two approaches to understand their respective impacts on model performance.
- Figure 3 presents a potential inconsistency. If the weights of deep layers (e.g., U-34) are updated while shallow layers (e.g., blocks 1 and 2) remain fixed, one would expect the features in the shallow layers to be frozen as well. Consequently, the similarity between shallow layers in U-34 should resemble that of the ST model. However, the similarities between shallow layers in Figure 3 exhibit variations across all models. This discrepancy requires further clarification. Are these variations due to changes in batch normalization statistics, or is there another factor at play?
- The paper makes claims about “disentangling clean and adversarial representations” and “disentangling robust and non-robust features,” as well as identifying layers with “greater learning capacity.” However, these concepts are not rigorously defined or operationalized. For example, what specific criteria are used to determine a layer's “learning capacity”? Without clear definitions and methodologies for these concepts, the claims may appear unsubstantiated. I suggest the authors either provide more concrete evidence and definitions or rephrase these claims to reflect the exploratory nature of the work.
- There seems to be a misalignment between the findings presented in Figure 4 and Figure 6(b). Figure 4 suggests that updating high layers may lead to robustness overfitting, yet Figure 6(b) indicates a significant proportion of updated gradients in high layers, particularly in the batch normalization layers. This apparent contradiction warrants further discussion. Is this phenomenon related to the dynamics of the decision boundary, as suggested in the paper? A more in-depth analysis of this misalignment would strengthen the paper's conclusions.
- The paper analyzes the representation similarity between different layers in DNNs trained using various methods. It would be interesting to extend this analysis to include models trained using CURE. How does the representation similarity in CURE-trained models compare to those trained using ST and AT? This comparison could provide further insights into the effectiveness of CURE in balancing robustness and generalization.

### Questions
- Is CURE used by training the model from scratch with the loss function in equation (5) or finetuning a pre-trained network? If the CURE is adopted on a pre-trained model, I am concerned that it may be unfair to compare it with other training-from-scratch methods. Besides, it also increases the computational cost to train the model twice (pre-train with ST and then finetune with CURE). 
- How stable is CURE when using different hyper-parameters ($\alpha,\beta$ and $p$)?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper unveils the underlying factors of the trade-off between standard and robust generalization in adversarial training by examining the layer-wise learning capabilities of neural networks during the transition from a standard to an adversarial setting. The paper demonstrates that selectively updating specific layers while preserving others can substantially enhance the network's learning capacity empirically, and proposes a method to leverage a gradient prominence criterion to perform selective conservation, updating, and revision of weights named CURE. The paper verified the effectiveness of CURE on various dataset and architecture, which verifying the effect in enhancing the trade-off between robustness and generalization and alleviating robust overfitting empirically.

### Strengths
This paper has good originality, high quality and clear expression. The paper unveils the trade-off between standard and robust generalization in adversarial training in the perspective of layer-wise learning capabilities of neural networks and proposes a new method to alleviate robust overfitting.

### Weaknesses
The analysis of selective adversarial training are empirically not theoretically.It's better to provide theoretically analysis of selective adversarial training.

### Questions
1.Is the proposed method still works well on larger dataset, for example ImageNet?
2.There are so many hyperparameters such as α,β,γ,r,d, how to mediate so many hyperpapameters effectively?
3.For deeper neural networks, such as resnet-101, is the proposed method still works well?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method to improve the trade-off between robustness and generalization in adversarial training.
First, this paper investigates the difference between adversarial and clean representations layer-wisely,
and next, it investigates overfitting in adversarial training when parameters of only some layers are selectively updated.
Based on the observation that some layers tend to suffer from overfitting, this paper proposes CURE that leverages a gradient prominence criterion to perform selective conservation, updating, and revision of weights.
To evaluate the trade-off, this paper establishes a new metric: Natural-Robustness Ratio which is calculated by using accuracy against C&W and natural accuracy.
CURE is evaluated in terms of this metric, robustness against several attacks including AutoAttack, and robustness against natural corruption.

### Strengths
- This paper addresses an important problem in adversarial training: Overfitting and the trade-off between natural accuracy and robustness.
- The detailed investigation of layer-wise learning phenomena in adversarial learning is novel and provides interesting insights.
Revealed layer-wise properties might inspire researchers in this area and might cause new defense methods.
- Gradient-based selective update for adversarial training is a new and interesting idea. 
The figure of gradients in the training (Fig. 6) intuitively shows how the proposed method works by using the information of gradients well.
- CURE is evaluated by using various attacks and architectures. However, baselines are not consistent and results might be cherry-picked.

### Weaknesses
 - This paper lacks an ablation study. Although layer-wise analyses are interesting, the proposed method contains several components besides selective updating. How is the performance if we use only RGP? 
If it is not good, are equations (4), (5), (7), and (8) relevant to the layer-wise analysis?
If other parts than the selective updating contribute to the performance, the layer-wise analysis may not be very worthwhile.

- This paper does not present a fair and honest evaluation and presentation of the results of the experiments.
The trade-off metric is intentionally designed to make the proposed method look overly good. Is there a rational explanation as to why the C&W is used in the evaluation of trade-off, even though AutoAttack performs better than C&W in terms of attack success rate? I suspect that C&W is chosen because the numbers of metrics are not better in the case of AutoAttack. In fact, robustness against AutoAttack of the proposed method is not always greater than baselines.
Additionally, the vertical and horizontal scales in Figure 1 are not aligned, which can be misleading.
Natural corruptions are selectively used from CIFAR10C. Their results may be cherry-picked. I would like to see the results against all natural corruptions in CIFAR10C. Baseline methods are not consistent over expreiments.
Why does Table 1 not contain the result of HAT, and does Table 2 not contain ACT, ARD, LAD, and LAS-AT?

- The boundary between the proposed and existing methods is described ambiguously. Eqs. (4) and (5) seem to be an objective function of TRADES. Why are these equations written in the section of the proposed method?
Additionally, SMU seems to be exponential moving average (EMA) with a stochastic parameter. SEAT (Wang & Wang, 2021) and other recent methods also use EMA, which is sometimes called weight averaging. Unlike them, the proposed method uses averaged parameters in the regularization term. I would like to see the comparison between averaging weights directly and using averaged weights for regularization.
- Minor issues
    - [a] might be related work that addresses the trade-off and focuses on the difference between the representations of clean data and adversarial examples. The method in [a] outperforms LAS-AT in terms of the trade-off. Since it seems to be concurrent work, I think that it is not necessary to compare.  
    [a] Suzuki S et al. "Adversarial Finetuning with Latent Representation Constraint to Mitigate Accuracy-Robustness Tradeoff." ICCV 2023.

### Questions
- How is the performance if we use only RGP? If it is not good, are equations (4), (5), (7), and (8) relevant to the layer-wise analysis?
- Is there a rational explanation as to why the C&W is used in the evaluation of trade-off? Is there any reasonable explanation for Natural-Robusthess Ratio? Why is eq.(9) suit to evaluate the trade-off?
- How does NRR become if using AutoAttack?
- What is the difference between TRADES and eqs.(4) and (5)?
- Why does Table 1 not contain the result of HAT, and does Table 2 not contain ACT, ARD, LAD, LAS-AT?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
