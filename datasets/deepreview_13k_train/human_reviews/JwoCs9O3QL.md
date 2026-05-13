# VLMGuard: Defending VLMs against Malicious Prompts via Unlabeled Data

- Decision: Reject
- Scores: 6, 3, 5, 6

## Abstract
Vision-language models (VLMs) are essential for contextual understanding of both visual and textual information. However, their vulnerability to adversarially manipulated inputs presents significant risks, leading to compromised outputs and raising concerns about the reliability in VLM-integrated applications.  Detecting these malicious prompts is thus crucial for maintaining trust in VLM generations. A major challenge in developing a safeguarding prompt classifier is the lack of a large amount of labeled benign and malicious data.  To
 address the issue, we introduce \model, a novel learning framework that leverages the unlabeled user prompts in the wild for malicious prompt detection. These unlabeled prompts, which naturally arise when VLMs are deployed in the open world, consist of both benign and malicious information. To harness the unlabeled data, we present an automated maliciousness estimation score for distinguishing between benign and malicious samples within this unlabeled mixture, thereby enabling the training of a binary prompt classifier on top. Notably, our framework does not require extra human annotations, offering strong flexibility and practicality for real-world applications. Extensive experiment shows \model achieves superior detection results, significantly outperforming state-of-the-art methods.  \textit{\color{purpleinplot}Disclaimer: This paper may contain offensive examples; reader discretion is advised.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses a challenge in VLM security in VLM security - detecting malicious prompts without requiring labeled data. The key innovation lies in analyzing unlabeled user data through subspace analysis of VLM representations. While the approach shows promising results, several fundamental questions about its theoretical foundation and practical applicability need to be addressed.

### Strengths
- New Problem Definition:
  - The paper presents a practical solution to reduce dependency on labeled data, which is particularly valuable because manually labeling malicious prompts is time-consuming and expensive.

- Technical Approach:
  - The proposed maliciousness scoring mechanism uses VLM's internal representations, which is computationally efficient as it requires only a single forward pass.
  - The scoring function $\kappa_i = \frac{1}{k} \sum \left( \lambda_j \cdot \langle f_i, v_j \rangle^2 \right)$  combines information from multiple principal directions, making it more robust than single-direction approaches.
  - The framework can be easily integrated into existing VLM systems since it doesn't require architectural modifications.

### Weaknesses
 - The authors offer some geometric intuition and empirical validation, but the theoretical foundation could be clearer in a few areas:
  - The choice of SVD subspace analysis, while effective empirically, lacks a solid theoretical basis to confirm its effectiveness in detecting malicious patterns. Specifically, it's unclear why the principal components derived from a mixed dataset of benign and malicious prompts would reliably isolate malicious patterns. The method assumes that malicious prompts form a distinct, low-dimensional subspace, but this assumption needs more rigorous justification. For instance, what if malicious prompts are not clustered but rather distributed across the representation space, or if they overlap significantly with benign representations in certain dimensions?
  - The current geometric explanation would be stronger with a formal analysis showing why this property holds across different types of attacks. The analysis should consider how different attack strategies (e.g., adversarial perturbations, semantic manipulation, or injection of specific keywords) might manifest in the VLM's representation space and whether SVD is guaranteed to capture these variations effectively.


- The authors use the common approach of last-token embeddings, but there are still a few questions:
  - How does information from earlier tokens affect detection? It's possible that crucial signals for detecting maliciousness are present in earlier parts of the prompt, and discarding these could limit the method's sensitivity. A more detailed analysis of the contribution of each token to the final representation is needed.
  - What properties of the last token make it particularly suitable? While the last token might aggregate contextual information, it is not clear why it is the optimal choice for detecting malicious content, especially since malicious intent might be embedded across the entire prompt. The method should justify why the last token's representation is more indicative of maliciousness than other tokens.
  - How robust is this choice across different prompt structures? Different prompt structures might lead to variations in how information is encoded in the last token's embedding. The method should demonstrate its robustness to these variations and discuss potential limitations when applied to diverse prompt formats.

### Questions
- Given your geometric intuition about malicious samples "malicious samples may occupy a small subspace within the activation space":
  - Could you provide formal conditions under which this property is guaranteed?
  - How does this property relate to the VLM's training objectives?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a defensive framework called VLMGuard, designed to safeguard Vision-Language Models (VLMs) from malicious user inputs. VLMGuard approaches malicious prompt detection as a binary classification task, operating within the VLM's latent space. It identifies prompts that fall into a subspace defined by the latent vectors of known malicious prompts, effectively flagging them as toxic or jailbreaking attempts.

### Strengths
- This paper focuses on a critical safety issue: the misuse of VLMs through malicious or adversarial user inputs. This topic is increasingly important due to the growing popularity and widespread deployment of VLMs.

- VLMGuard introduces an interesting approach by utilizing unlabeled user inputs to enhance the detection of malicious content. This method presents a promising and effective solution to the problem.

### Weaknesses
1. **The motivation behind VLMGuard is unclear.** While it is purportedly designed for VLMs, the integration of VLM concepts into the method is not evident. VLMGuard appears to function as a general binary classifier using extracted latent features applicable to any deep neural network. The lack of a clear rationale and organized presentation diminishes the method's potential significance.

2. **The presentation is wordy and lacks informativeness.** The introduction fails to provide an overarching view of the method. Additionally, Figure 1 lacks annotations necessary for reader comprehension.

3. **There is insufficient discussion of novelty and technical contributions.** Although the authors highlight that VLMGuard requires no labeled data, it seems to rely on latent vectors of known malicious prompts. Furthermore, as indicated by Eqs 5, 6, and Figure 2, the solution resembles an SVM approach [a1]. The authors should clarify the novelty and contributions compared to existing methods.

[a1] M. A. Hearst, S. T. Dumais, E. Osuna, J. Platt, and B. Scholkopf, "Support vector machines," IEEE Intelligent Systems, vol. 13, no. 4, pp. 18-28, July-Aug. 1998, doi: 10.1109/5254.708428.

4. **There is a lack of comparison with closely related baselines.** The authors should compare their method with state-of-the-art content moderation solutions, such as Aegis [a2], LlamaGuard [a3], LlamaGuard2 [a3], LlamaGuard3 [a4], and OpenAI-Moderation [a5].


[a2] https://arxiv.org/abs/2404.05993
[a3] https://arxiv.org/abs/2312.06674 
[a4] https://arxiv.org/abs/2407.21783  
[a5] https://arxiv.org/pdf/2208.03274

5. **(minor) Figure 1 is misleading.** While the paper does not evaluate any of OpenAI's VLMs, it uses the OpenAI logo, potentially confusing readers. This should be corrected to accurately reflect the VLMs used in the evaluation.

### Questions
Please refer to the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Vision-language models (VLMs) are crucial for understanding visual and textual information but are vulnerable to adversarial inputs, which can compromise their reliability in applications. Detecting these malicious prompts is essential to maintain trust in VLM outputs. A significant challenge is the limited availability of labeled benign and malicious data for developing effective classifiers.

To tackle this, the paper introduces VLMGUARD, a novel framework that utilizes unlabeled user prompts from real-world deployments for malicious prompt detection. These prompts contain both benign and malicious information. The approach includes an automated maliciousness estimation score to differentiate between benign and malicious samples within this unlabeled dataset, allowing for the training of a binary prompt classifier without requiring additional human annotations.

Extensive experiments demonstrate that VLMGUARD achieves superior detection performance, significantly surpassing existing state-of-the-art methods, thus offering a flexible and practical solution for real-world applications.

### Strengths
- This paper explores the defense in VLM malicious generations, giving a good reference to the research on this aspect.

- The proposed method VLMGUARD is simple but effective to achieve the defense, and the good performance obtained by the experiments strongly supports this point.

- The ablation study is organized well to clearly demonstrate the whole proposed method. And it makes the paper easy to follow.

### Weaknesses
 - I am curious about why the binary classifier outperforms the direct use of the maliciousness score for detection, as illustrated in Fig. 4. The training dataset is based on an unlabeled dataset that has been annotated with maliciousness scores. Consequently, the accuracy of the binary classifier relies on the quality of these annotations, which in turn depends on the effectiveness of the maliciousness score detection. This raises the question: **is the upper bound of the binary classifier's performance essentially limited by the accuracy of the maliciousness score detection?** However, the results in Fig. 4 contrasts this view.

- I noticed that the values for $\pi$ are chosen from the set {0.001, 0.005, 0.01, 0.05, 0.1} as stated in Section 4.1. Is it possible for the proportion of malicious prompts to be higher, perhaps 0.5 or more? I am interested in understanding whether the proposed defense mechanism remains effective when faced with such a higher rate of malicious prompts.

### Questions
Listed in the weakness of the paper. 

Score can be improved if concerns listed above are resolved.

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
This paper presents a novel approach to defending Vision-Language Models (VLMs) against malicious prompts. The proposed method leverages the intrinsic capabilities of VLMs to assign pseudo-labels to unlabeled data, and subsequently trains a binary classifier to detect malicious prompts using this pseudo-labeled dataset. By doing so, the method significantly enhances the robustness of VLMs in detecting and mitigating malicious prompts.

### Strengths
Clarity and Simplicity of the Approach:
The overall idea and methodology presented in this paper are highly intuitive and easy to follow. The process of feeding inputs into the model to obtain embeddings, followed by performing SVD, and finally identifying outliers, is clear and logically structured. This clarity allows for smooth comprehension of the workflow, making the contributions more accessible to both researchers and practitioners.

Significance in Addressing a Critical Problem:
The paper addresses a critical issue in trustworthy AI: the detection and defense against malicious prompts in VLMs. The significance of this contribution cannot be overstated, as enhancing VLMs' robustness to malicious inputs is a crucial step toward ensuring reliable deployment of AI systems in real-world applications. The focus on using pseudo-labeled, unlabeled data is particularly valuable in reducing the dependency on manually labeled datasets, which is often a bottleneck in scaling robust AI solutions.

Substantial Performance Improvement:
The experimental results demonstrate considerable improvements over existing baselines, showcasing the practical impact of the proposed method. The enhancements in robustness against malicious prompts, as reflected by the increased AUROC scores in the experiments, highlight the effectiveness of the approach. This strong empirical performance further strengthens the paper's contribution.

### Weaknesses
Limited Novelty in Core Contribution:
The core contribution of this work—applying SVD to detect malicious prompts—while effective, does not appear to be particularly novel. SVD has been extensively used in anomaly detection tasks across various domains, and its direct application here may lack the originality expected in top-tier conference submissions. The paper could benefit from further emphasizing any unique insights or enhancements introduced in the specific context of VLMs and malicious prompt detection, beyond the straightforward use of SVD.

Unclear Necessity of Training the Protective Prompt Classifier:
A significant question arises regarding the necessity of the protective prompt classifier. Given that the proposed “maliciousness estimation in the latent subspace” seems capable of distinguishing malicious samples effectively, the added step of pseudo-labeling and training a binary classifier may seem redundant. The paper could have provided stronger justification for why the classifier is needed, beyond simply determining the decision threshold \tau. It would strengthen the contribution if the authors could clarify whether the classifier introduces additional benefits in terms of generalization or robustness that are not achieved by the latent subspace estimation alone. Without this clarification, the added complexity might appear unnecessary.


**Post-Rebuttal**:

The authors have not addressed my concerns regarding the necessity of training a classifier. Overall, the paper attempts to implement some simple functions using complex modules, lacking true innovation. I am inclined to rate it between 5 and 6.

### Questions
The biggest issue I see is related to Weakness 2.

Relation to Adversarial Images:The relationship between this work and adversarial images needs further clarification. While malicious prompts are discussed, there seems to be some overlap with the concept of adversarial examples, especially when dealing with adversarial attacks on the visual input. Could the authors elaborate on how their approach relates to or differs from traditional adversarial attack detection.

Applicability Beyond Multimodal Models:The method proposed in this paper does not seem inherently restricted to multimodal models. Would the authors agree that this approach could also be applied to unimodal models, such as those in CV or NLP? For instance, could this method be adapted for adversarial attack detection in CV models, where the "jailbreak" prompts are replaced by adversarial attacks?

### Soundness
3

### Presentation
3

### Contribution
3
