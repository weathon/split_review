# Tight Lower Bounds under Asymmetric High-Order Hölder Smoothness and Uniform Convexity

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
In this paper, we provide tight lower bounds for the oracle complexity of minimizing high-order Hölder smooth and uniformly convex functions. Specifically, for a function whose $p^{th}$-order derivatives are Hölder continuous with degree $\nu$ and parameter $H$, and that is uniformly convex with degree $q$ and parameter $\sigma$, we focus on two asymmetric cases: (1) $q > p + \nu$, and (2) $q < p+\nu$. Given up to $p^{th}$-order oracle access, we establish worst-case oracle complexities of $\Omega\left( \left( \frac{H}{\sigma}\right)^\frac{2}{3(p+\nu)-2}\left( \frac{\sigma}{\epsilon}\right)^\frac{2(q-p-\nu)}{q(3(p+\nu)-2)}\right)$ in the first case with an $\ell_\infty$-ball-truncated-Gaussian smoothed hard function and $\Omega\left(\left(\frac{H}{\sigma}\right)^\frac{2}{3(p+\nu)-2}+ \log\log\left(\left(\frac{\sigma^{p+\nu}}{H^q}\right)^\frac{1}{p+\nu-q}\frac{1}{\epsilon}\right)\right)$ in the second case, for reaching an $\epsilon$-approximate solution in terms of the optimality gap. Our analysis generalizes previous lower bounds for functions under first- and second-order smoothness as well as those for uniformly convex functions, and furthermore our results match the corresponding upper bounds in this general setting.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the oracle complexity of minimizing high-order Hölder smooth and uniformly convex functions, particularly under two asymmetric cases: when the degree of uniform convexity $q$ is greater than $p + \nu$, and when $q < p + \nu$, where $p$ is the order of smoothness, and $\nu$ is the Hölder degree. The authors establish tight lower bounds for these cases, generalizing previous lower bounds for uniformly convex functions with first- and second-order smoothness. They employ the $\ell_\infty$-ball-truncated Gaussian smoothing operator to achieve dimension-free smoothness for their hard function construction, providing theoretical insights into high-order optimization.

### Strengths
The problem studied in the paper is both important and well-motivated. The paper provides a rigorous analysis with novel contributions to the study of oracle complexity for asymmetric high-order convex functions, extending previous research by offering a general framework. The authors carefully construct proofs to demonstrate their lower bounds, presenting the results in a way that is accessible for further theoretical work. Additionally, the use of truncated Gaussian smoothing introduces an innovative approach to managing complexity in high-order smoothness contexts, achieving dimension-free smoothness without dependence on dimensionality.

### Weaknesses
The paper does not cover the case of $q= p + \nu$

### Questions
How might future work address the remaining case of $q = p + \nu$, and what specific challenges are anticipated?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies oracle lower bounds for minimizing high-order holder smooth and uniform convex objective functions using pth-order oracles. The lower bounds are proven by explicit construction of hard problem instances, and match known upper bounds for the function classes considered.

### Strengths
The paper presents the problem setup, ideas, and results clearly. The lower bounds obtained are tight, and contribute to the oracle complexity of convex optimization literature.

### Weaknesses
The paper presents the problem setup, ideas, and results clearly. The lower bounds obtained are tight, and contribute to the oracle complexity of convex optimization literature.

The paper provides oracle lower bounds for function classes not studied before (in terms of lower bound). The construction of the hard instances, although novel (e.g. using the truncated Gaussian for the smooth), inherits some ideas used previously. For instance, the function in line 218 - line 220 is also used in [1]. It would be great if the authors can provide a brief summary/comparison of which parts of the lower bound construction are used before, and which parts are new.



### Questions
Is the norm in $||\nabla^i f||$ (in line 201 and many other places) the operator norm?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies oracle complexity lower bounds for optimizing highly-smooth uniformly-convex functions with high-order methods.

Tight lower bounds are established in the "asymmetric" cases when $q\neq p+\nu$, where $q$ is the uniform-convexity degree, $\nu$ is the Holder-continuity degree, and $p$ is the oracle access degree.

### Strengths
This paper is well written. The results are motivated, well-explained and well-situated with respect to prior work.

I especially liked discussion such as the one appearing in lines 170-191 explaining the intuition in the lower bound construction, and the subtle challenges appearing with respect to prior work on similar subjects.

I haven't checked the math too carefully, but the authors make convincing points so that I believe the results should be solid.

### Weaknesses
One might argue that there isn't much technical novelty, as the two lower bound constructions are adaptations of previous know lower bounds (essentially the Nemirovski function and the Nesterov function), with relatively similar analyses to prior works.

Personally, I do not think this should prevent acceptance, as the authors explain what are the key differences, and the optimization community would benefit from these lower bounds being published.

One major concern is the claim in line 168 that Gaussian smoothing is dimension-free, while uniform smoothing over an l2 ball is not. This seems incorrect, as Gaussian smoothing is effectively uniform smoothing over an l2 ball with radius proportional to $\sqrt{d}$ due to concentration of measure. The authors appear to be comparing smoothing with different approximation parameters, which would naturally lead to different smoothness constants. Specifically, if one considers a $\delta$-approximation for both, the smoothness parameters should be comparable. The same issue arises with softmax smoothing, which has a $\log(d)$ factor in its approximation parameter, meaning that a $\delta$-approximation would have a smoothness constant of order $\log(d)/\delta$, which is not dimension-free, albeit a milder logarithmic dependence.

As written, the proofs hold for deterministic algorithms. The authors do not discuss what is the algorithm class their lower bound holds for, and specifically I believe their results hold for deterministic (or more generally, zero-respecting) algorithms. The first lower bound based on the Nemirovski max function should hold also for randomized algorithm (with a quadratically larger dimension) based on so called "robust-zero-chain" arguments due to "Lower bounds for finding stationary points" by Carmon et al., but these are not given by the authors. Moreover, the second lower bound based on in the Nesterov function is not a robust zero-chain so it shouldn't hold beyond deterministic/zero-respecting algorithms, if I am not mistaken. The authors should discuss this in their paper.



### Questions
## Two inaccuracies
I recommend to slightly revise the paper according to the following points:

1) In line 168 it is argued that Gaussian smoothing is dim-free, whereas uniform (over an l2 ball) is not. I believe this might be wrong, since they are essentially the same. Gaussian smoothing is nearly the same as uniform smoothing over an l2 ball with radius $\approx\sqrt{d}$, since the distributions are nearly the same by concentration of measure. So it's just that the authors seem to be comparing a $\delta$-approximation smoothing to a $\delta\sqrt{d}$-approximation, which clearly wouldn't have the same smoothing parameters. Is this the case, or am I missing something? Similarly, I believe the same is true for sofrmax smoothing, which isn't really dim-free since the approximation parameter has a $\log(d)$ factor. So making is $\delta$-approximate would mean that the smoothness constant is $\approx\log(d)/\delta$, no? This is a milder logarithmic dependence as opposed to polynomial, but still not entirely dim-free.

2) As written, the proofs hold for deterministic algorithms. The authors do not discuss what is the algorithm class their lower bound holds for, and specifically I believe their results hold for deterministic (or more generally, zero-respecting) algorithms. The first lower bound based on the Nemirovski max function should hold also for randomized algorithm (with a quadratically larger dimension) based on so called "robust-zero-chain" arguments due to "Lower bounds for finding stationary points" by Carmon et al., but these are not given by the authors. Moreover, the second lower bound based on in the Nesterov function is not a robust zero-chain so it shouldn't hold beyond deterministic/zero-respecting algorithms, if I am not mistaken. The authors should discuss this in their paper. 

## Additional question
- What seems to be preventing a lower bound for the symmetric $q=p+\nu$ case? Why do both proof techniques break? It would be great if the authors discuss this in the paper.


## Minor comments
- Notation: $\|\cdot\|$ refers to operator $\ell_2$ norms, maybe should emphasize this (just adding the word "operator") to avoid confusion with Frobenius l2.
- Lemma 1 (i) - the authors probably forgot to assume the function is $L$-Lipschitz.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides general lower bounds for functions, which are uniformly convex with degree $q$ and parameter $\sigma$ and whose $p^{th}$-order derivatives are H&ouml;lder smooth for degree $v$. The proposed lower bounds focus on two asymmetric cases: (1) $q>p+v$ and (2) $q<p+v$, matching the corresponding upper bounds in these cases.

### Strengths
* The proposed lower bounds on this work match the corresponding upper bounds for general algorithms in these settings, therefore the results are of great interest to the community.
* The use of the truncated Gaussian Smoothing using the $L_{&infin;}$-norm is an interesting technical novelty to circumvent the dimensionality dependencies that would arise otherwise when using Smoothing.

### Weaknesses
The main issue for me that causes confusion in section 4, concerning case (1) $q>p+v$ is the following:

* In line 327 in the lower bound for $F(x_T)-F(x^*)$ the first term is $-2p\beta\rho(T-1+5/8\sqrt{d})$, then you use the assumption that $2T\geq T-1+5/8\sqrt{d}$, however in line 328 your term becomes $-4\beta\rho T$, omitting $p$. I was wondering if there was a reason for this, as it is not discussed and in this setting $p\geq 1$, therefore for me it is not trivial to remove it.

In several places in the paper there are potentially typos that cause me confusion both in the main part and in the appendix. More specifically:

__Line 783__ $\rightarrow$ you say $1/\sqrt{d}$ is a truncated Gaussian, I think you meant to say $Z_i/\sqrt{d}$

__Line 230__ $\rightarrow$ I think it should be Lemma 1, not Lemma 14 according to the derivation in the appendix as well.

__Line 934__ $\rightarrow$ You have a $\beta^v$ appear in the first inequality, which is confusing to me does it not directly arise from the second inequality, where you use Lipschitzness?

__Line 293__ $\rightarrow$ I believe here that $x_t$ should be $x_s$.

__Line 296__ $\rightarrow$ Should the equality here be $\geq$, since the way that $e_{\alpha(s)}$ is chosen is for it to be the maximum possible that has not already been chosen.

__Line 317__ $\rightarrow$ Lemma 14 should be Lemma 1 here or am I mistaken?

__Line 1011__ $\rightarrow$ Similar to 296 it should be $\geq$ or am I mistaken here again?

__Line 1019__ $\rightarrow$ I think it would be beneficial to reference Lemma 1 here for justification as the write up is extremely lengthy and it caused some confusion for me here.

For Section 5, I only have one question. Concerning lines 402,403, what do you mean by scaling of $\tilde{f}$ and how does this imply directly that all of the properties of $\tilde{f}$ translate to properties of $f$. This seems a little bit informal to me.

I also found that there is at least one missing citation in the line of upper bounds for the case of H\"older Smooth functions.

### Questions
Please reference the weaknesses for my questions.

### Soundness
3

### Presentation
3

### Contribution
3
