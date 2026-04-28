# Locate-then-edit for Multi-hop Factual Recall under Knowledge Editing

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
The locate-then-edit paradigm has shown significant promise for knowledge editing (KE) in Large Language Models (LLMs). While previous methods perform well on single-hop fact recall tasks, they consistently struggle with multi-hop factual recall tasks involving newly edited knowledge. In this paper, leveraging tools in mechanistic interpretability, we first identify that in multi-hop tasks, LLMs tend to retrieve implicit subject knowledge from deeper MLP layers, unlike single-hop tasks, which rely on earlier layers. This distinction explains the poor performance of current methods in multi-hop queries, as they primarily focus on editing shallow layers, leaving deeper layers unchanged. To address this, we propose IFMET, a novel locate-then-edit KE approach designed to edit both shallow and deep MLP layers. IFMET employs multi-hop editing prompts and supplementary sets to locate and modify knowledge across different reasoning stages. Experimental results demonstrate that IFMET significantly improves performance on multi-hop factual recall tasks, effectively overcoming the limitations of previous locate-then-edit methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses challenges in existing locate-then-edit knowledge editing methods, particularly focusing on multi-hop knowledge editing. The authors first investigate why locate-then-edit approaches struggle with multi-hop fact editing using tools from mechanistic interpretability, such as the logit lens and causal intervention. Their findings suggest that later MLP layers play a crucial role in storing multi-hop knowledge. To better update these knowledge-storing MLPs, the authors introduce a supplementary set construction method for each edit, transforming each edit into a multi-hop chain. This supplementary set then generates virtual multi-hop prompts specifically targeting the knowledge being edited. The authors utilize two-hop templates from this supplementary set to modify the model’s later layers, thereby enhancing multi-hop knowledge editing.

### Strengths
- **Comprehensive Analysis**: The paper presents a thorough analysis in Section 3, identifying that information related to multi-hop knowledge is stored in later MLP layers. Using interpretability tools such as the logit lens and causal interventions, the authors confirm this and propose edits to the last layer based on these findings.
- **Empirical Validation**: Experiments in Tables 3 and 4 show that the proposed method outperforms previous methods on multi-hop knowledge editing tasks, providing compelling evidence for its effectiveness.

### Weaknesses
 - **Insufficient Presentation**: Section 5.2 lacks clarity as Tables 5 and 6 are referenced but not included in the main paper, instead being located in the appendix. While space constraints are understandable, omitting key results from the main discussion detracts from readability and coherence. Additionally, the absence of descriptions for the "base" in Tables 5 and 6 and missing details on the datasets used in Table 4 (e.g., whether MQuAKE is consistently used) leaves gaps in understanding.
- **Questionable Analysis of Results**: In Table 3, performance seems to decline post-editing compared to the original, but there is no discussion on the possible causes for this drop. If editing knowledge reduces performance, the rationale for the edits becomes unclear. It appears that “original” performance refers to accuracy on the unedited answer, but if so, why wasn’t accuracy on the correct answer also reported for the original model? Clearer explanations are necessary to clarify these performance metrics.
- **Limited Novelty in Method and Analysis**: The primary contribution of this work lies in the insight, obtained through interpretability tools, that multi-hop knowledge editing requires updating the later MLP layers. However, there is no clear experimental analysis showing that editing the later layers specifically contributes to performance improvement. It raises the question of whether merely expanding the support set was sufficient for better performance, implying that gains may not be attributed solely to the proposed method. To substantiate this claim, it would be useful to report the impact of the editing layers on performance, comparing different layers with and without the supplementary set.

### Questions
- **Figures**: Consider widening Figures 2(a) and 2(b) to improve readability and enlarge the subfigures in Figure 6 for better visibility.
- **Tables**: Provide a clearer explanation of the term “base” in Tables 5 and 6. It’s unclear whether this refers to the “original” in Table 3 or another baseline. Clear labels and descriptions would enhance understanding.

### Soundness
3

### Presentation
2

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
This paper introduces IFMET, a novel locate-then-edit method for knowledge editing for language models.
It aims to improve the multi-hop factual recall by modifying both shallow and deep layers of model weights.
Previous methods focus on shallow layers and thus struggle with multi-hop editing.
IFMET addresses this by using multi-hop prompts and supplementary sets to locate and edit knowledge across multiple layers.
This allows the language model to answer multi-hop queries more accurately post-edit.
Experimental results show that IFMET outperforms existing knowledge editing methods (such as Mello, and MEMIT) on multi-hop knowledge editing.

### Strengths
1. This paper fills a gap in KE for multi-hop knowledge editing. It addresses the limitations of traditional local-then-edit methods that primarily operate in shallow layers.
2. The paper gives detailed explanations and experiments about how single-hop and multi-hop queries are handled differently within language models. The used LogitsLen and causal intervention experiments are interesting.
3. The proposed IFMET is compared with strong baselines across experiments and shows great performance.

### Weaknesses
1. The used language model GPT-J (6B) is a bit outdated. More recent language models are expected to be considered. While the paper focuses on multi-hop knowledge editing, the choice of an older model raises concerns about the generalizability of the findings to current state-of-the-art models. The performance of IFMET on models like Llama-3, which have different architectures and training regimes, remains an open question. The observed improvements might not directly translate to these newer, more complex models, thus limiting the practical impact of the proposed method.
2. How about the performance of the generality and locality of knowledge editing? The editing should also affect related facts but not affect other unrelated facts. The paper needs to provide a more comprehensive analysis of how the edits propagate through the model's knowledge graph. It's crucial to demonstrate that IFMET can modify specific facts without causing unintended side effects on other, unrelated knowledge. The evaluation should include metrics that quantify both the intended changes and any collateral damage to the model's overall knowledge base. For example, editing a fact about a specific city should not alter facts about other cities or unrelated topics.
3. The paper lacks discussions about editing efficiency. What is the time complexity of IFMET? The computational cost of IFMET needs to be clearly defined, especially in comparison to other knowledge editing methods. The paper should detail the time complexity of each step in the IFMET pipeline, including the locate and edit phases. This analysis should also consider the impact of the supplementary set size on the overall editing time. Without this information, it's difficult to assess the practical applicability of IFMET for large-scale knowledge editing tasks.
4. Compared to Mello, IFMET requires supplementary set construction from external sources (same for MEMIT and ROME). This may hinder its applications in real cases. The reliance on external knowledge sources for supplementary set construction introduces a dependency that could limit the applicability of IFMET in scenarios where such resources are not readily available or are expensive to obtain. The paper should discuss the implications of this dependency and explore potential alternatives for generating supplementary sets internally, using the language model itself.

### Questions
1. The biblology style should be consistent. Some lines are underlined and others are not.
2. How does IFMET perform on other language models? Like recent Llama-3.
3. How long does IFMET take to edit one multi-hop sample?
4. Can IFMET deal with unstructured facts for knowledge editing as in [1]?
5. Line 387, cizizenship --> citizenship.
6. Figure 1, Mardrid --> Madrid.

 [1] Updating Language Models with Unstructured Facts: Towards Practical Knowledge Editing

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses an important limitation in knowledge editing for LLMs - their poor performance on multi-hop factual recall tasks after editing. Through careful mechanistic analysis using tools like LogitLens and causal intervention experiments, the authors discover that LLMs process multi-hop queries differently from single-hop ones - they accumulate implicit subject information in middle layers before retrieving the final answer from deeper MLP layers. This explains why current KE methods, which focus on editing shallow layers, fail at multi-hop tasks. Based on these insights, they propose IFMET, a novel locate-then-edit approach that edits both shallow and deep MLP layers using supplementary knowledge sets and multi-hop prompts. Their experimental results on the MQuAKE dataset show improvements over existing methods, particularly for complex multi-hop queries.

### Strengths
1. Strong Empirical Analysis: The authors provide a thorough, well-designed investigation into how LLMs process multi-hop queries differently from single-hop ones. The use of LogitLens and causal intervention experiments to track information flow through different layers is particularly impressive.

2. Novel Theoretical Insight: The discovery that implicit subject information accumulates in middle layers before being used to retrieve answers from deeper MLP layers is an important contribution to our understanding of LLM reasoning. This finding not only explains the limitations of current KE methods but also has broader implications for LLM interpretability research.

3. Good result: The proposed IFMET solution is elegant and well-motivated by the theoretical findings. This is a practical solution that improves performance on multi-hop queries.

### Weaknesses
Overall, this paper is solid. But some parts of this paper are missing:

1. Why do we need to conduct "Locate-then-edit" editing when we have some very good performance RAG-based editing methods [1][2]? There is no need for this paper to compare performance with RAG-based editing in the experiments part, but a short discussion should be included on why IFMET is superior to these RAG-based methods.

2. Currently, only experiments are conducted on MQUAKE-3k; more benchmarks, such as MQUAKE-T, could be included.

### Questions
See weakness

### Soundness
4

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
4

### Summary
The paper introduces IFMET, a novel locate-then-edit approach for knowledge editing in Large Language Models (LLMs), specifically targeting multi-hop factual recall tasks. The authors leverage mechanistic interpretability to identify that LLMs retrieve implicit subject knowledge from deeper MLP layers in multi-hop tasks, unlike single-hop tasks, which rely on earlier layers. This insight leads to the development of IFMET, which edits both shallow and deep MLP layers. Experimental results show that IFMET significantly outperforms existing methods on multi-hop factual recall tasks.

### Strengths
1. The paper provides a thorough and interesting analysis of the differences between single-hop and multi-hop tasks, highlighting the importance of editing deeper layers in LLMs.

2. The writing is clear, making the proposed method easy to understand and follow.

3. The experimental results are impressive, demonstrating significant improvements over existing methods in multi-hop factual recall tasks.

### Weaknesses
1. The method may have certain limitations. Specifically, using WikiData and SPARQL queries to construct the supplementary dataset may not be applicable to non-factual or non-encyclopedic data, limiting the generalizability of the approach. The reliance on structured knowledge bases like WikiData restricts the method's applicability to domains where such resources are not readily available or easily queryable. This raises concerns about the method's performance on tasks involving unstructured or less formalized knowledge. Furthermore, the process of converting information into SPARQL queries can introduce biases or inaccuracies, potentially affecting the quality of the supplementary dataset and, consequently, the overall performance of the knowledge editing process.

2. The organization of the paper could be improved. The experimental section is relatively short, with some important experimental tables relegated to the appendix. Additionally, the paper lacks a comprehensive ablation study. The absence of a thorough ablation study makes it difficult to assess the individual contributions of different components of the proposed method. For example, it is unclear how the performance of IFMET is affected by the choice of specific layers for editing or the size of the supplementary dataset. The lack of detailed ablation experiments hinders a deeper understanding of the method's behavior and limits the ability to optimize its performance.

3. The explanation and analysis of the experimental results are somewhat lacking. For instance, in Table 3, it is unclear what the values represent (e.g., accuracy) and why the performance of IFMET improves as the edit batch size increases, while the performance of other baselines decreases. More detailed explanations and discussions of these observations would strengthen the paper. The paper does not provide sufficient analysis of the observed trends in the experimental results. For example, the reasons behind the performance differences between IFMET and other baselines across varying batch sizes are not adequately explored. A more in-depth analysis of these results, including potential explanations for the observed behaviors, would significantly enhance the paper's impact.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3
