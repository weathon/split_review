# Language-Guided Object-Centric World Models for Predictive Control

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
A world model is essential for an agent to predict the future and plan in domains such as autonomous driving and robotics. To achieve this, recent advancements have focused on video generation, which has gained significant attention due to the impressive success of diffusion models. However, these models require substantial computational resources. To address these challenges, we propose a world model leveraging object-centric representation space using slot attention, guided by language instructions. Our model perceives the current state as an object-centric representation and predicts future states in this representation space conditioned on natural language instructions. This approach results in a more compact and computationally efficient model compared to diffusion-based generative alternatives. Furthermore, it flexibly predicts future states based on language instructions, and offers a significant advantage in manipulation tasks where object recognition is crucial. In this paper, we demonstrate that our latent predictive world model surpasses generative world models in visuo-linguo-motor control tasks, achieving superior sample and computation efficiency. We also investigate the generalization performance of the proposed method and explore various strategies for predicting actions using object-centric representations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a language-guided, object-centric world model for predictive control, which is both computationally efficient and effective in robotic and autonomous tasks. Using slot attention for object-focused representation and language guidance, it outperforms diffusion-based models in task success, speed, and generalization.

### Strengths
- Effectively uses SAVi to extract object-centric frame features, enhancing computational efficiency and model accuracy.
- Compares against two baseline models (Seer and Susie), highlighting the advantages in efficiency and success rate of the proposed approach.
- Demonstrates generalization capabilities to unseen tasks and objects, showing robustness in diverse environments.

### Weaknesses
 - The contribution in terms of "object-centric" design feels limited, as it primarily substitute the encoder for SAVi without introducing distinct object-centric innovations.
- The lack of an experiment comparing your proposed model with a VAE-based variant (ours + VAE in Tab.1) makes it difficult to conclusively justify the benefits of slot attention.
- Comparison against video diffusion models would be more appropriate than models like instructpix2pix, as diffusion models are more aligned with the proposed model's multi-frame prediction capability.
- The analysis suggesting that future state prediction alone suffices for action decoding is questionable; the low accuracy for "instruction + 0 future steps" (2.5%) compared to near-zero performance for Seer implies that baseline results may lack rigor, potentially outperforming when future states are not predicted.
- The dataset used is overly simplistic, limiting the scope of validation for the world model. Testing across multiple, varied environments would better demonstrate the model’s general applicability and robustness.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes to extend Slot Former to conditioned on language instruction object-centric dynamics prediction model. Such model could be used for decoding future actions for given state and instruction. Such predictions are in tern used for decoding the best action for the next time step. The paper showed that in the synthetic environment with large dataset, using such structured repression leads to better performance in comparison to using diffusion models for future state prediction. In addition, authors showed that such model is able to generalize to unseen tasks.

### Strengths
- The paper is well-written and mostly easy to follow. 
- The authors provide a comparison with several image generation baselines adapted for the robotics domain, showing large gap from them. 
- The authors study how robust their method to some changes in the environment, such as changing the block type or changing the task to unseen one.

### Weaknesses
- Overall, the proposed method is a relatively straightforward modification of the SlotFormer, incorporating language goal-conditioned predictions and trained on a large dataset of demonstrations. While not inherently problematic, the method's effectiveness should be rigorously evaluated across diverse and challenging environments. Furthermore, a comprehensive comparison with state-of-the-art world models, such as TD-MPC2 [6] and PWM [7], is crucial to ascertain its relative performance and potential advantages.

- While the improved performance on the synthetic dataset is encouraging, it remains unclear how the method would perform in more realistic scenarios where both object-centric models and corresponding agents can struggle. As mentioned by authors, recently it was shown that object-centric methods are able to decompose much challenging images or videos (e.g. see DINOSAUR for images or VideoSAUR [5] /SOLV for videos). Thus, it would be important to test how object-centric world models perform in more realistic environments with visually more complex scenarios, e.g. by training LSlotFormer on VideoSAUR or SOLV slots on environments like ManiSkill2. For instance, evaluating the model's ability to generalize to novel object configurations, lighting conditions, and background complexities would provide a more comprehensive assessment of its robustness and practical applicability.

- The comparison to standard baselines on this task is not sufficiently thorough. While outperforming diffusion models for video prediction is a positive result, it is not clear if the usage of a world model with object-centric representations is comparable to or surpasses state-of-the-art algorithms trained using the same data. A direct comparison with methods that leverage similar object-centric inductive biases would be particularly informative.

- Some experimental results would benefit from further analysis: for example, the paper does not provide a clear explanation for why using language conditioning for the agent itself leads to a decrease in the success rate. Investigating the potential interference or redundancy introduced by language conditioning in the agent's decision-making process could shed light on this observation.

- Some potentially missing related work in video-based object-centric learning, control with object-centric representation and world models based on the object-centric representations:

1. Focus: Object-centric world models for robotics manipulation [1]
2. Learning Dynamic Attribute-factored World Models for Efficient Multi-object Reinforcement Learning [2]
3. Self-Supervised Visual Reinforcement Learning with Object-Centric Representations [3]
4. Entity-Centric Reinforcement Learning for Object Manipulation from Pixels [4]
5. Object-Centric Learning for Real-World Videos by Predicting Temporal Feature Similarities [5]
6. TD-MPC2: Scalable, Robust World Models for Continuous Control [6]
7. PWM: Policy Learning with Large World Models [7]

### Questions
- What is trained during "Predict future dynamics"  Figure 1(b)? If nothing remome "fire" sign near the world model? 

- "nature of slot attention not being robust to variable object number" this could be clarified

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- The work proposes to inject language control in object centric world models and show its effectiveness in control. 
- It argues that object centric models, specifically based on slots as studied in the paper, are more efficient and performant than large scale video generation models based on diffusion. 
- They conduct experiments on a simulated table top manipulation benchmark to justify their method and various design choices.
- They present an analysis on how to tune these world models in terms of action decoding, look ahead steps, access to past states to achieve good performance.

### Strengths
- The paper is well written and easy to understand. 
- The problem of building a world model for predictive control is a useful and relevant one to solve. 
- The authors have ablated the components of their approach fairly well, including how to do the best action decoding, how many past steps to use in the world model etc.

### Weaknesses
 - The authors do not have a SlotFormer baseline, which does not use any language conditioning. Given that one of the key claims of the paper is that language conditioned object centric world models help downstream tasks, checking the importance of being language centric is critical. Adding that baseline would be helpful. Specifically, the authors should train a SlotFormer model on the same data and compare its performance on the block manipulation tasks. It would be valuable to see if a non-language conditioned model can learn to perform any of the tasks or if it completely fails, providing quantitative results (e.g., success rate) for this baseline.
 - For the evaluation of this approach, the authors have used the language table simulation environment, which involves some objects to be manipulated on a table top setting. This makes sense since there is a clear distinction between foreground (the objects) and background, which favors object centric approaches over general video generative models. However, showcasing some other scenarios or evaluation setups where maybe lets say intuitively a video generative model would have an edge, would have been interesting and more convincing to see. For instance, evaluating the model on environments with more complex visual scenes, varying backgrounds, or occlusions would provide a more comprehensive understanding of its capabilities and limitations. It would be particularly interesting to see if the model can still effectively segment and track objects in such scenarios.
 - Minor: The qualitatives in figure 3 are not the easiest to parse, if the author’s method works well, but having a video to see the predictions would make the difference much clearer, I couldn’t find anything in the suppmat.

### Questions
A few questions (some overlapping with Cons. section above):
- Is language table the de-facto setting for studying object-centric control? It seems fairly limited and biased towards object centric approaches since it is clearly possible to discard the background information quite easily. Studying it in cases of ambiguity, where sometimes the background is obvious to ignore and sometimes not would bring more of the community to investigate this topic.  
- In section 4.6, Is a world model really necessary? - Have the authors reported a pixel2action baseline, basically that does the same learning procedure, and except for learning from images directly, extract from some off the shelf network. The current results only ablate the absence of future slots, which makes sense, but that doesn't answer the question generally about needing a world model or not.

### Soundness
3

### Presentation
3

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
The authors propose to train a language-conditioned latent dynamics model whose state representations are object-centric “slots” provided by a frozen pre-trained model. They then train an inverse dynamics model that predicts the actions corresponding to the transitions of the autoregressively-generated latent slot representations.

### Strengths
- The paper is written quite clearly, I think the authors presented their ideas quite well
- I appreciate the ablation discussions in 4.6.

### Weaknesses
 - Despite the paper being relatively clearly written, I would highly recommend using ICLR 2025’s extended page limit to increase the size and quality of your visualizations. For instance, for Figure 3, it’s very hard to see where the cube and moon are in the scene. I likewise cannot see any empirical quality differences between your approach’s generations and SuSiE’s.
- The approach is not tested on a wide range of tasks – only the simulated LanguageTable benchmark. It’s not at all clear to me that it would generalize to the real world. Given that SuSiE was evaluated both in sim (CALVIN) and on real-world robots on Bridge-like tasks and showed good performance (compared to strong real-world baselines like RT-2), it is unclear if the present paper’s approach would similarly scale to such more complex tasks.
- Similarly, the authors claim: “However, the major drawback of language-guided video-generation models is the requirement of large-scale labeled language-video datasets and the corresponding high computational cost. Therefore, latent predictive models, which abstract video to predict forward in compact latent state spaces, can serve as an alternative from a computational efficiency perspective.” 
  - If this is true, it seems more sensible to evaluate in the real world, where data is more limited than in sim.
  - Additionally, SuSiE does show that an off-the-shelf image generation model pre-trained on general image-language data can be fine-tuned to work well with robot data just on existing relatively limited robot datasets. If that’s the case, it seems highly unclear that sample efficiency is a problem.
- “The task is to move a block to another block based on the description of the colors or shapes … which are the red moon, blue cube, green star, and yellow pentagon.” This likewise seems very limited – I understand that there are generalization experiments, but the Bridge dataset used for SuSiE’s real-world experiments contain a much wider range of actions and objects, and thus also a much wider range of language (including many noisy labels). It has thus demonstrated to be scalable to a wider range of language and visual entities, which I think would similarly benefit this approach (as it stands, being able to generate latent state trajectories for such a limited number of objects and actions does not say much about its scalability).
- As it stands, given that the approach was only evaluated on a single task setting and said setting is not that representative of real-world language-conditioned visuo-motor robotics tasks, I do not think that this approach has sufficiently demonstrated its general applicability. I think more experiments in a wider variety of domains would be very helpful, especially in real world experiments.
- Finally, I think it would be important to include results that showcase in what settings visual and object-centric world models each excel or break down. I can imagine some cases wherein image or video generation is bad: for example, if I ask a robot to fetch me something from a closed cabinet, the image generator would have to effectively “imagine” what the inside of that cabinet looks like. However, I do not have corresponding intuition for object-centered world models (though it seems like their weaknesses might be quite similar). See last question for more.

### Questions
- It’s interesting that Seer gets basically 0% on all tasks. What are the qualitative failure cases there? 
- Since SuSiE was already evaluated on CALVIN, which is simulated, why not evaluate your approach in that setting?
- In what qualitative settings would object-centered world models be more or less effective than image ones? Do the authors have any intuitive examples of this, and is there any experimental evidence to back that up?

### Soundness
2

### Presentation
2

### Contribution
1
