# Lexical Diversity-aware Relevance Assessment for Retrieval-Augmented Generation

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Despite their extensive applications, large language models trained on vast historical datasets still struggle with hallucination issues, particularly when addressing open-ended, factual, and commonsense questions. In contrast, Retrieval-Augmented Generation (RAG) methods have proven effective in enhancing large language models' responses to such inquiries, making them a focal point of research.
However, previous RAG approaches overlook the lexical diversity of queries, hindering their ability to achieve a granular relevance assessment between queries and retrieved documents, resulting in suboptimal performance.  In this paper, we introduce a Lexical Diversity-aware RAG (DRAG) model, comprising a Diversity-sensitive Relevance Analyzer (DRA) and a Contrastive Relevance Calibration Module (CRC). Specifically, DRA decouples and assesses the relevance of different query components (words, phrases) based on their levels of lexical diversity, ensuring precise and comprehensive document retrieval. According to the DRA assessment, CRC further emphasizes the pertinent knowledge of the retrieved relevant documents through contrastively eliminating the adverse effects of irrelevant contents. By integrating DRA and CRC, the proposed method effectively retrieves relevant documents and leverages their pertinent knowledge to refine the original results and generate meaningful outcomes. Extensive experiments on widely-used benchmarks demonstrate the efficacy of our approach, yielding a 12.5\% accuracy improvement on HotpotQA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a Lexical Diversity-aware RAG framework. In DRA module, the author tailors query decoupling task and corresponding relevance assessment to eliminate the negative impact caused by lexical diversity, applying a granular retrieval and reranking process. Then, the contrastive decoding method is introduced in CRC module for subsequent answer generation, utilizing the result from DRA module. The proposed framework is evaluated by numerical experiments on three tasks across multiple datasets.

### Strengths
1.	It raises the question about how lexical diversity can influence the retrieval stage, and proposes a comprehensive framework to handle it. 
2.	I believe the proposal of query decoupling part is good, it covers three attributes from a reasonable perspective.
3.	The CRC utilizes the assessment from DRA, which is a very natural design.

### Weaknesses
1. The paper mainly follows the standard approach of training models with generated data and then performing inference. The contrastive decoding method is just integrated within the framework. From this perspective, it has limited novelty.
2. The author only provides experiments to demonstrate that the proposed method outperforms others, but there is a lack of detailed experiments and analysis showing how the identified issue of lexical diversity is addressed by the proposed framework.

### Questions
1.	Is it necessary to train the model component of DRA in different scenarios? If it is intended to be general, how well does this module generalize across different datasets?
2.	In the appendix C, comparing other retrieval models, why weren’t more commonly used retrieval models selected? Based on the experiments presented, it seems hard to see a significant improvement in retrieval performance using the DRA component.

### Soundness
3

### Presentation
3

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
This paper introduces a Lexical Diversity-aware RAG (DRAG) model, comprising a Diversity-sensitive Relevance Analyzer (DRA) and a Contrastive Relevance Calibration Module (CRC).

DRAG: A small model trained to decouple queries and classify the relevance of retrieved documents.

CRC: Calibrate the model’s decoding process by contrasting it with outputs under noise information.

### Strengths
This paper explores word-level decomposition for Retrieval-Augmented Generation (RAG) and introduces a method to train Large Language Models (LLMs) to effectively ignore noise in the context.

### Weaknesses
This paper proposed a good solution for word-level decomposition. However, I have two questions about the evaluation process.

1. The first stage just involves using a trained LLM to process the query, which improves the performance of multihop-query. This module works great.  However, how about this module compare to normal query decompose? The processes between these two methods are highly similar.

2. For the second stage, CRC, how about this process compared to a normal LLM + Ranker? They share the same function. The improvement gain of CRC in Table 3 is marginal.

### Questions
The same with the weakness section.

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
The paper introduces a Lexical DRAG model, aiming to enhance LLMs by addressing the limitations of previous RAG methods. DRAG incorporates a DRA module and a CFC module to refine the relevance assessment between queries and retrieved documents. The method significantly improves performance by ensuring a more granular and accurate relevance evaluation, leading to a 12.4% accuracy boost on the HotpotQA benchmark.

### Strengths
- The focus on improving the diversity of the retrieved documents in RAG systems is promising and practically beneficial, addressing a critical problem in the field.
- The method’s effectiveness is clearly demonstrated through substantial experiments, showing notable improvements in accuracy across several benchmarks.
- The paper is well-written, and the idea is easy to understand and follow.

### Weaknesses
 - While the method is innovative, its technical depth appears limited, relying significantly on GPT-4 data augmentation. The application of contrastive relevance calibration could be viewed as a nuanced extension of contrastive decoding, lacking substantial novelty.
- The validation for the correctness of generated data is missing. Effective validation would ideally include rigorous human annotation to ensure the quality and factual accuracy of the augmented data.
- The need for an additional module to decompose the query and multiple retrieval processes introduces considerable computational costs, which might limit the method’s applicability in real applications. This aspect, along with its impact on system efficiency, should be discussed.
- The model’s applicability to complex, multi-hop question answering scenarios (e.g., identifying sequential factual relationships) seems limited. When a sub-query is dependent on the other one, it is hard to retrieve relevant documents in a single retrieval step.

### Questions
Please consider to reply to my concerns in weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Lexical Diversity-aware RAG, which conducts relevance assessment between queries and documents from the perspective of lexical diversity and adopts contrastive decoding to eliminate the adverse effects of irrelevant contents. Experiments on two short-form, two multi-hop and one long-form knowledge-intensive generation/QA tasks show its superior performance.

### Strengths
1. The paper provides a fine-grained relevance assessment between queries and retrieved documents by introducing the concepts of lexical diversity, which is both interesting and important. It helps to filter out irrelevant content more accurately, reducing hallucinations and errors in downstream generation.
2. The paper offers valuable insights into document reranking in RAG, emphasizing the importance of delivering high-quality content to improve RAG performance.
3. The experiments show that the proposed method achieves strong performance.

### Weaknesses
The paper clearly offers new insights and solutions for the RAG research field. However, this paper has some issues that need to be addressed or clarified:
1. The explanation of the invariant component in Lines 200-203 lacks clarity. For example, "Paris," the capital of France, is often referred to as the "City of Light." If a retrieved document uses "City of Light" without explicitly mentioning "Paris," whether the method proposed is able to handle such issues? Could the author clarify how the proposed method handles cases where "invariant" components have common alternative expressions or propose ways to extend the method to account for such cases?
2. The "supplementary" component serves a valuable purpose, but it is generated directly by the fine-tuned LLM, which inevitably introduces hallucinations. These hallucinations can inject noise into the output, compromising the accuracy of the scoring results. Could the authors also discuss if there are any measures to mitigate this issue or the potential solutions?
3. The contribution of the proposed CRC is limited, as many solutions have explored to utilize the contrastive decoding in RAG to solve similar issues[1][2][3]. Besides, CRC requires parallelly deploy two identical LLMs, this will result in double the deployment costs and computational overhead. Could the authors ptovide more clearly differentiate their CRC approach from existing contrastive decoding methods in RAG? And, the author may also need to clarify the computational efficiency concerns and discuss any potential optimizations or trade-offs.
4. The transferability of the proposed method remains uncertain. The paper leverages data from PopQA and TriviaQA to generate training sets for fine-tuning the model, followed by validation on PopQA, TriviaQA, HotpotQA, 2WikiMultihopQA, and ASQA. While these datasets include a variety of question-answering formats, such as short-form, multi-hop, and long-form, they are all based on wiki-style content. To more convincingly demonstrate the method's effectiveness, the authors should extend their evaluation by testing the trained model on more open and domain-diverse RAG datasets, like FreshQA. Could the author also discuss the potential challenges in applying their method to non-wiki-style datasets and propose specific experiments to show the performance on these datasets?
5. The experiment setup is unclear, and the appendix does not provide additional information: (1) How is factual accuracy calculated? (2) Why is accuracy used as the evaluation metric for the multi-hop dataset, while many prior works, such as SuRe[4], SeaKR[5], and DRAGIN[6], typically use EM/F1 as evaluation metrics? (3) Were all the comparison methods reproduced under the same conditions? (4) What is the source of the retrieval?
6. This paper only compares a few recent RAG methods, and to some extent, the proposed approach is also similar to query expansion/decomposition-based RAG methods. Could the authors propose more comparisons among different RAG methods, such as SeaKR[5], DRAGIN[6], RQ-RAG[7], etc., to help to highlight the differences?
7. Please refer "Questions" section for some minor but noticeable issues.

### Questions
1. In Lines 751-752 of the Appendix, the author claims that "manual evaluation indicates GPT-4's predictions align well with human assessments." However, they do not provide any details on the evaluation methods or results to support this claim. Although GPT-4 is highly capable, it still produces hallucinations and incorrect predictions. It is unclear how the author ensured accurate data filtering and quality control to guarantee the correctness of the synthesized data. Could the authors provide specific information about their evaluation process, such as the number of samples evaluated, the criteria used for assessment, and any inter-rater reliability measures if multiple evaluators were involved?
2. Table 3 presents the overall impact of DRA and CRC but lacks a detailed analysis of the effectiveness of individual components within DRA. Specifically, how do the <invariant>, <variant>, and <supplementary> components each contribute to the observed performance improvements? Could the authors conduct an ablation study that isolates the impact of each component on the overall performance?

### Soundness
3

### Presentation
3

### Contribution
2
