# Bridging the gap between offline and online continual learning

- Decision: Reject
- Scores: 6, 3, 5, 3

## Abstract
Instead of training deep neural networks offline with a large static dataset, continual learning (CL) considers a new learning paradigm, which continually trains the deep networks from a non-stationary data stream on the fly. Despite the recent progress, continual learning remains an open challenge. Many CL techniques still require offline training of large batches of data chunks (i.e., tasks) over multiple epochs. Conventional wisdom holds that online continual learning, which assumes single-pass data, is strictly harder than offline continual learning, due to the combined challenges of catastrophic forgetting and underfitting within a single training epoch. Here, we challenge this assumption by empirically demonstrating that online CL can match or exceed the performance of its offline counterpart given equivalent memory and computational resources. This finding is further verified across different CL approaches and benchmarks. To better understand these counterintuitive experimental findings, we design a framework to unify and interpolate between online and offline CL and provide a theoretical analysis showing that online CL can yield a tighter generalization bound than offline CL.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Online continual learning is considered much more challenging than offline continual learning due to the combined challenges of catastrophic forgetting and underfitting due to a single pass. This paper presents a unified framework to combine online and offline continual learning. It demonstrates that online continual learning becomes more performant than offline CL when both use the same memory and compute. It proposes a long-short-term memory based framework to unify online and offline CL paradigms. It presents a theoretical study on the generalization bound on online and offline CL.

### Strengths
This paper proposes a unified framework combining online and offline CL to achieve the best of two worlds i.e., online CL improves stability and offline CL improves plasticity.

It studies stability-plasticity tradeoff in online and offline CL and the impact of sequence length, buffer size and task size on their performance.

It presents generalization bound analysis using a proposed unified framework and ties it with memory allocation policy. And it presents theoretical justifications for why online CL performs superior to offline CL in various specified settings.

The experimental results on various benchmark datasets demonstrate that online CL outperforms offline counterparts when they both use the same compute and memory.

### Weaknesses
Although combining online and offline CL is interesting, using the same memory and compute for online CL as used by offline CL makes both computationally expensive. Online CL uses many more iterations at each timestep to match offline CL’s compute overhead. Thus online CL becomes ill-suited for many real-world applications e.g., on-device learning where fast adaptation / speed is critical. Online CL’s performance gains are mostly attributable to higher compute (more SGD updates) and memory usage.

This paper defines online CL based on batch learning i.e., learner receives a batch of new data and makes multiple iterations where each iteration combines a new batch with a sampled batch of old data from the buffer. This becomes very similar to offline CL with larger batch size. A more realistic online CL can be defined such that an online learner learns new data sample-by-sample manner (instead of batch-by-batch) using a single training iteration that combines a new sample with a batch of old data. This is much faster than the former definition and suitable for real world applications where speed matters. Another difference is the number of times each new sample is seen by the learner. Unlike the latter definition, the former one allows the model to see each new sample multiple times which is not truly a single pass (core ingredient of online CL).

I am not convinced that single pass causes underfitting and online CL requires multiple iterations at each timestep. Underfitting originates from specific design choices for example training from scratch where online CL model is randomly initialized and struggles due to lack of an optimum initialization (pre-training on a subset of data). There are methods that do not exhibit underfitting. An example of such a method is REMIND [1] that performs a base initialization using a subset (10% of ImageNet). REMIND performs online continual learning in sample-by-sample manner at each timestep with one SGD step / iteration on a mini-batch consisting of one new data and several old data. REMIND achieves competitive accuracy to the offline variant.

Although this paper presents valuable insights and observations, the proposed framework focuses mainly on how to balance memory and compute between online and offline CL. It does not propose any specific mechanisms to mitigate catastrophic forgetting, enhancing stability and plasticity and underfitting issues (when present due to design choices). It lacks sufficient scientific contributions.

It is unclear how much each online and offline CL model forgets due to absence of offline upper bound (jointly trained on all data).

[1] Hayes et. al., “Remind Your Neural Network to Prevent Catastrophic Forgetting”, In ECCV, 2020.

[2] Yasir et al., “A Real-time Evaluation in Online Continual Learning: A New Hope”, In CVPR 2023.

### Questions
Why do we need a unified framework combining online and offline CL from real-world application perspectives?

What is the offline upper bound (jointly trained on all data) which shows how much online CL / offline CL model forgets?

How practical is the online CL when using the same compute and memory as offline CL? Can this online CL keep up with the speed of data stream as described in this work [2]?

How does the proposed unified framework perform when a learner receives and immediately learns a single data point at each timestep i.e., sample-by-sample manner?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work tries to bridge the gap between offline and online continual learning. It corrects the memory sizes and computational budgets to bridge this gap:

1) Issue in Memory: 
- Offline CL – $M_{offline}$ has access to all samples of this task along with memory size of M, O(|M| + |$C_{task}$|)
- Online CL – $M_{online}$ stores has access to only the incoming batch along with memory size of M, O(|M| + |$C_{batch}$|). 
- where $C_{batch}$ << $C_{task}$
- (Note: It’s not just |M| as claimed)

**Correction**: |$M_{online}$| = |$M_{offline}$ + $C_{task}$ - $C_{batch}$|

2) Issue in Computation:
- Offline CL approaches uses far more computation compared to Online CL methods! 

**Correction**: Equalize both offline and online CL methods to use the same computational budget C.

*Experiments*: In Section 3.3 and 6, the paper shows that once both corrections are implemented, online continual learning methods outperform offline continual learning methods.

3) Then, the work focuses on interpolating between |$M_{offline}$| and |$M_{online}$| with short-term and long-term memories.

- Short-term memory ($M_{short}$) : FIFO ordering (stores last |$M_{short}$| samples), emptied at each task boundary.
- Long-term memory ($M_{long}$): Stores the latest sample ejected from the short-term memory by reservoir sampling mechanism.

They start with a theoretical analysis, showing effects and results obtained from minimizing discrepancy. Please let me know if there are inaccuracies in my summary.

### Strengths
[Computation] The correction to normalize computational costs is correct, and fleshing out findings based on that assumption further can be very valuable!

[Easy to Read] The paper was understandable, even though it took some time to navigate through the notations. Would have preferred an informal claim alongside the formal notations/theorems for building intuitions and ease-of-reading.

[Good contribution] This work investigates a valuable problem in my view!

This is a partial review, once my main concerns are addressed I can give detailed comments in the feedback period for further sections.

### Weaknesses
I am only listing critical issues in the work currently. If resolved, I can list the other issues in the work.

**W1.** *$C_{task}$ and $M_{online}$ have different distributional constraints* [**Critical**]
- The fundamental discrepancy arises from the proposed memory correction. Offline continual learning employing a 2000-sized memory buffer ($M_{offline}$) is notably disadvantaged relative to online continual learning with a 7000-sized memory ($M_{online}$).
- This stems from the fact that while the data distribution within a task ($C_{task}$) remains static, the memory ($M_{online}$) has the potential to represent samples from all past data distributions.
- Concretely, I think the primary factor favoring online CL over offline CL in Section 3.3 comes from this imbalance in representation. 5000 samples from the latest distribution $C_t$ (in $M_{offline}$) are markedly less useful than 5000 samples across $D_1, ..., D_t$ (in $M_{online}$), hence it performs poorer. 

I would be very surprised if online continual learning ever outperforms the offline continual learning setting, elaborated below.

*What if , with the only difference being short-term memory?*

What is the fair correction to memory then? (I agree with the paper equalizing computation)
- Equalize the long-term memory alongside computation. Interpolate between short-term memory from size $C_{batch}$ to $C_{task}$ 

- Concretely, in Section 3.3, the offline model can use a far larger short term memory (5000) compared to an online model (64). Both have the same fixed sized long term memory but have equal computation.  

I claim (informally): Any training algorithm (with compute budget C) where 64 samples are sequentially introduced can be mimicked when you have access to those 64 and subsequent samples (totaling 5000 samples). The reverse is not feasible due to the inaccessibility of future samples. 

Conclusion: Offline continual learning should be strictly better than online continual learning in principle! (Strictly better because future samples help improve performance)

However, this diametrically opposite to the aim of this work. I hope the above informal statements conveys the core intuition behind why offline continual learning is going to be better than online alternatives.

**W2** *Bound not tight, and likely vacuous* [**Critical**] 
- Theorem 1, in its current form, merely establishes an inequality without showing that the bound is tight. However, the subsequent arguments rely heavily on the bound being tight.
- For proof of theorem 1 to be complete, one must additionally show that the same hypothesis h* achieves equality in both Eq 9 and Eq 8 in Appendix A.1. It is unclear to me that the best hypothesis on distribution of memory samples will necessarily be the best for overall data distribution. However, note that I haven't looked at Mansour et al. (2009).

 *Would the tightness, if shown, convince me?*

- It would make the proof of the theorem complete. However, for deep learning systems, generalizations bounds likely more sophisticated than Theorem 1 are shown to be vacuous [1]. I would not hinge my entire motivation on minimizing discrepancy due to this. 
- Because of this reason, I think the theoretical motivations for the empirical results are quite poor and Section 5 adds little value to the work.
- However, I am perfectly happy to consider predictions from Corollary 2.2 on their own terms and empirical results in Figure 3 from it.

[1] Uniform convergence may be unable to explain generalization in deep learning.

### Questions
Currently, the paper comprises of incorrect memory assumptions used for empirical results (W1: Section 3.3 and Section 6) and vacuous  theoretical motivations (W2: Section 5). 

I am open to drastically changing my current score if **W1** is thoroughly addressed by the authors. However, as it stands I think there are fundamental flaws in the work due to confusing the nature of $C_{task}$ and $M_{online}$ and I am fairly confident in this claim.

### Soundness
1 poor

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper empirically demonstrates that online CL can match or exceed the performance of its offline counterpart given equivalent memory and computational resources. Then the paper give a theoritical explanation from the optimal storage allocation policy.

### Strengths
1. the observation of online CL can match or exceed the performance of its offline counterpart given equivalent memory and computational resources is interesting.
2. This paper further verifies the observation on other methods.
3. The theoritical explanation from the optimal storage allocation policy is valid.

### Weaknesses
(1) It seems that Figure 1 and Figure 1 are the same figure. You need to fix this problem.
(2) The experiment for supporting the emprical observation is not very valid. You should consider more complex datasets (e.g., ImageNet) or class incremental learning in NLP tasks (e.g., intent classfication). Only conducting experiments on the CIFAR dataset is not enough. 

(3) I don't know what benifit can we learn from this observation? Can we use it to  reduce the forgetting problem?

### Questions
Can we use it to improve the performance of current online continual learning methods? Can it principally reduce the forgetting of vision or NLP models in continual learning? I do not see the benifit of this observation.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors compare the *online learning* and *offline learning* setting by proposing to allow for the *online learning* setting as much memory as in the *offline learning* setting. They provide detailed theoretical and experimental analysis of multiple memory allocation settings, thus effectively interpolating between the online setting and the offline setting. Experiments are done on Split-Cifar100, Mini-Imagenet100 and Core50, and using several competitve methods like ER, SCR and ICARL. They find that under a fixed memory budget, it is more efficient to store most of the memory in the long term memory rather than in the short term memory (thus, the *online setting* is more efficient).

### Strengths
- It's an interesting idea to compare the two settings under these circumstances. It is true that the common definition does not impose constraints on the computational cost, so it makes sense to compare it's performance to the one of offline learning under the same computational cost
- The discovery that less short term memory is better is interesting and could help the field to move forward

### Weaknesses
- 1) While some theoretical analysis is provided, I don't think that this is sufficient to prove the claims of the paper. In particular, the analysis of Eq (6) seem to show that "a minimum amount of short term memory" should be used. In that case, why are you using short term memory at all if the analysis concludes that you should not use it ? (It's also a question, please inform me if I missed something here). In the case that I am correct, I think that these analysis are not necessary to the paper.
- 2) I think an important comparison is missing to the paper which is for me the main point. You claim that the optimal setting is using a small short-term memory but I have not seen experiments not using any short term memory (which would collapse to the GDumb baseline [1]). Indeed, if this baseline performs well under your experimental setting then the claim of the paper changes completely and the novelty is not here anymore. So I think it's very important to include this baseline that uses all the memory available (i.e 7k for cifar100) as long term memory.
- 3) It would be nice to have results for Split-Cifar100 and Mini-Imagenet with more splits (20), since then the total allowed memory would also be smaller.

[1] "GDumb: A Simple Approach that Questions Our Progress in Continual Learning", A Prabhu, PHS Torr, PK Dokania

### Questions
- Do you plan to release the code ?
- c.f weaknesses (2), did I understand something wrong in the analysis Eq (6) ? If the analysis concludes that you should use minimum short term memory why do you use any at all ? If it's just that it's working better experimentally but that the analysis concludes something different then I think it's better to remove this analysis altogether.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
