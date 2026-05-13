# BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
Pursuing artificial intelligence for biomedical science, a.k.a. AI Scientist, draws increasing attention, where one common approach is to build a copilot agent driven by Large Language Models (LLMs). However, to evaluate such systems, researchers typically rely on direct Question-Answering (QA) to the LLM itself or through biomedical experiments. How to benchmark biomedical agents precisely from an AI Scientist perspective remains largely unexplored. To this end, we draw inspiration from scientists’ crucial ability to understand the literature and introduce BioKGBench. In contrast to traditional evaluation benchmarks that focus solely on factual QA, where the LLMs are known to have hallucination issues, we first disentangle “Understanding Literature” into two atomic abilities: i) “Understanding” the unstructured text from research papers by performing scientific claim verification, and ii) interacting with structured Knowledge-Graphs for Question-Answering (KGQA) as a form of “Literature” grounding. We then formulate a novel agent task, dubbed KGCheck, using KGQA and domain-based Retrieval-Augmented Generation (RAG) to identify factual errors in existing large-scale knowledge graphs. We collect over two thousand data points for the two atomic tasks and 225 high-quality annotated samples for the agent task. Surprisingly, we find that state-of-the-art general and biomedical agents have either failed or performed inferiorly on our benchmark. We then introduce a simple yet effective baseline, dubbed BKGAgent. On the widely used popular knowledge graph, we discover over 90 factual errors, which provide scenarios for agents to make discoveries and demonstrate the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes several tasks related to the scientific literature review and evaluates the performance of LLMs and LLM-based agents. The authors also propose an agent to address the task. These tasks include KG QA, scientific claim verification and the combined KG checking tasks. Lots of mainstream LLMs are tested. Several agent designs are also evaluated with access to the tools defined by the authors.

### Strengths
* The constructed test cases for KG QA and claim verification might be helpful in evaluating clinical-related models and agents
* The designed evaluation mechanism would be used as a good reference for future agent evaluation design

### Weaknesses
 - Novelty as a benchmark work: 
	- When evaluating the LLMs only (Table 7), the LLMs do not have access to the KG or literature database, making the task a straightforward task. Similar tasks/datasets have been proposed a lot
	- When evaluating the agents (Table 8), the assumption is that the tool design is not part of the agent design (as the same set of tools are provided by the authors instead of designed by the designer of the baseline agents). This assumption makes this benchmark not generalizable and limited by the design of tools used to access KG and literature
	- The agent benchmark task is not designed to be result-oriented 
- Comparison with works of the KG-guided QA setting, such as Think-on-graph [1]
	- Both lines of work assume that external knowledge sources can be used to answer questions. What is the uniqueness of this work besides applying KG-enhanced QA to the biomedical domain?
- Soundness of the evaluation metrics
	- Why the potential relationship is refute if the relationship is not on the KG (which could totally due to the sparsity of the KG)? What is the difference between existing relationship and potential relationship?
- Missing details
	- For the claim verification task, when predicting label for a claim, does the model have access to the while corpus with 5664 articles, or it only have access to the particular article that the claim is induced from?
	- If this task is about global claims (instead of context-specific claims per article), how to handle the potential conflicts between claims?
	- What is the additional information the Qwen model used for evaluation has access to (compared with the evaluated LLMs that produce the answers)? 
	- Does the framework support unseen nodes on the KG, or does it assume all entities used for evaluation have to be on the KG already?
	- For the baseline agent without access to the "our tools", how do they access the KG and literature pool?

### Questions
Please refer to the questions in the "Weaknesses" section

### Soundness
1

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
This paper introduces BioKGBench, a benchmark for evaluating AI agents in biomedical science, designed to tackle the challenges of understanding and verifying scientific knowledge. Unlike traditional benchmarks that focus on narrow tasks like question-answering, BioKGBench emphasizes two critical abilities: Knowledge Graph Question Answering (KGQA) and Scientific Claim Verification (SCV). These tasks help assess agents' abilities to analyze both structured (knowledge graphs) and unstructured (scientific literature) data. 
The authors also introduce BKGAgent, a baseline model that effectively identifies inaccuracies in biomedical knowledge graphs, offering a useful tool for keeping scientific databases accurate and up-to-date.

### Strengths
1. The paper proposes three tasks—Knowledge Graph Question Answering (KGQA), Scientific Claim Verification (SCV), and Knowledge Graph Checking (KGCheck).

2. The study successfully identifies 96 inaccuracies within the knowledge graph, marked as "Refute" annotations. This finding is particularly significant because it challenges the common assumption that knowledge graphs contain precise information.

### Weaknesses
 1. The proposed method utilizes the Retrieval-Augmented Generation (RAG) approach; however, it lacks comparison with recent RAG-based baselines such as Self-RAG and KG-RAG. This absence makes it challenging to evaluate the effectiveness of the proposed method against state-of-the-art techniques, potentially limiting the credibility of the results.

2. The KGCheck task is primarily focused on verifying knowledge within knowledge graphs. While this is valuable, its narrow application may restrict the overall utility of the task in broader contexts.

3. The approach may face scalability issues when applied to larger and more complex knowledge graphs. 

4. The study relies solely on one KG proposed in 2020, which may not reflect the most current state of knowledge representation. Given that the KG used is relatively old, there is a risk that the findings regarding inaccuracies and errors may not accurately reflect the current capabilities and improvements in more recent KGs. As KG evolve, their accuracy and completeness can change, potentially rendering the results of this study less relevant over time.

5. The results of the study may not be easily generalized to other KGs beyond the one used. Different KGs can vary significantly in structure, content, and accuracy, making it uncertain whether the identified issues and the effectiveness of the proposed tasks will hold true across various knowledge representations.

### Questions
1. What's the difference between KGQA and STaRK [1]?

2. Clinical Knowledge Graph used in the paper has difference references including [32], [33], and [53] in the paper.

[1] Wu, Shirley, Shiyu Zhao, Michihiro Yasunaga, Kexin Huang, Kaidi Cao, Qian Huang, Vassilis N. Ioannidis, Karthik Subbian, James Zou, and Jure Leskovec. "STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases." arXiv preprint arXiv:2404.13207 (2024).

### Soundness
2

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
4

### Summary
This paper introduces BioKGBench, which explores the LLMs’ capability to do “KGCheck” - checking existing knowledge graph and cross-referencing with external literature or databases. They divide this task into two atomic sub-tasks: (1) knowledge graph question answering (KGQA), where the agent needs to answer questions of a knowledge graph; and (2) scientific claim verification (SCV), where the agent verifies a claim by querying the evidence from external datasets or literature. 

To solve the tasks, this paper proposes BKGAent, which is a multi-agent framework containing a team leader, KG agent and validation agent equipped with a set of tools. The proposed framework achieves better performance than existing baselines.

### Strengths
1.	The sub-task design of KGCheck aligns well with the methodology of human scientific research, which consists of database queries and literature review. This benchmark may be useful for future study.
2.	The proposed BKGAgent incorporates various tools and interactions between agents, and achieves better performance than baselines.

### Weaknesses
1.  From Figure 5 and Table 8, the performance of “BKGAgent” is similar to that of “AutoGen w/ our tools”. It seems that the key performance gain is achieved by the tools. Thus, the effectiveness of using three agents in this framework is not clear.
2.  The first sub-task – KGQA is closely related to the body of work on KBQA. However, the relation with KBQA is not discussed in this paper. Also, is it possible to benchmark KBQA methods in the KGQA subtask and use them instead of KG agents in the KGCheck task?
3.  The performance of proposed framework on the sub-tasks are not reported and compared with baselines (Table 7).
4.  The metrics (understanding, reasoning, efficiency, KG process, information retrieval) are not explained and it is not clear what these scores imply.

### Questions
1.	What is the proportion of different reasoning types (one-hop, multi-hop, conjunction) involved in the KGCheck task?
2.	What is the recall rate of errors detected by BKGAgent on the KGCheck task?

### Soundness
2

### Presentation
3

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
This work investigates the challenge of "ai agent for scientific literature" that focus solely on factual QA, leading to LLM hallucinations. A novel benchmark BioKGBench which integrates a Knowledge Graph Question Answering task and a Scientific Claim Verification task is proposed. Detailed construction (data source, statistics etc.) and a baseline is proposed to validate the quality of BioKGBench.

### Strengths
a) A novel benchmark called BioKGBench for evaluating biomedical ai agent is proposed.

b) Extensive evluation on existing ai agents are compared.

c) A baseline called BKGAgent is proposed.

### Weaknesses
a) Lack cost analysis of BKGAgent.

b) The generalizability of proposed pipeline to other domains is not discussed.

c) Minor writing issues.

### Questions
a) How the labels are made for SCV task? Any human agreement tests on the labeling?

b) Do the authors have a vision on the difference between proposed agent method and the existing agent methods? How the difference can impact on the performance on BioKGBench?

c) Do the authors have a vision on how the generalizability of proposed pipeline to other domains?

d) In line 363-364, the authors may want to avoid using the word "propose" since the metrics used are common.

e) How the classification is made for SCV task? Is it a self-critique / prompting process or a trainable process? If it's a prompt-based process, what is the scoring criteria?

### Soundness
3

### Presentation
3

### Contribution
3
