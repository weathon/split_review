# Improving Generalization with Flat Hilbert Bayesian Inference

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 3, 8, 6

## Abstract
We introduce Flat Hilbert Bayesian Inference (FHBI), an algorithm designed to enhance generalization in Bayesian inference. Our approach involves an iterative two-step procedure with an adversarial functional perturbation step and a functional descent step within the reproducing kernel Hilbert spaces. This methodology is supported by a theoretical analysis that extends previous findings on generalization ability from finite-dimensional Euclidean spaces to infinite-dimensional functional spaces. To evaluate the effectiveness of FHBI, we conduct comprehensive comparisons against seven baseline methods on the \texttt{VTAB-1K} benchmark, which encompasses 19 diverse datasets across various domains with diverse semantics. Empirical results demonstrate that FHBI consistently outperforms the baselines by notable margins, highlighting its practical efficacy. Our code is available at \url{https://anonymous.4open.science/r/Flat-Hilbert-Variational-Inference-008F/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work presents an algorithm called Flat Hilbert Bayesian Inference (FHBI), which incorporates Sharpness-aware minimization (SAM) technique in Bayesian inference. Specifically, together with SAM, the authors perform Stein variational gradient descent (SVGD) as the dynamics of the model parameters, which leads the particles (models) to flat and diverse modes. FHBI is tested on VTAB-1K, a collection of various classification tasks, and achieves better performance on average among different Bayesian NN methods.

### Strengths
- The work extends generalization bounds from finite-dimensional parameter spaces to functional spaces, which leads to FHBI, a theoretically grounded Bayesian inference algorithm.
- The performance improvement by the proposed method is validated through extensive comparisons with previous works.

### Weaknesses
 - I don't see any particular weaknesses in this paper.

### Questions
- The method is tested only in fine-tuning regime. Is there any reason for that? 
Testing the proposed models trained from scratch would strengthen the empirical significance of the proposed method. I am not sure which datasets would be suitable, but datasets like ImageNet and its variants (ImageNet-A [1], and ImageNet-C[2]), and scientific machine learning benchmarks might be good datasets as uncertainty prediction would be critical. 

[1] https://arxiv.org/abs/1907.07174
[2] https://arxiv.org/abs/1903.12261

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper combines sharpness aware minimization (SAM) with SVGD in RKHS as the Flat Hilbert Bayesian Inference (FHBI). It extends the proof of [1] to infinite-dimensional functional space.
Empirical validations show better performance of FHBI compared to previous Bayesian inference approaches on various datasets.

[1] Pierre Foret, Ariel Kleiner, Hossein Mobahi, and Behnam Neyshabur. Sharpness-aware minimization for efficiently improving generalization. In 9th International Conference on Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021. OpenReview.net, 2021.

### Strengths
1. Incorporating SAM into SVGD can somehow improve the stability. The idea generally makes sense. 
2. The paper is clearly written overall, and it is easy to capture the motivation.
3. The empirical results are superior and tested on various datasets.

### Weaknesses
Even though I agree that the proposed method may be effective in some conditions, I am not convinced by the theory in this paper. Following are my concerns. 
1. Notations.  
    * Empirical posterior should be $\mathbb{P}_{\theta|S}$ not $\mathbb{P}_S$, which is the data distribution. And the prior distribution should be $\mathbb{P}_{\theta}$.
    * $p(\theta|S)\propto p(\theta)p(S|\theta) = p(\theta)\prod_{i=1}^n p(y_i, x_i|\theta)$
     The exponential average loss should be related to a specific distribution. I do not know how you can obtain this form directly. 
     * What is "general loss"? I have never heard this terminology. $\mathcal{L}_{\mathcal{D}}(\theta)$ is often called population loss/ true error/ generalization error in different papers or learning theory books. 
2. For Theorem 2, what is the exact definition of $h(1/\rho^2)$? It should be clearly presented in the main paper. In your derivation, $\mathcal{O}(\rho^2)$ is simply ignored, which means $\rho$ should be very small, which in turn gives a large $h(1/\rho^2)$.
3. You are actually deriving an upper bound of the true risk, which is the empirical risk plus some complexity term. However, the sample complexity is not directly reflected in the bounds presented in the main paper. You claim that you can approximate the true posterior $p(\theta|\mathcal{D})$. This is impossible if you only have limited samples $n$. 

4. Experiments
	* How does data augmentation affect the empirical results? Have you used it in all baselines or just your method? 
	* As shown in Figure 3, the runtime of the FHBI increases fast w.r.t the number of particles. Compared to SVGD, the margin also grows with the number of particles. Where is the computation bottleneck? Can you find any way to reduce it? 

### Questions
Have you compared SVGD+SAM to SGLD+SAM [1, 2]? 


[1] Van-Anh Nguyen, Tung-Long Vuong, Hoang Phan, Thanh-Toan Do, Dinh Phung, and Trung Le. Flat seeking bayesian neural networks. Advances in Neural Information Processing Systems, 2023.

[2] Yang, Xiulong, Qing Su, and Shihao Ji. "Towards Bridging the Performance Gaps of Joint Energy-based Models." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents Flat Hilbert Bayesian Inference(FHBI),   a method to compute a posterior inference by integrating along the flow of distributions that converges to the target posterior.   By formulating  the derivative of the flow with the pushforward function that lives in a vector valued RKHS,  the framework naturally establishes the "flow of infinite number of particles" which allows one to target the "general posterior" as opposed to "empirical" posterior in the setting of Bayesian Inference.   Importantly, the method differs from Stein Variational Gradient Descent in that it derives the infinitesimal pushforward function that reduces the "worst upper bound" of the KL divergence in a way that resembles adversarial training.

The propsoed  paradigm is made implementable by the computable form of $\lambda p(\theta | S)$, together with the upper bound of the KL divergence  to general posterior defined with the KL divergence to empirical posterior.  
The Efficacy of the algorithm is verified through experiments and its scaling properties are investigated and compared with respect to SVGD.

### Strengths
- This research presents a scheme that generalizes both SVGD and SAM in the context of Bayesian Inference. 
The idea of FBHI itself is very clearly stated and convincing, and its efficacy are validated with ample experiments. 
The layout of the derivation is very instructive as well. 
The claimed sharpness advantage (that FBHI would is more sharpness-aware) is also validated in experiments, empirically  
showcasing the mechanism behind the advantage of the method.

### Weaknesses
 - While the relation of FHBI to SAM and the interpretation with spatial and angular repulsive force is insightful,  the reviewer was a little confused in the introduction and in the multiple reference to SAM that sounded as if SAM would be the major idea on which to develop FHBI (which, in retrospect, is not "directly" so?).  Meanwhile, it is  true in the algorithm that when m=1, the algorithm agrees with SAM in the end.  In the current presentation the connection to SAM seems something a posteriori.

 If indeed the sharpness-aware philosophy is indeed the "motivation" of FHBI (which is, unfortunately, not yet clearly conveyed to this reviewer), the reviewer would like to see more analytical connection to SAM's derivation.  

- In the similar note, as the reviewer will post in the "Questions" section, the reviewer feels that the supposedly the important connections to SVGD and SAM are not clearly explained through objective function and derivations (**more than $\rho=0$ and $m=1$ )

### Questions
- In my understanding, Theorem1 expresses the tradeoff relation between (1) worst-case empirical loss  that scales with the size of the neighborhood (radius of the step size)   (2) wellness of the upperbound approximation based on the empirical loss.  The reviewer is making in his mind a super-rough analogy of "local linear approximation of a complex function", whose worst case error scales with the size of the neighborhood, and "functional ascending step" is analogous to choosing the direction of worst error in this approximation. 

If this analogy is correct,  the neighborhood radius $\rho$ as well as the update size $\epsilon$ would be roughly analogous to a stepsize in Euler-Maruyama simulation of the ODE, except that in the context of FBHI the system to be simulated is infinite dimensional.  Would the method improve its performance by choosing $\rho$ and $\epsilon$ to be small, and running the iterations for greater number of times, as in ODE simulation?    Also, with this intuition it feels as if $\rho$ shall be similar to $\epsilon$;  why are they chosen quite differently in the experimental section? 

While the reviewer is not too confident of the intuition based on this super-rough analogy, the reviewer also believes that it is crucial that the paper provides some explanation (either numerical or experimental, or at the very least, the heuristic with intuitive explanation) regarding the choice of $\rho$ and $\epsilon$, both for the sake of the future practical user of FBHI and the for the sake of the future schemes that will possibly branch out from FBHI.

- In the similar note as above, because the "wellness" of RKHS method generally depends on the affinity between the choice of the kernel (and the hence the nature of the continuity of functions in the space) and the dataset.   In the case of  this research,  the choice, I believe, is indirectly related to dataset because RKHS is a space of functions on "parameters".  Is there any ablation study regarding this choice, or at the very least, a good heuristics that would help the user to choose appropriate Kernel in the applications? 

- It is explained in the paper that $\rho=0$ would correspond to  SVGD, and "in equation" it seems so. However, because the paper emphasizes its connection to SVGD, the reviewer wishes to see why this comes about in connection to Theorem 1 and the derivation of SVGD. 

- Is there comparisons against SAM in the setting of section 6.2?

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
3

### Summary
In traditional variational inference, the goal is to approximate an intractable posterior \( p(\theta | \mathcal{S}) \) by selecting a variational distribution \( q \) from a family \( \mathcal{Q} \) that minimizes a divergence, often the KL divergence, resulting in the optimization problem:

$$
\arg \min_{q \in \mathcal{Q}} \, \text{KL}(q(\theta) \parallel p(\theta | \mathcal{S})),
$$

where \( p(\theta | \mathcal{S}) \), termed the "empirical posterior" by the authors, is the target distribution.

This paper introduces a variational family within a Reproducing Kernel Hilbert Space (RKHS) framework and further reformulates the optimization problem to focus on approximating the "general posterior," \( p(\theta | \mathcal{D}) \), over the dataset \( \mathcal{D} \). The optimization problem thus becomes:

$$
\arg \min_{f \in \mathcal{H}^d, \, \|f\| \leq \epsilon} \, \text{KL}(q_{[I + f]}(\theta) \parallel p(\theta | \mathcal{D})),
$$

where \( q_{[I + f]}(\theta) \) represents the transformed variational distribution. This reformulation leads to multiple steps of approximation, relaxation, and bounding, culminating in an iterative optimization procedure (detailed below Lemma 1).

The proposed method, Flat Hilbert Bayesian Inference (FHBI), is designed to enhance generalization in Bayesian inference by leveraging the structure of RKHS.

### Strengths
* Originality: 
I'm uncertain about the level of originality here. Variational families within an RKHS framework have, to my knowledge, been explored previously. 
* Quality: The work appears to be of high quality. The results seem technically correct, and while I haven’t meticulously checked every mathematical detail, the derivations appear consistent with expectations.
* Clarity: Overall, the paper is well-written. I appreciated the clear, step-by-step walkthrough of the optimization problem and the detailed exposition of various bounds and relaxations necessary to implement the proposed approach.
* Significance: The proposed method, Flat Hilbert Bayesian Inference (FHBI), is presented as a generalization of Stein Variational Gradient Descent (SVGD) and Sharpness-Aware Minimization (SAM). The experiments demonstrate promising potential for FHBI in applications like LoRA-style fine-tuning.

### Weaknesses
 * The general posterior defined, $p(\theta|\mathcal D)$, does not appear to me to be the correct theoretical counterpart to the "empirical" posterior. See more in questions below.
 * If the paper’s originality hinges partly on targeting the "general posterior" $p(\theta|\mathcal D)$, I have reservations about its practical benefits. In addition to my concerns about the missing sample size term, targeting this posterior seems unlikely to yield practical advantages and might even be counterproductive. The authors expend considerable effort introducing approximations to recast the optimization problem in terms of the "empirical posterior," which requires potentially loose bounds. The value of this detour would be enhanced by a more thorough discussion of why these approximations are justified or necessary.
 * The paper emphasizes "improving generalization" as a primary benefit of FHBI, yet this claim seems tenuous without more foundational support. It's unclear what is meant by "enhancing generalization in Bayesian inference" mathematically, as the method doesn’t inherently introduce any features that theoretically boost generalization. Rather, it appears that FHBI, when applied to fine-tuning, yielded improved generalization performance on a benchmark dataset compared to baseline methods. This distinction between observed outcomes and the initial methodological intent would be clearer if the authors clarified that FHBI’s generalization performance was more an empirical finding than a theoretically driven design choice.



### Questions
Major:
* Something seems amiss in going from the empirical posterior $p(\theta|\mathcal S)$ to what you call the general posterior $p(\theta|\mathcal D)$. Let $L_n(\theta) = \frac{1}{n} \sum_{i=1}^n -\log p(y_i|x_i,\theta)$. Then the empirical posterior is $p(\theta|\mathcal S) = \exp(-n L_n(\theta)) p(\theta)$. The population counterpart to this is $\exp(-n L(\theta)) p(\theta)$. But this is *not* your general posterior which no longer has any dependence on sample size $n$. 

Minor:
* Currently, the way the loss $\ell$ shows up in Section 3 might give the wrong impression that it is something one can freely choose. In fact the loss has to be (proportional) to the negative log likelihood. I think you need to write out explicitly what $\ell(f_\theta(x),y)$ is. 
* The sentence above Eqn (5), "In turn, the solution $\hat f^*$ that solves the maximization problem above is given by". Which maximization problem above? There are so many approximations here, please use \label and \ref to refer to exact maximization problem. (I also doubt this is a true statement, (5) is not really a solution but an approximation of a solution right?)
* Would you consider labeling the iterative procedure right below Lemma 1 and making it painfully clear how that turns into Algorithm 1?

### Soundness
2

### Presentation
3

### Contribution
2
