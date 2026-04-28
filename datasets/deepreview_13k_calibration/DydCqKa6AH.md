# Learning to Generate Diverse Pedestrian Movements from Web Videos with Noisy Labels

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
Understanding and modeling pedestrian movements in the real world is crucial for applications like motion forecasting and scene simulation. Many factors influence pedestrian movements, such as scene context, individual characteristics, and goals, which are often ignored by the existing human generation methods.
Web videos contain natural pedestrian behavior and rich motion context, but annotating them with pre-trained predictors leads to noisy labels. 
In this work, we propose learning diverse pedestrian movements from web videos. 
We first curate a large-scale dataset called CityWalkers that captures diverse real-world pedestrian movements in urban scenes.
Then, based on CityWalkers,  we propose a generative model called PedGen for diverse pedestrian movement generation. PedGen introduces automatic label filtering to remove the low-quality labels and a mask embedding to train with partial labels. It also contains a novel context encoder that lifts the 2D scene context to 3D and can incorporate various context factors in generating realistic pedestrian movements in urban scenes. 
Experiments show that PedGen outperforms existing baseline methods for pedestrian movement generation by learning from noisy labels and incorporating the context factors. In addition, PedGen achieves zero-shot generalization in both real-world and simulated environments. The code, model, and data will be made publicly available at \url{https://genforce.io/PedGen/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a context-aware generative model for realistic pedestrian movement prediction. It leverages a conditional diffusion framework that uses 3D point clouds to capture spatial scene context. PedGen offers a solution suitable for applications in autonomous systems, crowd simulation, and urban planning.

### Strengths
Context is an important factor in pedestrian trajectory prediction, which poses a challenge due to the difficulty of identifying and measuring it while predicting future paths. This paper proposes a valuable idea, supported by clear visualizations and thorough ablation studies.

### Weaknesses
1- I find Fig. 3 confusing. Based on the context of the paper, it appears that only one timestep is observed, and the rest are predicted. However, Fig. 3 suggests that the model is fed with the timesteps from t=1 to t=T.

2- The learnable mask *m* needs to be explained more in the paper. How is this mask learned?

### Questions
1- Since pedestrian path generation is done in static settings, the social attributes of pedestrians are not taken into account. Are other pedestrians considered as objects when calculating the collision measure? 

2- How is the collision rate  affected by the ablations?

3- The training of masks *m* in Fig. 3 is unclear. How are these masks trained, and which part of the loss function guides this training?

3- Looking at Table 3.b, it appears that the goal has a significant effect on error reduction. However, in practice, the goal of a pedestrian is generally unknown when predicting the path. Why is the goal handled as context in this work? Shouldn’t the model predict the goal as part of the path prediction process? I am also curious to see visualizations with an ablated version where the goal is not provided as input.

4- mADE is mentioned to be measured across 50 movements. Does this mean that 50 possible paths were generated?

### Soundness
2

### Presentation
2

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
The authors propose a method for learning pedestrian movements from web videos by using pre-trained predictors to generate pseudo-labels through off-the-shelf 4D human motion estimation models, despite the inherent noise in the labels. To refine these noisy labels, they introduce the PedGen model, which filters out noise and incorporates conditional inputs that may influence pedestrian behavior, thereby lifting the 2D scene into a 3D representation. The authors intend to provide open access to both the dataset and the model.

### Strengths
1. This paper focuses on using noisy labels to learn pedestrian motion, a novel approach with the potential to benefit various research areas.
2. The authors contribute a dataset accompanied by a label generation and filtering strategy, addressing the challenge of noise in automated labeling pipelines.
3. The results demonstrate performance improvements over baselines, and comprehensive ablation studies are conducted to validate the approach.

### Weaknesses
1. Although the automated labeling and filtering pipeline is essential, it is a fairly common approach, limiting the novelty of this contribution.
2. The baselines used in the comparison experiments appear weak, with only three included, potentially limiting the robustness of the results.
3. While using the goal as a conditioning factor is crucial and enhances pedestrian movement prediction, some conditions are often not visible or are difficult to capture in practical applications, such as autonomous driving. This raises concerns about the real-world applicability of the proposed setting and whether alternative solutions might address this limitation.

### Questions
1. How does the proposed method handle scenarios where conditional inputs are unavailable or unreliable, as might be the case in applications like autonomous driving?
2. Could the authors elaborate on why only three baselines were chosen for comparison, and whether additional baselines might provide a more comprehensive evaluation?
3. Could you clarify the specific novel aspects of the automated labeling and filtering pipeline? Additionally, is there potential for further innovation in this pipeline to enhance its originality, or were there particular design constraints that influenced its current implementation?

I am open to reconsidering my final rating if the authors address the concerns raised.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors propose to learn pedestrian movements from web videos. To this end, they curate a large-scale dataset called CityWalkers that captures real-world pedestrian movements in urban scenes from YouTube, with some extra efforts to generate pseudo-GT labels and remove the low-quality labels. Given this dataset, the authors propose a generative model where a context encoder is introduced to incorporate various context factors, including goal, human, and scene, in generating realistic pedestrian movements in urban scenes. 

Experiments show that the proposed outperforms existing baseline methods for pedestrian movement generation by learning extra data and incorporating the context factors.

### Strengths
1. The concept of integrating contextual information into pedestrian generation is sound and has already demonstrated effectiveness in related trajectory generation tasks.
2. The ablation studies examining each factor are thorough and well-executed.
3. The visual examples provided in both the main paper and supplementary materials are satisfactory.

### Weaknesses
1. Unclear Task Definition: Section 4.1 outlines the overall task definition, but it seems that only the 3D location of pedestrians and the 2D image of the scene in the first frame (t_1) are provided, while all other elements are predicted. Is this interpretation correct? If so, what is actually learned from this setup, considering there could be millions of plausible results? Or do we learn the bias in the training set? Is this a reasonable setup? The paper does not adequately address the inherent ambiguity in predicting full motion sequences from a single initial frame and location. The potential for overfitting to the training data's biases is a significant concern, especially given the generative nature of the model. The lack of constraints on the predicted motion could lead to unrealistic or physically implausible movements, which are not sufficiently discussed.

2. Clarification of Contributions: The overall contributions should be clarified. Lines 97-101 describe the contributions in a confusing manner. For instance, line 98 states, “1) A new task of context-aware pedestrian movement generation from web videos with unique challenges in dealing with label noise and modeling various motion contexts.” This seems contradictory since the dataset with noisy labels is presented as a contribution in “A new large-scale real-world pedestrian movement dataset, CityWalkers, with pseudo-labels of diverse pedestrian movements and motion contexts” (l. 99). I have significant doubts about the dataset's quality and question whether a noisy dataset can genuinely be considered a contribution. The paper needs to better articulate how the noisy labels are handled and why this dataset, despite its noise, is a valuable contribution. The claim that the dataset captures diverse movements is not sufficiently supported by quantitative analysis of the dataset's diversity.

3. Need for More Explanations About Results: Based on Table 2(b), incorporating scene information yields only minor improvements. The priority order appears to be Goal, Human, and Scene, which raises questions about the usefulness and necessity of including Scene in the overall model. The authors should provide an explanation for this observation. The marginal improvement from scene context raises concerns about the complexity added to the model. It is unclear if the computational cost of incorporating scene information is justified by the limited performance gains. A more detailed analysis of the specific scenarios where scene context is most beneficial is needed.

4. Visual Results for Complex Scenes: More visual examples are needed to illustrate how pedestrians navigate around obstacles, such as chairs, trees, or cars, to reach their targets. Without these examples, the scene context seems to have limited utility, as indicated by the table. The current visual examples do not demonstrate the model's ability to handle complex interactions with the environment. The lack of clear examples of obstacle avoidance and navigation in cluttered scenes makes it difficult to assess the true impact of the scene context on the generated movements.

### Questions
Please address my concerns in weakness as well as in below.

1. Given that the ground truth (GT) is primarily generated using existing methods, how do the authors ensure consistency across these various methods? For example, is the generated depth map aligned with the generated 4D human pose? If there is a discrepancy, what potential drawbacks arise from this mismatch, and how can the proposed method address them?
2. How do the authors convert the depth labels into a 3D point cloud without knowing the camera parameters (l.310)? Am I missing any assumptions here?
3. It appears that only static objects and elements are considered in the scene context, as there is no explicit modeling of dynamics in the context encoder. Do the authors intentionally exclude dynamics during scene context modeling, or are these dynamics treated as static objects? Is it valid to assume that other road participants, such as pedestrians, are not significant in the modeling process for pedestrian motion generation? I find this assumption questionable, especially since collisions are used as evaluation metrics in this study.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies a new task of generating context-aware pedestrian movements by learning from web videos with noisy labels. Different from previous human motion generation task that focuses on in-door human motion generation, the proposed method can generate outdoor human movements conditioned on scene information and person identity information. To achieve this goal, this paper also introduces a new dataset named as CityWalker, which contains outdoor urban pedestrian movements from web videos. Experiments on several benchmarks demonstrate the effectiveness of the proposed method.

### Strengths
1. The contribution of this paper is comprehensive because it contains both dataset and method, which can provide reference for future research in this area.
2. The focus of this paper is interesting, generating human motion in outdoor environment is not well-studied by previous work and this paper present a solution to this task, which may be useful for autonomous driving and related field.
3. This paper is well-written and easy to understand.

### Weaknesses
Although this paper clarifies their task as motion generation, the proposed method and evaluation metrics are more like motion prediction, i.e., output person movements by accepting current condition inputs. The evaluation metrics also does not involve the diversity evaluation of the generated human motion. Therefore I have doubts about the task type of this paper, maybe motion prediction is more accurate.

### Questions
In weakness.

### Soundness
4

### Presentation
4

### Contribution
3
