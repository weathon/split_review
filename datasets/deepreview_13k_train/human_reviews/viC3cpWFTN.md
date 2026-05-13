# Clip21: Error Feedback for Gradient Clipping

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Motivated by the increasing popularity and importance of large-scale training under differential privacy (DP) constraints, we study distributed gradient methods with {\em gradient clipping}, i.e., clipping applied to the gradients computed from local information at the nodes. While gradient clipping is an essential tool for injecting formal DP guarantees into gradient-based methods~\citep{abadi2016deep}, it also induces bias which causes serious convergence issues specific to the distributed setting. Inspired by  recent progress in the error-feedback literature which is focused on taming the bias/error introduced by communication compression operators such as Top-$k$~\citep{richtarik2021ef21}, and  mathematical similarities between the clipping operator and contractive compression operators, we design \algname{Clip21} -- the first provably effective and practically useful error feedback mechanism for distributed methods with gradient clipping. We prove that our method converges at the same $\cO(\nicefrac{1}{K})$ rate as distributed gradient descent in the smooth nonconvex regime, which improves the previous best $\cO(\nicefrac{1}{\sqrt{K}})$ rate which was obtained under significantly stronger assumptions.
Our method converges significantly faster in practice than competing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper the authors study the convergence of Gradient Descent (GD) for the optimization of sum of functions $f:=\frac{1}{n}\sum_{i=1}^if_i(x_i)$ (which arises naturally in Empirical Risk Minimization) when each of the individual gradient $\nabla_xf_i(x)$ is clipped. They assume Lipschitz gradient. Their contribution are the following:
* naive gradient clipping fail convergence in simple cases, even on mean-estimation tasks
* by fixing the mean estimation task with clipped gradients, it is possible to fix GD+clipping algorithm itself
* different variants are proposed, with their own rates  
  
The results are illustrated on logistic regression, *with* and *without* convex regularization (i.e. with a convex and a non-convex task). Importantly, the work generalizes the n=1 case, and retrieve the same rates as existing literature for n=1.

### Strengths
### Clarity
The paper is extremely well written. The position of this work to the related work is clear. The problem is clearly stated. There are very convincing examples, progressive explanations of the proof strategies, and the "right level" of details.  

### Significance & Quality
Elementwise Gradient clipping is widespread in the Differential Privacy literature; therefore these theoretical results are significant. The hypothesis on $f$ are realistic even in the context of deep learning, making the paper relevant for the community.

### Weaknesses
## Practical relevance

While the paper is well written and provide interesting insights, I have a few concerns about its usefulness *in practice*.

### Relevance to Differential Privacy

Element-wise gradient clipping is typically used DP-SGD (Abadi et al, 2016). DP-SGD uses clipping to control the sensitivity of gradient steps. Then DP-SGD adds a Gaussian noise to the clipped gradient to create a Gaussian mechanism. In Alg 1, the clipped vectors are aggregated, but the influence of a noise $\zeta_i$ on the mean estimate $\frac{1}{n}\sum_iv_i$ is not studied, therefore it is not clear if this algorithm would work in the context of differential privacy.  The paper does not address how the error introduced by clipping interacts with the noise addition required for DP, which is a critical consideration for practical DP-SGD implementations.

### Relevance for exploding gradients

As written in the paper:

> we are not employing clipping as a tool for taming the exploding gradients problem, and our work is fully complementary to this literature. [...] Clipping after averaging does not cause the severe bias and divergence issues we are addressing in our work.

While the authors correctly state that their focus is not on exploding gradients, the practical relevance of clipping is often tied to this issue. The paper's analysis does not explicitly connect to scenarios where gradient magnitudes are highly variable, which is a common motivation for using clipping in deep learning. The $(L_0, L_1)$ smoothness condition is mentioned, but a more detailed discussion of how the proposed method behaves under such conditions, and how it compares to other methods designed for exploding gradients, would be beneficial.

## Comparison against vanilla GD

The paper positions itself against the Clip-GD algorithm (among others... ), in all experiments. But experiments with comparison against **vanilla GD** are lacking.  

### Conclusion

See my question below.

### questions:
 ### When do we care about the average ?  
  
This is a high level question.  
    
The idea of Algorithm 1 is to estimate the average $\frac{1}{n}\sum_ia_i$ *exactly*. Clipping may help to circumvent instabilities when some individual gradients $a_i$ are too high (whetever the reason, exploding gradient being an example, numerical inaccuracies another). In this case, **biasing the average direction** with clipping *is* the wanted behavior, since we don't want the descent step to be driven by a single example with exceedingly large gradient norm. The average operator $\bar a:=a\mapsto \frac{1}{n}\sum_ia_i$ is not robust by definition against outliers. 

By building an estimator of this average operator $\bar a$, aren't we falling back to the issues the average operator $\bar a$ was suffering in the first place?  The paper does not provide a clear justification for why estimating the average of clipped gradients is a desirable objective in scenarios where the unclipped gradients are highly variable or contain outliers. It would be useful to discuss the trade-offs between the bias introduced by clipping and the potential benefits of a more stable average.

### Comparison against vanilla GD
  
Can you clarify what are the use-cases in which Clip21-GD overcomes **vanilla GD** (and not only Clip-GD) ? What makes your algorithm different from vanilla GD in practice? Experiments are lacking to compare against it.    The lack of comparison against vanilla GD makes it difficult to assess the practical advantages of the proposed method. It's unclear if the added complexity of Clip21-GD is justified compared to standard gradient descent, especially when the clipping is not needed for stability.

### Typo
For citations, for example a top of page 5, I recommand to use `\citep{}` instead of `\cite{}`, for example in `Richt ´arik et al. (2021); Fatkhullin et al. (2021); Richt ´arik et al. (2022),`.  

> it will become “inactive” in at most k⋆ steps (i.e., ∇fi(xk) − vik−1 ≤ τ  

Missing `)`. 


### Questions
### When do we care about the average ?  
  
This is a high level question.  
    
The idea of Algorithm 1 is to estimate the average $\frac{1}{n}\sum_ia_i$ *exactly*. Clipping may help to circumvent instabilities when some individual gradients $a_i$ are too high (whetever the reason, exploding gradient being an example, numerical inaccuracies another). In this case, **biasing the average direction** with clipping *is* the wanted behavior, since we don't want the descent step to be driven by a single example with exceedingly large gradient norm. The average operator $\bar a:=a\mapsto \frac{1}{n}\sum_ia_i$ is not robust by definition against outliers. 

By building an estimator of this average operator $\bar a$, aren't we falling back to the issues the average operator $\bar a$ was suffering in the first place?  

### Comparison against vanilla GD
  
Can you clarify what are the use-cases in which Clip21-GD overcomes **vanilla GD** (and not only Clip-GD) ? What makes your algorithm different from vanilla GD in practice? Experiments are lacking to compare against it.    

### Typo
For citations, for example a top of page 5, I recommand to use `\citep{}` instead of `\cite{}`, for example in `Richt ´arik et al. (2021); Fatkhullin et al. (2021); Richt ´arik et al. (2022),`.  

> it will become “inactive” in at most k⋆ steps (i.e., ∇fi(xk) − vik−1 ≤ τ  

Missing `)`.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article presents Clip21-GD, a new  client-side gradient clipping algorithm designed for distributed training. The inspiration for Clip21-GD is drawn from the error feedback mechanism EF-21, employed to accelerate the convergence of gradient-compression distributed optimization algorithms. Notably, Clip21-GD achieves a convergence rate of $O(1/K)$, the same as standard distributed Gradient Descent (GD), and provides a more refined theoretical convergence analysis compared to EF-21, highlighting distinctions between clipping and compression operations.

### Strengths
-The theoretical convergence analysis for Clip21-GD is a strong point, as it reveals valuable insights. The theoretical $O(1/K) $ convergence rate surpasses that of the CE-FedAvg, signifying faster convergence.

### Weaknesses
- The article's motivation may need further clarity. While it claims to address the importance of deep neural network (DNN) training, the use of gradient descent (GD) in Clip-GD may appear unsuitable for DNNs. While Clip-SGD is briefly mentioned in the appendix for VGG 11 training, its theoretical convergence rate is not thoroughly explored in the main text, leaving room for ambiguity. The theoretical analysis focuses on deterministic gradients, which is a significant departure from the stochastic gradients used in DNN training. The lack of a clear theoretical connection between Clip21-GD and its stochastic counterpart, Clip21-SGD, weakens the motivation for applying Clip21-GD to DNNs.

- The necessity of a client-side gradient clipping algorithm is not sufficiently explained. The implementation of clipping the average gradient of clients on the server side may seem more straightforward and effective in managing explosive gradients to prevent convergence issues. The paper does not sufficiently justify why client-side clipping is superior to server-side clipping, especially considering the added complexity of implementation and the potential for increased communication overhead. A more detailed analysis of the trade-offs between client-side and server-side clipping is needed.

- The article's disclosure that gradient clipping in Clip21-GD will not work after a specific number of steps ($K=O(1/\tau)$) raises questions about the algorithm's practicality and long-term effectiveness. The purpose and usability of Clip21-GD beyond this threshold remain unclear. This limitation is a significant concern, as it restricts the applicability of the algorithm to a finite number of iterations. The paper should provide a more thorough discussion of the implications of this limitation and potential strategies for mitigating its impact.

### Questions
The article's disclosure that gradient clipping in Clip21-GD will not work after a specific number of steps ($K=O(1/\tau)$) raises questions about the algorithm's practicality and long-term effectiveness. The purpose and usability of Clip21-GD beyond this threshold remain unclear.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Gradient clipping is a commonly-used technique in training deep neural networks to resolve the exploding gradient issue. This paper shows that in a distributed setting, naively clipping the client gradient would result in large estimation error. To overcome this challenge, this paper proposes the Clip21 mechanism inspired by the error-feedback framework. The authors establish theoretical guarantee for the convergence rate of Clip21 to stationary points, and the rate is faster than previous works. Finally, experiments are conducted to demonstrate the efficiency of the proposed approach.

### Strengths
1) The Clip21 method proposed in this paper seems to be novel. Although there are previous works on the error-feedback framework, none considers the setting of clipped gradients.

2) The authors establish rigorous theoretical analysis for Clip21 under standard assumptions. Notably, heterogeneous client objective functions are allowed.

3) Overall speaking, the paper is well written and all definitions and theorem are stated clearly.

### Weaknesses
1) While gradient clipping is originally known to solve the exploding gradient problem, it seems not reflected in theoretical analysis of this paper. This paper still considers the standard $L$-smooth setting rather than $(L_0,L_1)$-smoothness, so the benefit of using clipped gradients is unclear from the theory. Specifically, the analysis does not account for the potential of the gradient norm to grow unboundedly, a situation that gradient clipping is designed to mitigate. The theoretical results should ideally demonstrate how clipping addresses this issue, perhaps by showing a bound on the gradient norm or a convergence rate that is robust to large gradients. The current analysis, however, does not seem to leverage the clipping operation to achieve any advantage over standard gradient descent under $L$-smoothness. 

2) This paper only considers the case for deterministic gradients. Although it is expected that similar results hold for stochastic gradients, in the gradient clipping literature more restrictive assumptions are made on noise (bounded noise rather than the more standard bounded variance, see e.g. [1]). It is unclear whether gradient noise is an issue in the distributed setting. The analysis should consider the impact of stochastic gradients, particularly in the context of distributed optimization where the noise characteristics can be significantly different from the centralized setting. The current analysis does not address whether the clipping operation interacts with stochastic noise in a way that would affect convergence, or whether the error-feedback mechanism is robust to stochasticity. 

[1] Zhang, J., He, T., Sra, S., & Jadbabaie, A. (2019). Why gradient clipping accelerates training: A theoretical justification for adaptivity. arXiv preprint arXiv:1905.11881.

### Questions
1) In your Example 1.1, what if one chooses different clipping thresholds for different clients, or use a 'soft clipping' $\nabla f(x)/(\|\nabla f(x)\|+a)$? In these cases the clipped gradient does not seem to cancel out.

2) (related to weaknesses 1) What is the motivation of considering gradient clipping at the client level? Because in a distributed setting, one only wants to optimize the averaged objective function, can we just clipp the averaged gradient at the server to accelerate training? If you clip the server's gradient instead of the clients, then the problem demonstrated by Example 1.1 does not exist, and there may be a more straightforward approach.

I am willing to increase my rating if my concerns are properly addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
