# READ-SQL: Reasoning Path Decomposer for Text-to-SQL

- Decision: Reject
- Scores: 5, 6, 5, 3, 3

## Abstract
Text-to-SQL is a longstanding task aimed at automatically converting natural language questions into SQL queries for database retrieval. Despite impressive advancements, particularly with Large Language Models (LLMs), existing methods still struggle with issues such as misinterpreted, omitted, or unwanted constraints.  To address these challenges, we propose READ-SQL, a novel framework employing a \underline{re}asoning p\underline{a}th \underline{d}compos\underline{er}, \textbf{READ}ER, for text-to-SQL tasks.  READER decomposes SQLs into clauses, sub-SQLs, and reasoning paths, supporting data preparation and confidence level determination in post-processing.  READ-SQL comprises two main models: a Generator and a Corrector, both trained via LoRA for parameter efficiency.  Based on READER's decomposition, READ-SQL generates two types of augmented data using an LLM: question/SQL pairs and question/reason pairs.  The Generator is trained on both original and augmented data to identify constraint changes and enhance reasoning.  The Corrector is trained on data from READER’s post-processing, improving self-correction by refining high-confidence SQLs and addressing low-confidence elements.  Extensive experiments show that READ-SQL significantly outperforms leading baselines, with READ-SQL-3B achieving 57.37\% execution accuracy on BIRD’s dev set, surpassing several 7B-parameter models and setting a new state-of-the-art with fewer parameters.  Additionally, READER and the Corrector show broad applicability when integrated with LLMs or other base models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents READ-SQL, a framework that uses SQL decomposition for two main purposes: (1) data augmentation for training an SQL generator and (2) self-correction by training a corrector that uses common and differing clauses among multiple generated SQLs to refine the SQLs. The model demonstrates improved performance over baselines on the BIRD, Spider, and various Spider benchmark variants.

Some comments on presentation and typos:

1. Line 301: "the above three kinds of data" — only two types are explicitly listed.

2. Figure 4: The caption refers to a yellow color not present in the figure.

3. Table 4: The first two rows label “coder-1.3B-1.3B” with “1.3B” duplicated unnecessarily.

### Strengths
1. The proposed SQL decomposer, utilizing AST parsing, is both novel and efficient, providing a scalable approach.

2. The self-correction method based on common and differing clauses is innovative.

3. The framework enhances performance for smaller models.

### Weaknesses
1. The writing could be improved to be more direct and accessible. Section 3.4 is incomplete — it only describes the extraction of common and different constraints without explaining the subsequent self-correction process. Some insights can be found in Figure 4, but the absence in the main text hinders comprehension.

2. The comparisons with other models are somewhat unfair; READ-SQL-3B includes two 3B models (i.e., a 3B generator and a 3B corrector), so a direct comparison with CodeS-3B may not be appropriate.

3. The performance improvements are modest, especially considering the combined use of two 3B models.

### Questions
1. Line 44 mentions three typical categories of text-to-SQL errors. Are there any statistics on the frequency of these error types?

2. How would the performance be affected if question-SQL pairs and question-reason pairs were combined into question-reason-SQL chain-of-thought data for fine-tuning CodeS?

### Soundness
3

### Presentation
2

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
This paper introduces READ-SQL, a novel framework for enhancing the text-to-SQL task by using a reasoning path decomposer called READER. The framework aims to address challenges such as misinterpreted or omitted constraints in SQL generation. READ-SQL comprises a Generator and a Corrector, both of which leverage READER to break down SQL queries into sub-SQLs and reasoning paths for better data preparation and correction. Extensive experiments show that READ-SQL outperforms competing baselines, achieving strong results with fewer parameters and demonstrating applicability across different models and scenarios.

### Strengths
1. The proposed framework achieves promising results using small LLMs (1B and 3B models), which is advantageous for local deployment and reduces computational resource requirements in real-world applications. Given that the text-to-SQL community primarily focuses on larger proprietary LLMs, this work advances research on smaller-scale LLMs, providing practical benefits for scenarios such as on-device AI.

2. This paper introduces common errors in text-to-SQL and presents a detailed error analysis to validate the framework. Experiments conducted on five well-recognized datasets, including BIRD and Spider variants, provide strong evidence of the framework's effectiveness, showcasing comprehensive experimental support.

3. Overall, the framework is technically sound and novel. The paper is well-structured and easy to follow, effectively presenting the methodology, experiments, and results, which allows readers to easily understand the contributions and significance of the proposed approach.

### Weaknesses
1. The baseline included in the paper is insufficient. As a submission in October 2024, and in reference to recent studies [1][2], the paper should compare against more advanced baselines, such as [3][4][5][6]. Although this comparison of performance may not be entirely fair due to the varying scale of model parameters, the authors could highlight their advantages in other aspects, such as model size, GPU resources, and runtime. Comparing to up-to-date baselines would strengthen the paper's position for submission to a top conference.

2. The paper lacks a detailed runtime analysis. Given the focus on using smaller-scale LLMs, adding an analysis of training and inference times would underscore the practical advantages of the lightweight design. Such an analysis would further emphasize the framework's efficiency in real-world settings, particularly for on-device and resource-constrained applications, thereby enhancing the paper's impact.

3. The performance of the proposed framework seems limited in terms of generalization across different datasets. While it shows significant improvement on the more challenging BIRD dataset (with more complex database environments), its performance on simpler Spider-based databases is less pronounced, and in some cases, even demonstrates negative optimization. This discrepancy seems counterintuitive, especially since the framework does not explicitly claim to be suited only for complex scenarios.

### Questions
1. Can READ-SQL work on larger-scale models (e.g., 13B, 34B LLMs)? Since the proposed framework already achieves comparable performance with small-scale LLMs, it would be interesting to explore whether the framework could outperform GPT-4-based methods when incorporating 70B models. Alternatively, if READ-SQL cannot work on larger-scale models, it would be helpful to explain why.

2. Since the most direct comparison for the model at the same scale is with SFT CodeS-1B and SFT CodeS-3B, could the authors provide a detailed analysis of the specific types of questions where READ-SQL shows improvement? A statistical analysis of correct samples based on difficulty level, along with a straightforward case study comparing READ-SQL with CodeS, would help readers better understand the contributions and improvements.

3. Does READ-SQL struggle when handling ambiguous questions? The improvement brought by READ-SQL in robustness datasets such as Spider-Syn and Spider-Realistic (+1.3 and +0.4) is not as significant as in standard datasets like BIRD and Spider (+2.35 and +0.8). Moreover, why does READ-SQL-3B even show negative optimization in Spider-DK (-0.2)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
READ-SQL introduces an innovative approach that leverages Abstract Syntax Trees (ASTs) to efficiently extract chains of reasoning by incorporating each SQL constraint, as well as to identify all sub-SQL components. This strategy supports their development of a two-step process involving generation and correction. The generator is trained on both SQL generation and reasoning tasks, enabling the model to learn step-by-step reasoning necessary for producing accurate SQL queries. Using the constraints generated from the READER, corrector will find the low-confidence constraints and try to fix them. Experimental results indicate that this method achieves state-of-the-art (SOTA) performance with open-source LLMs under 3 billion parameters.

### Strengths
1) The primary strength of this paper lies in the READER method. By decomposing SQL queries into sub-queries, the proposed approach effectively facilitates multi-step reasoning, guiding the model to generate the final answer.

2) The proposed approach achieves state-of-the-art performance compared to all models with fewer than 3 billion parameters on two well-known benchmarks: BIRD and Spider.

### Weaknesses
1) The main weakness of this paper lies in the experimental section. The baselines used are primarily methodologies that do not represent the most recent advancements in the field, such as Distillery, CHASE-SQL, and CHESS. Although the paper states that the main baseline is the SFT CodeS model itself, it would be beneficial to compare their approach with more advanced fine-tuning methods, such as using zero-shot chain-of-thought prompting to generate reasoning steps and training the CodeS model with those reasoning paths. Specifically, the absence of comparisons with methods that leverage large language models for few-shot or zero-shot reasoning, which have shown strong performance in SQL generation, is a notable gap.

2) According to the results shown in Table 2, there are two instances where the performance of READ-SQL is lower than the SFT version of the CodeS model. This may indicate overfitting on the Spider dataset, which could explain why READ-SQL outperforms the SFT CodeS model on Spider specifically. The fact that performance dips on certain subsets raises concerns about the robustness and generalizability of the proposed method, suggesting a potential bias towards the training data characteristics.

3) To better assess the effectiveness of their proposed correction methodology, it would be valuable to compare it with basic self-correction methods, such as those outlined in the DIN-SQL paper. This comparison would help determine whether the improvement comes solely from an additional LLM call or from the specific advantages of the proposed method. Without this comparison, it is difficult to isolate the contribution of the proposed correction mechanism from the general benefits of iterative refinement using a large language model.

### Questions
N/A

### Soundness
2

### Presentation
3

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
READ-SQL is a framework designed to improve the conversion of natural language queries into SQL commands, an area known as text-to-SQL. This framework incorporates two main models, Generator and Corrector, which work with a core module, READER. READER decomposes SQL queries into components, helping to build reasoning paths. The Generator initially formulates SQL based on input questions and generated data, while the Corrector refines these SQLs by focusing on high- and low-confidence components. Together, they achieve significant accuracy and efficiency improvements over comparable models, even those with larger parameter sizes, as shown in the extensive experiments on benchmarks like BIRD and Spider​.

### Strengths
1. READ-SQL outperforms existing models on the BIRD benchmark, achieving high execution accuracy and efficiency.
2. Extensive testing on multiple datasets and with various experimental setups (e.g., ablation studies, different model sizes) demonstrates the framework's consistency and robustness.

### Weaknesses
1. The paper highlights three key issues in text-to-SQL: misinterpreted constraints, omitted constraints, and unwanted constraints. However, these issues are neither addressed nor mentioned in the experimental section, nor are they resolved in the proposed approach, which I find confusing.
2. The authors state, “However, existing methods primarily focus on optimizing SQL generation without improving the model’s understanding of the question or establishing strong relationships between questions and SQL clauses.” From my perspective, schema linking already serves to establish relationships between queries and SQL structure, which weakens this point as a unique limitation. Additionally, READ-SQL does not appear to be significantly better than other methods in terms of understanding the question. Furthermore, they mention, “Additionally, since these methods do not employ an end-to-end architecture, there is potential for information loss during the process.” Based on my understanding, T5-based and GPT-4-based approaches share a similar end-to-end structure with READ-SQL, as they transform inputs directly into SQL queries. Therefore, this limitation also seems unconvincing. Overall, the motivation for READ-SQL remains unclear to me.
3. Although augmented data enhances performance, generating question/reason pairs involves complex processing that may pose implementation challenges. More importantly, even with additional training data, the performance gains on the Spider dataset are less significant than on the BIRD dataset. This raises the question of whether the observed improvements might be due to overfitting, as the paper indicates that most of the augmented data originates from the BIRD dataset.

### Questions
1. What specific advancements does READER bring compared to earlier SQL decomposers?
2. How scalable is READ-SQL beyond 3 billion parameters, and are there plans for optimizing even larger-scale models?
3. Through augmented data generation, where question/SQL pairs and question/reason pairs are created, READ-SQL enhances comprehension of complex queries. Open-sourcing this related data would further support the broader community.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studied the Text-to-SQL task, and proposed a READ-SQL framework to improve the model's understanding of questions and SQL clauses. READ-SQL parsed the SQL into AST and decomposed into clauses to form the sub-SQLs and reasoning paths. Based on the sub-SQL and reasoning, READ-SQL generated augmented data with the LLM to train a Generator sensitive to constraint changes and reasoning. READ-SQL also trained a Corrector to recognize low-confident clauses for self-correction. Finally, the authors conducted extensive experiments to demonstrate the effectiveness of the proposed method.

### Strengths
1. The idea of aligning the natural language and structured syntax to correctly interpret the constraints is interesting.
2. The paper proposed to generate the augmented training data via clause decomposition of SQL, which is novel.
3. The proposed method outperformed leading baselines, and surpassed larger models on BIRD dataset.

### Weaknesses
1. The proposed seemed to be an incremental improvement of the existing Text-to-SQL methods, and the technical contributions seemed to be limited.
2. The inference pipeline of the proposed framework is unclear. The paper detailed introduced the data generation process, but it did not show how the trained generator and corrector were used to generate the SQL, i.e., the paper lacked an overall description from the text input to the SQL output.
3. The motivation behind the proposed method should be clarified more clearly. For example, what is the purpose of constraint identification and decomposition, and why can it solve the problems mentioned in the introduction.
4. Some technical introductions are unclear, which makes it difficult to understand the paper.
- What does the constraint or sub-SQL mean, and what can be considered as a constraint?
- What are the goals of the Generator and Corrector, how are they used in SQL generation, and how is the Corrector trained and realized?
- The proposed method regenerated the question based on the sub-SQL, so what is the relation between the generated question and the original ones, and have the authors considered their consistency? Besides, how did the authors ensure that the sub-SQL could solve the generated question?

### Questions
See the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
