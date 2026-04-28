# Auto-GDA: Automatic Domain Adaptation for Efficient Grounding Verification in Retrieval Augmented Generation

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
While retrieval augmented generation (RAG) has been shown to enhance factuality of large language model (LLM) outputs, LLMs still suffer from hallucination, generating incorrect or irrelevant information. One common detection strategy involves prompting the LLM again to assess whether its response is grounded in the retrieved evidence, but this approach is costly. Alternatively, lightweight natural language inference (NLI) models for efficient grounding verification can be used at inference time. While existing pre-trained NLI models offer potential solutions, their performance remains subpar compared to larger models on realistic RAG inputs.  
RAG inputs are more complex than most datasets used for training NLI models and have characteristics specific to the underlying knowledge base, requiring adaptation of the NLI models to a specific target domain. 
Additionally, the lack of labeled instances in the target domain makes supervised domain adaptation, e.g., through fine-tuning, infeasible.
To address these challenges, we introduce Automatic Generative Domain Adaptation (\framework). Our framework enables unsupervised domain adaptation through synthetic data generation.
Unlike previous methods that rely on handcrafted filtering and augmentation strategies, \framework employs an iterative process to continuously improve the quality of generated samples using weak labels from less efficient teacher models and discrete optimization to select the most promising augmented samples.
Experimental results demonstrate the effectiveness of our approach, with models fine-tuned on synthetic data using \framework often surpassing the performance of the teacher model and reaching the performance level of LLMs at 10\,\% of their computational cost.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces a novel framework to enhance the performance of NLI models in verifying retrieved evidence within retrieval-augmented generation settings. The paper addresses the issue of performance drop in out-of-domain inputs. To alleviate this problem, the authors propose an automatic generative domain adaptation method to fine-tune NLI models in an unsupervised manner. In the proposed method, this framework considers both diversity and quality by using a sequential augmentation technique and optimizing a distribution-matching objective in the data generation process. Experimental results demonstrate that the NLI model fine-tuned with the proposed method achieves performance closer to that of LLM models without sacrificing efficiency.

### Strengths
- The proposed method is novel and practical in RAG scenarios.
- This manuscript is clearly written and easy to follow.
- The experimental results are well conducted, showing advantages in terms of accuracy and efficiency.

### Weaknesses
 - The paper would benefit from a more detailed analysis to clearly demonstrate the robustness of the proposed method across various domains. In real-world scenarios, domain boundaries are often ambiguous, and it’s common to encounter mixed or overlapping domain data. By evaluating the model in a multi-domain or domain-mixing setting, the authors could provide stronger evidence of its robustness and practical applicability in complex, realistic cases.

- It would be valuable to include an analysis of how the model performance depends on the quality of the initial synthetic data generation. If initial data is inaccurately generated, it might negatively influence the model’s performance. An examination of whether the model can correct or adapt to potential errors in this initial phase would clarify the method’s resilience to suboptimal synthetic data.

- The paper’s selective objective function appears complex, suggesting that the model could be highly sensitive to hyperparameter choices. Observing large variations in hyperparameter values for each dataset implies that tuning these parameters may be challenging. Providing further insights into the model’s hyperparameter sensitivity and offering guidelines for tuning could improve the approach's usability and reliability in diverse settings.

### Questions
See the weaknesses

### Soundness
3

### Presentation
3

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
This paper tackles the issue of hallucinations in Large Language Models (LLMs) used in retrieval augmented generation (RAG) applications, where verification of generated outputs through natural language inference (NLI) models is essential. The authors propose Automatic Generative Domain Adaptation (Auto-GDA), an unsupervised framework that generates high-quality synthetic data to fine-tune lightweight NLI models for specific RAG domains. Key contributions include formalizing the unsupervised domain adaptation problem, developing the Auto-GDA framework for efficient sample selection, and demonstrating that models fine-tuned with Auto-GDA outperform weak teacher models and approach the performance of human-labeled references, all while achieving significantly lower latency than LLMs. This work presents a promising solution to enhance NLI model performance in real-time RAG applications.

### Strengths
- The proposed Automatic Generative Domain Adaptation (Auto-GDA) offers a novel approach to unsupervised domain adaptation, effectively generating high-quality synthetic data to fine-tune NLI models tailored for specific RAG contexts.
- Empirical results demonstrate that models fine-tuned with Auto-GDA significantly outperform weak teacher models and achieve performance levels comparable to those using human-labeled data, indicating its effectiveness in improving NLI model accuracy.
- The paper is well written and easy to understand.

### Weaknesses
 - The effectiveness of the Auto-GDA framework relies heavily on the quality of the synthetic data generated. Poorly generated data, particularly those with incorrect labels or unrealistic content, could lead to suboptimal fine-tuning and negatively impact NLI model performance. The selection process, while intended to filter out low-quality samples, might not be perfect, and the impact of remaining noisy data on the fine-tuned model's performance needs further investigation.
- Although the framework aims to address domain mismatches, (in my own opinion) there may still be challenges in generalizing to highly diverse or previously unseen domains, potentially reducing the model's effectiveness in broader applications. The evaluation, while including datasets with open-ended and diverse domains, might not fully capture the complexities of real-world scenarios where the target domain is significantly different from the training data. I'm curious how well the proposed method performs under such extreme conditions?

### Questions
Refer to weaknesses.

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
4

### Summary
The paper considers the problem of domain adaptation of the natural language inference models (NLI) which are often used in retrieval-augmented generation (RAG) to judge the entailment of the generated response from the retrieved context. The paper proposes Auto-GDA, a method for generating synthetic data for a given domain, that can be used for finetuning an NLI model to improve its performance in this domain. The proposed method is iterative and consists of three steps: (1) seed data generation using an LLM; (2) data augmentation e.g. using paraphrasing or sentence deletion; and (3) data filtering, to minimize their proposed enhanced distribution matching objective; steps 2 and 3 can be repeated iteratively. The method is tested on several datasets that provide human labels for NLI, and compared versus existing off-the-shelf systems and several ablations.

### Strengths
* A relevant research direction of adapting RAG components to user domains
* Comprehensive related work section
* Detailed description of the proposed approach, used datasets, baselines, and experimental details
* The proposed method is compared to a series of existing NLI solutions on several datasets, and inference time is also compared for various methods

### Weaknesses
1. The presented Auto-GDA method is rather complex (involving multiple steps and components, including heuristic augmentation techniques) and has several important hyperparameters, such as $\lambda_d$ and $\lambda_u$ in eq. (2), population sizes M and K, or the number of iterations. Hyperparameter tuning requires running the proposed approach 50 times (line 446), including training of the NLI model on the generated data (from my understanding). At the same time, improvements over simply using LLM-generated data are quite modest (row 4 vs 2 in Table 2).
    - Furthermore, the high cost of running hyperparameter optimization, augmentation, and data selection in the proposed approach, motivates the substantial increase of data points in the simple baseline of using LLM-generated data, to make their computational costs similar. This would make the baseline stronger and reduce its difference versus the proposed approach even further.
    - Performance gains versus out-of-the-box NLI models are also rather small, e.g. comparing the best performing (domain-adapted) Auto-GDA versus the best performing “complex” method out-of-the-box (83.7 vs 80.5, 86.7 vs 85.4, 92.5 vs 90.4, 88.3 < 89.4), or Auto-GDA (Flan-T5) vs MiniCheck-T5 (75.6 \approx 75.4, 68.7 < 74.1, 82.4 vs 79.1; only one high improvement 78.3 vs 64.0).
2. I would expect more ablations of the proposed approach, e.g. testing the removal of each of the terms in eq. (2), or on the contrary using only one of these terms for filtering.
3. The motivation for the proposed approach is to improve RAG pipelines in domain-specific scenarios, however no experiments with domain-specific RAG are presented to demonstrate these improvements. For example, domain-specific RAG scenarios considered in [1] could act as potential testbeds, e.g. RobustQA [2].

### Questions
1. What is the time of running each step in Auto-GDA (steps 1-2-3 and NLI model training), for different datasets (with their sizes)?
2. One of the arguments for the necessity of domain adaptation in the introduction is that “inputs may follow a specific format due to the RAG prompt template” (line 79). Why not pass evidence and claims to NLI models without this template, if it reduces domain shift and hence improves performance?
3. What criteria is used to select optimal hyperparameters using optuna? Is it performance on some dataset (which one)?
4. How do you tune hyperparameters of unsupervised domain adaptation baselines?
5. Are there particular reasons why Vectara-2.1 outperforms AlignScore on RAGTruth and vice versa on other datasets? E.g. due to some specific training data or algorithm specifics.
6. Do you plan to release open-source code for the proposed approach?
[Update during discussion: all questions answered]


Comments
* Due to the high amount of notations, it may be hard to follow the method sometimes, e.g. trying to remember what a particular notation means. 
* Line 43: “even when the most capable LLMs are used with RAG, hallucination rates of 20 – 30% persist (Santhanam et al., 2021).”  too old reference
* Figure 1: “RAG task performance (ROC-AUC).” Unclear x label: it seems that it is RAG performance (unclear how measured with ROC-AUC), but it is NLI performance for RAG as far as I understand
* Line 233: “we also generate realistic initial samples using LLMs”. Use a more specific term than “samples”
* Line 384: “Optimizing the objective for a subset Q”. What does Q refer to here?
* Line 429: better define “complex” category

### Soundness
3

### Presentation
3

### Contribution
2
