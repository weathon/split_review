# Rethinking the Stability-Plasticity Trade-off in Continual Learning from an Architectural Perspective

- Decision: Reject
- Scores: 6, 5, 6, 3, 6

## Abstract
The quest for Continual Learning (CL) seeks to empower neural networks with the ability to learn and adapt incrementally. Central to this pursuit is addressing the stability-plasticity dilemma, which involves striking a balance between two conflicting objectives: preserving previously learned knowledge and acquiring new knowledge. Existing studies have proposed numerous CL methods to achieve this trade-off. However, these methods often overlook the impact of basic architecture on stability and plasticity, thus the trade-off is limited to the parameter level. In this paper, we delve into the conflict between stability and plasticity at the architectural level. We reveal that under an equal parameter constraint, deeper networks exhibit better plasticity, while wider networks are characterized by superior stability. To address this architectural-level dilemma, we introduce a novel framework denoted Dual-Architecture (Dual-Arch), which serves as a plug-in component for CL. This framework leverages the complementary strengths of two distinct and independent networks: one dedicated to plasticity and the other to stability. Each network is designed with a specialized and lightweight architecture, tailored to its respective objective. Extensive experiments across datasets and CL methods demonstrate that Dual-Arch can enhance the performance of existing CL methods while being up to 87% more compact in terms of parameters than the baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the stability-plasticity trade-off in Continual Learning from an architectural perspective. Its main finding is that there is a trade-off between the deep and the wide property of neural networks. In principle, the deeper networks cope better with plasticity, while wider networks cope better with stability. Furthermore, the paper also proposes a framework which makes use of distillation to improve continual learning performance on top of several baseline methods.

### Strengths
S1) The main finding (claim) (deeper networks help with plasticity, while wider networks help with stability) is, up to my best knowledge, novel and interesting.

S2) The proposed dual architecture seems to offer a fair increase in performance.

S3) Well written and easy to understand paper.

S4) The code is provided for easy reproducibility.

### Weaknesses
W1) The paper has a relatively low level of novelty as it mainly combines existing observations and techniques. Although, it seems to do all these from a novel perspective.

W2) Empirical evaluation of the main claim could have been more thorough.

W3) The paper needs a careful proofread. For instance, there are some typos: e.g., Tables 1 and 4 Captions “ANN”->”AAN”.

### Questions
Q1) Your main finding from Section 3 (deep->plasticity; wide->stability) was tested just in combination with iCaRL if my understanding is correct. This may throw some shadows on its generality. Have you considered evaluating everything in combination also with other baseline methods?

Q2) Have you considered more realistic settings with many more tasks? (considerably higher than 20)

Q3) (optional) The proposed dual architecture framework shows promise for class-incremental learning. Have you tested or considered its effectiveness also in other continual learning settings?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors demonstrate the impact of architecture of a neural network to its capability in continual learning (CL). They show that with same amount of parameters, a wider network has a higher stability and a deeper network has a higher plasticity. From this observation, they develop a CL framework featuring two networks, each with architecture adjusted to optimize one of the stability and plasticity. They showed through experiments that this framework could be used in combination with several popular CL methods to achieve enhanced performance and reduced parameter counts.

### Strengths
The basic idea of the proposed method is based on a sound and clear observation about the relation between a model's architecture and its stability/plasticity characteristics in CL tasks.

Additional experiments including ablation studies and analysis of the stability-plasticity tradeoff make a strong case.

### Weaknesses
Plasticity and stability are not static properties of an architecture. For example, throughout the continual learning process, if a model is trained more for each task, the model will appear to be more plastic. This simple observation weakens the argument of a “stability-plasticity” tradeoff at the architecture level.

Most experiments use CIFAR-100 for which the ResNet-18 architecture might be over-parameterized. This raises questions about the validity of the claimed performance and parameter efficiency improvements.

If we compare Table 2 and Table 3, we can see that the performance of ResNet18 without Dual-Arch is comparable or worse than the performance of using “Sta-Net” as a stable learner only. Thus, “Sta-Net” seems to be a more reasonable choice of baselines, especially if previous works already demonstrated that “wider and shallower networks exhibit superior overall CL performance”.

While it is likely true that Dual-Arch could improve parameter efficiency, the specific cases shown in the paper may exaggerate the differences. As in Figure 3a, performance of ResNet-18 exhibits very limited performance drop with reduction in number of parameters. This suggests that ResNet-18 is already over-parameterized for the CIFAR-100/10 task.

In the design of the Dual-Arch, only the stable learner is involved in the prediction and evaluation. What is the mechanism for this stable learner in Dual-Arch to exhibit plasticity similar to or even more than the plasticity of a single plastic learner (as shown in Figure 4c). This is intriguing because structurally, the stable learner should be less plastic; and during training, both models received the same epochs of training. It would be nice if the authors could provide some explanation.

One explanation would be that a stable learner is able to learn more from the data because it gains advantage through learning from the distilled knowledge. It seems fair to also compare the proposed method with a stable learner with twice the amount of training epochs - so we can control the total training to be same.

### Questions
The paper focuses on specific variants of ResNet, which exemplify the stability-plasticity tradeoff. It would be interesting to see if this tradeoff generalizes to other variants of ResNet or even other architectures. 

If we compare Table 2 and Table 3, we can see that the performance of ResNet18 without Dual-Arch is comparable or worse than the performance of using “Sta-Net” as a stable learner only. Thus, “Sta-Net” seems to be a more reasonable choice of baselines, especially if previous works already demonstrated that “wider and shallower networks exhibit superior overall CL performance”.

While it is likely true that Dual-Arch could improve parameter efficiency, the specific cases shown in the paper may exaggerate the differences. As in Figure 3a, performance of ResNet-18 exhibits very limited performance drop with reduction in number of parameters. This suggests that ResNet-18 is already over-parameterized for the CIFAR-100/10 task.

In the design of the Dual-Arch, only the stable learner is involved in the prediction and evaluation. What is the mechanism for this stable learner in Dual-Arch to exhibit plasticity similar to or even more than the plasticity of a single plastic learner (as shown in Figure 4c). 
This is intriguing because structurally, the stable learner should be less plastic; and during training, both models received the same epochs of training. It would be nice if the authors could provide some explanation.

One explanation would be that a stable learner is able to learn more from the data because it gains advantage through learning from the distilled knowledge. It seems fair to also compare the proposed method with a stable learner with twice the amount of training epochs - so we can control the total training to be same.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Building on the architectural design of continual learning (CL), the paper proposes that wide and shallow network layers exhibit better stability, while deep and thin networks show better plasticity. It combines these two structures using knowledge distillation, improving model performance under the same parameter count. The paper adopts specific model structures for different requirements, inspiring optimization from a fundamental architectural perspective rather than merely focusing on weight optimization. However, the experiments are all based on ResNet18, lacking validation on a wider range of model architectures.

### Strengths
This paper extends previous research by exploring the relationship between model width, depth, and model stability and plasticity. It innovatively uses knowledge distillation to combine two structures, demonstrating strong originality. Unlike most previous continual learning methods that focused on optimizing weights, this paper employs different architectures for different task requirements, inspiring optimization from a fundamental architectural perspective.

### Weaknesses
This paper does not sufficiently emphasize the limitations of previous methods and the advantages of its own approach. For instance, designing the framework based on structural characteristics. The value of the paper is not clearly highlighted. Additionally, the methods section lacks mathematical descriptions, such as the definition of continual learning and the specific loss function formulas. Moreover, the experiments are conducted only on ResNet18, lacking validation on a broader range of model architectures, such as transformers.

### Questions
1.  What is the workflow of the testing process  
2.  How is the replay mechanism implemented? 
3.  Should Table 1 indicate the original ResNet for easier reading by the audience?
4. Why is there no experiment involving Pla-Net---SatNet in the ablation study in Table 3?

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
The paper investigates the trade-off between plasticity and stability in neural networks and introduces an approach that leverages two  architectures (sta-net and pla-net) to address this balance. Experimental results across multiple datasets and various continual learning  methods demonstrate the improvements achieved with this approach, highlighting its effectiveness and potential for enhancing model performance.

### Strengths
* The paper provides an interesting exploration of the tradeoff between plasticity and stability at an architectural level under a fixed parameter count constraint. The insight that deeper networks enhance plasticity while wider networks favor stability is particularly compelling can help in designing more balanced models in the future. 
* The dual-arch model using two models one for plasticity and other for stability is simple and effective as shown in experiments on various datasets.
* The paper is clear and well-organized.

### Weaknesses
 * **Motivation and presentation.** The paper’s motivation could be strengthened. Specifically, Table 1 is challenging to interpret, as it lacks a total parameter count despite referencing it in the text. Additionally, the table format makes it difficult to assess the isolated effects of depth and width, as both vary simultaneously across rows. The updated text could benefit from a clearer reflection in terms of parameters, as the motivation behind the table is still not evident. Additionally, the broader implications of these results on other architectures, as highlighted by other reviewers, remain unclear and need further explanation.
* **Details on Hyper-Parameters:** More transparency around hyper-parameter tuning is needed, particularly for $\alpha$ and $\beta$. Various works [1,2] have emphasized the impact of hyper-parameter tuning in continual learning, and it is important to discuss the assumptions and the setup in the paper. Further, could the authors provide confidence intervals for the methods? Without error bars, it’s hard to fully justify the two-architecture approach. For example, in Table 3, the performance difference is minimal (less than a percent) compared to simply using two stable network architectures. From the additional experiments provided, it is evident that varying $\alpha$ impacts performance. This necessitates a more thorough analysis rather than relying on values from prior work, given the differences in context and methodology. Moreover, the reported mean and standard deviation suggest that the performance differences between the two sta-Net architectures, as well as between sta-Net and pla-Net, are less than 1%. This small margin underscores the need for further experiments on additional datasets to validate the conclusiveness of the results.
* **Comparison with Related Work:** The paper would benefit from a more comprehensive comparison with works [3, 4, 5] that use methods like distillation or network expansion to address similar issues in continual learning with better performance. These comparisons are essential to clarify the unique contributions of this study and position it with respect to prior works. The comparison with Heterogeneous Continual Learning was intended to evaluate the knowledge distillation adoption, which is central to the proposed method. While DER and MEMO are replay-based methods, the requested comparison with expansion-based methods was relevant as they share similarities with the proposed approach regarding the inclusion of additional parameters.

### Questions
* For KD, do you use the current dataset? 
* Can you report forgetting in Table 2 as reducing forgetting is a key focus of the work?
* Regarding the ablation studies, how are the stability (sta-net) and plasticity (pla-net) architectures trained? Specifically, how is the loss modified from Eq. (2)? Clearer details would help readers better understand Figure 4 and Table 3.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper studies the stability-plasticity dilemma in continual learning from an architectural perspective. Through empirical studies, the authors demonstrate that network architecture impacts learning dynamics: deeper networks exhibit better plasticity while wider networks show better stability. Based on this insight, they propose Dual-Arch, a method using two specialized networks with complementary strengths: a deeper, thinner network optimized for plasticity and a wider, shallower network designed for stability. The framework operates by having the plastic network learn new tasks with flexibility, then transferring this knowledge to the stable network through knowledge distillation. A key feature of Dual-Arch is its ability to serve as a plug-in component for existing continual learning methods. Through extensive experiments on class incremental learning setting, the authors demonstrate that their approach not only improves performance but also achieves significant parameter efficiency compared to baseline methods, while addressing the task-recency bias.

### Strengths
-  I found the method simple yet pretty intuitive and results look promising as well.
- Related work is comprehensive, explaining past work on forgetting and architecture (e.g., depth, width, and network components). They also cover complementary learning system-inspired works, which is highly related.
- The paper is well-written with a clear structure
- Experiments are detailed with thorough analysis of the algorithm

### Weaknesses
 - While parameter efficiency is emphasized, the approach is resource-intensive in terms of compute. The stable network requires waiting for the plastic network to complete learning, which, intuitively, should double the runtime compared to standard replay methods. Reporting runtime or FLOP counts would be helpful. Re-running the experiments and recording clock time may not be feasible during the rebuttal period. However, I would suggest the authors add at least FLOP counts and discuss whether their algorithm may end up taking more time.
- The analysis using iCaRL in Section 3 is somewhat counterintuitive. Although iCaRL is a well-established approach, it has distinctive features like knowledge distillation and prototype-based classification, which may obscure the architecture's direct impact on stability and plasticity. I would expect using a simpler, more standard algorithm, such as experience replay, to provide a clearer understanding of these effects. I don't suggest the authors try to repeat the experiments in a short period of time. However, it would be good to discuss why iCaRL was chosen beyond saying it is a classical replay method.
- Section 3’s results largely align with existing findings, such as those presented in "Wide Neural Networks Forget Less Catastrophically." So, I do not think they add much to existing knowledge.

### Questions
- Dual-Arch appears to heavily rely on ("exploit") the class incremental setup.  For instance, how does the model perform predictions within a task? And what if task boundaries are not available? Although many methods in the literature rely on this kind of information, I believe a truly continual learning model should ideally be ready to make predictions at any stage and be more robust. How could authors address these limitations? 
- In relation to the "plastic learner," did the authors consider resetting its weights periodically? Previous work, such as https://arxiv.org/abs/1903.04476 and https://arxiv.org/abs/2206.09117 suggests that resetting weights can improve model plasticity.
- Vision transformers are increasingly being used in continual learning (e.g., L2P, DualPrompt, CODA-Prompt). While these methods typically rely on frozen pretrained weights rather than directly training the architecture, I'm curious about how the insights regarding depth and width presented in this paper could transfer to vision transformer architectures. What would be the architectural implications for transformers in terms of stability-plasticity trade-off?
- Comment: Section 5.3 has a typo in "ABALATION STUDY."

### Soundness
3

### Presentation
4

### Contribution
3
