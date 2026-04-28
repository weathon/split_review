# How Can Language Models Learn from Mistakes on Grade-School Math Problems

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6

## Abstract
Language models have demonstrated remarkable performance in solving reasoning tasks; however, even the strongest models still occasionally make reasoning mistakes. Recently, there has been active research aimed at improving reasoning accuracy, particularly by using pretrained language models to "self-correct'' their mistakes via multi-round prompting. In this paper, we follow this line of work but focus on understanding the usefulness of incorporating ``error-correction'' data directly into the pretraining stage. This data consists of erroneous solution steps immediately followed by their corrections. Using a synthetic math dataset, we show promising results: this type of pretrain data can help language models achieve higher reasoning accuracy directly (i.e., through simple auto-regression, without multi-round prompting) compared to pretraining on the same amount of error-free data. We also delve into many details, such as (1) how this approach differs from beam search, (2) how such data can be prepared, (3) whether masking is needed on the erroneous tokens, (4) the amount of error required, (5) whether such data can be deferred to the fine-tuning stage, and many others.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper improving math reasoning in LLMs by adding error-correction data directly into pretraining, instead of using the usual multi-round prompting---that dominant self-refine approach. Using a synthetic math dataset, the authors show that training with examples of mistakes followed by corrections leads to better reasoning accuracy, even beating models trained on error-free data. The study tries to answer some interesting question: how to prepare error-correction data, is finetuning sufficient to learn self-correction or is pretraining necessary and whether how this approach compares to beam search. Although on a synthetic and a very controlled setup, the results present some fresh perspective into pretraining LLMs to do better revisions.

### Strengths
- The paper is very well written. Although the results are dense, the authors did a good job summarizing and condensing the main takeaway messages.

- The studied problem is interesting: We still don’t fully understand how to pretrain LLMs for effective reasoning from the ground up. This paper explores self-correction within the pretraining phase, a fresh perspective that hasn’t been widely explored in the literature, aside from a few works like Quiet-STaR.

- The experiments and ablations are well-designed. The authors clearly state their research questions early on and address them in a logical sequence.

### Weaknesses
My main concern with this paper is the uncertainty around whether these findings will generalize to practical LLM pretraining scenarios. I'll expand on some specific limitations below:

- The types of problems in the i-GSM dataset don’t reflect real-world reasoning tasks. Specifically, every reasoning step required here is limited to a single type of computation—finding the next node in a directed acyclic graph (DAG) and calculating its value. But what about other reasoning types where models need to compare values, handle ambiguity, or apply commonsense knowledge? Although I appreciate the focus on math reasoning, can the authors confidently assert that these results will apply to more complex, realistic reasoning tasks? For instance, how would this approach fare on tasks requiring multi-step arithmetic with varied operations, or problems that involve logical deductions based on contextual information?

- Current LLMs struggle with error detection, as the authors note in the introduction. However, their findings in L259-260 suggest that error detection can be effortlessly embedded within the model’s internal states. This may be due to the task’s synthetic nature, where the model could have learned to encode specific errors, like “skip step,” in its parameters. But this is unlikely to generalize to other errors. For example, could the model's hidden states reliably detect other error types, like incorrect calculations involving multiple digits, or errors arising from misinterpreting problem constraints? The current setup might be too simplistic to capture the nuances of real-world error detection.

- The paper’s fine-tuning experiment is limited to simple LoRA tuning. What about full fine-tuning using a fraction of the pretraining data? The authors mention (L484-485) that the cost of full fine-tuning would match pretraining with retry data, but this wouldn't hold if we fine-tune with just a fraction of the pretraining data. Would the results remain consistent in that scenario? It's unclear whether the observed benefits of pretraining with error correction would persist if a full fine-tuning approach with a smaller dataset was used, potentially allowing the model to adapt more comprehensively.

- I’d expect more discussion on inference-time algorithms and their impact on performance. If I’m following correctly, most experiments use greedy decoding or occasionally beam search. It would be insightful to understand how additional inference-time resources—like generating more tokens or applying consensus voting—might affect error correction. Result 4 (concerning model retries) is based on greedy decoding; how would this result change with sampling? Specifically, how would the retry mechanism behave under different sampling temperatures, and could a more robust inference strategy mitigate the need for extensive pretraining with error correction?

### Questions
See weaknesses above

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the impact of training language models with "error-then-retry" format data on the reasoning performance. With experiments on a synthetic GSM8k-style math reasoning datasets, the authors conclude that pretraining with such data improves reasoning accuracy than on same amount of "error-free" normal data, and LoRA fine-tuning with such data does not help.

### Strengths
1. I like how the authors approach this problem in a data-centric, rigorous way: controlled experiments on synthetic data. 
2. Experiments are solid

### Weaknesses
The paper mainly experiments with one type of error: inserting a wrong parameter that cannot be computed next. While this is easy to implement, it would be hard to simulate all kinds of errors that language models can make in real-world reasonings scenarios. This cast doubts on how the suggested approach can be deployed to train LMs on non-synthetic data. If the authors could provide some discussion on how the method can be generalized to different errors (e.g., math calculation error, context misunderstanding, ...) in a scalable and controllable way, that would be very promising.

### Questions
I would like to hear the authors' thoughts on the inference-time scaling properties of model trained with "retry" data: given a fixed inference-time computation budget, is it better for model to produce reasoning chains with retry (more tokens to reach final answer, but average accuracy is higher) or without retry (less tokens to reach final answer, but average accuracy is lower)?

### Soundness
4

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
3

### Summary
The paper aimed at improving language model accuracy in reasoning tasks (grade-school math) by pretraining with "error-correction" where errors are followed by immediate corrections, to teach models self-correction as they generate outputs. The authors show that pretraining with error-correction data boosts reasoning accuracy, without multiple rounds of prompting.

### Strengths
- The paper proposed an interesting idea by incorporating error-correction data directly in pretraining, rather than relying on post-generation prompting for correction with empirical evidence of improved performances. 
- The authors compared different experimental settings, such as “retry upon regret,” masking, and pretraining versus fine-tuning with retry data.

### Weaknesses
 - The paper has unclear justification for synthetic data choice.
- Writing and the structure of the paper is very unclear and hard to follow. For example, the experimental setting or conclusion section is not contained in the paper.
- While the paper presents extensive experimental results, the paper primarily focuses on using one model, it is unknown if such techniques are generalized to different models (e.g., LLAMA, Gemma, Mixtral etc.). The paper further lacks comparisons to existing methods.

### Questions
The paper would benefit significantly from a reorganization into a structure that aligns more closely with the familiar flow of this venue. Specifically, it would help to present the experimental settings early in the paper, followed by a dedicated focus on results and analysis. Additionally, the authors could simplify the tables to better highlight key findings, and consider using plots to present some of the results for improved clarity and reader comprehension.

### Soundness
3

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
This work focus on understanding the usefulness of “error-correction” data into the pretraining stage. The experiment results show that error-correction data can improve the mathematical ability of the model more effectively than error-free data.

### Strengths
- The experiments are well-designed and rigorously conducted.
- The finding that “even when model is pretrained on retry data with high error rate, it does not tend to produce erroneous steps” is interesting.

### Weaknesses
 - Some previous work[1] has already pointed out that error-correction data enables LLM to achieve higher reasoning accuracy compared to error-free data.
- This work only evaluates on IGSM dataset, which is a synthetic data. It would be more convincing to also experiment on realistic mathematical datasets. The current evaluation is limited to a single synthetic dataset, which raises concerns about the generalizability of the findings to real-world mathematical problems. The specific characteristics of the IGSM dataset, such as its structure and the types of errors it contains, might not be representative of the complexities and nuances found in more realistic mathematical datasets. This limitation makes it difficult to assess the practical impact of the proposed pretraining approach.


### Questions
- Will the experiment code and data be open sourced?
- In section 3.1, as the can_next is “a linear classifier on top of its hidden states”, is the one who “knowing can_next(A)=false” actually the linear classifier rather than the model itself? Does the author mean that because the hidden states of the model show a distribution that can be accurately predicted by the classifier, the model "knowing can_next(A)=false"?
- It would be appreciated if the authors provide some insights about why “the slightly more complex retry miss data does not improve accuracy by much”

### Soundness
4

### Presentation
3

### Contribution
3
