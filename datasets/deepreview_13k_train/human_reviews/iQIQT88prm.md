# Adversarial Machine Unlearning: A Stackelberg Game Approach

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
This paper focuses on the challenge of machine unlearning, aiming to remove
the influence of specific training data on machine learning models. 
Traditionally, the development of unlearning algorithms runs parallel with that of membership inference attacks, a type of privacy threat to determine whether a data instance was used for training. 
Recognizing this interplay, we propose a game-theoretic framework that integrates the attacks into the design of unlearning algorithms.
We model the unlearning problem as a Stackelberg game, introducing a two-player dynamic: a defender striving to unlearn specific training data from a model, and an attacker employing membership inference attacks to detect the traces of the data.
Adopting this adversarial perspective allows the utilization of new attack advancements,  facilitating the design of unlearning algorithms.
Our framework stands out in two ways. First, it enables the exact implementation of advanced membership inference attacks, providing verification for the effectiveness of unlearning. Second, it enables differentiation through optimization problems of attacks, making the framework readily integrable into end-to-end learning pipelines.
We present extensive experimental results to validate the efficacy of the proposed framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In summary, the paper presents a novel approach to machine unlearning by framing it as a Stackelberg game where a defender aims to remove specific training data from a model while an attacker uses MIAs to detect traces of the data. This approach combines the fields of machine unlearning and MIAs and leverages gradient-based techniques to enhance the unlearning process, ultimately providing a more robust and effective solution.

### Strengths
The proposal of a Stackelberg game framework for addressing the problem of machine unlearning is a notable originality. Using game theory to model the interaction between the defender and attacker in the unlearning process adds a new dimension to this research area. This framework allows for a systematic and strategic approach to unlearning.

The use of implicit differentiation to design a gradient-based solution method for the game is another novel idea. This enables more efficient and effective optimization of unlearning, making it amenable to end-to-end pipelines.

### Weaknesses
1. The authors need to further clarify the selection of metrics and justify how they can benefit real-world applications. This should goes back to the objective of machine unlearning. The objective of machine unlearning is to to negate a subset of data’s influence on the model. The goal should be maintaining a high performance of the model while erasing the imprint of the data from the model. Hence, if I understand it correctly, the performance should be as high as possible regardless of the retraining performance as long as the effectiveness of the unlearning is acceptable.

2. The authors consider the setting where the forget set is randomly sampled. First, It is not clear to me why this assumption will hold in real-world scenario when the machine unlearning is motivated by regulations in certain geographical regions. Second, if the forget set is randomly sampled, from a statistical point of view, the problem of machine unlearning becomes the problem of understanding how training dataset size can affect the model performance (the difference between the original performance and the retraining performance).

3. In the empirical results, the authors only demonstrated the effectiveness of the framework. The missing piece is the effectiveness of the proposed gradient-based method. It seems that the paper is lack of demonstration on which point the gradient-based method is converging to. For example, how the utilities of both players evolve during the training process? And which solution concept the algorithm is converging to if it is converging?

### Questions
My questions are left in the "Weaknesses" section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel framework for machine unlearning, which aims to remove the influence of specific training data from machine learning models。

### Strengths
•	It introduces a game-theoretic approach that integrates membership inference attacks (MIAs) into the design of unlearning algorithms, enhancing the robustness and reliability of unlearning.
•	It develops a gradient-based algorithm that uses implicit differentiation and differentiable optimization to solve the game, allowing for easy integration into end-to-end pipelines.
•	It validates the effectiveness of the framework and algorithm on two image classification datasets, showing a balanced trade-off between model utility and unlearning effectiveness.

### Weaknesses
•	It does not provide any theoretical analysis of the game, such as convergence, complexity, or optimality guarantees or discussions.
•	It does not consider multiple attackers or multiple attack methods, which may pose stronger or more stealthy threats to the unlearning process.
•	It does not conduct experiments on more datasets or more complex models, to demonstrate the generalization and scalability of the framework and algorithm.

### Questions
Please address the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel machine unlearning method, Stackelberg game (SG) unlearning, which integrates membership inference attack (MIA) into the unlearning algorithms. Specifically, the MIA strives to distinguish forget samples from test samples using outputs generated by the unlearned model. Conversely, the primary objective of the unlearned model is to confound the MIA's attempts to make such distinctions. Then, implicit function theorem is leveraged to solve the SG unlearning with gradient-based solution that fits into end-to-end pipelines. Experiments on CIFAR10 and CIFAR100 show the effectiveness of the proposed SG unlearning method.

The main contribution is that this work proposes to integrate MIA into the design of unlearning, offers a refreshing adversarial perspective to the realm of machine unlearning.

### Strengths
- The proposed method SG unlearning is intriguing and novel from my perspective. While the idea of integrating attacks into a defensive framework is not original, this method offers a fresh angle for machine unlearning.
- Addressing the unlearning problem is crucial.

### Weaknesses
 - Details of the proposed method is not clear.
    - Regarding Eq.(5), what is the precise formulation for $f$? Do the stationarity conditions account fo $\nabla V(\tilde{D}_{\theta_u}^{tr}; \theta_a^{'})$? It would enhance comprehension if the complete equation for $f$ were explicitly presented.

- The manuscript could benefit from more meticulous notation for clarity.
    - In Eq.(4), should $D_{\theta_u}$ actually be $D_{\theta_u}^{val}$? Alternatively, is it meant to be $\tilde{D}_{\theta_u}^{tr}$?
    - In Section 5, when referencing $n$ as indicative of size, is this referring to the size of the attack model parameters?
    - For example, in Section 3, $i$ in $(x_i, y_i)$ denotes the indices, it might be more clear to use $(x_j^f, x_j^f)$ rather than $(x_f^j, x_f^j)$.

- Missing details in the experiments and unconvincing results.
    - All experiments only consider the setting where the forget set is randomly selected, accounting for 10% of the training data, and only employs ResNet-18. A broader set of conditions (e.g., 20% forget set, class-specific forgets, poisoned sample forgets, and varying network architectures) would have enriched the analysis. The lack of experiments on class-wise unlearning is a significant limitation, as this is a common scenario in machine unlearning [2,3]. Furthermore, the paper does not explore the impact of forgetting poisoned samples, which is another crucial aspect of machine unlearning [5].
    -  What number of epochs is used for the retrained models? And what additional computational overhead does the MIA introduce? It would have been better if these could be provided to show the efficiency. The paper lacks a detailed analysis of the computational cost associated with the proposed method, particularly the overhead introduced by the MIA. This makes it difficult to assess the practical applicability of the approach.
    - How does the unscrubbed model perform? Also, results in tables for method like FF and IU fail to unlearn, how these methods perform with increased noise level? The paper should provide the performance of the unscrubbed model on the test, retain, and forget sets to establish a clear baseline. Additionally, the behavior of FF and IU under varying noise levels needs to be more thoroughly investigated, as the current results do not provide a complete picture of their limitations.
    - Considering the MIA is already integrated into the unlearning algorithm, KS and MIA metrics is quite related to the performance of MIA. Incorporating common metrics like Weight Distance [1], Activation Distance [2,3], Relearn Time [4] and Epistemic Uncertainty [5] might offer a more holistic performance view. The evaluation is limited by its reliance on metrics that are closely tied to the integrated MIA. The paper should include more diverse metrics, such as Weight Distance, Activation Distance, Relearn Time, and Epistemic Uncertainty, to provide a more comprehensive assessment of the unlearning performance.
    - Besides, it would be better if the loss/accuracy curve (from the retrained model and the proposed method) could be provided to show the convergence. The paper lacks a convergence analysis, which is crucial for understanding the behavior of the proposed method. Providing loss and accuracy curves for both the retrained model and the proposed method would help to address this concern. The theoretical evidence for convergence is also missing.
    - The literature review appears to overlook some recent developments in the field (e.g., [5-8]). It would strengthen the paper's comparative analysis if at least one contemporary method were included for benchmarking. The literature review is not comprehensive and omits several recent works in the field. The paper should include a comparison with at least one contemporary method to provide a more robust evaluation. It is also unclear how the proposed method compares to techniques that involve pruning [1].
    - Minor: FT seems achieve the best test acc. in tables.

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
