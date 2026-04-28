# Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 3, 5, 8

## Abstract
It has been reported that LLMs can recognize their own writing. As this has potential implications for AI safety, yet is relatively understudied, we investigate the phenomenon, seeking to establish whether it robustly occurs at the behavioral level, how the observed behavior is achieved, and whether it can be controlled. First, we find that the Llama3-8b–Instruct chat model - but not the base Llama3-8b model - can reliably distinguish its own outputs from those of humans, and present evidence that the chat model is likely using its experience with its own outputs, acquired during post-training, to succeed at the writing recognition task. Second, we identify a vector in the residual stream of the model that is differentially activated when the model makes a correct self-written-text recognition judgment, show that the vector activates in response to information relevant to self-authorship, present evidence that the vector is related to the concept of ``self'' in the model, and demonstrate that the vector is causally related to the model’s ability to perceive and assert self-authorship. Finally, we show that the vector can be used to control both the model’s behavior and its perception, steering the model to claim or disclaim authorship by applying the vector to the model’s output as it generates it, and steering the model to believe or disbelieve it wrote arbitrary texts by applying the vector to them as the model reads them.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper investigates the self-recognition ability of large language models (LLMs), focusing on the Llama3-8b-Instruct model. The authors explore whether the model can reliably distinguish its own outputs from those of humans and other models. The study highlights the implications of self-recognition for AI safety, suggesting that such ability might be related to situational awareness, potentially influencing how an AI system reacts in training versus deployment contexts. The authors use a combination of behavioral experiments and model inspections to identify a specific vector in the residual stream responsible for this self-recognition. Additionally, they demonstrate that manipulating this vector can alter the model’s output to claim or disclaim authorship of text.

### Strengths
- the exploration of a "self-recognition" vector in the residual stream is innovative and provides new insights into how LLMs process self-generated text.
- the experiments are comprehensive, employing multiple datasets, paradigms, and control measures. The use of both paired and individual presentation paradigms adds depth to the investigation.
- the findings have important implications for AI safety, as the ability to control model behavior through vector manipulation could influence future approaches to securing LLMs against misuse.
- the paper is detailed and generally clear, with extensive appendices supporting the main findings.

### Weaknesses
 - some sections, particularly those on the technical details of vector activation and steering, are dense so simplifying these descriptions or providing more diagrams could improve comprehension
- while the appendices provide valuable information, some essential points might be better included in the main body to avoid over-reliance on supplementary material.
- although the work is thorough for Llama3-8b-Instruct, it would be beneficial to discuss whether these findings might extend to larger or more diverse models.

### Questions
1. Could the authors clarify if the "self-recognition" vector can influence the model’s responses to unseen, completely out-of-domain prompts?
2. Is there potential for the identified vector to generalize to models beyond Llama3-8b-Instruct, or is it highly specific to this architecture?
3. How might the ability to manipulate self-recognition vectors be used responsibly to mitigate risks, and what safeguards could be put in place?

### Soundness
3

### Presentation
3

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
The authors explore the capability to recognize text as being self generated in LLaMA-3-8b models.
They find that LLaMA-3-8b-instruct (but not the base model) can distinguish texts created by it from texts created by humans, but not from texts created by other similar language models.
Then they create a “self-recognition” vector that corresponds to this capability. They evaluate it in various ways, showing that this vector indeed explains how the model makes a decision about whether a given text was written by it or not.

### Strengths
Authors make a convincing claim that capabilities related to self-recognition arise during the post training process.
The analysis of the “self-recognition” vector is meticulous.
The text is easy to follow.

### Weaknesses
According to lines 94-95, you include the source text and the instructions in the questions. This has two significant downsides:
First, it decreases safety relevance. For example, in the introduction you mention the risk of collusion when the model recognizes it is talking to itself. But in such scenarios the model won’t have the full context (e.g. it will not know the other instance’s system prompt). 
Second, it’s much harder to tell what is the mechanism behind self-recognition. You argue in 3.1.2 that perplexity doesn’t matter, but you don’t make a convincing case that the model doesn’t use this type of reasoning at all (it would be hard to make such a case).

It seems likely that the vector you found is just something like “this looks like a text from an RLHFed model”. RLHFed models tend to speak in a different way than humans. For example, a text with N tokens generated by an RLHFed LLM will usually have more characters than a text with N tokens written by a human. Base models are similar to humans in this regard. You found that LLaMA can’t distinguish their text from texts generated by other RLHFed models, but can distinguish from humans and from the base model, so this is consistent. It seems also consistent with your other findings, e.g. around line 349 or 453. You could try to refute the simple version of this hypothesis by verifying the accuracy of a simple classifier (e.g. Naive Bayes over a bag of words) trained to distinguish human and LLaMA text.

Overall, differences between texts generated by humans and RLHFed models are much easier to spot than differences between texts generated by different RLHFed models. I think that as long as the models can’t distinguish themselves from other LLMs, it’s pretty hard to make a convincing claim that they have a real self-recognition ability.

Minor things:
Line 151, “In all but the SAD dataset …” - I don’t see anything SAD-specific on 1a
Figure 1a: the font is much too small. Also what is “LLaMA” on the plot?
Table 1: why compare only to human text, not other LLMs?
Section 3.2 could use a summary of findings.
Figure 4: a better caption, what is left and what is right?
Table 3 in Appendix 1 is unclear

### Questions
Have you tried the setup where the source text and instructions are not shown to the model? If yes, what is the performance there?

In line 159 you mention that you trim all texts “to a set length”. Is this length in tokens or in characters/words?

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
2

### Summary
The paper investigates the ability of LLMs to recognize their own writing, focusing specifically on Llama3-8b-Instruct. The authors make three main contributions:
1.Demonstrate that the RLHF'd chat model can reliably distinguish its own outputs from human writing, while the base model cannot
2.Identify and characterize a specific vector in the model's residual stream that relates to self-recognition
3.Show this vector can be used to control the model's behavior regarding authorship claims

### Strengths
1.This paper conduct thorough and controlled experiments using multiple datasets with different characteristics including cnn, xsum, dolly and sad.
2.Clear ablation studies with statistical analysis demonstrate causal relations.
3.Successfully isolated a specific vector in the residual stream using contrastive pairs method and provide evidence of vector’s causal role through steering experiments.
4.Identify the correlations between vector activation and confidence.

### Weaknesses
1.The paper’s experiments are mainly limited to one model family(LLama3) with a relative small LLM(8B).
2.The paper cross referenced many figures in the appendix which is hard to read.
3.More discussion needed on practical applications for AI Safety and Model Alignment.
4.More details on methods and statistical analysis need to be added.

### Questions
1.Have you investigated whether similar vectors exist in other model architectures? This would help establish the generality of your findings.
2.It’s better to describe how the similar vector is derived in details.
3.How stable is the identified vector across different fine-tuning runs? This would have implications for the reliability of using it as a control mechanism.
4.Could you elaborate on how the vector's properties change across model scales? This might provide insights into how self-recognition capabilities emerge during training.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper dives into the mechanistic explanation of 'self-recognition' for the LLM-generated texts, using LLaMA3-8b-instruct as a case. In the paper, the authors show that LLaMA3-8b-instruct recognizes its generated text from others, such as humans and other LLMs with high performances across two tasks and four datasets. By comparing with the LLaMA3-8b-base model, the authors point out that RLHF enables such self-recognition ability in LLMs. To investigate how self-recognition is represented and computed inside the model, the authors use steering each layer's activations to observe the effect on the output. By zeroing out each layer separately, the authors get causal evidence that layer 16 is the most intensive for representing such 'self-recognition' ability in LLaMA3-8b-instruct. Finally, by 'coloring' the texts based on the steering vectors, the model can interpret the output texts in its own way, showing a valid representation of the vectors.

### Strengths
- The authors choose two different task scenarios (paired and individual paradigms) as well as four datasets to investigate the question. The authors also did a comprehensive sanity check to ensure the stability and contribution of the result, such as testing the model before and after RLHF, correlating with perplexity, and normalizing the length effect and positional bias in LLM.

- The authors investigated the computation and representation of 'self-recognition' in the model. By identifying the layers and extracting vectors, the authors show the correlational and causal relationship between the model computation in certain layers and the ability to recognize the self-generated texts. The authors also show the representation can indeed be used to change the style of a text, which reveals the solidity of the representation they find.

- The writing is generally clear and satisfying.

### Weaknesses
 - From a perspective of cognitive science, I still wonder what makes the 'style' of language that LLMs speak and humans different. The authors did a lot of work to find out the valid representation of such an ability to recognize self-generated texts. But what makes the style different is still unclear. If such representation could map on specific features of the style (length for example, or tone, some special word frequency, etc.). It may make sense to ask humans to do the same task (their 'self' is humans) and to see the performance. Probably this can be a good point to make about how LLMs and humans process and understand the language differently.

 - The caption of each figure can be more detailed. For example, in Figures 3 and 5, there are multiple sub-figures but I cannot gain any information to distinguish them only from the figure and caption. It could be more reader-friendly to add details in the caption.

### Questions
- One question I found interesting is when the authors choose to steer the activations, why a very big multiplication on the embedding would result in less effect (for example, in Figure 4, 15 or 16 layer, as the multiplicator grows, the effect grows as well. But when it comes to 14, it is weaker instead, and even turn negative)?

### Soundness
4

### Presentation
4

### Contribution
3
