# Improving Instruction-Following in Language Models through Activation Steering

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
The ability to follow instructions is crucial for numerous real-world applications of language models. %
In pursuit of deeper insights and more powerful capabilities, we derive instruction-specific vector representations from language models and use them to steer models accordingly. These vectors are computed as the difference in activations between inputs with and without instructions, enabling a modular approach to activation steering. We demonstrate how this method can enhance model adherence to constraints such as output format, length, and word inclusion, providing inference-time control over instruction following.
Our experiments across four models demonstrate %
how we can use the activation vectors to guide models to follow constraints even without explicit instructions and  to enhance performance when instructions are present. Additionally, we explore the compositionality of activation steering, successfully applying multiple instructions simultaneously. Finally, we demonstrate that steering vectors computed on instruction-tuned models can transfer to improve base models.
Our findings demonstrate that activation steering offers a practical and scalable approach for fine-grained control in language generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel method to improve the instruction-following capabilities of language models using activation steering. Experiments on four different language models demonstrated the effectiveness of activation steering for three different tasks.

### Strengths
1. Clear presentation and writing.
2. The proposed method is simple and effective.
3. The experiments and analysis are comprehensive and solid.

### Weaknesses
1. The three instruction-following tasks are related to format, length, and word inclusion/exclusion, which are not broad enough for general instruction following cases. Specifically, the 'format' category, while encompassing 13 sub-instructions, still focuses primarily on output structure rather than semantic understanding or complex reasoning. The tasks do not adequately test the model's ability to follow instructions that require nuanced interpretation or multi-step reasoning.
2. No limitation or discussion section in the paper.

### Questions
1. line 159, "...perform a small grid search over neighboring values on a held-out set of examples to fine-tune the steering effect". How the examples are chosen? How many examples and what's the granularity of the grid? Does it need to be done for every layer?
2. Figure 4 is a bit confusing. Maybe it's better to mention how the delta is computed (e.g. after steering - original, w/ inst - w/o inst), instead of using "w/ vs. w/o", or simply "steering w/". Is this quality score a good metric? It's almost opposite with the results of accuracy.

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
3

### Summary
The paper "Improving Instruction-Following in Language Models Through Activation Steering" proposes using activation steering to enhance the instruction-following abilities of language models. By deriving instruction-specific vectors based on activation differences between inputs with and without instructions, the method adjusts model behavior during inference to meet specific constraints such as output format, length, and keyword control.

### Strengths
The paper introduces a novel approach to activation steering through instruction-specific vector representations, allowing dynamic control over model behavior without retraining. 

The paper covers multiple constraint types (format, length, word-specific) across several models, highlighting the robustness and adaptability of the approach. The cross-model transferability experiments are valuable, showing that steering vectors from instruction-tuned models improve base models. 

The paper is well-structured and clearly explains each step.

Significance: activation steering offers a scalable solution for fine-grained control over LLM outputs. The demonstrated cross-model transferability suggests a cost-effective way to get instruction-following improvements.

In sum, this paper presents an original, well-executed, and practical contribution, for various real-world applications.

### Weaknesses
Cross-model transferability is a promising aspect of this work, yet the analysis here could benefit from more quantitative depth. Specifically, it would be useful to test how much performance degrades when steering vectors from instruction-tuned models are applied to base models of different architectures or parameter sizes. A more rigorous analysis should explore the impact of varying the number of parameters in both the source and target models, and also consider the effect of architectural differences, such as the number of layers or attention heads. For example, do steering vectors trained on a 1B parameter model transfer effectively to a 100M parameter model, or to a model with a different attention mechanism? This analysis is crucial to understand the practical limitations of the proposed approach.

The paper notes minor drops in response quality when adhering to certain constraints, particularly in the length and word-specific steering tasks. While the authors discuss this, it would be beneficial to implement strategies to mitigate these effects. The observed quality drops suggest a potential trade-off between instruction following and overall response coherence. It is important to understand the specific mechanisms that cause this degradation. For example, does the steering process introduce inconsistencies in the generated text, or does it limit the model's ability to generate diverse and contextually relevant responses? A more detailed analysis of the types of errors introduced by steering would be valuable.

### Questions
The need for unique vectors per instruction could impact scalability, particularly for highly variable, user-specific instructions. Clarifying how the approach handles diverse variable instructions would add practical insights.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper applies an activation steering method to improve the constraint following of LLMs such as response length and format. It also shows that multiple steering can be applied simultaneously and some steering generalizes from the instruct model to its base version.

### Strengths
- The steerability of LLMs, which this is tackling, is an important research area that has real-world implications.
- There are interesting findings in the paper, such as combining steering vectors and generalization to the base model.
- The paper is well written and easy to understand. The experimental setups look solid and diverse.

### Weaknesses
 - Novelty: the method of steering by activation itself is not novel and has been used in other papers. The authors claim the application is different, but previous works on writing style and topic changing are related to response format and mentioning a word. Some aspects of the method (combining steering vectors) seems novel, but maybe the author can clarify exactly which parts are novel.
- Motivation: From reading the paper, the motivation was not that very clear. Why is this method necessary? Explicit instruction in words seems to work better and simpler, while the proposed method can lead to nonsensical responses. What is the main motivation of using this method instead? 
- The proposed method doesn’t seem very general and may require adjusting for each instruction. For example, the method led to an opposite effect in the word exclusion task. In the length task, it is not clear how the exact length is translated into the vector scaling parameter.
- The dev set is using the same base queries as the evaluation? This makes it hard to judge how the method will generalize to unseen queries.
- It seems some task have extremely low number of samples. For example, there are only 12 sample for the format task, is that correct? 
- There are some typos around L175 where commas are placed incorrectly.

### Questions
- Maintaining quality is important for steering methods, but only one of the experiments shows the quality evaluations. I saw some results in the appendix, but I think it needs to be discussed in the main text. 
- In the length experiment, c=20 steering seems to help with different length constraints. I want to know if this steering makes the response generally shorter, which then happens to increase accuracy, or it makes it adhere to the specific length instruction more strongly? Because of the fixed c=20 value, I feel like it is likely the former.
- The plots are too small and sometimes use similar colors (dark blue vs light blue), which makes them hard to see. I think the writing can be made more concise to make more room for the plots.
- How are the base models following instruction? Is few-shot prompting used? 
- Seems to be missing this related work that also does “capitilzation” https://arxiv.org/pdf/2311.06668

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper develops a way to obtain steering vectors from  instruction prompts. Focusing on output modifiers such as “answer in uppercase,” they develop a way to obtain steering vectors by contrasting instructions with and without the modifier and averaging representation vectors from many paired samples, then they propose a steering approach that introduces scaling to the mean target magnitude.  They gather 12 format modifiers and 19 language modifiers and test their method on a data set of instructions on four language models ranging from about 3b to 9b parameters, sweeping over layers.  They test the ability to use the steering alone to add modifiers, and to use it to strengthen a modifier in a prompt. They also test vector negation by reversing word-inclusion modifiers to become word-exclusion, and they test composition of modifier vectors.  They also find that vectors from instruction-tuned models work very well on original models in some cases.

### Strengths
The derivation of steering vectors from instructions is an interesting research target and a good extension beyond similar work deriving such vectors from binary states or ICL prompts. The paper’s choice of deriving steering vectors from instruction modifiers is clever and novel, which allows the authors to create diverse training sets and also easily quantify the accuracy of results. The paper investigates nearly all the natural applications with useful measurements, including measurements of quality degradation in the presence of steering.  Positive results on negation and composition are interesting to see, and it is particularly interesting to see that vectors derived from instruction-tuned models work better than vectors from pretrained models when applied to pretrained models.

### Weaknesses
The presentation was sometimes uneven, giving the impression that the results might be curated to avoid showing results that did not work very well. Such cherry-picking should be resisted. For example: Figure 3 slices efficacy data by model and by instruction in different ways but does not provide breakouts by task for all four cases (bare prompt, prompt+modifier, prompt+steer, prompt+modifier+steer), which would help the reader build intuition about the failure cases.

Similarly: quality degradation was measured differently for different tasks, making it hard to compare. The paper would be improved if the appendix plotted or had a uniform table of quality degradation, computed the same way for every comparable task.

Other failure cases are mentioned but not measured: word exclusion is described as unpromising due to the presence of an embedding signal, but measurements of its failure are not shown. Full results should be shown.

It is stated that “it seems impractical to compute a separate steering vector for each possible length,” however that doesn’t seem impractical at all. Such specific-length steering vectors should be computed and compared to one another, and also to the conciseness concept described in the paper. If they do not work, that should be quantified and shown.

In appendix tables 8 and 9, many configurations are omitted with the explanation that "steering was unnecessary as the models typically followed the instruction."  Again, negative or "unnecessary" results should not be omitted. A key goal should be to explore and explain the limits of the observed effects. Failure or unhelpful cases are an important subject of experiments.

Some natural questions are unanswered, for example, whether the clusters of steering vectors over which means are taken are cleanly separated from each other (i.e., before taking means) or not.  It would be informative to plot a projection of the raw steering vectors for several of the tasks, for example, in a scatterplot as done in Hendel 2023.  In particular it would be interesting to see how closely-related vectors such as “answer of length n” for various n are arranged with respect to each other in representation space.

The choice of “c” is not fully justified, and it seems that the scaling factor “c” might be arbitrary. For example, c might mediate a tradeoff between efficacy and quality degradation.  It would be informative to plot tradeoffs over a sweep of c, if that is the case.

### Questions
* Can the the full grid of performance measurements of every modifier task (including both format and language) in all four cases (bare prompt, prompt+modifier, prompt+steer, prompt+modifier+steer) across models be included, perhaps in appendix?
* Similarly, quality degradation is broken out for some settings but not others. Can quality degradation measurements be shared in the same way over all modifiers?
* What are the measured results of word exclusion prompt steering vectors and specific numeric length modifiers? If they are failure cases, it will be helpful to see the extent to which they fail, and to share some of the typical behavior.
* Do the populations of sampled vector differences separate cleanly for different tasks, or is there some overlap?  It will be informative to plot these.
* Does the scaling factor induce a smooth tradeoff between output quality and accuracy in following the instruction?  It would be helpful o measure this.

### Soundness
3

### Presentation
3

### Contribution
3
