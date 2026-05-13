# A second-order-like optimizer with adaptive gradient scaling for deep learning

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
In this empirical article, we introduce INNAprop, an optimization algorithm that combines the INNA method with the RMSprop adaptive gradient scaling. It leverages second-order information and rescaling while keeping the memory requirements of standard DL methods as AdamW or SGD with momentum. After giving geometrical insights, we evaluate INNAprop on CIFAR-10, Food101, and ImageNet with ResNets, VGG, DenseNet, and ViT, and on GPT-2 (OpenWebText) train from scratch and with LoRA fine-tuning (E2E). INNAprop consistently matches or outperforms AdamW both in training speed and accuracy, with minimal hyperparameter tuning in large-scale settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces INNAprop, a combination of the INNA optimizer with RMSprop gradient scaling. The resulting method has memory requirements similar to methods such as AdamW. Experiments show that this optimizer is competitive with AdamW.

### Strengths
The derivation of the algorithm is clear and the performance often seems competitive with AdamW. Large-scale models such as ViT-B/32 and GPT-2 were trained.

### Weaknesses
The INNAprop algorithm seems like a relatively straightforward extension from INNA. From what I can tell Algorithm 2 can be derived directly from the INNA equations in Table 2 and adding the factor $\frac{1}{\sqrt{v_{k+1}} + \varepsilon}$ to the gradient. The motivation from a continuous dynamical systems perspective and the derivation done in appendix B seem equivalent to those from the INNA paper. This means that the theoretical insights from this paper seem limited.

This in itself wouldn't be a bad thing if the paper could make strong experimental claims about this small tweak to INNA leading to consistently stronger performance. However, this seems difficult to conclude for a few reasons, such as:

* No comparisons were made with INNA (without the RMSprop scaling) or other algorithms (Adam, ADAGRAD, SGD)
* In figures 3 and 6 INNAprop is sometimes indistinguishable from AdamW

Another surprise is that the optimal values for $\alpha$ and $\beta$ seem quite different to those found in the INNA paper (which ends up using $(0.1, 0.1)$ and $(0.5, 0.1)$) and it would be great to understand why. (In general, I am not convinced that the comparison with AdamW was the way to go, given that the proposed algorithm is far more similar to INNA. It would be insightful to know how the RMSprop extension changes INNA's behaviour and the choice of optimal hyperparameters for INNA.)

I understand that with limited compute it can be difficult to run large amounts of experiments, but I don't think that in it's current form this paper really provides new insights to the community: The RMSprop addition to INNA is pretty straightforward, and whether it really makes a difference is still hard to say.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new first-order optimization algorithm: INNAprop. The algorithm combines the INNA method with RMSProp to derive a novel optimization scheme. The authors evaluate INNAprop empirically against AdamW, the de facto standard deep learning optimizer. They explore a set of diverse tasks spanning image classification and natural language processing using several different classes of deep learning architectures.

### Strengths
I thought the introduction was strong and successfully explained the need for improved optimization algorithm algorithms in terms of real-world impact. The authors back this up by deriving a memory-efficient version of their algorithm matching the memory overhead of existing approaches.

A thorough discussion of the algorithm and how it can be derived is provided. The authors also discuss comparisons between INNAprop and several other methods in the literature, in terms of its derivation. This is a valuable contribution that helps to place the proposed method among existing work. On the surface, I felt that the combination of the two methods could be of limited novelty. However, after reviewing the derivation I feel this constitutes a reasonably strong contribution.

The paper is clear and well-written. The authors provide a thorough set of diverse experiments to investigate the proposed method and include multiple runs to account for variability. From my review of the manuscript, all results look sensible and technically sound.

### Weaknesses
Claiming second-order without computing second-order statistics doesn't seem accurate to me. The finite difference approximation may not be sufficiently accurate to achieve these benefits. However, I am not overly familiar with this approximation that the authors adopt from prior work. One way to alleviate this concern would be to provide additional justification for this terminology. Or, to include empirical evidence that the finite-difference approach is providing a good approximation of the actual second order statistics.

One of the claimed contributions is that INNAprop "matches or outperforms AdamW in both training speed and final accuracy on benchmarks". However, Fig. 2 shows the faster training speed of AdamW (the final error bars overlap for test accuracy so I'd agree that they match performance). Fig. 3 shows INNAprop as faster to converge for ResNet, but slower once again for ViT. The test accuracy is once again matched in both experiments. Fig. 4 shows a similar convergence speed with a modest (~1%) increase in accuracy for INNAprop. Finally, Fig. 5 shows a modest win for INNAprop on the smaller settings and matched performance for the larger model. For the LoRA finetuning (Fig. 6), there is a small win for the small setting and INNAprop matches AdamW on the medium and large setting.

The improvement over Adam variants is small across the board. The notable wins are on vision finetuning (Fig. 4) and small-scale GPT-2 training (Fig. 5). There are many methods that propose similarly slim margins and none are adopted by the community. Furthermore, under scrutiny from third-party implementations, the gains are often difficult to replicate [1]. Sadly, my honest opinion is that this method will not gain traction with the community --- it is unclear when it should be used over AdamW.

While often spurious, it is common for optimization algorithms to include theoretical analysis of their convergence. I do not consider this a critical weakness of this paper.



### Questions
Can you explain how you "systematically favored AdamW through the choice of recommended hyperparameters (scheduler, learning rates, weight decay)"? In more established tasks, I feel this is a reasonable claim. However, where INNAprop showed wins (finetuning on an uncommon dataset and training tiny GPT-2 models), I expect that standard AdamW hyperparameters are suboptimal. How much compute budget was spent tuning AdamW compared to INNAprop? I am also concerned that two different settings of INNAprop are shown in all experiments against a single choice of hyperparameters for AdamW.

In the appendix, you derived the DINAdam variant. Do you also explore this algorithm empirically?

With my initial review, I am recommending that the paper be rejected. I believe the paper is technically correct and the proposed algorithm is sufficiently novel. However, I do not believe that the algorithm provides a meaningful practical contribution for the wider community at this time. My concern is that a practitioner would always choose AdamW over INNAprop due to the marginal expected gains, increased risk of failure, and the additional overhead of parameter tuning required. My score would change if the authors could provide clear guidance on when a practitioner would choose INNAprop over AdamW and expect a win. 

Minor points:

- "we provide quite extensive experiments" vague statement in abstract. I would prefer that this be made more precise.
- "extra second-order geometrical intelligence" vague technical term. What do you mean by this? I think this should be clarified in the main text.

-------
**Post-rebuttal:**

Following the response from the authors, I have increased my score (and reduced my confidence). This is due primarily to the author's point that several results that I considered to be minimal improvements are in fact significant relative to the current state-of-the-art.

I retain concerns that the proposed algorithm is unlikely to see widespread community adoption. However, the paper is sound and proposes a novel technique. I would prefer that we present novel and correct methods to the community for their consideration.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce a second-order optimization method, INNAprop, which combines the INNA method with RMSprop, while not increasing the memory-footprint. The method is evaluated on a few image classification benchmarks, and GPT-2 with the OpenWebText dataset, and directly compared to AdamW with somewhat favorable results.

### Strengths
It is a comprehensive and well-written paper that does a good job of explaining the motivation for, and the math behind, the proposed method. I do appreciate the main thesis of the work, and the effort that went into it. I like the discussion of, and approach to, hyperparameter tuning, as well as the comprehensive Appendix.

### Weaknesses
My main objection is the empirical evaluation. Firstly, the reported improvements (on test sets) are generally very marginal. The performance gains, while present, are often within the noise level of typical stochastic optimization runs, making it difficult to ascertain the true benefit of INNAprop. For instance, a 0.1-0.3% improvement on CIFAR-10 or ImageNet is not particularly compelling, especially when considering the added complexity of the method. Secondly, the results are not pushed to SOTA-level --- even for the chosen architectures (that are pretty old and pretty small). The choice of ResNet-18 and similar architectures, while common, does not demonstrate the potential of the method on more complex and modern architectures. The lack of experiments on larger models and datasets leaves a significant gap in the evaluation. Thirdly, there are too few experiments to convince me that the proposed method really works better than, or even as well as, AdamW. The limited number of benchmark datasets and the lack of ablation studies on key components of INNAprop make it difficult to draw definitive conclusions. Since the method is not faster, or less computationally demanding, I find myself unconvinced of its overall usefulness.

### Questions
I noticed that you mentioned the lack of computational resources two times (lines 259 and 359). You should know, that I am very sympathetic to that challenge. Still, my suggestion is that you bite the apple and invest that extra time and computational cost --- to really make a convincing case for your method :-)

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper combines RMSprop adaptive gradient scaling to the existing INNA optimizer, which is based on the Dynamical Inertial Newton. The obtained optimizer leverages second-order information while having similar computational requirements to first-order methods. With appropriate hyper-parameters the optimizer matches and in some cases outperforms AdamW.

### Strengths
The paper is well written, and easy to follow.
-    The derivation of the algorithm is well motivated.
-    They leverages second order information without requiring the hessian.
-    The algorithm seems to perform on par or even outperform AdamW in certain settings like language modeling.
-    The experiments cover a good amount of tasks between image classification and language modeling.
-    The authors open-source the code.

### Weaknesses
 -   The introduction of the paper makes a big deal about the energy consumption of training large language models, but the authors don't measure or show how their method compares to the competitors in terms of wall-clock time in their experiments. Particularly interesting would be seeing how wall-clock time on ImageNet or language modeling tasks compare.
-   The method lacks comparison with more recent optimizers other than AdamW. Sophia for example is another fast and efficient second-order optimizer paper, which the author cite, but don't compare with. Lion is another recent and high performing optimizer, which was cited but not compared with either.
-   Numeric results are reported without standard deviation/standard error or confidence intervals

### Questions
-   How does INNAprop compare in terms of wall-clock time to AdamW or Sophia?
-   How does INNAprop compare to Sophia/Lion and other more recent high performing optimizers?
-   Is the increase in test accuracy of INNAprop compared to AdamW statistically significant? What are the error ranges?

### Soundness
2

### Presentation
3

### Contribution
3
