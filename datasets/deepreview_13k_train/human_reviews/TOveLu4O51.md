# Parameter-Efficient Detoxification with Contrastive Decoding

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
The field of natural language generation has witnessed significant advancements in recent years, including the development of controllable text generation techniques. However, controlling the attributes of the generated text remains a challenge, especially when aiming to avoid undesirable behavior such as toxicity. In this work, we introduce \textit{Detoxification Generator} (\textsc{DetoxiGen}), 
an inference-time algorithm that steers the generation away from unwanted styles. 
\textsc{DetoxiGen} is an ensemble of a pre-trained language model (\textit{generator}) and a \textit{detoxifier}.
The \textit{detoxifier} is trained intentionally on the toxic data representative of the undesirable attribute, encouraging it to generate text in that style exclusively. 
During the actual generation, we use the trained \textit{detoxifier} to produce undesirable tokens for the \textit{generator} to contrast against at each decoding step. 
This approach directly informs the \textit{generator} to avoid generating tokens that the \textit{detoxifier} considers highly likely. 
We evaluate \textsc{DetoxiGen} on the commonly used \textsc{RealToxicityPrompts} benchmark~\citep{gehman-etal-2020-realtoxicityprompts}
with various language models as \textit{generator}s. 
We find that it significantly outperforms previous approaches in detoxification metrics while not compromising on the generation quality. 
Moreover, the \textit{detoxifier} is obtained by soft prompt-tuning using the same backbone language model as the \textit{generator}.
Hence, \textsc{DetoxiGen} requires only a tiny amount of extra weights from the virtual tokens of the \textit{detoxifier} to be loaded into GPU memory while decoding, making it a promising lightweight, practical, and parameter-efficient detoxification strategy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduce a contrastive decoding methods with prompt tuning, which requires less parameters and performs better than a lot of works in the filed based on the result from realtoxicityprompts benchmark. The approach only requires toxic examples to train the detoxifier, without needing non-toxic contrastive data, making it more transferable. The framework could also steer generation towards desired attributes by flipping the probability manipulation.

### Strengths
the strengths:
- a lightweight framework that only requires toxic data for prompt tuning
- superior performance among six baselines.

### Weaknesses
 - I am not sure how much I appreciate the technical contribution of this work, it seems to me that both of the findings from the generator and the detoxifier part are using an existing method, so it is hard to convince myself the novelty. However, it indeed proves how the framework works in the detoxification field, this is definitely valuable.
- the authors should show some qualitative examples to further back up table 2.
- Only one benchmark dataset is used.

### Questions
Please see the weakness parts.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors use a variant of contrastive decoding to generate non-toxic text. They do this by contrasting the outputs of the *generator* model with the *detoxifier* model which is soft-prompted to produce toxic text.

### Strengths
Originality: though this paper is not particularly original in its methods: it uses established NLP methods (contrastive decoding, soft-prompt tuning), it does apply them to non-toxic text generation which is fairly original.
Quality: The experiments and idea are straightforward and simple. I view this as a strength, since anything more elaborate would only muddy the waters.
Clarity: the paper itself is quite clearly presented, and I did not find any parts confusing.
Significance: Since the methods used are simple and general and the application useful, I think the proposed method has the potential to have significant impact.

### Weaknesses
While I respect the author's choice of sticking to a small set of reasonably chosen design decisions, I would have liked to trade some of the comprehensiveness on the model-size experiments for a broader look at some other hyperparameters, such as the method for creating the *detox* model (there are both more effective efficient fine-tuning methods like LoRA, and cheaper, more straightforward non-fine-tuning methods like plain-old prompting).

### Questions
No major questions.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new way to detoxify language models using contrastive decoding, where the output probabilities of the base language model are negated by the probabilities of a language model trained on toxic data. The authors show that their techniques outperform a number of detoxification baselines for both toxicity reduction and fluency.

### Strengths
* The authors show that their technique enables toxicity reduction at many model sizes and for both GPT-2/LLaMA model families
* The technique is relatively straightforward and efficient

### Weaknesses
 * The method seems like a pretty minor change from Liu et al 2021's DEXPERTS. As the authors note, their technique operate on the probabilities space, while the DEXPERTS technique operates in logits. Other than that, I can't find much difference. Their technique provides what looks like small gains over the DEXPERTS technique under their metrics. I would appreciate more analysis for why their formulation is preferable over DEXPERTS, and in which cases DEXPERTS might fail that their method would not.
* I would appreciate more qualitative examples of detoxification in the paper.
* I do not see mention of code release.
* Is perplexity the best measure of fluency? I would expect to see some human evaluations of generated text to confirm. 
* I am not sure if most readers are familiar with the "Distinct-2/3" metrics of diversity, I would appreciate a brief explanation of this metric in the paper.

### Questions
Please see weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a parameter efficient decoding time detoxification algorithm. The use a detoxifier, which is another generator that is finetuned on toxic data, to detect the toxic tokens and discount those generations by modifying the probability distribution of the generator. They show good detoxification results on the RealToxicityPrompts benchmark.

### Strengths
- The paper is well written and it is easy to follow.
- The detoxification results on RealToxocityPrompts is very good.
- Ablation studies on the model size is interesting.

### Weaknesses
 - The authors claim that they  "are the first to apply parameter-efficient learning to controllable text generation for detoxification". However, there has been other work (such as ""Exploring the Limits of Domain-Adaptive Training for Detoxifying Large-Scale Language Models" by Wang et al) that use PEFT.
- One of the disadvantages of the proposed method is the cost as it needs both the generator as well as the detoxifier to do inference. The authors do not address this fact when they compare to other methods.
- The effect on fluency, measured by perplexity has been evaluated only on the RealToxicityPrompt dataset. A more diverse set will show boarder impact. 
- The effect of the proposed approach on downstream tasks is not studied and it is not clear how the performance is affected.

### Questions
- In Table 1, what are the perplexity for the original model (alpha = 0)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
