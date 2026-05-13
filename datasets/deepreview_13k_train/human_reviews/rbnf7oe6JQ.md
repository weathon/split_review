# CircuitFusion: Multimodal Circuit Representation Learning for Agile Chip Design

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
The rapid advancements of AI rely on the support of integrated circuits (ICs). However, the growing complexity of digital ICs makes the traditional IC design process costly and time-consuming. In recent years, AI-assisted IC design methods have demonstrated great potential, but most methods are task-specific or focus solely on the circuit structure in graph format, overlooking other circuit modalities with rich functional information. In this paper, we introduce CircuitFusion, the first multimodal and implementation-aware circuit encoder. It encodes circuits into general representations that support different downstream circuit design tasks. To learn from circuits, we propose to fuse three circuit modalities: hardware code, structural graph, and functionality summary. More importantly, we identify four unique properties of circuits: parallel execution, functional equivalent transformation, multiple design stages, and circuit reusability. Based on these properties, we propose new strategies for both the development and application of CircuitFusion: 1) During circuit preprocessing, utilizing the parallel nature of circuits, we split each circuit into multiple sub-circuits based on sequential-element boundaries, each sub-circuit in three modalities. It enables fine-grained encoding at the sub-circuit level. 2) During CircuitFusion pre-training, we introduce three self-supervised tasks that utilize equivalent transformations both within and across modalities. We further utilize the multi-stage property of circuits to align representation with ultimate circuit implementation. 3) When applying CircuitFusion to downstream tasks, we propose a new retrieval-augmented inference method, which retrieves similar known circuits as a reference for predictions. It improves fine-tuning performance and even enables zero-shot inference. Evaluated on five different circuit design tasks, CircuitFusion consistently outperforms the state-of-the-art supervised method specifically developed for every single task, demonstrating its generalizability and ability to learn circuits' inherent properties.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a multi-modal representation method for agile digital IC design. 
Evaluations show that the proposed method achieves significant performance improvement over several SOTA methods.

### Strengths
The paper proposes to use multimodal representations to estimate digital IC performance efficiently. This strategy is novel as compared to previous LLM-based methods.

The technique details on how to encode each modality and fuse modalities are elaborated clearly.

The paper comprehensively evaluates multiple tasks and compares them with many SOTA methods to show the impressive performance of the proposed method.

An ablation study is also performed to show the impact of each individual modality on the estimation error.

### Weaknesses
It is unclear why a summary-centric fusion is used to fuse the three modalities, lacking quantitative support.

It is unclear how the netlist encoder is pre-trained.

The comparisons with previous methods are unfair since the reported results are not based on the same number of model parameters across all baselines.

### Questions
Q1: How do you label data for fine-tuning?

Q2: How long does it take for pre-training and fine-tuning the model?

Q3: How are the correlation coefficient (R) and mean absolute percentage error (MAPE)in Table 2 obtained? I.e, Based on a single inference or multiple inferences?

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
1

### Summary
This paper introduces an approach to circuit representation learning using multimodal fusion and implementation-aware alignment.

### Strengths
* The paper is structured well and easy to follow. All training steps and the proposed methodology is clearly illustrated with representative figures, these make it easy to follow and understand the proposed approach and results.
* Evaluations are comprehensive and comparison are done against many recent methods. 
* The approach of this fusion approach that overcomes the hardware unique (P1 to P4) looks novel and interesting.

### Weaknesses
 * The dataset contains only 41 RTL designs, this might not be representative of the entire space. It would be nice to demonstrate the effectiveness of the proposed method on a wider range of dataset.


### Questions
* For sequential logic, how well does it handle logics with multiple clocks? Can it optimize such tasks?

### Soundness
2

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
3

### Summary
This paper proposed a multimodal and implementation-aware circuit encoder. It encodes circuits into general representations that support different downstream circuit design tasks with three modalities: hardware code, structural graph, and functionality summary. CircuitFusion demonstrates excellent generalizability and the ability to learn circuits’ inherent properties compared to state-of-the-art supervised methods in the empirical study.

### Strengths
• This paper proposes the first multimodal fused and implementation-aware circuit encoder that fuses three modalities (i.e., HDL code, structural graph, and functionality summary). 
• CircuitFusion outperforms state-of-the-art (SOTA) task-specific supervised models in design quality evaluation task empirically
• CircuitFusion is able to perform few-shot and zero-show inference.

### Weaknesses
• Most existing multi-modality encoders, such as CLIP, seem to be mainly used as a controller for generation, such as stable diffusion text to image generation. This paper, however, uses it as an evaluator, which I personally feel does not fit the purpose. 
• I feel the argument about scalability is not significant enough to consider as one of the strengths. Since deep learning models are naturally scaled with larger datasets, and such large datasets are not available right now and may not be available in the future due to the IP issue, achieving excellent results with limited data is more important than scalability to large but nonexistent datasets.

### Questions
Could you provide examples from related work where multimodal models have been successfully used for evaluation tasks, particularly in hardware or software domains? Additionally, could you elaborate on the specific advantages that a multimodal approach offers for circuit evaluation tasks compared to traditional unimodal methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper designs a CircuitFusion pre-training workflow to achieve an implementation-aware representation of RTL codes. The CircuitFusion aligns three RTL modalities(hardware code, structural graph, and functionality summary) with corresponding netlists and encodes them to an embedding vector for RTL design quality evaluation. The paper also presents a retrieval-augmented inference flow to improve fine-tuning and enable zero-shot.

I read the rebuttals and decided to keep my decision.

### Strengths
1. The CircuitFusion successfully encodes and aligns the hardware code, structural graph and functionality summary of RTL into an embedding vector and achieves SOTA performance. During pre-training, techniques include masked modeling, contrastive learning and mixup embedding summary matching are employed to enhance the model's understanding of circuit functionality.

2. This paper introduces a register-based circuit splitting method to enable fine-grained encoding and detailed representation with low computational complexity and scalability.

3. This paper proposes a retrival-augmented inference method to enable the model to integrate external knowledge effectively, leading to improvements in both zero-shot and few-shot learning scenarios.

4. Sufficient ablation studies and experimental evaluations are conducted to valitate the necessity of the above arrpoachs.

### Weaknesses
1. Regarding the technical novelty of this work, a related work was published on ICCAD 2024, named RTLRewriter [1]. Many techniques are similar to each other. RTLRewriter is a multimodal one that considers manual, code, and notes and also incorporates graph partitioning techniques, retrieval-augmented inference, etc. 

2. During zero-shot inference, it is not reliable to simply average the performance metrics of retrieved similar circuits to make predictions. This issue seems to be reflected in the experimental results in Table 3, where the performance decreases with the increased available retrievals. Meanwhile, sufficient circuit data is required when building a VectorStore with quality metrics, which contradicts the concept of zero-shot inference.

3. The CircuitFusion implements summary-centric fusion to achieve alignment with information from other modalities. However, this approach may result in an underrepresentation of structural information or code-level details, which could be particularly important in timing, power and area performance. Additional experiments and explanations are needed to demonstrate the necessity of the summary mode.

4. The downstream applications should be further elaborated. Specifically, how to adjust the RTL design based on the obtained performance predictions warrants more detailed discussion. Currently, this work shows less relevance to the title's concept of 'agile chip design', as it does not adequately illustrate how CircuitFusion can be effectively applied to the optimization of RTL code. Prior works: [1] uses the encoded different modal RTL for new code reconstruction. [2] can notate detailed timing information on HDL and set fine-grained optimization options in the synthesis script for optimization applications.

5. The uploaded source code for CircuitFusion lacks readability and is hard to run. For example, many of the files mentioned in the README do not exist (data_bench, pretrain_model, pos and others).

### Questions
1. This paper regards the performance of synthesized netlists as the RTL quality metrics. However, one RTL code can be synthesized into many gate-level netlists based on different configurations and optimization objectives, can the authors provide a detailed description on the selection of representative gate-level netlists, to represent the true performance of RTL and guide optimization.

2. In Table 3, please explain why the prediction error of CircuitFusion increases with the number of retrievals. 

3. There is an inherent issue of information asymmetry between different circuit modalities, and it can be computationally expensive to calculate the similarity and alignment between these features. Can the authors provide more evidence to demonstrate that the summary-centric approach is more effective compared to simple alignment or using other modalities as the central focus?

### Soundness
3

### Presentation
3

### Contribution
3
