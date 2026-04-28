# Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation

- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 6, 6, 6

## Abstract
With the recent emergence of foundation models trained on internet-scale data and demonstrating remarkable generalization capabilities, such foundation models have become more widely adopted, leading to an expanding range of application domains. Despite this rapid proliferation, the trustworthiness of foundation models remains underexplored. Specifically, the out-of-distribution detection (OoDD) capabilities of large vision-language models (LVLMs), such as GPT-4o, which are trained on massive multi-modal data, have not been sufficiently addressed. The disparity between their demonstrated potential and practical reliability raises concerns regarding the safe and trustworthy deployment of foundation models. To address this gap, we evaluate and analyze the OoDD capabilities of various proprietary and open-source LVLMs. Our investigation contributes to a better understanding of how these foundation models represent confidence scores through their generated natural language responses. Based on our observations, we propose a self-guided prompting approach, termed \emph{Reflexive Guidance (ReGuide)}, aimed at enhancing the OoDD capability of LVLMs by leveraging self-generated image-adaptive concept suggestions. Experimental results demonstrate that our ReGuide enhances the performance of current LVLMs in both image classification and OoDD tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The goal for the paper is to evaluate the out-of-distribution detection (OoDD) capabilities of LLMs (some private and open models)

### Strengths
- easy to read
- easy to duplicate

### Weaknesses
 - motivation for the work
- limited impacts
- extending from a prior work in text-based method.

### Questions
- Why we need to evaluate the capabilities 
- as LLM gets huge weekly, the measurement still makes sense?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a self-guided prompting approach, termed Reflexive Guidance (ReGuide), aimed at enhancing the OoDD capability of LVLMs by leveraging self-generated image-adaptive concept suggestions. Experimental results demonstrate that our ReGuide enhances the performance of current LVLMs in both image classification and OoDD tasks

### Strengths
Strengths:
•This paper represents the first effort to extend zero-shot Out-of-Distribution Detection (OoDD) to generative Large Vision-Language Models (LVLMs) in reference to CLIP. Building upon this foundation, the authors define the task and propose corresponding evaluation methodologies, which offer valuable insights for future research；
•The paper evaluates and analyzes the OoDD capabilities of various proprietary and open-source LVLMs. Furthermore, the authors propose a two-stage self-guided prompting approach, termed Reflexive Guidance (ReGuide), to unlock the potential of LVLMs. Experimental results demonstrate that the ReGuide enhances the performance of LVLMs in both image classification and OoDD tasks.

### Weaknesses
Weaknesses:
•The paper introduces new tasks and evaluation metrics. However, certain details in this regard are somewhat lacking. For instance, the paper mentions using only 25% of the benchmark subsets but does not specify which portions are utilized. It would be preferable to provide a list of these subsets to facilitate the replication and comparison of subsequent work. Additionally, other similar details need to be verified.

•In the experimental evaluation, the ‘valid ratio’ varies across different methods. And only valid responses are included when measuring performance, which results in inconsistencies in the samples used to calculate metrics for each method. This may not be justifiable. Have you considered adopting a more consistent evaluation approach?

•The novelty of this paper is somewhat limited.  Firstly, it introduces the OoDD task for LVLMs; however, the rationale behind this task remains debatable. Considering the robust capabilities of LVLMs and their ongoing advancements, LVLMs are anticipated to directly recognize objects within images. In comparison, the method proposed in this paper is overly complex and excessively reliant on prompts. Secondly, the approach presented in the paper appears to be more akin to prompt engineering, lacking substantial innovative contributions.

### Questions
see weakness

### Soundness
3

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
3

### Summary
Overall this is a solid paper. This paper addresses the underexplored trustworthiness of foundation models, particularly focusing on the out-of-distribution detection (OoDD) capabilities of large vision-language models (LVLMs). The authors highlight the gap between the demonstrated potential and practical reliability of LVLMs, raising concerns about their safe deployment. To address this, the researchers evaluate and analyze the OoDD capabilities of various proprietary and open-source LVLMs. They propose a novel approach called Reflexive Guidance (ReGuide), which aims to enhance the OoDD capability of LVLMs by using self-generated image-adaptive concept suggestions. Experimental results show that ReGuide improves the performance of current LVLMs in both image classification and OoDD tasks.

### Strengths
[Promising research topic] This paper focuses on an under-explored topic, the reliability of large vision-language models. [Benchmark contribution] This paper define the concept of Out-of-Distribution Detection on LVLMs, and conduct extensive experiments to build a benchmark and give insightful analysis. [Method contribution] Furthermore, they propose a method ReGuide on the prompt to boost the performance of LVLMs. They verify the effectiveness of the proposed method on GPT-4o and InternVL.

### Weaknesses
Since the out-of-distribution detection on vision-language foundation models is a new definition proposed in this paper, I would suggest to add a demonstration figure to show this concept in a visually straightforward way. You can compare the conventional OOD, OoDD on CLIP and OoDD on LVLMs.

### Questions
Please see Weaknesses.

### Soundness
3

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
This paper explores to enhance out-of-distribution detection (OoDD) in large vision-language models (LVLMs). The authors emphasize the increasing importance of these models in various domains and highlight the challenges related to their trustworthiness, specifically in dealing with out-of-distribution (OoD) inputs. To address this, they propose a self-guided prompting approach called Reflexive Guidance (ReGuide), which leverages LVLMs’ visual interpretation capabilities to improve OoD detection by generating image-adaptive concept suggestions. The experiments demonstrate that ReGuide significantly boosts the performance of both open-source and proprietary models in OoD detection tasks.

### Strengths
1. The introduction of the ReGuide method is interesting. By using image-adaptive concept generation, the authors provide a unique solution to enhance OoD detection in LVLMs. This approach leverages the strong visual recognition capabilities of these models, offering a novel way to bridge gaps in OoD detectability.

2. Comprehensive Evaluation: This paper comprehensively evaluates both proprietary and open-source LVLMs, providing a balanced comparison across different models. This may be helpful for future research.

3. Detailed Analysis: The authors provide a well-rounded analysis, including experimental results, visual feature interpretation, and the effectiveness of ReGuide on near- and far-OoD datasets. This depth of analysis gives credibility to their findings and demonstrates the robustness of their proposed method. Furthermore, it demonstrates the potential of introducing LVLMs to the area,

### Weaknesses
1. Limited Explanation of Failures: Although the paper provides examples of failure cases, it does not fully delve into the underlying causes or offer detailed solutions for these issues. While the authors acknowledge the problem of overconfidence in models such as GPT-4o with ReGuide, further exploration of these limitations could strengthen the study. There is still not a robust method to effectively introduce LVLMs to the OoD tasks.

2. Model-Specific Insights: The paper focuses on generic findings across models, but a deeper investigation into how specific models (e.g., GPT-4o vs. InternVL2) behave differently when ReGuide is applied could add nuance to the conclusions. For example, the differences in false positive rates (FPR) between models with and without ReGuide should be presented for a better comparison. 

3. Scalability and Practicality: While the ReGuide method shows a promising direction, the computational overhead and API limitations mentioned in the paper could present challenges for practical, large-scale implementation. This issue is touched upon but not sufficiently addressed in terms of how ReGuide might be optimized for deployment at scale. Meanwhile, the inference cost analysis can further improve the paper's quality and inspire further work.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2
