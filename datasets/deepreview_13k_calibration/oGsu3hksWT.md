# Bayesian Learning with Deep Q-Exponential Process

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
Regularization is one of the most fundamental topics in optimization, statistics and machine learning. To get sparsity in estimating a parameter $u\in\mbR^d$, an $\ell_q$ penalty term, $\Vert u\Vert_q$, is usually added to the objective function. What is the probabilistic distribution corresponding to such $\ell_q$ penalty? What is the \emph{correct} stochastic process corresponding to $\Vert u\Vert_q$ when we model functions $u\in L^q$? This is important for statistically modeling high-dimensional objects such as images, with penalty to preserve certain properties, e.g. edges in the image.
In this work, we generalize the $q$-exponential distribution (with density proportional to) $\exp{(- \half|u|^q)}$ to a stochastic process named \emph{$Q$-exponential (Q-EP) process} that corresponds to the $L_q$ regularization of functions. The key step is to specify consistent multivariate $q$-exponential distributions by choosing from a large family of elliptic contour distributions. The work is closely related to Besov process which is usually defined in terms of series. Q-EP can be regarded as a definition of Besov process with explicit probabilistic formulation, direct control on the correlation strength, and tractable prediction formula. From the Bayesian perspective, Q-EP provides a flexible prior on functions with sharper penalty ($q<2$) than the commonly used Gaussian process (GP, $q=2$).
We compare GP, Besov and Q-EP in modeling functional data, reconstructing images and solving inverse problems and demonstrate the advantage of our proposed methodology.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduce deep q-exponential process (deep q-EP) as a modeling technique that combines the recently-proposed q-exponential process of [Li et al, 2023] with the deep Gaussian process approach of [Damianou & Lawrence, 2013].  Deep q-EP is a generalization of the deep Gaussian process for q $\neq$ 2 and allows for more modeling flexibility beyond the Gaussian assumption.  The authors propose and derive a variational inference strategy for the model.  They also perform several experiments involving regression and classification on machine learning datasets and compare the performance of their method with other baselines.

### Strengths
- The paper is generally clearly written and easy to follow.  The sections are organized well and the contributions are quite clear.  The authors consistently draw connections with the literature and reference the papers on which their result is built, namely [Li et al, 2023] and [Damianou & Lawrence, 2013]. 
- The idea is an interesting one and has the potential to be influential -- GPs are widely used throughout machine learning and any improvement in a widely-used method can be an important contribution. 
- The variational inference method for q-EP appears to be novel.  As far as I can tell, variational inference has not been applied to this model class until this paper.
- The application of multi-layer deep GP to q-EP also appear to be a novel idea that no one has tried before.

### Weaknesses
 - Though an interesting idea, the paper is pretty straightforward combination of deep GPs and q-EPs.  In this sense, the novelty may be a bit limited.  
- The main critique I have of the paper is that it provides limited insight into when and why we expect deep q-EPs to be better than deep GPs.  There is one sentence in the abstract -- "Despite the enhanced expressiveness, GP, as an L2 regularization prior, tends to be over-smooth and sub-optimal for inhomogeneous subjects, such as images with edges" -- though this idea is not expanded upon later in the paper.  Are the authors advocating that we should always use deep q-EPs over deep GPs?  Or are there specific types of data in which we should expect deep q-EPs to outperform deep GPs?  Little guidance is given about how a practitioner should think about the relative advantage of each approach and in what situations one is advantageous over the other.    
- I appreciate that the authors conduct several experiments to compare the performance of their method against deep GPs, though the results appear somewhat mixed.  In several cases, the performance of the two methods are quite close and it is unclear to me exactly the benefit of one over the other.  Of course, it's not expected that the new method would outperform deep GPs in every instance.  But for the cases in which deep q-EPs is superior, little explanation/analysis is given on why these results make sense.  I think providing more analysis on which types of data/situations are most suited for deep q-EPs would greatly improve the paper.
- Though deep q-EPs can have any value for q, it appears that the authors mainly use q=1 for the experiments.  There is no explanation given on why this choice was made and how a practitioner should select q in practice.  Is there any theoretical reason why we would expect q=1 to work better than q=2 for the datasets that you experimented with?  It would also be interesting to understand how sensitive are the results to the particular choice of q.



### Questions
- Does mean field variational inference approach ever lead to suboptimal inference due to absence of correlation in the posterior?  Can you comment on the choice of using VI in comparison to MCMC (as stated in the origin q-EP paper of Li et al)?  Is there any experiment you can perform to understand how well VI approximates posterior in comparison to MCMC for your q-exponential process? 
- In Figure 1, is there any insight into why q-EP identifies different features that are important in comparison to GP-LVM?
- In Figure 2, it is stated that “Among these models, deep Q-EP yields the most accurate prediction and the tightest uncertainty bound.” But the caption seems to indicate that deep GP performs marginally better.  It is not clear to me that deep Q-EP is more accurate for this example.  Also, since the numbers are very close, do you have the standard deviation of different runs to understand how stable these numbers are depending on initialization?  
- Figure 3 is interesting, though why is it the case that deep q-EP seems to have better decision boundary?  is there anything about the model that makes this result expected?  Would a deeper GP help performance?  Also, could this result be sensitive to the choice of kernel?  If you adjusted the smoothness parameter, do you get different results? 
- In section 5.4, the result between DKL-GP and DKL-QEP appears quite close, at least for MNIST — do you have standard deviations for these runs?  For CIFAR-10, it's a bit strange that all the methods don't perform much better than 70% accuracy.  Though state-of-the-art performance is certainly not expected, this seems too far below what can be achieved using other methods that the experiment may no longer be realistic.  Therefore, I'm not sure this dataset is a practical use case of the method.  

Minor points:
-  Eq. (1) is confusing to read.  r has dependence on u, \mu, and C; this is not obvious in the definition of p.
- In Eq. (2), does it always make sense to assume noise has the same q as the prior?  Is a more realistic assumption that noise is Gaussian with q=2?  How would having a different q in the prior vs. likelihood change the posterior though?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper extends the Q-Exponential Processes (QEP), a technique that generalizes Gaussian processes to Q-exponential distributions, to deep learning by stacking them into multiple layers in a similar fashion to deep Gaussian processes. The paper takes over the deep GP inference machinery of performing structured variational inference and adapts it to the QEP case. The paper reports results on a set of regression and classification benchmarks that are in commonplace use in GP research.

### Strengths
- The presented material is technically correct, well-structured, and understandable.
- The literature survey is comprehensive.
- The paper reports a comprehensive set of experiments.

### Weaknesses
 - The idea of generalizing Gaussian processes to the Q-exponential distributions is a solid conceptual step as it enhances the expressive power of the model family. I am having hard time to say the same for making a stack of them. This is a rather incremental step that can be taken by straightforward calculations. I am not able to find a concrete scientific problem behind this enterprise that could be valuable for the machine learning research leadership.
- The applied approximate inference approach is a standard and straightforward application of the well-known solution developed originally for deep GPs. I was not able to detect any technical challenges or original ideas that may be interesting.
- The performance improvement is ignorably small for the classification setup and it is yet to be decided based on R2 scores for the regression setup. Based on bare numbers available in Table 1 it is not straightforward to conclude that Deep QEP brings a clear improvement.

### Questions
- Can the authors report R2 score for the regression experiments so that one can quantify the absolute performance improvement by moving from deep GPs to deep QEPs?
- How does the STD column in Table 1 help interpret the results? And is it the standard deviation of MAE across repetitions?
- Likewise, what is the take-home message of Figure 3? In what sense does the Deep(er) QEP plots are better than the alternative deep variants? At first sight it looks to me like all of them perform comparably at the center and all fail at the corners. The rest is undecisive details.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper generalizes Q-EP (Q-exponential process)  to deep Q-EP so that one can inherit a flexible regularization through the controlled parameter q, which is advantageous in learning latent representations while modeling data inhomogeneity. This generalization is realized by introducing sallow Q-EP as a latent variable model and then building a hierarchy of the sallaow-Q-EP layers. Finally, an inference mechanism based on a sparse approximation via inducing points and a variational strategy is proposed.

### Strengths
Starting from Q-exponential process (Q-EP) that has been proposed as an L_q relaxation to Gaussian process (GP) with more desirable regularization properties through its parameter q (with q = 2 corresponding to GP), this paper proposes a contribution to deep probabilistic models via a new model that
(i) generalizes Q-EP to  deep Gaussian process (GP) with some flexibility of regularization
(ii) uses a scalable variational inference based on sparse approximation via inducing points.

### Weaknesses
 * The proposed theory presented in section 2 is too heavy and no explanations nor intuitions are supporting it. 
* Line 214 states that "Compared with optimization method (Lawrance, 2003), the Bayesian training procedure (Tistsias 2010) is robust to overfitting ..." without any justification or explanation.
* It seems that the proposed inference method induces a matrix inversion with a complexity leading to O(N^3); would it be possible to use a sequential Monte Carlo as proposed by Wang Yali et al. "Sequential Inference for Deep GP, (2016).
* Experiments are not convincing since most have been done on toy data. Furthermore; It would have been convenient to experiment Deep  GP on non-stationary noise (heteroscedasticity)

### Questions
(1) What is the complexity behind your variational strategy? Why it is scalable ? 
(2) your sparse approximation by inducing points is not clear, please elaborate more on that, both on the sparsity approximation and the choice of the inducing points.
(3) is your approach appropriate for dealing with a realistic approach as "coupled tomography imaging" as proposed in (Li, 2003).

### Soundness
2

### Presentation
2

### Contribution
2
