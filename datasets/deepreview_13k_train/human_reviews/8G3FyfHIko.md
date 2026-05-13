# GDrag:Towards General-Purpose Interactive Editing with Anti-ambiguity Point Diffusion

- Decision: Accept
- Scores: 6, 6, 8, 6, 6

## Abstract
Recent interactive point-based image manipulation methods have gained considerable attention for being user-friendly. However, these methods still face two types of ambiguity issues that can lead to unsatisfactory outcomes, namely, intention ambiguity which misinterprets the purposes of users, and content ambiguity where target image areas are distorted by distracting elements. To address these issues and achieve general-purpose manipulations, we propose a novel task-aware, training-free framework called GDrag. Specifically, GDrag defines a taxonomy of atomic manipulations, which can be parameterized and combined unitedly to represent complex manipulations, thereby reducing intention ambiguity. Furthermore, GDrag introduces two strategies to mitigate content ambiguity, including an anti-ambiguity dense trajectory calculation method (ADT) and a self-adaptive motion supervision method (SMS). Given an atomic manipulation, ADT converts the sparse user-defined handle points into a dense point set by selecting their semantic and geometric neighbors, and calculates the trajectory of the point set. Unlike previous motion supervision methods relying on a single global scale for low-rank adaption, SMS jointly optimizes point-wise adaption scales and latent feature biases. These two methods allow us to model fine-grained target contexts and generate precise trajectories. As a result, GDrag consistently produces precise and appealing results in different editing tasks. Extensive experiments on the challenging DragBench dataset demonstrate that GDrag outperforms state-of-the-art methods significantly. The code of GDrag will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes GDrag, a general-purpose optimization-based framework to tackle diverse interactive point-based image editing tasks. GDrag introduces two strategies, an anti-ambiguity dense trajectory calculation method (ADT) to calculate the trajectories, and a self-adaptive motion supervision method (SMS) to refine latent features. The experiment performance demonstrates the powerful editing capabilities of GDrag.

### Strengths
1.	Originality: The paper addresses the issue of intent ambiguity in dragging-based image editing tasks with an anti-ambiguity dense trajectory calculation method, and specifically constrains movement on dense trajectories, demonstrating good originality overall.
2.	Quality: The paper clearly outlines its innovations, presents a reasonable discussion, provides sufficient experimental results, and demonstrates good quality.
3.	Clarity: The discussion is mostly clear.
4.	Significance: The method proposed in this paper facilitates users in expressing their intentions, enhances interaction, and achieves competitive results, making it of considerable significance.

### Weaknesses
[1] Introduction: The problem statement lacks persuasiveness due to unclear writing. Begin by explaining what "handle points" in drag-based diffusion are. Don’t assume that all readers are already familiar with the task of drag-based diffusion and the terminology used. Without an explanation of handle points, readers may struggle to understand the trajectories derived from them, which ultimately undermines the intent behind the examples illustrating the problem.

[2] Intention Understanding Model: Although the paper is presented as a model for understanding intention, the method proposed seems more focused on effectively executing predefined intentions rather than genuinely understanding them. The system appears to categorize intentions into a limited set of predefined actions, rather than inferring user intent from the drag trajectory itself. This limits the system's ability to handle novel or nuanced user interactions that fall outside of its pre-programmed categories.

[3] Practicality: Since the approach relies on heuristic methods based on categorical intentions, its practical applicability appears limited. The reliance on predefined categories for intention recognition restricts the system's adaptability to diverse user needs and complex scenarios. The system’s performance is likely to degrade when faced with user intentions that do not neatly fit into the existing categories, which are not exhaustive of all possible user intentions.

[4] Computational Analysis: Functionally, placing dense points is likely to lead to significant computational overhead. However, there is a lack of experimental validation, as no computational analysis has been conducted to assess this aspect. The paper does not provide any quantitative data on the computational cost associated with the dense trajectory calculation, making it difficult to assess the feasibility of the approach for real-time applications.

### Questions
1.	The "rotation" in the middle row of Figure 3 is somewhat unclear. Is it intended to rotate the back edge of the bottle to the front? Please provide a clearer explanation here.
2.	The reasoning behind the use of low-rank adaptation in line 324 is somewhat vague. Please provide a more detailed explanation here.

### Soundness
3

### Presentation
3

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
The paper introduces a task-aware, optimization-based framework for general-purpose interactive editing (GDrag).  GDrag categorizes point-based image manipulations into three atomic tasks based on user intents, and convert sparse trajectories into dense trajectories via a carefully designed graphical user interface. Based on the converted dense trajectories, a set of fine-grained optimization parameters are applied for motion supervision. GDrag achieves superior performance on DragBench.

### Strengths
1. GDrag focuses on solving the ambiguity of user intents. The proposed Anti-ambiguity Dense Trajectory (ADT) Estimation, i.e., the graphical user interface is interesting, especially for rotation task.
2. The paper is easy to understand.

### Weaknesses
My primary concern is whether the estimation of dense points and point trajectories proposed in the paper will be affected by the performance of the semantic segmentation model, and whether there might be significant deviations for more complex motions, such as the transition of a hand from an open to a closed position.

### Questions
1. The ablation study in Table 3 shows that the proposed Self-adaptive Motion Supervision (SMS) barely contributes to the performance improvements. It will be better to provide comparison between traditional motion supervision and SMS.
2. Since GDrag uses augmented dense trajectories for motion supervision, the qualitative comparison among other state-of-the-art methods seems a little bit unfair. What do the results of these methods look like using denser trajectories?
3. The computational complexity in line 299 seems not right. The compared methods usually select a fixed timestep and optimize N times, which is much less than O(TL).
4. Is it necessary to use features of the original UNet? Why not use features of UNet w/ LoRA directly?
5. Is there any experiments on the variation of hyper-paramters \rho and \beta?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces GDrag, a novel task-aware, optimization-based framework designed for interactive image editing. This method addresses the limitations of existing point-based diffusion models, particularly the challenges of intention ambiguity and content ambiguity in image editing tasks. Existing point-based methods, such as DragDiffusion and FreeDrag, struggle with accurately modeling diverse editing tasks, often leading to mixed or unclear trajectories (intention ambiguity) and a lack of precise target identification (content ambiguity). Current approaches also face challenges in representing 3D manipulations, relying too much on single denoising time steps.

 To overcome these issues, GDrag introduces three atomic editing tasks—relocation, rotation (both in-plane and out-of-plane), and non-rigid transformations (like scaling or content creation/removal). This task-aware design allows the system to simplify complex manipulations by breaking them into smaller, specific tasks. ADT (Anti-ambiguity Dense Trajectory Estimation): This component improves the precision of 3D edits by selecting the semantic and geometric neighbors of handle points, allowing the creation of dense, contextually informed trajectories rather than simple 2D lines. SMS optimizes latent features by sampling them from various denoising steps, enabling a more detailed control of motion and addressing content ambiguity. Additionally, SMS applies low-rank adaptation techniques, allowing GDrag to preserve target details at multiple granular levels.

### Strengths
## Originality
The paper identifies and addresses key limitations in existing point-based image editing methods, specifically intention ambiguity and content ambiguity, offering a well-defined solution to these issues. 
- By categorizing editing actions into distinct tasks (relocation, rotation, non-rigid transformations), GDrag allows for more targeted and effective edits. This task-oriented approach enables clearer control over image transformations and reduces the complexity of handling diverse editing requirements.
- Innovative Dense Trajectory Estimation (ADT): ADT is a significant advancement in managing trajectory information. It enhances the precision and reliability of editing by creating a dense point set with contextual information, which is especially valuable for complex 3D manipulations
- Self-Adaptive Motion Supervision (SMS): The SMS method introduces a robust way to optimize latent features across multiple denoising steps. This enhances generative models’ performance by allowing finer-grained control and preserving target details at various levels, improving the overall quality of the edits.

## Quality
GDrag is evaluated on DragBench, a benchmark that effectively demonstrates its advantages over existing methods. The results show both quantitative and qualitative improvements in trajectory accuracy and image quality, providing strong empirical evidence for its effectiveness. Compared to other baseline models, GDrag consistently delivers more precise and visually appealing edits, highlighting its promising performance in the interactive image editing.

## Clarity
The overall organization and writing of the paper are well-executed. It clearly articulates the significant limitations of current methods in point-based image manipulation task and presents an effective solution. The logic and details of the proposed method are well thought out, with no apparent flaws.

## Significance
I believe the main work of this paper makes a substantial contribution to the task, particularly in defining the issues of intention and content ambiguity and proposing an effective solution. The overall approach is highly intuitive and, in my opinion, offers valuable insights that could inspire future research in this area.

### Weaknesses
- I personally think that adding more details about the core modules in the ablation study section could make it easier for readers to follow and better grasp the key aspects of these modules.
- In lines 299-302, the authors employ a random optimization step. I suggest that adding a comparison between fixed and variable optimization steps would enhance the persuasiveness of the paper, providing a clearer understanding of the benefits of using a variable approach.

### Questions
- A detailed definition of the Distance metric would be beneficial, particularly in distinguishing it from the Mean Distance metric used in DragDiffusion [1]. Providing a more comprehensive explanation of the Distance metric, including its calculation and interpretation, could help clarify its role in evaluating model performance. Supplementing these details in the Appendix would enhance readability for new readers, offering them a clearer understanding.



[1] DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing. Shi et al.

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
4

### Summary
This paper proposes a system referred to as GDrag to resolve intention based on user given drag. GDrag introduces two strategies to mitigate content ambiguity, including an anti-ambiguity dense trajectory calculation method and a self-adaptive motion supervision method.

### Strengths
[1] Proposed problem (intention-awareness) for drag-based editing is challenging issue.

[2] Proposed method is reasonable

[3] Figure is illustrative

### Weaknesses
[1] Introduction: The problem statement lacks persuasiveness due to unclear writing. Begin by explaining what "handle points" in drag-based diffusion are. Don’t assume that all readers are already familiar with the task of drag-based diffusion and the terminology used. Without an explanation of handle points, readers may struggle to understand the trajectories derived from them, which ultimately undermines the intent behind the examples illustrating the problem.

[2] Intention Understanding Model: Although the paper is presented as a model for understanding intention, the method proposed seems more focused on effectively executing predefined intentions rather than genuinely understanding them.

[3] Practicality: Since the approach relies on heuristic methods based on categorical intentions, its practical applicability appears limited.

[4] Computational Analysis: Functionally, placing dense points is likely to lead to significant computational overhead. However, there is a lack of experimental validation, as no computational analysis has been conducted to assess this aspect.

### Questions
My questions are based on weakness. Please give me a rebuttal on them.
User intention may highly differ from drag, is there any analysis of understanding human intention based on input drag?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The primary goal of this work is to address two issues inherent in current point-based image manipulation: intention ambiguity and content ambiguity. To tackle intention ambiguity, the paper defines a taxonomy of atomic manipulations that can be combined to form complex actions. For content ambiguity, the authors introduce the Anti-Ambiguity Dense Trajectory calculation method (ADT) and a Self-Adaptive Motion Supervision method (SMS). In ADT, each atomic manipulation is defined using a dense point set and corresponding point trajectories from an image segmentation model, allowing for better specification of the motion direction for specific tasks. SMS enhances performance by jointly optimizing point-wise adaptation scales and latent feature biases. The proposed methods demonstrate significant advantages in both quantitative and qualitative comparisons.

### Strengths
1. The writing is clear, engaging, and easy to understand.
2. The objectives of addressing intention ambiguity and content ambiguity are both reasonable and aligned with practical needs.
3. The process of decomposing drag-based manipulation into three atomic manipulations is concise and effective, facilitating future research.
3. The approach of optimizing $z_0$ to replace optimizing $z_t$ demonstrates a degree of novelty.

### Weaknesses
My primary concern is whether the estimation of dense points and point trajectories proposed in the paper will be affected by the performance of the semantic segmentation model, and whether there might be significant deviations for more complex motions, such as the transition of a hand from an open to a closed position.

### Questions
Including a discussion of some failure examples would make the paper more comprehensive.

### Soundness
3

### Presentation
3

### Contribution
3
