# KEEP: Towards a Knowledge-Enhanced Explainable Prompting Framework for Vision-Language Models

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Large-scale vision-language models (VLMs) embedded with expansive representations and visual concepts have showcased significant potential in the computer vision community. Efficiently adapting VLMs such as CLIP, to downstream tasks has garnered growing attention, with prompt learning emerging as a representative approach. However, most existing prompt-based adaptation methods, which rely solely on coarse-grained textual prompts, suffer from limited performance and interpretability when handling tasks that require domain-specific knowledge. This results in a failure to satisfy the stringent trustworthiness requirements of Explainable Artificial Intelligence (XAI) in high-risk scenarios like healthcare. To address this issue, we propose a Knowledge-Enhanced Explainable Prompting (KEEP) framework that leverages fine-grained domain-specific knowledge to enhance the adaptation process across various domains, facilitating bridging the gap between the general domain and other specific domains. We present to our best knowledge the first work to incorporate retrieval augmented generation and domain-specific foundation models to provide more reliable image-wise knowledge for prompt learning in various domains, alleviating the lack of fine-grained annotations, while offering both visual and textual explanations. Extensive experiments and explainability analyses conducted on eight datasets of different domains, demonstrate that our method simultaneously achieves superior performance and interpretability, shedding light on the effectiveness of the collaboration between foundation models and XAI. The code will be made publically available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the Knowledge-Enhanced Explainable Prompting (KEEP) framework, designed to improve the adaptability and interpretability of vision-language models (VLMs) like CLIP for domain-specific tasks. Traditional prompt-based methods often rely on general, coarse-grained textual prompts, limiting their performance and interpretability, especially in critical fields like healthcare that require high levels of trustworthiness in Explainable AI (XAI). KEEP addresses this limitation by integrating fine-grained, domain-specific knowledge through retrieval-augmented generation and specialized foundation models, enhancing the relevance of prompts for specific domains. This approach enables more reliable and informative image-wise explanations and outperforms existing methods in both accuracy and interpretability. Experiments across eight diverse datasets validate the effectiveness of this framework, highlighting the beneficial synergy between foundation models and XAI.

### Strengths
1、	This paper proposes a knowledge-enhanced explainable prompting framework that leverages fine-grained domain-specific knowledge to enhance the VLM adaption, improving the performance of VLMs on various domains.
2、	The paper shows that the proposed method can be effectively and flexibly applied across various specialized domains, including both medical and natural modalities, achieving promising results on multiple datasets.

### Weaknesses
1、	The approach requires additional vision-language models and a retrieval-augmented generation (RAG) system to provide domain knowledge, which are complex and heavy.
2、	Since a domain-specific model is needed, why not directly use a domain-specific model for classification instead of investing so much effort into training CLIP for a relatively simple classification task?
3、	Overall, the method introduces too many powerful systems and models and adds a substantial amount of extra information, yet it only addresses a basic classification task. This seems somewhat unworthy, and it may be unfair to compare it with other methods that do not utilize additional models.
4、	The structural innovation of the method is limited, which only uses a simple cross-attention mechanism.

### Questions
The authors have constructed a complex and extensive pipeline, incorporating a substantial amount of additional information, yet it ultimately only accomplishes a simple, basic classification task. This approach does not seem worth the effort. Typically, such complex and extensive pipelines are built to tackle more advanced and challenging tasks.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper simultaneously improves the model performance and interpretability by integrating domain-specific knowledge with prompt engineering. In particular, it takes advantage of pretrained Large Language Models (LLMs) to query knowledge from external datasets, and generate the image-wise prompt by comparing the knowledge and image embeddings. The prompts and images are then jointly utilized in a model trained with contrastive and standard classification objectives. Experimental results demonstrate the advantage of the proposed method among multiple datasets, and validate the usefulness of domain knowledge.

### Strengths
(1) Combining general LLMs with domain-specific knowledge is an important problem, and the paper proposes a framework that generalizes to different datasets.

(2) The paper shows that, with more fine-grained prompts, the model can achieve higher accuracy with more efficient data usage.

(3) It offers extensive ablation studies, which facilitates understanding the contributions of individual components.

### Weaknesses
(1) Despite the emphasis on integrating domain knowledge specific to each sample, there is no quantitative evaluation of the relevance of extracted knowledge. This is particularly important considering that many of the applications in the paper involve high-stakes decisions (e.g., clinical diagnosis) and LLMs can potentially suffer from hallucination. It is necessary to perform a user study with domain experts or evaluate with ground truth annotations (e.g., comparing the similarity between generated prompts with clinical reports [ref1]). 

(2) Related to the previous comments. Looking at the results in Figure 4, it appears that the proposed knowledge is only marginally better than random knowledge in terms of faithfulness, and altering the knowledge prompts leads to negligible changes to the model performance. This is relatively worrisome, as it indicates that the validity of knowledge has limited effects on the model behaviors. 

(3) The paper only compares with general prompting methods that do not have access to domain knowledge, and it is unclear how advantageous is the proposed method in specific domains. It is reasonable to include state-of-the-art methods of the corresponding datasets in Table 1 (e.g., Derm7pt, Pneumonia, etc.)

(4) The authors claim that cross-attention is used to provide sub-region explanations. However, the method utilizes a standard instance-wise contrastive objective without explicitly considering the spatial dimension. No evidence is provided to validate how such a paradigm helps address the issue. 

(5)  Figure 5 visualizes the gradient-based saliency maps of several examples. Nevertheless, since gradient-based approaches can have mixed explainability [ref2], it would be helpful to further consider other explainable AI methods, e.g., [ref3, ref4].

(6) The authors argue that the proposed method is the first framework for generating instance-wise prompts with domain knowledge. Nevertheless, similar problems have been explored before (e.g., [ref5, ref6]), which also leverages LLMs and contrastive learning.

References

[ref1] Exploring the Boundaries of GPT-4 in Radiology. EMNLP, 2023.

[ref2] Evaluating saliency map explanations for convolutional neural networks: a user study. IUI, 2020.

[ref3] A Unified Approach to Interpreting Model Predictions. NeurIPS, 2017.

[ref4] RISE: Randomized Input Sampling for Explanation of Black-box Models. BMVC, 2018.

[ref5] Improving Radiology Report Generation Systems by Removing Hallucinated References to Non-existent Priors

[ref6] Retrieval Augmented Chest X-Ray Report Generation using OpenAI GPT models. PMLR, 2023.

### Questions
(1) Please consider additional quantitative evaluation on the quality of generated knowledge prompts.

(2) Why does permuting the knowledge prompts only have minor effects on the model behaviors? Does it imply that the model still mostly relies on abstract descriptions of the class label instead of specific concepts?

(3) Why does the cross-attention enable sub-region explanations? Do the authors mean that it leads to better gradient-based explanations?

(4) More comprehensive comparisons with domain models and exploration of additional explanation methods would be useful.

(5) Please justify the distinctions with prior studies (see weaknesses).

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors leveraged the fine-grained domain-specific knowledge from existing domain-specific models to enhance the VLM
adaption in a knowledge-enhanced explainable prompting framework.  Overall, this paper achieves good performance, and the experimental results demonstrate the effectiveness of introducing domain knowledge. However, there are some critical issues that need to be overcome.

### Strengths
1. The idea of introducing domain-specific knowledge is intriguing and makes sense.

2. The writing of the paper is easy to follow and understand.

3. The performance of the proposed method is good.

### Weaknesses
1.  Though the authors claim that the methods are leveraged in various domains, the paper only implements their methods in natural and medical imagery, where natural images are the main focus domain of existing VLMs. Thus, the only experimental domain to support the VLM adaption in this paper is the medical domain, which might not be enough to support the validation of the proposed method.

2. As the authors provide better text prompts as domain-specific knowledge, the solo better text prompt should be ablatively studied.

3. Since you already leverage the BiomedCLIP to provide domain-specific knowledge, why you do not directly prompt the BiomedCLIP yet still prompt the natural vision-based CLIP? 

4. Existing methods are still cornered in the natural vision, which is not really changing the domain gap of CLIP.

5. Actually, this method is not the first attempt to achieve the domain adaption of CLIP, yet the compared methods are only the traditional natural-vision based prompt learning method. More recent methods with regard to domain prompt learning like [1,2] should be added to make a fair comparison. 

[1] Domain-controlled prompt learning

[2] Domain prompt learning with quaternion networks

### Questions
1. Could you provide more experimental results with regard to other domains to provide better support?

2. The solo better domain-specific text prompt could be better ablatively studied.

3. Why not directly leverage the domain-specific VLMs like BiomedCLIP?

4. Could you give more comparisons with regard to other domain adaptation/ prompt learning methods?

If these issues are well addressed, I would certainly raise my scores.

### Soundness
3

### Presentation
3

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
This paper proposes to improve the generalization of VLMs to various domains by using additional knowledge. Specifically, it introduces two relevant components: 1. Knowledge-enhanced prompt creation is utilized to enrich the specific-domain contexts via RAG; 2. Knowledge-enhanced prompt learning is utilized to further align the semantic correspondences between images and knowledge-enhanced prompts. Experiments are conducted on various datasets.

### Strengths
1. The motivation of this paper is good.
2. This paper is easy to follow.
3. Experiments seem valid.

### Weaknesses
1. Overclaim about the motivation. This paper claims that it is the first work (in the abstract) to use knowledge-based contexts. However, I found a very similar work [a] published in the year 2023, which does the same thing as this paper. However, the authors do not cite and discuss with [a], or even not provide any experimental comparison.

2. Novelty is limited. First, utilizing RAG to enrich the prompt is not new, it is a widely used strategy in LLM processing. Second, prompt learning is just simply based on the attention mechanism. Moreover, the two proposed components have already been investigated in paper [a].

3. Experiments are insufficient. First, the authors should provide statistical results to show the performance gap due to the domain gap. Second,  many ablations like cross-dataset transfer, domain generalization, and types of prompts should be provided. These are the basic experimental implementations to validate the effectiveness of the proposed method.

[a] Knowledge-Aware Prompt Tuning for Generalizable Vision-Language Models. ICCV2023

### Questions
1. Overclaim about the motivation. This paper claims that it is the first work (in the abstract) to use knowledge-based contexts. However, I found a very similar work [a] published in the year 2023, which does the same thing as this paper. However, the authors do not cite and discuss with [a], or even not provide any experimental comparison.

2. Novelty is limited. First, utilizing RAG to enrich the prompt is not new, it is a widely used strategy in LLM processing. Second, prompt learning is just simply based on the attention mechanism. Moreover, the two proposed components have already been investigated in paper [a].

3. Experiments are insufficient. First, the authors should provide statistical results to show the performance gap due to the domain gap. Second,  many ablations like cross-dataset transfer, domain generalization, and types of prompts should be provided. These are the basic experimental implementations to validate the effectiveness of the proposed method.

[a] Knowledge-Aware Prompt Tuning for Generalizable Vision-Language Models. ICCV2023

### Soundness
2

### Presentation
3

### Contribution
2
