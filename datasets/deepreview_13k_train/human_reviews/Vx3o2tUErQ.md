# REPANA: Reasoning Path Navigated Program Induction for Universally Reasoning over Heterogeneous Knowledge Bases

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Program induction is a typical approach that helps Large Language Models (LLMs) in complex knowledge-intensive question answering over knowledge bases (KBs) to alleviate the hallucination of LLMs. However, the accurate program induction usually requires a large number of high-quality parallel data of a specific KB, which is difficult to acquire for many low-resource KBs. Additionally, due to heterogeneity of questions and KB schemas, the transferability of a model trained on a single dataset is poor. To this end, we propose REPANA, a reasoning path navigated program induction framework that enables LLMs to reason over heterogeneous KBs. We decouple the program generation capability into perceiving the KB and mapping questions to program sketches. Accordingly, our framework consists of two main components. The first is an LLM-based navigator, which retrieves reasoning paths of the input question from the given KB. The second is a KB-agnostic parser trained on data from multiple heterogeneous datasets, taking the navigator's retrieved paths and the question as input and generating the corresponding program. Experiments show that REPANA exhibits strong generalization and transferability. It can directly perform inference on datasets not seen during training, outperforming other SoTA low-resource methods and even approaching the performance of supervised methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces REPANA, a program induction framework designed to improve reasoning over heterogeneous knowledge bases (KBs) by leveraging a structured, two-part framework. REPANA separates the process of knowledge base schema perception from question-to-program mapping to improve Large Language Model (LLM) performance in low-resource KBs. It integrates two core components: a KB navigator, which retrieves reasoning paths, and a KB-agnostic parser that generates program sketches, allowing models to generalize across various KBs without extensive training on each. REPANA demonstrates superior generalization by performing well on unseen datasets, even approaching supervised methods in certain metrics.

### Strengths
- Decouples KB schema perception from program generation, allowing for greater transferability across different KBs.
- Performs effectively without large annotated datasets, alleviating the need for extensive manual annotations.
- Adaptable to varying KB structures, making it effective across diverse datasets with minimal retraining.

### Weaknesses
 - Relies on topic entities for effective path retrieval, which limits performance in questions lacking clear topic entities.
- Accuracy declines with longer reasoning paths or multi-hop questions.
- It can hardly handle complex questions since the framework mainly focuses on exploring single reasoning chains.
- This method may be time costly since it utilizes LLMs multiple times in every search step.
- What is the relation of this work and other KBQA work which conducts pruning then answering (please list one such representative work as well if possible)?

### Questions
- How does REPANA handle questions without clear root entities effectively in various KBs?
- Why do you use the dev set to test your model in Table 2? Although you claim that questions during testing do not overlap with the training set, it is fairer to compare the performance of the same test set.
- Have you tried directly performing relation and entity filtering on ChatGPT instead of on tuned small Llama models?
- What is the performance of LLMs, like ChatGPT4 and Llama3-70b, on the datasets in Table 1 with few-shot demonstrations?
- The majority of MetaQA results in Table 1 are over 90, and half of the results are over 95. The dataset may not validate for differencing model performance.
- The format of Figure 3 looks weird.
- Appendix A should be removed.
- what is the cost of additional instruction tuning and what is the size of the dataset (did you mention this in the paper)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces REPANA, a framework for reasoning path navigated program induction that enables Large Language Models (LLMs) to reason over heterogeneous knowledge bases (KBs) with low-resource data. REPANA deals with the challenges of program induction. Usually, this requires a large amount of high-quality parallel data for a particular KB. It also addresses the poor transferability of models trained on single datasets because of the heterogeneity of question and KB schema. The experiments demonstrate that REPANA has strong generalization and transferability, outperforming other state-of-the-art low-resource methods and approaching the performance of supervised methods.

### Strengths
-	The proposed REPANA decouples the program generation capability into perceiving the KB and mapping questions to program sketches, which is an effective way.
-	REPANA exhibits strong transferability and generalization capabilities. This is an advantage for low-resource KBs where annotated data is scarce.

### Weaknesses
-	REPANA 's performance is affected by the lack of topic entities in the question, which can limit its effectiveness in scenarios where the question does not provide a clear starting point for reasoning.
-	REPANA's path navigation is prone to errors in questions with longer inference chains. 
-	Although REPANA aims to alleviate the need for high-quality parallel data, it still relies on some amount of annotated data from rich-resource KBs.

### Questions
1.	How does REPANA handle questions that involve ambiguous or multiple root entities, and what is the impact on the accuracy of the retrieved reasoning paths?

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
2

### Summary
This paper addresses the problem of answering queries using a knowledge base (KB). The paper proposes a system in which a LM is conditioned on the given
query and generates a reasoning path through the KB. Then the answer to the query can be obtained by executing the path on the KB. The system consists of two
parts: a navigator and a KB-agnostic parser, both of which are based on LMs. The navigator proposes a reasoning path based on the question, and the parser takes
as input the question and proposed reasoning path and outputs a final program. The parser is KB-agnostic because it is trained across a variety of KBs and can
be applied to a new KB without extra training. Compared to other methods that do not train on the target KB, the proposed method obtains better F1. An ablation
shows that the reasoning path input to the parser is a crucial part of the system when evaluated on unseen KBs.

### Strengths
- The paper proposes a method for the knowledge-base reasoning problem
- The results of the proposed method are better than those of other "low-resource" methods
- Table 4 shows the results of an ablation indicating that the reasoning path is crucial for good performance on unseen KBs.

### Weaknesses
The writing has many shortcomings:
- The method section is somewhat unclear to me. For example, is the process in 4.1.2 used only for inference, or is it used somehow in training or to create the training data? Specifically, the paper does not clearly articulate how the reasoning paths are generated for training examples, and whether this process is the same as the one used during inference. This lack of clarity makes it difficult to assess the validity of the training procedure and the overall reproducibility of the method.
- Continuning on the previous point, what is the difference between a "reasoning path" (ostensibly the output of the navigator) and a "program" (ostensibly the
  output of the parser)? The paper needs to provide a more precise definition of both concepts, including the specific data structures used to represent them and the formal language in which the program is expressed. Without this level of detail, it is hard to understand the exact role of each component in the system and how they interact.
- Line 54 says that a shortcoming of agent methods is that they require a "topic entity" to occur in the question, but from line 256 ("We use the topic entities of the input question"), it seems REPANA has the same weakness. This inconsistency undermines the paper's claims about the novelty of the approach. The paper should acknowledge this limitation and discuss how it might be addressed in future work.
- There are many typos / grammatical errors (please see the "Questions" section for some examples)

### Questions
Typos: 
- line 50: "still rely" -> "still relies"
- line 104: "Through of this naval" -> "Through this novel"
- line 108: "fist train" -> "first train"
- line 260: "rooot" -> "root"
- line 321: "can significantly improves" -> "can significantly improve"
- line 323: "model sometimes generate" -> "model sometimes generates"
- line 339: "almost all schema items .. are unseen" - can you quantify this?
- Table 2: why is REPANA's result marked as dev set while all others are not?
- Table 3: grailqa is mentioned but not included in the table

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposed a new approach for KB based reasoning task. The approach consists two steps: 1) KB navigator to collect relevant paths (schema information) from KB. 2) A KB-agnostic parser to generate the program. The KB navigator leverages the underlying KB to localize the corresponding reasoning paths using the walk-search process. The parser is trained using LoRA and is focusing on learning sketches of the output program. The parser is trained with multiple heterogeneous datasets to maximize the generalization across different KB databases. The paper shows decent performance boost on unseen low-resource databases such as GrailQA, WebQSP, ComplexWQ coming with existing methods. In the ablation studies, it further validates the effectiveness of the proposed KB-walk retrieving strategy and mixed instruction training for low-resource scenarios.

### Strengths
1. The paper presents a framework for KB based reasoning task. It tackles one of the challenges with KB QA that different knowledge graph has different schema for program induction. The authors set up complicated KB pipeline to investigate how to improve the generalization capability of such system.
2. Evaluation is comprehensive. The authors includes many of the previous work and conduct thorough experiments to demonstrated that the proposed approach helps on low-resources settings. Ablation studies seems solid. The performance boost is decent comparing with other approaches. 
3. Although there are some grammatical issues in the writing, the paper in general is easy to follow and well-structured.

### Weaknesses
1. It would be great if the authors could pay more attention to the writing. Here are some grammatical issues: 
 - Line 108, fist -> first
- Line 228, leverage -> leverages
- Line 289, Over fitting -> overfitting
- Line 323, generate -> generates
- Line 114, missing on at the end of the line
- Line 437, introducing -> introduced
2. For the KB parser, the proposed approach leverages a rephrasing approach to make output program heterogenous, but fails to mention how to recover the entities and relations at inference time. Would that be possible to shed light on how this is done?
3. The proposed method involves an iterative way to extract a subgraph of a KB and LoRA finetune an LLM to generate a homogenous output program. Given that there are already some research works on unifying the output program (e.g. [1] here), I fail to see the main contribution from the proposed approach.

### Questions
1. Because the parser training masks the KB specific relations, how do we recover such relations at inference time? For instance, in Line `the relation “Highest poing"` (is it a typo here?) will be rephrased to "peak elevation", how do we map it back at inference time? Have you conducted any experiments to check the accuracy of such mapping?

### Soundness
3

### Presentation
3

### Contribution
2
