# Convergence Analysis of the Wasserstein Proximal Algorithm beyond Convexity

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
The proximal algorithm is a powerful tool to minimize nonlinear and nonsmooth functionals in a general metric space. Motivated by the recent progress in studying the training dynamics of the noisy gradient descent algorithm on two-layer neural networks in the mean-field regime, we provide in this paper a simple and self-contained analysis for the convergence of the general-purpose Wasserstein proximal algorithm without assuming geodesic convexity on the objective functional. Under a natural Wasserstein analog of the Euclidean Polyak-{\L}ojasiewicz inequality, we show that the proximal algorithm achieves an unbiased and linear convergence rate. Our convergence rate improves upon existing rates of the proximal algorithm for solving Wasserstein gradient flows under strong geodesic convexity. We also extend our analysis to the inexact proximal algorithm for geodesically semiconvex objectives. In our numerical experiments, proximal training demonstrates a faster convergence rate than the noisy gradient descent algorithm on mean-field neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The linear convergence of Wasserstein proximal point method is  established based on a Wasserstein analogue of the Euclidean PL inequality and the convergence of the algorithm when the subproblem is solved inexactly is also studied.

### Strengths
New convergence results based on the PL inequality.

### Weaknesses
It seems the analysis is well aligned with that in optimization. So what is the key challenges in the analysis?

### Questions
1) For $\mu$-strongly convex objective, this paper provides a sharper result. How is it achieved compared to existing work?
2) Except the common ones mentioned in this paper, are there any functionals that could satisfy the PL inequality?
3) In optimization, PL is special case of KL (with exponent $1/2$). Is it also possible to study the Wasserstein proximal point method under the more general KL condition?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The convergence of the  Wasserstein proximal algorithm 
without assuming geodesic convexity on the objective functional and the improvement of convergence rates
also for the geodesically convex case is a very interesting topic as well as the extension to the inexact proximal algorithm
and numerical experiments underlining the theory are highly welcome.
So the intention of the authors is fine and ''roughly'' the methods and proofs fit.
However, the mathematical realization lacks accuracy which is necessary for such a paper.
The authors should go through their paper step by step, pose correct assumptions, metrics and so on,
starting with my remarks below.

### Strengths
The task to show unbiased and linear convergence rate of the general-purpose Wasserstein proximal algorithm
for optimizing a functional under merely a  Polyak-Łojasiewicz (PL) inequality is interesting 
and the numerics with two-layer wide neural networks is promising.

### Weaknesses
Both the mathematical writing and the English is faulty 
(below I list only few of the shortcomings I detected, but there are many more).
The mathematical notation is not used in a correct way, 
 the authors have to give all and correct assumptions for their claims to hold true.

- formula (2): maybe change $\rho'$ to something else, since the first one looks like a derivative
- line 067: there is a notation switch  between $\varphi$ and $\phi$
- the authors write that they ,,assume that the strong subdifferential exists for every $\rho \in \mathcal P_2^a$'';
 this will never be the case; you do not mean this, so please fix
	- line 193 ''satisfy'' instead of ''satisfies''
	- line 208: A functional $F$
	- line 232: $v$ should be $\nu$
	- line 277: ''any stationary point  ... is a global minimum $F^*$''. Please reformulate, it is a global minimizer - not a minimum
	- Definition 3.2: give a reference to the Hopf-Lax ''formula''; maybe write that many definitions are taken from Ambrosio 2013;
	note that it resembles the Moreau envelope in the Hilbert space setting;
	further there is a notation mismatch: $\xi$ was used as subgradient, now it is the regularization parameter, in (2) this was $\eta$.
	The definition supposes that a (unique) proximum exists. I could live without ''unique'' if the authors write $\rho_\xi \in prox_{F,\xi} (\rho)$, but then the existence is only clear with additional assumptions on $F$. 
	In Lemma A2 the authors clarify that $F$ has to be lower semicontinuous (but this is not enough, see below).
	- Lem A.1: under the correct assumptions (you also need differentability), this is the well-known Gronwall lemma; why you don't use this name. 	Please reformulate also in correct English. 
	- Lem A.2: The lemma is wrong (also in Hilbert spaces if you assume just $F$ is lsc, take just $F(y)= - exp(y)$), 
	not only the formulation ''algorithm (2) admits a minimizer'' .
	Suppose that the authors mean that the Wasserstein proxy exists for all $\rho$.
	Please address which metric is used (weak^* convergence)
		The closed balls in $\mathcal P_2(\mathbb R^d), W_2)$ 
	are known to be tight, see (M. Yue, D. Kuhn, and W. Wiesemann. On linear optimization over Wasserstein
balls. Math. Program., 2021, Theorem 1). On the other hand, under correct assumptions you can find the result of the whole lemma in Ambrosio's book.

	- line 676 what is $\mathcal B_C$?
	- line 681: it must be $K$ not $K_i$

	- Lem A3: Do you need some smoothness assumptions on $\rho$?

	- Lem A4:  This is exactly Prop. 3-1 , 3.3 Ambrosio 2023.  Further (2) is ''if and only if''
	  - line 716: there should be a ''='' between $D_+$ and $D_-$ 
		
	- Proof of Lem 3.1: Since Lem A2 is not correct it cannot be used in the proof.

	- Def B.1: reformulate, what is defined here
	Proof of Thm 3.2: line 316: why you have an additional $\xi$ in the second summand? 
	line 333: the last equality should be an inequality
	The rest appears to be correct.
	
		- Cor 3.4: what do you mean by $\varphi(x,y)$ ''is uniformly in $y$'' (uniformly what?)

- clean up the reference list, in particular please respect capitals

### Questions
- formula (2): maybe change $\rho'$ to something else, since the first one looks like a derivative
- line 067: there is a notation switch  between $\varphi$ and $\phi$
 - the authors write that they ,,assume that the strong subdifferential exists for every $\rho \in \mathcal P_2^a$'';
  this will never be the case; you do not mean this, so please fix
	- line 193 ''satisfy'' instead of ''satisfies''
	- line 208: A functional $F$
	- line 232: $v$ should be $\nu$
	- line 277: ''any stationary point  ... is a global minimum $F^*$''. Please reformulate, it is a global minimizer - not a minimum
	- Definition 3.2: give a reference to the Hopf-Lax ''formula''; maybe write that many definitions are taken from Ambrosio 2013;
	note that it resembles the Moreau envelope in the Hilbert space setting;
	further there is a notation mismatch: $\xi$ was used as subgradient, now it is the regularization parameter, in (2) this was $\eta$.
	The definition supposes that a (unique) proximum exists. I could live without ''unique'' if the authors write $\rho_\xi \in prox_{F,\xi} (\rho)$, but then the existence is only clear with additional assumptions on $F$. 
	In Lemma A2 the authors clarify that $F$ has to be lower semicontinuous (but this is not enough, see below).
	- Lem A.1: under the correct assumptions (you also need differentability), this is the well-known Gronwall lemma; why you don't use this name. 	Please reformulate also in correct English. 
	- Lem A.2: The lemma is wrong (also in Hilbert spaces if you assume just $F$ is lsc, take just $F(y)= - exp(y)$), 
	not only the formulation ''algorithm (2) admits a minimizer'' .
	Suppose that the authors mean that the Wasserstein proxy exists for all $\rho$.
	Please address which metric is used (weak^* convergence)
		The closed balls in $\mathcal P_2(\mathbb R^d), W_2)$ 
	are known to be tight, see (M. Yue, D. Kuhn, and W. Wiesemann. On linear optimization over Wasserstein
balls. Math. Program., 2021, Theorem 1). On the other hand, under correct assumptions you can find the result of the whole lemma in Ambrosio's book.

	- line 676 what is $\mathcal B_C$?
	- line 681: it must be $K$ not $K_i$
	
	- Lem A3: Do you need some smoothness assumptions on $\rho$?
	
	- Lem A4:  This is exactly Prop. 3-1 , 3.3 Ambrosio 2023.  Further (2) is ''if and only if''
	  - line 716: there should be a ''='' between $D_+$ and $D_-$
		
	- Proof of Lem 3.1: Since Lem A2 is not correct it cannot be used in the proof.
	
	- Def B.1: reformulate, what is defined here
	Proof of Thm 3.2: line 316: why you have an additional $\xi$ in the second summand? 
	line 333: the last equality should be an inequality
	The rest appears to be correct.
	
		- Cor 3.4: what do you mean by $\varphi(x,y)$ ''is uniformly in $y$'' (uniformly what?)
	
- clean up the reference list, in particular please respect capitals

### Soundness
1

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
4

### Summary
This paper provides convergence analysis of (inexact) Wasserstein proximal algorithm (WPA) for minimizing functionals satisfying PL inequality, where linear and unbiased convergence rates are achieved. This paper also sharpens the previous convergence analysis under strong geodesic convexity. Experiments on sampling from 1-D standard Gaussian and training mean-field neural network validate the faster convergence of Wasserstein proximal algorithm.

### Strengths
* This paper is the first to analyze Wasserstein proximal algorithm under PL-inequality and obtains linear and unbiased convergence rates, which is a generalization of proximal algorithm in Euclidean space without smoothness and convexity assumptions. For KL objective, PL-inequality is equivalent to log Sobolev inequality (LSI) which is interesting to MCMC community.

* This paper also sharpens the analysis of [Yao & Yang, 2023] and [Cheng et al., 2024] under strong geodesic convexity.

### Weaknesses
 * This paper doesn't show the implementation details of WPA. The proximal operator is intractable to calculate in the Wasserstein space.

* The convergence rate under PL for KL objective resembles the convergence rate of the proximal sampler under LSI  (Thm 3 of [Chen et al., 2024]}. However, the proximal sampler seems to be more implementable.

* The experiments are weak: the experiments only consider low dimension examples, but the large-scale problem setting is more interesting to machine learning and sampling community and the provided algorithm should be robust to large-scale problems. The implementation of WPA in training mean-field neural networks is ambiguous, especially for (17).

* This paper is short of some references discusing training mean-field neural network using mean-field Langevin algorithm such as [Fu & Wilson., 2023] and [Kook et al., 2024].

### Questions
* The WPA seems to be a natural generalization of proximal algorithm in Euclidean space, but the implementation is still unclear to me. How can you implement WPA generally? 

* For the application of WPA in sampling, as I mentioned in Weakness part, the rate of WPA for KL objective is the same as the rate of proximal sampler, but the proximal sampler is easier to implement. How is WPA competitive with proximal sampler?

* For the application of WPA in training mean-field neural networks, how can you implement update (17)? Can this be exactly solved or approximation? There should be more clarification on that. Also, this paper claims the unbiasedness with particle approximation as the only error resource. Can you show the approximation error in terms of the number of particles $N$? This could be interesting in this application. As is shown in [Kook et al., 2024], you can apply any unbiased log-concave samplers to sample from the empirical distribution, and the distance (KL, W2) between the empirical distribution and the solution of training mean-field neural networks is non-asymptotically bounded in terms of $N$. How is WPA competitive with other unbiased samplers?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors prove error rates of the proximal point algorithm in the Wasserstein space based on a Polyak-Lojasievwicz property. Moreover, they provide a convergence result under a certain small (exponentially decaying) error within the computation of the Wasserstein proximal mapping. The authors show some proof-of-concept numerics to show the validity of their claims.

### Strengths
The main result of the paper (Thm 3.2) seems to be correct and interesting to me. As far as I know, it extends the knwon convergence rates in terms of the function values. Also the part regarding the inexact update steps is highly relevant, since the solution of the Wasserstein proximal mapping is often just computed numerically.

### Weaknesses
I would like to emphasize that for most problems it is the hardest part to prove the PL property for the considered functional and not to derive convergence after the PL property is proven. The paper could benefit significantly from stating some lighter assumptions or examples where the PL property is fulfilled. The relation LSE vs PL goes in the right direction, but should be outlined more in detail.

Also, the authors only consider convergence rates in terms of the function value. They do not even mention existing convergence results in terms of the iterates (for strongly convex functionals, convergence rates in the Wasserstein metrics appear as a special case from [SKL2020], for (not strongly) convex functionals, weak convergence of the iterates was shown in [NS2022]).

In addition, even though I have not seen the main result in the literature, some concepts of the paper already appeared in the literature and the literature part on them should be clarified. Moreover, there exists plenty of technical errors and inexact parts in the paper. I include a list below (not ordered by importance).

Summarizing, the paper feels a bit unfinished. While the main result is interesting, the step towards convergence of the iterates is still missing. Moreover I would suggest to change the "beyond convexity" in the title to "under Polyak-Lojasievwicz property" to directly clarify the assumptions (or somehow else represent this assumption in the title). Finally, the paper currently contains too many small errors and typos for being published. I am willing to raise my score, when the authors correct the errors during the rebuttal phase.

List of confusions:

- Did I miss something or is Lemma A.1 just the Gronwall inequality (see https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality for references)? No need to reprove it.

- The assumptions required for the proof of Lemma A.2 are not sufficient. In order to use Prokorov's theorem for constructing a solution of the proximal map, you need that F is lsc *wrt weak convergence in $P_2(\mathbb{R}^d)$* (at least on $W_2$-bounded sets) which is a stronger assumption than lsc *wrt Wasserstein-2*. Under this stronger assumption the statement is already explained in [AGS2005] after eqt (10.3.1b).

- Regarding Definition 3.1 In the space of probability measures the PL property was already defined and used in [BV2023], see also "entropy-entropy production inequalities" from [KMV2016]. In particular, it is already outlined in [BV2023] that one obtains convergence of Wasserstein gradient flows via the Gronwall inequality. I am clear that this is not the same statement, since you are considering a (backward) discretizations of the gradient flow. However, since the main idea of your proof consists out of applying the Gronwall inequality, this coincidence should be mentioned.

- The proof of Lemma A.3 is not fully correct under these assumptions. In order to apply Lemma 10.4.1 from [AGS2005], the additional assumption $\rho\in C^1(\mathbb{R}^d)$ has to be fulfilled. In order to ensure this, you have to assume that your initialization is $C^1$ and that the iterates of the Wasserstein proximal point algorithm remain $C^1$ over the algorithm. A proof for this statement is missing.

- The notation in Section 3.2 and in the proof of Thm 3.8 gets completely messed up. The term $\eta_{n+1}$ (appearing first in line 383) remains undefined. Then the assumption of Thm 3.8 states that $\eta<1/L$ while the proof sets in line 785 sets $\eta=1/L$.

Small comments, formating errors and typos:

- To avoid confusion it would be worth mentioning that the Hopf-Lax formula is also known as Moreau-Yoshida approximation (cf. [AGS2005]).

- Lemma A.1: u maps from where to where?

- Lemma A.2: The domain of F is missing in the statement

- Lemma A.3: Assumptions are missing (for instance existance of optimal transport maps, F is lsc etc.).

- please define semiconvexity and clarify in Thm 3.8 that it is *geodesically* semiconvex.

- line 334: The last equality should be a greater or equal...

- line 783: $\beta$ is missing the index

- The green font color for citations is hard to read.

### Questions
I stated all my questions and suggestions in the weaknesses part.

### Soundness
2

### Presentation
2

### Contribution
3
