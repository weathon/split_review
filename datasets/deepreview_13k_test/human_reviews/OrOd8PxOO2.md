# Universal Humanoid Motion Representations for Physics-Based Control

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
We present a universal motion representation that encompasses a comprehensive range of motor skills for physics-based humanoid control. Due to the high dimensionality of humanoids and the inherent difficulties in reinforcement learning, prior methods have focused on learning skill embeddings for a narrow range of movement styles (\eg locomotion, game characters) from specialized motion datasets. This limited scope hampers their applicability in complex tasks. We close this gap by significantly increasing the coverage of our motion representation space. To achieve this, we first learn a motion imitator that can imitate \textit{all} of human motion from a large, unstructured motion dataset. We then create our motion representation by distilling skills directly from the imitator. This is achieved by using an encoder-decoder structure with a variational information bottleneck. Additionally, we jointly learn a prior conditioned on proprioception (humanoid's own pose and velocities) to improve model expressiveness and sampling efficiency for downstream tasks. By sampling from the prior, we can generate long, stable, and diverse human motions. Using this latent space for hierarchical RL, we show that our policies solve tasks using human-like behavior. We demonstrate the effectiveness of our motion representation by solving generative tasks (\eg strike, terrain traversal) and motion tracking using VR controllers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a system to train human motion controllers that can imitate large motion datasets and be used efficiently for training tasks such as terrain navigation and vr motion following.

Key contributions:

1. Modification of PHC to learn a better motion controller.

2. A VAE like distillation process to obtain a controller and an action space that can be used efficiently for downstream tasks.

### Strengths
1. A controller that can imitate the whole AMASS dataset.

2. A wide range of tasks to verify the efficiency of the system.

### Weaknesses
1. No comparison with baselines that resemble the proposed method, e.g., Physics-based character controllers using
conditional VAEs, by Won et al or ControlVAE: Model-based learning of generative controllers for physics-based characters. by Yao et al, which also uses VAEs.

2. The main difference between the proposed system and other systems is that the proposed system is able to scale to the whole AMASS dataset while other systems are mainly doing locomotion or something similar. However, this is not well demonstrated in the downstream tasks, which are mostly just comprised of locomotion tasks in addition to some simple reaching, which the other systems can already do pretty well (maybe less efficiently?).

### Questions
1. It will be nice to showcase some scenarios where the benefit of learning the whole AMASS dataset is useful.

2.  What are the motions that PHC cannot handle?

3. I feel like the motion quality produced in the downstream tasks is suboptimal/unnatural. It will be nice to have a metric to measure the motion quality generated in the downstream task for potential future improvement for future work.

4. For the speed task (and other tasks as well, but speed task is one of the results in the ASE paper, so I will focus on this), looks like the motion quality of ASE is really bad, while the original ASE paper has pretty good motion quality (at least visually), any comment on the discrepancy?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the context of human motion representation, the paper proposes a method to create a fundamental representation of humanoid motion that can be used for humanoid control, human motion generation or motion tracking. This representation is created via two main elements: an imitation method and a physics-based learned prior.
The distillation is made through a VAE-like architecture that learns the prior R and decoder D that are then used for each downstream task to generate to generate the action.

### Strengths
- The paper is well written
- The presented goal of learning a universal human motion latent representation is very interesting, and the effectiveness on relevant downstream tasks is well presented
- The curation of the mocap training dataset for PHC (along with other modifications) increases robustness and allows fail states recovery
- The downstream tasks are relevant and show interesting use cases for the learned representation
- The ablation study is quite compelling

### Weaknesses
- Quantitative results on the VR-controller tracking task are a little bit disappointing compared to Scratch
- The references section could be cleaned up and harmonised, notably for publication conferences
- Although the writing is clear, some typos remain (e.g. Guassian)

### Questions
- In section 4.3, a failure case is described using the prior R but it is unclear to me how do we recover from it apart from restarting the task's policy learning? Does it happen often?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work provides a method to learn a universal humanoid motion prior for different downstream tasks, the prior is designed to cover a wide range of motions. The learned latent space can be used for long, stable and diverse motion generation, and also for solving tasks with natural motions. The latent is learnt by first training an imitator controller to imitate a wide range of human motions, and then learn the latent space by distilling the learned motion imitator. Results show the learned controller could generate a wide range of human motion, and outperform baselines on downstream tasks by a large margin.

### Strengths
1. The work is well-motivated, addressing the problem that motion imitator can hardly be used for downstream tasks (especially when interaction with the environment is required) and learned motion prior can not cover a wide range of human motions.
2. Method is well demonstrated with details, and most designs are well-explained. Clear ablation study also shows the effectiveness of different components. Additional implementation details and hyper-parameters are provided in the supplementary materials for the community to reproduce the results. 
3. The learned humanoid motion prior showed impressive motion imitating performance over a wide range of human motion, and also showed promising results when applying to diverse downstream tasks, including motion tracking and locomotion over complex terrains, et al.
4. The supplement videos make the difference between proposed method and baseline more comprehensive.

### Weaknesses
1. One of this work’s claims is that previous work has limited coverage of the learned latent space that can not cover the wide spectrum of possible human motion. But in Table 1, there is no comparison with ASE or CALM or Imitate&Repurpose on motion imitation performance. Though ASE, or CALM might be a bit hard to compare, Imitate&Repurpose should be reasonable to compare with. I’m not expecting it to perform better, just for completeness.
2. Though PHC+ exhibit great performance on motion imitation, it’s comparison with PHC might be a bit unfair, since one of the modification fo PHC+ is “removing” some hard-negative in the dataset, provide motion imitation result on modified dataset might be beneficial. 
3. Some content is a bit hard to read: In Figure 3, it’s quite hard to see the human motion in the Figure 3(e) row, and the title for each row is really hard to see. (Minor issue)

### Questions
1. Is the proposed method robust against methodology and dynamics changes? It would be interesting to see these results and potentially enable appling the proposed method to humanoid robots.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
