### Summary

This paper proposes a concept forgetting method, Label Annealing (LAN). The method is evaluated in a setting where a pre-trained model is fine-tuned on a dataset without a specific concept. The authors compare their method against three baselines and report better performance.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed approach is efficient on all experiments presented in the paper.
- The paper is well written and the method is clearly explained.

### Weaknesses

#### Some Related Works

[1] Pathologies of Neural Network Models and the Importance of Weight Decay in Optimization.
[2] Deep Learning versus Shallow Learning: A Large Scale Empirical Study.

#### comment

I have strong concerns regarding the evaluation of the proposed method.
- The authors evaluate their method by fine-tuning a pre-trained model on a dataset without a specific concept and compare it against three baselines. However, the paper does not report how the initial performance of the pre-trained model is affected when tested on data without the concept. It is expected that the performance would drop, but it is not quantified. This is important to justify why a complex method like the proposed LAN is needed. In addition, the paper does not report how the baselines perform on the same task of fine-tuning a pre-trained model on a dataset without a specific concept? It seems that the baselines were trained on the full dataset. If this is the case, it is not a fair comparison, since the proposed LAN is fine-tuned on a specific subset of the data.
- The authors should also report the baseline performance (on the full dataset) in Table 1, Table 2 and Table 3. This is important to quantify the performance drop when fine-tuning on data without a concept and to quantify how much the baselines degrade in performance when fine-tuning on the subset of the data without a concept. At the moment, the paper does not provide sufficient information to evaluate the trade-off between performance drop and concept violation.
- The authors should also report the results of the ablation study for more than one epoch. It is reasonable to assume that the results reported for one epoch are upper bounded and that the performance will drop for higher number of epochs. The generalization of the results of the ablation study is limited if only one epoch is evaluated. 
- The authors should also report the results of the proposed LAN for different number of fine-tuning epochs. At the moment, the paper only reports the results of LAN for a single epoch and for a specific learning rate. It is possible that the performance of the model will drop for different number of epochs or different learning rates.

I have additional concerns regarding the soundness of the proposed algorithm.
- The authors claim that their algorithm is computationally efficient. However, the algorithm requires the model to be trained for multiple epochs to achieve good performance. This is not computationally efficient, especially when compared to training the model from scratch on the full dataset. 
- The authors should also justify why the proposed algorithm converges. It seems that the proposed algorithm is an iterative algorithm that may not converge. In addition, the paper does not provide any theoretical guarantees on the convergence of the algorithm. This is a major concern, since the convergence of the algorithm is not guaranteed.
- The proposed algorithm seems to be very sensitive to the learning rate. The authors should provide a more detailed analysis of the sensitivity of the algorithm to the learning rate. At the moment, the paper does not provide sufficient information to evaluate the robustness of the algorithm to the learning rate.

Overall, I believe that the proposed method is not well evaluated and the soundness of the proposed algorithm is questionable. The paper does not provide sufficient information to evaluate the proposed method and the claims made by the authors are not well supported by the experimental results.

### Suggestions

The evaluation of the proposed method needs significant improvement to properly assess its effectiveness and justify its complexity. The paper should include a detailed analysis of the pre-trained model's performance on the full dataset, as well as on the subset of data with the concept removed. This is crucial to understand the baseline performance and the impact of removing the concept on the model's accuracy. Furthermore, the baselines should be evaluated under the same conditions as the proposed method, i.e., fine-tuned on the subset of the data without the specific concept. This would ensure a fair comparison and allow for a proper assessment of the trade-off between accuracy loss and concept violation. The current evaluation, which appears to compare baselines trained on the full dataset with the proposed method fine-tuned on a subset, is not adequate and makes it difficult to draw meaningful conclusions about the method's effectiveness. The paper should also include a more comprehensive ablation study, reporting results for more than one epoch to better understand the generalization of the findings. The sensitivity of the method to the learning rate should also be thoroughly investigated, as the current analysis is insufficient to establish the robustness of the algorithm.

To address the concerns regarding the soundness of the proposed algorithm, the authors should provide a more detailed analysis of its computational efficiency. The claim that the algorithm is computationally efficient is not well-supported, given that it requires multiple epochs of fine-tuning. A comparison with training the model from scratch on the full dataset would be beneficial to justify the efficiency claims. Furthermore, the paper should include a theoretical analysis of the convergence of the proposed iterative algorithm. The current lack of theoretical guarantees on convergence is a major concern, and the authors should provide a formal proof or a strong argument to support the claim that the algorithm converges. The paper should also include a more detailed analysis of the sensitivity of the algorithm to the learning rate, as the current analysis is insufficient to establish the robustness of the algorithm. The authors should explore a wider range of learning rates and provide a clear explanation of how the learning rate affects the performance of the algorithm. The current analysis only provides a limited view of the algorithm's behavior under different learning rates.

Finally, the paper should include the baseline performance of the pre-trained model on the full dataset in Tables 1, 2, and 3. This is essential to quantify the performance drop when fine-tuning on data without a concept and to quantify how much the baselines degrade in performance when fine-tuning on the subset of the data without a concept. The paper should also report the results of the proposed LAN for different numbers of fine-tuning epochs. The current results are limited to a single epoch and a specific learning rate, which is not sufficient to evaluate the generalization of the method. The authors should explore a wider range of epochs and learning rates to provide a more comprehensive evaluation of the proposed method. The paper should also include a more detailed analysis of the trade-off between accuracy loss and concept violation. The current analysis is insufficient to evaluate the effectiveness of the proposed method, and the authors should provide a more detailed analysis of the trade-off between these two metrics.

### Questions

Please refer to the "Weaknesses" section for my questions.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
