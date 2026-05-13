# GasketRAG: Systematic Alignment of Large Language Models with Retrievers

- Decision: Reject
- Scores: 5, 8, 6, 6, 5

## Abstract
Retrieval-Augmented Generation (RAG) has emerged as a powerful method for enhancing the output quality of large language models (LLMs). However, existing retrievers are not specifically optimized for LLMs, and retraining them requires substantial resources. Furthermore, current approaches are often constrained to either improving the relevancy of retrieved documents or refining the documents post-retrieval. Various stages within the typical RAG pipeline present challenges in aligning LLMs with retrievers. To address these issues, we propose GasketRAG, a novel approach that introduces a gasket between the retriever and the LLM to improve their collaborative performance. By employing innovative techniques, we gather high-quality preference data and use the gasket to optimize both retrieval ranking and document refinement simultaneously. Our approach circumvents the need for constructing complex training and inference pipelines. In a fair comparison against the latest RAG methods across multiple test datasets, GasketRAG demonstrated a clear advantage.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a “gasket” component positioned between the retriever and the large language model (LLM) within the RAG (Retrieval-Augmented Generation) framework. This gasket is trained using the KTO algorithm to selectively filter relevant sentences from the retrieved passages, leveraging preference data collected from the LLM and retrieval models. Experiments conducted on six datasets across three tasks demonstrate that the proposed GasketRAG method outperforms prior RAG approaches in most cases. Detailed analyses of KTO training, iteration counts, and latency are also provided, highlighting the features and efficiency of the GasketRAG approach.

### Strengths
1) This paper proposes a new RAG pipeline, GasketRAG, which introduces a gasket model to regulate data flow for improved LLM generation.
2) Extensive experiments on six datasets across three tasks, along with detailed analyses, are conducted to evaluate the effectiveness of GasketRAG approach.

### Weaknesses
1) The title and motivation of this paper may be somewhat overstated, as the proposed GasketRAG lacks a clear alignment mechanism between the LLM and the retriever. The core issue is that the 'alignment' is implicitly driven by the LLM's ability to answer questions correctly, rather than a more nuanced interaction that considers the retriever's inherent preferences or biases. The gasket model, while filtering sentences, doesn't explicitly address the fundamental differences in how retrievers and LLMs process information, such as the retriever's sensitivity to specific keywords versus the LLM's broader contextual understanding.
2) The proposed GasketRAG pipeline primarily relies on a model to filter relevant sentences and performs two retrieval steps before the LLM generation, which may lack sufficient novelty to make it stand out. The approach resembles pseudo-relevance feedback, where initial retrieval results are used to refine subsequent queries. The novelty is further diminished by the fact that the core mechanism is sentence filtering, which is a relatively straightforward operation. The two retrieval steps, while potentially improving results, add computational overhead without a substantial conceptual leap.
3) The description of preference data construction is somewhat disorganized, such as the settings of the base models for the gasket and generation components, as well as the distinctions between data construction and training process. The lack of clarity makes it difficult to understand the precise nature of the preference data and how it is used to train the gasket model. For example, it's unclear how the 'preferred' and 'dispreferred' labels are assigned, and whether the data collection process introduces any biases.

### Questions
1) How does the gasket model function as an aligner between large language models (LLMs) and retrieval models? My understanding is that the gasket is trained to select sentences that help the retriever find more relevant passages and assist the LLM in generating accurate answers. However, it’s unclear where the systematic alignment between the LLM and the retriever occurs.
2) How is “preference” defined for the LLMs and retrievers? According to Section 3.3, both LLM and retriever preferences are determined based on whether the LLM generator can produce a correct answer from the selected sentences. This seems to indicate that the “preference” signal comes solely from the LLMs. Besides, is it accurate to call this preference data?
3) Have you considered comparing the gasket model with a sentence-level ranking model, such as training a BERT model using the preference signal from the LLM to rank all sentences in the retrieved passages? This approach could potentially offer greater efficiency than an LLM-based filtering model, as BERT is generally faster and more lightweight.
4) In lines 201–203, it states “In the preferred group, for each y′, we calculate the average sentence index number. A lower average index number indicates that the retriever ranks useful information higher.” Why is the sentence index linked to retrieval effectiveness? The second-round retrieval yields a new set of passages, and how to assign the sentence IDs to these passages?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces GasketRAG, a novel approach to improve the performance of Retrieval-Augmented Generation (RAG) systems. 

The key contributions are:
1. A gasket model that acts as an intermediary between the retriever and the large language model (LLM) in the RAG pipeline. This gasket filters and refines the retrieved information to better align with both the retriever's and LLM's preferences.

2. A method for collecting high-quality preference data from both the LLM and retriever, which is used to train the gasket model offline. This avoids the complexity and instability of joint training approaches.

3. The use of weighted Kahneman-Tversky Optimization (KTO) to train the gasket model, which doesn't require initial supervised fine-tuning and enhances stability.

4. A two-iteration RAG process where the gasket model first filters initial retrieval results to enhance the query, then filters the results of a second retrieval before passing information to the LLM.

5. The authors evaluate GasketRAG against several baseline RAG methods across six datasets covering open-domain QA, multi-hop QA, and fact-checking tasks. Results show that GasketRAG outperforms existing methods on most test sets and metrics, demonstrating improved performance and stability across different question types.

6. The paper also highlights the fact about GasketRAG's ability to generalize, as the gasket model trained on preferences from one LLM (LLaMA-3-8B) still provides benefits when used with a different LLM (GPT-3.5-turbo) as the generator.

Overall, GasketRAG presents a novel approach to aligning retrievers and LLMs in RAG systems, addressing challenges in existing methods and demonstrating superior response accuracy and correctness.

### Strengths
**Originality:**
The paper presents a novel approach called GasketRAG that introduces an intermediate "gasket" model between the retriever and language model in retrieval-augmented generation (RAG) systems. This is an original idea that aims to systematically align the preferences of both components. 


_Key original aspects include:_ 

1. Using a gasket model as an information bottleneck to control data flow and align the retriever and LLM
2. Collecting high-quality preference data from both the LLM and retriever to train the gasket offline
3. Employing a two-iteration RAG process with query enhancement
4. While building on existing work in RAG, this approach creatively combines ideas in a new way to address alignment challenges.


**Quality**
The paper demonstrates strong technical quality in several ways:
1. Rigorous experimental design comparing GasketRAG against multiple state-of-the-art baselines across 6 diverse datasets
2. Careful ablation studies examining the impact of different components by experimenting with different iteraton and weights. 
3. Use of multiple evaluation metrics (Accuracy and Correctness) and comparing multiple baseline RAG systems.
4. Detailed analysis of results including failure cases such as how more iterations could be resulting in performance degradation, latency analysis.
5. Open-sourcing of code and data anonymosly to enable reproducibility
6. The use of weighted Kahneman-Tversky Optimization shows technical sophistication.
7. comparison of results between different setups  of the proposed approach such as effectiveness of weighted KTO.


**Clarity**
Overall, the paper is clearly written and well-structured. Key strengths in clarity include:

1. Clear problem motivation and positioning relative to prior work by citing multiple relevant recent research work. 
2. Detailed method description with helpful diagrams (e.g. Fig 1 and 2) and logical division of implementations steps such as classifying the sentences list at high level first and then addressing each sentence group seperately. 
3. Thorough experimental setup details with extnsive comarison between existing baselines.

Some sections (e.g. 3.3 Preference Collection) are quite dense and could potentially be clarified further. But on the whole, the paper effectively communicates the key ideas and contributions.

**Significance**
This work has the potential for significant impact in several ways:

1. Addressing a key challenge in RAG systems by better aligning retrievers and LLMs
2. Improving performance on important tasks like open-domain QA and fact-checking
3. Providing a flexible approach that can work with different off-the-shelf retrievers and LLMs
4. Offering insights into preference learning and information filtering for language models
5. The strong empirical results across multiple datasets suggest the approach could be widely applicable. 
6. The ability to generalize to different LLMs (e.g. from LLaMA to GPT-3.5) is particularly noteworthy.

### Weaknesses
 1. **Limited exploration of gasket model architectures:**  The paper uses LLaMA-3.1-8B-Instruct as the gasket model but does not explore alternative architectures or model sizes. Experimenting with smaller models or different architectures, such as encoder-only models or models with varying numbers of parameters, could provide insights into the trade-offs between performance, computational cost, and memory footprint. This is particularly important for deployment in resource-constrained environments. The paper should include a more detailed analysis of the gasket model's architecture and its impact on the overall system performance.
2. **Limited exploration of different retrievers:** The paper uses ColBERTv2 as the retriever but does not explore how GasketRAG performs with different retrieval methods. Given that retriever performance can vary significantly depending on the dataset and task, experimenting with alternative retrievers such as BM25, DPR, or Sentence-BERT would demonstrate the method's robustness and generalizability. The paper should also analyze how the gasket model's filtering mechanism interacts with different retriever outputs.
3. **Effective of various iteration scenarios against baseline:**  The effectiveness of iteration results claim that the 2-Iteration GasketRAG achieves the best overall performance but at the same time latency results shows that GasketRAG has slightly higher latency compared to SelfAsk and Iter-RetGen. However, the 1-Iteration Gasket is significantly faster than both while also delivering better performance. but there seems to be no experiments conducted for comparing GasketRAG with various iteration against other baseline RAG methods for accuracy and correctness to understand the impact of accuracy and correctness and make trade-offs. The paper should include a more comprehensive analysis of the trade-offs between the number of iterations, accuracy, correctness, and latency, especially when compared to other baseline RAG methods.

### Questions
1. How does the runtime and resource usage of GasketRAG compare to baseline methods, especially for larger-scale applications?

2. Have the authors experimented with different architectures or model sizes for the gasket model besides LLaMA-3.1-8B-Instruct? What were the trade-offs observed between performance and efficiency when using smaller models?

3. Have the authors tested GasketRAG with different retrieval methods besides ColBERTv2?

4. Have the authors experimented different iterations mode of GasketRAG and compared Accuracy/Correctness with other base line RAG approaches along with its latency to demonstrate different trade-offs?

5. Have the authors identified any potential biases introduced by preference data collection method?

6. How well does GasketRAG perform in larger datasets?

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces GasketRAG, a novel approach designed to enhance Retrieval-Augmented Generation (RAG) by optimizing the interaction between retrievers and large language models (LLMs). GasketRAG incorporates a "gasket" mechanism that facilitates improved collaboration between the retriever and LLM. This approach allows for the simultaneous optimization of both retrieval ranking and document refinement, eliminating the complexities associated with traditional training and inference pipelines. In comparative tests against state-of-the-art RAG methods, GasketRAG demonstrated superior performance across multiple datasets.

### Strengths
1.	This paper proposes a method to use an enhanced query (query + important sentences) to improve the performance of RAG techniques.

2.	This method considers both the preference of LLMs and retrievers by training gasket with data integrated with these preferences.

3.	Experiment performances show the effectiveness of the method.

### Weaknesses
1.	The motivation of the Gasket remains unclear to me. The authors claims that gasket is designed to consider the preference of both the retrievers and the LLM and that it serves as an information bottleneck to control the behavior of both the retriever and the LLM. However, it’s difficult to understand why retrieving the documents again with a combination of query and retrieved sentences could necessarily “control” the behavior of the retriever, consider its preference and benefit the final prediction. Specifically, the mechanism by which the gasket's sentence selection and query modification leads to improved retrieval is not well-defined. The paper lacks a clear explanation of how the gasket's training process translates into a demonstrable change in the retriever's behavior, and how this change aligns with the LLM's preferences. As shown in Table 4, more iterations could even harm the performance, suggesting that the iterative refinement process is not consistently beneficial and may introduce instability.

2.	Also, the claim about the alignment between LLMs and retrievers is also questionable. The only related part in the paper is section 3.3, where the training data of the gasket is collected considering the preference of LLMs and retrievers. However, it remains unclear how and why this could align them. The paper does not provide a rigorous analysis of how the preference data collection process ensures that the gasket learns to bridge the gap between the retriever and the LLM. The connection between the training data and the claimed alignment is not sufficiently justified, leaving the reader to question the validity of this claim.

3.	The method could not outperform the baseline models if it’s not specifically trained on the target dataset (WikiMultiHop, PubHealth, and StrategyQA). Also, I find the setting of testing on the dataset that has been used for the training of gasket is not quite fair for other baseline models since they do not require this. This raises concerns about the generalizability of the proposed approach. The fact that GasketRAG requires dataset-specific training to achieve superior performance suggests that it may overfit to the training data, limiting its applicability to new, unseen datasets. The lack of a thorough evaluation on diverse datasets makes it difficult to assess the true robustness of the method.

4.	The overall logic of the paper could be improved.

### Questions
1.	I think you should use \text{-} in the equations from L161-L168, now it looks like Top “minus” k.

2.	Could you explain a little bit more about the definition of “retriever preference” and how it’s related to the overall inference period of the proposed method? 

3.	Are there analyses about the differences between the sentences selected in the first and the second round? 

4.	Are there analyses about the advantage of the sentences retrieved in the second round and how could we explain the results in a more concrete way than only saying it’s an alignment between the preference of LLMs and retrievers?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a framework which attempts to adjust what sentences are presented to an LLM based on signal about whether those sentences allow the LLM to produce the correct answer or not. GasketRAG fine-tunes an intermediate LLM using preference training (Weighted KTO optimization) to improve the model's ability to choose which sentences are relevant to a specific query from a set of retrieved passages. 
This leads to improvements over previous RAG systems on several question answering datasets.

### Strengths
- The problem addressed by this paper is interesting and important, it is clear that future RAG system must close the loop between retriever and LLMs. This method introduces an attempt to solve this important issue.

### Weaknesses
 - The authors claim that the "preference" from the retriever is being used within the data collection but it seems like the only signal which decides between preferred and dis-preferred is whether an LLM can use the retrieved sentences to answer the query correctly. I do not think the Gasket is being trained on any retriever preference signal (please explain if you believe this to be a misconception).
- The GasketRAG concept is not very novel, it is actually a simple re-ranking module which helps determine which retrieved documents are relevant to a specific query. There are many such methods which leverage LLMs such as RankGPT (Sun et al 2023) and they should be used as baselines in this work.
- Preference training might be sophisticated and interesting but the motivation to use it is unclear. It seems to me that simple SFT could also allow for the "gasket" model to identify which textual chunks are relevant for the query.
 - Why is the "Direct" performance of both models in Table 2 sometimes stronger than the NaiveRAG implementation? This is very strange behavior, especially in factual QA datasets like these ones.

### Questions
See weaknesses

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
3

### Summary
The IR-LLM mismatch is a critical problem for RAG systems. In this paper, the authors propose to introduce a gasket model between retrievers and LLMs to enhance the RAG performance. Specifically, the Gasket model learns to select key sentences preferred by both LLMs and retrievers and iteratively generate context-augmented queries, and a data construction algorithm and a learning algorithm are designed to train the Gasket model. Experiments show some performance improvements over baselines.

I raise my score from 3 to 5 due to the rebuttal, but  my main concerns are still here for the over-claim problem and the incremental contribution.

### Strengths
In general, I think it is important to address the IR-LLM mismatch problem, and the idea of leveraging a gasket model is reasonable just like the classical copilot paradigm.  Furthermore, I think the learning algorithm and the data construction method for learning set preference with hidden labels are also helpful.

### Weaknesses
1. The idea of iteratively refining/rewriting queries is not new, although previous studies may not train their refining/rewriting models;
2. Relevant context selection/identification is also not a new idea. There are many related studies in long context LLMs and RAG methods;
2. Although the title is "systematic alignment of LLMs with retrievers", I don't think LLMs and Retrievers can be systematically aligned by only rewriting queries and selecting sentences;
3. The performance improvement in experimental results is not significant, especially comparing with naive RAG. The authors should analyze these surprising results in detail.
3. Furthermore, I think the baselines are too weak and the results are not convincing, the authors should at least compare their methods with: 1) the long context models which can identify and leverage information in long contexts; 2) RAG methods with denoising and iterative query rewriting components; 3) the same model of GasketRAG, but replacing the Gasket model with a strong LLM (e.g., GPT 3.5, Llama 3, etc.) without any training.

### Questions
See Weaknesses in above.

### Soundness
2

### Presentation
2

### Contribution
2
