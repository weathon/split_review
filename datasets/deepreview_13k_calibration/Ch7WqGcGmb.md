# Error Feedback Reloaded: From Quadratic to Arithmetic Mean of Smoothness Constants

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 3, 8, 6

## Abstract
Error Feedback (\algname{EF}) is a highly popular and immensely effective mechanism for fixing convergence issues which arise in distributed training methods (such as distributed \algname{GD} or \algname{SGD}) when these are enhanced with greedy communication compression techniques such as TopK. While \algname{EF} was proposed almost a decade ago~\citep{Seide2014}, and despite concentrated effort by the community to advance the theoretical understanding of this mechanism, there is still a lot to explore. In this work we study a modern form of error feedback called \algname{EF21}~\citep{EF21} which offers the currently best-known theoretical guarantees, under the weakest assumptions, and also works well in practice. In particular, while the theoretical communication complexity of \algname{EF21} depends on the {\em quadratic mean} of certain smoothness parameters, we improve this dependence to their {\em arithmetic mean}, which is always smaller, and can be substantially smaller, especially in heterogeneous data regimes. We take the reader on a journey of our discovery process. Starting with the idea of applying \algname{EF21} to an equivalent reformulation of the underlying problem which (unfortunately) requires (often impractical) machine {\em cloning}, we continue to the discovery of a new {\em weighted} version of \algname{EF21} which can (fortunately) be executed without any cloning, and finally circle back to an improved {\em analysis} of the original \algname{EF21} method. While this development applies to the simplest form of \algname{EF21}, our approach naturally extends to more elaborate variants involving stochastic gradients and partial participation. Further, our technique improves the best-known theory of \algname{EF21} in the {\em rare features} regime~\citep{EF21-RF}. Finally, we validate our theoretical findings with suitable experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Error Feedback (EF) uses contractive compressors to improve distributed training methods. EF has been around for almost a decade(Siede et al 2014), and suitable theory had been developed for its variant EF21 (Richtárik et al 2021). In this work, the authors improve the analysis of EF21 by allowing for larger step sizes through a refined analysis of varying smoothness constants of the different client loss, leading to an improvement from the quadratic mean to the arithmetic mean of the respective constants.
They describe how they came up with this idea, and by doing this they propose a variant of EF21 called EF21-W which weights the different client gradient inversely proportional to their smoothness constant. They also provide n improved analysis of EF21 is achieved by extending an analogous analysis of EF21-W.
In the supplementary material they extend the algorithm to more advanced versions like EF21 SGD which uses stochastic gradients instead of gradients and EF21 PP which requires partial participation of clients. The authors also provide experimental results for logistic regression with non-convex regularization. They show significant improvement for largely varying smoothness constants and very limited improvements for more balanced cases.

### Strengths
The paper is very well written, in particular, the narrative that led the authors to the results is instructive and plausible. The claimed convergence theory is rather exhaustive and applies under quite general assumptions (Assumptions 1-3 only require bounds on the smoothness constants and a lower bound on the optimal function value; a version of the results that leads to linear convergence uses Assumption 4, Polyak-Lojasiewicz inequality, which is a rather weak condition for linear convergence). The improvement in the admissible stepsize for EF21 will be potentially relevant for distributed optimization with largely varying smoothness constants. Furthermore, the authors also provide versions of their algorithms in the stochastic setting (EF21-SGD) and a setting of partial participation (EF-21PP).

### Weaknesses
From their theory and experiments, it remains unclear whether the Improvement of the results are coming from the provably larger admissible step size or from different weighting of the clients (as in EF21-W) -- the experiments only seem to compare EF21 with the original stepsize to EF21-W with the improved stepsize (similarly, EF21-W-SGD vs. EF21-SGD).
Furthermore, the novelty of the underlying ideas is not sufficiently discussed. In particular, the usage of differently weighted clients’ gradients based on Lipschitz constants seems to be very related to similar ideas used in importance sampling fro stochastic optimization. (e.g., Zhao, P., & Zhang, T., "Stochastic optimization with importance sampling for regularized loss minimization", ICML 2015). Ideally, a discussion of the connection of their work with this body of literature should be part of the paper.

### Questions
- Can you provide experiments that clarify whether the improvement of the results in the setting of largely varying smoothness constants is coming from larger admissible step size or from the different weighting of the clients?
- Please include a discussion of the connection between the idea underlying EF21-W and importance sampling.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new weighted version of EF21 with better theoretical guarantees. Experiments show that the proposed EF21-W outperforms the baselines.

### Strengths
1. This paper proposes a new weighted version of EF21 with better theoretical guarantees. 

2. Experiments show that the proposed EF21-W outperforms the baselines.

### Weaknesses
1. It seems that the proposed EF21-W is simply a method that uses the local smoothness constants to obtain a weighted average of the local gradients sent by the workers, which actually has nothing to do with EF21. I mean, if we totally remove the communication compression and EF21 parts, we could still obtain a distributed gradient descent algorithms with weighted average of gradients on the server side and the same improvement in the theoretical results (from quadratic mean to arithmetic mean of the smoothness constants). Adding communication compression and EF21 seems too deliberate to me and prevents the paper from presenting the core idea in a clean and crispy manner.

2. The experiments seem too simple and small to me. I mean, the linear/logistic regression models on libsvm datasets could be easily trained in a short time on some modern and cheap hardware such as a normal laptop, which doesn't require distributed training or communication at all. I understand these experiments are meant to verify the theoretical results, but the experiment settings are just too simple and synthetic, which makes the experiments seem meaningless to me.

3. The proposed algorithm, EF21-W is far from practical, since in real-world complicated models and training tasks, typically it is very difficult to obtain the smoothness constants, while the smoothness constants are essential for EF21-W.

### Questions
1. If we simply re-weight the gradients with $w_i$ in the gradient averaging without using communication compression or EF21, would we obtain the same improvement in the theoretical results (from quadratic mean to arithmetic mean of the smoothness constants)?

2. For the more complicated models or tasks, such as neural networks, how to obtain the smoothness constants and apply EF21-W?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents with a weighted version of EF21, a modern form of error feedback, which previously offers the best theoretical guarantees under the weakest assumptions. And the proposed weighted version of EF21 improved the dependence on the quadratic mean of certain smoothness parameters to their arithmetic mean. 

In addition to the detailed description of the weighted error feedback algorithms, this paper introduces the steps took to discover the weighted EF21, starting from adding one more client node to enhance the convergence rate in EF21, to generalizing the cloning idea, replacing the quadratic mean of the smoothness parameters to their arithmetic mean, improving convergence rate, to overcoming the shortcomings with cloning clients with weighted version of EF21. 

Finally, the paper conducted experiments on non-convex logistic regression on benchmark datasets and non-convex linear regression on synthetic datasets, showing a faster convergence rate in situations of high variance in smoothness constants.

### Strengths
This paper proposed an intuitive algorithm based on EF21, improving the convergence rate in cases of high variance in smoothness constants, taking the readers through the journey of discovering the algorithm. The process of discovery is clearly described in the paper with simple and effective examples. The math presented in the main paper is enough to clarify the core idea behind the algorithm, and more detailed explanations can be found in the appendix. After taking the readers through the discovery process, the paper presents with 2 sets of experiments conducted on the new algorithm, accompanied by clear figures illustrating the improvement of the algorithm over the original EF21.

### Weaknesses
This paper did not discuss the choices of compressor used in the experiments, as in the original paper of EF21. In the EF21 paper, experiments were conducted on fine-tuning k and the step sizes, which is overlooked in this paper. 

This paper conducted experiments under specific settings with limited explanation for the parameters chosen, such as the number of clients in each experiment.

### Questions
Why is top1 compressor chosen to be employed in all experiments? If the algorithm is designed for a specific setting, can that be clearly described in the paper?

Why is the number of clients set to be 1000 in the logistic regression experiments, and set to be 2000 in the linear regression experiments? Is it chosen for a specific problem setting? Will the algorithm behave differently with different number of clients?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors offers a refined analysis of the popular EF21 algorithm to show that this algorithm actually depends on the arithmetic mean of Lipschitz constants instead of the quadratic mean. In the process the authors also proposed new versions of EF21, and showed that this analysis can be extended to a wide variety of EF21 variants.

### Strengths
1. Improves theoretical understanding of existing popular approach.
2. Presentation is very clear, and easy to follow
3. Contribution is meaningful, because it further promotes the use of EF21 under certain cases.

### Weaknesses
1. Did not propose a newer version of EF21 that outperforms the original one (probably not a weakness, but more of a hope)

### Questions
N/A

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
