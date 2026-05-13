# Larger language models do in-context learning differently

- Decision: Reject
- Scores: 1, 6, 6, 8, 8

## Abstract
We study how in-context learning (ICL) in language models is affected by semantic priors versus input--label mappings.
We investigate two setups---ICL with flipped labels and ICL with semantically-unrelated labels---across various model families (GPT-3, InstructGPT, Codex, PaLM, and Flan-PaLM).
First, experiments on ICL with flipped labels show that overriding semantic priors is an emergent ability of model scale.
While small language models ignore flipped labels presented in-context and thus rely primarily on semantic priors from pretraining, large models can override semantic priors when presented with in-context exemplars that contradict priors, despite the stronger semantic priors that larger models may hold.
We next study \textit{semantically-unrelated label ICL} (\ticl{}), in which labels are semantically unrelated to their inputs (e.g., foo/bar instead of negative/positive), thereby forcing language models to learn the input--label mappings shown in in-context exemplars in order to perform the task.
The ability to do \ticl{} also emerges primarily with scale, and large-enough language models can even perform linear classification in a \ticl{} setting.
Finally, we evaluate instruction-tuned models and find that instruction tuning strengthens both the use of semantic priors and the capacity to learn input--label mappings, but more of the former.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The following paper analyzes the role of ICL techniques in LLMs when influenced by semantic heuristics. The authors anialkize We analyzed two setups -- ICL with inverted labels and ICL with semantically unrelated labels -- in different model families. The major findings point out that there are spiccatr abilities beyond semantics in models with more paramenters while. So the authors also study instruction-tuned models by observing that semantic heuristics can have effects even in low-scale models.

### Strengths
The paper is very interesting and argues hot topics however although the experiments are exhaustive they are not best introduced and could be discussed in more detail.

### Weaknesses
The paper does not expose scientific novelty.

Although the experiments and the (slightly crude) discussion are good, these experiments or something similar has been presented here before: https://neurips.cc/virtual/2023/76728.

I would be grateful to the authors if they could highlight the new paper's substantial improvements.

### Questions
Please read the Weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The study investigates the effects of semantic priors versus input-label mappings on in-context learning (ICL) in language models, exploring two scenarios: ICL with flipped labels and ICL with semantically unrelated labels. The findings reveal that large language models demonstrate an emergent ability to override semantic priors when presented with contradicting in-context examples, a capability that smaller models lack. Additionally, the study introduces semantically-unrelated label ICL (SUL-ICL), where models must learn input-label mappings from in-context examples. This ability also emerges with model scale, with larger models capable of performing linear classification in SUL-ICL settings. Finally, evaluation of instruction-tuned models indicates that instruction tuning enhances the reliance on semantic priors and improves the ability to learn input-label mappings, though it primarily strengthens the former.

### Strengths
1.	This paper is well-written. The major analysis point is clear and the experimental design makes sense to me. A large number of experiments are conducted in this paper to support the point that the ability to override the semantic prior trained during the pretraining process and learn new input-label mappings from the context emerges with larger scales.

2.	The analysis part about instruction-tuned models that they are worse at overriding the semantic priors is quite surprising and could inform people about the two-side effect of the instruction tuning.

### Weaknesses
1.	As mentioned in the limitations, more experiments on the generation tasks could make this paper stronger. One possible way would be inserting wrong/different facts from the semantic prior and see if the model would respond based on the newly inserted facts. It's unclear if the observed behavior in classification tasks would directly translate to more complex generation scenarios, where the interplay between semantic priors and in-context examples might be more nuanced. For example, in a summarization task, would a model presented with contradictory facts in the prompt still override its pre-existing knowledge, or would it attempt to reconcile the conflicting information in a more sophisticated way? The current study primarily focuses on classification, and extending the analysis to generation would provide a more comprehensive understanding of the phenomenon.

2.	I’m curious if the conclusions about the sizes would still stand in the newly trained LLMs with better structures and training corpus. It is difficult to tell if this behavior is really directly related to the model sizes or if it could be also affected/changed by other factors/techniques.  Some results on the Llama3, Mistral, or Qwen models could better prove the authors’ point. The paper's conclusions are primarily based on scaling within specific model families, and it's not entirely clear if these findings generalize to models trained with different architectures or on different datasets. For instance, models with enhanced attention mechanisms or those trained with a greater emphasis on factual accuracy might exhibit different patterns of semantic prior overriding. The current study doesn't explore these potential confounding factors.

3.	I am still not fully convinced about the practical value of the findings in this paper even after reading the FAQs in the appendix part. Considering the behavior of semantic prior overriding could be both beneficial (manipulate existing knowledge) and harmful (noise or false knowledge in the content), I think a section discussing how to control the behavior of overriding the semantic priors generally (or separately for small and large language models) could make this paper stronger by providing more controllability to the current LLMs. The paper highlights the emergent ability to override semantic priors, but it lacks a discussion on how this behavior can be controlled or modulated. In practical applications, it's crucial to have mechanisms to either encourage or discourage this overriding behavior depending on the specific use case. The current study does not address this aspect.

### Questions
1.	Could the behavior of overriding semantic prior be acquired not only by using larger models but also by using better training techniques and corpus?

2.	Are there any methods to control the semantic-prior overriding behavior in different cases (e.g., could we make larger models perform less in this way or vice versa? )? The practical value would be largely decreased if only larger or smaller language models could behave in one specific way.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides an analysis of the in-context learning abilities of models of different families, sizes, and training strategies (instruction-tuned vs non). Three ICL settings are explored: regular, flipped label, and semantically unrelated labels. Prior studies show mixed results regarding whether models primarily use prior semantic knowledge from pertaining or truly learn from inference-time examples. The current paper provides experimental results which show that smaller models rely more heavily on prior knowledge and are less capable of true ICL compared to larger models, and that instruction tuning seems to increase both ICL and the use of semantic priors.

### Strengths
The study provides a lot of data regarding their research questions. A wide variety of models and data are tested, and the analysis is both focused and rich. Some may say that the results are “obvious” given our experience of ICL, but the study seems to be thorough and if published will serve as evidence for arguments about ICL and scale which are currently made based on anecdotes.

### Weaknesses
Some in the ICLR community may find the results too obvious to justify giving them space at the conference.

### Questions
Is there any way to disentangle a model’s robustness to noisy input from reliance on semantic priors? The settings where greater than 0 but fewer than 100% of example labels are flipped might be interpreted in this way: The models learn the “true problem” they must solve from the regular examples and treat the flipped label examples as noise. One option would be to include an experiment comparing a model given N regular examples vs one given N regular and M flipped examples for various N and M.

### Soundness
4

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
The authors present a comprehensive study on the effect of semantic prior in In-Context Learning (ICL) settings. They use several classification tasks to measure ICL performance, designing four experiments:

1. Regular ICL
2. Flipped ICL: The authors flip a percentage of the labels in the context. They observe that larger models flip their answers more often. The authors conclude that larger models are less tied to their semantic priors.
3. Unrelated ICL: They swap the labels with semantically unrelated labels (e.g., yes/no --> foo/bar). They observe that larger models are more robust to this change. Surprisingly, instruct-tuned models are less robust to this change.
4. Linear classification: The authors evaluate the ICL performance of the models on high-dimensional (from 16 to 64) linear classification problems. Larger models perform better on these tasks.

### Strengths
- The authors present their work in a clear and concise manner.
- The experiments are well-designed, and the results are well-presented.
- The appendix is well-structured and provides additional information on the experiments.
- The experiments are comprehensive, spanning multiple datasets, architectures, and models.
- The studied phenomenon is interesting and highly relevant.y

### Weaknesses
The title is somewhat of an overstatement. The authors provide convincing evidence that larger models are better at ICL, but they do not provide evidence that these models do something fundamentally different from their smaller counterparts. A title like "Larger Language Models are Better In-Context Learners" or "Larger Language Models Are Less Tied to Semantic Priors" might be more appropriate.

While the authors perform a comprehensive study of the phenomenon (which is extremely valuable), they draw very few conclusions from the experiments. It would have been interesting to see a more in-depth analysis of WHY larger models are less tied to their semantic priors, or WHY instruct-tuned models become more tied to their semantic priors. However, the authors limit themselves to observing these phenomena without investigating their causes. To be fair, these additions may be slightly out of scope for the paper.

In section 6, the authors perform the ICL linear classification experiment. This is an interesting experiment, but most of the results are relegated to the appendix (Section D.4). Since the appendix section is relatively small, and the authors have another page to spare, I would suggest moving the results to the main paper. (Of course, the authors should prioritize the requests of other reviewers which may suggest more experiments.)

### Questions
This is evidently a very well-written and thoroughly investigated paper. My only reservation lies in the title, which I believe overstates the results of the paper. I am willing to increase my score if the authors agree to this small request.

I hope the authors find this review helpful. I am looking forward to reading the final version of the paper.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors study the role of semantic priors in in-context learning. In order to do so, they study modified in-context learning settings in which the labels of the examples are flipped (flipped ICL) and in which the labels are replaced with semantically unrelated labels (SUL-ICL). 

These experiments show that smaller models tend to stick to the same response as vanilla ICL when presented with flipped ICL examples. This shows that they ignore the concrete input-output examples in the prompt and instead stick to their semantic prior. In contrast, large models pick up the pattern present in the input-output examples and respond in the flipped way.

Similarly, they show that while small models don't benefit from an increased number of demonstrations in the SUL-ICL setting, larger models do. 

Using the same settings they show that instruction tuned models stick more to their semantic priors in flipped ICL but also are better at picking up the pattern in the few shot examples in SUL-ICL.

### Strengths
The authors shed new light on in-context learning. Their modified ICL settings can help to disambiguate in-between looking up the right task vector (c.f. [1]) versus performing actual in-context learning. They refer to what I just called "looking up the right task vector" as sticking to the semantic prior.

Thereby, they demonstrate that larger models are required for actual ICL in the sense of incorporating the pattern present in the input-output examples into the LLMs repsonse.

The authors study many different model families across a variety of ICL tasks.


[1] https://arxiv.org/abs/2310.15213

### Weaknesses
The writing could be improved. E.g., the notion of semantic priors could be introduced earlier (maybe already in abstract) and in more detail (maybe in the introduction). The model names in the figure captions should be augmented with their respective size for easier readability for readers that don't know all the model name - model size combinations across the studied model families by heart.

The section about performing high-dimensional classification tasks via in-context learning somehow comes a bit out of the blue and is not nicely incorporated into the flow of the remaining paper.

As acknowledged by the authors in the limitation section the sample size of 100 per ICL task variant & model combination is rather small. Maybe to make sure the discovered trends are robust it would be worthwhile to do 1000 samples for one of the model families (as a reasonable trade-off between scientific insight and experimental cost).

### Questions
Do you think that studying the models of different sizes through the lens of mechanistic interpretability on the introduced ICL variations could provide valuable insight into the difference in behaviour in-between small and large models?

### Soundness
3

### Presentation
3

### Contribution
3
