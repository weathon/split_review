# Scaling Laws for Downstream Task Performance in Machine Translation

- Decision: Accept
- Avg Score: 6.60
- Scores: 3, 6, 8, 8, 8

## Abstract
Scaling laws provide important insights that can guide the design of large language models (LLMs). Existing work has primarily focused on studying scaling laws for pretraining (upstream) loss. However, in transfer learning settings, in which LLMs are pretrained on an unsupervised dataset and then finetuned on a downstream task, we often also care about the downstream performance. In this work, we study the scaling behavior in a transfer learning setting, where LLMs are finetuned for machine translation tasks. Specifically, we investigate how the choice of the \emph{pretraining} data and its size affect downstream performance (translation quality) as judged by: downstream cross-entropy and translation quality metrics such as BLEU and COMET scores. Our experiments indicate that the size of the finetuning dataset and the distribution alignment between the pretraining and downstream data significantly influence the scaling behavior. With sufficient alignment, both downstream cross-entropy and translation quality scores improve monotonically with more pretraining data. In such cases, we show that it is possible to predict the downstream translation quality metrics with good accuracy using a log-law. However, there are cases where moderate misalignment causes the downstream translation scores to fluctuate or get worse with more pretraining, whereas downstream cross-entropy monotonically improves. By analyzing these, we provide new practical insights for choosing appropriate pretraining data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes scaling laws for pre-training data and downstream data in the context of machine translation. The authors demonstrate that when the pre-training data is sufficiently aligned with the downstream task, both the downstream cross-entropy (CE) loss and translation quality adhere to the proposed scaling laws. However, if the pre-training data is not well-aligned, the downstream CE may still align with the scaling laws, but other metrics of translation quality may exhibit misalignment.

### Strengths
The paper conducts extensive experiments and present some interesting findings.

### Weaknesses
1. "Inaccurate" statement: The field of machine translation is increasingly adopting decoder-only architectures, whereas this paper focuses exclusively on encoder-decoder models. This focus leads to findings that conflict with those from SoTA decoder-only translation models. For example, in lines 355-359, the authors claim that "there is no need to pretrain the models when the fine-tuning data is large enough." This assertion totally contradicts the findings in [1], which states that "you only need a large amount of data for pre-training and a small number of data for continued fine-tuning." The key difference is that [1] employs a decoder-only model but it achieves top performance among other SoTA translation models. I am inclined to agree with the latter explanation because your training and test data are from the same domain (WMT). Training on WMT data usually yields better results on the WMT test set (especially BLEU), which might give the illusion that using only fine-tuning data is sufficient. However, this approach may lead to poor generalization abilities. A large training dataset may have less impact on in-domain test data, but it's essential to ensure that the model generalizes well to out-of-domain data. Therefore, the authors should also investigate the model's performance on other out-of-domain test datasets to provide a more comprehensive evaluation before make this statement.

2. Out-of-date metric: Most of the findings in this paper rely on BLEU scores. However, BLEU is increasingly regarded as an inaccurate metric that does not align well with human judgments, especially when compared to other metrics like COMET. The inclusion of ROUGE also seems weird, as ROUGE is primarily used for summarization evaluation rather than translation. While it might be applicable in certain cases, it is not a mainstream choice for assessing translation quality. The authors should consider using more suitable metrics, such as BLEURT, to provide a more accurate evaluation of their models.

3. Unclear writing: While this is a minor issue, the paper's writing feels disjointed and contains redundant information. There are several instances where the same points are reiterated, such as "when the distribution is well-aligned, both metrics and CE align with the scaling laws." Moreover, the frequent references to figures that are located several pages away disrupt the reading flow and make it difficult to follow the arguments being presented.

4. Lack of definition: I struggled to understand what the authors mean by the "distribution of pre-training and downstream task." It wasn't until midway through the paper that I realized this likely refers to the amount of monolingual target language data included in the pre-training dataset—where more target language data equates to a more "aligned distribution." One question here, if the authors were to conduct experiments on another low-resource language like Icelandic, where the fine-tuning data consists of a small amount of news content but the available pre-training monolingual data is primarily from games, the "distribution/alignment" becomes ambiguous. Alternatively, one might employ cross-lingual learning using a high-resource language like German, for which abundant news data is available. In this scenario, which dataset constitutes a "more aligned distribution"—the Icelandic data from a different domain or the German data from the same domain? I believe that the term "distribution" is too abstract and makes the paper challenging to understand. Providing a more precise definition or elaborating on this concept would greatly enhance the clarity of the paper.

5. A narrow scope in high-resource languages: The focus on high-resource languages is not particularly compelling, as SoTA models already perform exceptionally well in these languages, regardless of scaling laws. People can simply amass large amounts of data for training to achieve excellent results. The paper's emphasis on utilizing billions of tokens for pre-training and millions of parallel sentences for fine-tuning is not practical for many mid- or low-resource languages, where those languages do not have the resource.  A more interesting and valuable direction would be to explore scaling laws that examine how high-resource languages can be used to support low-resource languages. Investigating how data from other languages can enhance translation quality in languages with limited resources would address a critical need in the field of MT and contribute to more inclusive and effective translation models.

### Questions
N/A

### Soundness
2

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
4

### Summary
Past work on scaling laws has mostly focused on pretraining loss rather than downstream transfer learning task performance. This paper attempts to establish scaling laws for transfer learning for machine translation. The paper specifically investigates how pretraining data size affects downstream translation performance, measured in terms of downstream cross-entropy loss as well as in terms of downstream machine translation metrics like BLEU. Results show that that size of finetuning data, as well as the similarity between the pretraining and finetuning datasets, have a large impact on downstream results and scaling behavior. Most interestingly, the results indicate that when pretrain and finetune are well enough aligned, there is a clear log scaling law for pretraining size on downstream machine translation metric performance. However, when pretrain and finetune are dissimilar, more pretraining data can sometimes even hurt performance on downstream machine translation metrics. This stands in contrast with downstream cross-entropy, which improves monotonically with pretrain size regardless of pretrain/finetune mismatch.

### Strengths
The paper seeks empirical answers to important questions -- scaling laws (even rough ones) for downstream transfer can provide useful guidance: When should one seek out different pretraining data vs more pretraining data? How much finetuning data is sufficient for good downstream performance?

The paper focuses specifically on machine translation -- an important NLP task that has not been the main focus of prior transfer learning scaling law work. This is a strength. The application focus lets the paper go into more depth in empirical analysis and leads to clearer takeaways. 

The paper concretely shows that downstream cross-entropy can be misleading. The paper finds that downstream cross-entropy monotonically improves with pretrain size, even when other machine translation metrics like BLEU do not. This is a useful result for future researchers.

### Weaknesses
Aspects of the presentation could be improved. Specifically, as a reader, I found it confusing that the paper essentially starts with a results / takeaways section before discussing experimental details. Then an experimental details section comes next, followed by a results / takeaways section. I think a more traditional ordering could be more effective here -- the intro could be used to discuss high-level takeaways up front, leaving the rest of the detailed results to be described after experimental setup is clear. Without having a clear understanding of experimental setup, I was left wondering in many cases how to interpret the early results discussion. 

The one experimental weakness that stood out to me: It's not entirely clear how "alignment" between pretrain and finetune is being defined. For the most part, it seems to mean in the context of this paper whether and to what extend that datasets share languages. This could be further clarified and formalized -- but, further, more nuanced measures of alignment could easily be reported. These might help clarify experimental takeaways having to do with alignment, which represent some of the more interesting results in this paper. 

Minor:

-Discussion of results on other tasks is odd given that paper is focused on MT.

-I couldn't follow remark 2 -- what was the main takeaway / hypothesis? Consider rephrasing this section for improved clarity. 

-"3.4 A Guide for ..." section is kind of confusing -- especially part 2.

### Questions
see above

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper analyses to what extent scaling laws apply if the pre-training and downstream data are well or less well aligned. They find that iff the data is less aligned, task-specific metrics can fluctuate when increasing the pre-training data, while increasing more monotonically if the data is well aligned. Their findings are mostly based on machine translation experiments but also generalize to more general tasks such as the tasks in the SuperGlue benchmark set.

### Strengths
- well written paper
- addresses a problem that is relevant for a large community
- thourough empirical analysis

### Weaknesses
Although the concept of alignement is central to this work and many times the authors refer to "degree of" or "not sufficient" alignment, no definition of alignment is given. I understand that this is not trivial but I would appreciate at least an attempt to provide a---ideally formal---definition that could also be used to quantify alignment. Currently, it seems the only way is to determine the degree in hindsight (see lines 227--228) by failing to fit the scaling law.

### Questions
To what extent do you expect your findings to carry over to decoder-only models more commonly found in current LLMs?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper investigates the scaling behavior of downstream performance metrics, including translation scores and cross-entropy loss, as a function of the size of the pretraining dataset in machine translation tasks. The authors conduct experiments using T5 models trained on different subsets of the Multilingual C4 dataset and fine-tuned on various translation tasks. They find that when the pretraining and downstream tasks have well-aligned distributions, both translation scores and cross-entropy loss improve monotonically with more pretraining data. However, when the distributions are not well-aligned, translation scores can exhibit non-monotonic behavior, while cross-entropy loss still improves monotonically. The authors propose a practical guide for evaluating the value of pretraining data for translation tasks based on downstream translation scores and demonstrate the effectiveness of their approach on multiple natural language processing tasks.

### Strengths
The paper's main contribution is its in-depth investigation of the impact of pre-training data on machine translation tasks and the proposal of a new logarithmic law to describe the change in downstream performance as the size of the pre-training data increases. This research is helpful to understand the performance of large-scale language models in specific downstream tasks and provides a new method for evaluating the value of pre-training data. From the perspectives of innovation and importance, the paper is highly valuable. Additionally, the quality and clarity of the paper are good, with detailed descriptions of experimental design and result analysis, and abundant charts and empirical evidence to support conclusions.

### Weaknesses
One potential weakness of the paper is it is focusing solely on downstream performance changes in machine translation tasks. This limits the comprehensive evaluation of the applicability of the logarithmic law to a wider range of natural language processing tasks.
For NLP tasks that use precision and recall as metrics, can these be effectively aligned with the pre-training procedure? Additionally, can cross-entropy be generalized to observe the scaling law?

It is recommended to include a reference to the inference scaling law from OpenAI’s o1 model and to discuss the scaling law within a broader framework.

### Questions
The alignment between the pre-training and downstream task is crucial to understanding the scaling law. I am not entirely clear on what “align” means in this context. Could you please explain in detail the meaning of “align” in this work?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates scaling laws for downstream task performance in machine translation, specifically examining how pretraining dataset size affects translation quality after finetuning. The authors propose a novel log-law to describe the scaling behavior of translation quality metrics (BLEU, ROUGE, COMET) and demonstrate that the relationship between pretraining data size and downstream performance heavily depends on distribution alignment and finetuning dataset size. A key finding is that while cross-entropy consistently follows power-law scaling, translation quality metrics may deviate from expected scaling patterns when pretraining and downstream distributions are not well-aligned.

### Strengths
- Exceptionally well-grounded in literature, with relevant prior work effectively woven throughout the paper's narrative.
- Strong experimental methodology with fully controlled experiments that isolate different variables' effects. In contrast to a lot of recent LLM works, the experiments are fully controlled which I appreciate a lot. The paper demonstrates comprehensive validation across multiple metrics and scenarios, with clear empirical support for the proposed log-law.
- The writing is clear and the structure effective. Clear and systematic presentation of results with thorough analysis.
- The proposed log-law for translation quality metrics is well-motivated and comprehensively validated.
- Makes important observations challenging common assumptions about cross-entropy and translation quality metrics.

### Weaknesses
 - Limited to pairwise language combinations in pretraining - would benefit from discussion about generalization to realistic multilingual pretraining scenarios.

- It would be a great addition to have a short discussion that connects these findings to recent successes in LLM-based MT. For instance, some works like https://aclanthology.org/2024.tacl-1.32/ and https://aclanthology.org/2024.acl-long.336/ fine-tuned directly on parallel data, but these LLMs are heavily English-centric and therefore there is a low distribution alignment. More recent work like ALMA https://openreview.net/forum?id=farT6XXntP and TowerLLM https://openreview.net/forum?id=EHPns3hVkj#discussion circumvent this issue by continuing pre-training on multilingual data before fine-tuning on parallel data.

- Minor  issues
    - Lines 142-143: "Tran et al., 2019" is repeated 3 times
    - Lines 264-265: it'd be nice to include fine-tuning dataset sizes here

### Questions
- This is in not a critique but I'm curious about your thoughts. You study pre-training with up to 2 languages. How do you think your findings translate to the more realistic setting of pre-training on a large number of languages, with severe misalignments in data size between the languages?

- Similarly, do you have any findings related to language similarity?

### Soundness
4

### Presentation
3

### Contribution
3
