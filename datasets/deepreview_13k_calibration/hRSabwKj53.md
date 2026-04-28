# One Language, Many Gaps: Evaluating Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
Language is not monolithic. While many benchmarks are used as proxies to systematically estimate Large Language Models' (LLM)  performance in real-life tasks, they tend to ignore the nuances of within-language variation and thus fail to model the experience of speakers of minority dialects. Focusing on African American Vernacular English (AAVE), we present the first study on LLMs' fairness and robustness to a dialect in canonical reasoning tasks (algorithm, math, logic, and comprehensive reasoning). We hire AAVE speakers, including experts with computer science backgrounds, to rewrite seven popular benchmarks, such as HumanEval and GSM8K. The result of this effort is \textbf{ReDial}, a dialectal benchmark comprising $1.2K+$ parallel query pairs in Standardized English and AAVE. We use ReDial to evaluate state-of-the-art LLMs, including GPT-4o/4/3.5-turbo, LLaMA-3.1/3, Mistral, and Phi-3. We find that, compared to Standardized English, \textbf{almost all of these widely used models show significant brittleness and unfairness to queries in AAVE}. 
Furthermore, AAVE queries can degrade performance more substantially than misspelled texts in Standardized English, even when LLMs are more familiar with the AAVE queries. Finally, asking models to rephrase questions in Standardized English does not close the performance gap but generally introduces higher costs. Overall, our findings indicate that LLMs provide unfair service to dialect users in complex reasoning tasks.git}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
I had wrongly submitted a review for another paper - I have now corrected this - I apologise! 

This paper explores how robust language models are to language variation and dialects. They create a test set with 1.2k query pairs in Standard English and African American Vernacular English (AAVE). They show that a variety of standard large language models perform worse on AAVE than on standard English, and on misspelled English. Prompting the LLM to rephrase quieries in Standard English improves performance but does not close the gap in performance. This is a nice contribution to the field and the dataset could be of general interest.

### Strengths
Nice dataset for measuring LLMs robustness to dialects Study showing brittleness of models to AAVE

### Weaknesses
Lack of discussion about the appropriateness of AAVE in different communications scenarios/tasks I would have expected some more experiments investigating different robustness techniques for LLMs to mitigate the problem with dialects

### Questions
Have the authors considered that people switch registers depending on pragmatics, and that a AAVE speaker when interacting via text with an LLM might naturally switch to something closer to Standard English by default?

Also some of the datasets used do not neatly fit into the type of problems that would require a lot of variation in vernacular eg. maths problems would be quite similar no matter what vernacular used and using a very different query for a maths problem in AAVE might be artificial and forced. The examples in Figure 1 do seem to be forced (especially the first three) and I think an AAVE speaker would feel like they are forcing a more significant difference than would be natural. I realise you have a naturalness check in the annotation pipeline, but this could just be that people thought it would plausibly be AAVE not that it should be AAVE - if annotators are given instruction to rewrite in AAVE they might do so even it is not very authentic. Some discussion of AAVE being different under different communication scenarios and tasks would be welcomed.

It was not clear if the answers were also rewritten in AAVE or just the queries as the description says it is just the queries, but the answers in AAVE would also be useful, measuring generation capability as well as understanding and reasoning.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a novel study on the fairness and robustness of LLMs when dealing with dialects, specifically African American Vernacular English (AAVE). The authors have created a benchmark dataset, ReDial, comprising over 1.2K parallel query pairs in Standardized English and AAVE to evaluate LLMs on reasoning tasks. The study finds that most LLMs show significant performance degradation on AAVE queries compared to Standardized English, indicating a lack of fairness and robustness.

### Strengths
The paper addresses a critical and underexplored issue in the field of natural language processing, namely the fairness and robustness of LLMs to dialectal variations within a language.

The creation of ReDial, a high-quality, human-annotated dataset for evaluating LLMs on reasoning tasks in AAVE, is a significant contribution to the research community.

The paper is well-organized, and the arguments are presented clearly, making it easy to follow the authors' reasoning and conclusions.

### Weaknesses
The paper attempts to explore potential reasons behind the observed performance degradation with AAVE, but it merely dismisses data skewness without offering alternative explanations.

In lines 343-372, 4 observations emerge from the experiments. 
(1) All models exhibit fragility when handling AAVE. 
(2) All reasoning tasks demonstrate vulnerability to AAVE. 
(3) Increasing model size does not enhance robustness against AAVE. 
(4) Highly curated datasets are particularly susceptible to AAVE. 
Observations (1) to (3) are acceptable. However, observation (4) contradicts the findings in Table 2, where LLaMA-3-8B-Instruct shows the least performance decline. In comparison, Mistral and GPT exhibit greater drops than LLaMA-3-8B-Instruct, making observation (4) questionable.

Is data skewness truly irrelevant to AAVE fragility? The experiment lacks persuasiveness. As illustrated in lines 415-419, the experiment simulates typographical errors by altering characters in Standardized ReDial and compares its performance to AAVE. Introducing typographical errors in Standardized ReDial increases perplexity. However, higher perplexity signifies greater uncertainty in token prediction. It does not accurately measure language familiarity, as illogical sentence structures can also result in high perplexity. Thus, it is inappropriate to compare this with AAVE.

### Questions
What are the theoretical underpinnings of the performance gap between Standardized English and AAVE in LLMs?

How do the findings generalize to other dialects or non-English languages?

Can the authors propose any solutions or strategies to mitigate the performance gap and improve fairness for dialect speakers?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
African American Vernacular English (AAVE) is a dialect less frequently seen in the training dataset. 
This paper proposed to assess the bias and robustness of LLMs thru a proposed benchmark, namely ReDial.
With native AAVE speakers' validation, ReDial covers 4 category reasoning tasks, including algo, math, logic, and comprehension.
The benchmark is then tested against GPT, LLaMA, Mistral, and Phi-3 models.
AAVE queries showed a suboptimal performance compared to standard English queries in various aspects.

### Strengths
- The paper is nicely organized and easy to follow. 
- Code is publicly available.
- The construction of the benchmark Redial is well presented, including the source benchmark of sampling and native speaker validation.
  - To ensure the quality of algo translation, annotators have a CS background.
  - The validation process employed an iterative approach for better quality and limited the usage of LLMs during the process
- Experiment covered a wide of range of popular models and investigate two prompting methods (zero-shot & zero-shot CoT)
- Appendix is informative

### Weaknesses
 - Using dialects to reduce bias and improve robustness of LLMs sounds like an exciting direction. ReDial (Reasoing with Dialect Queries) currently contains one dialect, AAVE, which may appear to be limited. Expanding the scope to include a diverse of dialects may more comprehensively capture the insight of dialects in general when assessing LLMs bias and robustness. 

- AAVE is widely spoken and has a large amount of data sources. What about other dialects sharing similar characteristics?

- Non-standard English dialect is semantically equivalent to the original English questions, offering similar insights to previous study on the impact of multilingual and tone on LLMs performance. 

- Table 3 showed the detailed comparison in performance among the four categories. However, it is not clear about which model is used. And other models' results were not included in the appendix. 

- The submission has one extra page. Refers to "There will be a strict upper limit of 9 pages for the main text of the submission, with unlimited additional pages for citations. "
- The claim that the daily use of LLMs is limited to zero shot, and zero shot chain-of-thought is unsound. (line 252)

- Perplexity is used as an indication of LLM's understanding of data. After injection of typos into standardized English ReDial, the perplexity of it exceeded the AAVE one. This may not reveal the fairness directly because the increased perplexity may reflect model's sensitivity to surface-level variations, in this case, typos, instead of a deeper understanding towards dialects. 

- Compared to increasing perplexity of standardized English ReDial, finetuning process could be adopted to improve the knowledge of a dialect and consequently reduce the perplexity of AAVE.

### Questions
- Have you attempted to fine-tune any models using the ReDial dataset? Given that fine-tuning could enhance the model’s understanding of the dataset, is it expected to improve the performance of LLMs?

- Have you tried to use few-shot prompt for in-context learning and thus potentially better performance? 

- Did you look into why GPT-4o & 3.5 turbo see a performance degradation with Chain-of-Thought prompting in original English questions? It may not align with prior research findings.

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
4

### Summary
This work proposed a new benchmark: ReDial, the human-annotated benchmark dataset that evaluates the fairness and robustness of large language models (LLMs) when handling African American Vernacular English (AAVE) dialect. This benchmark contains questions including algorithmic, mathematical, logical, and comprehensive reasoning, and compares model performance on parallel Standardized English and AAVE prompts.

The study finds that most LLMs and most types of questions, show significant brittleness when dealing with AAVE, performing substantially worse than with Standardized English. Additionally, simply asking models to rephrase queries in Standardized English fails to close the performance gap, often increasing computational costs. The authors argue that this dialectal unfairness reflects deeper issues in how LLMs are trained and evaluated.

### Strengths
1. This work provides the first comprehensive evaluation of large language models (LLMs) on dialect fairness and robustness, specifically focusing on African American Vernacular English (AAVE), which is a contribution to NLP fairness and LLM literature.

2. This paper introduces the ReDial dataset, a benchmark in AAVE and Standardized English, which covers different domains such as algorithm, logic, math, and comprehensive reasoning tasks. This new dataset is valuable for future research on dialect robustness in reasoning tasks.

3. The paper conducts extensive experiments on multiple current LLMs, such as GPT-4, LLaMA, and Mistral, showing their brittleness when handling AAVE, thereby providing strong empirical evidence of dialectal bias in complex reasoning tasks.

### Weaknesses
1. The poor performance of models on non-standard English, especially AAVE, is somewhat expected, given the dialectal imbalance in training data. While the paper provides empirical evidence, the findings don't go beyond what could be anticipated, limiting its novelty.

2. This paper points out the weakness of LLM when handling AAVE but doesn’t propose any effective solutions to mitigate these issues. However, it mentions that simple data augmentation isn’t enough. Providing alternative strategies such as new architectures or advanced data augmentation techniques would make this work more strong.

3. Since the main contribution of this paper is the creation of the ReDial dataset and its evaluation, a benchmark track rather than the main conference would be a suitable place.

4. Although the paper covers algorithms, logic, math, and comprehensive reasoning tasks. There are still standardized methods to evaluate fairness. I feel for fairness evaluation, those methods are worth trying.

5. The paper demonstrates the performance degradation on AAVE reasoning tasks, but it does not dive deeply into which specific linguistic features of AAVE (e.g., vocabulary, syntax) cause model confusion. This leaves a gap in the theoretical understanding of the problem. Providing more insight would be better.

### Questions
1. Could further experiments distinguish the impact of model architecture and training strategies on the performance drop? For example, LLaMA 3-8B shows a smaller performance drop on AAVE, while similar-sized models like Phi-3 Small experience a significant drop. Does this suggest that different model architectures handle language variations differently?

2. Model size doesn’t seem to be the sole factor—larger models don’t always mitigate the performance drop on AAVE. For example, Mistral and Phi-3 Small models still experience significant performance degradation. Does this imply that task-specific model optimization is more crucial?

3. GPT-4o’s errors in rephrasing may indicate a lack of fine-grained understanding of AAVE semantics and syntax. Does this suggest that the model’s knowledge is insufficient for AAVE, further explaining its weaker performance on AAVE tasks？

4. Could further fine-tuning or training with a dataset containing more dialectal data improve models’ performance on AAVE? Specifically, could models that struggle with rephrasing tasks benefit from additional exposure to dialects?

5. Is 1.2K parallel sentence pairs enough to cover the diversity of AAVE and represent the real-world usage of the AAVE community? Would a more diverse and larger dataset be necessary to further validate the model's performance?

### Soundness
2

### Presentation
3

### Contribution
2
