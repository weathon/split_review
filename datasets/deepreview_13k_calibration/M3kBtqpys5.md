# Trusted Multi-View Classification via Evolutionary Multi-View Fusion

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 8, 3, 6

## Abstract
Multi-view classification methodologies grounded in the Dempster-Shafer theory, renowned for their reliability in decision-making, have garnered significant application across various safety-critical domains due to their capacity to provide a degree of trustworthiness for each view. However, the adoption of a late fusion strategy by these methodologies constrains the interaction of information among views, thereby leading to suboptimal utilization of multi-view data. A recent advancement aimed at mitigating this limitation involves the generation of a pseudo view by concatenating all individual views. Nonetheless, the effectiveness of this pseudo view may be compromised when incorporating underperforming views, such as those afflicted by noise. Furthermore, the integration of a pseudo view exacerbates the issue of imbalanced multi-view learning, as it contains a disproportionate amount of information compared to individual views. To address these multifaceted challenges, we propose an approach termed Enhancing Trusted multi-view classification via Evolutionary multi-view Fusion (TEF). Specifically, we introduce an evolutionary multi-view architecture search method to generate a high-quality fusion architecture serving as the pseudo view, thus enabling adaptive selection of views and fusion operators. Subsequently, each view within the fusion architecture is enhanced by concatenating the decision output of the fusion architecture with its respective view. Our experimental findings underscore the efficacy of this straightforward yet potent strategy in mitigating the imbalanced multi-view learning problem, consequently enhancing TEF's performance, particularly on complex many-view datasets featuring more than three views compared to its counterparts. Comprehensive experimental evaluations conducted on six multi-view datasets corroborate the superior performance of our proposed method over other trusted multi-view learning approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper illustrates two main issues in existing trustworthy fusion methods: the lack of feature interaction in late fusion and the insufficient attention given to multi-view imbalance, which leads to inadequate training and suboptimal performance. To address this, the authors innovatively propose an evolutionary computation adaptive method that introduces high-quality pseudo-views, significantly enhancing the performance of trustworthy fusion methods on complex multi-view datasets. Furthermore, the authors present an effective solution for view imbalance and conduct extensive experiments to validate its effectiveness.

### Strengths
1. The paper presents the motivation for the research in detail through illustrations, and the structure of the paper is logical and well-written.
2. The paper demonstrates considerable innovation, as the authors first identify two key challenges in trustworthy multi-view fusion and provide effective solutions.
3. The authors validate the effectiveness of their method through extensive experiments, with results showing significant advantages over existing trustworthy and non-trustworthy fusion methods across five evaluation metrics on six datasets.

### Weaknesses
1. I am interested in your concatenation operation. Why is the late-stage fusion information only concatenated with the pseudo-views and not with the original views? What effects would concatenation have?
2. Why did you choose evolutionary computation for generating pseudo-views? Have you considered gradient neural architecture search or reinforcement learning?
3. Can early fusion features not assist in training? Why was the final choice made to use late-stage features to address view imbalance?

### Questions
See in the weakness.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This research is significant in the field of trustworthy fusion and addresses two main challenges in current methods. First, many approaches overlook feature-level interactions, resulting in suboptimal performance. Second, high-quality pseudo-views exacerbate multi-view imbalance. The authors propose the TEF method, which utilizes evolutionary multi-view architecture search to generate high-quality pseudo-views, enabling adaptive selection of viewpoints and fusion operations. Experimental results demonstrate that this strategy significantly enhances TEF's performance on complex multi-view datasets, particularly in cases with three or more viewpoints. Evaluation results confirm the superiority of the proposed method compared to existing techniques.

### Strengths
1. The authors first review previous work and identify its limitations.  
2. They innovatively introduce neural architecture search to generate high-quality pseudo-view architectures, providing a detailed description that effectively addresses the issue of insufficient feature interaction. Although this technique is time-consuming, it offers an effective solution.  
3. The use of concatenation operations to solve the imbalance between multi-views is actually quite interesting, appearing simple yet effective.  
4. Extensive experiments also demonstrate the effectiveness of TEF.

### Weaknesses
See in the questions.

### Questions
1. The paper indicates that introducing a single pseudo-view is effective; have there been any attempts to use multiple pseudo-views to further enhance the results?
2. Is this method a general concept? Can other trustworthy fusion methods also adopt similar strategies to improve model performance?
3.What do you believe is the fundamental reason behind achieving state-of-the-art results?
4.Regarding the time-consuming issue caused by using the NAS algorithm, while the paper suggests some solutions, I would still like to know if the authors have plans for further research in the future to tackle more complex data or deeper network issues.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents TEF (Trusted multi-view classification via Evolutionary Fusion), aiming to address challenges in multi-view classification such as limited view interaction and learning imbalance. TEF utilizes evolutionary neural architecture search to create pseudo-views and applies a balanced fusion strategy. The method shows potential improvements over existing approaches in certain comparisons.

### Strengths
1. Combines evolutionary NAS with multi-view classification, offering a novel approach.
2. The methodology is clearly explained with effective visuals.

### Weaknesses
1. The emphasis on learning imbalance within pseudo-view-guided multi-view classification may not be as critical as the authors suggest. As long as the overall contributions of different views are balanced, focusing on the specific imbalance of the pseudo-view might be unnecessary. More evidence or justification would be helpful to show that this imbalance significantly impacts performance.

2. The experimental comparisons may not ensure fairness, as it seems that the benchmarks used in this study do not align with those originally used in previous TMVC methods (e.g. ECML [1]). This raises concerns about consistency and fairness. Clarifying whether all models were evaluated under similar conditions would improve the reliability of the results.

3. The claimed robustness of TEF in handling noisy or uncertain real-world data is not well-demonstrated. More experiments simulating practical conditions are needed to validate this aspect.

4. Actually, the method seems to rely on aligning pseudo-view generation with target domain performance using validation labels. However, when samples are noisy, there appears to be no specific strategy to mitigate this noise. How does your approach show advancements over existing methods, especially given that Evidential Deep Learning has known limitations in fusion frameworks that could risk performance degradation?

### Questions
1. Can you provide more justification or empirical evidence showing that learning imbalance within pseudo-view-guided multi-view classification significantly impacts model performance?

2. The benchmarks used in the paper seem different from those used in prior TMVC studies. Were the TMVC methods evaluated under the same conditions as your proposed TEF? Clarifying this would address concerns about fairness in experimental comparisons.

3. Can you show additional experiments or real-world examples demonstrating TEF's effectiveness in handling noisy or uncertain data?

4. Actually, the method seems to rely on aligning pseudo-view generation with target domain performance using validation labels. However, when samples are noisy, there appears to be no specific strategy to mitigate this noise. How does your approach show advancements over existing methods, especially given that Evidential Deep Learning has known limitations in fusion frameworks that could risk performance degradation?

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
4

### Summary
The paper addresses the issues present in pseudo-views generated by previous methods and proposes a solution. It introduces an evolutionary multi-view architecture search approach to generate high-quality fusion architectures to serve as pseudo-views, thus enabling adaptive selection of views and fusion operators.

### Strengths
The overall writing of the paper is smooth and easy to understand.

The experimental results are extensive and solid.

### Weaknesses
I'm not sure if the proposed pseudo-view generation method is innovative compared to previous neural architecture search (NAS) methods. 

Additionally, I'm uncertain whether the proposed method can be applied to large-scale end-to-end multimodal datasets. This is because the method might be inefficient, especially for high-dimensional and complex multimodal data, and the number of operators in the NAS process may be insufficient to cover all necessary functions. Increasing the number of operators might also lead to a significant increase in computational cost. I am open to increasing the score upon receiving a well-justified explanation.

### Questions
Could you please describe in detail the differences from other multi-modal NAS methods, such as the DC-NAS (Divide-and-Conquer Neural Architecture Search for Multi-Modal Classification) mentioned in the manuscript?

At the methodological level, what is the significance of concatenating pseudo-views with the original views? In principle, it seems that the pseudo-view already contains the information of the original view.

### Soundness
3

### Presentation
3

### Contribution
3
