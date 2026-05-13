# The Cost of Scaling Down Large Language Models: Reducing Model Size Affects Memory before In-context Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We study how down-scaling large language model (LLM) size impacts LLM capabilities. We begin by measuring the effects of weight pruning – a popular technique for reducing model size – on the two abilities of LLMs: (a) recalling facts presented during pre-training and (b) processing information presented in context. Surprisingly, we find that existing pruning techniques affect these two abilities of LLMs differently. For example, pruning more than 30% of weights significantly decreases an LLM’s ability to recall facts presented during pre-training. Yet pruning 60-70% of weights largely preserves an LLM’s ability to process information in-context, ranging from retrieving answers based on information presented in context to learning parameterized functions such as a linear classifier based on a few examples. Moderate pruning impairs LLM’s ability to recall facts learnt from pre-training. However, its effect on model’s ability to process information presented in context is much less pronounced. The said disparate effects similarly arise when replacing the original model with a smaller dense one with reduced width and depth. This similarity suggests that model size reduction in general underpins the said disparity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study the effects of weight pruning, a popular technique for reducing model size, on the two core capabilities of LLMs: (a) recalling facts presented during pre-training and (b) processing information presented in context. They find that existing pruning techniques affect these two abilities of LLMs quite differently. The paper presents a detailed analysis of the experimental results, which show that the effects of down-scaling LLMs depend on the specific pruning technique used. The authors conclude that there is a trade-off between model size and performance, and that the optimal model size depends on the specific task and dataset.

### Strengths
- The paper investigates the impact of down-scaling large language models on their capabilities, which is an important topic in the field of natural language processing. 
- The authors provide a detailed analysis of the experimental results, which can help researchers and practitioners better understand the trade-offs between model size and performance. 
- The paper provides insights into the development of more efficient language models, which are becoming increasingly important for a wide range of natural language processing tasks.

### Weaknesses
 - The paper is empirical in nature, and the authors acknowledge that their observations may not generalize to the full spectrum of tasks and large language models. 
- The study focuses on evaluating two pruning algorithms that are unstructured pruning, evaluation on structured pruning methods are expected. 
- The study could include other types of tasks, like NLI, classification, summarization, to make the study more solid.

### Questions
How the structured pruning methods, e.g., LLM-Pruner, performs on these two LLM capabilities?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Pruning parameters from large language models can affect aspects of model performance differently. The authors strive to characterize these effects by separating fact recall from in context learning. They explore the relative impact of pruning on several different tasks using several base models and multiple pruning techniques. Overall they find that even moderate pruning can degrade fact recall settings, here in-context learning seems more robust.

### Strengths
The settings for evaluating fact recall and in context learning seem useful in general.

Multiple settings for pruning to push for more robust result interpretations

Multiple model families were used in evaluation.

A range of tasks were presented.

### Weaknesses
Fact Recall and In Context Learning are some reasonable aspects, but the authors could have considered more. Detailed Instruction Following, and Heavy Reasoning feel like other key aspects, as well as the ability to learn from Few Shot inline. I would have loved to see some more details.

Are all In Context Learning tasks equally difficult? Could a few more gradations be helpful here?

Are there a few more settings that one could use for evaluating model performance? The set of tasks seems rather small.

I'm assuming that pruning is primarily used to increase inference speed, right? If that's the case, I'd like to see tradeoffs between accuracy and inference speed be presented here.

It seems that Dense Pruning of 30B -> ~13B underperforms the unpruned 13B param model, right? I'd love to see more discussion here about what is going on there.

### Questions
It seems that Dense Pruning of 30B -> ~13B underperforms the unpruned 13B param model, right? I'd love to see more discussion here about what is going on there.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Edit - the authors have addressed concerns within my review and also contrasted the novelty of their work with previous pruning/ICL studies.  I'm increasing my score accordingly.

Continuing off recently proposed LLM pruning methods (i.e., SparseGPT and Wanda), the authors explore the effect of LLM pruning on both parametric knowledge (i.e., knowledge memorized by the model) and knowledge learned via ICL.  Towards this end, the authors explore the effect of pruning for pretrained OPT-13B/30B and LLamA-13B/33B models.  The authors main contributions are experiments evaluating the pruned-sparsity levels of the aforementioned models versus (a) parametric knowledge and (b) ICL knowledge, as measured via several Q&A tests; parametric knowledge is measured using a closed-book Q&A test, while ICL knowledge is measured using an open-book Q&A test where the in-context prompt is contains a counter-factual answer compared to the training data.  Furthermore, the authors also test ICL knowledge by providing in-context information detailing parametric functions and measure the models predictive accuracy in this case.

### Strengths
The topic is important and interesting and, at a high-level, the experimental design make sense.  Furthermore, as LLM parameter sizes continue to grow, the question of how new pruning methods (i.e., LLM-Pruner, SparseGPT, and Wanda) affect a model's parametric and ICL knowledge is important.  However, more care is required to ensure model performance is accurately being measured.

### Weaknesses
 # Evaluation
The major weakness of the paper is the effective testing of LLM parametric and ICL knowledge.  In particular, how do the authors verify that the in-context evidence contradicts a fact present in training data?  Although LLama was trained on
publicly available data, it is not a simple matter to verify that the answers in the Q&A datasets align or misalign with the massive dataset used to train LLamA (note that, the dataset itself was never released, so all public datasets would have to be evaluated in their entirety for verification).  In this case, it is not clear how Verifying that "answers do not exist in the pre-training corpus" is possible.  While the authors discuss previous work which has explored LLMs' abilities to override in-memory/parametric knowledge, such works set up measurement guardrails to do so through fine-tuning, e.g.:
- "DissentQA. Neeman et al. (2022) constructed the DissentQA dataset from the NaturalQuestions dataset. It contains pairs of
questions and evidence for a made-up answer that is different from the factual one. It assesses
whether the model can override its memory formed during pre-training with new context."
"Given that the anticipated made-up answers are randomized and
different from the factual ones, the model cannot depend on memorization from its pre-training
data to generate responses. This evaluation framework rigorously assesses the model’s ability to
override its pre-training data with new, context-specific information." <- Neeman et al. (2022) fine-tune their evaluated T5 models, thus ensuring that the parameterized answers are learned and relevant questions and answers are actually counter-factual (relatedly, gold passages are considered in Longpre et al. (2021)). This work does not fine-tune the evaluated LLMs, thus relating to the earlier criticism on the validity of the presented results.

Furthermore, the exact measurement of accuracy used in the paper is potentially incorrect and too conservative for recently release instruction-tuned LLMs like LLaMA and OPT.  From the text:
- "Answers are the model’s prompt completions produced by greedy decoding. We report the
percentage of answers that exactly match ground truth." <- Two important remarks: greedy is known to be extremely suboptimal for recent
instruction-tuned LLMs, and an exact match is not necessarily a fair metric.  Such chat models are known to be extremely wordy, so if the model produces some lead up text followed by the correct answer, this metric discounts such a correct response.  For the former, it makes sense as a fair, reproducible benchmark across different sparsity percentages per model (e.g., nucleus sampling would produce differing results between runs), please include in the text why greedy is used.  However, note that the latter is an extremely important problem which biases all related results.

# Claims
Several claims require revision or further discussion.  In general, wrt to key contributions, it is necessary to discuss how the presented methodology differs from previous work.  E.g., the SparseGPT paper itself reports zero-shot performance for different datasets at different sparsity levels (which effectively tests parametric knowledge), how does the presented benchmark differ from this?  Why does the presented work differ in conclusions wrt parametric knowledge compared to the SparseGPT paper, i.e., SparseGPT showed high sparsity while retraining zero-shot performance.  Why is this not the case in the presented work?  These types of questions, and their ensuing answers/justifications, require significant discussion.  More examples from the paper:
- "From work on image classification, however, we know that down-scaling neural networks affects more than just top-line metrics or task accuracy. Pruning, for example, can introduce biases (Hooker et al., 2019) or disproportionate affects on certain subsets of the data (Jin et al., 2022)." <- This claim is too strong, it makes it seem as though it is a certainty that such effects occur given down-scaling.  However, a significant amount of work has shown that pruning is an effective tool for vision models.
- "It is difficult to assess these abilities in isolation, as a standard downstream task needs to process the
information provided in context as well as access the information stored in weights." <- Please contrast related work which has previously explored zero-to-many shot ICL performance (across different target applications); see the following for an extensive overview:
Dong et al, "A Survey on In-context Learning", https://arxiv.org/pdf/2301.00234.pdf
- "Improve inference efficiency. Our work reveals that scaling down model size alone has little impact
on tasks demanding processing information in the LLM’s context. Practitioners may thus use our
findings to identify scenarios where decisions could be routed to a smaller model instead of a larger
one without hurting task performance (Chen et al., 2023; Dohan et al., 2022)." <- The latter work already explores how the parameter size affects performance.  In particular, the Wanda paper already tackles the question of how pruning affects ICL performance (and compares to SparseGPT)
- "Our work differs from prior scaling studies in two ways: while prior work (Kaplan et al., 2020b) studies
joint scaling of both pre-training corpus size and model size, we focus on scaling model size alone.
Furthermore, instead of measuring task performance, we focus on foundational capabilities of LLMs–fact recall and ICL. These capabilities drive the success for many real world applications of LLMs" <- This is wrong for a number of reasons.  Firstly, "we focus on scaling model size along" is not a valid contribution, as this would, by definition, be provided in the study of "joint scaling of both pre-training corpus size and model size."  Secondly, the work of Kaplan does not study pruning, but rather LLM model size->training->resulting performance.  It is necessary to demarcate the difference between these two paradigms.
-"In-weight versus in-context learning" <- Please explain how the considered work differs from Longpre et al 2022, which extensively explores In-weight versus in-context learning.
- "the versatility of LLMs calls for a different approach to assessing pruned models. Our work begins to fill this gap, proposing to evaluate pruning’s effect on fact recall and ICL." <- As previously mentioned, what the authors define as fact recall is equivalent to the task of zero-shot question answering; the effect of pruning on various tasks has been explored, e.g., within the papers of the pruners specifically used within this work (SparseGPT and Wanda), as well as in the LLM-Pruner paper.  Furthermore, the effect of pruning an LLM to various sparsity levels on ICL was extensively explored in the Wanda paper.  Please revise your contributions, and position them within the context of previous works.
-" In all the above settings, as a simple point of comparison, we measure the effect of downscaling on perplexity" <- Please note in the paper that this was previously considered in both the SparseGPT and Wanda papers.
-"  we focus on foundational capabilities of LLMs – fact recall and ICL" <- Fact recall is zero-shot Q&A, which may be thought of as a specific task.  Please adjust this claim.

# Presentation
Overall, the writing and presentation of the discussed work could be significantly improved.  E.g.:
- "removing more than 30% of weights leads to significant (> 5%, relative) accuracy degradation on fact recall related tasks (Figure 1, left). Fact recall suffers similarly from dense down-scaling." <- Please have some text which segways from the first paragraph (page 2) to the list of 3 bold-faced items.  The intro currently reads like a collection of text/paragraphs which do not blend into one another.  E.g., combine all the bold-faced-starting paragraph in page 2 into a single paragraph, which: -States the paper shows the following dichotomy wrt pruning LLMs.  For fact recall/parametricknowldge, minimal pruning significantly degrades performance.  [insert your bold-faced-starting text here] In stark contrast, large-scale  pruning does not significantly degrade ICL performance. [insert your second bold-faced-starting text here]. [insert your third bold-faced-starting text here]
- Same comment for italicized-starting-text, which proceed bold-starting-text; please segway the various paragraphs together.  It is very difficult for a reader to understand the point that is trying to be made when sentences exist independently.

### Questions
-Why did the authors not consider the GINC dataset for ICL, from Xie et al's "An Explanation of In-context Learning as Implicit Bayesian Inference?"

-"From the OPT family, we evaluate the two largest models that fit in our hardware
setup" <- Please state the hardware setup

-In Table 1, please define what is meant by "Context Type"

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates the effects of pruning and down-scaling large language models (LLMs) on the model capabilities. Specifically, the authors focus on two abilities of modern LLMs: (1) the ability to process information stored in the weights (fact recall) and (2) the ability to process information that is available in context. To evaluate down-scaled models on these capabilities, they use a suite of benchmarks covering four tasks, open-book QA, closed-book QA, overriding QA, and learning tasks (i.e., model needs to understand underlying function based on examples given as in-context learning). Experiments on 6 base LLMs, each with 9 different sparsity levels demonstrate different model behavior in terms of the two capabilities. Model ability to process information in weights degrades with moderate level of pruning (>30%), while model ability to process information in context does not really degrade even with aggressive pruning (up to 70%).

### Strengths
Overall, I think the paper discusses an important question regarding the trade-offs of having smaller-scaled models and its impact to model capabilities. The experiments are well-thought, with the use of different benchmark tasks to isolate different model capabilities being tested and the use of different base LLMs to see that the effects are similar across different model families. I think the main findings of this paper will be useful for future work in this area. The paper is well-written.

### Weaknesses
 - Although down-scaling and pruning are the main topic of the paper, the technical details on methods used is very limited (even in the Appendix too). If space is an issue, I would suggest to cut down the paper motivation which is repeated multiple times throughout the paper.
- Relatedly, there is very little discussion regarding down-scaling vs. pruning. For general readers it would be helpful to understand what are the difference between the two, and is one a specific version of the other?
- For learning tasks evaluation, why only consider task with scalar values as labels? I understand this needs to be something that model can generalize through the examples, but if we focus on language capability of the model, I would expect that a natural language task is used instead.
- For ICL results, it seems the performance drops significantly (not gradually) from 70% above, do you have intuition why?
- As the paper only use some particular pruning methods, do you have any opinion on whether the same findings will hold for other pruning methods? It would be good to have a short discussion on the difference between them.

- Section 5 is hard to follow without examples, there are multiple notations without explanation, e.g. K (page 7), x, D=4, N=32, etc
- Would be good to release the version of datasets that are used for benchmarking

### Questions
- For learning tasks evaluation, why only consider task with scalar values as labels? I understand this needs to be something that model can generalize through the examples, but if we focus on language capability of the model, I would expect that a natural language task is used instead.
- For ICL results, it seems the performance drops significantly (not gradually) from 70% above, do you have intuition why?
- As the paper only use some particular pruning methods, do you have any opinion on whether the same findings will hold for other pruning methods? It would be good to have a short discussion on the difference between them.

**Things to improve the paper**
- Section 5 is hard to follow without examples, there are multiple notations without explanation, e.g. K (page 7), x, D=4, N=32, etc
- Would be good to release the version of datasets that are used for benchmarking

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
