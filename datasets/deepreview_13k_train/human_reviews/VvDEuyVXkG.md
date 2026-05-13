# Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Multimodal Retrieval Augmented Generation (mRAG) plays an important role in mitigating the “hallucination” issue inherent in multimodal large language models (MLLMs). Although promising, existing heuristic mRAGs typically predefined fixed retrieval processes, which causes two issues: (1) Non-adaptive Retrieval Queries. (2) Overloaded Retrieval Queries. However, these flaws cannot be adequately reflected by current knowledge-seeking visual question answering (VQA) datasets, since the most required knowledge can be readily obtained with a standard two-step retrieval. To bridge the dataset gap, we first construct Dyn-VQA dataset, consisting of three types of ``dynamic'' questions, which require complex knowledge retrieval strategies variable in query, tool, and time: (1) Questions with rapidly changing answers. (2) Questions requiring multi-modal knowledge. (3) Multi-hop questions. Experiments on Dyn-VQA reveal that existing heuristic mRAGs struggle to provide sufficient and precisely relevant knowledge for dynamic questions due to their rigid retrieval processes. Hence, we further propose the first self-adaptive planning agent for multimodal retrieval, \textbf{OmniSearch}. The underlying idea is to emulate the human behavior in question solution which dynamically decomposes complex multimodal questions into sub-question chains with retrieval action. Extensive experiments\footnote{Code and dataset will be open-sourced.} prove the effectiveness of our OmniSearch, also provide direction for advancing mRAG.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new dataset: Dyn-VQA, that fills the gap in existing multi-modal RAG benchmarks by including questions that require varied and dynamic retrieval strategies, 1.5k samples for 9 domains, 2 languages and 3 categories of questions, including rapidly changing knowledge, multimodal knowledge required problem and multi-hop reasoning in mVQA, which is a very essential practical problem in VLM driven search engines.
The paper also presents: OmniSearch, a self-adaptive planning agent decomposes complex questions into sub-questions and dynamically plans retrieval actions to address these challenges. The authors conducted extensive experimental results show that OmniSearch improves performance over traditional heuristic mRAGs.

### Strengths
- Originality: The authors have an innovative and practical focus on the gap in existing benchmarks, especially the dynamic retrieval, and multi-modal multi-hop questions. This dataset is extensively curated manually and reflects some real-world complexities.

- Clarity: The paper provides clear definitions, comprehensive descriptions of the dataset construction, and detailed experimental setups. Included some comparison with baselines and highlights the uniqueness and impact of OmniSearch.

- Quality: The authors conducted extensive ablation experiments to compare the performance of OmniSearch.

- Significance: This work provides valuable insights into dynamic planning agent for RAG in multimodal LLMs, focus on a crucial challenge for advancing AI's real-world applicability in mVQA tasks.

### Weaknesses
 - The dataset's limited size of 1.5k samples, with only 178 questions covering all three challenging categories, raises questions about whether its complexity and diversity are sufficient to benefit the broader research community.

- In data curation part, the dataset only includes English and Chinese, and the authors filtered intractable instances that doesn't translate well, this might limit the dataset's diversity or introduce bias. if more languages are included, and examples are elaborated on how human are correcting Google Translate API, the dataset would be more convincing to be used to evaluate model's generalizability and performance on culturally specific questions that might present real-world challenges.

- For the omniSearch agentic flow, there is no discussion of the latency or computational overhead associated with the multi-step retrieval process.

- The authors seem to not ablate the feedback generation effectiveness in the experiment sections.

- In the experiment part, no reasoning-based commercial search engine such as GPT-4o are included as baselines.

- Figure 3 seems to have a typo in the question, what's the price of this car rather than what's the price on this car?

### Questions
- Can the authors elaborate more on the process of how the AI researchers are selected and trained to curate dataset, and how the distribution is defined?
- Can the authors conduct experiments with GPT-4o and also include the latency evaluations? Would also love to see how the feedback generation are effective in other baselines.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Dyn-VQA a new dataset for benchmarking multimodal retrieval-augmented generation (mRAG) methods. The dataset is constructed specifically with tasks that require adaptive retrieval methods that can handle changing answers, multi-hop reasoning and multi-modal knowledge. The authors run several baselines/benchmarks on this dataset with different MLLM models, and mRAG methods. The authors also introduce OmniSearch, a self-adaptive planning agent designed to overcome the limitations of current mRAG methods (the limitations this dataset addresses), and show a performance gain from OmniSearch.

### Strengths
1. They introduce a strong, novel dataset, Dyn-VQA, which offers a new, and uniquely hard multi-modal retrieval challenge for adaptable, multi-hop retrievals - which mimics real world settings well. 

2. Strong experimental section - they benchmark this dataset with several MLLMs, and several types of mRAG methods. 

3. They introduce the OmniSearch method which performs very well on this task. 

4. The paper is mostly clearly written and well motivated.

### Weaknesses
1. The dataset has a strong motivation, however, the abstract and introduction could more clearly address the concepts of (as you labeled them) (1) Non-adaptive Retrieval Queries and (2) Overloaded Retrieval Queries. Clarifying these issues up front would help position and motivate the work better - and I felt they weren't so clearly explained.

2. There could be more discussion around the scalability and computational cost of OmniSearch to provide a better sense of its applicability in real-world/time settings.

### Questions
1. Could you say more about the computational costs of OmniSearch specifically as it scales with multi-step, dynamic retrievals?

2. It is interesting that no questions was correctly answered by all models - and in general Figure 5 is really interesting to see - do you have any intuition for this distribution? Could it be used to sort of profile what tasks a specific LLM is good at?

### Soundness
4

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
4

### Summary
The authors focuses on a dynamic visual question answering (VQA) task, where the answers can change over time (e.g., "What is his latest film?"). The authors introduce a new dynamic VQA benchmark to investigate the limitation of current multimodal retrieval augmented generation (mRAG) methods. The authors propose a new retrieval method, OmniSearch, which is based on the self-adaptive planning agent.

The contributions of this paper include (i) a new benchmark for the dynamic VQA task and (ii) a new approach---a self-adaptive planning agent---to improve task peformance.

### Strengths
- **Introduction of a new VQA benchmark**: The authors focus on "dynamic" visual questions, where answers can change over time. This type of question is frequently encountered in real-world scenarios but is underrepresented in existing VQA datasets. The authors propose a new benchmark featuring dynamic visual questions that reflect the complexity of real-world inquiries.

- **Proposal of a new mRAG approach**: The author introduces a self-adaptive retrieval agent that plan seach retrieval actions in real time and demonstrate its effectivness on dymanic VQA tasks. This approach is designed as a plug-and-play module that can be incorporated into various MLLMs, showing its applicability.

- **Presentation**: The paper is clearly written and easy to follow.

### Weaknesses
 - **Sustainability of Benchmark Accuracy**: Since the answers to certain questions in this benchmark may change over time, there is a risk that the answers will become **outdated** after the benchmark is publicly released. This raises concerns about how to ensure accurate model evaluation in such cases (i.e., when the benchmark's ground-truth answers no longer reflect current information). How will the benchmark address this issue to continue providing reliable, up-to-date evaluations?

- **Unclear Definition of "Hops" in Questions**: The benchmark offers "multi-hop" visual questions, which the authors claim are often missing in existing VQA benchmarks. However, the paper lacks clarity in defining a "hop". While the authors consider one reasoning step as one hop, they do not specify how they define a single reasoning step. Interpretations of reasoning steps can vary; for example, some may consider a particular reasoning process as requiring two steps, while others might view it as involving only one step. Setting clear criteria for defining a reasoning step is essential.

- **Missing Related Work**: While the paper focuses on multi-hop visual questions, it does not address recent work in this area. For example, it omits the citation, "Kil et al., II-MMR: Identifying and Improving Multi-modal Multi-hop Reasoning in Visual Question Answering, ACL'24."

### Questions
Please see the weakness of the paper.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose OmniSearch to address the limitations of existing Multimodal Retrieval Augmented Generation (mRAG) methods: (1) non-adaptive retrieval queries and (2) overloaded retrieval queries. Additionally, considering these limitations cannot be adequately reflected in current knowledge-seeking visual question answering datasets, the authors construct the Dyn-VQA dataset. It consists of three types of “dynamic” questions and requires complex knowledge retrieval strategies. Experiments demonstrate the effectiveness of the proposed OmniSearch.

### Strengths
1.	The proposed Dyn-VQA dataset bridges the gap in the existing VQA-based mRAG benchmarks. It is oriented towards real-world problems and emphasizes the ability to retrieve dynamic knowledge during the question-answering process.
2.	This paper provides the analysis of the statistical information, data quality and diversity of the proposed Dyn-VQA dataset.
3.	The experiment results show the effectiveness of the proposed OmniSearch method.

### Weaknesses
1.	The scale of the proposed Dyn-VQA dataset is small, containing only 1,500 questions. It is significantly fewer than existing knowledge-seeking VQA datasets.
2.	Although the proposed OmniSearch shows the potential in application, the innovation is limited.
3.	As mentioned in the case study, the OmniSearch method struggles with questions that require long-term reasoning chains and fine-grained questions.

### Questions
1.	The authors may consider expanding the scale of the Dyn-VQA dataset.
2.	The Dyn-VQA dataset considers two languages (Chinese and English). I wonder if there are impacts on different LLM or MLLM models? For example, some models only support Chinese and English, but others support more languages.
3.	The authors should explain how OmniSearch dynamically decomposes the sub-questions and how it determines whether a question has been resolved?
4.	The authors should explain the difference between OmniSearch and the chain-of-thought method. 
5.	In experiments, the authors may consider evaluating the effectiveness of OmniSearch based on more LLMs or MLLMs.

### Soundness
2

### Presentation
3

### Contribution
2
