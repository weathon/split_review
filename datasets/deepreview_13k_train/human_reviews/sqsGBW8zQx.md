# Understanding and Enhancing Context-Augmented Language Models Through Mechanistic Circuits

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Recent studies have extracted circuits from the computational graphs of language models for simple language tasks such as entity tracking or indirect object identification. In our paper, we scale up circuit extraction to a real-world language modeling task: context-augmented language modeling for question-answering (QA) tasks and understand the potential benefits of circuits towards downstream applications such as data attribution. We extract circuits as a function of internal model components (e.g., attention heads, attention layers, MLPs) using causal mediation analysis techniques. Leveraging the extracted circuits, we first understand the interplay between the language model's usage of parametric memory and retrieved context towards a better mechanistic understanding of context-augmented language models. We then identify a small set of attention heads in our circuit which performs reliable data attribution by default, thereby obtaining attribution for free in just the model's forward pass! Using this insight, we then introduce AttnAttrib, a fast data attribution algorithm. Through a range of empirical experiments across different extractive QA benchmarks, we show that performing data attribution with AttnAttrib obtains state-of-the-art attribution results across different language models. Finally, we show the possibility to steer the language model towards answering from the context, instead of the parametric memory by (i) using the attribution from our extracted attention head as an additional signal during the forward pass and (ii) scaling the output of a small set of attention heads. Beyond mechanistic understanding, our paper provides tangible applications of mechanistic circuits in the form of reliable data attribution and model steering.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper leverages the internal behavior of attention heads for feature attribution. The authors build on prior methods to identify influential attention heads that determine whether the model relies on internal memory or external context. Furthermore, they demonstrate that by controlling these specific attention heads, they can steer the behavior of LLMs.

### Strengths
* This paper analyzes attention patterns in LLMs to examine their reliance on contextual versus parametric knowledge, revealing the presence of key attention heads (or circuits) involved in this process.

### Weaknesses
 * The contribution of this paper is unclear. The probing method used was introduced in prior work (Wang et al., 2022). Although the authors mention some limitations of this prior work, these issues also apply to the current paper, such as only testing on a simple extractive QA task, reliance on a high-quality probe dataset, and limited practical impact.
* For "understanding context-augmented language models," the feature attribution task based on extractive QA is overly simplistic. This work remains an interpretability task with the extractive answer already given. Note that various feature attribution methods, including those based on attention analysis, have been extensively studied over the years [1]. Is the proposed method better than prior attention-based methods? Moreover, it remains unclear whether the detected attention heads generalize across different tasks and domains.
* For "enhancing context-augmented language models," the experimental results are too weak, with no baseline comparisons (see the next point).
* While this paper aims to address knowledge conflicts between contextual and parametric knowledge, it overlooks a substantial amount of relevant literature. Notably, some of these works also conduct causal analysis. Below is a selective list
  * Mallen, Alex, et al. "When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories." Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2023.
  * Wang, Fei, et al. "A Causal View of Entity Bias in (Large) Language Models." Findings of the Association for Computational Linguistics: EMNLP 2023. 2023.
  * Wu, Kevin, Eric Wu, and James Zou. "How faithful are RAG models? Quantifying the tug-of-war between RAG and LLMs' internal prior." arXiv preprint arXiv:2404.10198 (2024).
  * More work can be found in this survey: Xu, Rongwu, et al. "Knowledge conflicts for llms: A survey." arXiv preprint arXiv:2403.08319 (2024).

[1] Wiegreffe, Sarah, and Yuval Pinter. "Attention is not not Explanation." Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP). 2019.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a circuit extraction method for question-answering by using causal mediation analysis. The proposed method can be used for QA tasks rather than entity tracking. They experiment on two constructed datasets, *copy* and *memory*, and reveal a small set of attention heads in the extracted circuit for context faithfulness. Based on these findings,  they present ATTNATTRIB, a fast and efficient data attribution algorithm, which shares a better performance and generality.

### Strengths
This work presents an intervention study on QA tasks, which extends the existing work of entity tracing to a more practical setting. 
The new ATTNATTRIB can outperform other baselines and also have a better generality.

### Weaknesses
 * the writing strongly hampers the contribution of this paper. The work often goes into technical details without contexts, definitions, and motivations (novelty and links to existing work), therefore, it is hard to understand the contribution of this work well (see comments in the questions below).
* the proposed interventional algorithm is very similar to ROME [1]. It is necessary to state the novelty of this work.  
* the experimental design can be improved as follows: (1) for each proposed algorithm, it is useful to give the basic background and discuss the relation between the existing method and the new method (2) this work claims that the detected mechanistic circuit extraction can be used for real-world tasks. However, the experiments focus on short-answer questions. A better setting is the open-ended QA tasks and long-form generations (3) the intervention performs the patching operation at the last token position. It is applicable to use Multi-choice QA to locate associations [2] (4) Regarding the effectiveness of the proposed interventional algorithm, it is necessary to add baselines such as ROME or gradient-based methods (5) I do not fully understand the design of the **memory** corrupted dataset. Can we use the queries solely for this goal?

In summary, the writing is a big issue of this submission, which prevents us from accurately assessing the scientific contributions. 
I am open to further discussions. 

[1] Locating and Editing Factual Associations in GPT

[2] Identifying Query-Relevant Neurons in Large Language Models for Long-Form Texts

### Questions
* it would be useful to define the computational graph, circuit, nodes, and edges in this graph
* $\mathcal{D}_{memory}$ corrupts the original context to force LLMs to answer based on parametric memory. Why don't you directly ask LLMs the question without context?
* what is the used **metric score**? It appears in Figure 1 and line 277 without any definitions. 
* Section 3.1 can be improved. The current structure is kind of tricky. (1) introduce the original dataset $\mathcal{D}$; (2) give the motivation why you design two corrupted variants:    $\mathcal{D}_{copy} $ \mathcal{D}_{\text{copy}}; (3) describe the two corrupted datasets with notations, respectively
* in section 3.2, it is useful to state the intuition of the proposed method at the beginning
* in line 247, "We selected this position for patching because the information in the last residual stream plays a crucial role in determining the probability distribution of the generated tokens." Do you have proof of this claim?
* in section 3.3.1, where is the experimental result? 
* in Algorithm 1, what is the definition of the data attribution algorithm and a span

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
3

### Summary
This paper explores the extraction of mechanistic circuits from language models to improve their interpretability, focusing on question-answering tasks. By leveraging causal mediation analysis, the authors identify key components such as attention heads that contribute to both parametric memory and context-based responses. They introduce the ATTNATTRIB algorithm, which enhances data attribution with minimal computational cost, and demonstrate how these insights can steer models towards more context-faithful answers, ultimately improving performance on extractive QA benchmarks.

### Strengths
● The experiments in this paper are rigorously designed and provide detailed explanations of the findings.

● The discovery that "the circuits activated when the model uses contextual information are markedly distinct from those invoked for parametric memory" is especially compelling. This highlights an important mechanistic difference between context-faithful and memory-faithful circuit components, with minimal overlap among the core elements activated in each mode.

● The paper is exceptionally well-written, with a structured and clear presentation that facilitates understanding of the complex methodologies and results.

### Weaknesses
● The paper’s claims about addressing limitations in synthetic probe dataset reliance seem overstated. While it critiques prior work for its dependence on synthetic datasets (lines 44-50), the proposed method also incorporates synthetic dataset design and path patching. This suggests the approach does not fully resolve these limitations. To strengthen the discussion, could the authors clarify how their method advances upon previous approaches in terms of synthetic data reliance and dataset design? 

● Although the findings in this paper are interesting, there appears to be limited advancement in the technical contributions regarding interpretability methods. Specifically, the paper would benefit from innovative approaches or improvements to the path patching process. For instance, in sections that discuss attention head selection and context-memory circuits, I expected to see new mechanisms that either optimize these components or introduce alternative techniques to improve the model's interpretability further. It would be helpful if the authors could expand on the aspects of the interpretability methods, particularly in causal mediation analysis and hierarchy extraction, where innovative contributions could enhance the model's practical applications and robustness.

● The generalizability of the interpretation results remains uncertain. It is unclear whether the extracted circuits would exhibit similar behavior on other types of datasets.

● The proposed ATTNATTRIB seems heuristic and limited, requiring full access to LLMs and beding specifically designed for this task. The authors could enhance the discussiong by evaluating its performance on other tasks, such as MATH or MMLU, to tetter assess its broader impact.

### Questions
Please summarize the entire process of completing question-answering (QA) tasks across different modules based on the findings presented in this paper.

### Soundness
3

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
3

### Summary
This work explores the mechanistic circuit in real QA task. They design two probe datasets and extract the Context-Faithfulness Circuit and Memory-Faithfulness Circuit. Specifically, they use a similar token to replace the answer token to force the model predict the answer based on the context. Also, they use a semantical-unrelated token to replace the answer token to force the model based on the memory. They find that the circuit between context-faithfullness and memory-faithfulness are different. Furthermore, they find that there are a small set of attention heads important for data attribution. Based on these findings, they propose a new attribution method, ATTNATTRIB, for extractive QA. The ATTNATTRIB method achieves good results on different language models.

### Strengths
1. This paper focuses on an important question: the difference between the mechanism of in-context learning and memory.
2. The general idea about designing the probe datasets for context circuit and memory circuit is good.

### Weaknesses
1. The dataset is too small to get the huge conclusions. There are only 200 questions (line 194). 
2. Other experiments should be made to support the conclusions. There are two main conclusions in this paper: a) The circuits of in-context and memory are different (Section 3.3.1). b) A small subset of attention heads are important for data attribution (Section 3.3.2). A hidden hypothesis of the experiments is: in-context learning cases share similar circuits, and memory cases share similar circuits. Only if this hypothesis is verified, constructing the circuits among in-context cases or memory cases is meaningful. The authors should conduct experiments to explore this. For example, they can do experiments on 5 types of knowledge and compare the circuits. 
3. The experimental settings of the comparison between the context case and the memory case is not convincing. Let’s think about one example. The groundtruth case is “Space Seattle is in New York. Where is Space Needle located?” => “Seattle”. The in-context probe case is “Space Needle is in New York. Where is Space Needle located?” => “New York”. The memory case is “Space Seattle is in __. Where is Space Needle located?” => “Seattle”. When comparing the in-context case and the memory case, the circuits are different. However, to get this conclusion, a hidden hypothesis is: the circuits between predictions with “Seattle” and “New York” should be similar. Otherwise, this comparison is meaningless. But this hypothesis is not verified.

### Questions
1. How many cases are there in the datasets for the experiments in Section 3?
2. What is the distribution of knowledge in the probe dataset? Is it possible to construct the circuits of different knowledge and see whether the circuits are the same in in-context learning/memory?
3. Is it possible to explore the circuits between cases with similar predictions? For example, some cases with prediction “Seattle” and some cases with prediction “New York”.

### Soundness
2

### Presentation
2

### Contribution
2
