# Representation of solutions of second-order linear equations in Barron space via Green's functions

- Decision: Reject
- Scores: 6, 5, 6, 6, 5

## Abstract
AI-based methods for solving high-dimensional partial differential equations (PDEs) have garnered significant attention as a promising approach to overcoming the curse of dimensionality faced by traditional techniques. This work establishes complexity estimates for the Barron norm of solutions of $d$-dimensional linear second-order PDEs, explicitly capturing the dependence on dimension. By leveraging well-developed theory for elliptic and parabolic equations, we represent the solutions of linear second-order equations using Green's functions. From these representations, we derive complexity bounds for the Barron norm of the solutions. Our results extend the prior work of  Chen et al. (2021) in two key aspects. First, we consider more general elliptic and parabolic equations; specifically, we address both time-independent and time-dependent equations. Second, we provide sufficient conditions on the coefficients of the PDEs under which the solutions belong to Barron space rather than approximating the solutions via Barron functions in the $H^1$ norm. As a result, our approach yields theoretically improved results, providing a more intuitive understanding when approximating the solutions of PDEs via two-layer neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper focuses on the theoretical underlying's of learning second order linear equations using shallow neural networks (SNN) (2 layer neural networks of the form $a (\sigma(w x +b)) )$ . The paper expands on previous works by showing that solutions of parabolic and elliptic PDEs can be represented in Barron space by using Green’s Functions, under the assumption of certain constraints and conditions. This work is directly applicable to physics-informed neural networks (PINNs) and shows that SNN can approximate the solutions to linear elliptic and parabolic PDEs without having to deal with the curse of dimensionality.

### Strengths
The paper provides very thorough proofs of all the theorems discussed in the paper. 
The paper provides an original proof to demonstrate that the solutions of linear PDEs can be approximated by a SNN.

### Weaknesses
While the specific theorems are unique, they only seem to be a minor change compared to previous works cited.
There were many grammatical errors throughout the entire paper that a simple spell check could have helped with.

### Questions
In assumptions 1, part (2) what are these details trying to say? It is not clear to the reviewer what the intuition is for these restrictions. Is this restriction related to how rapidly your dynamics can change? If so, in physical systems there can be large changes in a small amount of distance, do you believe the theory presented would hold if A(x,t) (or any of the other parameters) changed if the parameters change rapidly?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This research paper investigates the representation of solutions to second-order linear PDEs in Barron space, a function space that is particularly well-suited for approximation by neural networks. The authors leverage Green's functions to establish complexity estimates for the Barron norm of solutions, explicitly capturing the dependence on dimension. This work extends previous research by addressing both time-independent and time-dependent equations and by providing sufficient conditions for solutions to belong directly to Barron space, rather than just being approximated by Barron functions. The paper concludes by discussing potential future research directions, including extending the findings to nonlinear equations and exploring the use of machine learning for learning Green's functions.

### Strengths
1. The paper extends the analysis of solution representation in Barron space to time-dependent parabolic equations. This expands the scope of previous work by Chen et al. (2021), which focused primarily on elliptic PDEs.
2. The authors prove that, under specific conditions, solutions of elliptic and parabolic PDEs directly belong to the Barron space. This improves upon earlier work that only showed approximations of solutions within Barron space in the Sobolev sense.
3. This research establishes a theoretical foundation demonstrating that AI-based PDE solvers and Green’s function learning methods can represent solutions while avoiding the curse of dimensionality. Additionally, these findings may offer theoretical support for existing two-layer PINN methods, particularly in the context of high-dimensional problems.

### Weaknesses
1. The paper is purely theoretical and lacks numerical experiments to validate the theoretical findings. The authors should provide practical experiments to support their theorems, utilizing AI-based PDE solvers such as Green’s function learning methods or PINNs, as stated in the paper.
2. The analysis is confined to a limited class of linear second-order PDEs in $\mathbb{R}^d$. However, these equations represent relatively simple cases compared to the more complex PDEs addressed by recent developments in machine learning-based PDE solvers.
3. While the paper focuses on two-layer networks, deeper architectures are more commonly used in practice. The authors should consider extending their analysis to deeper networks to improve the relevance and applicability of their findings.
4. The paper uses the probabilistic definition of Barron space, which can be abstract and challenging to characterize function classes with.

### Questions
1. Can the authors provide practical experiments to support their theorems, utilizing AI-based PDE solvers such as Green’s function learning methods or PINNs?
2. The analysis relies on the ReLU activation function, which may not be optimal for AI-based PDE solvers. Can the authors provide more specific criteria for determining which activation functions would be suitable or unsuitable for their analysis? What modifications or adaptations would be necessary to accommodate different activation functions?
3. What specific AI-based PDE solvers do the authors have in mind? How do the theoretical findings, based on weak solutions, relate to the strong solutions typically sought by AI-based PDE solvers?
4. This paper is focused on a two-layer analysis, which seems somewhat limited, as practical architectures rarely use only two layers. Is it feasible to extend the analysis to multi-layer networks?
5. Given that the analysis is confined to a limited class of linear second-order PDEs in $\mathbb{R}^d$, which are relatively simple compared to the more complex PDEs addressed by recent machine learning-based PDE solvers, could the authors extend their approach to handle nonlinear PDEs or various boundary value problems?
6. Is it feasible to extend the analysis to the spectral Barron space setting? What challenges might arise, and what benefits could this alternative definition offer?  
7. Is there a difference between Assumption 1 and the assumption that it is based on self-adjoint elliptic PDEs? Can the authors characterize the types of PDEs to be considered in this paper?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper considers some a priori estimates of certain second-order liner parabolic and elliptic equations in terms of Barron spaces. Such estimates have been studied recently, but the present paper have several updates: (i) it gives an estimate for parabolic equations, while existing studies have focused on elliptic cases; (ii) even for the elliptic cases, it gives a better estimate.
In PDE theories, various estimates have been studied in major function spaces such as the Sobolev, Lebegue, Besov spaces. Compared to these function spaces, Barron spaces are more deeply connected to two-layer networks, and thus the current result gives insights about the efficiency of such networks in approximating solutions of the target equations.

### Strengths
I am not an expert on the research topic, and my review is based on the authors' claims and the closest work Chen+2021.

In reading these papers, I understood that a priori estimates in Barron spaces are important in approximation theories for shallow (two-layer) networks. On this topic, this paper has at least two new contributions.
(i) (According to the authors of the present paper,) up to Chen+2021 or its successors, basically only elliptic equations were considered. In PDE theories, it is quite standard and necessary to next consider parabolic, time-dependent systems. In this direction, (again according to the authors) the only preceding study is Weinan+2022, which gave some result for heat equation. This paper gives a new estimate on more general parabolic systems, which seems new and important. (On this point, please see my question below.)
(ii) For elliptic systems, Chen+2021 gave an estimate, but the estimate is described in terms of an $H^1$-solution which is in some sense close to the solution in the Barron space. This paper more directly gives an estimate in terms of the data $f$ (Theorem 2).

### Weaknesses
As written above, I am not an expert on this research field, and cannot say if the authors' claim on the novelty of this research is in fact correct or not. (I just compared the results with those in Chen+2021.) I also cannot judge the impact/novelty of the method of the argument. (The only thing I can say for sure is that argument with Green functions is one typical way in general PDE theories.)

From a person like me, one weakness of this paper is that the overall presentation is not quite clear (or direct), and some basic knowledge and/or comparison with related papers are necessary to understand the strength of this paper.
For example, on the second point (ii) in Strengths, the authors claim in L.98 that ``We establish that the solutions belong directly to Barron space rather than approximating them in the Sobolev sense.'' (I made the sentence short.) But its meaning is not explained later (as far as I understand.) In Remark 3, Theorem 2 is compared to the results in Chen+2021, but there the main topic seems to be the difference of assumptions. After going back and forth between these two papers I understood in the following way:

* Chen+2021 also gave an estimate on the solution $u$ in terms of a Barron norm; for example, Theorem 2.9. In this sense, Chen+2021 also shows the existence of a solution in Barron space (this first caused some confusion in me.) And it also discussed its dependence on the dimension parameter $d$.
* However, the estimate in Chen+2021 is constructed with a parameter $\varepsilon$, which is a distance from an associated $H^1$-solution of the target equation. In this sense, the bound is not natural.
* The present paper gives a more direct bound: a bound with the Barron norm of the data $f$.  This is what usually expected in PDE theories.

This effort might have been demanded simply because I am not an expert, but compared to the present paper, Chen+2021 was more simply written and easy to understand even for me. I hope that the presentation would be improved so that the description becomes more consistent, and the overall paper becomes much more readable for wide range of readers.
Please see Questions, where the confusions caused in me should be more visible.

### Questions
1. One of the biggest contribution of this paper should be the estimate for parabolic systems. The authors themselves mention that there is one existing study Weinan--Wojtowytch(2022), but no comparison is given. I think this should be clarified. (Maybe some comment on Theorem 1 compared with the results in Weinan+2022 is necessary.)
2. Similarly to the above, the strength of Theorem 2 compared with the results in Chen+2021 should be clarified. Is my understanding correct? If not, please clarify it.
3. I might misunderstand something, but it seems that the upper bound of the norm estimate in Theorem 2 tends to zero as $d\to \infty$ (the coefficient before $\| f\|$ seems to go to $0$.) Is this correct?

### Soundness
3

### Presentation
2

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
This work proves that the solution of second-order linear PDEs lies in Barron space using  Green’s functions, which provides theoretical support for PINN. This also gives a justification for answering why neural networks can break the curse of dimensionality for approximating the solution of high-dimensional partial differential equations. This is an extension work of  Chen et al. (2021). In this work, the authors consider more general elliptic and parabolic equations, including time-dependent problems. Unlike the previous work, the authors provide sufficient conditions on the coefficients of the PDEs instead of approximating the solutions via Barron functions in the $H_1$ norm.

### Strengths
This paper is generally well-written. The authors prove that under certain conditions, the solution of a class of PDEs belongs to Barron space. It answers why two-layer neural networks can approximate the solution of PDEs well, especially for time-dependent problems.

### Weaknesses
1. This work is a generalization of Chen et al. (2021). The proof framework is similar to Chen et al. (2021) and Weinan & Wojtowytsch, 2022.
2. I am not sure the conditions on the coefficients of PDEs are satisfied in practice. How do you check whether such conditions are satisfied?

3. In Assumption 1(1), for any $\boldsymbol{\xi}$ and $(t, \boldsymbol{x})$, there exsits two universal constants $0 < \lambda \leq \Lambda < 1$ such that the inequality holds. It seems that this assumption is strong. Could you give some example PDEs to illustrate that this assumption can be satisfied?
4. In Assumption 1(2), I wonder if the given sufficient condition is computationally verifiable.
5. Page 10, line 505-506, about the estimate $||u - u_{\delta} ||_{W_2^1(B_R)} \leq \frac{\tilde{C}_1}{R} + \tilde{C}_2 \delta^{\alpha}$. The authors state that $\tilde{C}_2$ depends on $R$ and other parameters; I wonder if this is a tight bound. If it is not tight, it does not give a meaningful estimate.
6. Line 289-290, "Suppose that $\mathbb{R}^d \subset \mathbb{R}^d$ is given". This sentence is a little bit confusing.
7.  Notation is not consistent. $(a,w,b)$ is used at the beginning of section 2.1, but $(a,\boldsymbol{b},c)$ is used in proposition 1. $(a,\boldsymbol{b},c)$ is the notation in the literature Ma et. al., 2022.
8. Minor issues. The cross reference in this manuscript does not work.

### Questions
1. In Assumption 1(1), for any $\boldsymbol{\xi}$ and $(t, \boldsymbol{x})$, there exsits two universal constants $0 < \lambda \leq \Lambda < 1$ such that the inequality holds. It seems that this assumption is strong. Could you give some example PDEs to illustrate that this assumption can be satisfied?
2. In Assumption 1(2), I wonder if the given sufficient condition is computationally verifiable.
3. Page 10, line 505-506, about the estimate $||u - u_{\delta} ||_{W_2^1(B_R)} \leq \frac{\tilde{C}_1}{R} + \tilde{C}_2 \delta^{\alpha}$. The authors state that $\tilde{C}_2$ depends on $R$ and other parameters; I wonder if this is a tight bound. If it is not tight, it does not give a meaningful estimate.
4. Line 289-290, "Suppose that $\mathbb{R}^d \subset \mathbb{R}^d$ is given". This sentence is a little bit confusing.
5.  Notation is not consistent. $(a,w,b)$ is used at the beginning of section 2.1, but $(a,\boldsymbol{b},c)$ is used in proposition 1. $(a,\boldsymbol{b},c)$ is the notation in the literature Ma et. al., 2022.
6. Minor issues. The cross reference in this manuscript does not work.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
A group of researchers have been using the concept of Barron spaces to explain why neural networks can overcome the curse of dimensionality. In this manuscript, the authors are showing that continuous solutions to some second-order linear PDEs are in a Barrow space, and they provide estimates for the Barron norm that have an explicitly dimension dependence.

### Strengths
- There is a surprising result that (continuous) solutions to elliptic PDEs (under many conditions) can lie directly in a Barron space. Barron spaces enable dimension-independent approximation rates for functions using neural networks, making them effective for understanding why NNs can overcome the curse of dimensionality.

- For each fixed t, the authors look at the Barron norm of u(t,.), and have an explicit factor on its growth with respect to t.

### Weaknesses
 - It looks like the Barrow norm estimates on the solution have a bound that depends on d, in a way that grows with d. The authors may want to comment on that as that might be a barrier for overcoming the curse of dimensionality in later investigations. 

- The biggest weaknesses is the requirement that the solution must be continuous. To guarantee that a solution is continuous, one typically has to rely on Sobolev embedding theorems and hence needs to impose more regularity on the coefficients of the PDE and righthand side. The reliance on Sobolev embedding theorems, while standard, introduces a significant constraint on the applicability of the results, as it necessitates strong regularity assumptions that may not hold in many practical scenarios. This limits the generality of the findings and should be addressed.

- One expects that Theorem 1 contains relatively weak estimates on the Barron norm of u(t,.). The growth of the Barron norm with respect to t, specifically as t^3, seems quite rapid and may not be optimal. This rapid growth could limit the practical utility of the result, especially for longer time horizons, and warrants further investigation into tighter bounds.

### Questions
- The assumptions on the elliptic equations make them self-adjoint in Section 1.3. Can your estimates be extended to solutions of non-self-adjoint elliptic operators?  Where is the technical barrier preventing you from extending this work? 

- In Theorem 1, shouldn’t ||c-b||_{L^\infty(\mathcal{D}) be replaced by an norm on (0,t)xR^d? I struggle to understand why the difference between c and b should impact the Barron norm of u(t,.). Also, why is it natural for your Barron norm in Theorem 1 to grow like t^3?

### Soundness
3

### Presentation
3

### Contribution
3
