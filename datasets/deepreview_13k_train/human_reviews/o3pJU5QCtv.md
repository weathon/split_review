# EC-Diffuser: Multi-Object Manipulation via Entity-Centric Behavior Generation

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
Object manipulation is a common component of everyday tasks, but learning to manipulate objects from high-dimensional observations presents significant challenges. These challenges are heightened in multi-object environments due to the combinatorial complexity of the state space as well as of the desired behaviors. While recent approaches have utilized large-scale offline data to train models from pixel observations, achieving performance gains through scaling, these methods struggle with compositional generalization in unseen object configurations with constrained network and dataset sizes. To address these issues, we propose a novel behavioral cloning (BC) approach that leverages object-centric representations and an entity-centric Transformer with diffusion-based optimization, enabling efficient learning from offline image data. Our method first decomposes observations into Deep Latent Particles (DLP), which are then processed by our entity-centric Transformer that computes attention at the particle level, simultaneously predicting object dynamics and the agent's actions. Combined with the ability of diffusion models to capture multi-modal behavior distributions, this results in substantial performance improvements in multi-object tasks and, more importantly, enables compositional generalization. We present BC agents capable of zero-shot generalization to perform tasks with novel compositions of objects and goals, including larger numbers of objects than seen during training. We provide video rollouts on our webpage: https://sites.google.com/view/ec-diffuser.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes entity-centric diffusion transformer architecture to generate the sequence of actions and latent states conditioned on a trajectory of image observations across multiple views. The paper claims that object centric representations facilitate composite generalization of behavior cloning agents. Experiments are conducted across three tasks namely, PushCube, PushT and FrankaKitchen to show the effectiveness of the proposed method.

### Strengths
The proposed method leverages object-centric representations to generate action-state sequences for Behavior Cloning and shows that it generalizes to manipulating multiple objects. Experiments are conducted across three different tasks.

### Weaknesses
The novelty of the proposed method is limited as it combines existing methods on entity-centric representation with diffusion policy. It builds upon the existing method [1] to use diffusion models instead of transformers for generating the action-state sequences for object manipulation. Diffusion models have already been shown to be useful for object manipulation tasks in prior works [2, 3]. Specifically, the core idea of using a diffusion model to generate action-state trajectories conditioned on a sequence of image observations has been explored, and the paper does not sufficiently highlight the unique challenges or adaptations required for the object-centric setting. The method's reliance on a pre-trained object-centric representation further diminishes its novelty, as it leverages existing work without introducing significant innovations in representation learning. The paper lacks a detailed analysis of how the proposed method addresses the specific challenges of multi-object manipulation compared to existing diffusion-based approaches. For example, it is unclear how the method handles the combinatorial complexity of multi-object interactions, and whether it introduces any specific mechanisms to address this issue. 

Missing experiments on evaluating the learned policies on real world robots. The experiments are limited to simulated environments, which may not accurately reflect the complexities of real-world robotic manipulation. The paper does not address the challenges of transferring the learned policies to real robots, such as dealing with sensor noise, model inaccuracies, and variations in object properties. 

Figure 4 and Figure 5 overlaps with the captions of the Tables above them.

### Questions
Is the DLP pretraining done separately for each task in IsaacGym environment? 

Further, if PushCube and PushT image observations were used together for pretraining DLP, can it handle the composition where both objects are present together?

Can the method generalize in manipulating novel objects? For example, what is the success rate when T-cubes are added to the Task 1 environment instead of normal cubes.

Since competing methods VQ-BET and EIT-BC work well for single objects, for multiple objects, can they be used sequentially manipulating one object at a given time? What is the performance of this baseline?

What is the performance of the method when using only the frontal view to train the diffusion model? Are two views essential?

Why is classifier-free guidance not used in the diffusion model? Can classifier-free guidance improve the success rate?

### Soundness
3

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
2

### Summary
This paper propose a diffusion-based behavioral cloning method. It uses the object-centric representations instead of pixel-level representation. Deep Latent Particle is used to get representation, followed by an entity-centric Transformer at the particle level to predict action sequences.

### Strengths
- This idea of predicting object manipulation actions through a diffusion-based architecture is interesting. By incorporating object-level information, the proposed method achieves a performance improvement over baseline methods.

- This paper also compare with the state-of-the art non-diffusion baseline, i.e., VQ-BeT, demonstrating the effectiveness of the proposed method.

### Weaknesses
 - The method depends on the capabilities of the image representation algorithm DLP, and experiments are conducted only in synthetic environments. It is unclear if it will perform well in more complex settings. For example, the method is only compared with one non-diffusion baseline VQ-BeT, which is preformed extremely bad on PushCube and PushT (2 out of 3 test environments used in this paper). I wonder why it is only tested on these three environments. Is it possible to also test the model on other environments that baselines achieve very good results, such as Multimodal Ant, BlockPush, UR3 BlockPush, or even nuScenes self-driving, to better demonstrate the advantage of the proposed method?

- What are the advantages of using a diffusion model over other transformer-based methods? Could you provide an intuitive explanation for why it is suitable for this task?

### Questions
- What's the motivation of using diffusion for this task? What are the advantages of using a diffusion model over other transformer-based methods?

- Is it possible to also test the model on other environments, such as Multimodal Ant, BlockPush, UR3 BlockPush, or even nuScenes self-driving, to better demonstrate the advantage of the proposed method?

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
The authors propose EC-Diffuser, a diffusion-based behavioral cloning method designed to enhance multi-object goal-conditioned manipulation tasks from high-dimensional pixel observations. This approach leverages a pre-trained object-centric encoder to map each observation into an unstructured set of latent vectors, where each vector corresponds to a specific object or the background within the observation. The diffusion model is trained to denoise these latent trajectories paired with corresponding actions, using the initial and goal representations as conditional information. To address the unordered nature of these latent representations, the authors employ a Transformer-based diffusion model due to its permutation equivariance.

The authors validate their approach through experiments on several simulated multi-object manipulation environments, demonstrating that it outperforms baseline methods. They also provide ablation studies to highlight the contributions of different components in their method.

### Strengths
* __Writing.__ The paper is well-written and easy to follow. The motivation behind addressing the challenges in multi-object manipulation from high-dimensional pixel observations is clearly articulated. 

* __Novelty.__ The authors present a novel integration of existing approaches by combining object-centric representations (Deep Latent Particles) with a diffusion-based behavioral cloning method. The use of an entity-centric Transformer to handle the unordered nature of latent representations is a noteworthy contribution.

* __Positioning.__ The paper is well-situated within the existing body of research, providing a comprehensive review of related work and clearly distinguishing its contributions from prior methods.

* __Experimental design.__ The authors conduct thorough experiments across several simulated multi-object manipulation environments. They adapt and compare against multiple competitive baselines, ensuring a fair and rigorous evaluation of their method. They also thoroughly compare their approach with both structured and unstructured latent representation-based methods, providing a comprehensive evaluation.

* __Performance.__ Experimental results demonstrate that the proposed approach consistently outperforms baseline methods.

### Weaknesses
 * __Alternative object-centric encoders.__ While the authors utilize DLPv2 as a powerful object-centric encoder, the paper would benefit from experimenting with other similar approaches. Since the DLP module appears to be easily replaceable with other object-centric encoders, exploring alternatives could provide insights into the generality and robustness of the proposed method. This would also demonstrate whether the observed benefits are specific to DLPv2 or applicable across different encoding techniques. Specifically, the paper lacks an analysis of how the performance of EC-Diffuser changes when using encoders with different inductive biases, such as those that explicitly model object relationships or those that produce more compact latent representations. A comparison with a simpler encoder, such as a basic convolutional network, would also be valuable to understand the necessity of the complex object-centric approach.

* __More generalization experiments.__ Although the authors present a wide range of experiments showcasing the advantages of their approach, additional generalization studies could strengthen the paper. Specifically, it would be interesting to see experiments involving novel object shapes, textures, or views where the use of object-centric latent representations might not be as beneficial at test time compared to regular unstructured latents. For instance, the paper could explore scenarios where the number of objects changes significantly during testing or where the objects have different physical properties (e.g., mass, friction). This would help to understand the limitations of the object-centric approach and identify scenarios where it might fail to generalize.

Minor Presentation Issues:

* There is a rendering issue with Figure 5, where the figure overlaps with the text.

* In Tables 2 and 3, the authors use __bold text__ to indicate the training setup. It might be clearer to mention this in parentheses in the column header. This is a minor stylistic suggestion but could improve the overall presentation.

### Questions
* __Table 1 results interpretation.__ In Table 1, regarding the performance of the __EC Diffusion Policy__ on the __PushCube__ environment, there is an unusual pattern where the success rate decreases when moving from one to two objects but then increases from two to three objects. In contrast, all other methods exhibit a consistent decrease in performance as the number of objects increases. Could the authors provide an explanation for this anomaly in their results?

* __Real-world limitations.__ It appears that the object-centric encoder is the main bottleneck when it comes to extending this model to real-world scenarios. Is this assessment correct? If so, do the authors believe that object-centric approaches are preferable for real-world applications, and how might they address the challenges posed by the encoder in practical implementations?

### Soundness
3

### Presentation
4

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
The paper presents a method that tackles the problems of behavior cloning and object manipulation. The method contains three main components: an object-centric encoder (DLP encoder), an entity-centric transformer (for temporal information aggregation), and a goal-conditioned diffusion-based decoder (for simultaneous prediction of states and actions). These components were proposed by previous methods, and EC-Diffuser appears to be a combination of several approaches. The results are superior compared to previous work on three simulation benchmarks. Furthermore, it can generalize to scenarios with a higher number of objects (trained on fewer objects, tested on more objects). The ablation studies (Table 5) show the effect of each component, revealing that the DLP encoder and goal-conditioned diffusion parts are the most important ones. Overall, the proposed method appears to be the new state-of-the-art. However, it seems to be a combination of previous methods: DLP (for object encoding), transformer-based sequence modeling (VQ-Bet), and diffusion-based decoding (diffuser). By combining these components, EC-Diffuser gains advantages over previous work through its use of the DLP encoder (better object-centric representations compared to VQ-Bet), improved entity-centric transformer (temporal information aggregation compared to DLPv2, which uses autoregressive prediction), and diffusion decoder (better handling of multimodality and uncertainty compared to VQ-Bet).

**Important note:** This review's technical content and analysis are my original work. Large Language Models were used solely to improve grammar and writing style, without altering any meanings or substantive feedback.

### Strengths
* Experiments:
   - The paper evaluates the method on three different benchmarks and provides ablation studies that demonstrate the effect of each component
   - Section 5.4 demonstrates the necessity of state generation, as it helps match objects across different frames. This evaluation approach was both effective and informative
* Performance:
  - The results demonstrate that EC-Diffuser performs exceptionally well on simulation benchmarks and can generalize to different scenarios (as shown in the object-number generalization experiments in Section 5.2)
* Code is available, and video results are presented on the website for better evaluation
* Overall, the paper clearly explains the problem, tasks, and methodology

### Weaknesses
 * Novelty:
     - As previously stated, EC-Diffuser appears to be a combination of previous work
     - The model incorporates the best components from several predecessors, such as:
          - Object-centric encoder from DLP (while its usage is fair, the results should perhaps not depend so heavily on the DLP encoder; without it, the performance is comparable to VQ-Bet) 
          - Transformer encoder from VQ-Bet, which uses a GPT-like transformer encoder on observations encoded by a VQ-VAE
          - Diffusion decoder that predicts both states and actions, similar to Diffuser which also employs this architecture for denoising both state and action
     - The core innovation seems to be in the specific combination of these existing components rather than in the introduction of fundamentally new architectural elements or training methodologies. The performance gains appear to stem from this combination, but the individual components are not novel.
* Real-world evaluation:
    - Can this model be evaluated on real-world datasets such as NuScenes (as VQ-Bet does)?
    - Can EC-Diffuser be adapted for use as GPT-driver?
     - Is it possible to generalize to real-world setups, or would EC-Diffuser be limited to simulation data?
     - What are the necessary changes to make EC-Diffusers work on real-world data?
    - The lack of real-world experiments raises questions about the practical applicability of the method beyond controlled simulation environments. The reliance on simulation data limits the assessment of its robustness and generalization capabilities in more complex scenarios.
* Inference runtime cost:
    - As stated in the limitations and future work section, diffusion inference is time-consuming due to its iterative denoising requirement
     - While real-time inference might not be crucial for simulation data, it is essential for tasks such as autonomous driving where real-time decisions are critical

### Questions
* As stated in the limitations, the model cannot capture the object-centric notion in scenes from the FrankaKitchen environment. The paper suggests that the DLP encoder could be modified to incorporate additional information, such as ResNet features. Could Slot Attention be used to obtain better object-centric features in FrankaKitchen?
* Could EC-Diffuser be applied to real-world datasets like NuScenes, setting aside its inference cost considerations? (See Weaknesses section as well.)
* Can EC-Diffuser generalize to different time horizons?
    - For instance, if the training set uses a time horizon H, could the model be tested on longer time horizons such as 2H?
    - Are there any architectural considerations that might enable or limit generalization to longer time horizons?
* Can the diffusion model's conditioning mechanism (goal action) be replaced with cross-attention instead of AdaLN?
    - Could the conditioning be improved this way, since any input could be tokenized and fed to the cross-attention layers? The authors' discussion and ideas would be informative.
    - Most state-of-the-art diffusion transformers (DiT) don't use cross-attention but instead use Multimodal DiTs, where both input and condition are tokenized and concatenated (as seen in SD3, SD3.5, etc.). Therefore, the claim about using AdaLN would also be reasonable.
* Minor formatting error: Table 1 and Figure 4 overlap, appearing to be a vertical spacing error.

### Soundness
3

### Presentation
3

### Contribution
2
