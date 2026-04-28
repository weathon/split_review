# Response Tuning: Aligning Large Language Models without Instruction

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 8, 5, 5

## Abstract
Instruction tuning---supervised fine-tuning using instruction-response pairs---is a foundational step in transitioning pre-trained Large Language Models (LLMs) into helpful and safe chat assistants.
Our hypothesis is that establishing an adequate output space can enable such a transition given the capabilities inherent in pre-trained LLMs.
To verify this, we propose Response Tuning (\method{}), which eliminates the instruction-conditioning step in instruction tuning and solely focuses on response space supervision.
Our experiments demonstrate that \method{} models, trained only using responses, can effectively respond to a wide range of instructions and exhibit helpfulness comparable to that of their instruction-tuned counterparts.
Furthermore, we observe that controlling the training response distribution can significantly improve their user preference or elicit target behaviors such as refusing assistance for unsafe queries. Our findings illuminate the role of establishing an adequate output space in alignment, highlighting the potential of the extensive inherent capabilities of pre-trained LLMs.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The main question this paper tries to answer is "how much do we lose by tuning just on the responses (response tuning) instead of instruction-response pairs (instruction tuning)". The authors use existing IT datasets and remove instructions from them to get datasets for response tuning. They fine-tune a variety of base-llms (not instruction tuned) and compare IT vs RT. They evaluate instructability with human evaluation, GPT-4 based response quality evaluation and pairwise assessment. They also evaluate core capabilities across standard benchmarks like MMLU, OpenbookQA, HellaSwag, ARC, GSM 8K, PIQA. Across a wide range of experiments, they show that response tuning comes close to instruction tuning. Additionally, they show the application of this method for preference alignment and safety alignment. Finally, they show that a similar trend holds for in-context learning, where using just responses doesn't degrade performance significantly compared to using instruction-response pairs.

### Strengths
* originality - The authors ask a simple question that hasn't been considered from a scientific point of view. "Can we use good responses instead of instruction-response pairs"
* quality - The authors run a wide variety of experiments to make their claim stronger and well substantiated. 
* clarity - The paper is well-written and easy to read. In most places all the necessary details and citations are provided
* significance - There is the scientific question on the source of gains due to instruction tuning. From a practical perspective, this raises the question whether, as a community, we should invest more energy looking at instruction-free response datasets which are free of instruction biases.

### Weaknesses
There are two main concerns regarding the soundness of these experiments

## Leaking instructions to response
The datasets in section 4, 5 and 6 are collected as instruction - response pairs. The data generation process may induce a leak from the instruction to the response. For e.g. if the instruction was "Write an article on the role of dinosaurs in prehistoric ecology", and the response was "Dinosaurs played a significant role in prehistoric ecology ...", the instruction can be inferred based on the response. In a trivial situation, for an instruction "Follow the rules x, y, z", the response could be "following the rules x, y, z, here's the response ...". To argue that one needs only the response (and not the instruction), the authors would need to show that the instruction cannot be trivially inferred from the response. Alternatively, an experiment training on high quality responses gathered without explicit instructions could also prove the point. The current experiments do not adequately address this fundamental issue, as the responses are still fundamentally linked to the instructions, potentially invalidating the core claims of the paper. Even if the responses are stripped of obvious instruction-related phrases, the underlying semantic structure and content are likely to be strongly influenced by the original instruction, making it difficult to isolate the effect of response-only training.

## Training setup (Section 4.1)
The authors use PEFT (QLoRA) but don't give any references that this is a standard setup for instruction tuning. It is possible that a less expressive training scheme (PEFT vs full fine-tuning) suppresses the utility of having instructions in the training data. Alternatively, if they could show that their PEFT-trained IT models are comparable to the best IT models on these datasets, that could alleviate this concern too. The lack of a comparison to fully fine-tuned models raises concerns about whether the observed results are an artifact of the training setup rather than a true reflection of the potential of response tuning. It is crucial to demonstrate that the chosen training method does not inherently disadvantage instruction tuning to make a strong case for the effectiveness of response tuning.

### Questions
My two main questions with potential fixes are indicated in the weaknesses section. Convincing experimental results for the two weaknesses will change my stance on soundness and the overall rating.   

Some suggestions that aren't critical to soundness
* "establishing an output space" is less standard than "establishing an output distribution". The authors do use "distribution" at various places in the paper, so it isn't clear why not use the same standard term everywhere (including the abstract)
* The authors use certain terms that aren't well-defined. 073 - "contextual refusals", 
* line 311 - "some fluctuations" - why are the fluctuations attributed to fine-tuning? if there's a good reason, it should be stated, if not, it is sufficient to state that the numbers are comparable. 
* line 333 - what does the up arrow mean?
* line 428 - what exactly is meant by "pattern matching"?
- Figure 4b - IT win-rate is 60% compared to RT win rate of 40%. This is a big difference but there is no discussion of this negative result in the text. 

The authors consistently use the narrative that "capabilities required to behave as a chat assistant are largely inherent in pre-trained LLMs and can be activated without explicit supervision from instruction-response pairs" (lines 096, 515 and perhaps more). However, there is no direct proof for the "capabilities being inherent in pre-trained LLMs". One can argue that training on responses adds these capabilities that aren't inherent, just like instruction-response pairs are supposedly adding these capabilities. This claim is unnecessary and unsubstantiated. This claim is unnecessarily distracting and I would urge the authors to stay focused on the central claim of response tuning being at-par with instruction tuning.

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
4

### Summary
This paper demonstrates that only fine-tuning base models on the responses in instruction datasets (response tuning, or RT) often results in comparable performance to fine-tuning on the responses *conditioned on the instructions* (traditional instruction tuning, or IT) without losing any core model capabilities. This supports the authors' hypothesis that models have already learned instruction following ability during pretraining, and instruction tuning thus mainly facilitates the model placing higher probabilities on tokens associated with helpful responses at inference time, or what the authors call "aligning the training response distribution". The authors measure response quality using 4 metrics: Likert-style individual response acceptability ratings + pairwise response preference selection using both human annotators and GPT4-as-a-judge. They find results to be consistent across 3 models from different families and on 3 instruction-tuning datasets, and also find that a larger Gemma model closes the gap between RT and IT more than a smaller one.

The authors further investigate whether using an LLM to refine the response quality along dimensions such as clarity, structure, and tone before training improves model response quality (as judged by GPT4), and find a positive result.

Finally, they extend their experimental setting to refusal, and show that only training on responses from refusal/safety datasets (and not the unsafe queries the responses are associated with) also yields comparable performance, without causing the model to over-refuse. This is particularly interesting, because it supports the hypothesis that models learn to identify unsafe queries during pretraining, but need tuning to learn the "language" of refusal.

### Strengths
- Originality: the paper takes a creative approach to an underexplored research question.
- Quality: The paper includes quite extensive experiments to answer 3 main RQs and is not lacking on content. The authors include multiple datasets and models in their analysis. I appreciate that they use both human and model evaluation that is generally well-controlled for biases (e.g., not using the same model/family to evaluate another model); given that both evaluation methods have known shortcomings, their results seem more robust due to the extensive effort given to evaluation.
- Clarity: The paper is generally well-written. Given there are a large amount of experimental results, the authors make good use of the Appendix for additional details while also making sure the main paper is readable and self-contained. I appreciate the delineation of the paper into 3 main sections corresponding to the 3 RQs of interest. Generally comprehensive lit review.
- Significance: The paper provides a useful datapoint an interesting insight to ongoing discussion about what models learn during instruction tuning. While the 2nd RQ is a bit orthogonal to the paper's narrative, the 1st and 3rd RQs are interesting and impactful. I would like to see it presented at the conference.

### Weaknesses
Main:
- My main qualm with the paper is the authors use the word "comparable" liberally when describing the performance of RT and IT tuning. However, in most cases, it is consistently the case that IT outperforms RT, often by what looks like rather substantial margins (e.g., Figures 2 and 4). I agree with the authors that it's really interesting that RT can make up the majority of the gap between the untuned and IT models, but I think the language can be toned down a bit and more discussion given to what performance aspects cannot be solely learned from RT alone. Alternatively, the authors could provide a quantitative definition of what they consider comparable performance.
Similarly, some of the differences in core capabilities (Table 1) seem meaningful (such as +7 on HellaSwag for Gemma 2 and -7 on GSM8k for Llama 3.1), but these are mostly chalked up to being typical or expected noise. It would be valuable to include a line for the untuned/base model in this table as a comparison point.
- The URIAL paper should certainly be discussed in the related work section as it asks a similar RQ and has similar conclusions to this paper (though different methods).
- The authors make a key assumption about the data they instruction- and response-tune on: that it hasn't been included in the pretraining data of the models in a meaningful way. This assumption seems to be supported by the poor performance of the untuned models in, e.g., Figure 2, but it should be stated more concretely.
- Practical impact: from an analysis/model understanding perspective, the paper is strong. The authors do not explain, however, what impacts only training on responses could have from a practical angle. Presumably, it is not cheaper to collect the response data, since human or synthetic data generation pipelines would still require the instructions or refusal query to be present. It could be faster to train the model when one does not have to run inference on the instruction tokens, though the loss computation is the same so this may be minor. I would appreciate some discussion about this, and/or quantitative #s on, e.g., finetuning speed, in the paper.

More minor:
- the authors use a number of terms in their main claims that are a bit vague and deserve proper definition, such as "output/response space", "training response distribution", "behavioral guide" and "inherent attributes" of the response space. I got the gist of what they were saying, but I don't think that should be assumed, and it would be good to be more consistent w/ terminology and more clearly define it.
- the paper could benefit if the authors added some analysis on models with open training data (such as Olmo or Pythia)-- this would allow them to perform a leakage analysis and understand what types of/how much instruction data is present in the pretraining corpus.
- Comparing Figs 3 and 6 it appears that both URIAL and URIAL-R are competitive with RT/IT, which raises the question of **why are we instruction-tuning in the first place?** I would appreciate some clarification of this in the rebuttal.

### Questions
Notes and minor other points:
- How are you testing the models' core capabilities in Table 1-- prompt format, instructions in prompt, greedy decoding, few-shot examples?
- typos line 044: "omits"; line 054 missing "we"; line 082: "guides"; line 092: "focuses"; line 405: missing "the"; line 406: extra "the"
- it would be good to link to the plots for the other models in the Appendix in the caption of each Figure, for reader's easy reference and cross-model comparison.
- related work: would be good to cite https://aclanthology.org/2020.emnlp-main.105/ for cross-task generalization as this was the earliest (?) work
- The authors should mention this concurrent work in a camera-ready: https://arxiv.org/abs/2409.14254
- I didn't find Figs 3/6 to be particularly useful and I am not sure what the 1-5 metric represented is. At a minimum it would be good to make the graphs represent the same metrics so that Figs 3 and 6 can be directly compared. 
- Using the word "significant" to describe results (lines 312, 403) implies you've done statistical testing

### Soundness
3

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
4

### Summary
The article suggests that the model's instruction-following capability can be acquired by fine-tuning using with the response data, and this hypothesis is validated through experiments. Furthermore, the article demonstrates enhanced preference alignment and safety by controlling the response distribution.

### Strengths
1. The article is well-written and highly readable.
2. It presents an interesting hypothesis and proposes a simple yet effective method.
3. Experiments were conducted across various benchmarks.

### Weaknesses
 1. The pre-training data for some models in the experiments not publicly available, and models like Gemma-2 already possess some instruction-following capability. This suggests that the pre-training data may inherently include instruction-response pairs, potentially skewing the experimental results and affecting accuracy. Specifically, the presence of instruction-response pairs in the pre-training data could mean that the observed instruction-following capability after fine-tuning is not solely due to the proposed method, but rather a result of the model's prior exposure to such data. This makes it difficult to isolate the true impact of the response tuning approach.
2. Experimental results show that the performance of Response Tuning still falls short of Instruction Tuning, particularly in human and GPT-4 evaluations. Although this is an interesting finding, deliberately constructing a response set without instructions for training seems neither effective nor efficient. The fact that instruction tuning outperforms response tuning, especially in more complex evaluations, raises questions about the practical utility of response tuning. The method's limited performance suggests that it may not be a viable alternative to instruction tuning, and its significance for advancing research remains questionable.

### Questions
1. Can you conduct similar experiments using models with publicly available pre-training data, such as OLMo, TinyLlama, and Pythia, to validate the conclusion of your article?
2. In Table 1, why does Instruction Tuning perform better on several benchmarks but have a lower overall performance compared to Response Tuning? How is the overall performance in Table 1 calculated? For instance, the arithmetic averages for Response Tuning on these benchmarks are 54.05 and 61.08, so why are they reported as 58.42 and 65.62?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Based on the hypothesis that language models learn to follow instructions during instruction tuning mainly by learning the output space, the paper presents experiments where models are trained only on responses ("Response Tuning" or RT) instead of conditioning them on instructions (the usual "Instruction Tuning" or IT).

RT on various Llama and Gemma models with data from Alpaca, Dolly, and LIMA performs comparable to IT on instruction following (AlpacaEval) and several core capability evaluations (MMLU, OpenbookQA, Hellaswag, ARC, GSM8K, and PIQA).

To further demonstrate the importance of the quality of the responses, the responses from the datasets above are refined using a larger LM, and training on this refined dataset improves AlpacaEval scores in both IT and RT setups.

When trained on LM responses corresponding to safety related refusals, though IT performs better than RT initially, with increasing amounts of data, performance of RT models eventually matches IT.

In an ICL (instead of finetuning) setup as well, it is shown that LMs can be aligned with human preferences using response demonstrations alone, with response-only ICL yielding comparable performance to paired-demonstration ICL in one evaluation setting (https://allenai.github.io/re-align/just_eval.html).

### Strengths
The main finding in this paper is interesting. It provides an insight into how LMs learn to follow instructions. Future work may be able to leverage this insight to improve instruction tuning procedures.

### Weaknesses
## Practical utility
The paper does not demonstrate the practical utility of the finding. It would be helpful in the following cases:

1. Obtaining instruction-response pairs is significantly harder than obtaining responses alone.
2. Training on responses alone is more effective than training on instruction-response pairs.

1 is not true in any of the experimental settings considered in the paper, and 2 is not true in any of the results, at least not significantly.

Suggestions for addressing this concern:

- There may be tasks where 1 is true. Code generation (from natural language instructions) is a good example. Does RT on code, which is much easier to obtain than paired NL-code examples do as well as IT? More generally, tasks with structured outputs that are easy to synthetically generate are suitable here.
- Tasks where the model performance is sensitive to the superficial features in the instructions would be helpful to demonstrate 2. Does RT make the model more robust to variations in instructions than IT in such cases?

## Role of the response refinement experiments
These experiments generally show the importance of the quality of the responses, but it is unclear how this is related to the main hypothesis about conditioning on instructions being unnecessary. Refinement generally helps in both IT and RT and RT settings. It would be more helpful to directly compare IT and RT models with and without response refinement. Does refinement increase the winrate of RT models against IT models?

### Questions
- What is the performance of the base models (Llama 3.1 8B and Gemma 2 9B) on the tasks shown in Table 1?
- (More of a suggestion) It would be easier to interpret the results in Table 3 if all the models (IT and RT with and without response refinement) are evaluated against a fixed reference model for AlpacaEval.

### Soundness
3

### Presentation
3

### Contribution
3
