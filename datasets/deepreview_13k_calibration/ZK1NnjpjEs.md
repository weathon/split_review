# Improving the Language Understanding Capabilities of Large Language Models Using Reinforcement Learning

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3, 3

## Abstract
Large language models (LLMs), primarily built on decoder-only transformer architectures, excel in natural language generation tasks and have shown promise in adapting to diverse downstream tasks using zero-shot and few-shot prompting techniques. However, these prompting methods often fall short on natural language understanding (NLU) tasks, where smaller encoder-only models like BERT-base consistently outperform LLMs on benchmarks such as GLUE and SuperGLUE. In this paper, we explore two approaches—supervised fine-tuning and proximal policy optimization (PPO)—to enhance the NLU capabilities of LLMs. To reduce the computational cost of full-model fine-tuning, we integrate low-rank adaptation (LoRA) layers, restricting updates to these layers during both supervised fine-tuning and PPO stages. In the supervised fine-tuning approach, task-specific prompts are concatenated with input queries and ground-truth labels from the NLU training corpus, optimizing the model using the next-token prediction objective. Despite this, LLMs still underperform compared to encoder-only models like BERT-base on several NLU tasks. To address this gap, we employ PPO, a reinforcement learning technique that treats each token generation as an action and evaluates the sequence of generated tokens using a reward function based on their alignment with ground-truth answers. PPO then updates the model to maximize these rewards, effectively aligning its outputs with the correct labels. Our experiments with the LLAMA2-7B model demonstrate that PPO-based fine-tuning significantly improves performance, delivering an average gain of 6.3 points over supervised fine-tuning on the GLUE benchmark. PPO surpasses zero-shot prompting by 38.7 points and few-shot prompting by 26.1 points on GLUE, while also outperforming these baselines by 28.8 and 28.5 points on SuperGLUE. Additionally, PPO exceeds the performance of BERT-large, a strong baseline, with an average improvement of 2.7 points on GLUE and 9.3 points on SuperGLUE. These improvements are consistent across models such as Qwen2.5-7B and MPT-7B, highlighting PPO’s robustness and effectiveness in enhancing the NLU capabilities of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a PPO-based fine-tuning approach to enhance the NLU capabilities of LLMs. Experiments on the GLUE and SuperGLUE benchmarks show that PPO achieves competitive results compared to supervised fine-tuning and enables LLMs, such as Llama 8B, to outperform BERT-large (340M).

### Strengths
The paper is very well written and very easy to follow.

### Weaknesses
My primary concern is the limited contribution of this paper. Personally, I didn’t find anything new or insightful in it. The conclusions are rather obvious. The authors highlight the improvement of PPO fine-tuned LLMs with sufficient training data compared to zero-shot and few-shot LLMs, but this outcome is quite predictable.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores the combination of low-rank adaptation (LoRA) and proximal policy optimization (PPO) to enhance natural language understanding capabilities of LLMs while reducing computational cost. Experimental results show that the combination of LoRA and PPO yields performance improvement over zero-shot and few-shot baselines on GLUE and SuperGLUE. The improvements are consistent across several LLMs such as Qwen and MPT.

### Strengths
Research on natural language understanding capabilites of LLMs is an important part of AI. The paper reports experimental results of the combination of two common methods, LoRA and PPO, on GLUE and SuperGLUE benchmarks.

### Weaknesses
LoRA and PPO are commonly used in LLM post training. For example, trlx [1] is one of popular LLM post-training tools, implementing both PPO and LoRA. This paper does not present novel methods or findings.

[1] trlX: A Framework for Large Scale Reinforcement Learning from Human Feedback

### Questions
What are advantages of this work compared to existing post-training frameworks, such as trlx, that support both LoRA and PPO?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies strategies to improve the NLU capabilities of LLMs, such as LLAMA2-7B, through SFT and RL techniques like PPO. The findings indicate that PPO significantly enhances the performance of SFT-optimized LLMs, demonstrating its effectiveness in further refining LLMs for NLU tasks. For instance, PPO training enables the LLAMA2-7B model to exceed BERT-large in performance on NLU tasks.

### Strengths
- The authors conducted comprehensive experiments on both the GLUE and SuperGLUE benchmarks, providing a thorough evaluation of their approach.
- The study includes experiments across various LLMs, including LLAMA2, Qwen2.5, and MPT, demonstrating the robustness and generalizability of the proposed method.

### Weaknesses
- For the single-task (ST) setting, the motivation for training a 7B parameter LLM to address NLU tasks remains unclear. By checking the GLUE and SuperGLUE leaderboards, it is evident that smaller bidirectional transformers with fewer than 1.5B parameters already achieve high performance (90+ overall scores) on NLU/classification tasks. This raises the question of why a significantly larger 7B LLM is needed to tackle NLU tasks using autoregressive decoding.
- For the multi-task (MT) setting, using SFT/RL (PPO, DPO, etc.) w and w/o LoRA to improve end task performance has been already widely used and the de facto settings in existing LLM research and production. This paper lacks of sufficient technical innovation/contribution or new findings that can benefit other research or the community.
- The paper lacks an error analysis or qualitative evaluation of LLM outputs on NLU tasks. An in-depth error analysis or qualitative evaluation of LLM outputs from both SFT and PPO-based models on NLU tasks would be valuable for understanding why autoregressive LLMs underperform compared to much smaller bidirectional models.

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper emphasizes the problem that current decoder-only transformer models fall short on natural language understanding tasks compared with much smaller encoder-only models such as Bert-base. To address this problem, this paper explores two approaches---supervised fine-tuning and proximal policy optimization --- to enhance the NLU capabilities of decoder-only transformer models. The authors perform extensive experiments on different tasks and backbone models to prove the robustness and effectiveness of both methods in improving NLU capabilities of LLMs.

### Strengths
This paper has several strengths worth noting:

1. The writing is clear, and the logical flow is easy to follow.

2. The experimental design is comprehensive, taking into account multiple factors that can influence performance, such as various datasets, backbones, and baselines.

3. I appreciate the attention to detail in this article, especially the thorough introduction to the prerequisites for PPO and the detailed design of the prompts, etc.

### Weaknesses
There are several weaknesses that need to be addressed:

1. This paper focuses on an interesting problem: decoder-only models perform worse than smaller encoder-only models. However, I question whether this issue still holds true with the emergence of more powerful language models, such as GPT-4o. It would be beneficial to test the most recent state-of-the-art models to evaluate the validity of this problem.

2. The datasets utilized in this paper (GLUE and SuperGLUE) are overly simplistic. I recommend validating the methods on more complex and updated NLU datasets.

3. The suggestion of fully supervised fine-tuning may not be considered a significant contribution, as prior works have proposed and conducted related experiments, such as P-tuning.

4. I believe the contributions of this work are somewhat marginal at the moment. It would be beneficial if the paper could highlight specific and detailed challenges and solutions related to using PPO to enhance NLU. Additionally, the paper could broaden the scope of the problem, such as by addressing more complex NLU scenarios.

### Questions
(1) In the paper, the authors conduct experiments using LORA to reduce computational costs. While using LORA instead of full training does save resources, it comes at the expense of performance. I wonder if full fine-tuning could compensate for the improvements achieved with PPO. I believe this is a crucial point that needs further investigation.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores methods to enhance the NLU capabilities of LLMs, which typically underperform compared to smaller encoder-only models like BERT. The authors employ a two-stage training involving SFT and PPO, and use LoRA to reduce computational cost. The experiments with the LLAMA2-7B model demonstrate that PPO-based fine-tuning surpasses the performance of BERT-large.

### Strengths
1. The authors construct a complete pipeline to improve the performance of LLMs on NLU tasks.
2. These improvements are consistent across different LLMs, highlighting PPO’s robustness and effectiveness in enhancing the NLU capabilities of LLMs.

### Weaknesses
1. Lack of novelty: This work simply employs LoRA + PPO on NLU tasks, without introducing new techniques or insights compared to previous works such as [1].

2. Insufficient baselines: though claiming that "LLMs with prompting methods fall short on natural language understanding (NLU) tasks", the most powerful proprietary LLMs such as GPT-4o are not evaluated in the experiments. Besides, popular prompting methods such as few-shot CoT are also not evaluated. In addition, for SuperGLUE, Qwen-2.5-7B, and MPT-7B, the results of SFT are not presented. Finally, the result of full-model SFT / PPO should be presented for comparison, since the full-model SFT may already outperform BERT-large.

3. Inadequate motivation: NLU benchmarks are typically used to measure the basic ability of pre-trained language models. Better fine-tuning performance on these benchmarks indicates that the pre-trained language model is more powerful and can also perform better on other real-world downstream tasks, while simply improving performance on these benchmarks via other techniques is less meaningful. It is common sense that current large foundation models have much better basic ability than previous small LMs such as BERT, making the contribution of this work poor. That's also why current works do not evaluate LLM on GLUE and SuperGLUE.

4. Error citation format: All citations in the paper are not bracketed.

[1] Parameter Efficient Reinforcement Learning from Human Feedback. https://arxiv.org/abs/2403.10704

### Questions
1. Is there more sufficient motivation for improving LLMs performance on GLUE and SuperGLUE? For example, after PPO on these NLU tasks, can the model perform better on other downstream tasks?
2. Is there any new techniques or insights compared to previous works?

### Soundness
2

### Presentation
3

### Contribution
1
