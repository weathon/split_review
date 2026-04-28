# Improving Probabilistic Diffusion Models With Optimal Covariance Matching

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
The probabilistic diffusion model has become highly effective across various domains. Typically, sampling from a diffusion model involves using a denoising distribution characterized by a Gaussian with a learned mean and either fixed or learned covariances. In this paper, we leverage the recently proposed covariance moment matching technique and introduce a novel method for learning the diagonal covariances. Unlike traditional data-driven covariance approximation approaches, our method involves directly regressing the optimal analytic covariance using a new, unbiased objective named Optimal Covariance Matching (OCM). This approach can significantly reduce the approximation error in covariance prediction. We demonstrate how our method can substantially enhance the sampling efficiency, recall rate and likelihood of both diffusion models and latent diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper propose to build on existing moment matching diffusion progress and focus on the estimation of the optimal covariance. They propose to improve over previous methods for estimating the diagonal of covariance with an additional network that amortizes the cost of computing explicitly the covariance during sampling. They show that their method is challenging with selected comparisons.

### Strengths
Thank you for your work!

- The paper demonstrates the application of OCM across different models (classical and latent diffusion), making the approach adaptable for a range of diffusion-based applications.

- The paper target efficient diagonal estimation to reach efficient sampling (leading to reduced number of step and more accurate samples).

- The proposed method is timely as it is based on recent covariance matching methods. It correctly try to improve efficiency over existing estimation techniques by amortizing the covariance estimation with an additional neural network. It still bases its estimation on learned diffusion model, making it comparable to previous ideas.

- It looks like very reasonable overhead for the Hutchinson estimator (M = 1 as noted in line 199) provide good performance which is in favor of the method that seeks efficiency.

- They propose an unbiased objective for diagonal covariance matching.

### Weaknesses
In general, the paper is good. However the results miss visualization (in the core text). A toy example would be welcome for visualization as well and easy results interpretation/comparison. The performances reported do not exhibit high improvement over other methods. Although it shows to be challenging! Maybe other performances should be reported to strengthen the defense of this method over others (the authors often point efficiency as a main goal, but no convincing observations in this favor

**General Comments** 

- The title is a bit misleading. You do not make optimal covariance matching, only diagonal matching. I also found the choice of diagonal only matching a little bit skipped. I do not say that it's a bad approximation, but it has its limitations. You should motivate more 'why' diagonal is already a good approximation (more than the complexity motivation).

- Figure 1 is not really relevant as so. Ok the number of Rademacher samples improves the diagonal structure, but we don't know the target. Could you estimate it for comparison? Or doing the same for a toy problem with known covariance? Can you quantify or give an idea of information loss induced by only estimating the diagonal (It depends on the problem of course)? Figure 1 do not provide more information than Appendix C4. Maybe the latter can be replaced by something that focus on your method. The number of Rademacher samples do not seems to be the main point of your method.

- Concerning Rademacher samples, it would be nice to see a metric (like FID and IS) evolving with M (the number of samples) to strengthen your claim line 199.

- Echoing with the previous point, it would be nice to show more extensive comparison with other covariance matching methods. Either that target full covariance or more costly diagonal estimation. Insist more on the advantage of your estimator concerning the estimation speed/accuracy ratio. In the same trend as table 4. Maybe you can have a small toy problem (MoG, ...) for which it is better to interpret results (and visualize them) + having access to GT covariance.

- I'm a little bit worried about the 'diagonal' only estimation. What if you have strong local covariance? Could be good to discuss, give hints about potential failure of your method in such setting. I take the example of [1] where they have to define a new sampling strategy as existing ones do not capture correctly covariance (or assumptions are too strong) leading to poor sample accuracy. This method also provides moment matching sampling, efficient by using vjp in spite of modelling the full covariance explicitly. Could you compare to similar method? For example, how do you compare to low-rank estimation which are also less demanding but can model non-diagonal elements?

- In the same idea as [1], current diffusion model and sampling strategies hardly comes without posterior sampling. It would be nice to study the benefit of your estimation for posterior problem. I think that is needed for a sampling method. 

- In equation (10), you still need $H(\tilde{x})$ which can be large as you mention. Do you model it explicitly for training the covariance network or do you model it implicitly using jvp/vjp benefits? This should be discussed. How does it slow down training compared to classical denoising-score matching or other methods?

- Can the introduction of an additional network (meaning additional approximation) lead to cumulative errors? This is not discussed at all, but the network not being well aligned with the covariance of the trained diffusion will surely lead to poor performances even if the diffusion model was good. 

**Spotted typos**

- Figure 1: The $K$ corresponds to $M$ in the main text, no? Could be changed for consistency.

- Line 195 and 812: ~Validity of OCM objetcive~ -> Validity of OCM objective.

- Line 309 and 427 ~COM-DDPM~ and ~OCM-DPM~ -> OCM-DDPM, no? 

- Appendix A.2: ~Vadality~ -> Validity.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes an approach to diffusion modelling in which the covariance matrix of the time-reversal of the "noising" process is set to a diagonal approximation of the correct form estimated from the approximation of the "score". 

In order to do this a pair of neural networks are trained; one to estimate the score as usual and a second to estimate this diagonal matrix. The majority of parameters are shared between the two networks, allowing this to be accomplished with only a small additional computational cost. The properties of the objective function used to learn this covariance are explored to an extent in theoretical work.

Numerical results are presented for a toy model and for some more substantial image generation scenarios.

### Strengths
To the best of my knowledge this approach to approximating the covariance matrix is novel and seems well motivated.

The numerical results do appear to show that this approach outperforms a number of alternative strategies and the settings of the image generation setting do seem reasonably challenging.

It seems that the additional implementation and training requirements of this approach over and above those of a more basic diffusion generative model are modest and so this approach could be incorporated into implementations of such approaches at small cost (both human and computational) which means that even modest improvements are potentially valuable.

### Weaknesses
The paper doesn't seem to propose anything radically new; the introduction of sensible approximations of the covariance of the time reversal has been explored quite widely in recent years and so the contribution of this paper is the particular approach to doing that which, while well motivated and seemingly having good properties, does not seem particularly radical. 

There are some odd choices made presentationally at times which to my mind make the paper a bit less readable and hence a bit less accessible. For example, the description of diffusion processes in Section 2.1 takes as a starting point a discrete time process; (1) is not a diffusion process although it is described as one. It might be arrived at as the time discretisation of a diffusion, which may in this case be exact, but that's not the same thing. These are minor points and haven't substantially influenced my view of the paper, but this seems the best box to put this in. The paper does contain quite a number of typos, strangely phrased sentences and similar; careful proofreading would make it more readable. E.g.
* Abstract: "diagonal covariances" is an odd phrase; covariances are the off-diagonal elements of the matrix. "diagonal covariance matrix" or similar might be clearer.
* Theorem 2: "objetcive"
* Theorem 2: "The objective in Equation (11) upper bounded the grounded objective." Didn't immediately seem to make sense to me; I /thought/ the intention was probably something like "The objective in Equation (11) upper bounds the base objective." or something of that sort, but it's not completely clear what the intended base objective was. It turns out that aside from the odd tense and phrasing, the statement of this theorem is using terms which are defined in the supplementary material!

The main evidence presented in support of the proposed approach is empirical and this evidence isn't completely overwhelming. E.g. from Table 3 it' seems that this method doesn't actually dominate other approaches in the literature although it often does well and doesn't seem to be outperformed by much when it is beaten. Of course, methods can be interesting without beating the state of the art uniformly, and there is the interesting suggestion that when other methods are outperforming this approach in terms of NLL they do less well in FID terms. That, of course, raises the question "why is this and what does it actually tell us?"

### Questions
Line 36: in what sense is this a "posterior" covariance? It seems from later in the paper that the covariance of the semigroup of the time reversal of the noising process is what's intended; I don't see that there's anything Bayesian going on.

Line 199: "In practice, we found M = 1 works well," raises some obvious questions:
1. How did you find this?
2. What does "works well" mean and how does increasing M to larger numbers change behaviour? A single sample provides an unbiased estimate, but its variance will clearly be large; generally one would expect performance to increase with larger M and so the question is how does the performance/cost tradeoff behave and this offhand comment doesn't give the reader much information which is a shame if you've done a proper study of this.

Have you done any comparison with the full covariance estimation approach of Zhang et al. (2024b)? While I appreciate it may sometimes be prohibitively costly it would have been nice to see what price is paid for making the diagonal approximation in at least as toy scenario. It seems as though strong correlation between coordinates in the true distribution might be reflected by strong correlation in the time reversal of the noising process, for example, and in those settings approximating it with a diagonal covariance although quite possibly still better than a naive choice might suffer relative to a more flexible approach whereas in settings in which there is not such strong dependency modelling it in the covariance matrix might not be particularly important.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce an optimal covariance matching objective based on score functions from pertained diffusion models to learn the covariance of the Gaussian transition kernel. 
The proposed method is superior at covariance estimation in terms of  less storage consumption and less number of network evaluations. 
Empirical results indicate that the proposed objective enhances performance in both sampling quality (NLL, FID) and efficiency (number of sample steps).

### Strengths
- The paper is well-organized, results are clearly presented, and the technique derivations are solid. 
- Overall paper organization is very smooth, the methodology part is easy to follow, and experiments are well-designed and coupled with the proposed methodology. e.g. from figure3, table 3 and table 5, I can see that the improved sample quality can be directly attributed from better covariance estimation. 
- Unlike the previous works which are of high requirements on storage and network evaluation in covariance estimate (especially the Hessian term), the proposed OCM barely needs 1 network evaluation for each sampling step, so that the method improves number of sampling steps without sacrificing too much sampling speed on covariance estimate.

### Weaknesses
 - The authors show that the proposed OCM improves covariance estimation for DDPM and DDIM, which results in improved sample quality and better efficiency. There are many other stochastic and deterministic samplers with different sampling schedules, does the improved covariance helps with all these samplers?


### Questions
- Is the proposed OCM able to help with other diffusion samplers? e.g. EDM [1] stochastic and deterministic samplers? 
- Any insights or intuitions why comparing to baselines, learning the covariance via OCM objective gives better covariance estimation over all noise levels? 
- Just out of curiosity, in Fig 3 (a) and (b), why the covariance error goes up for all methods when t is roughly in range [0, 400]? 

[1] Karras, Tero, et al. "Elucidating the design space of diffusion-based generative models." Advances in neural information processing systems 35 (2022): 26565-26577.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose an $x_t$-dependent diagonal covariance estimation method that directly learns from score function. This leads to improved efficiency and more stable/robust denoising, which in turn improves the image generation quality.

### Strengths
1. Very clear and comprehensive presentation, easy to read and follow.
2. The proposed method is a general method that applies to various settings.
3. The description of experimental details is generally comprehensive.

### Weaknesses
1. The idea seems both incremental and way-too simple, which is not a fundamental change in the covariance estimation that would lead to a revolutionized/big change in the performance and/or efficiency. It will have a limited impact on the community.

2. The experimental results seem not extraordinary. It does not fundamentally improve the performance (generation quality), which is understandable since covariance is more about sampling efficiency and sample diversity. However, even in terms of the sampling diversity and efficiency, such as indicated by Table 4, the proposed method does not significantly beat strong baselines. Moreover, there are no error bars or uncertainty in the experimental results.

### Questions
I have no more questions. I like the presentation (as well as the soundness of the idea, of course) and think this alone makes the paper okay to accept. I am just simply not impressed by the results.

### Soundness
3

### Presentation
4

### Contribution
2
