# Vision-Language Models Provide Promptable Representations for Reinforcement Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Humans can quickly learn new behaviors by leveraging background world knowledge. In contrast, agents trained with reinforcement learning (RL) typically learn behaviors from scratch. We thus propose a novel approach that uses the vast amounts of general and indexable world knowledge encoded in vision-language models (VLMs) pre-trained on Internet-scale data for embodied RL. We initialize policies with VLMs by using them as promptable representations: embeddings that encode semantic features of visual observations based on the VLM's internal knowledge and reasoning capabilities, as elicited through prompts that provide task context and auxiliary information. We evaluate our approach on visually-complex, long horizon RL tasks in Minecraft and robot navigation in Habitat. We find that our policies trained on embeddings from off-the-shelf, general-purpose VLMs outperform equivalent policies trained on generic, non-promptable image embeddings. We also find our approach outperforms instruction-following methods and performs comparably to domain-specific embeddings. Finally, we show that our approach can use chain-of-thought prompting to produce representations of common-sense semantic reasoning, improving policy performance in novel scenes by 1.5 times.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a simple but effective approach of improving visual embeddings from pre-trained VLMs by providing VLMs with useful prompts. For example, to detect spider in Minecraft, instead of directly encoding the scene using a vision encoder, the authors extract more meaningful representations from the VLM by giving auxiliary information like “Spiders in Minecraft are black. Is there a spider in the image?”. This can help the VLM to focus on task-specific/domain-specific information and produce more meaningful embeddings that are useful for training a RL policy. The authors show that the proposed approach outperforms policies trained using generic image features from a vision encoder ( on 3/3 tasks), as well as domain specific image features (on 2/3 tasks).

### Strengths
- The main contribution of the paper “Prompting VLM via auxiliary information and task context” allows extracting more meaningful representation from a VLM is quite interesting and easily applicable to a range of tasks. Instead of fine-tuning VLM for specific domains, it’s easier to plug-and-play existing VLM and extract meaningful representations via prompting.
- Overall, the paper is well written and is systematic in its evaluation. I also appreciate the authors willingness to address concerns preemptively (lack of visual tokens as input to the policy MLP, not fine-tuning VLM similar to RT-1).

### Weaknesses
 - Given that the approach is using a VLM, it’d be nice to test the model for “unseen” tasks, containing objects and instructions not seen during training. For instance, does the policy generalise form “Combat Spider” to “Combat Zombie”? The current evaluation, while showing promising results, lacks a rigorous assessment of the model's generalization capabilities to novel scenarios. Specifically, the paper should explore how the policy performs when faced with new object categories or task instructions not encountered during training. For example, assessing the transfer from 'Combat Spider' to 'Combat Zombie' would provide insights into the model's ability to adapt to new challenges.
- I also recommend a stronger evaluation on Minecraft benchmark consistent with the evaluations done in MineDOJO. Currently, the paper shows result on only three tasks. For a more exhaustive evaluation, MineDOJO recommends evaluation on a collection of starter tasks (32 programmatic and 32 creative tasks). The evaluation on Minecraft is limited, focusing on only three tasks. To provide a more comprehensive assessment, the paper should include a broader range of tasks from the MineDojo benchmark, which includes 32 programmatic and 32 creative tasks. This would offer a more robust evaluation of the proposed method's performance and generalizability within the Minecraft environment.
- While I understand that the authors didn’t have the resources to train a RT-1 style baseline, would it still be possible to train an action decoder on top of the VLM to produce actions. I think having a strong RT-1 style baseline is very important to properly evaluate the question (2) mentioned in the paper — “How does PR2L compare to approaches that directly “ask” the VLM to generate the best possible actions for a task specified in the prompt?” The paper lacks a strong baseline that directly leverages the VLM for action generation, similar to RT-1. While the authors acknowledge resource constraints, training an action decoder on top of the VLM would provide a more direct comparison to methods that use VLMs to directly output actions. This is crucial for properly evaluating the paper's question regarding how PR2L compares to approaches that directly ask the VLM to generate actions.

### Questions
Apart from questions asked in the weaknesses section, I have additional questions: 

- The proposed architecture compresses the task-relevant features from the VLM into a single CLS token which can severely restrict the information available to the policy. While this may work for simpler environments like Minecraft which doesn’t have a lot of clutter, it might not work for other environments / tasks (rearrangement tasks in indoor environments). Did the authors try an approach like Perceiver IO (Jaegle et al, 2021) which encodes N tokens to K (1≤K≤N) tokens?
- I think the first question — “Can promptable representations obtained via task-specific prompts enable more efficient learning than those of pretrained image encoders?” is not really answered. It’s unclear what efficiency mean (faster to train in FLOPS? faster to train measured by amount of training steps?). I think the paper can be made stronger by comparing training efficiency when using the proposed approach vs using VLM image-representations directly.
- I didn’t fully understand the various ablations done. Specifically, did the authors try just giving task context (and no auxiliary information)? Similarly, did the authors try giving just auxiliary information without giving task context.
- While I don’t expect this experiment to be performed for rebuttal, I really wish the authors evaluated their approach on tasks that are visually more complex (or the environments are more cluttered). For [e.g](http://e.gm)., using the approach to perform rearrangement tasks in indoor environments like Habitat / AI2 Thor.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces promptable representations for reinforcement learning (PR2L), which uses the semantic features of pre-trained VLM as state representation for reinforcement learning; the main advantage of PR2L to other pre-trained representations is that PR2L allows extract task-specific features from a generic pre-trained models by injecting task knowledge via prompting. PR2L outperforms both domain-specific representations and instruction-following methods on several tasks in MineCraft domain.

### Strengths
PR2L presents an interesting and creative way of utilizing pre-trained VLMs as representations for visual policy learning. It is unlike prior pre-trained representations for control work in which the features are generic (i.e., directly encoding the image observation); it is also different from recent Vision-Language-Action work (Brohan et al., 2023) in that it does not require fine-tuning a pre-trained VLM and enable high-frequency policies that are disentangled from the VLM backbone. 

As VLMs are increasingly adopted in decision-making pipelines, PR2L is a timely work that presents a lightweight and simple alternative to the existing literature. 

The paper itself is generally well-written and free of grammatical errors.

### Weaknesses
This paper's weaknesses mainly lie in its experimental methodologies.

1. The only form of prompt that PR2L uses essentially amounts to object detection in the scene. This introduces a confounding factor of whether PR2L outperforms baselines because it is able to recognize objects better in the scene. It is unclear if the performance gain is due to the VLM's ability to extract task-relevant features or simply its superior object detection capabilities compared to the image encoder alone. A more controlled experiment is needed to isolate the impact of the prompt-based representation.

2. The paper claims that the prompts are different from instruction following; however, the prompts are still manually constructed and task-specific. It's unclear the advantage of doing so as instructions, by construction, should exist as it is a direct form of task specification. The distinction between a task-specific prompt and a task-specific instruction is not clearly delineated, and the paper does not provide a strong justification for why prompts are superior to instructions in this context.

3. The improvements of PR2L over its various ablations appear only moderate. Furthermore, the best prompt format for the tasks are not consistent; for Spider, it is helpful to include contextual information of what a spider looks like in MineCraft, whereas for the other two tasks, it is more helpful to disregard such information. Therefore, applying PR2L to a new task may require substantial prompt engineering for the best performance. The lack of consistency in prompt design across tasks raises concerns about the generalizability of the approach and the effort required to adapt it to new scenarios.

4. PR2L is only evaluated on 3 tasks; these tasks are also the simplest in the MineDojo benchmark. The paper would be strengthened if more tasks and domains are evaluated. Currently, it is not convincing that PR2L can be generally applied to other visuomotor control domains. Relatedly, PR2L does not outperform MineCLIP on most tasks; given that MineCLIP exists and is open-sourced, PR2L's stated advantages can be better demonstrated via a new domain in which foundation pre-trained representations do not already exist. The limited number of tasks and the lack of a clear advantage over existing methods in the same domain make it difficult to assess the true potential of PR2L.

5. BLIP-2's vision encoder may not be the strongest baseline for pre-trained vision encoders. Several prior works such as VC-1, R3M, MVP, VIP are trained for decision-making and robotics tasks and may constitute stronger baselines in that category. The choice of a potentially weaker baseline makes it difficult to ascertain the true performance gains of PR2L.

### Questions
1. Could a baseline that somehow incorporates oracle object detection information be included? This will test whether PR2L does better because it detects the object of task interest in the scene.

2. Could more tasks and qualitatively different prompts be tested in the paper? Ideally, some tasks in MineCraft requires more than just object detection as auxillary information that may be implicitly captured by a VLM.

3. Could additional pre-trained vision encoder baselines be included? 

I am willing to improve my assessment of the paper if these questions as well as the points in the Weakness section can be adequately addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Paper presents an approach to provide task-relevant visual representations for RL, especially in an open-world environment.The main idea is to take a pre-trained VLM (vision-language model), feed it with the current visual observation, and a meticulously picked prompt about the current task, and then use the resulting embeddings produced by the last two layers of the VLM transformer as the representation. The authors also propose some additional techniques that could be helpful: 1) the VLM has to generate some text out of the prompt and use the embedding to correspond to both the prompt and the produced text, not just the embedding of the prompt only; 2) prompt engineering; 3) an encoder-decoder transformer is used as the policy to distill the representations into a summary embedding. Experiments and ablations on three Minecraft tasks show some promises.

### Strengths
+The study is relevant and could be of interest to many audiences with a background in large models, reinforcement learning, and representation learning.

+The method is well-motivated and technically sound. Pretrained VLM indeed provides open vocabulary and even knowledge-aided representations for multimodal input, which can be quite beneficial to open-world environments. Plus, it is plausible to tweak the representation further via prompting. This is a very neat idea.

+The results look impressive. Although the method is only evaluated on limited (3) tasks in a single environment (Minecraft), the advantages over the baselines and ablative approaches are significant. I do think the authors did a good job of comparing it against several interesting baselines, including no generation, no prompt, etc.

### Weaknesses
-Albeit the promises shown by the results on 3 tasks on Minecraft, I don't think the approach is thoroughly evaluated, especially given their claim on "leverage contextual prior information" and "visually-complex RL tasks" (see abstract). I have the following suggestions:

1) There are some other approaches that are designed to tackle similar issues, especially in Minecraft, ex. [1,2,3]. Although I agree some settings could be different (RL vs. IL, etc), they all deliver some backbone design or objective functions that could facilitate better representations. Comparisons against these missing baselines would help the reader with a better understanding of the significance of the proposed method.

2) Minecraft is indeed a challenging domain in terms of open-world and complex visual observations. However, the tasks being evaluated here (spider, cow, sheep) do not seem to be challenging enough to justify the effectiveness of the proposed method, especially on the claimed "leverage contextual prior information". These mobs are indeed very common and the tasks themselves do not seem to involve complex visual stimuli. My suggestion is to try some long-term and open-ended tasks like surviving, collecting items, etc. [7] offers a few of them and worth taking a look at.

Minor: some references on open-world representation learning and Minecraft agents should be cited: [1-6].

### Questions
-In Figure 2 and 3, why do some curves not have shadows?

-Some prompts shown in Table 1 require hand-crafted domain knowledge, ex. "Spiders in Minecraft are black". Is is possible to avoid this?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a general task-related visual representation as input to the policy, aiming to improve the efficiency of reinforcement learning. By inputting task-related information (including auxiliary information) into VLM as prompts, efficient fusion with the current visual state is achieved. This paper verifies the effectiveness of this approach through experiments.

### Strengths
[1] The method proposed in this paper, PR2L, is very straightforward, and the story sounds reasonable. The organization of the paper is very clear, and it is polished well. 

[2] The experimental analysis is quite comprehensive, and ablation experiments have demonstrated the effectiveness of each part of the proposed method. Conducting experiments in a challenging environment like Minecraft is persuasive.

### Weaknesses
[1] Concerns about computational cost. Obtaining promptable representation requires running a complex VLM on every image returned from the environment, along with the prompt and answer. This cost is prohibitively high and not practical. The authors should provide a more detailed analysis of the computational overhead, including the specific inference time of the VLM, the memory footprint, and the impact on overall training time. It would be beneficial to see a breakdown of the computational resources required for different components of the method, such as the VLM, the policy network, and any other auxiliary modules. Furthermore, the authors should discuss the scalability of their approach to more complex environments and tasks, where the computational demands may be even more significant.

[2] Concerns about the performance of the learned policy. The visually rich representation obtained at such a high computational cost should greatly improve the performance of the policy. However, the authors did not provide videos of rollouts on relevant tasks, making it difficult to judge the effectiveness of the promptable representation in a real Minecraft environment (the three tasks used in the paper are not very complex). The absence of qualitative results makes it challenging to assess the practical implications of the proposed method. It is crucial to demonstrate that the learned policy can effectively generalize to unseen scenarios and exhibit robust behavior in a dynamic environment like Minecraft. The authors should include visualizations of the agent's behavior, showcasing its ability to navigate, interact with objects, and achieve task-specific goals.

[3] Insufficient literature review. Since the authors conducted experiments in Minecraft, they should have provided a more comprehensive discussion of articles that control and plan within Minecraft. However, the authors left out the following important literature.

1. Open-world multi-task control through goal-aware representation learning and adaptive horizon prediction.
2. Video pretraining (vpt): Learning to act by watching unlabeled online videos.
3. Describe, explain, plan and select: Interactive planning with large language models enables open-world multi-task agents.
4. CLIP4MC: An RL-Friendly Vision-Language Model for Minecraft.
5. GROOT: Learning to Follow Instructions by Watching Gameplay Videos.
6. Learning from Visual Observation via Offline Pretrained State-to-Go Transformer.

### Questions
My main concerns are presented in the "Weaknesses" box, please refer to it.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
