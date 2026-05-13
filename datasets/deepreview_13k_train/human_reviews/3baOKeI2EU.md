# UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Chains of thought (CoTs) have achieved success in enhancing the reasoning capabilities of large language models (LLMs), while their effectiveness is predominantly observed in LLMs. 
    Existing solutions methods adopt distillation to inject chain-of-thought capabilities into small models (SLMs).
    However, they: 
    (1) can not guarantee the rationality of the generated explanation due to hallucinations; 
    (2) ignore diverse structures of CoT during knowledge transfer.
    In this paper, we propose a unified CoT distillation framework termed UniCoTT for considering diverse structural CoTs (\emph{i.e.}, chain, tree, and graph).
    UniCoTT contains two core strategies: iterative construction for structured CoTs and the structural constraint strategy.
    Specifically, UniCoTT prompts LLMs to iteratively produce accurate explanations with answers and unifies structured explanations as UniCoT which is seen as a bridge for knowledge transfer.
    Furthermore, UniCoTT utilizes the proposed unified supervised learning and structural consistency learning strategies to transfer knowledge of structured CoT to SLMs. 
    Experimental results show that UniCoTT can significantly improve the performance of SLMs on multiple datasets across different NLP tasks. **Our code is available in our supplementary materials.**

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focuses on distilling the reasoning capability, specifically chain-of-thought reasoning, from large language models into smaller models. Specifically, the paper uses prompts to guide a larger teacher model to generate multiple explanations, or "thoughts," for given questions and answers. These explanations are represented in a graph structure. Then, the small student model is trained using traditional cross-entropy loss along with a novel structural consistency loss and supervised contrastive loss proposed by the authors.

### Strengths
- The writing is clear and easy to follow, with a well-defined motivation for the research.
- The distillation framework proposed is innovative, especially in using a graph structure to represent different chains of thought and introducing corresponding training methods.
- The approach is extensively tested on multiple benchmark datasets, demonstrating strong empirical performance.

### Weaknesses
 - The framework mainly focuses on distilling explanation and reasoning abilities into base models like BERT. A concern is the limited application scope of such encoder-based models. To further validate the effectiveness of the proposed distillation framework for reasoning abilities, it would be interesting to distill the chain-of-thought reasoning from larger models into smaller decoder-based models and test them on complex reasoning tasks.

### Questions
- Why focus on using an encoder as the student model?

### Soundness
3

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
The paper presents a novel framework for transferring the reasoning capabilities of large language models (LLMs) to small language models (SLMs) through a structured chain-of-thought (CoT) distillation approach. The authors propose UniCoTT, which considers diverse structural CoTs (chain, tree, and graph) and employs two core strategies: iterative construction for structured CoTs and a structural constraint strategy. The framework aims to address the challenges of ensuring the rationality of generated explanations and ignoring diverse structures of CoT during knowledge transfer. The experimental results demonstrate significant performance improvements of SLMs on multiple NLP tasks across various datasets.

### Strengths
1. The paper introduces a unified framework that handles diverse structural CoTs, which is a significant advancement over existing methods that focus solely on chain structures.
2. The authors provide extensive experimental evidence to support the effectiveness of UniCoTT, showing improvements across different NLP tasks and datasets.
3. The consideration of structured reasoning pathways (tree and graph) in addition to chains is a strength, as it better captures the complexity of human reasoning processes.

### Weaknesses
1. The paper could benefit from a discussion on the computational complexity of UniCoTT and its scalability, especially when dealing with very large datasets or more complex reasoning tasks. Specifically, the paper lacks a detailed analysis of how the iterative construction of structured CoTs impacts training time and resource consumption, particularly for large-scale datasets. Furthermore, the scalability of the method with respect to the complexity of the reasoning tasks is not sufficiently addressed. For instance, how does the method perform when the reasoning requires multiple steps or involves a large number of interconnected concepts?
2. The construction of UniCoT relies on APIs of LLMs, which may not be accessible or feasible in all situations. The paper could address potential alternatives or mitigation strategies. The reliance on external LLM APIs introduces a practical limitation, as access to these APIs may be restricted or costly. The paper should explore alternative methods for generating the structured CoTs, such as using smaller, open-source models or developing a more efficient, in-house approach. Besides, SLMs usually refer to small language models, e.g., 2B and 3B. The authors mainly conducted experiments on BERT and RoBERTa, which were not convincing enough.
3. While the results are promising, the paper primarily focuses on question-answering and NLU tasks. It would be beneficial to see how UniCoTT generalizes to other types of tasks. The evaluation is limited to a narrow range of tasks, and the paper does not provide sufficient evidence to demonstrate the general applicability of the proposed framework. It is unclear whether the method would perform well on tasks such as text summarization, machine translation, or code generation, which involve different types of reasoning and knowledge transfer.

### Questions
1. How does the performance of UniCoTT scale with the size and complexity of the knowledge to be transferred? Are there diminishing returns as the complexity increases?
2. What are the limitations of the current implementation of UniCoTT, and how might these be addressed in future work?

### Soundness
3

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
4

### Summary
This paper proposes UniCoTT, a unified distillation framework to transfer the diverse reasoning structures with CoT to smaller language models such as BERT and RoBERTa. Firstly, UniCoT is proposed as a unified bridge of various CoT structures, which is constructed by iteratively prompting LLMs to produce explanations with correct answers. After that, a node-level supervised contrastive loss and a structural consistency loss are designed as part of the training objective. Experiments on multiple reasoning datasets verified the effectiveness of UniCoTT by surpassing the baseline methods by a large margin.

### Strengths
1. The proposed method is technically sound and intuitively makes sense. It is very interesting to transfer the knowledge from structured CoT texts into smaller models that can leverage rationale knowledge in a unified manner.
2. Experimental results on several benchmarks show some improvement upon baselines and the authors conduct extensive ablation studies and analyses on various design choices.
3. The paper itself is generally well-written.

### Weaknesses
1. The generalizability of KNIFE is yet to be known. The proposed framework is only verified in multiple-choice datasets. Whether it could be extended to other task settings like text generation remains a concern. Specifically, the reliance on a structured, node-based representation of reasoning may not translate well to tasks where the output is not a discrete choice but rather a sequence of text. The method's effectiveness in tasks requiring more nuanced or creative text generation, such as summarization or dialogue, is unclear. Furthermore, the structural consistency loss, which is central to the approach, might not be directly applicable to tasks where the notion of a 'correct' reasoning structure is less well-defined.
2. The process of iteratively constructing UniCoT is hard to understand from the main body of the current version. I would suggest the authors move some content from the appendix to the main body. Meanwhile, it would be helpful if the authors could provide some overall statistics on the constructed UniCoT. For example, the averaged nodes and edges of the structure. Without a clear understanding of the iterative construction process, it is difficult to assess the robustness of the generated structures and the potential for bias or instability in the distillation process. The lack of statistics on the average size and complexity of the generated graphs makes it hard to evaluate the computational overhead and the scalability of the approach.

### Questions
1. The authors list "hallucinations" as one of the major drawbacks of previous works, and motivate the design of UniCoTT in ``introduction'' section. I am wondering how the designed UniCoTT framework helps to alleviate this issue.
2. In lines 385-386, why $\alpha$ and $\beta$ is set to 0.5 and 0.2 respectively? Is it an intuitive trial or a result of a grid search?
3. It would be interesting to test the annotation efficiency of CoT with the teacher model. An empirical conclusion of how many annotations are enough for great distillation performance would be insightful.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper  introduces UniCoTT, a teacher-student framework aimed at transferring complex reasoning abilities from large language models (LLMs) to smaller language models (SLMs). UniCoTT extends traditional chain-of-thought (CoT) reasoning by leveraging diverse structured reasoning paths, such as chains, trees, and graphs, within a unified distillation process. This approach involves iterative CoT construction, node-level supervised contrastive learning, and structural consistency learning to reinforce reasoning capabilities in SLMs. Experimental results on factual reasoning, multiple-choice QA, and natural language understanding tasks demonstrate that UniCoTT outperforms existing methods, enhancing SLM performance across several benchmarks.

### Strengths
- Extends CoT reasoning with diverse structures, which broadens the reasoning capabilities of SLMs.
- Implements structural consistency and contrastive learning, effectively aligning SLMs with complex CoT reasoning paths.
- Demonstrates superior performance on multiple tasks, showing effectiveness and generality in knowledge transfer.

### Weaknesses
UniCoTT’s increased complexity and computational requirements could make real-world deployment challenging. To be fair, as distillation strategy proposed in this paper uses three types of reasoning and more compute to create dense supervision. The baselines like CoT may also uses more compute like more chains in self-consistency to increase the quality of distillation data.

### Questions
No

### Soundness
3

### Presentation
3

### Contribution
3
