# Understanding Augmentation-based Self-Supervised Representation Learning via RKHS Approximation and Regression

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
Data augmentation is critical to the empirical success of modern self-supervised representation learning, such as contrastive learning and masked language modeling.
However, a theoretical understanding of the exact role of augmentation remains limited.
Recent work has built the connection between self-supervised learning and the approximation of the top eigenspace of a graph Laplacian operator, suggesting that learning a linear probe atop such representation can be connected to RKHS regression.
Building on this insight, this work delves into a statistical analysis of augmentation-based pretraining.
Starting from the isometry property, a geometric characterization of the target function given by the augmentation, we disentangle the effects of the model and the augmentation,
and prove two generalization bounds that are free of model complexity.
Our first bound works for an arbitrary encoder, where the prediction error is decomposed as the sum of an estimation error incurred by fitting a linear probe with RKHS regression, and an approximation error entailed by RKHS approximation.
Our second bound specifically addresses the case where the encoder is near-optimal, that is it approximates the top-$d$ eigenspace of the RKHS induced by the augmentation.
A key ingredient in our analysis is the \textit{augmentation complexity},
which we use to quantitatively compare different augmentations and analyze their impact on downstream performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work provides a statistical analysis of augmentation-based pretraining using the so-called augmentation operator. This operator is naturally introduced and several properties of this operator are stated. Upper and lower error bounds, which apply to arbitrary encoders, are derived. The augmentation complexity is emphasized as a central object contributing to error analysis in both learning and augmentation.

### Strengths
The paper gives a structured foundation for augmentation based learning. The augmentation operator is well motivated and its central role is well highlighted. The obtained error bounds show, in a good way, a separation in the contribution of the model and the augmentation. The analysis seems rigorous and, personally, I find the appearance of the spectral properties of the augmentation intriguing.

### Weaknesses
-I find the text very dense and compressed; and thus not easy to read. I acknowledge that the task of fitting the results and concepts in the 9 page limit is difficult. Therefore, I would suggest that the authors consider whether the text is better published in a journal with fewer page restrictions.
-Some concepts could be motivated more. That is particularly helpful for readers less familiar with the topic. For example, the motivation behind the choice of the distribution $P_{AX}$ is not immediately clear. Additionally, while the space $\mathcal{F}_B(\Gamma;\epsilon)$ is central to the paper, a more intuitive explanation of its significance would be beneficial.
-I find, that the assumptions and notations should be pointed out more clearly. For instance

       -it seems it is assumed, but I did not see it stated explicitly, that $P_\mathcal{A}$ has a density, and that $p(a|x)$ and $p(x|a)$ exist.

       -What is A in E(g(A)|x). Similarly, X is not defined as a random variable (it is clear from the context but should be defined).
      
       -The notational difference between $p$ and $p(\cdot,\cdot)$ is small.

-Is $\hat{\psi}$ always assumed to be of the form (10) or is (10) just an example? The form of $\hat{\psi}$ should be clarified.

-Proposition 1, (iv): What does it mean that g* satisfies Assumption 1? Assumption 1 is an Assumption on $f^* \in \mathcal{L}^2(P_X)$, or does the statement in (iv) refer to (1)? The proof of statement (v) is done in the proof of statement (iv); I think those parts can be moved to the proof of statement (v).

-In (1), how are A and A' drawn from $p(\cdot |x)$? A motivation for (1) would be helpful.

-Can Assumption 1 be verified; is it a restrictive assumption? Furthermore, can $\epsilon$ or violation of Assumption 1 be inferred during the learning process?

-Definition 3: Is $G^{-1}$ well-defined, even if $d = \infty$?

-Remark after Lemma 2: What is $\|\cdot\|_n$?

-How is $d$ chosen? Equation (20) would motivate to choose $d$ such that there is a large gap between $\lambda_d$ and $\lambda_{d+1}$, but your result improves such a guess for $d$ compared to HaoChen21 and Saunshi22. It would be helpful to elaborate on this.

-Is $\bar{\phi}$ an eigenfunction of $\Gamma^*\bar{\Gamma}$? If so, how restrictive is the condition $\hat{\phi} = \bar{\phi}$; is this just the choice of the encoder?

-Does Lemma 9 need a condition on boundedness of the matrix $QDQ^T$ or absolute convergence of the sum $\sum\limits_{i = 1}^\infty \lambda_i q_i^T q_i$?

### Questions
General remarks

-The assumptions and notations should be pointed out more clearly. For instance

       -it seems it is assumed, but I did not see it stated explicitly, that $P_\mathcal{A}$ has a density, and that $p(a|x)$ and $p(x|a)$ exist.

       -What is A in E(g(A)|x). Similarly, X is not defined as a random variable (it is clear from the context but should be defined).
      
       -The notational difference between $p$ and $p(\cdot,\cdot)$ is small.

-Is $\hat{\psi}$ always assumed to be of the form (10) or is (10) just an example?

-Can you explain the choice of the distribution $P_{AX}$ a bit more? Particularly, it could be emphasized how the conditional distribution $P(\cdot |x)$ has to be given. You can refer to the given examples.

-Can your approach be used to build or suggest an augmentation-based pretraining? Maybe under assumptions on prior information on the distribution $P_X$?

-Proposition 1, (iv): What does it mean that g* satisfies Assumption 1? Assumption 1 is an Assumption on $f^* \in \mathcal{L}^2(P_X)$, or does the statement in (iv) refer to (1)? The proof of statement (v) is done in the proof of statement (iv); I think those parts can be moved to the proof of statement (v).

-In (1), how are A and A' drawn from $p(\cdot |x)$? A motivation for (1) would be helpful. The space $\mathcal{F}_B(\Gamma;\epsilon)$ is a central object, it would be good to motivate it more.

-Can Assumption 1 be verified; is it a restrictive assumption?

-Can $\epsilon$ or violation of Assumption 1 be inferred during the learning process?

-Definition 3: Is $G^{-1}$ well-defined, even if $d = \infty$?

-Remark after Lemma 2: What is $\|\cdot\|_n$?

-How is $d$ chosen? Equation (20) would motivate to choose $d$ such that there is a large gap between $\lambda_d$ and $\lambda_{d+1}$, but your result improves such a guess for $d$ compared to HaoChen21 and Saunshi22.

-Is $\bar{\phi}$ an eigenfunction of $\Gamma^*\bar{\Gamma}$? If so, how restrictive is the condition $\hat{\phi} = \bar{\phi}$; is this just the choice of the encoder?

-It is good to see a separation of model and augmentation in the error analysis. Do you think a combination, for instance, through augmentation based on the model, can be fruitful, too?

-Does Lemma 9 need a condition on boundedness of the matrix $QDQ^T$ or absolute convergence of the sum $\sum\limits_{i = 1}^\infty \lambda_i q_i^T q_i$?


Minor comments:

-Did you compute the ``sweet spot" mentioned in the introduction? Can it be computed?

-In Section 2.1 some reference for conditional expectation and RKHS could be added.

-Proof of Proposition 1: The proof should also contain showing that $\mathcal{H}_\Gamma$ is complete.

-Are $K_X$ and $K_A$ square integrable? It seems so from (4) and necessary from the proof of the statement that $\Gamma^*\Gamma$ and $\Gamma\Gamma^*$ are integral operators. Are conditions on P_AX$ needed that (4) holds?

-Below Definition 2: I don't think that convexity of $D_{\chi^2}$ is needed because the bound $S_\lambda\leq \kappa^2$ follows from (11), via $\kappa^2 \geq K_X(x,x) = S_\lambda$.

-First sentence of Section 3: Assumption 1 could be mentioned to recall the bound for $\|f^*\|$ in $H_{\Gamma}$.

-Lemma 5: Below Lemma 5, it is mentioned that the required 4th order bound holds. Why is the condition for such a bound included in the statement of the lemma?

-Around Definition 2 you can refer to Examples 1,2,3 for examples of the augmentation complexity.

-Are there exponential lower bounds on $\kappa$ in Examples 2,3?

Typo: Page 4: "the the", the word ``the" was used two times

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper builds upon recent work on self-supervised representation learning to study the effect of augmentation on the generalization properties. The key insights are that 1) augmentation can be seen as introducing a natural kernel $K_X$ between the inputs, kernel which has to be estimated based on the unlabeled data, 2) the labeled data serves then to find a linear predictor, whose generalization performance is bounded by the authors, with a bound that crucially depends on some quantities related to the augmentation procedure. The main point for the proof is an assumption, called 'isometry' (w.r.t. the augmentation) by the authors, on the optimal solution. Numerical experiments on estimating these quantities are then performed.

### Strengths
I appreciated the goal of the paper and that it improves on the presentation of some of its competitors. The discussions and remarks were enlightening and I chuckled when reaching the Appendix (A, B) to see the anticipation of some of my questions or critiques. The article clearly involved some work and the literature review appears quite adequate. The presence of the experiments nicely complements the theoretical part, justifying in particular the interest of introducing $\kappa$ in the analysis.

### Weaknesses
The key proof element is Assumption 1. I wished Section 2.1 was written differently so as to improve its clarity, emphasizing the assumptions that really matter based on my understanding, that is 1) $\Gamma \Gamma^*$ is Hilbert-Schmidt 2) eq. (8) + $f^* \in R(\Gamma^*)$ rather than the more obscure (1) or Ass.1. The writing of Proposition 1 can be definitely improved.

I think the comparison with the source condition of Cabannes et al. could be more developped since the authors' assumption ($f^* \in R(\Gamma^*)$) looks quite similar. I looked for the formula corresponding to (1) in HaoChen et al. but could not find it. Also the final predictor of Definition 1 used a bound constraint on the norm, I am not sure whether it is common in some literature since I am used rather to regularized versions. These formulations require better justification I would say. I also have doubts with the comparison with the RIP.

About Cabannes: no, a source assumption is meant to say the problem of recovering $f^*$ is well-posed since the optimal solution belongs (or close) to the range of the kernel integral operator. Thus assuming $f^* \in R(\Gamma^*)$ is precisely the same idea, and that has nothing to do with how the kernel is selected. You "pre-select" it by choosing your augmentation method and you assume that your problem has a chance of being solvable.

About RIP: I disagree, RIP as underlined by another reviewer has to hold for every vector and characterizes a property of a matrix. Your assumption bears on a single vector $f^*$ and says that you hope that the augmentation procedure does not lose much of the "variance".

Most of your assumptions correspond to putting yourself in a setup where you can solve the problem. There is no harm in that but you should be open about it.

Unbounded kernels: Reviewer tXrm asked you the same question and you answered that "we assumed they were integrable". It is not because it is a classical tool to have bounded kernels that it means your setting allows for them. You have chosen not to work with a pre-defined kernel (e.g. Gaussian), so live with it, and prove that there are indeed cases where $K_A$ and $K_X$ are square integrable. I had suggested some choices of augmentation (Dirac and Gaussian) which should give (counter) examples, please test out those or others, but I would not be satisfied just with an answer saying that you make this strong assumption on a clearly large class of kernels because of proof conveniencies.

Is $u_i$ small: take $f^*=u_i \psi_i$ for $i$ chosen such that $\lambda_i < 1-\epsilon$, do you get that $u_i=0$ based on (8)? I think that (8) prevents $f^*$ to be encoded mainly with the indices corresponding to the smaller $\lambda_i$, so that most of its variance is in the first eigenvalues. In your example if I take $\alpha$ large, you are precisely showing that the associated coefficient $u_2$ is quite small.

### Questions
- Which formula corresponding to (1) can be found in HaoChen et al.?
- Can you quote some articles that used a bound constraint on the final predictor as you do? In general imposing constraints simplifies proofs, is this reason of your choice?
- Can you give examples of augmentations that do not lead to $\int K_X(x,x) dp(x) <\infty$? $p(a|x)=\delta_x$ for instance? Similarly, give some examples where $\Gamma \Gamma^*$ is clearly Hilbert-Schmidt (Gaussian blur I guess)? I ask this because it is not a given that $K_X(x,x)\in\mathbb{R}$ in my opinion. There are kernel integral operators that are not related to RKHSs.
- Is it true that (8) implies that $u_i \approx 0$ for $\lambda_i < 1-\epsilon$? It seems to me to be the case. Eq.(8) can then be interpreted as requiring that $f^*$ is mostly encoded only on the first eigenvalues of $\Gamma \Gamma^*$, in other words that it is 'simple/low dimensional', and that has little to do with RIP I would say. Please discuss further this aspect, and if possible suggest a reformulation of Sec 2.1.

I would upgrade my score if these questions and those of the other reviewers are answered.

The authors could underline that Cabanes et al. also restrict themselves to the quadratic loss despite the contrastive inspiration coming from classification, and use the arguments in Cabanes et al. to justify it through calibration.

Minor:
- p2 please add some context words, 'upstream/unlabeled', 'downstream/labeled' to simplify the reading for non-experts.
- p3 last line $\phi$ not $\phi(a)$ which are values
- p4 'the the'
- Quoting Forrest Gump, ``my mama always said'' never to start a sentence with a mathematical expression.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors consider augmentation-based representation learning, where a feature map is learned from an unlabelled dataset augmented using some mechanism. 
The paper provides a learning theory for this setup using a regression problem, where the regressor is linear in the learned features. 

The authors consider an augmentation mechanism defined by a conditional distribution $p(a|x)$, which modifies a data point $x$ to an augmented sample $a$ stochastically. 
Given this mechanism, the regression function is defined by the conditional expectation $\mathbb{E}[g(A)|x]$ of some function $g$. 
For this, the authors show that the problem may be described by an RKHS, and using this framework, they investigate the role of the feature map and augmentation.

### Strengths
The theoretical framework introduced in the paper is interesting and original. 
The authors introduce an RKHS structure to the representation learning problem. Specifically, the target function $\mathbb{E}_A[g(A)|x]$ may be considered as an element of an RKHS whose kernel is given by the augmentation-induced joint distribution . 
The framework thus enables us to quantitively analyse the performance of a downstream regressor using a kernel machinery, as well as establishes a criterion of good representation (approximation to the basis of the RKHS).

### Weaknesses
### Clarity 
A major issue is the lack of clarify. The paper is currently dense, not accessible to a general audience (as someone who is not well-versed in the area, I find the paper really challenging to read), and thus requires a major revision. Because of this, I have to admit that I have not fully understood the contribution of the paper. Specific comments are summarised below. 
 
### Significance 
There are some elements that make the evaluation of significance difficult: 
* It is not clear how reasonable the assumption on the target function is. It seems that the assumption is conveniently introduced so that we can analyse the problem using a particular RKHS. Is there any motivating example for using $\mathbb{E}_A[g^*(A)|x]$ as a target? It should be more straightforward to work with (functions on ) the augmentation space $\mathcal{A}$ rather than $\mathcal{X}$, as in Johnson et al., 2023.  
* The encoder has to be of the form (10), as otherwise $\hat{\Psi}$ are not included in the RKHS. Therefore, the claim that the encoder $\hat{\Psi}$ can be arbitrary is not accurate to me. 
* The soft-invariance assumption is not straightforward to interpret. How does it measure "invariance"? Since $\mathbb{E}[g(A)|x]$ and $g(a)$ are functions on different sets, the invariance is not well-defined.
* The dimensionality dependency on the upper bound seems to be very pessimistic, as the authors admitted. I 

Comments: 
* The problem is not well presented. It would have been more helpful if the authors had provided a high-level problem description and define symbols accordingly (e.g., as in the introduction of Johnson et al., 2023). For example, how representation learning is performed is not really mentioned using symbols in the paper (e.g., $\hat{\Phi}$ is not mentioned up to page 4). 
* Some symbols are loosely defined or mentioned before formally defined; e.g., $\hat{\mathcal{H}}_d$ is mentioned before the formal definition of \hat{H}_{\Gamma}. 
* Presentation of technical results could be improved. For instance, Proof Sketch of Theorem 1 only decomposes Theorem 1 into two parts, repeating what is mentioned in the remark, and thus could be omitted. 
* For Proposition 1, the authors might want to check Chapter 11 of "An Introduction to the Theory of Reproducing Kernel Hilbert Spaces" by Paulsen and Raghupathi.  
* Using the same symbol for different density functions is confusing ($p(a)$ and $p(x)$). 
* Section 5. The term "strong" augmentation is obscure. One may consider an augmentation distribution that is independent of $x$, in which case the augmentation complexity is 1. Is the dependency between $A$ and $X$ considered a measure of "strong"?

### Questions
* (9) requires a suitable regularisation that depends on $B$ and $\varepsilon$. In some sense, the analysis addresses a well-specified case. What happens if this is violated? 
* (12): Why is $G^{-1/2}$ required?
* "As shown in Wang et al. (2022b), there is...": Is this an existence statement?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper gives a theoretical analysis of how the distribution of augmentations affects the accuracy of contrastive learning methods, building on previous work that has studied this problem through the lens of RKHS regression, and focusing on nonparametric encoder-complexity-independent bounds. The authors first discuss the augmentation operator and show that it induces a pair of dual operators with corresponding eigenfunction decompositions. They then introduce the concepts of *augmentation complexity* (based on the infinity norm of a kernel defined by the augmentations) and the *ratio trace* (which roughly characterizes "how much" of the eigenspaces of the corresponding RKHS are captured by a given encoder).

The authors then prove a number of results based on these quantities. First, they show that the error of a downstream predictor can be decomposed into an approximation-error term (how closely the function can be recovered from the learned encoder's representation) and a downstream-estimation-error term (how well the linear readout actually recovers this function). Second, they consider approximating the top-d eigenspace of the RKHS using only a finite pretraining dataset, and show that this can be used to bound the approximation error term.

Finally, the authors consider how their "augmentation complexity" measurement translates to real augmentations, focusing on masking transformations. They give theoretical values for it for the hypercube examples discussed in Cabannes et al. (2023), and also show how to estimate it for masked language modeling on the `wikipedia-simple` dataset.

### Strengths
**[S1]** The paper is overall clearly written and easy to follow, and the authors do a good job introducing the problem and explaining their analysis. I found the "proof sketches" for the main results to be very useful as well.

**[S2]** The formalism of the dual operators and the isometry property are quite elegant. The authors build on previous work but present the previously-studied concepts in an insightful way, and clearly lay out the underlying structure produced by the augmentation distribution.

**[S3]** The main results in sections 3 and 4 go further than previous work in characterizing how much information the augmentations alone can provide about the function of interest. In particular, Theorem 1 shows how the error of a function decomposes into approximation and estimation error, and furthermore identifies how the approximation error component depends on the "trace gap"; Theorem 2 then shows that finding the empirical top eigenspace can lead to small approximation error even if $\lambda_{d+1}$ and $\lambda_d$ are close.

**[S4]** The analysis of the augmentation complexity of real augmentations is quite interesting, both for the theoretical values for particular masking strategies and for the empirical estimation of the augmentation complexity of real augmentations used for masked language modeling.

### Weaknesses
 **[W1]** This work focuses on analyzing the effect of the augmentations alone, without considering the impact of inductive biases. I understand that this was an intentional choice, and I do think that this makes the analysis of augmentations more "pure". However, such an approach means that the theoretical results here may not have much explanatory power for real augmentations. The paper's claim that they "disentangle the effects of the model and the augmentation" is misleading, as the analysis primarily focuses on the augmentation distribution, with the model's role being limited to achieving a good ratio trace. It's not clear how this analysis could be extended to models with more structured inductive biases. While the authors claim their analysis refutes the idea that model-independent guarantees are vacuous, this is not necessarily true, as their bounds may still be vacuous for realistic augmentation distributions.

**[W2]** The analysis starts from a strong assumption that the target function $f^*$ lies in a particular RKHS and satisfies a particular soft invariance condition. However, it's difficult to tell what this assumption actually means, or whether it would be true in practice. In particular, the RKHS membership seems quite strict, and adding even an arbitrarily small perturbation to $f^*$ might cause the assumption to no longer hold. While the authors note that such assumptions are common in learning theory, the practical implications of this assumption for real-world functions remain unclear. The assumption that $f^*$ can be represented as an expectation of some function $g$ on augmentations is also quite strong and lacks clear justification.

**[W3]** The empirical results about real augmentations suggest that the true augmentation complexity of real-world datasets is *massive* (on the order of $\kappa \approx 10^{100}$). As such, it seems likely that the bounds in Theorem 1 and Theorem 2 would be effectively vacuous for real-world data. This is a significant limitation, as it suggests that the theoretical analysis may not be practically relevant for many real-world scenarios. The paper does not adequately address the implications of this high augmentation complexity for the practical applicability of its bounds.

### Questions
**On inductive biases.** In the appendix, you state "the nonparametric analysis established in this work clearly refutes the claim in Saunshi et al. (2022) that learning guarantees independent of the model inductive bias are necessarily vacuous". I don't think this is true. As I understand it, Saunshi et al. show that when augmentations are approximately disjoint, the eigenspectrum of $\Gamma\Gamma^*$ decays extremely slowly, with many of the eigenvalues of $\Gamma\Gamma^*$ being close to 1 (or, under their notation, many eigenvalues of the normalized Laplacian $L_\circ = I - A_\circ$ being close to 0). This means that the approximation error of the top-d eigenspace is necessarily very large. I think this same analysis also applies to your results; Saunshi et al.'s approximately-disjoint augmentations would imply $\lambda_{d+1} \approx 1$ and so your $\tau \approx 1$, leading to a blowup in the first term of your equation 14.

If I'm correct, I think this deserves more discussion, and I don't think you can say that you've refuted the claims of Saunshi et al. I also think the paper could be improved by giving more context about the relationship of your results to those of Saunshi et al. For instance, is there any relationship between your augmentation complexity and Saunshi et al.'s approximately-disjoint augmentations? One might expect that approximately-disjoint augmentations would imply a high augmentation complexity; if so, that could be useful to discuss.

Also, what do you mean by "disentangle the effects of the model and the augmentation"? It's not clear to me how the presented results disentangle these effects, although I do think they give a clear explanation of the role of the augmentations in particular.


**Interpreting the soft invariance criterion.** Can you give any intuition about what satisfying Assumption 1 actually means in practice? It seems unlikely to me that functions of practical interest could be *exactly* represented as expectations of some function $g$ on augmentations, and I also don't see any way to verify whether or not Assumption 1 holds.

**Part (iv) of Proposition 1.** Proposition 1 part (iv) states that $g^*$ satisfies Assumption 1. This doesn't make sense to me; Assumption 1 is a statement about $f^*$, not $g^*$. Do you mean to say that $g^*$ satisfies Equation (1)?

The proof of part (iv) also seems potentially incorrect. In particular I'm not sure how $\langle g^*, (I - \Gamma \Gamma^*) g^* \rangle_{P_A} \le \epsilon ||g^*||^2_{P_A}$ implies $\langle g_0, (I - \Gamma \Gamma^*) g_0 \rangle_{P_A} + ||g_1||^2_{P_A}  \le \epsilon (||g_0||^2_{P_A} + ||g_1||^2_{P_A})$; shouldn't $||g_1||^2_{P_A}$ be $\langle g_1, (I - \Gamma \Gamma^*) g_1 \rangle_{P_A}$ instead? It also seems like your proof here implies that $R(\Gamma^*) \subseteq \mathcal{F}_B(\Gamma; \epsilon)$ for all $\epsilon$. But that doesn't seem like it could be true; perhaps I'm misunderstanding something.

**Asymptotic behavior of Theorem 2.** In Theorem 2, don't the quantities $\overline{\lambda}_d^{-1}$ and $\gamma_G$ potentially depend on $N$? It seems like that could affect the asymptotic behavior of the bound in equation (20). Can you say anything about the convergence or boundedness of these quantities?

**Relationship of this analysis to that of Johnson et al. (2023).** I noticed that parts of your analysis resemble some of the statements of Johnson et al. (2023) at a high level; in particular, your soft invariance assumption is similar to their "approximate view invariance" assumption, and the decomposition in Theorem 1 is somewhat similar to their bound in Proposition 4.2. The details are different (their analysis focuses on approximating functions $\mathcal{A} \to \mathbb{R}$ rather than $\mathcal{X} \to \mathbb{R}$ and doesn't include the approximation error of the encoder) but it might still be worth including a brief discussion of the similarities.

**Other suggestions / comments.**
- Section 2 states "Similar to RIP, this property clarifies the the role of augmentation: The augmentation defines a set of features (eigenfunctions) ordered by their a priori relevance to the target function." This wasn't clear to me; how does the isometry property relate the relevance of the eigenfunctions to the target function?
- The definition of $||f||\_n^2$ in section 3 doesn't seem to be used anywhere in the main paper.
- It took me a while to locate the definition of $\hat{f}$ when reading Theorem 1; perhaps you could add a reference back to equation (9) where it is defined.
- Section 4 discusses the empirical eigenspace $\hat{\mathcal{H}}\_d$ before actually defining what it is, which was a bit disorienting; it might make sense to define it at the start of section 4 instead of at the end of page 6.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
