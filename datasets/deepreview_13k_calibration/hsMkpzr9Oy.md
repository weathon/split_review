# Mexa: Multilingual Evaluation of English-Centric LLMs via  Cross-Lingual Alignment

- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 5, 5, 6, 5

## Abstract
English-centric large language models (LLMs) often show strong multilingual capabilities. However, the multilingual performance of these models remains unclear and is not thoroughly evaluated for many languages. Most benchmarks for multilinguality focus on classic NLP tasks, or cover a minimal number of languages.
We introduce \genericname, a method for assessing the multilingual capabilities of pre-trained English-centric LLMs using parallel sentences, which are available for more languages than existing downstream tasks. \genericname leverages the fact that English-centric LLMs use English as a kind of pivot language in their intermediate layers. It computes the alignment between English and non-English languages using parallel sentences to evaluate the transfer of language understanding from English to other languages. This alignment can be used to estimate model performance in other languages.
We conduct studies using various parallel datasets (FLORES-200 and Bible), models (Llama family, Gemma family, Mistral, and OLMo), and established downstream tasks (Belebele, m-MMLU, and m-ARC). We explore different methods to compute embeddings in decoder-only models.
Our results show that \genericname, in its default settings, achieves a statistically significant average Pearson correlation of 0.90 with three established downstream tasks across nine models and two parallel datasets.
This suggests that \genericname is a reliable method for estimating the multilingual capabilities of English-centric LLMs, providing a clearer understanding of their multilingual potential and the inner workings of LLMs.
\begin{center}
\renewcommand{\arraystretch}{1.2}
\footnotesize
\begin{tabular}{ll}
     \hf \, \textbf{Leaderboard} &\href{https://huggingface.co/spaces/cis-lmu/Mexa}{\path{hf

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose a method to predict the performance of English-centric LLMs on other languages using information about the alignment between English and other languages in the LLMs. The central hypothesis here is that the LLMs performance on a task is primarily dependent on the English performance, and performance on other languages depends on how well its representations are aligned with English. The paper proposes a measure MEXA to compute the similarity of representations between languages and shows that MEXA score is high correlated to the language performance on a task. Results are shown on 3 classification tasks and multiple, diverse languages including low-resource languages. MEXA score only requires a small parallel corpus to compute the alignment scores between the languages.

### Strengths
- The paper proposes a simple approach for prediction of multilingual performance, that requires few resources and is easy to implement. 
- The experiments are done on a wide range of languages, showing inclusivity and making the results solid. 
- The related work on understanding alignment is well-covered.

### Weaknesses
 - There is prior work on prediction of performance of multilingual NLP models based on various features like linguistic similarity, vocab overlap, embedding similarity, pre-training data size etc. These have not been discussed. This is directly relevant to the work, and in fact the proposed work can be considered a special case of many of these approaches, where only a single feature - the MEXA score is used for performance prediction. In the light of these works, the novelty is limited. The moot question to answer is how good is just a single feature - the MEXA score compared to using a plethora of features that previous works have used. A discussion with respect to previous work would be useful. 
- The work focusses only on classification tasks, and does not cover generation tasks. When the NLP landscape have moved towards generative capabilties, evaluating prediction of generation quality is also important. This has been mentioned as a limitation of the work in the paper. 
- The comparison with absolute cosine similarity is very limited (Section 5.3). To solidly establish the benefits of MEXA over cosine similarity, it would be good to report absolute cosine similarity results with the same default settings (weighted average, mean pooling) across all tasks and models.  

### Questions
Table 2 is complicated to read. Please consider reorganizing to improve readability.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a method, MEXA, to evaluate the multilingual strength or capability of English centric LLMs. MEXA is an intrinsic evaluation method that utilizes a parallel corpus and calculate the embedding distances between parallel sentences in comparison to two random sentences in two different languages. A number of evaluations are conducted using several 7B models and using approximately 100 parallel examples from two datasets. The results show that their proposed method strongly correlates with the multilingual performance of the under-observation models.

### Strengths
The approach is simple and empirical results are quite strong.

### Weaknesses
The authors use only 100 examples in their evaluation which is a very small number while they have more examples available. Even if they want to keep the compute small, they should try a few models on more examples and may show that their approach require a little as 100 parallel examples.

The authors mention several tasks in Appendix but then decided to use only three tasks. I did not understand the relation behind this choice and why authors did not try to run of a larger number of tasks to show the generalization of their methodology. Authors also mentioned that the primary focus of their paper is natural understanding task. As far as I understood, their technique is general and should work for a diverse set of tsaks.

Presentation of results in tables make it very hard to digest them. Authors may select one best strategy like mean/max and present the results. Table 1 and 2 both are very hard to understand.

What is the motivation of keeping the proposed method limited to monolingual models? What about multilingual models? Expanding the experiments to multilingual model will greatly increase the impact and breadth of the proposed method.

I did not understand which of the final combination of layers work the best for MEXA? Is it a combination of all layers or a specific layer? From Figure 2, it seems that the alignment scores are best for middle layers. Is it correct? What is the optimal layer for MEXA?

A few arguments need empirical support or support from literature. - Line 50-51: for these models to be effective in other languages, it is important that the other languages align with the main language. The basis of this assumption is unclear and authors should support it empirically or from literature.

What is the exact prompt given to models and what is their impact?

Figures and tables are extremely small. I was unable to read them on paper. I am not sure this small size is even allowed by the conference. Authors should move a few models to appendix and present fewer models.

### Questions
- The authors use only 100 examples in their evaluation which is a very small number while they have more examples available. Even if they want to keep the compute small, they should try a few models on more examples and may show that their approach require a little as 100 parallel examples.

- The authors mention several tasks in Appendix but then decided to use only three tasks. I did not understand the relation behind this choice and why authors did not try to run of a larger number of tasks to show the generalization of their methodology. Authors also mentioned that the primary focus of their paper is natural understanding task. As far as I understood, their technique is general and should work for a diverse set of tsaks.

- Presentation of results in tables make it very hard to digest them. Authors may select one best strategy like mean/max and present the results. Table 1 and 2 both are very hard to understand. 

- What is the motivation of keeping the proposed method limited to monolingual models? What about multilingual models? Expanding the experiments to multilingual model will greatly increase the impact and breadth of the proposed method.

- I did not understand which of the final combination of layers work the best for MEXA? Is it a combination of all layers or a specific layer? From Figure 2, it seems that the alignment scores are best for middle layers. Is it correct? What is the optimal layer for MEXA?


- A few arguments need empirical support or support from literature. - Line 50-51: for these models to be effective in other languages, it is important that the other languages align with the main language. The basis of this assumption is unclear and authors should support it empirically or from literature. 

- What is the exact prompt given to models and what is their impact?

- Figures and tables are extremely small. I was unable to read them on paper. I am not sure this small size is even allowed by the conference. Authors should move a few models to appendix and present fewer models.

### Soundness
2

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
This paper presents MEXA, a method to evaluate the multilingual capabilities of English-centric LLMs. Given the lack of multilingual benchmarks available, multilingual capabilities of English-centric LLMs may not be well evaluated across diverse languages. 
MEXA relies on parallel sentences to calculate alignment scores between English and non-English languages to measure the transfer of language understanding from English to other languages. The authors ablate around optimal choices for layer and aggregation strategies in computing embeddings. The authors evaluate the MEXA across three multiple-choice style downstream tasks and observe that the MEXA scores demonstrates a strong correlation with downstream task performance.

### Strengths
The problem is very well motivated, particularly given the lack of multilingual benchmarks and such alignment based methods would be valuable to estimate multilingual performance in a resource-efficient manner. Such methods would be useful for determining model readiness for production deployment in specific languages.

The proposed method is straightforward and does not require any creation of additional sophisticated benchmarks or extra resources and is largely model-agnostic.

The paper is well-structured and easy to follow.

The authors perform exhaustive experiments across a wide range of languages and models, offering valuable, in-depth insights.

### Weaknesses
1. The MEXA formulation relies on relative scoring and does not account for the magnitude of cosine similarity. For example, in cases where scores are close to each other but also have low magnitudes, this minimal difference is inconsequential and does not necessarily imply alignment. Thus, the limitations of standard cosine similarity, as discussed in Section 5.3, are also relevant here. In the NMT literature, following bitext mining, which incorporates relative scores, an absolute scoring mechanism, such as a final cosine similarity threshold, is often applied to retain only high-quality pairs. Additionally, margin-based approaches have consistently shown better performance than standard cosine similarity methods (see: https://aclanthology.org/2021.acl-long.507/). Adding an absolute component to the formulation, would be beneficial.

2. The authors report correlation scores but omit absolute scores. Including absolute scores, at least for select tasks, would provide a more comprehensive evaluation and further strengthen the paper.

3. The authors’ evaluation is restricted to discriminative tasks, omitting open-ended text generation tasks. It is therefore unclear whether MEXA scores correlate with the LLM's multilingual text-generation capabilities.

4. FLORES (derived from Wikipedia) and BIBLE (potentially a component of the pre-training data) are used as parallel datasets; and many benchmarks may also be Wikipedia-based, however, it remains uncertain whether MEXA is generalizable in terms of demonstrating reliable correlations with other parallel datasets from unseen distributions. Further, the authors do not provide any method of determining the optimal choice of the parallel data to be utilized in the MEXA score computation.

5. The paper’s ablations are somewhat conventional, with previous studies having compared similar design choices. While the plots offer some valuable insights, the authors only discuss these superficially and omit in-depth analysis. For instance, since Belebele derives from FLORES, one would ideally expect it to exhibit a superior correlation with the prediction of downstream performance on Belebele. However, as illustrated in Figure 5.2, the Bible dataset exhibits a stronger correlation. The authors should explore and discuss such deviations from expected outcomes in their paper. Another example is the contrast between romanized versus native script performance, something that is actively being explored in literature, (see: https://aclanthology.org/2024.acl-long.833/, https://arxiv.org/abs/2201.12501). While the authors briefly discuss this aspect, they do not extend their analysis to other languages. Such detailed insights would add substantial value and enhance the overall assessment of the paper.

### Questions
1. How is the MEXA score for English in the first row of Table 1 calculated, given that the MEXA formulation is designed to compute alignment between English and a non-English language?

2. Prior works (https://arxiv.org/abs/2405.14782) have demonstrated that likelihood based evaluation and generative evaluation exhibit different trends, how would MEXA correlations change when switched to a generative evaluation?

3. Since the distribution of MEXA scores may vary depending on the model, the statement in lines 431-432 may not be appropriate to make.

4. How does one compare MEXA scores across different translation datasets to determine whether the trends remain consistent? If they are inconsistent, what criteria should guide the selection of the most appropriate translation dataset?

5. For different models, what is the optimal layer to compute MEXA scores? Does the choice of layer vary significantly between models, and for a new model, would it be necessary to conduct an independent analysis to determine the optimal layer, or could insights from existing experiments offer a reliable estimate?

6. Echo embeddings would serve as a valuable baseline and a useful ablation in this analysis (see: https://arxiv.org/abs/2402.15449).

### Soundness
3

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
5

### Summary
This paper proposes Mexa, a metric for quantifying cross-lingual alignment between language representations in LLMs. Most LLMs are English-centric and achieve multilingual performance in part by using English as a pivot language. This occurs in the middle layers of LLMs, where sentence representations are less language-specific, exhibiting cross-lingual alignment (similarity in vector representations). The degree of cross-lingual alignment of parallel sentences indicates to what extent English is utilised as a pivot language. Mexa quantifies this by comparing the cosine similarity of parallel sentences to non-parallel sentences, producing a metric that captures to what extent cross-lingual parallel sentences are representationally aligned. The authors present Mexa as a way to quantify cross-lingual transfer and estimate task performance based on how aligned languages are with English. Their results support the viability of this, with Mexa achieving comfortably higher correlation coefficients with downstream task performance than cosine similarity. The authors test different ways of computing sentence representations for Mexa, finding that different strategies are more effective for different types of downstream tasks.

### Strengths
(1) The main finding – that Mexa serves as a way to estimate downstream task performance based on cross-lingual alignment – is robustly supported by the results. Experiments were conducted across several LLMs, languages, and tasks, and Mexa exhibits very high correlation with task performance (both in terms of absolute correlation values and compared to cosine similarity.

(2) The authors have explored a number of design decisions for Mexa (which token representations to use to obtain sentence embeddings, how to pool embeddings) and present a full analysis of their findings. This provides practitioners with a clear guide of how to use and interpret Mexa in different contexts.

(3) The study conducted by the authors represent a valuable contribution to our understanding of multilingual LLMs. They build on previous findings and produce new insights into the mechanisms underlying cross-lingual transfers in LLMs.

### Weaknesses
 (1) The authors seem to assume at the outset that cross-lingual representational similarity WILL entail better cross-lingual transfer. This assumption is the motivating factor behind Mexa. Their results do strongly suggest this, but they should be more cautious in stating this as a hypothesis (or assumption) at the start of the paper, or provide a survey of previous work proving the relation between alignment and downstream performance. It’s possible that alignment helps to some extent, but that too much cross-lingual overlap can impede performance e.g. for high-resource languages, where using English as a pivot might not be optimal. This might or might not be the case. My point is that the authors gloss over the assumption that more alignment implies better downstream performance for other languages. I see it more as a hypothesis that their findings strongly support.

(2) Mexa is not complex as a technical contribution. It is a simple way to encode relative cross-lingual similarity. While this in itself does not degrade its value as a contribution (its impact is clearly useful), it does not introduce impressive novelty from a technical standpoint.

### Questions
The writing in some parts of the paper could be made a bit clearer, specifically lines 139--147 and 197--202. Sentences like “This criterion imposes…”, “This suggests…”, “Another motivation…” are somewhat ambiguous in the first reading. It’s not clear if the authors are referring to their motivations for introducing a new concept or citing the motivations of previous research.

### Soundness
4

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
4

### Summary
This paper proposes Mexa, which is a leaderboard for estimating the cross-lingual abilities of English-based large language models. Mexa works by using a large corpus of parallel sentences (e.g., FLORES or Bible corpora) and calculating the semantic similarity score between the given model's embeddings of the English and non-English parallel sentences. These are considered aligned if the similarity between the parallel sentences is greater than between any two non-parallel sentences. This score is aggregated over the whole corpus, and it is found to be a strong predictor of performance on downstream non-English tasks (modulo the corresponding English performance on the task). This is a useful benchmark because parallel sentences and English benchmarks are widely available, but multilingual benchmarks are less readily available.

### Strengths
1. The proposed Mexa approach is interesting and novel. I could see this approach inspiring future work in analysis of multilingual LLM performance.

2. It is impressively accurate at predicting the performance of several decoder-only English-centric LLMs on 3 different multilingual datasets

### Weaknesses
1. Lack of variety in LLMs considered. All LLMs evaluated are quite similar: they are all decoder-only models with very similar architectures. For a benchmark to be useful it needs to be reliable on arbitrary models including new ones that might be invented in the future, so it would be good to evaluate on a wider variety of architectures. Even something like Mixtral would be a good place to start. This is particularly important since some of the assumptions behind Mexa (e.g. in the paragraph at line 49-63, about English being the pivot language in the middle layers) seem based on analysis of Llama so may not hold as well when evaluating models with other architectures.

2. Benchmarks used. Mexa is quite good at predicting performance on the three multilingual benchmarks considered (table 2). However, it's not clear to me why only three benchmarks are considered; table 4 lists several more that are available. In particular, both m-MMLU and m-ARC rely on machine translation to generate the multilingual data, which means that they are more likely to align with the semantic similarity measures used, so I am not sure whether this generalizes to performance on realistic multilingual tasks. Also, there is a bit of tuning on these datasets (weighted average vs. last token, max pooling vs. mean pooling, FLORES vs. bible), and there is no held-out benchmark to truly evaluate generalization.

3. Inability to benchmark closed-source models. Unless I misunderstood, Mexa requires access to the weights to be able to evaluate a model. This makes it relatively impractical: practitioners may want to select a model by using Mexa to estimate performance on their desired task, but they will not be able to evaluate closed-source models.

### Questions
1. The idea of an "English-centric" LLM is referenced several times in the paper, but I do not see a concrete definition of "English-centric" anywhere in the paper. From my understanding, the intent of Mexa is to evaluate only English-centric LLMs, so it would be good to define what you mean by this so that practitioners know whether or not to use Mexa for a given LLM.

2. L252 "Although there are multilingual models [...] our focus here is on LLMs which are **state-of-the-art in English based tasks**": Why is the focus only on evaluating SOTA LLMs? The intention of Mexa is to be a public benchmark and leaderboard, so it will be used for a variety of LLMs, right? (including e.g. some that are really focused on one task so aren't SOTA across a variety of tasks). I am thinking it would be good to evaluate on a greater variety of LLMs for this purpose.

3. More generally, as a suggestion, I wonder if positioning this work as a benchmark was the best strategy. It was only evaluated on some relatively strict cases (open-weights/open-source models that are English-centric and decoder-only/Llama-esque and state-of-the-art on English-based tasks) which I think will hinder its usability as a benchmark (if evaluations do indeed need to be limited to such models). It may be better to position it as analysis?

### Soundness
2

### Presentation
3

### Contribution
3
