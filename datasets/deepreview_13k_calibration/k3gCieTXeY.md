# INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge

- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 5, 8, 8

## Abstract
The performance differential of large language models (LLM) between languages hinders their effective deployment in many regions, inhibiting the potential economic and societal value of generative AI tools in many communities. However, the development of functional LLMs in many languages (\ie, multilingual LLMs) is bottlenecked by the lack of high-quality evaluation resources in languages other than English. Moreover, current practices in multilingual benchmark construction often translate English resources, ignoring the regional and cultural knowledge of the environments in which multilingual systems would be used.
In this work, we construct an evaluation suite of 197,243 QA pairs from local exam sources to measure the capabilities of multilingual LLMs in a variety of regional contexts. 
Our novel resource, \ourdata, is a comprehensive knowledge- and reasoning-centric benchmark across 44 written languages that evaluates multilingual LLMs for performance in the actual language environments where they would be deployed. 
We release \ourdata for public use.\footnote{\url{https://huggingface.co/datasets/CohereForAI/include-base-44}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper collects multiple-choice questions in a wide range of languages other than English and evaluates a selection of multilingual LLMs. For further analysis, the questions are categorized as cultural or region-specific (subdivided further into region-implicit and region-explicit). The evaluation shows that there is room for improvement in LLM performance and that the performance varies across different languages.

====
The score is increased after the rebuttal.

### Strengths
* The paper presents a new benchmark called Include, which collects multiple-choice questions sourced from existing exams in a variety of languages and domains. The selection of exams is conducted through a community survey, which appears to be an appropriate method for reaching out to native speakers and obtaining links from them. Two down-sampled versions of Include are available, which offer an equal amount of tasks in different languages and domains.

* The paper evaluates the performance of 15 multilingual LLMs in five-shot and zero chain-of-thought fashion. 

* The paper analyses the results with respect to language, script, domain, and question category (cultural, region-implicit, region-explicit, academic) and formulates clear take-away messages.

### Weaknesses
 * Only two LLMs are evaluated using both 5-shot and 0-shot CoT methods. It's unclear why the 0-shot CoT evaluation is missing for most models.

* Although the paper focuses on evaluating multilingual models, which seems to be a practical scenario, an ablation study with monolingual LLMs in a subset of languages could establish an upper bound for performance. It is crucial to understand if the observed performance is due to the multilingual nature of the models or if monolingual models could achieve similar or better results on their respective languages.

* The paper does not provide the actual names of the collected exams, along with their publication dates and formats. This information could be important for considering potential leakage to the LLM's pre-training data. The lack of transparency regarding the source of the questions makes it difficult to assess the novelty and potential biases of the benchmark.

### Questions
* Why are only two LLMs evaluated using both 5-shot and 0-shot CoT methods? 

* Have you try prompting the LLM in English and the target non-English question in 5-shot evaluation? Does the prompt language affect the performance?

* What is the chance that the LLMs have already been trained on some of the Include questions?

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
They construct a benchmark including 197,243 QA pairs in 44 languages. They collect it from local exam sources to measure the capabilities of multilingual LLMs in a variety of regional contexts. Experimental results show that these models perform inconsistently across different languages, particularly struggling with region-specific questions.

### Strengths
- The dataset is extensive, covering a broad range of domains and covering various application scenarios.

- The writing is generally clear.

### Weaknesses
 - Experimental analysis is not quite enough and needs more takeaways.

Many of the experimental conclusions mentioned are known or intuitive. For example: In line 323 "Most instruction-tuned models perform slightly worse or on par with their base counterpart" which has been discovered in previous work[1][2] on English training corpus. Also for conclusions like LLMs' performance is poor on unseen language during pretraining.

Although a lot of effort has been put into building this benchmark, I feel that there is still a lack of takeaway, especially considering that one of the purposes of the Evaluation model is to improve the model. It's better to provide more find-gained analysis and insight like Figure 4 and also the insightful display (on the Main page rather than the Appendix) for conclusions like line142 model performs
worst on cultural questions.

- Doubts about the reliability of experimental findings

As you mentioned, some questions are "Cultural" and some are "Implicitly Regional". I am curious about the instructions for evaluating these two types of questions. Have you given the country or culture context of the questions being asked like: answer the question under  XXX culture? 

- The Question Format is simply MCQ

Understanding that MCQ is more accessible and easier to deal with, however, open-ended questions can reflect the models' performance on real application scenarios.

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work identifies a lack of high-quality multilingual data available to evaluate LLMs. Existing resources are often translated from English and focus on a specific regions or domains. To address this gap, the authors introduce a large multi-lingual evaluation benchmark from close to 2000 regional exams across 44 languages, including high-, mid and low-resource languages. A range of 15 models is then evaluated on the new benchmark. The results indicate that performance largely varies across models and languages and there is still room for improvement even among the best performing models.

[see below for my response to the author comments.]

### Strengths
* The paper introduces a large and high-quality evaluation dataset that addresses previous short-comings of existing LLM benchmarks. 
* Specifically, it identifies the fact that most existing multi-lingual resources are translated and therefore do not adequately reflect regional and cultural aspects that become relevant when models are actually deployed in respective environments.
* The paper’s structure is clear, the English is good and it is easy to follow
* The main contribution is an LLM benchmark, and as such it is not conceptually novel. However, it addresses a relevant short-coming and the introduction of „regional knowledge“ makes it original.
* Results are discussed in detail and Section 5 and the Appendix

### Weaknesses
 * The paper argues that existing LLM benchmarks do not adequately cover multi-linguality nor regional knowledge and it lists related benchmarks in the introduction and related work. However, this argument is only on a qualitative level and would benefit from quantitative facts about, the size, number of languages, etc. of individual existing benchmarks. This could be included in a table providing an overview. 

* The paper is long on numbers, but short on more qualitative insights. For example, if a model fails to answer an exam question, is this due to a linguistic failure (the model fails to understand the question) or does it lack the regional/cultural knowledge? What types of errors do the models make? Insights of this kind would be crucial to make the results of the paper actionable for future model development, and while difficult to carry out automatically at scale, could be conducted manually on a sample for illustrative purposes. 

* The evaluation also does not contain any hard evidence that the knowledge contained in the proposed benchmark cannot be tested by existing ones. It would be interesting to see correlations between performances on different benchmarks. This would be straightforward to do at least for the subsets of external benchmarks that are already included under „Rounding up the Benchmark“ in Section 3.1.

### Questions
* On the technical side, it is not clear to me how exactly the model’s answer to a question is extracted from its output. In the first paragraph of Section 5.4 (lines 440-448), the authors mention that the adopt the prompt template by Hendrycks et al. and mention that the model does follow it consistently. What does the expected output look like and how exactly is the answer retrieved in case the model does not follow it? An example would be beneficial.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a new resource to evaluate the multilingualism of LLMs. The dataset, called Include, comprises multiple-choice questions from 44 languages about regional and global knowledge. The authors evaluate a battery of LLMs ranging from closed-source models (GPT-4o) to a variety of open-source models (C4AI-Aya, Mistral, Gemma, Qwen, Llama, XGLM, and Bloom). The paper presents a thorough analysis, comparing the performance of the models in different languages, domains, and regional/global knowledge. Finally, the authors discuss the challenges of evaluating these models in a setting with several languages.

### Strengths
* The paper is well-written and is easy to follow.
* The resource presented in this paper addresses a very prevalent challenge: the disparity in resources involved in the development of LLMs for English and non-English languages. Moreover, not only allows for the assessment of the quality of LLMs in the given languages but also in their regional cultural knowledge, which is most of the time ignored by the large body of research.

### Weaknesses
I did not find any major weaknesses in this paper. However, here are some possible improvements for this work:
* **Asses the difference in performance when the model is asked in English**: Etxaniz et al. (2024a) showed that these LLMs perform better in English although they understand the target language. They propose the " Self-translate " method, which prompts the same model to first translate the example into English before answering the question. Although I do not think you need to necessarily apply the "Self-translate" method, it would be nice to translate the examples into English (using machine translation) and compare the difference in performance. This way you can assess the knowledge encoded in the LLMs separately from their language capabilities.

### Questions
I have a couple of comments and questions about your work:
* **I missed some key references**: There are a couple of papers that are very aligned with this work, for instance, in the line of generating evaluation resources for LLMs in low-resource settings (particularly Basque):
  * (Etxaniz et al., 2024b): They present (along with pre-training data and models) an evaluation suite for Basque based on C1-level certificate of proficiency exams, reading comprehension exercises, trivia questions, and  Public Service examinations.
  * (Etxaniz et al., 2024c): They analyze the effect of regional vs non-regional knowledge of the LLM using an evaluation dataset that is parallel in English and Basque.
* **Have you tried any variants of Claude?** As for my experience, Claude performs better than GPT-4o in a couple of languages other than English that I tested. I am not asking to repeat the experiments with Claude, but I just have the curiosity of whether my personal feeling is reflected in your data.
* **Remove Answer Acc. from Table 1:** This metric is not comparable among the models in the table (as far as I understand). This can lead to confusion where worse models perform better just because they generate more wrongly formatted answers. If not removed, I would at least remove the bold results to avoid comparisons.


### References:
 * [Do Multilingual Language Models Think Better in English?](https://aclanthology.org/2024.naacl-short.46/) (Etxaniz et al., 2024a)
 * [Latxa: An Open Language Model and Evaluation Suite for Basque](https://aclanthology.org/2024.acl-long.799/) (Etxaniz et al., 2024b)
 * [BERTAQA: How Much Do Language Models Know About Local Culture?](https://arxiv.org/pdf/2406.07302) (Etxaniz et al., 2024c)

### Soundness
4

### Presentation
4

### Contribution
4
