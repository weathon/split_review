# EraseDiff: Erasing Data Influence in Diffusion Models

- Decision: Reject
- Scores: 6, 6, 3, 8, 5

## Abstract
In response to data protection regulations and the ``right to be forgotten'', in this work, we introduce an unlearning algorithm for diffusion models. Our algorithm equips a diffusion model with a mechanism to mitigate the concerns related to data memorization. To achieve this, we formulate the unlearning problem as a bi-level optimization problem, wherein the outer objective is to preserve the utility of the diffusion model on the remaining data. The inner objective aims to scrub the information associated with forgetting data by deviating the learnable generative process from the ground-truth denoising procedure. To solve the resulting bi-level problem, we adopt a first-order method, having superior practical performance while being vigilant about the diffusion process and solving a bi-level problem therein. Empirically, we demonstrate that our algorithm can preserve the model utility, effectiveness, and efficiency while removing across two widely-used diffusion models and in both conditional and unconditional image generation scenarios. In our experiments, we demonstrate the unlearning of classes, attributes, and even a race from face and object datasets such as UTKFace, CelebA, CelebA-HQ, and CIFAR10. The source code of our algorithm is available at https://github.com/AnonymousUser-hello/DiffusionUnlearning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**POST REBUTTAL NOTE FOR AUTHORS:**

I would like to thank the authors for patiently answering my questions and acknowledge that I have read their responses. 

--------------------------------------------------

**PRE REBUTTAL REVIEW:**

This paper tackles the privacy issue with respect to the generations of diffusion models. Diffusion models, pose significant privacy risks as they can memorize and regenerate individual images from their training datasets and this paper aims to propose an unlearning algorithm. The setup considers access to a pretrained diffusion model as well as the "forgetting data"(data to be forgotten) and the "remaining data" (data which needs to be modeled correctly in the diffusion model). 

EraseDiff casts this problem to a bi-level optimization problem that fine-tunes the model with the remaining data while deviating the generative process to erase the influence of the forgetting data.

### Strengths
- EraseDiff introduces a new approach to data unlearning in diffusion models.
- The method is more efficient than retraining the entire model, but requires more comparison in terms of other recent baselines in the literature.
- The paper provides extensive empirical evaluations, comparing with existing unlearning algorithms for neural networks.
- The technique can be applied to both conditional and unconditional image generation tasks.
- The paper grounds its methodology in a solid theoretical framework

### Weaknesses
 - I understand the assumptions made in the paper are that we do have access to $\mathcal{D}_r$. However, is this a reasonable assumption for large scale diffusion models? Often times, we have access to a pre-trained diffusion model and also to the forgetting data ($\mathcal{D}_f$) but assuming access to $\mathcal{D}_r$ which may be very large might not be reasonable. Have the authors thought about the case where we do not have access to the remaining data? How does the algorithm change? Is there significant impact on the results?

- The impact of unlearning seems to have affected the samples quality significantly. 
- The assumption in the methodology that they access to $\mathcal{D}_r$, hinders the use of the algorithm for large scale diffusion models such as Stable Diffusion. 

See my questions below.

### Questions
- There is no definition of the hyper-parameter $\lambda$. Does it control the balance between retaining and forgetting data?

- Authors have missed important citations: [2] and [3].

- Can the authors clarify on the connections and similarity of their work compared to [1], [2] and [3]? From my understanding, [1] also fine-tunes the score network to minimize the generation probability of samples that can be labeled as a specific class. Also in [2] and [3] authors propose similar approaches for removing concepts. I believe the claim made in the introduction about this work being the first to study unlearning in diffusion models is incorrect. 

- A believe it would be nice to be able to compare your method against Selective Amnesia [2]. In Table 1 of [2] there is results on CIFAR10  and the FID on the remaining classes seems to be much lower (9.08) than what you have reported in Table 2 (seems to be on average above 20). I would appreciate it if the authors provide more comparisons or clarifications with respect to [2]. 

- The texts on Figure 3 are not easily readable. What is the y axis (frequency)? How do we interpret this plot?

I am willing to modify my score once the results and comparisons with existing baselines in the literature are clarified.  


[1] Rohit Gandikota, Joanna Materzynska, Jaden Fiotto-Kaufman, and David Bau. Erasing concepts from diffusion models. arXiv preprint arXiv:2303.07345, 2023.

[2] Heng, Alvin, and Harold Soh. "Selective Amnesia: A Continual Learning Approach to Forgetting in Deep Generative Models." arXiv preprint arXiv:2305.10120 (2023).

[3] Gandikota, R., Orgad, H., Belinkov, Y., Materzyńska, J., & Bau, D. (2023). Unified concept editing in diffusion models. arXiv preprint arXiv:2308.14761.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a bi-level optimization approach for the unlearning of diffusion models. Specifically, the inner objective focuses on data sanitization, while the outer objective seeks to retain the utility of the diffusion model with respect to the retained data. Moreover, the proposed technique is versatile, accommodating both conditional and unconditional image generation. Its effectiveness has been demonstrated across several datasets, including UTKFace, CelebA, CelebAHQ, and CIFAR10.

### Strengths
1. Assess the performance of the unlearned model using a diverse set of metrics to capture multiple perspectives. These metrics include the Fréchet Inception Distance (FID), accuracy (Acc), Membership Inference Attack (MIA), Kullback-Leibler (KL) distance, and weight distance.
2. Examine the effectiveness of the proposed approach across several datasets: UTKFace, CelebA, CelebAHQ, and CIFAR10.

### Weaknesses
The proposed method primarily focuses on class-wise unlearning and may have limitations when applied outside this specific context (e.g., nudity removal, artistic style removal).

### Questions
How effective is the unlearning process when subjected to adversarial attacks?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the development of an algorithm called EraseDiff, which aims to address the privacy risks and data protection regulations associated with diffusion models. These models, known for their high-quality output and ease of use, pose concerns related to privacy, memorization of training data, generation of inappropriate content, and potential violation of data ownership and copyright laws. The proposed algorithm formulates unlearning as a bi-level optimization problem, with the goal of scrubbing the information associated with forgetting data from diffusion models without the need for retraining the entire system. The algorithm is evaluated in various scenarios, including the removal of classes, attributes, and races from different datasets, and it demonstrates improved performance compared to baseline methods.

### Strengths
1. This paper focuses on a crucial question: the issue of privacy within the diffusion model.

### Weaknesses
1. The formulation of the diffusion model unlearning problem in this work seems unconventional. Both the inner and outer objectives aim to optimize the model parameters. As such, it can be naturally defined as a multitask problem. One task seeks to preserve the utility of the diffusion model for the remaining data, while the other aims to eliminate the information related to the data slated for removal.

2. The inner objective of this work strives to make the diffusion model incapable of generating meaningful images corresponding to C_f. The rationale behind defining sample unlearning in this manner is unclear. A more intuitive approach would be to ensure that the model, when trained with both the remaining and the forgetting data, has parameters equivalent to those obtained when trained solely on the remaining data after the unlearning process.

### Questions
N/A

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper propose the first(up to their knowledge) unlearning algorithm for diffusion models in order to let the models learn to erase the learning effects by some specific training data and still remember the distribution of other training data, without retraining the models from scratch. Such algorithm help protect privacy, prevent misuse, mitigate or erase bad impact by some undesirable training data but preserve model utility with respect to remaining training data.

### Strengths
1. This paper proposes a new strategy to finetune diffusion model to eliminate effects of some training data.
2. This includes experiments comparing the effectiveness of their model on both label-conditional and unconditional diffusion models, showing that by the algorithm provided, a pretrained model can actually forget designated data and preserve the rest. 
3. Problem addressing, motivation, method(learning objective design and finetune pipeline), experiments are clear.
4. This paper demonstrate efficacy and efficiency to scrub diffusion model and such contribution can be significant if more and more privacy concerns are addressed on those generative models.

### Weaknesses
The evaluation is based too much on image label, which might only be a small subset of the potential problem cases. 
For class conditional diffusion model, it makes sense to run the finetune algorithm to forget all training images for specific class, it is like a reverse-process of few-shot learning. 
For unconditional diffusion model, the training data still provide image class(but diffusion model is not able to access label during training or testing). Then, by erasing some all data from a specific class, the diffusion model does not actually "forget well" about those data. Such case is severe especially for alike classes, and for human face dataset like CelebA. Most importantly, if the elements in forgetting subset do NOT share enough common property(for example, a photographer want you to erase all photos she took, but those photos are of huge variety with many semantics, despite "her special style" can be labeled, this is often not a label available in original model training), in that case, it is hard to evaluate how good the model forgets such subset.

### Questions
Suggestions:
1. Design more experiment(and have more discussion) on random(or not so well-labeled) subset, demonstrate model efficacy.
2. Evaluating unconditional diffusion model utility with respect to specific sub-dataset can be hardly well-defined, so try to narrow-down and specify the problem you want to tackle in a more guided way(such as to only some specific conditional diffusion model).
3. Try more types of condition(or context).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an unlearning algorithm for diffusion models in order to mitigate the concerns about data memorization. With the goal of scrubbing the information for certain classes, this paper proposes to maximize the variational bound on the sub-dataset under those classes while also minimizing the objective function on the remaining data.  To solve the constrained optimization, the author proposed to view it as a bi-level optimization and perform maximization and minimization alternatively to erase the information while maintaining the model quality. The proposed method is simple and effective, as demonstrated by numerical experiments. My major concern is that the practical performance fails to outperform in both forgetting and remaining classes. The author may claim their method achieves a better tradeoff, which is not fully supported by the experiments and could be subjective. It would be better to demonstrate some kind of “optimality” either theoretically or empirically to back up this simple idea.

### Strengths
The idea is simple and effective. The effectiveness is shown via numerical experiments, where the proposed method achieves an arguably better tradeoff between forgetting some certain classes and remaining to perform well in other classes.

### Weaknesses
Is there a theoretical guarantee to do the optimization alternatively? It seems not necessary in this setting, as we may do it completely in a separate way, i.e., do the maximization first to completely scrub the forgetting classes and then fine-tune to make up the performance on the remaining dataset. Which way would be better, and why?

We also see a drop in the quality of generated figures from Table 2, and the proposed model is worse than finetune from Table 3.

### Questions
Minor typo: page 3, “the variational bond” above equation (1).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
