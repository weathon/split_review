# A Controlled Study on Long Context  Extension and Generalization in LLMs

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Broad textual understanding and in-context learning require language models that utilize full document contexts. Due to the implementation challenges associated with directly training long-context models, 
many methods have been proposed for extending models to handle long contexts. However, owing to differences in data and model classes, 
it has been challenging to compare these approaches, leading to uncertainty as to how to evaluate long-context performance and whether it differs from standard evaluation. We implement a controlled protocol for extension methods with a standardized evaluation, utilizing consistent base models and extension data. Our study yields several insights into long-context behavior. First, we reaffirm the critical role of perplexity as a general-purpose performance indicator even in longer-context tasks. Second, we find that current \textit{approximate} attention methods systematically underperform across long-context tasks. Finally, we confirm that exact fine-tuning based methods are generally effective within their extension range, whereas extrapolation remains challenging.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Using consistent base models and extension data, the study yielded several insights into long-context behavior. First, it reaffirmed the critical role of perplexity as a general-purpose performance indicator. Second, current approximate attention methods systematically underperform in long-context tasks. Finally, it confirmed that exact fine-tuning based methods are generally effective within their extension range, whereas extrapolation remains challenging.

### Strengths
1. This work is the first to conduct a fair and comprehensive comparison of different long context extension methods, resulting in several useful conclusions.

### Weaknesses
1. Based on my experience, increasing the model size in long-context downstream tasks such as LongBench yields some interesting conclusions that are inconsistent with the 7B model. I hope you can add some simple experimental results from the 13B model to discuss this point.

2. While enhancing the model's long-context capabilities, we also care about the impact of different methods on short-text performance and the extent of knowledge forgetting. I hope you can add some results from the common Open LLM Leaderboard to discuss this point.

### Questions
please see weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper evaluates several freeze/fine-tuning long-context methods on several public LLMs. Based on its experiments, it argues that (1) PPL is still an important metric in long-context scenarios, (2) "approximate attention" methods show poor performance (3) "exact fine-tuning based methods" are effective within trained range but cannot further process longer texts well.

### Strengths
1. The paper evaluates many methods under a controlled setting.
2. The paper proposes several might-be-useful conclusions based on their experiments.

### Weaknesses
1. More evaluation of short texts is required to check whether these methods perform well in keeping the original performance. (for example, NTK by parts may behave better on this than NTK-rope.)
2. The so-called "approximate attention" method includes many quite different methods and can be misleading. It isn't very clear to include the streaming-LLM methods / longlora / landmark into one class. And MinInference-style work shows promising performance now, the conclusion that 'approximate attention is poor' might be misleading.
3. self-extend seems to be more like NTK-F than 'approximate attention'.
4. The contribution of the work might be limited if the arguments were not sufficiently robust.

### Questions
As the (1)-(3) in weakness.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper systematically evaluates various methods for extending the context length of LLMs, aiming to provide insights into the behavior of long-context models and establish a standardized evaluation framework. It designs a controlled protocol for comparing context extension methods using consistent base models and extension data. The study includes an examination of the performance of different attention mechanisms in long-context tasks, confirms that perplexity remains a relevant performance indicator in longer-context scenarios, and presents findings indicating that exact fine-tuning methods are effective within their extension range, while approximation methods tend to underperform. Additionally, the paper emphasizes the open-sourcing of codebases, models, and checkpoints to promote transparency and facilitate further research.

### Strengths
- The paper introduces a novel controlled protocol for evaluating long-context extension methods, addressing a significant gap in the literature regarding the comparison of such techniques.
- The study is comprehensive, utilizing a variety of metrics and tasks to assess model performance. The use of standardized base models and extension data enhances the quality of the comparative analysis.

### Weaknesses
 - The study is limited to three base models, which may not accurately represent the performance of other, potentially larger models. Expanding the analysis to include a more diverse set of base models could strengthen the conclusions.
- While the paper acknowledges limitations due to fixed hyperparameters, a more in-depth exploration of how different hyperparameter settings might affect the results would be beneficial.
- The generalization of findings to longer contexts beyond 32k (e.g., 128k and 1m) is not addressed, which is a significant limitation given the focus on long-context models.
- The insights provided in this paper have been discussed in previous studies, and I did not gain any new takeaways from it.

### Questions
- What is the performance of new models, such as Qwen2.5, in this experiment?
- What are your thoughts on the generalization behavior of these methods for contexts longer than 32k? Are there any preliminary findings or conjectures regarding this?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a comprehensive empirical study on long-context extension methods for language models, including 4 methods that adapt the RoPE positional embedding, and 4 methods that approximates the attention operations. The paper ensures a fair comparison of these methods and conclude with three key takeaways: (1) contrary to claims in previous works, perplexity and downstream task performance has high correlations; (2) RoPE-adaptation methods in general work better than attention approximation methods; (3) Dynamic NTK works best among compared methods.

### Strengths
1. The topic of this paper is timely and important. While there is a lot of recent work on long-context extension, the experiments were conducted with different base models and different training data, hence there is a lack of fair comparison. This work aims to answer this important question.
2. The background section (section 3) is mostly well-written and provides a unified view of these various context extension methods.
3. The authors conducted extensive experiments and ensured the comparison is conducted in a fair manner.

### Weaknesses
1. I'm not fully convinced by some of the experiment results and takeaways. See questions below.
2. The paper mentions lack of "quantitative rankings of different methodologies" as a motivation of this work. While this paper finds NTK-Dynamic to work best in general, this paper does not provide a full ranking.
3. The presentation and organization of the paper can be improved in various aspects. e.g., using more visualizations instead of tables to summarize the results and highlight main findings; having a table to summary the key characteristics of the 8 compared methods.

* Figure 1. I am surprised by the LM-Infinite result as the authors of the LM-Infinite reported an pass rate of about 80\% on the task of Passkey Retrieval, which is very similar to the needle-in-the-haystack evaluation conducted in Figure 1. However, LM-Infinite fails most cases on NIAH as reported in Figure 1. Could you help explain what are potential aspects that lead to this gap?
* Line 484 "Perplexity and downstream tasks". I'm not fully convinced by this argument and Figure 4. It seems that the linear trend in Figure 4 is highly dependent on LongLora and Landmark, in a sense that the linear trend is likely to disappear without these two compared methods. 
  * It seems that when perplexity is below certain level, e.g., below 6, the perplexity differences between models are small but the downstream performance differences are large. Thus I'm concerned with the claim that perplexity is a "general-purpose performance indicator" as suggested in the abstract, it can only indicate well within a certain region from my understanding.
  * Could you please consider adding metrics such as rank correlation to further strengthen the claim?
* Line 505 "Context extension hurts in the short term and gains in the long term". I'm not quite sure what this title means here. What are "short term" and "long term" referring to here?
* Is there any inference speed trade-off between these compared methods? e.g., Are attention approximation methods faster? By how much? For some applications the inference speed may be critical. Providing such information will help users make informed decisions.

Others:
* Line 194: What is the CLEX method here? Currently there is little introduction of it.
* Line 221: "key matrix", are you referring to "key and query matrices"?

### Questions
* Figure 1. I am surprised by the LM-Infinite result as the authors of the LM-Infinite reported an pass rate of about 80\% on the task of Passkey Retrieval, which is very similar to the needle-in-the-haystack evaluation conducted in Figure 1. However, LM-Infinite fails most cases on NIAH as reported in Figure 1. Could you help explain what are potential aspects that lead to this gap?
* Line 484 "Perplexity and downstream tasks". I'm not fully convinced by this argument and Figure 4. It seems that the linear trend in Figure 4 is highly dependent on LongLora and Landmark, in a sense that the linear trend is likely to disappear without these two compared methods. 
  * It seems that when perplexity is below certain level, e.g., below 6, the perplexity differences between models are small but the downstream performance differences are large. Thus I'm concerned with the claim that perplexity is a "general-purpose performance indicator" as suggested in the abstract, it can only indicate well within a certain region from my understanding.
  * Could you please consider adding metrics such as rank correlation to further strengthen the claim?
* Line 505 "Context extension hurts in the short term and gains in the long term". I'm not quite sure what this title means here. What are "short term" and "long term" referring to here?
* Is there any inference speed trade-off between these compared methods? e.g., Are attention approximation methods faster? By how much? For some applications the inference speed may be critical. Providing such information will help users make informed decisions.

Others:
* Line 194: What is the CLEX method here? Currently there is little introduction of it.
* Line 221: "key matrix", are you referring to "key and query matrices"?

### Soundness
3

### Presentation
2

### Contribution
2
