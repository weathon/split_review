# Benchmarking and Enhancing Large Language Models for Biological Pathway Reasoning

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Large language models (LLMs) have demonstrated remarkable performance across various domains of biology, but their ability to reason about biological pathways remains underexplored. This includes reasoning about how perturbations in biological systems lead to various downstream effects through complex intermediate processes. Such reasoning is crucial for explaining and predicting biological phenomena, as well as for formulating hypotheses and designing experiments.

In this study, we investigate whether LLMs can effectively understand and reason about biological pathways by introducing BioMaze, a comprehensive benchmark focusing on reasoning about the effects and mechanisms of natural and synthetic interventions—such as mutations, infections, or treatments—on various downstream targets under different conditions through complex intermediate pathway processes. BioMaze spans multiple biological domains and is categorized along three reasoning dimensions, capturing various aspects of pathway reasoning.

We evaluate LLMs using the BioMaze benchmark with reasoning methods like Chain-of-Thought (CoT) and pathway graph-augmented approaches. Results show that while LLMs can understand mechanisms in natural organisms, they struggle with predicting phenomena after perturbations, highlighting their limitations in reasoning about biological pathways. To address these challenges, we propose PathSeeker, a novel LLM agent that interactively reasons through subgraph-based navigation within the pathway graph. This approach enhances LLMs' reasoning in biological pathways by leveraging pathway graph augmentation, particularly in cases involving perturbations, potentially bridging the gap between LLMs' current capabilities and the complexities of biological systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses a gap in LLMs to reason biological pathways, especially with complex perturbations, interventions, and varying conditions. To address this gap, the authors first introduce a new benchmark, BioMaze, that contains 1.3k high-quality questions for biological pathways reasoning.

Next, the paper evaluates LLMs on BioMaze with existing reasoning methods and finds that they struggle with perturbations. Then the authors propose a new reasoning approach, PathSeeker, that reasons through subgraph-based navigation within pathway graph. PathSeeker achieves better performance in biological reasoning.

### Strengths
1. Clear identification of research gap: I think it is an interesting question whether LLMs can reason on biological pathways, and how well they do it. The authors have identified the limitations here clearly.

2. Innovative benchmark: BioMaze is a valuable contribution to the field, providing a systematic evaluation framework for assessing LLM performance across various dimensions of biological pathway reasoning.

### Weaknesses
1. Data presentation is not very clear. For example, when the paper evaluates the performance of different models and reasoning methods, it simply writes "performance" without defining the metrics. Therefore, it is not clear whether a higher number means a better performance. In Table 2 and 3, the authors underline the lowest results, which is confusing.

2. Baseline choice is not clear. The paper uses CoT as a baseline in 5.3.1 Task Analysis. I think a better baseline may be a method with pathway graph augmentation since PathSeeker also uses pathway graph augmentation.

3. Analysis is not thorough enough. If the authors want to claim that PathSeeker reduces the performance gap between natural and intervened/perturbed groups, then they should provide more evidence and analysis on them.

### Questions
1. In Figure 4, how are the lines fitted? For the right figure (open-ended questions), the gap between CoT and PathSeeker is very small. What is the standard deviation?

2. In Table 2, Table 3, Table 6, and Figure 5, please add what metrics and units are used. Also add evaluation method in Experiment section.

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
5

### Summary
This paper introduces a benchmark to evaluate LLMs' reasoning abilities about biological pathways including perturbed pathways. The benchmark is diverse and covers different biological domains and scenarios.

The authors' evaluations show that while LLMs understand natural mechanisms well, they struggle with intervention scenarios

The authors propose PATHSEEKER, an LLM agent that navigates pathway graphs using subgraph-based exploration. This approach improves reasoning accuracy, including accuracy for intervention scenarios.

Key contributions:

* BioMaze Benchmark
* Evaluation of LLMs on benchmark
* PATHSEEKER Agent, analysis of its performance on benchmark, its failure modes, and ablation study

### Strengths
* The benchmark is a solid contribution. The authors did good work in breaking down the benchmark by various categories.
* PATHSEEKER has promise, though I wish it were better motivated and contextualized within related work within systems biology as well as graph reasoning tasks with LLMs as well as graph-based RAG techniques.
* The breakdown of failure modes for LLM reasoning over pathways, particularly in terms of causality, and showing how the graph augmentation helps is useful. Breaking down the reasons for failure with human validation is also a useful contribution and I wish I saw more of that.

### Weaknesses
* With PATHSEEKER, I think there is a lack of motivation for explore the pathways via subgraphs other than "Inspired by how humans browse web networks". I don't disagree with this approach per se, but I don't think the authors motivate doing it this way as opposed to, say for example, adding including the whole graph or a big chunk of it into the prompt template. Indeed, as an experiment I pasted an XML file of a MAPK KEGG map into GPT-4's context window and it fits. And if something doesn't fit, context windows will get bigger. I think the authors should motivate the local approach, for example, by citing work that demonstrates failure modes for graph-based reasoning with LLMs, and citing work that shows how local approaches do better. 
* I find it concerning that the authors did not include results for a cutting edge model like GPT-4, Claude, PALM 2 and limited tests to GPT-3.5 and Llama-3 8b, neither of which were fined-tuned for performance in this domain. The gap between GPT-3.5 and GPT-4, as an example, on general medical QA performance is quite large. This makes me worry the benchmark might be already saturating on more advanced models. Budget could have been an issue, but could have fine-tuned GPT-3.5 (perhaps on hold-out data from their benchmark), or they could have used their instance of LLaMa-3.1-405B to answer questions as well as evaluate them. Similarly, they could have used other fine-tuned open source models to evaluate.

### Questions
"We then apply multiple data filters and validation steps to ensure the correctness, quality, and relevance
to biological pathways. The correctness of each question is validated by checking whether LLMs
can answer it accurately using the original paper content, allowing us to exclude question-label pairs
with errors. Question quality is ensured through several filters, removing questions that are poorly
defined, unpredictable (e.g., asking for specific measurement values), query more than one fact, are
trivial with answers revealed in the question’s context, or are unrelated to biological pathways. After
all the filters, BioMaze contains 1.3k high-quality questions for biological pathways reasoning"
Can you give me more confidence that these questions all have a single right answer that can be answered from the context? To what degree are the manually verified? Filters are great, but where does the buck stop? 

A pathway is essentially a knowledgebase. It would be good to connect this work to recent approaches that use knowledgebase graph structure in RAG, such as GraphRAG. Indeed, generally speaking, contextualization within prior work could be stronger.

Biggest question: Why did you not run eval on cutting-edge larger models or larger open-source models like your LLaMa-3.1-405B, or fine-tuned SLMs. Bit sus. Willing to upgrade review if this concern is addressed.

### Soundness
4

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
1

### Summary
This paper introduces BioMaze, a large-scale benchmark for evaluating large language models' ability to reason about biological pathways. The authors also introduced PATHSEEKER, a new approach to enhance LLMs' performance on these tasks.
They found that while LLMs can understand basic biological mechanisms but LLMs struggle when asked to reason about perturbations or interventions in biological systems. 
Through their experiments, they observed that LLMs perform worse on perturbed systems compared to normal conditions.

### Strengths
1. The study is very comprehensive. I like the rigorous experimental design that systematically evaluates different aspects of pathway reasoning.
2. It contributed to the field of BIOLOGICAL PATHWAY REASONING by making benchmarks and the problem formulation combining biological pathway reasoning with LLM capabilities.
3. I also found myself enjoy reading the paper and like the well-structured presentation progressing logically from problem motivation to solution.

### Weaknesses
1. The author presents error categorization but it doesn't provide detailed analysis of when and why particular types of errors occur. If the authors can provide more analysis of the occurance, it would be nice.
2. The validation of ground truth answers relies heavily on LLMs themselves (LLaMA 3.1-405B and GPT-4). This circular dependency could reinforce existing model biases.

### Questions
1. Maybe the author can try to answer the reason why particular types of errors occur in categorization.
2. May using other models to do ground truth answers validation.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study explores the under-examined ability of LLMs to reason about biological pathways, particularly focusing on how system perturbations affect downstream biological processes. The authors introduce the BioMaze dataset, a benchmark designed to assess LLMs’ reasoning on how various interventions, like mutations, infections, or treatments, impact downstream targets through complex pathway mechanisms across different biological contexts. With this dataset, the authors then test LLMs with reasoning techniques such as Chain-of-Thought (CoT) and graph-augmented methods, and they find that while LLMs can understand basic biological mechanisms, they struggle with predicting effects after perturbations. To enhance the reasoning ability of LLMs, the authors also developed PathSeeker. In this novel approach, the LLM agent navigates pathway subgraphs to improve performance in pathway reasoning, particularly in scenarios with biological perturbations.

### Strengths
1. BioMaze benchmark for biological pathway reasoning: The authors present BioMaze, a benchmark dataset designed to evaluate LLMs’ reasoning abilities within a biological context. BioMaze focuses on assessing how well LLMs comprehend and reason about complex biological pathway phenomena, including cause-effect relationships in natural and perturbed conditions. Curated from the literature, this dataset includes high-quality questions and answers generated with Llama 3.1405B and GPT-4. Covering multiple biology subfields, BioMaze undergoes extensive filtering and validation to ensure relevance, accuracy, and diversity of pathway scenarios.
2. Pathway graph augmentation via PATHSEEKER agent model: Given that biological pathways are naturally structured as networks, the authors incorporate pathway graph data to improve LLM reasoning. They introduce PATHSEEKER, a novel graph-augmented agent that navigates pathway subgraphs to enrich LLM understanding and support reasoning in complex pathway contexts. This approach allows LLMs to access and utilize structural information essential for nuanced pathway reasoning, particularly in scenarios involving biological interventions.
3. Comprehensive evaluation and analysis: The paper conducts a thorough evaluation across multiple LLM models and experimental settings, systematically analyzing LLM performance with and without pathway graph augmentation. Additionally, the ablation study of PATHSEEKER explores its effectiveness by examining API usage, step distribution, and performance impact. These analyses further strengthen the value of pathway augmentation, validating the importance of PATHSEEKER in enhancing LLMs’ reasoning capabilities in biological pathway contexts.

### Weaknesses
1. Limited evaluation method for open-ended questions: outputs from different LLMs are evaluated by another LLM, specifically using the Llama 3.1 405B model, which is considerably powerful but would be costly to replicate the results. It would be more helpful if the authors could consider some alternatives, such as using rule-based keyword-matching or for example, using ROUGE score or embedding-based summarization methods to compare how similar or dissimilar answers from LLMs are to the ground truth answers. Another alternative could be to construct different evaluation methods based on the failure modes discovered later from the error analysis study. 
2. see questions

### Questions
1. Pathway graph limitations: This paper highlights that faulty reasoning persists even with pathway augmentation, especially with perturbations. Could the authors provide more insight into potential sources of error in the pathway graph data? Is it the case that some specific cases or graph structures are more challenging for the LLM to navigate, and some are easier for LLMs to handle?
2. Handling multi-step reasoning decline: Given that CoT reasoning shows decreased accuracy with increased steps, have the authors considered alternative strategies or mechanisms, such as hierarchical reasoning, to mitigate this drop in performance, or are those questions just naturally challenging? 
3. Error analysis: The error analysis indicates that omissions remain an issue with PATHSEEKER. What approaches might the authors consider to address these issues, especially when key pathway branches are missed? Could further database expansion, enhanced subgraph search criteria, or developing a different graph search algorithm improve the performance?
4. Using RAG: would authors consider incorporating RAG into this framework given the graph structure of biological pathways? Specifically, RAG could allow the model to retrieve specific or relevant information from related literature or pathway databases. This retrieval would provide the LLM with dynamic access to more detailed and more recent biological knowledge, instead of the graph structure constructed from a fixed database KEGG, as currently used in the paper. 
5. Evaluator setting in this paper: this paper proposes using the llama 405B model as the evaluator model for LLM's outputs, as this is costly to run multiple times, would authors consider any alternative evaluation approaches such as applying rule-based methods or using alternative LLMs to strengthen the statistical validity of the benchmarking results?

### Soundness
3

### Presentation
3

### Contribution
3
