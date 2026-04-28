# See It from My Perspective: How Language Affects Cultural Bias in Image Understanding

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Vision-language models (VLMs) can respond to queries about images in many languages. However, beyond language, culture affects how we see things.  For example, individuals from Western cultures focus more on the central figure in an image while individuals from East Asian cultures attend more to scene context (Nisbett 2001).  In this work, we characterize the Western bias of VLMs in image understanding and investigate the role that language plays in this disparity. We evaluate VLMs across subjective and objective visual tasks with culturally diverse images and annotations. We find that VLMs perform better on the Western split than on the East Asian split of each task.  Through controlled experimentation, we trace one source of this bias in image understanding to the lack of diversity in language model construction. While inference in a language nearer to a culture can lead to reductions in bias, we show it is much more effective when that language was well-represented during text-only pre-training. Interestingly, this yields bias reductions even when prompting in English. Our work highlights the importance of richer representation of all languages in building equitable VLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present an interesting study that looks into the problem of Western bias in VLMs model and what role language plays in the disparity between model performance on western-centric datasets vs others. They study this problem by conducting controlled experiments for different visual understanding tasks (e.g., object identification, question answering, and art emotion classification). In this study they focus on the disparity in performance between English and Chinese and use a specific bias ratio to determine such error disparity. The main takeaway message from the study is that the underlying language model plays a big role and that it's important to make sure that the pretraining stage of the language model has a suitable level of language diversity to facilitate transfer to different cultures and languages.

### Strengths
The paper has some important strengths that I list below:

1. Very relevant topic considering that many SOTA VLMs used by the community are typically trained with English-only datasets and we don't know to what extent their pretraining can facilitate transfer to other cultures

2. Two important results provided by this paper: 1) a study of the bias ratio of open-source models out of the box; 2) a controlled study that investigates the capabilities of models after pretraining depending on their language model training.

### Weaknesses
Despite the strengths highlighted, the current paper falls short in certain aspects that I highlight below:

1. I find the structure of the paper a bit confusing because it uses the terms "bias sourcing" and "bias characterisation" as titles which haven't been described before. I believe that it would be more informative to use as titles the actual names of the experiments to make sure that the reader is aware of the corresponding content that will be described in that section.

2. The measure of bias that is reported in the current paper is misleading because it implicitly assumes that the reference metric is an accuracy. However, the authors do not acknowledge this in any way. Considering that novel models are purely generative, I believe it's important to clarify how this study can generalise to more general tasks that involve free-flow generation.

3. I think it's important to consider what is the effect of the model generations to the overall performance. I think the authors should state, together with the accuracy score, how many times the model actually provides a meaningful answer to the prompt rather than say something like "I cannot answer to this". I'm mentioning this mostly because when testing models trained in English with Chinese prompts, it might be the case that models might not follow the prompt at all. It would be useful to report this explicitly in your results (how many times does the model reply following the format provided?).

4. Using newer LLMs for their study would have been useful such as Llama-3 or Qwen instead of Llama-2. This is mostly because they are generally stronger LLMs compared to Llama-2

### Questions
N/a

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
4

### Summary
The paper aims to investigate if vision-language models are biased due to the language mix in the pretraining data or the instruction tuning data, by drawing inspiration from cognitive science research suggesting culture could affect visual perception. The authors measure western bias, or the ratio between performances over English-specific data and Chinese-specific data.

### Strengths
The paper presents a very novel perspective in understanding VLMs. The experiments seem well designed and well executed. The conclusions could inspire interesting discussions. Overall I think this is a good paper.

### Weaknesses
Considering English to represent the entire West and Chinese to represent the entire East Asia is over-generalizing. It is perfectly ok to discuss English bias (instead of Western bias), and it would only strengthen the paper.

The authors seem a bit eager to reach identical conclusions on both subjective tests and objective tests, to the point that they did not discuss opposite trends on Dollar Street (but did show the results visually in Figure 5(b)). In Figure 5(b), Western bias on Dollar Street becomes worse when the prompt is in Chinese. This contradicts the description in Line 428: prompting in a culturally closer language reduces Western bias on objective and subjective tasks. 

It is common for the same instruction tuning data or the same prompting technique to have different performances on different tasks. VLM performance is just nuanced. [1] suggests that there are several VL skills learned by VLMs that could conflict. Hence, I do not think discussing this fact would weaken the paper. Rather, ignoring this fact would cause confusion and, in the worse case, be read as twisting data to suit a particular argument. 

Some additional details would be beneficial:

Section A.4 should contain a more detailed description of the logit lens, so that the paper becomes more self-contained. The numerical results should be shown as tables. 

The comparison between Baichuan2 and Llama2 should contain more detail. For example, what are their architectures? What was their training data mix? Such data are missing from the main text and the appendix. It is the authors' job to support the claim that these models are essentially identical except training data.  

Prompting in a culturally closer language reduces Western bias on objective and subjective image understanding tasks, especially if it was common during LLM pre-training -- what does "it" refer to?

### Questions
What are the architectures of Baichuan2 and Llama2? What was their training data mix? What are some other differences and similarities between the two models?

### Soundness
3

### Presentation
3

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
This paper investigates the effects of language modeling in multicultural image understanding. The authors focus on English and Chinese as proxies for Western and Eastern cultures, and show how Western bias (defined as the performance ratio on Western data over Eastern data) across different tasks varies as a factor of the base LLMs, language prompt and fusion corpora. Based on performance in three tasks, the authors argue for including multilingual and multicultural data early in model development, as opposed to later stages (fusion and prompts).

### Strengths
1. The paper proposes a systematic evaluation of language modeling towards multicultural image understanding in VLMs: the authors use two different pretrained LLMs as backbone (one English, and one English–Chinese); prompts in English and Chinese; and fusion corpora in English-only, Chinese-only and mixed.
2. The results corroborate the findings that earlier adoption of multilingual data in LLMs consistently benefits upstream VLMs.
3. A mechanistic study shows that the hidden states of Chinese tokens of a multilingual VLM initialized with an English backbone only decode to English, which the authors suggest is due to the model not effectively modeling the visual perspective of Chinese speakers.

### Weaknesses
1. The caption of Fig 4 says that “western bias reductions are seen across all tasks when prompting in Chinese.” However, from Fig 4, it seems that prompting in Chinese mostly exacerbates the performance of VLMs.
2. Prior work had explored the role of language in multilingual understanding and generation in VLMs, such as [1, 2]. It would be good to discuss these papers and compare your findings with theirs.
3. It would also be good to report overall performance, in addition to bias, for these models. For example, a model that performs at random will likely have a bias of 1.
4. Nit: Please make text in Figures much bigger.

### Questions
1. I understand that using the Chinese-translated version of the LLaVA dataset allows for a potentially better comparison with English models. But, as reinforced by your results, it would be great to see how culturally-relevant data affects performance and bias. For this, you could explore using the Wukong dataset [3].

---
[3] Gu et al. Wukong: A 100 Million Large-scale Chinese Cross-modal Pre-training Benchmark. NeurIPS 2022.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the Western bias in vision-language models (VLMs) and the role of language in cultural bias within image understanding. It evaluates VLMs on tasks with culturally diverse images and annotations, finding a Western bias that can be reduced by more diverse language representation during pre-training. The paper highlights the importance of multilingual foundation models for equitable VLMs and provides empirical evidence that a balanced language mix in pre-training significantly reduces bias.

### Strengths
* The paper discusses the cultural bias in VLMs, providing a comprehensive analysis of how language influences this bias in VLMs.
* The paper offers a comparative analysis between English and Chinese, two major languages, which provides valuable insights into bias reduction.
* The paper presents a comprehensive methodology, with controlled experiments to trace bias sources and measure the effects of different language modeling choices on bias.

### Weaknesses
 * The study's focus on English and Chinese may limit the generalizability of the findings to other languages and cultures.
* While the paper provides evidence of bias reduction, the authors need to do a deeper analysis of why certain models exhibit less bias, potentially through a more detailed examination of their training data and processes.

### Questions
* Could the authors elaborate on how their findings on language mix during pre-training could be extended to other non-Western languages and cultures?
* The findings in the paper are somewhat conventional and reflect existing consensus in LLMs. What do the authors think the same findings reflect about the relationship between vision(image) and language(text)?

I look forward to an active discussion with the authors during the rebuttal phase and will revise my score accordingly.

### Soundness
3

### Presentation
3

### Contribution
3
