# Enhancing Document Understanding with Group Position Embedding: A Novel Approach to Incorporate Layout Information

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
Recent advancements in document understanding have been dominated by leveraging large language models (LLMs) and multimodal large models. However, enabling LLMs to comprehend complex document layouts and structural information often necessitates intricate network modifications or costly pre-training, limiting their practical applicability. In this paper, we introduce Group Position Embedding (GPE), a novel and efficient technique to enhance the layout understanding capabilities of LLMs without architectural changes or additional pre-training. GPE achieves this by strategically grouping the attention heads and feeding each group with distinct positional embeddings, effectively encoding layout information relevant to document comprehension. This simple yet powerful method allows for effective integration of layout information within the existing LLM framework.  We evaluate GPE against several competitive baselines across five mainstream document tasks. We also introduce a challenging benchmark called BLADE, specifically designed to assess layout comprehension. 
 Extensive experiments on both established and BLADE benchmarks confirm the efficacy of GPE in significantly advancing the state-of-the-art in document understanding.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces Group Position Embedding (GPE), a method to enhance layout comprehension in Large Language Models (LLMs) without requiring architectural changes or extra pre-training. By grouping attention heads with distinct positional embeddings, GPE effectively encodes layout information for document tasks. Tested on five standard benchmarks and the challenging BLADE benchmark, GPE shows significant improvement in document understanding over existing methods.

### Strengths
(1) interesting task

(2) new method

(3) extensive experiments

### Weaknesses
(1) Missing important details for dataset construction: Any critiria to manual and filter challenging question-answer pairs for the data scenarios of Forms, Slides, and Websites? Why is Newspapers constructed with an initial manual selection whereas SynthDocs being synthetically generated? For SynthDocs whose answers are synthetically generated, any filtering measure to ensure the data quality?

(2) Missing the intuitive motivation of the proposed method: Although this paper verified the effectiveness of the proposed method compared with other approaches on Layout-aware Position Embeddings through the empirical experiments, it lacks of more intuitive explanations on the advantages of the proposed method, which can provide more insights for the follow-up work.

(3) Missing the clarification of the experiment results: According to  the experiment results in Table 1, vanilla Qwen2-7B  outperforms GPE-Qwen2-7B on VisualMRC, which needs more clarifications.

### Questions
Please refer to the weaknesses

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
4

### Summary
This paper introduces a new positional encoding method to tackle the limitations of current LLMs/MLLMs' lack of layout information for addressing layout-aware document understanding tasks. A dataset named BLADE is designed to mainly focus on measuring the performance on complex-layout aware questions. Various experiments with different model configurations are conducted.

### Strengths
1. The paper proposed a new positional encoding to address the limitation of existing LLMs/MLLMs neglecting layout information. 
2. A benchmark is proposed specifically focusing on evaluating the performance of various LLMs/MLLMs on document understanding tasks with complex layouts.

### Weaknesses
1. Motivation: The limitations of current positional encoding methods adopted by other frameworks are not clearly defined. The research gaps are not clearly defined.
2. The methods are described well with the technical workflow without specific reasons and experiments as to why the positional encoding is working. For example, there is no explanation or citation as to why different position information giving various heads are reasonable for the research aim. 
3. The datasets are not clearly described making understanding breakdown categories difficult. 
4. The proposed methods are only evaluated on LLM which is expected to see whether it's workable on MLLMs and pretrained document understanding models. 
5. More reading order setups should be tried like XY-cut. 
6. There are some typos and some possible errors in the paper, like Table 2 SCOIE performance. Some bolded digits in the performance tables are not the highest.

### Questions
1. Motivation and Related Work: what is the limitation of current positional encoding methods adopted by pretrained document understanding frameworks and what are the limitations of them? 
2. Dataset: is that necessary to have a layout-aware dataset. Only focusing on layout-complex questions may ignoring the performance on other generative tasks. 
3. Model and Evaluation: is there any reason you chose those LLMs/MLLMs? It would be better to give more insight analysis for this part by giving more ablation and case studies. 
4. Is it possible to show some qualitative analysis of benchmark datasets like CORD, SROIE?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper makes two main contributions: (1) it uses group position embedding to ensure that different attention heads focus on different views of position, and (2) it introduces a new document AI dataset, BLADE, which highlights the model's ability to handle complex layout information. Experimental results demonstrate improved performance, and the ablation studies are comprehensive.

Updated on 23th Nov 2024: raise the score

### Strengths
1. The proposed group position embedding is novel.
2. The proposed BLADE dataset is important to the field.
3. The experiments are extensive, especially the comparison of different approaches to fuse layout information is insightful.

### Weaknesses
1. Although the experimental results in Tables 2 and 3 demonstrate the superiority of GPE, the results in Table 1 appear somewhat contradictory to those in Tables 2 and 3, requiring further explanation or experiment.
2. The paper needs a section discussing why GPE is effective in guiding attention heads to focus on different positional views. Including a visualization of attention scores or similar analysis would provide valuable insights, as the improved performance alone is insufficient to fully explain the mechanism.

3. The writing requires improvement, as several paragraphs are vague and difficult to understand. For example:
(1) Lines 248-249: What is the value of lambda? Does GPE discretize all coordinates into integers, allowing us to obtain position embeddings for specific position?
(2) Line 418: In the experiment regarding reading order, I cannot understand the difference between W/O and LOCAL. A concrete example would help illustrate the distinctions between each setting.
(3) Line 473: It would be helpful to introduce the design of the group function where it first appears, in Section 3.2, using a formal mathematical definition. This would clarify the paragraph, as I found it confusing without prior context on the group function.

### Questions
See weakness

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a simple yet effective method, Group Position Embedding (GPE), for encoding spatial positional information in LLM-based document understanding tasks. This technique enables LLM models to comprehend document layouts without altering their architectures. Additionally, the authors introduce a new benchmark, BLADE, for evaluating complex document processing.

### Strengths
1.This paper introduces a simple layout embedding approach, termed Group Position Embedding (GPE), for enhancing LLM-based document understanding.
2.This paper proposes a new benchmark, BLADE, designed for the evaluation of complex document evaluation. 
3.Extensive ablation experiments have been conducted to validate the effectiveness of GPE.

### Weaknesses
1. The rationale behind GPE is unclear. The introduction section fails to adequately explain the workings of the group position embedding, instead, it merely highlights the advantages without providing underlying reasons. It is also unclear what the principles and feasibility of the mapping function g_r() are, and the distinction between Gr(k) and Gr(i) on lines 196-197 is also not elucidated. Further explanation is needed on how the n-dimensional spatial position is mapped into different attention heads. The meaning of the hyperparameter scaling factor \lambda and its impact on the approach should also be clarified.
2. This paper is not the first to utilize head-specific layout position embeddings. Previously, LAGaBi [https://aclanthology.org/2023.findings-emnlp.521/] employed diverse Gaussian kernels to encode relative positional information for each attention head. 
3.The paper's writing quality is subpar. Inconsistent and non-standard academic expressions are used. For instance, in LLMs, l typically denotes the number of layers rather than dimensions, which should be represented by d or dim. The figures do not clearly demonstrate the mapping mechanism of group position embedding and convey some ambiguity. For instance, Figure 1 shows that only the key-state and value-state encode n-dimensional spatial position information, whereas the query-state receives only 1-dimensional position information, which is confusing.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
1

### Contribution
2
