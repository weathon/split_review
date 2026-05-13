# Dropout-Based Rashomon Set Exploration for Efficient Predictive Multiplicity Estimation

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Predictive multiplicity refers to the phenomenon in which classification tasks may admit multiple competing models that achieve almost-equally-optimal performance, yet generate conflicting outputs for individual samples.
This presents significant concerns, as it can potentially result in systemic exclusion, inexplicable discrimination, and unfairness in practical applications.
Measuring and mitigating predictive multiplicity, however, is computationally challenging due to the need to explore all such almost-equally-optimal models, known as the Rashomon set, in potentially huge hypothesis spaces. 
To address this challenge, we propose a novel framework that utilizes dropout techniques for exploring models in the Rashomon set.
We provide rigorous theoretical derivations to connect the dropout parameters to properties of the Rashomon set, and empirically evaluate our framework through extensive experimentation.
Numerical results show that our technique consistently outperforms baselines in terms of the effectiveness of predictive multiplicity metric estimation, with runtime speedup up to $20\times \sim 5000\times$.
With efficient Rashomon set exploration and metric estimation, mitigation of predictive multiplicity is then achieved through dropout ensemble and model selection.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of how to measure and mitigate predictive multiplicity.
To achieve them, the authors utilize the dropout technique to explore the models in the Rashomon set.
Rigorous theoretical analysis is provided to connect dropout and Rashomon set.
Numerical results demonstrate the effectiveness of the proposed method.

### Strengths
1. The proposed method is simple, straightforward, and well-motivated. Utilizing the dropout technique to explore the models in the Rashomon set is interesting.
2. Rigorous theoretical analysis is provided to connect dropout and Rashomon set.
3. The paper is well-written and well-organized. The authors first show the implementations on linear models and extend them to feedforward neural networks. 
4. The limitations and potential solutions are also discussed in the paper.

### Weaknesses
1. In the experiments, the authors mentioned that "On the other hand, AWP outperforms both dropouts and re-training, since it adversarially searches the models that mostly flip the decisions toward all possible classes for each sample." I may miss some details of the method part, how can the proposed method to adversarially search the models since the dropout is random?
2. As mentioned by the authors, good performance comes at the cost of efficiency.

### Questions
1. It seems the proposed method is only evaluated on in-distribution scenarios. Can it be applied to out-of-distribution data?
2. Are the uncertainty scores calibrated? In other words, are the confidence scores reliable?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper described a Rashomon set exploration method through Drop-out with probabilistic bound. The paper starts with fairly well-covered literature of Rashomon set research and motivates its proposal by pointing out the computation cost of existing empirical solution (re-training, AWP). The solution is fairly simple by adopting Drop-out where Rashomon set likely rests. Probably the most significant part of this paper (theoretically) would be pointing out the probabilistic bound of Rashomon set under Drop-out. Empirical results show the proposed method is computationally efficient than previous solutions and even showing better divergence metric than retraining.

### Strengths
1. Predictive multiplicity itself is an interesting topic that worths more investigation. The method proposed in this work is a great complement of existing literature in this field.
2. The paper is well written and motivated. It comes with sufficient background knowledge to understand the gap in the literature.
3. Potential application of this approach is covered in Section 5, which is good since I was concerning where people can use this innovation in their work.

### Weaknesses
1. Model augmented by Dropout could result in a fairly small search space of Rashomon set. I am not very convinced that this is a good idea in practice if our goal is to look for a better model that can address various reliability problem of predictive model. e.g. fairness etc. It maybe inspirational to see the movement of predictive multiplicity measurement, but I am wondering what is the practical meaning of it. Specifically, the use of dropout, while computationally efficient, might severely limit the diversity of models explored within the Rashomon set. This could lead to an underestimation of the true predictive multiplicity and a limited ability to find models that address issues like fairness or robustness, which often require exploring a much broader range of model parameters and architectures.
2. The paper demonstrates the effectiveness of the proposed method on toy datasets that were used for decades. As the paper concerns the efficiency of existing methods, I am wondering if the authors can introduce more realistic tasks to show the effectiveness of the proposed method quantitatively.  While COCO is good example, it is very qualitative without much statistic support. The reliance on small, well-trodden datasets like those from UCI, while common in early predictive multiplicity research, does not sufficiently demonstrate the method's applicability to real-world scenarios. The inclusion of CIFAR-10/-100 is a step in the right direction, but the quantitative results are not as compelling as they could be. The COCO example, while visually appealing, lacks the statistical rigor needed to support the claims of efficiency and effectiveness. More complex and diverse datasets, along with more detailed quantitative analysis, are needed to fully validate the proposed approach.
3. There is a descriptive gap in section 3.2 where transforming deviation between $L_{SSE}(\mathbf{w}_D^*)$ and $L_{SSE}(\mathbf{w})$ suddenly become  deviation between  $L_{SSE}(\mathbf{w}_D^*)$ and $L_{SSE}(\mathbf{w}')$. I don't quite see why they are aligned or if the model works correctly under $L_{SSE}(\mathbf{w}')$ if it is not trained with such dropout rate.

### Questions
The proposition 1 uses deviation between  $L_{SSE}(\mathbf{w}_D^*)$ and $L_{SSE}(\mathbf{w}')$ but not original model parameter $L_{SSE}(\mathbf{w}')$. How to make the connection ?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the possibility of using Dropout to explore the Rashomon set. It proves that for a FFNN, we could bound the probability that a Dropout realization is in a certain Rashomon set. In experiments it shows that the proposed the method does not explore the Rashomon set as effectively as AWP (as measured by several predictive multiplicity metrics), but is much faster as it does not retrain any model.

### Strengths
1. This paper establishes some theoretical bounds (although seemingly loose) on the probability that FFNNs with Dropout are in the corresponding Rashomon Set.
2. The proposes method is easy to implement.

### Weaknesses
1. It is unclear what's the practical use of the propose method. It is fast, but it does not explore the Rashomon set well. For this reason, we can only mitigate predictive multiplicity *as estimated by Dropout* but not in general. 
2. Following 1, it seems like additional experiments on whether the mitigation via Dropout also transfers to, say, AWP, is interesting. 
3. The bounds in Proposition 2 and 3 only converge to 1 when $d\to\infty$, which does not seem like useful. See Q3 as well.
4. It is not clear why a concentration bound helps. Notably, in applications, we want the models that are in the Rashomon set but closer to the boundary. In fact, it seems like in practice we need to sample a few weights and empirically verify that they have low loss (?). If so, a concentrated distribution, especially one that's more concentrated when the dim of the model increases, seems like a bad feature. A method that samples very diverse model that potentially has a higher probability of falling outside the Rashomon set seems more desirable.

### Questions
1. AWP is slower due to re-training, but the models are trained only once. Therefore, doesn't it run *faster* than Dropout (because it uses fewer samples/models to explore the Rashomon set) with a reasonably large test data?
2. What does "5 models" mean in Figure 4b? 5 different base weights, or 5 different architectures?
3. Is $\epsilon$ and the $L$ in Eq.(5), (7) and (10) related to the "sum" of loss or the "mean" of loss? It seems like it's the sum? If so, by changing $\epsilon$ to some offset on the mean loss, we can probably get a convergence basing on the sample size, which is much more meaningful than dimension of the model's hidden layers.

### Soundness
3 good

### Presentation
2 fair

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
This paper’s main goal is to explore Rashomon sets of feed-forward neural networks with the help of dropout. Both Gaussian and Bernoulli dropouts are considered, the former involving the addition of noise to the weights of the networks. The approach is used to estimate the Rashomon set, and proof of the consistency of the approach is provided. Empirical results show the effectiveness of the approach on various datasets.

### Strengths
The idea is intuitive. It leads to impressive computation time saving compared to other approaches from the literature. The article is well-written and clear. The experiments are directly in line with the motivations of the work (ethical concerns).

### Weaknesses
 **Major**

1.1 – The biggest weakness of the approach concerns its limitations. As honestly discussed by the authors in Section 6 – Limitations, the fact that when the hypothesis space to explore is huge (that is when the predictor has many parameters to tune), the exploration that is done by the dropout approach is fairly limited. This is clearly related to Proposition 4, where an important value of $M$ is necessary for layers having hundreds of neurons and an important value of $k$ is necessary with complex neural networks. The authors acknowledge that the dropout method explores a smaller subset of the Rashomon set compared to retraining, which could lead to an underestimation of the predictive multiplicity. However, the degree of this underestimation and its impact on the conclusions are not thoroughly investigated. A more detailed analysis of how the limited exploration affects the reliability of the estimated multiplicity metrics is needed.

1.2 – Two scenarios could occur: the first one is that the hypothesis space to explore is relatively small. That is, it is fairly explored by the dropout method. But, even though a 30x to 5000x speedup over other approaches is seen, it is never defended that those other approaches are not scalable with small hypothesis space. Even though there is a huge speedup gain, if the other approaches are relatively fast (do not take hours to compute), then why favourising dropout? The second scenario is that the hypothesis space to explore is large. The time gain is then undermined by the limitation in the exploration. Plus, when it comes to large models, it is common to retrain only the classification head of the predictor, or to fix many layers; doing so could really fasten the retraining scheme, thus undermining the potential advantage of the dropout approach. The paper should include a more detailed discussion on the computational cost of retraining and AWP in the context of smaller hypothesis spaces and partial retraining, and how the dropout method compares in these scenarios.

2 – It seems to me that both the depiction in Figure 2 and the speedup reported in Table 1 are lacking important details. For example: How many different models are sought? How many reruns were done for retraining VS how many dropouts were computed? What was the total time for each individual method? To my understanding, many reruns are already needed in the first place, no matter the approach, in order to ensure that the reference model is an « empirical minimizer »; was that taken into account when comparing the time for building the empirical Rashomon sets in Table 1? What was the size of the predictor used on these different UCI tasks (this kind of information is necessary in the main article, not the supplementary material)? The paper needs to clarify whether the time for obtaining the initial empirical minimizer is included in the reported speedups. Furthermore, the number of models generated for each method and the specific architecture used in the UCI experiments should be included in the main text for better reproducibility and understanding.

3 – I feel like something is conceptually wrong with the comparison between retraining and the current dropout scheme. Retraining makes it such that the validation loss is the highest possible. Therefore, it makes sense that many runs are needed in order to find models close to the « empirical minimizer ». With the dropout scheme, an empirical minimizer is found, and then dropout is applied while making sure the training loss does not diminish too much. The two approaches do not have the same objectives. The paper should clarify that the goal of retraining is to find models within a certain loss threshold of the empirical minimizer, not to maximize the validation loss. The comparison should be framed in terms of exploring the Rashomon set, not in terms of optimizing validation loss.

4.1 - The dropout leads to a scheme where each new model depends on the initial model. All of the models are thus dependent. Therefore, the estimation of the Rashomon metrics is biased. And while « not all estimators of predictive multiplicity metrics carry a theoretical analysis of its statistical properties such as consistency and sample complex », I feel like it is a property of interest. Indeed, one of the motivations of the work is the need for ethics and, more specifically, fairness. I see the goal in exploring the Rashomon sets to find many predictors giving different predictions to people for different reasons. But having all of the models interconnected makes it such that the reasons for the predictions are all linked and just a few are explored with the dropout scheme. The paper needs to address the potential bias introduced by the dependence between models generated by the dropout method and discuss the implications for the reliability of the estimated multiplicity metrics, especially in the context of fairness and ethical considerations.

4.2 – Proposition 5 aims at proving that the approach is not biased, but relies on the assumption that «  the models around W∗ are uniformly distributed in a d-dimensional ball with center $\mathbf{W}^*$ and radius $\delta$, i.e., $B(\mathbf{W}^*, \delta)$. Accordingly, we may assume that the population means $\mu$ for a sample can be expressed as [...] ». The method explicitly does that (especially the Gaussian dropout), exploring around the « population mean », that is, the empirical minimizer. Therefore, assuming the uniform distribution of the Rashomon set around a center trivially leads to the unbiasedness of the dropout scheme, but is unreasonable. The paper should acknowledge that the uniform distribution assumption is a simplification and discuss its limitations. The theoretical analysis should be extended to consider more realistic distributions of models in the Rashomon set.

**Minor**

1 – Typo: « Moreover, as lone as »

### Questions
1 – It is said that « not all estimators of predictive multiplicity metrics carry a theoretical analysis of its statistical properties such as consistency and sample complex » Could you provide some citation supporting this claim?

2 – What justifies fixing a single Bernoulli or a Gaussian dropout parameter for all layers simultaneously? Shouldn’t the layers be treated independently?

3 – Concerning the quantification of predictive multiplicity, it is said that « [f]or example, Long et al. [2023], Cooper et al. [2023] and Watson-Daniels et al. [2023] quantify predictive multiplicity by the standard deviation, variance and the largest possible difference of the scores (termed viable prediction range (VPR) therein) respectively » So, what definition between those three is retained in the article?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
