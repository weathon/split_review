# Memorization in In-Context Learning

- Decision: Reject
- Scores: 3, 5, 8, 5, 6

## Abstract
In-context learning (ICL) has proven to be an effective strategy for improving the performance of large language models (LLMs) with no additional training. However, the exact mechanism behind this performance improvement remains unclear. This study is the first to show how ICL surfaces memorized training data and to explore the correlation between this memorization and performance on downstream tasks across various ICL regimes: zero-shot, few-shot, and many-shot. Our most notable findings include: (1) ICL significantly surfaces memorization compared to zero-shot learning in most cases; (2) demonstrations, without their labels, are the most effective element in surfacing memorization; (3) ICL improves performance when the surfaced memorization in few-shot regimes reaches a high level (about 40\%); and (4) there is a very strong correlation between performance and memorization in ICL when it outperforms zero-shot learning. Overall, our study uncovers memorization as a new factor impacting ICL, raising an important question: to what extent do LLMs truly generalize from demonstrations in ICL, and how much of their success is due to memorization?

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates the role of memorization in in-context learning (ICL) for LLMs. It shows that ICL significantly surfaces memorized training data, particularly when demonstrations without labels are used, and it establishes a strong correlation between memorization and improved model performance. The study finds that memorization levels increase with more demonstrations, with surfaced memorization reaching up to 75% in many-shot settings. Moreover, performance on memorized instances consistently surpasses that on non-memorized instances, raising questions about how much of ICL's success is due to true learning versus memorization.

### Strengths
This paper proposes a novel approach to quantify the level of memorization within ICL, contributing to a study in understanding the behavior of LLMs.

### Weaknesses
1. The paper presents findings that are already well-known in the field of machine learning: models perform better when they memorize training data, which is often referred to as "data leakage." It is unclear whether the primary motivation of this study is to investigate the relationship between ICL and memorization or to propose a method for quantifying memorization.

1. The paper claims to explore the "correlation between memorization and performance on downstream tasks" (lines 13-14). However, the Pearson correlation coefficient appears to be computed based on match scores across different k-shot settings. The memorization and downstream ICL tasks have different formats and purposes, which makes the correlation analysis questionable. Additionally, the negative correlation for the RTE dataset contrasts with the positive correlations for other benchmarks, casting doubt on the overall claim of correlation.

1. The authors do not provide an explanation for the observed experimental results. For example, the six observations drawn from Figure 2 are stated as mere observations without discussing the underlying reasons or contributing factors behind the results.

1. The comparison of different k values in evaluating memorization in Figure 2 is not adequately justified. The importance of the number of demonstrations as a variable for quantifying memorization remains unclear.

1. The use of 25-shot and 50-shot as examples of few-shot scenarios is too much. I expect that few-shot settings refer to 3-shot to 5-shot examples. Zero-shot results do not clearly indicate memorization level, as exact match criteria might be influenced by formatting issues rather than actual memorization. True few-shot settings, such as 3-shot, could provide a better output by constraining the output format, allowing for more precise evaluation.

1. Only GPT-4 is evaluated in the experiments. Including more LLMs in the experiments would provide stronger support for the paper's claims and offer broader insights.

1. The paper's presentation could be improved in several areas:
    * The repeated use of the phrase "memorization in ICL" is ambiguous, as it could imply that LLMs are memorizing the demonstrations instead of the training data. Since the study aims to explore memorization in LLMs using ICL as a tool, it would be clearer to use "memorization by ICL."
    * Figure 2 is intended to compare different settings, but the use of multiple curves for various datasets in a single subfigure makes it challenging to interpret comparisons. The authors should consider placing curves for different settings but the same dataset in each subfigure for clarity.

### Questions
1. How are non-memorized and memorized instances determined in Figure 3?
1. What is the relationship between the number of shots (k) in downstream ICL and the number of shots used in memorization experiments? The two tasks seem to serve different tasks with different purposes.

### Soundness
3

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
3

### Summary
This paper examines the role of memorization in in-context learning (ICL) for large language models (LLMs), investigating how ICL surfaces memorized training data and analyzing its impact on downstream task performance across zero-shot, few-shot, and many-shot regimes. The authors propose a method to measure memorization by testing if model-generated completions match known dataset instances. They find that ICL significantly increases memorization compared to zero-shot, with the amount of memorized information correlating strongly with performance improvement. This study highlights memorization as a key factor impacting ICL effectiveness, prompting questions about the extent to which LLMs generalize from demonstrations versus relying on memorized knowledge.

### Strengths
1.	The paper is the first to systematically examine the relationship between ICL and memorization in LLMs, providing new insights into how memorized knowledge influences ICL performance.
2.	The study uses a detailed approach to measure memorization across multiple settings (full information, segment pairs and labels, and only segment pairs), allowing for a granular analysis of which prompt elements drive memorization in ICL.
3.	The paper demonstrates a robust correlation between memorization and improved performance in downstream tasks, highlighting memorization as a previously under-explored factor in ICL success.
4.	The methodology and results are clearly presented, making the findings accessible and useful for future research on optimizing ICL methods and evaluating LLM generalization.

### Weaknesses
1.	While the experiments are thorough, they are conducted in relatively simple datasets, limiting the paper’s ability to generalize findings to more complex, real-world tasks (e.g., legal, medical datasets). The datasets used, such as WNLI and TREC, are relatively small and do not fully capture the nuances of real-world scenarios where the data is often unstructured, noisy, and requires more sophisticated reasoning. This raises concerns about the applicability of the memorization findings to more complex tasks that involve longer text sequences and intricate relationships between data points.
2.	The study does not address potential challenges in handling longer contexts, which are often needed in real-world applications and may limit the practicality of the proposed memorization detection method in large-scale LLMs. The method's reliance on exact or near-exact matches might become computationally expensive and less reliable as the context length increases, potentially missing subtle forms of memorization that are not verbatim repetitions. This is particularly relevant in scenarios where the model might paraphrase or rephrase memorized information rather than reproducing it exactly.
3.	While the paper successfully identifies memorization as a factor, it does not provide a concrete analysis of how much ICL performance improvement is due to memorization versus actual generalization, leaving this as an open question. The paper establishes a correlation between memorization and performance but does not quantify the extent to which memorization contributes to the observed performance gains. It remains unclear whether the model is truly generalizing from the provided examples or simply relying on memorized patterns, which is a critical distinction for understanding the true capabilities of ICL.
4.	The experiments rely solely on GPT-4, limiting the generalizability of the findings to other LLMs. The authors could strengthen their conclusions by evaluating memorization across a range of models with varying training data and architectures. The use of a single model, even a powerful one like GPT-4, makes it difficult to determine if the observed memorization patterns are specific to this model's architecture and training data or if they are a more general phenomenon across different LLMs.

### Questions
1.	How would the memorization-performance correlation change if tested on larger, more diverse datasets, such as those in professional domains?
2.	Could future work incorporate real-time memorization detection to dynamically assess memorization levels in longer contexts?
3.	How does ICL performance vary between tasks that rely heavily on memorized information (e.g., factual knowledge) versus tasks that require more abstract reasoning or generalization?
4.	Is there a threshold where memorization starts to negatively impact performance, particularly if memorized information conflicts with task requirements?
5.	Would alternative architectures that prioritize generalization over memorization yield lower memorization rates in ICL while maintaining strong performance?
6.	How might the findings differ if fine-tuned LLMs with domain-specific training data are tested, where memorization may play a more prominent role?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper seeks to quantify the correlation between LLM memorization of specific datapoints in well-known datasets and the ICL performance on these dataset subsets. They examine several datasets, selecting datapoints from these and using an existing protocol from another work to quantify how many datapoints the LLM has memorized, testing memorization in few, many, and zero-shot regimes. They then correlate this to the performance using ICL on these exact datapoints, but overall in aggregate, rather than on a per-datapoint level. Authors then draw a set of observations from this experiment and conclude that the results raise the question of if ICL works by memorization.

### Strengths
The paper is very well written. It is clear and easily to follow, and the experimental setup is also very intuitive. The mechanism by which ICL works is a very relevant and important question.

### Weaknesses
The paper only experiments on GPT-4. Authors claim that it is the only LLM that fulfills their criteria but this is somewhat hard to believe, especially given the existence of long-context open-source models. The authors claim that they do not have the resources to run these experiments on e.g. llama3 or some other long-context open-source model that fulfills their criteria, but I believe it would strengthen the paper considerably to have more than a single model for testing.

It is not clear what authors provide beyond confirming existing works in the area. It is not justified adequately why these experiments they perform give us any new information about how ICL fuctions. Specifically, the core claim that ICL performance is correlated with memorization levels seems self-evident, given that ICL relies on providing examples that the model has likely seen during pre-training. The paper does not adequately address the possibility that the observed correlation is simply a result of the model recalling memorized training data, rather than a deeper mechanism of ICL.

### Questions
Use additional models, it's hard to take a study that only uses a single closed-source model seriously.

I need additional justification for why these experiments tell us about how ICL functions. To me they tell me that in cases where there is dataset contamination ICL performs better, but this is to be expected. What about when there is no dataset contamination and ICL still works, how does this work? This is the more interesting question to me.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper explores the phenomenon of memorization in In-context Learning (ICL) across different regimes (zero-shot, few-shot, and many-shot) using large language models (LLMs). It aims to quantify how much of the model's performance improvement during ICL can be attributed to memorized training data.

### Strengths
Relevant Topic: The topic of memorization in LLMs is timely and relevant, given the increasing reliance on these models for various tasks without full retraining.

Experimental Design: The approach to quantify memorization using modified data contamination methods is methodologically interesting and innovative.

### Weaknesses
Incremental Contribution: The insights and contributions of the paper are not sufficiently novel or significant. The findings that ICL surfaces memorization and that memorization correlates with performance do not extend significantly beyond what is already suggested or known in the literature.

Lack of Practical Implications: The paper does not sufficiently discuss the practical implications of its findings. While it notes the correlation between memorization and performance, it fails to explore how these insights could be used to improve model design or deployment in real-world applications.

Theoretical Depth: The discussion around why certain memorization occurs in specific ICL settings lacks depth. There is no substantial theoretical analysis or explanation beyond the observational data presented.

### Questions
Can the authors provide more detailed insights into how these findings could influence practical model training or deployment strategies? How do the authors envision their methodology being adapted or expanded to cover more diverse models and tasks to verify the generalizability of the findings?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors address the memorization problem in the context of In Context Learning. 
We recall that memorization is the process of memorizing data from the pre-trained dataset.
It is generally evaluated by measuring the ability of the model to regenerate those data at the inference step.
The main objective of this work is to understand how memorization correlates with Performances in ICL. To this end, the authors propose to study different settings to estimate memorization of the model (using GPT-4 in the experiment), on the dataset used in the pre-training of the model (or that are likely to be seen during its training according to previous works). Authors propose to evaluate different ICL variants (varying between description, example, and labels) in different k-shot settings (number of examples given in the context). For scoring memorization, authors mostly rely on "Time Travel in LLMs: Tracing Data Contamination In Large Language Models," published at ICLR last year.
In the experiments section, authors compare the different memorization scores according to the number k (of k-shots), the information given in input (instruction, example, and/or labels), and the matching method (exact matches, near exact matches).
In subsection 5.2, the correlation between task performance and memorization is compared, showing that the more the dataset is memorized, the more it correlates with performance.
Accordingly, the contributions are the following:
* A new method to measure memorization in ICL, proposing to evaluate memorization with k-shot (the metrics exact match and the near exact match was proposed in [1])
* How to correlate the memorization with performances (in the setting proposed) 


[1] "Time Travel in LLMs: Tracing Data Contamination in Large Language Models", Shahriar Golchin and Mihai Surdeanu, ICLR 2024

### Strengths
*The originality of the paper proposing a study of memorization impact on performances, while generally it mainly involves detecting contamination
*Experiments are well designed to answer the research question (correlation between performances and memorization)
*A proposal to measure memorization based on a comparison of the number of demonstrations (number of examples in the prompt)

### Weaknesses
 * Only one model is used in the experiments, which is too few to conclude on a general statement (notice that the choice is, however, justified)
* Most of the pipeline relies on the memorization score design in [1] 
* The state-of-the-art lack of explicit explanation (section 6), but contains at the best of my knowledge the most relevant references
* Results should be better/extensively discussed (mainly for the 5.2 experiments)
* Metrics and what the reported results are missing in 5.2 (the two tables 1 and 2)

### Questions
* Observation 3 states that performance improvements are highly correlated with memorization. Can you explain why, according to results, particularly how can you explain the negative correlation on RTE 
* Tables 1 and 2 report a correlation (Pearson) between performances and memorization; however, the number of k-shots is not specified, nor is the setting (Full Information, Segments pairs, and labels, only segment pairs) to measure the correlation. What did you choose for the memorization metric here?

### Soundness
2

### Presentation
3

### Contribution
2
