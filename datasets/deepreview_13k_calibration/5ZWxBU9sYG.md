# How to Craft Backdoors with Unlabeled Data Alone?

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3

## Abstract
Relying only on unlabeled data, Self-supervised learning (SSL) can learn rich features in an economical and scalable way. As the drive-horse for building foundation models, SSL has received a lot of attention recently with wide applications, which also raises security concerns where backdoor attack is a major type of threat: if the released dataset is maliciously poisoned, backdoored SSL models can behave badly when triggers are injected to test samples. The goal of this work is to investigate this potential risk. We notice that existing backdoors all require a considerable amount of \emph{labeled} data that may not be available for SSL. To circumvent this limitation, we explore a more restrictive setting called no-label backdoors, where we only have access to the unlabeled data alone, where the key challenge is how to select the proper poison set without using label information. We propose two strategies for poison selection: clustering-based selection using pseudolabels, and contrastive selection derived from the mutual information principle. Experiments on CIFAR-10 and ImageNet-100 show that both no-label backdoors are effective on many SSL methods and outperform random poisoning by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors defined NLB (No-Label Backdoor) attacks, which poisons an unlabeled dataset, such that SSL (Self-Supervised Learning) models trained upon it exhibits both targeted and untargeted backdoor behavior when it is finetuned for a downstream task.
And proposed both a clustering-based and a contrastive method for selecting a subset of training data to perform NLB by injecting BadNet triggers. The proposed methods, especially the contrastive method, significantly outperforms the random baseline across SimCLR, MoCo v2, BYOL and Barlow Twins.

### Strengths
1. The NLB attack setting sounds innovative and interesting, given that SSL models are the dominating majority of foundation models.
2. The authors introduced intermediate/intrinsic metrics like CCR (Clustering Consistency Rate) and joint mutual information to assist the comprehension of their poison backdoor selection method.
3. The authors also included experiments to compare NLB with label-aware oracles and to test the resistance to finetuning.

### Weaknesses
1. The authors demonstrated extremely limited literature review. They rendered Trojan attacks on SSL models as an underexplored topic while there have been a number of works investigating it [1,2,3,4]. Also, the excuses the authored found to rule out Trojan attacks on Text-Image contrastive learning from comparison isn't convincing. This paper ended up with random selection as the only baseline, giving in a misleading result as if their method performs very well, while a minimum poison rate of 0.2 is by no means acceptable comparing to the commonly used 1% poison rate.
2. The paper lacks a clear demonstration of how their method is being used and evaluated in practice, e.g. how the BadNet/Blend triggers are injected, how ASR is being computed, how CCR, especially for label-aware case, is determined, etc. Their account of mutual information is also very crude and is hardly related to their eventual "efficient" implementation.
3. The experiments are limited to relatively old SSL models and more recent models like DINO, DINO v2, MoCo v3, Mugs, etc are not involved.
4. The experiments are limited to using the same relatively small dataset for both (poison/pre) training and (downstream/defensive) finetuning.

### Questions
1. Why do the authors not compare their attack with any of the existing Trojan attacks against SSL, like [1,2,3,4]. Instead of crafting a backdoor attack, this work sounds more like proposing a clever way of selecting a subset to poison with random and dated triggers targeting old models and small datasets, but the eventual poison rate is remarkably high.
2. How is CCR computed for label-aware methods? Did you mean in Table 3 that you randomly poisoned $M$ samples from the class (in terms of label) of data that is most heavily chosen by the proposed clustering-based/contrastive method?
3. Why label-aware methods only poisoned the class chosen by the proposed method instead of all possible ones given that you are testing the poison subset selection performance and the real oracle choice could fall in a different class?
4. Why would a poison attack on a high CCR subset be expected to generalize to other data? With high CCR, couldn't $H(Z^*|S)$ be very low and causes the poison to be effective for the class that is most heavily impacted only? In Figure 5, many classes are still forming an identifiable cluster despite being drawn closer. Which classes of them contain samples that are being selected by your methods?
5. The same dataset is being used for finetuning and training which doesn't resembles the practical use the most. How about taking a SSL trained model on ImageNet-100 and finetune it on CIFAR-10 and vise versa? What about some other defensive methods like backdoor removal methods.
6. If the choice of SSL model for feature extraction is not relevant as in Table 6, do they result in the same/very similar choice of poison dataset? It will be nice to see their ratio of overlapping part. If they are dissimilar, why? In addition, given that there is a "pseudo target class" eventually (thus high ASR), have you considered using a target class's average feature as an anchor and optimize for a trigger instead of using a fixed one?
7. In Section 2.2 why would lower ASR be the attack's goal? Is that a typo?
​

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes poison selection strategies for backdoor poisoning in Self-Supervised Learning.

The two proposed strategies are
(1) K-means clustering-based selection using pseudolabels
(2) contrastive selection derived from the mutual information principle

In the first approach, unlabeled data is annotated using “pseudolabels” by clustering algorithms like K-means, and use these cluster pseudolabels for choosing a cluster of samples for backdoor trigger injection.

But as the authors experimental demonstrate, this approach has some limitations. K-means produces imbalanced clusters
and low class consistency rate (CCR) [the ratio of samples from the most frequent class in each cluster].

The second strategy attempts to mitigate the issues above by using a mutual information (MI) formulation. The idea is to associate triggers with chosen samples so that it introduces a good backdoor feature. The MI approach generates poison sets whose members have high similarity with each other and low similarity with other non-poisoned samples.

Experiments demonstrate that the MI approach to select poison samples performs better than random selection and clustering based for poisoning SSL methods like SimCLR, MoCo v2, BYOL and Barlow Twins on datasets CIFAR10 and ImageNet100.

### Strengths
The paper attempts to solve the problem of automatically choosing unlabeled samples to add triggers to when poisoning a Self-Supervised Learning (SSL) dataset. Prior work has assumed that information about the poison set is available to the attacker in some form, which ensures similarity of poison set samples. This approach might boost attack performance of Backdoor Attacks against SSL methods.

The paper attempts to solve the problem using a naive approach of k-means clustering and then proposes to use the Mutual Information (MI) formulation to select poison sets. The baselines used are sound, and the experiments are performed on a set of widely used SSL methods.

The writing is good, and the paper is easy to follow.

### Weaknesses
The major weaknesses I would like to point out are:

1. The paper is currently missing experiments to show how the selection strategy performs against the defense proposed in this paper.

[A] Tejankar, Ajinkya, et al. “Defending Against Patch-based Backdoor Attacks on Self-Supervised Learning.” Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

This defense technique is extremely relevant to SSL attacks, and I believe the paper should incorporate this defense in its experiments.

2. The paper does not provide any information about the poison set clusters created by the algorithm. As a starting point, I would like to see a histogram of labels in the poison set chosen and also the target pseudolabel of the poison set. Do the selection strategies pick certain labels? Does that provide us with any information about which classes in the dataset are more likely to be better candidates for adding triggers?

3. (Section 4) The paper says, “We set the default poison rate to 60% of the number of samples per class, which amounts to 6% of CIFAR-10 and 0.6% of ImageNet-100 in total.” But in related work, the paper mentions “However, both methods require poisoning many samples from the target classes (e.g., 50% in Saha et al. (2021)), which is hard to get for the attacker that only has unlabeled data.” It seems the paper ends up using a higher poisoning budget than prior work for their main experiments. Why is such a high poisoning budget required, and does that diminish advantages over prior work?

### Questions
Some additional questions which I would like clarification about.

1. (Section 2.2) “calculate attack success rate (ASR) w.r.t. this class (lower the better).” Is lower better or higher better for ASR?

2. (Section 3.1) If it's an unlabeled dataset, how is the K to be chosen? For example, what is K if we want to add No-Label Backdoors to Common Crawl?

3. (Section 3.1) Figure 2(a) seems to show results from multiple K-means runs with K=10. How many times was the K-means clustering repeated?

4. (Section 3.2) To the best of my knowledge, typical multi-view contrastive SSL is based on maximizing mutual information between two augmented views of the same image.

[B] Su, Weijie, et al. “Towards all-in-one pre-training via maximizing multi-modal mutual information.” Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

[C] Bachman, Philip, R. Devon Hjelm, and William Buchwalter. “Learning representations by maximizing mutual information across views.” Advances in neural information processing systems 32 (2019).

It would be great if there is some clarification regarding whether the above statement is more representative of SSL than “The mutual information principle is a foundational guideline to self-supervised learning: the learned representations Z should contain the most information of the original inputs; mathematically, the mutual information between the input X and the representation Z”. 

The authors can provide references to prior work where SSL is formalized as maximization of I(X;Z).

This paper might be relevant.

[D] Tschannen, Michael, et al. “On Mutual Information Maximization for Representation Learning.” International Conference on Learning Representations. 2019.

5. (Section 3.2) The symbol P in Equation 3 seems to be overloaded. P is the poison set, and it also seems to be the binary function. Some clarification regarding the notation will be helpful.

### Soundness
3 good

### Presentation
2 fair

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
The paper explores the security implications of Self-supervised Learning (SSL), focusing on backdoor attacks that could arise from maliciously poisoned datasets. Given that SSL thrives on unlabeled data to learn features economically, the authors delve into a no-label backdoor setting, a scenario distinct due to the unavailability of labeled data, which is common in existing backdoors. They introduce two strategies for selecting poison samples: a clustering-based selection utilizing pseudolabels, and a contrastive selection based on the mutual information principle. Through experiments on CIFAR-10 and ImageNet-100, they demonstrate the effectiveness of these no-label backdoors across various SSL methods, showing a significant improvement over random poisoning.

### Strengths
- The problem investigated in this paper is quite important. Self-supervised learning (SSL), which has become more popular nowadays, is also vulnerable to backdoor attacks.
- This paper is easy to follow.

### Weaknesses
 - The technical contribution is limited. This paper claims this is an un-target backdoor attack. However, the attack still samples the poisoning examples from a specific class, which is determined by the pseudo-label or the contrastive selection. The only difference with previous works is that the authors select poisoning example candidates by the clustering results, rather than the labels.
- This paper didn't mention some important works in the SSL backdoor attack (e.g., CTRL [1]). In addition, the author didn't compare the proposed work with SOTA SSL backdoor attacks.
- In the threat model, the authors assume that the attack has no domain expertise to create labels for the dataset. However, for the proposed pseudo-labeling method, the authors use $K$, the same as the number of classes, which is unavailable for the attacker according to the threat model. Therefore, the proposed method is not actionable.
- How can CCR be measured without the label information? CCR is the ratio of samples from the most frequent class in each cluster. If the attacker has no label information, how can he know the number of classes of each cluster and the most frequent class? Maybe the authors want to use it to show the statistics of the feature space, but the writing makes the readers think that the attack uses CCR to choose the cluster.
- In Figure 4, for the clustering method, the ASR first increases and then decreases. The authors should give a reason for this observation.
- The defense discussion is not enough. Fine-tuning is not a SOTA defense, especially in SSL.  The author should consider some more advanced defenses (e.g., ASSET [2]).

### Questions
Please see the weakness.

### Soundness
2 fair

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
The paper presents an approach for crafting backdoor attacks on datasets without access to label information. Namely, the authors focus on datasets used to train SSL models. In order to achieve this goal, the authors propose several techniques, such as clustering the data points in some latent space and choosing a random cluster, or 2) choosing samples that have high mutual info with each other, and low mutual info with other samples. The authors evaluate their method on 2 datasets: CIFAR10 and ImageNet-100, and implement several SSL methods. They also compare with using labels' information for backdoor attacks, which performed slightly better. Finally the authors evaluate their method against a fine-tuning defense.

### Strengths
- the paper presents an attack against SSL methods, and show its effectiveness on 2 datasets
- the attack using no labels has an ASR a bit lower than the ASR when using labels

### Weaknesses
 - the authors do not evaluate against previous methods proposed to backdoor contrastive learning methods [1,2,3]
- the authors consider only a single type of defenses, and show that the defense is not 100% effective. however, there exist several defenses that approach this problem differently, and might provide a good defense against this attack, such as [4]

### Questions
- can you please add an evaluation of the other proposed methods?
- can you add more defenses, that seem suitable against your type of attacks, and evaluate the success of your method when those defenses are used?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
