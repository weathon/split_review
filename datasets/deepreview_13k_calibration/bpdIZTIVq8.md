# IGOR: Image-GOal Representations are the Atomic Building Blocks for Next-Level Generalization in Embodied AI

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 3, 6, 6

## Abstract
We introduce Image-GOal Representations (IGOR), aiming to learn a unified, semantically consistent action space across human and various robots. Through this unified latent action space, IGOR enables knowledge transfer among large-scale robot and human activity data. We achieve this by compressing visual changes between an initial image and its goal state into latent actions. IGOR allows us to generate latent action labels for internet-scale video data. This unified latent action space enables the training of foundation policy and world models across a wide variety of tasks performed by both robots and humans. We demonstrate that: (1) IGOR learns a semantically consistent action space for both human and robots, characterizing various possible motions of objects representing the physical interaction knowledge; (2) IGOR can “migrate” the movements of the object in the one video to other videos, even across human and robots, by jointly using the latent action model and world model; (3) IGOR can learn to align latent actions with natural language through the foundation policy model, and integrate latent actions with a low-level policy model to achieve effective robot control. We believe IGOR opens new possibilities for human-to-robot knowledge transfer and control. See video demonstrations on our anonymous webpage.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents IGOR, a framework that learns a latent action space consistent between human and robot data. The latent action model can be used to train a foundation world model conditioned on latent actions. By labeling robotics dataset with latent actions and finetuning with real actions, IGOR enables training a foundation policy model.

### Strengths
- The paper seems technically correct, and experimental results are sound
- Other than the method section, the presentation is clear and text is well-written
- The idea of using image goal representation as latent action is, to my knowledge, new.

### Weaknesses
 - It would help to add a method figure to visualize contents in section 2.1-2.3
- Missing citations, discussions, and baselines:
    - For latent action: various previous work has explored using point tracks (https://xingyu-lin.github.io/atm/, https://im-flow-act.github.io/) or text as latent action, how does IGOR compare to those, and why is image goal necessary given the alternative choices?
    - For world model: I would imagine if a VLM is used to convert a human video clip into a short text description, and then language-based video generation model can also generate robot videos. A similar idea using point tracks is also explored (https://homangab.github.io/gen2act/)
    - For policy model: prior works have explored vaiours alternative representations for latent actions: HOPMan (https://homangab.github.io/hopman/), Tract2Act (https://homangab.github.io/track2act/), Gen2Act (https://homangab.github.io/gen2act/) just to name a few. They have demonstrated more task diversity and difficulty than IGOR.
- As a foundation model, IGOR’s evaluations are too simple and not comprehensive enough
    - The paper could benefit from real robot experiments since IGOR policy is trained on a large-scale real robot dataset
    - The paper only demonstrates very simple 2-dimensional or gripper open/close tasks, which are not difficult from a robotics point of view, especially given how much data IGOR requires. Can IGOR handle more fine-grained or long-horizon tasks?
- Needs further clarification of contributions (see Questions section)

### Questions
What is the core contribution of IGOR? Is it the latent action model based on image and goal, or also the world model and policy model? Without judging its usefulness, I do believe the former is novel.  The claim for novelty of the latter seems unjustified without discussions or experimental justifications with regard to other baselines as I pointed out in the weakness section.

I also question the impact and utility of IGOR latent action model if it does not lead to a superior world model or policy model. The paper also doesn’t provide evidence that the IGOR latent action goes beyond coarse actions such as 2D movements and gripper open close, and language or point tracks may very well represent these actions well. Can IGOR represent actions that are more fine-grained (e.g. tasks demonstrated in the ALOHA paper), long-horizon? The authors are welcome to provide additional explanations or experimental results.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method to leverage human videos for training a policy and world model in a latent-action space. They are then combined with a low-level policy trained on robotic data to perform downstream manipulation tasks. Qualitative results demonstrate that the model effectively learns latent actions, and the use of latent actions is shown to improve downstream performance on SIMPLER tasks.

### Strengths
The motivation behind using human videos to learn a latent-action model is both interesting and important. The qualitative results and videos demonstrate that the proposed method can effectively learn a reasonable latent action space.

### Weaknesses
1. [Major] The major concern of this paper is the lack of quantitative results and comparisons. The latent action model is primarily presented through qualitative visualizations, and the downstream performance is only compared to a variant without latent action conditioning. It should also be compared to other approaches. For instance, it’s worth comparing to methods like UniPi [1] and SuSIE [2] which utilize video/subgoal generation combined with low-level robot action inference. These methods have a similar assumption to this paper, as they also use internet-scale video data pre-training and a small amount of robot data.

2. [Major] It is also worth designing and evaluating the downstream robotic tasks from a more comprehensive perspective regarding generalization. The three tasks in SIMPLER used in the paper are in-distribution tasks included in the RT-1 dataset, and there is no evaluation of unseen tasks or more out-of-distribution tasks. The tasks are also quite simple, such as opening a drawer or picking up a can, which are well within the capabilities of many existing methods. A more rigorous evaluation would include tasks that require more complex reasoning or manipulation skills, and ideally, tasks that are not part of the training distribution.

3. [Major] The paper makes several claims that are not convincingly supported by the experiments (see below).

> “l.93: which may hold great potential for next-level generalization in embodied AI.”

There is no experimental evidence demonstrating that the proposed method achieves 'next-level' generalization. It is not compared to any other zero-shot manipulation methods, as mentioned earlier. Additionally, it is unclear what is meant by 'next-level’. The same question applies to the paper’s title.

> “l.502: We argue that forward prediction in latent action space, rather than the original image space, offers several advantages. For example, we can perform sub-task understanding for image-goal representations, and the compressed latent action could be easier to predict than the entire image.”

There is no evidence to support this argument. There are no comparisons to UniPi kind of approach as mentioned above. The claim that latent actions are easier to predict is not substantiated by any quantitative analysis or comparison to direct image prediction methods. The paper needs to provide empirical evidence to back up this claim, such as comparing the prediction accuracy or computational cost of predicting latent actions versus predicting raw pixel changes.

4. [Minor] The use of the term 'foundation' in 'foundation policy/world model' seems a bit arbitrary. What does it specifically mean? The paper does not demonstrate that the model is generalizable or reusable across a wide range of tasks, which is typically a characteristic of a foundation model. The term seems to be used more as a buzzword than a reflection of the model's actual capabilities.

### Questions
1. Could the authors provide more details on the data preprocessing? Specifically, how do you exclude low-quality videos, what are the 'stabilization techniques' mentioned in the paper, and what is the reasoning behind the chosen optimal frame rate?


2. It is unclear what is the purpose of the world model? It is entirely not used for low-level control.

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
Igor defines a unified latent action space, with the goal of enabling transfer among large-scale robot and human activity data.    Visual changes between an initial image and its goal state are compressed into latent actions from internet-scale video data.  IGOR learns a semantically consistent action space for humans and robots, can ‘migrate’ the movements of the object in one video to other videos and can learn to align latent actions with natural language through the foundation policy model.  IGOR is trained by minimizing the reconstruction loss of the goal state.  If compressed sufficiently the image-goal pairs with similar visual changes will have similar embeddings.  It is trained on human video data and robot data with the actions removed.  It has been integrated with a low-level policy and show improved perfomance in low data regime and on SIMPLER.

The latent action model consists of a pair of IDM and FDM.  IDM is trained to predict a given the full sequence of observations, vision features are extracted from a ViTa nd then an ST-Transformer with a temporal causal mask.  Learnable readout tokens are used to extract and compress the visual changes.  VQ is applied to each token.  a_t is the latent action embedding.  FDM uses a single frame ViT to reconstruct o_t+1 with reconstruction loss.  

The world model is continuous time rectified flow, and learns to predict future frames conditioned on the history and the future latent actions.  Open-SORA is the starting point: a 3D VAE that encodes to a latent space and an ST-RFT that generates the latent from text conditioning.  Two modificaitons were made: the text input is replaced with latent actions and the generation is conditioned on the output of the FDM (2:T).

The foundation policy model and low-level policy.    For pretraining, raw observations input and latent actions are output.  Training is the same as the LAM.  The second fine-tuning stage a low-level policy is added to generate continuous outputs.  It’s an ST-transformer with ViT image encoder.  Low-level is an ST-transformer.

Section 3 describes the experiments.  Data comes from open-x, ssv2, EGTEA, EGO4D.  Filtering is done on video quality.  Finetuning is on RT1.  LAM is pre-trained first.  The pretrained LAM labels is used to label actions on the pretraining dataset and to retrain the foundation policy and world model.  The low level p[olicy is fine-tuned on top of the RT-1 policy.  Image-goal pairs are visualized in Fig. 3, latent actions are able to control the changes in objects in different real-world scenes.  LA are semantically consistent across different tasks and human / robot.  Foundation policy can properly follow different language instructions.  Quantitative results in SIMPLER and on the predictiveness of latent actions on robot actions.

### Strengths
Overall a great paper that I’ve been wanting to see for a while (e.g., latent actions for pretraining); it’s well-written, detailed, should be reproducible and innovative.

### Weaknesses
The only downsides to the paper are 1) that the evaluation is only on a few tasks and in SIMPLER (the promise of these approaches is more generalization, so it would be great if there were some real robot experiments) 2) that the pretraining dataset is on the smallish side for foundational capabilities.  It is great that the authors can show such capabilities at a small scale as a proof of concept even still.  3) demonstration of broader foundational capabilities (related to point 1).

### Questions
* It would be great if you could add / share the intuition for adding why having an IDM and FDM?

p.8 image -> pair of images

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
The paper proposes Image-GOal Representations (IGOR), which learns a unified and semantically consistent latent action space shared across different tasks and embodiments, enabling the knowledge transfer among internet-scale video data. The authors show the efficacy of the proposed approach by providing both qualitative and quantitative results showcasing the generalizability of IGOR for different tasks and across different modalities. The paper also includes robot policy learning results to highlight the effectiveness of pretraining with latent actions for robot learning.

### Strengths
- The paper proposes IGOR, a method that learns a shared semantically consistent latent action space across different tasks and embodiments, enabling the knowledge transfer among internet-scale video data.
- The paper proposes a novel architecture for learning a latent action model and combines it with a foundational policy and world model learned on this latent action space. Further, a low level policy can be learned to map this latent action to a robot action making the learned model useful for robot learning.
- The paper includes qualitative results showing that the same latent action applied to different scenes and embodiments leads to similar future frames, highlighting the generalizability of the learned latent action space. 
- Quantitative results showing improvements in policy performance (Fig 6a) and predictiveness of the latent action for robot actions (Fig 6b)  further emphasize the usefulness of such a system for robot control.

### Weaknesses
 - The paper proposes a latent action model architecture combining inverse and forward dynamics modeling. Based on the description in the paper, the inverse model architecture seems very specific using ViT for patch processing followed by a spatio-temporal transformer. Then vector quantization is added to each readout token followed by the latent action being derived from these vector quantized tokens. Ablation studies justifying these design choices would be great and would help the community get insights about architectural choices that matter when designing such models.
- What are the resources and time required to train this model? And what is the inference frequency when running the policy?
- From Fig 6b, it seems like the latent actions are more predictive of robot positions than rotations or gripper movements. The tasks shown in the paper include opening/closing a drawer, picking up a coke can, and moving near which I do not think require much rotations. Since the goal of this work is to show that such a unified latent action helps embodied AI, it would be great if the authors could include more diverse tasks with varying levels of difficulty.
- Further, I would be curious to see if the proposed latent action struggles when a task involves larger rotations (since this would be a potential limitation of the method).

### Questions
It would be great if the authors could address the questions/concerns mentioned in Weaknesses. I am willing to increase my score once these concerns have been addressed.

### Soundness
3

### Presentation
3

### Contribution
3
