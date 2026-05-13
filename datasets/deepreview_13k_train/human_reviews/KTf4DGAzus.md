# Towards Robust Multi-Modal Reasoning via Model Selection

- Decision: Accept
- Scores: 5, 6, 5, 6

## Abstract
The reasoning capabilities of LLM (Large Language Model) are widely acknowledged in recent research, inspiring studies on tool learning and autonomous agents.
    LLM serves as the ``brain'' of the agent, orchestrating multiple tools for collaborative multi-step task solving.
    Unlike methods invoking tools like calculators or weather APIs for straightforward tasks, multi-modal agents excel by integrating diverse AI models for complex challenges.
    However, current multi-modal agents neglect the significance of model selection: they primarily focus on the planning and execution phases, and will mainly invoke predefined task-specific models for each subtask, making the execution fragile.
    Meanwhile, other traditional model selection methods are either incompatible with or suboptimal for the multi-modal agent scenarios, due to ignorance of dependencies among subtasks arising by multi-step reasoning.
    \looseness=-2
    \\
    To this end, we identify the key challenges therein and propose the \framework framework as a plug-in with negligible runtime overhead at test-time.
    This framework improves model selection and bolsters the robustness of multi-modal agents in multi-step reasoning.
    In the absence of suitable benchmarks, we create MS-GQA, a new dataset specifically designed to investigate the model selection challenge in multi-modal agents.
    Our experiments reveal that our framework enables dynamic model selection, considering both user inputs and subtask dependencies, thereby robustifying the overall reasoning process.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper concentrates on the issue of model selection for multi-modal reasoning tasks. It introduces the Model Selector for the Multi-Modal Reasoning (M3) framework, designed to model the dependencies among subtasks and enhance model selection in multi-modal reasoning. To explore the model selection challenge in multi-modal tasks, the authors have created the MS-GQA dataset. The experiments demonstrate that the M3 framework improves the robustness of reasoning on the MS-GQA dataset.

### Strengths
1. This paper adeptly formulates the model selection problem within multi-modal reasoning contexts and constructs the MS-GQA dataset.
2. The paper is well-founded in its pursuit to address the overlooked subtask dependencies in previous works. The proposed M^3 framework innovatively and effectively models the relationship between samples, selected models, and subtask dependencies.
3. The experiments conducted on MS-GQA demonstrate the efficiency and efficacy of the M^3 framework.

### Weaknesses
1. The primary concern is that model selection is a small part of multi-modal reasoning. It remains to be seen whether it is important for the entire task and how it can benefit real-world applications. The selection method proposed in this paper involves complex proxy training and may need to be more universally applicable or scalable for different reasoning tasks.

2. Lack of reproducibility: The paper must include crucial details, such as the LLM used. The constructed MS-GQA dataset is not yet open-sourced, and the paper fails to provide even a single example of the dataset. Furthermore, the paper does not demonstrate how the proposed methods can improve various reasoning tasks and whether they can be applied to open-source models like LLaMA.

3. The implementation of the baselines is weak: The original HuggingGPT paper dynamically selected models for tasks through in-context task-model assignment, yet this paper describes it as only using "external metrics" and implements it as "choosing the most recently published one for each subtask", which is misleading and causes unfair comparisons.

4. The experiments could be more convincing: This paper only reports results on a newly created MS-GQA dataset. Even though it's compared to simple baselines that do not require training, like directly using the latest or best models (as shown in Table 2), the proposed M^3 method does not show consistent improvements and may even significantly degrade performance. It would be more convincing if experiments were conducted on more reasoning tasks, as done in VisProg and HuggingGPT.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the need for improved model selection in multi-modal agents to enhance their robustness in multi-step reasoning tasks. The authors introduce the M3 framework to facilitate dynamic model selection, considering user inputs and subtask dependencies, and they present the MS-GQA dataset as a benchmark for evaluating their framework's performance.

### Strengths
Identification of Critical Challenge: The paper recognizes and addresses a significant challenge in multi-modal agents, which is the selection of appropriate models for subtasks, a crucial aspect often overlooked in prior research.

Introduction of the M3 Framework: The paper presents the M3 framework, which aims to improve model selection by considering user inputs and subtask dependencies. The framework is designed with negligible runtime overhead at test-time, making it practical for real-world applications.

Creation of the MS-GQA Dataset: The authors introduce the MS-GQA dataset, specifically designed for investigating model selection challenges in multi-modal agents. This dataset is a valuable resource for benchmarking and advancing research in this area.

Experimental Findings: The paper provides experimental evidence that the M3 framework enhances dynamic model selection and, as a result, bolsters the overall robustness of multi-modal agents in multi-step reasoning tasks.

### Weaknesses
Limited Baseline Comparison: The paper could benefit from a more comprehensive comparison of the M3 framework with existing methods. While it claims to outperform traditional model selection methods, a detailed comparison with state-of-the-art techniques would provide a more robust evaluation. Specifically, the paper lacks a clear explanation of how the chosen baselines were selected and why they are representative of the current state-of-the-art in model selection for multi-modal agents. The paper should also include a discussion of the limitations of the baselines, and how these limitations might affect the comparison with the M3 framework.

Insufficient Experimental Discussion: The discussion of experimental results could be more in-depth. The paper does not thoroughly analyze the scenarios where the M3 framework performs exceptionally well or falls short. A deeper dive into the results would provide valuable insights into the framework's strengths and limitations. For instance, the paper should include a detailed analysis of the performance of the M3 framework on different subtasks, and how the performance varies with the complexity of the subtask. The paper should also analyze the impact of the size of the training dataset on the performance of the M3 framework.

Real-World Application Discussion: While the paper discusses the practicality of the M3 framework, it could delve further into real-world applications or use cases where this framework could be deployed effectively. This would provide a clearer vision of its potential impact. The paper should provide specific examples of how the M3 framework could be used in real-world scenarios, and discuss the potential benefits and challenges of deploying the framework in these scenarios. The paper should also discuss the limitations of the M3 framework in real-world applications, and how these limitations could be addressed.

### Questions
Please see weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the importance of model selection in multi-modal agents, where Large Language Models (LLMs) play a central role in orchestrating various tools for collaborative multi-step task solving. Unlike traditional methods that use predefined models for subtasks, these multi-modal agents excel by integrating diverse AI models for complex challenges. However, existing multi-modal agents tend to overlook the significance of dynamic model selection, focusing primarily on planning and execution phases, which can make the execution process fragile.

The paper introduces the M3 framework as a plug-in with a small runtime overhead at test time. This framework aims to enhance model selection and improve the robustness of multi-modal agents in multi-step reasoning scenarios. In the absence of suitable benchmarks, the authors create a new dataset called MS-GQA, designed to investigate the model selection challenge in multi-modal agents. The experiments demonstrate that the M3 framework enables dynamic model selection by considering both user inputs and subtask dependencies, ultimately enhancing the overall reasoning process. The authors plan to make their code and benchmark publicly available.

### Strengths
The paper provides a clear analysis of the challenges.   
Besides the method, the paper also provides a dataset as one of the contributions.  
The experimental results show significant improvements.

### Weaknesses
The method uses a heuristic process to perform selection which the capacity is relying on the pre-trained models themselves.  
How about the generalization capacity for the zero-shot tasks?

### Questions
refer to the above content.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studied the model selection problem in multi-modal reasoning. It first formulated this problem, and then proposed $M^3$ framework as an initial attempt in this field. This paper also created a new dataset, MS-GQA, as a benchmark to compare different methods.

### Strengths
1. This paper formulated the model selection problem in multi-modal reasoning, which is a new direction worth investigating.

2. This paper made an initial yet comprehensive effort to study this problem, including a model-selection framework, MS-GQA datasets, as well as a comparison between possible baselines.

### Weaknesses
1. The significance of the problem is not well illustrated. While the paper has shown the existence of model selection problem, I am not aware of how important this problem is. There can be lots of problems in multi-modal reasoning, but some may not be of much value. Specifically, is there a huge gap between an oracle model selection and a random selection? Is there a naïve solution that can approach the oracle performance? The authors are suggested to add these preliminary experiments to illustrate the significance of the problem. It would be helpful to see a comparison with a very simple baseline, such as always picking the first model in the sequence, or a majority vote approach, to understand the value added by the proposed method. Without such baselines, it's difficult to gauge how much improvement is truly gained by the proposed framework.

2. Lack of ablation study on model inputs. The paper claims that other model selection methods do not take subtask dependency into account. However, the ablation study does not show the effect of using subtask dependency as input. More broadly, because the framework uses various inputs, including multi-modal inputs, node embedding, subtask dependency, a more extensive ablation can be done by removing each component successively. This will show the importance of each component. It is not clear whether the subtask dependency is truly contributing to the performance gain, or if the performance is mainly driven by the multi-modal inputs and node embeddings. A proper ablation study should systematically remove each input feature to quantify its contribution.

### Questions
1. Presentation should be improved. I find some of the notations are used without introducing first, which hinders a smooth reading. 
Especially in Section 3.2:
* Page 4, bottom line, $\phi \circ \psi$ is used but they have not been introduced.
* Page 5, Section 3.2.1, Para 1, $\psi := [\psi_1, \psi_2]$ is used without explanation.

2. Why choose SER as the metric rather than accuracy? From Figure 1, I thought a wrong model selection will mainly cause the system to give false answer. But the main metric adopted is to measure the successful execution rate. I think there is a difference between successful execution and final accuracy.

3. What is the difficulty level in tab2? How do the authors define the difficulty level?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
