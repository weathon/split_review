# On the Diversity of Synthetic Data and its Impact on Training Large Language Models

- Decision: Reject
- Avg Score: 5.80
- Scores: 8, 6, 6, 3, 6

## Abstract
The rise of Large Language Models (LLMs) has accentuated the need for diverse, high-quality pre-training data. 
Synthetic data emerges as a viable solution to the challenges of data scarcity and inaccessibility.
While previous literature has focused predominantly on the quality and quantity of real data, our work enables the measurement of diversity in synthetic data and explores its impact on LLM performance. 
We study the downstream effects of synthetic data diversity during both the pre-training and fine-tuning stages by introducing a new diversity metric, \textit{LLM cluster-agent}, designed to evaluate the diversity of synthetic datasets. 
Through a series of controlled experiments with models of 350M and 1.4B parameters, we demonstrate that the proposed cluster-based LLM scoring of diversity correlates positively with both pre-training and supervised fine-tuning performance. 
Our findings also reveal that synthetic data diversity in pre-training affects supervised fine-tuning more significantly than pre-training itself, even for smaller models. 
We hope this study advances our understanding of the optimal use of synthetic data in LLM training and opens new avenues for efficient data generation processes.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper aims to address an important gap in LLM research - impact of a diverse dataset on LLM performance on task generalization. More so, it attempts to quantify "diversity" by introducing a clustering based metric for it and proposes an agentic pipeline for the same. Elaborate comparisons have been done with other heuristic and model-based metrics. Multiple open-sourced and proprietary models have been use to generate synthetic data and compare how diversity metric compares across different model architectures and sizes.

### Strengths
1. Elaborate comparisons have been done with other heuristic and model-based metrics.
2. Multiple open-sourced and proprietary models have been use to generate synthetic data and compare how diversity metric compares across different model architectures and sizes. 
3. Cluster generation and verification step is a much needed verification step for agentic pipelines and that has been addressed appropriately.
4. Conducting large scale study to systematically investigate the effectiveness of a diverse synthetic dataset in pre-training as well as SFT processes is a huge positive that strengthens the underlying hypothesis.

### Weaknesses
1. Lack of a rigorous human evaluation study : Agentic pipelines generally need to be heavily intertwined with a human-in-the-loop aspect during initial experimentation. I am a bit unclear on how to test the reliability and quality of the metadata and metrics generation step in the pipeline. The error in this initial step would be propagated to later steps and would potentially make the metric unreliable.
2. Assessing cluster purity - an elaborate statistical analysis on the clusters formed is missing, how do we trust the final clusters formed and how do we assess cluster purity?
3. Lack of control on the number of clusters formed - there needs to be a systematic prompt injection to define the optimal number of clusters to be formed (and a process to find the optimal number of clusters in the first place). I understand that there has been ablation studies on the number of clusters, but how do I pick this optimal number which might also vary across different styles and topics)
4. Parameter Sensitivity: The performance of the clustering may depend on the choice of parameters like K (number of samples for clustering), N (number of clustering iterations), J and M (for metadata/metric generation). Optimal parameter settings may need to be determined.

### Questions
1. How do you decide on the optimal number of clusters? Is there a cluster evaluation technique (similar to elbow curves, cluster homogeneity metrics for traditional clustering techniques) in place?
2. Can we have a human eval study included to address the metric reliability issues?

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
This paper runs a study on the effect of diversity for synthetic data used to pretrain LLMs. To accomplish this, they develop a llm-based diversity metric called LLM Cluster-agent that measures the diversity of datasets. This pipeline is an iterative clustering mechanism that uses a metadata and metrics generation prompt to extract features used to generate clusters. A clustering prompt is used to prompt an LLM to group randomly selected samples from the corpus into clusters. From here, the LLM Cluster score is used to measure the diversity of the synthetic data based on the ratio between the number of clusters with the number of samples.

Using this metric, the authors pretrain multiple 350M and 1.4B parameter llama models on a combination of real and synthetic data to measure the performance of these models on downstream tasks as a function of the diversity of the synthetic data, and find that model performance correlates with LLM Cluster score. Furthermore, authors run extensive ablations on different synthetic generation prompts.

### Strengths
Content of the paper is fairly complete and extensive. Explanation of LLM Cluster-agent is clear and concise. Lots of details provided in the main manuscript and in the appendix to show exactly what they are doing. Ablations are elaborate and extensive. Paper gives convincing evidence that diversity in synthetic data generation can be controlled and is correlated with downstream performance. Generated metric may be a strong indicator for the efficacy of a synthetic data generation pipeline for pretraining.

### Weaknesses
The work does not sufficiently show that LLM cluster score is more correlated with performance than baseline metrics. Figure 1 is the main result showing that LLM cluster score correlates with downstream performance. However, it is difficult to see if other baseline metrics provided in the paper would not also be correlated with performance. Argument would be more convincing if there were also diagrams or concrete correlation metrics of the other baseline metrics not aligning with performance in a similar diagram. The only evidence given that performance is more correlated is through visual inspection of Figure 4 and 5 in Section 3.3, and through visual inspection of Figure 6 and 7. Some of these correlations seem marginal at best on inspection. For instance, LLM Cluster score for Cosmopedia v0.2 performs the worse, but its performance is about on par with v0.1 and Topics in Figure 7a, 7c, and 7d.

Main question would be whether the authors can show some quantitive correlation metrics or diagrams between LLM cluster score and other baseline metrics and downstream performance to show that LLM cluster score is a better indicator for performance than other baseline metrics. 

In Figure 5, is the model trained on only real data trained on more real data to match the number of synthetic tokens? Judging from the results, it seems like you are not. Would be interesting to quantify the efficacy of training with synthetic data. Similarly in Figure 9, it seems like the number of tokens that the model is train on is increasing as you increase the synthetic to real data ratio. This diagram would be more convincing if it kept the amount of data/tokens used for training static.

Also am interested in the cost of evaluating these datasets using LLM Cluster score. Previous approaches used either no LLMs or open source LLMs like GPT-2. However, with this metric, all of these results are done using GPT-4o. Is this technique viable for researchers trying to quantify the diversity of their synthetic datasets? 

LLM Cluster-agent pipeline seems to have some similarity with the field of explainable/unsupervised clustering of text data, such as 
```Wang, Zihan, Jingbo Shang, and Ruiqi Zhong. "Goal-Driven Explainable Clustering via Language Descriptions." The 2023 Conference on Empirical Methods in Natural Language Processing``` and other related work, which should be cited in the related work.

There are also some typos in the manuscript. Other parts are a bit vague and unclear:
* Line 098 has a typo "per-training". 
* On line 147, it is unclear what "due to similar patterns in part-of-speech tagging and syntactic often present in them"? Is this supposed to be "syntax"?
* In section 2.1, it is unclear how capturing the underlying distribution of clusters and cluster sizes implies that this measure originates from the principle of entropy. What does this mean?
* Seems to be an extra space on line 309 and line 422.
* Extra "diversity" in the description of Figure 4, near line 289/290.
* Is LLM Cluster-agent the name of the metric itself? Or is it the pipeline that you have developed for generating clusters? In the Abstract, you state that LLM Cluster-agent is "a new diversity metric", but in Section 2.1, you state that it is "pipeline that leverages LLM's abilities to interpret semantic meanings", and then later, on line 199-200, you state that "LLM Cluster score" is the actual diversity metric. There also is inconsistent capitalization of this name throughout the manuscript.
* Line 409: Cosmopedia is spelled "Cosmppedia"
* On line 464-465 in Section 3.7, the paper states that larger models "generally achieve higher accuracy, suggesting that more capable models benefit more from increased synthetic data diversity". However, the models achieving higher accuracy can be attributed just to larger model size. I think that the authors meant to say that the performance of the larger models are more correlated with diversity, not that they achieve higher accuracy. Furthermore, as stated before, this statement would be more convincing and concrete if the authors provided quantitative metric for this correlation.
* In Section 2.1, line 197, the paper states that the verification step is important in "removing some unreasonable clusters." What does this mean? What are examples of unreasonable clusters?

Nit: Would add a citation for the footnote on page 3 regarding the degradation of performance for long-context situations, maybe Lost in the middle (Liu 2023) or something similar.

### Questions
Main question would be whether the authors can show some quantitive correlation metrics or diagrams between LLM cluster score and other baseline metrics and downstream performance to show that LLM cluster score is a better indicator for performance than other baseline metrics. 

In Figure 5, is the model trained on only real data trained on more real data to match the number of synthetic tokens? Judging from the results, it seems like you are not. Would be interesting to quantify the efficacy of training with synthetic data. Similarly in Figure 9, it seems like the number of tokens that the model is train on is increasing as you increase the synthetic to real data ratio. This diagram would be more convincing if it kept the amount of data/tokens used for training static.

Also am interested in the cost of evaluating these datasets using LLM Cluster score. Previous approaches used either no LLMs or open source LLMs like GPT-2. However, with this metric, all of these results are done using GPT-4o. Is this technique viable for researchers trying to quantify the diversity of their synthetic datasets? 

LLM Cluster-agent pipeline seems to have some similarity with the field of explainable/unsupervised clustering of text data, such as 
```Wang, Zihan, Jingbo Shang, and Ruiqi Zhong. "Goal-Driven Explainable Clustering via Language Descriptions." The 2023 Conference on Empirical Methods in Natural Language Processing``` and other related work, which should be cited in the related work.

There are also some typos in the manuscript. Other parts are a bit vague and unclear:
* Line 098 has a typo "per-training". 
* On line 147, it is unclear what "due to similar patterns in part-of-speech tagging and syntactic often present in them"? Is this supposed to be "syntax"?
* In section 2.1, it is unclear how capturing the underlying distribution of clusters and cluster sizes implies that this measure originates from the principle of entropy. What does this mean?
* Seems to be an extra space on line 309 and line 422.
* Extra "diversity" in the description of Figure 4, near line 289/290.
* Is LLM Cluster-agent the name of the metric itself? Or is it the pipeline that you have developed for generating clusters? In the Abstract, you state that LLM Cluster-agent is "a new diversity metric", but in Section 2.1, you state that it is "pipeline that leverages LLM's abilities to interpret semantic meanings", and then later, on line 199-200, you state that "LLM Cluster score" is the actual diversity metric. There also is inconsistent capitalization of this name throughout the manuscript.
* Line 409: Cosmopedia is spelled "Cosmppedia"
* On line 464-465 in Section 3.7, the paper states that larger models "generally achieve higher accuracy, suggesting that more capable models benefit more from increased synthetic data diversity". However, the models achieving higher accuracy can be attributed just to larger model size. I think that the authors meant to say that the performance of the larger models are more correlated with diversity, not that they achieve higher accuracy. Furthermore, as stated before, this statement would be more convincing and concrete if the authors provided quantitative metric for this correlation.
* In Section 2.1, line 197, the paper states that the verification step is important in "removing some unreasonable clusters." What does this mean? What are examples of unreasonable clusters?

Nit: Would add a citation for the footnote on page 3 regarding the degradation of performance for long-context situations, maybe Lost in the middle (Liu 2023) or something similar.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The main idea presented in the document is studying the impact of diversity in synthetic data on the performance of large language models (LLMs) during pre-training and fine-tuning. They propose a new metric called "LLM Cluster-agent" to quantify the diversity of large-scale synthetic text datasets. This metric uses an LLM to cluster text samples based on generated metadata and scoring criteria.They generate synthetic datasets with varying levels of diversity by controlling factors like:
    - The underlying distribution of topics and generations per topic
    - Prompts/templates used for synthetic data generation (e.g. adding styles, personas)
    - Base LLM models used for generation (GPT-4, GPT-3.5, open-source models)
    - Ratio of real vs. synthetic data used for pre-training

They pre-train 350M and 1.4B parameter LLMs on combinations of real data and the synthetic datasets of varying diversity levels. They evaluate the pre-trained and also supervised fine-tuned LLMs on several benchmarks. Their experiments show that the proposed LLM Cluster-agent diversity metric correlates positively with the performance of both pre-trained and fine-tuned LLMs. They find that larger diversity in synthetic data benefits model performance, especially for fine-tuning. But too much synthetic data can deteriorate performance. They ablate the design choices of their LLM Cluster-agent pipeline.

### Strengths
1. The paper is well written and clearly organized
2. The authors discuss an important issue of understanding diversity metric.

### Weaknesses
1. Context Length Limitation:
- The paper criticizes previous methods for context length limitations (lines 192-195), but the proposed method also faces similar constraints
- How does this represent an improvement over existing algorithms?
- Current LLMs have a maximum context length they can process. For extremely long documents, the clustering may need to be done in segments. What specific solutions does the method offer to address the context length challenge?
- Can you please clarify how your method specifically addresses or improves upon the context length limitations of previous approaches. Please provide a more detailed comparison of how your method handles long documents compared to existing techniques.

3. The authors state that their findings "present scalability and potential to be applied on a larger scale." However, their largest experiment is limited to 1.4B parameter models due to computational constraints. Extrapolating their diversity metric's performance and conclusions to much larger models (e.g., hundreds of billions of parameters) may be an overreach without empirical evidence at those scales. Please discuss any theoretical reasons or preliminary evidence that suggests their findings would scale to much larger models, or to explicitly acknowledge the limitations of extrapolating beyond the scales tested.

4. Belief in prompted clustering quality: Their LLM Cluster-agent metric relies heavily on the quality of prompted clustering done by LLMs. While LLMs can be very capable, assuming that their clustering perfectly captures true data diversity based on generated criteria is a strong belief. The metric's performance could degrade for highly complex data distributions.

5. Diversity dimensionality: Their metric provides a single score capturing overall diversity. However, diversity is a multi-dimensional construct. Existing metrics focus on different facets that may still be relevant.

6  Self-Verification Process Design:
- Why wasn't a more capable "teacher" model used for the self-verification step?
- Would using a more advanced model for verification improve the reliability of the results?
- What was the rationale behind using the same model for both clustering and verification?

7. This point is just good to have. I am not reducing scores for this: The evaluation is based solely on automatic metrics. Incorporating human evaluation of the generated synthetic data and model outputs could provide a more holistic understanding of the diversity and quality aspects.

### Questions
The paper is well written but I still have a lot a of questions. It would be great if authors can answer them

1. Sampling Parameters and Methodology (This is my biggest concern):
- How are the parameters K (samples for clustering) and J (samples for metadata generation) selected?
- For the M repetitions in metadata generation, are different J samples used each time?
- What is the justification for these parameter choices?

2. Self-Verification Process:
- How is the effectiveness of the self-verification step evaluated?
- Does the verification use the same LLM model or a different one?
- How do different values of M and K affect the consistency of clustering results?

3. Generalizability:
- Has this diversity measurement approach been tested on different types of datasets beyond the described text data (e.g., mathematical content)? If not can you do some additional experiments beyond mathematical domain like finance, biomedical or logical reasoning to show more generalizability of the proposed metric. 

4. Comparative Analysis:
- How does the LLM Cluster-agent method compare quantitatively to existing diversity measurement approaches?
- What specific advantages does it offer over traditional methods? A detailed comparison would be more helpful

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a framework to understand the efficacy of synthetic data, with a focus on quantifying the extent and effect of diversity in synthetically-generated data. To this end, a novel model-based metric, LLM Cluster score, is proposed. Based on a subsample of the data, attributes are identified by an LLM that can uniquely characterize individual samples and cluster similar ones. A random sample is taken and the data points within it are clustered. Based on the results of these clustering iterations, the diversity metric is calculated. This diversity metric is shown to be positively correlated with model accuracy metrics, demonstrating that [1] this metric is a good measure of diversity, and [2] more diverse data results in better model performance.

### Strengths
- This work proposes a novel, model-based metric
- The methodology allows for limitations of model context lengths
- Several insightful analyses surrounding accuracy, diversity, and token balance are presented.

### Weaknesses
 - The number of samples is a cause for concern.  (J=5, K=10) 

-- J=5 : does this imply that the model uses 5 samples to infer the metadata and metrics that characterize the entire distribution? Given the size of the data and the number of topics that may be present (100K/300K), it merits more discussion on whether J samples can represent the data sufficiently. The metadata and metrics extracted from such a small sample may not capture the full diversity of the dataset, potentially leading to a skewed representation of the underlying distribution. This is especially concerning given the high dimensionality of the data and the potential for significant variation across different subsets.

-- K=10 : Having obtained metadata and metrics, as well as a prompt that grades samples according to the rubric defined, lines 192-194 suggest that only K samples out of the dataset are then assigned to clusters by the LLM. Can a cluster score over 10 samples definitely yield an idea of the diversity of the dataset? This is a critical limitation, as the cluster score is derived from a very small subset of the data, and it is unclear how well this score generalizes to the entire dataset. The small sample size may not capture the full range of cluster structures present in the data, leading to an inaccurate assessment of diversity. This could benefit from more supporting evidence.

In light of this, conducting sensitivity analyses, and extending the ablation studies in B.2 to higher values of K and a range of values for J would mitigate this concern. Furthermore, including other clustering metrics in the ablation study beyond the novel LLM cluster metric would help corroborate these values more strongly.

- The self-verification module could benefit from clarification along the following lines: 

-- Was there any human evaluation performed in order to verify the outcomes of the self-verification module, and in order to find the optimal verification prompt? The lack of human evaluation raises concerns about the reliability of the self-verification process. Without a ground truth comparison, it is difficult to assess whether the module is accurately identifying invalid clusters or if it is introducing biases. The choice of the verification prompt is also critical, and without human feedback, it is unclear if the prompt is effectively capturing the intended criteria for invalid clusters.

--  Using the same model to verify its own reasoning chain and clustering judgements may lead to a positive bias; the verification module would benefit from utilizing an LLM that is not part of the earlier steps of cluster score generation pipeline. The potential for confirmation bias is a significant concern. If the same model is used for both clustering and verification, it may be predisposed to confirm its initial judgments, even if they are incorrect. Using an independent LLM for verification could provide a more objective assessment of the clustering results.


- There is a lack of clarity on the difference between the "metadata" and "metric" axes. How are these factors differentiated? Based on the sample outputs in Appendix D.2, there is some overlap between the nature of the "metadata" and "metric" keys, in terms of quantifiability and subjectivity. This lack of distinction is made stronger by the prompt templates in Appendix D.1, where the templates for metrics and metadata generation are nearly identical. It would be helpful to delineate [1] how these terms are different in theory, [2] in practice, how the outcomes of their respective prompts differ, and [3] whether this difference is essential to maintain, as opposed to a single prompt that generates factors that could be either "metrics" or "metadata". The current definitions are vague, and it is unclear why two separate prompts are needed if the outputs are so similar. The lack of a clear distinction between metadata and metrics undermines the interpretability of the results and raises questions about the validity of the approach.

- Additionally, some of the "metadata" and "metrics" are ill-defined, with only qualitative judgements associated with them, and that too only for the values on the extreme ends of the 1-5 scoring scale (See Appendix D.2) . This raises a concern: LLMs often show a lack of consistency in their outputs, even for the same input. This is an even greater concern when LLMs are used to confer subjective evaluations on the input. The diversity metric proposed in this work may be non-reproducible, especially over different  samples of the same dataset. The inconsistency could be be mitigated by including a more detailed, unambiguous rubric. The results would also be strengthened by running multiple trials with various seeds for random sampling the data. The lack of a detailed rubric and the reliance on LLM-generated subjective evaluations introduce a significant source of variability and potential bias. This makes it difficult to reproduce the results and undermines the reliability of the proposed diversity metric.

- Figures 5 and 6 show that the inter-cluster variance achieved by using LLM Cluster score is higher than that achieved by other methods, thus demonstrating its efficacy in segmenting a dataset with 100K-300K topics. However, owing to the non-uniform scaling of the X-axis and the non-comparable nature of the range of values ([24,24.2] for Perplexity, [192,100] for K-Means, [3.5,5] for LLM Cluster score), it is not possible to definitively determine that a higher cluster score is more correlated with diversity than a higher measure of any other diversity metric. Contextualizing the comparative performance of these scores and their usefulness in 3.2 onwards, along with presenting standardized results in the visualizations would help better understand the benefits of LLM cluster score over other metrics. The lack of standardized results and the non-uniform scaling of axes make it difficult to compare the performance of the LLM cluster score with other metrics. This hinders the ability to draw definitive conclusions about the superiority of the proposed metric.

### Questions
- Lines 185-187: across all M iterations, what is the nature of the sampled J instances, are these samples exclusive of one another? Or is the sampling entirely random and from the whole distribution, which means that there may be common elements  in different J-sized samples across the M iterations?
- The work also states that the clustering is performed N times. Does the K-sized sample change over each iteration out of N? If so, are the K-sized samples exclusive of one another, or are they randomly samples each time from the entire dataset, thus allowing for common elements?
- Instead of clustering only K samples, which may not yield a diversity score representative of the entire dataset, it may be more fruitful to cluster all elements in the dataset, taking K samples at a time, and following a iterative approach akin to K-Means to merge existing clusters and obtain a more comprehensive idea of the clusters produced by the LLM Cluster-agent over the dataset. 
- (Lines 186-187) Documenting the intuition behind using a metadata and metric gathering prompt (that summarizes the most frequent subset of metadata and metrics) instead of scoring the samples individually over every metadata and metric generated, would help convey the rationale of the approach better.

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
The paper investigates the importance of diversity in synthetic data used for training large language models (LLMs). This study introduces a novel metric called LLM Cluster-agent, an LLM-based agent to evaluate the diversity of synthetic datasets. The authors analyze how diversity affects model performance during both the pre-training and fine-tuning phases. Through experiments involving models of 350M and 1.4B parameters, the authors demonstrate that greater diversity in synthetic data generally correlates positively with improved performance, especially during fine-tuning. They also explore various methods for generating synthetic data using various `Topic-*` prompt templates to increase the diversity of the synthetic data generated. Finally, they also study the dynamics of synthetic tokens in pertaining corpora and the model performance metrics. The performance improvement also correlates with the value of the diversity score reported by the LLM agent.

### Strengths
1. The authors propose a novel approach LLM Cluster-agent to quantifying the diversity of text datasets, specifically tailored for synthetic data, which is often more challenging to evaluate.
2. The authors carry out systematic controlled experiments across various factors, such as topics, prompt styles, generation models, and real-to-synthetic token ratios, providing insights into optimal practices for synthetic data generation.
3. The findings offer practical guidance on balancing real and synthetic data and selecting synthetic generation models to enhance performance, which could be valuable for researchers and developers of LLMs.
4. From the ablation experiments, the clustering performance drops with low K and high N values, indicating potential scalability and applications to compute diversity in real-world scenarios.

### Weaknesses
1. The primary drawback I observe is the separation between the generation and diversity measurement processes. According to the pipeline, diversity is only measured after data generation is completed. For example, if 4.5B tokens are generated and the resulting LLM diversity score is low, this would make the generation effort ineffective. Did the authors consider iterative diversity checks during the generation process. For example, implement intermediate diversity assessments at smaller generation intervals (e.g., every 100M tokens). This would allow to adjust or halt generation if diversity metrics fall below a desired threshold, optimizing the process early on and reducing waste in cases of low diversity outcomes.
2. Another significant limitation of this approach is its heavy reliance on large pre-trained LLMs to evaluate various criteria. How do the authors guarantee the stability of the metrics and metadata generated? Was any human evaluation performed to verify the overall reliability of the pipeline? The results could be more reliable if the authors conduct an inter-rater reliability tests by comparing diversity metrics generated by multiple LLMs or align LLM-generated metrics with human evaluations. A smaller human-annotated sample can be used to validate the model-generated diversity scores as this would enhance the overall reliability of the pipeline.
3. In the cluster generation step, the clustering process is localized to the number of samples that can be fit in the context window of the LLM. This can lead to random and unpredictable cluster formations leading to unpredictable diversity scores. Did the authors try any approaches that can mitigate the issue?

### Questions
### Questions:
1. How is GPT-40 prompted to extract a hierarchy of topics and a set of keywords covered in the page's content? 
2. In the Synthetic Data Generations section, it is unclear how the downweighting of Cosmopediav0.1 and Cosmopediav0.2 was done.
3. There is a brief explanation, but it is still unclear why `topic-style persona` almost always outperforms `multi-topic-styles persona`. Intuitively, the latter is supposed to provide more diversity. 
3. What would be the average price for carrying out such an experiment due to the presence of multiple proprietary LLM calls? 
4. From the ablation experiments, it looks like when K = 10 and N =10K, the diversity score stabilizes. Do the authors report all their experiments with this configuration?
5. Would be interested to know the comparison between the following method say KMeansDiversityScore, where we identify $C_i$ clusters using K-means of embeddings of samples and get cluster size $S_i$ from $K$ randomly selected samples. Repeat this experiment $N$ times and then compute the diversity score using the same formula. This experiment can provide a good comparison if the metric and metadata generation followed by the metadata gathering step has a positive effect in computing good diversity scores.

### Suggestions:
1. Typo at line 093: s\per-training\pre-training
2. Missing citation `??` at line 1055

### Soundness
3

### Presentation
3

### Contribution
3
