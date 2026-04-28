# Adversarial Training for Defense Against Label Poisoning Attacks

- Decision: Accept
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
As machine learning models advance in complexity and increasingly depend on large volumes of publicly sourced data, such as the human-annotated labels used in training large language models, they become more vulnerable to label poisoning attacks. These attacks, in which adversaries subtly alter the labels within a training dataset, can severely degrade model performance, posing significant risks in critical applications. In this paper, we propose $\textbf{Floral}$, an adversarial training defense strategy based on support vector machines (SVMs) to counter label poisoning attacks. Utilizing a bilevel optimization framework, we cast the adversarial training process as a non-zero-sum Stackelberg game between an $\textit{attacker}$, who strategically poisons critical training labels, and the $\textit{model}$, which seeks to recover from such attacks. Our approach introduces a projected gradient descent algorithm with kernel SVMs for adversarial training. We provide a theoretical analysis of our algorithm’s convergence properties and empirically evaluate its effectiveness across diverse classification tasks including sentiment analysis on the IMDB dataset. Compared to baseline robust models and foundation models such as RoBERTa, our method consistently achieves higher robust accuracy as the attacker’s budget increases. These results underscore the potential of $\textbf{Floral}$ to enhance the resilience of machine learning models against label poisoning threats, thereby ensuring robust classification in adversarial environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper aims to solve the label poisoning attacks by formulating an adversarial training defense strategy, FLORAL based on SVM. The adversarial training is cast to a non-zero-sum Stackelberg game with an attacker. The projected gradient descent (PGD) is proposed to solve this problem. The experiments on two datasets show the robustness of the proposed method.

### Strengths
- The notation in this paper is generally clear, making the formula easy to follow.
- The plot illustration is clear.
- The theoretical proof and analysis is clear and promising.

### Weaknesses
 - The experiments are limited. The datasets are relatively small. 
- The author claims that FLORAL can be integrated with neural network but I did not find it. The proof here is all based on SVM and I suspect the proof for neural network, especially for the non-convex neural network, will be different. If the framework can only work and guarantee on SVM-based classifier, the contribution will be decreased a lot.
- Since it is a general method, the vision dataset, even MNIST, should be given. 
- One of the contribution is projected gradient descent. The discussion about why it works should be given.

### Questions
- What is meaning of $\mathcal{I}_C$ and $\mathcal{I}_z$ in Line 294?
- More details about Moon dataset should be given. I especially interested in the multiple classification tasks and I hope more details about the experiment details can be given.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents FLORAL, an adversarial training defense strategy that utilizes support vector machines (SVMs) to mitigate label poisoning attacks. FLORAL frames the training process as a non-zero-sum Stackelberg game, positioning an attacker who strategically poisons key training labels against the model’s objective of resilience. The FLORAL employs a projected gradient descent algorithm with kernel SVMs to improve the robustness of adversarial training.

### Strengths
1. The paper is well-presented, with clear and high-quality writing.
2. The figures are visually appealing.
3. The FLORAL achieves  SOTA  performance compared to the selected baselines.

### Weaknesses
1. All baselines examined in this paper were published before 2021. To support the claim of achieving state-of-the-art performance, the authors may consider including comparisons with more recent methods. The absence of comparisons with contemporary techniques makes it difficult to fully assess the novelty and practical relevance of the proposed approach. Specifically, methods that leverage more advanced optimization techniques or different adversarial training paradigms should be considered to provide a more comprehensive evaluation.
2. Have the authors considered placing the figures and tables at the top of the current page?
3. The authors mention using ``SVM with an RBF kernel, which serves as a basic benchmark (Hearst et al., 1998).'' Have more recent approaches been considered as benchmarks? The choice of a 1998 SVM as a primary benchmark is questionable, given the significant advancements in machine learning since then. It would be beneficial to include comparisons with more recent kernel methods or other non-linear classifiers that are known to perform well in similar settings.
4. Could the authors add a comparison with adversarial training methods? The lack of comparison with other adversarial training methods is a significant omission. Given that the proposed method is framed as an adversarial training defense, a direct comparison with existing adversarial training techniques, even those designed for feature perturbation rather than label poisoning, would provide valuable context and help to position the proposed approach within the broader landscape of adversarial robustness.

### Questions
1. Please use the reference citation format specified in ICLR.
2. The datasets in this paper are all binary classification datasets. Does this approach apply exclusively to binary classification tasks, or could the authors provide additional results on non-binary classification datasets to expand the analysis?
3. The Moon and IMDB datasets represent entirely different types of data. Could the authors clarify the preprocessing steps applied to each dataset in the experiments? Currently, it is unclear how the proposed method effectively applies to such diverse data types？
4. The results in Table 1 show that the 1998 method, SVM, is the second-best performing method, following only the proposed approach. This is somewhat surprising, as more recent methods from 2021 or 2018 would be expected to outperform an older approach, especially given their likely state-of-the-art status upon publication. Could the authors provide an explanation for this finding?
5. RoBERTa is widely regarded as a pre-trained language model in the NLP community. Could the authors explain the rationale for using RoBERTa as a baseline in this study?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces FLORAL, a defense mechanism against label-flipping poisoning attacks targeting machine learning (ML) models. The authors argue that these poisoning attacks, which alter the training data labels to mislead model learning, pose a more challenging defense problem than attacks based on feature manipulation.

The FLORAL defense is based on the formulation of the training problem as a non-zero-sum Stackelberg game. This novel approach transforms the learning problem under poisoning attacks into a bilevel optimization problem. The training is performed during several rounds, during which an attacker tries to maximize the damage induced by label flipping while the training algorithm minimizes the loss of the dataset poisoned by the attacker. FLORAL uses a projected gradient descent algorithm to solve this optimization problem, tailoring the solution specifically to support vector machines (SVMs) while indicating that it can be extended to neural networks. The authors provide theoretical proof that model parameter updates by FLORAL remain bounded and that the algorithm converges to the Stackelberg equilibrium.

Regarding experimental validation, FLORAL is tested on both a synthetic dataset and the IMDB sentiment analysis dataset, using seven established defenses as baselines. On the synthetic dataset, a SVM protected by FLORAL significantly outperforms these baseline defenses, maintaining robustness even with 40% of poisoned labels. For the IMDB dataset, FLORAL-defended SVM is compared against a RoBERTa language model. The results demonstrate that an SVM trained with FLORAL on the poisoned IMDB subset performs more robustly than a poisoned RoBERTa model as the percentage of poisoned labels increases.

### Strengths
Thanks to the authors for submitting this interesting work. The proposal of the paper is for sure original and novel since the problem of defending an ML model against a label flip poisoning attack is cast as an adversarial training problem for the first time. The specific formulation of the problem as a non-zero sum Stackelberg is also original and enables the design of a defense algorithm that outperforms existing defenses. Moreover, the theoretical analysis behind the convergence to the optimum of the proposed training algorithm is good. Finally, regarding the experimental evaluation, it is appreciable that the experimental evaluation considers several state-of-the-art defenses. In this way, it is possible to assess that the proposed defenses overcome several defenses and not some specific ones.

### Weaknesses
A key weakness of the paper lies in the lack of clarity about the motivation for using adversarial training to counter poisoning attacks and for formulating the problem as a non-zero-sum Stackelberg game. Adversarial training, particularly in the context of evasion attacks on ML models, typically aims to train the model on possible attacks to make it robust against test time attacks, as explained in Sections 1 and 3.3 in this paper. Instead, defenses against poisoning attacks often focus on removing or mitigating the impact of poisoned samples once the attack _has already been performed_. Given this distinction, the paper does not sufficiently explain why including a simulated poisoning attack within the training procedure should diminish the impact of already poisoned samples. The motivation seems clear when the training set is clean: the training procedure takes into account the worst attacks that the attacker can perform using the clean training set. However, in practice, the defense algorithm will most often be applied to an already poisoned dataset. In this scenario, the attacker in the game flips labels that can have _already_ been flipped, disrupting the initial attack performed to poison the dataset. If it is the reason behind the efficacy of the defense, the authors should state it clearly in the paper. Otherwise, they should provide an intuition behind the efficacy of the attack when it is applied to a poisoned training set. Moreover, it is not clear the meaning of the equilibrium of the game in the context of defending against poisoning attacks. The authors should also clarify this aspect. 

The experimental evaluation also appears to have several notable shortcomings that should be addressed to strengthen the validation of the proposed defense. First, the attacks used to generate poisoned datasets do not represent the state-of-the-art. While the authors demonstrate that their defense outperforms existing defenses against the relatively simple attack on the synthetic dataset, FLORAL is less effective than the baselines against the Alfa attack (Xiao et al., 2015) when considering more realistic attack budgets (e.g., 5% and 10%). While it is reasonable that a single defense may not counter every attack type, the authors should examine if the defense is also less effective than other considered defenses when considering other attacks proposed in literature, like the ones in (Biggio et. al., 2011) and (Paudice et. al., 2018). Furthermore, the effectiveness of the defense against the baselines is shown only on two dataset. To demonstrate that the defense generalizes well, the authors should consider testing it on additional datasets, as done in (Biggio et al., 2011) and (Paudice et al., 2018). Finally, the comparison between the robustness of FLORAL-defended SVMs and RoBERTa on the IMDB dataset is not fair, in my opinion. The authors states that `Adversarial datasets were created by fine-tuning the RoBERTa-base model on the clean dataset to identify influential training points` (Section 5). This approach inherently biases the attack towards RoBERTa, as it is crafted specifically to target that model. Therefore, the finding that an SVM defended by FLORAL outperforms RoBERTa in terms of robustness on a poisoned dataset may not be reliable, as the attack is tailored to RoBERTa. I suggest that the authors perform the comparison in a fairer way, for example by creating adversarial datasets by flipping the most influencial points for an SVM trained on IMDB.

Finally, the presentation of the paper is almost good, but there are a few unclear, unsupported, or potentially misleading statements that need clarification:
- In the caption of Figure 2, the authors state that `label poisoning affects any point in the input space uniformly`. However, this statement seems counterintuitive. Intuitively, flipping the labels of points closer to the decision boundary should have a greater impact on shifting the boundary than flipping labels of points far from it.
- In Section 3, the authors claim that `In the case of an SVM-based classifier, the minimax formulation would only safeguard against
attacks that target data points very far from the decision boundary. These attacks are unlikely to alter the SVM classifier significantly, as such points are less likely to be support vectors, i.e. the critical data points that define the decision boundary.`. However, no references or further explanation are provided to substantiate this observation.
- The authors describe the considered attacker in the game as white-box. However, they subsequently state that `However, in practice,
the attacker’s knowledge of the model may be limited. To account for this, we assume the attacker operates under a constrained budget, allowing the poisoning of at most B labels per round` (Section 3). This constraint does not limit the attacker’s knowledge (which remains white-box) but rather restricts the attacker’s capability to flip labels within a budget.

### Questions
- What are the motivations for employing an adversarial training procedure and formulating the defense problem as a non-zero-sum Stackelberg game? (See the Weaknesses section for further details.)
- What precisely does the Stackelberg equilibrium represent within the FLORAL algorithm?
- Could the algorithm described in Section 3.2 return a projection that does not satisfy Constraint 6 of the problem formulation? If so, what implications would this have for the convergence of the training algorithm?
- Can the authors address the concerns regarding the experimental evaluation? (See the Weaknesses section for further details.)
- Could the authors clarify the unclear and unsupported statements listed in the Weaknesses section?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an adversarial training algorithm to mitigate label flipping attacks against Kernel SVM. Label flipping attacks aim to poison the training process of a Deep Neural Nets-based model via flipping the labels of training data. Similar as the vanilla adversarial training algorithm, the proposed method defines a bi-level optimization problem. The inner-layer problem is to choose the target training samples to flip their class label, in order to maximize the training loss of the classifier. The out-layer problem aims to minimize the worst-case classification loss facing the label flipping noise. This work presents a stability analysis to prove the convergence of the proposed method. Empirical study conducted over two datasets confirms the validity of the proposed method for enhancing the robustness of Kernelized SVM.

### Strengths
It is interesting to use the framework of adversarial training to defend label flipping attacks. The design of the proposed is further enhanced with a theoretical proof the convergence of the proposed method.

### Weaknesses
1. Label flipping attacks have been extensively investigated in the past years. This study lacks a comprehensive comparison to the recent advance in this field. I list a few as below [1,2,3].

[1]. Elan Rosenfeld, Ezra Winston, Pradeep Ravikumar, and J. Zico Kolter. 2020. Certified robustness to label-flipping attacks via randomized smoothing. In Proceedings of the 37th International Conference on Machine Learning (ICML'20)
[2]. Andrea Paudice, Luis Muñoz-González, and Emil C. Lupu. 2019. Label Sanitization Against Label Flipping Poisoning Attacks. In ECML PKDD 2018 Workshops.
[3]. P. Tavallali, V. Behzadan, A. Alizadeh, A. Ranganath and M. Singhal, "Adversarial Label-Poisoning Attacks and Defense for General Multi-Class Models Based on Synthetic Reduced Nearest Neighbor," 2022 IEEE International Conference on Image Processing (ICIP), Bordeaux, France, 2022, pp. 3717-3722.

2. Why Q is chosen as ${\tilde{y}_i}{\tilde{y}_j}K_{i,j}$ is not clearly justified. Specifically, it's not clear why the kernel matrix K is not modified to reflect the potential changes in the input space due to label flips. The justification should explain why the kernel remains static despite the change in labels, and how this choice impacts the overall optimization problem.

3. It is unclear why using the dual variables $\lambda_i$ to choose training samples to flip their labels is better than using the influence function. The paper needs to elaborate on the specific advantages of using dual variables in this context, especially considering that influence functions are a well-established method for identifying influential training points. A more detailed comparison of the computational cost and accuracy of both approaches is needed.

4. The proposed method seems limited only to Kernelized SVM, yet not generalizable to other model architectures. The paper should discuss the challenges in extending this approach to other models, such as deep neural networks, and whether the core ideas can be adapted or if new formulations are required.

### Questions
1. Include more defensive baselines into the comparative study, especially [1] mentioned in the weakness comment. 

2. Clarify the bullet point 2 and 3 in the weakness comment. 

3. Justify if the proposed method can be exntended to other model architectures. If possible, please demonstrate how the proposed method can be generalized with further empirical evaluations.

### Soundness
2

### Presentation
2

### Contribution
2
