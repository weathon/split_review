# UniGEM: A Unified Approach to Generation and Property Prediction for Molecules

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Molecular generation and molecular property prediction are both crucial for drug discovery, but they are often developed independently. Inspired by recent studies, which demonstrate that diffusion model, a prominent generative approach, can learn meaningful data representations that enhance predictive tasks, we explore the potential for developing a unified generative model in the molecular domain that effectively addresses both molecular generation and property prediction tasks. However, the integration of these tasks is challenging due to inherent inconsistencies, making simple multi-task learning ineffective. To address this, we propose UniGEM, the first unified model to successfully integrate molecular generation and property prediction, delivering superior performance in both tasks. Our key innovation lies in a novel two-phase generative process, where predictive tasks are activated in the later stages, after the molecular scaffold is formed. We further enhance task balance through innovative training strategies. Rigorous theoretical analysis and comprehensive experiments demonstrate our significant improvements in both tasks. The principles behind UniGEM hold promise for broader applications, including natural language processing and computer vision.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a unified model for molecular generation and property predictions. Since diffusion models require diffusing the 3D molecular conformers to a collapsed state, the molecular structures in the early time steps do not contain any meaningful structural information. As a result, the joint training of generation and property prediction can be inconsistent in the early stage. The author develops a theoretical framework to explain this issue. To solve this issue, this paper proposes a novel training paradigm that separates the diffusion time steps into two stages, which are nucleation time and growth time. The joint training would only be conducted during the growth time. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
(1) The presentation of the major idea is very clear. This reviewer can understand the motivation fluently through reading the introduction part. This article is well-organized and easy to follow; 

(2) The theoretical analysis is well-developed and can explain the tradeoff phenomenon properly.

### Weaknesses
(1) It appears that the nucleation time cannot be determined prior to training the diffusion models. This could prove to be highly costly if there is a need to repeatedly retrain the diffusion models with varying hyperparameters, which may be impractical in real-world applications;

(2) While the theoretical framework is well-developed, this reviewer believes that the theoretical analysis section occupies an excessive portion of the paper. Given that the phenomenon observed by the authors is quite intuitive, experimental observations or straightforward explanations could suffice;

(3) Although the experimental results demonstrate the effectiveness of the proposed method, UniGem only marginally outperforms the baseline methods across most datasets and tasks. Furthermore, the molecular generation benchmark is not entirely convincing at this stage, as the evaluation metrics used in this benchmark fail to distinguish the capabilities of various state-of-the-art generation models. Also, in the molecular quantum property prediction benchmark tasks, UniGem only slightly surpasses the baseline models, and many quantum properties are absent from the reported benchmark results. Overall, the current empirical results do not sufficiently convince readers of the superiority of the proposed method;

(4) The novelty is a little bit limited from the algorithmic contribution side. The major contribution is splitting the diffusion training into two different stages and only conducting the joint training in the later stage. This is somehow not that significant in more general application domains.

### Questions
How do you determine the nucleation time before training diffusion models? Currently, it seems that the nucleation time cannot be determined before training the diffusion models. This gonna be extremely costly to select the most suitable nucleation time.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes UniGEM, a unified method designed to effectively address both molecular generation and property prediction tasks. Experimental results and ablation studies demonstrate the effectiveness of the proposed approach.

### Strengths
1. The paper presents an innovative and well-reasoned approach. Denoising has recently emerged as a dominant pre-training method for molecular representation learning, with strong physical interpretability. Combining the diffusion model with representation learning is a promising direction and good first trial.

2. Decoupling atom type and coordinates during generation is an interesting approach. Together with theoretical insights, this approach shows promise in reducing generation error. This technique resembles some protein generation models, where pure chain geometry is initially learned before predicting amino acid sequences.

3. Experiments validate the efficacy of the proposed framework.

### Weaknesses
1. The experimental setup lacks depth. To better demonstrate the effectiveness of the proposed method, I suggest testing on a property-conditioned generation task using the QM9 dataset, a standard benchmark for generative models. This would offer a more challenging evaluation, testing both the model’s ability to learn representations related to specific conditions and its capacity to capture the underlying data distribution—goals that align very well with the proposed method’s objectives.

2. The comparisons lack recent SOTA methods. It would be valuable to compare UniGEM’s performance in prediction tasks against other pre-trained methods that also leverage denoising, such as UniMol or Frad (I understand that the model backbones differ, yet this comparison could at least shed some lights). This will test whether UniGEM’s approach (i.e., diffusion-based denoising, with larger noise levels and more fine-grained steps) offers advantages over conventional coarser denoising techniques in representation learning.

### Questions
No further questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes UniGEM, a unified approach for molecular generation and molecular property prediction. The authors carefully designed both generative and predictive objectives in a single unified framework. Interestingly, these two objectives exhibit a synergistic relationship, enhancing each other's performance.

### Strengths
- The problems of interest, molecular generation and property prediction, are important for real-world applications, e.g., drug discovery.

- Proposed method seems reasonable; (1) applying the predictive and atom type loss near t=0, (2) changing atom type loss to classification loss, and (3) learning only coordinates when t is far from 0.

- The findings are interesting; simultaneously learning both predictive and generative objective improve each other's performance.

### Weaknesses
 - Insufficient baselines.

My major concern is the omitted baselines. For example, [1,2,3] also study 3D molecular generation and often outperform this method. I think such 3D molecular generation baselines should be in main tables for comparison.

---
- Marginal improvements.

Considering the omitted baselines [1,2,3], the improvements seem marginal for me. Furthermore, it seems that [3] largely outperforms this paper. 

---
- Complexity of the framework.

UniGEM introduces many design choices, e.g., t_n and oversampling ratio. I think this may limit the generalizability to other datasets, i.e., require extensive hyper-parameter tuning.

### Questions
1. How much time does it take the overall training?

2. Can EGNN be replaced by recent 3D GNNs, e.g., [4], to further improve performance?

3. Can the authors provide visualizations of the denoising process for generated samples?

[4] Liu et al., Spherical Message Passing for 3D Molecular Graphs, ICLR 2022

### Soundness
3

### Presentation
3

### Contribution
2
