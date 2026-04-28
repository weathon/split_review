# Cost-Sensitive Multi-Fidelity Bayesian Optimization

- Decision: Reject
- Scores: 3, 5, 5, 5, 6

## Abstract
In this paper, we address the problem of cost-sensitive multi-fidelity Bayesian Optimization (BO) for efficient hyperparameter optimization (HPO). Specifically, we assume a scenario where users want to early-stop the BO when performance increase is not satisfactory with respect to the required computational cost. Motivated by this scenario, we introduce \emph{utility function}, which is predefined by each user and describes the trade-off between the required BO steps and the cumulative best performance during the BO. This utility function, combined with our novel acquisition function and the stopping criteria, allows us to dynamically choose for each BO step the best configuration that we expect to achieve the maximum utility in future, and also automatically stop the BO around the maximum utility. Further, we improve the sample efficiency of existing learning curve (LC) extrapolation methods (e.g., Prior Fitted Networks) with transfer learning, while successfully capturing the correlations between different configurations to develop a sensible surrogate function for multi-fidelity BO. We validate our algorithm on various LC datasets and found it outperform all the previous multi-fidelity BO baselines, achieving significantly better trade-off between cost and performance of multi-fidelity BO.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This manuscript seeks to address the problem of hyperparameter optimization particularly for the training of machine learning models which routinely provide low fidelity performance signals that can be leveraged to improve the efficiency of the optimization procedure. More specifically, this paper proposes numerous improvements to multi-fidelity Bayesian optimization (BO), including (i) a generalized notion of performance that accounts for cost and (ii) an acquisition function based on the expected improvement in the full trajectory of extrapolated future performance outcomes (rather than the typical one-step ahead outcome). The generalized performance, which the authors call "utility", can be specified analytically/parametrically, or otherwise learned from a user's preference. The authors further propose a cost-based stopping criterion for the BO procedure according to values of this "utility". Finally, the authors investigate the use of in-context learning frameworks such as prior-fitted networks (PFNs) to accurately extrapolate learning curves in a few-shot manner by transfer learning from curves of hyperparameter configurations from related tasks/datasets.

### Strengths
## Significance

This manuscripts seeks to simultaneously improves on various aspects of BO, including multi-task BO (warm-starting BO from related tasks), multi-fidelity BO (leveraging low fidelity performance signals), cost-aware BO, and also optimal stopping for BO, all in a coherent and unified manner. These aspects are timely and important long-standing open problems in BO. In spite of some potential shortcomings (identified below), some of the high-level ideas and concepts could readily translate to other multi-fidelity frameworks of this kind.

## Originality

This work proposes novelties in number of different components, e.g. in the acquisition function by a) generalizing the performance ($y$) to a quantity that is normalized/penalized by budget/cost (which they call a "utility" function), and also b) generalize this quantity to be based on extrapolated performances. Finally, c) to be able to accurately and efficiently carry out this extrapolation in a few-shot manner, they incorporate recent in-context learning approaches based on PFNs, which are trained on priors implicitly specified by benchmark datasets containing learning curve, and adapt augmentation strategies like mix-up to learning curve data to mitigate the possibility of overfitting.

### Weaknesses
## Quality

The technical quality of the proposed methodology could be improved. In particular, I found many aspects of the approach to be arbitrary and not well-motivated. For instance, for the stopping criterion described starting *line 250*, the choice of using the BetaCDF with parameters $\beta, \gamma > 0$ and probability $p$ as the probability of improvement (PI), beyond working fine empirically on the benchmark problems considered, seem highly convoluted and totally arbitrary to me.

A major concern I have in the empirical evaluation of the proposed method is in the "normalized regret of utility" (Eq. 3), which is the primary metric that is reported. Beyond being quite complicated to compute (evidenced by lines 417-420), it is also not obvious to me that this is the "holy grail" metric we should be aiming for in the first place. Does this metric not differ depending on the surrogate/extrapolation model of choice? Furthermore, I am unclear as to how this metric is even defined for other methods such as Random, BOHB, etc. which don't explicitly model the performance $y$, and in which it's unclear how the "utility" can be incorporated? I would be interested in seeing a more conventional plot showing the current best performance (or regret) along the vertical axis. 

Another concern is that the reported empirical results all display the BO iteration along the horizontal axis, which is highly misleading in the context of multi-fidelity BO. It seems to me that the notion of a BO step means totally different things in different frameworks. For instance, in BOHB, a BO step signifies training a model with a particular hyperparameter configuration to full completion, but in most cases they are trained for a fraction, e.g. 27/81 epochs, resulting in a *fractional* BO step (in this example 1/3rd of a BO step). In contrast, under the proposed framework, a BO step is the advancement of a configuration by a single epoch. Therefore, I am doubtful that the results presented show an apples-to-apples comparison.

Furthermore, in multi-fidelity BO just showing BO steps along the horizontal axis (fractional or otherwise) is not entirely informative either, especially when cost is of interest. In addition to fractional BO steps, I would like to see a plot with the wall-clock time along the horizontal axis.

## Clarity

A significant weakness of this paper is its lack of clarity, particularly in many parts of the paper (describing important technical details) which I found cryptic and difficult to parse. Some examples include:
- *lines 215-219* (details on learning curve extrapolation and how its used to compute the "BO performance")
- *lines 417-420* (details on computing bounds on the "utility") - this is indecipherable

More generally, this manuscript could benefit from more careful copy-editing. Some specific examples (non-exhaustive) of where writing quality could be improved are enumerated in the "Miscellaneous Remarks" section.


### Miscellaneous Remarks

- The overloaded use of the term "utility" is confusing as utility functions already plays a central role in Bayesian decision theory (of which Bayesian optimization is an special case [Garnett, 2023]). As such, statements such as "We call this trade-off utility" (*line 67*), "We introduce the concept of utility, ..." (*line 110*), and "We first introduce the detailed notion of utility function" (*lines 95-96*), are likely to raise eyebrows.
- *line 40* - "receives more attention"
- *line 77* - "hyperparamter"
- *line 78* - "improve it in future"
- *lines 84-86* - ?
- *line 98* - "a recently introduced"
- *line 107* - "a reasonable and stable way" -- "reasonable" the reader can probably infer but what makes a "utility" function "stable"?
- *line 77* - "hyperparmater"
- *line 161* - "surrogate function" -> "surrogate functions"
- *line 199-200* - the sign of the second term in the binary cross-entropy loss is wrong
- *line 431* - "despite of the transfer learning"
- *line 351* - "For easier transfer learning"
- *line 364* - "training epochs at future"
- *line 538* - "numerous empirical evidences"

### Questions
- *line 164* - The proposed method works with a fixed, finite pool of hyperparameters. Firstly, I would contend with the claim that this is the "convention" in BO, where it is arguable the exception rather than the rule. However, my biggest question is how this pool is populated in the first place? I would guess randomly, which begs the question of how comparisons are carried out against other methods in which this is not a common practice, e.g. BOHB? Furthermore, details are missing as to how many hyperparameter configurations there are in this pool. Fig 7c hints that this is around 10, which seems minute?
  - As you progress through the BO procedure and gain more information about the correlations between hyperparameter configurations, it is not really possible to leverage this knowledge to consider novel hyperparameter settings to evaluate meaning you're simply stuck with your initial pool. Do you directly compare against methods with this limitation imposed or not?
- Please clarify the question regarding "normalized regret of utility" (Eq. 3) raised above
- Please clarify the question regarding the horizontal axis raised above
- The ablation study concerning the use of mix-up is interesting (Fig 6). However, have you carried out an analysis to compare the standalone extrapolation performance of your proposed in-context LC curve prediction set-up (with/without mix-up) against more traditional approaches (that may be both simpler and cheaper)?
- *line 406* "Each column corresponds to the cherry-picked examples from each benchmark" - "cherry-picked" is a pejorative term used to describe the practice of isolating only the results that place your method in a good light and/or your competitor's in a bad light. Are the chosen results actually representative of all the other results you could have shown, or are they in fact cherry-picked? If so, we cannot rely upon these reported results to make an assessment of the proposed method!
- *line 446* - how special is the mix-up augmentation strategy? Could you obtain comparable results by fitting an emulator/surrogate model to be able to interpolate entire learning curves between hyperparameter configurations? This would also give you infinitely many training examples that would more accurately preserve correlations between the configurations; granted, it's relatively more expensive but still cheap in absolute terms.
- *line 183* ("utility" function) - It is unclear to me at what stage and exactly how you would elicit user preference data. By generating many pairs of performance-cost pairs upfront and having the user choose their preferences before proceeding with the optimization procedure I assume?
- *line 350* - "We select 23 tasks with 4 different hyperparameters based on [*sic*] SyneTune (Salinas et al., 2022) package" -- what does it mean to select tasks based on some package? You adopt the same set of tasks that they consider in their experimental benchmarks?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes CMBO, a cost-sensitive multi-fidelity BO methods, which target hyper-parameter tuning problems. CMBO is built upon freeze-thaw BO, which allows for pausing (freeze) the configuration run at intermediate epoch, and resuming (thaw) the run at with remaining epoch later. Specifically, CMBO introduces the utility function to account for the trade-off between the cost and performance of BO steps, then propose a EI-based acquisition function for this utility. CMBO’s optimization policy is based on maximizing the utility (the expectation of the proposed utility), instead of maximizing the validation performance as previous methods. Moreover, to support these steps, CMBO adopts Prior-fitted Network concept to extrapolate the learning curves (LC), which allows for computing the utility-based acquisition function.

### Strengths
-	The idea of extrapolating LC to compute the acquisition function (AF) sounds interesting to me.
-	The authors also improve the problem of PFN cannot be trained with dataset, and instead need prior distribution. The mixup strategy fixes this issue.
-	There are many analyses to support the results.
-	The ranking results in Tables 1, 3, 4 seem to be impressive.

### Weaknesses
-	It’s strange that the reported results are in terms of normalized regret of the utility U, which seems to be not common in the field. The utility is the term proposed by the authors. FSBO, ifBO and QuickTune seem to use the normalized regret of the function evaluation f(x).

### Questions
-	In Table 1, the results of baseline methods change when alpha changes. Is this because of the different normalized regret that I mentioned in the Weakness section? This is because alpha is a parameter of utility function, which only belongs to the proposed CMBO. Other methods, such as Random Search should not be affected by this parameter. Can the authors provide addition results - the normalized regret of evaluation values f(x) - as other baselines?

-	Are PFNs trained only once, or do we need to retrain PFN during CMBO? How does the training time of PFNs compare to the evaluation of a HPO epoch?

-	Minor: Can the authors explain more about the choice of PFNs? How about using Deep Gaussian Process as FSBO baseline?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work developed a new framework of multi-fidelity Bayesian optimization in consideration of budget/cost penalty. An improved acquisition function, as a variant of the expected improvement (EI), was proposed to represent the cost-performance utility of decision makers. The surrogate models were built by the learning curve extrapolation method in conjunction with a data augmentation strategy. Additionally, a stopping criterion was introduced to adaptively save the cost, thereby achieving best utility. Finally, the HPO experiments demonstrated the effectiveness and superiority of the framework.

### Strengths
1. The motivations are clear. Existing multi-fidelity optimization methods mainly assumed a given budget, little focusing on the active learning strategy with limited cost.
2. The solutions are innovative, including the improved acquisition function and the data augmentation strategy in transfer learning.
3. The experiments is well-organized to show the effectiveness and implications.

### Weaknesses
1. The presentation is not good enough. The utility function is hard to define and learn from noisy preference data. As aligning utility from preference learning was not performed in the experiments, a definition or assumption should be enough rather than trivial content from line 182 to line 201. On the other hand, the basic definition of multi-fidelity optimization problems were missing. It is not mentioned whether it is a maximization or minimization problem. This should be highly related to the design of utility function.
2. The solution, especially the improved acquisition function, may not work in cost-limited problems. This work only introduces the penalty rather than constraints. In other word, if there were cost constraints, this framework may not ensure the cost during search is within the constraints.
3. The experiment settings seem unfair. The metric was related to utility $U$, however, it is not clear whether other baselines considered $U$ as their objectives as well. If not, the comparison may be unfair due to different objectives.

### Questions
1. How to determine the hyperparameters in the framework, such as $\delta_b$ in the stopping criterion?
2. In line 412, why use different $\beta$ for the proposed method only?
3. Why not consider a bigger $\alpha$ and other format of cost independent of the budget number $b$?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces CMBO (Cost-sensitive Multi-fidelity Bayesian Optimization), a novel framework for hyperparameter optimization that explicitly considers the trade-off between computational cost and performance. The key innovation is the introduction of a utility function that captures user preferences regarding this trade-off, which can be learned from preference data. The method combines three main components: (1) a novel acquisition function that maximizes expected utility improvement, (2) an adaptive stopping criterion that determines when to terminate optimization based on utility saturation, and (3) a transfer learning approach using Prior-Fitted Networks (PFNs) with a novel mixup strategy for learning curve extrapolation. The authors evaluate their method on three benchmark datasets (LCBench, TaskSet, PD1) against several baseline methods, demonstrating superior performance especially in scenarios with strong cost penalties.

### Strengths
The technical approach is well-developed and carefully constructed. The paper provides detailed explanations of each component, including the mathematical formulations and algorithmic details.

The transfer learning component using PFNs with the proposed mixup strategy shows notable improvement in sample efficiency, which is particularly important for early-stage optimization decisions.

The paper addresses a practical concern in hyperparameter optimization - the need to balance performance gains against computational costs - that is relevant to many real-world applications.

### Weaknesses
The paper's fundamental premise regarding the novelty of considering cost-performance trade-offs in multi-fidelity BO is questionable. Many existing multi-fidelity acquisition functions already incorporate such trade-offs implicitly. The authors should better differentiate their approach from existing methods that handle exploration-exploitation balance.

The experimental comparisons may not be entirely fair, as some baselines do not incorporate transfer learning while the proposed method does. A more equitable comparison would include state-of-the-art transfer learning HPO methods.

The paper could benefit from a more thorough ablation study to isolate the contributions of different components, particularly to demonstrate whether the utility function provides benefits beyond what's already captured in traditional multi-fidelity acquisition functions. 

Also as a MFBO paper, the paper did not compare to SOTA MFBO methods like MFKG, CFKG, BOCA, MF-UCB.

The claim that existing multi-fidelity BO methods "tend to over-explore" (Line 53) is not well-substantiated and could be contested. The authors should provide empirical evidence for this claim or revise it.

### Questions
How does the proposed utility-based acquisition function fundamentally differ from existing multi-fidelity acquisition functions that already balance exploration and exploitation? Could you provide a detailed comparison with specific acquisition functions?

Have you considered comparing your method with non-myopic acquisition functions or RL-based approaches (e.g., work by Hsieh et al. 2021 or Dong et al. 2022) that might address similar concerns about long-term optimization strategy?

Could you provide additional ablation studies that:
- Compare the method without the utility function to isolate its contribution
- Evaluate the performance against other transfer learning HPO methods
- Demonstrate the individual impact of each component (acquisition function, stopping criterion, transfer learning)

The paper assumes users can effectively specify their preferences regarding the cost-performance trade-off. How sensitive is the method to misspecified preferences, and what guidance can be provided to users for setting these preferences effectively?

Could you clarify how the proposed method differs from simply annealing the exploration parameter in traditional acquisition functions? The current presentation makes it difficult to distinguish the novelty of your approach from this simpler alternative.

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
A new optimization objective, utility, is proposed in Bayesian optimization. Under this goal, the corresponding acquisition function, multi-fidelity strategy and stop strategy are reconstructed. Among the highlights, utility proposes that it is more suitable for scenarios where users need to balance precision requirements and computing overheads. When a large amount of resources are invested to improve only a small amount of precision, the optimization process can be terminated. As for large and small quantities of quantification, the author proposes a kind of quantitative definition of utility on the user side by allowing users to make choice feedback. Finally, under this index, the method presented in this paper shows excellent advantages.

### Strengths
1. The utility is closer to the actual user's consideration, rather than waiting for training convergence, which will waste a lot of computing resources, and the user only gets limited benefits.

2. The utility's quantification design is clever, allowing users to provide data through 2 out of 1 judgment, and then accurately estimate the quantification function. This design is easy to use and more suitable for users.

3. A large number of experiments are conducted under the utility criterion, and the method shows consistent superiority and stability.

### Weaknesses
1. Some words are not serious or well-founded, such as One may argue on line 55 and One may argue on line 65, saying that it is difficult for users to obtain the total budget and let users evaluate how to balance benefits and expenses.

2. Figure 2 is called true utility. I think the evaluation here is not true utility. Instead, the author assumes the model and estimates the parameters based on the data generated by the model (user data). However, if the data answered by the user does not match the model set by the author, the fitting effect is much worse.

3. In algorithm 1, if N is given here, how to solve the continuous parameter problem faced by traditional BO? It's supposed to be easy to perfect, but the author didn't do it in this version.

4. This paper explains the ins and outs of utility, but only regret is used as the core index during comparison. If the utility curves, termination points and subsequent trends of different algorithms can be compared, the advantages of the algorithm will be more intuitively understood.

### Questions
1. In Equation 2, the expression of b + t, b represents BO step, and t represents training epoch. How do they add up?

2. In algorithm 1, why is t updated in step 12?

3. In Equation 3, utility starts to decrease as bo progresses, so there should be a time when Umax=Uprev, and regret=0, but in the following experiments, there is no time when Umax=Uprev is equal to 0.

4. In equation 5, p_b > 0.5 stops. However, a larger p_b indicates a higher probability of subsequent utility. Why does this stop at this time?

5. Line 448: Multi-fidelity BOs are better than black-box BOs. However, multi-fidelity is not applicable in real industrial scenarios. Since black boxes are used, different epochs cannot be used to terminate the BOs. This statement is not appropriate.

### Soundness
3

### Presentation
2

### Contribution
4
