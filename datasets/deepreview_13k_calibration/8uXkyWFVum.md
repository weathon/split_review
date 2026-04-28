# Amuro and Char: Analyzing the Relationship between Pre-Training and Fine-Tuning of Large Language Models

- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 3, 5, 5, 3

## Abstract
The development of large language models leads to the formation of a pre-train-then-align paradigm, in which the model is typically pre-trained on a large text corpus and undergoes a tuning stage to align the model with human preference or downstream tasks.
In this work, we investigate the relationship between pre-training and fine-tuning by fine-tuning multiple intermediate pre-trained model checkpoints. Our results on 18 datasets suggest that i) continual pre-training improves the model in a latent way that unveils after fine-tuning; ii) with extra fine-tuning, the datasets that the model does not demonstrate capability gain much more than those that the model performs well during the pre-training stage; iii) although model benefits significantly through supervised fine-tuning, it may forget previously known domain knowledge and the tasks that are not seen during fine-tuning; iv) the model resembles high sensitivity to evaluation prompts after supervised fine-tuning, but this sensitivity can be alleviated by more pre-training.
\footnote{Code, results, and data to reproduce the experiments are available at \href{https://anonymous.4open.science/r/AmuroCharRelease-DEC5}{https://anonymous.4open.science\\/r/AmuroCharRelease-DEC5}. All the model checkpoints resulting from this work are available at \href{https://huggingface.co/KaiserWhoLearns/PTvsSFT_OLMo1b}{https://huggingface.co/KaiserWhoLearns/PTvsSFT\_OLMo1b}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the relationship between pre-training and fine-tuning in large language models by fine-tuning multiple intermediate pre-trained model checkpoints. The authors aim to understand how models develop during pre-training and how this affects their performance after fine-tuning on downstream tasks. The main contributions include empirical findings that continual pre-training improves models in ways only revealed after fine-tuning, that fine-tuning benefits tasks not learned during pre-training, that fine-tuning can cause forgetting of previously known tasks, and that prompt sensitivity after fine-tuning can be mitigated with more pre-training.

### Strengths
1. The paper addresses an under-explored area by empirically studying the interplay between pre-training and fine-tuning stages in language model development.
2. It provides valuable insights that can inform more efficient training strategies, such as early stopping in pre-training when fine-tuning yields better results.
3. The study is thorough, involving experiments on 18 datasets across various tasks, enhancing the validity of the conclusions.

### Weaknesses
1. The study focuses on a single, relatively small model (OLMo-1B), which may limit the applicability of the findings to larger models or different architectures. Specifically, the model's 1 billion parameters may not capture the complex dynamics of larger models with tens or hundreds of billions of parameters, where emergent behaviors and scaling laws might significantly alter the observed relationships between pre-training and fine-tuning. The conclusions drawn from this model may not generalize well to models with different architectural choices, such as those employing different attention mechanisms or normalization techniques.
2. Due to the scarcity of models with available pre-training checkpoints, the conclusions are based on limited data, potentially affecting the robustness of the results. The lack of diverse checkpoints from various models makes it difficult to ascertain whether the observed phenomena are model-specific or more general. This limitation introduces a potential bias, as the findings might be skewed by the particular characteristics of the chosen model and its pre-training process.
3. The paper primarily analyzes downstream performance without deep exploration of model internals or theoretical underpinnings of the observed phenomena. The study does not delve into the representational changes within the model during pre-training and fine-tuning, which could provide a more mechanistic understanding of the observed performance changes. Without examining the internal states and activations, it's challenging to pinpoint the exact reasons behind the observed behaviors. Furthermore, the lack of theoretical grounding makes it difficult to predict how these findings might generalize to other scenarios.
4. The benchmark datasets (flan-style) seem too simple and out of date for modern LLMs. For example, MT-bench, alpaca-eval, and arena-hard. The datasets used for evaluation, being relatively simple, might not fully capture the capabilities of modern LLMs, particularly in complex reasoning or instruction-following tasks. The use of more challenging benchmarks, such as MT-bench, alpaca-eval, and arena-hard, could provide a more comprehensive assessment of the models' performance and reveal potential limitations not apparent with the current datasets.

### Questions
1. Could you provide more details on the selection criteria for the datasets and how they might influence the observed dichotomy between tasks learned during pre-training and those requiring fine-tuning?
2. How do you anticipate your findings would generalize to larger models or different architectures, given that your study was conducted on a relatively small model?
3. Can you elaborate on potential signals or metrics during pre-training that could indicate an optimal point to stop pre-training and begin fine-tuning?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the dynamics of capability acquisition in large language models (LLMs) and provides emprical analyses that reveal the contribution of the pre-training and fine-tuning stages to downstream capabilities. Multiple intermediate pre-training checkpoints were fine-tuned and evaluated, leading to four main findings:
1）the pre-training stage can enhance the performance of the fine-tuned model, even when such improvements are not apparent in the pre-trained model itself;
2）fine-tuning is more beneficial for tasks that have not been learned during the pre-training stage;
3）a model fine-tuned for specific tasks may forget knowledge and capabilities in other domains;
4）fine-tuned models show high sensitivity to evaluation prompts, but this sensitivity can be alleviated by more pre-training.

### Strengths
This paper analyze the downstream performance of intermediate pre-training checkpoints and the corresponding fine-tuned models, and draws some insights that can help in developing more efficient and effective LLMs.

### Weaknesses
1) The experiment employed only a single base model, which limits the generalization of the empirical findings. In addition to the five candidate models mentioned by the authors, Baichuan2-7B may also be considered a candidate that has released intermediate checkpoints. https://huggingface.co/baichuan-inc/Baichuan2-7B-Intermediate-Checkpoints
2) The parameters of the base model used in this paper amount to 1 billion, which does not include widely used model sizes of LLMs, such as 7 billiion.
3) The num of tasks for supervised fine-tuning is relatively limited, with only 4 tasks, including summary generation, question generation, natural language inference and paraphrase detection. This limits the generalization of the results.
4) The conclusions derived from the empirical analysis largely align with the established perspectives within this field, providing limited novelty.
5) There are no promising experiments demonstrating how these findings can inform the developing of LLMs.

### Questions
none

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
This work analyzes the relationship between Pre-Training and Fine-Tuning of Large Language Models. The authors conduct experiments on multiple intermediate pre-trained checkpoints to analyze how models develop as they train. Through experimental results, they find i) continual pretraining improves the model in a latent way that manifests after fine-tuning; ii) fine-tuning most benefits datasets where the model does not show capability during pre-training; iii) although the model benefits significantly through supervised fine-tuning, it may forget previously known domain knowledge and tasks not seen during fine-tuning; iv) the model exhibits high sensitivity to evaluation prompts after supervised fine-tuning, but this sensitivity can be alleviated through more pre-training

### Strengths
(1)	This work explores an interesting topic in LLMs by investigate the relationship between pre-training and fine-tuning.

(2)	The authors conduct some experiments provide some observations in LLM training.

### Weaknesses
(1)	There are some observations that are relatively easy to obtain (e.g., although the model benefits significantly through supervised finetuning, it may forget previously known domain knowledge and tasks not seen
during fine-tuning), which have limited impact on the literature.

(2)	The authors should provide a related work section to summarize the difference between this work and previous related studies.

(3)	The model backbone selected in this work is limited (only OLMo model). Have you tried other open-source models (e.g., OpenELM).

### Questions
see Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigate the relationship between pre-training and fine-tuning by fine-tuning multiple intermediate pre-trained model checkpoints to understand how models develop as they train. The authors conduct experiments on 18 datasets and give following insights into LLM training based on the result: 
(1) continued pretraining can improve a model in ways that are only revealed after fine-tuning;
(2) tasks for which the model already performs well during pre-training benefit much less from fine-tuning than those where the model does not demonstrate capabilities;
(3) although supervised fine-tuning can improve performance on in-distribution tasks, it can also cause the model to forget domain knowledge or tasks that it was previously capable of solving;
(4) fine-tuned models show high sensitivity to evaluation prompts, but this sensitivity can be alleviated by more pre-training.

### Strengths
**(1) The problem that this paper seeks to respond is important and valuable.** E.g., How do pretraining and fine-tuning interact to produce the resulting model? Does more pre-training hinder better fine-tuning results? What does the model learn and forget during pre-training and fine-tuning? These questions are straightforward and valuable.

**(2) This paper is well written.** The author clearly clarifies the problem that each part tries to address, making it easy to understand.

**(3) The author clearly states the limitations of their work.** It is always good to see the authors states the limitations as it makes the paper more rigorous.

### Weaknesses
 **(1) The experiments are insufficient.** To explore the relationship between pretraining and fine-tuning, it is necessary to ensure the generalizability of the conclusions. Verifying only one language model (OLMo-1B) is insufficient to provide convincing conclusions. I believe the author needs to validate their conclusions on more LLMs.

**(2) Some of the conclusions are not rigorous.** e.g. line 300-303, the authors state that "some tasks can be learned during pre-training, while others are not." This may be because the pretraining data possibly includes data from similar types of tasks (not necessarily contamination), whereas tasks that cannot be learned during pretraining (such as MNLI, XSum, and BoolQ) do not have such similar task data included in their pretraining datasets. In such case, the conclusion become completely meaningless. I suggest the author carefully examine the types of tasks included in the pretraining dataset before drawing conclusions.

**(3) Some insights are uninspired with limited practical guidance value.** E.g., the authors suggest that early stopping in pre-training and starting fine-tuning is an efficient way of utilizing the resource when the downstream datasets are never picked up by the model during pre-training. However, the practical issue is that if we want to train a specialized model, we should directly choose a well-pretrained model. We typically don't aim to start from the pretraining phase again. The primary purpose of pretraining is to equip the model with stronger foundational capabilities, providing a solid base for better specialization through further SFT.

### Questions
See weaknesses.

typos:
line 299: pre-trining->pre-training

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper explores the relationship between fine-tuning and pre-training LLMs through fine-tuning multiple pre-training checkpoints of large language models.

There are some findings based on experimental results:
- The pre-trained model may excel at some tasks without fine-tuning. 
- Continual pre-training improves the model in a latent way that is only observable after fine-tuning.
- The fine-tuned model may forget some unused abilities.
- The fine-tuned model exhibits high sensitivity to evaluation prompts, but this sensitivity can be alleviated through more pre-training

### Strengths
- Exploring the relationship between pre-training and fine-tuning is a valuable direction with significant implications for improving training efficiency and downstream task performance.
- The paper conducts a series of experimental analyses and summarizes some conclusions, which have some guiding significance for researchers who are new to the field.

### Weaknesses
 - The conclusion drawn from the paper is relatively superficial and has been discussed in many previous works or some industry consensus, which does not meet the bar of an ICLR paper.
- The paper lacks some deeper insights into analyzing the parameter changes or loss changes during the pre-training or fine-tuning stages, which would provide theoretical support for the observed experimental phenomena. Specifically, the paper does not analyze how the weight matrices change during pre-training and fine-tuning, nor does it explore the loss landscape and how it changes with different stages of training. This analysis is crucial for understanding the underlying mechanisms of the observed phenomena.
- The paper's layout is somewhat chaotic, with some figures/tables and related text not on the same page, which poses a significant obstacle to reading.

### Questions
- In Section 5, the author claims that "the benefits of fine-tuning an LLM could exceed the benefits of continued pretraining", but in Section 7, the author also claims that "pre-training can improve models in unseen ways". These two viewpoints seem contradictory.
- During the fine-tuning process, the paper conducts experiments on different specific tasks. What if it is in a general setting (such as AlpacaEval, MT-Bench), would the conclusions be different?

### Soundness
2

### Presentation
2

### Contribution
2
