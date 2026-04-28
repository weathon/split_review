# Audio Large Language Models Can Be Descriptive Speech Quality Evaluators

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 8, 6

## Abstract
An ideal multimodal agent should be aware of the quality of its input modalities. Recent advances have enabled large language models (LLMs) to incorporate auditory systems for handling various speech-related tasks. However, most audio LLMs remain unaware of the quality of the speech they process. This limitation arises because speech quality evaluation is typically excluded from multi-task training due to the lack of suitable datasets. To address this, we introduce the first natural language-based speech evaluation corpus, generated from authentic human ratings. In addition to the overall Mean Opinion Score (MOS), this corpus offers detailed analysis across multiple dimensions and identifies causes of quality degradation. It also enables descriptive comparisons between two speech samples (A/B tests) with human-like judgment. Leveraging this corpus, we propose an alignment approach with LLM distillation (ALLD) to guide the audio LLM in extracting relevant information from raw speech and generating meaningful responses. Experimental results demonstrate that ALLD outperforms the previous state-of-the-art regression model in MOS prediction, with a mean square error of 0.17 and an A/B test accuracy of 98.6%. Additionally, the generated responses achieve BLEU scores of 25.8 and 30.2 on two tasks, surpassing the capabilities of task-specific models. This work advances the comprehensive perception of speech signals by audio LLMs, contributing to the development of real-world auditory and sensory intelligent agents.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on predicting MOS using a recently popular audio LLM approach. The model provides a natural language description of audio quality across several key dimensions, such as noisiness, coloration, and discontinuity, before assigning an overall MOS score. This process resembles a CoT approach, in which the model evaluates different aspects of audio quality to arrive at a final score. The authors claim that this method of MOS prediction is more accurate than traditional regression-based MOS prediction models.

### Strengths
This paper proposes to predict the MOS within the framework of a currently popular audio LLM scheme. The authors present their method clearly and effectively, detailing how the model assesses various aspects of audio quality before generating an overall MOS score. Experimental results demonstrate the effectiveness of this approach, indicating that the proposed method achieves a higher accuracy in MOS prediction compared to traditional regression-based methods.

### Weaknesses
- According to the ITU-T definition, the MOS should be an integer between 1 and 5. However, in the example provided in Section 1, the sentence ".....Taking into account all factors, the overall MOS score is only 2.4" conflicts with this definition, as MOS should not be a decimal. This discrepancy suggests a fundamental misalignment with the official MOS standard, which could impact the validity of the work.
- Although the authors extend the application of audio LLMs to MOS prediction, this appears to be a relatively incremental extension of prior works, such as SALMONN, which already covers a wide range of audio understanding tasks. As such, the methodological contribution may seem limited, potentially lacking the level of innovation typically expected at ICLR.
- The authors mention in Section 4.3 that the model requires SFT before RL. However, SFT is not mentioned at all until this point, which may lead readers to assume that RL alone is responsible for training the model. A more transparent approach would be to explicitly state from the outset that the model uses a typical SFT + RL pipeline, rather than emphasizing only certain parts of the process. Furthermore, the specific details of the SFT stage, such as the dataset used, the loss function, and the training procedure, are not clearly defined, making it difficult to assess the contribution of this stage to the overall performance.
- In later sections, the term "full-ft" appears, but it is unclear if this is meant to refer to the same process as SFT. If they are indeed synonymous, it would be clearer and less confusing to use consistent terminology throughout the paper. This will ensure readers understand the training pipeline without ambiguity. The lack of clarity regarding the distinction between full fine-tuning and SFT raises concerns about the reproducibility of the experiments and the interpretability of the results.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper contributes to the below 3 aspects and talks importance of descriptive information of audios in Multimodal LLM
(i) Importance of speech quality evaluation in multimodal agents especially for speech. (ii) Provide descriptive speech quality evaluation sets important for benchmarking the evaluation of audio quality in Audio LLMs. (iii) A novel learning strategy called ALLD that allows end to end perception and generation

### Strengths
The paper shows clear outcomes for the novel proposal and experiment
- ALLD achieves the best performance across all systems according to evaluation metrics, and the BLEU score demonstrates the efficacy of this distillation strategy
- Paper describes means of generating evaluation data which is descriptive and can improve Audio LLM performance

### Weaknesses
While the improvements from the experiments have shown improvement its not clear on why the LCC and SRCC haven't improved for LIVE and P501 datasets.
Also, descriptive language is subjective to users, unlike evaluation score like BLEU, how do you propose to adhere to similar descriptive style for the evaluation generation

### Questions
Please explain the reason for lower LCC and SRCC for LIVE and P501 datasets.

Please share details on how you plan to generate descriptive text for audio data maintaining uniformity

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents an innovative approach to integrating speech quality evaluation into audio large language models (audio LLMs), addressing a gap in audio LLMs that typically overlook signal quality. The authors introduce a novel dataset that pairs Mean Opinion Score (MOS) ratings with natural language-based assessments (text descriptions) across multiple dimensions of audio quality, including noisiness, coloration, discontinuity, and loudness. This allows the audio LLM to generate descriptive judgments of quality. They propose an "Alignment with LLM Distillation" (ALLD) framework, distilling knowledge from a reference LLM to guide the audio LLM in emulating human-like quality assessments. Experimental results show that ALLD outperforms traditional MOS prediction models in both accuracy and descriptive capability, achieving lower mean square errors and higher BLEU scores.

### Strengths
**Originality**: This work introduces a descriptive, language-based dataset for speech quality assessment, allowing audio LLMs to conduct more nuanced evaluations. The ALLD framework presents an innovative approach by guiding audio LLMs through token-level distillation.


**Quality**: The comparisons between traditional regression methods and descriptive, audio LLM-based approaches offer valuable insights into fine-tuning and demonstrate the effectiveness of natural language guidance.


**Clarity**: The paper is generally well-written and clear, though Section 2.2 could benefit from further refinement.


**Significance**: Repurposing Audio LLMs for speech quality evaluation addresses a critical need, given the limited availability of reliable automated metrics and the high costs of subjective evaluation. This work provides a pr

### Weaknesses
While a strengths and weaknesses comparison between two systems across specific sub-dimensions is reasonable, it is unclear how a human or LLM might synthesize these into an overall preference judgment. For example, if System 1 outperforms System 2 in one sub-dimension but falls behind in another, the basis for an overarching preference remains ambiguous. The dataset relies on LLM responses to make arbitrary decisions on whether Speech A or Speech B is preferable, using sub-dimensional scores as part of the reasoning. This raises concerns about consistency and the interpretability of such comparative judgments.
* Since the Teacher model is also used as the description generator, it would be useful to explore the generalizability of the ALLD framework. Given that BLEU scores are calculated on synthetic descriptions produced by the Teacher, examining how well ALLD performs on independently generated descriptions could add valuable insights. For example, one could compare ALLD with a smaller set of human-generated descriptions on the same dataset to assess its generalizability further.
* It remains unclear how the VoiceCraft edits, which are a core component of the dataset, affect the perceived quality of the speech. The paper claims that human listeners cannot distinguish between original and edited speech, but this claim lacks direct empirical support within the paper itself. Without a perceptual test or citation to relevant literature, the validity of this assumption is questionable, potentially undermining the reliability of the dataset.

### Questions
1. Can the authors kindly clarify the framework or the decision criteria for generating preference judgments when systems perform differently across sub-dimensions?
2. If the teacher model used during distillation is the same as the description generator of the training dataset, could this lead to a potential bias in the interpretation of the BLEU scores? 
3. Is there empirical support for the claim that human listeners cannot distinguish between original and edited speech produced by VoiceCraft? Including a perceptual test comparing original and VoiceCraft-edited audio samples or citing relevant literature if such a test exists can help here.

### Soundness
2

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
2

### Summary
This paper introduces a new approach for the speech quality evaluation tasks using audio llm. Additionally, the paper also introduce a new dataset for speech quality evaluation that include human like natural language description of the quality of speech. The proposed method alignment with LLM distillation (ALLD) for the audio LLM training. The ALLD aligns the generated sequence of the audio LLM to an expert LLM's response based on meta-information. The author also evaluated the proposed ALLD model on several evaluation dataset. The experiments showed that the proposed method outperformed SOTA regression model.

### Strengths
1. The paper introduces a new dataset for speech quality evaluation using human like natural language description. 
2. The proposed ALLD seems like an interesting approach which leverages token level distillation based on the implicit reward modeling from DPO.
3. The paper also shows that the speech quality evaluation can be integrated into multitask learning framework without degrading the performance of other tasks. 
4. The experiment results look promising

### Weaknesses
1. The author might need give better clarification of the dataset. At the beginning, I had the impression that the corpus was newly created from the paper. Actually the dataset is from previous work but generated the human like description labels from LLM. The description of the data generation process is not very clear, specifically how the prompts were designed and what kind of LLM was used to generate the descriptions. This lack of detail makes it difficult to assess the quality and potential biases of the generated labels.
2. The proposed method showed better results than Full-ft method. However, the improvement doesn't look significant. The paper lacks a thorough analysis of the statistical significance of the improvements. It's unclear whether the observed differences are practically meaningful or just due to random variations. Furthermore, the paper does not provide any ablation studies to understand the contribution of different components of the proposed ALLD method. For example, it would be helpful to know the performance of the model without token-level distillation or the RL-based fine-tuning.

### Questions
1. The formulate 1 looks like it is based on token level. However the formulate 2 is sequence level. How is formulate 1 rewritten into formulate 2?
2. why the proposed ALLD gave improved results over Full-FT? Could you share more insights? Is the improvement from the newly prepared data corpus? or the proposed ALLD method?

### Soundness
3

### Presentation
2

### Contribution
3
