# HESSO: Towards Automatic Efficient and User Friendly Any Neural Network Training and Pruning

- Decision: Reject
- Scores: 6, 3, 6, 3

## Abstract
Structured pruning is one of the most popular approaches to effectively compress the heavy deep neural networks (DNNs) into compact sub-networks while retaining the original network performance. The existing methods suffer from multi-stage procedures along with significant engineering efforts and human expertise. The Only-Train-Once series (OTOv1-v3) has been  recently proposed to resolve the many pain points by streamlining the workflow by automatically conducting \textit{(i)} search space generation, \textit{(ii)} structured sparse optimization, and \textit{(iii)} sub-network construction. However, the built-in sparse optimizers in the OTO series, \ie, the Half-Space Projected Gradient (HSPG) family, have limitations that require hyper-parameter tuning and the implicit controls of the sparsity exploration, consequently requires intervening by human expertise. To further address such limitations, we propose a novel Hybrid Efficient Structured Sparse Optimizer (\algacro). \algacro{} could automatically and efficiently train a DNN within a single run to produce a high-performing sub-network. Meanwhile, it is almost tuning-free and enjoys user-friendly integration for generic training applications. To address another common issue of irreversible pruning performance collapse observed in some DNNs, we further propose a novel Corrective Redundant Identification Cycle (\cric{}) to plug into \algacro{} for reliably identifying indispensable structures. We numerically demonstrate the efficacy of \algacro{} and its enhanced version \hessocric{} on a variety of applications ranging from computer vision to natural language processing, including large language model. The numerical results showcase that \algacro{} can achieve competitive performance to varying state-of-the-art benchmarks and support most DNN architectures. Meanwhile, \cric{} can effectively prevent the irreversible performance collapse and further enhance the performance of \algacro{} on certain applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Hybrid Efficient Structured Sparse Optimizer (HESSO), a structured pruning algorithm. In addition, for reliably identifying the indispensable structure, the authors introduce Corrective Redundant Identification Cycle (CRIC). The experimental results show that HESSO with CRIC plugged in can perform well on various types of models, e.g., image classification, object detection and large language models.

### Strengths
1. This paper is well written and organized.
2. This paper provides thorough experiments, by evaluating the performance of HESSO on various tasks and comparing with many other pruning methods.
3. It is demonstrated that HESSO is able to achieve strong and impressive results with a considerable pruning ratio.

### Weaknesses
See questions.

### Questions
1. What is the computational cost of employing HESSO? I am wondering whether it will significantly increase the computational memory and flow training speed.
2. Seems CIRC can be used as a generic module to identify the indispensable structures. Can it be applied to other pruning algorithms and what is the performance?

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
The paper addresses the challenge of deploying large deep neural networks by proposing **HESSO**, a new optimizer that enables automatic one-shot joint training and structured pruning for various DNN architectures and tasks. HESSO simplifies the hyper-parameter setup and employs a progressive pruning strategy to explicitly control sparsity exploration, enhancing usability. It optionally integrates a Corrective Redundancy Identification Cycle mechanism to accurately identify redundant groups, minimizing the risk of irreversible performance degradation caused by pruning indispensable structures.  The authors have conducted experiments on various type of tasks and models.

### Strengths
1.By simplifying hyper-parameter tuning and explicitly controlling sparsity exploration, HESSO enhances usability, making it accessible to practitioners without deep optimization expertise.

2. The optimizer is designed to be applicable to any DNN architecture and task, increasing its potential impact across various domains and applications.

### Weaknesses
1. As a paper on structured pruning, it does not compare with state-of-the-art methods on ImageNet, such as OFA, EagleEye ResRep, etc. The comparisons are too simplistic, making it impossible to see the advantages of the proposed method. Furthermore, in experiments on large models, it only compares with SliceGPT, which is not tailored for structured pruning. More mainstream baseline methods like LLMPruner need to be included for comparison. Overall, the experimental section significantly dampens my enthusiasm for this paper.

2. The authors' discussion of related work in the field is rather lacking and not sufficiently grounded. The entire introduction, methodology, and experimental discussions focus only on OTO-based papers[4,5,6]. However, as far as I know, there are many papers on automatic structure search for structured pruning, including OFA[1], EagleEye[2], etc. I suggest that the authors provide a more comprehensive coverage of the field, which would effectively enhance the quality of this paper.

### Questions
Please see the weakness part.

### Soundness
1

### Presentation
2

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
The manuscript presents a novel approach to deep neural network (DNN) training and structured pruning through Hybrid Efficient Structured Sparse Optimize (HESSO). The topic is highly relevant in the current AI landscape, where deploying efficient models in resource-constrained environments is critical. HESSO stands out by simplifying hyper-parameter setup and offering a progressive pruning strategy that enhances user-friendliness. In addition, the authors also discuss the limitations of the proposed method and the approximation errors of salience scores.

### Strengths
1. This paper is well-motivated, and the topic is highly relevant in the current AI landscape, where deploying efficient models in resource-constrained environments is critical. 
2. The manuscript provides a well-structured theoretical framework for HESSO, which helps justify the design choices made in the method.
3. The authors conduct extensive experiments in an array of tasks.

### Weaknesses
1. While HESSO aims to simplify hyper-parameter tuning, the manuscript does not provide sufficient evidence to support the claim of reduced sensitivity. A comparative analysis of tuning efforts required for HESSO versus traditional methods is needed.
2. The scalability of HESSO to larger models is not well demonstrated. A table or figure listing the computational cost of applying HESSO to models across different model sizes should be provided.
3. The optimal sparsity levels appear highly dependent on training transparency and available resources, making the method's performance less consistent across different scenarios. This variability undermines the claim of a generally applicable, tuning-free approach.
4. The method's reliance on training data for saliency score calculation raises concerns about potential overfitting, particularly during the pruning phase. The lack of evaluation on held-out datasets further exacerbates this issue.

### Questions
1. How does HESSO manage the trade-off between sparsity and performance? Is there a recommended range for optimal sparsity levels?
2. Is there a risk that the method could lead to overfitting, especially during the pruning phase? Maybe evaluation in held-out datasets are needed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes HESSO, a novel optimizer designed for structured pruning of DNNs. HESSO aims to automatically and efficiently train any DNN to produce high-performing sub-networks with minimal need for hyper-parameter tuning, enhancing user-friendliness. Additionally, this paper introduces an extension of HESSO called HESSO-CRIC to address issues related to the irreversible performance collapse that sometimes occurs in pruned models. HESSO and HESSO-CRIC are evaluated across various applications, including computer vision and natural language processing, where it demonstrates competitive performance compared to existing baselines.

### Strengths
1. The paper is well-written, with clear organization and rigorous logic, making it understandable to readers.
2. HESSO can automatically and efficiently train and prune DNNs with any architecture, providing competitive performance, which holds broad significance in the field of neural network pruning.
3. The authors conducted a comprehensive analysis of how approximation errors of saliency score can lead to misidentification of indispensable structures in pruned DNNs, resulting in performance collapse. This part is well-organized, highly interesting, and very insightful.

### Weaknesses
1. I believe the main issue with this paper is the lack of many necessary comparison baselines, or the existing comparison baselines are outdated.
1) Section 4.3: In the CoFi [1] method, BERT-Base achieves a lossless F1 score on the SQuAD dataset with a 70% reduction in parameters (Figure 2 in CoFi). However, in the HESSO method, BERT-Base shows a drop of about 4% in F1 score with approximately a 50% reduction in parameters.
2) Section 4.4: HESSO seems to be inferior to the ATO [2] method, as ATO achieved a TOP-1 accuracy of 76.07% with a 61.7% reduction in FLOPs, only a -0.06% drop compared to the baseline. However, under the same FLOPs, the accuracy of HESSO is below 76%.
3) Section 4.6: The authors only compare with the SliceGPT method, lacking comparisons with some important structured pruning baselines for LLMs, such as LLM-Pruner (with LoRA fine-tuning) [3], LoRAPrune [4] and LoRAShear [5].
Due to the lack of the above baselines, I have concerns about the effectiveness of the HESSO method.
2. It seems that HESSO is simply improved version of OTO v3. As far as I know, OTO v3 also proposes a hybrid training scheme that applies different update mechanisms to important and redundant variable groups. HESSO does not seem to introduce any significant innovations but rather represents a minor technical improvement over OTO v3.
3. Different saliency scores likely result in varying approximation errors. The authors should demonstrate whether the CRIC mechanism effectively corrects each type of approximation error. Therefore, the authors should show the impact of different saliency scores in HESSO-CRIC on the final accuracy.
4. The phrase "can not be recovered given user resources" in Definition 3.1 is confusing, as it is evident that models with different parameters require significantly different training resources. The authors should clarify the definition of "user resources" more explicitly.

### Questions
1. In line 215, the authors state, “The selection of the saliency score in HESSO is flexible and can be tailored to different purposes.” I would like to know how the authors select the saliency score for different tasks in Sections 4.2-4.6. 
2. In lines 503-507, the authors state, “Since both HESSO and HESSO-CRIC … without requiring tensor parallelism.” Does this mean that the HESSO method does not support models larger than 3 billion parameters? In addition, since both HESSO and HESSO-CRIC utilize full gradient information of LLMs, I would like to know the training cost of HESSO and HESSO-CRIC on LLMs.
[1] Structured Pruning Learns Compact and Accurate Models. ACL 2022 Main.
[2] Auto-Train-Once: Controller Network Guided Automatic Network Pruning
from Scratch. CVPR 2024.
[3] LLM-Pruner: On the Structural Pruning of Large Language Models. NeurIPS 2023.
[4] LoRAPrune: Structured Pruning Meets Low-Rank Parameter-Efficient Fine-Tuning. ACL 2024 Findings.
[5] LoRAShear: Efficient Large Language Model Structured Pruning and Knowledge Recovery. ArXiv.
[6] OTOv3: Towards Automatic Sub-Network Search Within General Super Deep Neural Networks. ArXiv.

### Soundness
2

### Presentation
3

### Contribution
1
