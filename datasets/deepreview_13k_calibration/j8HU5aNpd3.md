# Retrieval or Global Context Understanding? On Many-Shot In-Context Learning for Long-Context Evaluation

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
Language models (LMs) have demonstrated an improved capacity to handle long-context information, yet existing long-context benchmarks primarily measure LMs' retrieval abilities with extended inputs, e.g., pinpointing a short phrase from long-form text. 
Therefore, they may fall short when evaluating models' global context understanding capacity, such as synthesizing and reasoning over content across input to generate the response. 
In this paper, we study \textit{long-context language model (LCLM) evaluation} through \textit{many-shot in-context learning (ICL)}. Concretely, we identify the skills each ICL task requires, and examine models' long-context capabilities on them. 
We ask the first question: 
\textit{What types of ICL tasks benefit from additional demonstrations, and are these tasks effective at evaluating LCLMs?} 
We find that classification and summarization tasks show notable performance improvements with additional demonstrations, while translation and reasoning tasks do not exhibit clear trends. 
This suggests the classification tasks predominantly test models' retrieval skills. 
Next, we ask: \textit{To what extent does each task require retrieval skills versus global context understanding from LCLMs?} 
We develop metrics to categorize ICL tasks into two groups: (i) \textbf{retrieval} tasks that require strong retrieval ability to pinpoint relevant examples, and (ii) \textbf{global context understanding} tasks that necessitate a deeper comprehension of the full input. 
We find that not all datasets can effectively evaluate these long-context capabilities. 
To address this gap, we introduce a new many-shot ICL benchmark, \textbf{\data}, designed to characterize LCLMs' retrieval and global context understanding capabilities separately. 
We benchmark 11 open-weight LCLMs using \data. We find that while state-of-the-art models demonstrate satisfactory performance up to 64k tokens in retrieval tasks, many models experience significant performance drops at only 16k tokens in global context understanding tasks

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to investigate the long context understanding capability of long context language models (LCLMs) via many-shot in-context learning (ICL). Specifically, the work proposes *(1)* a retrieval load ratio metric to identify tasks that requires retrieval of similar ICL examples to perform effectively, and *(2)* a global context index to identify tasks that need true global context understanding capability to perform well. Lastly, the author compiled ManyICLBench, a benchmark to assess LCLMs' retrieval skills and global context understanding skills separately.

### Strengths
- In general, the paper is well written. The discussion of related works is comprehensive and thorough.
- The paper is well motivated and targets the important gap of the lack of evaluation for LCLMs' true context understanding ability.
- This work presents an extensive set of experiments, offering great empirical insights for the community.

### Weaknesses
 - It is unclear as to how Section ```4```. fits into the paper. How exactly does identifying the tasks that perform better/worse with more shots contribute to evaluating the global understanding capability of LCLMs?

- A number of prior works [1][2][3] have studied many-shot ICL in LCLMs. This work tries to provide a more comprehensive evaluation by adding tasks besides classification, however, the experiments do not include any closed-source API models.

- In the retrieval load experiments, removing the 10% similar ICL example would likely results in an absence of certain labels or an imbalanced ICL set with respect to the test input -- making the performance drop inevitable and might not be attributable to the reliance of retrieval skills. This also explains the results on non-classification tasks as they typically have a much larger output label space.

- To the best of my understanding, it seems that the retrieval skill discussed in the paper refers to the model's skill of inferring from similar input-output demonstrations to answer the test input -- which is not entirely the same as Needle-in-A-Haystack-style tasks that are explicitly about finding and retrieving phrases in the context. The retrieval skills in ICL might also involve a certain degree of understanding, instead of retrieval alone. Thus, the results might not be able to disentangle retrieval skills and global context understanding skills.

### Questions
- Why is BM25 retriever adopted? Have you experiment with embedding-based approach that might captures the semantics better?
- Line ```259```: llama-3.1-7B --> 8B.
- This is a rather minor point -- but it might be better to move Figure ```6``` & ```7``` to the main context as they are referred in the main discussion.

### Soundness
3

### Presentation
2

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
The paper introduces Many-ICLBench, a new many-shot ICL benchmark. The analysis first dives into the trends of models across different lengths and categories of ICL tasks. Then, novel metrics, Retrieval Load Ratio and Global Context Index, are used to divide tasks into two categories. Finally, many existing open-source models are evaluated on the benchmark, revealing interesting insights.

### Strengths
- The paper builds upon previous works on many-shot in-context learning by extending the analysis to more types of tasks, such as summarization, translation, and reasoning tasks. These tasks provide a more holistic and realistic evaluation of long-context language models for ICL.
- The paper reveals interesting findings; in particular, the categorization of ICL tasks into retrieval vs. global context understanding can help practitioners in choosing which datasets to use during evaluation. 
- Many-ICLBench may be a useful artifact to the community to test long-context language models.

### Weaknesses
 - InfiniteBench also includes a diverse set of long-context language modeling tasks, such as QA, summarization, and ICL. There is no strong argument that Many-ICLBench is the first to “create a realistic long-context benchmark emphasizing retrieval and global context understanding skills.” What makes Many-ICLBench more appealing for users to test on over InfiniteBench?
- The findings can benefit from the inclusion of more SoTA long-context language models in the analysis, such as GPT-4/4o, Claude, and Gemini. For instance, one of the findings on the translation task is that the tested models do not benefit from the increasing number of demonstrations. However, Gemini was able to see improvements on a similar task. It would be useful to provide empirical evidence to show that the lack of improvement stems from the lack of multilingual capabilities of the model/model size.
- BM25 does not seem sufficient as a measure between two examples, as it only measures the lexical overlap between them. Using metrics such as BERTScore or the score from a dense retriever that can capture semantic similarity would make the “Retrieval Load Ratio” more convincing. Furthermore, math problems or other reasoning tasks seem unlikely to have lexical overlap even if they are using similar reasoning steps, whereas classification tasks are more likely to. The work could use more validation on this measure.
- In Appendix C, it’s shown that the quantized and unquantized versions exhibit similar trends, but the absolute number appears to differ significantly on certain tasks at long lengths: Llama 3.1 70B at 64k differs up to 6 points on Symbolic. The difference in the absolute value may affect the finding “the paradox of model size” in Sec 6 since the larger models are quantized and may have a lower absolute performance while the smaller models are not quantized.

Missing citations on the role of ICL:
* Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi, and Luke Zettlemoyer. 2022. Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 11048–11064, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.
* Jane Pan, Tianyu Gao, Howard Chen, and Danqi Chen. 2023. What In-Context Learning “Learns” In-Context: Disentangling Task Recognition and Task Learning. In Findings of the Association for Computational Linguistics: ACL 2023, pages 8298–8319, Toronto, Canada. Association for Computational Linguistics.

### Questions
- How is the average Pearson correlation coefficient calculated for Figure 1b? 
- It seems from Figure 1a that Llama 3.1 70B Instruct is able to perform well on all tasks at 64k context length before dropping at the 128k input length. How would the Global Context Index change if the inputs were expanded to include 32k and 64k input lengths? Furthermore, do different models exhibit similar or different Global Context Index?

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
This paper aims at exploring whether LLMs rely more on retrieval or global context understanding to perform tasks like text classification, summarization, reasoning, and translation in many-shot ICL with long-context settings. Using BM25 to measure similarity between demonstrations, the authors assume that a performance drop from removing similar examples indicates high reliance on retrieval. Author(s) suggest that classification and summarization tasks need retrieval ability, while reasoning tasks need global context understanding, though the latter concept is not clearly defined in the paper. Extensive experiments were conducted across a collection of 11 tasks.

### Strengths
1. a comprehensive analysis on many-shot ICL across a wide range of tasks and long-context LLMs.

2. The problem studied in this paper is interesting, hard to investigate, and may provide insights into a deeper understanding of LLMs.

### Weaknesses
1. The paper centers on the distinction between retrieval ability and global context understanding. Yet, it lacks formal definition of these two concepts, and provides limitted discussion on their meanings and implications for LLMs or downstream tasks. I think there is significant overlap between these two concepts.


2. Regarding RQ2 ("What skill does each task primarily measure?"), author(s) state that "a more pronounced drop in performance upon removing similar examples, which indicates the task’s heavy reliance on retrieval capabilities." This statement requires supporting evidence and rationale, as almost all NLP tasks require global context understanding. It may be insufficient to draw this conclusion simply based on similarity between demonstrations and performance drop.


3. The similarity between demonstrations, estimated using BM25, is based on lexical overlap, which is a limited metric. Lexical similarity does not necessarily capture true semantic similarity, nor does it reliably indicate a preference for retrieval or global context understanding.


4. Prior works have demonstrated that lexical overlap as a similarity measure may lead to spurious correlations. This raises questions about the generalizability of the results.


5. Statements such as "classification tasks benefit from more demonstrations" or "classification tasks predominantly test models’ retrieval skills" lack roust supporting evidence. It is not clear why more demonstrations means better retrieval skill. It may be possible that more similar demonstrations can better illustrate the decision boundary.


6. Previous works have shown demonstration order can impact the performance, but this aspect has not been discussed in this work.

### Questions
1. When measuring the similarity of demonstrations for (x, y), do you only consider x or both x and y?

### Soundness
2

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
3

### Summary
This paper explores the capabilities of long-context language models (LCLMs) in handling long-text information, particularly their abilities in global context understanding versus retrieval capabilities. The paper assesses LCLMs through many-shot In-Context Learning (ICL) and introduces a new benchmark, MANYICLBENCH, to separately measure the retrieval skills and global context understanding capabilities of LCLMs.

The key findings and contributions are:
1. Classification and summarization tasks show significant performance improvements with additional demonstrations, while translation and reasoning tasks do not exhibit clear trends.
2. Tasks are categorized into retrieval tasks and global context understanding tasks by analyzing performance changes when removing different examples.
3. A new benchmark, MANYICLBENCH, is introduced to evaluate the retrieval and global context understanding capabilities of LCLMs.

### Strengths
1. Originality: This paper pioneers a new evaluation paradigm for LCLMs by differentiating between retrieval and global context understanding skills and also .introduce a new benchmark MANYICLBENCH providing new tools for evaluating long-text models.
2. Quality: The study offers a rigorous experimental design and insightful data analysis, though it could benefit from broader model diversity.
3. Significance: It provides valuable contributions to LCLM evaluation and practical applications, suggesting promising directions for future research.

### Weaknesses
1. Task Coverage: While the paper covers a variety of task types, there may still be other types of tasks not fully considered, such as dialogue systems or multi-document summarization. The current selection of tasks, while diverse, primarily focuses on single-turn question-answering or text generation scenarios. This leaves a gap in understanding how LCLMs perform in more complex, interactive, or multi-faceted tasks that require maintaining context over multiple turns or integrating information from several sources, which are crucial for real-world applications.
2. Lack of practicality: At present, exploratory research on LCLMs may change with the iteration of model versions. Some conclusions of the article have certain reference significance for future progress, but not much practical significance. The rapid pace of development in LCLMs means that specific findings related to particular model architectures or training methods may quickly become outdated. The paper's focus on specific model versions and context lengths might limit the generalizability of its conclusions, making it difficult to apply the findings to future models or different settings. The lack of a clear connection to real-world applications also reduces the immediate practical value of the research.

### Questions
1. Does the paper discuss specific challenges encountered in long-text processing, such as information forgetting or context confusion?
2. Do models show a performance decline when processing extremely long texts, and is this related to the model's capacity or training methods?

### Soundness
2

### Presentation
3

### Contribution
2
