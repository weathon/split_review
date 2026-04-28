# Adversarial Attack Robust dataset pruning

- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 6, 6, 6, 5

## Abstract
Dataset pruning, while effective for reducing training data size, often leads to models vulnerable to adversarial attacks. This paper introduces a novel approach to create adversarially robust coresets. We first theoretically analyze how existing pruning methods result in non-smooth loss surfaces, increasing susceptibility to attacks. To address this, we propose two key innovations: (1) a Frequency-Selective Excitation Network (FSE-Net) that dynamically selects important frequency components, smoothing the loss surface while reducing storage requirements, and (2) a "Jointentropy" score for selecting stable and informative samples. Our method significantly outperforms state-of-the-art pruning algorithms across various adversarial attacks and pruning ratios. On CIFAR-10, our approach achieves up to 58.19% accuracy under AutoAttack with an 80% pruning ratio, compared to 42.98% for previous methods. Moreover, our frequency pruning technique improves robustness even on full datasets, demonstrating its potential for enhancing model security while reducing computational costs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new dataset pruning method aimed at enhancing model robustness against adversarial attacks. Through theoretical analysis, the authors find that existing pruning methods often lead to non-smooth loss surfaces, which increases the model's vulnerability to attacks. To address this issue, the paper introduces two key innovations: First, a Frequency-Selective Excitation Network (FSE-Net) that dynamically selects essential frequency components to smooth the loss surface and reduce storage requirements; second, a sample selection scoring based on "Joint Entropy," which selects stable and informative samples. Experimental results demonstrate that this method significantly outperforms existing pruning algorithms across various adversarial attacks and pruning ratios, showing its potential in enhancing model security and reducing computational costs.

### Strengths
1. **Frequency-Selective Excitation Network (FSE-Net):** By dynamically selecting essential frequency components, it smooths the loss surface, thus enhancing robustness against adversarial attacks while reducing storage needs, making it suitable for resource-limited devices.
2. **Joint Entropy-Based Sample Selection:** This method selects stable and informative samples based on their importance during training, improving both the robustness and performance of the pruned model.

### Weaknesses
1. Lemma 1 is critical, but in the derivation, the assumption that $\frac{\partial f_{\theta}(\tilde {x})}{\partial \theta}$ is bounded is overly restrictive and lacks supporting evidence, requiring a more rigorous mathematical proof. Specifically, while weight initialization schemes and bounded activation functions may prevent gradient explosion in standard training, it is not clear that these mechanisms guarantee boundedness under adversarial perturbations. The behavior of the gradient with respect to model parameters when the input is an adversarial example, $\tilde{x}$, needs to be explicitly addressed, as these perturbations can drastically alter the loss landscape and potentially lead to unbounded gradients, which would invalidate the lemma.
2. Appendix E lacks detailed structural information, providing only the structure names. The absence of specific layer configurations, activation functions, and parameter counts makes it difficult to reproduce the results or to fully understand the complexity of the Frequency-Selective Excitation Network (FSE-Net).
3. Pseudo-Code in the second line has a missing definition for \(\hat{X}_{i,j}\). This lack of definition makes it impossible to understand how the Discrete Cosine Transform (DCT) coefficients are used in the algorithm.
4. Equation 6 applies derivatives only to correctly classified samples. If the count of correct classifications decreases during updates, can incorrect samples still guide parameter updates? Otherwise, the function will only reinforce correct predictions without helping incorrect ones become correct. This raises concerns about the algorithm's ability to recover from poor initializations or during training phases where the model's accuracy temporarily decreases.
5. The terms "high energy" and "low energy" appear the first time without a precise definition. Without a clear threshold or method for determining what constitutes high or low energy, the algorithm's behavior becomes ambiguous and difficult to analyze.
6. Section 3.3 lacks clarity on how it integrates with previous algorithms (requires a flowchart or equivalent explanation). The paper does not clearly explain how the Frequency-Selective Excitation Network (FSE-Net) and the Joint Entropy-based sample selection interact, making it difficult to understand the overall methodology.

### Questions
See Weaknesses.

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
The paper explores dataset pruning in the context of adversarial attacks. Two techniques are used to improve robustness against adversarial attacks while reducing training time and storage requirements.

1) A new (joint-entropy) score is introduced for selecting samples

2) A ML model is applied to the images to prune particular frequency components. 

The result is the ability to defend against adversarial attacks, as well as adversarial training, but at a much lower cost.

Results are generated for a range of adversarial attacks (AA, PGD-20, C&W). AA also includes the gradient-free Square Attack. 

For CIFAR100
* Performance against AA when using adversarial training on the entire original dataset using TDFAT is 26.61%
* It is 17.92% using CCSFEM (coreset selection algorithm) with a 50% prune rate
* For the proposed learnable frequency (LF) pruning technique this is 23.41% with a 50% prune rate 
* And for both joint-entropy scoring for dataset prunng and LF (JELF) it is 22.85% with a 50% prune rate

### Strengths
Interesting exploration of the ability to prune datasets with adversarial robustness in mind and a frequency-component selection based technique for introducing low-cost adversarial robustness. Results indicate the ability to make significant savings without sacrificing a significant amount of robustness vs. state-of-the-art adversarial training techniques.

### Weaknesses
 * Some closely related work appears to be missing
* Small number of datasets explored

### Questions
Q1: Are any of the following considered as closely related work?
* Adversarial Coreset Selection for Efficient Robust Training (IJCV/ECCV’22)
https://arxiv.org/abs/2209.05785
* Less is More: Data Pruning for Faster Adversarial Training (AAAI-23 workshop, SafeAI)
https://arxiv.org/abs/2302.12366
* Adversarial training with informed data selection (EUSIPCO’22)
https://arxiv.org/abs/2301.04472
* Efficient Adversarial Contrastive Learning via Robustness-Aware Coreset Selection (NeurIPS’23)
https://arxiv.org/abs/2302.03857

Q2: There is also the Sabre work: https://alec-diallo.github.io/publications/sabre 
Is this related as it performs a spectral decomposition of the input and selective energy-based filtering?
(https://arxiv.org/html/2405.03672v3)

Q3: Could you comment briefly on the overall practicality of the technique, accuracy is still very low vs. adversarial samples?

Q4: When using LF (Ours-LF) to preserve 50% of the frequency components, what are the actual reductions in training data storage requirements results?

Q5: Do you have a similar table to Table 2 for CIFAR-100?

Q6: Have you considered an adaptive attack?

Q7: For larger datasets would the LF pruning approach still be feasible?

### Soundness
3

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
This paper proposes a method to enhance model robustness against adversarial attacks on pruned datasets. It first theoretically analyzes how existing pruning methods result in non-smooth loss surfaces. A learnable Frequency Pruning algorithm is proposed to smooth the model’s local minimum geometry. Besides,  it introduces a data importance score, based on analyzing variations in model logit entropy throughout the training process, to select a coreset. Experiments across various datasets and adversarial attacks are studied to demonstrate the efficiency.

### Strengths
1. This paper presents an efficient algorithm for data pruning in adversarial training settings. It achieves considerable robustness under AutoAttack while improving training efficiency by removing data points. The novelty and motivation of studying robustness against adversarial attacks on pruned datasets are interesting and helpful for the community.

2. Data selection from the perspective of the loss curvature and surface of neural networks is more in line with the essence of adversarial training.

3. Fltering frequency to enhance the effectiveness of data selection and the quality of the coreset for adversarial training is quite interesting.

### Weaknesses
1. The definition of Joint Entropy is confusing. It is mentioned in Abstract and Introduction, but I do not see it in the method section.

2. The definition of Reward Score on page 6 is confusing.

3. The paper introduces the FSE-Net to extract different frequency components. Its structure and impacts on robustness and clean accuracy should be discussed.

4. I am confused about the relationship between JE, JELF, LF. The author should provide more explanation (e.g., is the Joint Entropy estimated before/after/by the FSE-Net?, what is the relationship between the FSE-Net and the Target Network?)

5. There is a lack of comparison with "Adversarial Weight Perturbation Helps Robust Generalization, NeurIPS 2020", and "Theoretically Principled Trade-off between Robustness and Accuracy, ICML 2019", to evaluate the effectiveness of the proposed method on different optimization goals and loss curvature optimization.

6. The transferability of coresets selected by the proposed method across different architectures should be evaluated.

### Questions
1. There is no explicit definition of Joint Entropy. Does it refer to a combination of multiple scores (such as EL2N, GraND, etc.)?

2. The definition of Reward Score on page 6 is confusing. What is its relationship to Joint Entropy? What is the exploration phase? What is the exploitation phase?

3. Does the effectiveness vary with different optimization goals and loss curvature optimization (e.g., "Adversarial Weight Perturbation Helps Robust Generalization, NeurIPS 2020", "Theoretically Principled Trade-off between Robustness and Accuracy, ICML 2019")?

4. As the proposed method selects a coreset from the training set, I am curious about its transferability (e.g., selected by ResNet-18, trained on ViT).

5.The relationship between JE, JELF, LF is unclear; could the author provide more explanation? (e.g., is the Joint Entropy estimated before/after/by the FSE-Net?, what is the relationship between the FSE-Net and the Target Network?)

### Soundness
2

### Presentation
2

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
This paper explores how current data pruning methods, specifically Random, Entropy [], and CCSFEM [],  affect the ResNet-18 model on CIFAR-10 and CIFAR-100 and the ResNet-34 model on Imagenet-1K against adversarial attacks. Namely AutoAttack,  PGD-20 and C&W attacks. The paper shows that the current data pruning methods result in poor performance against adversarial attacks, especially for high percentages of dataset pruning, and that can be attributed to the non-smooth loss landscapes around the minima. Therefore, a new dataset-pruning method is introduced that uses a Frequency Selective Excitation Network (FSE-Net) that selects important frequency components to smooth the loss landscape and a Joint-Entropy score for selecting samples. This new method can generate a corset that, when used for training, results in more accurate models under adversarial attacks than current data pruning methods. This new method also reduces the computational costs of training.

### Strengths
Well motivated paper and problem- clearly shows how current data pruning methods do not account for adversarial attacks, providing a new lens to evaluate data pruning. 

Breadth of Experiment: The CIFAR-10, CIFAR100 and Imagenet1K dataset are used to demonstrate the effect of data pruning on adversarial attacks

Theoretically motivated method, highlighting that insights from theory can lead to better methods.

### Weaknesses
 **Qualitative Results:**

Line 187-188: "Frequency pruning removes textural details while preserving key shape features, helping the model focus more on shape, as shown in Fig. 1." Figure 1 does not clearly show this; how were these examples selected? Could you better explain how this figure demonstrates how it makes the model focus more on shape than textural details?

Figure 2 is qualitative, mainly as smoothness is not defined; I presume that the smoothness of the overall landscape is from -1 to 1 (x-axis). This could be significantly improved by providing a quantitative measure for smoothness to allow for more comparable measures. For example the average gradient magnitude or curvature.

These loss landscape figures are not averaged, and given that, there can be quite different results depending on the random directions used to generate the plots. See A.4 in [1]. Plotting the average loss landscape from 5 runs along with the standard deviation would help further the position that smoothness and adversarial robustness are linked.

**Lacking Averages:**

Throughout the paper, averages and standard deviations are missing; this significantly hampers the results and does not follow best practices. Could you provide an average from 5 runs.

**Magic numbers:**

The reason for the values chosen for $\epsilon$, learning rate, and number of iterations is not explained or justified within the experimental setup. Could you explain and justify each key hyperparameter choice, and describe any hyperparameter tuning process you may have used. Why on Imagenet did you use **1000** randomly selected points from the validation set for AutoAttack? What analysis did you use to determine that **1000** points were sufficient to get representative results?

**Clarity:**

Currently, Tables, specifically 1 and 3, are complex to read. From what I understand, the other methods result in worse performance against the Attack methods. However, your methods can outperform the baseline models (trained on 100% of the training dataset). If I have correctly interpreted the results, having the tables show the difference from the baseline method would be more precise. This will make it more straightforward that your method improves the adversarial robustness.

Training setup is not clearly explained; see lines 364-365: "All datasets were normalized before feeding into the models, and standard data augmentations were applied" This is fine within the body. However, I expect a link to the appendix that explains this in detail to ensure this is reproducible.

**Limited Evaluation:**

The experiments only utilise ResNet18 on CIFAR10 and CIFAR100 and ResNet34 on Imagenet1K. It is unclear why the architecture was changed for  Imagenet1k. What was the reason? To further improve the results and align better with the results motivation of resource-constrained environments, I expected the MobileNet, Shuffflenet and EfficientNet to be explored. These results are necessary for the impact of the paper, as it is unclear if it can be extended to other architectures.

**Minor Points:**

Figures 3b and c have black lines that are not explained.  
Line 55: double full stop at the end of the sentence nor is the section of the  Appendix stated.
Line 178: Generation error is not defined, I presume you mean Generation loss.

### Questions
See questions in weaknesses above. More concretely: 

1. Why are the mean and standard deviation not presented? At least 3-5 runs should provide adequate evidence for the findings.
2. Could the magic numbers be explained? Why are they selected and used? What is the justification?
3. Could further models be explored, for example, MobileNet, or ShuffleNet?
4. Why was ResNet18 only explored on CIFAR10 and CIFAR100?

If these questions are reasonably addressed, I will happily increase my score.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach to creating adversarially robust coresets. There are two main innovations:  1) a Frequency-Selective Excitation Network that dynamically selects important frequency components and 2) a “Joint-entropy” score for selecting stable and informative samples.

### Strengths
1. This paper proposes a novel approach to train a robust model
2. Compared to adversarial training, this method reduces the size of the training set and does not rely on any specific adversarial attack, thereby improving the training efficiency

### Weaknesses
1. I am not convinced that the model trained on some carefully selected and augmented data can be robust to adversarial attacks. Unlike adversarial training, this method does not rely on any specific adversarial attack. Therefore, it is suggested to conduct a more comprehensive evaluation of your method on different attacks, such as l2-AA [1], l1-AA [2], and sAA (l0-bounded perturbations) [3], compare the results to baseline methods to further demonstrate the effectiveness of your method.

2. Line 58-59: If I understood correctly, FSE-Net is used to select important frequency components, so it is more like a data augmentation or purification method. However, it does not reduce the training samples or the size of the images. In this regard, why do you claim that FSE-Net can reduce storage requirements? You should provide a detailed explanation or quantitative analysis of how selecting frequency components translates to reduced storage needs.

3. Line 93-94:  Stutz et al. (2021) and Liu et al. (2020) establish a correlation between loss landscape flatness and adversarial robustness in the context of **adversarial training**. However, the training data are not perturbed in your method. You need a more extensive theoretical/numerical analysis of the relationship between loss landscape flatness and adversarial robustness in your context. For example, you can plot the adversarial loss landscape in both input and parameter spaces for your method (refer to Figure 4 in Stutz et al. (2021), and Figure 3 and 12 in Liu et al. (2020))

4. As illustrated in Figure 3 (b) and (c), it seems that the model is trained on the coreset (50% of the the original dataset) for 500 epochs. In Appendix B, you mentioned that the model is trained on the whole dataset for 200 epochs. Although the dataset becomes smaller, the total computation remains unchanged or even increases. Therefore, the "Time per epoch" you adopted in Table 2 is inappropriate since it cannot reflect the actual training time. You should clarify the number of epochs used for training on the full dataset vs. the coreset. If you use the same epoch in Table 2, you should indicate it in the title. 

5. From a qualitative perspective, you should visualize some images generated by FSE-Net and those selected by JE-score, and give a brief analysis of them, highlighting how the processing affects image characteristics and potential implications for model robustness.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2
