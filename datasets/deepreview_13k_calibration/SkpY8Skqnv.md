# $\mu$LO: Compute-Efficient Meta-Generalization of Learned Optimizers

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
\commentall{
Learned optimizers (LOs) have the potential to greatly decrease the wall-clock training time of neural networks, significantly reducing training costs. However, LOs suffer from poor meta-generalization, especially when used to train networks much larger than those seen during meta-training. 
To bridge the generalization gap, we consider the recently proposed Maximal Update Parametrization (\mup) that allows zero-shot generalization of optimizer hyperparameters from smaller models onto larger ones by aligning the distribution of gradients for small and large neural networks. We highlight that \mup theory can be extended to the case of learned optimizers and consider the meta-training problem as finding the learned optimizer under the \mup. 
When evaluating LOs meta-trained with \mup we observe large improvements in meta-generalization compared to standard LOs, which optimize networks in standard parametrization (SP). When applying our strongest $\mu$LO (trained for 103 GPU-hours) to large-width models we are often able to match or exceed the performance of VeLO, the largest publicly available learned optimizer, meta-trained with 4000 TPU-months of compute. Finally, we observe that $\mu$LOs also improve generalization to longer training horizons ($25\times$ those observed during meta-training) and deeper networks (than those seen during meta-training) when compared to their SP counterparts. %Our method has the potential to significantly reduce meta-training cost while improving the generalization of learned optimizers.
} %% end of \commentall
Learned optimizers (LOs) can significantly reduce the wall-clock training time of neural networks, substantially reducing training costs. However, they can struggle to optimize unseen tasks (meta-generalize), especially when training networks much larger than those seen during meta-training. To address this, we derive the Maximal Update Parametrization ($\mu$P) for two popular learned optimizer architectures and propose a simple meta-training recipe for $\mu$-parameterized LOs ($\mu$LOs). Our empirical evaluation demonstrates that LOs meta-trained with our recipe substantially improve meta-generalization to wider unseen tasks when compared to LOs trained under standard parametrization (e.g., as they are trained in existing work). When applying our $\mu$LOs, each trained for less than 250 GPU-hours, to large-width models we are often able to match or exceed the performance of pre-trained VeLO, the most performant publicly available learned optimizer, meta-trained with 4000 TPU-months of compute. We also observe that learned optimizers trained with our $\mu$LO recipe also exhibit substantially improved meta-generalization to deeper networks ($5\times$ meta-training) and remarkable generalization to much longer training horizons ($25\times$ meta-training).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes $\mu$LO, a new approach, inspired by hyperparameter transfer with the maximal update parameterization ($\mu$P), for training learned optimizers. Using $\mu$P for a model's initialization and weight updates has been shown to enable transferring high quality hyperparameter settings for the optimizer to networks of greater width, depth and longer training horizons.  Similarly, $\mu$LO addresses the limited ability of previous learned-optimizers to generalize to wider networks and longer training horizons by deriving the learned optimizer update required by $\mu$P.  Experiments show that $\mu$LO generalizes better than learned optimizers trained with standard parameterizations when applied to networks of larger width, depth, and longer training horizon as was observed for $\mu$P in the standard hyperparameter transfer settings.

### Strengths
- The experimental results are quite compelling and show $\mu$ LO addresses the generalization issues of previous incantations of learned optimizers.
- This is an interesting application of $\mu$ P and could potentially reduce the cost of model tuning dramatically.  However, the bar is quite high and will require additional work to compare $\mu$ LO with newer optimizers like Shampoo and Modula.

### Weaknesses
 - While the experimental results are strong, they do not back up the claimed benefit that $\mu$ LO addresses the three issues of $\mu$ -transfer by avoiding the need for hyperparameter tuning for reach new architecture and task.
- The experimental results are missing comparisons to VeLO-4000 in Tables 5 and 6.  I think another reasonable baseline is per-task tuned Adam and $\mu$ Adam in the resource constrained setting to see if $\mu$ LO obvious the need for task specific optimizer tuning.
- The proposed $\mu$ LO does not take into account followup work on $\mu$ P that extends the original theoretical justification for transferring across width to depth (see [Tensor Program VI](https://arxiv.org/abs/2310.02244)).  Hence, the generalization across depth is more consequential then intended and may be improved with an explicit maximal update parameterization for depth.
- The legend for Figure 4 does not distinguish between dashed and solid lines.

### Questions
- According to Table 1, $\mu$ LO_M and $\mu$ VeLO_M are trained on ImageNet classification using 3-layer MLP with 3 different width.  Is that correct?  Does that mean transformer and ViT architectures studied in Figure 4 d and e were not seen during meta-training and are there to show generalization to unseen architectures?
- Please include VeLO-4000 in Figures 5 and 6.
- Why is $\mu$ LO better than $\mu$ VeLO on average despite VeLO being a more powerful model?
- How does $\mu$ LO compare to a per task tuned Adam/ $\mu$ Adam?
- What is the overhead of using the learned optimizer per gradient step relative to Adam?

### Soundness
2

### Presentation
2

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
The paper investigates the limitations of current learned optimizers (LOs)—small, data-driven neural networks designed to optimize other neural models—in their ability to generalize to longer optimization horizons and larger models than those encountered during meta-training. The authors derive the Maximal Update Parametrization (muP) for two popular LO architectures and propose a simple meta-training recipe for mu-parameterized learned optimizers (muLOs). Empirical evaluations demonstrate that muLOs can match or exceed the performance of VeLO—a state-of-the-art LO trained with 4000 TPU-months of compute—when applied to large-width models.

### Strengths
1. Effective Identification of Limitations in Learned Optimizers: The authors clearly pinpoint the generalization issues of current LOs, especially their generalization issues with larger models and longer training horizons.
2. Innovative use of Maximal Update Parametrization: By applying muP to LOs, they leverage theoretical guarantees for zero-shot hyperparameter tuning, going further to transfer optimizers. 
3. Practical Solution to Costly Hyperparameter Optimization: The proposed muLOs offer a way to avoid expensive HPO on each new architecture and task, addressing a significant practical challenge.
4. Significance in the Field: By enhancing the generalization capabilities of LOs and making them more practical for large-scale applications.

### Weaknesses
 1. Lack of Information on Computational Cost: The paper does not provide detailed information about the overall computational resources required for the method, spent on hyperparameter tuning for the mu-based methods. This is crucial for practitioners who may need to pre-train the optimizer themselves and assess the feasibility of implementing the method. Specifically, the paper lacks a breakdown of the resources needed for meta-training the learned optimizers and the subsequent fine-tuning or application to new tasks. This makes it difficult to assess the practical cost-benefit of the proposed approach.
2. High Pre-Training Computational Cost: According to Line 356, the pre-training of an LO with already tuned hyperparameters amounts to 16 TPU-months. This is a substantial computational expense, prohibiting practitioners from pre-training an LO themselves. This means that a SoTA method would be preferred, and hence the comparison to VeLO seems more critical. The paper should clarify if this cost is for a single LO or multiple, and how this cost scales with the complexity of the optimizee model.
3. Unclear Method Overhead: There is insufficient information regarding the computational overhead introduced by using the LOs compared to standard optimizers. Specifically, the paper does not quantify how much slower the training process becomes when employing the neural network-based optimizer. For practical applications, understanding this overhead is essential for adjusting compute budgets and training timelines accordingly. The authors should provide a detailed analysis of the per-step computational cost of the LOs compared to standard optimizers like Adam or SGD, including the forward and backward passes through the LO network.
4. Limited Clarity in Results Presentation: Throughout the paper, the primary metric presented is the training loss. However, details about how this metric is calculated and presented are lacking. For instance, in Figure 2, it is unclear whether the loss is measured exactly at the presented iteration if the error bars represent standard deviation across different seeds, or how the results would differ if showing the best loss achieved so far or using a moving average. The paper should also specify if the loss is computed on the entire training set or a subset, and if any smoothing or averaging is applied before plotting.
5. Absence of downstream Evaluation Metrics.
6. Incomplete Presentation of Experimental Results: In Section 4.1.1, the authors mention collecting data for 1,000 training steps, but the plots presented display only 50% of this range (Figure 3 + appendix). Additionally, information about the number of seeds used and the variability across runs is missing. The paper should clarify the reason for truncating the plots and provide the number of seeds used for each experiment, along with a discussion of the observed variance across different runs.
7. Ambiguities in Generalization Evaluation (Figure 4):
* Convergence Similarities: In Figures 4a and 4b, the loss curves for muAdam and the proposed muLOs converge to similar values. This suggests that the primary benefit is improved early performance (anytime performance), but without considering the method's overhead, it's unclear how significant this benefit is in practical applications. The paper should quantify the speedup in convergence achieved by the muLOs compared to muAdam, and discuss the trade-offs between early performance and computational overhead.
* Behavior of muAdam in Figure 4c: The loss trajectory of muAdam has an unexpected shape in Figure 4c without a clear explanation, making it difficult to understand the underlying reasons. The authors should provide a detailed analysis of why muAdam's loss curve behaves erratically in this specific case, and discuss the implications for its generalization capabilities.
* Confusing Legend and Color Coding: The legend in Figure 4 uses the same markers for VeLO and LO, and for muVeLO and muLO, making it challenging to distinguish between the different methods.
8. Terminology Clarification Needed: The paper refers to muAdam, but it is unclear whether this refers to muAdam or muAdamW. The authors should explicitly state which variant of Adam is being used, and justify their choice.
9. Inconsistent Performance Across Tasks (Figure 5): In Figure 5a, muLO appears to diverge, and across the tasks in Figures 5a and 5b, the ranking between muLO and muVeLO changes significantly. This inconsistency makes it difficult to determine which optimizer performs better overall and under what conditions, complicating the decision-making process for practitioners. The paper should provide a more detailed analysis of the factors that influence the performance of muLO and muVeLO across different tasks, and offer guidance on when to prefer one over the other.
10. Questionable Claims About Stability: The claim in Line 516 that "muVeLO_M stably decrease training loss over time for each task" seems inaccurate. In Figure 6a, the loss begins to diverge, contradicting this statement. This raises concerns about the reliability of the method and the validity of the conclusions drawn. The authors should address the apparent divergence in Figure 6a and clarify the conditions under which muVeLO_M can be expected to stably decrease training loss.
11. High Variance in muVeLO Performance: The figures indicate that muVeLO exhibits a higher standard variance in its performance, while other methods show minimal variance. Understanding why muVeLO has higher variability is important for assessing its reliability and for guiding its practical adoption. The authors should investigate the sources of this variance and provide insights into how it can be mitigated.

### Questions
1. Can you provide detailed information on the computational resources required for your method, specifically the hyperparameter tuning of the mu-based methods?
2. Given that retraining of both the LO and VeLO is infeasible, how do you justify LO use compared to the SoTA method?
3. How much additional computational overhead does using the LO introduce compared to standard optimizers/ SoTA, and how does this affect training speed?
4. Could you clarify how the training loss is calculated and presented throughout the paper, and whether the error bars in Figure 2 represent standard deviation across different seeds?
5. Could you include any validation metric, to assess the practical impact of your method?
6. In Figure 3, why do the plots display only 50% of the collected data, and could you provide information about the number of seeds used and variability across runs?
7. Is muAdam in your experiments referring to muAdam or muAdamW, and could you clarify this terminology?
8. Given the inconsistent performance between muLO and muVeLO across tasks (as seen in Figures 5a and 5b), can you provide guidance on which optimizer performs better under specific conditions?
9. How do you reconcile the claim that "muVeLO_M stably decreases training loss over time for each task" (Line 516) with the divergence observed in Figure 6a?
10. Why does muVeLO exhibit higher variance in its performance compared to other methods, and what are the implications for its practical adoption?

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
3

### Summary
This paper proposed new optimizers to overcome the generalizability issue of the existing hand-crafted learned optimizers. It showed extensive experimental results so that the proposed optimizers improve meta-generalization to wider unseen tasks in most cases.

### Strengths
*	Despite some cases where the proposed optimizers do not show the best performance, the “overall” results show that the proposed optimizers show better performance and better stability. 


*	It is interesting and informative that it shows a stable performance in the longer horizon.

### Weaknesses
•	Why don’t you show results on ResNet and Plain ResNet (i.e., without residual connections)? Earlier, it has been shown that the reason why ResNet (with residual connections) works well by loss landscape – ResNet shows a smoother landscape while Plain ResNet shows a bumpy loss landscape in [1]. If the proposed optimizers can show stable performance even in Plain ResNets, I believe this work will be shown to be very effective. 		

•	In a nutshell, the technical addition of this work on top of the standard LP is adding 1/FAN_IN coefficient on the right term (the updated amount for the weight) in (2) if the weight is part of a hidden layer. In that sense, it is unclear how much technical contribution this work would contain. I wonder if the authors’ claim is that it shows a great advancement by adding such a small change. The modification seems like a minor adjustment to the update rule, and it's not immediately clear why this specific scaling factor would lead to such significant improvements in generalization. A more thorough analysis of the theoretical underpinnings of this modification is needed to justify its impact.

•	The result in Fig 4 is confusing with regard to the goal of the work. The goal of this paper is to develop a better-generalizable optimizer. However, it did not show the best performance on the most “out-of-distribution” tasks (transformer language modeling and ViT image classification, Fig. 4.) (Although the authors argued that their LOs are meta-trained with only 0.004% of VeLO-4000.) Hence, the contribution of this work is diluted. The proposed optimizers do not show the best performance for Transformer LM, in Fig 5 either. The fact that the proposed method does not consistently outperform existing methods on these more complex tasks raises concerns about its practical applicability and the extent of its generalization capabilities. The argument that the method was trained on a smaller dataset does not fully address the performance gap.

•	The legend in Fig 4 needs to be fixed. Either of VeLOM or LOM needs to be dotted line. Also, either of μLOM or μVeLOM needs to be a dotted line (by looking at (c), μVeLOM is a dotted line).

### Questions
•	Why did you select only MLP and Transformers (for language and vision) to show results on?

•	I am wondering how the loss landscapes of the approaches on ResNet and Plain ResNet would look.

### Soundness
3

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
4

### Summary
In this paper, the authors aim to improve on the challenging task of improving the meta-generalization of Learned Optimizers (LOs) to longer optimization trajectories and larger base models while maintaining compute efficiency. The authors derive Maximal Update Parametrization for two popular learned optimizer architectures, enabling zero-shot hyperparameter transfer from smaller models to larger ones. A simple training recipe for µ-parameterized LO is proposed which leads to substantial improvement in meta-generalization to wider networks, deeper networks, and longer training horizons with orders of magnitude less computational cost.

### Strengths
• Overall, I think the paper is well-written and addresses a very meaningful problem in the meta-learned optimizer. 

• The empirical performance of the proposed algorithm is very good (Figures 4, 5, and 6), and it is particularly impressive that they were able to get such good results using so little compute relative to VeLO (which is extremely expensive …).

### Weaknesses
• The proposed method is quite simple, essentially, describing a way to construct a model such that the meta-learned optimizer can generalize to larger-width networks, deeper networks, and longer training trajectories. As far as I am aware the novelty of this paper is relatively limited since most of the findings are originally derived from [1] where Maximal Update Parametrizations was originally proposed. Therefore, from my perception, this appears to be a straightforward application of that work. Could the authors please elaborate on the technical novelty, of this paper? If the technical novelty is more than just an application of Maximal Update Parametrizations, I am happy to increase my score.

• The paper could be made more self-contained. I had to read [1] before really understanding much of the terminology and language being used in this paper.

### Questions
• From my understanding [1] shows how to initialize the network such that you can scale the width of the network while maintaining optimal hyper-parameters. This paper seems to suggest that using this strategy also allows you to scale the depth of the network and the optimization trajectory. Why is that the case? Can the authors please add some discussion about that and clarify more theoretically why the results are the way they are.

### Soundness
3

### Presentation
3

### Contribution
2
