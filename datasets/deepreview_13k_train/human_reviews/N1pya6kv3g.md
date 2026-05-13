# PREMIUM: LLM Personalization with Individual-level Preference Feedback

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
With an increasing demand for LLM personalization, various methods have been developed to deliver customized LLM experiences, including in-context learning, retrieval augmentation, and parameter-efficient fine-tuning. However, most existing methods are not readily locally deployable, limited by the compute cost, privacy risks, and an inability to adapt to dynamic user preferences. Here, we propose to use a tag system to efficiently characterize user profiles, inspired from the insights from personality typology and recommendation systems. Based on the observation, we present a locally deployable LLM-agnostic framework for achieving LLM personalization: $\textbf{PREMIUM}$ ($\textbf{P}$reference $\textbf{R}$anking $\textbf{EM}$powered $\textbf{I}$ndividual $\textbf{U}$ser $\textbf{M}$odeling), which obtains individual-level feedback by having users rank responses and continuously self-iterates optimization during the interaction between the user and the LLM. Notably, a variant of PREMIUM, PREMIUM-Embed, can effectively capture user preferences while being deployable with laptop-level resources. Besides algorithmic innovation, we further prepare a novel dataset, Ranking-TAGER, which provides a valuable evaluation protocol for LLM personalization. Extensive experiments validate that PREMIUM remarkably outperforms various baselines, achieving a 15\%-50\% higher accuracy and a 2.5\%-35\% higher win rate on Ranking-TAGER, as well as a 3\%-13\% higher accuracy and a 2\%-7.5\% higher F1 Score on LaMP-2. More importantly, we further demonstrate that PREMIUM can develop an effective strategy with minimal interactive data, adapt to dynamic user preferences, and demonstrate excellent scalability in both scale and functionality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose PREMIUM, a framework for LLM-agnostic personalization.\
PREMIUM uses a tag-based system inspired by personality typology and recommendation systems to capture user preferences.\
This approach, along with a variant called PREMIUM-Embed, can run efficiently on minimal hardware, such as a laptop.\
Extensive experiments show that PREMIUM significantly improves personalization accuracy and adaptability to changing user preferences.

### Strengths
1. The proposed method provides a well-structured approach to selecting user tags, which enhances the personalization process by aligning it with user-specific characteristics.
2. The introduction of a new benchmark dataset, Ranking-TAGER, specifically designed for personalized LLMs, is a valuable contribution. \
This dataset not only allows for standardized evaluation of personalized language models but also fills a critical gap in LLM research.

### Weaknesses
1. The explanation of the process after tag selection in Section 4 is unclear.
While the paper describes selecting tags based on the embeddings of the query and tags, it lacks a clear follow-up on how these tags are subsequently used to influence the LLM's responses.
A detailed, step-by-step breakdown of how the selected tags are integrated into the LLM's response generation would help clarify this process. Specifically, it is not clear how the selected tags are transformed into a format that the LLM can understand and utilize. For instance, are the tags directly appended to the prompt, or is there a more sophisticated mechanism involved, such as using the tags to modify the attention mechanism or the hidden states of the LLM? Additionally, a flowchart or diagram showing the progression from tag selection to final response would improve comprehensibility.
2. A user study focusing on the readability and user perception of the tag selection process would enhance the paper's empirical rigor. 
Specifically, assessing the clarity of the tag-based personalization process and how users perceive its effectiveness in delivering personalized responses would provide valuable insights. This should include an analysis of whether users find the selected tags to be relevant to their queries and whether the resulting responses are perceived as more personalized compared to a non-personalized baseline. It is also important to evaluate the user experience of the tag selection interface, including its ease of use and the cognitive load it imposes on the user.

### Questions
Please refer to Weaknesses.

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
This paper proposes an LLM personalization method based on tag selection. Specifically, it introduces training a tag selector that adaptively selects suitable tags for each given query. The selected tags are then combined with the query to form a new prompt, which is used to request personalized responses from the LLM. The training of the tag selector relies on fitting user rankings of responses generated with different tags.

### Strengths
S1. The proposed method does not include training LLMs.
S2. The proposed method looks like it can be applied to closed-source LLMs.
S3. Most parts of the paper are generally easy to follow.

### Weaknesses
W1. Relying solely on tags for personalization may result in limited effectiveness, as the ability to personalize is heavily constrained by the predefined tags and their level of granularity. To my knowledge, the tag-based method is also not dominant for recommendation.

W2. The approach to achieving personalization is not clearly defined. User tags do not seem to be directly used for prompt generation but are instead used to rank the generated outputs. If this is the case, achieving personalization would require the tag selector to be specific to each user. This implies that a separate selector would need to be learned for each user, which could lead to efficiency issues and reduced learning efficacy, especially when data is sparse.

W3. Many important baselines, e.g., [1] and [2], are not compared.

W4. When applied to real-world scenarios, the method requires users to rank numerous responses, which could hinder its practical implementation.

W5. The recommendation appears to be a suitable task for evaluating personalization capabilities. Why not directly assess the method's effectiveness with the recommendation task?

W6. How does the method perform compared to soft-prompt tuning-based methods?

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a new framework called PREMIUM for LLM personalization with individual-level preference. The framework adopts a tag system to represent user profiles and preferences, thereby guiding the LLM to generate more user-specific responses. The framework encompasses two main variants: PREMIUM-Prompt and PREMIUM-Embed, with the latter being particularly emphasized due to its efficiency and lightweight design, enabling deployment even on devices with limited computational resources.  

The paper also introduced a new dataset, Ranking-TAGER, explicitly designed to evaluate LLM personalization methods that employ a tag-based user profile system. The dataset adopts an AI annotator to generate preference feedback with explanations.

The results demonstrate that PREMIUM-Embed consistently outperforms a variety of baselines across different datasets and setups. Notably, it achieves higher accuracy and win rates compared to methods that do not use tag system or do not leverage preference feedback.  

Further experiments provide a deeper dive into the capabilities of PREMIUM-Embed, showcasing its adaptability to dynamic user preferences, generalizability to expanded tag libraries, and extendability to binary tags.

### Strengths
The paper addresses a timely and important topic: LLM personalization.

The proposed PREMIUM framework is LLM-agnostic, broadening its applicability and increasing its relevance to the research community. It is also efficient and lightweight, enabling local deployment and making personalized LLMs more accessible.

The Ranking-TAGER dataset is a valuable contribution to the research community, providing a much-needed benchmark for evaluating LLM personalization methods that utilize tag-based user profiles.

The paper conducted extensive experiments and comprehensive analysis to showcase the proposed framework's effectiveness.

### Weaknesses
The method of embedding based tag recommendation is well-studied in recommendation system community. 

The assumption of preference feedback limits its applicability in real-word use cases.

It is unclear how groundtruth user tag is generated in evaluation. 

Lack of discussion on how to determine the tags in tag library.

### Questions
1. In many cases, the queries asked by users may not need any personalization at all, such as reasoning tasks, or knowledge related QA tasks. How do these extra tags affect the performance of non-personalized tasks, which ideally should not be affected?

2. Would it be possible to also add more evaluation from other LLMs instead of just Qwen1.5-72B, to see how different LLMs as autorater affect performance? 

3. What is the impact of m responses in preference ranking?

4. The paper could be even stronger in evaluation, if it can also do some evaluation with proprietary LLMs such as ChatGPT or Gemini.

5. The paper assumes the assumption of preference feedback during interaction, which might limit the applicability in real-world use cases.  It might be worth some discussion as its limitation.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work developes a lightweight and dynamic framework PREMIUM, which capitalizes on the tag-based approaches in recommendation, to achieve alignment between LLMs and user preferences. Tags can be selected based on prompt-driven LLM generator or embedding matching. Also, it collects a AI-annotated dataset, Ranking-TAGER, specifically designed for evaluating LLM Personalization. Experiments are conducted on LaMP-2 and Ranking-TAGER.

### Strengths
1. It seems as a simple and lightweight framework, with significant improvement shown in the experiments.
2. It focuses on an interesting and important research question, Personalized LLM, with a well-surveyed understanding of the current state of the field.

### Weaknesses
1. One of the contributions, the construction of the Ranking-TAGER dataset, appears to be confusing. In my view, incorporating AI annotators is not persuasive. Also, Including tags as user characteristics in datasets is uncommon in real-world scenarios. Could you explain more about the contribution of Ranking-TAGER?
2. The evaluation setting of adapting to dynamic user preference, as in one of the challenges addressed, seems simple, because the changes in user preferences have already been abstracted by different tags. Could you provide experimental results on more difficult settings?

### Questions
1. Please see weakness.
2. A general question: What is the precise personalization that this work focuses on? Please provide a concise concept definition of "personalization" with specific examples.

### Soundness
3

### Presentation
4

### Contribution
3
