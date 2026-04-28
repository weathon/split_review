# SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Smartphone agents are increasingly important for helping users control devices efficiently, with (Multimodal) Large Language Model (MLLM)-based approaches emerging as key contenders. Fairly comparing these agents is essential but challenging, requiring a varied task scope, the integration of agents with different implementations, and a generalisable evaluation pipeline to assess their strengths and weaknesses. In this paper, we present \ours, a comprehensive \textbf{S}mart\textbf{P}hone \textbf{A}gent \textbf{Bench}mark designed to evaluate (M)LLM-based agents in an interactive environment that simulates real-world conditions. \ours\ offers three key contributions: (1) A diverse set of tasks covering system and third-party apps in both English and Chinese, focusing on features commonly used in daily routines; (2) A plug-and-play framework enabling real-time agent interaction with Android devices, integrating over ten agents with the flexibility to add more; (3) A novel evaluation pipeline that automatically assesses agent performance across multiple dimensions, encompassing seven metrics related to task completion and resource consumption. Our extensive experiments across tasks and agents reveal challenges like interpreting mobile user interfaces, action grounding, memory retention, and execution costs. We propose future research directions to ease these difficulties, moving closer to real-world smartphone agent applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Spa-Bench, a comprehensive benchmark designed for evaluating smartphone agents across a variety of tasks in both English and Chinese languages. This benchmark supports over 340 tasks that span single-app and cross-app scenarios, covering different app types and real-world complexities such as third-party app interactions and varying difficulty levels. SPA-BENCH also integrates a plug-and-play framework that supports 11 agents and features a scalable, automated evaluation pipeline. This pipeline assesses agent performance based on success rates, efficiency, resource consumption, and reliability, eliminating the need for handcrafted evaluation logic. Experiments reveal that while proprietary (M)LLM-based agents outperform open-source counterparts, they still face challenges in real-world application due to time and cost inefficiencies. The paper emphasizes the need for advancements in UI understanding, memory retention, and error handling to improve the practicality of autonomous smartphone agents. I raise an acceptance of this paper.

### Strengths
1. Diverse task collection of 340 tasks

2. Automated evaluation pipeline consists of multiple evaluation metrics

### Weaknesses
Paper can be better organized.

Paper can be better organized. For example, there is a very large blank space between line 188 and 191. These large blank spaces need to be fixed.

In the paper, authors mention the human-executed trajectory to avoid shortcuts. Why do we need to avoid the shortcuts? I think it is not a bad choice if the agent is able to find a shortcut solving the problem.

### Questions
1. Paper can be better organized. For example, there is a very large blank space between line 188 and 191. These large blank spaces need to be fixed.

2. In the paper, authors mention the human-executed trajectory to avoid shortcuts. Why do we need to avoid the shortcuts? I think it is not a bad choice if the agent is able to find a shortcut solving the problem.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The present work introduces a new smartphone agent benchmark called “SPA-BENCH.” The motivation for this research stems from the rapid development and increasing adoption of (multimodal) LLM-powered smartphone agents. SPA-BENCH seeks to address the challenges of evaluating these agents by providing a structured evaluation environment that simulates real-world conditions. SPA-BENCH includes a diverse set of tasks that cover both single-app and cross-app tasks on system and third-party applications, catering to both English and Chinese users. The authors also conduct extensive experiments with 7 off-the-shelf LLM agents and 4 finetuned LLM agents, highlighting the key insights derived from these experiments.

### Strengths
1.This paper studies an important and timely problem. Developing a comprehensive benchmark is important to advance LLM agents in smartphone applications. 

2.The present work includes comprehensive experiments with 11 LLM agents on diverse tasks. The findings derived from these experiments could provide insights for future LLM agent design.

3.This paper introduces a plug-and-play framework, which could facilitate real-time interaction with Android devices. It is important to support diverse tasks and minimize the gap to real-world usage.

4.The design of the proposed benchmark is adequately motivated. In general, the paper is well-written.

### Weaknesses
1.The evaluation tasks are constructed by human annotators. It is fine, but I think the present work will benefit a lot if the authors could discuss more about the process of recruiting human annotators and protocols for quality control. It will also be great if the authors can discuss the possibility of synthesizing behavior trajectory, which might extend the impact of present work from solely evaluation to fine-tuning or even pre-training.

2.In addition to off-the-shelf LLM agents and fine-tuned agents, it is also important to evaluate locally deployable agents and cloud-based agents [1], which is particularly relevant for mobile agent setting. I suggest the authors to re-organize the taxonomy of agents as two main categories, i.e., agent-as-a-model (fine-tuned or pre-trained models customized for agentic tasks) [2] and agentic workflow (usually based on off-the-shelf model, possibly with modular design) [3].

3.Can SPA-bench be applied to a broader range of smart devices? Such as tablets with Android systems or IOS devices. I think it is important to discuss the potential and challenges here.

4.The authors should also elaborate on the main differences of smartphone agents compared to PC agents or cloud-based agents. It provides important insights for context of application.

### Questions
Please refer to the Weaknesses above.

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
This paper presents a benchmark for mobile device control agents, featuring the incorporation of Chinese applications in addition to English apps and newly proposed evaluation metrics regarding task completion. The benchmark includes a set of tasks that involve single and multi-app usage. The authors assess the performance of state-of-the-art agents developed through prompting or fine-tuning (e.g., agent fine-tuned with reinforcement learning). The valuable analyses in this work reveal the limitations of existing algorithms, particularly when handling tasks that span multiple applications or incorporate Chinese-language interfaces. 

The key contributions of these works are benchmark task suites with both English and Chinese apps, additional evaluation metrics, and experiments with in-depth analyses of various agents.

### Strengths
S1 - This benchmark offers a notable addition to the community by employing Chinese applications. This expands the scope and applicability of benchmarking in multilingual contexts.

S2 - The benchmark includes diverse tasks, levels, and metrics. It also introduces several new evaluation metrics. Furthermore, a novel coarse-to-fine evaluation approach has been proposed.  

S3 - The authors provided comprehensive benchmark references and included many of the existing baselines. Hence, this study offers a comprehensive comparison, enabling valuable insights. For example, it reveals the necessity of improved memory capabilities and lack of understanding in task termination.

### Weaknesses
W1 - This benchmark’s unique challenge is unclear. The authors should highlight the specific interesting challenge or novel difficulties it poses compared to existing benchmarks.

W2 - While the newly introduced termination metrics are intriguing and valuable, they seem to require more careful design. Could the authors propose a strategy for applying these metrics to agents that do not produce language-based rationales for termination? (Minor) Additionally, it would be helpful if the authors could underscore the significance of these metrics (e.g., why the ability to understand the termination of the tasks would be important when developing agents) while introducing the metric (i.e., Section 5.1).

W3 - The criteria for levels 1, 2, and 3 appear somewhat ambiguous. If the levels are based solely on the number of steps required, the division doesn't sound necessary. Could the authors clarify this distinction if these levels also account for the complexity of cross-app usage?

W4 - Several claims in the paper require further elaboration. For instance, the qualitative complexity of the a11y tree could be clarified by providing additional metrics, such as the number of tokens, as referenced in lines 367-371. Additionally, could the authors further elaborate on what they mean by "adequately grounding them in real-world context", as mentioned in lines 386-397?

W5 - It would be helpful to clarify the source of parsing errors. Are these issues arising from the agent's operations, or are they related to the environment? Additionally, there is a minor typographical error with a misplaced comma in line 449.

W6 - The paper lacks details on the specific prompts used for agents, and supplementary materials would facilitate the reproducibility of the experiments.

### Questions
Q1 - Could the authors elaborate on the unique challenge introduced by this benchmark? While it is clear that this work provides valuable references and novel attributes (e.g., evaluation metrics), a more explicit articulation of its key contributions would be helpful.

Q2 - Could the authors explain the rationale for the coarse-to-fine evaluation design? While this sounds helpful, I couldn't find a rationale for this design choice. Can the authors provide the reason for choosing this method? Also, what happens if the agent meets the second fine-grained part but misses the first coarse-grained part (or is it ensured that these cases don't usually occur)? A deeper insight into the reasoning and clarification behind these would offer a better understanding of the effectiveness of this approach.

Q3 - (Minor) For some experiments, English and Chinese languages are treated separately (e.g., human annotation in line 318). Could the authors clarify the motivation for this separation?

Q4 - In line 430, the term "shortcut" used by the M3A agent is somewhat ambiguous. Does this mean the agent generates a new action outside the predefined action space? If so, how is this interface managed within the environment? If not, clearer phrasing could avoid potential misunderstandings, such as stating, "The predefined action space includes combinations of actions that humans typically perform independently". 

Q5 - Could the authors confirm if the fine-tuned agents were trained specifically on the dataset proposed in this benchmark? If they were fine-tuned, what factors might explain their low success rates? If they were not, wouldn't it be fair to fine-tune them when comparing the algorithmic performance? Although it might not be necessary to fine-tune them in this benchmark specifically, noting how they are trained (e.g., whether they are trained in this benchmark or not) seems necessary to be noted to avoid misleading the readers.


I note that I am highly willing to raise the overall scores.

### Soundness
3

### Presentation
3

### Contribution
2
