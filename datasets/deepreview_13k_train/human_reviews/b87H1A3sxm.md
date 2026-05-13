# Enhancing Adversarial Robustness Through Robust Information Quantities

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
It is known that deep neural networks (DNNs) are vulnerable to imperceptible adversarial attacks, and this fact raises concerns about their safety and reliability in real-world applications. In this paper, we aim to boost the robustness of a DNN against white-box adversarial attacks by defining three new information quantities---robust conditional mutual information (CMI), robust separation, and robust normalized CMI (NCMI)---which can serve as robust performance metrics for the DNN. We then utilize these concepts to introduce a novel training method that constrains the robust CMI and increases the robust separation simultaneously. Our experimental results demonstrate that our method consistently enhances model robustness against C\&W and AutoAttack on CIFAR and Tiny-ImageNet datasets with and without additional synthetic data. Specifically, it is shown that our approach improves the robust accuracy of a DNN by up to 2.66\% on CIFAR datasets and 3.49\% on Tiny-ImageNet in the case of PGD attack and 1.70\% on CIFAR datasets and 1.63\% on Tiny-ImageNet in the case of AutoAttack, in comparison with the state-of-the-art training methods in the literature.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper develops a new regularizer for adversarial training (AT) by extending the work of Yang et al. (2023) and introduces three new information-based metrics: robust conditional mutual information (CMI), robust separation, and robust normalized CMI (NCMI). The authors theoretically and empirically demonstrate that adversarial robustness is inversely proportional to adversarial NCMI. Based on this insight, they design an objective function that combines the AT loss with an NCMI-based regularization term. To optimize this objective, they propose a relaxed alternating algorithm.

### Strengths
- The paper is technically sound, with the objective function being theoretically justified and proven.
- It shows improvement to white-box attacks.
- The paper is well-written and easy to follow.
- Experiments show improvement across the board.

### Weaknesses
 - While the improvement in results is consistent, it is often quite small. For example, the best AA accuracy for CIFAR-10 with WRN is improved by only about 0.25%.
- Given the iterative nature of the algorithm, it would be useful to know the time complexity of training relative to baseline methods.

### Questions
1. How does the training time compare to, say, TRADES?
2. Besides training time, are there other limitations or weaknesses of the method? For instance, how does it handle class imbalance?
3. Is the drop in natural accuracy expected (theoretically)?

Additional questions (not directly related to the paper but relevant to adversarial robustness):

4. Adversarial training (AT) is often limited to very small images, and the white-box accuracy is often too low for reliable deployment. Do the authors have any ideas on how to scale AT effectively?

5. Methods based on stable diffusion have shown significantly improved performance in adversarial robustness. Could the authors comment on how their approach compares to these methods, and whether diffusion-based techniques might complement or enhance their framework?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Inspired by the information geometry analyzed in the previous work, this paper proposes three advanced metrics which are robust CMI (Conditional Mutual Information, CMI), robust separation and robust NCMI (Normalized CMI, NCMI), where they can be incorporated into adversarial training methods for further enhancing the model’s robustness.

### Strengths
1. The mathematical analysis is adequate for enhancing the reliability. Detailed theoretical introductions in the paper and the supplementary materials demonstrate the feasibility of information theory in the adversarial robustness.

2. The consideration of the perturbation in the worst case for learning general robust features makes a rational extension for these metrics.

### Weaknesses
1. The Introduction lacks a clear and concise statement of the main problem that the proposed metrics aim to address. While the authors mention the susceptibility of data near the decision boundary, they do not explicitly connect this to the limitations of existing adversarial training methods. A more detailed explanation of how the proposed defense, specifically through robust CMI and robust separation, addresses this problem would significantly strengthen the motivation.

2. The rationale behind using the smaller WRN-28-10 model for the larger dataset containing synthetic data, as opposed to the larger WRN-34-10, is not adequately justified. The inconsistency in model capacity across different experiments raises concerns about the comparability of results and the generalizability of the proposed method. A thorough explanation of this choice, including potential trade-offs between model capacity, computational cost, and performance, is necessary.

3. The paper lacks a comprehensive ablation study analyzing the impact of individual components and hyper-parameters. While the proposed method combines robust CMI and robust separation, their individual contributions to the overall performance are not thoroughly investigated. An ablation study demonstrating the performance gains achieved by each component separately and in combination would provide valuable insights into the effectiveness of the proposed approach. Additionally, the sensitivity of the method to different hyper-parameter settings (e.g., $\alpha$ and $\beta$) should be systematically explored and reported.

4. The evaluation primarily focuses on robustness under L$_{\infty}$-norm attacks, while the generalization ability of the proposed method against L$_{2}$-norm attacks remains unclear. Including evaluations against specific L$_{2}$-norm attacks, such as PGD-L$_{2}$ and C\&W-L$_{2}$, would provide a more comprehensive assessment of the model's robustness across different threat models. This would strengthen the claim of improved generalization ability and demonstrate the practical applicability of the proposed method in various adversarial settings.

### Questions
While authors evaluate the robustness of the checkpoint with the highest validation accuracy, I wonder if evaluations from the last checkpoint can also be presented here. Besides, the authors can include a comparison of robustness results between the checkpoint with highest validation accuracy and the last checkpoint. This comparison could reflect the potential overfitting or the stability of the robustness gains over the course of training.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper uses CMI and normalized CMI (NCMI) to improve an established defense (adversarial training) against adversarial attacks. The authors take CMI, NCMI and robust separation as three measurements to quantify the robustness.
Extensive experiments are conducted to verify the effectiveness of the proposed method.

### Strengths
- This paper provides both theoretical and experimental results to support their statements.
- It is easy to follow the presentation of the paper.
- Incorporating CMI and NCMI into adversarial training.

### Weaknesses
 - The experimental improvement does not seem significant in Table 1 and 2. In a few cases, it even decreases more on clean accuracy compared to the increase in robust accuracy.
- This paper does not include enough baselines, only TRADES and MART are included. There are many papers that use MI to improve adversarial robustness, such as HBaR[1], VIB[2], and IB-RAR[3]. 
- Need more concrete ablation study, such as the different values of $\alpha$ and $\beta$ in equation(40). Specifically, the interaction between these two parameters needs to be explored, rather than just varying them independently.

[1] Revisiting Hilbert-Schmidt Information Bottleneck for Adversarial Robustness

[2] Deep variational information bottleneck

[3] IB-RAR: Information Bottleneck as Regularizer for Adversarial Robustness

### Questions
- How to choose the $\lambda$ value in equation(33)? Or how to choose the $\alpha$ and $\beta$ values in equation(40)?

- Why is the code for fixing random seeds in the GitHub page commented out? Given that the improvement is minor in Table 1 and 2, I would expect to see the variance or error bars (maybe only a part of the experiments due to high computation costs) to see if there are overlaps among error bars.

- What is the difference between the proposed CMI, NCMI, and CMI, NCMI in [4]?

I will increase my rating if my concerns are properly addressed.


[4] Conditional mutual information constrained deep learning for classification.

### Soundness
3

### Presentation
3

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
This paper introduces several new quantities to improve the model robustness, which can also serve as measures of robust performance. The paper provides theoretical proofs for the proposed theorems and uses experiments across multiple datasets to demonstrate the effectiveness for the proposed method against various types of attacks.

### Strengths
1. This paper is well-written and easy to follow.
2. The authors provide detailed proofs for the theorems proposed in this paper.
3. Experiments are conducted on multiple datasets, and the results outperform baseline methods in most scenarios.

### Weaknesses
1. The primary concern with this paper is its novelty. It appears to apply conditional mutual information from paper [1] to the field of model robustness, so a clearer explanation of the paper's novel contributions would be beneficial. Specifically, the paper should clearly articulate how the proposed robust CMI, robust separation, and robust NCMI differ fundamentally from the standard CMI, separation, and NCMI, beyond simply applying them in a robust setting. The distinction between optimizing for clean data versus adversarial data needs to be more explicitly addressed in the context of these information-theoretic measures.
2. The paper provides the model robustness results against white-box adversarial attacks. It would strengthen the evaluation if the black-box attacks also be included as a metric to assess the robustness of a model. The evaluation should include a wider range of black-box attacks, such as those based on transferability or query-based methods, to provide a more comprehensive assessment of the model's robustness in real-world scenarios.
3. Appendix F presents the adversarial results against different perturbation budget, it would be better if TRADES and MART are also included as baseline models in this figure. This would allow for a more direct comparison with state-of-the-art adversarial training methods across different levels of perturbation.
4. How are the default settings for hyper-parameters $\alpha$ and $\beta$ determined? The paper should provide a more detailed explanation of the hyperparameter selection process, including the range of values explored and the specific criteria used to determine the optimal settings. A sensitivity analysis of these parameters would also be beneficial.

### Questions
Please refer to the weaknesses section. Additionally, would it be possible to move the visualization and pseudo-code from the appendix to the main text.

### Soundness
3

### Presentation
3

### Contribution
3
