# Instruction Following without Instruction Tuning

- Decision: Reject
- Avg Score: 6.00
- Scores: 3, 5, 10, 6

## Abstract
Instruction tuning commonly means finetuning a language model on instruction-response pairs.
We discover two forms of adaptation (tuning) that are deficient compared to instruction tuning, yet still yield instruction following; we call this \textit{implicit instruction tuning}.
We first find that instruction-response pairs are not necessary: training solely on \textit{responses}, without \emph{any} corresponding instructions, yields instruction following. 
This suggests pretrained models have an instruction-response mapping which is revealed by teaching the model the desired distribution of responses.
However, we then find it's not necessary to teach the desired distribution of responses: instruction-response training on narrow-domain data like poetry still leads to broad instruction-following behavior like recipe generation.
In particular, when instructions are very different from those in the narrow finetuning domain, models' responses do not adhere to the style of the finetuning domain.
To begin to explain implicit instruction tuning, we hypothesize that very simple changes to a language model's distribution yield instruction following.
We support this by \textit{hand-writing} a rule-based language model which yields instruction following in a product-of-experts with a pretrained model.
The rules are to slowly increase the probability of ending the sequence, penalize repetition, and uniformly change 15 words' probabilities.
In summary, adaptations made without being designed to yield instruction following can do so \textit{implicitly}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on exploration of approaches to enable LLM’s instruction following capabilities without instruction tuning. It discusses three different approaches including training solely on responses, instruction-response training on narrow-domain data, and changing a model’s distribution to yield instruction following. Though studying an interesting direction not widely adopted by main-stream approaches, the paper still has multiple drawbacks.

### Strengths
The phenomenon of instruction following without LLM post-training is observed in practice. It would be interesting to find the root cause or theoretical foundation of such phenomenon.

### Weaknesses
1. All three approaches explored in this paper perform significantly worse than their comparable instruction-tuned versions in terms of win rates against the instruction-tuned models. It is unclear about the motivation of this work from the practical aspect.

2. Besides missing practical motivation, the paper lacks theoretical analysis or parameter-level insight on why response-only tuning, narrow-domain instruction tuning, or distribution perturbation of certain tokens helps on instruction following as claimed in the paper. Some related work discussing how instructing tuning modifies LLMs could be referred to for this line of study.

3. It is still unclear whether the instruction following capability has already been partially obtained through pretraining. Indeed, the experiments with OLMo, in which no instruction-tuning data was intentionally included in its pretraining, show similar conclusions as the experiments with Llama-2. However, existing pretraining corpus could include instruction tuning components from contents like human dialogues from novels, question-answer pairs from websites, etc. It requires careful investigation on the roles of pretraining, instruction tuning, as well as preference learning to reach persuasive conclusions about LLM’s instruction following capability.

### Questions
None.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes that the instruction-following ability can be obtained without explicitly using instruction. It presents findings that models can follow instructions when trained only on response data, without explicit pairing with instructions. Additionally, single-task finetuning—training on narrow data domains like poetry or coding—also elicits broad instruction-following behavior across different tasks, such as recipe generation. The study also introduces a rule-based approach with simple modifications, showing that small changes to a language model’s distribution can yield instruction-following capabilities. This work challenges traditional views on instruction tuning, suggesting that implicit methods can lead to general instruction-following, raising questions about the necessity of explicit instruction tuning in developing adaptable, instruction-capable language models​

### Strengths
1. The phenomenon proposed by this paper, Instruction Following without Instruction Tuning, is novel and interesting. 
2. This paper is well-written, easy to follow, and explicitly illustrates the points that might lead to misunderstanding, e.g. the definition of instruction-following behavior in line 183; the use of templates in line 178; and the potential rephrasing in line 280.

### Weaknesses
1. This paper tries to reveal a transformative finding in the area of Instruction Tuning, while the experiments conducted in this paper are too limited to support the finding: 
(1) Only 2 LLMs are experimented, and all of them are slightly out-dated. Although as mentioned in line 101, the authors use these 2 LLMs because it is common to include instruction-tuning data during pretraining in modern days, only presenting results on 2 LLMs is still so limited. It gives the impression that your finding is only useful for slightly earlier LLMs. 
(2) For the response-tuning setting, only the LIMA dataset is utilized, which is also really limited. How can we know whether the instruction-following ability you mentioned can only be derived from the LIMA dataset? The LIMA dataset has some unique characteristics, e.g. all of them are long and deal with complex instructions. What if standard instruction data is utilized? What if the datasets used in single-task fine-tuning settings are used in response tuning?     
(3) Only the AlpacaEval metric is used to judge if the model has the instruction-following ability, which is not enough and is potentially biased.

2. Related to the previous point, I think this phenomenon (response tuning to get instruction-following ability) might probably only work for some types of tasks. For example, if you only finetune the response on your Chess task, I don’t think the LLM can obtain a reasonable instruction-following ability. Thus more detailed experiments and discussion should be provided. 

3. The definition of instruction-following behavior in line 183 is not convincing to me and your experiments of rule-based response adapter actually deepened my suspect: If doing Slowly upweight EOS, Uniform token changes, and Encourage word diversity leads to better win rates, how can you ensure the gain on win rates is caused by real instruction-following ability or the drawbacks of this evaluation metric, which will give higher scores as long as the output is long and diverse. I think more controlled experiments and discussions are required for this part.

### Questions
1. More response examples should be provided for all the settings including response tuning, single-task tuning, and rule-based tuning.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper conducts an exploration of instruction tuning of large language models (LLMs) in three progressively deeper layers. Firstly, the authors present what appears to be a radical conclusion—that fine-tuning solely on the answers while disregarding the instructions can significantly enhance the model's ability to follow instructions. Following this surprising conclusion, the authors further emphasize that the effectiveness of this "response tuning" method has no necessary correlation with the diversity of responses. In certain tasks, even employing extremely narrow, single-task responses for fine-tuning can improve the model's instruction-following performance. Finally, the authors provide their ultimate conclusion: this implicit instruction tuning method merely requires a slight adjustment in the model’s parameter distribution. The authors developed a rule-based language model and found that minimal alterations to the model’s output distribution can achieve remarkable improvements in instruction-following capabilities.

### Strengths
This is undeniably an exemplary piece of work. The authors courageously put forward a new paradigm for instruction tuning and meticulously present their arguments in a step-by-step manner.

From a conceptual perspective, the conclusions of this paper have significantly transformed my understanding of instruction following. The authors demonstrate that instruction following can largely be accomplished by directly optimizing the response, and that these responses need not overly emphasize diversity.

From an experimental standpoint, I highly appreciate the extensive experiments carried out by the authors. Naturally, I will add some of my personal viewpoints in the "weaknesses" section.

Regarding the writing, I must apologize that I did not find the abstract particularly fluent to read. However, the instruction section is exceptionally well-written. The step-by-step, question-and-answer format is particularly captivating.

### Weaknesses
I have several minor suggestions regarding this paper. However, these suggestions by no means diminish its outstanding merits.

Firstly, as previously mentioned, the experimental section requires further consideration. At this year's International Conference on Machine Learning (ICML), Allen Zeyuan Zhu presented his work titled "The Pythics of Language Models." In this work, he maintained extremely strict control over variables from the pretraining phase, ensuring that there was no overlap or interference between the pretraining data and the data used for fine-tuning. Given that the conclusions of this paper are similarly groundbreaking, I suggest that, if resources permit, the authors could consider controlling variables from the pretraining phase. This would alleviate concerns about potential interference from the pretraining data of the LLaMA model affecting the conclusions. Naturally, pretraining costs are extremely high, and I do not consider this a shortcoming on the part of the authors. Nevertheless, conducting experiments using a wider range of base models might render the conclusions more robust.

Additionally, in the section on single-task tuning, although the conclusions are quite remarkable, I believe that the discussion of two exceptional datasets (one of which pertains to chess) could be enhanced.

Finally, I found the abstract to be less engaging than the introduction.

### Questions
There are no specific questions. Kindly refer to the weakness. Additionally, ICLR does not have a best paper nomination. However, I consider this work worthy.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper ran a comprehensive ablation study on instruction tuning, testing out several dimensions of the original instruction tuning design --- (1) tune conditionally on prompt? (2) tune over all tasks? (3) even tuning? The results show that current instruction tuning is kind of an overkill, thus suggesting finding simpler and more principled post-training techniques.

### Strengths
+ The object of study lies at the central place of post-training technique. I find the selected problem important and fundamental. 
+ The article provides new insights into the post-training process, along with literature like LIMA, that post-training process could be more lightweight than we assume currently. The caveat in the conclusion is also important and worth highlighting that both adding AND removing behaviors picked up in pretraining is difficult.

### Weaknesses
 + Experiments are well designed and insightful. Even though, I wonder whether the inclusion of other instruction following benchmarks could add to the solidness of the results, e.g. MT Bench, or Arena hard.
+ Worth noting that none of the ablated methods out-performs original instruction tuning. Therefore, this paper is not contributing new techniques to the field, as intended. Maybe introducing another dimension of measurement could be useful, e.g., language distribution drift to pretrained model, or alignment tax as measured by drop of performance on capability benchmarks.

### Questions
NA

### Soundness
4

### Presentation
4

### Contribution
3
