# LINA: An LLM-driven Neuro-Symbolic Approach for Faithful Logical Reasoning

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
Large Language Models (LLMs) have exhibited remarkable potential across a wide array of reasoning tasks, including logical reasoning. Although massive efforts have been made to empower the logical reasoning ability of LLMs via external logical symbolic solvers, crucial challenges of the poor generalization ability to questions with different features and inevitable question information loss of symbolic solver-driven approaches remain unresolved. To mitigate these issues, we introduce **LINA**, a LLM-driven neuro-symbolic approach for faithful logical reasoning. By enabling an LLM to autonomously perform the transition from propositional logic extraction to sophisticated logical reasoning, LINA not only bolsters the resilience of the reasoning process but also eliminates the dependency on external solvers. Additionally, through its adoption of a hypothetical-deductive reasoning paradigm, LINA effectively circumvents the expansive search space challenge that plagues traditional forward reasoning methods. Empirical evaluations demonstrate that LINA substantially outperforms both established propositional logic frameworks and conventional prompting techniques across a spectrum of five logical reasoning tasks. Specifically, LINA achieves an improvement of 24.34% over LINC on the FOLIO dataset, while also surpassing prompting strategies like CoT and CoT-SC by up to 24.02%. Our code is available at https://anonymous.4open.science/r/nshy-4148/.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose LINA, a framework that decomposes the reasoning steps for complex questions using four main components: (1) an LLM-based logic extractor, (2) an LLM-based query extractor, (3) an LLM-powered logic deducer, and (4) a core algorithm that integrates context and derived results to analyze the correctness of the underlying answers. They also provide theoretical analysis of LINA’s properties and complexity. Experimental results demonstrate that LINA significantly improves performance on benchmarks requiring multi-step reasoning, outperforming existing methods like Chain-of-Thought (CoT) by a substantial margin.

### Strengths
**Originality: 4/5**

A closely related work, SatLM, uses the Z3 solver as its logical reasoning backbone, whereas LINA leverages an LLM-prompt-based approach. While both frameworks share a similar conceptual foundation, LINA’s LLM-based reasoning backbone is more adaptable to loosely defined questions, enabling it to outperform the more rigid solver approach. This novel application of an LLM-driven deductive logic engine enhances generalizability.

**Quality: 3.5/5**

Pros: The authors provide both theoretical proofs on complexity and robust experimental results across multiple benchmarks. One question that arises is how well the LLM-powered deductive logic engine performs on standard logical deduction problems.

Cons: The reported accuracy for ReClorTeam (GPT-4-0613) on the ReClor leaderboard is 90.10, which is notably different from the numbers presented in this paper.

**Clarity: 3.5/5**

Pros: Figure 1 effectively clarifies the pipeline, and the appendix, which includes the actual prompts, further aids understanding.

Cons: Figure 2 is challenging to interpret without sufficient context, and it’s unclear why the Chain-of-Thought (CoT) approach does not explore additional steps.

**Significance**

This work is of the interest for both neural symbolic community and NLP community.

### Weaknesses
As shown in strength.

### Questions
1. How well the LLM-powered deductive logic engine performs on standard logical deduction problems.
2. The reported accuracy for ReClorTeam (GPT-4-0613) on the ReClor leaderboard is 90.10, which is notably different from the numbers presented in this paper. What may cause the difference?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces LINA, a neuro-symbolic approach designed to enhance the logical reasoning abilities of LLMs. LINA implements a hypothetical-deductive reasoning paradigm by enabling LLMs to autonomously manage logical reasoning without external solvers. It extracts propositional logic from natural language, and performs deductive logical reasoning. Empirical results show LINA outperforms existing methods, including LINC and other prompting techniques.

### Strengths
Improving LLM-based reasoning with neuro-symbolic integration is a good research problem. The writing is well-structured and clear. Empirical results are given with details. Code and data are provided for reproducibility.

### Weaknesses
The core concept of the proposed approach is an agentic framework equipped with formal logic, which is relatively common. The advantages of translating natural language into formal logic and using LLMs for reasoning remain ambiguous. The effectiveness of the agentic framework is influenced by the capabilities of base model and potential self-bias. The application scope of the method is limited.

### Questions
1) The authors propose an agentic framework that utilizes formal logic to enhance LLMs. Could a broader comparison with other relevant approaches (in addition to LINC) [1-4] be considered to provide a more comprehensive evaluation?


2) LLMs are generally stronger in processing natural language compared to formal logic. Could the authors clarify the advantages they see in converting logical reasoning tasks from natural language into Propositional or First-order Logic for LLM-based reasoning? If this conversion strategy offers benefits, might it be more effective to prompt LLMs with Chain-of-Thought reasoning including Propositional or First-order Logic?


3) The authors introduce an agentic framework for symbolic reasoning without an external solver. Could they explain the rationale behind this choice in more detail? If the concern is that formal logic generated by LLMs may be unreliable for external solvers, how does the proposed framework address this issue? Additionally, since the agentic approach relies on a sufficiently capable base model for sub-task management, would this framework extend well to smaller models (such as 7-8B parameters)?


4) Given that LLMs can struggle with self-bias [5], could the authors discuss any potential limitations in having the same LLM serve as both the deductive reasoner and supervisor/judge? Are there mechanisms in place to help mitigate self-bias and enhance the model's verification process?


5) One challenge with deduction using formal logic can be the restricted scope, especially if the required deduction rules are not explicitly included as known information. Could the authors share any strategies to address this challenge? Additionally, do they see any potential for extending this formal logic framework to reasoning tasks that require broader expressiveness, such as math reasoning, coding, and question answering?


Reference:

[1] Pan, Liangming, et al. "Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning." The 2023 Conference on Empirical Methods in Natural Language Processing.

[2] Yang, Sen, et al. "Neuro-symbolic integration brings causal and reliable reasoning proofs." arXiv preprint arXiv:2311.09802 (2023).

[3] Xu, Fangzhi, et al. "Symbol-LLM: Towards foundational symbol-centric interface for large language models." arXiv preprint arXiv:2311.09278 (2023).

[4] Xu, Jundong, et al. "Faithful Logical Reasoning via Symbolic Chain-of-Thought." arXiv preprint arXiv:2405.18357 (2024).

[5] Huang, Jie, et al. "Large Language Models Cannot Self-Correct Reasoning Yet." The Twelfth International Conference on Learning Representations, 2024.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a framework called LINA to address the generalization problem and information loss found in existing methods. The framework consists of two main components: an Information Extraction Module and a Symbolic Reasoning Module. First, the Information Extraction Module condenses and translates the reasoning question into a symbolic format. Then, the Symbolic Reasoning Module iteratively performs one-step deductive reasoning, utilizing both symbolic and natural language, with a judgment step to verify the correctness of each reasoning step. By leveraging GPT-3.5 and GPT-4o, the paper demonstrates that LINA outperforms the baselines across five datasets. Additionally, the paper includes comparisons to ToT and SatLM, along with an ablation study and a case study.

### Strengths
(1)	The framework claims to effectively address the issue of poor generalization to different question formats and the problem of information loss when using only symbolic language by combining symbolic and natural language.

(2)	The main experiment shows that the method surpasses the baselines across five datasets using GPT-3.5 and GPT-4o.

### Weaknesses
(1) The level of innovation in this work raises some concerns. To the best of my knowledge, some previous work (SymbCoT [3]), also addresses the issue of information loss by leveraging both natural language information and first-order logic (FOL). The key difference is that SymbCoT conducts reasoning and verification as a linear process, whereas this work transforms the process into an iterative one. In summary, it appears that this work mainly modifies the linear process from SymbCoT into an iterative framework, which limits its novelty. From my perspective, the primary innovation lies in this framework’s adaptability to a wide range of question formats, a feature the previous work lacks.

(2) The Information Extraction Module requires further clarification. How is the context classified? Additionally, how do you determine the "ease of translation"? Upon reviewing the context classification prompt provided in the appendix, it seems more focused on simplifying logical statements rather than classification. Please clarify if my understanding is incorrect.

(3) In Section 4.2, you explain that the context is first classified into lengthy text and non-lengthy text, with the lengthy text then being condensed into shorter sentences. These condensed texts are further classified based on their ease of translation. Further details are needed to understand this process. For example, how many classes are used in this step? Which classes will be translated, and which will not? This is important because the paper claims an advantage in using both symbolic and natural language, so it is crucial to understand what content is represented in symbolic language and what remains in natural language.

(4) The Reasoning Module lacks crucial details. Firstly, there is no explanation of how the deductive process works and how information LS, NL, and H interact to reach the reasoning conclusion C. Secondly, when performing the Check() operation, is it checking for errors in the reasoning process, or is it verifying whether the information contradicts or supports the hypothesis? Third, you mention that if an error occurs, the supervisor may adjust C or reset C = H. How is this step implemented exactly? This is not explained in the main text nor in Algorithm 1, and more details are needed to help readers understand how the reasoning module operates.

(5) The paper lacks a detailed analysis, which hinders the reader's understanding and the transparency of the framework. For example, the paper's main claim is that it addresses information loss and improves the framework's generalizability, but there is a lack of relevant analysis to support this claim. Besides, prior work in this stream (e.g., LINC [1], Logic-LM [2], SymbCoT [3]) typically includes an analysis of accuracy per necessary proof depth in ProofWriter. Including this type of analysis would be valuable, as it could demonstrate how robust your method is with respect to increasing reasoning complexity, a common challenge in real-world applications. Furthermore, the paper lacks an error analysis, which would provide a clearer understanding of where failures occur and improve confidence in the proposed framework.

(6) The analysis section also lacks some details. In Section 5.4, when you state that the LLM cannot generate effective z3 solver code or easily adapt for execution, does this mean that the rule-based solver completely fails to execute the problem, or can it execute but fail to reach the correct answer? Do you have quantitative data, such as execution rates, to back up this observation?

### Questions
(1) Why did you choose to use the train set of FOLIO while using the validation set for other datasets? Is there a specific reason for this decision? Most prior work (e.g., Logic-LM) typically evaluates the test set of FOLIO, so it would be helpful to clarify the rationale behind this choice.

(2) Could you provide more details about how the hypothesis is generated? Additionally, could you elaborate on how the Reasoning Process Judgment is integrated into the framework? It appears in Figure 1 but is not included in Algorithm 1, which causes some confusion. Providing more information on this would make the methodology easier to follow for readers.

(3) Do you have quantitative data to support your claim?

### Soundness
2

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
This paper proposes a pure prompt-based framework that solves reasoning problems, namely LINA. The framework first prompts LLM to convert problem into formal logic representation with natural language information; then it solves the problem as a deductive reasoning task by iteratively prompt the reasoner for deducing new facts and the supervisor for verification.

### Strengths
See below

### Weaknesses
## Novelty

The proposed method is a pure prompt-based framework with a straightforward design. The specific design of performing reasoning without using external tools has been studied in several prior works [1,2]. That said the novelty of this work is minor.


## Quality

The idea of "removing the tool usage yields better performance for deductive reasoning" is poorly motivated and justified

L48 "First, the process of converting logical problems into formal expressions leads to information loss"
- This is true for problems without FOL groundtruth, such as ReClor and LogiQA which are evaluated in the experiments.
- However, **these problems are not meant to be solved with the traditional formal logic method in the first place**, the prior work such as SatLM and LogicLM mostly focuses on solving the NLI task with datasets that come with groundtruth FOL annotations. Also note that ReClor and LogiQA contain not only deductive reasoning but also other reasoning tasks that cannot be characterized by FOL.
- That said, criticizing translation leads to information loss is fine, but it hardly motivates the approach proposed here if it is meant to solve problems that already fall outside of the formal logic bucket.

L78 "Second, the reliance on specific external tools results in poor generalization of these methods, limiting them to solving only certain types of problems, such as FOL propositional inference problems or satisfiability problems"
- This statement is problematic. Many works show tool usage increases rather than decreases the capability of LLMs in solving formal reasoning problems.
- Formal tools such as Prover9 and Z3 can be used for not only propositional logic but also first-order logic. And sat problem is a very generic problem setting where many reasoning problems can be converted into a sat problem, and being able to solve sat problem should be not considered as a disadvantage.
- That said, the authors should motivate their work properly.


Not every reasoning problem in ReClor and LogiQA can be formed into deductive reasoning:
- The authors propose to solve all reasoning problems with deductive reasoning. This is simply inappropriate for many of the problems in ReClor and LogiQA. For example, ReClor contains questions like "which of the following most challenges/supports/aligns with the argument in the context?" and "which of the following arguments shares the same reasoning pattern as that in the context", such questions do not fit into any formal logic categories and certainly cannot be solved with deductive reasoning.


The experiment setting misses many details and is potentially problematic:
- It's unclear how many ICL examples are used for GPT CoT baselines. However, an accuracy of 76 with GPT-4o on ReClor seems too bad to be true. As a comparison, [3] shows that with just a few ICL examples, GPT-3.5 can achieve about 60% accuracy and GPT-4 can achieve above 90% accuracy, which aligns much better with the scores reported in the public leaderboard.
- As mentioned above, including methods like LINC in ReClor and LogiQA benchmarks is not sensible, as these methods are designed for NLI task and not these benchmarks.


## Clarity

The paper is generally easy to follow.


## Significance

While I agree with the authors that moving beyond standard NLI tasks into more "in the wild" reasoning problems such as that in ReClor is an interesting and important direction, it cannot justify the pure prompt-based design, as it effectively rendering the approach into yet another fancy CoT method that could hallucinate during its reasoning. From a pure performance perspective, the significance of this work is still questionable as the results from the baseline approach are too bad to be true. That said, the significance is also minor.

### Questions
see above

### Soundness
1

### Presentation
2

### Contribution
1
