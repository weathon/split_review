# Attacking Audio Language Models with Best-of-N Jailbreaking

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
In this work, we investigate the susceptibility of Audio Language Models (ALMs) to audio-based jailbreaks and introduce Best-of-N (BoN) Jailbreaking, a black-box jailbreaking algorithm to extract harmful information from ALMs. To craft jailbreak inputs, our approach samples audio augmentations and applies them to malicious prompts. We repeat this process until we find a set of augmentations that elicits a harmful response from the target ALM. Empirically, we find that applying BoN with 7000 sampled augmentations achieves an attack success rate (ASR) of over 60% on all models tested, including the preview model for the released GPT-4o. Furthermore, we uncover power laws that accurately predict the ASR of BoN jailbreaking as a function of the number of samples. These power laws allow us to forecast the effectiveness of BoN jailbreaking as a function of the number of sampled augmentations over an order of magnitude. Finally, we show that BoN jailbreaking can be composed with other black-box attack algorithms for even more effective attacks—combining BoN with an optimized prefix attack achieves 98% ASR on Gemini Pro and Flash. Overall, by exploiting stochastic sampling and sensitivity to variations in a high-dimensional input space, we propose a scalable, composable, and highly effective black-box algorithm for attacking state-of-the-art ALMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces "Best-of-N (BoN) Jailbreaking," a black-box algorithm designed to exploit weaknesses in Audio Language Models (ALMs) by extracting harmful information through audio-based attacks. The BoN method uses repeated audio augmentations, such as changes in pitch, speed, and background noise, to malicious prompts until it elicits harmful responses from the target ALM. The study shows that BoN achieves a high attack success rate (ASR), with results exceeding 60% ASR on several top ALMs, including a preview version of GPT-4o’s voice mode. Additionally, the authors discover power laws that allow them to predict ASR based on the number of samples, helping forecast the efficiency of BoN jailbreaking. The approach becomes even more effective when combined with other jailbreak techniques, reaching up to 98% ASR in some models. This paper highlights the difficulty of securing ALMs due to their sensitivity to continuous input variations, proposing BoN as a scalable and effective method for targeting ALM vulnerabilities.

### Strengths
- Proposed Best-of-N (BoN) Jailbreaking is novel, specifically tailored for attacking ALMs. BoN is unique in its application of audio augmentations to create high-entropy inputs, exploiting the ALM's sensitivity to continuous input variations. The combination of BoN with other jailbreak methods, such as the PrePAIR technique, showcases an innovative blend of audio augmentations and iterative refinement for more effective attacks.

- The discovery and application of power-law scaling to predict ASR with increased samples indicate a high-quality analysis, providing valuable insights into the scalability and potential impact of the proposed BoN method.

- The paper is well-structured and effectively explains complex ideas, making the novel BoN method accessible. Visualizations such as graphs that show the ASR progression with sample size and the power-law behavior, enhance clarity by illustrating key results.

### Weaknesses
 - A significant limitation of this study is the decision to turn off Gemini’s safety filter. In real-world applications, LLMs and ALMs rely on both alignment techniques and safety filters for safeguarding against misuse. By disabling these filters, the study's attack success rate may be artificially inflated, making the findings less practical and relevant in environments where safety filters are essential. Including experiments with the safety filter enabled would provide a more realistic assessment of the BoN method's effectiveness and its relevance to real-world deployments.

- The study does not evaluate the audio quality of the modified samples post-attack, which is an important aspect for assessing the stealthiness of these attacks. A low audio quality in the altered samples could make the attacks easily detectable or unnatural. A quality metric, such as the ViSQOL score, would allow for a quantitative comparison between the original and post-attack audio samples. Without such an analysis, it is unclear if the BoN attacks are feasible in scenarios where high-quality audio is essential for covert operations.

- The term "ASR" is commonly used to denote "Automatic Speech Recognition" in the speech research community. Could the authors consider using an alternative term?

### Questions
- How might the ASR be affected if the safety filter remained active? Including this would provide a clearer picture of BoN’s practical effectiveness and real-world implications. Would the authors consider conducting additional experiments with the safety filter enabled to better align the study with real-world conditions?

- Audio quality after attack modifications is an important factor for stealthy and practical attacks. Could the authors provide details on the perceptual quality of the modified audio samples, perhaps using a metric like the ViSQOL score?

- The term "ASR" is commonly used to denote "Automatic Speech Recognition" in the speech research community. Could the authors consider using an alternative term?

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
This research paper explores the vulnerabilities of Audio Language Models (ALMs) to audio-based jailbreaking attacks. The authors introduce a novel algorithm called Best-of-N (BoN) Jailbreaking, which leverages random audio augmentations to elicit harmful responses from ALMs. They demonstrate the effectiveness of BoN jailbreaking on several state-of-the-art ALMs, including Gemini and GPT-4o. The authors also uncover power laws that predict the effectiveness of BoN as a function of the number of sampled augmentations. Finally, they investigate the composition of BoN with other jailbreaking techniques, demonstrating that combining these methods can lead to more potent attacks.

### Strengths
This paper successfully introduces a new black-box jailbreaking algorithm called Best-of-N (BoN) that effectively extracts harmful information from Audio Language Models (ALMs) by exploiting their sensitivity to variations in audio input. The audio domain is in general underexplored so I appreciate this effort.

The paper looks into different aspects such as combinations with other attacks. In addition, the paper provides detailed insights into the workings of BoN jailbreaking, including analysis of the transferability and semantic meaningfulness of the augmentations used. The research highlights the challenges of safeguarding ALMs with stochastic outputs and continuous input spaces.

### Weaknesses
My main concerns regarding this paper are that the methodology of the attack is not adequately described, and the evaluation begins without sufficiently introducing the approach and settings.

For example, to understand the experiments, the reader needs to know what is defined as "harmful information."

It is difficult to assess the novelty of this work. Although the authors propose an attack against an alternative domain, the method used is unclear. Additionally, we do not gain many modality-specific insights and could potentially derive the same findings from other, text-only models. It would be beneficial if the paper included some audio-specific insights.

For instance, what is the signal-to-noise ratio (SNR) of the input? Would a human notice the attacks? Does the attack also work if it is played over the air?

In the introduction, the paper describes the "robustness" of the models (third paragraph). However, the method used is not described, and the findings there are not particularly useful.

It would also be appreciated if the authors uploaded a few audio samples for listening.

### Questions
See above

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces BoN, a new jailbreaking technique for ALMs. Based on various audio augmentation methods, BoN bypasses the safeguards of SOTA ALMs through repeated sampling with higher ASR. Authors also show that BoN jailbreaking can be composed with other jailbreak techniques.

### Strengths
1. The research question, studying the jailbreak vulnerabilities of ALMs, is relatively interesting.

2. The experimental part is comprehensive and complete. The appendix is detailed.

### Weaknesses
1. As stated in line 157-159, PAIR and TAP are classical jailbreak techniques, and both of them achieve good performance on jailbreaking text-only LLMs. However, when applying single audio augmentation and TTS engine, the ASR on ALMs decrease to below 5%. This result looks counterfactual and lacks of detailed discussion. The authors should provide a more detailed analysis of why this decrease occurs, or discuss the potential reasons when transferred from text to audio.

2. Technical contribution is limited. (1) Lack of detailed description of the proposed algorithm PrePAIR. (2) From the limited description of PrePAIR, while universal, this algorithm is not highly relevant to the previous sections and the “audio” part in language models, which makes the motivation unclear. The authors should clarify the connection between PrePAIR and the audio aspects of language model, and explain how this algorithm relates to the overall motivation of the paper. 

3. As a supplementary section of the pre-experiments, Section 3 (especially Section 3.1 & 3.2) does not give clear and valuable insights, which also makes the pre-experiment part lengthy. The authors should highlight the key findings more clearly, which would help this reviewer and other readers understand the value of this section.

4. The presentation of the paper needs to be improved. For example, the duplicated part in upper left figure 1.

### Questions
1. See weakness 1. Are there any more insights and discussion?

2. See weakness 2. Do the PrePAIR have any relationship with the audio part in ALMs?

3. See weakness 3.

### Soundness
3

### Presentation
2

### Contribution
2
