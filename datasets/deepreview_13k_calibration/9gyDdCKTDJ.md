# Gaitor: Learning a Unified Representation for Continuous Gait Transition and Terrain Traversal for Quadruped Robots

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
The current state-of-the-art in quadruped locomotion is able to produce robust motion for terrain traversal but requires the segmentation of a desired trajectory into a discrete set of skills such as trot, crawl and pace. This misses the opportunity to leverage commonalities between individual gait types for efficient learning and are unable to smoothly transition between them. Here we present Gaitor, which creates a learnt representation capturing correlations across multiple distinct gait types resulting in the discovery of smooth transitions between motions. In particular, this representation is compact meaning that information common to all gait types is shared. The emerging structure is interpretable in that it encodes phase correlations between the different gait types which can be leveraged to produce smooth gait transitions. In addition, foot swing characteristics are disentangled and directly addressable. Together with a rudimentary terrain encoding and a learned planner operating in this structured latent representation, Gaitor is able to take motion commands including gait type and characteristics from a user while reacting to uneven terrain. We evaluate Gaitor in both simulated and real-world settings, such as climbing over raised platforms, on an ANYmal C platform. To the best of our knowledge, this is the first work learning an interpretable unified-latent representation for multiple gaits, resulting in smooth and natural looking gait transitions between trot and crawl on a real quadruped robot.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Gaitor, a framework for learning effective representation of different gaits for quadrupedal locomotion and adaptive terrain traversal schemes. The model is composes of 3 segments: (1) a VAE which encodes history of robot states (proprioceptive) into latent embeddings and decodes to future sequence of states and footholds, (2) an AE which encodes local terrain heightmap filtered using LTI in frequency domain based on future footholds and decodes the same and (3) a planner MLP which takes the phase of the motion and terrain latent to output the radius of an elliptical trajectory in polar coordinates. The latent embedding of past trajectory is filtered to remove high-frequency components as most information is captured by the low-frequency components and then converted into polar form with phase angles. In the polar form, the radius predicted by the planner is used to modulate the latent space to adjust foot-step height and lengths. The proposed setup is demonstrated on a real-world scene.

### Strengths
Gaitor introduces an adaptive planner in the latent space of the VAE. It builds upon the advances introduced by VAE-loco on discretizing the latent space to represent different phases of the footsteps in a gait. Finally, the terrain embeddings are used to modulate the latent trajectories and hence the required footstep height and length for a given heightmap. This helps in building a framework for continuous transition between different quadrupedal gaits.

### Weaknesses
The paper is not written clearly. There is a lot of missing information and abuse of notations. Further, the authors do not justify their choices via suitable ablations which weakens the overall contributions of their method.

How are the latent visualizations constructed specifically? From the material in the paper, it seems like only two lowest-variance (low-frequency, low noise) components of VAE latent embedding are selected and transformed into polar coordinates about the mean as center?

If only the selected components are modulated by the planner predictions of radius, are other components of the latent space discarded before input to decoder? If not, what happens if they are discarded? Else vice-versa? From the context, it seems those are high-frequency components and do not contain much information.

The inference pipeline is not clearly mentioned anywhere. The inputs are the history of states to the VAE which gives a latent trajectory representation. Now, how are the heightmap features calculated? The paper mentions “The height of the terrain at the future footholds are measured from this height map”. How do you get the future footholds? How are the predicted states used?

There has to be an appendix section clearly mentioning the construction of LTI transfer function for getting $y_k$ from $	heta_k$. What is $y_k$? How is $	heta_k$ constructed? How do you define angle between FL/FR and RR/RL? What is $w$ in equation (1)?
Without any definition, the authors have introduced the subscript “$c$” in equation (4)? Which when followed in section 3.2 becomes more confusing. What are $C$-discrete bins? What is $r^*$?

The paper is not very understandable at this point. However, it gives the readers an intuition of what is happening and how it is useful in understanding continuous transition between multiple gaits.

The paper contains remarks like “For example, it is possible to transition from trot to crawl to pace and the reverse only” without any reason.

### Questions
See weakness above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes Gaitor, an imitation learning-based method for learning a continuous latent space of gaits for locomotion. A VAE latent space is trained on examples of expert trajectories. The paper uses the observation made by Mitchell'23 that good controllers can be created as elliptical trajectories in that latent space. The controller learns to predict an appropriate elliptical trajectory conditioned on terrain features. It is shown that the method can be used to automatically transition between gaits by representing the desired gait on a scale (trot = 1, crawl = 0, pace = -1) and continuously interpolating this variable. This experiment was performed in simulation, but transitioning between trot and crawl is possible on the real robot too.

### Strengths
- The paper proposes a promising method for gait transitions for locomotion
- The method doesn't use gait phases, instead implicitly discovering them from imitation data, which is a scalable approach.
- The empirical finding that it is possible to transition from trot to crawl is interesting.

### Weaknesses
 - It is claimed that prior methods do not learn a shared representation between skills. However, Caluwaerths'23 proposes Locomotion-Transformer, which in fact does this, and reports similar results to this paper. Comparing to Locomotion-Transformer would help put the results in context.
- The presentation of the method is poor.
  - Fig 1 - none of the symbols are defined.
  - "Robot-specific encoding" section: $q_k, ee_k, \tau_k, \lambda_k, \dot{c}_k, \Delta c_k$ are all undefined.
  - "The latter is recommended for its simplicity, but the one hot encoding produces the same results". So which one was used in the experiments? Were all experiments performed with both?
  - "Terrain encoding" section: the terrain encoding is not defined in this section. Is terrain encoding same as $z_G$? Also $z_G$ is undefined.
  - Page 4 describes a method diagram in text which would be much more easily explained in a figure. Figure 1 presumably depicts the same information but is not helpful for understanding the method since Sec 3.1 doesn't reference the figure. The reader needs to guess what is the correspondence between the text and the figure. See e.g. Hafner'20 for an example of good presentation.
  - Eq 1. Y, U, s are undefined. The LTI function is never mentioned in the rest of the paper. Since all of the symbols are undefined, it is unclear whether this is used in the method at all, and if yes where.
  - "Training the VAE and Terrain AE" section: terrain encoder is undefined. Unclear how $\hat\theta_c(k)$ is produced. The VAE loss as far as I can tell doesn't depend on the terrain encoder, so it's unclear how the terrain encoder can be trained with those gradients. The terrain decoder is undefined.
  - There is a missing reference in the second line of Sec 2.
  - The citation for GECO is wrong. It is Rezende'18

### Questions
1. Why is it important that the method doesn't use gait phases as an inductive bias? A comparison to Yang'21 that showcases this difference between methods would strengthen the paper.
2. A discussion of a comparison to Locomotion-Transformer is crucial. 
3. Overall, the paper is promising but I am unable to recommend accept due to poor presentation.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a system that utilizes a VAE to encode different quadrupedal gaits into a continuous latent space. A planner then can utilize this latent space to continuously switch between gaits to accomplish different locomotion tasks.

### Strengths
1. The system is able to generate interpretable latent space that can be used to continuously switch between different gaits. It is also demonstrated on a real Anymal robot.

2. The analysis of the latent space demonstrates its interpretability.

### Weaknesses
I don't understand the approach section. It would be great if the authors could make the description clearer. See questions below.

1. " All pose orientations are represented in tangent space." Can you specify what you mean here?

2. I don't quite understand why it is called a VAE instead of just a neural network that maps input to output. My understanding is that a VAE will try to reconstruct the input at its output, but that doe not seem to be the case here. Perhaps this is why I am very confused when reading the paper. My understanding is the proposed "VAE" learns to project the input to a latent space, which is then used to reconstruct the output (which is different from the input). VAE is also used when given the same input to generate multiple plausible outputs, in the context of robots, say given the same user command velocity, generates different gaits that can follow this velocity. I am not sure where is the variational part in the proposed vae.

3.  "The gait input is a label for each gait. This can be a one-hot encoding for each gait or a slider, where the three gaits, trot, crawl, and pace are [1, 0, −1]. The latter is recommended for its simplicity, but the one hot encoding produces the same results and
permits smooth transitions between gaits." I am confused by this sentence, who recommended the latter (and what is the latter?) And are you using this recommended option or are you using the one-hot encoding? And this performance predictor is never used again (I search for PP and performance predictor), what is it used for in the whole system?

4. I am not sure how the different components are used after training. My naive guess is the past trajectory is fed into the vae, and then output the future trajectory for robot control. The encoding of the inputs can be modified by the planner to adjust gaits. It would be nice to make it clearer how the system works.

5. Why is an additional planner needed to deal with terrains since terrain is already an input to the decoder and the training data for the decoder and planner are the same (or could be the same)? Maybe an ablation study is needed?

### Questions
1. " All pose orientations are represented in tangent space." Can you specify what you mean here?

2. I don't quite understand why it is called a VAE instead of just a neural network that maps input to output. My understanding is that a VAE will try to reconstruct the input at its output, but that doe not seem to be the case here. Perhaps this is why I am very confused when reading the paper. My understanding is the proposed "VAE" learns to project the input to a latent space, which is then used to reconstruct the output (which is different from the input). VAE is also used when given the same input to generate multiple plausible outputs, in the context of robots, say given the same user command velocity, generates different gaits that can follow this velocity. I am not sure where is the variational part in the proposed vae.

3.  "The gait input is a label for each gait. This can be a one-hot encoding for each gait or a slider, where the three gaits, trot, crawl, and pace are [1, 0, −1]. The latter is recommended for its simplicity, but the one hot encoding produces the same results and
permits smooth transitions between gaits." I am confused by this sentence, who recommended the latter (and what is the latter?) And are you using this recommended option or are you using the one-hot encoding? And this performance predictor is never used again (I search for PP and performance predictor), what is it used for in the whole system?

4. I am not sure how the different components are used after training. My naive guess is the past trajectory is fed into the vae, and then output the future trajectory for robot control. The encoding of the inputs can be modified by the planner to adjust gaits. It would be nice to make it clearer how the system works.

5. Why is an additional planner needed to deal with terrains since terrain is already an input to the decoder and the training data for the decoder and planner are the same (or could be the same)? Maybe an ablation study is needed?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Due to the requirements of the expected trajectory segmentations into a discrete set of skills, current methods mostly discretize commonalities among gait types, leading to less smooth transitions. To overcome these problems, the authors introduced Gaitor, leveraging a unified representation to capture the correlations among gait types. With the help of terrain encoding and a learned panner operation, Gaitor can take motion commands into account. Specifically, a modified variational autoencoder is applied to infer the robot's current and estimate the future state, which is also determined by the terrain latent space from the autoencoder. The evaluation is in simulated and real-world settings.

### Strengths
1. The writing, figures and tables are clear and understandable.
2. The proposed method is sound. Gaitor uses VAE and autoencoder to transfer the robot state and terrain information into latent space and does further operations like manual control or fuses information on the manifold, which is a good try to integrate multi-information.

### Weaknesses
1. The elements in the formula should be demonstrated more carefully, there are some units that first appear without description.
2. In this paper, there are few works to compare. Although it is firstly to do the task, there should be some way to compare the proposed methods with others, or it is hard to evaluate the performance.

### Questions
No more question.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
