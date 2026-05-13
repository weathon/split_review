# KEFI: Kernel-based Feature Identification for Generalizable Classification

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
To achieve satisfactory generalization performance on previously unseen domains, existing domain generalization (DG) methods often assume fixed domain-invariant features from a set of training domains for good generalization on new domains. However, this assumption can be overly strict, especially when the source domains lack shared information or when the target domains utilize information from selective source domains in a compositional manner. This leads to the natural question of how we utilize information from the source domain to the target domain in an appropriate way. In response to this challenge, we propose an innovative framework that includes an attribute-based feature extractor that captures from the source domains semantically meaningful components referred to as \textit{attributes} and a \textit{Kernel-based Attribute Identifier} that leverages kernel learning theory to define the decision boundaries for these attributes collected from the source domains. This dynamic learning approach empowers the classifier to effectively identify the learned attributes in the domains it has not encountered before. We empirically validate our method on well-established DG benchmarks,
achieving competitive results compared to state-of-the-art techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes KEAI, a framework for domain generalization (DG) using attribute representations and kernel learning. It extracts meaningful attribute features from source domains and uses kernel methods to cluster them into distinct bases with clear decision boundaries. At test time, KEAI identifies which learned attributes are present in the target domain and selectively utilizes them for prediction. The main contributions are 1) an attribute-based representation for DG capturing semantic concepts, 2) a kernel learning approach for robust attribute identification across domains, and 3) achieving strong empirical results compared to prior DG methods. KEAI provides an innovative way to leverage source knowledge when generalizing to new target domains. Experiments validate its effectiveness for domain generalization over the listed baselines.

### Strengths
1.	The paper is dedicated to the utilization of target domain-specific information to improve the domain generalization ability of the model, and the proposed method is able to better determine whether a piece of information is present in the target domain or not, compared with the previous methods.
2.	Experiments across standard DG benchmarks demonstrate improvements over the listed baselines.
3.	The proposed techniques are technically sound, with proper formalizations.
4.	The paper is well organized, and the architecture and algorithm descriptions are sufficient.

### Weaknesses
1.	The motivation for this paper is not detailed in the introduction. Detailed examples of why and how previous methods have failed to utilize target domain-specific information are needed.
2.	Contributions and novelties of this paper compared to previous studies are not explicitly presented in the paper. The novelty of this paper is limited since the kernel-based methods have been widely studied.
3.	There is no comparison of experimental results with the latest state-of-the-art methods. Important references published after 2021 were not investigated.
4.	Experiments are not sufficient to support claimed benefits, such as determining whether an attribute is present in the target domain.

### Questions
1.	What is the main contribution of this paper relative to previous methods, just relying on determining whether an attribute appears in the target domain does not prove that this work has a breakthrough, please clearly describe the contribution and novelty of this paper.
2.	The approach in this paper first performs attribute representation learning and then utilizes a kernel-based approach to categorize the attributes. So, how does the method determine whether an attribute is present in the target domain or not since the training process does not include a structure to process the attribute's origins?
3.	Why are there no up-to-date state-of-the-art methods for comparison, the methods reported in the paper were published in 2021 and before. Additional results with the latest methods are needed to demonstrate the validity of the proposed methods.
4.	The paper does not report the experimental results of the proposed method in identifying whether an attribute appears in the target domain or not. Therefore, the motivation and claimed effectiveness of this method is difficult to prove.
5.	How does the method in this paper perform in a multi-source domain setting? The experimental results in a simple single-source domain setting are not sufficient to prove the superiority of the approach.
6.	Why did the paper not investigate the literature published after 2021 such as [1] and [2].
[1] Pcl: Proxy-based contrastive learning for domain generalization, CVPR2022.
[2] Style neophile: Constantly seeking novel styles for domain generalization, CVPR2022.

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed an attribute-based feature extractor to capture semantically meaningful components  from the source domains referred using a Kernel-based Attribute Identifier. It leverages kernel learning theory to define the decision boundaries for these attributes collected from the source domains. They evaluate on multiple benchmarks to compare with several methods.

### Strengths
This paper proposed an attribute-based feature extractor to capture semantically meaningful components  from the source domains referred using a Kernel-based Attribute Identifier. Generally, the paper is easy to follow and such idea is interesting. They evaluate on multiple benchmarks to compare with several methods.

### Weaknesses
The attribute-based representation seems very tricky to obtain, especially for multiple source domains, it is not reasonable to put all sources together to learn the attribute-based representation. Different domains do have their own domain-specific attributes. The experiments do have provided such results to interpret what the attribute-based representation. Are they meaningful or matched with human-understandable attributes.

The performance improvement is not good enough, as shown in Table 1. The improvement is marginal.

### Questions
The interpretation of attribute-based representation.

The performance improvement.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an attribute-based feature extractor and leveraging kernel learning theory to delineate the decision region of attributes collected from the source domain.

### Strengths
1. The KEAI framework efficiently captures meaningful components from source domains, addressing challenges in domain generalization.

### Weaknesses
1. How to find K (K group), by tuning? If yes, the ablation study on K is missing
2. Why are the dimensions of attributes equal? An explanation or proof is missing
3. The computation cost of the whole algorithm is missing
4. Experimental results are not convincing. E.g., Table 1,  the experimental results seem sometimes worse than others. Ablation study didn't compared with other methods.
5. Some typo in formulations, e.g., missing +C*$\xi_k$ in soft version
6. Confused about the basis of attributes? How could you find the basis of attributes by formulation (3) without any attribute labels?

### Questions
1. Confused about the basis of attributes? How could you find the basis of attributes by formulation (3) without any attribute labels?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the domain-free domain generalization (DG) problem, where the domain labels for multiple source domains are unavailable in the learning procedure. To extract the representations with explicit semantic structure and interpretable components, i.e., attributes, this work proposes a kernel-based attributes identifier, where the attributes are learned with parameterized feature extractors and then the effective attributes are selected by the proposed identifier. By feature selection, the learned representations have less redundant information compared with the considering the combination of all attributes. Experiments on standard DG datasets are conducted, where the proposed method outperforms other comparison methods.

### Strengths
+ A kernel-based feature extraction and selection method is proposed to learn the attributes in multiple domains; the basic motivation is clear.
+ Experiment analysis is conducted from different aspects, e.g., comparison and ablation.

### Weaknesses
 - The related works in DG are not properly discussed. Indeed, there are methods that share the same motivation and goal with the proposed method, i.e., learning attributes with the complex multi-domain data. Thus, it is hard to evaluate the real merits of this paper.
- The technical parts are presented directly, while the innovations and justifications are insufficient.
- The comparison methods in experiments should contain more latest SOTA methods.

- The discussion on related works is indeed insufficient. Basically, this method focuses on learning interpretable representations with explicitly decomposed components. However, there are works that also consider the decomposition or encoding of attributes from different perspectives, e.g., information bottleneck [r1] and rate reduction [r2].

- In the methodology part, only the kernel-based feature selection procedure is presented, while the justification and in-depth analysis are also necessary. Specifically, compared with other methods that also aim at learning attributes, what are the limitations in the existing methodology? Correspondingly, what are the advantages and weaknesses of the proposed method in learning components?

- In experiment validation, the proposed method achieves higher accuracies compared with other methods, while the comparison methods are generally proposed before 2021. To ensure a fair and appropriate comparison, the latest SOTA methods in DG are highly expected to be considered.

- Though it is natural to decompose the input into different attributes, the number of attributions $K$ seems to be a hyper-parameter and the learned $K$ attributes lack interpretability. In related works, e.g., [r1], some justifications and intuitions are provided for learned attributes.

- Since $K$ is a hyper-parameter, it is indeed necessary to provide theoretical analysis or reasonable explanation. In its current form, only experiment results with different parameter selection is provided, while the analysis is insufficient.

### Questions
1. The discussion on related works is indeed insufficient. Basically, this method focuses on learning interpretable representations with explicitly decomposed components. However, there are works that also consider the decomposition or encoding of attributes from different perspectives, e.g., information bottleneck [r1] and rate reduction [r2].

2. In the methodology part, only the kernel-based feature selection procedure is presented, while the justification and in-depth analysis are also necessary. Specifically, compared with other methods that also aim at learning attributes, what are the limitations in the existing methodology? Correspondingly, what are the advantages and weaknesses of the proposed method in learning components?

3. In experiment validation, the proposed method achieves higher accuracies compared with other methods, while the comparison methods are generally proposed before 2021. To ensure a fair and appropriate comparison, the latest SOTA methods in DG are highly expected to be considered.

4. Though it is natural to decompose the input into different attributes, the number of attributions $K$ seems to be a hyper-parameter and the learned $K$ attributes lack interpretability. In related works, e.g., [r1], some justifications and intuitions are provided for learned attributes.

5. Since $K$ is a hyper-parameter, it is indeed necessary to provide theoretical analysis or reasonable explanation. In its current form, only experiment results with different parameter selection is provided, while the analysis is insufficient.


[r1] Li, Bo, et al. "Invariant information bottleneck for domain generalization." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 36. No. 7. 2022.

[r2] Chan, Kwan Ho Ryan, et al. "ReduNet: A white-box deep network from the principle of maximizing rate reduction." The Journal of Machine Learning Research 23.1 (2022): 4907-5009.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
