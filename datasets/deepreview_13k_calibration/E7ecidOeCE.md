# Selecting Influential Samples for Long Context Alignment via Homologous Models’ Guidance and Contextual Awareness Measurement

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
The expansion of large language models to effectively handle instructions with extremely long contexts has yet to be fully investigated.
The primary obstacle lies in constructing a high-quality long instruction-following dataset devised for long context alignment.
Existing studies have attempted to scale up the available data volume by synthesizing long instruction-following samples.
However, indiscriminately increasing the quantity of data without a well-defined strategy for ensuring data quality may introduce low-quality samples and restrict the final performance.
To bridge this gap, we aim to address the unique challenge of long-context alignment, i.e., modeling the long-range dependencies for handling instructions and lengthy input contexts. 
We propose \textbf{GATEAU}, a novel framework designed to identify the influential and high-quality samples enriched with long-range dependency relations by utilizing crafted
\textbf{Homologous Models' Guidance (HMG)} and \textbf{Contextual Awareness Measurement (CAM)}.
Specifically, HMG attempts to measure the difficulty of generating corresponding responses due to the long-range dependencies, using the perplexity scores of the response from two homologous models with different context windows.
Also, the role of CAM is to measure the difficulty of understanding the long input contexts due to long-range dependencies by evaluating whether the model’s attention is focused on important segments.
Built upon both proposed methods, we select the most challenging samples as the influential data to effectively frame the long-range dependencies, thereby achieving better performance of LLMs.
Comprehensive experiments indicate that GATEAU effectively identifies samples enriched with long-range dependency relations and the model trained on these selected samples exhibits better instruction-following and long-context understanding capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
To effectively handle instructions with extremely long contexts in expansion of large language models (LLMs), this paper proposes GATEAU, a novel framework designed to identify the influential samples enriched with long-range dependency relations by utilizing crafted Homologous Models’ Guidance (HMG) and Contextual Awareness Measurement (CAM). Specifically, HMG uses the perplexity scores of the response from two homologous models to measure the ability in modeling long-range dependencies. CAM is used to measure difficulty of understanding the long input contexts by evaluating whether the model’s attention is focused on important segments. Extensive experiments on several LLM benchmarks demonstrate the effectiveness of the proposed algorithms.

### Strengths
(1)	This paper proposes an efficient and practical influential-sample-selecting algorithm for long context alignment of large language model. The motivation of the HMG and CAM component is clearly explained in Section 3.

(2)	The organization of this paper is clear and easy to follow. The notations used in Section 3 are all well clarified.

(3)	The experiments are truly extensive, validating the effectiveness of the proposed methods. In particular, the SOTA result in Tables 1-4 is a surprise for me that using part (e.g. 10\%) of the whole dataset can achieve better performance than using the whole dataset. Ablation study in Section 4.3 also verifies the effectiveness of the components (i.e. HMG and CAM).

(4)	Overall, the effort in selecting influential samples for long context alignment in LLM truly makes sense, and the proposed algorithm is simple, motivated, and effective.

### Weaknesses
(1)	In Eq.(2), the explanations for the new notation $\theta _{A}$ and $\theta _{B}$ should follow immediately after their appearance in Eq.(2).

(2)	In Tables 1-4, the captions should be put at the top (instead of the bottom) of the table.

(3)	In section 4.2 Impact of GATEAU, the paper first analyzes the experimental results in Tables 2 and 4 (line 413), and then analyzed the results in Tables 1 and 3 (line 429). It will be better to analyze the experimental results according to the order of Tables.

(4)	The memory storage and running time of the proposed algorithm is missing, which in my opinion can help readers understand the proposed algorithms more comprehensively. For example, in Eq.(2), HMP model uses short context model $\theta _{A}$ and long context model $\theta _{B}$ to compute the perplexity distance, so does the proposed algorithm have more model parameters (e.g. of  $\theta _{A}$ and $\theta _{B}$ ) than the existing algorithm (e.g. only has $\theta _{B}$)? Therefore, I would suggest to add a table to compare the memory burden as well as the execution time with the existing methods on long context alignment.

(5)	It is a surprise for me that in Table 1 and 3, the proposed algorithm with less dataset can achieve SOTA results in all settings. So, can you give some example (whether simulation or real-world dataset, or theoretical analysis) to explain in what kind of situation the proposed algorithm may fail to achieve SOTA results?

(6)	If I understand correctly, in the proposed algorithm, we need to choose some part of the whole dataset (e.g. 10\% or 30\%) to train the model. How does this paper choose this percentage? And in real-life applications, how do we choose the part (whether 10\% or 30\%) from the whole dataset to align LLM?

### Questions
(1)	Could you give some comparisons of memory burden between the proposed algorithms and other exiting methods?

(2)	Could you give some examples to show the failure of the proposed algorithm? It is a little unbelievable that one algorithm can achieve the best performance on all datasets, especially with less training data than existing ones.

(3)	Could you give some insights into the setting of the utilization percentage of the whole dataset of the proposed algorithm?

### Soundness
2

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
This paper proposes a new data selection algorithm, GATEAU, for training long-context instruction following models. Gven a long-context instruction following dataset, the algorithm calculates two metrics: Homologous Models' Guidance (HMG) and Contextual Awareness Measurement (CAM). In particular, HMG measures the difficulty of generating responses due to long-range dependencies by by comparing perplexity scores of responses between two homologous models with different lengths of context windows. CAM measures the difficulty of  utilizing important parts of the long-input by evaluating whether the impoartant segments are being utilized using the attention scores. The author measures the effectiveness of the proposed method on various benchmarks (e.g., LongBench, LongBench-Chat and MT-Bench).

### Strengths
1. The writing is clear (except some questions I have in the Questions section below) and the author explains the proposed method well with clear formulations.
2. The author uses different benchmarks (LongBench, LongBench-Chat, MT-bench, Needle-in-a-haystack) to show the effectiveness of the proposed method on (long/short)-context instruction following tasks.

### Weaknesses
1. 
- The method proposed heavily depends on the perplexity that measures the similarity between the base model's answer and the desired answer. The model $\theta_A$ (e.g., LLaMA-2-7B-base-64k as mentioned in the paper) in the method that calculates the perplexity is a base model (model that only does completion). It does not make sense to measure the perplexity of a base model on an instruction-following dataset because the base model wasn't trained to follow instruction. In this case, the perplexity can be high and it does not accurately measures the difficulty of a document. The author also acknowledges this and in the first metric (HMG) uses a homologous short context model $\theta_B$ as a reference model and calculates the difference between PPL of $\theta_A$ and $\theta_B$. The author claims that this "mitigate the influence brought by lacking other capabilities" (e.g., instruction-following capability, long-context capability). However, there is no guarantee that lacking other capabilities contribute equally in increasing PPL of two models. Essentially the data where the models measure the PPL on is out-of-distribution data (both models were not trained on the instruction-following data and $\theta_B$, which is extended to a longer-context window using zero-shot method, was not trained on long-context data) and model's behavior is unpredictable. Plus, $\theta_A$ was obtained by continual pretraining on long-context data. While HMG assumes $\theta_A$ and $\theta_B$ are similar models, it also depend on what the continual pretraining dataset is (here the method implicitly assumes that the additional dataset is small). If the additional dataset is very large, $\theta_A$ and $\theta_B$ can perform very differently. The core issue is that the perplexity scores from a base model, particularly on long-context data, are not reliable indicators of difficulty for instruction-following tasks. The base model's lack of instruction-following training and the zero-shot extension to long contexts for $\theta_B$ introduce significant uncertainty in the perplexity values, making them questionable for data selection. Furthermore, the assumption that the continual pretraining dataset is small enough to maintain similarity between $\theta_A$ and $\theta_B$ is not rigorously justified, and this similarity is crucial for the validity of the HMG metric.
- Moreover, for second metric (CAM), the LLM that measures the PPL was not trained on instruction-following dataset (and therefore the behavior is unpredictable) and there is no such reference model.

2. LESS [1] is an optimizer-based method that select a subset of instruction-following dataset by estimating data influence (selecting data points that minimizes the validation loss) and this can be as one of the baselines.

Minor issues:
1. For Table 5, current bold numbers are a bit misleading. Usually bold numbers indicate the highest numbers across some category but here it seems the proposed method is bold. Also, for 13B models, it seem the w/o HMG and w/o CAM settings are not reported. Is there a particular reason of not doing so (e.g., computational constraint)? The ablation study on 7B model does show the effectiveness.

### Questions
1. For perplexity guidance (line 377), which $\theta$ do you use ($\theta_A$ or $\theta_B$ -- I am assuming $\theta_B$ here)?
2. What is the context length of MT-Bench? The paper mentions that MT-Bench is for short-context instruction following. Since the proposed method, GATEAU, is designed for long-context, do you have any hypothesis on why it also improves on the short-context instruction following tasks (Table 4)?

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
3

### Summary
The paper introduces GATEAU, a framework aimed at improving the alignment of large language models with long-context data by identifying influential samples. GATEAU leverages two main components: Homologous Models’ Guidance, which assesses the difficulty of generating responses based on perplexity differences between models with varying context windows, and Contextual Awareness Measurement, which evaluates whether models focus on crucial segments in long input contexts. Through these mechanisms, GATEAU selectively curates samples to enhance LLMs' ability to follow instructions with long-range dependencies.

### Strengths
- The paper addresses an important challenge of optimizing data selection for long-context alignment, enhancing LLMs' performance in real-world applications that require handling long, complex contexts.
- The paper provides comprehensive evaluations across multiple tasks and varied compression ratios, which helps illustrate the model’s versatility and effectiveness.
- The methodology for Homologous Models’ Guidance is well-motivated. Leveraging LLM collaboration for data selection is interesting.
- Ablation study and human evaluation are conducted to verify the effectiveness of the method.

### Weaknesses
 - The study only tests on the LLaMA2 family, which may restrict the generalizability of findings. Additionally, HMG relies on perplexity differences between homologous models with different context windows, leaving unclear guidance on applying the technique to other models lacking such variants.
- There is no analysis of the time efficiency of the data selection method. Since CAM requires estimating importance scores for each segment, which may be computationally expensive, time efficiency is a critical factor.
- The CAM module’s process for calculating attention weights is vague, particularly in obtaining the attention weight across tokens in response $y$ to token $t_j$. Including pseudo-code or further clarification would make the implementation more accessible.
- The method of dividing long inputs into equal segments may overlook the fact that important information could span multiple segments. Additionally, segment importance can depend conditionally on other segments, an aspect not accounted for in the current approach.
- The method averages attention across heads and layers without distinguishing them, potentially introducing noise, as different heads or layers may capture varied aspects of the input [1]. Calibrating the attention aggregation could improve focus on relevant input sections.
- Key hyperparameters, such as the number of segments, remain unexplored, missing potential for optimization in specific contexts.

### Questions
Please refer to the weakness part.

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
This paper introduces GATEAU, a data selection framework designed to identify critical instruction samples for long context alignment of LLMs. Specifically, GATEAU consists of two core modules: Homologous Models' Guidance (HMG) and Contextual Awareness Measurement (CAM). HMG assesses the difficulty of generating responses due to long-range dependencies by comparing the perplexity scores of homologous models with varying context windows. CAM measures how effectively a model focuses on relevant segments of extended input. The outputs of HMG and CAM are combined to produce a final ranking criterion for data selection. Extensive experiments indicate that the proposed method significantly enhances the long-context instruction-following capabilities of LLMs.

### Strengths
1. This paper is well motivated. Identifying high-quality long instruction-following samples is essential for improving long context alignment. 
2. The proposed GATEAU aligns naturally with the challenges of long-range dependency modeling, making the methodology intuitive and easy to understand.
3. The authors demonstrate the effectiveness of GATEAU through extensive experiments across multiple benchmarks. The results consistently show that the selected samples significantly improve model performance on both long and short instruction-following tasks.

### Weaknesses
1. The proposed method may assign similar high scores to duplicate or highly similar samples, assuming they contribute independently to model improvement. However, repeated exposure to similar samples may not add incremental value and could even undermine the alignment process of LLMs. Specifically, the framework lacks a mechanism to explicitly penalize or down-weight samples that are semantically close, potentially leading to a skewed training distribution that overemphasizes certain types of long-context dependencies at the expense of others. This could result in the model becoming overly specialized to specific patterns present in the redundant samples, hindering its ability to generalize to a wider range of long-context instructions.
2. The paper does not discuss the computational resources required to implement the GATEAU framework. A selection method that is slow or computationally prohibitive is less feasible in practical scenarios, especially for extremely long instruction-following examples. The absence of detailed information regarding GPU memory usage, processing time per sample, and overall scalability makes it difficult to assess the practical applicability of the proposed method, particularly when dealing with large-scale datasets containing extremely long instruction sequences. This lack of clarity raises concerns about the real-world feasibility of the approach.
3. Although the paper includes ablation studies, it lacks an experiment testing the effectiveness of using a single model's perplexity (e.g., LLaMA-2-7B-base-64k) as the sole criterion for data selection. Adding this experiment would provide valuable insight into the authors' claim on page 4, line 174, that high perplexity alone does not adequately reflect response difficulty in long-context scenarios. Without this baseline, it remains unclear whether the improvements observed are primarily due to the multi-model comparison or if a simpler perplexity-based approach could achieve comparable results, especially given that perplexity is a widely used metric for assessing model uncertainty.

### Questions
1. How does the proposed framework handle potentially redundant or highly similar samples? Could repeated high-scoring samples lead to an overrepresentation of certain types of data, thus limiting the diversity and richness of long-context dependencies in the selected dataset?
2. Would this approach remain feasible for datasets of larger scale, and what are the expected costs in terms of time and resources?
3. Is there some display problem in Figure 2?

### Soundness
2

### Presentation
3

### Contribution
3
