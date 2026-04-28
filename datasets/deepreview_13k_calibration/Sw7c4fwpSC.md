# Assessing Open-world Forgetting in Generative Image Model Customization

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Recent advances in diffusion models have significantly enhanced image generation capabilities. However, customizing these models with new classes often leads to unintended consequences that compromise their reliability. We introduce the concept of \textit{open-world forgetting} to emphasize the vast scope of these unintended alterations, contrasting it with the well-studied \textit{closed-world forgetting}, which is measurable by evaluating performance on a limited set of classes or skills.
Our research presents the first comprehensive investigation into open-world forgetting in diffusion models, focusing on semantic and appearance drift of representations. We utilize zero-shot classification to analyze semantic drift, revealing that even minor model adaptations lead to unpredictable shifts affecting areas far beyond newly introduced concepts, with dramatic drops in zero-shot classification of up to 60\%. Additionally, we observe significant changes in texture and color of generated content when analyzing appearance drift.
To address these issues, we propose a mitigation strategy based on functional regularization, designed to preserve original capabilities while accommodating new concepts. Our study aims to raise awareness of unintended changes due to model customization and advocates for the analysis of open-world forgetting in future research on model customization and finetuning methods. Furthermore, we provide insights for developing more robust adaptation methodologies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the issue of “open-world forgetting” in generative image model customization, highlighting how fine-tuning models for new classes can inadvertently degrade performance on previously learned classes. The authors systematically analyze open-world forgetting through the introduction of semantic and appearance drift concepts, using zero-shot classification to measure semantic drift. To mitigate this issue, they propose a “drift correction” method, designed to reduce the model's tendency to forget prior knowledge when learning new concepts. Experiments demonstrate that drift correction significantly reduces semantic and appearance drift, enhancing the stability and reliability of customized models.

### Strengths
The introduction of open-world forgetting is a novel perspective in the domain of diffusion model customization. While previous research often focuses on task-specific performance, this paper broadens the scope of forgetfulness evaluation, bringing strong innovation.

### Weaknesses
1. The paper’s structure is confusing. For instance, lines 513-532 discuss contributions to open-world forgetting before defining it clearly, and these lines largely repeat lines 108-119, adding unnecessary redundancy.

2. Key metrics lack basic explanation in the main text, with details only in supplementary materials. This makes it hard for readers to grasp the evaluation approach without prior knowledge.

3. The paper focuses on how fine-tuning degrades original model capabilities but doesn’t assess how the proposed method impacts performance on the fine-tuning tasks.

### Questions
1. Were alternative metrics for measuring semantic drift considered? For instance, could user evaluations on the semantic consistency of generated images be feasible?

2. Has the drift correction method been tested on more complex or diverse concepts beyond the simple categories presented? For example, in Figure 2a, “a sampled pair from the most dissimilar outputs (purple triangle) shows a complete change in content, colors, and scene composition that no longer matches the prompt.”, What happens if drift correction is applied in this case, do the colors and scene composition match the prompts better?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the concept of "open-world forgetting" to emphasize the vast scope of these unintended alterations during the model customization of foundation generative models (i.e., Stable Diffusion). The authors conduct a comprehensive investigation of the semantic and appearance drift of representations. To address these issues, this paper proposes a mitigation strategy based on functional regularization which preserves original capabilities while accommodating new concepts. The contribution of the paper can be summarized as follows:

1. $\textbf{Introduction of Open-World Forgetting Concept:}$ The paper defines open-world forgetting in pre-trained foundation generative image models and systematically assesses its impact, focusing on how models lose previously learned concepts after adaptation.

2. $\textbf{Semantic and Appearance Drift Analysis:}$ It introduces two evaluation approaches:
Semantic Drift: Uses zero-shot classification to measure changes in a model's semantic understanding.
Appearance Drift: Examines shifts in visual attributes like color and texture after customization, introducing the "Color Drift Index" (CDI) as a metric for quantifying these changes.

3. $\textbf{Mitigation Strategy:}$ The paper proposes a functional regularization technique aimed at reducing open-world forgetting, enabling models to integrate new concepts while retaining prior knowledge. This method proved effective in maintaining both semantic and appearance integrity in fine-tuned models.

### Strengths
1. The concept of open-world forgetting represents a novel extension to the field of model adaptation and customization, particularly in generative models. While catastrophic forgetting has been explored in closed-world contexts, applying it to open-world scenarios in text-to-image models is original and fills an important gap in understanding how fine-tuning affects broad model knowledge.
2. The proposed Color Drift Index (CDI) for assessing appearance drift is a new and creative metric tailored to the nuances of generative models. This provides a fresh approach to evaluating visual consistency, which goes beyond typical performance metrics in generative model research.
3. By providing quantitative results with the CDI and zero-shot classification performance across multiple models and concepts, the authors present strong empirical evidence for their findings, which enhances the reliability of their conclusions.
4. The use of functional regularization as a mitigation strategy is well-executed and shows practical effectiveness, backed by solid data on how it mitigates both semantic and appearance drift.
5. By proposing methods to measure and mitigate unintended model alterations, the work establishes a foundation for future research on safeguarding foundational knowledge in generative models, which will inspire other researchers to work in this direction in the future.
6. The proposed method is simple yet effective and the writing of the paper is clear and easy to follow.

### Weaknesses
The authors have mentioned some of the limitations in the paper:
1. The analysis is limited to a small subset of concepts and may not capture all potential instances of forgetting. 10 concepts are apparently not enough to reflect the effectiveness of the proposed method comprehensively. The scale is recommended to be scaled up to at least a hundred to thousand level.
2.  This study has mainly focused on evaluating the impact of diffusion model customization and only focuses on evaluating two very representative but not new (DB was proposed in 2022) works. The results would be more convincing if the authors evaluated their methods on more SOTA methods. For instance, as the author mentioned in the related works:

[1] Ligong Han, Yinxiao Li, Han Zhang, Peyman Milanfar, Dimitris Metaxas, and Feng Yang. Svdiff:
Compact parameter space for diffusion fine-tuning. ICCV, 2023b.

[2] Wenhu Chen, Hexiang Hu, Yandong Li, Nataniel Rui, Xuhui Jia, Ming-Wei Chang, and William W
Cohen. Subject-driven text-to-image generation via apprenticeship learning. arXiv preprint
arXiv:2304.00186, 2023b.

[3] Jing Shi, Wei Xiong, Zhe Lin, and Hyun Joon Jung. Instantbooth: Personalized text-to-image
generation without test-time finetuning. arXiv preprint arXiv:2304.03411, 2023a.
3. The results in Table 1 and Table 2 are not significant enough.

### Questions
1. Is the customization method used in Figure 3 DB? Please clarify it in the revised version,
2. I recommend the author to increase the number of concepts in the evaluation. 10 concepts might be a "cherry pick".
3. Add more images generated by the model before and after applying your methods which would be intuitive and easy to understand.

Overall, I believe this paper is valuable to the community and I would be happy to raise the score if my concern can be well addressed.

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
4

### Summary
This paper presents a study on open-world forgetting during the customization of generative image models, specifically focusing on diffusion models like Stable Diffusion. The authors define open-world forgetting as the unintended changes in model behavior when adapted to new classes or content, distinguishing it from the more limited scope of closed-world forgetting. They explore how fine-tuning models with even small sets of data  can lead to significant drifts in both the semantic understanding and appearance of images generated by the model. Key methodologies discussed include using zero-shot classification to measure semantic drift and assessing changes in appearance through color and texture analysis. The paper also introduces a mitigation strategy through functional regularization to minimize these drifts while incorporating new concepts.

### Strengths
1. The paper successfully highlights the issue of open-world forgetting, which is less studied compared to closed-world scenarios, providing a valuable framework for further research in model customization.
2. The use of zero-shot classification to quantify semantic drift and the introduction of novel metrics for appearance drift offer robust tools for understanding model behavior post-customization.

### Weaknesses
1. While the study provides detailed insights into open-world forgetting, the generalizability of the findings across different types of generative models or broader sets of data remains unclear.
2. The mitigation strategy's effectiveness is potentially limited by the quality of the data used for fine-tuning and the subjective nature of assessing image quality and drift.
3. How does the model perform when fine-tuned with highly diverse or noisy datasets? Does the regularization technique maintain its effectiveness across such variations?
4. What is the long-term stability of models customized using these techniques? Do they continue to maintain reduced levels of forgetting with continued use or additional rounds of customization?
5. How do quantitative assessments of drift align with qualitative evaluations from human observers? Is there a significant disparity, and how can it be addressed?

### Questions
See weaknesses.

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
This paper delves into open-world forgetting in diffusion models,. Unveiling semantic and appearance drift, this paper proposes functional regularization to maintain original capabilities. Besides, this paper supports studying open-world forgetting and offers insights for stronger adaptation methods.

### Strengths
1.The paper is well-written and easily comprehensible.

2.The proposed method is simple and straightforward.

3.The motivation for addressing both Appearance Drift and Semantic Drift is commendable.

### Weaknesses
1. This paper solely analyzes Appearance Drift and Semantic Drift in the context of OPEN-WORLD FORGETTING, leaving uncertainties about their occurrence in closed-world scenarios. It is unclear if the observed drifts are unique to open-world settings or if similar phenomena would manifest when fine-tuning a model on a fixed, limited set of classes. The paper should discuss the potential for these drifts in closed-world scenarios and provide justification for focusing solely on open-world forgetting.

2. The analysis in this paper focuses on two methods, Dreambooth and CustomDiffusion, overlooking recent approaches like BLIP-Diffusion [1] and HyperDreamBooth [2]. It is not clear whether the conclusions drawn about Appearance Drift and Semantic Drift are generalizable across different personalization techniques. The paper needs to address the potential for these drifts in other methods, particularly those that employ different training strategies or architectures. Specifically, how do methods like BLIP-Diffusion, which uses a pre-trained subject representation, and HyperDreamBooth, which utilizes hypernetworks, behave with respect to these drifts? Do these methods inherently mitigate or exacerbate the observed drifts?

3. While this paper claims to mitigate Appearance Drift and Semantic Drift using a mitigation strategy, the relevant qualitative results are missing, and the effectiveness needs to be intuitively demonstrated. The paper lacks visual evidence to support the claim that the proposed mitigation strategy effectively reduces the observed drifts. Without qualitative examples, it is difficult to assess the practical impact of the proposed mitigation. The paper should include visual comparisons of generated images before and after applying the mitigation strategy to demonstrate its effectiveness.

4. The related work section requires updating. For instance, [2] and [3] in relation to this paper should be discussed and analyzed. The paper should provide a more comprehensive overview of the existing literature on diffusion model personalization and forgetting. The discussion should include a detailed analysis of how the proposed method relates to and differs from other approaches, including those that address similar issues or use similar techniques.

### Questions
Please see the above Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
