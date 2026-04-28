# Interpreting Adaptive Gradient Methods by Parameter Scaling for Learning-Rate-Free Optimization

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 8, 5

## Abstract
We address the challenge of estimating the learning rate for adaptive gradient methods used in training deep neural networks. While several learning-rate-free approaches have been proposed, they are typically tailored for steepest descent. However, although steepest descent methods offer an intuitive approach to finding minima, many deep learning applications require adaptive gradient methods to achieve faster convergence. In this paper, we interpret adaptive gradient methods as steepest descent applied on parameter-scaled networks, proposing learning-rate-free adaptive gradient methods. Experimental results verify the effectiveness of this approach, demonstrating comparable performance to hand-tuned learning rates across various scenarios. This work extends the applicability of learning-rate-free methods, enhancing training with adaptive gradient methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a learning rate tuning method for adaptive optimization algorithms. Besides, this paper also proposes a method to interpret adaptive gradient methods as parameter-scaled SGD. Experimental results show that the proposed method can be comparable with adaptive gradient methods with hand-tunned learning rates.

### Strengths
1. This paper uses parameter rescaling to interpret adaptive gradient methods, which could be helpful for further investigating the behavior of adaptive gradient methods.
2. The proposed learning-rate-free methods can be useful to avoid the hyperparameter tunning in adaptive gradient methods while still achieving fast convergence.

### Weaknesses
1. The paper organization is not clear to me. In particular, Algorithm 2 looks pretty complicated to me. The authors just explain each steps after the algorithm, while I am still not very clear about the motivation and why such a method can be developed.

2. Second, the equations are also not clear. The authors claim that the adaptive methods can be viewed as applying the steepest descent to parameter-scaled networks based on Eqs 1-4. However, the notations are not clear, what's the formal definition of $f'$, why $f'$ needs to be introduced, and how to leverage it?

3. In Section 3, equation (7) is also confusing, in Adam, $\alpha$ is also depending on the randomness of the stochastic gradients, when why $E u = \nabla f(w)/\alpha^2$ can hold?

4. The reasoning from (9)-(11) is also not clear to me, if you only want to mention that the learning rate should not depend on $\alpha$, why do you still need equations (10) and (11)?

5. The convergence analysis is also not clear, the authors just provide a very simple proof in the appendix, in the main part, I actually do not see anything that is related to the convergence. Additionally, the proof is also not clear, many notations such as D,G are not clearly presented; the assumption that $\alpha_k$ coverges to $\alpha$ is also not presented; Eq. (15) is also not well justified.

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes two new algorithms Parameter-scaled stochastic Polyak step-size and Parameter-scaled D-Adapt from the intuition of parameter scaling, and compares their performance to other algorithms.

### Strengths
The problem studied is interesting. It is important to learn whether we can make adaptive gradient methods learning rate-free.

### Weaknesses
The contribution of the paper is unclear. In the first sentence in the abstract, the authors claim that they "address the challenge of estimating the learning rate for adaptive gradient methods." The issue is important, but after reading the paper, I do not follow how they addressed the issue.

Then, the authors claim they "interpret adaptive gradient methods as steepest descent applied on parameter-scaled networks ." Authors need to explain why their new interpretation is important to the ICLR community.

Also, the authors claim they "propose learning rate-free adaptive gradient methods". It appears that algorithm 2 is the method they propose. However, in algorithm 2, there are a lot of hyper-parameters, including $\eta_k$, $\gamma_k$, and even $\alpha_k$. It is not clear to me why Algorithm 2 is "learning rate-free". The explanation about the notations in Algorithm 2 should be clearer.

In section 5.2, authors should report the metrics for their reinforcement learning experiment. It is hard to understand the value of the proposed PS-SPS and PS-DA-SGD from Table 3. Also, the authors mention that they removed all the batch normalization layers in the CIFAR-100 experiment. What are the benefits of such removal?

Authors should also clearly write their assumptions and conclusions into a formal theorem in Section 4.2.

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an efficient learning-rate free gradient-descent type optimization technique. The approach reconciles learning-rate-free approaches with parameter-wise adaptive gradient scaling methods. This result is achieved intuitively by reinterpreting gradient scaling as parameter rescaling. The approach builds on recently introduced methods for learning-rate-free optimization techniques and extends those to a parameter-wise step-size adaptation.

### Strengths
The presentation of the paper is clear and the approach is simple yet original and efficient and has potentially a promising impact.

### Weaknesses
While the approach is intuitive and a convergence proof is given, the approach exhibits heuristic qualities and doesn't discuss the resulting dynamic of the adaptation. Especially, in consideration of the potential complex resulting dynamics by applying parameter wise step-size adaptation.

### Questions
Is there something that can be said about label noise sensitivity/robustness of the proposed method?

### Soundness
3 good

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method to apply adaptive gradient methods, such as Adam, to learning-rate-free methods for deep learning.
The experiments demonstrate the proposed method works on various scenarios, including image classification to reinforcement learning and semantic segmentation.

### Strengths
The experiments are conducted on cases where learning rate configuration is crucial, such as reinforcement learning and training of ViT from scratch and demonstrate that the approach is comparable or even better to the baselines.
I hope this approach relieve us from learning rate tuning.

### Weaknesses
* To my understand $c$ in Algorithm 1 is a hyperparameter. If so, does it mean that this method introduces a parameter to eliminate learning rate? How sensitive the proposed method to this parameter?
* Algorithm 1 also requires $f^*$, which I think is the loss value at the optimum. For deep models, obtaining such a value sounds quite challenging.

### Questions
* How to tune $\gamma_k$?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
