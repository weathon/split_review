# ASROB: Measuring Automatic Speech Recognition from One Book

- Decision: Reject
- Scores: 6, 5, 3, 8

## Abstract
The MTOB (Machine Translation from One Book) benchmark measures the ability of large language models (LLMs) to "learn to translate between English and Kalamang—a language with less than 200 speakers and therefore virtually no presence on the web—using several hundred pages of field linguistics reference materials," predominantly with long in-context learning. However, many endangered languages like Kalamang are primarily oral, so supporting only text is insufficient: speech must be a first-class citizen for applications to be useful to actual communities. In this paper, we present ASROB (Automatic Speech Recognition from One Book), an extension of MTOB to speech tasks—Kalamang speech-to-text recognition (ASR) and Kalamang speech to English text translation (S2TT)—using an additional 15 hours of transcribed and translated Kalamang speech recordings. Our baselines measure the long mixed-modal (text+audio) in-context learning abilities of the Gemini 1.5 family. 1.5 Pro reaches 24.6% CER on ASR and 6.53 BLEU on S2TT, already beating the 34.2% CER and 4.51 BLEU achieved by a human who learned Kalamang from the same resources, but there is still substantial headroom for models to improve beyond this. We hope that ASROB will help evaluate extreme mixed-modal capabilities in LLMs and increase focus on supporting endangered languages in their spoken form.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new benchmark, ASROB, built on top of MTOB, which is a benchmark made of a Kalamang grammar, an English-Kalamang lexicon and English-Kalamang parallel sentences. ASROB adds 15 hours of transcribed and translated Kalamang speech to English. Human and model (gemini 1.5 flash and pro) baselines are provided and analyzed with different in context learning settings. Initial results show that some of the model baselines surpass the human baseline.

### Strengths
* The work is meaningful as it presents a testbed for improving zero-shot/few-shot capabilities of LLMs in a real-world low resource language scenario.
* The presentation is excellent: details, presentation flow, justifications for all design choices on the benchmark and the baseline models
* Experimental results are quite thorough

### Weaknesses
 * While the paper presents very interesting results and analyses of baselines models, the main contribution from a dataset perspective is limited to a low resource speech recognition and translation corpus.
* Even if the benchmark is meant to test in context learning, other baselines (e.g. finetuning MMS (https://github.com/facebookresearch/fairseq/tree/main/examples/mms)) would strengthen the paper.

### Questions
316: “we surprisingly do not see much difference between the two sets” What is the intuition or explanation for this?

Comments rather than questions:
* Mitigations for contamination: the authors could consider using the noai tag
* gpt-4o: Moshi (https://arxiv.org/abs/2410.00037) can also be cited

### Soundness
3

### Presentation
4

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
In this work, the authors present a new benchmark, ASROB (Automatic Speech Recognition from One Book), for long in-context learning using 15 hours of transcribed and translated Kalamang speech. Kalamang is an extremely low-resource languages, spoken by less than 200 people living on an island in Indonesian Papua. ASROB can be used to evaluate multimodal in-context learning where the entire data is fed as a long prompt to a natively multimodal LLM like Gemini 1.5. Gemini 1.5 Pro yields less than 25% CER on ASR and around 6.5 BLEU on spoken translation (to English). In contrast, a human Kalamang learner exposed to the same Kalamang resources, achieves 34% CER and 4.5 BLEU on the same evaluation sets.

### Strengths
- This is the first work that shows the power of long in-context learning for multimodal tasks like ASR and spoken translation. With no training and merely feeding all the data as an input prompt to a model like Gemini 1.5 Pro,  ASROB yields an impressive CER of around 25% for a new language like Kalamang.

- The authors publicly release the new benchmark ASROB that contains 15 hours of transcribed and translated speech in Kalamang. This is an important step towards language preservation and a vital contribution to existing data resources for extremely underresourced languages of the world.

- The authors have very carefully considered the ramifications of releasing such a resource, and added all the necessary safeguards in place.

- The draft is very well-written and clear in its exposition.

### Weaknesses
 - One main weakness is in the baselines. There is no comparison to regular finetuned baselines for the ASR and spoken translation (ST) tasks, that make use of the 15 hours of transcribed and translated speech. While the main objective of this work is to promote multimodal in-context learning with text and speech, it would still be useful to see how existing pretrained ASR/ST models fare after finetuning with labeled Kalamang speech. Specifically, the absence of a fine-tuned baseline makes it difficult to assess the true effectiveness of the in-context learning approach. The authors should consider fine-tuning a model such as Whisper or SeamlessM4T, which have shown strong performance on various speech tasks, to provide a more robust comparison.

- For the human baseline, the human only closely follows a little more than 1 hour of speech recordings rather than the full 15 hours. This makes the human baseline considerably weaker than the model baseline, apart from all the other factors mentioned in Section 4.1 that make the human baseline weaker. In the abstract, the authors mention "already beating the 34.2% CER and 4.51 BLEU achieved by a human who learned Kalamang from the same resources" which is a bit misleading given the 1 hour vs. 15 hour disparity. The authors should consider softening this claim. The comparison is not an apples-to-apples comparison, and the claim should be adjusted to reflect the difference in exposure to the data.

### Questions
- As mentioned under weaknesses, there are no comparisons to standard finetuned ASR and ST using the 15 hours of labeled Kalamang speech. We could start with a pretrained multilingual, multimodal model (e.g., Whisper, Seamless M4T, etc.), and finetune on the labeled Kalamang data using a parameter-efficient finetuning approach like LoRA. One could cascade the speech input and concatenate the outputs to mimic the evaluation setting of ASROB. These are important baselines to compare against and will also help calibrate the current CER/BLEU numbers better.

- Since the BLEU scores are quite low, like the authors did with CER for the ASR task, it might be useful to see a character-level evaluation metric (such as chrF++) for spoken translation as well.

- This is a somewhat minor point, but why is the benchmark named ASROB when the evaluations are on both ASR and spoken translation?  ASROB implies that only transcribed speech is available as part of the benchmark.

- From Fig 3, could the authors comment on why there's a degradation in WER and BLEU scores when increasing the number of few-shot audio samples from 3^2 to 3^3?

- For audio in the prompt, the authors increment by powers of 3 from 1-shot to 27-shot. It would be useful for the reader to know how many hours of speech each few-shot setting (3,9,27) amounts to.

- In Fig 3, the human baseline is placed against 27 audio examples (on the x-axis) which is presumably much more than 1 hour of speech? Given that the human only closely followed roughly an hour of speech, can the authors clarify the placement of the human learner dot in Fig 3?

- A minor editorial comment: The first line of the abstract is identical to the first line of the introduction.

  
I am happy to revise my scores after hearing from the authors during the rebuttal phase.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores the mixed-modality in-context learning (ICL) capabilities of Large Language Models (LLMs) for low-resource languages. 

Specifically, it investigates how Gemini 1.5 Flash/Pro models perform on automatic speech recognition (ASR) and speech-to-text translation (STT) tasks for the Kalamang language under zero-shot and few-shot scenarios. 

The results demonstrate that, in certain settings, these models can outperform human evaluation baselines on both tasks.

### Strengths
1. This paper focuses on leveraging LLM techniques for low-resource languages that are primarily oral and lack written traditions. By drawing more attention to these communities, it could benefit the groups that use these low-resource languages.

2. This work releases new data—including 15 hours of transcribed and translated Kalamang speech—and provides human evaluation baselines, which will help future studies focusing on this language.

3. This provides benchmark information for mixed-modality ICL, particularly for native multimodal models.

### Weaknesses
1. Lack of Novelty: This paper primarily builds on the existing MTOB, adding only a speech modality which just directly use the multimodal capabilities of the Gemini LLM. This addition is relatively straightforward, limiting the paper's innovative contribution.

2. Limited Scope: This study focuses solely on one language (Kalamang) and one LLM (Gemini 1.5), which weakens the generalizability of the results. While the authors note that Gemini is "the only LLM with publicly available native audio input at the time of writing," the study would benefit from including additional low-resource languages, especially from diverse language families, to provide a more comprehensive evaluation.

3. Inappropriate Experiment Design: The human evaluation baseline in this study appears unclear and potentially flawed for several reasons:
    - The results are likely influenced by various factors, such as the human learner’s education level, familiarity with similar languages, and other personal attributes. However, the paper does not provide details on these factors or mention the number of human learners involved, which could significantly impact the baseline’s consistency.
    - The human learner was only given 1 hour of study material, whereas the LLM had access to all 15 hours of content.

These issues raise serious questions about the validity of the human evaluation baseline in this study.

4. Lack of Detailed Explanation and Analysis: The paper lacks sufficient explanation and analysis, particularly regarding the ASR results in Figure 3, where the outcomes are quite surprising. It would benefit from a deeper analysis on points such as: 
    - why including the Lexicon yields the best performance
    - why adding more examples negatively impacts performance

### Questions
1. Clarification on Few-Shot Examples: It is unclear whether discourse-level or phrase-level examples are used as few-shot examples.

2. Accuracy of CER Measurement: Given that "the audio files include interspersed Papuan Malay (the region's vehicular language), not just Kalamang," it is unclear how Character Error Rate (CER) is measured accurately in this code-switching context.

3. Significance of BLEU Improvement: In the STT task, Gemini Pro achieves a BLEU score of 1.66 without any specific knowledge of Kalamang in the prompt. Is an improvement to 6.53 truly significant in this context?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new task called ASR from One Book (ASROB), which involves speech recognition and translation of the indigenous language Kalamang, using only the grammatical resources available for the language. For Kalamang, the resources are limited to a grammar book and a small set of parallel sentences with English. The authors collected 15 hours of audio recordings from native speakers and transcribed and translated them using an anchor language.

The benchmark dataset comprises discourse-level (long-context) audio recordings that require transcription and translation into English. This work aims to encourage support for more indigenous languages, leveraging recent advancements in large language models (LLMs) to promote inclusivity.

### Strengths
1. This paper introduces a novel task of transcribing and translating indigenous languages with minimal resources. Due to the long-context nature of the audio and the limited language resources, only advanced models with large context windows are suitable for evaluating such tasks. Attempting these tasks with smaller models would present an interesting challenge.

2. The evaluation of ASROB using Gemini models with multimodal capabilities and extended context windows demonstrates strong performance on the task, even surpassing human evaluation by the paper's first author.

3. The authors have taken sufficient measures to prevent data contamination, ensuring that the resources are not included in LLM pre-training.

### Weaknesses
While the proposed method (using Gemini Pro 1.5) outperforms human baselines, further evaluation is needed to identify which types of resources could improve the use of LLMs for this task. An ablation study using different portions of the grammar book or varying numbers of parallel sentences could help determine which resources are most beneficial and inform future research on resource acquisition for indigenous languages. Specifically, the paper lacks a detailed analysis of how the size and specific content of the grammar book impact performance. It is unclear whether certain grammatical constructs are more easily learned by the model than others, and if so, whether this correlates with the frequency or complexity of those constructs in the grammar book. Furthermore, the study does not explore the impact of varying the quality of the parallel sentences, such as the presence of noise or errors in the translations, which could be a critical factor in real-world scenarios where such resources are often imperfect.

### Questions
Do you have insights into the types of errors made by the multimodal LLMs? Could these errors be addressed by adding more audio data, or are they due to limitations in the grammar books that are specific to audio-related tasks?

### Soundness
4

### Presentation
4

### Contribution
4
