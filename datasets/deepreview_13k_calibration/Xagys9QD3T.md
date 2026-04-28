# Pseudo-Probability Unlearning: Towards Efficient and Privacy-Preserving Machine Unlearning

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 5, 3, 3

## Abstract
Machine unlearning—enabling a trained model to forget specific data—is crucial for addressing biased data and adhering to privacy regulations like the General Data Protection Regulation (GDPR)'s ``right to be forgotten." Recent works have paid little attention to privacy concerns, leaving the data intended for forgetting vulnerable to membership inference attacks. Moreover, they often come with high computational overhead. In this work, we propose Pseudo-Probability Unlearning (PPU), a novel method that enables models to forget data efficiently and in a privacy-preserving manner. Our method replaces the final-layer output probabilities of the neural network with pseudo-probabilities for the data to be forgotten. These pseudo-probabilities follow either a uniform distribution or align with the model’s overall distribution, enhancing privacy and reducing risk of membership inference attacks. Our optimization strategy further refines the predictive probability distributions and updates the model's weights accordingly, ensuring effective forgetting with minimal impact on the model's overall performance. Through comprehensive experiments on multiple benchmarks, our method achieves over 20\% improvements in forgetting error compared to the state-of-the-art. Additionally, our method enhances privacy by preventing the forgotten set from being inferred to around random guesses.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes an efficient machine unlearning solution, Privacy-Preserving Unlearning (PPU), that aims to minimize privacy leakage while maintaining model performance. The proposed algorithm is evaluated on two datasets and two deep neural network models, demonstrating its effectiveness in reducing the forget error on forgotten data. The paper provides a comprehensive evaluation of the algorithm and compares it with multiple baseline unlearning methods.

### Strengths
- The paper addresses an important problem of efficient and privacy-preserving machine learning and provides a practical solution.
- The evaluation covers two datasets, two models, and multiple baseline machine unlearning algorithms.

### Weaknesses
 - The proposed PPU algorithm seems to only work for deep neural networks and classification tasks and may not be applicable to other types of models or tasks.
- The optimization goal of the PPU algorithm could be wrong. The algorithm aims to maximize the forget error on forgotten data instead of minimizing the discrepancy between the original and unlearned models. This approach may lead to unintended consequences, such as the model becoming overly sensitive to the retained data or exhibiting unpredictable behavior on unseen data. The goal should be to minimize the difference in model parameters or output distributions between the original and unlearned models, while ensuring the model forgets the specific data.
- In the evaluation section, the retain error and forget error metrics could be further explained to provide more insights into the algorithm's behavior. For example, it would be helpful to understand how these metrics change with different sizes of the forget set or different levels of model complexity. A more detailed analysis of the trade-off between these two metrics would also be beneficial.
- There are many editing issues throughout the paper, such as typos, missing citations, and missing figures.

### Questions
1. Why does the proposed algorithm focus on minimizing the forget error on forgotten data instead of minimizing the discrepancy between the retrained and unlearned models?
2. Have you considered scenarios where the model's prediction confidence may not accurately reflect the sensitivity of the data?
3. What are the key factors that influence the trade-off between privacy preservation and model performance in the context of machine unlearning?
4. The proposed algorithm seems to only work for classification tasks and small datasets. How scalable is the proposed algorithm to large-scale datasets and complex models? How easy or difficult to adapt the proposed PPU to more challenging datasets or tasks, for instance ImageNet dataset, regression model, or generative model?
5. Can you provide more insights into the retain error and forget error metrics and how they reflect the unlearning algorithm's performance in different scenarios?
6. I do not see the forgot error comparison in Figure 3, and there is also no Figure 4 to support the claim that "According to Figure 3, PPU’s forget error is very close to that of retraining, particularly in the Lacuna-10 experiment, where it is the closest match. In the membership inference attack experiment, shown in Figure 4, PPU consistently achieves nearly 50% accuracy, indicating strong privacy preservation" in Line 408. Can you please check on this?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Pseodo-Probability Unlearning (PPU), a novel method that enables models to forget data efficiently and in a privacy-preserving manner. PPU replaces the final-layer output probabilities of the neural network with pseudo-probabilities for the data to be forgotten. The pseudo-probabilities are initialized from some distributions (e.g., a uniform distribution) and are further refined to maintain performance on the remaining data. Extensive experiments demonstrate the efficiency of PPU while preventing privacy leakage.

### Strengths
1. The idea of modifying the final-layer output probabilities of the neural network to pseudo-probabilities for machine unlearning is novel.
2. The paper is overall well-structured and generally easy to follow.

### Weaknesses
1. Adding an independent paragraph for contributions in the Introduction Section would be better.
2. The method SISA is considered to be exact unlearning.
3. Some typos. "Figure ?" on line 080. $\mathcal D_r$ and $D_{fog}$ on line 139. "The dual variables $\lambda_k$" on line 269. Missing space characters after $\lambda$s on line 478 and line 480.
4. Miss descriptions of Table 3 in the main text.
5. The font size of the text in the figures is too small.
6. Reuse of the notation $f$ for both the model and the forget set.
7. Experiments on larger datasets and networks (e.g., ImageNet) would be better.

### Questions
1. Should $\lambda_k$ in Section 4.2.2 be $\alpha_k$?
2. Should "retrain error" on line 485 be "retain error"?
3. What is $w_k$ in Equation 6?
4. The goals in Section 5.4 and Section 5.5 are different. Are the two goals contradictory? Can PPU achieve both of them simultaneously?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This research studies methods for achieving unlearning, which involves forgetting information about specific data from a trained model. In particular, it points out that with existing unlearning methods, it is possible to identify whether or not a piece of data has been unlearned by using a membership inference attack and that this can lead to privacy violations. This research proposes a method that enables unlearning while preventing such privacy violations. Specifically, the authors propose a method that not only makes it impossible to classify the data to be forgotten but also makes the output probability of the final layer when classifying the data to be forgotten to match a uniform distribution or a distribution with random probabilities for each class. They argue that this prevents privacy violations associated with unlearning. They also consider optimization methods for implementing such a method.

### Strengths
The perspective on privacy violations of unlearning through membership inference is important, and this paper introduces this perspective as a new contribution.

### Weaknesses
It is not sufficiently discussed whether the proposed method can indeed prevent privacy violations of unlearning through membership inference. In addition, there is no experimental comparison with other methods from this perspective.

The proposed method claims that if the probability output of the final layer is uniform or random, it can avoid membership inference. Is this true? It is unlikely that the probability output of the final layer is uniform by chance. Could it be evidence that the probability output of the final layer was the target of unlearning?

The same applies if the probability output of the final layer is random. If such randomness does not appear in any other test data, it is possible to infer that it is artificial randomness. To show that the data to be forgotten is not identified by membership inference, it may be necessary to show, for example, using statistical testing, that the probability output of the final layer for the data contained in the test data is statistically indistinguishable from the probability output of the data to be forgotten.

### Questions
The motivation for the proposed method in the introduction was the privacy violation in unlearning through membership inference. However, in the experiment, only test, retain and forget errors were evaluated. There was no experimental evaluation of privacy violations through membership inference. It is necessary to experimentally evaluate whether the proposed method is more robust against privacy violations through membership inference than other methods.

The proposed method claims that if the probability output of the final layer is uniform or random, it can avoid membership inference. Is this true? It is unlikely that the probability output of the final layer is uniform by chance. Could it be evidence that the probability output of the final layer was the target of unlearning?

The same applies if the probability output of the final layer is random. If such randomness does not appear in any other test data, it is possible to infer that it is artificial randomness. To show that the data to be forgotten is not identified by membership inference, it may be necessary to show, for example, using statistical testing, that the probability output of the final layer for the data contained in the test data is statistically indistinguishable from the probability output of the data to be forgotten.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper tries to solve the efficiency and privacy leakage of machine unlearning. The problem and topic is interesting and hot. I have some comments as follows.

Strengths: 1. The experiments and evaluation are sufficient.

Weaknesses:
1. The problem statement is not clear. In the introduction and abstract, the authors claimed that they aim to solve the efficiency and privacy leakage of machine unlearning. However, in the section 3, the problem definition section, it has not mentioned the definition related to the efficiency and privacy leakage problems in machine unlearning.

2. Regarding the privacy leakage in machine unlearning, the authors ignored the common attacks that compare the model difference before and after unlearning to implement inference attacks. To the reviewer's understanding, the proposed method is infeasible for these attacks in machine unlearning because the original model performs well on erased samples but now randomly predicts them, which is a huge difference.

3. The paper needs heavy proofreading. There are many typos, for example "Figure ??" in page 2.

### Strengths
1. The experiments and evaluation are sufficient.

### Weaknesses
1. The problem statement is not clear. In the introduction and abstract, the authors claimed that they aim to solve the efficiency and privacy leakage of machine unlearning. However, in the section 3, the problem definition section, it has not mentioned the definition related to the efficiency and privacy leakage problems in machine unlearning.

2. Regarding the privacy leakage in machine unlearning, the authors ignored the common attacks that compare the model difference before and after unlearning to implement inference attacks. To the reviewer's understanding, the proposed method is infeasible for these attacks in machine unlearning because the original model performs well on erased samples but now randomly predicts them, which is a huge difference.

3. The paper needs heavy proofreading. There are many typos, for example "Figure ??" in page 2.

### Questions
No additional questions.

### Soundness
2

### Presentation
1

### Contribution
1
