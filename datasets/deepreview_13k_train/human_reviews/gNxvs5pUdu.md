# DocMIA: Document-Level Membership Inference Attacks against DocVQA Models

- Decision: Accept
- Scores: 6, 6, 6, 6, 6, 6

## Abstract
Document Visual Question Answering (DocVQA) has introduced a new paradigm for end-to-end document understanding, and quickly became one of the standard benchmarks for multimodal LLMs. Automating document processing workflows, driven by DocVQA models, presents significant potential for many business sectors. However, documents tend to contain highly sensitive information, raising concerns about privacy risks associated with training such DocVQA models. One significant privacy vulnerability, exploited by the membership inference attack, is the possibility for an adversary to determine if a particular record was part of the model's training data. In this paper, we introduce two novel membership inference attacks tailored specifically to DocVQA models. These attacks are designed for two different adversarial scenarios: a white-box setting, where the attacker has full access to the model architecture and parameters, and a black-box setting, where only the model's outputs are available. Notably, our attacks assume the adversary lacks access to auxiliary datasets, which is more realistic in practice but also more challenging. Our unsupervised methods outperform existing state-of-the-art membership inference attacks across a variety of DocVQA models and datasets, demonstrating their effectiveness and highlighting the privacy risks in this domain.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents membership inference attacks tailored to Document Visual Question Answering (DocVQA) models, highlighting potential privacy vulnerabilities in handling sensitive document data. It introduces white-box and black-box attack methods that work without relying on auxiliary datasets, offering practical insights into real-world privacy risks. The attacks utilize features that typically arise from training data exposure. By addressing the unique complexities of multimodal data, these attacks outperform current baselines, underscoring the need for improved privacy safeguards in DocVQA systems.

### Strengths
- Fills a critical gap in privacy research for multimodal AI applications by designing MIA for DocVQA
- By designing attacks that operate without auxiliary datasets, the paper presents a more realistic and practical approach for assessing privacy risks in scenarios with limited data access
- The attacks can be employed in both whitebox and blackbox attacks settings
- The attacks use intuitive optimization-based discriminative features

### Weaknesses
 - The attacks rely on repeated instances of documents in the training data, which may not always be present in real-world DocVQA applications, potentially limiting the generalizability of the approach
- While the paper identifies privacy risks, it lacks a discussion or evaluation of potential defenses that could mitigate these vulnerabilities

### Questions
- Given the assumption of repeated document exposure, how would the attacks perform in settings where training data consists of unique or one-time documents, with minimal repetition?
- What are some potential countermeasures or defense strategies to mitigate the privacy risks highlighted by these membership inference attacks?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the document-level membership inference attacks targeting multi-modal models for document visual question answering. The main idea is to extract discriminate features between member and non-member documents based on their optimization trajectory. For black-box settings, a proxy model is utilized to extract discriminate features that are relevant for the black-box target model. Empirical results show that the proposed approach consistently performs well in various settings.

### Strengths
1. The idea of leveraging optimization trajectory for membership inference is novel. 
2. The empirical performance of the proposed method is stable, indicating a good generalization over different attack settings.

### Weaknesses
1. There is a lack of ablation study on the choice of the features. In particular, giving some insights about what features are most useful for learning discriminative features between member and non-member documents. Of course, a conclusion of all obtained features being equally important or specific features being more relevant for certain applications are also good observations. 
2. There is no clear explanation on the asymmetric transferability between different proxy and target model pairs Table 2. I think these are all key observations that demystify the success of membership inference attacks.

### Questions
Having additional ablation studies as well as providing more insights on the asymmetric transferability between different proxy and target models will improve the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Document-level Membership Inference Attacks (DocMIA), focusing on Document Visual Question Answering (DocVQA) models. The paper presents two novel membership inference attacks tailored for DocVQA, targeting both white-box and black-box attack scenarios. These attacks enable adversaries to determine whether a particular document was part of the training set, even in the absence of auxiliary datasets. The proposed attacks leverage unsupervised optimization-based methods that outperform existing state-of-the-art membership inference attacks, underscoring the privacy vulnerabilities present in DocVQA models.

### Strengths
- The focus on DocVQA models for membership inference is unique. Previous research has mainly centered on generic models or other multimodal domains, while this paper contributes significantly to understanding privacy risks specific to document processing and VQA models.
- The paper employs solid, theoretically grounded approaches to devise the DocMIA attacks. The white-box attack uses optimization-based discriminative features, allowing more robust membership inference without requiring shadow models. The experimental setup includes multiple DocVQA models (VT5, Donut, Pix2Struct), ensuring that results are thorough and comparable.
- Given the sensitive nature of document data, this paper’s contributions are valuable for highlighting vulnerabilities in DocVQA models. The presented attacks have significant implications for the adoption of such models in privacy-sensitive applications, urging the development of more robust defenses.

### Weaknesses
 -  While the paper references relevant literature, it does not include direct empirical comparisons with existing black-box defenses. Including black-box defenses as baselines would allow a more comprehensive assessment of DocMIA’s performance, helping to contextualize its strengths better.
- The experimental setup lacks some critical details, such as the specific training dataset used for GAN priors in particular baselines. Information on hyperparameters for certain attack baselines (e.g., gradient-based attacks) would improve reproducibility.
- The paper does not address the performance of DocMIA under dataset distribution shifts. This gap is significant as DocVQA models may be deployed across varied domains, potentially affecting the reliability of the proposed attacks. Testing DocMIA under different dataset shifts would provide insights into its robustness.

### Questions
How does DocMIA perform when there is a significant distribution shift between the public and private datasets? For instance, if the private dataset is derived from a financial dataset, but the public dataset stems from a different domain (e.g., legal documents), how would that affect the attack’s efficacy?

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
3

### Summary
The paper aims to make a fine-grained membership inference attach, which can determine whether a sensitive document is included in the training dataset. For the white box and black box, the authors have developed different MIA approaches according to their characteristics. Experimental results confirm that their methods outperform baselines.

### Strengths
1. This paper is the first attempt to target document-level membership inference attacks.
2. This paper designs attack modes for white box and black box respectively.

### Weaknesses
1. The challenges of the work are underdescribed by the authors, and it is difficult for the reviewer to understand the technical challenges between fine-grained inference attacks and coarse-grained attacks, proposed by Tito et al.. The authors express it more as if they were writing an experimental report.
2. "shadow training of proxy models becomes infeasible.", the reviewer suggests the authors describe in words how to solve this problem and highlight it.
3. While the paper introduces methods to adapt the attack to black-box models through knowledge transfer, this approach may not be as effective as direct white-box attacks due to the inherent limitations in approximating the behavior of complex models.

### Questions
1. Briefly describe how to solve “shadow training of proxy models becomes infeasible".
2. While the paper introduces methods to adapt the attack to black-box models through knowledge transfer, this approach may not be as effective as direct white-box attacks due to the inherent limitations in approximating the behavior of complex models.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduce the first document-level membership inference attacks Document-Level Membership Inference Attacks (DocMIA) for Document Visual Question Answering (DocVQA) models, addressing privacy risks in multimodel contexts. Through extensive experiments across multiple datasets and models, significantly outperform existing membership inference baseline.

### Strengths
1、This paper proposes Document-Level Membership Inference Attacks (DocMIA), which deal with the multiple appearances of the same document in the training set.

2、DocMIA consistently achieves high performance across all target models, the strong performance of  DocMIA highlights the privacy risks posed by optimization-based features of membership.

### Weaknesses
1、The writing in this paper is clear and accessible, providing a well-structured and understandable presentation of the authors' ideas and methods. However, the text is overly verbose, with an excess of written content and a lack of visual aids. The absence of a diagram illustrating the attack process detracts from an intuitive understanding of the attack methodology. Adding visual elements would enhance the reader's comprehension and provide a more direct insight into the core processes discussed.

2、There are some typographical problems with the manuscript. The position of Figure 1 is not ideal and should be adjusted to be centered side-by-side, similar to Figure 2.

### Questions
1、The paper presents experiments on four target models for the DocVQA dataset but only conducts experiments on two models for the PEL-DocVQA dataset, without providing an explanation for this choice of setup. This lack of clarification on the experimental design for the PEL-DocVQA dataset leaves the rationale for the selection of models unclear. It is recommended to include an explanation for this experimental setting.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work tackles document-level inference for VQA models that have been trained on text as well as visual-documents, where additional processing steps like OCR and repeated instances of documents make the problem significantly different from standard MI under language models. The authors propose attacks that are free of any auxiliary data, for both black-box and white-box access models.  The proposed attacks are evaluated on multiple datasets, outperforming both existing and newly-designed baseline inference methods.

### Strengths
- The work tackles document VQA systems, which post a lot more challenges than simple text-based language models. Understanding leakage in this scenario would be helpful.
- The attack methodology is interesting and straightforward, and the authors experiment with multiple ways of "fine-tuning" the target model to measure scores used for membership inference.
- Results are presented very well, and overall the figures/tables are very neat, with a very detailed Appendix.

### Weaknesses
I think the works make a fair contribution, but I do have some concerns (major and minor listed below and under questions) that the authors could answer to help me better understand some of their design choices.

- The evaluation design is completely disconnected from how MI attacks are usually evaluated. Currently, thresholds are computed based on average values in $D_\text{test}$. In MI (or similar evaluations), the standard protocol is to sweep over the non-member's values and based on the FPR (false positive rate) dictated by a certain threshold, compute the TPR (true positive rate). From there, multiple statistics (such as AUC for the TPR-FPR curve, or TPR at a specific FPR) can be computed. I would request the authors to re-evaluate their methods using this approach. I also do not know why the authors have constructed their own version of baselines- there are existing attacks (as one example, see Min-k%++)

- Appendix E.1: "... have assumed complete knowledge of the original training questions" This is a very strong assumption! This implies that the adversary also knows the exact questions associated with the target document (and by extension the answers). This was not mentioned clearly anywhere in the main paper. The fact that performance drops when this is relaxed is not surprising to me, and demonstrates that the majority of performance reported in the paper is originating from this strong (and obfuscated) assumption. The relaxed setting here (where exact questions are not known) should be the **default** setting in the main paper- after all, true "document" inference would not entail one knowing which *exact* questions and answers were present in the training data


## Minor comments

- L31: "...fuels a significant number of operations daily" - source?
- L49-50: "...utilize a dual representation..." - please cite relevant works
- L102-102: "The literature indicates that...." - this is not the case. While recent work [1] does suggest that parameter access may be necessary for optimal membership inference, the cited papers here (and most empirical results) indeed conclude that additional access to parameters does not help with membership inference.
- L114: "...larger scale models"- please see [2] that indeed tackles inferring the use of certain text documents for LLMs.
- L186: "adversary lacks access to an auxiliary data". Membership-inference evaluation by design needs "non-members" to compute thresholds for membership classification (and as recent work [3] has shown, you cannot just use any non-member data especially when it comes to language). What the authors probably mean here is that there is not *enough* auxiliary data, and should clarify this.
- L191: "...would be prohibitively expensive" - this would be a problem for a resource-constrained adversary, but an adversary that is malicious (in the security sense) will not be limited like this. An adversary can always use public/pretrained models as a starting point.
- L210: "...types of documents" - define knowledge of "type" of documents/questions
- L447: "Table 1 (right)" - there is only one table. Please fix reference (similarly for Table 1 (left), etc.)

### Questions
- L106: why is the adversary query-restricted?

- Section 4.2.1: How is convergence defined here? There is some (unintentional) leakage happening, since you need to know when "convergence" happens for members to stop the optimization at that point. A true test to check for this would be to run it for a pre-defined set of iterations, record the loss at each iteration, and use that as the feature vector.

- L354: How are gradients back-propagated via the OCR generation pipeline?

- Section 5.3: How are the questions constructed? Are they picked based on what was in train/test data?

- L410: What is "predicted labels"? Isn't the task to generate an answer? If so, just say 'generated text'

- L1008: "...paraphrase the original training questions" - do their answers remain the same?

### Soundness
3

### Presentation
3

### Contribution
3
