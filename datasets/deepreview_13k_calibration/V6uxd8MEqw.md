# Advancing Prompt-Based Methods for Replay-Independent General Continual Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 5, 8, 8

## Abstract
General continual learning (GCL) is a broad concept to describe real-world continual learning (CL) problems, which are often characterized by online data streams without distinct transitions between tasks, i.e., blurry task boundaries. These requirements result in poor initial performance, limited generalizability, and severe catastrophic forgetting, heavily impacting the effectiveness of mainstream GCL models trained from scratch. While the use of a frozen pretrained backbone with appropriate prompt tuning can partially address these challenges, such prompt-based methods remain sub-optimal for CL of remaining tunable parameters on the fly. In this regard, we propose an innovative approach named MISA(Mask and Initial Session Adaption) to advance prompt-based methods in GCL. It includes a forgetting-aware initial session adaption that employs pretraining data to initialize prompt parameters and improve generalizability, as well as a non-parametric logit mask of the output layers to mitigate catastrophic forgetting. Empirical results demonstrate substantial performance gains of our approach compared to recent competitors, especially without a replay buffer (e.g., up to 18.39%, 22.06%, and 11.96% performance lead on CIFAR-100, Tiny-ImageNet, and ImageNet-R, respectively). Moreover, our approach features the plug-in nature for prompt-based methods, independence of replay, ease of implementation, and avoidance of CL-relevant hyperparameters, serving as a strong baseline for GCL research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors proposed a new prompt based method for general continual learning. Here they utilize forgetting-aware initial session adaption that employs pretraining data to initialize prompt parameters to improve generalizability. Additionally, they propose to use a simple non-parametric logit mask at the output layers to mitigate catastrophic forgetting. With comprehensive experiments and analysis they show the effectiveness of the method in GCL setup.

### Strengths
1. The idea of the paper is clearly presented with comprehensive experiments, ablations, and analysis. 
2. Though the paper uses concepts from other previous works the combination of the ideas and their effective implementation in the GCL setup is interesting and useful for the continual learning community.

### Weaknesses
1. The paper aims to address the challenging general continual learning (GCL) setup. However, in this setup, the classes can appear one by one and the model may need to learn one class at a time. No discussion on how to handle such a situation is presented in the paper. 
2. Though the authors presented experiment with blurry task/class boundaries, in true GCL setup the labels of the classes might not be known ahead of time. In such cases, the model needs to detect novel classes and then learn that new classes (see [1]). How the current algorithm would handle such scenarios is not discussed in the paper. 
3. The algorithm assumes the availability of the pertaining data. This is a strict constraint. In most practical cases this would not be available. For instance for large opensourced pre-trained vision, vision-language, and language models, the corresponding pretraining data is not publicly released. In the absence of any pertaining data or with very limited accessibility of pertaining data how this algorithm will perform? 
4. The paper failed to cite and/or compare with many related works. For example: [2,3,4].

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces MISA, a novel method that enhances prompt-based approaches in Generalized Continual Learning (GCL) by incorporating a forgetting-aware initial session adaptation and a non-parametric logit mask. Experiments demonstrate the proposed method's effectiveness and its ability to improve performance on three representative datasets: CIFAR-100, Tiny-ImageNet, and ImageNet-R.

### Strengths
1. The paper is well-structured and easy to understand.
2. The authors aimed to propose an effective methodology for a scenario that is closer to real-world conditions, compared to the common CL scenarios assumed by existing prompt-based CL methods.

### Weaknesses
1. The methodology appears to lack substantial novelty. The approach of using SAM for effective initialization and leveraging previously learned knowledge with masking for robustness against forgetting has been proposed and utilized numerous times in CL.

2. In the context of GCL, demonstrating the performance of a pre-trained model on natural images only with similar or closely related benchmarks weakens the paper's claims. It would be important to show that the SAM + masking with a pre-trained model approach remains strong when tested on benchmarks composed of datasets from significantly different domains, such as completely different views, 3D data, or medical imagery.

3. The scenario used in the paper is based on an already proposed (limited) GCL scenario that assumes blurry and task-free settings, which may not fully capture the (real) general scenario. I believe including experiments that reflect more realistic situations, such as not knowing the number of classes in the beginning or noisy datasets, would enhance the paper's contribution.

### Questions
Please address the concerns mentioned above in weaknesses.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents MISA, an innovative approach for tackling General Continual Learning (GCL), arguably the most challenging form of Continual Learning. They do so by starting from a pre-trained model, refined with prompts, and introducing two key components:

ISA-FAM, which is applied at the start of each learning session (essentially, at the beginning of each GCL task). This component ensures proper prompt initialization. Here, "proper" means achieving both robust generalization capabilities and mitigating future forgetting. To enhance the learning effectiveness of prompts in this phase, the authors introduce a “prompt augmentation” technique, where prompts are trained using an approach involving an MLP that is later thrown away at the end of this phase..

Non-parametric Logit Masking: similar to prior CL methods, the authors propose a session mask that preserves the final activations of classes not present in the current learning session. Since GCL involves blurred task boundaries and often lacks task identifiers, they use a unique batch-level mask designed to function universally across scenarios.

The experimental validation utilizes widely recognized CL datasets, with a particularly rich ablation analysis that provides in-depth insights into the method’s effectiveness.

### Strengths
1) The method introduced by the authors meets their claim and proves to be the SOTA in GCL;
2) the ablation section is really rich and thorough, probing deeply every aspect of the method;
3) while the components used by the authors are not exactly novel per se, their combination and the proposed modifications prove to be interesting and effective;
4) by cleverly leveraging the pre-trained data, the authors eliminated the need for a replay buffer. At the same time, they showed that the model can benefit from storing past exemplars in case it is allowed;
5) the key components of MISA are plug and play, as shown by one of the ablations (Table 5), meaning that they could work out of the box if applied on other methods;
6) The code is available in the supplementary material, which greatly helps reproducibility.

### Weaknesses
1) While it is true that a buffer is not mandatory for MISA, it still depends on the pre-train data for the ISA-FAM phase. This still poses a limitation, as the pre-train data may not be available; specifically, the method's reliance on a pre-trained model, fine-tuned with prompts, introduces a dependency on the quality and relevance of this initial pre-training data. If the pre-training dataset is not representative of the target tasks or if it is unavailable, the performance of MISA could be significantly compromised. This is a practical concern that limits the general applicability of the method.
2) the experimental section lacks the case of a completely out-of-distribution dataset. The evaluation is limited to datasets that are relatively similar to the pre-training data, which does not fully assess the robustness of the method in real-world scenarios where the data distribution can shift drastically. This is a critical gap, as the method's ability to handle such shifts is crucial for its practical use.

### Questions
1) In the ISA-FAM phase, the classification heads are trained with the prompts but later discarded (replaced by the previously trained heads) when the real learning session begins. Why is that? This way, I suppose prompts would "communicate incorrectly" with the classification heads, as the latter are replaced;
2) is there any reason why DualPrompt was selected as the prompting method? Did you consider more performing methods like Coda-Prompt[1] or HiDe-Prompt[2]?
3) you did cite [3] but not [4] for General Continual Learning, although the latter was published earlier. Is there any particular reason for this? Did you prefer the former over the latter in your GCL formulation?

[1] Smith, James Seale, et al. "Coda-prompt: Continual decomposed attention-based prompting for rehearsal-free continual learning." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023. 

[2] Wang, Liyuan, et al. "Hierarchical decomposition of prompt-based continual learning: Rethinking obscured sub-optimality." Advances in Neural Information Processing Systems 36 (2024).

[3] Pietro Buzzega, Matteo Boschini, Angelo Porrello, Davide Abati, and Simone Calderara. Dark experience for general continual learning: a strong, simple baseline. 2020.

[4] Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ales Leonardis, Gregory Slabaugh, and Tinne Tuytelaars. A continual learning survey: Defying forgetting in classification tasks. PAMI, 44(7):3366–3385, 2021.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes a prompt-based method for General Continual Learning (GCL), an incremental setting where task boundaries between consecutive tasks are not rigid, allowing certain classes to reappear in later tasks. GCL represents a challenging yet realistic scenario, as the absence of clear boundaries limits the applicability of many algorithms and techniques, particularly those relying on model expansion. The authors leverage two key strategies: (1) refining the pre-trained model’s initialization to improve resilience to distribution shifts, thereby preserving performance; and (2) using masking techniques during cross-entropy loss computation, selectively based on the classes present in each batch. Experimental results indicate strong, promising performance relative to existing solutions, complemented by extensive ablation studies.

### Strengths
- The writing is brilliant. It is a pleasure to review papers like this one.
- The idea behind FAM is noteworthy and represents the main contribution of this work.
- The experiments are extensive and cover all that is needed to understand the proposed approach.

### Weaknesses
I have only a few minor questions and suggestions.

1. While reading Sec. 4.1, I was initially puzzled by the optimization problem outlined in Eq. 2. Specifically, I questioned the advantage of fine-tuning prompts using the same data employed during pre-training. Since the gradients should be near zero around the pre-training weights, this raised some concerns about the utility of prompts. The rationale becomes clearer a few lines later; however, to improve readability, I suggest that the authors provide some context earlier in Sec. 4.1.

2. While reading Sec. 4.3, I began to wonder if FAS could also be effectively applied to standard class-incremental learning. The idea does not seem strictly constrained to the GCL setting.

3. In reviewing Eqs. 5 and 6, I noticed similarities with Meta-Learning, particularly Meta Agnostic Meta Learning (MAML). These equations suggest an optimization setup where some data is used to train the model (inner loop) and other data is used for “differentiable” evaluation (outer loop). I believe that discussing this connection in the main paper would add value, but I’d like to hear the authors' perspective on this.

4. The prompt augmentation is the only aspect that doesn’t fully convince me. Even with an MLP layer, the resulting complexity seems comparable to that of a straightforward learnable prompt. Perhaps the MLP affects the training trajectory, introducing a smoothing effect across iterations. In my experience, concatenation-based prompting strategies tend to be less effective, though this may not be due to reduced parameters or complexity. Instead, I suspect it depends on how these prompts are incorporated into the pre-trained model. I recommend that the authors test their approach with [a] as a fine-tuning strategy (i.e., using addition instead of concatenation).

5. The masking strategy used in this work is identical to that of ER-ACE (ICLR 2022). I think the paper should be more transparent about this similarity.

### Questions
See section above.

### Soundness
3

### Presentation
4

### Contribution
3
