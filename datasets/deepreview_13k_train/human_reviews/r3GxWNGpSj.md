# XTransplant: A Probe into the Upper Bound Performance of Multilingual Capability in LLMs via Cross-lingual Transplantation

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Current large language models (LLMs) often display significant imbalances in their multilingual capabilities and cultural adaptability, primarily due to their unbalanced and English-centric pretraining data.
For these English-centric LLMs, the disparities between English and non-English languages hinder their ability to utilize their robust English-based capabilities within non-English contexts, while also limiting access to valuable multilingual knowledge derived from non-English "language-specific neurons" within English contexts.
Motivated by this, our work explores the possibility for LLMs to leverage the strengths of both English and non-English languages, aiming to further unlock their multilingual potential.
To this end, we propose a probing method named $\mathcal{X}$Transplant, which directly transplants feed-forward activations from English input to non-English (or from non-English to English) during inference stage, allowing the model to benefit from both English and additional multilingual knowledge.
Through extensive experiments on our pilotsets and representative LLMs across different tasks and languages, we empirically prove that both the multilingual capabilities and cultural adaptability of LLMs hold the potential to be significantly improved by the cross-lingual feed forward transplantation, respectively from $\texttt{En} \rightarrow \texttt{non-En}$ and $\texttt{non-En} \rightarrow \texttt{En}$. 
Additionally, we also establish the upper bound performance of LLMs obtained through $\mathcal{X}$Transplant (relative growth of +80\% in multilingual capabilities, +39\% in cultural adaptability), highlighting the underutilization of current LLMs' multilingual potential. 
We do hope our further analysis and discussion could suggest promising directions for deeply unlocking the multilingual potential of current English-centric LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors propose a new method, XTransplant, to exploit English-based capabilities within non-English contexts using English-centric Large Language Models (LLMs). For this purpose, XTransplant utilizes the feed-forward activations of a decoder layer on English text into a layer of the decoder on non-English input (or from non-English into English) while predicting the first new token. To select optimal pairs of layers in different languages, the authors investigate all possible combinations and their performance, referred to as the instance-aware upper bound in this paper. The experimental results on XNLI, XQuAD, and XCOPA with LLaMA-2-7B-Chat, Mistral-7B-Instruct-v0.3, Qwen2-7B-Instruct, and Chinese-Alpaca-2-7B show that the proposed XTransplant improve the performance under the setting of the instance-aware upper bound.

### Strengths
- In an ideal situation, XTransplant can enhance task-solving performance by accessing the knowledge of centric languages like English.
- In an ideal situation, XTransplant can work on both English- and Chinese-centric LLMs.
- This work investigates all possible pairs of source and target layers.

### Weaknesses
 - In the experiments, the authors compared the upper bound results of XTransplant using the best combination of layers with baseline results. This is unfair and should not be reported as the main result of XTransplant. Reporting the result for analyses is acceptable. Instead, the authors can use the average or median performance in Figure 5 as the main result.
- For fair comparison, the authors need to decide the pair of source and target layers based on the performance of validation data.
- Furthermore, the test set size for each language is limited to 50 instances. This size is quite small. The authors need to consider the variance of the results for each language in such a small setting. Thus, increasing the test set size is required to make the results more reliable.
- When targeting cross-lingual tasks, utilizing machine translation is one of the easiest way. However, such a basic approach is not considered as a baseline in the paper. Instead, the authors concatenate the two different languages in PIM, a baseline approach.
- Considering the computational inefficiency of choosing the upper bound pairs of layers, reporting the computational cost of doing that is also required.

### Questions
- What is the reason for applying XTransplant only when generating the first new token?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The article focuses on the performance of language models in distinct languages and cultural contexts. Past findings show that popular LMs perform much better in English than in other languages, which is caused mainly by the unequal composition of their training data. 
This work considers a trade-off between two options for applying LMs to distinct languages: 1) 
prompt models in English, to use its strong performance in the high-resource language or 2) prompt in the target language, potentially unlocking culture/language-specific information obtained by the model.

To leverage the promises of the two mentioned approaches, the authors propose a new method (UpperBound XTransplant) that patches the latent embedding to improve model performance in multilingual prompt-based tasks. The proposed algorithm finds the pair of layers between which the representation is transferred: from the prompted model to the target language prompted model. A greedy search is performed across N^2 possible pairs (where N is the number of layers) with the objective of finding the pair of layers for which transfer would maximize the probability of predicting a gold answer token.
This simple method offers a significant improvement in solving cross-lingual and cross-cultural tasks but also poses a risk of lurking into the gold answer when modifying the latent representation of the model.

### Strengths
- The authors present an in-depth discussion of the proposed methods, analyzing the statistics across different tasks and providing examples of cross-cultural prompts to demonstrate how the method works on a low level. 


- The scope of experiments is broad and encompasses multiple tasks and models, including an instance of a language model trained on Chinese as a majority language.


- The method achieves significant improvements over the baselines, which is impressive for such a not complicated approach. However, this may be due to the reasons described in the weaknesses.

### Weaknesses
 - My main criticism is based on my strong suspicion that the improvements of the UpperBound method result mainly from lurking into the gold answer, i.e., the test set is used for tuning the methods. One indicator of that is the large improvement in English2English setting, which should not benefit at all from the enhanced cross-lingual transfer. This questionable result puts the whole point of improving multilingual capabilities in doubt. One solution to resolve that would be testing UpperBound with constant layer pairs for each language, e.g., after determining them based on a devset.

- Greedy search comes with a high computational cost of performing O(N^2) additional predictions. The authors mention that this could be alleviated by always pathing from the last layer or to the target layer, this setting should be analyzed in more detail. Another option would be pre-setting layer pairs, as described in the previous point.

- Much less severe criticism is connected to the lack of results for base (i.e. not instructed) models. My guess is that they could be less influenced by the language of the prompt.

### Questions
- Why do you only use En->non-En configuration in cross-lingual tasks and non-En->En in cross-cultural tasks? 

- Did you observe 0.0 accuracy in the English subset of XCOPA for Qwen-2? This score seems dubious in light of the model’s technical report.

### Soundness
1

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
5

### Summary
The paper introduces "XTransplant," a method designed to enhance the multilingual capabilities and cultural adaptability of LLMs by cross-lingual transplantation of feed-forward activations. The paper highlights the unlocking of current LLMs' multilingual potential and suggests promising directions for future research.

### Strengths
The paper introduces the X Transplant method, a novel way to enhance the multilingual capabilities of large language models by cross-lingual transplantation of feed-forward activations.

Extensive experiments demonstrate improvements in both multilingual capabilities and cultural adaptability.

### Weaknesses
1.  Lack of comparative comparisons: The paper lacks comparisons with task-specific supervised fine-tuning and translation-then-inference approaches (translating prompts with a translation tool and then performing inference with the translated prompts). These methods represent alternative upper bounds for multilingual LLMs. Additionally, there are no comparisons between LLMs of different model sizes, which could provide insights into the impact of model capacity on performance.

2. Why not patching hidden states: While the method involves transplanting feed-forward activations from non-English inputs to English, it does not explore the potential of directly patching the hidden states of English into the processing of non-English inputs. 

3. Implications for improving multilingual LLMs: How can the conclusions of this work be utilized to enhance the performance of multilingual LLMs or inform continued training strategies? Providing deeper insights into the practical applications of your findings would increase the importance of the research.

4. Limited practical applicability: The approach requires parallel bilingual inputs (non-English and corresponding English sentences). In real-world applications, such parallel data may not be readily available, limiting the practical applicability of the method.

### Questions
1. When transplanting the feed-forward activations from non-English to English in the XQUAD task, is the model's output in English or the non-English language?

2. In Table 1, the performance on the English XNLI test set increases significantly from 60 to 94. Could you elaborate on the experimental settings or conditions that contribute to this substantial improvement?

3. The experimental setup regarding the selection of the i-th layer and j-th layer for MSi→Tj (x) in Table 1 and Figure 5 is not clearly explained. Could you provide more details on how the layers are chosen and how the transplantation is performed?

### Soundness
3

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
This paper proposed a method called XTransplant to benchmark the upper bound performance in two scenarios: multilingual capability and cultural adaptability. Specifically, XTransplant replaces the feed-forward activations from one source language input to the target language input in the inference. For multilingual capability, the direction is En -> non-En, aiming to leverage good English generation capability. For cultural adaptability, the direction is non-En -> En, aiming to leverage the knowledge potentially only encoded in the non-En language-specific neurons.

### Strengths
- The paper is well-motivated. I think the idea is interesting and novel.
- The experiments are extensive.
- The results reported in the paper show that XTransplant can consistently improve the performance.

### Weaknesses
 - I understand that the main motivation is to benchmark the upper bound. But I see it is super expensive to investigate all the combinations (NxN). That might be a problem if one wants to see the performance on a specific downstream task with limited computation resources. 

- I also have concerns about whether xTransplant really offers the upper bound of a model, without any theoretical proof. One could argue it is also possible to transplant self-attention outputs.

### Questions
$\textbf{Suggestions / Questions}$:


- line 52-53: "curse of multilinguality" and "negative interference" are basically talking about the same thing (or more correctly, the curse of multilinguility if one type of negative interference when the languages are so many), the authors could consider condensing the two sentences.

- Figure 1 is not clear how the method is carried on. the authors could cosider have one sentence in the caption to describe how the proposed method works.

- line 74, "given a certain question", the authors should limit the span of such a question, i.e., a question that requires knowledge learned in non-English texts

- line 145: what is the "another version" of x_s, I would assume it is the translation. the author should specify it.

- line 161: what is the intuition of only changing the first new token? If the first new token does not change before and after the transplanting, the remaining tokens will be the same (greedy decoding).

- section 3.2: I am not sure I understand why it is called bi-directional transplant. It is either En -> non-EN or non-EN -> EN for a specific prompt. I would be more inclined to call it Mutual or Parallel transplant.

- section 5.1: how do the authors define language consistency? I guess it is the frequency of the input and output being in the same language. The authors should make it clear. Additionally, my intuition is that Xtransplant should be bad for language consistency because it changes the original activation to the activations obtained from another language. However, the authors' results suggest this is not the case. Can the authors give explanations? Additionally, it would be interesting to see some actual examples.

- line 203-204: "Questions in above datasets are in different multilingual languages". I don't understand this sentence but I guess the author means "Each question in the above datasets is available in multiple languages"?


$\textbf{typo}$:

Line205: "we we performed" -> "we performed"

### Soundness
3

### Presentation
2

### Contribution
3
