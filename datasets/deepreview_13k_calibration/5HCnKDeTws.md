# When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 5, 8

## Abstract
While large language models (LLMs) often adopt \textit{finetuning} to unlock their capabilities for downstream applications, our understanding on the inductive biases (especially the scaling properties) of different finetuning methods is still limited. To fill this gap, we conduct systematic experiments studying whether and how different scaling factors, including LLM model size, pretraining data size, new finetuning parameter size and finetuning data size, affect the finetuning performance. We consider two types of finetuning -- full-model tuning (\fmt) and parameter efficient tuning (\pet, including prompt tuning and \lora), and explore their scaling behaviors in the data-limited regime where the LLM model size substantially outweighs the finetuning data size. Based on two sets of pretrained bilingual LLMs from 1B to 16B and experiments on bilingual machine translation and multilingual summarization benchmarks, we find that 1) LLM finetuning follows a power-based multiplicative joint scaling law between finetuning data size and each other scaling factor; 2) LLM finetuning benefits more from LLM model scaling than pretraining data scaling, and \pet parameter scaling is generally ineffective; and 3) the optimal finetuning method is highly task- and finetuning data-dependent. We hope our findings could shed light on understanding, selecting and developing LLM finetuning methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a scaling law for language model fine-tuning. The claim is supported by experiments with fine-tuning in machine translation and summarization tasks. The other scaling factors besides fine-tuning dataset size are LLM size, pretraining data size, and PET parameter sizes for the Prompt Tuning and LoRa fine-tuning regimes. The core finding is that a multiplicative scaling model achieves better fits than a closely additive scaling model.

### Strengths
It's excellent to see scaling law investigations extended to fine-tuning, where they can potentially provide a lot of practical value.

The paper is generally clear and direct, and the experimental findings are quite rich.

### Weaknesses
The precise nature and strength of the findings is difficult for me to discern, and I am not sure of the value of this result for fine-tuning work. All of this leaves me concerned about the paper, but I am open-minded. I am going to express my concerns as questions and see what the answers are.

1. Table 2 shows that the multiplicative scaling is better than the additive one for WMT14 En-De. However, the multiplicative model seems strictly more expressive than the additive one, so I am not sure this is surprising. Why not add even more terms for even more expressivity? Can there be, and should there be, some controlling for the complexity of the law itself?

2. Where are the counterparts of Table 2 for the other tasks and other metrics (besides perplexity)? My apologies if I am overlooking something in the paper. It seems like these other numbers would be given prominently.

3. The paper does say that the BLEURT-RougeL picture "shows high correlation with the PPL scores in general", but eye-balling Figure 7 in the appendix doesn't support this too well, though it's easy to imagine that the quantitative picture is different. But what is the quantitative picture?

4. The promise of the paper is that the scaling law will provide guidance for people seeking to fine-tune. However, the guidance seems to me that perplexity will generally go down for all methods, but that the best method and precisely ideal stopping point will be highly variable. This guidance is very familiar and doesn't need to be characterized with a "scaling law". Is there more specific guidance implicit in this work?

### Questions
1. Table 2 shows that the multiplicative scaling is better than the additive one for WMT14 En-De. However, the multiplicative model seems strictly more expressive than the additive one, so I am not sure this is surprising. Why not add even more terms for even more expressivity? Can there be, and should there be, some controlling for the complexity of the law itself?

2. Where are the counterparts of Table 2 for the other tasks and other metrics (besides perplexity)? My apologies if I am overlooking something in the paper. It seems like these other numbers would be given prominently.

3. The paper does say that the BLEURT-RougeL picture "shows high correlation with the PPL scores in general", but eye-balling Figure 7 in the appendix doesn't support this too well, though it's easy to imagine that the quantitative picture is different. But what is the quantitative picture?

4. The promise of the paper is that the scaling law will provide guidance for people seeking to fine-tune. However, the guidance seems to me that perplexity will generally go down for all methods, but that the best method and precisely ideal stopping point will be highly variable. This guidance is very familiar and doesn't need to be characterized with a "scaling law". Is there more specific guidance implicit in this work?

__The authors gave thoughtful answers to the above questions, which helped me understand the work better, and I raised my score by 1 point in response.__

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work provides a set of simple but extensive scaling law experiments on comparing pretraining, fine-tuning, and parameter-efficient tuning LLMs on translation and summarization tasks.

### Strengths
- This work provides a set of straightforward and well-motivated set of experiments.  The authors are clear where there are reasonable scaling patterns, and cases where there is no discernible pattern.

### Weaknesses
 - Some typographical/grammar mistakes. E.g. "propmt" in Figure 2, "infers" rather than "implies", "there exits a critical point" etc
- It is unclear to me if the set of tasks chosen (translation, and multi-lingual summarization) are representative of broader applications of fine-tuning. However, I think the results stand on their own for this set of narrow applications at least.
- The lack of clarity regarding the specific model sizes used in Figures 2, 3, and 4 makes it difficult to fully assess the scaling behavior. The experiments in Figures 3 and 4, in particular, seem limited by the exclusive use of a 1B parameter model, potentially missing interesting trends that might emerge with larger models.
- Figure 5's interpretation of the 'critical point' is ambiguous. It's not immediately clear whether this point represents a performance crossover or a more nuanced relationship between the compared methods. The description lacks sufficient detail to understand the practical implications of these critical points.

### Questions
- What model sizes are used in Figures 2/3/4?
- Figure 5 is unclear to me. Does the critical point refer to when A outperforms B in "A vs B"?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper describe a multiplicative joint scaling law, considering different factors including LLM model size, pretraining data size, finetuning data size, PET parameter size, on machine translation and summarization tasks.

### Strengths
- The paper introduces a multiplicative joint scaling law and offers comprehensive experiments to empirically demonstrate that this law applies to both machine translation and summarization.
- This paper provides insightful observations regarding fine-tuning, especially parameter-efficient fine-tuning (PEFT) which I think is the most interesting part for the community now, and its relationship with parameter or data size scaling laws.

### Weaknesses
Minor:
-The paper evaluates only MT and summarization. Including more tasks or languages, particularly low-resource translations, would enhance the paper's comprehensiveness.
Major:

Major:
-Regrettably, it seems that the proposed scaling law may exhibit a significant mismatch for parameter-efficient fine-tuning when the model size is 16B. This raises concerns about the law's applicability to larger models, especially those of 70B or exceeding 100B in size.
-The paper omits some details regarding model training. Conventionally, MT models employ an encoder-decoder architecture. I believe all models in this study are decoder-only. How did the authors approach training with a decoder-only architecture for MT tasks? How might this differ from the scaling laws when using an encoder-decoder model? What prompts were utilized for MT training?

### Questions
Please see weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper examines scaling laws for LLM adaptation methods (finetuning, PET like LoRA and PT), where the LLMs were trained on two different machine translation corpora (En->ZH and EN->De) and adapted to either the other translation task, or article summarization in an unseen language.
The paper is primarily empirical, and the goal is to fit scaling laws and identify general trends that could transfer across problem domains (e.g. vision, multimodal, etc).

### Strengths
### Overall
The paper is clearly written. The methodology is generally explicit, and the authors do a good job of interpreting the (many) experiments in the paper.

The figures are clear and well-organized. 

Excellent references to existing work in identifying scaling laws.

### Experiments
The experimental results are somewhat expected (given enough data, use FMT, with limited data, use PT or LoRA). The authors do a good job of explaining and justifying these conclusions given experimental evidence, with the appropriate amount of uncertainty given the noisiness of the data. I think that correctly calibrating the uncertainty is a great strength of the paper. 

Excellent analysis of scaling different axes (pretraining data, model size, finetuning data)

### Weaknesses
### Experiments
#### Fig 2:
Given the poor extrapolation to the 16B model, I'd like to understand the cause -- i.e. is this the right form of the equation, or does this multiplicative scaling break down at larger parameter counts?
One way to test this might be to compare the fit by including 16B in the fitting procedure, vs excluding it. It would also be helpful to see the actual data points plotted alongside the fitted curves to better assess the quality of the fit, especially in the regions where the extrapolation is poor. Furthermore, it would be beneficial to explore alternative functional forms for the scaling laws, such as power laws with offsets or logarithmic terms, to see if they provide a better fit to the data, particularly for the 16B model.

#### Fig 4:
I liked the analysis of scaling to larger PET settings (LoRA and PT in Fig 4). Since the datasets seem to support up to 1e-6 and 1e-7 training sentences, I wish the authors had compared the scaling on even larger finetuning datasets to enable direct comparison to FMT in Figure 3. Specifically, it would be valuable to see if the performance of PET methods continues to improve with larger datasets or if they plateau, and how this compares to the scaling behavior of FMT. This would require extending the x-axis of Figure 4 to match the range of Figure 3, and it would provide a more comprehensive comparison of the different adaptation methods.

#### Fig 5
I didn't really understand Figure 5. My my understanding is that the figure analyzes the fitted power laws, and the x-y- point indicates the estimated amount of finetuning necessary to achieve the performance parity between the two approaches at different model sizes. Does the ordering here matter (e.g. FMT vs LoRA, or LoRA vs FMT) -- my understanding is that it should not. It would be helpful to clarify the axes of this plot and the precise meaning of the x-y coordinates. It's unclear what the practical implications of this analysis are, and how it helps to choose between different adaptation methods. A more detailed explanation of the figure and its interpretation would be beneficial.



### Questions
- How does zero-shot evaluation work in Figure 7? If the source language is unseen, how is the model able to get nontrivial performance on the task?

### Typos:
- P4 footnote: is pretty week → pretty weak
- Fig 2. center column: Propmt → Prompt

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
