# Analysis of a class of stochastic component-wise soft-clipping schemes

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 6, 3, 3

## Abstract
Choosing the optimization algorithm that performs best on a given machine learning problem is often delicate, and there is no guarantee that current state-of-the-art algorithms will perform well across all tasks. Consequently, the more reliable methods that one has at hand, the larger the likelihood of a good end result.  To this end, we introduce and analyze a large class of stochastic so-called soft-clipping schemes with a broad range of applications.
	Despite the wide adoption of clipping techniques in practice, soft-clipping methods have not been analyzed to a large extent in the literature. In particular, a rigorous mathematical analysis is lacking in the general, nonlinear case. Our analysis lays a theoretical foundation for a large class of such schemes, and motivates their usage.

	In particular, under standard assumptions such as Lipschitz continuous gradients of the objective function, we give rigorous proofs of convergence in expectation. These include rates in both the convex and the non-convex case, as well as almost sure convergence to a stationary point in the non-convex case. The computational cost of the analyzed schemes is essentially the same as that of stochastic gradient descent.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
As reminded in the paper, authors such as Mikolov (2013); Duchi et al. (2011); Kingma & Ba (2015) previously proposed element-wise gradient updates. In this paper, the authors recall the soft-clipping approach presented by Zhang et al. (2020a) and propose a class of methods that combine the idea of element-wise gradient updates with soft-clipping. To be more precise, the methods analyzed here are a direct generalization of the “element-wise clipped version” of the soft-clipping algorithm of Zhang et al. (2020a).

Under standard assumptions on the learning rate (Robbins–Monro conditions), standard regularity of the loss function, and standard noise assumptions, the authors prove that the class of stochastic optimizers they proposed converges to a stationary point. In particular, they show that the minimum norm of the gradient converges to 0. All the theoretical results presented in the paper are pretty standard, including the proof-technique aspect: Lemma 2 and Lemma 3, Theorem 1 and Theorem 2 are reminiscent of their respective version for vanilla SGD.

From an experimental aspect, the experiments compare the performance of the stochastic methods introduced in this paper w.r.t. well-known ones such as Adam, SGD + Momentum, and others. The authors conclude that their performances are comparable.

### Strengths
**Originality**: The authors present a novel class of stochastic optimizers that combine the idea of soft-clipping and element-wise gradient updates.

**Quality**: The theoretical setting is well-posed and well-presented. Indeed, all assumptions are clearly stated, grounded in the literature, and are not restrictive. Together with their proof, the theoretical results are clearly stated and easy to follow and understand.

**Clarity**: The key messages of the paper are clearly reported at the end of the "Introduction". The readers can follow the whole discussion with little effort.

**Significance**: Given the success of both soft-clipping and element-wise gradient updates, it is important to study if the interaction of these two ideas brings additional non-trivial advantages.

### Weaknesses
 **Research Aspect:**

While the topic is clearly of interest, I am left wondering about the effective novelty of the contribution. To be more specific, Theorem 3.1 and Theorem 3.2 in Zhang et al. (2020a) already provide convergence results for a hard-clipping algorithm. Additionally, in _Appendix F Soft Clipping_ of the same paper, the authors give a fairly reasonable explanation of why such results should easily generalize to the _soft-clipping_ version of their algorithm.

If I look at Theorem 1 and Theorem 2 of the paper under review, I observe that these are convergence results for optimizers which are a generalization of the “element-wise clipped version” of the soft-clipping algorithm of Zhang et al. (2020a).

While it is clear that these are different algorithms, it is not clear which additional theoretical benefit one inherits by allowing:
1) More general clipping functions (w.r.t. the one in Zhang et al. (2020a));
2) The element-wise clipping itself.

Questions presented later articulate my concerns and provide actionable suggestions on how to improve the contribution of this paper.

**Experimental Validation:**

The experiments presented compare the performance of the stochastic methods introduced in this paper w.r.t. well-known ones such as Adam, SGD + Momentum, and others. Here are some actionable suggestions to improve the experimental aspect of the paper:

1) Figure 1 and Figure 2 lack confidence bars around the lines to represent the uncertainty. They are difficult to read and it would be more interesting to plot those lines in log-scale to clearly see the comparison between the performance of the methods.

2) None of the experiments presented is meant to verify the theoretical insights provided in Section 2. Especially, it would be relevant to verify Theorem 1, Corollary 1, and Theorem 2. There is no need for sophisticated setups: I suggest starting with at least a simple landscape such as a quadratic one: $f(x) = x^{\top} A x$ where $x \in \mathbb{R}^d$ and $A \in \mathbb{R}^{d \times d}$ is or is not an SDP matrix would suffice.
Given that these are the core results of the paper, I would expect even a simple graph where you compare the decay of the minimum of the norm of the gradients w.r.t. the bound that you derive. This would not only validate the theoretical results empirically but also show how loose these bounds are. If anything, at least verifying this for Corollary 1 should be doable as the shape of the bound is very explicit.

3) I suggest adding a comparison of each clipped-component-wise method with its NON-component-wise version: This would help understand the benefit of the new methods and of clipping component-wise w.r.t clipping in a non-component-wise way.

**Quality of the Exposition**:

Regarding style and organization of the text, I would invite the author to reformulate the text written before Section 1 to:

1) Add a section named “Introduction” where you discuss the problem at hand, what you achieved in this paper, and how it is relevant;
2) Add a section called “Related Works” of “Literature Review”;
3) Make sure that the exposition is fluent and pleasant to read rather than a list of points: Separating text in paragraphs is very helpful.

Coming to **Section 1**, currently called Setting, I suggest moving this whole section to the Appendix and just quickly presenting the content of such a section: The assumptions are pretty standard and could be easily summarized in a sentence at the beginning of Section 2 (currently named “Converged Analysis”). For example, one could simply start Section 2 by stating _“In this section, we will provide a convergence analysis for all methods that fit into the setting that is described in the introduction. The assumptions are standard ones from the literature and are reported in Appendix C”_. Of course, if something is NOT standard in the literature, it is worth stating it clearly in the main paper.

Coming to **Section 2**, Lemma 2 and Lemma 3 are not key results and can be moved to the appendix.

Coming to **Section 3**, there is no need to report all the technical details of the numerical experiments in the main paper. I suggest moving the best portion of this section to the appendix.

Coming to the **Appendix**, please consider reporting the statements of the theorems before their proof.

Additionally, there are some typos. Among others, these are the most visible ones:

1) Just below Eq. (3). Please, specify where $(x_i,y_i)$, even if it is $(x_i,y_i) \in \mathcal{X} \times \mathcal{Y}$;
2) On the fifth row from the bottom of page 1: “If the function sufferS”. Add the “s”;
3) At the beginning of page 4: Add the capital letter T to “there” in both lines and add where $x_i$ belongs;
4) Third line from the top of page 3: “stochastic optimization algorithms that mitigateS this issue, is that of performing the gradient update”. Add the “s”.
5) Just above Lemma 2: “but their sharpnessES”. Add the plural. OR, keep it singular and at S after “differ”.

**Conclusion**:

This paper proposes a class of stochastic optimizers based on the combination of soft-clipping and element-wise gradient updates. The authors provide standard convergence bounds under standard assumptions: Their proofs are mostly based on standard techniques applied to the specific case addressed in the paper. The experimental section shows the performance comparison between some of the proposed methods and classic ones such as Adam and SGD + Momentum: The Accuracy and Perplexity are comparable across optimizers. Unfortunately, none of the theoretical results is experimentally validated.
To conclude, the class of optimizers is interesting, but the theoretical analysis provided here is too restricted to be a substantial contribution (questions below might provide inspiration). The experimental side is also lacking and deserves more attention (see above for some suggestions). From an organizational perspective, the manuscript needs significant rewriting (see above for some suggestions).

### Questions
Here is a list of questions that I think could guide the authors toward a better final product:

1) What is the behavior of the optimizers w.r.t escaping saddles? What about their preference for sharper or flatter minima?

2) Could you please elaborate on the advantages of component-wise clipping?

2.a) From a **theoretical perspective**,  I am not sure about the actual benefits of component-wise updates. Indeed, you use Assumption 1 only in the proof of Lemma 2 where you show that $\lVert H(\nabla f, \alpha) \rVert < c_h \lVert\nabla f \rVert^2$. Then, you (implicitly) use it also to derive a bound on the expected value of the norm of G. From my perspective, Assumption 1 could be replaced with the following:

i) There exists $c_g \in \mathbb{R}^{+}$ such that $\lVert G(x,\alpha) \rVert < c_g \lVert x \rVert$;

ii) There exists $c_h \in \mathbb{R}^{+}$ such that $\lVert H(x,\alpha) \rVert < c_h \lVert x \rVert^2$.

This way, you could cover more general cases, including yours and also that of Eq. (5) from Zhang et al. (2020a).

2.b) From an **experimental perspective**, in both of your experiments, it seems that Clipped SGD as implemented in Abadi et al. (2015) is the best performer. Is there any case you could find where component-wise clipped methods have better performance than the non-component-wise methods?

What I find missing is a comparison between the optimizer of Eq. (5) (which is without the component-wise clipping) and your component-wise clipped version. In general, for each component-wise clipped method you proposed, I would like to see a clear comparison with its counterpart without component-wise clipping. This would experimentally clarify that having a component-wise clipping is advantageous.

2.c) Of all the component-wise soft-clipping schemes provided, which ones are more advantageous? Is there a way to somewhat understand a recommended shape of the functions $g$ and/or $h$? Which ones clearly show an advantage w.r.t. the one in Eq. (7)? If one were to find one that works better than the one in Eq. (7), how about its NON-component-wise version?

**Minor Questions**:

1) Why is it necessary that $l$ is a non-negative loss function?
2) Can you be more explicit regarding G and H and their mutual relationship?
3) What is the relative size of the constants $B_i$ w.r.t the constant you would find with vanilla SGD? 
4) The scheduler used in the experiment is in line with those used in the theoretical results. However, I am sure you noticed that in 150 epochs, it drops from an initial value of $\beta$ to $\sim 0.985 \beta$. It does not strike me as a learning rate that decreases much. How would this compare to a learning rate kept constantly equal to $\beta$?
5) You write that _“We also note that the clipping schemes all require a higher step size for optimal performance than that of both Adam and SGD with momentum, which exemplifies their better stability properties”_. Can you elaborate further on this claim?
6) Could you please make sure that the colors of the lines of different optimizers are consistent between Figure 1 and Figure 2?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The article introduces a class of soft clipping schemes for various applications which have not been extensively analyzed in the literature, especially in nonlinear cases. It provides a theoretical foundation, demonstrating convergence properties, and highlights that these soft clipping algorithms perform similarly to state-of-the-art methods like Adam and SGD with momentum on large-scale machine learning tasks.

### Strengths
1.	The article gives proofs of convergence in expectation with rates in both the convex and the non-convex case.

2.	The numerical experiments in this paper are beautiful which shows that soft-clipping algorithms may offer regularization benefits in cases where other algorithms tend to overfit, encouraging the use of soft-clipping algorithms and further research in the field.

### Weaknesses
1.	The comparative analysis with other literatures is insufficient, and it is difficult to see the innovation of the convergence results or proofs in this paper.

2.	This paper lacks some intuitive understanding and analysis of the theorems and corollaries given. Especially for the symbols $\w_k(w)$ without interpretation in Corollary 2, it’s hard for readers to understand and what insight the corollary hopes to provide.

### Questions
1.	Have similar convergence analyses been conducted in other literature? If they exist, can you provide a comprehensive comparison to highlight the advantages of the results presented in this paper?

2.	Is it reasonable to assume that $\sum_{k=1}^\infty \alpha_k^2 < \infty$ and $\sum_{k=1}^\infty \alpha_k = \infty$ as stated in Theorem 1? Could you offer a more intuitively understandable explanation for this assumption?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors analyze a general soft-clipping scheme which extends vanilla clipping schemes such as the one from Eisenman & Stillfjord (2022), and the one from Zhang et al. (2020a). They provide its convergence analysis in the convex and non-convex setting under various assumptions. Furthermore they also compare such clipping schemes, instantiated with several clipping functions, with usual methods for training DNNs, and show that such method can achieve empirical results similar to state of the art methods.

### Strengths
### Originality

The results given in the paper are, up to my knowledge, novel. The fact that the method and its proof work for a very general range of clipping schemes makes such proof useful to a larger extend in the literature.

### Quality

Unless I am mistaken, overall the proofs look good and of quality.

### Clarity

The previous works, context, and assumptions for the theorems, as well as the main results (in theory and practice) are clearly described.

### Significance

I believe the problem considered is of interest to the community, since the authors considered the soft clipping scheme method, which has been shown empirically to obtain a good performance in practice, in particular for deep learning.

### Weaknesses
 - 1. I think that the comparison with state of the arts results (theorems, assumptions), could be made a bit more explicit and structured (see question 1 below)
- 2. I think that the reason why considering new special soft-clipping schemes could be elaborated on further (see question 2 below).

### Questions
1. Although the state of the art is well stated which allows one to dig further into the appropriate references, I believe a more explicit *comparison* with the state of the art, gathered at one place in the paper (perhaps in Appendix) would improve the quality of the paper. For instance, I think the two most related papers are the ones from Eisenman & Stillfjord (2022), and the one from Zhang et al. (2020a). Even though by checking those references one may get some idea on the difference between those papers and the submitted one (i.e. Eisenman & Stillfjord (2022) only deal with a strongly convex setting, while Zhang et al. (2020a) have slightly different assumptions, and also, the submitted paper studies a general form of clipping)), I still think it would be good to compare the method exposed in the paper with those two papers more systematically (perhaps in Appendix, in a structured form such as a table) (for instance, saying which algorithms is a special case of which (some algorithms may have momentum, some may have general component-wise functions etc), what assumptions they make in the papers, and what is the resulting convergence rate. For instance, in the strongly convex setting, does the results in the paper retrieve the results from Eisenman & Stillfjord (2022) ? Also, it would be interesting if possible to compare how taking different assumptions and/or considering more general settings actually impacts the proofs compared to the previous ones in the literature. 

2. Although a general form of clipping is analyzed, if I am not mistaken, I didn’t see any motivation or related works related to the new gradient clipping schemes from the Appendix A (i.e. Examples 2-4). And in practice it seems that those do not make a big difference (most curves are superimposed so it is hard to differentiate them). Therefore, even though having a general convergence proof is always good, I think it would be even better to further motivate the use of any of the new Examples 2-4 from Appendix A, for instance by mentioning whether they are present in the literature, discussing how their shape depart from the classic soft-clipping (and why it is advantageous), or through experimental results that would show their advantage in some cases.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the family of SGD-type methods with non-linear transformation of the stochastic gradient such that this transformation can be seen as a linear approximation of the stochastic gradient w.r.t. the stepsize. Under standard assumptions (Lipshitz gradients, bounded variance) and some non-standard assumptions (boundedness of the third moments of the iterates) the authors derive $\mathcal{O}(\frac{1}{\ln(K)})$ and $\mathcal{O}(\frac{1}{K})$ convergence rates for non-convex and strongly convex cases respectively. Some special cases of the methods fitting the considered framework are tested in the numerical experiments with the training of neural networks. They show similar (slightly worse sometimes) performances to the standard methods like Clipped-SGD or Adam.

### Strengths
S1. The paper is clearly written and the overall idea of considering different non-linearities/clipping operators is promising.

S2. The proofs are correct.

### Weaknesses
W1. The paper does not provide a justification of why and when it is beneficial to use the considered methods.

- W1.1. From the theoretical perspective, the existing results under considered assumptions are either stronger or match the derived ones. Indeed, under bounded variance and smoothness assumptions, standard SGD also converges (and the known rates are even better), e.g., see [1, 2]. The authors claim that their methods do not require step size restrictions, but this is achieved by using a different assumption (Assumption 6) which effectively replaces the step size restriction with a bound on the third moment of the iterates. This is not a relaxation of assumptions, but a change of assumptions, and the standard SGD analysis can also be performed without step size restrictions under the same assumptions.

- W1.2. From a practical perspective, the considered methods do not show better performance than the standard methods in the experiments considered in the paper. Moreover, since the stepsize decreases over time, all the considered methods will be very close to standard SGD (in view of formula (9)), which is known to have bad convergence on some problems with a lack of smoothness [3] or with a presence of the heavy-tailed noise [4, 5]. The authors argue that the considered methods should behave similarly to standard clipping in heavy-tailed noise settings, but this is not obvious since the proposed methods can be seen as SGD with a quadratic perturbation w.r.t. the stepsize. Furthermore, the settings considered in the submission are not suitable for heavy-tailed noise since they assume bounded variance, which is a stronger condition.

W2. Although the paper focuses on the theoretical analysis of the considered methods, the derived results require improvements.

- W2.1. Assumption 6 is quite restrictive: it is unclear apriori whether it holds in the considered setup. Indeed, it can be the case that $\mathbb{E}[\|\|w^k - w^\ast \|\|^3] = \infty$ while Assumptions 3 and 4 are satisfied, e.g., for simple quadratic function with linear noise $f(v,\xi) = \|\|v\|\|^2 + \langle \xi, v \rangle$, where $\xi$ is zero mean random vector with a bounded variance but an unbounded third moment (e.g., one can take shifted Pareto distribution with tails decaying as $x^{-4}$) we have Assumption 3 with $L_{\xi} \equiv 2$, Assumption 4 is also satisfied with some $\sigma$, but Assumption 6 is not satisfied. The authors refer to the work of Eisenmann & Stillfjord (2022), but in that work, it is assumed that the fourth moment of the gradient is bounded (and the fourth moment of $L_\xi$) to derive Assumption 6. Such assumptions are even stronger than for the standard analysis of SGD. Even in the finite-sum case, where the third moment exists, assuming that Assumption 6 holds for all $k$ is a strong assumption that requires a formal justification, as it implies some form of stability of the method.

- W2.2. The result of Theorem 1 seems to be not tight: when full gradients are used the theorem does not recover the rate of a deterministic counterpart -- Gradient Descent. This happens because $B_i \neq 0$ even when full gradients are used in the method. A similar issue is present in Theorem 2. Moreover, one can improve the rate from Corollary 1 to $\mathcal{O}(1/\sqrt{K})$ (instead of $\mathcal{O}(\frac{1}{\ln(K)})$) if one takes $\alpha_k \equiv 1/\sqrt{K}$. The fact that the analysis does not recover the best-known results in standard cases raises concerns about its tightness in other non-trivial cases.

- W2.3. Assumption 1 does not include some interesting special cases as standard gradient clipping (the second part of the assumption does not hold). It seems that even with the updated assumption, standard component-wise clipping is still not covered.

### Questions
My main question is about the motivation of this work: why and when SGD-type methods with soft clipping should be used? In the current shape, the theory shows no benefit over the existing results. Moreover, the derived results are even weaker since they rely on an additional restrictive assumption. The numerical experiments also do not provide enough evidence that the methods with soft-clipping can outperform the existing algorithms (in both experiments standard Clipped-SGD performs better than other methods with soft clipping).

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes and studies a class of component-wise soft clipping algorithms. For strongly convex and non-convex smooth objective functions, the authors establish convergence guarantees of the proposed methods to minimizer/ stationary points. To verify the theoretical results, the authors conduct experiments demonstrating the effectiveness of the soft clipping methods.

### Strengths
The paper is well written and is easy to read. 

The theoretical analysis looks correct, though I do not check all the technical details. The soft clipping framework seems novel.

### Weaknesses
1) Although the authors mention in the abstract that theoretical guarantees can provide guidelines for us to choose what algorithms to use, there is little discussion about this aspect in the paper. More specifically, it is unclear through the theoretical results why or when soft clipping is better than hard clipping or vanilla SGD. For the non-convex case, the convergence rate is only $O(1/\log K)$ which is much slower that standard results for GD/SGD or (hard) gradient clipping, though the assumptions seem to be a little different. The paper does not provide any concrete guidance on how the derived theoretical results can be used to select appropriate clipping parameters or even justify the use of soft clipping over other methods in practical scenarios. The theoretical analysis, while seemingly correct, lacks a clear connection to practical algorithm design and selection.

2) It seems to me that although soft and hard clipping are not exactly equivalent, they are basically the same since the induced step size only differs by a constant scale. In the introduction, the authors motivate the study of soft clipping by saying that "A drawback of the rescaling in (4) is that it is not a differentiable function of the gradient", which looks confusing, since it is unclear why being differentiable here is favorable. The paper does not elaborate on the specific benefits of differentiability in this context, especially considering that hard clipping, despite its non-differentiability, is widely used and performs well in practice. The argument for differentiability as a key advantage is not sufficiently justified.

3) I think there are some existing works on either component-wise or non component-wise clipping, and some of them are cited in this paper, but there is little comparison between these papers and the current paper. The paper lacks a thorough comparison with existing literature, making it difficult to assess the novelty and practical impact of the proposed soft clipping methods. A more detailed discussion of how this work differs from and improves upon existing clipping techniques is needed.

### Questions
1) In the experiments, do you compare component-wise clipped SGD with the original clipping method (non component wise)? 

2) Can you briefly discuss why the theoretical results in this paper imply that component-wise clipped SGD is superior to other popular methods?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
