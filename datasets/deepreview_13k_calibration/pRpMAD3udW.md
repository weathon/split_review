# Mastering Robot Manipulation with Multimodal Prompts through Pretraining and Multi-task Fine-tuning

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Prompt-based learning has been demonstrated as a compelling paradigm contributing to large language models' tremendous success (LLMs). Inspired by their success in language tasks, existing research has leveraged LLMs in embodied instruction following and task planning. 
In this work, we tackle the problem of training a robot to understand multimodal prompts, interleaving vision signals with text descriptions.
This type of task poses a major challenge to robots' capability to understand the interconnection and complementarity between vision and language signals. In this work, we introduce an effective framework that learns a policy to perform robot manipulation with multimodal prompts from multi-task expert trajectories. Our methods consist of a two-stage training pipeline that performs inverse dynamics pretraining and multi-task finetuning. To facilitate multimodal understanding, we design our multimodal prompt encoder by augmenting a pretrained LM with a residual connection to the visual input and model the dependencies among action dimensions. Empirically, we evaluate the efficacy of our method on the VIMA-BENCH~\citep{jiang2023vima} and establish a new state-of-the-art (10\% improvement in success rate). Moreover, we demonstrate that our model exhibits remarkable in-context learning ability. Project page: \url{https://midas-icml.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Good paper! This paper proposes a new method called MIDAS for robot manipulation with multimodal prompts. The key ideas are:
A two-stage training pipeline with inverse dynamics pretraining and multi-task finetuning
An effective multimodal prompt encoder that augments a pretrained language model with a residual connection to visual features
Modeling action dimensions as individual tokens and decoding them autoregressively
The method is evaluated on the VIMA-BENCH benchmark and establishes a new state-of-the-art, improving success rate by around 10%. The ablation studies demonstrate the benefits of the proposed training strategy and prompt encoder design.

### Strengths
- The inverse dynamics pretraining is an interesting idea to enable the model to infer actions from visual observations. This facilitates in-context learning from demonstration examples in the prompts.

- Modeling action dimensions independently and decoding them autoregressively is intuitive and shows improved performance.

- Comprehensive experiments on the challenging VIMA-BENCH benchmark with clear improvements over prior state-of-the-art.

- Ablation studies provide useful insights into the contribution of different components.

### Weaknesses
The prompts are quite controlled during pretraining versus the more complex prompts at test time. It is unclear if the pretraining fully transfers to the downstream tasks.



### Questions
- For the inverse dynamics pretraining, were other self-supervised objectives explored besides simply reconstructing the actions?

- What stopped the baseline VIMA model from reaching the same performance with just more compute/data?

- Is there other complementary information like force sensors that could augment the visual observations?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of multi-modal prompting in "embodied tasks", i.e., the combination of language and image to train a model to be capable of multi-tasks. The authors introduced a two-stage training pipeline, in pretraining, using the inverse dynamic modelling loss, and in fine-tuning, using a multi-task imitation loss.

Overall, this paper can be seen as a follow-up of the VIMA[1] paper. Results show a 10% success rate gain in the VIMA benchmark.

### Strengths
The paper is well written. I am glad to read the detailed analysis of the ablation studies. The introduction and related works sections indicate the authors are very familiar with relevant literature.

### Weaknesses
While this paper looks technically sound to me, I found the small improvements based on the VIMA paper can not be viewed as a significant contribution that is sufficient to be accepted in ICLR. The claimed contributions include (1) a MIDAS training framework, i.e., introducing inverse dynamic modelling loss, page 5 Eq(3) in pretraining + multi-task imitation loss; (2) residual connections in the visual layers; 
(3) a small performance gain (10%) compared to the VIMA paper. However, using inverse dynamic modelling loss and multi-task supervision loss are all intuitive and an easy follow-up step after the VIMA paper. Therefore, the reviewer found the contributions are not sufficient to be published as a long paper in ICLR.

Nov 23 update: regarding (3), after reviewing the additional experiments the authors submitted, I think the performance looks good for me. I will raise my score to 5 accordingly.

### Questions
- The authors add the appendix pages in the main paper, which exceeds the page limits. Please remove the appendix in the revision.
Nov 23 update: Have no concerns after rebuttal.

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
This work proposes a new method to learn multi-model prompt robot policy. The  main differences from a prior work, VIMA, are the following:

1. Have a pre-training phrase that pretrains on prompts asking the robot to follow a certain motion.
2. A new encoding method to encode multi-model prompts.
3. A method to model the dependency among action dimensions.

### Strengths
- The pretraining method makes sense in that it uses the implicit motion data in each trajectory as the training signal.
- The new prompt encoding and action dependency modeling are valid.
- Presentation of the experiment results are comprehensive, and extensive details are given for the method explanation. 
- Experimentation is rigorous and follows prior benchmarking.

### Weaknesses
1. The pretraining method is not general enough: it only concern about instruction of "follow motion for ..." for a particular motion trajectory, and therefore it mainly tackles the tasks with prompts given a certain motion of a certain trajectory. This means it assumes the task at hand is always similar to follow motion, which is not true.

- An example to illustrate this: it can do well for task T10, but for task T13, when it sweeps something without touching an object, it cannot generalize.

2. For the pretraining method to work, this method also assumes that the prompts contains the motion trajectory keypoint, which is a very narrow assumption and might not always hold. The end users would not be expected to provide the entire trajectories all the time. Therefore the pretraining on motion following is a bit overfitting to the tasks that VIMA designed.

- related to this point: the work advocates for inverse dynamics modeling, but I think this is quite specific to the VIMA-bench task setting with algorithmic oracle. It would be hard to model inverse dynamics in real world.

3. Effectiveness of proposed method: in terms of experiment results (for the full results in Appendix A), there are not significant improvement over VIMA; for those tasks (T10) that has significant improvement, it seems to because the pretraining phase overfits to "Follow Motion" task.

### Questions
1. In Appendix  A page 14, two variations of "Ours" are:
- w/ pretrain
- w/ Encoder-Decoder
Is "w/ Encoder-Decoder" with or without pretraining? Are these two variations adding "pretrain" and "Encoder-Decoder" on top of some common method or is one of them adding on top of another?

3. For task T13, could you provide more details on the failure cases of VIMA and this method respectively? Providing some video rollouts of the two methods would be great. 

4. The authors are encouraged to provide full experiment results in the main text rather than a portion of it.

5. The conclusion mentioned that the work "demonstrate the in-context learning capability". Could the authors elaborate more on this?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes new learning methods to master simulated tabletop robot manipulation from multi-modal prompts. Specifically, their method involves two stages, first inverse-dynamics pretraining then multi-task finetuning. State-of-the-art results are demonstrated on the multimodal prompt benchmark VIMA-BENCH. Furthermore, authors conducted ablation studies to justify the effectiveness of design choices and showcase in-context learning ability achieved by the trained model.

### Strengths
- The proposed method is effective, as demonstrated by its new SOTA performance on VIMA-BENCH.
- Comprehensive ablation studies draw insights into the effectiveness of proposed method.
- Demonstrated in-context learning ability described in Section 4.3 is interesting and impressive.
- The paper is well-written and presented.

### Weaknesses
 - Albeit the method is interesting and demonstrated improvement is impressive, the proposed method is only evaluated on a single benchmark. It would be more solid if authors cloud show similar improvement on other robot learning benchmarks such as RLBench (James et al., 2020).
- It's totally legitimate for the authors to argue other benchmarks do not support multimodal prompts. In that case, I would encourage authors to extend existing VIMA-BENCH by adding more representative tasks to show the in-context learning ability of models trained with the proposed method.
- Although this paper is not designed to address real-robot manipulation, showing proof-of-concept demos would justify the feasibility of applying this method on real hardware.
- Missing citations. Authors are encouraged to discuss the following recent related work:

Radosavovic et al., Robot Learning with Sensorimotor Pre-training, arXiv 2023.

Shah et al., MUTEX: Learning Unified Policies from Multimodal Task Specifications, CoRL 2023.

### Questions
To encode multimodal prompts, the introduced RC provides a direct connection between input embeddings and LM's output embeddings. With this shortcut, is there any performance difference between LMs with varying depth?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
