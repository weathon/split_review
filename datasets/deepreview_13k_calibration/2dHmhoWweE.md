# Lookbehind Optimizer: k steps back, 1 step forward

- Decision: Reject
- Avg Score: 4.75
- Scores: 8, 5, 3, 3

## Abstract
Sharpness-aware minimization (SAM) methods have gained increasing popularity by formulating the problem of minimizing both loss value and loss sharpness as a minimax objective. 
In this work, we increase the efficiency of the maximization and minimization parts of SAM's objective to achieve a better loss-sharpness trade-off.
By taking inspiration from the Lookahead optimizer, which uses multiple descent steps ahead, we propose Lookbehind, which performs multiple ascent steps behind to enhance the maximization step of SAM and find a worst-case perturbation with higher loss. Then, to mitigate the variance in the descent step arising from the gathered gradients across the multiple ascent steps, we employ linear interpolation to refine the minimization step. 
Lookbehind leads to a myriad of benefits across a variety of tasks. Particularly, we show increased generalization performance, greater robustness against noisy weights, as well as improved learning and less catastrophic forgetting in lifelong learning settings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel optimization method, called Lookbehind, that leverages the benefits of multiple ascent steps and linear interpolation to improve the efficiency of the maximization and minimization parts of sharpness-aware minimization (SAM). The experiments show that Lookbehind improves the generalization performance across various models and datasets, increases model robustness, and promotes the ability to continuously learn in lifelong learning settings.

### Strengths
S1. The work is well motivated. Finding a simple but effective method to improve SAM is both interesting and important. 

S2. The paper is well written and easy to follow. The illustration in Fig. 1 and Fig. 2 are helpful to understand the main results.

S3. The authors conduct numerous experiments to showcase the benefits of achieving a better sharpness-loss trade-off in SAM methods. These experiments are comprehensive and convincing. Additionally, the paper includes several ablation studies.

### Weaknesses
W1. As mentioned by the authors, one inherent drawback of Lookbehind is the computational overhead, which leads to an increase in training time by a factor of $k$. This overhead is a significant practical concern, especially when training large models or using extensive datasets. The paper does not provide a detailed analysis of the trade-off between the increased computational cost and the achieved performance gains, making it difficult to assess the practical applicability of the method in resource-constrained environments.

W2. No convergence analysis for Lookbehind is provided. This lack of theoretical grounding makes it difficult to understand the conditions under which Lookbehind is guaranteed to converge to a good solution. While empirical results are promising, a theoretical analysis would strengthen the paper and provide a more solid foundation for the proposed method. Specifically, it would be beneficial to understand how the interpolation parameter and the number of lookbehind steps affect the convergence rate and the quality of the solution. Furthermore, the paper does not discuss the potential for divergence or instability under certain conditions.

### Questions
Q1. Drawing inspiration from the Lookahead optimizer, can the fast weights (updated in line 8 of Algorithm 1) be approximately updated using any standard optimization algorithm like SGD or Adam?

Q2. Why not conduct an analysis of the sensitivity of Lookbehind to the step size $\eta$ for the fast weights?

Q3. Anderson acceleration has a similar flavor to Lookbehind, and it has been employed in solving minimax optimization problems.What is the relation between Lookbehind and Anderson acceleration?

Minor Comments:

(1) On page 3, in line 4 from below, should "slow weights" be replaced with "fast weights"?

(2) On page 8, in line 13 from below, should "$\rho$” be repaced with "$\alpha$”?

(3) On page 8, in line 4 from below, "$0\geq \alpha^*<1$” should be "$0\leq \alpha^*<1$”.

### Soundness
4 excellent

### Presentation
4 excellent

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
The paper presents a new approach for the multiple ascent steps Sharpness-aware minimization training, which has been proven to enhance the generalization ability of neural networks. In particular, the authors introduce a variance reduction technique to better leverage the information along the trajectory instead of using the last updated model parameter only. Extensive experiment results on both single-task and continual learning show the effectiveness of the proposed approach.

### Strengths
- While previous studies have shown that multi-step ascent SAM does not improve over single-step SAM, the paper proposes to utilize multiple gradients along the ascent trajectory for a better maximization step. Motivated by the Lookahead optimizer, the proposed method stabilizes the training, thus improving the performance of the model.
- The paper is well-written and easy to follow.
- The authors conduct experiments on many datasets and backbones and empirically verify the benefit of Lookbehind SAM over SAM. The ablation studies showcase how their method is better than naive Multistep-SAM and Lookahead SAM.
- Lookbehind is readily applicable to different SAM-based training methods (e.g. ASAM). Moreover, it is robust to the hyperparameter tuning.  
- The proposed adaptive $alpha$ utilizes the similarity in the updating directions between the first and last gradients can eliminate the need to tune this parameter while maintaining superior performance.

### Weaknesses
 - The authors claim that "a drawback of any multiple ascent step SAM method is the computational overhead which increases training time by a factor k". However, while Lookbehind calculates k ascent steps (line 6 in Algorithm 1) and k descent steps (line 8), Multistep-SAM performs k ascent steps and only a single descent step, requiring almost half the complexity.

- Can the authors compare Lookbehind against averaging the ascent gradients baseline, which has been proven to be able to improve SAM [1] (and also performs k ascent steps and a single descent step only)?

- More detailed descriptions are needed for Figure 2 and Figure 11. The decay term can be omitted for simplification.

- While leveraging multiple ascent steps can improve over the original SAM/ASAM, a prior study [2] shows that the inner gradient ascent can be calculated periodically while maintaining similar performance to the conventional SAM (i.e. it is redundant to compute the ascent gradient at every step). Can the author elaborate more on this?

- Since the computational complexity is multiplied by k, can the authors compare Lookbehind against SAM/ASAM at different training budgets?

### Questions
- While leveraging multiple ascent steps can improve over the original SAM/ASAM, a prior study [2] shows that the inner gradient ascent can be calculated periodically while maintaining similar performance to the conventional SAM (i.e. it is redundant to compute the ascent gradient at every step). Can the author elaborate more on this?

- Since the computational complexity is multiplied by k, can the authors compare Lookbehind against SAM/ASAM at different training budgets?

[2] Liu, Yong, et al. "Towards efficient and scalable sharpness-aware minimization." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors focuses on contributing to the Sharpness-Aware Minimization (SAM) algorithm, more specifically the multiple-ascent SAM, where they proposed Lookbehind SAM. Lookbehind SAM average the history gradient solved during multiple ascent steps for each batch training. e authors empirically show the effectiveness of their method via experiments on CIFAR, ImageNet and as well as lifelong learning settings.

### Strengths
1. The paper is clearly written and easy to follow. But some of the presentations need to be improved.
2. The proposed method seems interesting.
3. I notice that the authors present valuable extra results, i.e. lifelong learning, in addition to the image classification that is typically used in SAM.

### Weaknesses
1. My first concern may be the title this paper, "Lookbehind Optimizer: k steps back, 1 step forward". The title obviously mimics the paper "Lookahead Optimizer: k steps forward, 1 step back". This somehow directly implies that the method of the presented paper is opposite to that in Lookahead paper. But they are very different. The proposed Lookbehind could not be used without SAM, and focusing on different gradients. Considering the proposed method contributes specifically to SAM, so at least, the paper ought to mention SAM algorithm in their title to give a clear view, such as Lookbehind SAM Optimizer or Lookbehind SAM. Not mentioning SAM in the title is unacceptable.

2. The motivation is not quite clear for me. The authors claim that the proposed method could reduce the variance derived from the multiple ascent steps. Why we need to reduce such variance is not clearly demonstrated. Specifically, the connection between reducing variance in the ascent gradients and an improved loss-sharpness trade-off is not sufficiently explained. It's not clear how averaging gradients from different points in the loss landscape leads to a better solution for the original minimization problem.

3. Although the proposed method seems interesting, yet its drawback is quite obvious. A single parameter update requires performing multiple backwards propagation to calculate the ascent gradient. In other words, the utility efficiency of training samples is quite low. Multiple backwards propagations are required on the same sample batch. Given that the improvement of the proposed method is marginal, the side effect of such a method can potentially be substantial. So, in my opinion, the proposed method may not be better than the vanilla SAM. The authors should provide a more thorough analysis of the computational cost versus the performance gain. A comparison of wall-clock time for training with Lookbehind SAM versus vanilla SAM would be very helpful.

4. Based on my tuning experience, the authors have not trained the models to achieve comparable results when using vanilla SAM in their baseline on Cifar dataset. The authors should at least trained models to achieve comparable results with those reported in the original SAM paper. For example, in the original SAM paper, WRN-28-10 can achieve an error rate of 16.5 with SAM, while in the given paper, it achieves an error rate of 19.5 with SAM, almost 3 percentage gap. Therefore, the reported results can not fully persuade me that their method is more effective. Also, many advanced SAM variants have not mentioned in their experiments. It is highly recommended that the authors make comparisons with these SOTA methods. The lack of comparison with other state-of-the-art SAM variants is a significant weakness. The authors should consider including comparisons with methods such as  Sharpness-Aware Minimization with Adaptive Stepsize (ASAM) and other relevant methods to properly contextualize their contribution.

5. For Figure 2, it is recommended that the authors draw some marks with respect to the gradient vector. The figure would benefit from a more detailed illustration of how the gradients are being accumulated and averaged. Visualizing the individual gradient vectors and their average would help clarify the method.

6. For Algm 1, it is recommended that the authors use $\theta$ to substitute fast weights $\phi$, as that used in the Lookahead paper.

### Questions
See Weakness.

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposes a new version of multi-step SAM using a linear interpolation technique. They discuss convergence properties of the algorithm and present numerical experiments.

### Strengths
The proposed method seems to outperform SAM in the settings studied.

### Weaknesses
 - The idea of multi-step SAM is not new and has been explored before. Although the interpolation step makes this work different from the previous work, I think that is a marginal contribution.

- The numerical experiments are rather limited. As far as I could tell, they only consider CIFAR and a down-sized version of ImageNet, only using ResNets. I think the complete ImageNet should be in the numerical studies, and some transformer-based models need to be added (such as ViTs or BERT).

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
