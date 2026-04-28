# Towards Perpetually Trainable Neural Networks

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Underpinning the past decades of work on the design, initialization, and optimization of neural networks is a seemingly inoccuous assumption:  that the networkis trained on a stationary data distribution. In settings where this assumption is violated, e.g. deep reinforcement learning, learning algorithms become unstableand brittle with respect to hyperparameters and even random seeds. One factor driving this instability is the loss of plasticity, meaning that updating the network’s predictions in response to new information becomes more difficult as training progresses. In this paper, we conduct a thorough analysis of the mehcnaisms of plasticity loss in neural networks trained on nonstationary learning problems, identify solutions to each of these pathologies, and integrate these solutions into a straightforward training protocol designed to maintain plasticity. We validate this approach in a variety of synthetic continual learning tasks, and further demonstrate its effectiveness on naturally arising nonstationarities

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper provides a good, deep analysis of the loss of plasticity. It provides four mechanisms that lead to loss of plasticity. This leads to the proposal of a training protocol that combines layer normalization, l2 regularization, and scale-invariant output parametrization. The effectiveness of these methods is shown in various supervised continual learning tasks and in some naturally arising non-stationary problems.

### Strengths
The paper is well-written and easy to read, for the most part. 

The analysis of loss of plasticity is well done and provides various insights into the phenomenon. The proposed methods are well motivated by these insights, and they seem largely effective on a wide variety of problems.

### Weaknesses
Although the paper contains good ideas, there are a couple of major issues that stop me from recommending a full acceptance at the moment.

- **Misleading conclusions**
    - The paper's conclusion says, " ... This paper has resolved a critical first step towards robust continual learning algorithms: ensuring that neural networks maintain their ability to learn over time. ...". The algorithms (Layernorm + L2) they propose maintain plasticity but at the expense of peak performance, so it is unfair to say that the proposed algorithm has "resolved a critical first step ."The goal of solving plasticity loss is not to just develop algorithms that maintain a constant level of performance across tasks, but *to develop an algorithm that will maintain the best possible performance for the network.* Consider the extreme case; an algorithm has a learning rate of 0. Clearly, this algorithm maintains plasticity, but it is the worst-performing algorithm. The results in the top-left panel of Figure 3, as well as in Figure 8, show the performance of L2+LayerNorm is worse than the peak of just LayerNorm. L2 is helping maintain plasticity but at the expense of peak performance. I think the conclusion of the paper should be changed to reflect that the proposed algorithms maintain plasticity but sometimes at the expense of peak performance. Specifically, the paper needs to acknowledge that while L2 regularization prevents catastrophic forgetting, it does so by limiting the network's capacity to learn new tasks to the fullest extent, which is a critical limitation in continual learning.
    - In the same vein as the point above, the use of classification loss in a regression problem increases the minimum loss that the network can get to because there will be a residual loss for each data point. Even though we might be able to maintain plasticity with a classification loss, it comes at the expense of the best possible performance. The paper needs to more clearly address the trade-offs of using a classification loss for regression, as this approach inherently limits the achievable performance ceiling compared to a direct regression approach. The paper should quantify this residual loss and discuss its implications for the overall performance of the proposed method.
    - At many points, the paper says the previously proposed methods "slow learning in the single-task setting." This suggests that the proposed method has no issues in the single-task setting. But again, that is not true. The proposed method can lead to sub-optimal performance in the single-task case (top-left panel of Figure 3, Figure 8). The paper needs to explicitly acknowledge that the proposed method can also slow down learning in single-task settings, and provide a more nuanced discussion of the trade-offs between plasticity and single-task performance. It is not enough to simply state that previous methods slow learning; the paper needs to show how the proposed method compares in terms of single-task learning speed and final performance.
- **Missing details of empirical evaluation.** The paper does not provide any details on the number of runs for each experiment, nor does it say what is the shaded region in each plot. It is unclear at the moment if any of the results in the paper have any statistical significance and if they will withstand the test of time. The paper should also include error bars or confidence intervals to show the variance of the results. Without this information, it is impossible to assess the robustness of the proposed method.

### Questions
- What exactly is scale-invariant output parameterization? This term is used at multiple points in the paper, but it is never explicitly defined. Is it just the conversion to classification loss using the 'two-hot' trick described in section B.3?
- What is "smoothing" on the right side of Figure 3? Similarly, what is "normalization"? Is it just layer norm or something else?
- $\gamma=0$ fails in Figure 3. The paper attempts to describe what is happening there. But I do not understand why the line for $\gamma=0$ loses plasticity.
- Can you please show a zoomed-in image of the blue line ($\gamma=0.99$) of the bottom left plot on the right side of Figure 3? It seems that the loss is increasing for the blue line, but it is unclear from the current image. And if possible, can you run this experiment for ten times longer? If the loss is increasing, a longer experiment will make it clear.
- Why wasn't L2 used in the RL experiments with C51? Is it already included in C51, or did it hurt performance?
- Which figure in the main paper does Figure 8 correspond to?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Paper presents several failure modes of nonstationary learning, and some solution for mitigating loss of plasticity in neural networks.

### Strengths
- Paper studies an interesting and important question - why do neural networks lose plasticity and how to mitigate this problem?
- Includes clear visualizations which summarize experimental findings nicely
- Thoroughly evaluates a variety of different solutions for solving the plasticity problem -- I especially appreciate the breadth of different solutions that were tried in section 4

### Weaknesses
Sec 1: Abstract/ Introduction
- Paper claims "[we] identify four primary mechanisms by which neural networks lose plasticity: unit saturation, preactivation distribution shift, unbounded parameter growth, and loss landscape pathologies induced by the network outputs". I believe this is overstating the contributions of the paper, as a number of these mechanisms have previously been identified in prior work. While the paper acknowledges that saturated activations have been previously identified, it does not adequately address the fact that preactivation distribution shift and unbounded parameter growth have also been studied in the context of plasticity loss. The claim of identifying loss landscape pathologies induced by network outputs as a distinct mechanism also requires more justification, as it is not immediately clear how this differs from previously identified issues with loss landscapes.

Sec 2: Related work
-  I think section 2.2 (Loss of Plasticity) needs to be much more specific about the contributions in the prior work, and to more clearly delineate how the contributions of this work differs. In its current form, this section only summarizes how prior work characterize the concept of plasticity in a very abstract manner, without mentioning any specific differences between this work and prior work. However, many of the ideas presented in this paper are very similar to ones already existing in prior work (especially Lyle 2021, Kumar 2023a, Abbas 2023), and it would be helpful for understanding the novel contributions of this paper beyond prior work if it were described in more specific terms. The related work section should explicitly discuss how the proposed mechanisms and mitigation strategies build upon or differ from existing approaches, particularly those that have explored similar concepts such as the use of non-saturating activations, normalization techniques, and regularization methods.

Sec 3: Failure Modes of Nonstationary Learning
- Sec 3.1: while prior works has already identified saturated activations to be a reason for loss of plasticity, this paper claims to provide a "novel explanation of why units die off". However, it is not clear how the experiments in this section supports any novel explanations. More specifically, Fig 2 show that at the beginning of learning a new task, many network representations have negative dot products with all network inputs, while after a few hundred steps, this leads to many dead neurons. This experiment alone demonstrates that saturated activations is a problem for nonstationary learning, but does not provide insights into why. The authors hypothesize (in text) that this behavior may be related to de reduction in confidence on the new task, followed by an increase in confidence after learning the new task, but no evidence was provided for this explanation. The paper should provide more direct evidence linking the observed behavior to the proposed explanation, potentially through additional experiments that isolate the effect of confidence changes on unit saturation.
- Sec 3.2: in this section, the paper claims that another reason for the loss of plasticity is the linearization of units. However, there are *no experiments* in this section. Therefore, there is no evidence that this phenomenon happens in practice. Furthermore, the paper itself noted "recovery from this state is possible", so even if it does happen in practice, the network could potentially quickly recover from this state, making it even more important to empirically understand to what extent this "plight" is a problem in practice. The lack of experimental validation for the linearization claim is a significant weakness, and the paper should include experiments that demonstrate the occurrence and impact of this phenomenon on plasticity loss, as well as the conditions under which recovery is possible.
- Sec 3.4: this section, the paper hypothesize that another reason for the loss of plasticity is that "regression to targets which have a large mean relative to their variance is innately difficult for neural networks". However, the experiments do not necessarily support this hypothesis. Instead, the experiments show that using distributional losses seem to mitigate loss of plasticity, which is a finding that has already been presented in prior work. While the paper's hypothesis could potentially explain why distributional losses work well, there are a number of other potential explanations, and the paper provide no additional evidence for why the proposed hypothesis is the correct one. The paper needs to provide more direct evidence for the proposed hypothesis, perhaps by manipulating the target mean and variance independently and observing the resulting impact on plasticity. Furthermore, the paper should discuss alternative explanations for the effectiveness of distributional losses and provide a rationale for why the proposed explanation is more plausible.

Sec 5: Natural Non-stationarities
- The paper is not specific enough about the exact environments/datasets being evaluated. In particular, the paper says it "trained on the arcade learning environments", as well as "a dataset from the WiLDS benchmark". However, the arcade learning environment includes over 50 games, and the WiLDS benchmark includes 10 different datasets. For the RL experiment, it is unclear whether the experiment is only trained on one environment (if so, which one?), or if the results are averaged over training runs on many different environments (if so, which ones?). Furthermore, the paper should be more specific about which particular dataset it used from the WiLDS benchmark for its experiment. The lack of specificity regarding the experimental setup makes it difficult to reproduce the results and assess their generalizability.
- Assuming the paper only evaluated on 1 RL environment, I believe this, in addition to only 1 distribution shift dataset, is not extensive enough to validate the efficacy of the proposed approach on realistic learning problems. The paper should include evaluations on a more diverse set of environments and datasets to demonstrate the robustness of the proposed approach.
- The proposed approach is using layer norm with L2 regularization. Why does the RL experiment only compare C51 with layer norm and C51 without layer norm? What about L2 regularization? Even if the L2 regularization doesn't help, or even hurts performance, I think it would
be informative to the reader. The paper should provide a more thorough analysis of the impact of L2 regularization on the RL experiments, even if it does not improve performance. This would help to understand the individual contributions of layer normalization and L2 regularization to the overall performance of the proposed approach.

Overall, I think this paper has some interesting insights. However, in its current, I believe this paper makes a number of claims which are unsubstantiated by the experimental results.

### Questions
See weaknesses section for questions

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper describes the ways to overcome degradation of training performance of the neural networks due to loss of plasticity.  The authors identify a number of reasons for the loss of training plasticity: preactivation shift, dead and effectively-linear units, norm growth, and shifts in the target function, and propose the simple ways to mitigate these phenomena.  The authors study the proposed interventions, based upon L2 regularisation and layer normalisation in two settings: deep reinforcement learning and classification

### Strengths
- It is very important to address the well-documented (as it is well-supported by the references in the paper) phenomenon of the lack of plasticity

- the paper is well motivated and clearly written, however, there are some questions to be resolved on quality and clarity of some particular aspects (see weaknesses below)

- originality: the work builds upon existing well-known methods such as L2 regularisation and layer normalisation, but builds new insight how these remedies could help solve the problem of learning from non-stationary data

- significance: it can help learn from non-linear data streams, both in reinforcement learning and classification scenarios

- the paper discusses in detail the experimental conditions and therefore, addresses reproducibility well

### Weaknesses
Cons:
- Clarity aspects: it is important to distinguish between the aspect of nonstationarity and continual learning, see Q1; the relative performance metric needs to be clarified, see Q2

- Quality aspects: see Q3-Q6

- Originality aspects: While the paper researches extensively into reasons of loss and plasticity, the remedies are based on well-known methodologies (L2 regularisation, layer normalisation) and therefore the message is mostly limited to identifying the remedies as opposed to novel methodological contributions towards solving this problem (see Q7)



### Questions
Q1. In the introduction, the paper discusses at length the problem of nonstationarity and continual learning at the same time. Although these problems are connected, I think it is important to distinguish between these two. With the problem of nonstationarity alone, one can see the catastrophic forgetting problem entangled with the plasticity loss. The introduction says, for example: “Our empirical evaluations aim to split the philosophical difference between these perspectives. In the following sections, we will evaluate the ability of a learning algorithm to maintain plasticity in a continual supervised learning task, where we fix some image classification dataset (in our case, CIFAR10) and at fixed intervals apply a random transformation to the inputs and labels.” This difference can be illustrated as follows (the example is a toy illustration of a distinction). Imagine that we have trained a model on 180 degrees rotated MNIST symbols. Then we realised that it was wrong and we actually want it to work on non-rotated ones. We decided to continue training from the last checkpoint where we stopped training for 180 degrees rotated MNIST symbols. At the end, we realise that the performance of the model dropped by X per cent due to the problems in Figure 1. In this case, we are happy with catastrophic forgetting (and don’t aim for lifelong learning), but we are not happy with the loss of performance. To address this point, two actions are suggested: (1) disentangling distribution nonstationarity problem in the introduction (2) calculating the baseline of the last task and all tasks performance: in Figure 6, how would the proposed changes affect the performance if we learnt the whole WiLDS dataset in a stationary distribution fashion? How would the proposed changes affect the performance on just the last task?

Q2. In Figure 6, not sure I understand how is the relative performance calculated? Is it calculated for the most recent task, for all tasks, and relative to what?

Q3. Figure 2, top left: should the axes have values? Does it also make sense to report fraction, not the absolute number?

Q4. “Mild L2 regularization (we use a value of 1e-5) is sufficient to resolve this issue in all three architectures.” Why this choice of the hyperparameter?

Q5. *“this analysis will provide a novel explanation of why units die off.”* Although I see the authors point, I’m not sure it’s an entirely correct description of the contribution. Sections 3.1 and 3.2 indeed shed the light on the process of dying out, but they do so through summarising evidence from existing works, i.e. Lin et al, 2016. What is the contribution is that the authors summarise a number of reasons for loss of plasticity and give the pathways towards improving plasticity.  Or am I missing anything?

Q6. “While saturated units have received much attention as a factor in plasticity loss, the accumulation of effectively-linear units has not previously been studied in the context of continual learning.” Not sure it fully covers such accumulation in the context of continual learning, as I mentioned in Q1 as the task itself does involve learning in face of nonstationarity but not tackling the question whether and how the previously accumulated knowledge should be used (or discarded). Would it be possible to contrast the added aspects of continual learning to previous works, such as Montufar (2013), in this analysis? 

Q7: Does different types of layer normalisation (batch normalisation, layer normalisation provide different impact?) Did the authors compare between those different remedies?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the problem of plasticity loss in neural networks trained on nonstationary learning problems. The paper conducted a series of experiments and analyses, identifying different mechanisms of plasticity loss, including saturation of nonlinearities, dead neurons, norm growth, and output sensitivity. Consequently, the paper shows that a combination of layer normalization and L2 regularization is a robust mechanism for mitigating all the aforementioned issues. The approach has been validated in an RL setting and on the WiLDS benchmark.

### Strengths
- The writing of this paper is very clear and easy to follow.
- The authors conduct a fine-grained empirical analysis of plasticity loss (4 different mechanism, 3 different architectures) and provide detailed explanations on how to interpret them. 
-  The authors proposed a training protocol (LN + L2 regularization) for mitigating the plasticity loss.

### Weaknesses
The contribution and novelty of the paper are a bit difficult to identify, especially considering previous work such as Lyle et al. 2023 (also cited in this paper), which indicates that factors such as dead units or weight norm may not fully explain the loss of plasticity in learning. Furthermore, normalization and L2 regularization have been studied in the past and are known as ways to prevent plasticity loss (for example, LN was studied in Lyle et al. 2023). Maybe try to extend the current work to a wider RL settings, or focusing on identify newer plasticity loss mechanisms would be better.

Some of the experiments could be questionable or appear to be missing. For example, why is there no L2 regularization used in Figure 6 left (the RL experiments with C51)? Is using a small learning rate equivalent to using a large learning rate? Is using a wider network the same as using a narrower one?

### Questions
Please see weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
