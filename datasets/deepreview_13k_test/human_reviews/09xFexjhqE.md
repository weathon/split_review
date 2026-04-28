# AutoLoRa: An Automated Robust Fine-Tuning Framework

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Robust Fine-Tuning (RFT) is a low-cost strategy to obtain adversarial robustness in downstream applications, without requiring a lot of computational resources and collecting significant amounts of data. This paper uncovers an issue with the existing RFT, 
where optimizing both adversarial and natural objectives through the feature extractor (FE) yields significantly divergent gradient directions. This divergence introduces instability in the optimization process, thereby hindering the attainment of adversarial robustness and rendering RFT highly sensitive to hyperparameters. To mitigate this issue, we propose a low-rank (LoRa) branch that disentangles RFT into two distinct components: optimizing natural objectives via the LoRa branch and adversarial objectives via the FE. Besides, we introduce heuristic strategies for automating the scheduling of the learning rate and the scalars of loss terms. Extensive empirical evaluations demonstrate that our proposed automated RFT disentangled via the LoRa branch (AutoLoRa) achieves new state-of-the-art results across a range of downstream tasks. AutoLoRa holds significant practical utility, as it automatically converts a pre-trained FE into an adversarially robust model for downstream tasks without the need for searching hyperparameters. Our source code is available at [the GitHub](https://github.com/GodXuxilie/RobustSSL_Benchmark/tree/main/Finetuning_Methods/AutoLoRa).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a decoupled fine-tuning framework for learning adversarially robust features. Specifically, a conventional robust finetuning pipeline consists of two losses: a natural objective and an adversarial objective. The paper shows that the divergence in gradients from the two objectives is correlated with downstream accuracy on robustness benchmarks. Therefore, it proposes to decouple a model into two branches where the second branch is constructed using Low-rank adaptation (LORA). In the decoupled training scheme, the main model (first branch) is only exposed to the adversarial objective and the LORA branch (second branch) is only exposed to the natural objective. The paper claims that the disentanglement avoids gradient divergence and leads to better downstream robustness.

### Strengths
* **Clear presentation**: the paper uses clear and concise notations for equations. The method section is easy to follow.

* **Good ablation study**: the paper conducts ablation study on important hyper-parameters such as the rank in LORA and the LR scheduler.

### Weaknesses
* **Missing ablation on Equation 5**: Equation 5 is the main loss function of the proposed method, which has three terms. The second cross-entropy term is a new addition $L_{KL}(h_{\theta}(\tilde{x}),y)$ in this paper and is not motivated and ablated in the experiments.  
* **Doubt on mitigating divergence**: a main motivation of the method is that it can avoid divergent gradient updates on the main model parameters. However, this is not validated through experiments explicitly. For example, even though the main model parameters are not directly trained on the natural objective, it is indirectly affected by the natural objective through the KL divergence. Moreover, the unexplained second cross-entropy term $L_{KL}(h_{\theta}(\tilde{x}),y)$ can be seen as a natural objective on perturbated input. 
* **Why parameter-free**: the claim on parameter-free can be confusing. The model not only fine-tunes the main model parameters but also additional LORA parameters. So, it is not parameter-free in the sense of fine-tuning. Even though the method reduces the need for extensive hyper-parameter tuning, the design choices of the automated scheduler and the rank selection for LORA are all hyper-parameters. It’s not clear what aspect of the proposed method is parameter-free.

### Questions
* Could the authors provide the cosine similarity between the two terms in the adversarial objective in Equation 5 and comment on the functionality of the second cross-entropy term $L_{KL}(h_{\theta}(\tilde{x}),y)$? 

* Could the authors clarify the parameter-free characteristic? It could be that I misunderstood the meaning here.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces AutoLoRa, an automated robust transfer learning framework. The authors present empirical evidence showing a significant divergence in the gradients of adversarial and natural objectives with respect to the feature extractor (FE), leading to unstable optimization. This observation motivates the authors to propose an auxiliary low-rank (LoRa) branch to disentangle the robust fine-tuning process, enabling the optimization of natural objectives through the LoRa branch and adversarial objectives through the FE.

Additionally, the authors introduce automatic schedulers for adjusting the learning rate and loss weights. The empirical results demonstrate that AutoLoRa achieves state-of-the-art robustness in downstream tasks without the need for hyperparameter search.

### Strengths
1. The paper is well-organized and well-written, making it easy to follow most parts of the paper.

2. The proposed method is well-motivated. The authors empirically discover that optimizing the natural and adversarial objectives leads to divergent optimization directions, which serves as the motivation for the LoRa branch.

3. The comprehensive results across various datasets provide strong support for the effectiveness of AutoLoRa.

4. AutoLoRa is parameter-free, offering practical utility. Additionally, the automated learning scheduler is adaptable to different methods.

### Weaknesses
1. The backbone models are pre-trained through robust supervised learning. It would be beneficial to demonstrate the performance of various backbone models pre-trained using robust self-supervised learning with AutoLoRa.

2. Robustness is currently assessed using AutoAttack. It would be more informative to assess the robustness under various attackers.

### Questions
Refer to Weaknesses.

### Soundness
3 good

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
Robust fine-tuning (RFT) is an efficient method to obtain a robust model on a downstream task by robustly fine-tuning a robust model that is adversarially trained on a large dataset. 
However, this paper shows that the existing methods (vanilla RFT, TWINS [Liu et al. 2023]) suffer from the same issue that optimizing both adversarial and natural objectives yields significantly divergent gradient directions.
This paper points out that this divergence can hinder obtaining high robustness and make the training unstable.

To resolve the issue of the divergent gradient directions, this paper proposes a robust fine-tuning framework called AutoLoRa using the low-rank adaptation (LoRA) technique. 
The idea is to have separate branches for adversarial and natural objectives: the adversarially pre-trained encoder is trained by the adversarial objective, and the LoRa branch is trained by the natural objective.

Additionally, AutoLoRa introduces automatic scheduling of hyperparameters, in contrast to vanilla RFT and TWINS, which require expensive hyperparameter searches. The balance between adversarial and natural objectives is determined by natural accuracy on the train set: as the standard accuracy increases, the weight on the natural objective decreases. The learning rate decays automatically with a condition of the validation accuracy.

In this paper, the pre-trained models are adversarially trained on ImageNet-1k. 
On the six downstream datasets (CIFAR10, CIFAR100, DTD-57, DOG-120, CUB-200, and Caltech-256), AutoLoRa achieves higher adversarial robustness compared to vanilla RFT and TWINS.

### Strengths
S1. This paper points out the common issue of vanilla RFT and TWINS [Liu et al. 2023] that optimizing both adversarial and natural objectives yields significantly divergent gradient directions, which is beneficial knowledge for the adversarial robustness research community.

S2. The application of LoRA for the adversarial robustness problem is novel, and separating the branches for adversarial and natural objectives with the low-rank branch is interesting. The results show that their method can effectively improve adversarial robustness.

S3. The proposed automatic strategy to determine hyperparameters is useful since adversarial training is time-consuming.

### Weaknesses
W1. A more careful ablation study is needed.

- (W1-1.) It remains unclear how much each of the two proposed components contributes to the performance: (1) the automatic hyperparameter scheduling and (2) the LoRa branch. To clarify, does AutoLoRa without automatic scheduling (utilizing grid search) yield a similar result to AutoLoRa with dynamic hyperparameter scheduling? In other words, does the dynamic hyperparameter scheduling contribute to the robustness improvement, or is it only for avoiding grid search? 

- (W1-2.) In line with (W1-1), it is also not evident how significantly the learning rate scheduling and the scalar parameter ($\lambda$) scheduling impact performance. While it appears that dynamic learning rate scheduling might not have the benefit of improving robustness, as seen in Table 5, I assume that dynamic scalar ($\lambda$) scheduling could contribute positively to performance, in addition to the benefit of avoiding grid search.

W2. The paper's claim regarding divergent gradient directions and training stability needs clarification.

- (W2-1.) The paper lacks evidence to support the claim that Vanilla RFT and TWINS are sensitive to hyperparameters. It would be helpful to specify which hyperparameters these methods are sensitive to and to what extent.
- (W2-2.) Since AutoLoRa employs automatic hyperparameter scheduling, it remains unverified whether the use of the LoRa branch indeed contributes to training stability regarding hyperparameters. To discuss the hyperparameter sensitivity, I would expect experiments comparing the different magnitudes of a specific hyperparameter and the corresponding performances for compared training methods.

W3: Natural accuracy trade-off in AutoLoRa compared to TWINS.
- For all cases in ResNet-18 and the three cases in ResNet-50, AutoLoRa exhibits a slightly lower natural accuracy compared to TWINS, despite achieving higher robust accuracy. Further discussion or insights on this trade-off would be valuable.

### Questions
Q1. Related to W1-2, it's worth considering the possibility of applying automated hyperparameter scheduling to Vanilla RFT and TWINS.   The scaler $\beta$ in Vanilla RFT or $\gamma$ in TWINS can be scheduled, by simply replacing $\lambda_2$ with $\beta$ or $\gamma$ in Equation 7. It would be interesting to see whether "Vanilla RFT + scaler scheduling" or "TWINS + scaler scheduling" can be better than the original methods. Additionally, comparing "Vanilla RFT + scaler scheduling" or "TWINS + scaler scheduling" with AutoLoRa could provide insights into the benefits of the LoRa branch.

Q2. How exactly is the gradient similarity calculated? A feature encoder has multiple layers to measure the gradient similarity. 

Minor comment:
- It appears that TWINS in this paper corresponds to the TRADES version of TWINS, known as TWINS-TRADES [Liu et al. 2023]. It might help clarify the paper's context by explicitly mentioning this relationship.

-------
[Liu et al. 2023] Twins: A fine-tuning framework for improved transferability of adversarial robustness and generalization. CVPR2023

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**Summary Of The Paper:**

This paper introduces AutoLoRa, a parameter-free automated robust fine-tuning framework to improve adversarial robustness in downstream tasks that disentangles the optimization process into two distinct components: (1) optimizing natural objectives via the LoRa branch, (2) and adversarial objectives via the FE. It addresses the issue of divergent gradient directions, when optimizing both adversarial and natural objectives through the feature extractor (FE), in existing robust fine-tuning methods and achieves state-of-the-art results across various tasks without the need for hyperparameter tuning.

### Strengths
**Strength:**

-   The motivation that optimizing both adversarial and natural objectives through feature extractor yields divergent gradient directions make sense. The proposed disentangling of the training objective by introducing the LoRA branch is consistent with the motivation.
-   Extensive empirical evaluation (including the P-test) demonstrates the improvements in Robust Fine-Tuning on various tasks.

### Weaknesses
**Weakness:**

-   The reason for automating scheduling hyper-parameters is not well illustrated, and the ablation study in Table 5 can not show its superiority, especially for the *RA* metric.
-   In Formula 7, the constant factor $6$ is not well-explained, and it could be considered as a hyper-parameter with further ablation study.
-   Table 4 is confusing. Specifically, when the adversarial budget is set to $8$ which is the default configuration, the resulting metric is supposed to be that in Table 2. However, this is not true.
-   Typo in Section 5.2 Ablation Study, the end of adversarial budgets paragraph says "consistently achieves consistently".
-   Diverse network backbone architectures are encouraged to be considered beyond ResNet.

### Questions
Refer to the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
