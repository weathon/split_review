# Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation

- Decision: Accept
- Scores: 3, 5, 6, 8

## Abstract
Generative pre-trained models have demonstrated remarkable effectiveness in language and vision domains by learning useful representations. 
In this paper, we extend the scope of this effectiveness by showing that visual robot manipulation can significantly benefit from large-scale video generative pre-training. 
We introduce \ourmethod, a straightforward GPT-style model designed for multi-task language-conditioned visual robot manipulation.
\ourmethod takes as inputs a language instruction, a sequence of observation images, and a sequence of robot states. 
It predicts robot actions as well as future images in an end-to-end manner.
Thanks to a flexible design, \ourmethod can be seamlessly finetuned on robot data after pre-trained on a large-scale video dataset.
We perform extensive experiments on the challenging CALVIN benchmark and a real robot.
On CALVIN benchmark, our method outperforms state-of-the-art baseline methods and improves the success rate from 88.9\% to 94.9\%.
In the setting of zero-shot unseen scene generalization, \ourmethod improves the success rate from 53.3\% to 85.4\%.
In real robot experiments, \ourmethod also outperforms baseline methods and shows strong potentials in generalization to unseen scenes and objects.
We provide inaugural evidence that a unified GPT-style transformer, augmented with large-scale video generative pre-training, exhibits remarkable generalization to multi-task visual robot manipulation. Project page: \url{https://GR1-Manipulation.io}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce GR-1, a GPT-style decoder-only transformer for language-conditioned robot manipulation. The model predicts both actions and future observations; the authors pretrain on Ego4D predicting future observations, followed by finetuning on robot data predicting both future observations and actions. The resulting model shows strong performance on the CALVIN benchmark as well as real-world language-conditioned robot manipulation on several pick-and-place tasks.

### Strengths
The paper is well-written, well-presented, and easy to follow. The idea is simple and easy to understand, which is a good thing. While the basic idea of training a GPT-style transformer in this manner is not exactly brilliant or surprising, it hasn't been done in prior work (as far as I know), and the design of the model is principled and well-executed. The CALVIN results are strong, improving significantly on the state-of-the-art.

### Weaknesses
The value of GPT-style video pretraining is the core narrative of this paper, and the primary way that the authors claim GR-1 improves on prior work. Given that, I would say the main weaknesses of this paper are related to a lack of sufficient evidence and discussion surrounding this claim.

- Training details/hyperparameters/etc are missing for the Ego4D pretraining phase, which should definitely be included given their importance to the method.

- The real robot experiments are a bit weak. There are not very many tasks, they are fairly simple, and the tested level of generalization is not very significant. Breaking down the tasks into separate pick and place phases provides some inherent supervision that makes the tasks  easier; I would have liked to see slightly more end-to-end tasks (e.g., "put the broccoli on the plate"). Given how broad the pretraining dataset is, if it really does help, it seems like better zero-shot generalization should be possible: e.g., slightly different objects not found in the robot data.

- The baselines are severely lacking. For example, the authors claim that "compared with VIMA, our method is capable of dealing with much more complex 6-DoF long-horizon language-conditioned robot manipulation tasks". A statement like that should be supported by a comparison to some sort of VIMA-like method (i.e., an encoder-decoder architecture with cross-attention). There is also *tons* of prior work on video pretraining for robotics, much of which is cited in Section 2.3: e.g., R3M, VIP, MVP, and many more. Many of these also pretrain on Ego4D and finetune on robot data. It is impossible to evaluate the strength of GR-1 without comparison to these other methods.

### Questions
- For the Ego4D pretraining, did you use the entire dataset, or some more relevant subset (e.g., hands and objects)?
- Why was $\Delta t = 1$ used during pretraining? If I understand correctly, this means that the next frame in Ego4D was always predicted, which is temporally very close considering that Ego4D videos are fairly high FPS.
- Why is GR-1 w/o pretraining so much better than the baselines in the CALVIN zero-shot setting?
-  "283M parameters, in which 46M of them are trainable" -- to clarify, this means that the majority of the parameters are the frozen MAE and text encoder parameters?
- What is the control frequency of the real robot during the execution of the policy?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper develops an approach for multi-task visual robotic manipulation by pre-training for video prediction on non-robotic datasets, and then fine-tuning on robot data. The main contribution of the paper is to demonstrate that pre-training for the task of video prediction on human datasets enables sample-efficient fine-tuning for manipulation, with some generalization across tasks. The experiments involve manipulation tasks on a simulation environment, and pick/place tasks in the real world.

### Strengths
- The task of video prediction on non-robot datasets for as a pre-training step for downstream manipulation is interesting, and novel to the best of my understanding. Importantly, this pre-training task can ingest all language-annotated video datasets, can hence can be potentially scaled to diverse videos on the web, beyond the Ego4D dataset in the paper. 

- Three external baselines are implemented for comparison, and experiments show some evidence of real-world manipulation, which strengthens the claims of the paper. 

- The vision transformer architecture is without significant bells and whistles, and has standard GPT-style encoder-decoder structure, making it easy to implement and train. In my understanding, the fine-tuning on robot data is very similar to the pre-training step in terms of training details, and doesn't require additional considerations. 

- Overall, the paper is well-written, easy to understand, and the approach is clearly described.

### Weaknesses
 - The results doesn't quite succeed in showing any generalization benefits of pre-training for video prediction on diverse data. This seems to be the main claim of the paper, and requires more thorough experiments for validation. The simulation environments seem to have all the tasks in a similar table-top setting, with very little scene variation across tasks. The zero-shot result is interesting, but it is shown for only a single task.

- The real-world experiments are in very simple pick and place tasks. The Ego4D videos used for pre-training contain such rich skills like articulated object manipulation, scooping, pouring etc. and so for properly showing the benefits of pre-training it is important to demonstrate that the approach can indeed tackle some of the interesting contact rich tasks that involve motions/skills beyond pick and place. In addition, the generalization results are limited to minor distractor and background variations, without variations in the task objects themselves. For reference, several recent robotics papers tackle such tasks and generalizations [1,2]

- The baselines are missing all relevant papers that also pre-train on human videos / image datasets. Many of these are cited in the related works, but some comparison is necessary to actually demonstrate that pre-training for video prediction has benefits compared to pre-training for other objects like masked prediction, contrastive learning etc. (which is a claim of the paper). For example, a multi-task version of R3M [3] can be a relevant baseline that pre-trains on Ego4D but to learn visual representations, and then fine-tunes with behavior cloning.

### Questions
Please refer to the weaknesses above for reference. 

- Is it possible to show generalization results (similar in line to the zero-shot results) but for more tasks and variations within tasks, like different scenes, different objects etc.? This is expecially important because the current simulation benchmark seems saturated with 88% baseline performance, and only marginal improvement to 94% with the proposed approach. 

- For the real-world experiments, is it possible to show benefits in tasks beyond pick/place and those that frequently occur in the pre-training Ego4D dataset like articulated object manipulation, scooping, pouring etc.?

- Why have ABC-> D style result instead of training on all the available tasks (except the held-out one)? I might be missing something here, so would appreciate a clarification, but it seems to me that the zero-shot result in the paper doesn't seem to be training a unified model across all but held out tasks, which seems a bit odd. 

- Is it possible to have comparisons to prior works that also train on datasets similar/identical to Ego4D but have different pre-training objectives? (please refer to weaknesses above for details)

- Is it possible to show qualitative results for the video-prediction (similar to Fig 6 and Fig 11) but for more real-world evaluations? If possible it will be helpful to show some *random* generations to get a sense of how much 

- Is there no forgetting in the pre-training followed by fine-tuning regime (as opposed to co-training)? My sense is that after fine-tuning on the robot dataset, the information acquired from pretraining will be largely lost due to domain shift in the two datasets. One simple way to test this is to look at video generation results of the model on Ego4D clips, just after pre-training, and after pre-training+finetuning. My sense is that the latter will be much worse than the former. I am curious if the authors considered any co-training strategy, where for fine-tuning, the dataset consists of some clips from the pre-training dataset as well as the robot data?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an approach for large-scale video pretraining for robot manipulation. The presented method, termed GR-1, first pre-trains a causal GPT-style transformer on actionless video data, and then finetunes the representation on a smaller number of robot demonstrations with actions. The key aspects of the approach are (1) using a GPT-style transformer for the embodied foundation model and (2) predicting the video tokens/generating future video frames as part of the training process. The approach is tested on the CALVIN simulation benchmark and on a real-world robot platform, outperforming the considered baselines.

### Strengths
* The general problem of making use of actionless human video data is of interest and importance to the research community.
* The problem is well-motivated and the literature review does a good job of contextualizing the paper in prior work.
* The paper is well-written and easy to follow.
* The figures are informative and effectively illustrate the benefits of the proposed approach.
* The experiments consider both simulation and real robot evaluation, as well as an ablation study, demonstrating GT-1's superior performance as compared to the considered baselines and support for GT-1's design choices.
* The discussion did a good job of describing the weaknesses and failure modes of the proposed method as well as the baselines.

### Weaknesses
 * The literature review is missing a number of relevant works. The baselines considered are also not necessarily state-of-the-art. This year, a number of works have come out that would be prudent to compare against.
  * V-PTR: similar high-level motivation of using video-based, prediction-focused pre-training and then action-based finetuning. This should have likely served as a baseline for the proposed method.
    * [A] Bhateja, Chethan, et al. "Robotic Offline RL from Internet Videos via Value-Function Pre-Training." arXiv preprint arXiv:2309.13041 (2023).
  * Diffusion policy: diffusion policy has shown very good results in terms of multi-task, low-data regime performance.
    * [B] Chi, Cheng, et al. "Diffusion policy: Visuomotor policy learning via action diffusion." arXiv preprint arXiv:2303.04137 (2023).
    * [C] Ha, Huy, Pete Florence, and Shuran Song. "Scaling up and distilling down: Language-guided robot skill acquisition." arXiv preprint arXiv:2307.14535 (2023).
  * Pretrained video representations, such as R3M, VIP, and Voltron consider transformers, MAEs, and temporal video frames similarly to the proposed work. Taking a policy learning approach with a pre-trained representation such as the ones listed would have been another good option for a baseline.
    * [D] Nair, Suraj, et al. "R3M: A universal visual representation for robot manipulation." arXiv preprint arXiv:2203.12601 (2022).
    * [E] Ma, Yecheng Jason, et al. "VIP: Towards universal visual reward and representation via value-implicit pre-training." arXiv preprint arXiv:2210.00030 (2022).
    * [F] Karamcheti, Siddharth, et al. "Language-driven representation learning for robotics." arXiv preprint arXiv:2302.12766 (2023).
* Given above works, I am not sure that the statement "GR-1 for the first time shows that a unified GPT-style transformer, augmented with large-scale video generative pre-training is able to effectively generalize to multi-task visual robot manipulation." is accurate/precise.
* I found section 3.2.2 to be a bit confusing in describing the masked tokens. The OBS token is masked to predict the future video frames, is that correct? This sentence: "all the tokens, including the [OBS] tokens, can only attend to all the language and observation tokens but not the [OBS] in the past" was particularly unclear for me. Why specifically the tokens in the past? The notation of [OBS] and observation tokens adds to the confusion.
* In the experimental setup, I did not quite understand the actual size of the training set. My assumption is that GT-1 does not handle data both with and without language.
* It would be helpful to have some measure of statistical significance for the results (e.g., standard error) to understand whether the differences in performance are meaningful.
* Future work description should be more insightful/in-depth than 'combine more robot data and video data in training'.

Some typos and points of confusion are listed below:

1. Often 'causal' is typoed as 'casual'.
2. In Sec. 4.1, '[an] LED and a light bulb'? 
3. In Sec. 4.1, 'datset'.
4. In Sec. 4.1, 'This highlight[s]' ... 'without collecting [a] large amount of data'.
5. The references should be proofread (e.g., to ensure the year is not entered twice, appropriate acronyms are capitalized (e.g., 'rl'), conference name formatting is consistent in terms of capitalization, etc.).

### Questions
1. How different is the D simulation setting from A, B, and C?
2. What is the $\Delta_t$ used in the experiments (e.g., 0.1 s)?
3. Why is only one action predicted at a time rather than a receding horizon style prediction? [B] found the latter to work well.
4. Is there multimodality in the distribution that can be modeled for the video frame prediction task?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes GR-1, a GPT-like autoregressive Transformer model that leverages large-scale video generative pretraining and downstream robotic dataset finetuning to solve language-conditioned robotic manipulation tasks. Specifically, the model is pretrained on Ego4D to reconstruct a future observation from the current observation, and then finetuned on robotic datasets with a combination of video prediction and robotic action prediction losses. Experiments on the Calvin Benchmark and on real robots show that the proposed method achieves better language-conditioned robot manipulation success rates on different task variations.

### Strengths
- The paper is clearly presented and easy to read.
- The proposed video generative pretraining approach, combined with downstream finetuning on task-specific robotic manipulation datasets, achieves better language-conditioned robotic manipulation performance than previous baselines like RT-1.
- The effectiveness of the proposed approach not only holds in simulation, but also transfers to real robot tasks.
- The proposed approach shows promises in scaling up to larger-scale video pretraining datasets and more robot manipulation tasks in the future.

### Weaknesses
 - Is there a plan to open-source the code and checkpoints? Making them available to the community would greatly facilitate efforts to scale up pretraining for robotics.
- Comparing Table 1 and Table 2, the performance on the Calvin Benchmark significantly falls when only using 10% of robotic dataset for finetuning (2k trajectories) compared to using 100% of finetuning dataset (20k trajectories). According to the table, it looks like the primary reason is that the success rate primitive skills (i.e., success rate for "1 task completed in a row") falls from 94.9% to 77.8%. Thus it would be helpful to provide a further analysis into this phenomenon along with the failure modes.
- For zero-shot generalization experiments conducted in the paper, looks like the experiments are primarily conducted on object position variations, color variations, and background variations. It would be helpful to provide an analysis on whether the policy can (1) generalize to longer horizon tasks than the length of the tasks seen during training (e.g., train the policy on 1-5 tasks in a row, test on 6-10 tasks completed in a row); (2) generalize to novel language instructions that are semantically similar to those seen during training but with different wordings (e.g., instead of "lift the red cube", use "pick up the red cube" as instructions; instead of "push the sliding door to the right", use "open the door to the right side" as instructions)
- It would be helpful to provide an ablation on the effect of different quantities of Ego4D pretraining datasets on downstream robot manipulation task performance. Also is there a (possibly smaller) subset of Ego4D dataset for pretraining that is especially helpful for downstream robot manipulation tasks?
- The number of visual features per image from the MAE encoder can be large, and as a result, the current policy might not generalize to very long horizon tasks. It would be helpful to explore using e.g., Perceiver Resampler, to downsample the number of input image features.

For the second to the last weakness points listed above, I wouldn't expect authors to address all of them given the limited rebuttal time, but it would be great if authors could address most of them.

### Questions
See "weaknesses"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
