# Using Interleaved Ensemble Unlearning to Keep Backdoors at Bay for Finetuning Vision Transformers

- Decision: Reject
- Scores: 5, 8, 3, 6

## Abstract
Vision Transformers (ViTs) have become popular in computer vision tasks. Backdoor attacks, which trigger undesirable behaviours in models during inference, threaten ViTs' performance, particularly in security-sensitive tasks. Although backdoor defences have been developed for Convolutional Neural Networks (CNNs), they are less effective for ViTs, and defences tailored to ViTs are scarce. To address this, we present Interleaved Ensemble Unlearning (IEU), a method for finetuning clean ViTs on backdoored datasets. In stage 1, a shallow ViT is finetuned to have high confidence on backdoored data and low confidence on clean data. In stage 2, the shallow ViT acts as a ``gate'' to block potentially poisoned data from the defended ViT. This data is added to an unlearn set and asynchronously unlearned via gradient ascent. We demonstrate IEU's effectiveness on three datasets against 11 state-of-the-art backdoor attacks and show its versatility by applying it to different model architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presented Interleaved Ensemble Unlearning (IEU), a method for finetuning
clean ViTs on backdoored datasets. IEU includes two stages, where the first one is designed to train a shallow ViT used to block potentially poisoned data and the second stage defends backdoor attacks utilizing unlearning. The experiments demonstrate that IEU out-performs existing defenses on diverse datasets and backdoor attacks.

### Strengths
-	The two-stage method is reasonable, especially, using a shallow model to learn shortcuts in the dataset in the first stage. 
-	The experiments show that IEU performs better than existing methods, including I-BAU and ABL. Besides, the ablation studies are well-organized, illustrating the necessity of designs in IEU.

### Weaknesses
 - The novelty is limited. The proposed IEU utilizes the unlearning strategy for backdoor defense. Compared to ABL, the main differences lie in using a shallow model to block potentially poisoned data and a confidence threshold to determine the unlearned samples rather than a fixed-sized unlearned set. Specifically, the use of a shallow model in the first stage, while effective, could be considered an incremental improvement over existing techniques. The core idea of using unlearning for backdoor defense has been explored in prior work, and the proposed method does not fundamentally deviate from this approach. The confidence threshold mechanism, although a practical addition, does not introduce a significant theoretical advancement. Further analysis is needed to clearly differentiate the proposed method from existing unlearning-based defenses and to highlight its unique contributions.

- I am confused as to why IEU is tailored to ViTs. According to my understanding, there is no customized design in IEU for transformer-like architectures. Also, the authors evaluate CNN models in Table 8. Hence, if I am correct, I recommend the authors revise the writing to highlight the universality of the proposed IEU. The paper currently overemphasizes the applicability to ViTs without providing sufficient justification. A more generalized description of the method's applicability to various architectures would strengthen the paper's impact.

- I suggest that Eq.2 could be further clarified in detail. If the logits for optimizing the objective in Equation 2 sometimes come from $f_p$, should the optimized parameters include $\theta_p$? The current formulation of Equation 2 is ambiguous regarding the role of $f_p$ and $\theta_p$ during the optimization process. A more detailed explanation of how the gradients are calculated and which parameters are updated in each stage would improve the clarity of the proposed method.

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Interleaved Ensemble Unlearning (IEU), a defense strategy designed to protect Vision Transformers (ViTs) (or any model in general) from backdoor attacks during the fine-tuning process.

The IEU approach uses a shallow ViT model as a 'poisoned module' to detect backdoored data and protect the main 'robust module,' which is fine-tuned on clean data sorted through the 'poisoned module'.
IEU operates in two stages: the first trains the poisoned module on backdoored data, while the second uses it to isolate potentially poisoned samples for unlearning by the robust module. By alternating between learning and unlearning, the IEU method mitigates the effects of poisoned images, maintaining high accuracy on clean data while effectively defending against backdoor attacks. 

Evaluation results on three datasets (CIFAR10, GTSRB, and TinyImageNet) demonstrate its competitive performance against other state-of-the-art backdoor defenses, especially for CIFAR10 and TinyImageNet.

### Strengths
- IEU provides a novel approach to mitigating backdoor attacks in ViTs by implementing a layered defense strategy that separates poisoned data using a shallow 'poisoned module'.

- The method’s two-stage process of alternating between learning and unlearning adds robustness against various backdoor attacks without relying on a pre-identified clean set.

- The paper provides comprehensive empirical evaluation against a wide array of backdoor attacks across multiple datasets (CIFAR10, GTSRB, and TinyImageNet), showcasing improvements in ASR reduction and maintenance of high clean accuracy on CIFAR10 and TinyImageNet.

- IEU demonstrates practical value, particularly in domains where ViTs are deployed for security-sensitive tasks, making it a valuable contribution to backdoor defense for ViTs.

- The paper also discusses the method's limitations (e.g., simple dataset, weak attacks, and instability) to provide insights into how to improve the method further in future works.

### Weaknesses
 - **Limited Explanations for reproducibility:** The article provides limited clarity in the explanations of the technical details, particularly in the specific architectures and configurations used for the 'poisoned module' and 'robust module', respectively. This provides limited insight into understanding the 'poisoned module,' which is the most important component of the proposed approach. Specifically, the paper lacks details on the number of layers, hidden dimensions, and attention heads used in the shallow ViT, making it difficult to reproduce the results. Furthermore, the specific training parameters for the poisoned module, such as learning rate, batch size, and optimizer, are not clearly stated, hindering reproducibility.

- **Generalizability to Complex Architectures:** It is unclear whether the proposed approach is generalizable to more complex ViT Architectures or is limited to standard ViT architectures. The paper does not explore the performance of IEU with deeper or wider ViT models, which are commonly used in practice. Further, while the approach is proposed specifically for the ViT, in theory, it can be applied to non-ViT-based models, improving the applicability of the proposed defense. The lack of experiments on other architectures limits the generalizability of the findings.

- **Limited insight on the limitations:** The article highlights the limitations and discusses them, providing insights on why the approach underperforms in certain cases. I am not strongly convinced that this is the only reason for underperformance (though it is minimal underperformance). For example, the authors argue that the GTSRB dataset is less complex than the other datasets evaluated, which is why underperformance happens. However, it is a failure case of a 'poisoned module' not to learn well enough to distinguish (as evidenced by Fig 2). Moreover, the Clean Accuracy is also lower, suggesting that $m_{\theta_p}$, which is directly related to the logits calculated by $f_p$, also affects the performance. Further, no insights have been provided as to why the poisoned module learn differently for the GTSRB dataset, nor have any suggestions on improving the training of the 'poisoned module' to prevent these failure cases. While I do not state that the approach should perform better for the GTSRB dataset natively, I think there is an oversight in identifying and discussing why the 'poisoned module' gives high enough logits for the poisoned images, which affects both Clean Accuracy as well as ASR directly.

### Questions
- Could the authors elaborate on the architectural choices for the shallow ViT used as the poisoned module?

- How does IEU perform on deeper ViT architectures for the 'poisoned module' not covered in the study?

I notice some sharp drops in ASR in Table 2. For Example, for ISSBA-CIFAR-10, the ASR is 100.00 for 0.2 and 0.0 for 0.5. Similar results can be for Smooth and Tiny ImageNet. Can the authors provide some insights on the sharp drops? This could provide better insights for future works to reproduce the results (or even improve).

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents Interleaved Ensemble Unlearning (IEU), a method aimed at defending Vision Transformers (ViTs) from backdoor attacks during fine-tuning on backdoored datasets. IEU employs a two-stage approach, using a shallow "poisoned module" ViT to filter potentially poisoned data and a "robust module" to learn clean data. In stage one, the poisoned module is trained to confidently predict backdoor-labeled data, while stage two involves using this module to identify and remove potentially backdoored data. This dynamic unlearning technique is tested on multiple datasets and against various attacks, showcasing IEU’s ability to improve attack success rate (ASR) and clean accuracy (CA).

### Strengths
1. The paper proposes a unique ensemble-based strategy specifically tailored for ViTs, addressing the scarcity of ViT-targeted backdoor defenses.

2. IEU is evaluated on diverse datasets (CIFAR10, GTSRB, TinyImageNet) and multiple backdoor attacks, providing extensive empirical data on performance improvements.

### Weaknesses
1. The presentation quality falls significantly short of the standards expected at a prestigious conference like ICLR. Readers without a strong background in vision transformers and backdoor attacks will likely struggle to follow the manuscript. Key background information, such as the concept of "unlearning", is notably absent. Additionally, Figure 1 presents mathematical notations to illustrate the proposed method, yet these notations lack sufficient explanation. For example, the symbol $\mathcal{D}^{ul}$ is used without clarifying its meaning.

2. Although the paper claims that IEU enhances ViT robustness against backdoor attacks, it lacks clarity on which specific design elements are tailored to address vulnerabilities unique to the ViT architecture. The method appears to treat ViTs as a generic architecture, without leveraging any specific properties of the attention mechanism or patch embeddings that might be more susceptible to backdoor attacks.

3. This paper lacks novelty. The ensemble strategy primarily relies on heuristic thresholds rather than introducing innovative designs. Additionally, Stage 1 does not present any novel contributions. The core idea of using a poisoned model to identify poisoned data is not new, and the method's reliance on a simple confidence threshold for filtering lacks sophistication.

### Questions
1. The proposed method heavily relies on the prediction of the poisoned module. What if the poisoned module itself is attacked by malicious users? How can the proposed method address this scenario?

2. The proposed method appears to be sensitive to the heuristic threshold $c_{thresh}$. How do the authors determine the value of the threshold?

### Soundness
2

### Presentation
1

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
Vision Transformers (ViTs) are increasingly used in computer vision tasks but are vulnerable to backdoor attacks that can compromise their performance, especially in security-sensitive applications. Existing backdoor defenses for Convolutional Neural Networks (CNNs) are not as effective for ViTs, and tailored solutions are limited.

To address this, the paper proposes Interleaved Ensemble Unlearning (IEU), a method for fine-tuning clean ViTs on backdoored datasets. In the first stage, a shallow ViT is fine-tuned to exhibit high confidence on backdoored data while maintaining low confidence on clean data. In the second stage, this shallow ViT serves as a "gate" to filter out potentially poisoned data from the defended ViT, which is then added to an unlearn set and asynchronously unlearned via gradient ascent.

The paper demonstrates IEU's effectiveness across three datasets against 11 state-of-the-art backdoor attacks and highlight its versatility by applying it to various model architectures.

### Strengths
- This paper explores a method for finetuning clean ViTs on backdoored datasets, Interleaved Ensemble Unlearning (IEU), giving a good reference to the research on this aspect.

- The proposed method IEU is simple but effective to achieve the defense, and the good performance obtained by the experiments strongly supports this point.

- The ablation study is organized well to clearly demonstrate the whole proposed method. And it makes the paper easy to follow.

### Weaknesses
 - I have some concerns regarding **the fairness of comparison with previous defense methods,** particularly due to the inclusion of the additional poisoned module, which involves an extra network for defense.

- The authors propose an effective framework of backdoor defense on ViT. It would be beneficial to consider a more realistic scenerio, where the attacker knows the existence of IEU and can generate a poisoned dataset to perform adaptive attacks. **It would be wonderful if the authors can design an adaptive attack for IEU and provide some experimental results.**

- I recommend conducting further experiments to assess whether BSD can successfully defend against backdoor attacks **with different target labels.** This could provide valuable insights into the robustness of the defense mechanism across various scenarios.

- There are existing backdoor defenses that focus on training clean models using poisoned datasets [1, 2], which could provide useful context for this research.

### Questions
Listed in the weakness of the paper.

Score can be improved if concerns listed above are resolved.

### Soundness
3

### Presentation
3

### Contribution
3
