# Understanding Synthetic Context Extension via Retrieval Heads

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Long-context LLMs are increasingly in demand for applications such as retrieval-augmented generation. To defray the cost of pretraining LLMs over long contexts, recent work takes an approach of synthetic context extension: fine-tuning LLMs with synthetically generated long-context data in a post-training stage. However, it remains unclear how and why this synthetic context extension imparts abilities for downstream long-context tasks. In this paper, we investigate fine-tuning on synthetic data for three long-context tasks that require retrieval and reasoning. We vary the realism of ``needle'' concepts to be retrieved and diversity of the surrounding ``haystack'' context, from using LLMs to construct synthetic documents to using templated relations and creating symbolic datasets. We find that models trained on synthetic data fall short of the real data, but surprisingly, the mismatch can be interpreted and even predicted in terms of a special set of attention heads that are responsible for retrieval over long context: \textit{retrieval heads} \citep{wu2024retrieval}. The retrieval heads learned on synthetic data are mostly subsets of the retrieval heads learned on real data, and there is a strong correlation between the recall of heads learned and the downstream performance of a model. Furthermore, with attention knockout and activation patching, we mechanistically show that retrieval heads are necessary and explain model performance, although they are not totally sufficient. %
Our results shed light on how to interpret synthetic data fine-tuning performance and how to approach creating better data for learning real-world capabilities over long contexts. %

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the mechanism behind synthetic context extension helping long-context LLMs, where the models are fine-tuned with synthetically generated long-context data. Across three long-context retrieval and reasoning tasks, the paper examines the effects of varying "concept expression" and "context diversity" in fine-tuning and demonstrates that synthetic data yields inferior performance compared to real data. Through analysis of retrieval heads, the paper interprets the performance gap between the two types of fine-tuning data.

### Strengths
1. The paper presents a framework for constructing synthetic long-context examples from existing databases with controlled similarity to real data.

2. The retrieval heads analysis provides interpretable insights into the behavioral differences between models trained on different datasets, helping explain both the effectiveness and limitations of synthetic data.

### Weaknesses
1. The visualization quality and clarity of figures should improve. 1) Figure 1's axis labels are of tiny size and poor resolution. The leftmost axis labels are occluded. The "Retrieval Heads" heatmap lacks a color scale legend. 2) Figures 4 and 5 would benefit from increased font sizes for better readability.

2. The subset relationship of retrieval heads. 1) The assertion in line 361 that synthetic data retrieval-scoring heads are "strict subsets" of those from real data training appears to contradict Figure 1, where certain heads (e.g., head #0, layer #21) show high scores in synthetic data plots but not in real data plots. 2) The characterization in line 428 describing these heads as "nearly" a subset requires clarification. The authors are encouraged to specify for which tasks and conditions the strict subset relationship holds versus where it is approximate.

3. The paper employs LoRA fine-tuning, and it would be helpful to know how might the observed patterns in retrieval head behavior and dataset relationships generalize to full parameter fine-tuning. If it is impractical to verify it empirically due to computational constraints, authors' predictions and explanations would be valuable.

### Questions
1. About limited real data training. 1) It would be better if the paper could quantitatively define the "limited" real data condition. 2) Figure 4 shows under some circumstances, synthetic data outperforms the limited relation subset of the real data. Could the authors discuss whether increasing synthetic training examples can help surpass limited real data performance? 3) Whether hybrid training (combining limited real data with synthetic data) could enhance performance, particularly for tasks where the retrieval head of synthetic is not a strict subset of the real data?

2. MuSiQue's context extension (line 137). It would be better if the authors could elaborate on what criteria governed the selection of padding paragraphs, and how to ensure the added context did not introduce extra information implying the answer to a certain hop's question.

3. In Table 4, cells in the columns "Compl.", "Inter.", "Rand" and row SummHay appear to have the same values as those in Table 3. The "Orig." value for (Real, Real) setting is also inconsistent with the addition of "Orig." and "delta" values in the following rows.

4. The paper employs LoRA fine-tuning, and it would be helpful to know how might the observed patterns in retrieval head behavior and dataset relationships generalize to full parameter fine-tuning. If it is impractical to verify it empirically due to computational constraints, authors' predictions and explanations would be valuable.

I am willing to change the score if my concerns are addressed.

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
2

### Summary
This paper provides a method to analyze how synthetic data help with long context tasks for LLM, and provides. The authors start by handcraft several principles (Concept Expression, Context Diversity & Symbolic Tasks) to construct data, and find that different tasks shares few similarity in preference. Then, the authors find that there is a high corelation between similarity of retrieval heads and model performance after finetuning, which can be regards as a metric to indicate the quality of the synthetic dataset.

### Strengths
The quality analysis of the synthesized datasets is reasonable. The authors provide evidences to show that there are no preset principles on how to synthesize data, and find similarity of retrieval heads to be a highly-corelated metric. Sufficient experiments have been done to support this.

This paper could be a guidance in future works for synthesize datasets, which can provides a new perspective for downstream tasks in LLMs.

### Weaknesses
This paper serves real data as the ceiling. However, the amount and distribution of real data may also influence the finetuned performance. Is it possible that in some cases, the synthesized dataset performs better than real data? (for example, the amount of data is larger) If so, the similarity of retrieval heads with real data may not be a good metric under such conditions.

This paper takes concept expression, context diversity and symbolic tasks as three principles to manually synthesize data. I am not sure if the combination of these has a good coverage of all possible.

In L202, it seems that the low-diversity version is also a meaningless version for the task. I can hardly imagine if the sentences “The grass is green. The  skyis blue...” can influence the model. This setting fused *diversity* with *quality*, making it hard to ablate their influence on the performance. In my opinion, the repeated pattern should be at least some meaningful text related to the task.

### Questions
As in weakness, it raises concerns involving two aspects:
1. Is the handcrafted principle in Sec. 3 representative enough?
2. What is the border of using similarity of retrieval heads to score a synthetic data? Is there some preconditions (such as amount)?

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
This paper utilizes a recently introduced concept of “retrieval heads” in transformers, i.e. the heads that copy tokens from the context to the output which are characterized by "retrieval score". 

The authors explore the influence of such heads on the fine-tuning on realistic and synthetic long-context data. They provide a fixed protocol for generating synthetic data and perform experiments that show that the configuration of retrieval heads is a good predictive feature for model performance.

Namely, they conduct the following experiments:

- mask out retrieval heads and observe drop in performance; 
- describe dataset with a vector based on retrieval scores of all heads in the model trained on this dataset and measure similarity between datasets via cosine similarity between these vectors. They find that the closer a synthetic dataset to the realistic one the better is the performance of the model trained on it.
- patch a weaker model (trained on synthetic data) by substituting its retrieval heads by the ones from a stronger model (trained on real data) and observe increased performance for the patched model.

### Strengths
- The authors designed a principled way to generate synthetic data for long-context fine-tuning.
- The authors introduce a way to measure similarity between synthetic and realistic datasets in terms of retrieval scores that is correlated with performance on these datasets. While it requires further investigation, I find this idea promising for guiding synthetic data generation of higher quality.

### Weaknesses
## Lack of contributions

I will outline the candidates for contributions and then explain why I think they are not sufficient for a conference paper.

As far as I understand, the main takeaways from the paper are:
- retrieval heads influence performance;
- models differently fine-tuned for the same task share a subset of retrieval heads;
- if we insert retrieval heads from a stronger model instead of the corresponding retrieval heads in the weaker model, the performance of the weaker model will improve;
- if we measure the similarity between synthetic and realistic datasets based on the retrieval scores of the models trained on them this similarity will correlate with performance;

The first two points were already discovered in [1]. The latter point follows from the first two points and the fact that heads in differently fine-tuned transformers can be interchangeably patched which was discovered in [2].

The fourth point is a promising step towards explaining how to generate synthetic data achieving realistic data quality. However, I find this step alone not enough for a conference paper as the authors do not explain how to generate synthetic data but only show a way to predict the performance of models trained on it while requiring access to realistic data to compute similarity with models trained on it (which is a big limitation as in real-world scenarios we do not have access to realistic data).

## Missing explanations for crucial parts

- Retrieval heads are introduced in line 293 (shown in italics) but it is still not clear how they are formally defined even though it is a crucial concept for the whole paper. I guess that they are the top-k heads after sorting by retrieval score, but would be nice to read it in text.
- It is also not explained how to detect common subsets (intersections) of retrieval heads between models trained on different datasets (this is important for sections 4.3 and 5). I also wonder whether any matching algorithm (to understand to which head in another model current head corresponds) is applied because simple matching by heads' indices might not be enough as models might have functional symmetry i.e. if we permute heads model outputs will not change while head indices will.
- There is no explanation for how patching is done. There is a phrase “following Prakash et al. …” in line 471, however, it is important to properly define this operation as it is a key part of the section 5.

## Experiment request

This paper provides a new way to generate datasets for long-context retrieval tasks, however, it is not immediately obvious for me that long-context fine-tuning is needed to solve them. Could you please provide results for base models fine-tuned only on short-context data to show that fine-tuning on long-context is really required for the constructed tasks.

## Unclear writing

- It is not explained what is EM in line 357. I guess it is "exact match" but it should be defined as the main performance metric used in experiments.
- Table 1 has duplicate columns “concept exp” and “context div” which is confusing.
- It is almost impossible to read axes' names in Figure 1.
- The caption in Figure 3 does not explain what the figure shows.
- Theta and RoPE embeddings are not defined in line 154.
- It is very hard to understand the tasks from the current descriptions. Could you please give examples of samples from datasets and needles for them (at least in appendix)?
- Where do numbers from paragraph in line 356 come from? Figure 1 does not have 0.35 EM or 0.32 and 0.20. Where do number of heads 129, 112 and 39 heads come from?

## Typos

- 280: a sparse of heads - sparse is not a noun
- 309: given AN evaluation example
- 351: H_synth reflects
- 481: is THE greatest
- 101: not \mathcal{M}
- 126: no dot in the end

### Questions
- In line 35 you say: “but pre-training a long context model would necessarily reduce the number of observed tokens.”. Could you please explain what do you mean by “observed tokens” and why pre-training on a long context reduces their number?
- Why does the Figure 4 contain several dots with the same name, e.g. R,R (L)?
- What is the difference between SummHay insight and SummHay retrieval in Table 2?
- In line 484 you say: “The success of these heads on different tasks likely is caused by upstream changes in the model during fine tuning, which specifically change the representations passed to these retrieval heads.” During patching, we copy heads from another model. They were not part of the patched model during fine-tuning and therefore, I don’t see how upstream changes made during fine-tuning of the patched model can help these new heads to perform better. Could you please elaborate on that?
- In line 194 you say: “In task specific cases, it is beneficial to make this data less realistic while encouraging generalization.". I can’t understand how making data less realistic encourages generalization. In all your experiments training on realistic data led to better generalization (better test performance). Could you elaborate, please?
- What is meant by the "target" and "synthetic" tasks in line 482? So far you have introduced only synthetic datasets.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Synthetic data is widely used to enhance long-context understanding and training in large language models, particularly in scenarios with limited resources. However, assessing the efficiency and performance impact of synthetic data on large language models remains challenging. This paper explores how synthetic data for context extension impacts downstream task performance, advancing understanding of long-context behavior and how synthetic data enhances language model capabilities.

### Strengths
1. The paper is clearly written and readily comprehensible.

2. The paper presents a clear and compelling motivation. The discussion on the impact of synthetic data in training large language models is insightful and valuable for advancing the exploration and understanding of LLM principles.

3. This paper presents clear and coherent experimental procedures along with well-organized technical results.

### Weaknesses
1. This paper attempts to explore the influence and effects of synthetic data on the training of large language models (LLMs). However, it fails to establish a unified configuration and pattern, leading to results that appear somewhat random. This may affect the generalizability and applicability of the paper to a broader range of contexts.

2. I have noticed that randomly dropping attention heads can sometimes improve performance. Is it possible that certain information is detrimental, and could selectively dropping the least important heads enhance performance?

3. The evaluation for the LLM's performance is single and subjective. It may not fully support the conclusion.

### Questions
1. This paper focuses on long-context learning. I am curious whether the influence of synthetic data—and the corresponding conclusions—would be similar in short-context learning with the synthetic data, potentially enhancing the generalizability of the paper's insights.

2. This paper is well-organized and technically sound; however, it still has limitations and uncertainties. I lean toward a weak acceptance and will take the other reviewers' opinions into account before making a final decision.

3. Please see the weaknesses outlined.

### Soundness
3

### Presentation
4

### Contribution
3
