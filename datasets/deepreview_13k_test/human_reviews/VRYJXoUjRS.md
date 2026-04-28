# Continual Learning via Learning a Continual Memory in Vision Transformer

- Decision: Reject
- Scores: 5, 8, 3, 3

## Abstract
This paper studies task-incremental continual learning (TCL) using Vision Transformers (ViTs).  Our goal is to improve the overall streaming-task performance without catastrophic forgetting by learning task synergies (e.g., a new task learns to automatically reuse/adapt modules from previous similar tasks, or to introduce new modules when needed, or to skip some modules when it appears to be an easier task). 
One grand challenge is how to tame ViTs at streaming diverse tasks in terms of balancing  their plasticity and stability in a task-aware way while overcoming the catastrophic forgetting. 
To address the challenge, we propose a simple yet effective approach that identifies a lightweight yet expressive ``sweet spot'' in the ViT block as the task-synergy memory in TCL.
We present a Hierarchical task-synergy Exploration-Exploitation (HEE) sampling based neural architecture search (NAS) method for effectively learning task synergies by structurally updating the identified memory component with respect to four basic operations ({\tt reuse, adapt, new and skip}) at streaming tasks.
The proposed method is thus dubbed as CHEEM (Continual Hierarchical-Exploration-Exploitation Memory). 
In experiments, we test the proposed CHEEM on the challenging Visual Domain Decathlon (VDD) benchmark and the 5-Dataset benchmark. It obtains consistently better performance than the prior art with sensible CHEEM learned continually.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposed to adapt a network for task-incremental learning. Considering the characteristics of different tasks, the proposed method learns additional parameters or reuse the model weight learned from previous tasks.
Experimental results demonstrate the effectiveness of the proposed method.
The presentation can be improvement.

### Strengths
1. Instead of simply learning more parameters, the proposed method considers reusing the model weight when the new task is similar with previous task.
2. Ablation study is conducted for each design component.

### Weaknesses
1. The presentation can be improve. For example, the figure 4 in the Introduction is overly detailed and contains redundant content. To illustrate the main idea, showing a case of only two or three sequential tasks are enough. For the Fig. 5, the corresponding description is far away from the figure, and a detailed figure for method will be helpful.

2. The overall designs are not focus to the continual learning. (i) For example, in line 244 "How to Adapt in a sustainable way" is related to the gradient vanishing or exploding when learning deep network. And the design of residual connection is not novel.
(ii) Using the cls-token to guide the task-specific learning is not a significant contribution because previous works also use the cls-token to select and learn task specific prompts as in L2P and DualPrompt. (iii) The proposed HEE-BASED NAS considers the task similarity but the novelty is limited due to (ii). 

3. The methods compared in Table 2 and Table 3 are limited and somewhat outdated; the latest papers in class-incremental learning should be included with necessary modifications.

4. With the parameter-efficient finetuning (PEFT) techniques, the task-incremental learning seems can be directly addressed by learning different PEFT module while keeping the main backbone frozen. The L2P learns the tasks prompt, which can be regarded as prompt tuning in PEFT. Although simply adding more prompts will quickly leads to performance saturation, adding more PEFT modules such as Adapter, LoRA may help. Therefore, a natural question is the comparison of the proposed method and the combination of different PEFT compare in terms of performance and number of learnable parameters.

### Questions
Please refer to the Weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focus on task-incremental continual learning (TCL). The proposed method, CHEEM, presents a hierarchical task-synergy exploration-exploitation sampling based NAS method for learning task-aware dynamic models continually with respect to four operations. The results on experiments conducted on the large-scale, diverse and imbalanced VDD benchmark demonstrate the better performance of CHEEM.

### Strengths
1. The proposed method proposes a novel hierarchical task-synergy exploration-exploitation sampling method based on NAS for learning task-aware dynamic models continually with respect to four operations.
2. This paper is good written and easy to follow.
3. The proposed method is evaluated on a persuasive experimental setup with larger datasets, which is similar with the wild scenarios.

### Weaknesses
1. There are not enough methods for comparison. In my opinion, the methodology of the paper may need to be compared with more methods，such as DualPrompt [1].

[1] DualPrompt: Complementary Prompting for Rehearsal-free Continual Learning. Wang. et.al. European Conference on Computer Vision.

### Questions
1. Due to the additional training time for NAS in this method, is the training time of the paper's method longer compared to other methods ?

### Soundness
2

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
This paper presents a novel way of designing a dynamic network in continual learning.
Specifically, this work first analyzes the potential component of the ViT network as the synergy memory and concludes with choosing the projection layer.
The paper designs a NAS-based framework and defines operations like Reuse, New, Adapt, and Skip and associated methods to achieve continual learning.
The author also shows experiments under task-incremental learning settings on multiple datasets.

### Strengths
1. Strong Motivation. The natural way to conduct continual learning is to re-wire the neural networks and it is good to see the trial on the popular vision transformers.
2. Reasonable designing. I think the design of Reuse, New, Adapt, and Skip is reasonable and complete.
3. The proposed task-synergy exploration-exploitation (HEE) is novel and effective.

### Weaknesses
1. Limited applicability. This paper only focuses on the task-incremental learning paradigm, which holds a strong assumption that the incoming streaming samples are organized as different domain groups and that the task IDs are available during inference. I have noticed the authors have explained their thoughts on this in Lines 92-102. However, I am still concerned about this because (1) I don't think assuming a common classification space is a problem since identifying the samples within a domain is much more difficult than identifying which domain is a sample in. In other words, a common space is compatible with separated spaces, i.e., the unified classification space can be easily decomposed into domain-separated spaces but it is hard to merge independent spaces into a unified one. (2) The design of CHEEM is based on the task-incremental learning setting and I cannot see the potential of applying CHEEM in more complex continual learning settings (class-incremental, domain-incremental, online continual learning, etc.).

2. The design and the training of the proposed method CHEEM. The training of the proposed CHEEM relies on the feature mean of each layer's output. My concern is why using the mean of the features is enough to identify the similarities of different tasks but ignores other information like the (co-)variances of the features. I am very interested in how to measure the similarity of various tasks but this paper has not discussed more potential options of this. 

4. Experiment results. (1) Why does the proposed method achieve worse performance on DAD shown in Table 4? I don't recognize the performance shown in Table 5. as SOTA performance since CHEEM loses on almost all datasets except the small dataset Aircraft. I think the authors did not make a reasonable explanation of the advantages of the proposed methods in the part of the experiment.
(2) It is stated in Lines 402 to 407 that the proposed method introduces fewer FLOPs compared to L2P. I am confused about how the number of `2.2G/task' in L2P. As far as I know, the L2P method maintains a fixed-size pool and only a sequential fixed-size prompt will be appended to the MHSA at all tasks so the increase of the FLOPs is fixed rather than increased per task. And the citation of L2P is not correct in the lines.
(3) Recent works on task-incremental learning have shifted into the vision-language models (like CLIP, which also employs the ViT as the backbone) [A, B], and I encourage the authors to explore the application of the proposed method in this challenging task.
```
    [A] Z. Zheng, M. Ma, K. Wang, Z. Qin, X. Yue, and Y. You. Preventing zero-shot transfer degradation in continual learning of vision-language
models. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023
    [B] Yu J, Zhuge Y, Zhang L, et al. Boosting continual learning of vision-language models via mixture-of-experts adapters. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 23219-23230.
```
5. The paper is hard to follow and the writing can be greatly improved, especially the structure of section 2.2.

6. Lack of citation of more vision-transformer-based continual learning methods:

```
[1] Jung D, Han D, Bang J, et al. Generating instance-level prompts for rehearsal-free continual learning. Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023: 11847-11857.
[2] Tang Y M, Peng Y X, Zheng W S. When prompt-based incremental learning does not meet strong pretraining. Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023: 1706-1716.
[3] Zhou D W, Sun H L, Ye H J, et al. Expandable subspace ensemble for pre-trained model-based class-incremental learning. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 23554-23564.
[4]Zhou D W, Ye H J, Zhang D C, Liu z. Revisiting Class-Incremental Learning with Pre-Trained Models: Generalizability and Adaptivity are All You Need, arXiv 2023.
```
And related NAS-based and archi-search-based methods:
```
[5]Gao Q, Luo Z, Klabjan D, et al. Efficient architecture search for continual learning. IEEE Transactions on Neural Networks and Learning Systems, 2022, 34(11): 8555-8565.
[6]Abati D, Tomczak J, Blankevoort T, et al. Conditional channel gated networks for task-aware continual learning. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2020: 3931-3940.
[7]Rajasegaran J, Hayat M, Khan S H, et al. Random path selection for continual learning. Advances in neural information processing systems, 2019, 32.
```

### Questions
Please see the weakness above.

### Soundness
3

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
4

### Summary
This paper proposes a new model for task-incremental continual learning (TCL) by Vision Transformers. To improve the overall streaming-task performance of TCL, this work proposes a NAS-based method cooperated with a Hierarchical tasksynergy Exploration-Exploitation (HEE) sampling method, which effectively learns task synergies by structurally updating the identifed memory component. In this way, the proposed model can tackle various tasks in TCL by adaptively using reuse, adapt, new or skip strategies. The authors conduct experiments mainly on the challeging Visual Domain Decathlon benchmak, which demonstrates the effectiveness of the proposed model.

### Strengths
1. The work conducts experiments on the challenging Visual Domain Decathlon (VDD) benchmark, and obtains good results. 
2. The work proposes a new model based on NAS and MoE, which is somewhat novel in continual learning field.

### Weaknesses
1. The writing and presentation of the paper is poor. 
2. Why the authors ignore class-incremental learning in this work? Compared with task-incremental learning, class-incremental learning is more practical. Although the authors have explained some in Line 97-102, it is still confused to me. 
3. The authors show an example of learned network architecture in Figure 4, but the conclusion is not clear to me. What insights can we get from the figure?
4. Please clarify the detailed differences between the adopted Visual Domain Decathlon (VDD) benchmark and other popular ones. More importantly, why the proposed model is specifically targeted at VDD? Please clarify this from the perspective of model design.  
5. Please clarify why you choose the projection layer after MHSA. As you ilustrated in Line 199-202, please clarify this from the perspectives of forward transfer ability, forgetting, simplicity and invasive implementation. 
6. Please conduct more comparison between your proposed model and existing models. For example, the authors only compare with S-Prompts and L2P in Table 2, it is not enough at all. Furthermore, I wonder if the authors have conducted a comparison with models at the same scale of parameters.

### Questions
See the Weakness.

### Soundness
3

### Presentation
1

### Contribution
2
