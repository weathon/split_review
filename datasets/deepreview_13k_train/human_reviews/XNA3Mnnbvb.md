# DART: A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control

- Decision: Accept
- Scores: 8, 8, 3, 8, 6

## Abstract
\label{sec:abs}
 
Text-conditioned human motion generation, which allows for user interaction through natural language, has become increasingly popular. Existing methods typically generate short, isolated motions based on a single input sentence. %However, human motions are continuous, long, and temporally extended with causal relationships. Creating long, complex motions that precisely respond to streams of text descriptions, particularly in online and real-time contexts, remains a significant challenge.
However, human motions are continuous and can extend over long periods, carrying rich semantics. Creating long, complex motions that precisely respond to streams of text descriptions, particularly in an online and real-time setting, remains a significant challenge.
Furthermore, incorporating spatial constraints into text-conditioned motion generation presents additional challenges, as it requires aligning the motion semantics specified by text descriptions with geometric information, such as goal locations and 3D scene geometry. 
To address these limitations, we propose \textbf{DART}, a \textbf{D}iffusion-based \textbf{A}utoregressive motion primitive model for \textbf{R}eal-time \textbf{T}ext-driven motion control. 
Our model, \methodname, effectively learns a compact motion primitive space jointly conditioned on motion history and text inputs using latent diffusion models.
By autoregressively generating motion primitives based on the preceding history and current text input, \methodname{} enables real-time, sequential motion generation driven by natural language descriptions.
Additionally,  the learned motion primitive space allows for precise spatial motion control, which we formulate either as a latent noise optimization problem or as a Markov decision process addressed through reinforcement learning. 
We present effective algorithms for both approaches, demonstrating our model’s versatility and superior performance in various motion synthesis tasks. 
Experiments show our method outperforms existing baselines in motion realism, efficiency, and controllability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes DART, a real-time, diffusion-based text-to-motion framework that enables interactive text-driven motion control. DART leverages a motion primitive as the action space and learns a diffusion model on top of the latent space to learn continuous human motion. The learned diffusion model conditions on both text and history motion input and can be autoregressively run in real-time. Results on a number of text-conditioned generative motion tasks show the superiority of the proposed method in motion generation quality, real-time interactive control, and alignment with text or scene.

### Strengths
- I find DART a well-designed system that leverages existing techniques (motion primitives, autoregressive diffusion models) in an intuitive way. Using a pre-trained motion primitive during the diffusion motion generation process is well-thought-out and, as can be seen from the result, very performant.
- The real-time **interactive** control part shown in the demo videos is very impressive and useful for downstream tasks. Asking the character to perform actions in real-time and the character has the ability to switch naturally to the next text prompt.
- DART is versatile in terms of the control input and optimization techniques it can interface with (direct optimization, RL, etc.) and the resulting motion is of high quality while conforming to the text prompt.
- Both quantitatively and qualitatively, I find the proposed method state-of-the-art.

### Weaknesses
 - Since BABEL has a limited vocabulary, DART's vocabulary is limited.
- Since motion generation in DART is autoregressive and real-time, I am wondering what the model would do if the text does not change but the model is continuously rolled out. Would the motion be repeated, or would the model be stuck in a weird space? Provide a few single-text prompt experiments for an extended period (e.g., several minutes) and analyze the resulting motion would be helpful.

### Questions
See weakness: how would DART perform if one text condition is given for a long time?

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
3

### Summary
Authors of this propose a text-conditioned motion generation method that is capable of generating long motion sequences, is controlled by a stream of text prompts, and has short inference time and is thus suitable of real-time settings. The promposed method autoregressively generates motion latents using latent diffusion models, conditioned on motion history and the next text input. The proposed method also supports spatial constraints such as keyframe in-betweening and goal reaching. This is done via latent noise optimization or RL by treating the latent noise as actions.

### Strengths
* Having text-to-motion generative models that are real-time and allow for spatial constraints are import components in computer graphics research. Therefore, I find the problem very relavent and interesting.
* Paper is well presented, clearly written, and easy to read.
* I appreciate the detailed overview of contrallable motion generation works in the related works section (Section 2).

### Weaknesses
 * The primary weakness of the paper lies in its similarity to several concurrent works addressing the same idea. While this isn’t necessarily a flaw of this specific work, it does somewhat limit its novelty and overall significance in the broader research landscape.


### Questions
1. What is the advantage of using latent diffusion models in this work? Since the data dimensionality is low, perhaps there is not much performance or speed improvements. 
2. Related to the previous question, what is the advantages of incorporating spatial constraints in the latent space versus the real motion space?
3. For the scene-interaction tasks, does the model have any awareness of the environment? For instance, in the walking upstairs example of Figure 3.b, is the motion first generated given the pelvis location, and the stairs are later added in the visualization?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces DART, a novel method for real-time and text conditioned human motion. While previous methods are limited to short and offline motion generation, DART uses diffusion-based framework to produce continuous motion by learning a motion primitive space conditioned on the text and motion history. DART can also use latent space optimization or reinforcement learning to control the motion generation under different spatial constraints.

### Strengths
- DART has indeed achieved real-time continuous motion generation. Continuous motion generation is an important issue and deserves attention.
- DART enables effective motion control, which is user-centric.
- DART can achieve real-time motion generation, which is user-friendly.

### Weaknesses
 - Due to the limitations of the methodology, training can only use frame-aligned text annotations, resulting in the model's performance on motion detail generation and generalization being significantly inferior to that of models trained with sequence-level annotated data, such as the HumanML3D dataset.

 - The experiments are insufficient, and the results are not solid enough. The MotionX dataset also provides frame-level data. Compared to the small-scale BABEL dataset, the authors lack demonstrations of training effectiveness on larger-scale datasets. Specifically, the MotionX dataset, despite its per-frame annotations, offers a more challenging and diverse set of motions than BABEL, and the paper does not address this.

 - The motivation is unclear. Simply using a short motion generator combined with an motion prediction network can achieve high-quality motion generation while ensuring the quality of motion completion and spatial control over motion points. However, the authors did not conduct a comparison. The paper fails to adequately justify why a novel method is needed when existing approaches, such as combining a method like MoMask [3] for short motion generation with a method like HumanMAC [1] for motion prediction, could potentially achieve similar or better results, especially in terms of motion quality and generalization.

### Questions
Given that current short motion generation methods (such as MoMask) can achieve excellent generalization, and motion prediction methods (such as HumanMAC) are also quite effective, a straightforward idea is to concatenate two separately generated motions. This approach ensures that the generalization and details of individual motions are outstanding, as single motion generation is trained on large-scale sequence-level annotated data (like MotionX and HumanML3D), while motion prediction is trained on long-duration motion datasets (like Human3.6M). If DART only supports frame-level annotated data, it means that the quality of individual motions will fall significantly behind current state-of-the-art methods, indicating that the motivation of the paper is unclear. Therefore, I suggest the authors:

- Provide results from training with sequence-level annotated data, even though the paper mentions that the performance is not good.
- Present performance results on the MotionX dataset, which also has frame-level annotated data but is more challenging than BABEL.
- Combine advanced motion generation methods (such as MoMask) with motion prediction methods (such as HumanMAC), and then compare DART’s performance in terms of individual motion generation quality and motion continuity. I anticipate that if DART does not address the issue of not being able to use sequence-level training data, the quality and generalization of the motions will be poor than other methods.

[1] Chen, Ling-Hao, et al. "Humanmac: Masked motion completion for human motion prediction." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

[2] Guo, Chuan, et al. "Generating diverse and natural 3d human motions from text." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

[3] Guo, Chuan, et al. "Momask: Generative masked modeling of 3d human motions." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

[4] Lin, Jing, et al. "Motion-x: A large-scale 3d expressive whole-body human motion dataset." Advances in Neural Information Processing Systems 36 (2024).

[5] Ionescu, Catalin, et al. "Human3. 6m: Large scale datasets and predictive methods for 3d human sensing in natural environments." IEEE transactions on pattern analysis and machine intelligence 36.7 (2013): 1325-1339.

[6] Punnakkal, Abhinanda R., et al. "BABEL: Bodies, action and behavior with english labels." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents a human motion diffusion model that allows for real-time generation with dynamic text conditioning, using an autoregressive latent-space model.  The technical contributions relate to the specifics of the latent + autoregressive architecture, and showing all that is capable of. Much like for VAEs, it is further shown that the latent can also be used an action, and therefore also used for (a) gradient-based motion sequence optimization, and (b) to develop RL policies for specific tasks. The time-precise text-conditioning is enabled by (trained on) the BABEL dataset, which has frame-aligned text annotation,  unlike the more generic motion clip captioning of other common human motion datasets. The results are demonstrated in a supplementary video. These demonstrations high-quality real-time motions, with dynamically changing text prompts, results for the various modes of generation, e.g., including RL, as well as various comparisons.

### Strengths
Strengths:
- The work demonstrates impressive real-time motion generation, with responsive, on-the-fly text conditioning;
  it provides the architectural design for these to work, as well as demonstrating the utility of the BABEL dataset
  in this context.
- the architecture is demonstrated to be effective across three different types of usage:  (1) autoregressive conditioning;
  (2) motion sequence optimization; (3) reinforcement learning
- The work provides what are, to the best of my knowledge, fairly thorough ablations and comparisons.
  The Appendices and video provide a variety of thorough motion-quality evaluation and ablation studies.

### Weaknesses
Weaknesses:
- video: foot-ground contact cannot be observed because of the faint ambient-occlusion-based ground shadows,
  and thus the motion quality is difficult to judge qualitatively.  Caveat: other papers on the same topic
  often suffer from a similar problem.
- Relevant related work is missing, e.g., "AMD: Autoregressive Motion Diffusion" (AAAI 2024);
   "Interactive character control with auto-regressive motion diffusion models" (SIGGRAPH 2024).
- References are often missing publication venue & other details
- It would be interesting to understand the impact of more "motion primitive" durations, i.e., H+F, on the results.
  A wider window provides more context and therefore perhaps better quality, while a shorter window may allow
  for more flexible transitions between different types of motions.
  I acknowledge the discussion of the H=1,F=1 case in Appendix E.3.
- The paper does not adequately address the presence of high-frequency artifacts in the motion capture data, which are distinct from the high-frequency details necessary for realistic motion. The method's handling of these artifacts, which manifest as jitter and glitches, needs further clarification. The paper should differentiate between these undesirable artifacts and the high-frequency content that contributes to the quality of the motion.
- The paper lacks a clear discussion of the limitations of using global sequence-level text prompts to guide the generation of short, local motion primitives. The potential for semantic ambiguity and unpredictable transitions between actions when using such prompts should be explicitly addressed, with examples provided to illustrate these limitations.

### Questions
The following is a mix of minor questions and feedback.

- (a) the paper discusses number of "frames" and "seconds" at various points, but to the best of my knowledge 
  it never mentions the actual frame rates (fps or Hz) of the motions.  Please do mention these numbers;  they are vital to understanding
  the speeds.  L429 mentions "frame rate exceeding 300", but this presumably refers to 300 generated frames per wall-clock second
  for the synthesis, but the reader does not know whether the actual motion frames being generated should be played at 30 Hz, 60 Hz, etc. In fairness to the authors, other papers also fail to document animation frame rates, but perhaps as a community we can reverse this trend.
- (b) work using RL, for either kinematic or physics-based motion generation, is by default
  autoregressive, and so may be worth furthing noting.  The biggest difference is perhaps that these 
  are usually not developed with text conditioning in mind.
- (c) "DART represents human motion as a collection of motion primitives"
  There are a great many definitions of "motion primitive" that have been introduced over the past 30 years,
  and this paper introduces another.  It might be more clear to simply refer to the "motion representation"
  used for DART, e.g., a short motion segment.
- (d) High frequencies in the raw motion capture are described as being problematic.
  However, in practice, high frequencies are necessary for high-quality representations of motions, due to the rapid
  accelerations that are part of many motions.
- (e) Figure 3:  Can the character perceive the environment?
- (f) The paper would be stronger if it documented examples of some of the limitations discussed in Section 5.
- (g) Would the output be amenable to physics-based tracking, to produce higher-quality motions, e.g., effectively
  a physics-based "projection"?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present a model that can generate long motions controlled by sequences of text prompts, in an online and real-time setting.
This model can additionally follow spatial control such as goal reaching.
The model is based on learning a compact latent space that encapsulates motion primitives.
A diffusion model is trained using this latent space, conditioned on motion-segment prefix and a text prompt.
The paper presents two ways to achieve spatial control: latent noise optimization and reinforcement learning.

The paper is well-written and achieves high-quality results. However, its novelty is weak, as it combines existing techniques. I tend to accept it as it combines these existing techniques in a novel and non-trivial way, to achieve SOTA results.

### Strengths
- Good exposition
- Qualitative results outperform prior art
- Quantitative results are either comparable (t2m) or outperform (spatial tasks) prior art
- Novel composition of known methods

### Weaknesses
 - Weak novelty: all the techniques mentioned are already known: autoregressive generation, latent motion space usage, RL predicting z as an action space, optimization-base control, ...
- Qualitative results contain many foot sliding and floating artifacts.
- RL-based control:
    - Should be compared to more than one method. In particular, there should be a comparison to methods doing running and hopping on the left leg. It can be compared to data-driven methods such as the ones used for optimization-based control, GMD (Karunratanakul et al. 2023), or the recent CLoSD (Tevet et al. 2024).
    - Skate and floor distance are used for both reward calculation and metric calculation. Testing a model on criteria that it was optimized for raises concerns.
- Some points still need clarification. See the "Questions" section.
- Several typos: 
   - L291: "teacle" 
   - L917: "w=5"

### Questions
Questions and Requests:
- In your model description, please cite works relevant to your techniques (e.g., cite MLD when you describe your latent motion space).  Although you cited such works in the RW section, mentioning them again adjacent to each technique would give a better context.
- L251: By diffusion sampler, do you mean DDPM/DDIM, etc.? This is not clearly stated until line 295, where it is only vaguely mentioned. It should be explained earlier and more explicitly.
- Please explain why you selected the deterministic DDIM.
- Can the two methods for achieving spatial goals be used for the same tasks? E.g., textual control is limited in the RL method and is more feasible in the noise optimization one. Please discuss. 
- Compare optimization time vs. baseline methods. In particular, I expect optimization using DART to be faster compared to DNO due to the usage of latent space. Is that correct? Please show relevant results.
- RL-based control: 
    - Are you using the same policy for any prompt, or do you train three different policies, one for each action? (walk/run/hop). If the former is correct, do you support any prompt, or just walk/run/hop?
    - scene observation (L368) - "the relative floor height to the human pelvis": relative floor height: are you considering a flat surface only? if not, are you holding the floor height of the whole scene or just at a specific temporal step? pelvis height: at which frame? 
- Appendix A:
    - L761: Are the locations global or relative to the root?
    - Cite more works that use representation redundancy, e.g., HML3D.
- L808: On one hand you argue that SMPL format is a must for your representation. On the other hand, The representation learned by the network (L758) is agnostic to betas (body definition). Please explain.
- L849: According to the Representation paragraph (L758), dt, dJ, and dR are already part of the representation, hence part of the reconstruction loss (L833). Then why use L_aux ?
- Appendix G rewards: It seems as if for some rewards (e.g., r_dist) "smaller is better", where for others (e.g., r_succ) "higher is better. Please explain.

### Soundness
3

### Presentation
4

### Contribution
3
