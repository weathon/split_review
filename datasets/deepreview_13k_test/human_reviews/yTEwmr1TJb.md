# Robots Pre-train Robots: Manipulation-Centric Robotic Representation from Large-Scale Robot Dataset

- Decision: Accept
- Scores: 8, 8, 8, 3

## Abstract
The pre-training of visual representations has enhanced the efficiency of robot learning. 
    Due to the lack of large-scale in-domain robotic datasets, prior works utilize in-the-wild human videos to pre-train robotic visual representation. 
    Despite their promising results, representations from human videos are inevitably subject to distribution shifts and lack the dynamics information crucial for task completion. 
    We first evaluate various pre-trained representations in terms of their correlation to the downstream robotic manipulation tasks (i.e., manipulation centricity). 
    Interestingly, we find that the ``manipulation centricity'' is a strong indicator of success rates when applied to downstream tasks.
    Drawing from these findings, we propose \textbf{M}anipulation \textbf{C}entric \textbf{R}epresentation (\textbf{\ours}), a foundation representation learning framework capturing both visual features and the dynamics information such as actions and proprioceptions of manipulation tasks to improve manipulation centricity. 
    Specifically, we pre-train a visual encoder on the DROID~\citep{khazatsky2024droid} robotic dataset and leverage motion-relevant data such as robot proprioceptive states and actions. 
    We introduce a novel contrastive loss that aligns visual observations with the robot's proprioceptive state-action dynamics, combined with an action prediction loss and a time contrastive loss during pre-training.
    Empirical results across four simulation domains with 20 robotic manipulation tasks demonstrate that \ours~outperforms the strongest baseline by 14.8\%. Additionally, \ours~significantly boosts the success rate in three real-world manipulation tasks by 76.9\%. Project website: \href{https://robots-pretrain-robots.io/}{\color{urlcolor}{robots-pretrain-robots.io}.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper first proposes manipulation centricity, a new metric for evaluating representations for robotics, and finds that it is a strong indicator of success rates in downstream robotic manipulation tasks. Building on this insight, it proposes RPM, a framework for learning visual representation for robotics from large-scale robotics dataset. Experiments in both simulation and the real world show that RPM leads to improved manipulation centricity and higher task success rate when evaluated using behavior cloning.

### Strengths
- The paper is clear and well presented
- The simulation experiments are rigorous and have a lot of diversity
- The paper presents a novel metric for evaluating visual representations for robotics, and novel findings on how to integrate robotics information (states, actions) for training better representations

### Weaknesses
- There could be more empirical analysis and intuition regarding how each loss affects manipulation centricity. Authors could explain intuitively how each loss contributes to better MC and visualize the gradcam of an encoder trained with each loss
- The paper lacks comparison to more state-of-the-art baselines, such as VIP/LIV, or object-centric pre-trained representations such as POCR/HODOR
- As I understand, the goal here is to make the representation pay attention to task-relevant regions e.g. robot and task-relevant objects. The authors have already demonstrated that this information can be obtained using SAM2. Have the authors considered directly using the masks as a form of supervision for training the representation? I think this could serve as a baseline, since RPM requires additional priveleged information that only a robotics dataset has, i.e. state and action, whereas we can generate segmentation masks for any general sources of data.
- The paper could benefit from more extensive real robot experiments

### Questions
- Why is it still necessary to attend to the manipulator region when there is already proprioception input?
- What is the evaluation protocol in the real world? How are the environments varied between training and evaluation, and what would count as a success?
- By attending the robot and task-relevant object, technically this would allow the representation to have stronger generalization capabilities. Perhaps the author should run some visual generalization experiments to find out if RPM enables better generalization.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes pre-train visual representations for robot manipulation by focusing on manipulation centricity, robot datasets (instead of human activity datasets), and auxiliary loss objectives for dynamic alignment and time contrastive learning. To measure Manipulation Centricity, they use Jaccard similarity between the binarized Grayscale CAM and SAM2’s foreground vs. background predictions. The proposed model RPM outperforms simulation and real robot tasks compared to baselines.

### Strengths
1. Detailed empirical validation across diverse tasks and simulation domains, plus real robot experiments
1. well-motivated concept of manipulation centricity with clear metrics
1. ablation studies and analysis of design choices 
1. insights about benefits of robot vs human datasets for pre-training
1. Clearly written key research questions and contributions

### Weaknesses
The work presents insights into the visual representations that focus on manipulation centricity and dynamic alignment perform better than existing approaches. However, there are certain assumptions whose implications are not clearly discussed.
1. DROID is chosen as the robot dataset of choice instead of other larger dataset in OXE.
1. RPM is a ResNet-based model instead of directly using / comparing to pretrained models like SAM2, etc.
1. The "manipulation centricity" does not seem to improve at similar scale across different simulators, with respect to success rate. 
1. A concise definition of manipulation centricity and how it is calculated should be present in the main paper, rather than existing only in appendix.

### Questions
1. What is the tradeoff between the visual realism of the simulator vs simulator-specific training required to achieve high success rate and manipulation centricity? For example, in RoboCasa, manipulation centricity seems really low compared to others.  How to compare it across simulators?

1. How does "manipulation centricity" depend on the choice of camera intrinsics and extrinsic with respect to the robot body frame?  

1. R3M has been shown to be a poor visual representation model for robotic tasks, as compared to visual datasets [1] and pretraining image distribution matters. Why none of the baselines involve vision only representation backbones for comparison?

[1] Dasari et al, 2023. An Unbiased Look at Datasets for Visuo-Motor Pre-Training, https://data4robotics.github.io/

### Soundness
3

### Presentation
4

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
This paper introduces a metric (manipulation-centricity) for assessing the ability of pretrained visual encoders to model task-relevant features for robot manipulation tasks; as well as a novel pretraining objective (RPM) that incorporates the robot dynamics information available in robotics datasets. The authors first establish a correlation between the metric they define and the success rate of policies that leverage the features generated by pretrained visual encoders. Having established a positive correlation they seek to design a pretraining objective for visual encoders and evaluate its performance on their proposed metric and the downstream policy success rates. The novelty in the pretraining objective the authors introduce is a dynamics alignment term which takes the form of the InfoNCE applied to embeddings of a sequence of state action pairs and image embeddings. This novel dynamics alignment term is combined with existing behaviour cloning and temporal contrastive terms to give the full learning objective. They apply this objective function to pretrain visual encoders for manipulation tasks and demonstrate that this pretraining objective leads to improvements on their metric and downstream task performance in both simulated and real-world experiments.

### Strengths
- The paper validates a pretraining objective for visual encoders that improves the performance of robot policy learning. 

- The paper introduces a novel metric for quantitatively analysing the features generated by visual encoders.

- The paper validates its claims in both simulated and real-world experiments.

- The paper includes analysis of the representations learnt in various approaches.

- The paper is concise and clearly presents the authors claims and results to validate these claims.

### Weaknesses
- The paper appears to focus on pretraining and freezing visual encoders while training policies on top of these encoders. It wasn't clear if they finetune all parameters on a given task (in the simulation and real-world policy learning experiments). In general, this may be relevant as policy performance can improve with finetuning of the entire architecture. I may have missed this in the paper but it would be good to see if the pretraining results include finetuning of the overall architecture on the robot manipulation task. 

- The similarity scores for the introduced metric are quite small and rely on thresholding the binarization of the Grad-Cam output. It seems like this is a good proxy for rudimentary manipulation tasks but it doesn't necessarily seem to be a metric that will generalise to more complex settings. The metric also relies on annotations or knowledge of the task relevant features within the image. 

- The pretraining dynamics alignment term incorporates chunks of state-action pairs with a history of 3 being cited as optimal. When it comes to highly dynamic tasks it is not clear how the alignment between individual images and such a history will necessarily be beneficial. For instance a single static image does not necessarily convey rich signals for dynamics (there is some signal but it is imperfect) when compared to a history of images,  aligning a state action history and a static image seems counterintuitive to me, I question whether the improvements observed are optimal relative to other methods of incorporating dynamics information. If the dynamics varied quite a lot between demonstrations on the same robot platform I question how this will effect performance. Clearly this term is working as demonstrated in the paper but I do have reservations over its usefulness and whether it is the optimal approach to incorporating dynamics information.

### Questions
Congratulations on this work and thanks for contributing it to the robot learning community. 

I wished to clarify if during policy training does the visual encoder always remains frozen and whether you finetune the entire architecture? In the first part of the paper when evaluating your introduced metric it is clear that the encoder is frozen, I wished to confirm whether this is also the case for the reported task success rates and whether you considered finetuning the entire architecture?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a representation learning approach named RPM that learns to encode images into low-dimensional states that are aligned with the proprioception state through contrastive learning. 

1. The authors showed that RPM outperforms existing learned robot representations on 20 tasks selected from 4 benchmarks. 
2. The authors proposed to use gradient heatmap as a heuristic named as "manipulation-centricity" to determine how much the learned representation contributes to the final manipulation task performance. 
3. RPM is showed to have highest manipulation-centricity than existing learned robot representations, and is evaluated with a real UR5 robot in lift, sweep and rearrange tasks.

### Strengths
1. The proposed heuristics of using gradient heatmap to indicate manipulation performance is interesting. It can be linked to existing work in visual affordance prediction. 
2. Aligning the vision representation with the robot proprio state and actions is interesting, and may encourage the model to focus more on task-relevant information. 
3. The writing is easy to understand.

### Weaknesses
1. The technical contribution is limited. The authors spent 4 pages between the introduction and experiment section to discuss their method. But, in fact, the only new technical point that the authors proposed is equation (1), which uses InfoNCE loss to bring visual features and proprio state/aciton closer. This looks hand-wavy. Even this innovation raises questions, as the proprio state/action only describe the robot trajectory but not the visual scenes. This is very likely to make the model overfit to the learned scenarios. 

2. The evaluation is questionable. RPM is evaluated on 20 tasks, 10 from MetaWorld, 4 from DexArt, 3 from RoboCasa, 3 from RoboMimic. However, these benchmarks combined include hundreds of tasks. Why just select these 20 particular tasks? Moreover, the "Can" task in robomimic is mentioned as challenging in this paper, but it is just a simple pick-and-place task of a moderate-size can. The evaluation raises serious questions about the generalization of this RPM method. 

2. Unnecessary discussion on how to use the human video datasets. The authors spend a considerable amount of efforts to explain the policy learning from human videos. But in the end, the conclusion is to not use human data. Human action data is abundant and contains rich and diverse behavior. If the authors' proposal is to not use them and use robot demonstrations, which in fact is the standard robot learning setup. I would prefer the paper to focus on the studied setting. 

3. Needs a more comprehensive ablation study. RPM is pre-trained with the DROID dataset, a large and relatively clean robot dataset, while many baselines that RPM compared against are not trained with DROID. 

4. In Table.1, HRP and VC-1 achieves better success rate than R3M-DROID, yet R3M-DROID's gradient heatmap focus more on the objects. According to the key finding, R3M-DROID shall perform better. 

4. The term "dynamics" is mis- and over-used, confusing in some sections.

### Questions
(see weakness)

### Soundness
2

### Presentation
3

### Contribution
2
