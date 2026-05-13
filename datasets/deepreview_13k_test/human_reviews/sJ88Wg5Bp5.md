# ViDA: Homeostatic Visual Domain Adapter for Continual Test Time Adaptation

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Since real-world machine systems are running in non-stationary environments, Continual Test-Time Adaptation (CTTA) task is proposed to adapt the pre-trained model to continually changing target domains. Recently, existing methods mainly focus on model-based adaptation, which aims to leverage a self-training manner to extract the target domain knowledge. However, pseudo labels can be noisy and the updated model parameters are unreliable under dynamic data distributions, leading to error accumulation and catastrophic forgetting in the continual adaptation process. To tackle these challenges and maintain the model plasticity, we design a Visual Domain Adapter (ViDA) for CTTA, explicitly handling both domain-specific and domain-shared knowledge. Specifically, we first comprehensively explore the different domain representations of the adapters with trainable high-rank or low-rank embedding spaces. Then we inject ViDAs into the pre-trained model, which leverages high-rank and low-rank features to adapt the current domain distribution and maintain the continual domain-shared knowledge, respectively. To exploit the low-rank and high-rank ViDAs more effectively, we further propose a Homeostatic Knowledge Allotment (HKA) strategy, which adaptively combines different knowledge from each ViDA. Extensive experiments conducted on four widely used benchmarks demonstrate that our proposed method achieves state-of-the-art performance in both classification and segmentation CTTA tasks. Note that, our method can be regarded as a novel transfer paradigm for large-scale models, delivering promising results in adaptation to continually changing distributions. Project page: \href{https://sites.google.google

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a Continual Test-Time Adaptation (CTTA) method called Visual Domain Adapter (ViDA), which addresses the challenges of error accumulation and catastrophic forgetting in models operating in dynamic environments. ViDA differentiates itself by leveraging both high-rank and low-rank feature spaces to maintain domain-specific and shared knowledge. The HKA(Homeostatic Knowledge Allotment) is also proposed to balance the integration of these features dynamically. This proposed method is evaluated on multiple benchmarks, showing good performance in classification and segmentation tasks.

### Strengths
The paper presents an intriguing exploration of the differential capabilities of low-rank and high-rank features in domain adaptation, suggesting potential for a wide range of applications. The analysis substantiates the underlying mechanisms of the proposed method's operation. Also, the proposed method is validated through extensive experiments. The experiments include several benchmarks in classification and segmentation tasks.

### Weaknesses
- Observing the t-SNE plots in the low-rank branch (Figure 1), it appears that the nighttime representation in the ACDC dataset is not aligning as a domain-shared characteristic. I think nighttime data is not clustering in the low-rank space, which may indicate unique domain characteristics. Quantitative analysis with clustering metrics could clarify this.

- In Figure 3(a), the inter-domain divergence does not seem to exhibit significant differences between high-rank and low-rank features across conditions c1 to c9. Does this imply that the effectiveness of the rank-based approach is sensitive to the type of corruption present in the data? Understanding this could inform the robustness of the proposed method across a wider array of scenarios.

### Questions
- Regarding Figure 1, it would be insightful to include the t-SNE results for each transformer block. Such detailed visualizations would help to understand feature spaces across the different layers of the network.

- Since t-SNE visualizations represent relative rather than absolute distances, I am curious about the quantitative differences in domain distribution distances within the ACDC dataset when comparing low-rank to high-rank representations. Quantifying this difference could bolster the demonstration of your method's efficacy in managing domain shifts.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of continual test-time model adaptation, where training data is not accessible and only continually changing target domains are available. To address error accumulation and catastrophic forgetting problems, they propose a homeostatic Visual Domain Adapter (ViDA) which explicitly manages domain-specific and task-relevant knowledge. Moreover, a Homeostatic Knowledge Allotment (HKA) strategy is introduced to dynamically merge knowledge from low-rank and high-rank ViDAs. Extensive experiments on standard TTA benchmarks demonstrate the effectiveness of the proposed approach.

### Strengths
- The problem of tackling continuously shifting target domains represents a substantial challenge and is an area that has not been sufficiently explored in existing literature.

- The paper is articulately composed and comprehensible, effectively communicating the core ideas of the study to the reader. I am confident that I have acquired a solid understanding of the authors’ work through my examination of the manuscript.

- Experiments are comprehensive with a variety of benchmark tasks.

### Weaknesses
- My main concern is the novelty. Separating the extracted features into domain-invariant and domain-specific components has been extensively explored in previous domain adaptation and domain generalization methods. It lacks clear pieces of evidence to show why the proposed method is preferable in the context of test-time adaptation.

- The experimental results, as illustrated in Table 1, indicate that the improvements achieved by the proposed method in comparison to previous approaches, such as CoTTA, are marginal.

- The section of the paper discussing large models, as well as the associated experiments, appear incomplete and somewhat abrupt.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to add two branches of low-rank and high-rank adapters to handle the problem of continuous test time adaption. The paper suggests that the low-rank adapter acquires domain-agnostic information, whereas the high-rank adapter acquires domain-specific knowledge. In addition, the paper proposes a Homeostatic Knowledge Allotment (HKA) technique for determining the contribution of the two branches. Experiments are carried out for the image classification task on the ImagenetC, CIFAR10C, and CIFAR100C benchmarks, as well as for semantic segmentation on the Cityscapes-to-ACDC benchmark. The experimental findings show that the proposed mechanism is successful, producing state-of-the-art outcomes for some pre-trained deep neural network architectures.

### Strengths
1. This paper employs two distinct adapters for acquiring domain-specific and domain-agnostic knowledge: low-rank and high-rank adapters.
2. The HKA technique for updating the weight contribution of these adapters depending on the prediction uncertainty value is a good idea.
3. The contribution of several components is demonstrated in the ablation analysis.
4. In the TTA scenario, experimental results for zero-shot generalization are novel.

### Weaknesses
1. There is no theoretical justification or an intuitive explanation for why the low-rank adapter acquires domain-agnostic information, whereas the high-rank adapter collects domain-specific knowledge other than experimental observation.
2. The backbone architecture in some experiments differs from prior developments, such as CoTTA.
3. What about the performance of the proposed approach CIFAR100-to-CIFAR100C method for ResNeXt-29 architecture?
4. Using the source data, retrain the "model added with low/high-rank adapters" for a few stages. Without access to the source domain data, it is impossible to employ off-the-shelf pre-trained models.

### Questions
1. There is no theoretical justification, nor even an intuitive explanation, for why the low-rank adapter acquires domain-agnostic information whereas the high-rank adapter collects domain-specific knowledge other than experimental observation.
2. The backbone architecture in some experiments differs from prior developments, such as CoTTA.
3. What about the performance of the proposed approach CIFAR100-to-CIFAR100C method for ResNeXt-29 architecture?
4. Using the source data, retrain the "model added with low/high-rank adapters" for a few steps. Without access to the source domain data, it is impossible to employ off-the-shelf pre-trained models.

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
The authors have proposed a method for continual test time adaptation and are improving previous methods significantly. They do so by incorporating a low-rank and a high-rank embedding scheme where high-rank scheme is shown to be sensitive towards domain specific features whereas low-rank scheme is shown to be sensitive towards domain-invariant features. Additionally, to weigh these features during adaptation, they introduced a homeostatic knowledge allotment strategy where they exploit the probabilistic nature of multiple forward passes to get the best set of parameters. Overall, the authors are achieving reasonably well results.

### Strengths
Continual Test Time Adaptation is a relatively new and challenging problem in the vision community. The authors have incorporated a paradigm that does just that. 

Originality
- This particular challenge is still at its infancy and the proposed ideas in this paper can help mature the challenge. In terms of originality, the authors have incorporated similar to [1] with their domain specific and domain invariant learning scheme; however, these proposed ideas have shown to contribute significantly, and they have shown it in the results. Additionally, their homeostatic knowledge allotment scheme is also quite useful in terms of what features should weigh more than the other. Therefore, I believe the work is original and is contributing to the field.

Quality
- Since the challenge has a very big  real world applicability, and the approach has shown to perform very well in this regard.
- Additionally, the authors have shown extensive experiments on various standard datasets where they outperform other SOTA approaches including CoTTA [2] and VDP [1].
- The authors have shown extensive ablation study and motivation to use the different components of the approach in the paper.

Clarity
- The paper is well written and easy to follow.
- The authors have clarified their statements with equations and experiments. 

Significance
- As mentioned previously, the CTTA has a lot of real-world applicability in IID and non-IID scenarios, and recently, works have been tackling both of them in different scenarios. This work has shown perform boost in this regard, and the authors have solifdified their claims with extensive experiments. 
- Additionally, as the paper mentions, it can be integrated with any networks very easily further boosting the applicability of the method.
- This work has potential to contribute significantly to the community.

References:
1. Gan, Y., Bai, Y., Lou, Y., Ma, X., Zhang, R., Shi, N. and Luo, L., 2023, June. Decorate the newcomers: Visual domain prompt for continual test time adaptation. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 37, No. 6, pp. 7595-7603).
2. Wang, Q., Fink, O., Van Gool, L. and Dai, D., 2022. Continual test-time domain adaptation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 7201-7211).

### Weaknesses
Concerns
- The authors mentioned that there is not any non-linear layer in ViDA. It is not clear what they mean by that. There is no activation? How are they implementing this network? The authors do mention that there is a direct linear projection of ViDA; however, I would like to understand the relationship of the layers within the model.
- How did the authors decide parameter 𝜭 in equation 5? Was it decided empirically?

### Questions
I recommend clarifying some confusions from the weakness section about the non-linearity of the model. 
- In what sense the is not any non-linear layer in ViDA? Is there no activation? How are you implementing this network? Is there a direct linear projection of ViDA? It would be important to understand the relationship of the layers within the model.
- How was the parameter 𝜭 in equation 5 set?
- Additionally, I suggest incorporating details such as the ablation study on homeostatic knowledge allotment from the appendix to the main paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
