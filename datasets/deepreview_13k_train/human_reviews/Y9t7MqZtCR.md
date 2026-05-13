# Sparse Weight Averaging with Multiple Particles for Iterative Magnitude Pruning

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
Given the ever-increasing size of modern neural networks, the significance of sparse architectures has surged due to their accelerated inference speeds and minimal memory demands. 
When it comes to global pruning techniques, Iterative Magnitude Pruning (IMP) still stands as a state-of-the-art algorithm despite its simple nature, particularly in extremely sparse regimes.
In light of the recent finding that the two successive matching IMP solutions are linearly connected without a loss barrier, we propose Sparse Weight Averaging with Multiple Particles (SWAMP), a straightforward modification of IMP that achieves performance comparable to an ensemble of two IMP solutions.
For every iteration, we concurrently train multiple sparse models, referred to as particles, using different batch orders yet the same matching ticket, and then weight average such models to produce a single mask. 
We demonstrate that our method consistently outperforms existing baselines across different sparsities through extensive experiments on various data and neural network structures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
SWAMP (Sparse Weight Averaging with Multiple Particles) is a new pruning method that enhances the performance of sparse neural networks by averaging multiple models trained with different stochastic gradients but sharing an identical sparse structure, known as a "matching ticket." This process results in improved generalization due to the creation of flat minima and maintains the important linear connectivity between successive solutions, a key strength of the traditional Iterative Magnitude Pruning (IMP) method. SWAMP has demonstrated its ability to outperform other pruning baselines across various datasets and network structures. The technique's success invites further theoretical investigation into why the convex hull of the weight space of these averaged models forms a beneficial low-loss subspace, which could provide deeper insights into the algorithm's effectiveness.

### Strengths
- The motivation behind SWAMP is firmly rooted in robust theoretical frameworks, notably the lottery ticket hypothesis and the concept of linear mode connectivity.
- The visualization of the loss landscape in Figure 2 provides a clear illustration of the methodology and supports the validation of the claims made.
- It is clear from the evidence presented in Table 4 that SWAMP is adept at identifying more effective pruning masks.
- Table 2 and 3 demonstrate that SWAMP achieves superior classification accuracy for a designated target sparsity level.

### Weaknesses
 - The study's reliance on demonstrating the process primarily through wide networks such as WRN and VGG-19, which are not the most parameter-efficient architectures, raises questions about the choice of models. An explanation of why these particular, potentially less efficient, models were selected for this research is needed.

- The improvement in accuracy provided by SWAMP over IMP is modest, as shown in Tables 2 and 3, and this increment is even less pronounced for the ResNet model as evidenced in Table 3. This calls for a discussion on the significance of the marginal gains achieved by SWAMP, particularly when benchmarked against other models.

- The feasibility of achieving an optimal sparse structure with SWAMP, especially for pre-trained models which are commonplace, may entail significant computational costs. It is imperative that the authors address the computational overhead, both in terms of space and time complexity, and the practical constraints when applied to large models, including Transformers. A comprehensive discussion on the limitations is warranted, given that IMP—the foundation of SWAMP—may have its own constraints with larger models.

- The applicability of the proposed method to architectures like Transformers needs clarification. In Table 8, the RoBERTa model exhibits a noticeable performance drop even with less than 50% sparsity. The question arises as to whether this decline is attributed to the inherent limitations of IMP, on which SWAMP is based, or if it pertains to the broader challenges of applying pruning techniques to RoBERTa. Additionally, it would be beneficial to understand whether the principles behind SWAMP remain valid for other models, such as GPT-like architectures, and how they compare with alternative pruning strategies for these models.

### Questions
Please refer to Weakness comments

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose weight averaging of sparse models trained from a checkpoint of a single model, in many ways "model soups" for Iterative Maginitude Pruning (IMP). The authors motivate the method for IMP as as model soups in the dense context are, with the loss landscape perspective: we know that LTs lie within the same loss basin, and might expect that weight averaging would find a better generalizing solution. Experiments demonstrate that the approach identifies solutions within a flatter region of the loss basin, and improved generalization over IMP and many other sparse training methods for CIFAR-10/100 and ImageNet models.

### Strengths
* The paper is overall well-written, with a good organization, clear writing for the most part, and a clear methodology.
* The experimental analysis is appropriate, using reasonable datasets and models (except VGG), and demonstrates clear knowledge of the sparse training literature appropriate to the methodology.
* The paper has a clear and well defined motivation: the method is motivated as cheaper than ensembles, much along the same lines of the model soups paper and how it is motivated for dense training.
* The loss landscape analysis also originally used in model soups is clearly applicable to the sparse domain, especially since much of the linear-mode connectivity methodology comes from the sparse literature to begin with.
* Hessian Trace analysis also provides some signal that the loss-landscape motivation for weight averaging holds in the sparse realm.

### Weaknesses
 * The method comes down to applying the model soup paper to sparse training/IMP. I believe there is sufficient novelty in applying a method only shown on dense training and not necessarily repeatable in the sparse training context, never mind the extensive analysis shown by the authors in this work. Saying that, it's also not the most novel research direction out there compared to many papers.
* As presented in the main body of the paper, SWAMP is *much* more expensive than most of the compared sparse training methods in e.g. Table 2 at *training time*. This is because IMP with weight rewinding is extraordinarily expensive in practice. However, the authors do demonstrate that the SWAMP methodology applies to other much more efficient sparse training methods in the appendix, notably RiGL, a state-of-the-art sparse training method, and one that is reasonably efficient. I believe the authors should focus their method as being widely applicable to sparse training methods in the main body of the paper, rather than focusing on IMP however - this is especially important given the motivation that SWAMP is better than training an ensemble (which is in fact likely cheaper than SWAMP when using more practical sparse training methods than IMP!).
* While CIFAR-10/100 results are relatively strong, the ImageNet results (Table 3) are relatively quite weak and not as obviously significant.

### Questions
* While the paper is motivated by comparing the generalization of a SWAMP to an ensemble of two IMP solutions, what is the comparison in generalization when using other sparse training methods, e.g. RiGL, given that these other methods often generalize better than IMP?
* Is there any reason to believe SWAMP is not a general method that applies to any sparse training method? If so what? If not, why focus on IMP?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a modification to the Iterative Magnitude Pruning algorithm, SWAMP. The basis of this algorithm is the empirical evidence that different models trained from the same matching tickets can be weight averaged without encountering a loss barrier post certain sparsity levels. SWAMP obtains marginal accuracy improvements with respect to the baselines used.

### Strengths
S1. The manuscript is well written

S2. The method is empirically sound and arguments are well made.

S3. Extensive empirical is provided to justify the merit in this approach.

### Weaknesses
W1. The authors have not empirically justified their choice of using Stochastic Weight Averaging (SWA) as opposed to SGD in the manuscript. It would be important to understand the impact of SWA on the proposed approach by demonstrating two things.
1. How does IMP perform when it uses SWA as opposed to SGD.
2. How does SWAMP perform when it uses SGD as opposed to SWA.

W2. Multiple instances of imprecise statements. For example, "As illustrated in Figure 1, our algorithm achieves superior performance, which is on par with that of an ensemble consisting of two sparse networks." It is not clear with respect to what are the authors claiming superior performance? Because in Figure 1, IMP-3 outperforms SWAMP in terms of accuracy.

### Questions
Q1. I would like to understand why is it that the authors choose to average the weights in SWAMP? As demonstrated in Figure 1, there might be individual IMP runs that outperform SWAMP. Why not take the best of multiple pruned weights?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends the Iterative Magnitude Pruning (IMP) technique by proposing an approach called SWAMP that trains multiple sparse models called particles in each magnitude pruning iteration of IMP using Stochastic Weighted Averaging (SWA) optimization. The particles in each pruning iteration exhibit the same matching ticket and their diversity is achieved through different batch orders. The trained particle masks are combined in the weighted average fashion to get the single mask of a given pruning iteration. This process of training multiple particles followed by the weighted average of their mask is repeated until desired sparsity or pruning iteration is achieved. The experimentation is conducted on multiple datasets along with different architectures to showcase the effectiveness of the proposed SWAMP model.

### Strengths
* The authors have done a great job in terms of summarizing their contributions compared to the IMP technique in Section 3.2. 
* The paper is very easy to read and the proposed contribution can be easily understood through Algorithm 1.
* Extensive experimentation is conducted on multiple tasks (vision and language), multiple datasets, and multiple architectures. 
* A very comprehensive ablation study is conducted to showcase the effectiveness of the proposed components in the paper. For example, Table  5 clearly shows the importance of the SWA optimization along with the weighted average mechanism of the particles to enhance the performance.

### Weaknesses
 * In terms of methodology, the proposed technique provides an empirically guided straightforward extension over the IMP technique. The proposed SWAMP therefore has a trivial contribution and therefore lacks novelty.
* In terms of experimentation, the performance gain over other techniques seems to be marginal and  reduces the significance of their proposed methodology. 
* In Figure 3, for relatively lower sparsity (e.g., sparsity of 20%), the proposed Weighted Average (WA) technique seems to underperform the individual particle performance. Does this mean, the proposed technique  harm the performance on the lower sparsity? The authors may need to provide more extensive justification to explain this phenomenon.

### Questions
In Figure 3, why does the proposed technique have a lower performance compared to individual particles in the lower network sparsity?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents SWAMP, a novel method using the average of multiple particles' stochastic weight averaging (SWA) to achieve improved model performance. The authors have tested SWAMP’s effectiveness across various tasks, including vision models (CNNs) and language models (RoBerTa finetuning), providing a comprehensive evaluation.

### Strengths
1. The paper is well-written, and easy-to-follow.
2. The authors have conducted extensive experiments, covering vision tasks and language model fine-tuning. Additional studies such as mask analysis and efficient implementation SWAMP+ are also provided.

### Weaknesses
While the authors address the computational efficiency of SWAMP+ in section 4.3, stating that it can utilize a single particle for the first few iterations, this claim seem to work because the networks are already very sparse. My concern lies in the computational cost of SWAMP+ at lower sparsity levels. Furthermore, did the authors test SWAMP+ on ImageNet?

See also my questions.

### Questions
1. The results in Figure 4 show that interpolated weights yield even lower errors compared to IMP weights. Could the authors provide a detailed explanation or hypothesis as to why this is the case?
2. Appendix B states, "The learning rate for this phase (SWA phase) is set to a constant value of 0.05." Does this imply that the minimum learning rate is set at 0.05 for SWAMP, and for other baselines such as IMP?
3. Do IMP and SWAMP use the same epoch T_0 to rewind weights?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
