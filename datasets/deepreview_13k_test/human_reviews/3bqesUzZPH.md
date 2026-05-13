# FTA: Stealthy and Adaptive Backdoor Attack with Flexible Triggers on Federated Learning

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Current backdoor attacks against federated learning (FL) strongly rely on universal triggers or semantic patterns, which can be easily detected and filtered by certain defense mechanisms such as norm clipping, trigger inversion and etc.
In this work, we propose a novel generator-assisted backdoor attack, FTA, against FL defenses.
We for the first time consider the natural stealthiness of triggers during global inference.
In this method, we build a generative trigger function that can learn to manipulate the benign samples with naturally imperceptible trigger patterns (\emph{stealthy}) and simultaneously make poisoned samples include similar hidden features of the attacker-chosen label. 
Moreover, our trigger generator repeatedly produces triggers for each sample (\emph{flexibility}) in each FL iteration (\emph{adaptivity}), allowing it to adjust to changes of hidden features between global models of different rounds.
Instead of using universal and predefined triggers of existing works, we break this wall by providing three desiderate (i.e., stealthy, flexibility and adaptivity), which helps our attack avoid the presence of backdoor-related feature representations. 
Extensive experiments confirmed the effectiveness (above 98\% attack success rate) and stealthiness of our attack compared to prior attacks on decentralized learning frameworks with eight well-studied defenses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a generator-assisted backdoor attack (FTA) against robust FL. The newly designed generator is flexible and adaptive, where a bi-level optimization problem is formed to find the optimal generator.

### Strengths
1. Clear model and algorithm

1. T-SNE visualization of hidden features and similarity comparison are helpful.

### Weaknesses
1. To emphasis the importance of flexibility and adaptability, the authors may consider add some experiments compared with their restricted version attacks against fixed batch of data and under non-adaptive setting.

2. The current baselines are all fixed and non-adaptive. I suggest the authors compare their results with SOTA trigger generated based attacks as [1] and [2].

3. The post-training stage defenses play a vital role in countering backdoor attacks. Even within the context of FL, certain techniques such as Neuron Clipping [3] and Pruning [4] have demonstrated their effectiveness in detecting and mitigating the impact of backdoor attacks. Consequently, I am curious to know how the proposed FTA performs when subjected to these post-training stage defenses.


[1] Salem, Ahmed, et al. "Dynamic backdoor attacks against machine learning models." 2022 IEEE 7th European Symposium on Security and Privacy (EuroS&P). IEEE, 2022. [2] Doan, Khoa D., Yingjie Lao, and Ping Li. "Marksman backdoor: Backdoor attacks with arbitrary target class." Advances in Neural Information Processing Systems 35 (2022): 38260-38273. [3] Wang, Hang, et al. "Universal post-training backdoor detection." arXiv preprint arXiv:2205.06900 (2022). [4] Wu, Chen, et al. "Mitigating backdoor attacks in federated learning." arXiv preprint arXiv:2011.01767 (2020).

### Questions
1. How to choose/tune a good or even an optimal (is it exist?) $\epsilon$?

2. The structure of generator network is crucial to balance the tradeoff between effectiveness and efficiency since the authors want to achieve flexible (each training example) and adaptive (every FL epoch). In the centralized setting in [1] [2], trigger generators specific to every label need be trained one time before machine learning, and it still require some training time. I wonder is there any modifications the authors made to increase the efficiency of the training to achieve a flexible and adaptive attack? 


[1] Doan, Khoa, et al. "Lira: Learnable, imperceptible and robust backdoor attacks." Proceedings of the IEEE/CVF international conference on computer vision. 2021. [2] Doan, Khoa D., Yingjie Lao, and Ping Li. "Marksman backdoor: Backdoor attacks with arbitrary target class." Advances in Neural Information Processing Systems 35 (2022): 38260-38273.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a backdoor attack in the federated learning scenario, using a generative model that optimizes the perturbation to achieve stealthiness. The trigger is optimized during the training to be flexible and adaptive. The evaluation shows that it can achieve a 98% attack success rate.

### Strengths
The paper focuses on an important problem, and the solution is clear. It is easy
to follow and understand. 

The evaluation uses multiple datasets and models, also compares with multiple
baselines.

### Weaknesses
The core idea of the paper is to leverage a generative model to add adaptive
perturbations, which has been studied in many existing works, e.g., Cheng et al.
AAAI 2021, Dynamic attack, etc. The paper applies this idea in the federated
learning domain, but there is nothing that the method is specific to this
domain. Namely, I do not see any challenges because of federated learning that
prevents existing work from being used. Thus, I do not think the paper is novel.

Related to the previous question, there has been studies in detecting function
based attacks, and the paper does not discuss that.

### Questions
What is the main technical contribution of the paper?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a stealthy and adaptive backdoor attack with flexible triggers for federated learning.

### Strengths
The studied problem of backdoor attack in federated learning is important.

The experiment results show that the generated trigger is less perceptible in human eyes, and comprehensive experiments are done to verify the success of the attack.

### Weaknesses
1. The novelty of the formulated problem, as well as the method design is limited.  Specifically, the problem formulation in Eq. (1)  is mostly the same with Eq. (3) of Lira [A], except for some minor differences like separating poisoned and clean datasets.  The solution to solve the proposed problem is also quite standard by alternating optimization of the two variables, which is also adopted by  Wasserstein Backdoor [B]. The generator of the trigger is also following the autoencoder structure as adopted by [A].   In this sense, the proposed attack seems to be a direct migration of Lira into a federated learning setting, which looks quite incremental.  

2. The defense baselines are not comprehensive. The authors can consider adding more defense baselines, e.g., RLR [C], Crfl [D],  to show that the attack can successfully break through defenses other than cluster-based filtering.

3. It is unclear why optimizing the triggers can guarantee a better attack towards cluster-based filtering (or minimizing the distance of updates with the poisoned update), as this is not reflected in the problem formulation. See details in my questions part.

4. There are some issues with the experiment results and the setup. The baseline benign accuracy is very low (shown in Table 2, 61.73% benign accuracy for CIFAR10 with ResNet, and also low for TinyImagNet), which makes the correctness of the experiment implementation questionable.  The setup of local epochs is also strange, in that the malicious clients run more epochs than the benign clients. This might introduce bias to other baselines because this would make the malicious updates significantly larger than other benign updates, which may affect the performance of other attack baselines when against filtering-based defense.   Also, the authors should test the results in IID setting as well as various Non-IID parameters to show its effectiveness. 


[A] Doan K, Lao Y, Zhao W, et al. Lira: Learnable, imperceptible and robust backdoor attacks[C]//Proceedings of the IEEE/CVF international conference on computer vision. 2021: 11966-11976.

[B] Doan K, Lao Y, Li P. Backdoor attack with imperceptible input and latent modification[J]. Advances in Neural Information Processing Systems, 2021, 34: 18944-18957.

[C] Ozdayi M S, Kantarcioglu M, Gel Y R. Defending against backdoors in federated learning with robust learning rate[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2021, 35(10): 9268-9276.
 
[D] Xie C, Chen M, Chen P Y, et al. Crfl: Certifiably robust federated learning against backdoor attacks[C]//International Conference on Machine Learning. PMLR, 2021: 11372-11382.

### Questions
It is suggested in Section 3.3 "one may consider alternately updating fθ while keeping Tξ unchanged, or the other way round... (but this couldn't work well)". However, it is later claimed that "Inspired by (Doan et al., 2022), we divide local malicious training into two phases. In
phase one, we fix the classification model fθ and only learn the trigger function Tξ. In phase two, we use the pre-trained Tξ∗ to generate the poisoned dataset and train the malicious classifier fθ". In my understanding, the two descriptions of alternating optimization are identical. Can the authors elaborate on it?

It is claimed on page 4 that "A stealthy backdoor attack on FL should mitigate the routing introduced by backdoor task and guarantee the stealthiness of model parameters instead of just the hidden features of poisoned samples compared to their original inputs". However, it is unknown how the authors are achieving this goal with their problem formulation in Eq. (1).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
