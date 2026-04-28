# Label-Agnostic Forgetting: A Supervision-Free Unlearning in Deep Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 8, 3, 5

## Abstract
Machine unlearning aims to remove information derived from forgotten data while preserving that of the remaining dataset in a well-trained model. With the increasing emphasis on data privacy, several approaches to machine unlearning have emerged. However, these methods typically rely on complete supervision throughout the unlearning process. Unfortunately, obtaining such supervision, whether for the forgetting or remaining data, can be impractical due to the substantial cost associated with annotating real-world datasets. This challenge prompts us to propose a supervision-free unlearning approach that operates without the need for labels during the unlearning process. Specifically, we introduce a variational approach to approximate the distribution of representations for the remaining data. Leveraging this approximation, we adapt the original model to eliminate information from the forgotten data at the representation level. To further address the issue of lacking supervision information, which hinders alignment with ground truth, we introduce a contrastive loss to facilitate the matching of representations between the remaining data and those of the original model, thus preserving predictive performance. Experimental results across various unlearning tasks demonstrate the effectiveness of our proposed method, Label-Agnostic Forgetting (LAF) without using any labels, which achieves comparable performance to state-of-the-art methods that rely on full supervision information. Furthermore, our approach excels in semi-supervised scenarios, leveraging limited supervision information to outperform fully supervised baselines. This work not only showcases the viability of supervision-free unlearning in deep models but also opens up a new possibility for future research in unlearning at the representation level.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Machine unlearning has been an emerging field due to increasing focus on data privacy. Typically, existing approaches toward unlearning rely on re-learning without forgotten data in a supervised manner, which is not practical since the huge amount of training costs and the need for labeled data. This paper proposes a novel machine unlearning framework without accessing any labels. They adapt the model at the representation level through approximation so that the learned knowledge about forgotten data can be removed. After the approximation, they propose a proper alignment to match changed representations to their original representations via contrastive learning. Empirically, they demonstrate the effectiveness of their unsupervised framework and outperform other supervised methods, which opens a potential new research direction in machine unlearning.

### Strengths
* Originality: This paper proposes a novel approach to unlearn without the need of labels and retraining process. They first capture the distribution of training data and forgotten data then unlearn forgotten data at the representation level. Then, through alignment with contrastive learning, they recover the shift for remaining data back to original model. These two steps, remove then recover, are original and novel, especially compared to other supervised approaches.
* Quality:  Though its low efficiency compared to other supervised methods, the results in the experiments showcase its effectiveness. Besides, they consider the scenarios that when a certain amount of supervised information is available, how helpful they would be to repair unlearning model. These shows its quality and the completeness of the paper. 
* Clarity: The presentation of this paper is clear and well-organized.
* Significance: Machine unlearning gains more emphasis due to increasing focus on data privacy. This paper proposes a new approach to solve it effectively. Additionally, it’s important to the field to do machine unlearning without using any labels and the need of retraining.

### Weaknesses
 * The first weakness of this framework is its efficiency. To capture data distribution, a certain amount of instance $x$ and two distribution modeling are needed. Though the framework doesn't need retraining process, framework efficiency and computational workload are encouraged to study and present in the paper. Specifically, the paper lacks a detailed analysis of the time complexity associated with the VAE training and the subsequent representation alignment. The number of epochs, batch sizes, and the computational resources required for these steps should be explicitly stated and compared to other unlearning methods. Furthermore, the memory footprint of the VAE models and the intermediate representations should be quantified to provide a comprehensive understanding of the computational overhead.
* The quality of representation extractor may affect framework performance. More representation extractors are needed to be considered to enhance the soundness of this method. The paper should explore the impact of different network architectures for the representation extractor, such as varying depths, widths, and the inclusion of skip connections. A sensitivity analysis is needed to understand how the choice of extractor influences the unlearning performance, particularly in terms of the trade-off between forgetting and retaining knowledge. It is also important to investigate the robustness of the approach to different types of representation extractors, including those trained on different datasets or with different levels of regularization.
* The availability to access $x$ in training data under machine unlearning scenarios lacks of description. Is this practical in the real-world scenarios? The paper needs to clarify the assumptions about the accessibility of training data, especially in the context of machine unlearning. In many real-world scenarios, accessing the original training data might be restricted due to privacy or logistical constraints. The paper should discuss the implications of this assumption and explore potential strategies to mitigate the need for direct access to the original training data, such as using synthetic data or leveraging pre-trained models.

### Questions
* In the implementation, the authors optimized the extractor unlearning loss and representation alignment loss ***alternately***. Does alternately update parameter works better than two-stage learning (saying optimize the extractor unlearning loss with the full epochs then optimize representation alignment loss)?
* (minor comment) Dot labels in Figure 1 can be replaced with their exact labels for better understanding.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a unique approach to the unlearning problem, addressing a scenario where labels may be available during training but inaccessible in the unlearning phase. This novel perspective enhances privacy protection during unlearning. The paper proposes a supervision-free unlearning method, utilizing a variational technique to model task-relevant representations' distribution. This enables effective information removal from the model. Additionally, a contrastive loss aids in model restoration, mitigating the influence of forgetting data and ensuring performance on the remaining data. The proposed method is rigorously evaluated across various tasks, demonstrating its efficacy in data forgetting, category forgetting, and denoising for noisy data.

### Strengths
This paper introduces a novel perspective on the unlearning problem by addressing a scenario where labels may be available during training but become inaccessible during the unlearning phase. This specific problem formulation is different from traditional approaches, which assume continuous access to labelled data throughout the unlearning process. This unique scenario could be a crucial addition to current unlearning, as it reflects real-world situations where label information may be sensitive, noisy, or entirely unavailable during the unlearning phase. This novel formulation expands the scope of unlearning research and adds a crucial dimension to privacy-preserving machine learning techniques. 

The paper also offers a potential impact for forgetting in deep models, emphasizing the importance of forgetting representations rather than just the correspondence between representations and labels, aligning with deep learning's characteristic of shared representation information between forgotten and retained data. 

The proposed supervision-free unlearning method, leveraging variational techniques to model task-relevant representations' distribution, is a novel contribution. This approach allows for effective information removal from the model and employs a contrastive loss to ensure model restoration, successfully mitigating the influence of forgetting data and maintaining performance on the remaining data. The strength also lies in its comprehensive experimental validation across various tasks, including data forgetting, category forgetting, and denoising for noisy data. This extensive evaluation demonstrates the efficacy of the proposed method. 

Regarding clarity, the paper is generally well-written and structured. The problem motivation and formulation are articulated in a clear and organized manner. There could be some improvement though (see weakness and questions for details)

### Weaknesses
The explanation of the contrastive loss component, particularly the utilization of the "sim loss," lacks comprehensive coverage, leaving room for confusion regarding which sim loss should be used and why use it.

While the paper is generally well-structured and articulated, there are instances where certain statements could benefit from further elucidation for improved clarity. Specific details are highlighted in the "Questions" section.

### Questions
1.	The paper assumes that training data, forgetting data, and remaining data are sampled from different distributions. Could the authors provide an illustrative example or rationale for this particular setup to justify its validity?

2.	In comparison to existing methods, it would be valuable to have an assessment of the time and storage efficiency of the proposed method. Understanding these efficiency metrics would provide additional context for evaluating the method's practicality.

3.	Could the intuitive interpretation of Equation 2 be expounded upon? Further elaboration on the meaning and implications of this equation would aid in enhancing the comprehension.

4.	The proposed method involves two approximations, one pertaining to Equation 4 where "h()" operates on all training data rather than just D_r, and the other involving Equation 8 which removes the second part. Could the authors elaborate on how these approximations may potentially impact the final output and results of the method?

5.	It's noted that both Equation 4 and Equation 6 are presented in the paper. However, it's not entirely clear how these equations are utilized in the proposed method, or alternatively, why they are not used. The paper primarily relies on Equation 5 and Equation 7, which are eventually combined into Equation 8. Additional clarification on the role and application of Equations 4 and 6 would be beneficial for a comprehensive understanding of the method.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the context of growing data privacy concerns, various methods for machine unlearning have arisen. However, these methods usually require constant supervision, which can be impractical due to the high cost of labeling real-world datasets. To overcome this challenge, this propose a supervision-free unlearning approach that doesn't rely on labels during the unlearning process. To achieve this, a variational method to approximate the representation distribution of the remaining data is done. Using this approximation, the modified model is able to remove information from the forgotten data at the representation level. To mitigate the lack of supervision, which affects alignment with ground truth, a contrastive loss is to ensure the matching of representations between the remaining data and the original model, thus maintaining predictive performance.

### Strengths
1. Quite a relevant problem in real-world applications.
2. Does not require information about the labels.
3. Experiments are extensive. The method shows good performance in the absence of data labels.

### Weaknesses
1. The optimization process lacks a clear explanation. Specifically, the rationale behind dropping certain terms in the final minimization is not adequately justified. It is unclear what the implications would be if these terms were retained. For instance, in the transition from equation 8 to equation 9, the objective changes from 'argmin' to 'argmax' without a clear explanation. This abrupt change in optimization direction requires further clarification to understand the underlying principles driving the optimization strategy.

2. There appears to be a typo in equation 1. The distribution should likely be P_r instead of P, and similarly, D should be D_r. This needs to be corrected for accuracy. Furthermore, the notational shift from 'argmin' in equation 8 to 'argmax' in equation 9 is confusing and requires a detailed explanation or correction. 

3. The paper mentions the existence of zero-shot unlearning methods that do not require access to data. This raises questions about the experimental setup presented in the paper. The current method requires access to both the retain and forget sets for modeling with VAE. In many real-world applications, the training dataset is hidden, making this assumption impractical. It is crucial to clarify how this method compares to zero-shot methods, especially considering that even in zero-shot settings, unlearning methods often do not assume access to labels.

### Questions
1. In equation 4 the term that is minimized how does it fit a VAE framework. In VAE we maximize the ELBO. Now If we take the KL term in Eq.-4 to be the Corresponding KL term in ELBO how does the first term correspond to the first term in ELBO? A detailed explanation will be better because in VAE we want to maximize the log-likelihood of data and then formulate an ELBO term. In this case, a detailed derivation with proper assumption will help to see how it is a VAE. What do we want to maximize here?
2. If my understanding is correct you drop the terms of KL in the final minimization. So it is simply an encoder without the decoder(as it is generally posed in the VAE framework). Is the formulation as VAE necessary?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on machine unlearning without the supervision of ground-truth labels during the forgetting process. They introduce a variational approach to approximate the distribution of representations for the remaining data. Leveraging this approximation, they adapt the original model to eliminate information from the forgotten data at the representation level. Experimental results across various forgetting tasks demonstrate the effectiveness of the proposed method.

### Strengths
1.	This is the first paper that solves the issue of machine unlearning without labels, which is of great importance. 
2.	The experiments are sufficient.

### Weaknesses
1. The technical part is hard to follow. Adding some illustrated figures would be better.
2.	I have a concern about the objective (2). In my opinion, data forgetting is not to maximize the distribution discrepancy to forgotten data. The relationship may be more complex.
3.	The VAE seems redundant. It is utilized to output the features on the given dataset. However, the original model can be directly used instead of training an extra model. In fact, (4) and (6) just mimic the features of the original model. So, the VAE can be viewed as an equivalent version of the original model.
4.	Several typos, e.g., jointly using $g_u^e$ and $g_U^e$. P in (1) should be P_r.
5. Why does the first constraint represent the distribution of the remaining data? The representation distribution of the remaining data over the model trained with full data is not equivalent to that of the remaining data over the model trained with only the remaining data.
6. Why does the second constraint represent the distribution of the forgetting data? The representation distribution of the forgetting data over the model trained with full data is not equivalent to that of the forgetting data over the model trained with only the remaining data.
Since the two constraints cannot represent their representation distribution separately, it may not be reasonable that the joint constraint can represent the real distribution.

### Questions
no

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
