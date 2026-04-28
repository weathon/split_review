# FedSecurity: A Benchmark for Attacks and Defenses in Federated Learning and Federated LLMs

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
\new{This paper introduces FedSecurity, an end-to-end benchmark that serves as a supplementary component of the FedML library for simulating adversarial attacks and corresponding defense mechanisms in Federated Learning (FL). 
FedSecurity eliminates the need for implementing the fundamental FL procedures, \textit{e}.\textit{g}., FL training and data loading, from scratch, thus enables users to focus on developing their own attack and defense strategies.
It contains two key components, including FedAttacker that conducts a variety of attacks during FL training, and FedDefender that implements defensive mechanisms to counteract these attacks. 
FedSecurity has the following features: \textit{i}) 
It offers extensive customization options to accommodate a broad range of machine learning models (\textit{e}.\textit{g}., Logistic Regression, ResNet, and GAN) and FL optimizers (\textit{e}.\textit{g}., FedAVG, FedOPT, and FedNOVA); 
\textit{ii}) it enables exploring the effectiveness of attacks and defenses across different datasets and models; and \textit{iii}) it supports flexible configuration and customization through a configuration file and some APIs. 
We further demonstrate FedSecurity's utility and adaptability through federated training of Large Language Models (LLMs) to showcase its potential on a wide range of complex applications.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces FedSecurity, a library with attacks and defenses for federated learning useful for benchmarking and assessing the quality of defenses against different sets of attacks. The library comprises of two components: 1) FedAttack for training-time attacks in FL, including data and model poisoning and data reconstruction attacks; 2) FedDefender, which includes defenses that can be applied at the aggregator before, during or after the aggregation of the model parameters.

### Strengths
+ Robustness of Federated learning is a hot topic and libraries for assessing the robustness of different aggregation methods and defensive techniques systematically is useful not only for the research community, but also for other ML practitioners and developers. 

+ The library seems to include a good set of attacks and defenses, although a table or a list with the complete catalogue of attacks and defenses would be beneficial for the reader. It is a plus that the library support some LLMs. 

+ The paper is well presented and easy to read.

### Weaknesses
 - The paper does not include new techniques or advancements in the state of the art. It entirely relies on attacks and defenses that have already been proposed in the research literature. The experimental evaluation is a confirmation that the code produces reasonable results, but there is no novelty in there either. 

- The authors did not provide the code implementation of the library (I believe it could be easily anonymized). Then, as the main contribution of the paper is the library, not having access to the code implementation makes it hard to assess its characteristics and possible weaknesses. 

- The coverage of the library misses attacks at test time (e.g., adversarial examples) and other privacy attacks that can happen both during the training and the deployment of federated learning models, such as property inference attacks or membership inference attacks, to cite some.

### Questions
+ Could the authors provide the whole catalogue of attacks and defenses implemented in the library?

+ Could the authors provide the code implementation (anonymized). 

+ Could the authors clarify the contributions of the paper for advancing the state of the art in robust federated learning?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces FedSecurity, a benchmark for simulating attacks and defenses in federated learning (FL).  FedSecurity has two main components: FedAttacker to inject attacks like data poisoning, model poisoning, and data reconstruction; and FedDefender to implement defenses like clipping, robust aggregation, and adding noise. It supports customizing attacks and defenses using provided APIs. It is also flexible to configure different models, datasets, and FL optimizers like FedAvg, FedOpt, etc. Experiments show Byzantine attacks like random noise can significantly degrade accuracy while defenses like m-Krum can mitigate it. Defenses may also inadvertently hurt accuracy when no attack happens. FedSecurity is also extended to federated training of large language models (LLMs) like BERT and Pythia. m-Krum defense is shown to be effective against backdoor and Byzantine attacks on LLMs.

### Strengths
1.	LLM extension: The benchmark is extended to federated training of large language models like BERT and Pythia, showing wider applicability.
2.	Real-world demonstration: A real-world experiment using edge devices shows the scalability beyond simulations.
3.	Analysis and insights: The experiments analyze impacts of attacks and defenses, highlighting the need to balance robustness vs potential negative impacts of defenses.

### Weaknesses
1.	Limited defense mechanisms: Only a small subset of defenses from the literature are implemented so far. More defenses could be included for completeness.
2.	Limited analysis: More in-depth analysis and visualization of how the attacks and defenses impact the model convergence would be useful.
3.	Small LLM experiments: Evaluations on large language models are limited to just BERT and Pythia. More experiments on diverse LLMs would strengthen this part.
4.	Narrow task types: Most experiments focus on image classification. Expanding the tasks to include NLP, recommendation systems, etc. would make it more representative.

### Questions
See in Weakness

### Soundness
2 fair

### Presentation
3 good

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
The authors introduce a comprehensive benchmark for simulating adversarial attacks and their corresponding defense strategies in the context of Federated Learning (FL). This benchmark, known as FedSecurity, is composed of two primary components: FedAttacker, which replicates attacks introduced during FL training, and FedDefender, which emulates defense mechanisms aimed at mitigating the effects of these attacks. FedSecurity is an open-source tool that can be tailored to encompass a wide array of machine learning models (e.g., Logistic Regression, ResNet, and GAN) and federated optimization techniques (e.g., FedAVG, FedOPT, and FedNOVA). Additionally, the authors demonstrate the utility of FedSecurity in the context of federated training for Large Language Models (LLMs), showcasing its adaptability and relevance in more intricate scenarios.

### Strengths
1. It is important to have federated Large Language Models (LLMs) benchmark at this point for the community. I look forward the authors can dig deeper in this category and provide more complete/efficient implementation.

2. Different categories of attack and defense methods been implemented.

### Weaknesses
1. To implement federated LLM, the bottleneck is always the computational power. I wonder if the authors can provide some of their pre-trained models before/after fine-tunning?

2. Large-scale experiment up to 1000 clients is usually needed for benchmark works.

3. A table for the real training time is suggested (better on different devices).

4. Need more ablation studies given it is a benchmark work.

5. Attacks/defenses for NLP tasks (e.g., [1]) can be added to the benchmark for LLM and/or smaller models.

6. More backdoor attacks/defenses can be considered, and different evaluation metrics are needed (e.g., backdoor attack success rate)

### Questions
Compared with existing federated learning benchmarks (e.g., Leaf [1], Flower [2]), what are the major advantages of the newly proposed benchmark?

[1] Caldas, S., Duddu, S.M.K., Wu, P., Li, T., Konečný, J., McMahan, H.B., Smith, V. and Talwalkar, A., 2018. Leaf: A benchmark for federated settings. arXiv preprint arXiv:1812.01097.
[2] Beutel, D.J., Topal, T., Mathur, A., Qiu, X., Fernandez-Marques, J., Gao, Y., Sani, L., Li, K.H., Parcollet, T., de Gusmão, P.P.B. and Lane, N.D., 2020. Flower: A friendly federated learning research framework. arXiv preprint arXiv:2007.14390.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a benchmark for federated learning security, including two components: federated attacker and federated defender. The federated attacker implements about eight classical attack methods covering data poisoning attacks, model poisoning attacks, and data reconstruction attacks. The defenders include before-aggregation, after-aggregation, and on-aggregation defenses.

### Strengths
A substantive assessment of the strengths of the paper, touching on each of the following dimensions: originality, quality, clarity, and significance. We encourage reviewers to be broad in their definitions of originality and significance. For example, originality may arise from a new definition or problem formulation, creative combinations of existing ideas, application to a new domain, or removing limitations from prior results. You can incorporate Markdown and Latex into your review. 
S1. This paper proposes a comprehensive benchmark for federated learning security, which is expected to prompt the prosperity of security research of federated learning.
S2. The benchmark attempts to incorporate large language models, indicating its generalization ability.
S3. The limitations and future direction have been discussed in this paper.

### Weaknesses
W1. This paper highlights that the benchmark considers LLMs; however, the unique challenges/differences between using LLMs and classical models are unclear. Specifically, the paper does not discuss how the large parameter size, different training procedures, and unique vulnerabilities of LLMs impact the effectiveness of the implemented attacks and defenses. For instance, the susceptibility of LLMs to backdoor attacks or the computational cost of defenses when applied to LLMs are not addressed.

W2. It seems that the implemented attack/defense methods were published before 2021. The authors are encouraged to reproduce more SOTA attacks/defenses to improve the utility of this benchmark further. The current selection of methods might not reflect the most recent advancements in the field, potentially limiting the benchmark's relevance for cutting-edge research. For example, more recent gradient-based attacks or defenses tailored for federated learning could be included.

W3. In footnote 2, the authors claim that their benchmark focuses on security rather than privacy. However it seems that “data reconstruction attack” is about privacy, which makes the taxology of this paper a little bit confusing. The inclusion of data reconstruction attacks, which are inherently privacy-focused, contradicts the stated focus on security, creating a conceptual inconsistency in the benchmark's design.

### Questions
See Weeknesses. Addressing these weaknesses will further improve the convincing and quality of this paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
