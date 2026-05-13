# What are the Essential Factors in Crafting Effective Long Context Multi-Hop Instruction Datasets? Insights and Best Practices

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Recent advancements in large language models (LLMs) with extended context windows have significantly improved tasks such as information extraction, question answering, and complex planning scenarios. In order to achieve success in long context tasks, a large amount of work has been done to enhance the long context capabilities of the model through synthetic data. Existing methods typically utilize the Self-Instruct framework to generate instruction tuning data for better long context capability improvement. However, our preliminary experiments indicate that less than 35\% of generated samples are multi-hop, and more than 40\% exhibit poor quality, limiting comprehensive understanding and further research.
   To improve the quality of synthetic data, we propose the Multi-agent Interactive Multi-hop Generation (\texttt{MIMG}) framework, incorporating a Quality Verification Agent, a Single-hop Question Generation Agent, a Multiple Question Sampling Strategy, and a Multi-hop Question Merger Agent. This framework improves the data quality, with the proportion of high-quality, multi-hop, and diverse data exceeding 85\%. Furthermore, we systematically investigate strategies for document selection, question merging, and validation techniques through extensive experiments across various models. Our findings show that our synthetic high-quality long-context instruction data significantly enhances model performance, even surpassing models trained on larger amounts of human-annotated data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the Multi-agent Interactive Multi-hop Generation (MIMG) framework, which incorporates a Quality Verification Agent, a Single-hop Question Generation Agent, a Multiple Question Sampling Strategy, and a Multi-hop Question Merger Agent. This framework enhances data quality, with over 85% of the data being high-quality, multi-hop, and diverse.

### Strengths
1. The motivation of this paper is clear.
2. The exploration of methods within each agent module of the framework is thorough.

### Weaknesses
1. The paper contains some errors; for example, Figure 10 shows only one image but is labeled (a).
2. While the authors have explored methods within each agent module of the proposed framework to enhance data generation quality, there is a lack of ablation studies between the agents, making it unclear which agent contributes the most.
3. The experiments are not sufficiently generalized, as they were only evaluated on InternLM. I believe validation on widely used models like the LLaMA series is necessary.
4. The experimental comparisons in the paper are somewhat confusing: it is unclear whether the authors aim to propose a SOTA dataset or a framework for generating data. If it is the latter, I believe comparisons with other works that generate multi-hop data using the same LLM should be included.

### Questions
1. The evaluation criteria for the data need further clarification, especially for metrics like Diversity.
2. In the experimental comparisons within the Data Utilization section, I am a bit confused about the details of LongMIT’s experimental data, such as the number of samples, the number of tokens, and comparisons with other datasets.
3. Please refer to the questions mentioned in the Weaknesses.

### Soundness
2

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
This paper primarily focuses on synthesizing multi-hop, high-quality instruction data. The authors propose a data generation framework that incorporates multiple components, including a quality verification agent, a single-hop question generation agent, a multiple question sampling strategy, and a multi-hop question merging agent. Through experimental analysis, the authors identify the most effective strategies for each component and combine them to produce the final synthesized long-context instruction data. The experiments demonstrate that these synthesized data can enhance model performance.

### Strengths
1. Compared to previous multi-hop data generation methods like Self-Instruct, the MIMG framework significantly enhances the proportion of multi-hop data, as well as the diversity and quality of the data.
2. The authors conduct a thorough analysis of various potentially impactful strategies, such as document selection strategies and the impact of question merging methods. This provides practical references for future research endeavors.
3. The synthesized long context dataset (LongMIT) effectively enhances long-context utilization in experiments.

### Weaknesses
1. Although the author provides a detailed analysis of the impact of different strategies on the multi-hop data ratio, quality, or diversity in various components, they do not analyze **the impact of these components on the final performance**. Specifically, the roles of the Quality Verification Agent, Single-hop Question Generation Agent, Multiple Question Sampling, and Multi-hop Question Merger Agent in the final framework are not discussed. Analyzing these would help demonstrate the independent contributions and practical necessity of each module. The provided metrics of high-quality, diversity, and multi-hop are not convincingly linked to downstream instruction-tuning performance. For example, it is unclear how a high score in the 'high-quality' metric directly translates to improved performance on specific tasks, and the paper lacks a clear demonstration of how these metrics interact to affect overall model performance.
2. Although the author compares the cost tokens of the proposed method in Section 4.2, Figure 12 still shows that LongMIT-GPT4o has **more than four times the cost tokens compared to Self-Instruct-GPT4o**. Considering that the method introduces multiple agents and complex merging strategies, this significantly increases the computational resources required while improving model performance, which may affect the feasibility of practical applications.
3. When analyzing different strategies, the author uses metrics such as retention ratio and average score. Could you provide a more detailed description and implementation method for these metrics to help readers better understand? Specifically, the paper lacks details on how the Quality Verification Agent's threshold is determined and what criteria are used to establish the 'average score' of the generated data.

### Questions
1. When analyzing different strategies, the author uses metrics such as retention ratio and average score. Could you provide a more detailed description and implementation method for these metrics to help readers better understand?

### Soundness
3

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
This paper introduces a Multi-agent Interactive Multi-hop Generation (MIMG) framework designed to enhance the quality of multi-hop instruction data for long-context tasks. The framework includes four main components: a Quality Verification Agent, a Single-hop Question Generation Agent, a Multiple Question Sampling Strategy, and a Multi-hop Question Merging Agent. Through these components, the proposed MIMG framework significantly improves the quality, diversity, and relevance of synthetic instruction data, which surpasses performance metrics achieved by models trained on larger human-annotated datasets.

### Strengths
The main strengths of this paper include: 

(1). Innovative Multi-agent Generation Framework: The proposed Multi-agent Interactive Multi-hop Generation (MIMG) framework incorporates multiple agents (Quality Verification Agent, Single-hop Question Generation Agent, Multiple Question Sampling Strategy, and Multi-hop Question Merging Agent), significantly improving the quality and diversity of generated data.  

(2). Extensive Experimental Validation: The paper systematically investigates various document selection, question merging, and validation strategies, backed by experiments across multiple models and domains, demonstrating the practical effectiveness and generalizability of the framework. 

(3). Enhanced Model Performance: Models trained with MIMG-generated data show an average improvement of 7.54% over those trained with larger, human-annotated datasets, underscoring the framework’s value in boosting long-context capabilities in large language models.

### Weaknesses
The main limitations of this paper are: 

1). The primary weakness of this paper lies in its limited novelty. The contributions primarily emphasize engineering implementations and optimizations rather than presenting groundbreaking theoretical or methodological advancements. While the proposed framework demonstrates effective improvements in long-context, multi-hop instruction datasets, it largely builds upon existing concepts and technologies in a structured engineering fashion.  

2). Limited Analysis of Long-term Effects on Model Robustness: While the paper demonstrates improvements in performance, it lacks a detailed investigation into how the synthetic multi-hop data affects model robustness and generalizability over long-term use, particularly in non-training contexts. 

3). Potential Bias in Synthetic Data Quality Verification: The quality verification process, although effective, relies on automated scoring and classification from LLMs. This approach may introduce bias, particularly in complex, nuanced cases where human judgment could differ, impacting the interpretability and reliability of the data. 

4). Token Cost of Rationale-based Generation: While rationale-based question generation can enhance quality, the paper notes that it significantly increases token consumption, raising concerns about its efficiency and scalability in resource-constrained environments. 

5). Minimal Exploration of Alternative Frameworks: The study primarily focuses on the MIMG framework without thorough comparisons to alternative data synthesis or augmentation frameworks, limiting insights into how it performs relative to other potential approaches.

### Questions
1.  Lack of Analysis on Failure Cases: There is limited discussion on the types of tasks or data where the proposed method may underperform. An analysis of failure cases or limitations in specific scenarios would provide a more balanced view of the framework's practical utility. 

2. A notable contradiction in this paper is the claim that "stronger LLMs can generate better single-hop questions" While the proposed framework aims to improve data generation quality and efficiency, the reported performance gains do not appear to match those achieved by simply using a stronger LLM. This inconsistency raises questions about the practical benefits of the proposed method, especially considering its added complexity. If a straightforward upgrade to a more powerful LLM yields comparable or superior results, the value of implementing this multi-agent framework diminishes. This aspect weakens the paper's argument for the proposed method as a more effective solution than alternative, less complex approaches.

3. To facilitate readers’ understanding of the related work in this field, it would be more effective to place the "Related Work" section immediately after the "Introduction." Currently, this section is written in a very general and unstructured manner, which makes it challenging to follow. Structuring the "Related Work" section into specific subcategories—such as "Large Language Models (LLMs)," "Multi-hop Instruction Datasets," etc.—would improve readability and provide a clearer context for the presented work.

### Soundness
3

### Presentation
3

### Contribution
2
