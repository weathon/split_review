# Open-Domain Text Evaluation via Contrastive Distribution Methods

- Decision: Reject
- Avg Score: 4.80
- Scores: 3, 5, 6, 5, 5

## Abstract
Recent advancements in open-domain text generation, driven by the power of large pre-trained language models (LLMs), have demonstrated remarkable performance. However, assessing these models' generation quality remains a challenge. 
In this paper, we introduce a novel method for evaluating open-domain text generation called Contrastive Distribution Methods (CDM). Leveraging the connection between increasing model parameters and enhanced LLM performance, CDM creates a mapping from the \textit{contrast} of two probabilistic distributions -- one known to be superior to the other -- to quality measures. We investigate CDM for open-domain text generation evaluation under two paradigms: 1) \emph{Generative} CDM, which harnesses the contrast of two language models' distributions to generate synthetic examples for training discriminator-based metrics; 2) \emph{Discriminative} CDM, which directly uses distribution disparities between two language models for evaluation. Our experiments on coherence evaluation for multi-turn dialogue and commonsense evaluation for controllable generation demonstrate CDM's superior correlate with human judgment than existing automatic evaluation metrics, highlighting the strong performance and generalizability of our approach

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new text evaluation method called Contrastive Distribution Methods (CDM). Among these, Generative CDM harnesses the contrast of two language models’ distributions to generate synthetic examples for training discriminator-based metrics, while  Discriminative CDM directly uses distribution disparities between two language models for evaluation. Experiments show the effectiveness of CDM on multi-turn dialogue and factuality in abstractive summarization.

### Strengths
1. The proposed method can outperform several baselines on both dialogue and summarization evaluation tasks.

### Weaknesses
1. The method design of negative sample generation raises concerns regarding its practicality and generalizability. While the authors acknowledge the importance of high-quality negative samples for discriminator performance, the rationale for training a separate model on task-specific data to generate these samples is unclear. The authors suggest that large language models (LLMs) like GPT-4 could potentially generate texts with controlled qualities via prompt design, which could offer a more efficient and adaptable approach. Relying on a task-specific model for negative sample generation might limit the method's applicability to new domains or tasks, as it would necessitate retraining for each specific scenario. A more detailed explanation of why the proposed approach is preferable to leveraging the capabilities of existing LLMs is needed.

2. The choice of baselines in the experimental evaluation appears somewhat outdated, particularly given the rapid advancements in LLM-based evaluation metrics. While the authors cite UNIEVAL [1] and G-EVAL [2] in the introduction and acknowledge their limitations, these methods represent important advancements in the field and should be included as baselines for a more comprehensive comparison. Their exclusion weakens the paper's claim of outperforming existing methods, as it leaves a gap in the evaluation against current state-of-the-art approaches. Including these baselines would provide a more accurate assessment of the proposed method's performance in the context of recent developments.

3. The experimental analysis presented in the paper lacks depth and detail. Key aspects, such as ablation studies, are not adequately addressed in the main content. This makes it difficult to fully understand the contribution of different components of the proposed method and to assess their impact on overall performance. A more thorough analysis, including a detailed examination of the effects of various design choices, is necessary to provide a more convincing evaluation of the method's effectiveness.

### Questions
I have included my questions in the weaknesses part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an interesting Contrastive Distribution Methods (CDM) for text generation evaluations. The idea presented in the paper is highly influenced from the contrastive decoding (Li et al. 2022) where the model tries to decode a sequence maximizing the contrastive momentum: m(s) = log p_expert(s) - log p_amateur(s). It builds on the partial order assumption that  the model with a larger number of parameters (expert) performs better than the smaller one (amateur), in the same model family. The paper explores two ways to use contrastive momentum for text evaluation: 1) generative CDM: the constravie momentum is used to generate negative examples by perturbing positive examples and then a discriminator is trained to separate positive examples from negative examples, and 2) discriminative CDM: estimated as the sum of the contrastive momentum at each time step. 

The experiments are done with multi-turn dialog (focusing on overall and coherence quality) and summarization (focusing on factuality) evaluations.  Discriminative CDM seems to perform better than the Generative CDM approaches on both tasks.

The paper is very interesting to read until the experiment section. The experiments and results section could have been better to strengthen their conclusions regarding their proposed methods for text evals.

### Strengths
The use of contrastive momentum for text evaluation is very interesting and could be easily generalized to different tasks and languages. 

The experiments are done on multi-turn dialogue and factuality in abstractive summarization, showing positive results for CDM. The authors have also investigated different ways of perturbing positive examples with CDM.

### Weaknesses
I felt that the experiment and results in the paper could have been a bit more thorough to make a strong conclusion about CDM as a general metric for text evaluation. Lots of questions were left unanswered. It will make it hard for people to adapt CDM in their usecases. I elaborate those questions below in the Question section.

I am not certain if the partial order assumption holds for different aspects of the text quality. For example, the authors evaluate CDM for the overall quality and coherence for dialog and factuality for summarization. It would be interesting to see if the partial order assumption holds for factuality, for examples, in the first place. The authors should report performance of expert and amateur models on different aspects. 

The authors have tried various sizes of T5 models. I think it might be of interest to include other model families in their comparisons.

For summarization, why are the authors focusing on factuality only? What about other dimensions: for example, Coherence,  Factuality,  Fluency,  Informativeness? It would have been nice to see how CDM does on various aspects. Also the comparison is limited to very few other metrics. Please see https://openreview.net/forum?id=OIe3kpwl40D for a better experimental setup.

The captions in Table 1 and Table 4 are not very clear. Is the data in the first block used to train T5 or do we use off-the-shelf T5 checkpoint? What is the “/” in 1200/3600 and 17567/2078? 

“Previous works report their performance inconsistently in either Spearman/Pearson correlation or an accuracy score with 0/1 quantization of the annotations. We adopt 0/1-quantization and report the accuracy of each baseline/model.” → This is not at all clear. It would be good to clarify this.

Minor: 

Section 4.2.2: Table 6 -> Table 5

sum_log m -> sum_m in Section 3.4.2.

### Questions
I am not certain if the partial order assumption holds for different aspects of the text quality. For example, the authors evaluate CDM for the overall quality and coherence for dialog and factuality for summarization. It would be interesting to see if the partial order assumption holds for factuality, for examples, in the first place. The authors should report performance of expert and amateur models on different aspects. 

The authors have tried various sizes of T5 models. I think it might be of interest to include other model families in their comparisons.

For summarization, why are the authors focusing on factuality only? What about other dimensions: for example, Coherence,  Factuality,  Fluency,  Informativeness? It would have been nice to see how CDM does on various aspects. Also the comparison is limited to very few other metrics. Please see https://openreview.net/forum?id=OIe3kpwl40D for a better experimental setup.

The captions in Table 1 and Table 4 are not very clear. Is the data in the first block used to train T5 or do we use off-the-shelf T5 checkpoint? What is the “/” in 1200/3600 and 17567/2078? 

“Previous works report their performance inconsistently in either Spearman/Pearson correlation or an accuracy score with 0/1 quantization of the annotations. We adopt 0/1-quantization and report the accuracy of each baseline/model.” → This is not at all clear. It would be good to clarify this.


Minor: 

Section 4.2.2: Table 6 -> Table 5

sum_log m -> sum_m in Section 3.4.2.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a reference-free evaluation metric for open-ended text generation. It exploits the properties between small amateur and large expert models; in the paper T5 of varying sizes is used. Results are compelling on multiple datasets, both for dialogue and summarization; summarization measures factual consistency between the input and output. The paper is most lacking in analysis to further convince the reader the metric is capturing the desired properties.

### Strengths
1a. The method is clever, effective, and mostly straightforward. It exploits contrastive properties of small amateur models and large expert models. Perhaps others can build upon the contrastive nature of this setup for improved or other types of evaluation.

1b. It is actually two methods, and the classifier-based discriminative method seems particularly effective.

2. Promising results on multiple datasets, correlating outputs with human preferences. Including results on factual consistency.

3. Includes ablation study on model sizes and other settings.

### Weaknesses
1. Performance seems especially bound by the expert model. This is not always the case for reference-free evaluation. Perhaps it is worth analyzing the cases where the metric fails, specifically looking at the types of errors the metric makes when the expert model is either very strong or surprisingly weak on a given input.

2. Although main results on multiple tasks are promising, the paper lacks analysis (qualitative or quantitative) to convince the reader CDM is capturing desirable properties of the outputs. For example, it would be useful to see examples of outputs that CDM rates highly and poorly, and analyze what properties of the text are being captured by the metric. It's unclear if the metric is capturing fluency, coherence, or other aspects of text quality.

3. Negatives in generative CDM are created at the segment level. My impression is this would lead to grammatically similar but semantically different negatives. Stronger negatives would likely differ in style and structural complexity. Even basic ordering differences, such as swapping "A is a B" with "B is a A" are not likely to be handled. This is especially concerning for tasks that require more complex reasoning or where subtle changes in wording can drastically alter the meaning.

4. The metric is evaluated solely against human preferences. It would be helpful to see if the metric can properly order a set of baseline models by their relative strength. Although it's possible I may have misunderstood if this is already being done or not.

### Questions
Q1: Is it really a safe assumption that small is worse than large? Aren't larger models also harder to train? I understand in practice your choice of T5 probably does obey this pattern, but naively scaling a model up or down and keeping most of the hyperparams fixed may not follow this pattern.

Q2: Can we do paraphrasing instead of segment replacement?

Q3: Did you consider using multiple seeds of amateur/expert? Do you expect it to influence results?

Q4: Have you considered using multiple contrastive evaluations combined? For instance, could train particularly biased amateur. For inspiration, see "He He et al. Unlearn Dataset Bias in Natural Language Inference by Fitting the Residual"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new framework, Contrastive Distribution Methods (CDM), for evaluating open-domain text generation. CDM is based on the assumption that larger model tends to have better open-domain generation performance than smaller ones, and is done by mapping the contrasts of two probability distributions to a quality measure. The authors explored two paradigms of CDM: Generative CDM, which generates synthetic examples for training a classifier, and Discriminative CDM, which uses the contrast between two distributions for direct evaluation. Experimental results show that CDM improves correlation with human judgments in multi-turn dialogue evaluation and factuality evaluation for abstractive summarization.

### Strengths
- The research problem (open-ended text evaluation) is important for current NLP community.
- The experiment results look promising. 
- The proposed method can fit in both the generative and discriminative paradigms explored in the past years.

### Weaknesses
 - The experiments were only conducted on T5 models, which raise the question of how well the decoder-only models perform with CDM.
- The proposed method relies heavily on the divergence between two distributions for quality prediction and it seems (1) picking the right amateur model may require extra effort, and (2) whether the method generalizes to larger model scales (e.g., >7b) is unknown. As noted by the authors, “Note that the smallest configurations… such as LLaMa-1/2(Touvron et al., 2023a;b), can still be too strong to serve as the amateur model in CDM”

### Questions
- Have you tried switching both amateur and expert models to larger scales? Will contrasting 7B and 70B output distribution yield good correlation with humans?
- Have you tried any decoder-only language models?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel method, called "contrastive distribution methods (CDM)," for assessing open-domain text generation. CDM offers two distinct evaluation metrics. First, the generative CDM focuses on the creation of negative samples for training a classifier. Second, the discriminative CDM emphasizes calculating the probability of sequence generation using a contrastive approach. Experimental results demonstrate the effectiveness of both the generative and discriminative CDM when comparing to several baseline methods.

### Strengths
**Clarity**: The paper is well written and easy to follow. It begins by outlining the assumption made (i.e., larger models perform better than smaller models at generation tasks), followed by a detailed explanation of the two CDM methods derived from the assumption. The experimental sections are clearly presented, offering comprehensive details and ablation studies.

**Originality**: The paper is original in the sense that it applies the contrastive decoding idea into developing both generative CDM and discriminative CDM.

**Substance**: Comprehensive ablation studies are carried out in the paper. These studies effectively determine the optimal strategies for constructing negative samples in the generative CDM and for aggregating in the discriminative CDM.

### Weaknesses
 **Soundness**: 
The paper appears to overlook crucial baselines. Specifically:
- For the generative CDM, there's no direct comparison with the expert/amateur model employed solely for constructing negative samples. This is a critical omission because it's unclear whether the performance gains are due to the contrastive method itself or simply the use of a stronger model for generating negatives. A direct comparison is needed to isolate the effect of the contrastive approach.
- For the discriminative CDM, a direct comparison is missing where the expert model is used to compute the generation score. This baseline is necessary to determine if the contrastive approach offers any advantage over simply using the expert model's probability as a generation score. Without this, the claim of the method's effectiveness is not fully substantiated.

These baselines are essential for establishing the paper's originality (applying the contrastive decoding idea into text generation evaluation) and shouldn't be omitted.

**Limitations**: 
The paper acknowledges some limitations in Appendix A.3. Additionally, I'm concerned regarding the method's applicability in two trends of open-domain generation evaluation:
   - **Fine-grained Evaluation**:  This is the case where users arbitrarily set the evaluation perspective. It's unclear if the negative sample creation strategy can consistently control construction towards a specific aspect. For instance, if the goal is to evaluate for factual correctness, can the negative samples be reliably generated to specifically target factual errors, or will they introduce other types of errors that confound the evaluation? The lack of control over the type of negative samples generated is a significant limitation.
   - **Holistic Evaluation**: This involves comparing generated outputs to a given input and assigning ranks. Given that the paper mentions that state-of-the-art Language Models like LLAMA-1/2 7b are too strong to act as amateur models, it suggests the approach is best suited for weaker models. This raises the question: can it effectively evaluate outputs from more advanced models? This potential constraint could limit its applicability. The paper needs to address how the method scales to evaluate outputs from models that are significantly stronger than the 'amateur' models used for negative sample generation.

### Questions
See the limitations in weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
