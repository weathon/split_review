# Video Generation with Learned Action Prior

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Stochastic video generation is particularly challenging when the camera is mounted on a moving platform, as camera motion interacts with observed image pixels, creating complex spatio-temporal dynamics and making the problem partially observable. Existing methods typically address this by focusing on raw pixel-level image reconstruction without explicitly modelling camera motion dynamics. We propose a solution by considering camera motion or action as part of the observed image state, modelling both image and action within a multi-modal learning framework. We introduce three models: Video Generation with Learning Action Prior (VG-LeAP) treats the image-action pair as an augmented state generated from a single latent stochastic process and uses variational inference to learn the image-action latent prior; Causal-LeAP, which establishes a causal relationship between action and the observed image frame at time $t$, learning an action prior conditioned on the observed image states; and RAFI, which integrates the augmented image-action state concept into flow matching with diffusion generative processes, demonstrating that this action-conditioned image generation concept can be extended to other diffusion-based models. We emphasize the importance of multi-modal training in partially observable video generation problems through detailed empirical studies on our new video action dataset, RoAM.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors tackle the problem of partial observability video prediction, which deals with video prediction problems in which the camera is also moving, in which case the video is influenced by both the scene dynamics and the camera's motion -- common in autonomous vehicles and robot manipulators. 

This work explicitly models camera motion dynamics by extending the observed image state (existing settings) by introducing three models build upon prior works. Two models are based upon SVG-lp that learn image-action priors (LeAP) -- 
- (i) vg-leap (imagen-action pairs generated using a single stochastic process), and 
- (ii) causal-leap (causal relationship between image and action), and 
- (iii) RAFI -- that augments the image-action state pair of an existing flow-matching model RIVER. 

For learning the latent action prior, two variational approaches are presented -- (i) combined image-action prior derived from both the observed image and action, with the assumption that image and action states are conditionally independent, and (ii) two separate posterior priors learnt for the image and action latent variables assuming causal interlinking. 

The experimental evaluations are performed on the RoAM dataset which consists of synchronized image-action pairs recorded with a Turtlebot robot using a stereo camera setup. The dataset has 45 training videos and 5 testing sequences (300k videos sequences of 25 frames each used for training). The models are evaluated on the task of video generation for generating 10 frames conditioned of randomly sampled 5 previous consecutive frames. Perceptual and semantic quantitative metrics are used for evaluation.

### Strengths
The problem of partially observable video prediction is quite interesting and has applications in autonomous vehicles that have an onboard camera (such as autonomous cars/taxis), drones (with an onboard camera), and robot manipulators (that have wrist-mounted cameras). 

Tackling video prediction under partially observable settings (where the acting agent is not visible on the camera) can be benefit robot applications (for instance pedestrian intent detection and prediction could influence autonomous driver decisions, video prediction networks as world models for robot manipulators etc.)

This work tackles the interesting idea of incorporating (robot) actions (as a learned latent) into the video prediction/generation task that have been traditionally conditioned on just image frames. 

The problem statement is interesting the authors motivate it well. The paper is also well-presented and articulated except for a few spelling errors (for instance lossses pg 6, divergance pg 6).

### Weaknesses
Although sound, I find the contributions (incorporating actions) to be minimal additions to the existing frameworks. For instance, in VG-leap, the extended image-action state pair is used to condition the SVG-lp model instead of just the images, and the latent posterior approximated with recurrent modules. 
Similarly, in Causal-leap, two stochastic posteriors are learned -- one each for image and action, learnt using recurrent modules. 
For RAFI, the image latent is concatenated with the action state along the image latent's channel dimension of an existing RIVER model. Given the extensive literature on latent conditioning methods, I would have liked to see comparisons/discussions with different latent conditioning methods for incorporating actions. 

I find the experimental evaluations quite weak. The experiments are performed just on the RoAM dataset which has just 45 video sequences for training and 5 for testing/inference I would have liked to see comprehensive comparisons -- for instance on the robot manipulation settings in which case the camera is mounted on the robot's wrist. The Causal-leap model should be evaluated on such a setting -- which has a larger action space (7dof instead of the 2-dimensional in RoAM) that was used to motivate the problem. A similar comparison could have been done on drones for instance. 

Evaluations on short sequences. Predicting just 10 frames or evaluating on 25 frame length long video sequences does not quantify as long-term video prediction (which was used to motivate the manuscript). In such short horizon prediction problems, it is harder to quantify the effect of the moving camera. I would have liked to see examples of video predictions that are influenced by external factors (for instance the car turning right due to an obstacle on the left -- collision avoidance being one of the motivations). The quantitative metrics used in the paper evaluate semantic/perceptual quality of the generated videos -- fvd, lpips, vgg-16 etc., and don't necessarily motivate incorporating actions into the video prediction problem. TLDR; how obstacles or other hinderances influence video predictions is quite unclear as the metrics primarily evaluate video quality and not decisions. This would also strengthen the applications of such systems.

### Questions
- How does the model perform on long-horizon video prediction problems. 
- How is the performance in different robot settings? (for instance, robot manipulators, drones, etc.)
- Were any other latent conditioning methods evaluated?

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
The paper proposes three action-conditioned video prediction training frameworks and shows empirical results of their efficacy on a robot video dataset.

### Strengths
* The paper adapts action-free VAE and flow-based formulation from video prediction literature to action-conditioned learning. 
* Empirical results show benefit of incorporating action information in training in terms of video prediction accuracy.

### Weaknesses
 * Missing related works. The paper revisits the literature on VAE-based and flow-matching-based video prediction models, without discussing the latter in the section of prior works. 
* The method restricts cameras to be static (line 148). This assumption does not hold in general for casual videos outside of the training data being used and limits the applicability of the method. 
* The assumption of causality between actions $a_t$ and observed framer $x_t$ is again specific to robot manipulation tasks with fixed cameras as in the RoAM dataset used in this paper. This assumption does not hold in generic videos. 
* The paper lacks a discussion of the potential benefit of incorporating actions into video modeling frameworks in general. Action-free video prediction training does not require action annotations and is much more scalable. If the downstream task is robot manipulation, an alternative approach is to train action-free video prediction models and extract robot actions via inverse dynamics [1]. More discussions would help strengthen the paper. If the goal is accurate video prediction itself, then how does the method compare to state-of-the-art video prediction architectures? 
* What's the relation of the proposed 3 distinct models? A much more extensive discussion on this would help clarify the motivation of developing three separate frameworks in the paper.  
* The paper claims results on incorporating camera motion (line 014) but empirically only evaluate on datasets with fixed cameras.

### Questions
* How are discussions on diffusion-based video prediction (line 131 - 135) related to camera controls (line 103)? 
* What's the action space in RoAM? Is it continuous or discrete? Does the method scale to high-dimensional action space?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper extended the stochastic video generation method with explicit encoding of camera motion dynamics, and then proposes three models , 1) SVG-LP extended with image-action joint states, 2) SVG-LP with disentangled image and action states (with a predefined causal dependency), and 3) RIVER jointly conditioned by the image-action states. This paper compares the proposed models in a action-labeled robotic video dataset named RoAM, and shows certain improvements than existing approaches that do not include camera motion dynamics.

### Strengths
- It shows that combining the camera motion dynamics with visual dynamics will help the video prediction as well as the action prediction. This idea is straightforward but is useful in many cases, such as the design of the world models in embodied agents.
- The paper is easy to follow, and the supplementary materials seem comprehensive.

### Weaknesses
Novelty
- The main weakness of this paper is lack of novelty. Indeed, applying camera motion dynamics to condition video generation is not a new story. Recent studies have even tried to customize video generation with user-directed camera movement (Direct-a-video, siggraph'24), or abstract textual motion descriptions (LEGO, eccv'24). In this case, multimodal training of actions and images to the basemodel such as SVG-LP may not meet the expectations of the audience in recent research communities. However, the modification of RIVER is quite trivial and the gain is quite marginal. It was expected that a good action interaction scheme with visual space would lead to a powerful world model that can predict faithful future actions along with physically reliable future frames. The proposed method did not show such kind of potential, according to its results.

Dataset Limitations 
- Limited diversity: The RoAM dataset is just about several indoor scenes with a specific robot and features mainly corridors, lobby space, staircases with human movements like walking and sitting. This limited setting may not fully represent the wide variety of real-world scenarios with moving cameras. It would be beneficial to test on a more diverse set of datasets that include a broader range of environments and camera movements.
- Data size and complexity: While the dataset contains a significant number of video sequences (more than 300k), each sequence has only 25 frames of image size 64 × 64 × 4 (again, the diversity of scenarios is limited). This relatively small frame size and limited sequence length (just 1 second may not capture large motions) may not capture all the complex spatio-temporal dynamics that occur in real videos. Larger frame sizes and longer sequences could provide more detailed information for the models to learn from, potentially leading to better performance and more accurate video generation.

Comparison with State-of-the-Art
- Poor visual quality and overfitting issues. The reported qualitative results are of poor visual quality, making it hard to convince that the proposed action prior indeed works. Moreover, the action prediction errors are surprisingly small. Are the GT action values small, or the overfitting issue just happened? 
- Incomplete benchmarking: The paper compares the proposed models with a few existing methods such as SVG-lp, RIVER, and ACPNet (cannot find its reference though). However, there are many other recent and relevant state-of-the-art video generation models that are not included in the comparison. For example, some of the latest diffusion-based models or other advanced variational frameworks may have different approaches to handling camera motion and image-action dynamics. 
- Lack of ablation studies on key components: While an ablation study is conducted to compare the performance of Causal-LEAP, VG-LeAP, and SVG, more ablation studies on other key components of the models could be useful. For example, analyzing the impact of different encoding and decoding strategies, the role of the latent variables in capturing image-action dynamics, or the effect of the conditional flow matching in RAFI on the overall performance would provide a deeper understanding of the models and help in identifying areas for improvement.

Minor Issue
- The citation in the paper may use the wrong latex command, using \citep{} instead of \cite{}.
- The font sizes in the plots are too small, especially Fig. 4 and 5, 7.

### Questions
Please check the questions in the section of the weaknesses.

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
3

### Summary
This paper tackles the partially observable video prediction problem, where the camera is in motion, by incorporating both camera movement and action. The authors propose three models: (1) VG-LeAP, which treats the image-action pair as a state from a single latent stochastic process; (2) Causal-LeAP, which learns a separate action prior conditioned on the observed images and action history; and (3) RAFI, which integrates the augmented image-action state with a conditional flow matching framework. Empirical results on the RoAM dataset demonstrate the effectiveness of these models in addressing partially observable video generation.

### Strengths
1. The paper addresses an important and interesting problem in video generation—partially observable video prediction.
2. The paper introduces three models based on variational frameworks and conditional flow matching.

### Weaknesses
1. The paper lacks a comparison with prior works that model camera motion in video generation. Several existing studies incorporate camera motion information [1-6]. The authors should discuss how their methods differ from these works and clarify the advantages of their approach.
2. Experiments are limited to the RoAM dataset, which includes camera action annotations. Testing the models on additional datasets and demonstrating generalization to video data without explicit camera action annotations (like A2D2 [7]) would strengthen the effectiveness of proposed models.
3. The rationale for proposing three distinct models is unclear. The authors should explain the specific advantages, disadvantages and computational complexities of each model and provide guidance on when to use each one.
4. The frames shown in Figures 6 and 8 are too blurry, hindering a proper assessment of video prediction quality. Providing zoomed-in key areas or video samples would improve evaluation clarity.

### Questions
1. What are the differences between the proposed methods and prior works listed in Weakness? What are the advantages of the proposed method?
2. What are the connections between the three proposed models? What is the purpose of proposing three models? What are the advantages and disadvantages of each model?
3. Can the proposed method generalize to video data without explicit camera action annotations?

### Soundness
3

### Presentation
2

### Contribution
2
