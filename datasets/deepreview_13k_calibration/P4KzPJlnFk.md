# Biology Instructions: A Dataset and Benchmark for Multi-Omics Sequence Understanding Capability of Large Language Models

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 5, 3, 5

## Abstract
Large language models have already demonstrated their formidable capabilities in general domains, ushering in a revolutionary transformation. However, exploring and exploiting the extensive knowledge of these models to comprehend multi-omics biology remains underexplored. To fill this research gap, we first introduce Biology-Instructions, the first large-scale multi-omics biological sequences-related instruction-tuning dataset including DNA, RNA, proteins, and multi-molecules, designed to bridge the gap between large language models (LLMs) and complex biological sequences-related tasks. This dataset can enhance the versatility of LLMs by integrating diverse biological sequenced-related tasks with advanced reasoning capabilities, maintaining conversational fluency. Additionally, we reveal significant performance limitations in even state-of-the-art LLMs on biological sequence-related multi-omics tasks without specialized pre-training and instruction-tuning. We further develop a strong baseline called ChatMultiOmics with a novel three-stage training pipeline, demonstrating the powerful ability to understand biology by using Biology-Instructions. Biology-Instructions and ChatMultiOmics are publicly available and crucial resources for enabling more effective integration of LLMs with multi-omics sequence analysis.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents "Biology-Instructions," a comprehensive dataset for training LLMs on multi-omics biological sequences. The authors developed ChatMultiOmics, a biology-specific model using a three-stage pipeline: unsupervised pre-training, instruction tuning, and reasoning-based fine-tuning. This approach enhances LLMs' performance in multi-omics tasks while maintaining conversational abilities. Extensive benchmarking shows ChatMultiOmics outperforms general-purpose and some specialized LLMs in sequence-based tasks.

### Strengths
Novel Dataset: The introduction of "Biology-Instructions" provides a new, large-scale dataset specifically tailored for multi-omics data (DNA, RNA, proteins, and multi-molecular sequences). This fills a crucial gap, as most current datasets in bioinformatics lack instruction-tuning data suited for large language models (LLMs) in multi-omics contexts.

### Weaknesses
1. Lack of Evaluation on Practical Applications: The model is mainly evaluated on isolated multi-omics tasks without a clear link to practical bioinformatics applications (e.g., case study on real-world drug discovery, wet-lab experiments design). This might limit its perceived impact outside academia.

2. Dataset Limitations: The "Biology-Instructions" dataset, while comprehensive for single-modality tasks (DNA, RNA, protein), lacks representation of cross-modality interactions essential for understanding complex biological networks. Limited inclusion of DNA–RNA–protein interactions hinders the model's ability to learn integrated biological insights. Examples of missing interactions include DNA–RNA regulatory loops, DNA–protein binding in gene expression control, RNA–protein associations for post-transcriptional modifications, and multi-molecule complexes like the spliceosome or transcription initiation complex Expanding the dataset to include diverse cross-modality interactions would allow models like ChatMultiOmics to more accurately represent complex cellular processes and enhance its real-world applications.

3. Potential for Data Leakage: The study fails to address or discuss potential data leakage or overlap between training and test sets. This is particularly concerning given the multi-omics nature of the dataset, where DNA, RNA, and proteins are interconnected through the central dogma of molecular biology. Such overlap could significantly impact the validity of the reported performance metrics.

4. Limited Error Analysis: The study lacks an in-depth error analysis, especially for tasks where the model performs poorly. Without this, it's difficult to identify specific weaknesses or areas for improvement in ChatMultiOmics.

5. Cell type-specificity: The "Biology-Instructions" dataset lacks cell-type specificity, a crucial factor for accurate biological modeling. Different cell types have unique gene expression profiles, regulatory networks, and molecular interactions that reflect their specialized functions. Without cell-type-specific data—such as neuron-specific RNA splicing, immune cell signaling, or hepatocyte-specific metabolism—the model may produce overly generalized predictions that miss cell-specific nuances. This limitation reduces the model's usefulness for research on tissue-specific diseases, drug development, and precision medicine.

### Questions
1. Comparative Performance with Specialized Models: How does ChatMultiOmics compare to established bioinformatics models (including non-LLM models like protein or RNA language models) in specialized tasks?

2. Interpretability of Predictions: How interpretable are the model's outputs, especially for complex interactions like enhancer-promoter binding or multi-molecular tasks? Does the model's reasoning path take into account its own interpretability?

3. Extension to Additional Omics: Can the model’s framework and dataset be adapted to other omics, such as metabolomics or microbiomics, and what would be the challenges involved?

### Soundness
2

### Presentation
2

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
This paper introduces “Biology-Instructions,” a large-scale multi-omics biological sequence-related instruction-tuning dataset encompassing DNA, RNA, proteins, and multi-molecules. This dataset aims to enhance LLMs’ ability to handle various biology-related tasks. It proposes a new training pipeline, “ChatMultiOmics,” demonstrating improvements in biological sequence understanding.

### Strengths
It bridges the gap between LLMs and biological sequence understanding through a new dataset and benchmarking tool called “Biology-Instructions.”

### Weaknesses
The study shows that LLMs require specialized pre-training to perform effectively on biology-related tasks, which may not be feasible or practical in all research settings.

Although the paper introduces a novel dataset and training method, it mainly reaffirms the importance of specific pre-training rather than providing new insights into biological sequence understanding.

The dataset may exhibit imbalances where certain categories are more represented than others. This could lead to the model overfitting to tasks with more data during training while neglecting tasks that have less data.

It appears that there is a lack of a data availability statement.

### Questions
See weakness.

### Soundness
2

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
This paper introduces a large-scale, multi-omics biological sequences-related instruction-tuning dataset and a biologically focused large language model (LLM) using a three-stage training pipeline to incrementally incorporate domain knowledge. The proposed model demonstrates superior performance across 21 biological sequence-related multi-omics tasks compared to state-of-the-art (SOTA) LLMs. The paper is well-structured, easy to follow, and provides numerous technical details.

### Strengths
Comprehensive Dataset: The introduction of a large-scale, multi-omics dataset is a valuable resource for the community.
Three-Stage Training Pipeline: The gradual incorporation of domain knowledge through a three-stage training pipeline is a thoughtful approach.
Performance: The model shows superior performance in a variety of tasks, highlighting its potential utility.

### Weaknesses
Technical Novelty: While the paper is resource-rich, it offers limited technical novelty. It primarily serves as a resource article.
Training Sample Size: The model is trained on 3 million samples, which is relatively small given the vast space of DNA, RNA, and proteins (in the billions) and the number of parameters in the LLM (8B Llama3.1).
Alignment of Human and Biological Language: The model's alignment of human language with biological language is an interesting concept but could be explored further.

Figure 7: There appears to be a discrepancy in the results. How can the model without stage 1 and stage 3 (third row) perform much better than the model without stage 1 (second row)? Is this a typo?
Figure 6: The figure is difficult to interpret as the methods are clustered together. A table might provide a clearer comparison.
Insights: The four findings presented seem intuitive and do not offer particularly novel insights.
Mixed Score Formula: The paper should include the formula for the mixed score used in single-label regression to enhance clarity.

### Questions
Figure 7: There appears to be a discrepancy in the results. How can the model without stage 1 and stage 3 (third row) perform much better than the model without stage 1 (second row)? Is this a typo?
Figure 6: The figure is difficult to interpret as the methods are clustered together. A table might provide a clearer comparison.
Insights: The four findings presented seem intuitive and do not offer particularly novel insights.
Mixed Score Formula: The paper should include the formula for the mixed score used in single-label regression to enhance clarity.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new dataset and model, Biology Instructions and ChatMultiOmics, designed for multi-modal biological data. The dataset distinguishes itself by unifying DNA, RNA, and protein data types, which were previously treated separately. The model undergoes three stages of training: continual pretraining, supervised fine-tuning (SFT), and reasoning training. After training on the Biology Instructions dataset, ChatMultiOmics demonstrates superior performance over state-of-the-art baselines on 21 tasks curated by the authors.

### Strengths
1-Unified Multi-Omics Dataset: By integrating DNA, RNA, and protein sequences within a single dataset, this work allows ChatMultiOmics to leverage a more comprehensive representation of biological data. This approach enables the model to capture cross-modal relationships that traditional, single-modal datasets cannot, potentially enhancing predictive power in complex biological systems.

2-Performance on Custom Benchmark: The model demonstrates improved performance on 21 tasks specifically designed by the authors. These tasks, which span classification, regression, and possibly other benchmarks within the domain, provide a new set of evaluation standards. The demonstrated gains in performance could serve as a reference point for future biological language models seeking to handle multiple data types concurrently.

3-Empirical Training Insights: The work contributes an empirical analysis of training methodologies suited to biological data. By introducing three distinct stages of training—continual pretraining, supervised fine-tuning, and reasoning training—the authors outline a potentially generalizable approach that may benefit future model development for multi-modal biological applications.

### Weaknesses
1-Focus Solely on Predictive Tasks: While the model excels in predictive tasks, the lack of generative experiments, such as protein and DNA design, limits its versatility. Generative tasks are becoming increasingly relevant, where designing novel sequences with specific functionalities is critical. Including generative experiments could enhance the paper by showing the model's potential in creating or optimizing biological sequences. The generative task is of the highest interest.

2-Lack of Structural Data Integration: The model currently relies only on sequence data as input, which, while valuable, is limited. In biological systems, structural information is crucial, as the 3D structure of molecules like proteins often determines their function. Incorporating structure data, such as 3D coordinates from protein databases (e.g., PDB), could enhance predictive capabilities.

3-Evaluation Limited to In-House Dataset: The performance metrics presented are limited to the authors' own test dataset, which limits the generalizability of the results. Reporting the model's performance on established, domain-specific datasets in DNA and protein domains, such as those used in ChatNT, ProLLaMA, and InstructProtein, would add robustness to the claims of improvement and allow a better assessment of the model's comparative advantages. Otherwise, it is unfair to judge the proposed model with others.

4-Minor language issues: in Line 315, "We" should be "we"; in Line 290, "Figure 10" should be "Table 10."

### Questions
1-Definition of Reasoning in Stage 3: Could you clarify what "reasoning" entails in the context of Stage 3 training? Specifically, how does reasoning differ from the classification and regression tasks in Stage 2? "Step-by-step" prompting alone does not fully justify the use of the term "reasoning," as true reasoning often involves complex inferencing, such as multi-hop or chain-of-thought reasoning. Did you explore techniques like chain-of-thought prompting, where the model reasons through intermediate steps, or alternative strategies that might better align with reasoning tasks?

2-IChoice of LoRA+ vs. Full-Parameter Pretraining in Stage 1: I am curious about the decision to use LoRA+ for continual pretraining instead of a full-parameter approach. Full-parameter pretraining could potentially offer stronger alignment with downstream tasks by updating the entire model. Additionally, I wonder if incorporating text data (e.g., biological literature or annotations) in Stage 1 could mitigate forgetting and enhance the model's knowledge base for better contextual understanding. This could enrich the model with domain knowledge without the constraints of task-specific fine-tuning alone.

3-Limiting Data to Human-Specific DNA and RNA: What was the rationale for restricting DNA and RNA data to human species only? Incorporating non-human data, including model organisms (e.g., E. coli, C. elegans, D. melanogaster), could improve the model's generalization and relevance to broader biological contexts, especially in fields like comparative genomics and evolutionary studies.

4-Enhancing Dataset Diversity with Multi-Hop Connections: The current dataset lacks multi-hop connections, which could limit the model’s ability to perform complex reasoning over interconnected data points. Mixing this dataset with established datasets from different domains, or incorporating multi-hop relational data, could enhance diversity and enable the model to capture deeper biological relationships. I am particularly interested in the potential for training another model with such a mixed dataset, as this could yield a more robust model capable of handling complex biological queries across domains.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper present a new extensive dataset called Biology-Instructions, which aims to enhance the ability of LLMs in comprehending multi-omics biological sequences like DNA, RNA, proteins, and multi-molecules. This dataset supports 21 tasks across various omics types and intends to bridge the gap between LLMs and complex biological sequence-related tasks. Additionally, the authors introduce an impressive baseline model named ChatMultiOmics that utilizes a three-stage training pipeline involving continued pre-training on biological sequences, extensive instruction tuning, and reasoning instruction tuning. Experimental results demonstrate significant performance improvements compared to existing general-purpose and biology-specific LLMs.

### Strengths
1. The paper introduces a comprehensive multi-omics instruction-following dataset, which significantly extends the application of LLMs to biological domains.
2. The three-stage training pipeline for ChatMultiOmics addresses existing limitations in instruction tuning for biological tasks.
3. The introduction of Biology-Instructions and ChatMultiOmics could drive advancements in computational biology, particularly in tasks like genetic regulation and therapeutic development. The dataset can potentially become a benchmark for future research.

### Weaknesses
1. While the dataset covers many tasks, it does not include all multi-omics interactions, and more complex regulatory networks are underrepresented. This limits the scope of the model’s generalizability. Specifically, the dataset seems to focus on pairwise interactions between omics modalities, neglecting higher-order interactions and feedback loops that are crucial in biological systems. For example, the interplay between transcription factors, chromatin accessibility, and RNA expression is not explicitly captured, which is a significant limitation for modeling complex biological processes.
2. The training process is impacted by task imbalances, which could affect the model’s ability to handle underrepresented tasks. The paper does not provide a detailed analysis of the distribution of examples across the 21 tasks, making it difficult to assess the severity of this issue. It is likely that some tasks, such as those involving less studied omics modalities or complex interactions, have significantly fewer training examples, potentially leading to biased model performance.
3. The third stage of training (reasoning instruction tuning) showed adverse effects on some regression tasks, indicating that further optimization of the training process is necessary. The paper lacks a clear explanation of why this occurs, making it difficult to pinpoint the exact cause. It's possible that the reasoning data used in this stage is not well-suited for regression tasks, or that the model is overfitting to the reasoning data at the expense of regression accuracy.

### Questions
1. Given the challenges posed by task imbalance in the dataset, does the trained model exists bias?
2. Could you provide more insights into why reasoning instruction tuning negatively impacted some regression tasks? Would a different approach to integrating reasoning data be beneficial?
3. What is main differerence compared with other bio-LLM dataset? such as Mol-Instruction. Your dataset construction process is very similar to Mol-Instruction.
4. Can you provide more details of data quality control process? especially for the reasoning data.
5. How about the performance of task-specific models? such as the conventional SOTA model for RNA-Protein Interaction Prediction. How does ChatMultiOmics compare to it?

### Soundness
3

### Presentation
2

### Contribution
3
