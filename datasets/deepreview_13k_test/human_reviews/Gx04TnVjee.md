# 3DTrajMaster: Mastering 3D Trajectory for Multi-Entity Motion in Video Generation

- Decision: Accept
- Scores: 6, 5, 8, 8

## Abstract
This paper aims to manipulate multi-entity 3D motions in video generation. Previous methods on controllable video generation primarily leverage 2D control signals to manipulate object motions and have achieved remarkable synthesis results. However, 2D control signals are inherently limited in expressing the 3D nature of object motions. To overcome this problem, we introduce \textbf{3DTrajMaster}, a robust controller that regulates multi-entity dynamics in \textit{3D space}, given user-desired 6DoF pose (location and rotation) sequences of entities. At the core of our approach is a plug-and-play 3D-motion grounded object injector that fuses multiple input entities with their respective 3D trajectories through a gated self-attention mechanism. In addition, we exploit an injector architecture to preserve the video diffusion prior, which is crucial for generalization ability.
To mitigate video quality degradation, we introduce a domain adaptor during training and employ an annealed sampling strategy during inference. To address the lack of suitable training data, we construct a 360$^{\circ}$-Motion Dataset, which first correlates collected 3D human and animal assets with GPT-generated trajectory and then captures their motion with 12 evenly-surround cameras on diverse 3D UE platforms. Extensive experiments show that 3DTrajMaster sets a new state-of-the-art in both accuracy and generalization for controlling multi-entity 3D motions. Project page: \url{http://fuxiao0719.io/projects/3dtrajmaster}.

\nnfootnote{$\dagger$: Work done during an internship at KwaiVGI, Kuaishou Technology. \textsuperscript{\Letter}: Corresponding Authors.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a 3D-trajectory-conditioned video generation method, fusing prior from pre-trained video diffusion models and from a proposed motion dataset.

### Strengths
The paper addresses the lack of 6-DoF controllability of existing video generation methods. The method is well-motivated and method designs are clearly explained. The advantage of 6-DoF control over 2D motion control is clearly demonstrated in experiments.

### Weaknesses
* The section on related works discusses prior methods on motion control and motion synthesis tasks, but could also include discussions on techniques for injecting controls to video foundation models, including ControlNet [1] and methods that allow 2D image editing by manipulation attention maps. In particular, ControlNet [1] is currently mentioned but not cited in the paper. 
* The proposed dataset is restricted to human and animal categories, and locations remain to be in cities. Whether it's feasible to scale this method to generic object categories and generic scenes remains an open question.  

[1] Lvmin Zhang, Anyi Rao, Maneesh Agrawala. Adding Conditional Control to Text-to-Image Diffusion Models.

### Questions
* Evaluation of multi-entity input sequence sets $N=2$, i.e., 2 entities, based on the qualitative examples. Is the method restricted to a small number of entities, and if so, does the restriction come from training data? If it's tied to training data distribution, it remains even more unclear if the method can potentially apply to generic settings where >>2 objects are moving, which is fairly common in dynamic scenes.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
3DTrajMaster" introduces a method for controlling multi-entity 3D motion in video generation using 6DoF pose sequences. The authors propose a novel plug-and-play 3D-motion grounded object injector that fuses entity descriptions with corresponding 3D trajectories using a gated self-attention mechanism. They address the lack of suitable training data by constructing a 360°-Motion Dataset, combining collected 3D assets with GPT-generated trajectories. The method is tested against prior 2D motion control approaches and shows state-of-the-art performance in both motion control accuracy and generalization.

### Strengths
The proposed 3D-motion grounded object injector, combining 6DoF pose sequences with entity descriptions, is an innovative contribution that extends beyond 2D control limitations.

**Dataset Creation**: The construction of the 360°-Motion Dataset addresses a notable gap in available training data, particularly for multi-entity scenarios, using an innovative combination of GPT and UE.

**Flexibility**: The plug-and-play nature of the proposed object injector facilitates broader applicability across different generative models, with the gated self-attention mechanism ensuring entity-specific trajectory adherence.

### Weaknesses
**Dataset Limitation**: The reliance on synthetic data and a limited number of assets may hinder real-world generalization. The "city" setting constraint for the dataset also limits the diversity of possible outputs.

**Generalizability**: The model's performance for generalized 3D scenes beyond those captured in the MatrixCity platform remains unclear. More evaluation of real-world, diverse datasets would strengthen the contributions.

**Evaluation Scope**: While evaluation metrics like FVD and CLIP Similarity are used, the lack of real-world evaluations or qualitative feedback from human users makes it hard to gauge practical effectiveness fully. Also, the author could consider comparing with recent 4D generation methods such as TC4D which also can control trajectory.

I will also check other reviewers's feedback.

### Questions
Will the dataset and code will be public after acceptance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
1. This paper aims to control the entities’ motion with 3D control signals in video generation.  3D control signals are a more natural representation compared to 2D signals as the motion is in 3D space. 
2. This paper proposed a plug-and-play module to integrate the entities with their respective 3D trajectories into a pre-trained video generative model to control the 3D motion. 
3. To avoid video quality degradation during the fine-tuning, they use a Lora-like domain adaptor and an annealed sampling strategy.
4. They construct a synthetic dataset collecting dynamic 3D human and animal assets with ground-truth 3D motion for training.
5. Experiments show that the proposed methods can achieve state-of-the-art performance in 3D motion control.

### Strengths
1. The proposed method is the first to control entities’ motion with 3D trajectories in video generation. The task is novel and reasonable as 3D control signals can fully express the inherent 3D nature of motion and offer better controllability in video generation compared to 2D control signals.
2. The method design is clear and reasonable.
3. The paper constructs a new synthetic dataset for this task. The dataset potentially benefits the following video generation with 3D entity control. 
4. The experiments are thorough and solid. Plenty of visualization results as well as the videos in the supplementary demonstrate the effectiveness and generability of the proposed method.
5. The paper is well-written and easy to follow.

### Weaknesses
1. The dataset lacks diversity in terms of background and motion types. The setting is restricted to a "City" environment (as noted in the paper's Limitations section), and the actions are primarily limited to walking. Consequently, models trained on this dataset are also constrained in their generalizability.
2. Foot skating/floating issues are prevalent in the dataset. This appears to result from inconsistencies between the relative motion and global motion of the dynamic entities, which could negatively impact model training by introducing artifacts.

Minor:

1. The explanation of the "ControlNet-like architecture" is vague and lacks clarity. The paper references this term in Lines 20 and 115, suggesting it pertains to the Object Injector, whose initial weights stem from the 2D spatial self-attention layer in the video generative model. However, this does not align with a true ControlNet-like module, which would typically function as a parallel module with zero-initialized layers designed to adjust the original features. Instead, the Object Injector is positioned after the 2D spatial self-attention layer, differing fundamentally from ControlNet-like behavior.
2. It would have been better to elaborate on Line 334: “This phenomenon reflects the model’s ability to learn 3D motion representations”? The reasoning behind this statement isn’t entirely clear.

### Questions
In Table 2, could you clarify the distinction between “Multiple Entities” and “All Entities”? Does “All Entities” include both “single” and “multiple” cases?

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
2

### Summary
Paper tackles the problem of multi-entity 3D control signals for video generation

Approach works by constructing an Unreal Engine dataset of assets with GPT4V generated trajectories and various camera angles, and then LoRAing it to do domain adaptation to prevent it from looking too much like the UE assets.

Extensive qualitative results indicate the method clearly works, and quantitative results indicate value of components + favorable results compared to several baselines.

### Strengths
The method clearly works. The supplemental provides extensive videos paired with prompts showcasing multiple walking agents. While generations are imperfect, I was shocked at the quality -- the assets seem to properly interact with light in the scenes, including full long shadows, as well as the terrain below, such as water. 

The method used to achieve this adaptation seems straightfoward, and the recipe seems generally replicable and applicable to other video generation models despite the fact that the generation model used is proprietary.

### Weaknesses
- Pose evals are human only; however, I think this is well motivated given the stated lack of general video pose predictors.

Quite honestly, I am not an expert in this domain and I lack the background to provide meaningful criticism. The results look good, the actors clearly follow the given trajectories, and the recipe given to achieve this generally makes sense and feels general enough to be useful for arbitrary video generation models.

### Questions
- Why does the alligator gait look so much worse than the other animals? Its legs seem to be almost static in some scenes.
 - It seems that the proprietary base video generation model is extremely strong (congrats!). Do you think this recipe will work with less strong video generation models, such as current open source models?

### Soundness
3

### Presentation
3

### Contribution
3
