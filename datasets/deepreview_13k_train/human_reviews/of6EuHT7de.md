# On the Byzantine-Resilience of Distillation-Based Federated Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
\gls{fl} algorithms using \gls{kd} have received increasing attention due to their favorable properties with respect to privacy, non-i.i.d.\ data and communication cost. These methods depart from transmitting model parameters and instead communicate information about a learning task by sharing predictions on a public dataset.
  In this work, we study the performance of such approaches in the byzantine setting, where a subset of the clients act in an adversarial manner aiming to disrupt the learning process.
  We show that \gls{kd}-based \gls{fl} algorithms are remarkably resilient and analyze how byzantine clients can influence the learning process. 
  Based on these insights, we introduce two new byzantine attacks and demonstrate their ability to break existing byzantine-resilient methods. Additionally, we propose a novel defence method which enhances the byzantine resilience of \gls{kd}-based \gls{fl} algorithms.
  Finally, we provide a general framework to obfuscate attacks, making them significantly harder to detect, thereby improving their effectiveness. Our findings serve as an important building block in the analysis of byzantine \gls{fl}, contributing through the development of new attacks and new defence mechanisms, further advancing the robustness of \gls{kd}-based \gls{fl} algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper first shows that distillation based method is more robust to conventional federated average using the Gaussian attack as an example. Then based on the observations, two labelling attack schemes are developed to break current distillation based robust algorithms and accordingly a new algorithm is developed to against the new attacks.

### Strengths
The paper is well written and constructed in a fluent structure. Extensive experiments have been conducted to verify the proposed ideas and methods. The proposed method is also somewhat new in the Knowledge distillation domain.

### Weaknesses
1. The comparison of FedAVG and KD-FL is a little weak and the experimental part is limited to KD-based methods, making the whole idea less convincing. The paper only shows a single comparison using a Gaussian attack on FedAVG and random label flipping on KD-FL, which is insufficient to make a general claim about the robustness of KD-based methods. A more comprehensive comparison should include a wider range of attacks, such as sign-flipping, model poisoning, or targeted attacks, to provide a more complete picture of the robustness landscape.
2. The proposed ExpGuard+F method is similar as the FLTrust methods, which is okay, however, the strength of the proposed method is not exactly reflected from the experiments. For example, is ExpGuard+F better than ExpGuard+GM and if yes, why? The experimental results should clearly demonstrate the advantages of ExpGuard+F over other aggregation methods, including a detailed analysis of the performance differences under various attack scenarios and intensities. The current experiments do not sufficiently highlight the specific benefits of the proposed method.
3. The study of HIPS conveys the message that some attacks are hard to detect and combat, but we can use simple mean aggregation instead. I could not see the significance of this point right now. The paper should provide a more nuanced discussion on the trade-offs between robust aggregation methods and simple mean aggregation, especially in the context of HIPS attacks. It should also explore the conditions under which each approach is more suitable, rather than simply stating that mean aggregation can sometimes perform better.

### Questions
1. It is not clear what is the strength (mean/variance) of the Gaussian attack that is used to show the superiority of KD-FL against FedAvg.  Meanwhile, it is not fair to draw the conclusion that KD-based method is more resilient to FedAvg by one comparison between random Gaussian attack to FedAvg and the random label flipping for KD-FL. A fairer comparison could include some other attacks.
2. The study of HIPS is interesting, however, the result simply suggests that sometimes robust aggregation is worse than mean aggregation. To make this point more valuable, it might be better to have a trade-off analysis or provide some guidelines to how to choose robust aggregation methods. 
3. The prediction for honest agent 4 in Figure 2 should be [0.61, 0.08, 0.31] to ensure the correct average prediction.
4. At least GM has been widely used in FedAVG for robust aggregation, therefore in line 387, when the authors say “As a result, applying them to aggregated parameters in Byzantine FedAVG is often impractical” does not make sense to me. It would be great if the authors either provide evidence supporting their claim about impracticality, or to revise their statement to better reflect the current state of practice in the field.
5. What is the baseline performance of FedAVG on the tested datasets? To me, KD-FL is more communication efficient as it only transfers predictions rather than model parameters, but is its performance better than or equivalent to FedAVG? If yes, then it makes sense to study KD-FL in Byzantine settings, otherwise, we can trade some communication for performance improvement and develop some communication-efficient and robust FedAVG algorithms. 
5. ExpGuard shares some similarities with the FLTrust method, which is not new. It would be better to clarify the strength and difference of ExpGuard against FLTrust [1].
[1] Cao, Xiaoyu, Minghong Fang, Jia Liu, and Neil Zhenqiang Gong. "Fltrust: Byzantine-robust federated learning via trust bootstrapping." arXiv preprint arXiv:2012.13995 (2020).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper evaluates the robustness of distillation based distributed learning to arbitrary (Byzantine) faults in the i.i.d setting. 

The work illustrates the resilience of KD-based algorithms and analyzes how
byzantine clients can influence them. It also proposes two byzantine attacks and assess their ability to break existing
byzantine-resilient methods. It also proposes a method to further improve the byzantine resilience of KD-based FL algorithms.

### Strengths
the paper addresses an important and previously undressed question: the robustness of distributed learning in the distillation setting

### Weaknesses
 the formal guarantees (left to appendix D) deserve a more prominent place in the paper, given that the core contribution of such a paper is to formally derive security guarantees and their limits when (in this case) the space of all possible attacks cannot rely on empirical validation

### Questions
What would be the effect of most comon robust aggregation schemes on KD-based FL? how would that change the bound in appendix D.1?

### Soundness
3

### Presentation
2

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
This paper studies the Byzantine resilience of federated knowledge distillation under IID data distributions. The authors start by analyzing the vanilla FedDistill and illustrate the vulnerabilities of FedAvg in the presence of Byzantine adversaries. The authors further propose three additional Byzantine attacks tailored for distillation-based federated learning methods. In response to enhance the federated distillation-based methods, the authors propose ExpGuard.

### Strengths
* The paper is, in general, well written.
* The proposed algorithms and the attack strategies are intuitive and easy to understand.

### Weaknesses
 * The most obvious weakness of the paper is that it addresses the IID data distributions. In contrast, the current state-of-the-art (SOTA) Byzantine resilient federated learning methods focus on non-IID data setups. 
* In Section 4, the motivating example to compare the vanilla FedAvg algorithm and the FedDistill algorithm is rather unfair. This is because the adversaries for the vanilla FedAvg employ model poisoning strategies, while the ones in FedDistill use data poisoning. It is important to acknowledge that while the final outcome of distillation is reflected in the predictions, the poisoned data used to train the model still stems from a polluted model, making the comparison less straightforward.
* In Section 4, the presentation in **the byzantine resilience of FedDistill** can be improved. All the theoretical theorems and lemmas have been deferred to the Appendix, making it hard to appreciate the real significance of resilience.
* In Section 5, the loss minimization attack (LMA) is a bit contrary to the prior Byzantine federated learning literature, e.g., [Karimireddy et al. (2022), Allouah et al. (2023)], where they assume the server is curious but honest. Here, the server is not reliable in the sense that it can manipulate the generated model parameters to mislead the training. At one extreme, the server can completely replace the model parameters to destroy the whole training process. Furthermore, the description of LMA implies that only the server has access to the mean of honest client predictions and Byzantine client predictions, which is based on the statement (line 320) "$\mathcal{L}$ that the server is trying to minimize". It is crucial to clarify that Byzantine clients also have access to this loss information.
* In Section 5.2, the authors did not explain why ExpGuard works, except by citing [Littlestone & Warmuth, 1994]. 
* It is recommended to group HIPS together with LMA & CPA and present the defending strategy after the attacking strategies.
* The experiments are not thorough enough in two regards. First, the authors need to compare with the performance with FedAvg under current SOTA Byzantine resilient algorithms, e.g., bucketing [Karimireddy et al. (2022)] and [Allouah et al. (2023)] NNM. Second, the ablation experiments do not consider varying the number of Byzantine clients. The algorithms may struggle under benign settings.

### Questions
* In Section 4, is it possible to compare the vanilla FedAvg and FedDistill under the same Byzantine adversaries?
* In Section 4 **the byzantine resilience of FedDistill**, it seems that the authors consider the full-batch gradient only. However, stochastic gradients are the ones that the machine learning community uses in practice. How will the choice of stochastic gradients affect the problem?
* In Section 4, the authors claim that previous work on byzantine FedDistill focuses mostly on basic label-flipping attacks. Is it possible to consider another classic data poisoning attack: data injection?
* In Section 5, is the loss minimization attack a plug-in attack on top of the original data poisoning attack at each Byzantine client?
* In Section 5, can the authors further justify ExpGuard? In particular, why does the exponential weight work, but the other choices won't?
* In Section 6, can authors conduct more thorough experiments to compare (1) FedDistill algorithm with FedAvg under SOTA defense (2) the varying number of Byzantine clients?

### Soundness
3

### Presentation
3

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
This paper explores the robustness of FedDistill, a knowledge distillation federated learning (FL) method, under Byzantine settings, where some clients act maliciously to disrupt training. The paper introduces two new Byzantine attacks, Loss Maximization Attack (LMA) and Class Prior Attack (CPA), that exploit this prediction-sharing approach. It also presents ExpGuard, a novel defense mechanism to counteract these attacks. The authors finally propose the HIPS method to obfuscate attacks, making them harder to detect. Experimental results demonstrate that FedDistill is more resilient than traditional FL aggregation methods.

### Strengths
1. Considering KD-based FL in a Byzantine setting is a good idea.
2. Propose two effective attacks for KD-based FL and a defending method. Additionally, the authors introduce a method that obfuscates attacks to make them harder to detect. 
3. The experimental results show the effectiveness of the proposed methods.

### Weaknesses
1. The paper only considers iid setting. Although the authors claim that non-iid setting in FL poses serious issues (line 122), they don't specify what kind of issue makes it unsuitable for KD-based FL. Moreover, non-iid setting is essential in FL and is closer to realistic scenarios.
2. The scale of experiments is limited. The paper only considers cross-silo settings (a small number of clients) and lacks cross-device settings (over a hundred clients).
3. The ExpGuard assumes that the Byzantine clients are identical during training, which may be not the case in reality.

### Questions
1. In line 328 and figure 2, shouldn't the least likely class be _dog_ rather than _cat_?
2. CPA attack requires a pretained model to obtain the similarity matrix, how do you get it in the experiments? Is this effective in a more realistic setting?
3. Will the distribution shift between clients' data and public data affect the performance of the server's model? It's better to provide additional experiments or theoretical analysis on how different levels of distribution shifts between client and public data might impact the server model's performance. This could help readers better understand the limitations and robustness of the proposed approach.

### Soundness
3

### Presentation
2

### Contribution
2
