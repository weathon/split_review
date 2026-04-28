# HDFlow: Enhancing LLM Complex Problem-Solving with Hybrid Thinking and Dynamic Workflows

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
Despite recent advancements in large language models (LLMs), their performance on complex reasoning problems requiring multi-step thinking and combining various skills is still limited. To address this, we propose a novel framework HDFlow for complex reasoning with LLMs that combines fast and slow thinking modes in an adaptive manner. Our approach consists of two key components: 1) a new approach for slow, deliberate reasoning called Dynamic Workflow, which automatically decomposes complex problems into more manageable sub-tasks and dynamically designs a workflow to assemble specialized LLM or symbolic reasoning tools to solve sub-tasks; 2) Hybrid Thinking, a general framework that dynamically combines fast and slow thinking based on problem complexity. 
Finally, we propose an easy-to-scale method for automatically synthesizing a large-scale dataset of 27K challenging reasoning problems for complex reasoning and a hybrid thinking tuning method that trains smaller LLMs on this dataset to internalize the fast/slow hybrid reasoning strategies.
Experiments on four reasoning benchmark datasets demonstrate that our slow thinking with dynamic workflows significantly outperforms Chain-of-Thought, and hybrid thinking achieves the highest accuracy while providing an effective balance between computational efficiency and performance. Fine-tuning using our hybrid thinking approach also significantly boosts the complex reasoning capabilities of open-source language models.}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a fast-slow thinking mechanism where the fast thinking is direct CoT and slow thinking is a dynamic workflow method. It also utilizes a dataset containing fast thinking process and slow thinking process to train a model to internalize the fast/slow thinking strategy.

### Strengths
1. strong performance improvement compared with direct CoT thinking

### Weaknesses
1. missing citation and discussion for System-1.x: Learning to Balance Fast and Slow Planning with Language Models, which also talks about the combination of fast thinking and slow thinking
2. This paper basically use cot as fast thinking and agentic planning as slow thinking. I feel like there's not much novelty here
3. missing baselines such as the method from System-1.x: Learning to Balance Fast and Slow Planning with Language Models

### Questions
N/A

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
This paper introduces a framework called HDFlow aimed at enhancing the complex reasoning abilities of LLMs. HDFlow combines fast & slow thinking modes in an adaptive manner to tackle problems that require multi-step reasoning and the integration of various skills. The framework is designed to automatically decompose complex problems into manageable sub-tasks and dynamically assemble specialized LLMs or symbolic reasoning tools to solve them, thereby improving both efficiency and accuracy in problem-solving.

### Strengths
## Strengths

1. The paper presents a new approach that facilitates deliberate, slow reasoning. (Compared to previous methods like CoT/PAL, ) this method automatically breaks down complex problems into smaller sub-tasks and designs a dynamic workflow to solve each sub-task using specialized LLMs or symbolic reasoning tools.
2. The proposed HDFlow is tested on 4 reasoning benchmark datasets. The Slow Thinking approach with Dynamic Workflow outperformed traditional CoT-like methods, achieving a notable average accuracy improvement.
3. Authors introduces an easy-to-scale method for automatically generating a large-scale dataset of ~27K reasoning problems. Using this dataset, they propose a hybrid thinking tuning approach to fine-tune smaller, open-source LLMs.

### Weaknesses
## Weakness

Major Concerns:

1. The whole framework seems like an engineering design, which incorporates adaptive modules and workflows to address some complex reasoning problems. It lacks the detailed technical contributions of a well-established research paper. I suggest the authors provide more explanations on the technical novelty. Specifically, the paper does not delve into the specifics of how the dynamic workflow is constructed, how the selection of specialized LLMs or symbolic reasoning tools is determined, and what the underlying algorithms are for adaptive module integration. The lack of a formal description of the core mechanisms makes it difficult to assess the true innovation of the proposed approach.
2. The authors claim that the framework is novel. However, there exist many previous works, combining fast and slow thinking to solve complex scenarios. Such as "SWIFTSAGE: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks" (it is just one of the examples). Could you please make a comparison with these previous baselines in the experiments? CoT baselines seem a little weak in 2024. The paper needs to demonstrate that HDFlow offers a unique advantage over existing methods, particularly those that also employ a fast and slow thinking paradigm. The absence of a comparative analysis against such baselines makes it hard to evaluate the true contribution of this work.

Minor concern:

1. CoT is considered to be fast thinking in this paper. It is quite different from the definitions in other works. Because CoT can also involve deliberate trial and error, or self-reflection. Could you provide some explanations on this point?

### Questions
I will read authors' rebuttal and discuss more about the paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents HDFlow, a novel framework designed to enhance complex reasoning in large language models (LLMs) by integrating fast and slow thinking modes. Inspired by dual process theory, HDFlow features two main components: Dynamic Workflow and Hybrid Thinking. Dynamic Workflow breaks down complex problems into sub-tasks, using specialized LLMs and symbolic tools to solve them. Hybrid Thinking adapts between fast and slow reasoning based on task complexity, improving efficiency and accuracy. The authors also developed a large-scale dataset of 27K challenging reasoning problems to train LLMs in these strategies. Experiments on four benchmark datasets show that HDFlow significantly outperforms existing methods like Chain-of-Thought, with Hybrid Thinking achieving the highest accuracy **on three out of four benchmarks**. This approach demonstrates the potential of combining dynamic workflows and hybrid thinking to advance LLMs' problem-solving capabilities.

### Strengths
- The paper is well-written, clearly conveying the core ideas and methodology.
- It presents a comprehensive process, covering theoretical framework, data synthesis, fine-tuning, and evaluation. This entire process provides strong evidence supporting the superiorty of HDFlow compared to existing methods.

### Weaknesses
 - In the "Reasoning Problem Synthesis" section, using GPT-4-Turbo with CoT to filter synthesized problems may limit the dataset's ability to enhance slow thinking, as all problems are solvable with GPT-4 + CoT?
- A contamination test is needed to ensure training data differs sufficiently from evaluation datasets. If the result is not promising, please decontaminate your training data.
- The claim that "hybrid thinking achieves the highest overall accuracy" is misleading, as it only tops three out of four benchmarks and does not have the highest average accuracy. This statement should be revised for precision.

### Questions
Minor comments:
1. The last sentence in the second paragraph of the introduction feels awkward.
2. The captions for Tables 1 and 3 mention a Fast/Slow ratio, which is not found in the Tables.
3. The last sentence of the first paragraph in sec 6.3 mentions an interesting finding. This could be further discussed for more insights.
4. There seems to be a contradiction in section 6.4 regarding the reliance on fast thinking, as the statement does not match the results in Figure 5.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces HDFlow, a framework designed to improve complex reasoning in large language models (LLMs) by adapting task-solving strategies from simple to more complex problems. According to the authors' ablation studies, the system achieved better results compared to the setting without the proposed modules.

### Strengths
**+1.** This paper introduces a reaonable method to enhance LLM reasoning.

**+2.** The experiments show that Hybrid Thinking outperforms Slow Thinking and original LLM baselines (COT).

**+3.** The paper is clearly written and easy to understand.

### Weaknesses
 **-1.** Although the concept of slow and fast thinking is fancy, the authors did not clearly define what constitutes slow and fast thinking. The proposed method fails to capture the full complexity of human cognition. I suggest either clarifying the related claims or reducing them if they do not strongly align with the method. Simply labeling quick responses as "fast thinking" and more detailed problem-solving as "slow thinking" seems to be an incorrect interpretation of the book [1].

Need more reasonable claims and demonstrations to support `To address these limitations, we propose a novel framework for complex reasoning with LLMs that combines fast (System I) and more analytical slow thinking (System II) adaptively, inspired by the dual-process theory of human cognition (Kahneman, 2017).`

**-2.** I suggest that the authors conduct a more careful and comprehensive literature review. Based on the reviewer's experience, several important and key references have been missed (published at least six months prior), such as [2], [3], and [4]. Additionally,  recent [5] provides a useful summary of  (many)  related similar work that the authors could refer to.

**-3.** I suggest adding more baselines beyond the self-produced ablations. The current experiments are weak and less convincing without at least two additional public-available baselines included.

### Questions
It would be appreciated if solve the questions mentioned in the weaknesses. Besides, there is a question about the workflow design:

**Additional**: Where are the graph-related illustrations used in this paper? It is suggested that this missing part be added.

### Soundness
3

### Presentation
3

### Contribution
3
