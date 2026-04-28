# Domain Prompt Matters a Lot in Multi-Source Few-Shot Domain Adaptation

- Decision: Reject
- Avg Score: 3.25
- Scores: 3, 3, 6, 1

## Abstract
Large vision-language models have demonstrated strong performance in multi-source few-shot domain adaptation (MFDA). Current methods predominantly like CoOp rely on identifying a domain-agnostic prompt, leading to the overlooking of known difference information between domains. However, extracting the domain information requires the model to have good identification ability for domain information. Although training models with domain prompts allow them to capture the specific semantic nuances of a particular domain, using learnable prompts increases the risk of overfitting on training samples and reduces the effectiveness of domain prompts in capturing target domain features during transfer. To address this challenge, we propose "domain-aware mixup," a method that allows the model to become more sensitive to specific domain information when facing cross-domain mixed feature information. Specifically, we design the prompt structure composed of domain prompt and context prompt to narrow the gap between the specific domain feature and the specific image feature extracted from the cross-domain mix feature. This approach enables us to efficiently train domain prompt terms, enhancing the model's ability to distinguish semantic distinctions between different domains. We empirically validate our method on the DomainNet and OfficeHome datasets, observing a performance boost of 5.3%-5.8% over the CLIP model and a 1.1%-1.5% advantage over the domain-agnostic tuning method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method to improve multi-source few-shot domain adaptation in large vision-language models. This new method uses a structured prompt with domain and context prompts to narrow the gap between specific domain and image features, enhancing the model's ability to distinguish between different domains. Experimental results on DomainNet and OfficeHome datasets show performance improvements against the state-of-the-art.

### Strengths
The author conducted adequate evaluation to support the proposed approach.

### Weaknesses
The paper is challenging to follow, and many of the concepts and motivations are either incorrect or unclear.

**Several claims that are unclear and unsupported:**

1.	“Using learnable prompts increases the risk of overfitting on training samples, which reduces the ability of domain prompt models to extract common semantic features. “ . This is not justified and likely wrong. If training one prompt for a domain do not have the issue, then training multiple prompts respectively for multiple domain should not have the issue as well. The authors need to provide a more rigorous argument or empirical evidence to support this claim. The risk of overfitting is not inherent to the number of prompts but rather to the complexity of the prompts relative to the data available for training. Simply stating that more prompts lead to overfitting is not sufficient.

2.	“Large-scale pre-trained vision-language models lack domain awareness during training, which hinders the acquisition of domain-specific tendencies necessary for effective domain adaptation tasks. “. The general training of a model should not influence its adaptation ability. The pre-training process aims to learn generalizable features, and the adaptation process should be able to fine-tune these features for specific domains. The authors need to clarify why the lack of domain awareness during pre-training is a specific problem for their approach, especially when domain-specific information is available during adaptation.

3.	“These models often misinterpret source domain-specific semantic features as belonging to the target domain, resulting in suboptimal performance for multi-source domain adaptation through prompt learning.” I think prompt tuning is proposed to address the problem that a model use source domain knowledge to complete tasks in target domain. The authors need to explain why standard prompt tuning is insufficient to address this issue and how their method specifically mitigates this misinterpretation. The claim that models misinterpret source features as target features needs more justification, as prompt tuning is designed to align the model with the target domain.

4.	“We train the prompt of the domain with this mixed-up feature.”. what do you mean “the prompt”? what is "the prompt" referring to? The term "prompt" is used ambiguously. Is it a single vector, a set of vectors, or something else? The authors need to define this term precisely and consistently throughout the paper. The phrase "mixed-up feature" is also unclear. What features are being mixed, and how does this mixing process work? This needs to be clarified with specific details.

**Unclear optimization objectives:**

It is unclear what the training objectives of [d] and [v] are. Both t^s and t^k are involved in equations 6 and 7, but it is not clear which prompt is optimized to minimize equation 7. The optimization process is not clearly defined. Which parameters are being updated, and how are the gradients calculated? The relationship between equations 6 and 7 and the optimization of [d] and [v] needs to be explicitly stated.

**Unclear annotation:**

Figure 3: [v] has been used for interpreting context prompts and should not be used to represent domain features. Furthermore, in equation 8, both f_t and f_s are used to represent features from the target and source domains, and the author should maintain consistency in their terminology. The use of [v] in Figure 3 is inconsistent with its usage elsewhere in the paper. The authors need to ensure that the notation is consistent and that the meaning of each symbol is clear. The inconsistent use of f_t and f_s also creates confusion and should be addressed.

### Questions
No additional questions.

### Soundness
2 fair

### Presentation
1 poor

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
The paper presents a domain prompt learning approach designed to extract domain-specific information and tackle domain adaptation within a few-shot setting. Instead of using domain-agnostic prompts shared across all domains, the proposed method distinctively categorizes prompts into two types: domain-specific prompts and context prompts. While domain prompts are specific to their respective domains, context prompts are shared across multiple domains. To further enhance the differentiation of domain-specific information across various domains, the authors introduce a domain-aware mixup technique. The effectiveness of the proposed method has been rigorously validated on several benchmark datasets.

### Strengths
* The paper introduces a prompt-learning-based method to address domain adaptation in vision-language models. 

* The author empirically validates the method on multiple benchmark datasets.

### Weaknesses
 * Prepending and learning domain-specific or instance-specific prompt tokens to handle distribution shifts is not a novel idea. For example, to improve generalization to OOD data, the prompt vectors are conditioned on image inputs at test time [1, 2, 3]. Additionally, the idea of dividing prompts into domain-specific and domain-agnostic parts is introduced in [4]. Specifically, [4] heuristically partition the prompts into domain-specific and domain-shareable components. During adaptation, a manually crafted regularization term is employed to preserve the domain-shareable part while allowing the domain-specific component updates.

* The paper falls short in providing a thorough review of related work. The previous works on domain adaptation with prompt learning between 2022 and 2023 are missed. Several works are mentioned above, and thus I suggest the author undertake a more exhaustive literature review and highlight the differences between the proposed method and those previous works.

* The presentation of the problem setting and motivation requires further clarification. While the paper puts forth a solution for few-shot domain adaptation, it doesn't clearly delineate the inherent challenges of the few-shot setting. Readers might wonder: How do limited labels influence the model's training? Specifically, does this scarcity impact the modeling of multi-source domains or the transfer of knowledge from the source to the target domain? The paper should elaborate on how the proposed method specifically addresses the challenges of limited data in a multi-domain scenario, as opposed to simply applying prompt learning techniques.

* The claims in the paper lack evidence. The author mentioned the extraction of domain information becomes more complex in multi-domain settings and using learnable prompts increases the risk of overfitting on training samples. However, those claims are neither supported with references nor empirical results. The paper needs to provide empirical evidence or theoretical justification for these claims. For instance, experiments could be designed to show the increased complexity of domain information extraction in multi-domain settings, or to demonstrate the overfitting risk of learnable prompts with limited data.

* The writing of the introduction may pose challenges for readers who are new to the subject because the author mentions many terms but without adequate explanation. For example, what are context prompts? What are the differences between the domain and the semantics? What are context variables and domain variables? What is cross-domain mixed feature information? The paper needs to define these terms clearly and provide examples to illustrate the concepts. Without a clear understanding of these terms, readers may struggle to grasp the novelty and contribution of the proposed method.

### Questions
Please see the section on weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the challenges in multi-source few-shot domain adaptation (MFDA) using large vision-language models. Current methods, like CoOp, utilize a domain-agnostic prompt, which often neglects the differential information between domains. The authors suggest that although training models with domain-specific prompts can help capture the unique semantic nuances of a domain, it also increases the risk of overfitting. To overcome these challenges, the authors introduce "domain-aware mixup," which allows the model to become more attuned to domain-specific information during cross-domain feature mixing. They empirically validated their method on DomainNet and OfficeHome datasets and reported performance improvements over existing models.

### Strengths
- The paper addresses a crucial problem in the domain of few-shot domain adaptation.

- The introduction of "domain-aware mixup" is a novel approach to handle the challenges of domain adaptation.

- Empirical validation on standard datasets provides evidence of the proposed method's effectiveness.

### Weaknesses
 - The paper could benefit from more ablation studies analyzing the effects of different prompts. Specifically, it is unclear how the performance varies with different types of prompts (e.g., handcrafted vs. learned prompts) and their combinations. The analysis should also include the sensitivity of the model to the prompt initialization and the number of prompts used per domain.

- The difference between the proposed method and existing works isn't clearly demarcated. The paper lacks a detailed comparison of the proposed domain-aware mixup with other domain adaptation techniques, particularly in terms of the underlying mathematical formulations and the specific mechanisms that lead to performance gains. A more rigorous comparison, perhaps through a table highlighting the differences in approach, would be beneficial.

- Implementation details and settings for the backbone model are missing. The paper does not specify the exact architecture of the vision-language model used, the pre-training dataset, or the fine-tuning parameters. This lack of detail makes it difficult to reproduce the results and assess the generalizability of the proposed method.

### Questions
- Can the authors provide more ablation experiments on the effects of the three types of prompts?

- What exactly is the differentiation between the current work and previous approaches in terms of formulae and figures presented in the paper?

- Would it be possible to test the method on more downstream tasks to evaluate its broader applicability?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses the problem of multi-source few-shot domain adaptation (MFDA). MFDA involves utilizing only a small amount of labeled data from multiple source domains and a few unlabeled data from a target domain. The goal is to transfer knowledge from the source domains to the target domain. The authors propose using the CLIP model and designing two separate pairs of prompts (a domain prompt and a context prompt) to better capture the distinct knowledge of the source domains. Additionally, a feature mixup mechanism is introduced to enhance the sensitivity to domain-specific information. Experiments were conducted on the DomainNet and OfficeHome datasets to demonstrate the superiority of this approach over CLIP and CoOP.

### Strengths
- The paper is addressing the challenging setting of MFDA.
- Prompting techniques are utilized to better learn the domain knowledge via the foundation model.
- Superior performance is achieved compared with CLIP and CoOP.

### Weaknesses
Many significant problems are found in the current format of the paper that prevents the understanding of the concept. The problem includes but is not limited to confusing writing, inconsistency of notations, expressions of novelty, experimental presentation etc. It is highly recommended that the authors to re-write the paper, re-organize the content and better polish the text for the reader to better understand.

The major problems:
* Novelty is limited:
    - The proposed method as in Sec. 3.2 is very similar to DAPL but extended to multi-source scenarios. The only difference is to introduce an additional [DOM]. Note, that DAPL has not been peer-reviewed.
    - The motivation for domain-aware mixup is confusing. I cannot be convinced and do not understand in the current writing, how it can enforce to learn domain-specific knowledge. The corresponding literature regarding mixup in the feature space is also not referenced and discussed (e.g. [1]).  
    - The description for deriving the domain-aware mixup is confusing. I assume the authors are trying to develop a method so that the learned prompt shares the knowledge between source and target domains (depending on Eq. 9)?

* Writing:
    - In the first sentence of Abstract: “large vision-language models … strong performance in MFDA”. There is no such reference applying large VL models in MFDA. In fact, MFDA is a rarely studied problem.
    - The description of the problem setting (MFDA) should be clearly explained at the beginning (abstract or introduction) so that the reader can refer better to the limitations of prior works.
    - Paragraphs 1 & 2 in the introduction: the connection is missing, and ‘prompt learning’ suddenly jumps in, making the concept broken.
    - Fig. 1 is not referred to in the paper.
    - Related work: after describing the related prior works of each field, it's suggested to write a couple of sentences to distinguish between them to show the novelty of the proposed method.
    - The description of the MFDA setting is very confusing in the first paragraph of the Method Section: “single target domain with \textbf{sparse} labels”, “…target distribution p_T(x, y) with label observation…” is mentioned, but the notation for target domain \tau is unlabeled. In the original MFDA paper (Yue et al., 2021a), the target data is unlabeled. What about the unlabeled data in source domains? Are they used during training (as in (Yue et al., 2021a))? It is very confusing that the problem setting description defers significantly as in (Yue et al., 2021a).
    - There is significant text overlapping with DAPL in the preliminary sections of both papers (only with some rewording..). It should be strictly prohibited.
    - What is [DOM] in Eq. 4? I assume it is a domain ID? And I assume [DOM] is the non-learnable component near the description of Eq. 4?
    - Notation: what is subscript d in Eq. 4 and superscript d in Eq. 5? They are not explained in the text. I assume they are the domain IDs?
    - What does it mean by ‘d*k categories’ as in the sentence after Eq. 5?
    - Eq. 6 is very confusing. For the outer summation on d \in {s, u}, what is the purpose of computing the similarity between the target domain prompt and source image features? How does the learning on unlabeled target data is realized?
    - What is inter-source domain mixup? In the current format of writing, I don’t understand why maintaining it will harm the representation learning on the target domain. The motivation is weak.
    - In the second paragraph on page 6, the notation of target domain data y_t is different from Section 3.
    - In Fig. 3, letters v and f are used to represent the features of “painting” and “real”. But v is used to represent text prompts as in Eq. 3
    - The feature mix-up formulation in Fig. 3 is different than Eq. 8. One uses \gamma and another one uses \lambda? and the weighting is different?
    - It is really confusing that the letter “t” is used to refer to text and target domain.
    - What are D^s and D^u in Eq. 10? They are never defined. I assume they are source and target domains, which is inconsistent with what is described in the problem setting. The problem setting is borrowed from (Yue et al., 2021a). But Eq. 10 is copied from DAPL paper. Please keep everything consistent throughout the paper. Also, Eq. 9 requires source data as well, why only D^u is passed to L_u as in Eq. 10?
    - The notations for loss functions in Eq. 7, 9, and 10 should be consistent.
    - Table 5 in the last sentence of Page 8 should be Figure 5.
    - The experimental setting/comparison is very confusing. What is “single best”, which can be both setting and method as in Table 1&2? What is source combined? Which rows in Tables 1&2 refer to the MFDA? How come the “Large model” in Table 1&2 can be the setting, it should be the model architecture.
    - For Figure 6&7, they are hard to see the differences. It is suggested to use a table to report the numbers.

### Questions
- In Eq. 1, what do g() and f() represent? I assume they are text and image encoders as described in DAPL.
- Missing information: “Diverse prompts are achieved by constructing a prompt bank that contains various configurations specific to each domain.” How does the prompt bank is constructed and what are the specific config for each domain?
- What is the relation between f^i_{mixup} and f_{u}? It seems they are the same. But neither f^i_{mixup} or f_{u} is used in the subsequent text?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
