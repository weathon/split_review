# DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Recent advances in natural language processing, primarily propelled by Large Language Models (LLMs), have showcased their remarkable capabilities grounded in in-context learning. A promising avenue for guiding LLMs in intricate reasoning tasks involves the utilization of intermediate reasoning steps within the Chain-of-Thought (CoT) paradigm. Nevertheless, the central challenge lies in the effective selection of exemplars for facilitating in-context learning. In this study, we introduce a framework that leverages Dual Queries and Low-rank approximation Re-ranking (DQ-LoRe) to automatically select exemplars for in-context learning. Dual Queries first query LLM to obtain LLM-generated knowledge such as CoT, then query the retriever to obtain the final exemplars via both question and the knowledge. Moreover, for the second query, LoRe employs dimensionality reduction techniques to refine exemplar selection, ensuring close alignment with the input question's knowledge. Through extensive experiments, we demonstrate that DQ-LoRe significantly outperforms prior state-of-the-art methods in the automatic selection of exemplars for GPT-4, enhancing performance from 92.5\% to 94.2\%. Our comprehensive analysis further reveals that DQ-LoRe consistently outperforms retrieval-based approaches in terms of both performance and adaptability, especially in scenarios characterized by distribution shifts. DQ-LoRe pushes the boundaries of in-context learning and opens up new avenues for addressing complex reasoning challenges.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose to leverage dual queries and low-rank approximation re-ranking to find the exemplars for in-context learning. LLM-generated knowledge can first be derived by dual queries so that the retriever can provide the final exemplars with both the question and the acquired knowledge. Experiments are conducted on several benchmark datasets when some of the datasets involve chain-of-thought (CoT) annotations. The experimental results show that the proposed method can outperform several conventional in-context learning methods with GPT-4 in the in-domain setup. With domain shifts, the proposed framework also surpasses baseline methods with two different LLM engines. Besides, the authors also conduct some ablation and analysis studies to show the effectiveness of the key component LoRE.

### Strengths
* S1: The LoRe component can significantly improve the performance of models that consider CoT as shown in the ablation study.
* S2: The improvements are consistent within most of the cases for both in-domain and domain-shifted scenarios.
* S3: Ablation and qualitative studies demonstrate the rationales behind the improvements.

### Weaknesses
 * W1: The idea of "dual queries" is not novel when many studies [a] have already utilized LLMs themselves to have better queries for retrieval augmentation.
* W2: Datasets are limited. All of the datasets are about arithmetic questions.
* W3: Some mentioned related studies like Auto-CoT (Zhang et al., 2022) are not compared in the experiments, especially while their studies are more general and conducted on more datasets.

### Questions
* Q1: I wonder if the authors conduct significance tests on the improvements of the proposed method over baseline methods.
* Q2: Following W2 and W3, it would be great if the authors could involve more datasets and baseline methods in the experiments.Q4:

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes DQ-LoRe, a method of completing reasoning tasks by retrieving higher quality in-context exemplars. In the first query, the question and initial exemplars are used to induce a CoT from the LLM, which is then used in the second query to retrieve the final exemplars. Those exemplars are then used as part of the prompt for the final inference to complete the tasks. The retriever is trained on BM25 and LLM predictions. PCA is used to reduce the embedding dimensions so that the retrieval can be based on non-spurious features.

Using GPT-4 as its engine, the method reaches state-of-the-art performance on GSM8K and shows strong out-of-domain performance. Ablation, visualization, and case studies are included to help better understand the method.

### Strengths
- The method achieves SOTA performance as well as great robustness on an important area of current NLP/LLM research: reasoning.
- The core method, DQ-LoRe is original to the best of my knowledge. It is also relatively easy to understand.
- The method is implemented at the prompt level, so it should be easy to apply to a wide range of models and use cases.
- The presentation of the study is good. Figure 1 is clear and helpful. The paragraphs are generally well written. See typos in the Questions section.

### Weaknesses
 - The return on Investment (ROI) of the method is not super high. The method outperforms SOTA accuracy by 1.7 at the cost of：
 1. Complex implementation. The method involves an additional query of the LLM, a retrieving step, a dimensionality reduction step, and a re-ranking step. One might find it hard to justify the complexity with the 1.7 point improvement.
2. High latency, as a result of the additional steps, which makes it not ideal for real-life use cases.
- Reproducibility: For complex systems like this, it is important for the authors to release their source code subsequent studies can make use of. I do not find a promise to release the source code. Will you release your code?
- Would be great to include more LLMs to demonstrate the generalizability of the method.

### Questions
- Typo? on page 9: "a dual-query framework that enhances in-context learning for multi-step reasoning tasks by considering the Contexts of Interest (CoTs) in input questions and exemplars"
- Typo on page 2: "Following the acquisition of re-ranked exemplars from the smaller retrieval model, DQ-LoRe subsequently provides the exemplars to the LLMs for inference.,"
- Would be nice to include an analysis of latency.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, authors propose a new approach to extract exemplars in LLM for effective inference. They propose a 2 stage process where first stage focuses on chain of thought reasoning for a given query, the chain of thought output is then used with dimentionality reduced model to extract similar queries which is then used to perform effective inference. They show improvement over previous approaches is choosing exemplars.

### Strengths
Well written paper. Easy to understand. Simple yet effective approach to improve prompt generation and model performance of LLMs.

### Weaknesses
Novelty not high in my opinion. Low-rank approximation is a neat extension, but it is being used as regularizer to some extent. No mention of any other form of regularization is mentioned.

To support statements like low-rank helps mitigate finding spurious correlation, it would be good to include a version of their approach in the experiment where low-rank approximation was not performed.
Minor but makes it a bit hard to read: Too many abbreviation and some like ERP are not expanded (assuming they consider it as background knowledge). Not much mention of what the baselines are. Will be good to include that a bit.

### Questions
To support statements like low-rank helps mitigate finding spurious correlation, it would be good to include a version of their approach in the experiment where low-rank approximation was not performed.
Minor but makes it a bit hard to read: Too many abbreviation and some like ERP are not expanded (assuming they consider it as background knowledge). Not much mention of what the baselines are. Will be good to include that a bit.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce a novel framework named DQ-LoRe, aimed at addressing the exemplar selection challenge in Large Language Models (LLMs) for in-context learning. They designed a dual-query mechanism, which first queries the LLM to obtain its generated knowledge and then queries the retriever to obtain the final exemplars. Additionally, they incorporated a low-rank approximation re-ranking technique to ensure that the selected exemplars align closely with the knowledge of the input question. This approach not only focuses on the similarity between the input question and the examples in the training set but also effectively leverages the relationship between the intermediate reasoning steps of the given question and the exemplars. Through a series of experiments, the authors demonstrated the superiority of DQ-LoRe in automatic exemplar selection. Overall, this work offers a fresh perspective on in-context learning and paves the way for future research.

### Strengths
1. Originality:
The paper introduces a novel framework named DQ-LoRe (Dual Queries with Low Rank Approximation Re-ranking) that addresses the challenge of selecting exemplars for in-context learning.
The approach of using Dual Queries is innovative. It first queries the Large Language Model (LLM) to obtain LLM-generated knowledge such as Chain-of-Thought (CoT) and then queries the retriever to obtain the final exemplars using both the question and the knowledge.
The concept of using Low Rank Approximation for re-ranking, especially in the context of in-context learning, adds to the originality of the work.

2. Quality:
The paper showcases extensive experiments to validate the effectiveness of DQ-LoRe.
The results indicate that DQ-LoRe significantly outperforms prior state-of-the-art methods in the automatic selection of exemplars for GPT-4.
The paper provides a comprehensive analysis, revealing that DQ-LoRe consistently surpasses retrieval-based approaches in terms of both performance and adaptability.

3. Clarity:
The paper is well-structured and presents its methodology and findings in a clear and concise manner.
The use of terms like Dual Queries, Low-rank approximation Re-ranking, and Chain-of-Thought are well-defined and contribute to the clarity of the paper's content.

4. Significance:
The paper addresses a central challenge in the domain of in-context learning, which is the effective selection of exemplars. The improvement in performance from 92.5% to 94.2% on GSM8K highlights the significance of the proposed approach. By pushing the boundaries of in-context learning, DQ-LoRe opens up new avenues for addressing complex reasoning challenges, making it a significant contribution to the research community.

In summary, the paper presents a significant and original contribution to the field of in-context learning by introducing the DQ-LoRe framework. The quality of the research is evident from the comprehensive experiments and analysis provided, and the content is presented with clarity.

### Weaknesses
 1. Limited Originality:
While the paper introduces the DQ-LoRe framework, the methods employed (such as BM25, PCA dimensionality reduction, etc.) are based on prior research. Although the authors have adeptly integrated and applied these methods within their framework, from an innovation standpoint, these techniques are not novel in themselves.

2. Methodological Concerns:
The first round of sorting in the paper uses BM25 to match the question with the question in the exemplar, aiming to find the exemplar most relevant to the question. The second round aims to find the Chain-of-Thought (CoT) most relevant to the question. This raises a question: Why not directly compute the similarity between the CoT in the exemplar and the CoT of the question itself? Instead, the approach seems to add unnecessary complexity by opting to compute scores for the generated CoT.

3. Experiments Could Be More Robust:
While the authors perform commendably in comparative experiments, the ablation studies appear to be lacking. For instance, it would be beneficial to compare the effects of two rounds of sorting versus a single round, and the effects of PCA dimensionality reduction versus no reduction. Such experiments might offer readers more insights into the efficacy of the methods.

4. Detailing Issues:
Figure 1 in the paper has errors. Specifically, in the "M Q&A Low rank embedding" section, "Embedding 1" appears twice, which might lead to confusion. Authors should ensure that all charts and graphics are accurate and clear to avoid any potential misunderstandings.

### Questions
1. Originality Concerns:
Could the authors elaborate on the novelty of the DQ-LoRe framework, especially considering that methods like BM25、PCA、text-davinci-003 dimensionality reduction have been previously employed in other works?

2. Methodological Clarifications:
What was the rationale behind opting for two rounds of sorting (first for matching the question with the exemplar and second for finding the relevant CoT) instead of directly computing the similarity between the CoT in the exemplar and the CoT of the question?

3. Experimental Details:
In the ablation studies, could the authors provide results comparing the effects of two rounds of sorting versus a single round? Additionally, it would be beneficial to see the effects of PCA dimensionality reduction versus no reduction. How do these individual components impact the overall performance?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
