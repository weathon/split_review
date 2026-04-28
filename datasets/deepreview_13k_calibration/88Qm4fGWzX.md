# Event-Customized Image Generation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
Customized Image Generation, generating customized images with user-specified concepts, has raised significant attention due to its creativity and novelty. With impressive progress achieved in \emph{subject} customization, some pioneer works further explored the customization of \emph{action} and \emph{interaction} beyond entity (\ie, human, animal, and object) appearance. However, these approaches only focus on basic actions and interactions between two entities, and their effects are limited by insufficient ``exactly same'' reference images. To extend customized image generation to more complex scenes for general real-world applications, we propose a new task: \textbf{event-customized image generation}. Given a single reference image, we define the ``event” as all specific actions, poses, relations, or interactions between different entities in the scene. This task aims at accurately capturing the complex event and generating customized images with various target entities. To solve this task, we proposed a novel training-free event customization method: \textbf{FreeEvent}. Specifically, FreeEvent introduces two extra paths alongside the general diffusion denoising process: 1) Entity switching path: it applies cross-attention guidance and regulation for target entity generation. 2) Event transferring path: it injects the spatial feature and self-attention maps from the reference image to the target image for event generation. To further facilitate this new task, we collected two evaluation benchmarks: SWiG-Event and Real-Event. Extensive experiments and ablations have demonstrated the effectiveness of FreeEvent.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new task called Event-Customized Image Generation, which aims to not only control subjects, but also customize all specific actions, poses, relations, or interactions between different entities in the scene. Then it designs a training-free approach, by alternating the cross-attention within U-Net to eanble target subject generation, and utilizing origin spatial feature and self-attention to enale entity transfer. Experiments on two data-sets validated the effectiveness.

### Strengths
- The proposed training-free approach is easy to adopt and can generate satisfying results.
- The paper is clear and easy to follow.

### Weaknesses
1. The task setting of event-customized image generation raises following concerns: The poses of each entity, as well as the overall spatial configuration of generated image is restricted to maintain identical with reference image, which hinders the diversity of generated images. Further, even if the poses are successfully maintained, the interaction semantic may be influenced. In the example of “skeleton, statue” in Figure(1), when the laptop is changed to a book, the interaction semantic between human and object is changed. Is it against the proposed definition of task setting? Further, can this approach be integrated with other components to enable generation on specific backgroud image? 
2. For Method design : (1) the spatial features and self-attention maps of reference images are adopted to inject event information, how to ensure such direct injection can prevent the leakage of subject information of reference image. (2) The auther claims that by equipping with subject-customized image generation approaches, it can generate entity-subject customized images by injecting target concept identifier tokens, can this approach be integrated with more advanced customization approaches to enable more flexible customization of regular concepts rather than just some celebrities visualized in Figure 6. 
3. In Experiment, (1) The task setting for quantitative evaluation is confusing. How to reproduce the reference image if all the entities within the image stay the same pose as input condition. Providing one visualized example would be helpful to understand it. (2) Quantitative evaluation only adopts a retrieval-based experiment, which is not convicing enough, and the user study for qualitative evaluation only adopts 30 samples. (3) Further, the interaction semantic of generated image is not verified across all the experiments. Considering that HICO-DET and SWIG both contains annotations of interaction, the generated images should also evaluate  corresponding interaction detection performance.

### Questions
1. Can the author list some specific applications in reality of the new-proposed task setting to convince me of its value?
In some cases, the interaction semantic and poses perservation requirement is conflicted, as mentioned in weaknesses. Can the author explain the priority of such requirements?
2, Can the proposed approach enable more flexible content generation, like specify the background image? Can the entity-subject customization ability be expand to more diverse subject customization other than only some celebrities?
3. Can the evaluation setting of retrieval-based experiment be more clearly explained with some visualized examples?
4. The author should provide more experiments to validate the effectiveness of approach, like report the performance on interaction detection task.

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
4

### Summary
This paper proposed a new task of extending the customized image generation to more complex scenes for general real-world applications.  The event incorporates specific actions, poses, relations and interactions between different entities in the scene. Free-event the method is proposed to solve the task by adding two extra paths along the diffusion denoising process, entity switching path, and event transferring paths. In addition, for evaluation, the paper proposed two more benchmarks.

### Strengths
-	The method seems correct
-	The writing and organization seem clear
-	The efforts to formalize a new benchmark and task, although from existing datasets

### Weaknesses
 - The major issue to argue in this paper is the usage of existing technical contributions for this new task. No theoretical justifications and no further big novel ideas. Whether the technical contributions are limited is worth discussion. The experimental results proved the evaluations. The new task and datasets are also worth reporting.

### Questions
see weakkness

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
4

### Summary
This paper introduces a new task, event-customized image generation, which aims at accurately capturing the complex task and generate customized images with various target entities. Meanwhile, a training-free event customization method, FreeEvent is proposed to solve the event-customized image generation task. The FreeEvent consists of two paths along side the general diffusion denoising process, i.e., the entity switching path and the event transferring path. The entity switching path applies cross-attention guidance and regulation for target entity generation while the event transferring path injects the spatial feature and self-attention maps from the reference image to the target image for event generation.

### Strengths
1. Clear limitation analysis of existing works, i.e., simplified customization and insufficient data.
2. Good motivations for addressing the proposed task.

### Weaknesses
1. Unclear Definition of "Event-Customized Image Generation": The paper’s definition of "event-customized image generation" lacks clarity, especially regarding the complexity and scope of events. Although the paper explains entity interactions, it does not address attributes adequately. Additionally, there is no quantitative measure for defining the complexity level that qualifies as an event, leaving ambiguity in how "event" is operationalized.

2. Lack of Comparison with Related Work: The training-free framework and emphasis on entity and attribute handling appear to align closely with prior work, specifically the ImageAnything framework [A]. The paper fails to compare itself with ImageAnything in terms of motivation, methodology, and structural framework, missing an opportunity to clarify its novelty and improvements over similar approaches.

3. Limited Information on Similarity Metrics: The similarity metric used for assessments in Table 1 is not specified, leaving readers uncertain about the criteria for evaluation. Without this information, the results may be hard to interpret, limiting the reproducibility and transparency of the evaluation.

4. Insufficient Performance Metrics: The paper could enhance its assessment by including standard image generation metrics, such as FID (Fréchet Inception Distance) and CLIP scores, for a more comprehensive comparison. Relying on a limited set of metrics may not provide a well-rounded evaluation, which could affect the perceived robustness of the proposed method.

### Questions
1. The definition of the "event-customized image generation" is somehow not clear. "Given a single reference image, we define the event as all actions and poses of each single entity, and their relations and interaction between different entities." The entity part is fully addressed, however, how about the attribute part? Is there any quantitative definition for how complex can leads to an event?
2. The training free framework and the focus on entity and attribute is somehow similar to a prior work, Imageanything[A]. Please give clear discussion and comparison with this work regarding motivation, methodology, and frameworks.
[A] Lyu Y, Zheng X, Wang L. Image anything: Towards reasoning-coherent and training-free multi-modal image generation[J]. arXiv preprint arXiv:2401.17664, 2024.
3. What kind of similarity metric is used to assess the methods in Tab.1?
4. Could the author include more metrics to assess the proposed FreeEvent and the existing methods, such as FID, CLIP score?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents FreeEvent, a novel approach to customized image generation, targeting complex event-specific scenes rather than just entity appearances or basic interactions. FreeEvent tackles event-customized image generation, where an "event" includes detailed actions, poses, and relationships between entities. FreeEvent introduces two innovative pathways: the Entity Switching Path for entity-specific guidance and the Event Transferring Path for spatial feature and attention transfer.

### Strengths
- Clarity and Readability: The writing quality of the manuscript is commendable, making the intent and message of the paper easy to comprehend.
- Resource-Efficient Methodology: The proposed method is training-free, which is notably advantageous in terms of computational resource requirements, making it accessible and feasible even in resource-constrained environments.

### Weaknesses
 - Overclaim: The manuscript introduces the 'event-customized image generation task' as a novel contribution. However, this task appears to have been previously addressed in the work titled "Learning Disentangled Identifiers for Action-Customized Text-to-Image Generation" presented at CVPR 2024.
- Lack of Methodological Novelty: The two pathways proposed in the paper appear to primarily combine existing methods. The Entity Switching Path employs a strategy similar to Attend-and-Excite for controlling content generation in specific locations, while the Event Transferring Path largely follows approaches resembling MasaCtrl. These methods are widely established and have been extensively discussed across numerous publications, which may limit the perceived innovation in the paper’s methodology. Specifically, the application of cross-attention for entity control and the use of diffusion features for style transfer are not novel contributions in themselves. The paper lacks a detailed analysis of how these existing techniques are adapted or improved for the specific task of event-customized generation.
- Suboptimal Qualitative Results: The qualitative results presented show room for improvement. Specifically, I noticed that the retention of person identifiers is weak in Figures 1c and 6, which raises questions about the underlying cause; the authors should clarify this aspect further. The generated images often exhibit inconsistencies in the appearance of the target entities, suggesting that the method struggles to maintain identity across different events. Additionally, the prompt “P: skeleton, statue, monkey, book” appears four times throughout the paper. Reducing the repetition of this sample would likely enhance the diversity and impact of the results shown.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
1
