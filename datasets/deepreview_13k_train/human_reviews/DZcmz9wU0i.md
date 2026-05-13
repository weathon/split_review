# Provable Convergence and Limitations of Geometric Tempering for Langevin Dynamics

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Geometric tempering is a popular approach to sampling from challenging multi-modal probability distributions by instead sampling from a sequence of distributions which interpolate, using the geometric mean, between an easier proposal distribution and the target distribution. In this paper, we theoretically investigate the soundness of this approach when the sampling algorithm is Langevin dynamics, proving both upper and lower bounds. Our upper bounds are the first analysis in the literature under functional inequalities. They assert the convergence of tempered Langevin in continuous and discrete-time, and their minimization leads to closed-form optimal tempering schedules for some pairs of proposal and target distributions. Our lower bounds demonstrate a simple case where the geometric tempering takes exponential time, and further reveal that the geometric tempering can suffer from poor functional inequalities and slow convergence, even when the target distribution is well-conditioned. Overall, our results indicate that geometric tempering may not help, and can even be harmful for convergence.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies the convergence guarantee of geometric tempering for the Langevin diffusion and its time-discretization the Langevin algorithm. The authors prove a convergence rate under a general tempering schedule, demonstrating dependency on the isoperimetry of the intermediate probability measures, in particular their log-Sobolev constant. While this constant can be suitably controlled when both measures are strongly log-concave, the authors show that even when both proposal and target densities are unimodal, intermediate measures can suffer from a poor log-Sobolev constant that scales exponentially with the distance between the modes of proposal and target measures.

### Strengths
While I am not an expert in annealing or tempering algorithms for sampling, it seems that this is the first paper that proves the convergence of geometric tempering for the Langevin diffusion using functional inequalities, which is interesting. The negative results also provide a good example of why tempering may not work in practice, despite both proposal and target measures having suitable isoperimetry.

### Weaknesses
 * The related work section could be better structured. For example, breaking into multiple paragraphs and adding paragraph titles could help with readability and following the discussion.
* The lower bound examples hold in dimension 1, and show exponentially bad dependence on the distance between modes. While these bounds are interesting, it is not very intuitive to me why it would be natural for the distance between modes to grow in fixed dimensions. On the other hand, in a high-dimensional setting, it is more intuitive that $m$ grows with square root of dimension. Could it be straightforward to (perhaps only intuitively) extend the lower bounds to high-dimensional settings?

* I believe for $KL(p_0, \mu_0)$ to disappear in Corollary 5, one needs to set $\lambda_0 = 0$. In that case, it would not be possible to choose $\lambda_t = 1$ for all $t > 0$ in a continuous manner.

* If all $\lambda_i$s are very close to 1 in Theorem 9, we are effectively running vanilla Langevin. In that case, why should we have exponential convergence time?

* The vanilla Langevin analysis only requires the log-Sobolev inequality and smoothness for discretization. Why do we additionally need dissipativity of proposal and target measures here?

    * In fact, the Langevin algorithm is known to convergence under extremely mild conditions, namely a weak Poincaré inequality (which holds for all locally bounded potentials, although without explicit control on the constant) and smoothness of the gradients, see e.g. [1] and references therein. Are there major challenges for obtaining convergence guarantees under (weak) Poincaré inequalities for the tempered Langevin algorithm? 

* Is there a sense in which one can choose optimal proposal distributions $\nu$ when we only know some information about $\pi$?

* I believe a summation over $i$ is missing in Equation (12).

* Some typos:
    * Line 152 missing absolute continuity before “... and $+\infty$ otherwise”.
    * Line 175: potential -> potentials
    * Line 119, 233, 253, 467: missing parentheses in citation
    * Line 238: satisfy -> satisfies
    * Line 336, 339, 383: section … -> Section …
    * Line 420: are unknown -> is unknown
    * Line 425: where we obtain
    * A typo in Line 439 makes the sentence unreadable.

### Questions
* I believe for $KL(p_0, \mu_0)$ to disappear in Corollary 5, one needs to set $\lambda_0 = 0$. In that case, it would not be possible to choose $\lambda_t = 1$ for all $t > 0$ in a continuous manner.

* If all $\lambda_i$s are very close to 1 in Theorem 9, we are effectively running vanilla Langevin. In that case, why should we have exponential convergence time?

* The vanilla Langevin analysis only requires the log-Sobolev inequality and smoothness for discretization. Why do we additionally need dissipativity of proposal and target measures here?

    * In fact, the Langevin algorithm is known to convergence under extremely mild conditions, namely a weak Poincaré inequality (which holds for all locally bounded potentials, although without explicit control on the constant) and smoothness of the gradients, see e.g. [1] and references therein. Are there major challenges for obtaining convergence guarantees under (weak) Poincaré inequalities for the tempered Langevin algorithm? 

* Is there a sense in which one can choose optimal proposal distributions $\nu$ when we only know some information about $\pi$?

* I believe a summation over $i$ is missing in Equation (12).

* Some typos:
    * Line 152 missing absolute continuity before “... and $+\infty$ otherwise”.
    * Line 175: potential -> potentials
    * Line 119, 233, 253, 467: missing parentheses in citation
    * Line 238: satisfy -> satisfies
    * Line 336, 339, 383: section … -> Section …
    * Line 420: are unknown -> is unknown
    * Line 425: where we obtain
    * A typo in Line 439 makes the sentence unreadable.




---
[1] A. Mousavi-Hosseini, T. Farghly, Y. He, K. Balasubramanian, M. A. Erdogdu. "Towards a Complete Analysis of Langevin Monte Carlo: Beyond Poincaré Inequality". COLT 2023.

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
4

### Summary
This paper presents a theoretical analysis of geometric tempering when applied to Langevin dynamics, a popular sampling method in machine learning and statistics. Geometric tempering is a technique that attempts to improve sampling from complex multi-modal distributions by sampling from a sequence of intermediate distributions that interpolate between an easy-to-sample proposal distribution and the target distribution. The authors provide the first convergence analysis under functional inequalities, proving both upper and lower bounds for tempered Langevin dynamics in continuous and discrete time. They also derive optimal tempering schedules for certain pairs of proposal and target distributions.

### Strengths
Perhaps surprisingly, the paper's findings are largely negative regarding the effectiveness of geometric tempering. The authors demonstrate that geometric tempering can actually worsen functional inequalities exponentially, even when both the proposal and target distributions have favorable properties. Through theoretical analysis, they show a simple bimodal case where geometric tempering takes exponential time to converge. More strikingly, they prove that similar poor convergence results can occur even with unimodal target distributions that have good functional inequalities. These results suggest that geometric tempering may not only fail to help with convergence but could actually be harmful in some cases, challenging the conventional wisdom about its utility.

### Weaknesses
In this paper they consider targets of the form $\nu^{1 - \lambda} \pi^{\lambda}$, where $\nu$ is called the proposal. In many other prior works, the targets are of the form $\pi^{\lambda}$, which corresponds to $\nu$ being an improper uniform distribution. This seems to be the main source of the largely negative results provided in this paper. Could the authors clarify the reason for considering target the above form?

### Questions
Please see question abobe

### Soundness
3

### Presentation
3

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
This paper offers a thorough study of geometric tempering combined with a Langevin MCMC scheme. In particular, a general theory is given which characterizes the error induced by said dynamics for arbitrary tempering schemes. Negative results are then given for the efficacy of tempering schemes (over the naive Langevin dynamics) both in terms of the intermediate distributions' log-Sobolev constants, as well as the worst-case convergence rate, although some regimes where the tempering is beneficial are highlighted.

### Strengths
The main positive result on geometric tempering (Theorem 3) seems quite thorough (in that it comprises every reasonable regime of interest) and about as good as one could hope for in this context.

The negative example is very intuitive and is a worthwhile inclusion into the paper. It offers a good characterization about why one might be skeptical about the occasional poor performance of these schemes in practice, and gives good intuition about the heart of the problem (the appearance of multimodality).

The inclusion of more concrete lower bounds is also insightful.

### Weaknesses
It would be more helpful if the paper offered more positive examples of instances where the tempering can improve over vanilla Langevin by at least polynomial factors; in particular, a comparative bound would be helpful in Propositions 6, 7. The current negative results, while insightful, leave the reader with a sense that tempering is rarely beneficial, which may not be the case in practice. The paper should aim to more clearly delineate the specific scenarios where geometric tempering provides a substantial advantage, rather than simply highlighting its potential drawbacks.

It would also be good if the paper could explore further the areas where tempering has a provable benefit over Langevin, especially in cases of multimodality where the algorithm would likely be used. The current analysis focuses primarily on worst-case scenarios and log-Sobolev constants, which may not fully capture the practical benefits of tempering in multimodal landscapes. A more nuanced analysis, perhaps considering specific types of multimodal distributions or introducing a measure of 'barrier height' between modes, would be valuable.

It is a bit strange to cite Durmus 2019 for the Langevin rate in the str. convex + smooth setting, compared to earlier work such as [1].

### Questions
The following suggestions relate to minor areas of the paper:

In Figure 2, should we not be scaling the $y$-axis logarithmically for a more reasonable demonstration?

The comment after (3) is strange. Probably, you mean to take $kh = t$ for a fixed choice of $t \in \mathbb R$, and then some schedule $h = t/K$ for a set of integers $K$, rather than what is written.

There is a spacing issue in Line 190~191.

Line 240: Lebesgue -> Lebesgue measure.

Line 425: where obtain-> where we obtain

It is a bit strange to cite Durmus 2019 for the Langevin rate in the str. convex + smooth setting, compared to earlier work such as [1].

Durmus, Alain, and Eric Moulines. "High-dimensional Bayesian inference via the unadjusted Langevin algorithm." (2019): 2854-2882.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work analyzes the convergence rate of Langevin dynamics with geometric tempering (LD-GT), a modification of the Langevin dynamics which attempts to follow the geometric path between a proposal distribution $\nu$ (e.g. a standard Gaussian) and the target distribution $\pi$. 
More precisely, LD-GT with tempering schedule $(\lambda_k)_k \subset [0,1]$ is

$$X_0 \sim \nu, ~~~~ X_{k+1} = X_k + h \nabla \log \mu_k(X_k) + \sqrt{2 h} \epsilon_k,$$

where $\mu_k \propto \nu^{1-\lambda_k} \pi^{\lambda_k}$ is the geometric path (and $\epsilon_k$ are independent Gaussians).

(Per the authors' account of the literature,) LD-GT was proposed since the 1990s, and one of the motivations is the intuition that sampling progressively from the path $\mu_k$ is easier than sampling directly from the target $\pi$, especially if $\pi$ is multi-modal. 

This work's contributions are two-fold:
- Precise convergence guarantees for LD-GT under certain common assumptions on the proposal $\nu$ and the target $\pi$: Poincare inequality (PI), log-Sobolev inequality (LSI), strong log-concavity.\
To this aim, a key sub-question is to estimate the PI or LSI constant of the path $(\mu_k)_k$. Besides showing how to best utilize well-known upper bounds, the authors also identify cases where these constants are surprisingly poor, leading to the next item.
- This work provides evidence that the original intuition motivating LD-GT is wrong, by exhibiting cases where LD-GT must converge very slowly (regardless of the choice of schedule). Remarkably this can even happen for well-conditioned and uni-modal targets $\pi$, for which vanilla LD can be expected to converge fast.

### Strengths
This paper addresses a natural question on the convergence of a sampling algorithm. The positive results (first item in "Summary") are of theoretical interest, as they address the technically difficult question of optimizing the upper bounds w.r.t the temperature schedule. The negative findings are surprising: namely, adding geometric tempering may actually slow down Langevin dynamics. This new insight is significant for both theory and practice.

The presentation is very clear and "flows" very nicely. All the technical claims are correct are far as I checked.

### Weaknesses
No substantial weaknesses, but the negative results of this paper naturally lead to a question which is not addressed nor mentioned in this paper, see "Questions" below.

Minor comments on the presentation:
- use citep instead of citet on lines 119, 233, 254, 468
- correct typos and/or grammar on lines 271, 326, 420, 496, 1389, 1494, 1838
- justify the fact that chi^2, KL > TV rather than say it "of course" holds (line 493)
- line 988 contains the proof of Corollary 13, not 17
- add details on the argument on line 1824 (I could not reconstruct it using Cauchy-Schwarz, only Jensen)
- use different markers for each curve in Figure 2
- consider using a log scale or showing less iterations in Figure 3
- consider including the example of section 4.1 in Figure 4, in addition to Figure 1 (which shows only $\lambda \in \{0, 0.45, 1\}$)

### Questions
The theoretical results in this work suggest that geometric tempering may not help the convergence of Langevin dynamics. Yet tempering is a strategy that is used in practice (per the authors' presentation of the literature). In practice, is tempering observed to lead to improved performance compared to vanilla Langevin dynamics? If yes, is there any intuitive reason why?

Minor questions:
- Would the conclusions, and the analysis techniques, of this paper still apply if one takes $\nu$ to be the Lebesgue measure instead of a probability measure?
- In practice, is the proposal $\nu$ always taken to be a Gaussian? Is it sometimes taken to be the Lebesgue measure? Or multi-modal?
- Is the $\frac{1}{2\alpha_\pi t}$ rate in Proposition 7 (line 433) classical? If so please give a reference.

### Soundness
4

### Presentation
4

### Contribution
3
