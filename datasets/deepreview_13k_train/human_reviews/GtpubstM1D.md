# Advancing Mathematical Reasoning in Language Models: The Impact of Problem-Solving Data, Data Synthesis Methods, and Training Stages

- Decision: Accept
- Scores: 8, 1, 3, 8, 8, 6, 6

## Abstract
Advancements in large language models (LLMs) have significantly expanded their capabilities across various domains. However, mathematical reasoning remains a challenging area, prompting the development of math-specific LLMs such as LLEMMA, DeepSeekMath, and Qwen2-Math, among others. These models typically follow a two-stage training paradigm: pre-training with math-related corpora and post-training with problem datasets for supervised fine-tuning (SFT). Despite these efforts, the improvements in mathematical reasoning achieved through continued pre-training (CPT) are often less significant compared to those obtained via SFT. This study addresses this discrepancy by exploring alternative strategies during the pre-training phase, focusing on the use of problem-solving data over general mathematical corpora.
We investigate three primary research questions: (1) Can problem-solving data enhance the model's mathematical reasoning capabilities more effectively than general mathematical corpora during CPT? (2) Are synthetic data from the same source equally effective, and which synthesis methods are most efficient? (3) How do the capabilities developed from the same problem-solving data differ between the CPT and SFT stages, and what factors contribute to these differences?
Our findings indicate that problem-solving data significantly enhances the model's mathematical capabilities compared to general mathematical corpora. We also identify effective data synthesis methods, demonstrating that the tutorship amplification synthesis method achieves the best performance. Furthermore, while SFT facilitates instruction-following abilities, it underperforms compared to CPT with the same data, which can be partially attributed to its poor learning capacity for hard multi-step problem-solving data. These insights provide valuable guidance for optimizing the mathematical reasoning capabilities of LLMs, culminating in our development of a powerful mathematical base model called JiuZhang-8B.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the impact of incorporating problem-solving data, various data synthesis techniques, and different training stages on enhancing mathematical reasoning capabilities in large language models (LLMs). The authors examine whether problem-solving data improves continued pre-training (CPT) effectiveness over traditional mathematical corpora and explore the optimal mixture ratios of such data. The study also assesses four data synthesis methods—response diversification, query expansion, retrospective enhancement, and tutorship amplification—highlighting the latter as particularly effective. Additionally, the authors compare the mathematical skills acquired during CPT versus supervised fine-tuning (SFT), finding that CPT leads to stronger mathematical reasoning capabilities, especially on complex, multi-step problems. These insights are applied to create JiuZhang-8B, a model that achieves competitive performance on mathematical reasoning benchmarks against other math-specific models.

### Strengths
1. The paper provides an in-depth analysis of the effects of problem-solving data on mathematical reasoning, particularly through comparisons of CPT and SFT, with valuable insights into the role of SFT’s instruction-following capabilities.

2. The authors explore and  compare different data synthesis methods, which is useful. The insights shared on the performance difference for the four different methods would be helpful for the LLM Reasoning community.

3. The comparison between models trained on SFT and CPT at varying difficulty levels adds further depth to understanding model capabilities.

4. Most of the sections are clearly written and well-structured, with detailed methodology on dataset curation and training, making it accessible and informative for the research community.

5. The final results of JiuZhang-8’s performance compared to SOTA LLMs is impressive, validating the insights and techniques shared earlier. The release of the model’s base version would greatly support community development.

### Weaknesses
1. The section on exploring the impact of different data distributions (5.2) is confusing and needs more clarification:
    1. While the authors note the inherent overlap in mathematical knowledge and the challenge in aligning data distribution with specific capabilities, the extent of overlap between knowledge points remains unclear. A dataset similarity analysis, perhaps using techniques like cosine similarity on TF-IDF vectors of problem text or knowledge point embeddings, could be helpful to quantify this overlap and address questions raised below.
    2. The capability analysis in Figure 3 suggests that GAOKAO’s knowledge capabilities  subsumes MATH, while ZHONGKAO encompasses questions requiring higher general knowledge capabilities than MATH. This should mean that a model trained to perform better on GAOKAO should perform even better in MATH than a model trained to perform better in ZHONGKAO. However this is not the case, The authors designate middle school data as IND to ZHONGKAO and high school data as IND to GAOKAO, yet models trained on middle school data (both SFT and CPT) outperform high school-trained models on the MATH evaluation set (see Table 2). This raises questions about: (a) how the authors define OOD capabilities—whether based on the absence of similar problems in training or lack of shared underlying concepts; and (b) the effectiveness of the knowledge point labels used for segmenting middle and high school data. It's unclear if these labels capture the nuances of mathematical concepts or if they are simply proxies for grade level. A more detailed analysis of the knowledge point distribution within each dataset, perhaps using topic modeling techniques, would be beneficial.
   3. Figure 3 indicates that ZHONGKAO includes more advanced (level 3) general knowledge questions than GAOKAO. Since both NuminaMath and Lila contains math problem-solving data, assuming the proprietary dataset also contains mostly Math problem solving data,  a more detailed analysis of why high school math-trained models perform significantly worse on the ZHONGKAO evaluation would be beneficial. This analysis should consider the specific types of general knowledge required by ZHONGKAO and how they differ from those in GAOKAO and MATH. For example, are there specific real-world reasoning skills or vocabulary that are more prevalent in ZHONGKAO?
   4. More granular difficulty-level analysis of the middle school and high school datasets, as applied in Section 5.3, would enhance clarity. Specifically, providing the distribution of reasoning steps within each of the middle and high school datasets would help contextualize the results in Section 5.2. This would allow for a more direct comparison of the impact of data distribution and problem difficulty on model performance.


2. Result 8 appears somewhat trivial and lacks novelty, given that prior research has shown LLMs—and even simpler neural networks—tend to learn simpler representations first. The authors could strengthen this result by providing a more detailed analysis of the specific types of errors made by the models on harder problems, and how these errors relate to the model's learning of simpler problems. This could involve error analysis techniques such as examining the frequency of specific types of incorrect reasoning steps.

3. Results 4 and 6 appear redundant. Result 4 (line 377) highlights that SFT is less effective than CPT in learning mathematical skills, while Result 6 (lines 427-428) conveys a similar conclusion, stating that SFT's in-domain learning ability is weaker than CPT’s. The authors should clarify the specific nuances of each result and how they contribute to the overall understanding of CPT vs SFT. For example, does Result 4 refer to overall mathematical ability while Result 6 refers to a specific aspect of in-domain performance? If so, this should be made more explicit.

4. It seems to be that the majority of the problem solving data seems to be proprietary, thus making it hard to reproduce. This limits the reproducibility of the results and the ability of other researchers to build upon this work. The authors should consider releasing a subset of their proprietary data or providing more details on the data collection and annotation process to enhance reproducibility.

### Questions
See weakness for questions

1. The authors claims of collecting 25 million problem solving data. Assuming authors collected approximately 930,000 pieces from NuminaMath [1] and 140,000 from Lila [2], Does it mean that the proprietary problem solving data alone contains ~24 million pieces? or are the pieces calculated differently from the dataset websites?

2. A brief summary on how Figure 3 (Ability dimensions of four evals) is computed would be helpful in understanding Section 5.2.

[1] https://huggingface.co/collections/AI-MO/numinamath-6697df380293bcfdbc1d978c

[2] https://lila.apps.allenai.org

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper attempts to advance the mathematical reasoning capabilities of LLMs through  problem-solving data and exploring different data synthesis methods during pre-training and post-training stages. The authors propose findings on the efficacy of using problem-solving data and propose a new JiuZhang-8B model that outperforms baseline models.

### Strengths
Here are some strengths:
- I appreciate the clear introduction and quickly getting to the point on issues with the current two-stage paradigm.
- The authors include information for reproducibility, such as hyperparameters and data mixture ratios.
- The authors develop and release a new model, JiuZhang-8B, which could add value to the community.

### Weaknesses
This paper needs some work. Here is a list of areas for improvement:
- I recommend briefly describing in the abstract and introduction what you mean by problem-solving data.
- The paper outlines three research questions but fails to present a clear rationale or context for each. Why are these research questions important to answer?
- I find the bolding to be a bit hard to read in the introduction. I recommend laying out your contributions in a bulleted list to avoid having to bold “Result X”.
- I recommend providing a brief description of the techniques mentioned in Result 3 or instead summarizing what types of techniques are the most effective rather than specifying specific names.
- In the abstract, you say “improvements in mathematical reasoning achieved through continued pre-training (CPT) are often less significant compared to those obtained via SFT.” If this is true, then why do you say in result 4 that “While SFT can facilitate some learning of mathematical capabilities, it has a clear disadvantage compared to CPT”?
- I think listing Results 1 to 8 is ineffective as it is easy for the reader to get lost and hard to understand the overall bigger picture. I recommend consolidation the results by topic to ensure clarity.
- I recommend explaining why you chose the data mixture ratios that you did and moving the less important training details like batch size to the appendix.
- Adding figures throughout would greatly enhance the argument. For example, add a main pipeline figure of the overarching framework you are implementing, and potentially new figures for sections 3, 4, and 5.
- The methodology appears insufficiently rigorous, particularly in the way data distribution and difficulty levels are analyzed.
- The experiments lack comprehensive justification, and the comparisons between different training setups (CPT vs. SFT) come across as arbitrary. What are the hypotheses leading to these decisions?
- Throughout the paper, there are bold claims about the effectiveness of problem-solving data and specific synthesis methods like Tutorship Amplification. I recommend relying less on superficial observations and instead adding more deep analysis of why certain methods are effective.
- I recommend adding some theoretical backing or intuition as to why these methods work.
- The paper repeatedly discusses the distinction between CPT and SFT stages, yet the insights presented do not meaningfully advance the reader's understanding. I recommend reducing redundancy and focusing on meaningful results.
- I am concerned about data quality. It seems there is heavy reliance on synthetic data and vague descriptions of the datasets. What is the data cleansing process?
- The real-world applicability or significance of JiuZhang-8B is not discussed.

Minor:
- “We employed the MinHash deduplicationLee et al. (2022) framework to enhance training data quality by removing documents with significant duplicate content.” should have a space between “deduplication” and “Lee”

### Questions
I feel that a lot of my questions are already contained in the weaknesses above. Here are some more:
- How do you ensure representative and high-quality data?
- Can you provide more intuition or theoretical support for these empirical results?
- Beyond releasing JiuZhang-8B, what are the practical implications of this research?
- The paper makes significant claims about the advantages of CPT over SFT in developing reasoning capabilities. How do the authors justify these findings theoretically? Could these results be influenced by the specific model architecture or training configuration used?
- Is there a detailed error analysis provided for cases where the model underperforms, especially on more complex mathematical problems?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper aims to understand how different aspects of training affect the ability of LLMs to do mathematical reasoning. This includes the tension between continuous pretraining and SFT, the use of problem solving data directly during CPT, the use of synthetic data generation and so forth. The authors provide a variety of fairly standard methods to test this, including some creative uses of synthetic data generation ( Query Expansion, Response Diversification, and Tutorship Amplification). They use LLAMA2 with the standard math evals, supplemented by a few that were introduced after the checkpoint in LLAMA2.  They apply their optimal methodologies to LLAMA3 to produce a new model JiuZhang-8B. JiuZhang-8B which has good performance especially relative to its size (Table 4)

### Strengths
The authors apply standard methods though in different variants than other work in this field. Their methods for synthetic data augmentation echo things I've seen before but not in this specific context.  They show some gains relative to larger models which is good.

### Weaknesses
This is solid work but does not feel like a major advance -- it is a set of good work with attention to evals and training procedures, but does not make any new conceptual advances.  IF ICLR were filled with papers like this one, the meeting wouldn't be intellectually exciting. This is very much "in the weeds" in engineering mixtures of LLM research

### Questions
What is the major advance of this paper?
What surprised you?
What did you learn that might generalize out of this narrow problem domain?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work investigates strategies to improve mathematical reasoning in large language models (LLMs). It explores the effects of:

Problem-solving Data: Focuses on using math-specific problem-solving data during the pre-training phase, rather than general mathematical text, to enhance reasoning skills.

Data Synthesis Methods: Evaluates four synthesis methods—response diversification, query expansion, retrospective enhancement, and tutorship amplification—for creating synthetic problem-solving data to overcome data scarcity.

Training Stages: Compares the impact of applying problem-solving data during the continued pre-training (CPT) phase versus the supervised fine-tuning (SFT) stage.

Results suggest that problem-solving data enhances math reasoning more effectively than general data. The paper introduces JiuZhang-8B, a math-specific LLM trained with insights from these strategies, which reportedly achieves comparable or superior performance to existing math-focused models despite fewer training tokens.

There are several interesting takeaways. For example, even if one provides many hard problems in the training data, expect improvements primarily in the easy/medium regime. Overall, this work is a valuable contribution to the community.

### Strengths
This work tackles several research questions and addresses them clearly and effectively. 

Specifically:

The study covers multiple aspects of training and data synthesis for LLMs in math reasoning, providing valuable insights into data handling (generation and sharding) strategies.

The analysis identifies tutorship amplification as particularly effective, offering practical value for generating synthetic data that improves reasoning abilities.

JiuZhang-8B demonstrates that the proposed methods lead to significant performance improvements, providing a practical model output as a proof of concept.

This work contributes to understanding how data complexity influences learning outcomes by segmenting data into difficulty levels and testing different mixtures.

### Weaknesses
While this paper summarizes several empirical results that are useful to the community, it makes limited efforts to advance understanding of the mechanics behind these observations. Future work in this direction would be of great value.

### Questions
Can the proposed synthetic data methods, especially "tutorship amplification", be effectively scaled or adapted to non-math domains?

How well would the identified CPT benefits translate to domains requiring other forms of reasoning (e.g., logical or scientific)?

Given the focus on hard data and high-volume problem-solving datasets, are there any recommendations for making this approach feasible for smaller labs with limited resources?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper aims to improve mathematical reasoning capabilities in large language models, investigating whether problem-solving data can outperform general mathematical corpora in improving these capabilities during pre-training. The study explores three research questions: (1) effectiveness of problem-solving data, (2) data synthesis methods, and (3) comparison between pre-training (CPT) and supervised fine-tuning (SFT) stages. Results indicate that problem-solving data significantly improves reasoning performance, with the "tutorship amplification" data synthesis method proving particularly effective. The paper also introduces JiuZhang-8B, a model based on these findings which performs comparatively with other math LLMs.

### Strengths
* The paper nicely states the research questions. Also arranging results along the corresponding research question smoothly helps with reading the paper.
* The level of details in the dataset, data mixture, and experiments is very good.
* The introduced model JiuZhang-8B achieves competitive performance with fewer tokens, highlighting efficient training and well curated training tokens.
* The results are clear and I like the attempts to explain why behind the results, particularly the advantage of CPT over SFT for reasoning tasks.

### Weaknesses
 * The paper shows promising results for mathematical reasoning but could benefit from testing on datasets that combine math with other fields, like physics. This would help assess if the model’s reasoning improvements generalize to interdisciplinary tasks requiring both math and domain knowledge, strengthening the case for broader applicability of the techniques.
* More analysis and clarity on why SFT underperforms CPT would strengthen the paper. Is the difference due to data volume limitations, catastrophic forgetting, or other factors?
* It would also be good to show some samples of the data, especially the generated or synthetic data. Also more details around data generation would be good like prompts or models used to generate data and if a human was used in the process for verification for example.

### Questions
* Is it really clear why SFT underperforms continual pretraining based on the experiments you performed?
* Does JiuZhang-8B learned math skills transfer to interdisciplinary tasks combining math with other fields?
* Could tutorship amplification be effective in other problem-solving domains?
* Is there any error analysis in JiuZhang-8B's problem-solving tasks?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to study the mathematical abilities of LLMs especially the effects of the type of training data (problem solving data vs general math data), using synthetic data in conjunction with real data, the effect of SFT vs CPT on the mathematical abilities of an LLM. The paper proposes training insights for optimizing the mathematical abilities of LLMs. The paper also proposes many synthetic data creation techniques like query expansion, retrospective enhancements, tutorship amplification for creating mathematical data. Finally they train a strong math specific model based on the findings of the previous questions.

### Strengths
- The paper is well written, and the overall direction of the paper is extremely important in the current times.
- Usually the data mixture ratio is one of the key secret sauces to training strong models, and the experiments in the initial section of the paper are important.
- The datasets used in the experiments are publicly available, and the experiments described in section 2 are extensive and cover the important cases.
- Synthetic data generation techniques can actually improve the robustness of the LLMs with respect to modifications (reframing of questions, or symbolic modifications) which could break the mathematical abilities of LLMs.

### Weaknesses
 - For figure 1, have you tried ablating the percentage of the math mixture to extremes like 2:8, 1:9 or even complete problem solving data. For the tasks considered in the paper, it could be the case that simply doing CPT with the problem solving data could be sufficient. It would be beneficial to see a more thorough exploration of the data mixture space, including scenarios where problem-solving data dominates or is the sole source of math-related training data. This is important because the optimal data mixture is often task-dependent, and a more detailed analysis could reveal whether the observed improvements are due to the specific mixture or simply the presence of any problem-solving data.
- Overall I could not find much weakness in the paper, the experiments seem easy to understand and sound.

### Questions
- For response diversification, it could happen that the model could generate incorrect logic leading to the correct answer, do you have simple checks in place to ensure that this does not happen?
- For results in table 2, how will the results change if you apply inference time techniques like Best-of-N sampling or using a reward models during inference? It could be that the conclusion changes significantly. One recent work (https://arxiv.org/pdf/2410.02725) showed that simply restarting the inference can change the accuracy on math tasks significantly.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 7

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper titled **"Advancing Mathematical Reasoning in Language Models: The Impact of Problem-Solving Data, Data Synthesis Methods, and Training Stages"** explores the limitations of current pre-training strategies for mathematical reasoning in large language models (LLMs). It addresses three primary research questions related to improving the model’s mathematical reasoning capabilities: (1) Whether problem-solving data during the pre-training phase is more effective than general mathematical corpora, (2) The efficacy of synthetic data, and (3) How these strategies differ between continued pre-training (CPT) and supervised fine-tuning (SFT). The authors present a variety of data synthesis methods and analyze their impact on model performance. The results suggest that problem-solving data significantly enhances performance, particularly when coupled with effective data synthesis techniques like tutorship amplification, leading to the development of a competitive model, JiuZhang-8B.

### Strengths
- The paper introduces new insights into the importance of problem-solving data and explores under-researched data synthesis methods like tutorship amplification. It delves into an interesting research question regarding the effect of data mix on performance. Additionally, the study examines the differing impacts of continual pretraining and supervised fine-tuning on final mathematical performance.

  These findings are likely to be of  importance for further research in the fields of pretraining and supervised fine-tuning. The paper's exploration of these topics contributes valuable knowledge to the ongoing development of machine learning models and their application in problem-solving tasks.

- The experiments are thorough, with detailed comparisons between different data types, synthesis methods, and training stages.  Although the technical depth is substantial, the paper is mostly well-written, with a clear exposition of the research questions and a logical progression through the results.

- This work could have a  impact on the development of LLMs for complex reasoning tasks, especially in mathematics. The introduction of JiuZhang-8B as a model trained on fewer tokens is interesting.

### Weaknesses
 - **Limited Practical Examples**: The paper could be enhanced by including more detailed, practical examples of how problem-solving data improves model performance. Concrete examples from the dataset would clarify the real-world impact of the proposed techniques.

- **Underexplored Larger Model Performance**:  The paper's experimental focus on mid-sized models like JiuZhang-8B, while informative, leaves a significant gap in understanding how the proposed methods perform and scale with larger language models. This limitation potentially understates the full impact and scalability of the presented approach.

  Expanding the analysis to include larger models in the 13B, 32B, or even 70B parameter range would provide crucial insights into the scalability and effectiveness of the proposed techniques. Such an expansion could reveal whether the benefits observed in mid-sized models persist, amplify, or perhaps even diminish when applied to more powerful language models. 

  Moreover, the inclusion of larger models in the study might necessitate an increase in the volume of training data. This presents an opportunity to further explore the interplay between data quality and quantity in the context of more capacious models. It could potentially reveal new insights into the optimal balance between these factors for different model sizes, providing valuable guidance for future research。

  

- **Generalization to Other Domains**: The focus is heavily on mathematical reasoning, but there is little discussion on how the proposed techniques might generalize to other domains that also require reasoning.

- **Data Synthesis Techniques**: Although the tutorship amplification method was shown to be most effective, the explanations for why certain methods (e.g., retrospective enhancement) performed poorly could be expanded. Further exploration of why specific synthesis methods yielded limited results would strengthen the paper.

### Questions
- Could the authors provide more specific examples of problem-solving data used during pre-training and demonstrate how it differs from general mathematical corpora?
- Could the authors provide more insights into the limitations of the retrospective enhancement technique? What additional methods or adjustments could make this approach more effective?
-  Have the authors considered applying the problem-solving data approach to other reasoning-heavy domains, such as physics or logic-based tasks? How would the methods transfer to these fields?
- How do the proposed data synthesis methods, such as tutorship amplification, perform when applied to larger LLMs like 72B? Is the impact equally significant?
- Given the success of the tutorship amplification method, do the authors plan to further refine this approach? Could it be applied in real-time tutoring systems or adaptive learning models for broader applications?

### Soundness
2

### Presentation
3

### Contribution
2
