# KnowTrace: Explicit Knowledge Tracing for Structured Retrieval-Augmented Generation

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Recent advances in retrieval-augmented generation (RAG) furnish large language models (LLMs) with iterative retrievals of relevant information to strengthen their capabilities in addressing complex multi-hop questions. However, these methods typically accumulate the retrieved natural language text into LLM prompts, imposing an increasing burden on the LLM to grasp the underlying knowledge structure for high-quality multi-step reasoning. Despite a few attempts to reduce this burden by restructuring all retrieved passages or even entire external corpora, these efforts are afflicted with significant restructuring overhead and potential knowledge loss. To tackle this challenge, we introduce a new structured paradigm (KnowTrace) from the perspective of explicit knowledge tracing, which treats LLM as an agent to progressively acquire desired knowledge triplets during iterative retrievals and ultimately trace out a specific knowledge graph conditioned on the input question. This paradigm clearly unveils the logical relationships behind the unstructured text and thus can directly facilitate LLM’s inference. Notably, it also naturally inspires a reflective mechanism of knowledge backtracing to identify supportive evidence and filter out useless retrievals in the correct trajectories, thus offering an effective way to stimulate LLM’s self-taught finetuning. Extensive experiments demonstrate the superiority of our paradigm over three standard multi-hop question answering benchmarks. Our code is available at https://github.com/xxrep/SRAG.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on incorporating structured knowledge (i.e., relational triplets of (subject, relation, object)) in iterative retrieval-augmented generation (RAG) to guide retrievals and facilitate multi-hop reasoning. For each question, a specific knowledge graph (KG) is progressively constructed from the retrieved documents across multiple retrieval iterations until a final answer can be derived. The authors also introduce a reflective mechanism called knowledge backtracking, which identifies the correct trajectories in the KG that lead to correct answers and fine-tunes the LLM to better construct the KG based on these trajectories. Experiments show that the proposed method outperforms selected baseline methods on three multi-hop QA tasks.

### Strengths
- Constructing knowledge graphs (KGs) from retrieved documents to guide multi-hop reasoning in RAG is an interesting idea.
- The knowledge backtracking mechanism provides an explicit way to train the LLM to learn intermediate reasoning steps (i.e., KG trajectories) before reaching the final answer.
- Experiments show that the proposed method outperforms baseline methods on three multi-hop QA benchmarks (although evaluated on a small subset of test samples).

### Weaknesses
 - Potentially limited practical value. My major concern is about the inference efficiency of the RAG system, as the proposed method requires constructing a knowledge graph (KG) for each question through iterative retrievals, which seems time-consuming. For example, with K = 5 documents retrieved per iteration, how many iterations are needed for each question? And what is the average inference time per question? A latency study comparing the proposed method with baseline methods is needed to validate its practical applicability.

- Unclear generalizability. As described in Section 4.1, only 500 questions are randomly sampled as the test set in each benchmark, which represents only a small portion of the entire test set (e.g., 2WikiMultiHop has 12,576 test samples in total), and thus the evaluation results may not be representative. Would the findings still hold if the evaluation were conducted on the entire test set? Furthermore, does the proposed method generalize to other open-domain QA tasks (e.g., NaturalQuestions/TriviaQA), which do not heavily rely on multi-hop reasoning? Would it still outperform baselines in such cases? Given the current simple evaluation setting, the generalizability of the proposed method remains unclear.

### Questions
Please address the technical questions in weaknesses.

Below are some clarification questions on self-taught fine-tuning:
1. In Figure 1, how are rationales generated given the correct trajectories (i.e., connected knowledge triplets)? Does the process involve prompting the LLM to generate a rationale that explains how these triplets lead to the final answer?
2. In Algorithm 2, what is the input/output data format in $\mathcal{D}_{z}$ used to fine-tune the model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes KnowTrace, an iterative retrieval-augmented generation (RAG) framework for complex, multi-hop question-answering tasks. KnowTrace consists of two main phrases: *(1)* knowledge exploration, which takes the input question and an initial knowledge graph (KG) and provide guidance (entity-relation pairs to expand) for further querying the retrieval corpus. *(2)* knowledge completion, which takes entity-relation pairs and retrieved passages and output completed knowledge triplets for an enriched KG for the next iteration, before reaching a desired answer.
In addition, the paper also introduces an extended self-taught finetuning framework leveraging rationale data from KnowTrace's explicit knowledge trajectory in the process.

### Strengths
- The paper targets a challenging multi-hop QA setting in RAG and presents a new framework supported by strong empirical performance.

- The paper is generally well-written, well-motivated, and introduces a cleaver incorporation of knowledge graph operation for structured RAG. 

- The paper includes multiple, comprehensive baselines to support the main experimental results of the proposed approach.

### Weaknesses
 - It is not entirely clear between the difference of KnowTrace and iterative restructuring-based RAG. To the best of my understanding, the restructuring-based RAG approaches adopted as the baselines only involve one-time inference. However, considering that KnowTrace employs multiple iteration, it might be fair to also compare restructuring-based RAG approaches in an iterative setting.

- The presentation could be further improved for better clarity. In particular, it is relatively difficult for readers to imagine the inputs and outputs at different stages of KnowTrace with only the high-level conceptual framework (Figure ```1```). For instance, it might be hard to imagine the so called "guidance" provided by knowledge exploration. It would be greatly beneficial if an actual example of the input and generation results is accompanied in the paper.

- The self-taught finetuning KnowTrace$^*$ could be further enhanced with the iterative RAG baselines which also provide rationales (CoT) or other related works (e.g., InstructRAG [1]).

### Questions
- How many numbers of iterations does KnowTrace adopted in the experimental results of Table ```1```?

### Soundness
2

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
5

### Summary
This paper focuses on using large language models (LLMs) for knowledge-intensive, multi-hop question answering. Specifically, it introduces an approach to iteratively store and combine retrieved relevant knowledge in the form of knowledge graph triples, ultimately using this structured information for answering questions. The structured nature of the reasoning process is also leveraged to filter the generated reasoning paths, and the model is also fine-tuned based on these filtered reasoning chains.

### Strengths
- The paper is well-written, clear, and easy to follow. The proposed method is straightforward, intuitive, and easy to implement.
- It is innovative that the paper leverages the structured nature of reasoning paths to filter and refine generated trajectories for model training.
- The method demonstrates strong empirical performance across multiple datasets compared to the baseline methods.

### Weaknesses
My main concern is with the novelty of this approach. Representing knowledge or reasoning processes in a structured format has been explored in several prior works [1, 2, 3, 4, 5], many of which were also tested on similar benchmark datasets. These works considered not only structured representations but also integrated unstructured knowledge to include information that may not fit neatly into a knowledge graph. The core idea is thus similar. The FLAG mechanism for knowledge exploration here also resembles the self-ask approach (also mentioned in this paper), where models automatically stop querying and generate an answer. It would be helpful for the authors to provide a more detailed comparison with these works to highlight the unique contributions of this paper. Specifically, the paper does not clearly articulate how its approach differs from prior work that uses graph-based representations for multi-hop reasoning, particularly in how it handles the extraction and utilization of knowledge graph triples from unstructured text. The paper also needs to clarify how the iterative knowledge storage and combination process provides a significant advantage over existing methods that also employ iterative reasoning with structured knowledge.

### Questions
In datasets like HotpotQA and Musique, many supporting facts may be difficult to represent solely in the form of triples. How did you address such cases?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Previously, most iterative RAG methods accumulate all retrieved passages into LLM prompts, creating challenges for handling long context and unstructured text. A more helpful way would be to develop specific structures from these passages for the LLM to better understand. To seamlessly incorporate the informative restructuring process into the iterative RAG for higher-quality multi-step reasoning, the authors propose KnowTrace, which coherently traces out question-specific knowledge structures to bolster multi-step reasoning.
Specifically, KnowTrace alternates between knowledge exploration and knowledge completion. During Knowledge Exploration, the LLM determines a set of entities and respective relations based on the current KG. During Knowledge Completion, the LLM fills in the entities based on the retrieved passages. Moreover, the authors illustrate a backtracking process that maps out a subgraph that contribute to the final prediction and use this to distill high-quality rationales. The mechanism is incorporated into self-improvement.
In the experiments, KnowTrace consistently outperforms other baselines. With backtracking, KnowTrace's performance improves in each iteration.

### Strengths
1. The method motivation is clear, which is restructuring the retrieved passages to facilitate better reasoning.
2. KnowTrace demonstrates stable improvement across all datasets and setups. The authors conducted ablations in knowledge prompting strategies, number of retrievals, etc. Figure 3 is particularly interesting, which shows that KnowTrace can improve scenarios with a large number of retrievals, suggesting better abilities to organize important information.
3. The self-improvement loop shows promising results on scaling such RAG methods.

### Weaknesses
No specific weaknesses.

### Questions
1. It seems that this self-improvement training and the inference steps could incur some overhead. Could you include a cost analysis?
2. The retrieved passages are in the form of free text, which is then transformed into knowledge triplets with the LLM. Would it be possible to directly retrieve from some KG?
3. For the back-tracing step, if the data is collected with a more powerful backbone model, would the quality be improved? Would the better-quality data contribute to more effective training for improvement?

### Soundness
3

### Presentation
3

### Contribution
3
