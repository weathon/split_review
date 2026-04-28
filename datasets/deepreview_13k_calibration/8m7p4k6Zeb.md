# From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Recent studies have shown that Large Language Models (LLMs) struggle to accurately retrieve information and maintain reasoning capabilities when processing long-context inputs. To address these limitations, we propose a finetuning approach utilizing a carefully designed synthetic dataset comprising numerical key-value retrieval tasks. Our experiments on models like GPT-3.5 Turbo and Mistral 7B demonstrate that finetuning LLMs on this dataset significantly improves LLMs' information retrieval and reasoning capabilities in longer-context settings. We present an analysis of the finetuned models, illustrating the transfer of skills from synthetic to real task evaluations (e.g., $10.5\%$ improvement on $20$ documents MDQA at position $10$ for GPT-3.5 Turbo). We also find that finetuned LLMs' performance on general benchmarks remains almost constant while LLMs finetuned on other baseline long-context augmentation data can encourage hallucination (e.g., on TriviaQA, Mistral 7B finetuned on our synthetic data cause no performance drop while other baseline data can cause a drop that ranges from $2.33\%$ to $6.19\%$). Our study highlights the potential of finetuning on synthetic data for improving the performance of LLMs on longer-context tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work proposes a set of synthetic tasks based dictionary-based key-value retrieval and uses it extend the context lengths of Mistral-7B-0.1 and GPT-3.5 turbo models. Finetuning on these datasets improves performance on MDQA and FLenQA benchmarks while discouraging hallucinations. Performance on general evaluation benchmarks like TruthfulQA, GSM8k is shown to be retained.

### Strengths
- Finetuning on randomly sampled key-value datasets is able to fix the “lost-in-the-middle” phenomenon for GPT-3.5 while retaining original knowledge.
- Finding that finetuning with answer templates performs better.
- Work on improving LLMs through synthetic datasets is crucial for the community.

### Weaknesses
1) The proposed synthetic dataset targets only retrieval tasks, like MDQA, while other important applications of long-context, such as in-context learning and RAG, involve \emph{understanding} the context as a whole. Hence, I have doubts about the scope of applications of this work. Concurrent works [1, 2] argue that finetuning/improving only retrieval capabilities does not capture all long-context applications.

2) In line 263, it is claimed that "..proposed data mitigates this primacy bias..", but the curve in Fig 5(b) still shows a descent, although with a higher accuracy. The claim of mitigation is not fully supported by the presented data, as the accuracy still decreases for middle positions, indicating that the model still exhibits some degree of primacy bias.

3) About line 270, "..we also finetune the models on the MDQA dataset ..", from what I have understood, the difference between performance upon finetuning on the proposed dataset vs MDQA, can arise from two factors:
  (a) Randomization of the position of the gold document.
  (b) Complexity due to requirement of english understanding.
Since point (a) is easy to track, further study is needed to understand the differences between the two. Point (b), for example, can be explored by including the <Mistral-7B ft with MDQA> row in Table 1. It is crucial to isolate the impact of these factors to understand the true benefits of the proposed synthetic data.

4) In Section 3.4, a possible reason MultiDocQA & IN2 outperform the proposed dataset is that the baselines require extracting information from multiple contexts. Can you solve this drop by adding a task that needs to retrieve the values of multiple keys? Such a task also discourages the hallucinations that MultiDocQA & IN2 seem to give rise to. The current single key-value retrieval task might be too simplistic to capture the complexities of real-world multi-document retrieval scenarios.

5) Regarding line 214, It is unclear why the finetuning and evaluation is fixed within one sliding window. Since some works can improve the maximum context length of Mistral (32k), evaluation at longer context lengths is needed. Section 3.5 is the right step towards this, but quality evaluations still need to be included. The lack of evaluation at extended context lengths limits the practical applicability of the proposed method.

6) Although manipulation of positional embeddings to extend context lengths without training is orthogonal to this work, Works like [3, 4] improve the context lengths of Mistral while maintaining performance on retrieval-like benchmarks. Either an explanation in related work or a comparison with baselines is needed. The absence of a discussion or comparison with these methods makes it difficult to assess the novelty and effectiveness of the proposed approach.

### Questions
<see Weaknesses>

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper targets the challenge of LLM accurately retrieving information and maintaining reasoning capabilities when processing long-context inputs. To this end, the author designs a synthetic dataset specifically for fine-tuning recent popular pretrained models. An interesting advantage of this dataset is it doesn't contain any factual information. Their evaluations on long context retrival and reasoning tasks show clear improvements. They also compare with three additional long-context augmentation datasets as baselines. Results show that their synthetic dataset achieves comparable performance in long-context retrieval and reasoning without causing the significant degradation on general benchmarks observed with other baselines.

### Strengths
The paper is well written and easy to follow. 

The problem addressed in this paper is pretty meaningful.

The experiments are comprehensive and effectively support the main points.

The idea is straightforward but produces good results.

### Weaknesses
I have some concerns about the experiments. 

(1) For stage 1, why does the author fine-tune Mistral 7B for 2 epochs but fine-tune GPT-3.5 Turbo for 3 epoches? Is the performance sensitive to the number of training epochs? 

(2) For stage 1, does it need any training strategy such as early stopping? Will a longer training hurt the performance on general benchmarks? Also, what will happen if we train with a larger key-value retrieval dataset? Will the performance on long context retrival and reasoning tasks further improve, and might it negatively affect general benchmark performance?

(3) Will the performance further improve if also fine-tune Mistral 7B with Multi-subkey dictionary key-value retrieval dataset?

(4) When fine-tuning with MDQA, does it train with 20 documents and place a gold document in some positions? If so, does this mean that the model is fine-tuned with too few samples? 

(5) The author presents fine-tuning with MDQA as a baseline in Section 3.2.1 but does not provide similar results for FLENQA in Section 3.2.2. Is there a specific reason for this? I’m curious whether the conclusions would remain consistent.

(6). How many tokens are used for training for the other baselines in stage 4? I think it's a little bit hard to say if this method beats the other baseline because the baselines actually shows good performance on long context retrival and reasoning tasks especially on FlenQA(cot), the performance is also ok on some datasets in the general benchmarks. 

A minor suggestion: I think it would be helpful to include the average accuracy/gap across all datasets in Table 2, as it would clarify the overall average degradation.

### Questions
(1). Is there any reason the dataset is built with 3 or 4 digits? I think 4 digits will count as 2 tokens in the GPT tokenizer, while 3 digits is just 1.
(2) Can GSM8K be considered a reasoning task? I think Triviaqa can also be considered a retrieval and reasoning task. Why can't those datasets improve performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes synthetic data generating for the tasks requiring  understanding of long context. Specifically, it generates a key-value retrieval task where an LLM is fine-tuned to find out a dictionary with the specified key value. To make the task more difficult,  the key becomes a tuple of integers and the order of integers are randomly shuffled. After fine-tuning the LLM, LLM is evaluated on MDQA and FlenQA dataset. The proposed synthetic data generation leads to performance improvement of  GPT-3.5-Turbo and Mistral.

### Strengths
- The proposed method is simple and effective.

- It does not degrade the performance on other benchmark datasets such as MMLU, HellaSwag, GSM8K, Triviaqa, NQ-open.

- The paper is well written.

### Weaknesses
 - Details of how key-value retrieval task is generated are missing, which seems to be critical.

- More extensive experiments need for validating the proposed method. For example, I highly recommend to evaluate the method on benchmark datasets such as RULER [1] and Long Bench [2] with different backbone LLMs such as Llama and Gemma.

### Questions
- Did you full fine-tune the Mistral or use parameter efficient fine-tuning (peft) such as lora?

- What is the rationale for choosing the number of samples in key-value retrieval tasks?

- In Figure 5b, Mistral-v0.1 is used, while Mistral-v0.2 is used in Figure 7b. Is there any reason why you use different version of Mistral?

### Soundness
3

### Presentation
3

### Contribution
3
