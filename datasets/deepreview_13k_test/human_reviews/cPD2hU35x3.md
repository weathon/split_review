# ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities

- Decision: Accept
- Scores: 5, 6, 6, 6, 6

## Abstract
In this work, we introduce ChatQA 2, an Llama 3.0-based model with a 128K context window, designed to bridge the gap between open-source LLMs and leading proprietary models (e.g., GPT-4-Turbo) in long context understanding and retrieval-augmented generation (RAG) capabilities. 
These two capabilities are essential for LLMs to process large volumes of information that cannot fit into a single prompt and are complementary to each other, depending on the downstream tasks and computational budgets.
We present a detailed continued training recipe to extend the context window of Llama3-70B-base from 8K to 128K tokens, along with a three-stage instruction tuning process to enhance the model's instruction-following, RAG performance, and long-context understanding capabilities.
Our results demonstrate that the $\mathtt{Llama3\text{-}ChatQA\text{-}2\text{-}70B}$ model outperforms most existing state-of-the-art models, including GPT-4-Turbo-2024-04-09, Qwen2-72B-Instruct, and Llama3.1-70B-Instruct, on ultra-long tasks beyond 100K tokens, as well as on the RAG benchmark using only a 4K context window, showing the strong long context capability across varying sequence lengths.
We further provide extensive comparisons between direct long-context and RAG solutions using the same state-of-the-art long-context LLMs.
Interestingly, we find that the performance of strong long-context LLMs using RAG improves when retrieving a larger number of chunks. With a large set of top-\emph{k} chunks, RAG consistently outperforms direct long-context solution using the same state-of-the-art long-context models (e.g., {\our} and Qwen2-72B-Instruct) on both 32K benchmarks and real-world 128K tasks.
To advance research in this field, we open-sourced the model weights,
training data, and the evaluation setup for the for the community: \url{https://chatqa2-project.io/}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a way to train a short context base model to handle long context. In involves positional encoding (RoPE) to allow long context handling, pretraining on long context data and RAG. The trained performance on llama 70b shows comparable results to commercial LLMs in long context.

### Strengths
The performance looks good.

### Weaknesses
- The method is not clearly presented. I don't understand what fundamental changes of RAG or finetuning that makes the long context performance better
- The ablation study of the training process / design is missing. I don't understand the takeaway message from this paper

### Questions
- More details in the method. The 3.1 and 3.2 looks quite common. Since the authors emphasizes RAG, what specific changes have the authors made? And how RAG is used in the training?
- I am a bit confused by the highlight of this paper. I suppose the authors want to present a training pipeline for long context. But I don't quite understand the ablation of why certain choices are made.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces ChatQA 2, an open-source long-context language model with a 128K token context window, aiming to achieve performance comparable to GPT-4-Turbo. By leveraging a continue pretraining and a three-stage instruction tuning process, ChatQA 2 demonstrates improved accuracy and robustness in handling large volumes of context and consistently outperforms direct long-context models when using RAG with sufficient top-k chunks.

### Strengths
1. This paper introduces a significant enhancement to Llama3-70B’s long-context processing abilities, extending its context window from 8K to 128K tokens. Compared to Llama3.1with 128K context window, the proposed ChatQA2 achieves better performance. 

2. This paper proposes a three-stage instruction tuning, and collect a long SFT dataset to enhance the model's capability to handle very long context sequences up to 128k tokens. 

3. The authors propose utilizing the latest long-context retriever to address challenges in the current RAG pipeline for LLMs, specifically the limitations of top-k chunk-wise retrieval.

### Weaknesses
1. Compared to Llama3.1, ChatQA 2 shows improved performance on InfiniteBench, which includes real-world long-context understanding tasks beyond a 100K context window. However, on long-context benchmarks within 32K tokens, ChatQA 2 does not outperform Llama3.1, possibly due to its instruction tuning being focused on long SFT dataset. The author should also pay attention to the performance of 32K tokens.

2. The long-context open-source model ChatQA 2 presented in this paper achieves strong performance, though it lacks some innovation. The synthetic dataset used in the long SFT dataset could be described in more detail.

### Questions
1. Will the collected long SFT dataset utilized in the three-stage instruction tuning be open source?

2. Will the ChatQA 2 model be open source?

### Soundness
2

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
This work develops ChatQA 2, a long context LLM based on llama3-8k model that matches the performance of the April version of OpenAI GPT4 models and outperform SOTA open-source models. This work introduces a two-stage adaptation pipeline including long context continued training and multi-stage instruction finetuning. The developed model is then evaluated on short-context RAG, medium context up to 32k and long context above 100k benchmarks to show the superior performances than the existing open-source models.

### Strengths
- The developed ChatQA2 model shows promising performances than existing open-source baselines and the April version of OpenAI GPT model. 

- The evaluation from short to long contexts are comprehensive and convincing.

- This work presents a detailed data and training recipe that enables a good-performing long-context model, bridging the gap between the commercial sector and open-source community for long context modeling.

### Weaknesses
- The authors should clearly articulate the relationship of this work and ChatQA 1.5, right now it was described as both a baseline (as shown in Table 4) and confusingly as "the first version of this work", i.e. the same work. If ChatQA1.5 is indeed a baseline, then it should be listed in all the tables and result analysis.

- Some details of the computational experiment are missing in section 3: how many epochs and tokens were trained in each stage? How much does this impact the results? For example, there is a discussion to the potential reason of low longbench scores due to under-training. The authors should present the trend of higher scores with more training epochs (in supplementary information).  Please also provide the data, and training for reproducibility purposes.

- The authors should improve the comprehensiveness of their ablation studies and results analysis: (1) The authors should also evaluate the retrieval-based tasks in infinitebench to further confirm the NIAH superior performances as shown at the beginning. (2) The section 5.2 is a bit lacking: the RAG numbers seem not being discussed. (3) The authors should add an ablation study to support their claim that started at line #177, i.e. using an alternative document breaker helps the training.

- Minor comments: (1) the authors should add citations of scrolls and longbench when they are mentioned in line # 252 and line # 253. (2) There seems to be a typo in line #261: "as it is vasincluded" seems a bit confusing. (3) The authors should keep the bold texts consistent in all tables, right now some Llama-3.1-128k models are made bold but some are not. For example, I am not sure why 48.15 is made bold in Table 3, but not 49.92 (for 3.1-70b-instruct).

### Questions
1. At several places, e.g. line 144, 168, 222, in this manuscript, the authors mentioned "the first version of this work.", what does that mean? Please clarify.

2. What are the key new insights that this work offer, considering that the Llama3.1-128k model was published late July? I am not complaining about anything, but mainly want to make sure the technical contributions of this work. I will appreciate the answer from the authors.

3. Around line #188, the authors mentioned "where the model is initially trained on 128k high-quality instruction following datasets", while also mentioning " these two stages involve relatively short contexts", what does that mean, why 128k high-quality datasets are short contexts? Is there a typo?

4. In the long sequence SFT data, the authors used NarrativeQA for synthetic data generation. Are there potential data contamination in the benchmarks?


5. Minor questions: line # 263: why are the documents segmented into 300-word chunks? Does the size matter for the benchmark results?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a recipe to extend Llama-3.0 models to long context windows (128K). The recipe involves increasing the RoPE frequency, continual pretraining on longer length corpus, then supervised fine-tuning on a mix of short and long context length instructions. They benchmark the model on tasks (synthetic and real-world) with various context lengths and found consistent gains over the original Llama-3 models, with the 70B model exceeding the performance of GPT-4-Turbo on some tasks. Ablation studies demonstrate tradeoffs involved with extending LLMs to handle long-context inputs.

### Strengths
## Originality
The technique of extending the context lengths of LLMs is not new. The most originality lies in the creation of the synthetic, long-context instruction dataset highlighted in Section 3.2. The authors seem to suggest that utilizing long-context retrievers for RAG is a contribution in Section 3.3.

## Quality
The paper is well written. Experiments cover a wide range of tasks and reflect actual usage of long-context LLMs in real life. Baselines covered are extensive. Nothing to pick here.

## Clarity
The recipe is simple and presented clearly in the paper. Particularly, technical details are well-documented in the Method Section (Sec 3).

## Significance
The topic of extending LLMs to support longer context than it was original pretrained is of itself significant, which in turn makes potential solutions significant.

### Weaknesses
## Discussion on the key factors influencing performance tradeoff amongst tasks with different context lengths in long-context models

A major part of the paper is dedicated to compare the performance of long-context models on various (shorter) context lengths, specifically 4K, 32K, and 100K+. As the authors stated in P8L429 "This suggests that extending short-context models to long-context has trade-offs.", it is important to pinpoint what exactly controls the trade-off. The authors claimed in P7L372 that "This difference (in 32K performance) can be attributed to the extensive 32K pretraining and large SFT data implemented by Qwen2-72B-Instruct and Llama3.1-70B-Instruct.", which seems to hint at the data distribution being mainly responsible for the tradeoff. However, to the extent of my knowledge, Llama3.1 didn't released their training recipe nor data distribution. Can the tradeoff be fully attributed to the context-length distribution in the continual pretraining and SFT dataset? More discussion would greatly benefit the work.

## Relevance of stage-wise instruction-tuning

The authors highlighted in P2L98 and P4L187 that the instruction-tuning is split into 3 stages: instruction-following on short context, QA on short context, then a mix of long context instruction-following and synthetic QA. Stated in P4L199 "Both the full long SFT dataset and the short SFT dataset from the first two stages are then blended for training." What is the relevance of breaking down the instruction-tuning into stages when the final stage includes all data from the first two stages? An ablation study on training the model all-at-once with all the available data would help justify the multi-stage approach. Perhaps there are benefits in gradually increasing the context-length when instruction-finetuning and is actually key to the success of this recipe.

## Evaluating tradeoffs with other LLM capabilities with standard, general benchmarks

Section 5.2 highlights the difference in performance of the proposed model on QA and summarization. Quote "We find that our model performs extremely well at QA tasks while performs relatively low for summarization. This can be attributed to the lack of summarization data in our SFT recipe." Indeed the SFT data is heavy on QA and thus accounting for the performance bias. It is concerning that the good performance on this model on the benchmarked tasks might merely be a tradeoff with other LLM capabilities (e.g. reasoning, ICL, commonsense, creative writing, coding). Providing results on more general benchmarks (e.g. MT-Bench, MMLU, HumanEval) would help users evaluate the entire spectrum of tradeoffs of the proposed recipe.

### Questions
See weakness section for questions.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents Llama3-ChatQA-2, a model based on LLama-3-base that is trained with an extended context window. The authors first collect a long SFT dataset for instruction-tuning and train the model with modified PE. On top of this, they integrate a long-context retriever to implement RAG. Extensive testing are conducted across a variety of tasks involving short, long, and ultra-long token lengths, achieving state-of-the-art (SOTA) results.

### Strengths
1. The paper provides open access to the trained model and training recipe, which facilitates further research in the field of LLM + RAG.
2. The paper focuses on increasing the context length of LLMs and has conducted extensive testing across benchmarks of varying lengths. It compares the performance with both open-source and proprietary models, achieving promising results.

### Weaknesses
Some sections of the paper are too brief, presuming the reader’s familiarity with certain concepts, particularly those related to RAG. For example, the meaning of “chunk size” and a simple introduction to the inputs and outputs of the E5-mistral retriever are not sufficiently explained. Since the paper emphasizes *open-source training data and reproduction recipe* compared to the open-access (Open Weights) Llama3.1-70B-Instruct, it would benefit from providing more detailed explanations, like [1].

> [1] The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*.

### Questions
1. Under what circumstances does RAG improve LLM performance? For instance, why does RAG cause a performance drop for Llama3-ChatQA-2 on En.MC in Table 2, while improving the performance of Llama3.1-Instruct? The SOTA results in Tables 2 and 3 were achieved without RAG. Does this suggest that the effectiveness of RAG depends on the specific benchmark rather than the context length?
2. Could you test the results with retrievers other than E5-mistral?

### Soundness
4

### Presentation
1

### Contribution
4
