# Emergence of Hierarchical Emotion Representations in Large Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 3, 6

## Abstract
As large language models (LLMs) increasingly power emotionally engaging conversational agents, understanding how they represent, predict, and potentially influence human emotions is critical for their ethical deployment in sensitive contexts. In this work, we reveal emergent hierarchical structures in LLMs' emotion representations, drawing inspiration from psychological theories of emotion. By analyzing probabilistic dependencies between emotional states in LLM outputs, we propose a method for extracting these hierarchies. Our results show that larger models, such as LLaMA 3.1 (405B parameters), develop more intricate emotion hierarchies, resembling human emotional differentiation from broad categories to finer states. Moreover, we find that stronger emotional modeling enhances persuasive abilities in synthetic negotiation tasks, with LLMs that more accurately predict counterparts' emotions achieving better outcomes. Additionally, we explore the effects of persona biases—such as gender and socioeconomic status—on emotion recognition, revealing that LLMs can misclassify emotions when processing minority personas, thus exposing underlying biases. This study contributes to both the scientific understanding of how LLMs represent emotions and the ethical challenges they pose, proposing a novel interdisciplinary perspective on the issue.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study reveals key advancements in how LLMs perceive, predict, and influence human emotions. As model size increases, LLMs develop hierarchical emotional representations consistent with psychological models. The research highlights that personas can bias emotion recognition, underscoring the risk of stereotype reinforcement. Additionally, the study demonstrates that LLMs with refined emotional understanding perform better in persuasive tasks, raising ethical concerns about potential manipulation of human behavior. These insights call for robust ethical guidelines and strategies to mitigate risks of emotional manipulation.

### Strengths
1. The writing in this paper is clear, and the figures are intuitive, making the author's ideas easy to understand.

2. The paper astutely identifies that LLMs' potential to comprehend emotions could enhance their capacity to manipulate emotions, which provides critical ethical considerations for the further development of LLMs.

3. The proposed hierarchical emotion extraction method appears simple and effective, offering a powerful tool for further analysis.

### Weaknesses
1. After reading the introduction, I expected Chapter 3 to discuss the model's ability and limitations in **perceiving** emotions, especially focusing on the circumstances under which the model fails. However, the paper mainly discusses how larger models outperform smaller ones in understanding emotions, which is rather obvious and does not provide sufficient novel insight. The analysis lacks a rigorous exploration of failure modes, such as specific emotional contexts or linguistic cues that might lead to misinterpretations. A more detailed investigation into the model's sensitivity to subtle emotional expressions and edge cases would be beneficial.

2. Chapter 4 employs synthetic data for testing but lacks sufficient quality validation. Including human and LLM prediction accuracy in a figure, such as Figure 6, would be beneficial, even if only for a subset. The use of synthetic data raises concerns about the generalizability of the findings to real-world scenarios. The absence of a comparison with human-annotated data makes it difficult to assess the reliability of the model's emotion predictions. A more robust validation strategy, including human evaluation, is needed to strengthen the conclusions.

3. The contributions of the paper are somewhat scattered, covering three different aspects, but the discussions on these points are inadequate. Given that “influencing human emotions” is highlighted as a major contribution, I expected more extensive coverage on this topic. While I understand that involving human subjects may incur additional costs, drawing conclusions solely from LLM dialogues in isolated scenarios lacks persuasiveness. This section also lacks deeper analysis. The paper would benefit from a more focused and in-depth exploration of the ethical implications of LLMs' ability to influence human emotions, including a discussion of potential risks and mitigation strategies.

### Questions
1. What is the underlying principle behind Chapter 3? Your algorithm extracts more nuanced and hierarchical emotional information, but can you elaborate on what further conclusions can be drawn from this? If I understand correctly, does the model's ability to use more emotion-related vocabulary lead to greater hierarchical richness?

2. Chapter 4 provides quantitative analysis from multiple perspectives, but could you offer specific examples of how different character background settings lead to different model emotion predictions? This would help provide more substantial insights.

3. Could you clarify what new insights your experiments provide to advance previous work in perceiving, predicting, and potentially influencing human emotions? Some aspects have been discussed individually in previous studies.

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
2

### Summary
This paper explores the development of hierarchical emotion representations in large language models (LLMs), particularly focusing on models like LLaMA 3.1 with up to 405B parameters. The authors propose methods to extract emotion hierarchies from LLM outputs by analyzing probabilistic dependencies between emotional states. They claim that larger models exhibit more intricate emotional hierarchies resembling psychological theories of emotion. Additionally, the paper examines the impact of persona biases (e.g., gender, socioeconomic status) on emotion recognition and explores the relationship between emotional modeling and persuasive abilities in synthetic negotiation tasks.

### Strengths
1. Innovative Approach: The paper introduces a novel and interesting methodology for extracting hierarchical structures of emotions from LLMs, bridging computational models with psychological frameworks.

2. Relevance and Timely: The topic is timely, addressing the intersection of AI, emotion modeling, and ethics.

### Weaknesses
1. Emotion Extraction Technique Concern: The method for extracting hierarchical structures based on next-word probabilities lacks rigorous justification. The paper does not adequately explain why next-word probabilities are a suitable proxy for emotional relationships, nor does it explore alternative methods such as directly prompting for hierarchical relationships or using existing emotion ontologies as a baseline for comparison. The absence of a clear theoretical link between next-word prediction and hierarchical emotion modeling is a significant concern.

2. Threshold Selection: The paper sets a threshold (0 < t < 1) for determining parent-child relationships but does not explain how this threshold is chosen or its impact on the results. The lack of a principled method for selecting this threshold raises questions about the robustness of the findings. It is unclear whether the observed hierarchies are artifacts of a particular threshold choice, or if they reflect genuine underlying structures. The paper should include a sensitivity analysis to show how the resulting hierarchies change with different threshold values.

3. Quantitative Metrics: Although the visual representations of emotion hierarchies are compelling, incorporating additional quantitative metrics or comparisons with human-annotated emotion hierarchies could provide stronger validation of the proposed method. The paper relies heavily on visual inspection, but lacks quantitative measures to assess the quality of the extracted hierarchies. For example, measures of tree similarity, such as the Robinson-Foulds distance, or comparisons with established emotion ontologies could provide a more rigorous evaluation.

4. The font in Figure 2 is too small to see easily.

### Questions
1.  Can you provide a more detailed justification for using next-word probabilities to extract hierarchical emotion structures? 

2. How did you determine the appropriate threshold value (0 < t < 1) for establishing parent-child relationships between emotions? Was this threshold empirically validated?

3. Besides visual representations, can you use some quantitative metrics to validate the integrity and accuracy of the extracted hierarchical emotion structures?

4. Besides emotion, I guess your method can visualize the structure of other entities. Can you extend this part more to enlarge the generalization of your method?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the emergence of hierarchical emotional representations in large language models and explores their abilities to predict and manipulate emotions. The focus of this study is on models such as LLaMA and GPT, analyzing their emotional hierarchies and the potential biases they may exhibit when identifying emotions of minority character roles. The study also assesses the performance of models in comprehensive negotiation tasks, revealing the correlation between emotional prediction accuracy and negotiation outcomes.

### Strengths
•  The analysis and extraction of the emotional hierarchy in LLaMA validate its similarity to human emotional structures, with the complexity of emotional hierarchy positively correlated with model parameter volume.

•  It validates that different roles and scenarios significantly affect LLMs’ emotion recognition abilities, providing guidance for how to avoid such biases in the future.

•  It analyzes the connection between emotional prediction ability and persuasive ability in negotiation tasks, offering practical insights for the application of artificial intelligence in emotionally sensitive environments.

### Weaknesses
•  The first two conclusions are quite obvious and lack in-depth exploration of their underlying causes. For example, what is the relationship between the breadth and depth of model emotional stratification and model parameters and pre-training corpora? Specifically, the paper does not delve into the mechanisms by which increased model size leads to more complex emotional hierarchies. It remains unclear whether this is due to a greater capacity to represent nuanced semantic relationships, or simply a result of overfitting to the training data. Furthermore, the analysis does not explore the specific types of data within the pre-training corpora that contribute to the development of these emotional hierarchies. For instance, does the presence of more emotionally charged text lead to a more complex hierarchy, or is it more related to the diversity of contexts in which emotions are expressed?

•  The discussion on ethics and biases is somewhat coarse in terms of categorization by region, ethnicity, cultural background, and other living conditions. The current analysis lacks granularity, failing to consider intersectional biases. For example, the paper does not investigate how biases may compound for individuals who belong to multiple minority groups. It also does not account for the nuances within broad categories like 'region' or 'ethnicity,' which can encompass diverse cultural norms and emotional expressions. The analysis should also consider how these biases might manifest differently across various emotional contexts, rather than treating all emotions uniformly.

•  There is a lack of discussion on how to leverage LLMs’ emotional prediction capabilities to optimize downstream dialogue tasks. The paper does not explore specific methods for incorporating the identified emotional hierarchies into dialogue systems. For example, it does not discuss how the distance measures within the emotion tree could be used to guide dialogue generation or response selection. Furthermore, the paper does not consider the potential for using these emotional predictions to adapt the tone and style of the dialogue, or to personalize the interaction based on the user's emotional state.

### Questions
•  The bias experiment could be expanded to more detailed demographic attributes or a broader set of test roles.

•  The analysis of the relationship between emotional prediction and other abilities (such as negotiation, persuasion) could be further expanded, rather than being limited to sales.

•  The wording around ethical issues in the abstract and introduction could be strengthened by providing specific examples of potential real-world impacts.

•  The presentation of Fig 6 needs to be optimized, with biases of different roles not being prominent enough.

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
3

### Summary
This study reveals three findings about emotional intelligence in large language models (LLMs) and its practical implications. First, as LLMs scale up, they develop hierarchical representations of emotions that align with psychological models. Second, the study uncovers how different personas (based on gender, socioeconomic status, etc.) can bias LLMs' emotion recognition, particularly showing systematic biases for minority attributes. Finally, through a synthetic sales negotiation task, the research demonstrates that better emotional prediction capabilities directly correlate with improved persuasion and negotiation outcomes.

### Strengths
There are three main strengths of this paper:

1. **High originality**: The exploration of hierarchical emotional representations in LLMs is novel and important. While previous studies have examined emotions in LLMs from various angles, none have investigated their hierarchical nature. Additionally, few works have explored the personalization of emotions, which this paper thoroughly investigates.


2. **High quality and clarity**: The paper presents solid evidence through multiple experiments and maintains clear, fluid expression throughout.


3. **Significant impact**: The findings on emotional hierarchy and personalized emotional biases provide valuable insights for future research and have important implications for LLMs' emotional reasoning and recognition.

### Weaknesses
There are three main weaknesses of this paper:

1. **Limited data for emotion tree construction**: The study utilized 5,000 prompts to test 135 emotion types, resulting in an average of only 37.03 prompts per emotion type. This relatively small sample size per emotion suggests the need for expanded data collection to construct a more detailed and robust emotion tree. The limited number of prompts per emotion category may not capture the full spectrum of nuances within each emotion, potentially leading to an incomplete or skewed representation of the emotional hierarchy. For instance, subtle variations in the expression of 'sadness' (e.g., disappointment, grief, melancholy) might be missed with such a small sample, affecting the accuracy of the hierarchical relationships identified.

2. **Dataset limitations**: The study exclusively relies on GPT-4 generated datasets. It would benefit from incorporating data from real-world scenarios (such as EDOS[1], EmpatheticDialogues[2], and GoEmotions[3]) for experimental validation. The use of synthetic data alone raises concerns about the generalizability of the findings to real-world emotional expressions. LLMs might generate emotional text that differs systematically from human-produced text, potentially leading to biased results. For example, the emotional intensity or the contextual cues associated with emotions might be different in LLM-generated text compared to human-generated text, which could affect the observed emotional hierarchy and bias detection.

3. **Format error**: (3.1) Citation formats require standardization (inconsistencies noted in lines 34, 48, 249, and 250); (3.2) Possible typo: "eutral" appears on line 362 (should this be "neutral"?)

### Questions
1. **Methodology Consideration**: Did the research employ various prompt types when constructing the emotion tree? Given that LLMs are typically sensitive to prompting, different prompt structures might elicit varying responses. This could potentially affect the emotional relationships identified in the study - for example, the strong connection observed between fear and shock in Llama3.1_8b might be weakened or altered with different prompt formulations. Therefore, I suggest conducting an ablation study on prompt sensitivity to quantify how different prompts affect the emotional hierarchy.

2. **Data Representation Query**: Considering that all the data used in the study was generated by GPT-4o, to what extent might this deviate from authentic human emotional expressions and patterns? I recommend that the authors compare GPT-4o generated data with existing human-annotated emotion datasets to quantify any differences. Additionally, human experts could evaluate the differences between GPT-4o generated data and real-world data.

### Soundness
4

### Presentation
3

### Contribution
4
