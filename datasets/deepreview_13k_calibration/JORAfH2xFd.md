# On the Stability of Iterative Retraining of Generative Models on their own Data

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 5, 8

## Abstract
\looseness-1
Deep generative models have made tremendous progress in modeling complex data, often exhibiting generation quality that surpasses a typical human's ability to discern the authenticity of samples. Undeniably, a key driver of this success is enabled by the massive amounts of web-scale data consumed by these models. Due to these models' striking performance and ease of availability, the web will inevitably be increasingly populated with synthetic content. Such a fact directly implies that future iterations of generative models will be trained on both clean and artificially generated data from past models. In this paper, we develop a framework to rigorously study the impact of training generative models on mixed datasets---from classical training on real data to self-consuming generative models trained on purely synthetic data. We first prove the stability of iterative training under the condition that the initial generative models approximate the data distribution well enough and the proportion of clean training data (w.r.t. synthetic data) is large enough. We empirically validate our theory on both synthetic and natural images by iteratively training normalizing flows and state-of-the-art diffusion models on CIFAR10 and FFHQ.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an analysis of iterative retraining of generative models on their own data. This is indeed a very tempting approach used in various fields. 

The analysis begins in a simple Gaussian case that enables the authors to provide intuition on the behavior of such a training method. 

The analysis then addresses two other cases: under no statistical error assumption were under inifinite sampling the stability and convergence can be retrieved.

### Strengths
The paper is clearly presented, the objectives are well stated and i believe that the authors propositions and lemma clearly answers their problematic.

The experiments seem conclusive.

### Weaknesses
see questions

My overall understanding of the field is limited. However i have a couple of questions:

1. How likely is assumption 3 ? can the authors provide example where such a bound stands ?
2. How is precision and recall computed in the experimental section ? what classifier is used here ?

### Questions
My overall understanding of the field is limited. However i have a couple of questions:

1. How likely is assumption 3 ? can the authors provide example where such a bound stands ?
2. How is precision and recall computed in the experimental section ? what classifier is used here ?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work authors focus on the problem of retraining the generative models with the combination of real and synthesised data coming from the previous state of the same model. With a series of theoretical derivations authors show that such a process is stable (under some assumptions). The theoretical theorems are also evaluated with additional empirical studies that seem to align with the main claims.

### Strengths
- To my knowledge this is the first work to study the theoretical stability of generative models when retrained on its own data. It is an interesting practical problem as soon we might struggle with distinguishing true training examples from fake synthetic images. This problem is well motivated in this submission.
- In the submission authors  provide theorems with proofs that shed a new light into the topic of continual retraining of generative models with self-generated data, showing that this process might be stable under the assumption of retraining the model with sufficient share of true data samples.
- This work might have some impact on theoretical fields of ML such as continual learning of generative models and practical aspects such as deployment of big diffusion models.
- This is one of the best written theoretical papers I have ever read. Everything is extremely clear and easy to follow. It reads as a good crime!

### Weaknesses
 - The contribution of the theoretical part has limited significance as it mostly concerns unfeasible setups with normally hard or impossible to achieve assumptions  (e.g. an infinite number of rehearsal samples generated by the model). Specifically, the assumption of an infinite number of samples makes the theoretical results difficult to apply in practice, where computational resources are always limited. Furthermore, the assumption that the generative models learn the true distribution 'well enough' is also problematic, as it is not clear how to quantify this 'well enough' in a practical setting, and it is unlikely that any real-world model will satisfy this assumption perfectly.
- The empirical evaluation of two simpler models is limited to 2 visualisations without quantitative measurements. This lack of quantitative metrics makes it difficult to assess the actual performance of the proposed method on these simpler models. Visualizations alone are insufficient to determine whether the observed trends are statistically significant or merely artifacts of the specific data and model configurations used. The absence of metrics like FID or IS scores, even for simple datasets, is a significant oversight.
- For Diffusion models, the evaluation is performed on 3 datasets, which is sufficient. However if I understand the setup correctly the whole analysis is performed on a single training seed. The differences presented in the plots are extremely small so it is unclear whether they are statistically significant, and therefore whether the main claims hold. This single seed evaluation raises concerns about the generalizability of the results. The observed stability could be a result of a lucky initialization or a specific training run, rather than a robust property of the method. Without multiple seeds, it's impossible to determine the variance in performance and whether the observed trends are consistent across different training runs.

Small not important detail:
Page 8 the end of Experimental Setup section, I spend some time trying to understand what emphconstant means :D - please correct a typo

### Questions
Did you consider evaluation how other sampling procedures that minimises the statistical approximation error might influence the findings presented in this paper? Maybe instead of drawing random samples, but for example those that best cover the data distribution (e.g. using herding alogrithm) could prevent the model from collapsing, or at least slow it down when retrained with bigger portion of sampled data?

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
The authors study the problem of generative models that are recursively trained with parts of the dataset are generated by an earlier version of the generative model. They provide theoretical proofs that suggest that if the share of generated data w.r.t. the original data is small enough, this training can still be stable, whereas otherwise it collapses.

### Strengths
**Well-structured.** The structure of the paper seems fine and I like how the simple cases are considered first to build an intuition before more complex cases are presented. Although the matter of the paper is quite technical, the formal introduction of the problem and the notation is well executed. Apart from one point (see "clarity" below), I think the overall presentation is good.

**Interesting and Timely problem.** the problem studied in this work is interesting and can be considered timely as indeed, content by generative AI is flooding the internet, which in turn is the key source of training data for generative models.

**Technical rigor.** I have the overall impression that the technical part is rigorously executed and I did not find any significant flaws. However, as pointed out below, I was not able to verify all steps of the proofs.

### Weaknesses
 **Clarity.** I am a bit puzzled by the use of $\succcurlyeq$ for matrices. When you write $\Sigma \succcurlyeq 0$, I suppose it is the usual condition for Sigma to be positive definite and not that each individual element of sigma should be larger than zero. This would rule out certain covariance matrices. On the other hand, the authors write $\nabla^2 f = H_f \preccurlyeq -\alpha I_d$, comparing two matrices (supposing that $I_d$ is the $d$-dimensional unit matrix). I suppose that it now constrains each element. Can the authors please clarify?

Measures: What is meant by precision and recall in the evaluation section? Is there a discriminator deployed that tries to differentiate between the real and fake samples? This needs to be clarified. I don’t currently see how generative models can have recall/precision.

**Clarity of the Proofs.** Unfortunately, some proofs in the paper offer room for improvement of clarity and were inaccessible for verification in their current form. For instance:
In appendix A.1., I can follow the proof of Lemma 1 and Lemma 2. However, it is not obvious how equation (13) implies the form of $\alpha(n)$ using the $\Gamma$-function. This should necessarily be clarified as there is not a word on how the form of $\alpha(n)$ comes into play.

**Some assumptions made in this work may not reflect reality well and may be oversimplifying.** While I know that certain assumptions are required to make the problem amenable to theoretical analysis, I have concerns that they may be overly restrictive in practice. In particular, we basically assume convexity of the loss function through assumption 1 and 2. As far as I can see, due to the Lipschitz constant on the Hessian being L (assumption 1) and the Hessian's eigenvalues being smaller than $-\alpha$ (interpreting the operator that way, please correct me in case this is not correct), in the ball of $\epsilon = \alpha/L$ around $\theta^*$, the Hessian will be negative definite, implying convexity. As the Theorems only state the existence of a radius $\delta > 0$ in which the convergence properties hold, we basically consider the convex part of the problem. As we know, modern loss landscapes are far from convex. It is highly unlikely that both the initial value and the optimum $\theta^*$ lie in a ball in which the loss function is convex.
Another impractical assumption may be the assumption of no approximation error. This is usually only shown for infinite-parameter models. I would be fine with these approximations if the empirical results would confirm the assumptions and the analysis that follows from them. However the evaluation results seem to rather confirm the doubts.

**The evaluation does not confirm the claims.** As far as I can tell, the point of departure for this work is as follows: Previous works [1,2] have already established that model training on solely generated data is unstable or collapses. On the other hand, training models again and again on the same dataset is stable (otherwise the models we currently have wouldn’t work at all, as they are trained epoch by epoch with the same data). The key claim of this work is therefore that there is some value $\lambda > 0$, i.e., a certain amount of generated data can be injected, such that model training remains stable. 

Unfortunately, the experimental results are not very convincing in that regard. Indeed, the leftmost column of Figure 3 shows that the resulting FID curve is almost a linear interpolation between $\lambda=0$ (stable) and $\lambda=1$ (unstable). This suggest that for every $\lambda>0$ training will be diverge in the end. Even for the smaller lambdas, we see that the training FID gradually increases. For \lambda=0.001, I guess one would require more than 5 steps of training to observe a statistically significant effect (as we are discussion the case of infinite retraining). Furthermore, there are no measures of disparity (e.g., standard deviations) displayed, would could solidify the empirical evaluation.

**Minor points**

Related work: I am aware of the fact that the studied problem is different from mode collapse in generative models, but I have the impression that there seem to be some connections. Maybe the authors can add a discussion on this point.

Write-up: Missing parenthesis in the last line of before the statement of the contributions “(DDPM…”

Last point of the contribution section: “Using two powerful diffusion models in DDPM and EDM” (“in” seems unexpected at this place)
There are many unclarities in the proofs:

“Since most methods are local search method[s]” (use the plural form here)

Proof in Appendix C. There are some formatting errors below eqn. 33. (theta is not properly displayed). 

Proof in Appendix D. Equation (39) theta’ is multiply defined, first by the outer quantor, then below the max after the $\leq$ sign. Consider using $\theta’’$ or similar in this case.

The PDF seems to render very slowly. Maybe the authors can check some of the vector graphics again to increase the overall accessibility.

**Summary:** Overall, this is an interesting work. While I do not contest the main results, I was not able to verify all proofs either as I wasn’t able to follow the arguments at some points. Furthermore, the empirical evaluation is almost contradictory to the theoretical claims in this paper. I will be willing to increase my rating to an accept-score, if the authors can clarify their proofs such that the validity of their results can be easily verified and convincingly show that values of $\lambda>0$ exist, where stable retraining is possible for a larger amount of retraining iterations (5 iterations are insufficient when considering an infinite regime).

### Questions
1. Have the authors tried running the experiment for more than 5 steps? 

2. Can the authors give standard deviations for the plots in Figure 3?

3. What do the recall and precision metrics in Figure 3 mean?

4. Can the authors clarify the >-operator for matrices?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article studies the stability of iteratively training generative models with generated samples as part of the training set. In this article, it is proven that under some regulatory and optimality assumptions, the model after many rounds of training will still be close to the original one. This article considers both the infinite-sample and finite-sample cases, and provide error bounds on model distances. Then, the article studies several popular deep generative models on standard benchmarks to investigate what happens in practice.

### Strengths
- The iterative training formulation has become a very important problem today as there are many powerful deep generative models and their generated samples are used to train or finetune other models. This article presents a very concise and elegant way to describe this task, which is able to leverage previous theory on deep generative models by its nature. 
- The assumptions are mild and the theoretical results are good. It is not surprising that with a small enough $\lambda$ the iterative training will be stable, but it is encouraging that $\lambda$ can be as large as $1/4$ in Thm 1. 
- The presentation of this paper is very clean. It is very easy to follow from background and preliminaries to assumptions, theorems, and proofs.

### Weaknesses
The main weakness of this article is that its experiments cannot fully justify the theoretical analysis. All experiments on the high-resolution image tasks are based on diffusion models, where there might be some shift from the theoretical analysis on maximum likelihood training as diffusion models optimize variants of ELBO. There should be experiments on models trained with the exact likelihood (and on real world datasets), such as flows and autoregressive models. While flows may have a larger $\epsilon$ due to their capacity issues, autoregressive models might be a better objective to look at. I'd like to see some experiments on this. 

Regarding Fig 3, the trends are not clear enough, and I'd like to see results for more iterations so that the trends become clear. The differences between different runs are very small, so the authors should run multiple experiments with different random seeds to reduce the effect caused by randomness. In addition, I'd like to see results on  $\parallel \theta_t - \theta^* \parallel$ for more direct comparison.

### Questions
Please refer to the weakness section for questions on experiments.


--------------

**After rebuttal** the authors have improved or added experiments that fully addressed my concerns. The results make the paper much stronger than the first draft. I think this paper is novel, sound, enlightening, and opens a new window to look at the current challenges of modern generative models.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
