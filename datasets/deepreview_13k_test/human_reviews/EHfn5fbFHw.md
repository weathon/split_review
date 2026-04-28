# Context-Augmented Code Generation Using Programming Knowledge Graphs

- Decision: Reject
- Scores: 8, 3, 5, 5

## Abstract
Large Language Models (LLMs) and Code-LLMs (CLLMs) have significantly improved code generation, but, they frequently face difficulties when dealing with challenging and complex problems. Retrieval-Augmented Generation (RAG) addresses this issue by retrieving and integrating external knowledge at the inference time. However, retrieval models often fail to find most relevant context, and generation models, with limited context capacity, can hallucinate when given irrelevant data. We present a novel framework that leverages a Programming Knowledge Graph (PKG) to semantically represent and retrieve code. This approach enables fine-grained code retrieval by focusing on the most relevant segments while reducing irrelevant context through a tree-pruning technique. PKG is coupled with a re-ranking mechanism to  reduce even more hallucinations by selectively integrating non-RAG solutions. We propose two retrieval approaches—block-wise and function- wise—based on the PKG, optimizing context granularity. Evaluations on the HumanEval and MBPP benchmarks show our method improves pass@1 accuracy by up to 20\%, and outperforms state-of-the-art models by up to 34\% on MBPP. Our contributions include PKG-based retrieval, tree pruning to enhance retrieval precision, a re-ranking method for robust solution selection and a Fill-in-the- Middle (FIM) enhancer module for automatic code augmentation with relevant comments and docstrings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Problem statement: 
- Models fail on complex code generation tasks 
- RAG improves with external knowledge, but fails on relevant context 
- Irrelevant information causes hallucinations 

Solution: 
- PKG: semantically represent and retrieve code 
- Provides fine-grained code retrieval by focusing on the most relevant segments while reducing irrelevant context through a tree-pruning technique. 
- PKG is coupled with a re-ranking mechanism to reduce even more hallucinations by selectively integrating non-RAG solutions.  
- 2 retrieval approaches—block-wise and function-wise—based on the PKG, optimizing context granularity.

### Strengths
- PKG: semantically represent and retrieve code and provides fine-grained code retrieval by focusing on the most relevant segments while reducing irrelevant context through a tree-pruning technique.
- The results indicate the benefits of using PKG.
- The experiments are thorough, and the paper is well written.

### Weaknesses
- There still exists a gap between ideal ranker & re-ranker, what was the reason for it.
- How reliable is the result? Based on multiple generations with low temperatures 
- Samples in MBPP & HumanEval present with misaligned or incorrect NL, under which error is that catered to? 
- When block-PKG performs better than func-PKG then why is ranking done for considering func-PKG? 
- Need to show cases of extraction with PKG providing better function than current RAG.

### Questions
- Line 097 paragraph can be converted to bullets for better visual capture 
- Line 146 is while added to list of blocks 
- Correct invert commas in line 218, 221 ... 
- Section 2.2 RETRIEVAL FROM PKG (steps) should be formatted same as section 2.1 
- Fig 3 step 2: shouldnt the similarity be between encoded query and function nodes, rather than function nodes as shown in diagram 
- Appendix experiment that can be added: [optional]
    - Compare performance when an empty node is taken as a substitute for non-RAG option of input augmentation 
- Table 2 formatting needs to be corrected for column value alignment 
- Also format the table borders for Table 1 and 2 
- For all figures, increase font size, not readable 
- Table 3 visual impact can be improved by color incorporation to display increase or decrease of error with PKG incorporation 
- When block-PKG performs better than func-PKG then why is ranking done for considering func-PKG? 

Which are cases where func gives better results than block-PKG and why? 

Line 1029 mention using block PKG 

Line 1012 also provide example for with RAG what result came

### Soundness
4

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
The paper proposes to learn a programming knowledge graph from a predefined code QA dataset to augment code generation. The paper aims to retrieve proper code segments semantically and thus improve the performance.

### Strengths
+ The idea and the presentation are clear.
+ The method is demonstrated to be useful in the given setting, i.e., retrieve code segments from a given code QA dataset. It's a somewhat novel idea to learn code representation in a knowledge graph.

### Weaknesses
+ The setting is kind of weird to me: in real-world applications, code generation is usually augmented by code documents, natural language thoughts, or similar question-solution pairs, which is to say, natural language could be used to retrieve helpful information. Instead, only focusing on code representations may be limited.
+ Accordingly, in a not realistic setting, the experiments are not convincing enough to me. For example, on both HumanEval and MBPP, using BM25 for RAG consistently gets lower performance than no RAG. Also, with PKG the performance improves, it seems to be not a fair comparison.

### Questions
+ What's the advantage of PKG to normal RAG in an open retrieval setting?
+ Is `max_token=512` in the experiments enough?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel code generation framework that leverages a Programming Knowledge Graph for improved context retrieval, reducing irrelevant data with tree pruning and re-ranking techniques.
By implementing function- and block-level retrieval that provides fine-grained, contextually relevant code, the framework enables more precise and relevant context for code generation tasks, achieving significant performance gains on benchmarks like HumanEval and MBPP.

### Strengths
1. The PKG approach adds a structured layer to context retrieval, improving relevance in code generation.
2. Tree pruning and re-ranking help eliminate irrelevant information, enhancing the quality of generated code.
3. Through function- and block-level code, the framework could provide highly relevant and precise context.
4. The approach demonstrates considerable improvements on established benchmarks like HumanEval and MBPP.

### Weaknesses
1. Building and maintaining the Programming Knowledge Graph may be resource-intensive and require domain expertise.
2.The framework’s effectiveness may be constrained to specific programming languages (e.g. Python) of code tasks.
3.The paper could benefit from a deeper exploration where PKG and retrieval mechanisms fail to improve or potentially hinder code generation quality.

### Questions
1. What is the computational cost of building and updating the PKG, and how frequently does it need maintenance to remain effective?
2. How does the additional complexity introduced by tree pruning and re-ranking affect code generation performance, and is this overhead manageable?

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
3

### Summary
This paper presents a novel framework for enhancing code generation by integrating a Programming Knowledge Graph (PKG) with existing language models. By structuring code as a graph that captures hierarchical and semantic relationships, the framework supports granular retrieval, improving contextual relevance and reducing the inclusion of irrelevant information. The approach employs block-level and function-level retrieval strategies, coupled with a re-ranking mechanism, to increase generation accuracy and mitigate hallucinations induced by irrelevant context. Extensive evaluations on widely recognized benchmarks (HumanEval and MBPP) show that this PKG-based approach achieves notable improvements in pass@1 accuracy and reduces assertion errors, outperforming standard Retrieval-Augmented Generation (RAG) methods, especially when using tree pruning to eliminate extraneous context.

### Strengths
This work introduces an innovative use of knowledge graphs to represent programming knowledge, advancing the precision of semantic retrieval in code generation. By integrating hierarchical relationships within the PKG, this approach opens new avenues for enhancing retrieval-augmented models in the code generation domain.

Through evaluations on HumanEval and MBPP benchmarks, the method demonstrates improvements over existing RAG approaches, including NoRAG and other RAG methods. The error analysis and topic-based performance breakdown add credibility, highlighting specific problem types that benefit from the PKG-based approach.

### Weaknesses
The PKG generation and retrieval processes involve multiple modules and steps  that contribute to system complexity and potentially high computational cost. However, the paper does not delve into the scalability or efficiency implications of these processes. A discussion on computational trade-offs would provide a more complete assessment of its feasibility.

The re-ranking mechanism in the paper is used to enhance retrieval accuracy, but the decision-making process is not detailed enough. The author should provide a more comprehensive description and explanation of the method. 

Although PKG generally performs well, the paper lacks an in-depth analysis of specific categories (e.g., string manipulation and data structure tasks) where PKG retrieval does not yield improvements. A focused examination of these cases could reveal limitations inherent to graph-based retrieval for these types, thereby helping to identify conditions under which PKG may be less effective.

### Questions
See the weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
2
