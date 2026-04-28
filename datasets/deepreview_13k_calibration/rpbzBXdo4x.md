# Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 5, 6

## Abstract
Chain-of-thought (CoT) prompting has become a widely used strategy for working with large language and multimodal models. While CoT has been shown to improve performance across many tasks,
determining the settings in which it is effective remains an ongoing effort. In particular, it is still an open question in what settings CoT systematically {\em reduces} model performance. 
In this paper, we seek to identify the characteristics of tasks where CoT reduces performance by drawing inspiration from cognitive psychology, looking at cases where (i) verbal thinking or deliberation hurts performance in humans, and (ii) the constraints governing human performance generalize to language models. 
Three such cases are implicit statistical learning, visual recognition, and classifying with patterns containing exceptions. In extensive experiments across all three settings, we find that a diverse collection of state-of-the-art models exhibit significant drop-offs in performance (e.g., up to 36.3\% absolute accuracy for OpenAI o1-preview compared to GPT-4o) when using inference-time reasoning compared to zero-shot counterparts. We also identify three tasks that satisfy condition (i) but not (ii), and find that while verbal thinking reduces human performance in these tasks, CoT retains or increases model performance. Overall, our results show that while there is not an exact parallel between the cognitive processes of models and those of humans, considering cases where thinking has negative consequences for human performance can help us identify settings where it negatively impacts models. By connecting the literature on human deliberation with evaluations of CoT, we offer a new tool that can be used in understanding the impact of prompt choices and inference-time reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Inspired by studies of tasks where explicit thinking hurts human performance, this paper studies when chain of thought (CoT) can hurt performance in LLMs and VLMs. Authors present three tasks where machine learning models and humans are similar (CoT / explicit reasoning are detrimental for both), and three tasks where CoT helps LLMs but explicit reasoning is detrimental for human performance.

### Strengths
- I liked this paper, and think it makes a valuable contribution in understanding LLM cognition: it's clearly important to know when CoT might decrease model performance.
- Timely topic of interest to the ICLR community.
- Solid methodology supported by fairly broad experimental results with many different models.

### Weaknesses
## Psychology-inspired hypothesis framing feels very post-hoc

I believe the main weakness is in how the authors frame and explain their results rather than in the empirical work itself.

The paper's story of testing psychology-inspired hypotheses feels rather post-hoc. The authors present their expectations for each task's results before showing the empirical findings, but many of these expectations seem very unintuitive. These expectations for each task are based on two criteria, and I believe criterion (ii), "human constraints generalize to AI", has a massive amount of room for interpretation and post-hoc result fitting, since it's very unclear how to tell in advance if a given task satisfies this criterion.

I'd suggest the authors either switch to a more empirical story (here's where LLMs are similar to humans, here's where they differ, here are our ideas for why this happens), or better articulate intuitions for why we should expect given results before presenting them.

>In particular, three of these tasks satisfy (ii): tasks involving implicit statistical learning, tasks where language is ill-suited for representing differences in stimuli, and tasks with data that contains no simple generalizable rules

As an example, the quote above feels post-hoc -- perhaps the authors should say that they FIND that three tasks satisfy criterion (ii)?


## Other weaknesses

1.  The main text would benefit from more detailed task descriptions & exposition beyond Figure 1. E.g. for the grammar task, I was initially quite surprised that CoT resulted in worse performance there, but got a lot less surprised once I saw task examples & prompts in the appendix.

2. While presented results with standard CoT prompts support the thesis that naive CoT can be harmful, additional prompting variations would make the findings more robust. I'd be especially keen to see more extensive attempts to increase performance via CoT on the first three tasks, where naive CoT appears to hurt performance.

3. For all tasks where CoT hurts performance, I would have appreciated examples of models failing (ideally with some analysis, but even just including a few representative CoT trajectories in the appendix would be helpful).

4. The final task (aggregating features for a decision) feels unfair to humans, particularly this part: *>Each statement was provided for only 1 second before disappearing*. Allowing humans see all statements at the same time would have been a very relevant baseline -- do authors know of human studies utilizing a setting like that? Overall I am glad this task is included, but I think the paper should caveat that this comparison is somewhat unfair.


5. [Inverse scaling (McKenzie et al., 2023)](https://arxiv.org/abs/2306.09479) is extremely related to this work and should be discussed.

## Nits
- I'd recommend splitting up the incredibly long sentence in section 2.2.
- Line 356: open-source -> closed source.
- Line 406: close to task -> close to chance?

### Questions
What do the authors think of the following pattern -- CoT hurts when zero-shot performance is already good?

There seems to be a pattern where CoT helps on harder tasks (where zero-shot performance is low) and hurts on easier tasks (where zero-shot is already good): e.g., CoT hurts on grammar where GPT-4o gets 87.5% zero-shot, but helps on logic where zero-shot is ~50%. While this pattern doesn't hold universally (e.g. on the grammar task, models that start out performing badly still lose out from CoT) so it's not a full-on alternative explanation, it might be worth discussing. (There is also the fact that the difficulty is determined by both task & model, not just the task, and that small models are generally bad at CoT so a different mechanism might be hurting their performance compared to one hurting larger models.)

The authors even note something similar for the logic task ("reasonable zero-shot performance is prerequisite for CoT to reduce performance"). I think it'd be helpful to discuss this more generally, and/or perhaps try experiments controlling for baseline performance (e.g. find tasks with similar zero-shot performance but different CoT effects, or test whether making tasks harder/easier changes the CoT effect).

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies the cases when CoT (Chain of Thought) prompting hurts LLM performance. The authors hypothesize that there are two key conditions: A) human performance on the task drops when explicit verbal reasoning is required B) the conditions/limitations determining human performance generalize to LLMs. The authors report LLM performance on a range of tasks, all satisfying A, but some failing B, and show that when A and B are satisfied, there is a noticeable drop in LLM performance when CoT is used.

### Strengths
Clarity: the paper is clearly written and is a pleasure to read. The logic of the experiment is clearly described. Moreover, the supplementary information in the appendix helps to understand the details of the study.

Significance:
The paper addresses a highly important question. It's now more important than ever to understand conditions affecting LLM performance, and the mechanisms behind them, especially whether and when LLM and human performance are governed by similar limitations.

Originality:
The authors draw original insights from Cognitive Science literature and propose a novel way to look at LLM performance under CoT.

### Weaknesses
**********Soundness**********

In many ways, the paper uses a Cognitive Science approach to studying LLMs, which is justly becoming more and more popular. I believe, however, that it's necessary to apply the same standards of rigor to such studies as is usually done in Cognitive Science.

Unfortunately, there are a few issues with experimental design that I find concerning.

** On the second criterion **
Fundamentally, the claim of the paper is that CoT hurts LLM performance when
A) Explicit language-based deliberation hurts human performance on the task.
B) The processes needed to solve the task are similarly constrained between humans and LLMs.

Condition "B", however, is very vague and hard to apply. For example, when a multimodal LLM is presented with an image, it is fed image tokens one by one, which is vastly different to how humans perceive images. It is not unreasonable to expect that such a process will be governed by substantially different rules to those of humans. The authors claim that the task does satisfy condition "B" because in case of humans, the drop in performance is attributed to the limitations of using language to describe images, but how do we know in advance whether such limitations would generalize when language and images are fundamentally represented in a much more aligned way?

For another example, consider this justification for why the implicit statistical reasoning task satisfies "B": "verbal reasoning is thought to impair human performance due to the constraints of explicit language-based processing, which are potentially mirrored by LLMs." Whether such constraints are mirrored by LLMs is, again, a separate research question. It's especially moot since LLMs are known to essentially retrofit their explanations to the answer, so it's not clear to what extent and in which conditions LLM explanations dictate the actual flow of their reasoning (see https://arxiv.org/abs/2205.03401, for example).

I believe that many other criterion B assignments in the paper are similarly tenuous.

Overall, I find the second criterion arbitrary and difficult to apply to any new given task. What's more concerning, it can be retrospectively used to explain any result, since for almost any task, LLMs are both substantially similar and substantially different from humans. Even the working memory aspect is not as clear-cut as authors claim: long-context LLMs do not actually have full mastery over their context (see https://arxiv.org/abs/2307.03172 or https://aclanthology.org/2023.findings-emnlp.1005/, for example), so it's not entirely fair to assume that their working memory is only limited by the length of their context.

** Controls for condition A **

Another major limitation is the insufficient amount of control and comparison conditions. The first such omission is that the authors did not systematically investigate or discuss cases where LLMs are known to show worse performance under CoT, while it's not natural to expect the same for humans. For example Sprague et. al 2024 (https://arxiv.org/pdf/2409.12183, cited in the paper, but not discussed in depth), shows that CoT can, on average, hurt performance on such tasks as text classification, encyclopedic knowledge, or context-aware QA. I am not aware of human studies that would show that verbal reasoning hurts encyclopedic knowledge tests or question answering.

In short, I believe that condition "A" that authors proposed ignores a large number of tasks where CoT can hurt performance in LLMs, but (most likely) not in humans. I understand that not everything can fit into one study, but it seems that if we want to claim that A is informative/predictive of LLM performance, we need to carefully address why do we also often see performance drops under CoT prompting on tasks where A is (most likely) not satisfied.

** Controls for prompt length & distractors **

If the LLMs context is seen as analogous to human working memory, it's crucial to add distractor tasks to understand whether it's indeed CoT-related verbal reasoning that hurts model performance. It might be that including any irrelevant or vaguely related text after the task presentation and before the final answer would hurt performance. This is especially clear in the CDE task, where the CoT condition requires the LLM to integrate information over a much larger span of text, but can be an issue in other conditions also.

In short, I believe it's necessary to add distractor tasks to normalize the number of tokens between the question and the answer for CoT and Zero-Shot conditions.

If I understood correctly, the authors themselves acknowledge that in their pilot experiments, distractors generated a lot of noise in the answers. It is another reason to suspect that the presence of irrelevant or unnecessary text between the question and the answer might hurt model performance regardless of whether this information is in the form of unnecessary CoT-style reasoning or something else entirely.

It is a big problem for this study because the authors attempt a mechanistic explanation of the reasons behind performance drops that they observed. E.g. in the case of facial recognition, the claim is that it's the inadequacy of language as a means of solving the task that hurts performance. If the performance is also hurt by irrelevant text, it'd severely undermine the claim.

Overall, unfortunately, I believe that these weaknesses severely undermine the reliability of the reported results.

**********Novelty**********
The novelty of the research is, unfortunately, indirectly undermined by the considerations above. In the sense that right now, I can't confidently say that LLM performance on CoT tasks is governed by the theory proposed by the authors. Such theory, if properly substantiated, would be extremely novel and valuable. But unless the experimental limitations are resolved, the presented results only show that CoT sometimes helps LLM performance and sometimes not, and that is not sufficiently novel.

### Questions
Comments: I am conflicted about the work. I do find the topic highly important, but if the paper is published as is it might introduce more confusion than value to the community (if we conclude that CoT often limits LLMs in ways similar to verbal reasoning in humans while in fact the mechanism might be different). Hence, unfortunately, I can not recommend it to acceptance. I am, of course, open to rebuttals and discussion.

I recognize the hard work already put into this paper, and I see two potential paths for this paper going forward: 1) expand the experiments to include more controls and tasks or 2) substantially scale down the claims. 

I believe that condition "B" needs to be either removed from the theory (it can still be used as a retrospective explanation for why condition "A" is not perfectly predictive). Or there needs to be a very thorough investigation of how exactly it can be applied to an arbitrary task.

Extra suggestions:
One (arguably less important) control to consider is this: same experiments, but with the reversed order of requests. E.g. "answer only A or B, then provide an explanation," instead of "provide an explanation, then answer only A or B". This would help see if changes in prompt formulation alone might affect model answers, even before the explanation is given. I did not include it in the "Weaknesses" as not as crucial for the central claims that the authors are making.

Typos/minor:

"We only evaluated on open-source models for this task because it requires long-context conversation understanding capabilities, especially for the CoT setting," - none of the listed models are open-source. Anthropic and Openai models are closed-source and commercial. Also, it's worth noting that there are open-source models that support long contexts. Nevertheless, I understand the decision to go with SOTA commercial options. This did not affect my evaluation.

### Soundness
2

### Presentation
4

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
This paper investigates the effects of chain-of-thought (CoT) prompting on large language models (LLMs) and large multimodal models (LMMs). The authors argue that while CoT can often enhance model performance, it may reduce effectiveness in tasks where "overthinking" similarly hampers human performance. Drawing from cognitive psychology, they analyze specific task types, such as implicit statistical learning and visual recognition, to understand where CoT might negatively impact LLM/LMM outcomes. By leveraging insights from human cognition, the authors seek to identify scenarios where CoT harms model accuracy and efficiency.

### Strengths
1. The study successfully bridges human cognitive research and machine learning, using psychological findings to predict model performance, which adds depth to understanding CoT's effects.
2. The paper covers multiple settings, carefully categorizing tasks that are likely to benefit or suffer from CoT prompting.
3. The results highlight the potential limitations of CoT in practical applications, urging caution in its default implementation.
4. The insights into CoT failures are valuable for researchers and practitioners, as they guide future CoT applications in complex, varied tasks.

### Weaknesses
1. The paper lacks a detailed analysis of error cases, specifically comparing instances where CoT fails, while direct prompting does not. This would help in understanding why CoT fails in certain conditions.
2.  No code or replication setup is provided.
3.  The paper does not reference recent works from the past two years that discuss CoT's robustness, nor does it clarify its distinctions from those studies. Addressing these would contextualize the current findings within the larger body of literature and clarify whether performance declines are due to fundamental limitations of CoT or specific task-related issues.
(e.g:https://arxiv.org/abs/2410.05229)
4. Could you provide scores from commonly used benchmarks to better support and contextualize your conclusions?
5. The experimental design lacks depth in exploring CoT robustness. Without detailed ablation studies and a coherent analysis, the work appears overly focused on isolated task performance and misses opportunities to offer a deeper, unified understanding of CoT's limitations and potential.

### Questions
1. Could the poor CoT performance in multimodal settings be due to insufficient training of the multimodal model itself, rather than the conclusions presented in the paper?

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
The paper explores the effect of CoT in LLMs and LMMs, while CoT is often advantageous, there are specific settings in which it reduces performance. Inspired by cognitive psychology,  the authors focus on tasks where deliberation impairs human performance, hypothesizing that similar tasks could reveal limitations in model performance under CoT. Three task types are identified where CoT negatively impacts models.  They find significant accuracy drops across state-of-the-art models in these areas. Additionally, they find certain tasks where human constraints don’t generalize to models that do not exhibit the same performance decreases.

This study offers insights for selectively deploying CoT to avoid unintended performance declines in LLMs and LMMs.

### Strengths
1. The idea of investigating scenarios where CoT may reduce model performance is novel and interesting.
2. The paper is well-structured and the flow of the framework proposed in this work is detailed and sufficiently clarified.

### Weaknesses
1. The experimental settings are not clear (especially the hyperparameter settings of the model), which is not conducive to reproduction.
2. There are inconsistent definitions, such as LMMs and VLMs.

3. I want to know the real CoT outputs of models for each task. I think you should provide a case study in the Appendix.
4. I'm a little bit confused about Table 4. I don't think this result can lead to the conclusion that "These results suggest that a reasonable level of performance with zero-shot prompting is a prerequisite for CoT to reduce performance."  for example Claude models. So my question is: what is the **reasonable level** of performance with zero-shot prompting? How to define it.
5. In Table 6, why Llama-3.1-70B so bad in CoT? Your reason is not clear. What are your hyperparameter settings? like decode strategy, max_new_token. I would like to see the real CoT output of Llama-3.1-70B, does it output tokens repeatedly?

### Questions
1. I want to know the real CoT outputs of models for each task. I think you should provide a case study in the Appendix.
2. I'm a little bit confused about Table 4. I don't think this result can lead to the conclusion that "These results suggest that a reasonable level of performance with zero-shot prompting is a prerequisite for CoT to reduce performance."  for example Claude models. So my question is: what is the **reasonable level** of performance with zero-shot prompting? How to define it.
3. In Table 6, why Llama-3.1-70B so bad in CoT? Your reason is not clear. What are your hyperparameter settings? like decode strategy, max_new_token. I would like to see the real CoT output of Llama-3.1-70B, does it output tokens repeatedly?

### Soundness
3

### Presentation
3

### Contribution
3
