# Visual Encoders for Data-Efficient Imitation Learning in Modern Video Games

- Decision: Reject
- Scores: 3, 3, 1, 3

## Abstract
Video games have served as useful benchmarks for the decision making community, but going beyond Atari games towards training agents in modern games has been prohibitively expensive for the vast majority of the research community. Recent progress in the research, development and open release of large vision models has the potential to amortize some of these costs across the community. However, it is currently unclear which of these models have learnt representations that retain information critical for sequential decision making. Towards enabling wider participation in the research of gameplaying agents in modern games, we present a systematic study of imitation learning with publicly available visual encoders compared to the typical, task-specific, end-to-end training approach in Minecraft, Minecraft Dungeons and Counter-Strike: Global Offensive.%

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on the challenge of training agents in modern video games, going beyond simpler games like those on Atari. The central research question is: How can images be encoded for data-efficient imitation learning in modern video games? To address this, the authors compare both end-to-end trained visual encoders and pre-trained visual encoders across three modern video games: Minecraft, Minecraft Dungeons, and Counter-Strike: Global Offensive.

the paper's main contributions can be summarized as follows:

1. **Addressing a Gap**: The paper tackles the challenge of training agents in modern video games, which has traditionally been resource-intensive and costly.
2. **Leveraging Large Vision Models**: It explores the potential of using publicly available large vision models to reduce costs and resource requirements, a pertinent issue given the current trend in machine learning towards larger models.
3. **Comparative Study**: A systematic study is conducted to compare the performance of publicly available visual encoders with traditional, task-specific, end-to-end training approaches in the context of imitation learning.
4. **Focus on Modern Games**: The study specifically targets modern video games, including Minecraft, Minecraft Dungeons, and Counter-Strike: Global Offensive, reflecting a move beyond simpler, classic game environments.
5. **Human-like Gameplay**: The authors emphasize training agents to play games in a human-like manner, using behavior cloning and offline training with human gameplay data, which is a step towards creating AI that can interact in complex environments in a natural way.

### Strengths
1. The authors have selected a diverse set of modern video games, including Minecraft, Minecraft Dungeons, and Counter-Strike: Global Offensive, for their experimental studies. This choice reflects a significant step forward from the commonly used Atari games in previous research, providing a more realistic and challenging benchmark for evaluating imitation learning techniques.
2. The paper introduces an innovative approach to imitation learning by leveraging publicly available large vision models. This strategy not only addresses the resource-intensive nature of training agents in modern video games but also democratizes access to high-quality training for smaller research groups or institutions.
3. The writing is clear, concise, and well-structured.

### Weaknesses
1. The selected tasks, such as chopping trees in Minecraft, appear overly simplistic. While the authors conclude that there is no significant difference between various visual encoders and input image resolutions, the simplicity of these tasks undermines the reliability of this conclusion. Evaluating models like CLIP and DINO on such straightforward tasks does not effectively demonstrate the differences between modern vision transformers and CNNs. A more rigorous evaluation would involve more challenging tasks, such as `MineRLObtainDiamondShovel-v0` or `MineRLBasaltBuildVillageHouse-v0`. These tasks require more complex sequences of actions and would provide a more robust testbed for evaluating the performance of different visual encoders.

2. In time-series decision-making tasks, the memory of historical states is crucial. The paper's use of LSTM to capture only a limited number of frames may be insufficient for long-horizon tasks. For instance, the paper does not specify the LSTM's hidden state size or the number of frames it processes. This lack of detail makes it difficult to assess the model's ability to capture long-range dependencies. The limited memory capacity could negatively impact the agent's ability to learn complex strategies that require remembering past events or states. A more thorough investigation into the memory mechanisms is necessary.

3. The recent Segment Anything model has shown promising results in various visual tasks. It would be beneficial for the authors to compare their approach with this model to explore its potential in the context of imitation learning in modern video games. The Segment Anything model's ability to segment objects within a scene could provide valuable information for the agent's decision-making process, potentially improving its performance.

4. The results in Table 2 indicate that the best model for tree chopping achieves only a 32% success rate. This performance is significantly lower than that of other models like VPT. This raises questions about the relative importance of the visual encoder in the overall agent architecture. It is possible that other components, such as the policy network or the action selection mechanism, play a more significant role in determining the agent's performance. A more detailed analysis of the contribution of each component is needed.

In conclusion, while the authors have compared a considerable number of vision encoders, the reliability of the results is compromised due to their choices in task setting and temporal transformer. The paper also lacks a comparison with the Segment Anything model and a detailed analysis of the contribution of different components to the agent's performance.

Some relevant work has not been cited:
1. Open-world multi-task control through goal-aware representation learning and adaptive horizon prediction [1]
2. A generalist agent [2]
3. GROOT: Learning to Follow Instructions by Watching Gameplay Videos [3]
4. Learning to drive by watching youtube videos: Action-conditioned contrastive policy pretraining [4]

### Questions
See in weakness.

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
This paper studies an important problem: whether a pre-trained vision encoder can boost the performance of sequential decision-making models. The authors comprehensively study four primary encoder categories: self-supervised trained, supervised trained, contrastive-learning trained, and reconstruction trained, and draw several interesting conclusions. This will be meaningful for choosing backbones to design policy models in complicated environments.

### Strengths
* The paper is well-written and easy to follow. 
* This paper studies an important problem: the difference of vision encoders in building policy models for decision-making. 
* The selected environments are three modern video games, which are popular and challenging. To some degree, I believe the conclusions drawn from these environments can be generalized to real-world scenarios.

### Weaknesses
 * **Missing some details.** It is not clear what kinds of image augmentation tricks are used. Why the image augmentation method is specific to the game? Why a pre-trained model (DINOv2) is better than the others? It lacks deep discussions.

* **Provides rollout videos for better understanding.** Rollout videos are very helpful for readers to understand the challenges of the environments and the effectiveness of the model. It is strongly recommended to include some videos in the supplementary materials. 

* **Insufficient evaluation tasks in the Minecraft domain.** In Minecraft, the "Treechop" task is the most basic and simple task. Although it is an important benchmark, however, conducting experiments solely on this task is not enough. It is better to include 2-3 extensive tasks, such as "Hunt animals", "Craft crafting_tables", and "Mine ores", to enhance the soundness. 

* **Concerns about the training data distribution of baselines.** 

* **Missing some baselines and references.** [1] proposed an important foundation model for decision-making in Minecraft, which was trained on large-scale YouTube gameplays with behavior cloning. It yields a good vision encoder that is specified in the Minecraft domain. Although it is cited in the paper, it does not participate in the comparison. I suggest the authors to compare VPT in the experiment. [2] is a large-scale pre-trained segmentation model, which has demonstrated strong cross-domain recognition capability. It should be included as a baseline. [3, 4, 5] are also imitation learning methods in the Minecraft domain, which are strongly related to this topic. I suggest the author reference these works and have necessary discussions. 

### Questions
My questions are listed in the weakness part. 

I will consider improving the rating if the author adequately addresses my concerns.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work compares using pretrained image encoders with learned end-to-end encoders trained with behavioral cloning. They consider a few variants of both ResNets and ViT end-to-end encoders with and without image augmentation. They compare these to encoders from language contrastive pretraining (CLIP), self-supervised pretraining (DINOv2), supervised pretraining (FocalNet), and reconstruction based pretraining (VAE). They compare this methods in 3 modern video game settings: Minecraft Dungeons, Minecraft, and Counter-Strike GO.

They find that image augmentation improves performance for end-to-end BC encoders in some cases, but in other cases it is better to train end-to-end. They first compare which end-to-end encoder is best and find ViT’s to be the most performant. They find that amongst the considered pretrained encoders, DINOv2 performed best. They further compare these methods in more data limited regimes; surprisingly, results are mixed even in the data-limited regime where one would expect pretrained encoders to shine.

### Strengths
The authors provide a valuable datapoint to the community for which existing pretrained encoders they may want to initialize their experiments from (seemingly DINO).

### Weaknesses
Small scope and unsurprising results. This paper is more of a baselines paper comparing existing methods. For a baselines paper, I would expect far more extensive experiments across domains and methods.

The domains considered here, while they are “modern video games”, are quite limited. E.g. for Minecraft they only consider the treechop task, which is the most basic thing one can do in Minecraft

### Questions
How do these methods compare in more domains? I would also expect experiments in simpler domains like e.g. atari, coinrun, maybe robotics environments.

How do the methods considered here compare to other common methods?

- auxiliary objectives for representation learning are quite common in reinforcement learning. Given this paper is studying the efficacy of different image encoders, it would seem natural to me to also include auxiliary self-supervised objectives into the end-to-end experiments
- the authors hold pretrained encoders fixed. It seems natural to also comp

How well tuned were the experiments for different encoders? It seems hyperparameters were held fixed across all architectures.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studied different video encoders for imitation learning in modern video games. The motivation is that existing pre-trained models are usually trained on real-world images, while the impact of distributional shift on video-game images remains unknown. The paper conducted a systematic research that compared different pre-trained visual encoders and from-scratch trained visual encoders in three video games. The observations suggest that pre-trained self-supervised models are worth trying in video game agent development.

### Strengths
- The writing is brilliant. The paper is very easy to follow.
- The study is systematic and leads to some interesting observations. The paper also gives insightful analysis for these observations, which may shed some light on the research of video-game agent development.
- The motivation is clear, and the identified problem (video-game image distribution is different from pre-training distribution) is meaningful for the community.

### Weaknesses
 - Although the paper offered many insights and potential analysis from the emprical observations, the paper lacks enough decisive conclusions. To be specific, I find that the following claims are not convincing:
  - In the last sentence from section 5.1: "while ViTs do not guarantee improvement over ResNets, they can provide significant improvement." This conclusion is drawn from the observation that ResNets are comparable with ViTs in Minecraft Dungeons, while are outperformed by ViTs for a large margin in Minecraft. However, the observation in Table 4 (the experiments in CS:GO) shows that ResNet outperforms ViT significantly. Therefore, it still remains unknown which of these two types of networks should be chosen as visual encoder.
  - In section 5.3, "This finding suggests that, if high-quality data is available for the specific task, it might be beneficial to consider training visual encoders end-to-end for BC agents, even in situations with less available data." As the finding shows the end-to-end encoders is comparable to pre-trained encoders, why do you say that end-to-end is beneficial? Moreover, as the pre-trained backbone is fixed during imitation learning in the paper, the trainable parameters for pre-trained settings are significantly less than end-to-end setting. I am curious if the performance will be better or worse if we don't fix the pre-trained visual encoders.
  - In the last paragraph of section 5.5, it states that the pre-trained visual encoders fail to generalize when the input image size shifts. There are three related questions:
    - The resize operation seems unreasonable. As the pre-trained encoder is fixed during BC training, the feature extracted from the image is fixed, which is distorted during resizing. What about padding the image to 280x280 and then resize it to 224x224?
    - How about unfreezing the visual encoders during training? It may address the last point I raised as the visual encoder can adapt to new input size during fine-tuning.
    - The conclusion is drawn from only one experiment, how about other cases that the pre-trained model fails when input image sizes are different?

- The conclusions are drawn without controlling some critical variables. For example, the effect of network size is overlooked in the paper.
- The experiments are constrained in a limited number of video game tasks. For example, there are thousands of tasks in Minecraft as shown by [1], and this paper only tested on the "Treechop" task. Also, the paper only studied the task-specific imitation learning, while large-scale pre-training adopted by VPT [2] or multi-task imitation learning [3] are not examined.
- (minor) A key motivation of this paper is that, the images are often related to real-world scenes, which differs from video games. But there seems not enough suppotive evidence in the paper, and the readers usually don't know whether video game images are used during pre-training. Maybe a summary table that presents the pre-training sources of different models will be clear.

### Questions
- How do you select the hyper-parameters for different experiments? 
- What are the original image sizes for Minecraft Dungeons and Minecraft?
- Why does the paper use FocalNet as classification supervised pre-trained encoders? ImageNet pre-trained models such as ViT / DeiT are also popular, which share the same architectures as in the other categories (language contrastive / self-supervised pre-trained) and thus are easy to be compared.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
