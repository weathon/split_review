# How Jailbreak Defenses Work and Ensemble? A Mechanistic Investigation

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Jailbreak attacks, where malicious prompts bypass generative models’ built-in safety, have raised significant concerns about model vulnerability. While diverse defense methods have been proposed, the underlying mechanisms governing the trade-offs between model safety and helpfulness, and their application to Large Vision-Language Models (LVLMs) remain insufficiently explored. This paper systematically investigates jailbreak defense mechanisms by reformulating the standard generation task as a binary classification problem to probe model refusal tendencies across both harmful and benign queries. Our analysis identifies two key defense mechanisms: safety shift, which generally increases refusal probabilities for all queries, and harmfulness discrimination, which enhances the model’s ability to distinguish between benign and harmful queries. Leveraging these mechanisms, we design two ensemble defense strategies—inter-mechanism and intra-mechanism ensembles—to explore the safety-helpfulness balance. Empirical evaluations on the MM-SafetyBench and MOSSBench datasets on top of LLaVA-1.5 models demonstrate the effectiveness of these ensemble approaches in either enhancing model safety or achieving an improved safety-utility balance. These findings offer valuable insights into jailbreak defense strategies and contribute to the development of more resilient LVLM safety systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper attempts to characterize internal jailbreak defenses into two categories: Safety Shift and Harmfulness Discrimination. The authors do this by prompting the model with a classification question and analyzing the output distribution for benign and harmful queries. Using this formulation, the paper propose intra and inter mechanism ensembling techniques that help balance the safety and usefulness trade-off offered by the model. The evaluation is performed on LLaVA-1.5.

### Strengths
The author tackle an important problem of characterizing how LLM jailbreak defenses work. The paper is well written and motivated. I appreciate the author's effort in evaluating a variety of defenses. Moreover, attributing defenses to safety shift and harmfulness discrimination is an interesting idea.

### Weaknesses
1. The analysis in this paper can also be applied to text-only LLMs. Since, text-only LLMs are more widely used, the authors should consider expanding the analysis.
2. The whole analysis focuses on affirmative response on benign queries and refusal on harmful queries. However, it does not take into account the quality of the generated responses (specially since the evaluation uses a pattern matching based judge). Combining multiple defenses could severely harm the quality of the returned responses. For instance, the query refactoring method Caption w/o image first captions the image and then adds it as text to the model prompt. While helping with safety, this would lead to decrease in quality of responses on benign queries.
3. The mechanistic analysis is done on a classification setting, and the insights might not transfer to the generative setting (as also hinted by the authors).

### Questions
1. The paper performs the entire evaluation on a single LVLM - LLaVA-1.5. It would be interesting to see if the findings generalize to other LVLMs like CogVLM and InternLM-XC.
2. The mechanistic analysis characterizes defenses as either safety shift or harmfulness discrimination. However, Figure 3 (b) shows that combination of SR + MO i.e. two safety shift techniques lead to an increase in distance from 0.5 to 0.63. This suggests that defenses might be providing different degrees of both safety shift and harmfulness discrimination.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the trade-off between safety and helpfulness in jailbreak defenses, highlighting two fundamental mechanisms: safety shift and harmfulness discrimination. The authors analyze various ensemble strategies to enhance model safety and improve the safety-helpfulness balance, demonstrating their effectiveness across multimodal contexts.

### Strengths
1. Introduces novel defense mechanisms (safety shift and harmfulness discrimination) for LVLMs, providing fresh insights into model security. 
2. Includes a comprehensive analysis supported by rigorous empirical validation across various datasets and models, utilizing a robust methodology by reformulating generation tasks into classification problems.
3. Evaluates two ensemble defense strategies (inter-mechanism and intra-mechanism integration), examining the balance between enhancing model safety and preserving usability.

### Weaknesses
1. The captions for the figures and tables in the paper are overly simplistic.
2. The experiments primarily rely on the MM-SafetyBench and MOSSBench datasets, which may not fully reflect the diversity and complexity of real-world scenarios.
3. While the paper proposes various defense strategies, it may not adequately discuss their feasibility and cost-effectiveness in practical deployment.

### Questions
1. While the paper focuses on LLaVA-1.5-7B and LLaVA-1.5-13B, how do the authors ensure that the findings apply to other models within the LLaVA series?
2. Can the captions for figures and tables be more detailed?
3. What is the optimal combination of the 27 defense methods, and can you analyze why this combination yields better results? Additionally, do these findings have universality for other models, such as language models?
4. Will these defense strategies affect the model's real-time response speed? Will they introduce additional overhead?

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
3

### Summary
This paper propose a novel and straightforward way to reformulate the
LVLM's generation problem as a binary classification problem, in order to
investigate the the mechanism of Jailbreak Defenses.

### Strengths
1. A new angle to investigate jailbreak defenses is proposed. It is 
   interesting.
2. The reformulation practice is interesting and valuable, providing a
   effective way to investigate the mechanism of jailbreak defenses.
3. Extensive experiments across various jailbreak defenses are conducted.

### Weaknesses
1. The motivation behind focusing on LVLMs is not clear.
2. Further analysis on the results (especially the ensemble part) is needed.
3. The selection of models under evaluation is not convincing.

### Questions
1. I believe the reformulation practice is valuable and straightforward.
   However, it seems that it can also be applied to other types of models,
   like LLMs. What is the motivation behind focusing on LVLMs?
2. The ensemble part is not well analyzed. Could you provide more insights
   on the ensemble mechanism? For example, provide some specific suggestions
   for ensemble strategies.
3. The selection of models under evaluation is not convincing; both models
   are LLaVA. Could you add some more models with different architectures
   to make the evaluation more convincing?
4. Given the results presented in Figure 4, does there exist any way to
   further investigate the representative power of the binary classifier?
   Furthermore, can this representative power of the binary classifier
   be improved?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper systematically investigates jailbreak defense mechanisms by reformulating the generative task as a binary classification problem to probe model refusal tendencies across both harmful and benign queries. Focusing on internal strategies, this study identifies two key defense mechanisms: safety shift and harmfulness discrimination. They increase refusal probabilities for all queries and enhance the model’s ability to distinguish benign and harmful queries, respectively. Experiments demonstrate the effectiveness of the ensemble defense mechanism.

### Strengths
1. This paper is well-written and easy to follow.

2. Two metrics, Mean Shift and Distance Change, are reasonable and can help to visualize the differences between different types of defenses.

3. The experiment part is comprehensive and some insights in Section 4.4 and 4.5 are interesting.

### Weaknesses
1. Although the authors mention that they do not assess the actual usefulness of model’s responses, but rather the willingness from a safety perspective, a core concern of this reviewer is that “Can some seemingly effective defense methods, like refactoring, truly keep a good performance on benign queries?”.

2. Lack of the experiments of defenses against stronger and various attackers. This reviewer is worried about the limit of attack methods, as well as the datasets. MM-Safety-Bench is a comprehensive benchmark, but the malicious query is quite direct and lacks of stealthiness. “Hide the text queries at the bottom of associated images” can only represent a few types of attack methods. More experiments on stronger or various attackers are recommended.

3. Although the experiment part is comprehensive, it lacks of some mainstream model optimization defenses, such as PPO and DPO.

### Questions
1. See weakness 1. Can some seemingly effective defense methods, like refactoring, truly keep a good performance on benign queries?

2. See weakness 2. Can MM-SafetyBench and MOSSBench represent most attack vectors?

### Soundness
3

### Presentation
4

### Contribution
3
