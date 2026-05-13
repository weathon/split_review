# Understanding the Robustness of Randomized Feature Defense Against Query-Based Adversarial Attacks

- Decision: Accept
- Scores: 8, 6, 6, 3

## Abstract
Recent works have shown that deep neural networks are vulnerable to adversarial examples that find samples close to the original image but can make the model misclassify. Even with access only to the model's output, an attacker can employ black-box attacks to generate such adversarial examples. In this work, we propose a simple and lightweight defense against black-box attacks by adding random noise to hidden features at intermediate layers of the model at inference time. Our theoretical analysis confirms that this method effectively enhances the model's resilience against both score-based and decision-based black-box attacks. Importantly, our defense does not necessitate adversarial training and has minimal impact on accuracy, rendering it applicable to any pre-trained model. Our analysis also reveals the significance of selectively adding noise to different parts of the model based on the gradient of the adversarial objective function, which can be varied during the attack. We demonstrate the robustness of our defense against multiple black-box attacks through extensive empirical experiments involving diverse models with various architectures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper showed that adding noises to some parts of models could protect the models from query-based attacks. The authors derived proofs to show that their method (adding noises) theoretically provided robustness to the models. Besides, they experimented this method with several datasets (Imagenet and CIFAR10) and models' architectures (i.e., ResNet50, VGG19, DeiT and ViT).

### Strengths
- The paper has a strong theoretical proof to show that the method can effectively provide robustness.
- The experiments are strong because the authors used Imagenet and CIFAR10 to show that their method and generalize in small and large datasets. Also, they tried with several models' architectures.

### Weaknesses
 - I understand that the paper focuses on black-box attacks, but in the experiment section, the authors may try evaluating models with white-box attacks as well.
- Please check the parentheses in equation (7).

### Questions
- In page 5, can you please give a reason for this sentence "We can observe that these ratios become higher when the data are perturbed toward the adversarial samples. In other words, the randomized model is more robust during the attack."?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to defend against black-box attacks by adding noise to intermediate features at test time. It is empirically validated effective against both score-based and decision-based attacks. The authors also provide theoretical insights on the proposed method.

### Strengths
1. The idea is straightforward, lightweight, and can be plugged into all existing defenses like adversarial training.
2. It is great to see the theoretical analysis for the defense method.
3. The paper is well-organized and easy to follow.
4. The authors do comprehensive experiments to study the effectiveness of the proposed method.

### Weaknesses
1. The motivation to inject feature noise is not clear compared to injecting input noise. "Unlike previous randomized defense approaches that solely rely on empirical evaluations to showcase effectiveness" is not correct, since RND also provides lots of theoretical analysis as the authors acknowledged in Sec. 2.3. The results are not significantly better than RND, but injecting feature noise requires a careful choice of the layer. Furthermore, the specific advantage of feature-space noise injection over input-space noise injection, in the context of black-box attacks, is not well-established. The paper should provide a more detailed comparison of the theoretical properties of these two approaches, clarifying why feature-space noise might be more effective or have different characteristics in this setting. The empirical results should also be more thoroughly analyzed to pinpoint the specific scenarios where feature noise provides a clear advantage.

2. The idea of injecting noise into hidden features is not novel, seeing Parametric Noise Injection: Trainable Randomness to Improve Deep Neural Network Robustness against Adversarial Attack, CVPR 2019. Although this is for defending against white-box attacks, adopting it for black-box attacks does not seem a significant contribution. The paper needs to clearly articulate the novel aspects of their approach compared to existing methods that use feature perturbation, even if the application domain differs. A more detailed discussion of the differences in methodology and the specific challenges addressed in the black-box setting is necessary to justify the contribution.

3. Does the proposed method have an advantage against AAA in defending score-based attacks? AAA is not designed for decision-based attacks, where the authors use AAA for comparison. The comparison with AAA is not entirely fair, as AAA is specifically designed for score-based attacks. The paper should provide a more comprehensive comparison against other defenses specifically designed for decision-based attacks, or justify the use of AAA in this context. The results should also be analyzed to determine if the proposed method provides a clear advantage over AAA in the score-based setting, or if the performance is comparable.

### Questions
Response to rebuttal: The authors provide a strong rebuttal and a good revision of the paper. My Q1 and Q3 have been well addressed, making me raise my score to 6. Although the method differs from the CVPR 2019 paper in Q2, the novelty is weak, i.e., perturbing feature to defend has been explored for a long time.

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
This paper investigates a well-known defense against black-box adversarial attacks (both score-based and decision-based) which involves adding a random noise to the input. The paper argues that the robustness-accuracy trade-off of such defense can be improved by adding noise to the intermediate layer instead. Theoretical and empirical analyses are provided to support this claim.

---

## Comment After Rebuttal

Once again, thank you so much for acknowledging and addressing my concerns! I appreciate your efforts.

Based on the new results (counting one successful attack query as a successful attack), there seems to be a minimal improvement from adding noise at the feature vs at the input. However, the result does show that the defense is effective in this difficult practical setting (~40% of samples are still correctly classified after 10k queries), and this convinces me that there are applications where this type of defense can be successfully applied.

I would really appreciate it if the author(s) could include this type of results and discussion (along with other suggestions during this rebuttal period) in the next revision of the paper. After reading the other reviewers' comments, I have no further concerns and have decided to adjust my rating from 5 to 6.

### Strengths
### Quality

The experiments are thorough, and the metrics are well-designed. Many models, datasets, and attack algorithms are included in the experiments. I like that the other baseline defense like AAA is also included. I also appreciate the comprehensive background section.

The paper also takes into account the nuance of picking the appropriate noise variance; they nicely solve this issue using the notion of the robustness-accuracy trade-off and pick the variance $\nu$ that results in a small fixed drop in the clean accuracy.

### Weaknesses
### Disadvantages of randomized models

I understand that the paper focuses on randomized models, but in practice, randomized models can be unattractive for two reasons:

1.  Its output is stochastic and unpredictable. For users or practitioners, what a randomized model entails is the fact that all predictions have some unaccounted chance of being wrong. One may argue that it is possible to average the outputs across multiple runs, but doing so would reduce the robustness and just converge back to the deterministic case (and with increased costs).
2.  **Definition of a successful attack**. This has to do with how a successful attack is defined on page 4: “…adversarial attacks are successful if the obtained adversarial example can fool the randomized model in the *majority* of its applications on the example.” I argue that in security-sensitive applications (e.g., authentication, malware detection, etc.), it is enough for the model to be fooled *once*. The randomness enables the attacker to keep submitting the same adversarial examples until by chance, the model misclassifies it.

I believe that these practical disadvantages limit the significance of this line of work.  

### First-order Taylor approximation

All the analysis in the paper uses the first-order Taylor approximation. First of all, this assumption should be stated more clearly. More importantly, I am not convinced that this approximation is good especially when the added noise or the perturbation is relatively large. Neural networks are generally highly nonlinear so I wonder if there is a way to justify this assumption better. An empirical evaluation of the approximation error would make all the analyses more convincing.

### Method for picking the intermediate layer

First, I wonder which intermediate layer is picked for all the results in Section 4. Do you pick the best one empirically or according to some metric? It will also be good to clearly propose a heuristic for picking the intermediate layer and measure if or how much the heuristic is inferior to the best possible choice.

### Loss-maximizing attacks

One of the big questions for me is whether the attack is related to the fact that most of the black-box attacks try to **minimize the perturbation magnitude**. Because of the nature of these attacks, all the attack iterations stay very close to the decision boundary, and hence, they perform particularly poorly against the noise addition defense. In other words, these attacks are never designed for a stochastic system in the first place so they will inevitably fail.

The authors have taken some steps to adapt the attacks for the randomized defense, mimicking obvious modifications that the real adversary might do (EoT and Appendix D.4). I really like these initiatives and also wonder if there are other obvious alternatives. One that comes to mind is to use attacks that **maximize loss given a fixed $\epsilon$ budget**. These attacks should not have to find a precise location near the decision boundary which should, in turn, make it less susceptible to the randomness.

This actually does NOT mean that the randomness is not beneficial. Suppose that the loss-maximizing attack operates by estimating gradients (via finite difference) and just doing a projected gradient descent. One way to conceptualize the effect of the added noise is a noisy gradient, i.e., turning gradient descent into *stochastic* gradient descent (SGD). SGD convergence rate is slowed down with larger noise variance so the adversary will have to either use more iterations or uses more queries per step to reduce the variance. Either way the attack becomes more costly. I suggest this as an alternative because it directly tests the benefits of the added noise without exploiting the fact that the distance-minimizing attacks assume deterministic target models.

### Additional figures

I have suggestions on additional figures that may help strengthen the paper.

1.  **Scatter plot of the robustness vs the ratio in Theorem 1.** The main claim of the paper is that the quantity in Theorem 1 positively correlates with the failure rate of the attack (and so the robustness). There are some figures that show the distribution of this quantity, but the figure that will help empirically verify this message is to plot it against the robustness (perhaps average over the test samples). Then, a linear fit and/or an empirical correlation coefficient can also be shown. Personally, this plot more clearly confirms the theoretical result than the density plot (e.g., Figure 2, etc.) or Table 6. I also think that $\nu$ should not be fixed across layers/models and should be selected to according to the clean accuracy.
2.  **Scatter plot of the clean accuracy vs the ratio in Eq. (14)**. Similar to the first suggest, I would like to see an empirical confirmation for both of these theoretical analysis.
3.  **Robustness-accuracy trade-off plot**. This has been an important concept for evaluating any adversarial defense. I would like to see this trade-off with varying $\nu$ as well as varying intermediate layers. The full characterization of the trade-off should also help in choosing the best intermediate layer, instead of just considering a few fixed values of $\nu$.

### Originality

One other weakness of the paper is the originality/novelty of the method. The most important contribution of this paper is the analysis on the gradient norm (i.e., sensitivity of the model) of benign and perturbed samples. The proposal to add noise to the intermediate layer instead of the input in itself is relatively incremental. However, the theoretical analysis does seem particularly strong to me, even though it does build up a nice intuition of the scheme. This is a minor weakness to me personally, and I would like to see more empirical results, as suggested earlier, rather than additional theoretical analyses.

### Other minor issues

- Eq. (7): the RHS is missing $L(...,y)$.
- 2nd paragraph on page 7: I think it was slightly confusing the first time I read it. It was not immediately clear to me that this is about Eq. (14) and what “product of this value and …” refers to.

### Questions
1. The paper mentions that the attack success rate is measured by “majority.” There’s an issue that I have already mentioned above, but I would like to know how many trials are used to compute this majority for the reported robustness in the experiments. If some variance can be reported too, that would be great. 
2. Section 3.3: from my understanding, the ratios plotted in Figure 3 involve both $\nu$ and $\nabla_{h(x)}(L \circ g)$. I wonder how $\nu$ is picked here. Is it picked like in Section 3.5 where the accuracy drop is fixed at some threshold (e.g., 1%, 2%)?
3. Section 4.1: it is mentioned that Qin et al. [2021] and Byun et al. [2021] are included in the comparison, but they never show up again. I wonder if the results are really missing or if these two schemes are basically the noise addition in the input.
4. Generally, I see a larger improvement for VGG and ViT vs ResNet-50 and DeiT. Is there any explanation or intuition the authors can provide to better understand this observation?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the defense method against query-based black-box attacks by injecting the noise into the middle layers of models. By theoretically analyzing the impact of both the adversarial perturbation and the noise injection on the prediction of the model, this paper tries to understand the impact of the proposed defense on robustness. Compared to the previous defense works that also inject noise into the model, the novelty of this paper is somehow in the noise injection to the feature space, i.e., the middle layer's outputs. Experimental results generally show the robustness improvement of injecting the noise to the feature rather than the input.

### Strengths
1. The proposed method that injects the noise into the features as the defense against the query-based black-box attack is novel and is empirically shown effective. 

2. The adaptive attack is well-considered, which makes the evaluation more comprehensive.

### Weaknesses
1. The organization of this paper can be improved. Assumption 1, Figure 1 and 2 are not referred to in the main text. It is confusing on the purpose of presenting the assumption 1 and Figure 1 and 2. 

2. The assumption and the theorem are incorrect. Even when the noise is small, the expectation of the randomized model is not necessarily consistent with the original model on the same data point, one simple counter-example is that when the input x is at the decision boundary, a small perturbation can change the prediction, so small noise may change the prediction. Theorem 1 is based on incorrect derivation, Eq. (23) and (24) may be incorrect as the gradient $\nabla_{h(x)}(L \cdot g)$ is anisotropic so the multiplication with Gaussian noise should not be an i.i.d. Gaussian noise. In addition, the assumption of the proof is the value of v and $\mu$ are small, so the approximation holds, but in the experiments, the value of $v$ is not present, and the value of $\mu$ is as large as 0.3, which is not negligible.

3. The correctness of Theorem 1 is not fully evaluated. The observation based on Theorem 1 is that the ratio $v/\mu$ is a factor of the robustness, if we fix the input x, then it is the only factor that affects the robustness. In Table 3, it is observed that the robustness is not strictly correlated to the ratio, this is reasonable since the inputs are changing during the multi-step perturbation. The correctness of the influence of the ratio can be verified by trying one-step perturbation so that the input x is kept the same, which is missing in this paper.

4. The evaluation of the decision-based attack is insufficient and the results are not good. It seems the proposed method only works on RayS, and the results on DeiT and ViT are not presented.

### Questions
1. Please verify if the Eq. (23) and the Eq. (24) are correct.

2. Please verify that assumption 1 is correct and that the theorems and experiments are strictly following this assumption.

3. I am curious about the impact of the ratio on the robustness when the gradients are fixed. Can you present the experimental results if possible?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair
