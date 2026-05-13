# Rethinking Adversarial Robustness in the Context of the Right to be Forgotten

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
The past few years have seen an intense research interest in the practical needs of the "right to be forgotten", which enables machine learning models to unlearn a fraction of training data and its lineage. As a result of this growing interest, numerous machine unlearning methods have been proposed and developed to address this important aspect of data privacy. While existing machine unlearning methods prioritize the protection of individuals' private and sensitive data, they overlook investigating the unlearned models' susceptibility to adversarial attacks and security breaches. In this work, we uncover a novel security vulnerability of machine unlearning based on the insight that the adversarial vulnerabilities can be bolstered especially for adversarial robust models. To exploit this observed vulnerability, we propose a novel attack called Adversarial Unlearning Attack (AdvUA), which aims to generate a small fraction of malicious unlearning requests during the unlearning process. AdvUA causes a significant reduction of adversarial robustness in the unlearned model compared to the original model, providing an entirely new capability for adversaries that is infeasible in conventional machine learning pipelines. Notably, we also show that AdvUA can effectively enhance model stealing attacks by extracting additional decision boundary information, further emphasizing the breadth and significance of our research. Extensive numerical studies are conducted to demonstrate the effectiveness of the proposed attack. Our code is available in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Unlearning allows machine learning models to forget training data, however existing machine unlearning methods do not consider the security implications of unlearning. The authors propose a new attack called Adversarial Unlearning Attack (AdvUA), which can exploit a security vulnerability in machine unlearning to reduce the adversarial robustness of unlearned models (white and black box scenario). AdvUA learns the decision boundary information of the victim target model and it works by generating malicious unlearning requests that target specific parts of the model that are important for decision making. This makes it easier for the attacker to extract decision boundary information by observing how the model behaves on the remaining training data.

### Strengths
The paper makes a significant contribution to the field of machine learning security by highlighting the importance of considering security when designing and implementing machine unlearning methods.  Strengths:
- Well written paper and identifies an important security vulnerability in machine unlearning.
- Proposes an effective attack, AdvUA, that can exploit vulnerability to significantly reduce the adversarial robustness of unlearned models.
- Provides a comprehensive evaluation of AdvUA on a variety of models and datasets, demonstrating its effectiveness against both standard and certified defense methods.

### Weaknesses
1) AdvUA can be computationally expensive, especially for large and complex machine learning models. How does the computation time complexity of AdvUA against certified defense methods vary based on the number of unlearning samples?

2) The authors should conduct further evaluation on real-world systems to better understand the practical impact of AdvUA.

### Questions
Questions for authors: 

Concern 1: Results show that AdvUA can perform reasonably well against certified defense methods, even when unlearning only a small number of training samples. How does the effectiveness of AdvUA against certified defense methods vary depending on the specific certified defense method used?

Concern 2: It is about the AdvUA attack’s computational time complexity in black box scenarios. How does the computation time complexity of AdvUA against certified defense methods vary based on the number of unlearning samples?

Concern 3: The effectiveness of AdvUA depends on the selection of the malicious unlearning requests, it is possible to design an algorithm to select suboptimal set of malicious unlearning requests?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In contrast to previous works that is focused on the adversarial robustness of a simple classifier, this paper takes care of a new setting: how to decrease the robustness of models during theunlearning process. Correspondingly, they proposed a new attack which is called AdvUA. The effectivenss of AdvUA is evaluated in both white-box and black-box setting. In addition,  AdvUA can further improve the performance of model stealing attack.

### Strengths
1 The soundness of AdvUA is good.

2 The experiment is relatively sufficient

3 It seems that AdvUA will bring significant gain to ASR of the mainstream attack, e.g. C&W and PGD attack.

### Weaknesses
 1 Although the experimental section shows promising gain on ASR after applying AdvUA, an important metric is obviously ignored: **the benign accuracy** of the model after unlearning. Ideally, a powerful attack will not only improve the ASR  but also has marginal impact on the benign function of the threat model. Therefore, I would suggest authors report both ACC  and ASR instead of ASR alone. Specifically, it's crucial to understand the trade-off between increased attack success rate and potential degradation in model performance on clean examples. The absence of this analysis makes it difficult to assess the practical implications of the proposed method.

 2 Some minor error exists: For example,"PDG" in Page 7.  I would suggest authors re-read the whole paper for further corrections. 

 3 The writing of this paper is not easy to follow for me. Some partitions of paper are redundant: For example, after definition 2, "the attacker misleads the unlearned model $W^u$ to directly misclassify the target victim samples without any further perturbations." What insights does this conclusion provide for the design of AdvUA? This statement, while potentially true, lacks a clear connection to the subsequent methodology. The paper would benefit from a more explicit explanation of how this observation informs the design choices in AdvUA.

 4 The computational cost of AdvUA could be unaffordable when the dataset is huge. Algorithm 1 shows that AdvUA needs to at least iterate through the data $|S_e|\times B\times |K_v|$ times. When $|S_e|$ is huge, large $|K_v|$ is needed to ensure the accuracy of accessment.  It may sharply increase the computational expenses of AdvUA. The paper should provide a more detailed analysis of the computational complexity and discuss strategies to mitigate the cost for large-scale datasets. The current discussion is insufficient to address the practical limitations of the proposed approach.

### Questions
1 Why don't the starting points of AdvUA, kNN, and Random overlap in Figure 6?

2 Almost all experiments are performed on CNNs. ViT are the another prevailing architecture in computer vision. Can AdvUA help exisiting attacks better envade robust ViTs [1,2] during unlearning? 

3 The authors only consider one kind of black-box settings:  The attacker use a surrogate model to unlearn various numbers of training samples with the first-order based method and then generate the adversarial examples. However, another black-box setting is that:  The attackers use a surrogate model to select samples for unlearning and victims use the selected samples to unlearn their own models. Is AdvUA effective in this situation?

For other questions, please refer to the weakness section.

[1] Mo et al. When Adversarial Training Meets Vision Transformers: Recipes from Training to Architecture. In NeurIPS 2022

[2] Peng et al., RobArch: Designing Robust Architectures against Adversarial Attacks, In arXiv 2023

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Based on the hypothesis that unlearning increases the vulnerability of deep learning models to adversarial attacks, this study examines methods to achieve adversarial attacks using unlearning on models without using adversarial perturbations. The authors have experimentally demonstrated that unlearning with randomly selected samples increases vulnerability to adversarial attacks. Also,  
 the authors introduced an algorithm that increases vulnerability more efficiently by selecting samples to be unlearned based on the density of the training data and the direction of the target sample.

### Strengths
The relationship between unlearning and adversarial robustness has never been discussed before, and this study makes us aware of a new research direction for the community. The experiments are meticulously conducted, and the results are reliable.

### Weaknesses
The intent of Theorem 2 is not clear. Could you please explain what theoretical justification this theorem gives about the proposed method?



### Questions
Question:
The intent of Theorem 2 is not clear. Could you please explain what theoretical justification this theorem gives about the proposed method?

Comments:
- Unlearning U should be defined as a mapping with specifying inputs and output.
- H should be should be defined before it appears for the first time.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce and highlight the notion that adversarially robust models can become more vulnerable to adversarial attacks after the model performs machine unlearning on a specified set of training examples. In light of this insight, the authors propose Adversarial Unlearning Attack (AdvUA), an unlearning attack that significantly reduces the robustness of the target model. Specifically, AdvUA selects training examples to unlearn that are both close to the target victim examples and in the same directional alignment as the adversarial attack. Experiments on 4 datasets using 6 different models, 3 adversarial attacks, and 2 unlearning techniques suggest AdvUA selects training examples to unlearn that lead to significantly less robust models than the chosen baseline methods: a kNN based approach that selects the k-nearest training examples to unlearn, and a random method which selects training to remove uniformly at random.

### Strengths
* The authors highlight an important vulnerability of adversarially robust models, this work is especially pertinent given the rapid rise in popularity of different machine unlearning techniques.

* The proposed method, AdvUA, is a simple approach that uses regional density and adversarial attack direction to maliciously select training examples to unlearn. The simplicity and effectiveness of this approach makes it potentially generalizable to a wide range of models and domains.

* The paper is relatively well-written and easy to follow.

* Experiments with different models, datasets, adversarial attacks, and unlearning techniques provides evidence that AdvUA outperforms the chosen baseline selection methods.

* The authors also evaluate AdvUA in black-box settings related to attack transferability and model stealing attacks.

### Weaknesses
 * One of my main concerns is the robustness of the results. The experimental setup section describes the experiments use 4 datasets, 6 model architectures, 3 adversarial attacks, and 2 unlearning techniques. This setup enables more than 140 different dataset-model-attack-unlearning combinations, however, the results in each section tend to only show a very select subset of these combinations. For example, Figure 6 only shows 2 attacks on the CIFAR-10 dataset, and 1 attack for the SVHN dataset; why aren't all the results shown for all the dataset-model-attack combinations, or aggregated in some way to give readers a general sense of AdvUA's effectiveness across different settings?

* I think there could be a more in-depth discussion between the $k$NN based approach and AdvUA using local density only. A comparison of $k$NN to this ablated version of AdvUA may be insightful and beneficial to readers. It's also not clear to me how $k$ is chosen in the experiments, and how impactful the choice of $k$ is on the results.

* It's not clear to me how robust AdvUA is to different unlearning techniques. I think a plot comparing results using the two different unlearning techniques would provide more evidence to the generalizability of the proposed approach. Have the authors also experimented with the gold standard unlearning technique of retraining from scratch on a small dataset/model?

* The clarity of the paper could be improved, please see the "Questions" section for details.

* There are some minor grammatical errors throughout the paper, consider using a service like Grammarly to fix these issues.

* Consider listing what datasets and models are being shown in Figure 6.

* Figures 1, 7, and 8 are not colorblind friendly.

### Questions
* What is the non-robust accuracy of the different models in Figure 1? It may be beneficial to readers to see that comparison.

* Is Figure 2 showing the density of training examples before or after unlearning?

* What dataset is being shown Figure 4? Also, how significant is the $\ell_{wd}$ gap between "before" and "after" unlearning for each local density scale in Figure 4? What does the "local density scale" represent, and how does it differ from $\ell_{wd}$?

* Where are the kNN and random baseline methods in Figure 7?

* Have the authors thought about how AdvUA can be used to train more robust models?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
