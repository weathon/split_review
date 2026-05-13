# Beyond Scale: The Diversity Coefficient as a Data Quality Metric for Variability in Natural Language Data

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
<- trailing '%' for backward compatibility of .sty file
Current trends in pre-training Large Language Models (LLMs) primarily focus on the scaling of model and dataset size.
While the \textit{quality} of pre-training data is considered an important factor for training powerful LLMs, it remains a nebulous concept that has not been rigorously characterized.
To this end, we propose a formalization of one key aspect of data quality -- measuring the \textit{variability} of natural language data -- specifically via a measure we call the diversity coefficient. 
Our empirical analysis shows that the proposed diversity coefficient aligns with the intuitive properties of diversity and variability,
e.g., it increases as the number of latent concepts increases. 
Then, we measure the diversity coefficient of publicly available pre-training datasets and demonstrate that their formal diversity is high compared to theoretical lower and upper bounds.
Finally, we conduct a comprehensive set of controlled \textit{interventional} experiments with GPT-2 and LLaMAv2 that demonstrate the diversity coefficient of pre-training data characterizes useful aspects of downstream model evaluation performance---totaling 44 models of various sizes (51M  to 7B parameters).
We conclude that our formal notion of diversity is an important aspect of data quality that captures variability and causally leads to improved evaluation performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a measure of text corpus diversity called "diversity coefficient" based on the cosine distance between Task2Vec vectors constructed from random subsets of the data. Arguing that the variability of pretraining data partly explain in-context learning and generalizability of LLMs, the authors show a correlation between the diversity coefficient and various performance metrics. On synthetic data with controlled variability, the proposed diversity coefficient follows human intuition about variability in datasets.

### Strengths
This paper tackles an important problem, potentially deepening our understanding of the effects of pretraining data quality particularly with respect to diversity.
The approach combines concepts from vision (task2vec) with language modeling to create an original measure for textual data diversity.

### Weaknesses
1. The use of cosine distance between task2vec embeddings as a diversity measure is not well motivated. Can we consider other textual embedding methods? What are the tradeoffs?
2. The absolute diversity coefficient value does not convey much information about what it means - I understand the author's argument for conceptual lower and upper bounds but these do not capture any representation of real natural language. The work should present a better way to understand the value of the measure of diversity.
3. The experiments on synthetic datasets are valuable, however the conclusions could be further strengthened by a study utilizing human annotation for diversity.

### Questions
In section 3.5, the authors use the GINC dataset generated from a mixture of hidden markov models - how natural is the resulting dataset? Does it come close to resembling text found on the web?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a metric to measure pre-training data diversity and analyses how data diversity affects model test time performance and model emergent capabilities. The diversity metric is based on an existing method to represent the data, Task2Vec. Textual data is encoded into a vector according to Task2Vec and data vectors' distance is used to estimate data diversity.  Task2Vec vectors are computed as the diagonal of the Fischer Information Matrix of the parameters \phi of the language model head (only the rest of the network is fixed) when these \phi parameters are fine-tuned on the target data to assess. On experiments, the authors show that higher data diversity relates to better test time performance, that mixed datasets give more diversity, and that the distribution of data distances can be used to characterise the datasets. 

While the rational behind the proposed method seems clear, I lack a bit of context on what previous work was done in relation to this issue (was diversity --and how measured-- use in data selection for known LLMs?) and existing approaches and baselines.  Perhaps this is discussed more in the Appendix sections, I suggest this should be made clearer in the main paper. Also, how this metric would help in the selection of data for pre-training?

### Strengths
A tool to measure pre-training data diversity.

### Weaknesses
 - While the authors evaluate performance against pre-training data diversity (section 3.1), the metric for performance is cross-entropy loss in LM, I wonder whether specific task evaluation on NLP tasks would make sense here (many NLP benchmarks used to benchmark LLMs on tasks like question answering, GLUE, etc.). It's unclear if the observed correlation with cross-entropy loss would translate to improvements on downstream tasks, which are the ultimate goal of pre-training. The paper should include experiments on a range of downstream tasks to validate the usefulness of the proposed diversity metric.
- The Vendi Score seems to be another approach to compute diversity, why was not included as a baseline in the main experiments (at least in main Table 1)? The absence of a comparison with this existing method makes it difficult to assess the relative merits of the proposed approach. It is important to understand how the proposed metric compares to other diversity measures in terms of computational cost, sensitivity to different data characteristics, and correlation with downstream task performance.


### Questions
1. Line 122, which t is used to compute the FIM matrix for sequences of a batch? Are all the steps from the sequence averaged? or is FIM only build based on the last step?
2. I suggest the authors to rewrite some pieces of text. There are places where authors use phrases like "by them" , "they ..." and it is not clear what the referents are what makes the reading and understanding of the paper more involved.
3. Task2Vec should be fully and better described in the main paper (including how was used before, its intuition, etc.).
4. Section I.2 should mention the data used to pre-train GPT2.

Minor comments:

- Figure 1 does not seem to add much to the understanding of the approach, maybe an algorithm would be more useful?
- All figures are too small to read.
- Line 751, "this more sophisticated aggregation method" which aggregation method?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a metric to measure the diversity of language modeling pre-training datasets. The proposed metric is the expected distance between Task2Vec embeddings of random batches sampled from a dataset. This metric is applied to several pre-training datasets, and compared to upper and lower bounds. The paper presents some experiments aiming to relate the proposed measure of diversity with downstream perplexity on C4 and OpenWebText2. In a synthetic setting, the proposed diversity metric increases with vocabulary size and number of latent concepts.

### Strengths
This work focuses on an important and potentially very impactful area of research. While the general belief of the community is that data diversity is an important factor for the performance of language models, the relationship between pre-training data diversity and downstream performance is currently poorly understood. The use of Task2Vec embeddings to measure data diversity is to the best of my knowledge novel. The diversity results presented in Table 1 align well with current intuitions in the community regarding CC-derived datasets being more diverse than non-CC Pile subsets.

### Weaknesses
 > Claim: “PRE-TRAINING IN HIGHER DIVERSITY LEADS TO BETTER EVALUATION PERFORMANCE” (Section 3.1)

The experiments in Section 3.1, aiming to relate their proposed measure of data diversity with performance, which in my view would amount to the most substantial contribution of the paper, are highly unconvincing.

Only three datasets are considered: PubMed, USPTO, and PubMed+USPTO. Linear regressions on three (!) datapoints are presented as evidence to substantiate the authors claim. Clearly, the actual relationship between diversity and performance will neither be linear nor monotonic — pre-training on random tokens (e.g., the upper bound of perplexity considered by the authors) would certainly lead to very bad performance while having maximal diversity. For most of the GPT-2 experiments, PubMed+USPTO has similar or higher loss than PubMed while also having higher diversity.
To make matters worse, the choice of the 2 pre-training datasets are highly unusual and not representative of the pre-training corpora of current language models. More convincing choices would have been C4, OpenWebText, The Pile (in its entirety), RedPajama, SlimPajama, RefinedWeb, Dolma, FineWeb, DCLM, … 
The experiments consist of many small-scale training runs, where the differentiating factor is scale (e.g., number of parameters and training tokens) and architecture (e.g., GPT-2 or Llama 2). Since what authors aim to study is the relationship between dataset diversity and performance, what should vary are the datasets. The results could be much more convincing if authors were to consider a single architecture and scale  (e.g., Chinchilla optimal 1B model), but as many pre-training datasets as possible.
Choice of evaluation metric: it is unclear why PPL on OpenWebText2 and C4 is a meaningful evaluation metric. For example, does PubMed lead to lower PPL because of its higher diversity, or because it is simply more similar to C4/OpenWebText? To get around this problem, work on pre-training data quality has started to use “early-signal benchmarks” — see the FineWeb or DataComp-LM papers.


> Other empirical results are less significant

In addition to the empirical results of Section 3.1, authors also show that concatenating datasets leads to higher diversity under their proposed diversity metric (Section 3.3), that the proposed cross diversity coefficient is higher than a single dataset’s diversity and leads to well-sepearted histogram distance clusters (Section 3.4), and that in a synthetic setting the proposed diversity metric increases with vocabulary size and number of latent concepts (Section 3.5). While these results are reasonable checks on the proposed diversity metric, they are not particularly compelling contributions. It would be interesting to know if other simpler embeddings approaches (e.g., N-gram, mean GPT-2 last layer embedding) fail such checks.


> It is not well motivated why to use Task2Vec encodings

Much prior work has considered N-gram or vector embedding based similarity metrics for text. While this work novelly considers Task2Vec embeddings for text, it is unclear why Task2Vec embeddings are preferable. While some discussion is provided in Appendix C (which I would encourage authors to partly move to the main text —or at least reference), it would be much more compelling if authors replicated the core empirical results of the paper (e.g., Figures 2, 3, and 4)  to show the limitations, if any, of simpler, previously proposed similarity measures.

The writing is sufficiently clear but could certainly be improved. The legibility of figures could also be improved.

### Questions
See the specific points made in the limitations section.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel approach to using diversity as a metric for evaluating the quality of training data used in training language models. The authors propose that this diversity metric correlates with downstream performance and use it to intervene in data compositionality. They claim that their metric is closely tied to model evaluation outcomes.

The diversity metric is computed using Task2Vec, which generates a vector representation based on text batches. This method relies on a GPT-2 embedding model, and the diversity score is determined by calculating the expected cosine distance between different batches of data.

The authors conduct multiple experiments across various datasets to calculate diversity scores, establishing lower and upper bounds to provide context for their results. To demonstrate the utility of the metric, they create a new dataset by merging two datasets, controlling for size, and training several language models of different sizes and architectures. They claim to show a correlation between the diversity metric and model quality, as measured by cross-entropy.

While the premise of the paper is clear and motivated, there are several flaws in the evaluation and claims. These shortcomings, along with suboptimal writing, suggest that the paper is not ready for publication in its current form. Additionally, several related works that should have been cited for comparison are missing. Below, I outline specific issues:


Validity of Claims
--------

- The authors assert that their work represents a paradigm shift in data-centric machine learning through the introduction of data diversity (L. 59). This claim is factually incorrect, as many previous studies have explored data diversity. Several relevant papers, which I list at the end of this review, were overlooked.
- The claim that their method is interpretable is problematic. The term "interpretable" can be subjective, and in this case, the proposed metric is as much a black-box as other metrics that output a single number. Describing the metric as interpretable seems like an overreach. Additionally, the range of values produced by the metric is not intuitive, with a lower bound around 0.05 and an upper bound of 0.4, which feels inelegant.
- The authors claim that higher diversity leads to better performance (Figure 2), but this relationship does not hold consistently. In some cases, performance declines with increased diversity, which the authors fail to address. Moreover, the presentation of results in graphs rather than tables makes it difficult to investigate this trend thoroughly.
- Importantly, the paper does not adequately account for potential confounding factors. When merging two datasets to create a more diverse one, the authors do not consider that other characteristics of the combined dataset may influence performance, aside from diversity.

In addition to these major concerns, there are minor inaccuracies in some claims:
- L.111: The assertion that the probe network’s parameters are the most important for solving the task may be incorrect. This point doesn’t heavily impact the paper’s argument but should either be substantiated or revised.
- L.266+269: The bounds discussed are described as theoretical, but they are actually empirical.


Evaluation
-----------

The evaluation is based solely on cross-entropy scores from some evaluation data, which is not a strong or convincing measure. Even if all results showed a consistent trend (which they do not), the claim that increased diversity leads to better downstream performance is weakly supported.

Formatting and Clarity
--------------

While relatively minor, the following formatting and clarity issues should be addressed in future revisions:
- L.33: Missing parentheses around citations (use \citep).
- L.66: The meaning of “latent concepts” is unclear and should be explained.
- L.69: There is a grammatical issue with “by them to.”
- Figure 1 is too small and would benefit from a size increase for readability.
- L.122: In the formula, “t-1:1” should be “1.”
- L.151: The phrase “pre-trained on the English language” is awkward. The model is trained on a corpus in English, not on the language itself.
- Captions for tables and figures are unnecessarily long.
- L.191-192: The argument about the lower bound is unclear.
- L.197: The term “non-special” token needs clarification.
- L.209: The meaning of “formal diversity” is unclear.
- Figure 3: Breaking it into subfigures (a-d) would make it easier to refer to each subfigure separately.
- L.317: The notation “+0.03-0.05” is unclear and needs to be clarified.
- Section 3.4: This section seems out of place. It should be moved to the beginning to help establish the validity of the metric early on.
- L.360: It seems that “right/left” was meant instead of “top.”

Relevant Previous Work
---------------

- https://arxiv.org/pdf/2307.12532
- https://arxiv.org/pdf/2205.06253
- https://arxiv.org/pdf/2407.15724
- https://arxiv.org/pdf/2103.03399v2
- https://arxiv.org/abs/2311.08695
- https://proceedings.mlr.press/v162/fang22a/fang22a.pdf
- https://arxiv.org/pdf/2403.00553


---------------

Post authors' response
---

I read the authors' response, and appreciate their responses, and believe the changes would make the paper much stronger.
However, since there are many changes required, I think it should go through another round of reviews.
I look forward reading the improved version of the paper. I will keep my scores unchanged.

### Strengths
- The introduction of a metric aimed at capturing the diversity of textual data is a valuable contribution. This could be useful for further research into how data composition impacts model training and performance.
- The authors provide some evidence supporting the idea that diversity influences model performance, specifically in terms of perplexity. This demonstrates a potential relationship between diversity and model generalization capabilities.

### Weaknesses
Validity of Claims
--------

- The authors assert that their work represents a paradigm shift in data-centric machine learning through the introduction of data diversity (L. 59). This claim is factually incorrect, as many previous studies have explored data diversity. Several relevant papers, which I list at the end of this review, were overlooked.
- The claim that their method is interpretable is problematic. The term "interpretable" can be subjective, and in this case, the proposed metric is as much a black-box as other metrics that output a single number. Describing the metric as interpretable seems like an overreach. Additionally, the range of values produced by the metric is not intuitive, with a lower bound around 0.05 and an upper bound of 0.4, which feels inelegant.
- The authors claim that higher diversity leads to better performance (Figure 2), but this relationship does not hold consistently. In some cases, performance declines with increased diversity, which the authors fail to address. Moreover, the presentation of results in graphs rather than tables makes it difficult to investigate this trend thoroughly. The lack of tabular data makes it impossible to perform a rigorous analysis of the relationship between diversity and performance, and the authors do not provide any statistical analysis to support their claims.
- Importantly, the paper does not adequately account for potential confounding factors. When merging two datasets to create a more diverse one, the authors do not consider that other characteristics of the combined dataset may influence performance, aside from diversity. For example, the combined dataset might have a different distribution of token frequencies or a different average sentence length, which could affect the training dynamics and final performance of the models.

In addition to these major concerns, there are minor inaccuracies in some claims:
- L.111: The assertion that the probe network’s parameters are the most important for solving the task may be incorrect. This point doesn’t heavily impact the paper’s argument but should either be substantiated or revised.
- L.266+269: The bounds discussed are described as theoretical, but they are actually empirical.


Evaluation
-----------

The evaluation is based solely on cross-entropy scores from some evaluation data, which is not a strong or convincing measure. Even if all results showed a consistent trend (which they do not), the claim that increased diversity leads to better downstream performance is weakly supported. The use of cross-entropy alone does not provide a comprehensive view of model performance. Metrics such as accuracy, F1-score, or BLEU score, depending on the task, would provide a more robust evaluation. Furthermore, the authors do not perform any statistical significance tests to determine whether the observed differences in cross-entropy are meaningful.

Formatting and Clarity
--------------

While relatively minor, the following formatting and clarity issues should be addressed in future revisions:
- L.33: Missing parentheses around citations (use \citep).
- L.66: The meaning of “latent concepts” is unclear and should be explained.
- L.69: There is a grammatical issue with “by them to.”
- Figure 1 is too small and would benefit from a size increase for readability.
- L.122: In the formula, “t-1:1” should be “1.”
- L.151: The phrase “pre-trained on the English language” is awkward. The model is trained on a corpus in English, not on the language itself.
- Captions for tables and figures are unnecessarily long.
- L.191-192: The argument about the lower bound is unclear.
- L.197: The term “non-special” token needs clarification.
- L.209: The meaning of “formal diversity” is unclear.
- Figure 3: Breaking it into subfigures (a-d) would make it easier to refer to each subfigure separately.
- L.317: The notation “+0.03-0.05” is unclear and needs to be clarified.
- Section 3.4: This section seems out of place. It should be moved to the beginning to help establish the validity of the metric early on.
- L.360: It seems that “right/left” was meant instead of “top.”

### Questions
Suggestions are listed in the main review.

### Soundness
2

### Presentation
2

### Contribution
2
