# In-Context Learning at Representation Level via Unlabeled Texts

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Large language models (LLMs) have exhibited impressive capability of In-Context
Learning (ICL), where LLMs perform relatively complicated tasks beyond the
pre-training objective by conditioning on the given demonstrations. Nevertheless,
ICL introduces two gaps between pre-training and inference: label appearance
(presence of inserted labels in the demonstrations) and weak semantic relevance
(independently sampled demonstrations exhibit less semantic coherence compared
to consecutive text segments in pretraining corpora). We propose a new inference
method that only use unlabeled inputs from the test set and label space. In this
method, we extract the representations of the demonstrations inputs independently
and fuse them to reshape the representation of the test input for inference. Inter-
estingly, without access to labels, our method outperforms traditional ICL with
extra information of gold labels. Furthermore, our method allows small models
to outperform the zero-shot performance of models that are twice their size (e.g.,
GPT-Neo-2.7B surpasses Llama2-7B, and Llama2-7B outperforms Llama2-13B).
Our code will be available at this.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel in-context learning (ICL) method at the representation level, leveraging (unlabeled) sentences from the test set.

The proposed method is motivated by two existing gaps between pre-training and ICL:
1. **Label appearance**: During pre-training, the text lacks task-specific signals, while in ICL, the input-label mapping introduces explicit task information.
2. **Weak semantic relevance**: Text used in pre-training tends to be more coherent, whereas ICL demonstrations are often relatively unrelated to each other.

To address these issues, the proposed approach builds on **unlabeled ICL**. 
Specifically, representations of different test sentences are first pre-computed using an LLM.
The new test input is then encoded with the same model, and this representation is used as a query in the attention mechanism, with $k$ relevant representations from the previous stage functioning as keys and values. 
Finally, the attention mechanism’s output vectors for the $k$ different samples are averaged and combined with the original test input feature vector. 
This final vector serves as input for the target language model’s lm_head, where the likelihood of each option is computed, and the option with the highest likelihood is selected as the final answer.

In the experiments, the proposed method is compared with zero-shot and few-shot ICL. Results indicate that it generally outperforms zero-shot and is comparable to other demonstration selection-based few-shot baselines.

### Strengths
- The proposed method does not rely on label information from demonstrations, making it applicable in cases where only relevant context is available without gold-standard labels.
- Interestingly, the proposed method can be interpreted as representing the vector of the target input within the space spanned by vectors of other samples.
- An analysis was conducted to examine the inner workings of ICL from the authors’ own perspectives, providing insights into the paradigm.

### Weaknesses
 - While assumptions like label appearance and weak semantic relevance are intriguing, I am somewhat doubtful, especially regarding weak semantic relevance. In pre-training, language models are exposed to a substantial variety of cases, some of which might closely resemble in-context learning scenarios. For instance, if multi-choice QA datasets were included in pre-training, the answer choices could introduce sequences that appear relatively unrelated. Thus, it may not be easy to guarantee that LMs are unfamiliar with inputs seen in in-context learning scenarios.
- I’m also unsure whether comparison with only zero-shot ICL is entirely fair. Although the proposed method does not utilize label information from the test set, it does use textual information from it. Could we add more reliable baselines, such as performing few-shot ICL with random labels (distinct from a random few-shot retrieval-based baseline) or using self-generated labels? Specifically, a comparison with few-shot ICL using randomly selected *unrelated* sentences from the training set, rather than random labels, would be a more rigorous test of the method's ability to leverage relevant context. This would help isolate the impact of the proposed method from the simple presence of any textual context.
- Equation 11 seems somewhat arbitrary, with no explanation provided for why those specific hyperparameters (e.g., 0.4 and 0.6) are applied in the weighted sum. Could you elaborate on this process? The lack of a principled approach to setting these weights raises concerns about the robustness and generalizability of the method. It's unclear if these values were chosen through a systematic search or based on intuition, and how sensitive the method's performance is to these specific values.
- It would be helpful if the paper included an analysis of the proposed method’s efficiency. While accuracy is critical for evaluating performance, the method’s efficiency is also a key factor in understanding its practical implications. The current analysis lacks a detailed breakdown of computational costs, including the time required for pre-computing representations, the overhead of the attention mechanism, and the memory footprint of storing these representations. A comparison with the computational cost of traditional ICL would be beneficial.

### Questions
- I am curious why sentences from the test set are used to construct representations for the method’s computation. What would happen if we relied on sentences from the training set instead? Although the proposed method does not rely on label information from the test set, avoiding the use of any hints or information extractable from the test set, if possible, would help ensure a fair evaluation.

### Soundness
2

### Presentation
2

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
This work proposes a new in-context learning paradigm. It is mainly motivated by the identified issue of weak semantic relevance in traditional ICL: ICL demonstrations exhibit weaker semantic dependence than the pretraining corpora. Therefore, the authors propose to process ICL examples independently for better coherence within each example. It then use the attention mechanism to integrate these independent representations of examples into the test input's representation. In addition, this method does not require labels for ICL examples. Experiments are conducted on four LLMs and eight datasets.

### Strengths
- This work highlights a discrepancy  between ICL and LLM pretraining - unlike coherent text used in pretraining, ICL demonstrations exhibit weaker semantic dependence
- The proposed paradigm of conducting ICL at the representation level is new.

### Weaknesses
 - The first concern is the absence of empirical evidence to support the theoretical claims about the weak semantic relevance's impact on ICL performance. Without quantitative evaluation, it is unknown whether the impact of this discrepancy is significant, making the main motivation of this work not well-supported. Additional experiments could be conducted to compare conventional ICL demonstrations with modified ones that include semantically coherent transitions.
- The proposed ICL paradigm simplifies the interaction between examples and the test input into a single step, potentially losing vital information that could be obtained in multi-layer interactions of conventional ICL.
- The proposed method is likely to increase computational and storage demands in computing independent representations of each example and reconstructing the representation of the test sample. However, there is a lack of analysis on the efficiency of the proposed method.
- There is a lack of experimental details. For example, the prompts used in Section 2 and the main experiments are not provided, and the methodology for selecting hyperparameters in Equation 11 is not introduced, and the references of the baselines used in the main experiment are missing.
- Some discrepancies in ICL performance of baselines are observed between this paper and the literature. For example, the 16-shot ICL performance using random examples for Llama2-7B on SST-2, RTE, and CoLA is reported as 93.16, 77.02, and 70.20, respectively in [1], which is 20-30 points higher than that reported in this study.

### Questions
- Why does the proposed method achieve the same accuracy across four different LLMs on MRPC and CoLA datasets?
- Why there is a decrease in performance when upgrading from Llama2-7B to Llama2-13B on SST-2 and Phrase datasets using the proposed method?

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
2

### Summary
This paper proposes a new representation-based in-context learning (ICL) paradigm, which utilizes unlabeled text in the test set for learning, without relying on annotated examples. The authors find that the presence of labels has a greater positive impact than negative impact on domain-specific datasets, but the opposite is true for general-domain datasets. Furthermore, the authors' proposed method performs inference by independently processing the representation of the example input, which is superior to the traditional ICL based on annotated examples, and allows smaller models to outperform larger models in zero-shot performance.

### Strengths
It proposes a new representation-based in-context learning (ICL) paradigm that utilizes the unlabeled text in the test set for learning, without relying on annotated examples.

It finds that the presence of labels has a greater positive impact than negative impact on specific domain datasets, but the opposite is true for general domain datasets.

The proposed method performs reasoning by independently processing the representations of the example inputs, which is superior to the traditional ICL based on annotated examples, and allows smaller models to outperform larger models in zero-shot performance.

### Weaknesses
- The paper requires some additional comparation to some in-context vector methods like [1][2], which also create a hidden state offset by in-context example.

- Required some additional ablation study to prove why use the unlabeled texts from test set rather than labelled.For example, if you use labelled data in your framework in Figure 2, how will the performance be?

- The improvement form increasing numbers of the retrieved hidden states is limited.

### Questions
- The link of the codes is invalid.

- Besides MRPC, the difference between labelled and unlabelled data for ICL is limited. Is there any more dataset can be used for prove the conclusion about un-labelled ICL in General-Domain.

- Could you share the prompts or give some analysis about the effect of the prompt use to get the presentation of the in-context examples?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper firstly proposes two gaps between current ICL paradigm and pre-training, label appearance and weak semantic relevance. Sometimes ICL benefits from the gap but sometimes it does not. Then it conducts corresponding experiments and observe different conclusions on specific-domain and general domain datasets, based on which it proposes its method -- fusing unlabeled samples to reshape the representation of the test input for inference. This method outperforms traditional ICL on models of varying sizes.

### Strengths
* This paper is well-written. The motivation demonstrated by preliminary experiments is very clear. 
* By viewing specific and general domain datasets separately, the observation is interesting.
* The experimental results show the method is effective.

### Weaknesses
* Though this method performs well on some NLU tasks, I'm curious about other diverse tasks like generation, reasoning and more difficult tasks in LLM era, since ICL can be used in many scenarios. 
* I'm curious that whether getting hidden states bring extra time cost, compared with top-k example selection in traditional ICL.
* The performance on specific domain datasets is sometimes worse than the baseline. (maybe trying whether to use gold labels can be further explored)

### Questions
* More analysis on time cost and latency brought by this method can be investigated.
* What about the performance on other diverse tasks in LLM era, like reasoning, etc.

### Soundness
3

### Presentation
3

### Contribution
3
