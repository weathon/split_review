# DiffVAS: Diffusion-Guided Visual Active Search in Partially Observable Environments

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Visual active search (VAS) has been introduced as a modeling framework that leverages visual cues to direct aerial (e.g., UAV-based) exploration and pinpoint areas of interest within extensive geospatial regions. Potential applications of VAS include detecting hotspots for rare wildlife poaching, aiding in search-and-rescue missions, and uncovering illegal trafficking of weapons, among other uses. Previous VAS approaches assume that the entire search space is known upfront, which is often unrealistic due to constraints such as a restricted field of view and high acquisition costs, and they typically learn policies tailored to specific target objects, which limits their ability to search for multiple target categories simultaneously. In this work, we propose DiffVAS, a target-conditioned policy that searches for diverse objects simultaneously according to task requirements in partially observable environments, which advances the deployment of visual active search policies in real-world applications. DiffVAS uses a diffusion model to reconstruct the entire geospatial area from sequentially observed partial glimpses, which enables a target-conditioned reinforcement learning-based planning module to effectively reason and guide subsequent search steps. Our extensive experiments demonstrate that DiffVAS excels in searching diverse objects in partially observable environments, significantly surpassing state-of-the-art methods across datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on the visual active search (VAS) problem. Current work usually assumes that the global search space is known, which is not consistent with practical VAS applications. Accordingly, the authors formulate the target-conditioned Visual Active Search in Partially Observable environments problem, which points out that the agent needs to explore the environment step by step while searching for the Target of the specified category.

Based on the above problems, this paper proposes to use the diffusion model to generate a panoramic search space map based on the existing observations, and construct a target-conditioned planning module to select the appropriate region according to the generated image. This paper trains and tests on DOTA and other datasets, and compares with other methods. The results show that the proposed method can achieve good results in single-class/multi-class/zero-shot settings.

### Strengths
This paper has the following strengths:
1. Good originality. This paper starts from a very practical problem, that is, in the real environment, the UAV cannot know all the information of the search environment map in advance, so it can only make decisions within the existing knowledge. This is a good motivation for the question. Therefore, the article has good originality.
2. Simple and logically sound method. In view of the incompletely explored characteristics, this paper proposes CGM model, which uses diffusion model to generate complete scene information. Then, the target exploration strategy is trained, and the exploration effect and the scene information construction result are used as the reward function. This is a simple yet effective approach in active exploration.
3. Good clarity. This paper elaborates and analyzes the problem of self-definition in detail. And a large number of quantitative methods are used to describe the various details of the method, such as how to construct the reward function, the details of the loss function and so on. At the same time, the overall expression logic of the paper is relatively clear, and a large number of experiments prove the effectiveness of the method.

### Weaknesses
This paper has the following weaknesses:
1. Problem setting to be optimized.  This paper points out that the action space is a patch that can reach any patch in the search area. After executing the action, the visual information of the patch will be added to the prior knowledge of the UAV. However, in fact, the UAV can also obtain the visual information of the path position during the movement. Taking Figure 1 in the article as an example, from grid1 to grid5, the UAV should be able to obtain the visual information of grid2-4 at the same time, not only the visual information of grid5. Therefore, based on the actual scene and the rationality of the action space, the problem setting in this paper needs to be further optimized. The current action space formulation allows the agent to teleport to any location, which is unrealistic for a physical UAV. This oversimplification could lead to policies that exploit this unrealistic capability and may not generalize well to real-world scenarios where continuous movement and path planning are necessary. The lack of consideration for the information gained during movement along a path also limits the practical applicability of the proposed method.
2. Details on training and testing are missing: For a series of experiments in this paper, the details of how the method is trained need to be further described. The lack of such descriptive information may prevent subsequent related work from being further developed above. Specifically, the paper lacks details on the specific optimization algorithms, learning rates, batch sizes, and the number of training epochs used. This level of detail is critical for reproducibility and for other researchers to build upon this work. Furthermore, the paper does not clearly describe how the diffusion model is trained and integrated with the target-conditioned planning module.
3. The motivation of the experimental setup needs further clarification.  The paper sets up single-class, multi-class and zero-shot experiments. However, the multiple-target category only gives results for three combinations, and zero-shot generalization cannot determine whether the category is the one that has appeared in the training phase. The experimental Settings need to be further supplemented. The choice of only three combinations for the multi-class experiments is not well-justified, and it is unclear if these combinations are representative of the overall performance. The zero-shot experiments also lack clarity, as it is not explicitly stated whether the zero-shot categories are completely disjoint from the training categories, or if there is any overlap. This makes it difficult to assess the true generalization capability of the proposed method.

### Questions
1. As far as I know, the methods you compare in this article, such as E2EVAS and MPS-VAS, are exploratory work with prior information about the scene. Please give the details of how to infer the above method under your problem setting, that is, without the full information of the scene.
2. Please provide motivation for the experimental setup, especially the class setup on multi-class experiments and zero-shot experiments.
3. Please provide more details about the training. In particular, how you've done policy training on datasets like DOTA. How do you sample episodes during training.

### Soundness
2

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
3

### Summary
Visual Active Search (VAS) is a framework for directing aerial exploration to pinpoint areas of interest using visual cues. Traditional VAS methods assume full knowledge of the search space and are tailored to specific target objects, limiting their practicality and versatility. This work introduces DiffVAS, a target-conditioned policy that searches for multiple object categories simultaneously in partially observable environments. DiffVAS uses a diffusion model to reconstruct the entire geospatial area from partial observations, allowing a reinforcement learning-based planning module to guide the search effectively.

### Strengths
+ Towards real-world situations, this work attempt to make decisions with incomplete information, the idea is  interesting and  practical. 
+Experimental results are sufficient.

### Weaknesses
My main concern about this article lies in the mismatch between the motivation and experimental validation. The author emphasizes that the research is motivated by the challenge of obtaining complete information in the more realistic world. This phenomenon is indeed widespread, and the method based on diffusion models is also suitable for reconstructing more complete information from incomplete information, with a technically sound framework. However, my main concerns are those the current experimental data and environmental settings may not adequately simulate the incomplete data situations in real-world scenarios, and there is even a relatively large gap, which makes it difficult to directly apply the model trained in this article to real-world environments.

If the model cannot be directly applied to the real world, then the novelty of the technical framework itself seems not that strong. The idea of reconstructing the whole from parts has already been explored in many published works. The approach overlaps significantly with DiffMAE(ICCV23), which combines MAE with diffusion models for image reconstruction. The contribution seems incremental without clear novelty. The method closely resembles MDT(ICCV23), which uses unmasked tokens to predict masked ones while preserving diffusion training.

### Questions
My first question is about the practicality in the real world, if the author can convince me that this work can be applied in the real world, then I won't have any further questions.
Otherwise, I think that the current technical framework itself lacks sufficient novelty. I know we can find detailed differences between papers, but hope the author could clarify the core technological novelty of this paper.

### Soundness
2

### Presentation
2

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
The paper presents DiffVAS, a framework for visual active search in partially observable environments. It introduces a new task setup, TC-POVAS, and uses a Conditional Generative Module (CGM) and a Target-Conditioned Planning Module (TCPM) to balance exploration and exploitation. DiffVAS achieves superior performance in multi-target search tasks through extensive experiments. However, there are some issues like an incomplete ablation study on reward functions, writing inconsistencies, and formatting errors in figures and tables.

### Strengths
1. The introduction of a Target-Conditioned Partially Observable Environment (TC-POVAS) enables multi-target visual active search to operate in partially observable environments, making it more aligned with real-world scenarios.
2. By utilizing a Conditional Generative Module (CGM) based on a diffusion model, DiffVAS can reconstruct the entire search space from partial observations, providing more accurate guidance for subsequent search decisions.
3. The introduction of the Target-Conditioned Planning Module (TCPM) uses a reinforcement learning strategy to balance exploration and exploitation, optimizing search performance in partially observable environments.
4. Through extensive experiments on multiple public satellite imagery datasets such as xView and DOTA, DiffVAS demonstrated superior performance in multi-target search tasks, achieving significant improvements over existing methods.

### Weaknesses
1. The paper’s ablation study on the reward function lacks the combination of $R^{AS} + R^{LU}$, which could provide deeper insights into the impact of these components on model performance. Specifically, it is unclear how the local uncertainty reward ($R^{LU}$) interacts with the active search reward ($R^{AS}$) and whether their combination would lead to synergistic improvements or if one dominates the other. This omission limits the understanding of the individual contributions of each reward term.
2. There are writing issues such as inconsistent capitalization of symbols like "Sgn" in the formulas (6) and (7). This inconsistency, while seemingly minor, can affect the readability and perceived rigor of the paper, potentially causing confusion for readers trying to understand the mathematical formulations.
3. Figure 3 has issues related to font, capitalization, and symbol representation. The lack of consistency in visual elements, such as font sizes and capitalization, along with a missing parenthesis in "Past Query Outcomes," detracts from the figure's clarity and professionalism. These issues make it harder for the reader to quickly grasp the information being conveyed.
4. In the "Zero-shot Generalization" section, there is a misexpression where it states "solely on DOTA on xView". This phrasing is ambiguous and could be interpreted as the model being trained on DOTA and tested on xView, which is not the intended meaning, thereby creating confusion about the experimental setup.

### Questions
1. Why was the combination of $R^{AS} + R^{LU}$ omitted in the reward function ablation study?
2. Is the presence of issues in writing and formatting, such as text descriptions and figure/table formats, an indication that the paper was prepared somewhat hastily?

### Soundness
3

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
4

### Summary
This paper introduces DiffVAS, a Visual Active Search (VAS) framework designed to handle multi-target search tasks in partially observable environments. The authors fine-tune a diffusion-based Conditional Generative Module (CGM) to reconstruct the full scene from partial observations then train a target-conditioned planning module (TCPM) using reinforcement learning with an exploration-exploition reward system to guide search policies based on target categories

### Strengths
1. The integration of a diffusion model for scene reconstruction within a VAS framework is novel and enables DiffVAS to work effectively with partial observations, a realistic approach for UAV-based geospatial searches.
2. DiffVAS shows good performance on both single- and multi-target tasks.

### Weaknesses
1. The diffusion model, while powerful, adds computational complexity. Real-time search and UAV deployment may be challenging
2. While cross-attention is introduced in DiffVAS framework, its specific contribution to performance is only briefly mentioned.  A deeper analysis might clarify its role further.
3. The evaluation relies primarily on the "Average Number of Targets" (ANT) metric, which, while informative, does not capture all aspects of performance, especially in practical scenarios. Metrics reflecting search efficiency (e.g., path length or cost-effectiveness) could provide a more holistic assessment
4. The paper simplifies the search task significantly by assuming a fixed UAV altitude and discretizing the action space into a grid structure. This abstraction does not capture the full complexity of real-world search tasks, where UAVs may need to operate at varying altitudes and adjust scale dynamically. The authors could explore multi-scale Active Visual Search (AVS) environments to better simulate realistic search scenarios.
5. By focusing solely on the exploration-exploitation balance through reinforcement learning, the framework oversimplifies the role of object detection. In practical applications, detection often involves noise, occlusions, and variable scene complexities, which are currently unaddressed. Future work could explore more challenging detection settings to evaluate DiffVAS’s resilience under realistic conditions.

### Questions
1. DiffVAS leverages a diffusion model to reconstruct the scene from partial observations, which could introduce significant computational overhead, especially in real-time or resource-constrained scenarios. Could the authors clarify the approximate time required for the diffusion model to reconstruct a single full observation image?
2. Can the authors provide further explanation and ablation studies or visualizations about the cross-attention layer in Figure 3?  What's the reference features and the target features? What's the AdaIN?
3. To better assess the contribution of the Conditional Generative Module (CGM), would it be feasible to input the ground truth full observation directly to the Target-Conditioned Planning Module (TCPM) to establish an upper bound on TCPM’s performance? This experiment could reveal TCPM's ideal capabilities and help quantify the effectiveness of CGM in assisting TCPM under varying levels of partial observations.

### Soundness
2

### Presentation
3

### Contribution
2
