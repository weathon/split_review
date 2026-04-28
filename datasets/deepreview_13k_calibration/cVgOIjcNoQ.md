# OmniChat: Enhancing Spoken Dialogue Systems with Scalable Synthetic Data for Diverse Scenarios

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 8, 3

## Abstract
With the rapid development of large language models, researchers have created increasingly advanced spoken dialogue systems that can naturally converse with humans. However, these systems still struggle to handle the full complexity of real-world conversations, including audio events, musical contexts, and emotional expressions, mainly because current dialogue datasets are constrained in both scale and scenario diversity. In this paper, we propose leveraging synthetic data to enhance the dialogue models across diverse scenarios. We introduce **ShareChatX**, the first comprehensive, large-scale dataset for spoken dialogue that spans diverse scenarios. Based on this dataset, we introduce **OmniChat**, a multi-turn dialogue system with a heterogeneous feature fusion module, designed to optimize feature selection in different dialogue contexts. In addition, we explored critical aspects of training dialogue systems using synthetic data. Through comprehensive experimentation, we determined the ideal balance between synthetic and real data, achieving state-of-the-art results on the real-world dialogue dataset DailyTalk. We also highlight the crucial importance of synthetic data in tackling diverse, complex dialogue scenarios, especially those involving audio and music. For more details, please visit our demo page at \url{https://sharechatx.github.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a large-scale synthetic spoken dialogue dataset, ShareChatX, covering a wide range of scenarios, including emotion, audio, and music. It also introduces a dialogue system, OmniChat, for diverse scenarios. Then, it conducts extensive experiments to compare the proposed method and existing ones, on both a previous dataset, DailyTalk, and its proposed method, and demonstrates that OmniChat has the SOTA performance. It also provides analysis on the data scale impact, optimal synthetic data ratio, expert feature selection strategies, and complex scenarios.

### Strengths
1. The paper contributes a very large-scale spoken dialogue dataset that covers a wide range of scenarios, which largely contributes to studies of related topics.

2. The paper conducts extensive experiments and provides detailed and thorough analysis from a lot of perspectives, offering lots of useful insights.

### Weaknesses
1. When trained wo/ real data, OmniChat does not leads to a large improvement, and is worse than Qwen2-Audio in metrics like METEOR, and GPT-eval. 

2. The paper provides some insights in finding the optimal synthetic data ratio. However, it may still be hard to tune the ratio in real-world scenarios, as the ratio choice rules discussed in the paper may not generalize to other dataset choices and tasks.

### Questions
1. After listening to the demo audios, I observed that the synthetic data sounds relatively plain and do not deliver a strong emotion, compared to real-world conversations. How well do you think the synthetic data can capture emotional nuances? Is there any potential solution to make the synthetic data more real?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces OmniChat, a spoken dialogue system using ShareChatX, a synthetic dataset covering emotional, audio, and musical contexts to enable nuanced, multi-modal interactions. With Mix-Former, a fusion module, OmniChat dynamically integrates features like emotion and background sounds, achieving strong performance on complex dialogues. OmniChat outperforms existing methods on DailyTalk and ShareChatX.

### Strengths
This paper introduces a new large-scale synthetic dataset, ShareChatX, covering different scenarios, including emotion, audio and music. Based on this dataset, this paper also presents a competitive spoken dialogue system, OmniChat, achieving SOTA performance on DailyTalk and ShareChatX. Overall, this paper is well-structured and could potentially contribute to the field of spoken dialogue systems.

### Weaknesses
1. The evaluation benchmark is not very comprehensive. Although the evaluation includes two datasets, one of the test sets is constructed similarly to the training set. This similarity may contribute to OmniChat’s superior performance, primarily due to in-domain training. Additionally, the evaluation datasets focus solely on chit-chat. It would be beneficial to include information-seeking instructions in the evaluation as well.

2. The evaluation metrics primarily include reference-based methods (BLEU, ROUGE-L, BERTScore, F1). Previous studies have shown that these metrics may not fully capture conversational quality. Moreover, GPT and human evaluation results are only provided for DailyTalk.

3. Although the paper emphasizes the importance of balancing synthetic and real data, it lacks a detailed analysis of how each synthetic data type (emotion, audio, music) individually impacts model performance.

4. The paper does not provide sufficient details about the model and experimental setup to ensure reproducibility.

5. Many existing voice assistants prioritize real-time settings, which are essential for practical applications. Given the model’s complexity, real-time latency and response times could present challenges.

### Questions
1. What are the model versions of the pre-trained audio encoders used, including Whisper, Emotion2Vec, and Beat?

2. Could you elaborate on the methods for manual verification (line 183) and manual evaluation (line 322)?

3. How do you overlay the music or audio onto the spoken dialogue speech data? What Signal-to-Noise Ratio (SNR) do you use, or are they simply added without adjustment?

4. What is the evaluation prompt used for GPT-Eval?

5. What parameters are included in the style settings? Is it gender, pitch, emotion, energy (line 197), or gender, pitch, speed, emotion (line 182)?

6. Have you evaluated the accuracy of style parameters other than emotion?

7. How many trainable parameters does OmniChat have? Including a comparison of trainable parameters in other models would be beneficial.

8. Missing references: Existing works in audio/emotion dialogue systems include:
   - *SD-Eval: A Benchmark Dataset for Spoken Dialogue Understanding Beyond Words*
   - *EMOVA: Empowering Language Models to See, Hear and Speak with Vivid Emotions*

9. What are the GPT and human evaluation results for ShareChatX?

10. What is the inference cost of the proposed model?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces OmniChat, a novel spoken dialogue system enhanced by synthetic data for handling diverse scenarios. The key contributions include:
1. ShareChatX - a large-scale synthetic spoken dialogue dataset covering various scenarios including emotional dialogues, audio events, and music contexts
2. OmniChat - a multi-turn spoken dialogue system with a heterogeneous feature fusion module (Mix-Former) for optimizing feature selection across different dialogue contexts
3. Comprehensive analysis of synthetic data usage in training spoken dialogue systems, including optimal ratios between synthetic and real data
4. State-of-the-art performance achieved on the DailyTalk dataset and other complex dialogue scenarios

### Strengths
1. The paper addresses a critical challenge in spoken dialogue systems by leveraging synthetic data to overcome the scarcity of large-scale, high-quality spoken dialogue datasets.
2. The proposed Mix-Former module effectively integrates multiple expert features (speech, emotion, beat) to handle diverse dialogue scenarios.
3. Comprehensive experimental analysis provides valuable insights into optimal training strategies, including the ideal balance between synthetic and real data.
4. The work demonstrates significant practical impact through state-of-the-art performance on real-world datasets.

### Weaknesses
1. The paper lacks detailed comparison with some recent baseline methods in spoken dialogue systems, particularly in terms of model size and computational requirements.
2. The evaluation metrics could be more comprehensive, especially for measuring the quality of generated speech beyond just content and emotion accuracy.
3. The methodology for ensuring quality control in synthetic data generation could be explained more thoroughly.

### Questions
Could you please share the ablation studies on different components of the Mix-Former architecture?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents ShareChatX, a benchmark suite dataset for training  and evaluating spoken dialog/language systems. ShareChatX contains spoken language annotations in different contexts/scenarios including audio events and music backgrounds. ShareChatX is created by prompting GPT-4o, followed by synthesizing speeches using off-the-shelf TTS model.

Based on ShareChatX, authors trained OmniChat, a spoken language model that achieves SOTA performance on the dataset DailyTalk, and ShareChatX itself. Ablation studies such as the mixing ratio of synthesized and real datasets, data volume scaling are provided.

### Strengths
- The annotated dataset ShareChatX could be potentially helpful for developing foundation models to spoken language tasks; the released
  model OmniChat may facilitate future development of spoken language models;
- OmniChat achieves SOTA performance on the DailyTalk dataset.

### Weaknesses
 - The presentation is sometimes confusing and needs to be improved. For example, Sec5.3 investigates data scale for "spoken dialog models". But it is unclear which are the dialog models -- are they OmniChat, or other audio models? The section is confusing and not contributing to the paper that much.

- Details about experiment settings are necessary to verify OmniChat's actual performance. Tab2 and Tab3 compare OmniChat with baseline models, of which experimental settings are not provided.

- Although ShareChatX is targeting spoken language tasks, but in its core it relies on LLM + TTS model, which is not end to end; there is still a gap between ShareChatX and more realistic and challenging spoken language processing tasks.

### Questions
- In table2 and table3, are baseline models trained, or the numbers are zero-shot performance?

- You mentioned you randomly sample some test set examples in line314. Are the claimed SOTA performances computed on these randomly sampled data? Are there any standard splits?

### Soundness
2

### Presentation
2

### Contribution
2
