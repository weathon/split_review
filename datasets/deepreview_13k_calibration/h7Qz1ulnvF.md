# Improving Complex Reasoning with Dynamic Prompt Corruption: A Soft Prompt Optimization Approach

- Decision: Accept
- Avg Score: 5.75
- Scores: 3, 8, 6, 6

## Abstract
Prompt Tuning (PT) has emerged as a promising Parameter-Efficient Fine-Tuning (PEFT) approach by appending trainable continuous prompt vectors to the input, maintaining competitive performance with significantly fewer trainable parameters. While PT has shown effectiveness in enhancing task performance, particularly for classification tasks, its application to complex reasoning tasks has been largely overlooked. Our investigation reveals that PT provides limited improvement and may even degrade performance in reasoning tasks. This phenomenon suggests that soft prompts can positively impact certain instances while negatively affecting others, particularly during the latter stages of reasoning.
To address these challenges, we propose a novel method called Dynamic Prompt Corruption (DPC), which seeks to optimize the use of soft prompts in reasoning tasks. DPC dynamically adjusts the influence of soft prompts based on their impact on the reasoning process. Specifically, it involves two key components: Dynamic Trigger and Dynamic Corruption. Dynamic Trigger measures the influence of soft prompts, determining whether their impact is beneficial or detrimental. Dynamic Corruption mitigates the negative effects of soft prompts by selectively masking key tokens that interfere with the reasoning process.
We validate our approach through extensive experiments on various large language models (LLMs) and reasoning tasks, including GSM8K, MATH, and AQuA. The results demonstrate that Dynamic Prompt Corruption consistently improves the performance of LLMs, achieving  4\%-8\% accuracy gains compared to standard prompt tuning. These findings highlight the effectiveness of our approach and its potential to enhance complex reasoning in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims to improve prompt tuning on LLMs. The authors claim that later reasoning steps in wrong examples usually have high attention values on the soft prompt tokens, which is interpreted as "attend to the hints in soft prompt and conflict with early reasoning steps". Therefore, the authors propose to corrupt the soft prompt with a mask when such bad attention behavior is detected. Experiments on several math dataset show that this method can improve the vanilla prompt tuning.

### Strengths
- Several math benchmarks are covered in the experiment section, including various difficulty levels easy (gsm8k) and hard (MATH).
- The paper is well written and easy to follow.

### Weaknesses
 - In this paper, soft prompt is interpreted as "carrier of task-related knowledge" or "hints", which is a bit casual and not well supported.

-  The major argument of this paper is LLM (later stage reasoning steps) shouldn't pay too much attention on soft prompts, which is very suspicious. Specifically,

     1. The authors derive this argument from empirical observation instead of rigorous causal relation analysis, or fundamental justification. 
     2. The prompt / input to LLM, prompt is structured as {soft prompt; question} where soft prompt is in the leading position. Then the authors observe some high attention on soft prompt (leading tokens) on wrong examples. However, according to [1], LLM trends to put non-useful attention values on leading tokens (e.g., first several tokens) and that's why leading tokens has high attention value. In other words, it does not mean high attention on soft prompts, which are in leading position, is a bad behavior.  
     3. On top of 2, the corruption mask that can improve reasoning accuracy is not because they mitigate bad high attention values on soft prompt, but something else, e.g., overfitting.

- In experiments table1, it's hard to validate any this prompt tuning methods (prompt tuning, act, dpc) is necessary or not on reasoning tasks. The authors should add full finetuning as the major baseline, and demonstrate that dpc is on par or even better than it.

### Questions
Please find my comments in the weaknesses section

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel technique called Dynamic Prompt Corruption (DPC) to optimize the utilization of soft prompts in intricate reasoning tasks. This method dynamically regulates the impact of soft prompts on the reasoning process. Experimental results demonstrate the effectiveness of this approach.

### Strengths
1. The athors adopt a probing approach, quantitatively analyzing the efficacy of soft prompts on guiding complex reasoning in LLMs. Its conclusions offer profound insights, and methods derived from these insights have demonstrated significant effectiveness in experiments. This work makes a substantial contribution to the field of LLM reasoning research, and I highly appreciate the innovative insights presented in this paper.

2. The article exhibits a clear and coherent structure, with well-organized content.

### Weaknesses
The experimental baselines in this study are relatively limited in number. A comparative analysis with other PEFT methods, like LORA, could enhance the experiments. If this paper can unveil shared observational conclusions among various PEFT methods, it would significantly strengthen the overall contribution of the study.

### Questions
1. Do other PEFT methods exhibit similar observations?
2. Apart from saliency scores, are there better probing tools available?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies why sometimes soft prompts can affect reasoning outcomes. The paper points out that certain specific tokens in prompts can significantly harm reasoning performance. To address these challenges, it proposes a method called Dynamic Prompt Corruption (DPC), which seeks to optimize the use of soft prompts in reasoning tasks. DPC dynamically adjusts the influence of soft prompts based on their impact on the reasoning process. Specifically, it involves two key components: Dynamic Trigger and Dynamic Corruption. It mitigates the negative effects of detrimental soft prompts by selectively masking key tokens that interfere with the reasoning process.

### Strengths
1. The problem addressed in the paper is genuinely existing, and the paper has strong practical value.

2. The paper uses experiments to analyze in detail the reasons why prompts can lead to reasoning errors in certain situations, demonstrating strong persuasiveness and logical coherence.

3. The method and analysis proposed in the paper are highly relevant, simple and effective, and easy to reuse.

4. The paper is well-written and easy for readers to follow.

### Weaknesses
1. The choice of the saliency score lacks explanation; it's unclear why this metric is used instead of others. Additionally, there should be more clarification regarding Equation (1).

2. The phenomenon presented in the article is largely based on observation, but the generalizability of the observed conclusions requires further validation. Additionally, the explanations for the phenomenon lack theoretical support.

### Questions
Please see weaknesses.

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
4

### Summary
This paper discovers that sometimes prompts can make the model generate the wrong answer, using the metric of saliency scores defined by Hadamard product of attention score and its gradients. When such cases happen, it is usually because the question part does not have even attention on the prompt (i.e., not reading hints carefully), or because the answer part relies too much on the prompt (i.e., misled by the hints, rather than thinking more on questions and previous steps in answer). Therefore, the authors proposed that one can use two step algorithm to fix. In the first step, they identity whether such bad cases happen. In the second step, they fix bad cases by adding masks to prompts, so that attention will be improved. Empirically such method can improve the performance on GSM8K, MAH, and AQuA.

### Strengths
Originality: the authors noticed that the attentions between soft prompts and question, and between soft prompts and answer, are nicely correlated with the final correctness. This observation is interesting and original. 

Quality: the observation is interesting. I especially like the visualizations in the paper. 

Clarity: this paper is well written and easy to follow. 

Significance: the observation that attentions will affect performance might be interesting to other researchers.

### Weaknesses
I will not give a high score to the quality of this paper, because it did not tell a "full story".
- The Figure 4 indeed shows difference between good and bad cases of the saliency scores, but the difference is not very big. For example, in Figure 4(c), good case has score of ~0.014, while bad case has score of ~0.019. While I agree such difference means we can improve our model by using the two step algorithm, this observation does not seem to be substantial. It seems entirely possible that in the next version of LLM, this difference may disappear.
- While I agree the two step algorithm is effective to improve the model's accuracy, the improvement is not significant as well.

Therefore, I think the significance of this paper is mild. I feel this algorithm may not be used by most researchers in the field.

### Questions
I do not have additional questions.

### Soundness
3

### Presentation
4

### Contribution
2
