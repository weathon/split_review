# Long-tailed Adversarial Training with Self-Distillation

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Adversarial training significantly enhances adversarial robustness, yet superior performance is predominantly achieved on balanced datasets.
 Addressing adversarial robustness in the context of unbalanced or long-tailed distributions is considerably more challenging, mainly due to the scarcity of tail data instances. 
 Previous research on adversarial robustness within long-tailed distributions has primarily focused on combining traditional long-tailed natural training with existing adversarial robustness methods.
 In this study, we provide an in-depth analysis for the challenge that adversarial training struggles to achieve high performance on tail classes in long-tailed distributions.
 Furthermore, we propose a simple yet effective solution to advance adversarial robustness on long-tailed distributions through a novel self-distillation technique.
 Specifically, this approach leverages a balanced self-teacher model, which is trained using a balanced dataset sampled from the original long-tailed dataset.
Our extensive experiments demonstrate state-of-the-art performance in both clean and robust accuracy for long-tailed adversarial robustness, with significant improvements in tail class performance on various datasets.
We improve the accuracy against PGD attacks for tail classes by 20.3, 7.1, and 3.8 percentage points on CIFAR-10, CIFAR-100, and Tiny-ImageNet, respectively, while achieving the highest robust accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper improves model robustness against adversarial attacks in long-tailed learning. 

The authors observed that adversarial training, compared with normal training, further sacrifices minority class accuracy over majority classes. This observation is interesting and quite intuitive after some thoughts. It could be inspiring to further works. 

Based on this observation, the authors proposed to use stronger constrains than previous methods to balance the accuracy among different classes. Specifically, previous methods uses balance-aware loss functions to balance accuracy in long-tailed adversarial training. The authors added resampling (when training the teacher model), another common technique to handle data imbalance, on top of those previous works. The overall method is limited in technical novelty. 

Experimental results show good improvements over previous methods. The experimental settings raise some concerns to me. 

Overall, I think this is a marginal paper. I lean toward accepting primarily due to the good numerical results shown under the specific experiment setting used by this paper.

### Strengths
1. The observation that adversarial training further harms minority classes compared to normal training is interesting and may inspire further works. 

2. The performance gain under the specific experiment setting is good.

### Weaknesses
1. The technical novelty is limited. The two methods used to handle long-tail learning in this paper are resampling (when training the teacher model) and a balance-aware loss function proposed by previous works. The core idea of using a teacher-student framework for adversarial training is also not new, and the specific combination of these techniques lacks significant innovation.

2. The proposed method has a noticeable limitation: It requires to train a teacher model on balanced data. This greatly limits its practical application. In most cases, the powerful large model used as teacher models (e.g., foundation models downloaded from Hugging faces) are trained on real-world datasets which are typically unbalanced. It is very hard to get an off-the-shelf model that is "balanced". This requires the users to train the balanced model on their own. As a training algorithm, this is considerable complexity overhead. Moreover, it is not discussed in the paper how the teacher model could affect the distillation. Does the re-sampling method matter? Does the size of the teach model matter? Does the re-sampled dataset has to be perfectly balanced or it could have some imbalance? If it is the later case, how much imbalance it could have?

3. Table 5 is not interpretable. Which part is CIFAR10 and which part is CIFAR100?

4. The experiment setting is limited. The largest imbalance ratio is 50 for CIFAR10 and 10 for CIFAR100 and ImageNet. However, on both datasets, it is common to experiment with much stronger imbalance, with the ratio up to 100 [1]. Experimenting with stronger imbalance ratio is important since it is a more challenging case for re-sampling based methods. Under the stronger ratio, I assume the training of the teacher model would face difficulty cause the minority classes have few samples and simple up-sampling might not help too much.

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors first provide a theoretical analysis explaining why adversarial training leads to robustness degradation in tail classes. Motivated by these findings, they propose a simple empirical solution to mitigate this issue. Specifically, they employ a distillation-based approach in which a balanced version of the long-tailed dataset is used to adversarially train a teacher model. This teacher model is then used to train a student model on the original long-tailed dataset. The authors conduct experiments across multiple datasets and various settings, such as with and without augmentations, different imbalance ratios, and more.

### Strengths
The key strengths of the paper are:
- The paper is mostly written well.
- The authors conduct comprehensive experiments, as well as provide theoretical motivations.
- While the improvement methods use standard techniques like balanced softmax and indirect gradient matching, it's interesting to see that a simple prior distillation step enhances performance.

### Weaknesses
 - The concept of Imbalance Ratio in the paper is not well explained. While I understand how it applies to a binary setup, it’s unclear what an imbalance ratio of 50 means for CIFAR-10-LT compared to an imbalance ratio of 10. I suggest that the authors include the number of samples in the least populated class for clarity.
- Related to this, the core assumption is that training on a balanced dataset will enhance feature learning for the tail classes. However, the proposed method may negatively impact overall performance if the long-tail ratio is extreme (e.g., 5 samples per class). This could lead to ineffective training of the teacher network, and the distillation loss may then degrade performance. I would be interested to hear the authors' thoughts on this.
- Additionally, given the smaller sample size (especially for tail classes), it would be helpful to report the mean along with error metrics, such as standard deviation, and to conduct statistical tests to verify that the proposed method significantly improves performance compared to other methods.


### Questions
- Please see weaknesses and clarify the imbalance ratio better, and conduct statistical tests for comparison with other methods.
- It’s unclear why the authors report the AutoAttack accuracy on the whole dataset but not for the tailed classes. I would like to see the AutoAttack accuracy on the tailed classes for Figure 1 and all relevant tables.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a method to improve adversarial robustness on long-tailed distributions. The primary contributions include a two step adversarial training paradigm which involve, (i) adversarially training a teacher model on a balanced sub-dataset obtained from the original unbalanced dataset, and (ii) adversarially training a student model on the unbalanced original dataset using knowledge distillation from the teacher model and an additional balanced softmax loss. Another notable contribution is a theoretical analysis demonstrating how traditional adversarial training methods fail to improve robust accuracy of tail classes even when compared to non-adversarially trained methods.

### Strengths
- The authors effectively justify the need for adversarial training methods tailored to long-tailed distributions through their theoretical analysis (Section 3.2) and empirical evaluations (Section 3.3).

- An intriguing result is the observation that adversarial training unexpectedly reduces robust performance on tail classes compared to non-adversarial methods when addressing long-tailed distributions.

- The experimental results demonstrate substantial improvements in both clean and robust accuracy on tail classes, outperforming existing adversarial training (AT) methods such as TRADES, MART, and AWP, as well as long-tailed AT methods like RoBal, REAT, and AT-BSL.

- These performance gains are consistently observed across multiple datasets and architectural frameworks, highlighting the method's potential usability.

### Weaknesses
 - The paper does not sufficiently explain why their proposed method outperforms existing AT methods focused on long-tailed distributions. Particularly, why should Knowledge Distillation be a good choice for handling adversarial-robustness on long-tailed datasets?

- The incorporation of knowledge distillation (KD) and balanced softmax loss appears somewhat arbitrary. E.g., KD has been already explored for training of long-tailed datasets [1,2,3]; balanced softmax has been used in AT for long-tailed data [4,5]; KD for AT is explored in [6]. However, I agree that KD is not used for all AT and long-tailed datasets simultaneously. Hence, I would like to get a better justification of the proposed method for clarity.

- The absence of a dedicated subsection that develops a theoretical or intuitive motivation for the proposed method diminishes the overall impact and comprehensibility of the paper. Providing a more thorough theoretical framework or intuitive explanations would significantly strengthen the paper’s contributions and clarity.

- The proof of Lemma 1 in Appendix A needs to be a bit more rigorous and show how having equal weights minimizes the variance of $\sum_{k=1}^n w_k x_k + b$ using Cauchy-Schwartz, and hence minimises the natural error.

- Some inconsistency in the naming of the balanced dataset, throughout the paper, but specifically on page 6, line 317 onwards, notation shifts from D_b to D_B.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

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
The paper's main contribution is the two-phase adversarial training of deep neural networks (ResNet-18) on CIFAR 10/100 and TynyImageNet datasets. Phase one is training on a Balanced dataset (e.g., 30 epochs), and Phase two is the Knowledge distillation on the long-tailed imbalanced dataset to improve the robustness of the model on a long-tailed imbalanced dataset. 

For this contribution, the paper presents a theoretical analysis of Theorem 1, which says robustness training will further impact (worsen) the accuracy of models on long-tailed datasets. Most of the iterative analysis is in the part of the Appendix rather than the main part of the paper. The proof of Corollary indicates that it is trivial according to equations 4 and 5, which appears to indicate that the readers should figure it out themselves. 

The main results show improvement compared to some SOTA algorithms. The author's results are shown to be the best in all cases. A typical training set was used for these results.

### Strengths
The two-phase training methodology uses the "self-distillation" approach, where phase one is trained on balanced datasets, and this trained model is used for knowledge distillation in the second phase to make models robust on long-trailed datasets. The performance of this approach is shown to be better performance. That is, the results shown surpass the mentioned SOTA results on RestNet18.

### Weaknesses
Explain why the proof of the theorem is not generic for any iterative learning processes. Also, a step-by-step explanation of how the weight values affect robustness accuracy in the proof is required.

Include a visual or mathematical explanation connecting Figure 2 and Theorem 1 to clarify their relationship.

The definition of variables $\Phi$ and $r$ in Equations 4 and 5 are required.

For reproducibility, the authors should indicate the availability of codes in the experimentation section.

### Questions
Mention which dataset is used for  Figure 3. 

A comparison with balanced datasets to determine where adversarial training improves the performance of adversarial tests could be included in Figure 3. 

In Figure 3, at IR =1, explain why both natural and adversarial training produces the same test results on the adversarial test data. 

Explain what loss function is used for $L_{KD}$ in Algorithms 1were used.

### Soundness
3

### Presentation
2

### Contribution
3
