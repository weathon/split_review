# Personality Alignment of Large Language Models

- Decision: Accept
- Scores: 5, 8, 5

## Abstract
Current methods for aligning large language models (LLMs) typically aim to reflect general human values and behaviors, but they often fail to capture the unique characteristics and preferences of individual users. To address this gap, we introduce the concept of Personality Alignment. This approach tailors LLMs' responses and decisions to match the specific preferences of individual users or closely related groups. Inspired by psychometrics, we created the Personality Alignment with Personality Inventories (PAPI) dataset, which includes data from 300,000 real subjects, each providing behavioral preferences based on the Big Five Personality Factors. This dataset allows us to quantitatively evaluate the extent to which LLMs can align with each subject's behavioral patterns. Recognizing the challenges of personality alignments—such as limited personal data, diverse preferences, and scalability requirements—we developed an activation intervention optimization method. This method enhances LLMs' ability to efficiently align with individual behavioral preferences using minimal data and computational resources. Remarkably, our method, PAS, achieves superior performance while requiring only 1/5 of the optimization time compared to DPO, offering practical value for personality alignment. Our work paves the way for future AI systems to make decisions and reason in truly personality ways, enhancing the relevance and meaning of AI interactions for each user and advancing human-centered artificial intelligence.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes  the concept of Personality Alignment for tailoring LLMs to match the preferences and behaviors of individual users or groups. The authors created a large-scale dataset called PAPI with data on behavioral preferences from over 300,000 real subjects across the Big Five personality dimensions. They also propose the Personality Activation Search (PAS) method for efficiently aligning LLMs with individual preferences during inference. PAS identifies key activation vectors corresponding to personality traits and optimally shifts activations in those directions. The authors  show that PAS achieves strong performance in capturing individual preferences with high compute efficiency compared to baseline methods.

### Strengths
A key strength of the work is the PAPI dataset, with over 300,000 real-world subjects providing detailed responses to the IPIP-NEO-120 and IPIP-NEO-300 questionnaires. The scale  is impressive.

The Personality Activation Search (PAS) method is interesting. By identifying key activation vectors that correspond to personality traits and optimally shifting activations in those directions, this approach can more effectively do personality alignment during inference. 

 The authors also conduct a comptehensive evaluation of PAS, comparing it against prompting-based (Few-Shot, P2) and RL-based (PPO, DPO) baselines on the PAPI dataset.

### Weaknesses
While the PAPI dataset is impressively large, it doesnt seem to be diverse. Around 60% of subjects are female and the average age is 25 years. This skew can potentially bias the results and limit generalizability to other populations.
Also, PAPI dataset relies on self-report data from personality questionnaires. While this is a standard approach in personality research, self-reports can be subject to biases such as social desirability and lack of self-insight. Incorporating additional data sources, such as behavioral measures or peer ratings, could be more useful.

The evaluation of PAS focuses primarily on high-level alignment with the Big Five traits. However, personality is a complex, multifaceted construct, and individuals can vary in their expression of specific facets within each trait. 

The PAPI dataset uses a multiple-choice format for collecting personality data. While this allows for structured and efficient data collection, it may limit the richness and naturalness of the responses.
The paper also compares PAS to prompting and RL baselines but does not include a comparison to fine-tuning the entire language model. This is an important consideration as well.S

### Questions
Some additional questions remian:

Can the authors provide more details on the human evaluation process, such as annotator screening, training, and inter-annotator agreement metrics? This would help validate the human evaluation results. The paper is light on this.
How do you expect the methods to perform on multilingual models and non-English datasets? 
The discussion on negative societal impacts of AI hyper-personalization (e.g. filter bubbles, opinion polarization) and is light. Authors should exand on this more. 
Finally, exploring beyond multiple choice for collecting preference data, such as open-ended text can be interesting and more useful.

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
5

### Summary
The paper introduces the concept of Personality Alignment for LLMs, that is, tailoring of responses to individual user preferences based on personality traits. Using the Big Five personality theory, the authors introduces the PAPI dataset modeling human personality distributions. The authors also propose a LLM tuning method based on disabling certain activation heads -- Personality Activation Search (PAS). Evaluation results demonstrate PAS’s performance and efficiency compared to traditional alignment techniques including RL- and prompting-based methods.

### Strengths
- Overall, I like this paper and I think it's a very good attempt in aligning LLMs from a personality perspective. 

- The paper is generally well-written and easy to read, illustrations are also made in a good quality.

- It's cool to see how personality affects downstream reasoning tasks. It has always been something missing in prior personality-related LLM work. And it's definite a god step here.

- The proposed method is efficient, and can provide better results compared to prompting-based methods. It may have wide applications in tailoring persona/personality-specific chatbots to end users.

### Weaknesses
 - Presentation: The authors claim that they collected 307k human samples to craft the PAPI dataset and the use of the IPIP-NEO-120/IPIP-NEO-300 for evaluations as part of their contributions. However, the IPIP-NEO series inventories were frequently used in prior works (e.g., Jiang et al., 2024 as mentioned in the paper), and the 307k responses are also publicly available.

- The implications of the 307k PAPI dataset are not that clear. For example, in the experiments authors performed, it seems only the overall average personality tendencies and specific participants' responses are used. So what's the actual advantages of using a such large dataset?

- The proposed tuning method, although efficient, but requires access to model weights. I doubt its ability to generalize such methods to black-box methods (e.g., GPTs) in the future.

### Questions
- In any of your experiments, did any of your tuning or evaluation methods trigger safety wall? For example, the model might refuse to answer some questionnaire questions related to consciousness or self-awareness.

### Soundness
4

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
This paper explores the personality alignment of large language models (LLMs). Specifically, it introduces a new dataset and proposes the PAS method for personality alignment based on this dataset.

### Strengths
The strengths of this paper can be summarized in three key points:

- It contributes a new dataset (or more accurately, a dataset generation pipeline).
- The proposed method is simple yet highly effective.
- The experimental analysis is comprehensive, with particularly detailed descriptions of the experimental setup.

### Weaknesses
The scope of the contribution is somewhat limited. I would have liked to see this method applied to a broader range of personalities, rather than being restricted to just the five personalities of the Big Five model. The authors could consider additional datasets, such as the Dark Triad or even the MBTI test (though MBTI remains controversial in psychology). Expanding in this way would enhance the paper’s overall contribution.

While the proposed method performs well on the dataset, it is actually quite similar to approaches used in many previous studies [1][2]. As a result, the novelty of the method is somewhat lacking, and the authors should be careful not to overstate their contribution. Specifically, the method appears to be another form of activation steering, which has been explored extensively in prior work. The authors need to clearly articulate the novel aspects of their approach compared to existing activation-based methods.

Essentially, the proposed method is a form of personalized alignment, so the authors should compare it against more baselines [3]. The current baselines do not adequately cover the personalized alignment space, and a more thorough comparison is needed to demonstrate the method's true effectiveness.

Figures 6 and 7 show a significant disparity between LLM-as-a-judge evaluations and human evaluations, which makes me question the consistency and reliability of the judgment process. The authors should provide a more detailed analysis of why these two evaluation methods diverge so significantly, and how this impacts the interpretation of the results. The lack of agreement between automated and human evaluation raises concerns about the validity of the automated metrics.

Other details: In line 1304, the authors mention that human annotators come from machine learning and computer science, but ML is a part of CS. Additionally, could the authors disclose the educational background of the annotators (undergraduate or graduate)?

### Questions
Could the authors explain why the PAS method is so effective by looking at the internal hidden layer representations of the model? Intuitively, direct training approaches like DPO/PPO might yield more noticeable improvements, but the results here contradict my expectations.

In line 429, the authors mention "Why Did Scaling Laws Fail?" but don't seem to fully answer this question. I would like the authors to explain this from the perspective of the domain's specificity. Is it because larger models learn more general alignment, which makes it harder for them to excel at aligning with a specific personality?

### Soundness
3

### Presentation
3

### Contribution
2
