# Emergence of Alignment and Local Elasticity in Two-Layer Neural Networks

- Decision: Reject
- Avg Score: 3.83
- Scores: 3, 3, 6, 5, 3, 3

## Abstract
Investigating phenomena such as Alignment and Local Elasticity is essential for understanding feature space of Neural Networks and enhancing performance across a wide range of tasks.
In this context, we investigate the emergence of these phenomena in two-layer neural networks performing a classification task.
This paper reveals Alignment and Local Elasticity emergence condition after one step of training are identical. 
In particular, we demonstrate that intra-class features are more aligned when the inner product of their mean and the covariance of the training data-label \ie \textit{train-unseen similarity} is large, with stronger Local Elasticity occurring under this condition.
We validate our theory through experiments with a two-layer network showing that both Alignment and Local Elasticity improve as the train-unseen similarity increases.
Furthermore, we claim that our analysis provides both theoretical and practical insights into the relationship between train-unseen similarity, alignment, and the improvement of clustering performance on unseen data for neural networks trained on similar domain data. This is supported by experiments, including a multi-layer CNN setup and detailed discussions.
Specifically, we show that higher train-unseen similarity improves Recall@1 in two-layer networks and that Alignment and Recall@1 exhibit a positive correlation in metric learning. 
We also present novel techniques for deriving operator norm bounds of non-centered Sub-Gaussian matrices, extending conventional regression analysis with standard Gaussian assumptions to the binary  classification setting.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The manuscript analyzes feature alignment and local elasticity in two layer nretworks trained with a single gradient step in the proportional regime. The authors extend similar proof scheme by (Ba et al. 2022, Moniri et al. 2024) in the context of Sub-Gaussian data and classification problems with two separable classes. They consider data distribution that might differ with respect to the training one; they characterize the effect of the distribution shift on the resulting feature alignment and local elasticity properties. They provide numerical illustrations to support their claims.

### Strengths
The main strength of this paper stands in the nice research idea. There have been different works in theoretical machine learning dealing with learned representations in two-layer networks trained with one step of gradient; this manuscript extends findings in the literature introducing novel data distribution and learning setting.

### Weaknesses
The main weakness of this work is the presentation of the manuscript. In many places the authors try to give intuition behind their results; although this is certainly welcome, the resulting effect is a disordered exposition in the main text that needs to be enhanced. The paper heavily relies on techniques already proven in other works, this fact induces some concern on the clear elements of novelty of this submission. The numerical illustrations are far from being clear.

The authors, in the first part of the main text, try to provide intuition behind their results. However, the resulting effect is a higher confusion. Figure 1 is far from being clear, and I struggled to understand many parts of this plot. For example: the origin is present only in the left panel; (a,b,c,d) are training data from the legend but this is not clear from the picture; $(a_1,a_2)$ are not defined in the central panel; the sphere and their transormed mapping are not defined; what are the grey arrows supposed to mean in the right panel?

In page 2 the math is not sound. One needs to provide a mathematical consistent definition; for example: $c_3, c_4$ are not clearly specified in Defs (1.1,1.2); the indices are not specified in the sum of Theorems (1.3,1.4). 

The concepts of Local Elasticity and Alignment structure are firstly defined in these definitions, and reported by citing related papers. There is never an explanation what these phenomena really are. The explanations associated are often unsatisfactory; for example: "Our analysis implicates that Alignment and Local Elasticity have strong relevance with how close ($\beta^T \mu$) the data distributions are to the training samples". It is not clear what is meant here.

Similarly to the above, the explanation for the CK framework is never provided and the authors refer only to related works.

A large part of the technical results should be moved to the appendix in order to provide more space for the intuition building. The results are largely extension of previous techniques to different settings, therefore the authors should focus more on the discussion of their results. All the lemmas between Page 6 and 8 could be moved to the appendix in my opinion for enhancing the discussion in the main text.

The related works section should be expaned. I would advice to compact the short section in Page 3 with the introduction to provide a more broad view on the field.

How crucial is the learning rate assumption scaling? [1] extended (Moniri et al. 2024) to the maximal learning rate scaling regime showing the presence of fully non-linear equivalent map. Also heuristic arguments would be welcome on this point.

The numerical illustrations need to be changed. Figures (3,4,5) are not understandable as the font size is too small.

It would be interesting to observe distribution shift that are not limited to $e\mu$ presented in this manuscript. Can the authors comment on this point?

I do not understand the training procedure detailed in Page 5. What does it mean to have a subscript $c$ for the second layer $a_c$?

Other minor points below. 
- Abstract: "recall@1"; Page 1: "Enable deep learning" -> "Enable deep learning methods"; Page 1: "1 1unseen"; Page 4: recall what is $\beta$ for the reader.

### Questions
The main concern on my side is the clarity of the exposition, below I will try to give some pointers for the authors. 

- The authors, in the first part of the main text, try to provide intuition behind their results. However, the resulting effect is a higher confusion. Figure 1 is far from being clear, and I struggled to understand many parts of this plot. For example: the origin is present only in the left panel; (a,b,c,d) are training data from the legend but this is not clear from the picture; $(a_1,a_2)$ are not defined in the central panel; the sphere and their transormed mapping are not defined; what are the grey arrows supposed to mean in the right panel? 

- In page 2 the math is not sound. One needs to provide a mathematical consistent definition; for example: $c_3, c_4$ are not clearly specified in Defs (1.1,1.2); the indices are not specified in the sum of Theorems (1.3,1.4). 

- The concepts of Local Elasticity and Alignment structure are firstly defined in these definitions, and reported by citing related papers. There is never an explanation what these phenomena really are. The explanations associated are often unsatisfactory; for example: "Our analysis implicates that Alignment and Local Elasticity have strong relevance with how close ($\beta^T \mu$) the data distributions are to the training samples". It is not clear what is meant here. 

- Similarly to the above, the explanation for the CK framework is never provided and the authors refer only to related works. 

- A large part of the technical results should be moved to the appendix in order to provide more space for the intuition building. The results are largely extension of previous techniques to different settings, therefore the authors should focus more on the discussion of their results. All the lemmas between Page 6 and 8 could be moved to the appendix in my opinion for enhancing the discussion in the main text. 

- The related works section should be expaned. I would advice to compact the short section in Page 3 with the introduction to provide a more broad view on the field. 


Regarding the technical part of the contribution, below are few pointers.

- How crucial is the learning rate assumption scaling? [1] extended (Moniri et al. 2024) to the maximal learning rate scaling regime showing the presence of fully non-linear equivalent map. Also heuristic arguments would be welcome on this point. 
      
[1] Asymptotics of feature learning in two-layer networks after one gradient-step, Cui et al. 2024. 

- The numerical illustrations need to be changed. Figures (3,4,5) are not understandable as the font size is too small. 

- It would be interesting to observe distribution shift that are not limited to $e\mu$ presented in this manuscript. Can the authors comment on this point? 

- I do not understand the training procedure detailed in Page 5. What does it mean to have a subscript $c$ for the second layer $a_c$?

Other minor points below. 
- Abstract: "recall@1"; Page 1: "Enable deep learning" -> "Enable deep learning methods"; Page 1: "1 1unseen"; Page 4: recall what is $\beta$ for the reader.

### Soundness
1

### Presentation
1

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
The paper studies the behavior of two quantities, namely *alignment* and *local elasticity*, in the training of a two-layer neural network via GD. Such quantities are used to characterize the feature learning phenomenon in a classification task: under the training process, they allow the authors to show that features enhance the alignment of samples from evaluation distributions which are similar to the training dataset. The results are validated by a number of numerical experiments.

### Strengths
The paper deals with an interesting topic, namely the deformation of the input data structure induced by a neural network and how it correlates with the training dataset as a single-step GD training is performed. The setup is quite generic, as the authors considered a two-layer neural network admitting a possible non-convex loss. As a result, it is found that the 'strength' of the deformation depends on how much the evaluation dataset is similar to the training set. Although this might appear not entirely surprising (the network has indeed been trained specifically to learn the characterizing features of the training dataset, and search afterward for similar features in the input), the paper proposes a quantitative approach to the problem by studying two quantities of interest, namely the alignment and the local elasticity, and show how such quantities indeed depend on the correlation between training database and signal in the input.

### Weaknesses
Unfortunately, the quality of the text is very poor, both at the $\mathrm{\LaTeX}$ editing level and in writing. Quantities are often not specified, sentences are sometimes broken (e.g., see lines 329-330, where a sentence reads "Under the assumption that new data is sampled from a multivariate normal distribution, i.e. $x\sim\mathcal N(\mu,\Sigma)$." missing the main clause [??]), notation is not introduced properly and conventions appears to change from one section to another, making the reading very difficult (see below for just a few comments). This lack of clarity and exposition quality results in compromised readability, and is, in my opinion, a major obstacle to the publication of the manuscript. On top of this, the discussion of the main theoretical results is minimal, and at some point confusing: see the *Questions* section where I list a series of points both on the form and on the content.

*Comments and questions*
- What does "11unseen" mean at line 050? At line 086 $F$ is introduced, but neither the dimension of $x$ nor the dimension of $W$ nor how $\sigma$ acts are clarified: I suppose the authors rely on the (at this point) standard notation in the discussed setup but all of this has to be specified, also because at line 107 $\beta$ appears and it is rescaled by $n\sqrt N$, both unspecified quantities. At some point in the text, the authors write "In case of any confusion of notation, please refer to Appendix C for clarification": although I understand that compactness is required in ICLR, I fear there is a limit to what can be deferred to the Appendix...
- The concept of *Evaluation sample* is referred to in Definition 1.1 without being introduced (its meaning is given at page 4). Similarly, the authors refer to $c_3$ and $c_4$ without giving context: this issue reappears in Definition 1.2. Therein, the definition of local elasticity is also confusing: do the local elasticity conditions depend on the chosen ordered pair $(c_3,c_4)$ as it looks? Despite being on page 2, it is not obvious what the authors are referring to, and their actual goal becomes more transparent only once the reading of the entire manuscript is complete...
- Although informal, statements of Theorems 1.3 and Theorem 1.4 hide, in my opinion, too many details: some of them (for example the range of some running indices, as in Theorem 1.3) can be inferred, but others have to be dug out from the Appendix subsequent pages, such as the (apparently absent, at first) role of the nonlinearity or the $x$ distribution.
- Is the orthogonal decomposition required for $\sigma(x)$ at line 167 the one explicitly stated soon after in terms of Hermite polynomials? 
- In line 184, the authors refer to an extension that might open "new avenues for analysis of deep representation of classification". Are they referring to the sub-gaussian assumption? Is it not a very common assumption for asymptotic analysis in particular when a Gaussian equivalence principle is applied or proved? Incidentally, Fig 2's relation with the product similarity to $\beta$ is not clear and its presence here, in my opinion, only adds confusion on the considered setup: it might be worth moving it directly to section 6 where the experiments are discussed.
- At line 202, it seems that the label vector $y$ of each datapoint is a row or column vector depending on the class (?!). Also, according to what is written here, $Y\in\mathbb R^{n\times 2}$, whereas $X\in\mathbb R^{n\times d}$. On the other hand, using a different (!?) notation, $\beta=\frac{1}{n\sqrt N}X^\top y$. The dimension of $\beta$ is not clear. If the authors meant  $\beta=\frac{1}{n\sqrt N}X^\top Y$, then $\beta\in\mathbb R^{d\times 2}$, so that $\beta^\top\mu\in\mathbb R^2$, whereas it seems that $\beta\in\mathbb R^d$.
- The reference to the training algorithm is not clear at line 204 as the loss used has not yet been specified.
- If $X\in\mathbb R^{n\times d}$ as in line 201 and $W\in\mathbb R^{d\times N}$ as in line 224, the product $XW^\top$ in Eq 2 is inconsistent. Assuming it to be $XW$, then $\frac{1}{\sqrt N}\sigma(XW)a_c\in\mathbb R^d$: if $y[c]$ has the same as $y_1$, $y_2$ defined at line 203, then it should be an $n$-dimensional vector, which would create another inconsistency... In Eq 3 another notation is used once again, namely $y[:,c]$ in place of $y[c]$ (?) and possibly $Y[:,c]$?
- Unless I am wrong, in the decomposition of the gradient in Eq 4, in the first two lines $a$ should be replaced by $a_2$: please check.
- The "proof" of Proposition 4.1 might benefit from moving some of the arguments above inside the proof itself or removed, as it essentially says that the Proposition is true... Proof of Lemma 4.3 in the main text, is not a genuine proof (nor a sketch). What $\Theta_{\mathbb P}$ means?
- Isn't Lemma 5.1 a special case of Theorem 5.2 obtained by taking e.g. $k=0$?
- Theorems 5.3 and 5.4 should be the core of the contribution, yet the comment on them is minimal and the expression of the alignment is given in terms of quantities whose definition is postponed in the appendix. Eq 11 is also unintelligible without sorting to the Appendix. It also seems that the result actually depends on the specific instance of the training dataset through $\beta$, as, in my understanding, the authors only average on the evaluation point. In this sense, I would have expected the theory or experiments to be simplified by some concentration result, as the one obtained in the proportional regime for classification tasks, e.g., by [Mignacco et al. (2020)](https://proceedings.mlr.press/v119/mignacco20a.html) or [Loureiro et al. (2021)](https://proceedings.neurips.cc/paper/2021/hash/543e83748234f7cbab21aa0ade66565f-Abstract.html) for the case of convex losses. Could the authors comment on this? Does concentration occur? On a side note, I am not sure if using the letter [מ‎](https://en.wikipedia.org/wiki/Mem) in Theorem 5.3 improves the readability of the manuscript (as the use of ב in Appendix H). The authors might consider the use of Latin and Greek letters, but this is, of course, up to them.
- What do the authors mean by "Considering randomness, we assume that the sole term $\mathscr C_{j,k}$ represents the Alignment"?
- I might have missed it, but the notation introduced in line 377 is never used in the main text, and is perhaps inconsistent, as $F_0(x)$ is put equal to both $F_0$ and $F'_0$ (?!).
- The dataset construction described in the *Data generation* paragraph in Section 6 is not very clear, e.g., it is not clear if the hyperplane is orthogonal to $\mu$ and passes through $e\mu$. A few additional lines, e.g., the description in Appendix A, should clarify.
- The appendix is written very poorly and, in some points, looks more like a collection of sketchy notes, rich in typos and poor in comments. In some points, the text is just confusing. For example, in line 890 the authors write "$\mathcal N_{(a,b)}(\mu,\sigma)$ is truncated Gaussian s.t. support of distribution, $\mathrm{supp}(\mathcal N_{(a,b)}(\mu, \sigma^2))\in(a, b)$, which is also known as Sub-Gaussian familly". Aside from typos and inconsistent notation in just one sentence, the definition looks different from the usual one, and indeed a dedicated Lemma D.1 is later introduced to *prove* that truncated Gaussians are subGaussians.
- Labels in the experiment figures are extremely small and almost unreadable.
- What is the role played by the separability condition on the training dataset in the theoretical analysis?
- It is not clear to me if Fig 3 and Fig 4 represent the results of the experiments only or if any quantitative comparison with the theoretical prediction is given. Could the authors clarify this point?
- In the discussion of the Recall @ 1 performance, the authors say that "the second phase provides a dataset which effectively supports training for retrieval tasks and is explainable by our theory": could the author clarify this point? From the plots, it looks like the Recall @ 1 performance is not obviously correlated with the Alignment results.
- What is the role of $\psi_1$ and $\psi_2$? Do the authors run multiple instances of their setup to obtain their curves?
- As a final comment, I iterate that on multiple points, the paper is not clear, lacks precision, or presents typos. I recommend a re-reading to improve grammar and fix some evident typos or the bad rendering of formulas and citations (e.g., in line 100 "say" has to be replaced with "Say" and $E_{x_3}$ has to be changed to $\mathbb E_{x_3}$; at line 297 maybe "hence" is better than "where", a space is missing before the definition of $\alpha$, which incidentally has the same name of the learning rate exponent, etc — tracking all typos in the manuscript would be a demanding task). Moreover, the text seems to be written using directly a "Python-like" notation fpr matrices, that it might be made more standard.

### Questions
*Comments and questions*
- What does "11unseen" mean at line 050? At line 086 $F$ is introduced, but neither the dimension of $x$ nor the dimension of $W$ nor how $\sigma$ acts are clarified: I suppose the authors rely on the (at this point) standard notation in the discussed setup but all of this has to be specified, also because at line 107 $\beta$ appears and it is rescaled by $n\sqrt N$, both unspecified quantities. At some point in the text, the authors write "In case of any confusion of notation, please refer to Appendix C for clarification": although I understand that compactness is required in ICLR, I fear there is a limit to what can be deferred to the Appendix...
- The concept of *Evaluation sample* is referred to in Definition 1.1 without being introduced (its meaning is given at page 4). Similarly, the authors refer to $c_3$ and $c_4$ without giving context: this issue reappears in Definition 1.2. Therein, the definition of local elasticity is also confusing: do the local elasticity conditions depend on the chosen ordered pair $(c_3,c_4)$ as it looks? Despite being on page 2, it is not obvious what the authors are referring to, and their actual goal becomes more transparent only once the reading of the entire manuscript is complete...
- Although informal, statements of Theorems 1.3 and Theorem 1.4 hide, in my opinion, too many details: some of them (for example the range of some running indices, as in Theorem 1.3) can be inferred, but others have to be dug out from the Appendix subsequent pages, such as the (apparently absent, at first) role of the nonlinearity or the $x$ distribution.
- Is the orthogonal decomposition required for $\sigma(x)$ at line 167 the one explicitly stated soon after in terms of Hermite polynomials? 
- In line 184, the authors refer to an extension that might open "new avenues for analysis of deep representation of classification". Are they referring to the sub-gaussian assumption? Is it not a very common assumption for asymptotic analysis in particular when a Gaussian equivalence principle is applied or proved? Incidentally, Fig 2's relation with the product similarity to $\beta$ is not clear and its presence here, in my opinion, only adds confusion on the considered setup: it might be worth moving it directly to section 6 where the experiments are discussed.
- At line 202, it seems that the label vector $y$ of each datapoint is a row or column vector depending on the class (?!). Also, according to what is written here, $Y\in\mathbb R^{n\times 2}$, whereas $X\in\mathbb R^{n\times d}$. On the other hand, using a different (!?) notation, $\beta=\frac{1}{n\sqrt N}X^\top y$. The dimension of $\beta$ is not clear. If the authors meant  $\beta=\frac{1}{n\sqrt N}X^\top Y$, then $\beta\in\mathbb R^{d\times 2}$, so that $\beta^\top\mu\in\mathbb R^2$, whereas it seems that $\beta\in\mathbb R^d$.
- The reference to the training algorithm is not clear at line 204 as the loss used has not yet been specified.
- If $X\in\mathbb R^{n\times d}$ as in line 201 and $W\in\mathbb R^{d\times N}$ as in line 224, the product $XW^\top$ in Eq 2 is inconsistent. Assuming it to be $XW$, then $\frac{1}{\sqrt N}\sigma(XW)a_c\in\mathbb R^d$: if $y[c]$ has the same as $y_1$, $y_2$ defined at line 203, then it should be an $n$-dimensional vector, which would create another inconsistency... In Eq 3 another notation is used once again, namely $y[:,c]$ in place of $y[c]$ (?) and possibly $Y[:,c]$?
- Unless I am wrong, in the decomposition of the gradient in Eq 4, in the first two lines $a$ should be replaced by $a_2$: please check.
- The "proof" of Proposition 4.1 might benefit from moving some of the arguments above inside the proof itself or removed, as it essentially says that the Proposition is true... Proof of Lemma 4.3 in the main text, is not a genuine proof (nor a sketch). What $\Theta_{\mathbb P}$ means?
- Isn't Lemma 5.1 a special case of Theorem 5.2 obtained by taking e.g. $k=0$?
- Theorems 5.3 and 5.4 should be the core of the contribution, yet the comment on them is minimal and the expression of the alignment is given in terms of quantities whose definition is postponed in the appendix. Eq 11 is also unintelligible without sorting to the Appendix. It also seems that the result actually depends on the specific instance of the training dataset through $\beta$, as, in my understanding, the authors only average on the evaluation point. In this sense, I would have expected the theory or experiments to be simplified by some concentration result, as the one obtained in the proportional regime for classification tasks, e.g., by [Mignacco et al. (2020)](https://proceedings.mlr.press/v119/mignacco20a.html) or [Loureiro et al. (2021)](https://proceedings.neurips.cc/paper/2021/hash/543e83748234f7cbab21aa0ade66565f-Abstract.html) for the case of convex losses. Could the authors comment on this? Does concentration occur? On a side note, I am not sure if using the letter [מ‎](https://en.wikipedia.org/wiki/Mem) in Theorem 5.3 improves the readability of the manuscript (as the use of ב in Appendix H). The authors might consider the use of Latin and Greek letters, but this is, of course, up to them.
- What do the authors mean by "Considering randomness, we assume that the sole term $\mathscr C_{j,k}$ represents the Alignment"?
- I might have missed it, but the notation introduced in line 377 is never used in the main text, and is perhaps inconsistent, as $F_0(x)$ is put equal to both $F_0$ and $F'_0$ (?!).
- The dataset construction described in the *Data generation* paragraph in Section 6 is not very clear, e.g., it is not clear if the hyperplane is orthogonal to $\mu$ and passes through $e\mu$. A few additional lines, e.g., the description in Appendix A, should clarify.
- The appendix is written very poorly and, in some points, looks more like a collection of sketchy notes, rich in typos and poor in comments. In some points, the text is just confusing. For example, in line 890 the authors write "$\mathcal N_{(a,b)}(\mu,\sigma)$ is truncated Gaussian s.t. support of distribution, $\mathrm{supp}(\mathcal N_{(a,b)}(\mu, \sigma^2))\in(a, b)$, which is also known as Sub-Gaussian familly". Aside from typos and inconsistent notation in just one sentence, the definition looks different from the usual one, and indeed a dedicated Lemma D.1 is later introduced to *prove* that truncated Gaussians are subGaussians.
- Labels in the experiment figures are extremely small and almost unreadable.
- What is the role played by the separability condition on the training dataset in the theoretical analysis?
- It is not clear to me if Fig 3 and Fig 4 represent the results of the experiments only or if any quantitative comparison with the theoretical prediction is given. Could the authors clarify this point?
- In the discussion of the Recall @ 1 performance, the authors say that "the second phase provides a dataset which effectively supports training for retrieval tasks and is explainable by our theory": could the author clarify this point? From the plots, it looks like the Recall @ 1 performance is not obviously correlated with the Alignment results.
- What is the role of $\psi_1$ and $\psi_2$? Do the authors run multiple instances of their setup to obtain their curves?
- As a final comment, I iterate that on multiple points, the paper is not clear, lacks precision, or presents typos. I recommend a re-reading to improve grammar and fix some evident typos or the bad rendering of formulas and citations (e.g., in line 100 "say" has to be replaced with "Say" and $E_{x_3}$ has to be changed to $\mathbb E_{x_3}$; at line 297 maybe "hence" is better than "where", a space is missing before the definition of $\alpha$, which incidentally has the same name of the learning rate exponent, etc — tracking all typos in the manuscript would be a demanding task). Moreover, the text seems to be written using directly a "Python-like" notation fpr matrices, that it might be made more standard.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the alignment and local elasticity in the feature learning process. Specifically, the authors analyze a two-layer neural network trained in the high dimensional limit and show the expression of alignment and local elasticity in this regime. Based on the theoretical analysis, the authors show that when the training data is closer to the data distribution, the class will have a better alignment and local elasticity.

### Strengths
The paper provides a rigorous theoretical foundation for alignment and local elasticity in a two-layer neural network with the explicit formula on both metrics. The analysis is solid and it provides a new perspective on feature learning in neural networks.

### Weaknesses
1. The presentation of the theoretical works needs to be improved, see Questions below. Specifically, many results are not well discussed in terms of their implications. The connection between the theoretical results and the practical implications for feature learning is not clearly established. For example, while the paper derives explicit formulas for alignment and local elasticity, it does not sufficiently explain how these formulas can be used to guide the design of better feature learning algorithms or architectures. The discussion lacks concrete examples of how the derived metrics can be used to diagnose and improve the performance of neural networks in practice. 

2. Experiments are limited to simulation data only. It would be very helpful to verify if the conclusion still holds when going beyond the simple two-layer neural network settings. The simulation data used in the experiments may not accurately reflect the complexities of real-world datasets. The paper should include experiments on more challenging datasets, such as those from computer vision or natural language processing, to demonstrate the generalizability of the theoretical findings. The lack of experiments on real-world data limits the practical relevance of the study. It is unclear if the observed relationships between data distribution, alignment, and local elasticity would hold in more complex scenarios.

3. It is unclear how to conclude Theorem 1.3 and 1.4 based on the formal version of Theorem 5.3 and 5.4. The authors should include more discussion on the relationship between these two results. The paper does not provide a clear and detailed explanation of how the results from the high-dimensional analysis in Theorem 5.3 and 5.4 translate to the finite-dimensional results presented in Theorem 1.3 and 1.4. The connection between the asymptotic regime and the practical setting is not well established, making it difficult to assess the practical significance of the theoretical findings. The authors should provide a more rigorous discussion of the assumptions and approximations made in the theoretical analysis and how they affect the validity of the conclusions.

### Questions
1. Why do Theorem 5.3 and 5.4 both appear in high probability formulation? The equation for the expectation is deterministic on both sides, what is the exact randomness here? 

2. Section 4 seems to be purely technical lemmas and has no direct implication on the main conclusion of the paper, therefore I suggest the authors defer it to the appendix. 

3. It is unclear how to conclude Theorem 1.3 and 1.4 based on the formal version of Theorem 5.3 and 5.4. The authors should include more discussion on the relationship between these two results.

4. Is it essential to use two-layer neural networks to conclude the relationship between $\mu^T\beta$ and the alignment and local elasticity? The conclusion is rather simple so I suspect onc may reach the same conclusion even in the linear model.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studies the change in the feature of a two layer network after one step of gradient descent. They showed that both alignment and local-elasticity emerges after one step of training

### Strengths
Both alignment and local elasticity are interesting concepts in deep learning and this work studies how they emerge during training.

The math is solid and the theoretical results are sufficiently clean that they can be understood rather easily

### Weaknesses
I think there are a few weaknesses.

1. The theorems are not sufficiently clear. For example, the result seems to only deal with one step of gradient descent after initialization, and neither theorem statements made this clear

2. The problem setting only deals with classification and this should be made clear in the abstract

3. The work claims to discover the relationship/connection between alignment and local elasticity in many places, but I do not see or understand what exactly is this connection. The conclusion I can draw from the paper is that they both occur after 1 step of GD, but co-occurrence does not feel like a strong enough connection

4. The problem setting is also very unclear. Judging from the problem setting 3.2, is only the first layer being trained? Perhaps it is, because training the second layer or not is irrelevant if the model is only trained for one step

5. After all, I think the problem setting is too restricted (two layer net, classification task, one step of GD) and the message is not sufficiently strong or interesting

Minor:
The figures are not quite visible. The fonts should be a lot larger

### Questions
Can the alignment part of the result be related to the alignment phenomena discussed in https://arxiv.org/abs/2410.03006？

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies feature learning in the conjugate kernel model with a focus on two phenomena called "alignment" and "local elasticity". The main observation is that, after one step of training, a distribution similar to the training data shows improved feature alignment and "stronger" elasticity.

### Strengths
Understanding scaling limits of feature learning is clearly an important theoretical direction so the topic is timely and worthwhile. The model setting (conjugate kernel) is an interesting one for questions of feature learning and remains under explored, in my opinion. The paper also converts the regression setting of Ba et al to a classification task, which could highlight important differences between the two the problems.

### Weaknesses
 - Throughout, the assumptions, theoretical setting, and analysis are presented in extremely unclearly. Notation frequently appears without introduction, for example, in Sec. 1.1, no assumptions are stated about the task, training data, objective, network used, etc. The distributions $c_3$ and $c_4$ appear without introduction (though they appear in Fig. 1) and why the subscripts 3 and 4 are used is never explained. Theorems 1.3 and 1.4 are stated without any real introduction and appear more to be more like approximate asymptotic calculations than anything close to a theorem.
- The lack of clarity extends to the writing and discussion of the related works. The alignment and local elasticity section of the related work is especially difficult to parse. What does it mean: "it is theoretically known that the Alignment structure corresponds to the situation where features from training data are aligned around labels"? Statements like this appear throughout the section and do not help to contextualize the results presented in the paper. It is unclear what specific theoretical results are being referenced, and how they relate to the current work. The paper would benefit from a more precise discussion of the existing literature on alignment and local elasticity in feature learning.
- I was not able to identify what the author(s) consider to be the main contribution. The informal theorems essentially state that the features align with the feature vector that results from optimization using unregularized least squares regression. This is not presented as a novel or surprising finding, and the paper does not adequately explain why this is an important result. The connection between the informal theorems and the formal theorems is also not clear.
- The formal theorem statements are arguably even less precise than the informal ones. For example, in 5.3, essentially nothing is directly defined and all the variable names are deferred to the appendix. At this point, it's not even useful to include it because it's simply uninterpretable. The lack of definitions makes it impossible to assess the validity or significance of the theorem. The reader is left to guess at the meaning of the variables and the scope of the result.
- The most important weakness is the lack of rigor. Assumptions are not stated, even in the more detailed theoretical results. For example, in Theorem 5.3, which is essentially just a calculation, none of the notation is even introduced in the main text, and the details given in Appendix H have odd formatting and typos. The absence of clearly stated assumptions makes it impossible to determine the conditions under which the results hold. The typos and formatting issues further undermine the credibility of the theoretical analysis.

### Questions
- What is the main theoretical contribution? 
- Can the authors state the results in a way that more clearly delineates the essential assumptions?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies two feature learning measurements: alignment and local elasticity of a two-layer neural network. They specifically show alignments between the neurons get improved within classes, and local elasticity emerges after a large gradient descent step. They consider the setting when the number of samples, the number of features and the input dimension go to infinity. They further implement numerical experiments to verify the phenomena.

### Strengths
1. Feature learning is an important topic in the theoretical foundations of deep learning. The alignment phenomenon observed in this paper seems to be interesting and could be useful to explain the success of neural networks.
2. The setup considered in this paper is a nice one to study feature learning of neural networks.

### Weaknesses
1. I do not see the motivation to study the alignment and local elasticity. They do seem to have some relation to feature learning, but the paper fails to show why such feature learning is important for better generalization. I think either designing experiments to explicitly show that improving alignment leads to better generalization or analytically building connections between generalization and alignment can be useful.

2. The machinery used in this paper is mainly developed by Ba et al. (2022). I do not see interesting new techniques. Please correct me if I miss anything.

3.  The writing of the paper needs improvement. I had a difficult time understanding the paper. 
- For example, definitions 1.1 and 1.2 do not seem to be sufficiently formal. 
- Also, why do theorem 1.3 and 1.4 hold with probability? Where does the randomness come from?
- How to see the improvement of alignment through the arguments in Theorem 5.3? The same in Theorem 5.4. 

There are many typos and missing periods. I will list a few below, but there are many more.
- Line 050 11unseen
- Line 168 extra period after $Hn(x)$
- Line 202 datum
- Line 202 the first y is a column vector but the second y is a row vector. 
- Line 226 missing period
- Line 298 no space between let and $\alpha$
- Line 309, 311,315 missing period
- …

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1
