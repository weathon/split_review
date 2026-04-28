# Understanding Catastrophic Forgetting in Language Models via Implicit Inference

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 8, 3

## Abstract
We lack a systematic understanding of the effects of fine-tuning (via methods such as instruction-tuning or reinforcement learning from human feedback), particularly on tasks outside the narrow fine-tuning distribution. In a simplified scenario, we demonstrate that improving performance on tasks within the fine-tuning data distribution comes at the expense of capabilities on other tasks. We hypothesize that language models implicitly infer the task of the prompt and that fine-tuning skews this inference towards tasks in the fine-tuning distribution. To test this, we propose \emph{Conjugate Prompting}, which artificially makes the task look farther from the fine-tuning distribution while requiring the same capability, and we find that this recovers some of the pretraining capabilities in our synthetic setup. Since real-world fine-tuning distributions are predominantly English, we apply conjugate prompting to recover pretrained capabilities in LLMs by simply translating the prompts to different languages. This allows us to recover in-context learning abilities lost via instruction tuning, natural reasoning capability lost during code fine-tuning, and, more concerningly, harmful content generation suppressed by safety fine-tuning in chatbots like ChatGPT.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A significant real-world problem with fine-tuned language models is the risk of the model forgetting how to perform tasks that it initially could handle. The authors found that fine-tuned models tend to perform more like their pre-trained counterparts on tasks that are far from the fine-tuning distribution. To address this, they introduce a method called Conjugate Prompting, which helps recover the pre-trained model's behavior by mitigating changes in implicit task inference. Five models and four non-English languages, with two additional transformations, demonstrate the effectiveness of this method.

### Strengths
1.	Well-written paper - clear and easy to read.
2.	The synthetic setup provides compelling evidence illustrating the trade-off resulting from fine-tuning and pre-training stages, specifically addressing the issue of catastrophic forgetting. The robustness of this analysis adds to the paper's credibility.
3.	Conjugate Prompting is simple but effective. The experiments conducted to validate this method are convincing, highlighting its practicality and potential benefits.

### Weaknesses
1.    In Section 2, the authors mentioned that the trade-off is less significant as the dataset size increases. Is this phenomenon consistent with the further expansion of the dataset, or is it merely an incidental occurrence specific to some certain smaller models?
2.    As the authors pointed out in the limitations section, this method would benefit from further validation and application in various domains and tasks involved.
3. In Section 2, the authors fine-tuned a GPT-2 model and explored the phenomenon of trade-offs. However, it remains unclear whether this phenomenon is consistent across larger-scale language models or exhibits significant variations in performance improvements for different tasks, especially during the fine-tuning process. Are these differences in trade-offs related to the complexity or similarity of the tasks involved?

### Questions
In Section 2, the authors fine-tuned a GPT-2 model and explored the phenomenon of trade-offs. However, it remains unclear whether this phenomenon is consistent across larger-scale language models or exhibits significant variations in performance improvements for different tasks, especially during the fine-tuning process. Are these differences in trade-offs related to the complexity or similarity of the tasks involved?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the effect of finetuning on pretrained transformer model's capabilities. The study is mostly empirically, involving both synthetic toy tasks on smaller transformers and more realistic tasks on medium size models. 

The key proposition of the paper is
1) Finetuning harms pretrained capabilities as an interference effect, especially on inputs that are somewhat close but not the same as the finetuning data distribution.

2) It is possible to alleviate this effect by manually make the prompt more dissimilar to the finetuned distribution but keep their underlying sematics, for example by translating them to different numerical regimes or different languages.

### Strengths
The paper studies an important phenomenon - the effect of finetuning, in the setting of transformers / language models. These are main-stream practices in the field and will enjoy broad interests in the results.

The propositions of the paper are reasonable and are adequately supported by their empirical results. 

The quantitative result on the impact of instruction tuning on ICL is particularly interesting. 

The synthetic experiments are interesting and provide a toy case that can be understood better. In addition, the synthetic experiment also provides a simple framework that can be somewhat useful for real-world situations.

The paper is in general well-written.

### Weaknesses
The paper try to emphasize the difference between "forgetting" and "suppressing" of the pretrained capabilities. However this distinction might be spurious. For example, even though the English instruction tuned model may still be able to do an ICL task in Spanish, this does not mean that it did not "forget" how to do this task in English. The core issue is that the model's ability to perform ICL in English has been degraded, regardless of whether the capability is still latent and accessible through a different prompt. The paper's framing could be misleading, as it suggests a fundamental difference where one may not exist. The model's performance on the original task is what matters, and that has clearly been reduced.

The method of proposed by the paper (re-formatting prompts) is a good simple trick that can be quickly applied to alleviate some forgetting. However it does not seem to attack the core of the problem, which is the fundamental over-specialization of the model onto the finetuning data. This over-specialization is a well-known issue in fine-tuning, and the paper's method, while practical, doesn't address the underlying mechanism of why this occurs. It is more of a band-aid solution than a fundamental fix. While the analysis is useful, the proposed solution is not novel.

The synthetic task is too simple - different tasks there simply correspond to different linear weights, while pretraining vs finetuning are just different prior distribution of those weights. It might be beneficial to expand that - even in the regression setups - to e.g. higher order functions (quadratic, quartic etc), such that the transformer model's ability to generalize across a diverse set of tasks in pretraining, and how this could be changed by finetuning, can be tested better. The current setup does not fully capture the complexity of real-world tasks and the generalization challenges that arise during fine-tuning. The simplicity of the synthetic task limits the conclusions that can be drawn about the behavior of models on more complex tasks.

The related works section is somewhat thin. The paper might benefit from a more in-depth discussion of closely related works on forgetting in the field of transformer language models, particularly related to the effect of finetuning and ICL. For example: arxiv 2211.00635.

### Questions
Similar to the synthetic task, what happens if at the instruction-tuning stage, the fine tuning task is multi-task trained together with the pretraining task with different mixing weights, how would this change the behavior? 

How do the behaviors observed scale with model size? Previous work (https://openreview.net/forum?id=GhVS8_yPeEa) has found that the forgetting becomes less of a problem when the model scales bigger, everything else being equal.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose to use translated prompts to study model behavior after fine-tuning outside of the fine-tuning distribution.

The first section describes a set of synthetic experiments where transformers are asked to learn linear functions, with a setup where the function is sampled from a continuous space of functions or from a fixed set of possibilities. In a single training scenario, Transformers learn both functions well, generalizing appropriately. The authors then train on a mixture of these two setups, showing that the tradeoff Transformer models achieve are quite suboptimal for the discrete setup. This is alleviated by more training on more examples, but the model approaches the Bayes error extremely slowly. The authors find that, unsurprisingly, models trained on the continuous setup and finetuned on the discrete setup rapidly become worse at the continuous setup. Next it is demonstrated that this forgetting is less prominent far from the fine-tuning description. The authors then describe a conceptual model of what they believe is going on—that the model is downweighting a prior of what problem is being solved, and snapping onto the fine-tuning task. Finally, the authors attempt to test this hypothesis by scaling in-context examples for the non-fine-tuned task out of the range of the fine-tuned task. This improves performance, providing evidence that pretrained abilities are not “lost” they are merely down-weighted in the prior of tasks the model presumes examples represent.

The authors go on to present they believe are sufficient conditions for accessing pretraining capabilities not selected-for in fine-tuning via prompting, which they term conjugate prompting. Next, the authors show that when fine-tuned for instruction following, models “forget” how to perform in-context learning, even when the model is prompted to perform ICL. This is interpreted as favoring the hypothesis that fine-tuning is largely changing how models estimate which task is being solved. This is used to motivate translation as a natural method of making prompts that are out-of-distribution for the fine-tuning set, but invertible back into it via translation back into English. The authors find that ICL capabilities can be recovered through translation. In the next subsection a similar experiment shows that models comply with instructions they would otherwise refuse when a similar translation strategy is used.

### Strengths
- The hypothesis is well-motivated, clearly expressed, and well operationalized: does finetuning get rid of tasks, or get rid of the model’s willingness to select certain tasks?
- While the synthetic experiments are somewhat artificial, they show a clear conceptual model of what kind of perturbations we may believe are going on in more realistic scenarios.
- The results are at least initially good evidence that the authors’ hypothesis is true in at least a limited way: models do not learn to up-weight fine-tuned tasks in other languages.

### Weaknesses
 - More experiments should have been conducted on massively pretrained LLMs. The two experimental setups shown appear well considered and interesting, but many questions are raised such as: how much finetuning data is required to see conjugate prompting make a significant difference? Does this vary with model size significantly? Does this work the same across all tasks? A single paper cannot answer all of these questions, but they are not even acknowledged, and the lack of experiments addressing any of these variables makes the evidence somewhat thin.
- The synthetic experiments are interesting, but they do relatively little as evidence that this is what should be happening in large language models. I think they are useful, but given the fact that somewhat limited experiments were conducted on true LLMs, and claims are focused in that direction, it feels a little bit lopsided in terms of focus.
- Many descriptions are confusing. For instance in Table 2 it is unclear without significant interpretative discretion by the reader whether percentages represent refusal or lack of refusal. Or in section 2.6 it is stated that “For instance, in Table 1 it is unclear whether languages represent fine-tuning or prompting languages. From context, it becomes clear that this is for prompting, but only with a significant amount of digging. Clearer descriptions are necessary. This is not a minor issue—I had to reread most sections multiple times to understand what they were describing.

### Questions
- “As noted in prior work” on page 3, should really cite other work.
- You never identify IF as “Instruction Following”, while this is guessable from context, it took me a few minutes to figure this out and I recommend you introduce it properly.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a theory of "implicit task inference" to model the behavior of language models in finetuning, which offers an explanation of the phenomenon of catastrophic forgetting. The paper then proposes a "conjugate prompting" technique to recover suppressed pretraining capabilities by making a prompt appear farther from the fine-tuning distribution. The paper uses a synthetic linear regression experiment to validate the proposed theory, and uses a synthetic ICL dataset and adversarial examples to examine the effectiveness of the proposed conjugate prompting technique on language models. Results show that conjugate prompting partially recovers lost ICL performance and harmful content generation of finetuned language models.

### Strengths
* The study introduces a fresh perspective on the issue of catastrophic forgetting through the lens of inferencing task identity. The theoretical formulation is neat and reasonable, showing that adaptation of task probabilities in finetuning is a potential explanation of catastrophic forgetting in language models.
* The proposed conjugate prompting technique is easy to understand and apply. As a simple translation, it is universally applicable to most tasks.  
* The concepts and methods are presented clearly, allowing for easy understanding of the proposed methodology. The graphical visualizations also significantly support the clarity of the presentation.

### Weaknesses
 * The paper's main weakness is the main assumption being restrictive and artificial, therefore failing to reflect the behavior of language models in most realistic settings. The main assumption of the paper (Equation 7) is that the input space of different tasks overlaps, so the model has to do probabilistic inference on the task identity. Both the proposed synthetic regression task and the ICL examples have this overlap. The ICL examples are purposefully designed to make it confusing by including two different instructions. Such examples are adversarial in nature and unlikely to exist in real-world applications of language models, where the task is usually clearly specified in the prompt. For example, the input of the summarization task "Please summarize the following passage: [text]" is very unlikely to be confused with the input of a translation task "Please translate the following passage to English: [text]" given a random passage in place of [text].

  It can also be argued that when the input space of different tasks overlaps, the problem itself is ill-posed as there is not a single correct answer for inputs from the intersection. The failure of finetuned models thus may come from the ambiguity of the task itself rather than from catastrophic forgetting.

* The proposed theory does not seem to explain the main part of catastrophic forgetting. Per the author's theory, if the tasks' input spaces don't overlap, the model does not need to adjust the task probability $g$ (as it would be already close to 1 for a good enough language model), and catastrophic forgetting would be much less if $g$ does not need to be modified. However, catastrophic forgetting is quite ubiquitous in practice for non-overlapping tasks and regardless of how good the language model is. In fact, catastrophic forgetting usually presents even if tasks are strictly non-overlapping (for example, when task identity is explicitly given during inference, referring to "task-incremental continual learning").

* The chosen experiment setting is not typical for catastrophic forgetting: catastrophic forgetting on language models is most clearly manifested in supervised task finetuning (e.g., on GLUE) and unsupervised domain finetuning (e.g., Codex, Minerva). Per my knowledge, there is no clear evidence of  catastrophic forgetting in instruction finetuning and RLHF yet (though forgetting is likely to exist). It would be better to choose a typical setting for evaluating the effectiveness of the proposed method.

* RLHF for alignment is not a good example of forgetting: the goal of alignment is to make the model refuse to answer when given a malicious instruction, rather than making the model forget how to follow harmful instructions. There is yet no generally effective method to make a model forget selected information (referring to "machine unlearning"). Catastrophic forgetting is usually recognized as a side-effect of finetuning and is direction-less (one cannot control exactly what is forgotten).

### Questions
* In section 2.5, what if the model is finetuned on a different set of discrete weights than $\mathcal{D}_{disk}$? Using a different set seems better matching real-world finetuning scenarios.
* It is observed that common LMs perform worse in languages other than English because of being primarily trained on English, so translation to another language is likely to reduce task performance (language gap). How does the reduction in performance because of forgetting compare to the reduction in performance because of the language gap? Would it be worth trading forgetting for the language gap?
* Could there be other kinds of mapping in conjugate prompting other than translation?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
