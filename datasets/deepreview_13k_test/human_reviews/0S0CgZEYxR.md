# Examining the Achilles' Heel of CLIP Models: The Worst-Performing Categories

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
Contrastive Language-Image Pre-training (CLIP) provides a foundation model by integrating natural language into visual concepts. Although previous studies have demonstrated that satisfactory overall accuracy can be achieved across numerous downstream tasks through well-designed textual prompts, this evaluation mechanism inevitably overlooks certain categories because the impact of some underperforming categories on overall performance remains limited, even if they are highly important. For example, on ImageNet, there are a total of 10 categories with class-wise accuracy as low as 0\%, which is significantly inferior to the overall performance of 64.1\%. This phenomenon reveals the potential risks of using CLIP models, especially in risk-sensitive applications. To address this issue, we investigate the alignment between the two modalities in the CLIP model and propose the Class-wise Matching Margin (\cmm) to measure the inference confusion. \cmm\ can effectively identify the worst-performing categories and estimate the potential performance of the candidate prompts. We further query large language models to enrich descriptions of worst-performing categories and build a weighted ensemble to highlight the efficient prompts. Experimental results clearly verify the effectiveness of our proposal, where the accuracy on the worst-10 categories on ImageNet is boosted to 5.2\%, without manual prompt engineering, laborious optimization, or access to labeled validation data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates the terrible performance of CLIP models in certain categories of ImageNet and highlights potential risks associated with their applications. To address this issue, the paper proposes to enrich their textual prompts. The Class-wise Matching Margin (CMM) is introduced as a measure of inference confusion, quantifying the margin between the similarity of images to the correct textual prompt and the most susceptible one. Leveraging LLMs, the paper enriches the textual prompts for these categories, leading to improved performance according to the conducted experiments.

### Strengths
The examination of the worst-performing categories in ImageNet is intriguing.

### Weaknesses
The problem definition lacks clarity and requires further elaboration. Specific information regarding the worst-performing classes in ImageNet is missing, hindering readers from determining whether the poor performance stems from inherent ambiguities within these classes or issues with the model itself. Additionally, the paper neglects to compare CLIP models with models learned using other methods, such as supervised learning or visual contrastive learning. This omission makes it challenging to discern whether the identified problem is exclusive to CLIP models or prevalent across all models, significantly impacting the paper's contribution.

The proposed method is relatively straightforward and does not exhibit notable performance improvements. The idea of enhancing performance through enriched textual prompts is intuitive, resulting in limited novel insights provided by this paper. Furthermore, the analysis of the specific effects of richer textual prompts on the model remains superficial.

In conclusion, this article lacks a clear and concise problem definition, and the underlying causes of the identified problem are unclear. Moreover, the proposed method is relatively trivial, yielding only modest performance improvements. Consequently, the contribution of this article falls short of justifying its publication at ICLR.

### Questions
No other questions.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the zero-shot image classification ability of CLIP. It mainly improves the accuracy of the worst categories. The paper proposes a Class-wise Matching Margin (CMM) to measure the underperforming categories. CMM is calculated based on the similarities of images and textual prompts. It can identify the worst-performing categories and estimate the potential performance of the candidate prompts. Furthermore, large language models are requested to enrich descriptions of worst-performing categories and build a weighted ensemble of prompts. CMM boosts the accuracy on the worst-10 categories on ImageNet to 5.2%, without manual prompt engineering, laborious optimization, or access to labeled validation data.

### Strengths
1. This paper is easy to follow.
2. Comprehensive experimental results are provided, and illustrations of the results are great.
3. There are complete implementation details of the method.

### Weaknesses
1. The main concern is the technical contribution. CLIP uses image-text similarity to perform zero-shot classification, so evaluating the similarities roughly equals evaluating classification accuracy. 
2. Pseudo-CMM is not clearly described. How to set the pseudo label for a sample?
3. The CPE algorithm is conducted on the test set. Although the paper claims the annotations are not used, it still seems inappropriate.

### Questions
1. What is the pseudo labels for test set?
2. Does each category have its own ensemble of prompts?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses a very interesting and overlooked topic: the worst-performing class of CLIP. To mitigate this issue, the authors propose CMM  to measure confusion. Also, the authors query LLM to enrich the descriptions of worst-performing categories. Experiments prove the effectiveness of the proposed method.

### Strengths
1. The discussion topic is very interesting and novel for me, I like it;
2. Good writing and smooth description;
3. Good discussion and meaningful visualization.

### Weaknesses
1. The contribution is not enough. I fully understand the importance of the discussed topic. But could you show more insight and the importance of your paper?
2. I cannot understand the LLM meaning in your paper: “We further query large language models to enrich descriptions of worst-performing categories.” Can we use other description models? Or can we describe the categories by ourselves? Ablation studies needed?
3. The paper is not well self-defined. For example, what PE in the Figure 1 means?
4. The main discussion of the paper is on CLIP? Have you investigated other methods? Such as BLIP. Do their worst prediction same with CLIP? Or could you ensemble different VL models to solve the problem you discussed?

### Questions
I think this paper's score should be between 5 and 6. Please provide a detailed rebuttal to convince me and further clarify your contribution.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
