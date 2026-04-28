# White-Basilisk: A Hybrid Model for Code Vulnerability Detection

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
The proliferation of software vulnerabilities presents a significant challenge to cybersecurity, necessitating more effective detection methodologies. We introduce White-Basilisk, a novel approach to vulnerability detection that demonstrates superior performance while challenging prevailing assumptions in AI model scaling. Utilizing an innovative architecture that integrates Mamba layers, linear self-attention, and a Mixture of Experts framework, White-Basilisk achieves state-of-the-art results in vulnerability detection tasks with a parameter count of only 200M. The model's capacity to process sequences of unprecedented length enables comprehensive analysis of extensive codebases in a single pass, surpassing the context limitations of current Large Language Models (LLMs). White-Basilisk exhibits robust performance on imbalanced, real-world datasets, while maintaining computational efficiency that facilitates deployment across diverse organizational scales. This research not only establishes new benchmarks in code security but also provides empirical evidence that compact, efficiently designed models can outperform larger counterparts in specialized tasks, potentially redefining optimization strategies in AI development for domain-specific applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces White-Basilisk, a compact AI model designed for detecting vulnerabilities in code with only 200 million parameters. This model integrates several advanced concepts including Mamba layers, linear-complexity Infini-attention, and a Mixture of Experts framework to process large codebases on limited computational resources. Evaluated on established benchmark datasets demonstrates superior performance of White-Basilisk compared to existing baselines.

### Strengths
1. The paper addresses a topic of significant importance within the field, which is timely and relevant to current research trends.
2. The performance of the proposed method outperforms established baselines across several existing datasets.

### Weaknesses
1. The paper lacks a well-formulated research question, which detracts from the theoretical impact of the study. The proposed approach is less technically motivated, which makes the paper more like an assembled engineering work.
2. The overall performance of the proposed approach is not explainable, missing an opportunity to provide insights into the operational implications.
3. Poor presentation especially with vague descriptions in the design details. 
4. Lack of sufficient references on related works and discussion of the existing research background

### Questions
The paper states "all while ideally being deployable in resource-constrained environments", while mostly the code vulnerability detection primarily occurs offline, implying that computational resources do not significantly constrain the process. The complex nature of large code space bug vulnerability detection further fosters the need for bigger models for understanding the code contextual information. why do authors make such claims and any specific motivation scenarios can support such claims?

The overall formula for explaining the design of the White-Basilisk seems rushed. Formula (3) introduces parameters Δ, B, and C without adequate definitions or explanations. How are these parameters used, and what significance do they hold in the computations? Additionally, the basis for setting parameter A and the selection of top-k values at 8 and 2 are unclear. If these choices are informed by existing work, the paper should provide citations or rationale for these specific values.

The paper only evaluates the proposed method on C/C++ tasks. Why does the study specifically focus on C/C++? The lack of comprehensive experiment undermines the claimed high performance compared to existing baselines.

How do the individual components of the proposed White-Basilisk model contribute to its overall functionality? Additionally, how have the authors determined the effectiveness and utility of each design element within White-Basilisk?

### Soundness
2

### Presentation
2

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
This paper is in the domain of code vulnerability detection, i.e. taking as input a computer program such as C++ code and output a list of vulnerabilities / weaknesses often mapped to a database of Common Weakness Enumeration (CWE) labels. This is a multi-label classification task.

The paper introduces a new model called White-Basilisk for solving this problem, which has the following features:
1. Novel architecture combining and adapting three pre-existing modules from deep learning literature: (1) Mamba layers (structured state space sequence models), (2) Infini-attention (modified attention layers with linear complexity), (3) Mixture of Experts (layers for adaptability)
2. The model tries to address the prevalent challenges in this domain with its White-Basilisk architecture: (a) long range dependencies and context in extended code sequences, (b) imbalanced data sets (c) resource efficiency (number of parameters, GPU resources required)
3. Evaluation is done on 5 datasets from literature using 3 evaluation metrics (accuracy, F1 and Vulnerability Detection Score (False Negative Rate) against a number of baselines (most being the base systems of the corresponding datasets). White-Basilisk consistently outperforms all chosen baselines on F-scores.

The paper claims its main contribution is the experiments to show that efficiently designed architecture (mamba + MoE + inifini attention) and smaller finetuned models outperform their larger counterparts.

### Strengths
1. Code Vulnerability Detection is an important topic and has gained recent traction since LLMs and ChatGPT both by NLP research community as well as cybersecurity researchers 
2. The architecture is novel, i.e. the combination pattern of mamba, MoE, and attention layers and the reasoning is sound
3. Evaluation is done on multiple standard datasets (benchmarks) and multiple baselines are used to demonstrate the effectiveness of the approach
4. Sufficient model implementation details are given in the appendix to make it reproducible
5. Considerable thought has been given to the carbon footprint implications of deep learning models which is rarely addressed in most papers
6. The point though not novel (it has been observed in multiple papers and blogs previously) is valid that smaller finetuned models often outperform larger resource-intensive models and we need to rethink AI efficiency.

### Weaknesses
The overall problem description and the empirical evaluation (Section 4) seems to be lacking in vital details that has lowered the paper's presentation and contribution factors. Addressing the following points can help remediate this:

1. While those familiar with the domain of code vulnerability detection and its literature will hardly notice it, the paper does not explicitly state what kind of problem it is solving. Note some things can be inferred from reading between the lines (section 4.3) but it would still be nice to explicitly state them by answering the following questions:. 
a) Is it a multi-label or multi-class classification problem? Can one code snippet be mapped to more than one vulnerability?
b) How many classes are in the output? Is CWE list being used for the lables? How granular?
c) If the different datasets have used different granularities of the output labels are they still comparable? A table displaying the data statistics could help.

2. The baseline systems are not well-defined. A single sentence for each system describing the architecture can suffice or more details can be added in the appendix. It is difficult to evaluate the effectiveness of this approach if one does not know how the other baseline systems were trained. Again  lots can be inferred from reading the names and reading the references but it would be nice to have it explicitly stated somewhere.
a) More explanation is needed to better understand what we are seeing in Tables 1 and 2.
b) What is UnixCoder? - Missing reference
c) What is CodeT5? - Missing reference
d) Are there any systems which use GPT as their backbone?
e) Was there any ablation tests done to investigate the individual contribution of mamba / MoE / Inifini Attention layers?

### Questions
Asked in the Weaknesses section (see above)

### Soundness
3

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
3

### Summary
The paper introduces “WHITE-BASILISK,” a hybrid model for detecting code vulnerabilities. This model combines a Mamba layer, linear self-attention, and a Mixture of Experts framework to achieve accurate vulnerability detection with only 200 million parameters, striking a new balance between efficiency and effectiveness. Specifically, the paper contributes to both model architecture and training methods, while expressing concerns about the current trend of increasing parameter counts to enhance performance.

### Strengths
This paper focuses on the efficiency challenges in vulnerability detection—a significant and original direction amidst the prevailing trend of scaling up model size. It introduces a hybrid model that achieves impressive detection performance with a limited parameter count, and the experimental results provide partial evidence supporting this claim. The presentation is logically structured, with a well-organized summary of related work, and a clear description of the model architecture and training methodology for the proposed approach.

### Weaknesses
In Section 2, the paper mentions the poor quality of current benchmarks, which fail to accurately reflect model performance in real-world scenarios, resulting in suboptimal effectiveness in practice. However, the experiments in this paper also seem to fall short in demonstrating the model’s real-world performance, making the claimed results less convincing.
In terms of innovation, the model structure appears to be primarily a combination and refinement of existing approaches (Mamba layers, infini-attention, and MoE). According to the authors, the model addresses challenges related to long dependencies and extensive codebases, but they also claim it resolves issues with diverse vulnerabilities and different programming paradigms, which often hinder the performance of ML-based approaches. Based on the description provided, this aspect is not clearly substantiated; the authors should explicitly detail how their model addresses the later challenge.

### Questions
In terms of presentation, although the authors have done well overall, there are still areas for improvement. When certain parameters are introduced for the first time, they should be explained, even if they are common within the field.
It is relatively clear how the proposed approach addresses the challenge of long dependencies and extensive codebases; however, the authors’ claim that it also addresses issues with diverse vulnerabilities and different programming paradigms needs further clarification—how exactly does the model achieve this?
In the experiments section, the authors should dedicate a subsection to describing the datasets used and the calculation method for the metrics.
In Section 4.2.1, the authors mention a “PerturbationLayer,” yet it is not represented in the White-Basilisk Architecture diagram (Fig. 1). Why is this the case?
Additionally, Section 4.2.1 discusses the robustness of the proposed approach. Relevant experiments should be included in the experiments section to demonstrate this robustness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new approach to vulnerability detection by utilizing an innovative architecture that integrates Mamba layers, linear self-attention, and a Mixture of Experts framework.

### Strengths
The proposed idea of combining the Mamba layer with self-attention layers sounds interesting.
Compared to LLMs, the proposed method enables effective processing of long code sequences while maintaining a relatively small parameter count.
The experimental results on real-world datasets show the advancements of the proposed method compared to the baselines.

### Weaknesses
The proposed architecture integrates Mamba layers, linear self-attention, and a Mixture of Experts framework; however, the ablation studies for the importance of each factor to the proposed model’s performance have not been conducted.

It is unclear and mentioned how each dataset is split for training and evaluating the models’ performance. Do the authors split the data into training, validation and testing sets?

In the pre-training phase of the proposed method, do the authors use all the data in the datasets used?

Lack of comparisons with state-of-the-art baselines, especially the methods based on graph neural networks and the methods leveraging both the semantic and syntactic relationships from the source code data, such as:

Guilong Lu and Xiaolin Ju and Xiang Chen and Wenlong Pei and Zhilong Cai. GRACE: Empowering LLM-based software vulnerability detection with graph structure and in-context learning. Journal of Systems and Software. 2024.

Van-Anh Nguyen and Dai Quoc Nguyen and Van Nguyen and Trung Le and Quan Hung Tran and Dinh Phung. ReGVD: Revisiting Graph Neural Networks for Vulnerability Detection. International Conference on Software Engineering. 2022.

Yangruibo Ding and Sahil Suneja and Yunhui Zheng and Jim Laredo and Alessandro Morari and Gail Kaiser and Baishakhi Ray. VELVET: a noVel Ensemble Learning approach to automatically locate VulnErable sTatements.  IEEE International Conference on Software Analysis, Evolution and Reengineering. 2022.

Daya Guo and Shuo Ren and Shuai Lu and Zhangyin Feng and Duyu Tang and Shujie Liu and Long Zhou and Nan Duan and Alexey Svyatkovskiy and Shengyu Fu and Michele Tufano and Shao Kun Deng and Colin Clement and Dawn Drain and Neel Sundaresan and Jian Yin and Daxin Jiang and Ming Zhou. GraphCodeBERT: Pre-training Code Representations with Data Flow. International Conference on Learning Representations. 2021.

Yaqin Zhou and Shangqing Liu and Jingkai Siow and Xiaoning Du and Yang Liu. Devign: Effective Vulnerability Identification by Learning Comprehensive Program Semantics via Graph Neural Networks. Annual Conference on Neural Information Processing Systems. 2019.
The rationale of the proposed architecture described in Figure 1 needs to be more explainable, especially for the positions of each block and the use of residual connections.

### Questions
From Section 5.1 to the end of the paper, the font size is too small and not aligned with the format requirements from ICLR.

Regarding the mixture of expert layers, the authors mention that “MoE layers allow the model to activate only a subset of parameters for each input, reducing significantly the computational cost compared to fully dense models of similar capacity. In the context of code vulnerability detection, this efficiency is crucial as it allows our model to handle effectively diverse types of code and potential vulnerabilities without adding to its complexity and number of parameters”. Qualitative experiments need to be conducted to demonstrate this claim.

What is the model configuration for the baselines? How do you fine-tune and apply them?

Regarding handling the class imbalance, how is it effective in improving the proposed model performance?

### Soundness
2

### Presentation
2

### Contribution
2
