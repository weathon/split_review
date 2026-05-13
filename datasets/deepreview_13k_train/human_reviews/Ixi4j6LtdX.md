# A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation

- Decision: Accept
- Scores: 6, 5, 8, 8

## Abstract
Knowledge distillation (KD) is a technique used to transfer knowledge from a larger ''teacher'' model into a smaller ''student'' model. Recent advancements in meta-learning-based knowledge distillation (MetaKD) emphasize that the fine-tuning of teacher models should be aware of the student's need to achieve better knowledge distillation. However, existing MetaKD methods often lack incentives for the teacher model to improve itself. In this study, we introduce MPDistil, a meta-policy distillation technique, that utilizes novel optimization strategies to foster both *collaboration* and *competition* during the fine-tuning of the teacher model in the meta-learning step. Additionally, we propose a curriculum learning framework for the student model in a competitive setup, in which the student model aims to outperform the teacher model by self-training on various tasks. Exhaustive experiments on SuperGLUE and GLUE benchmarks demonstrate the efficacy of MPDistil compared to $20$ conventional KD and advanced MetaKD baselines, showing significant performance enhancements in the student model -- e.g., a distilled 6-layer BERT model outperforms a 12-layer BERT model on five out of six SuperGLUE tasks. Furthermore, MPDistil, while applied to a large language teacher model (DeBERTa-v2-xxlarge), significantly narrows the performance gap of its smaller student counterpart (DeBERTa-12) by just $4.6$% on SuperGLUE. We further demonstrate how higher rewards and customized training curricula strengthen the student model and enhance generalizability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper proposes a meta-policy distillation method MPDistill which consists of four steps. First, the teacher is fine-tuned on the task. second, the student is fine-tuned by using the task loss and the distillation loss. Third, the meta-teacher is trained to optimize the teacher's outputs and the student's representations. Fourth, a student curriculum model is trained to generate a sequence of tasks for student fine-tuning and rewards calculation. Experiments show promising results.

### Strengths
1. Using a curriculum model to learn a set of tasks for the student is interesting.
2. Comparison with different methods are reported.

### Weaknesses
1. The framework is very heavy since it consists of bi-level optimization and reinforcement learning loss. Specifically, the bi-level optimization for the meta-teacher involves nested loops, which can be computationally expensive and difficult to converge. The reinforcement learning component for the curriculum model adds another layer of complexity, potentially leading to unstable training and high variance in performance.
2. The framework consists of four steps. Some important training details are missing. For example, the exact architecture of the meta-teacher and the student curriculum model are not clearly defined. The hyperparameter settings for each step, including learning rates, batch sizes, and optimization algorithms, are not sufficiently detailed. It is hard to reproduce the results without these specifics.

### Questions
1. Meta-teacher uses a bi-optimization, which is computationally expensive. What is the training cost of the proposed method compared to the baselines?
2. The curriculum model parameters are learned via a reinforcement learning loss, which may lead to unstable training. The performance variance of the proposed method is not reported.

-----------------------------------------------------
Thanks for the authors' response. I keep my rating.

### Soundness
3 good

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
This paper studies the problem of meta-learning based knowledge distillation, where the teacher model should be tuned during distillation.
The proposed made several adjustment to this setting with teacher fine-tuning, meta-teacher learning and student curriculum learning, each of which can somehow improve the performance.
The authors conduct extensive experiments on the natural language understanding tasks and the results somehow demonstrate the effectiveness of the proposed method.

### Strengths
* The meta-learning-based knowledge distillation task is interesting and still under-explored.
* The experiments are extensive.

### Weaknesses
 * My major concern is that the paper is overall hard to follow. Specifically, in the introduction section, the authors list several challenges of MetaKD, while these challenges seems scattered and the major challenges are missed.
* The proposed method consists of several steps and the authors make several adjustment in each step. However, these adjustment seems quite straightforward, I wonder the purpose of these design and why it works.
* Concerning the detailed design of the proposed method, the meta-teacher takes hidden state representation from both the teacher and student models to generate the final output, this could be a indirect learning from ground truth labels acoress the student models. Besides the efficiency advantages, I wonder whether it is more effective to directly use the parameter-efficient fine-tuning.
* The curriculum learning has been widely studied in the literature of KD and I wonder whether it is necessary to include it in the meta-learning-based KD. The authors should provide detailed explaination on this with more ablation studies.

### Questions
* Please clearly organize the challenges and motivation of this paper.
* Concerning the detailed design of each part, what are they purposed for?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Meta-learning-based knowledge distillation methods is a family of distillation techniques in which the teacher model is taking into account the student's performance to improve its learning. This paper introduces a new meta-learning-based knowledge distillation method which:
(i) introduces a meta-teacher model with takes as input the original teacher's and student's representations and outputs improved predictions;
(ii) introduces a reinforcement learning-based “student curriculum learning" process in which the student aims to outperform the meta-teacher by training itself on a suitable set of tasks, possibly different from the task at hand.

### Strengths
This is a well-written paper that introduces a novel technique that often times gives large improvements in the student's performance. The authors have made an extensive experimental evaluation comparing their results with other distillation techniques to give convincing arguments about their claims.

### Weaknesses
— If my understanding is correct, it seems to me that the main benefits come from the  “student curriculum learning" process that exploits data points from other tasks that are in general not available to the other baselines the authors compare against and the teacher model itself. In that sense, it is not so surprising that the student model outperforms the teacher and that the improvements margins are high enough — this should probably be made a bit more explicit by the authors. (Indeed, it is known that the student-model can certainly outperform the teacher-model in scenarios it has access to more examples, see e.g., [1, 2, 3]).

— The proposed technique is somewhat involved (implementation-wise).

### Questions
I don't have any questions.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents MPDistil, a meta-policy knowledge distillation framework for language models. The motivation is to tune both teacher and student models in a collaborative way. The proposed method consists of 4 steps, teacher fine-tuning, student distillation, meta-teacher learning, and student curriculum learning. The method is compared with the state-of-the-art baselines on SuperGLUE tasks and shows advantages. In several reported results, the teacher model outperforms the original teacher models, and the student model also outperforms the original teacher models. Finally, several discussions are presented with experiments.

### Strengths
1. The paper is easy to follow, and the methodology is well-motivated.
2. The method is compared with the state-of-the-art baselines, and the method shows advantages.
3. Ablation study is provided to help understand the contribution of each design.
4. Several interesting discussions are presented.

### Weaknesses
1. Given the previous work of Zhou et al. (2021), the presented method is not very novel, since the basic idea of teaching teachers is the same.
2. The performance gain could be mostly attributed to a better teaching model. It would be better to conduct some cross-verifications by using the meta-teacher obtained in the proposed method as the teachers for other models.
3. Larger language models are encouraged to be used in the experiments to better show the value of distillation.

### Questions
1. Have you tried using the meta-teacher as the teach in the baselines?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
