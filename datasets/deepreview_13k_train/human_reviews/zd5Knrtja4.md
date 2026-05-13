# TimeRAF: Retrieval-Augmented Foundation model for Zero-shot Time Series Forecasting

- Decision: Reject
- Scores: 6, 6, 3, 5

## Abstract
Time series forecasting plays a crucial role in data mining, driving rapid advancements across numerous industries. 
With the emergence of large models, time series foundation models (TSFMs) have exhibited remarkable generalization capabilities, such as zero-shot learning, through large-scale pre-training. 
Meanwhile, Retrieval-Augmented Generation (RAG) methods are widely employed to enhance the performance of foundation models on unseen data, allowing models to access to external knowledge. 
In this paper, we introduce **TimeRAF**, a **R**etrieval-**A**ugmented **F**orecasting model that enhance zero-shot time series forecasting through retrieval-augmented techniques.
We develop customized time series knowledge bases that are tailored to the specific forecasting tasks.
TimeRAF employs an end-to-end learnable retriever to extract valuable information from the knowledge base.
Additionally, we propose Channel Prompting for knowledge integration, which effectively extracts relevant information from the retrieved knowledge along the channel dimension.
Extensive experiments demonstrate the effectiveness of our model, showing significant improvement across various domains and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed TimeRAF, a Retrieval-Augmented Forecasting model that enhances zero-shot time series forecasting by using customized knowledge bases and a learnable retriever to integrate external knowledge, demonstrating significant improvements across various domains and datasets.

### Strengths
1.	Paper writing is good. There is no difficulty in understanding the paper.

2.	The proposed method is straightforward and achieves state-of-the-art performance.

3.	Comprehensive ablation studies and other evaluations are conducted to check the effects of the model

### Weaknesses
1.	The major novelty is the utilization of RAF for time series modeling. However, in terms of RAF itself, the novelty is quite limited.

2.	The difference with the previous RAF for time series is unclear. In the related work section, the author claimed that ‘existing time series RAG methods are either limited to historical data or do not support foundation models’ and provided two citations. However, it seems the gap is not significant. Could the authors elaborate more on this motivation?

3.	In line 192, the authors claimed ‘retrieve information solely from datasets that are distinct from the input source’. What is the distinction here? How to define it.

4.	In line 226, the authors mentioned ‘By weighing the importance of different components of the combined embedding’. However, it seems the average of the embeddings is calculated. Thus, how to weigh them.

5.	In line 244, the authors mentioned ‘it is challenging to guarantee that retrieved candidates’. What is the reason?

6.	In the ablation study of the choice of knowledge base, the authors mentioned ‘TimeRAF engages a meticulously curated multi-domain dataset’. This implies the domain of an input time series should exist in the base. However, what would happen if a new domain emerges (e.g., stock) but the base contains no such time series?

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduce a novel framework TimeRAF designed to leverage retrieval-augmented generation for zero-shot time series forecasting. The authors develop customized time series knowledge bases that are tailored to the specific forecasting tasks and employ an end-to-end learnable retriever to extract valuable information from the knowledge base. Through comprehensive experimental discussions, the manuscript demonstrates the effectiveness of the proposed approach beyond existing works.

### Strengths
S1. The manuscript is well-written. And, the presentation of figure is clear and easy to understand.

S2. The experiments are comprehensive, and provide some interpretable discussion to analyze why the model is good.

S3. The research is novel and unresearched in the field.

### Weaknesses
W1. Could you provide the source code to enhance the reviewers' trust in the reproducibility of your work?

W2. The introduction of the retrieval process inevitably leads to increased time cost, so I am concerned about the model's efficiency. I believe it is essential to add some theoretical analysis and empirical discussions.

W3. Have you considered the issue of label leakage introduced by RAG in the process of building the knowledge base? Different datasets may have very similar or identical temporal patterns, which could also lead to potential label leakage problems.

### Questions
Q1. On the Electricity dataset, the performance of TimeRAF is not the best. Could you analyze the reasons for this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method for few-shot and zero-shot time series forecasting. This method applies an RAG style to aids forecasting, where it retrieves some helpful data from a pre-collected dataset. The retriever is learnable and can calculate retrieval scores to select most relevant data. To integrate retrieved data, the author proposes a Channel Prompting way to extract valuable information. Overall the paper is easy to understand.

### Strengths
1. The paper is well-written and easy to understand
2. It combines retrieval-augmented models with TS, contributing to the efficient model adaptation.

### Weaknesses
1.The improvement shown by RAF in Fig. 3 is marginal(only 0.00x improvement in most datasets), which is the core issue and raises concerns about whether the pre-trained model used is already too powerful, thus reduces the necessity of RAF process.

2. The author should give the memory usage for storing retrieval data and its time cost, especially when compared to storing a foundation model directly.

3. The evaluation datasets are limited. It would be valuable to assess the model’s performance on cross-domain datasets that extend beyond the original knowledge base.

### Questions
1. The details of retrival, how much data is used for forecasting after retrieval in TimeRAF?
2. The memory and time costs associated with the retrieval process.
3. The pre-training backbone appears too powerful, limiting the visible improvements. Have the authors explored replacing the backbone with alternative foundation models to better understand the effectiveness of RAF?

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
4

### Summary
This paper introduces **TimeRAF**, a Retrieval-Augmented Forecasting model designed to enhance so-called zero-shot time series forecasting by leveraging retrieval-augmented techniques. The model integrates external time series knowledge bases to supplement forecasting tasks, employing an end-to-end learnable retriever.

### Strengths
1. The article is well-structured.
2. Some experiments are meaningful.

### Weaknesses
1. **Channel Prompting Efficiency Concern**:  
   If I understand correctly, **Channel Prompting** requires each channel to process and fuse information from **k retrieved time series**. This may introduce significant computational overhead, especially for datasets with many channels (e.g., **traffic data**). The paper lacks an analysis of the efficiency and scalability of this mechanism in such scenarios. Furthermore, the claim that channel-independence leads to efficiency and scalability is not valid. The result of channel-independence is that each multivariate time series requires querying channel * k external time series data, while without channel-independence, only k external time series are required (i.e., the same set of multivariate time series shares k external time series).

2. **Lack of Pre-training Details for TSFM**:  
   The paper omits essential information about the **pre-training process** of the time series foundation model (TSFM), such as the **datasets used, training procedure, and loss functions**. This raises concerns about the reproducibility and transparency of the method. While the authors claim to use a pre-trained model, the significant discrepancy between their reported results and the original paper's results for the same pre-trained model raises concerns about the validity of their implementation.

3. **Misinterpretation of Zero-Shot Learning**:  
   I disagree with the zero-shot setup in the paper. True zero-shot learning implies that the model is tested on datasets it has **never seen during training**. For example, training on **ETTh1** and testing on **ETTh2** would align with this standard. However, as depicted in **Figure 2**, TimeRAF appears to fine-tune both the retriever and forecaster on parts of the test data, which **violates the principles of zero-shot forecasting**. The authors could refer to **GPT4TS or TimeLLM's zero-forecasting setup** for a more rigorous zero-shot methodology.

4. **Unfair Comparison in Experiments (Table 2)**:  
   The experiments reported in **Table 2** are not entirely fair. According to **Section 4.1**, TimeRAF uses an input length of **512**. For fair comparison, **all baselines** should have the same input length. However, the reported metrics for baselines like **iTransformer, PatchTST, and DLinear** do not correspond to **input length = 512**. I have run these models with input lengths of **512**, and the results (e.g., PatchTST on **ETTm1** with 96-step forecast: 0.292, and **ETTm2**: 0.165) differ significantly from those reported in the paper. The use of different input lengths for baseline comparisons diminishes the reliability of the experimental results. Furthermore, the authors use results from other papers for full-shot methods, while using their own implementation for the TTMB backbone, without clearly stating this in the main text.

5. **Incomplete Experimental Results**:  
   The paper only reports results for a single forecast length (**96**). To comprehensively demonstrate the effectiveness of TimeRAF, it is essential to present results for **multiple forecast horizons** (e.g., **96, 192, 336, and 720**). This would provide a more complete evaluation of the model’s performance. The provided results for other forecast lengths are not convincing, as the full scripts for all steps were not provided, and the results without RAF do not match the original TTM paper's results.

6. **Typos and Grammar Issues**:  
   There are several typos and grammatical errors in the paper. For example:
     - **Lines 53-70**: “our exploration of Retrieval-Augmented for time series Forecasting (RAF)” is awkwardly phrased.  
     - **Line 301**: “...updating the retriever,, the whole...” has an extra comma.  
   The authors should carefully proofread the paper to improve its clarity and polish.

7. **Missing Axis Labels in Figure 5**:  
   **Figure 5** lacks a **y-axis label**, which makes it difficult to interpret the results. Proper labeling is essential for readers to understand the figures accurately.

8. **Scaling Issue in Retrieval-Augmented Forecasting**:  
   One important concern is how TimeRAF handles cases where the **retrieved time series data** are in **different magnitudes** than the input data. It would be useful if the authors could elaborate on any **normalization or scaling techniques** employed to address this issue. Even after normalization, significant differences in data distribution may still exist, which could hinder effective integration.

9. **Implementation Details for Database Usage (Section 3.3)**:  
   The paper mentions that **non-similar data** are used during training, while **similar data** are used during inference (Section 3.3, lines 187-193). However, the specific **implementation details** of how this is done for different datasets are unclear. Providing more insights here would enhance the paper's reproducibility and understanding.

10. **Lack of Code Availability**:  
   The authors do not provide **code** for their experiments. Releasing code is crucial for **reproducibility** and would allow the community to verify the results and build upon the work.

### Questions
1. How scalable is the Channel Prompting mechanism for high-dimensional datasets with many channels?
2. How does TimeRAF ensure consistent scaling between retrieved external time series data and input data to avoid magnitude mismatches?
3. Why do the authors claim a zero-shot setup if the model fine-tunes on test data? How does this setup align with the standard definition of zero-shot forecasting?
4. What datasets and loss functions were used to pre-train the TSFM? How does the pre-training contribute to the model’s performance? 
5. Can the authors provide results for other forecast lengths (e.g., 192, 336, and 720) to validate TimeRAF's generalization capability across multiple horizons?

### Soundness
2

### Presentation
2

### Contribution
2
