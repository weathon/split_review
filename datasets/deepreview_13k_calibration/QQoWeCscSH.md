# Unlocking Speech Instruction Data Potential with Query Rewriting

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
End-to-end Large Speech Language Models (**LSLMs**) demonstrate strong potential in response latency and speech comprehension capabilities, showcasing general intelligence across speech understanding tasks. However, the ability to follow speech instructions has not been fully realized due to the lack of datasets and heavily biased training tasks. Leveraging the rich ASR datasets, previous approaches have used Large Language Models (**LLMs**) to continue the linguistic information of speech to construct speech instruction datasets. Yet, due to the gap between LLM-generated results and real human responses, the continuation methods further amplify these shortcomings. Given the high costs of collecting and annotating speech instruction datasets by humans, using speech synthesis to construct large-scale speech instruction datasets has become a balanced and robust alternative. Although modern Text-To-Speech (**TTS**) models have achieved near-human-level synthesis quality, it is challenging to appropriately convert out-of-distribution text instruction to speech due to the limitations of the training data distribution in TTS models. To address this issue, we propose a query rewriting framework with multi-LLM knowledge fusion, employing multiple agents to annotate and validate the synthesized speech, making it possible to construct high-quality speech instruction datasets without relying on human annotation. Experiments show that this method can transform text instructions into distributions more suitable for TTS models for speech synthesis through zero-shot rewriting, increasing data usability from 72\% to 93\%.  It also demonstrates unique advantages in rewriting tasks that require complex knowledge and context-related abilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel framework for constructing high-quality speech instruction datasets using query rewriting with multi-LLM knowledge fusion. The key contributions are:

- A query rewriting framework that leverages multiple LLMs to rewrite text instructions to better match TTS model training distributions while preserving semantics.
- A multi-agent annotation and validation approach using multiple ASR models and embedding-based similarity metrics to ensure quality.
- A knowledge fusion method that combines strengths of different LLMs to handle challenging rewriting cases.

### Strengths
- Novel and practical solution to an important problem in speech instruction dataset creation.
- Comprehensive evaluation across multiple datasets and metrics.
- Detailed ablation studies validating each component.
- Cost-effective compared to human annotation.
- Strong experimental results showing clear improvements in both data quality and downstream task performance.
- Good technical novelty in combining multiple LLMs and agents for robust performance.

### Weaknesses
 - Limited analysis of failure cases and error patterns.
- No direct comparison with other query rewriting methods from adjacent domains.
- Validation relies heavily on embedding similarity - could benefit from human evaluation.
- Parameter sensitivity analysis missing (e.g., impact of different thresholds).
- Scalability and computational costs not thoroughly discussed.

### Questions
/

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a query rewriting framework for rewriting text queries such that TTS models are able to easily process and synthesize. To accomplish this, several LLMs are prompted to rewrite the input query such that things like abbreviations and formulas would be written in a way that a TTS model can understand. Multiple ASR models are used to filter the TTS outputs and match them against the original input to make sure that they are aligned. In order to increase the diversity of the speakers, an LLM is prompted to generate speaker descriptions which are passed to the TTS model to control the speaker identity and style. Knowledge Fusion is used to improve the model's performance on rewriting challenging queries. Experiments show that their technique improves the linguistic alignment between the text and generated speech while

### Strengths
Paper presents a detailed infrastructure for generation and filtering synthetic datasets for speech instruction datasets. Results show consistent improvement over naive TTS generation. Experimental results show across multiple datasets that the generated speech is higher quality across WER, SIM and PASS and that their technique improves downstream performance on NarrativeQA.

### Weaknesses
One of the main issues with this paper is the Main Result in Table 4 and Section 5.3. Authors only show that performance improves for exactly 1 model and on exactly 1 dataset. This is not sufficient evidence to claim that this technique extrapolates to other downstream tasks. This is very strange, since the authors clearly had all of these other datasets available that they could have used for evaluation.
This table is also not very well explained; there is no experimental setup section about how this experiment was performed. Furthermore, the introduction of a threshold parameter in the updated Table 4, which was not present in the original results, further complicates the experimental setup and makes it difficult to interpret the results. The exact differences between the 'Golden' and 'LLM Continue' alignment targets are also unclear, as is the nature of the experiment in the first row of Table 4, which lacks a training target, threshold, or construction method. Additionally, there is no text normalization ablation in Table 4, which is a critical baseline for this kind of work.

Parts of this manuscript are poorly written and explained. Lots of typos and grammatical errors. (See questions)
In the second part of Section 5.2, the authors say they use ROUGE-L to "evaluate the quality of the generated results", however, it doesn't seem like this metric is used anywhere. 

The implementation details in section 5.1 on page 7 also state that top-p for generation is 10 (I am assuming 10%), which is extremely low, this might as well be greedy sampling.

Furthermore the use of Knowledge Fusion is not very well explained. Section 4.3 states that they use Meta-Llama-3-8B-Instruct on line 266/267 as the backbone model to train "the model"? In Figure 3, it seems like they just train a Llama model, how does this integrate with the existing rewriting models in the results sections, where something like "Phi3+Llama3+Qwen2+KF" is written? How do these LLMs integrate with each other in the pipeline?

Furthermore, the abstract, introduction and conclusion all repeat this statement of improving data usability from "71% to 93%" (the conclusion actually says 91%)  but it is unclear where this number actually comes from. 

Ablations are incomplete. In particular, it is unclear whether this technique improves over just having the LLMs rewrite the queries and using raw TTS after that.

### Questions
On line 053, you say that these training methods "treat the speech modality as files rather than instructions", what does this mean?
Furthermore, you state that the integration of "traditional tasks in the speech domain (such as speaker classification, speech entity recognition, etc.)" led to the trained models to "lack the ability to follow speech instructions and lead to hallucinations due to the severe bias in task distribution." Where is any reference for this phenomenon? 

In Figure 1, it is stated that these are depictions of several recognition errors in ASR models. However, the second error: "Sentence Pattern Error" is strange, it doesn't seem like there is any error other than capitalization? Is the error that the bot didn't put the "?" at the end? But semantically, the text is a question, not a sentence, so I am not sure what the error here is.

Typos and grammatical mistakes throughout the manuscript:
* Extra period in Equation (1) on line 147, it should not be there since line 149 is the continuation of the sentence afterwards. Also an extra period in Equation (2), (3), (4)
* Line 161, "oringal" instead of "original"
* Incorrectly capitalized "We" near the end of line 192 in section 4.1
* The sentence at the end of line 199 in Section 4.1 is grammatically incorrect: "And the quality for $s_o$ could get by" should be something like "The quality of $s_o$ is given by" or something like that?
* The sentence spanning lines 203 and 204: "In the case of using the same similarity calculation method, since the performance of this evaluation approach depends on the orthogonality of the ASR models’ performance." is grammatically incomplete, it should probably say something like "This metric requires that the ASR models' performance be uncorrelated with each other so that we do not see consistent ASR errors on the same input."
* Missing spaces around the period on line 212/213 in section 4.2
* Missing space after "Section 4.2." on line 261 in Section 4.3
* Missing space after the comma on line 283 in Section 5.1
* Caption for Table 1 should state what Num is instead of just stating the names of the columns.
* Missing space on line 308 between "Table 2" and "provides"
* On line 352, "ROUGEL" should be "ROUGE-L"
* On line 406, "fintinue" should be "finetune"
* Caption for Table 8 is just wrong, it isn't "Examples of speech style descriptions generated by GPT-4", it seems like someone copy and pasted the caption for Table 2 and didn't edit it afterwards.
* In Section E.1, License is spelled "Lince" many times
* Extra period on line 335/336 "alignment.," 
* Missing spaces "thenear" on line 545 in the Reproducibility statement and "thetransparency" on line 555/556 in the Ethics and Ethics Statement. Also, the title of the Ethics statement is "Ethics and Ethics Statement", shouldn't this just be "Ethics statement"?

### Soundness
3

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
4

### Summary
The paper addresses the enhancement of instruction-following capabilities in speech language models through the creation of an improved synthetic speech instruction dataset. To achieve this, the authors propose a method to rewrite text instructions, aligning them more closely with the typical training distribution of TTS models. This rewriting framework utilizes multiple LLMs and incorporates annotation and validation of synthesized speech via a combination of ASR and embedding methods. Experimental results on several text-based QA datasets demonstrate that this approach enhances the usability of synthetic data and improves the preservation of linguistic information within synthesized speech.

### Strengths
1. Generating high-quality synthetic speech instruction data is a valuable task for the community, yet it remains relatively underexplored.
2. The paper introduces a versatile framework that integrates existing LLMs, ASR, and text embedding methods in a plug-and-play manner, requiring no additional training aside from the knowledge fusion component.
3. Results from automatic metrics indicate that the proposed framework enhances the quality and usability of synthetic data.

### Weaknesses
Quality

1. The paper begins by highlighting the gap between LLM-generated responses and human responses, but it’s unclear if their framework effectively addresses this. Human responses often include disfluencies or may involve mid-sentence question reformulations. A more rigorous human-in-the-loop evaluation would be beneficial to assess if fine-tuning on their synthetic speech data genuinely enhances the speech language model's ability to follow "spoken" human instructions.
2. The quality of synthetic data is primarily assessed using automated metrics. While I recognize the potential cost, a relevance judgment by human evaluators could provide valuable insights into whether the synthetic data aligns with how humans would expect to interact with a speech model. Given that the core objective is to improve the model's ability to follow human instructions, human-in-the-loop evaluation is essential.

Clarity

1. The paper could benefit from improved readability, particularly with the equations. Including backpointers to the sections where variables are first introduced would aid in following the mathematical formulation.
2. There are typos, such as "finitune" on page 8. A thorough proofreading is recommended to address these grammatical issues.
3. It’s unclear whether all embedding methods in Table 5 are used, or if only a subset based on Table 6 is applied.
4. The reference to "71% to 93%" lacks context. Clarifying what this range represents would improve comprehension.

### Questions
Refer to weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses text normalization in Text-to-Speech (TTS) through Large Language Model (LLM) utilization, aiming to better capture contextual information. By leveraging multi-LLM query rewriting and multi-agent annotation, the authors propose an innovative data generation framework that enables end-to-end speech language models (LSLMs) to better follow spoken instructions. This approach aligns synthetic speech and textual information with TTS models, achieving improvements in data usability and quality while minimizing reliance on human annotation. However, the method remains primarily a data augmentation strategy limited to specific TTS model, and lacking comparision with typical text normalization method for TTS.

### Strengths
The paper tackles text normalization for TTS using a text-based LLM framework, potentially improving contextual understanding and data synthesis efficiency for LSLM training.

### Weaknesses
 - Limited Scope: The focus is primarily on input text rewriting for TTS, which is essential for text normalization but less relevant to speech language models (SLMs) training. The framework generates instruction data but does not advance model training methods.

- Limited Technical Contribution: This work is mainly a data augmentation strategy, using TTS for producing instruction data in a speech-question/text-response format without introducing new training algorithms for LSLMs.

- Lack of Baseline Comparison: Text normalization in TTS has a rich history, especially in industrial applications. Prior studies, such as [1] and [2], propose alternative normalization techniques. The only rule-based baseline provided here involves basic numeric conversion, which oversimplifies comparison and limits validation of this method against established techniques.

- Insufficient Details on Model Training and Evaluation: The results section ("Use synthetic data to fine-tune LSLMs") lacks clarity regarding fine-tuning methods. For example, Table 4 lists "Qwen2-Audio-7B-Instruct" as the model, but it remains unclear if it was continually fine-tuned. Additionally, input-output specifics for this model are not provided.

- Dependency on Specific TTS Model: The study employs only Parler TTS for text synthesis. It’s uncertain how the framework would perform if a phoneme-based TTS model were used, particularly regarding out-of-vocabulary issues.

- ASR Model Dependency: The method’s efficacy in cases where ASR systems fail to recognize rare words is uncertain, raising questions about the proposed solution's handling of out-of-vocabulary cases

### Questions
Some suggestions are listed below: 

- Figure 1: Highlight differences using color or bold font for better visibility.

- Figure 2: Text readability is hindered by font size; should consider increasing.

- Table 8: The caption appears incorrect and should be reviewed for accuracy.

### Soundness
2

### Presentation
2

### Contribution
2
