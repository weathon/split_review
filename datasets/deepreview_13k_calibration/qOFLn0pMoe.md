# High-Probability Convergence for Composite and Distributed Stochastic Minimization and Variational Inequalities with Heavy-Tailed Noise

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
High-probability analysis of stochastic first-order optimization methods under mild assumptions on the noise has been gaining a lot of attention in recent years. Typically, gradient clipping is one of the key algorithmic ingredients to derive good high-probability guarantees when the noise is heavy-tailed. However, if implemented na\"ively, clipping can spoil the convergence of the popular methods for composite and distributed optimization (\algname{Prox-SGD}/\algname{Parallel SGD}) even in the absence of any noise. Due to this reason, many works on high-probability analysis consider only unconstrained non-distributed problems, and the existing results for composite/distributed problems do not include some important special cases (like strongly convex problems) and are not optimal. To address this issue, we propose new stochastic methods for composite and distributed optimization based on the clipping of stochastic gradient differences and prove tight high-probability convergence results (including nearly optimal ones) for the new methods. In addition, we also develop new methods for composite and distributed variational inequalities and analyze the high-probability convergence of these methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of composite and distributed stochastic optimization and variational inequalities. The author aims at giving high probability convergence bounds for the two problems.
The author considers the setting that the noise has bounded central $\alpha$-th moment and uses the method of gradient clipping for this condition of heavy-tailed noise.

### Strengths
Strengths:
(1) This paper is written very well and is well-organized.
(2) Two standard problems (distributed composite stochastic optimization and distributed composite VIPs) are studied and many convergence bounds are given. In the first case, they develop two stochastic methods for composite minimization problems – Proximal Clipped SGD with shifts (Prox-clipped-SGD-shift) and Proximal Clipped Similar Triangles Method with shifts (Prox-clipped-SSTM-shift). Instead of clipping stochastic gradients, these methods clip the difference between the stochastic gradient and the shifts that are updated on the fly. In the second case, they also apply the proposed trick to the methods for variational inequalities.

### Weaknesses
 (1) High probability bounds do not bring some technical challenges than the in-expectation ones. After establishing the martingale difference sequences, the Freedman’s inequality is enough to give a high probability bound. In this line, there are numerous papers in recent years. 
(2) The technical contribution is limited. The author uses gradient clipping to handle the $\alpha$-th moment, which is frequently used in recent papers. The $\alpha$-th moment condition is also widely studied. Combining the technique in gradient clipping and the technique in distributed composite minimization/distributed composite VIPs, most of the results in this paper are easily obtained. 
(3) The paper is too long and more suitable for a review in the journal.
Refer to the following papers:
E. Gorbunov, M. Danilova, and A. Gasnikov. Stochastic optimization with heavy-tailed noise via accelerated gradient clipping. Advances in Neural Information Processing Systems, 33:15042– 344 15053, 2020a. 
E. Gorbunov, F. Hanzely, and P. Richtárik. A unified theory of sgd: Variance reduction, sampling, quantization and coordinate descent. In International Conference on Artificial Intelligence and Statistics, pages 680–690. PMLR, 2020b. 
E. Gorbunov, M. Danilova, I. Shibaev, P. Dvurechensky, and A. Gasnikov. Near-optimal high 349 probability complexity bounds for non-smooth stochastic optimization with heavy-tailed noise. arXiv preprint arXiv:2106.05958, 2021. 
E. Gorbunov, M. Danilova, D. Dobre, P. Dvurechenskii, A. Gasnikov, and G. Gidel. Clipped stochastic methods for variational inequalities with heavy-tailed noise. Advances in Neural Information Processing Systems, 35:31319–31332, 2022.
A. Beznosikov, E. Gorbunov, H. Berard, and N. Loizou. Stochastic gradient descent-ascent: Unified theory and new efficient methods. pages 172–235, 2023.
K. Mishchenko, E. Gorbunov, M. Takác, and P. Richtárik. Distributed learning with compressed gradient differences. arXiv preprint arXiv:1901.09269, 2019.
A. Sadiev, M. Danilova, E. Gorbunov, S. Horváth, G. Gidel, P. Dvurechensky, A. Gasnikov, and P. Richtárik. High-probability bounds for stochastic optimization and variational inequalities: the case of unbounded variance. arXiv preprint arXiv:2302.00999, 2023.

### Questions
What are the technical innovations of this paper compared to existing works? This paper seems to be a simple combination of existing techniques in related works.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Problem is to derive algorithms with high probability convergence rate guarantees with heavy-tailed noise and composite and distributed optimization and variational inequality. To go around the difficulty in the composite setting, the authors suggest using a technique involving clipping the difference between the stochastic gradients and a "shift" vector that is updated at every iteration to estimate the optimal gradient. The authors also consider the accelerated version of this method under both convexity or quasi-strong convexity assumptions. Similar results are also derived for variational inequality with assumptions such as star-cocoercivity, quasi strong monotonicity or monotonicity.

### Strengths
The paper is quite comprehensive, covering different problem templates such as convex or quasi strong convex, composite or distributed, moreover variational inequality with different assumptions. Heavy tailed noise and high probability guarantees are important avenues for research with potential impact in practice also due to the usage of clipped algorithms which also find use in practice. Since the research area is quite active, the table helps put the contributions in context. The developments of the ideas are well-motivated. For example, the authors show both naive or non-implementable approaches to highlight the difficulties and also point out the new techniques.

### Weaknesses
— Even though the paper takes the time to introduce the new ideas by the naive approach or non-implementable approach, since the paper is trying to do many things at the same time (distributed, convex, quasi strong convex), things get too complicated too quickly and makes it difficult for the reader to both understand and/or appreciate the novelties, new techniques or new results. For example, Theorem 2.2 is really difficult to unpack. Why not present a simpler version of the result in the main text and maybe also the crux of the analysis (which, from the presentation of the authors, is clipping the difference between shifts and the gradients) and how this helps. Right now, even though I see that the authors say including shifts and clipping differences is important, I cannot appreciate how this helps things in the analysis. I think it is better to have weaker/simpler results in the main text but convey the idea (both high level and technical) to the reader rather than trying to pack too many things into a small space.

Even though I think that the main idea for extension to composite case is well-explained (only on a high level, as I described above), what is the reason for this paper being able to extend to distributed setup but not the previous works? Since this is one of the main claims and focus of the paper, this is an important aspect.

For example, an important aspect of the analysis seems to be that the authors can provide a boundedness results for the iterates to go around the need to assume bounded domains. However, I cannot see explanations about this technique in the main paper which would help the reader get something out of the paper. Of course, this is developed in the earlier literature, but it is also used in this paper, so why not share this important point with the reader?

— Comparisons are quite confusing, especially with the work of Nguyen et al. 2023. Looking at the first section of the table, one can see that 3rd and 5th lines differ on following: 1. Nguyen et al. 2023 does not have distributed results (not clear if this is a fundamental drawback, i.e., why can't the results of Nguyen et al 2023 be extended to distributed setup in a straightforward way?) Second is the difference of R^2 vs V in the bounds. Even though it is difficult to unpack here too, after reading 9-line table description (a bit too long and probably would be better to have this clarification in the main text), I see that $R^2 \leq V$ since $V$ also includes terms with the norms of stochastic gradients at the solution. Then, this means that in terms of the constants, actually Nguyen et al. 2023 is better, is this correct? If so, it is better to state this in the paper for helping the reader understand both improvements in the paper and also the drawbacks compared to other works.

Also, the previous work by Nguyen et al. 2023 does not assume unique solution whereas this work does, why do we need this? The authors say in the footnote of page 3 that it is "for simplicity" but can we avoid it? What happens when we remove it? What does it affect in the analysis? Again, if this is a drawback compared to Nguyen et al. 2023 that seems more restrictive, this needs to be stated.

Another point is that for constrained setting, authors mention a couple of times the drawback of Nguyen et al. 2023 in requiring the gradient at the solution to be $0$, which is for sure an important drawback for a constrained result, on the other hand, depending on M and R, when Nguyen et al result applies, it is better, is this correct? Moreover, Nguyen et al. 2023 has the additional requirement for $\nabla f(x^*)=0$ but they don't seem to have the assumption of unique solution that the current submission has, how to compare these two (in the mere convex case) since they are both rather restrictive?

Also, skimming Nguyen et al. 2023, that paper seems to suggest that the approach also taken in this submission uses a union bound and resulting in a worse dependence in terms of the logarithmic terms. Since the authors do not put the dependence on the probability parameter in Theorem 2.2, it is difficult to compare, can the authors clarify? In my understanding, this drawback is appearing in the beginning of page 24, with an additional factor of $T$, is this the case? Can you please compare the dependence with log terms involving probability parameter compared to Nguyen et al. 2023?

— Organizations of the proofs are not very helpful for the reader. For example, Theorem D.1 has a 9 page proof and Theorem C.1 5-6 page proof, it is really difficult to follow for a reader. Please consider splitting to intermediate results and explaining the high level structure to help your reader.

— The paper is 115 pages. This, in a conference review cycle which gives to reviewers less than 20 days for 4-6 papers is a bit too much. Hence, I am not sure how suitable this paper is for a conference since there is almost no chance for reviewers to be able to do justice to this paper by checking the arguments. I can see that after page 55, the proofs for the variational inequality part starts and it is so long for the results that constitute 1 page in the main text making the presentation of the paper even worse. I appreciate that the authors are trying to avoid splitting too thin but maybe in this case, different papers are justified if the extension to variational inequality is significant enough. If not, the authors might decide to include this result only as a footnote and keep an "arXiv version" with full details. Submitting a version to a conference that can be reviewed is I think much better. This way, the authors will have enough space both in the main text and supplementary of the conference version to convey the main important ideas.

### Questions
Please see the questions above. I also summarize some of them below:

— What is the main reason making the extension of Nguyen et al. 2023 to distributed case non-straitghtforwrard and what is the main tool used in this submission for being able to handling distributed setup?

— What is the reason for assuming unique solution? Can it be avoided?

— With regards to Nguyen et al. 2023 how to compare different assumptions? This paper assumes unique solution and Nguyen et al 2023 assumes $\nabla f(x^*)=0$ in constrained case. Which one is more restrictive?

— Is it true that in terms of constants, Nguyen et al. 2023 has a better rate in the non-distributed setup?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies composite and distributed optimization as well as variational inequality problems. The paper proposes new stochastic gradient clipping methods with theoretical convergence bounds.

### Strengths
* The paper is technically sound. It provides theoretical analysis of the proposed methods. Proof sketches are presented to support the theoretical results. Related work and existing results on clipping methods are discussed in the paper
* The paper is well-written. The problem setting is clearly presented, followed by the proposed methods and theoretical analysis.

### Weaknesses
 * The significance can be enhanced by clarifying the motivation and theoretical improvements of the new clipping method, such as providing theoretical analysis to illustrate the efficiency of this gradient update. The contribution can be strengthened by including a discussion that compares the derived bounds in this paper with existing gradient clipping results.
* The main contribution of the paper is the introduction of new optimization methods. It would be great to include experiments to validate the proposed methods and compare them with relevant algorithms for both the optimization and variational inequality problems considered in this paper.
* The motivation for considering both composite optimization and variational inequality problems is unclear. These two problems appear to be independent and weakly connected. The contribution of addressing two problems appears incremental.

### Questions
1. Regarding Assumption 1, would it be better to clarify that equations (4) and (5) apply to all i in [n]?
2. It would be helpful to include a discussion after each theorem to compare the bound with existing clipping method bounds.
3. How would the proposed algorithm perform in the centralized composite optimization problem? Would it yield better convergence bounds compared to existing bounds?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
