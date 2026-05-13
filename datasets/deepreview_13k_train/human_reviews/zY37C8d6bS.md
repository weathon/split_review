# Semantic Skill Extraction via Vision-Language Model Guidance for Efficient Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Extracting temporally extended skills can significantly improve the efficiency of reinforcement learning (RL) by breaking down complex decision-making problems with sparse rewards into simpler subtasks and enabling more effective credit assignment. However, existing abstraction methods either discover skills in an unsupervised manner, which often lacks semantic information and leads to erroneous or scattered skill extraction results, or require substantial human intervention. In this work, we propose to leverage the extensive knowledge in pretrained Vision-Language Models (VLMs) to progressively guide the latent space after vector quantization to be more semantically meaningful through relabeling each skill. This approach, termed **V**ision-l**an**guage model guided **T**emporal **A**bstraction (**VanTA**), facilitates the discovery of more interpretable and task-relevant temporal segmentations from offline data without the need for extensive manual intervention or heuristics. By leveraging the rich information in VLMs, our method can significantly outperform existing offline RL approaches that depend only on limited training data. From a theory perspective, we demonstrate that stronger internal sequential correlations within each sub-task, induced by VanTA, effectively reduces suboptimality in policy learning. We validate the effectiveness of our approach through extensive experiments on diverse environments, including Franka Kitchen, Minigrid, and Crafter. These experiments show that our method surpasses existing approaches in long-horizon offline reinforcement learning scenarios with both proprioceptive and visual observations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes using vision-language models (VLMs) to annotate temporally extended skills from offline datasets. Specifically, the annotation is on the latent space after vector quantization and is improved iteratively. It saves the extensive manual labeling process. The proposed method shows robust improvements over the existing state-of-the-art techniques and the authors conduct ablations on the effectiveness of VLM guidance.

### Strengths
+ The proposed method utilizes the knowledge of VLMs as accurate skill annotations to iteratively identify helpful low-level skills for various tasks;

+ The annotation from VLMs is done in discrete latent space from the codebook which improves both the learning of the codebook, and the representation of each latent;

+ The paper provides theoretical analysis to guide the algorithm designs;

+ The empirical experiments show decent and robust improvements over existing methods.

### Weaknesses
Is it possible to finetune the VLMs to achieve even higher performance since the tasks are quite different from what VLMs are typically trained on (Internet data)? And is it cost-effective to fine-tune VLMs just to label the skills?

### Questions
Is it possible to finetune the VLMs to achieve even higher performance since the tasks are quite different from what VLMs are typically trained on (Internet data)? And is it cost-effective to fine-tune VLMs just to label the skills?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The method proposes a hierarchical policy, with a high-level skill selection policy trained via offline RL. A second low-level policy trained by behavior cloning outputs the actions given the current state and selected skill. For the skill extraction, a vector quantizied VAE is trained with labels provided by a VLM.

### Strengths
- The proposed hierarchical policy is an interesting method, with promising results.
- The discretization offered by VQ-VAE enables the use of Q-Learning for the high-level skill policy while retaining the continuous output space of a low-level action policy.

### Weaknesses
 - The clarity of the text should be improved. It often is hard to parse, and the text leaves it unclear, what the intentions are. For Example:
    - The introduction leaves it unclear what the authors define as "skill"
    - The Preliminary section's formatting makes it hard to parse. The Markov Decision Process (MDP) abbreviation is never actually defined. For VQ-VAE sg() is not defined. Same for Eq. 3
    - Section 5 suddenly appears without any stated goal or context. What is it supposed to show?
    The experiment section introduction is hard to read. In the last sentence of Section Five, the text describes the following order:
    6.5 -> 6.2 -> 6.1 -> 6.4 -> 6.3. Then, it references Fig. 5, which is late in the Appendix.
    - Line 210 states Eq. 3 but actually references Eq. 1
- Figure 1 suggests the policy extraction process requires the codebook model. But the High-level policy, in my understanding, outputs a skill selection, i.e., a codebook entry. Why does it require the codebook?
- Please clarify: Is the VLM only used during training or during rollout? Follow-up Question for the Ablation 6.3: For the method without VLM, in which stages has it been left out?
- The mentioned main limitation is "proper initialization". Please explain what initialization means, as this is barely mentioned in the rest of the main text.
- Ablations regarding the VAE policy decoder are missing. In general, the architecture of the policy decoder is not clear from the paper.

The proposed method and use of VQ-VAE + VLM is interesting. However, in its current state, the paper is hard to parse. Without improvements to the text, I tend towards reject.

### Questions
- Out of interest: How many skills were identified with VLM guidance compared to those without VLM guidance?
- From my understanding, the codebook is learned self-supervised with labels provided by the VLM. Do you have any experiments in a purely IL setting? Or could you provide further motivation for the policy extraction via Q-Learning dependent on a reward function?
- For 6.4: could you provide some graphical visualization of the table? I believe this would make the claimed slower degradation more apparent.
- Does the VQ get a single frame or multiple frames to segment? How does the segmentation work? How are the initial and terminal state of a primitive skill $\bar{s}$ determined?

### Soundness
3

### Presentation
2

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
This paper proposes a novel method called VanTA (Vision-language model guided Temporal Abstraction) that utilizes Vision-Language Models (VLMs) to extract meaningful skills from offline reinforcement learning. VanTA extracts skills through an iterative process that involves initial segmentation based on VQ-VAE, followed by using VLM to assign meaning to the skills and update the codebook.

### Strengths
The paper proposes a novel method called VanTA (Vision-language model guided Temporal Abstraction) that utilizes Vision-Language Models (VLMs) to extract meaningful skills from offline reinforcement learning. It claims to overcome the limitations of existing unsupervised learning approaches or methods that require human intervention.

### Weaknesses
The experiment section lacks baselines related to skill learning among the comparisons. It is difficult to determine whether VanTA's performance is due to the proposed algorithm or simply because it uses a skill learning framework. Given that skills are learned in the form of a codebook, a comparison with [1] seems necessary, and a comparison with [2], which utilizes LLM, also appears to be needed. The ablation study, while present, does not sufficiently isolate the impact of VLM guidance, as it only compares against a non-VLM method, which does not address the core concern that the performance gain might stem from the skill learning framework itself, rather than the specific VLM-guided approach. Furthermore, the lack of comparison with [2], which also leverages language models for skill learning, makes it difficult to assess the novelty and effectiveness of VanTA's approach, particularly in how it utilizes VLMs compared to other language-guided methods.

### Questions
* The experiment section appears to lack baselines related to skill learning among the comparisons. It seems necessary to include comparison groups associated with skill learning in the baselines.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces VanTA, an approach that integrates vision-language models (VLMs) into offline reinforcement learning (RL) for sparse reward settings. The author presents a hierarchical offline RL framework, where high-level skill policy training is augmented by the use of VLMs. Specifically, VLM is queried with image pairs to identify performed skills (e.g., pulling, pushing, picking, …), and this result is incorporated into the learning process of vector-quantized variational autoencoder (VQVAE), aiming to guide the discrete latent skill space to be more semantically meaningful. Conditioned on the skill, low-level control policy is separately learned via behavior cloning. Experiments on multiple environments show the superiority of VanTA.

### Strengths
1. The research direction of grounding VLMs to manipulation and beyond represents a significant and promising area of investigation in the field.
2. The paper is well-organized and demonstrates consistent terminology usage, making it clear to readers.
3. The experimental validation is comprehensive, spanning multiple environments.

### Weaknesses
1. The primary concern is the novelty of the contribution. The concept of extracting semantic skills via VLMs and grounding them to action policies has been previously explored, as demonstrated in [1]. The authors should clearly differentiate their approach from existing work, particularly regarding their VQVAE implementation compared to [1]. While the authors claim their approach is more automated, the core idea of using VLMs for skill extraction remains similar, and it's unclear if the automation is a significant enough departure to constitute a novel contribution. The distinction between using human-labeled language descriptions versus automated semantic extraction via VLMs needs to be more rigorously justified, especially considering that recent VLMs could potentially automate the labeling process in existing methods.

2. A fundamental aspect of skill-based RL approaches is their ability to reuse extracted skills while reducing action space exploration, enabling rapid [2, 3] or even zero-shot [1] adaptation to new tasks. The paper should elaborate on the method's generalization capabilities beyond the tasks represented in the offline dataset. The current focus on single-task performance limits the impact of the work, as the potential for skill reuse and transfer is not adequately explored. The paper should address how the learned skills can be adapted to new, unseen tasks, and provide empirical evidence to support these claims.

3. The application of VLMs in this work may not fully leverage their potential. Foundation models' primary advantage lies in their domain-agnostic knowledge, which should facilitate rapid policy adaptation across diverse domains. However, the proposed method's reliance on domain-specific reward structures potentially limits its generalization capabilities. The authors should address whether policies trained on specific tasks can generalize to different tasks. The reliance on task-specific reward structures for low-level policy learning undermines the potential for domain-agnostic skill transfer that VLMs could enable.

### Questions
1. The implementation of behavior cloning (BC) for low-level policy learning (Line 229) appears to require expert demonstrations in the offline dataset. Then, how does BC-based learning achieve good performance with mixed-quality datasets in the Minigrid experiments?

2. When reading through the middle sections of the paper, I  expect the VQVAE's encoder and decoder to serve as the high-level and low-level policies, respectively. Given that the training already utilizes expert datasets and Line 159 indicates that the VQVAE's decoder is replaced with a policy decoder, the authors should justify their architectural decision to train separate high-level and low-level policies instead of leveraging the VQVAE's existing structure.

3. Given the large model size of the VLM used in this paper, I am not surprised that it outperforms other baselines. Did other baselines employ models of comparable size to the VLM?

4. Was there any specific fine-tuning or prompt engineering applied to the VLM? While Line 104 points out the limited reasoning abilities of VLMs, it appears that this paper uses them as-is without any specialized adaptation techniques.

### Soundness
3

### Presentation
3

### Contribution
3
