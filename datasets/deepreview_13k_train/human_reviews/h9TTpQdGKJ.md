# Learning Transferable Robust Representations for Few-shot Learning via Multi-view Consistency

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Despite the success on few-shot learning problems, most meta-learned models only focus on achieving good performance on clean examples and thus easily break down when given adversarially perturbed samples. While some recent works have shown that a combination of adversarial learning and meta-learning could enhance the robustness of a meta-learner against adversarial attacks, they fail to achieve generalizable adversarial robustness to unseen domains and tasks, which is the ultimate goal of meta-learning. To address this challenge, we propose a novel meta-adversarial multi-view representation learning framework with dual encoders. Specifically, we introduce the discrepancy across the two differently augmented samples of the same data instance by first updating the encoder parameters with them and further imposing a novel label-free adversarial attack to maximize their discrepancy. Then, we maximize the consistency across the views to learn transferable robust representations across domains and tasks. Through experimental validation on multiple benchmarks, we demonstrate the effectiveness of our framework on few-shot learning tasks from unseen domains, achieving over 10\% robust accuracy improvements against previous adversarial meta-learning baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses adversarial robustness in the unseen domain of meta-learning. The paper finds that existing adversarial meta-learning methods have a significant degradation of robustness in the unseen domain, and proposes a method for acquiring task-independent representations by introducing self-supervised learning to solve this problem. The paper proposes a method for acquiring task-independent representations by introducing self-supervised learning. The paper introduces two encoders that handle different views generated from the input and optimize the adversarial noise to maximize the distance on the common latent space between these views. It also aims to obtain a representation with better discriminative performance by optimizing the encoders with contrastive learning loss using the two views. In experiments, the paper has compared the proposed method with meta-learning and adversarial meta-learning baselines and analyzed by ablation study to verify the effectiveness of the method. On the other hand, the proposed method has little theoretical basis, and the introduction of task-independent loss blurs the difference from general self-supervised learning, so its contribution to the field of meta-learning is not clear.

### Strengths
+ The paper is well-written and easy to follow.
+ The paper introduces self-supervised learning to adversarial meta-learning and shows that multi-view-based adversarial training and representation learning can improve certain robustness in meta-learning benchmarks.

### Weaknesses
 - **W1.** Although the paper successfully improves the performance of the model by introducing bootstrapping and contrastive learning, these contributions to robustness are already widely known outside of meta-learning and thus have little novelty [a,b]. In other words, the proposed method has little contribution other than introducing these technical components into the meta-learning problem setting, and it is unclear whether meta-learning is really necessary for generalizing adversarial robustness across domains. This is a problem of the adversarial meta-learning setting itself, and a baseline and comparison with non-meta-learning is needed to address this concern (-> Q1).
- **W2.** The paper adds one more encoder for multi-view representation learning, increasing the capacity of models. Since there are no comparative experiments with baseline or ensemble methods with the same model capacity, it is not possible to distinguish the performance improvement by the proposed method from ones by increasing model capacity. Current baselines and evaluations are hard to say fair (-> Q2).

### Questions
- **Q1.** Is meta-training really necessary? In previous studies [c,d], pre-trained models trained on meta-training datasets without meta-training were introduced as an important baseline for evaluating clean accuracy. In the case of this paper, a comparison with a baseline pre-trained with adversarial training (e.g., TRADES) would confirm the significance of meta-training.
- **Q2.** Does the proposed method outperform the baseline when the model capacities of the proposed method and the baseline are aligned? The current experimental evaluation is not fair because it only provides results compared to the baseline with different model capacities during meta-training.

[c] Tian, Yonglong, et al. "Rethinking few-shot image classification: a good embedding is all you need?." Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XIV 16. Springer International Publishing, 2020.

[d] Miranda, Brando, et al. "Is Pre-training Truly Better Than Meta-Learning?." arXiv preprint arXiv:2306.13841 (2023).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a meta-adversarial multi-view learning framework to learn robust meta feature representations. It first generates multi-view latent adversaries using a query set, then maximizes consistency across different views to learn transferable representations. The paper is well-structured and presents comprehensive experiments and analyses to demonstrate its superior cross-domain performance.

### Strengths
1.	The paper is well-motivated, focusing on the significant issue of robustness under domain shift within meta-learning.
2.	The paper is well-structured, conducting comprehensive experiments to demonstrate its superior cross-domain performance and the effectiveness of each component.

### Weaknesses
1.	In my view, the multi-view latent attack enhances the model’s meta generalizability to some extent, therefore, it outperforms other Adversarial Meta-Learning methods in the cross-domain setting. And the multi-view training is quite similar to the task augmentation meta-learning methods [1,2,3]. Thus, I believe that a discussion or comparison in the related work section would enhance understanding of the multi-view’s effect.
2.	During meta-testing, the evaluation was conducted on only 400 randomly selected tasks, which significantly impacts the final accuracy. What would the final performance be if the number of evaluated tasks during meta-testing were increased?
3.	How does the model perform under different attacks, apart from the PGD-20 attack?

### Questions
See Weaknesses 1-3

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper pays attention to the adversarial meta-learning problem, especially the unseen domain adversarial robustness transferability issue. To address this issue, this paper proposes a meta-adversarial multi-view representation learning (MAVRL) method by using bootstrapped multi-view encoders and label-free multi-view adversarial latent attacks. Multiple experiments show the effectiveness of the proposed method.

### Strengths
1.	This manuscript is well organized and easy to follow. 
2.	The motivation is reasonable and experiments are abundant.
3.	The proposed idea is interesting.

### Weaknesses
Several main concerns are as follows:

1.	This work is mainly built on TRADES and the key contribution is introducing the multi-view consistency loss, inspired by the adversarial self-supervised learning. In this sense, the TRADES should be a straightforward baseline in the main experiment in Table 1. In addition, some latest generic adversarial training methods are also recommended to be added into Table 1. Furthermore, because TRADES has been a common method in the field of adversarial training, why only AT is employed for other competitors in the experiments in Table 3? This is not fair. 

2.	According to the description in this paper, it seems that two encoders are used during training. Therefore, how to use the proposed model during test? It means that one encoder will be discarded during test? This part should be clear.

3.	Some details of the proposed framework are not clear. For example, which kind of FSL classifier is used in the proposed framework? Why select this kind of classifier? 

4.	In the experiments part, many comparison experiments are not fair. For example, why other AML methods are not compared in Table 2? In fact, there is a trade-off problem in adversarial training [1]. It is somewhat difficult to compare two adversarial meta-learning methods with two kinds of accuracies [2].   

5.	Some latest adversarial meta-learning methods are not reviewed, such as [2]. In addition, the work in [2] had already considered the unseen domain adversarial robustness transferability issue. Importantly, the work of [2] can achieve much better results than this work. 

6.	Only one kind of adversarial attack is considered in this paper. More kinds of adversarial attacks are recommended to be added into this work [2], making the proposed method more convincing.

7.	In the supplementary material, it seems that only 200 and 400 tasks are used to perform the meta-training and meta-test, respectively. I doubt the effectiveness of the experimental results, because the variance and randomness of the results will be very large, especially for adversarial training. 

### Questions
Please kindly refer to the above comments.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work aims to improve the robustness of meta-learning methods under domain shift. To this end, the authors introduce contrastive learning to the adversarial meta-training process. They propose to bootstrap multi-view encoders instead of single one to overcome representation collapse. The experiments on CIFAR-FS and mini-ImageNet verify the effectiveness of proposed method.

### Strengths
The paper is organized and written well and the paper looks quite well polished. The overall story is clear to me.

### Weaknesses
My main concerns are the meaning of the problem solved in this work and effectiveness of the proposed method. Concretely,
1. I do not think it is still mearningful for few-shot learning to meta-train on a small base dataset nowadays. In fact, since the pre-trained large vision bockbone, like CLIP and MoCo, have been provided and have far more generalizing representation than the model trained on small base dataset, I think it is more useful to use them for few-shot learning. It can hindle many different target domains simultaneously and also obtain very strong performance, as shown in [a,b].

2. Even compared with existing models under traditional setting (training on base dataset), the performance of the proposed method is far lag behind them in clean setting. For example, for 5-shot tasks, FeLMi [c] achieves 89.47 on CIFAR-FS, 86.08 on miniImageNet and 77.61 on miniImageNet-->CUB, while this work only obtains 67.75, 47.56 and 53.70 respectively. Although the performance is improved in robust setting, the cost in clean setting is too expensive, which makes it meaningless.

3. Considering the robust test is based on PGD attack and the model also use PGD attack for training, so the main reason why this method works under the robust setting is the use of project gradient descent (PGD), which is already a very common method.

4. It is hard to believe that MetaOptNet performs worse than MAML in both clean and robust setting. In my experience, although MAML has a wider range of applications, such as reinforcement learning and so on, MAML is lag behind MetaOptNet in terms of few-shot classification. A direct evidence is the Table 6 and Table 12 in [d], where MetaOptNet achieves far better performance than MAML in both clean and robust setting. I think they are the reasonable results. Even we evaluate in the cross-domain settings, the results shouldn't be so different, since mini/Tiered-ImageNet or CARS are not so different with CIFAR-FS. MetaOptNet still should outperform MAML, as least in clean setting, although the difference could be smaller than in-domain.


### Questions
Please answer the questions in weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
