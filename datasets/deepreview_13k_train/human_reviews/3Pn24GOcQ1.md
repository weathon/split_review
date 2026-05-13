# Geometry of the Loss Landscape in Invariant Deep Linear Neural Networks

- Decision: Reject
- Scores: 6, 6, 6, 5, 6

## Abstract
Equivariant and invariant machine learning models seek to take advantage of symmetries and other structures present in the data to reduce the sample complexity of learning. Empirical work has suggested that data-driven methods, such as regularization and data augmentation, may achieve a comparable performance as genuinely invariant models, but theoretical results are still limited. In this work, we conduct a theoretical comparison of three different approaches to achieve invariance: data augmentation, regularization, and hard-wiring. We focus on mean squared error regression with deep linear networks, which parametrize rank-bounded linear maps and can be hard-wired to be invariant to specific group actions. We show that the optimization problems resulting from hard-wiring and data augmentation have the same critical points, all of which are saddles except for the global optimum. In contrast, regularization leads to a larger number of critical points, again all of which are saddles except for the global optimum. The regularization path is continuous and converges to the hard-wired optimum.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies the three related problems of learning the linear predictor under squared loss. The problem is not simple since the output dimension is $>1$ and it has been known since the seminal work of Baldi & Hornik that there are small-rank optimal matrices that generate saddles in the original problem. The paper studies similar problems in the data augmentation and regularization cases and shows the same loss landscape characteristics.


------------------------------------------------------------------------

After the author's response, I increased my score to 5. I may increase again during the discussion phase between the reviewers.


------------------------------------------------------------------------

After the author's second response, I increased my score to 6.

### Strengths
Comparing learning with data augmentation vs an invariant architecture is an interesting problem and linear networks may be a good place to start for a theoretical study. The paper is written rather well but the global structure of the paper (presentation order) is confusing (see Weaknesses).

### Weaknesses
It is not clear how much technical novelty there is in the paper. Proposition 2 is copied from Zhang and Theorem 4 is copied from Trager. Theorem 4 seems rather trivial, how is this novel compared to Baldi and Hornik?

The landscape complexity questions are interesting for complex losses where the full set of critical points is not known. In this paper, all local minima are global which is a stronger result on the loss landscape (and yes, possible for linear networks). Interestingly, the global minima are equivalent between problems in the infinite data limit, but what happens for finite data? Is there a separation between the problems? Like using invariance is better than using data augmentation? That kind of result would make the paper much more interesting. I might have missed such a point in the paper due to quick reading and confusing organization of the paper.
I think it'd be better to state the three problems early in the paper similar to 

Levin, Eitan, Joe Kileel, and Nicolas Boumal. "The effect of smooth parametrizations on nonconvex optimization landscapes." Mathematical Programming (2024): 1-49.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores the loss landscape geometry of invariant deep linear neural networks, focusing on three approaches for enforcing invariance: data augmentation, regularization, and hard-wiring. The paper provides a theoretical comparison, demonstrating that the global optima for all three methods are equivalent in the limit of strong regularization and full data augmentation. It also examines the critical points of the loss landscapes, showing that data augmentation and hard-wiring result in identical sets of critical points, while regularization introduces additional ones. Empirical experiments show that training with data augmentation converges to a critical point that parametrizes an invariant function, data augmentation is computationally more expensive than hard-wiring, and regularization falls in between.

### Strengths
- The paper provides a mathematically rigorous analysis of the loss landscapes for the three approaches and is a good contribution to the study of loss landscapes.
- By establishing that data augmentation and hard-wiring result in identical critical points, the paper offers a unifying perspective on invariance in optimization. This connection complements recent study on comparing equivariant architectures and data augmentation.
- The empirical results align well with the theoretical findings, providing concrete evidence that training with data augmentation converges to a critical point that parametrizes an invariant function.

### Weaknesses
The settings considered in the paper seem limited. In particular:
- As the authors also acknowledge, this paper focuses on deep linear networks. The results depend heavily on properties almost unique to this type of networks, such as that the network’s function space is a vector space of linear maps. There does not seem to a clear path that could extend the results here to other, especially nonlinear, architectures. Specifically, the analysis relies on the ability to decompose the weight matrices and analyze the loss landscape through the lens of linear algebra, which is not directly applicable to non-linear networks with activation functions. The paper does not address how the non-convexity introduced by activation functions would affect the conclusions about the equivalence of global optima or the critical points.
- The main results are limited to cyclic and finitely generated groups, which does not apply to continuous groups in common datasets, such as rotation and scaling. This is a significant limitation because many real-world invariance problems involve continuous transformations. The analysis of cyclic groups relies on the discrete nature of the group action, and it is not clear how the results would generalize to Lie groups, where the group action is continuous and requires different mathematical tools for analysis.

### Questions
- I was not able to follow Section 4.3 and would appreciate any clarification on the main conclusion from the experiment or which theorem the experiment seeks to support.
- Nordenfors et al. (2024) points out that the set of stationary points are identical for data-augmentation and hard-wiring, on both linear and certain nonlinear architectures. Could the authors comment on whether these results are more general than Theorem 3? 
- Can the results in this paper provide useful insights for practitioners? I do not believe a lack of immediate practical implication is a major weakness, but the paper might reach more audience by including some motivation for studying the loss landscape or invariant deep linear networks.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the loss landscape of three approaches to achieve invariance: data augmentation, network hard-wiring, and regularization. The authors solve the optimization problems arising from each method and find that the first two approaches share the same critical points, whereas regularization leads to a larger number of critical points. Additionally, experiments show that data augmentation indeed results in invariance of the trained network, and that both data augmentation and hard-wiring converge to the same global optimum.

### Strengths
- The authors theoretically solve the optimization problems arising from three different approaches in a bounded-rank linear model and discuss their solutions. This analysis offers fresh insights for the learning-with-symmetry community on the use and comparison of methods to achieve invariance.
- They not only characterize the global optima of these approaches but also identify all the critical points, demonstrating that regularization leads to a greater number of critical points, which is an interesting result.
- The authors verify their theoretical findings through experiments on the rotated MNIST dataset, showing that while both hard-wiring and data augmentation converge to the same global optimum, data augmentation demands higher computational costs.
- The paper is well-written.

### Weaknesses
 - As noted on line 169, the theoretical scope of this paper is limited to finite and cyclic groups. However, in many real-world applications, the relevant groups are not finite or cyclic, such as permutation group [1], rotation group [2], and sign and basis transformation group [3]. This limitation reduces the practical applicability of the paper’s findings. Specifically, the analysis does not directly extend to continuous groups like $SO(3)$ which is crucial for 3D object recognition, or the permutation group $S_n$ which is fundamental in set-based learning. The lack of a clear path to generalize the results to these common groups significantly restricts the impact of the theoretical analysis.
- Some assumptions in the paper lack adequate justification. For instance, in Remark 2, the authors use $Y=WX+E$ to suggest that the rank assumption of $\overline{Z}^\mathrm{inv}$ is mild. However, the noise matrix in this example seems unrealistic, as real datasets typically have structured rather than random correlations between data and labels. The assumption that the noise $E$ is i.i.d. is a strong simplification and does not reflect the complex dependencies often found in real-world data. Furthermore, in Corollary 1, the authors assume that the singular values of three matrices are pairwise distinct, but this assumption is not justified. This assumption is critical for the analysis of critical points, and without empirical validation, it is unclear if the theoretical results hold in practice. Verifying whether these assumptions hold in real datasets would improve the paper’s applicability.
- Some key citations are missing. In Proposition 1, the authors characterize invariant linear maps under a cyclic group. However, [1] previously characterized all invariant and equivariant linear maps for symmetric groups, and [4] extended this work to identify all polynomials equivariant under symmetric groups. The absence of these key references undermines the novelty of the theoretical contribution, as similar results have been established in the context of symmetric groups and equivariant polynomials.

### Questions
In Figure 3(a), why doesn’t the non-invariant component of $W$ converge to zero? Additionally, in Figure 4(a), why does the non-invariant component of $W$ increase for data augmentation?

### Soundness
3

### Presentation
3

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
This paper explores how different methods for enforcing invariance in neural networks—such as hard-wiring, regularization, and data augmentation—affect the loss landscape and optimization process. Focusing on deep linear networks, the authors compare these approaches in terms of their critical points and global optima. They show that for rank-constrained linear maps, both hard-wiring and data augmentation yield the same critical points, most of which are saddle points except for the global optimum. Regularization, while producing more critical points, eventually converges to the same global optima. The study provides theoretical insights into how these methods influence learning processes in machine learning models and helps explain their performance in reducing sample complexity. The authors also present experimental results to demonstrate convergence behavior in practical settings.

### Strengths
* The paper provides a deep theoretical comparison of different approaches to enforce invariance (data augmentation, regularization, and hard-wiring). By proving the equivalence of global optima across these methods and analyzing critical points in function space, the authors offer valuable insights into the optimization landscapes of invariant models.

* The paper specifically addresses the impact of invariance in deep linear networks, which is a significant area in machine learning. By narrowing down the study to a structured problem, it successfully derives concrete results that are applicable to broader, more complex architectures.

* The combination of theoretical results with empirical validation is a strong aspect of this paper. The authors provide experimental evidence supporting their theoretical conclusions, such as the similarity in performance and convergence rates of data augmentation and hard-wired models. This connection strengthens the practical relevance of the theoretical findings.

### Weaknesses
 * The paper focuses exclusively on deep linear networks, which are a simplified model of neural networks. While this approach allows for clear theoretical insights, the results may not fully generalize to more complex architectures, such as non-linear or deep convolutional networks that are commonly used in real-world applications. Specifically, the analysis of critical points and convergence behavior is highly dependent on the linearity assumption, and it is unclear how these findings would translate to the non-convex loss landscapes encountered in non-linear networks. The paper does not adequately address the challenges posed by non-linearities, such as the presence of spurious local minima and saddle points that are not present in the linear case.

* The study centers on particular group-invariant structures, which might not cover a wide range of practical invariance cases. Invariance to more complex transformations, such as non-linear or higher-dimensional transformations, may require different analyses, limiting the applicability of the results to a broader set of machine learning problems. The paper's focus on linear transformations within the context of deep linear networks restricts its scope, as many real-world invariances involve non-linear operations (e.g., perspective transformations in images) or complex combinations of transformations. The theoretical framework presented may not be directly applicable to these more general cases, and the paper does not provide sufficient discussion on how to extend the analysis to more complex invariance structures.

### Questions
* The paper focuses on deep linear networks for tractability, but how do you anticipate the results extending to non-linear neural networks, which are more prevalent in practical applications? Have you considered the potential challenges or modifications needed for such generalization?

* How do you expect the optimization landscape and critical points to change when considering more complex or non-standard invariance structures? Could your theoretical framework be adapted to handle these?

* Given the computational efficiency noted in your experiments, how scalable are the findings, particularly regarding the comparison between data augmentation and hard-wiring, when applied to much larger models or datasets, such as in convolutional or transformer networks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates how different methods of implementing invariance - by having it hard wired, imbued in the data, or encouraged using regularisation - affect optimisation. They study the simple case of deep linear networks, rank-constraining them to make the optimisation non-convex. In this case the three different settings share the same optimum in the regulariser’s limit and have the same critical points, with the regularisation having more than the hard-wiring/data-augmentation cases.

### Strengths
**Novelty:**

This work studies an important, timely question - the relation between hard-wiring and learning symmetries. Although not explicitly stated, this would have implications for network design and generally when should one hardwire a symmetry vs just imbue it in the data and whether if there is a hidden symmetry will it be learnt.

**Scientific quality:**

The setting nicely relates between the three different cases, albeit naturally in the limited linear case given here. 

**Clarity:**

The paper is well written and neatly organised. It has a good, logical flow, giving examples and generally trying to expand on theorems where possible. Section 2 is especially well, concisely presented given the large background.

### Weaknesses
 **Novelty:**

As there are many works trying to answer this question it’s currently unclear what this one adds that others don’t. It’s known that networks can learn to respect symmetries, with empirical results being given eg. in [5-6]. [2] looked at using data augmentations vs feature averaging, which is not the same but similar to the data augmentation vs hardwiring cases here. These are select examples but still, the contrast to existing works isn’t as clear as it would ideally be.

**Scientific quality:**

It’s unclear how the rank-constrained setting is related to real cases. In practice networks are universal - linear networks are often assumed for tractability but is limiting the expressivity realistic, and if so then how? Is it assumed solely to make the loss landscape nonconvex and if so, why not get that through a myriad of other ways? Recommend clarifying this.

There’s a special focus on cyclic and finite groups, without a clear explanation/motivation why. Do these encompass many of the common groups in geometric deep learning? What do they fail to describe?

Lines 397-399 - recommend showing how some weights tending to the same value results from the theorems. 

**Clarity:**

This paper suffers from the page limit as many similar theoretical deep learning papers do. This stops the authors from sufficiently expanding on the different results and giving more intuition for their theorems. Still, currently there’s an insufficient emphasis on the “why” relative to the “what”. For example, the abstract details the problem, the setting, and the results, but not what they mean, hence not explicitly answering the problem. This problem is evident on many levels in the main body as well. This is evident also in the contributions section (1.1). Other than that high level, theorems are given with little intuition as to why they hold or what they mean. The paper has a decent information density as it is so it’s naturally difficult to accommodate everything, but it can not only leave the reader confused but more importantly make it harder to understand how the results tie together and get at the underlying problem. Another example is the related work section - it’s unclear what important context these works give relating to this study, and if they don’t then why they are mentioned at all.

Throughout the paper numbers/axis titles on plots should be bigger.

Lines 47-49 - The stated problem is different than the impression one gets from the abstract - the latter implies “can symmetries be learnt and how does their optimisation look” whereas the former says something else. Recommend rephrasing either or both.

Line 53 - what does benevolent mean here? Recommend replacing.

Line 71-72 - unclear what’s meant here by linear invariant neural networks given the different settings.

Lines 197 - shouldn’t det-variety be defined? It’s not a well known term, and if it’s not important enough to be defined it should be delegated to the appendix or not used.

Line 211 - what’s r in this context?


### Questions
**Scientific quality:**

Lines 74-76 - how is this intuitive/obvious? It’s important to give that intuition. To play devil’s advocate, if it’s obvious then it’s even moreso important to clarify why this is studied and what new insight was achieved if any.

Lines 234-236 - isn’t it possible to formulate this for any group with a countable number of generators?

Lines 243-245 - do all roots work equally well? Assuming this corresponds to several classes of solutions no?

Lines 267-269, remark 2 - this is a good example but it’s unclear how typical this is, although it makes some intuitive sense that it would be. Making that clearer could be nice, are there more grounded reasons to believe some analogy of this generally holds? Seems related to the manifold hypothesis - you’re assuming there’s some latent structures and small deviations from it. Also although the rank can technically be large it might have many small singular values, no?

Line 395-396 - why change Adam’s betas?

Figure 1 - it’s quite interesting how results are similar for CE even though the theorems don’t hold for it, is this discussed anywhere?

For the hard-wiring experiments why not use a different B with a different size? Eg. to make all cases have a similar number of parameters, although their expressivity is clearly the same.

Lines 486-496 - this is a nice decomposition but I believe I saw it in other works, are you aware of it appearing elsewhere in the literature?

Line 496-497 - why is the double descent interesting? Do you mean the orange line in figure 3.a?

**Clarity:**

Line 41 - “have shown” how? Feels like a citation’s needed.

Lines 47-49 - where in the paper are the solutions studied/referred to? Eg. when are the regularised solutions invariant? This is implicitly shown but not discussed. 

Lines 123-124 - deteriorates how so? This is interesting and seems relevant here, consider slightly expanding.

Lines 145-146 - why is the tangent space relevant here? I didn’t understand where it was heavily used throughout the paper.

Lines 162-170 - missing caption?

Lines 169-170 - is finite and cyclic defined anywhere?

Lines 285-293 - the connection to manifold regularisation is interesting but it’s unclear what it adds - what’s lost if it’s removed? What does it say in this context?

Lines 295,296 - isn’t \bar{Z(\lambda)}^{reg} defined twice? Is it just different forms of the same expression? Generally this theorem’s intuitive meaning/interpretation is unclear.

Lines 303-305, thm 2 - why wouldn’t it be continuous, due to the rank constraint? Generally solutions to L2 regularisations are continuous so recommend making this clearer.

Lines 333-336 - this is quite interesting, it would be nice to discuss this - why it happens, potential implications, etc.

Many of the previous kinds of comments about intuition/interpretation and what vs why hold for section 3.4 as well.

Lines 373-377 - does spurious here mean suboptimal? Recommend clarifying.

**Minor points, suggestions, etc.:**

In the first paragraph what about classical examples eg. graphs/images?

There are some papers that weren’t mentioned which could be relevant throughout the paper, eg. [1-3, 7]. [2] specifically has some potential overlap and I recommend clarifying what’s different than their work. [7] might have overlap with section 4.3, specifically the weight decomposition.

Recommend merging section 1.1 with 1.

[4] and generally Saxe/Ganguli’s works are relevant both in spirit and regarding results, at least as some of the first to study deep linear networks in modern deep learning.

Lines 270-274 basically say that you’re taking projections and as everything is linear it’s fine, which is nice but can be spelled out more explicitly.

Section 3.3 - can anything meaningful be said about the case where the symmetry is only “on average” embedded in the data, so only partial group orbits are included?

Some small experiments with regular nonlinear networks showing whether these results hold and if so then to what extent would be instructive.

[1] Gerken, Jan E., and Pan Kessel. "Emergent Equivariance in Deep Ensembles." arXiv preprint arXiv:2403.03103 (2024).

[2] Lyle, Clare, et al. "On the benefits of invariance in neural networks." arXiv preprint arXiv:2005.00178 (2020).

[3] Fuchs, Fabian Bernd. Learning invariant representations in neural networks. Diss. University of Oxford, 2021.

[4] Saxe, Andrew M., James L. McClelland, and Surya Ganguli. "Exact solutions to the nonlinear dynamics of learning in deep linear neural networks." arXiv preprint arXiv:1312.6120 (2013).

[5] Olah, C., Cammarata, N., Voss, C., Schubert, L., and Goh, G. Naturally occurring equivariance in neural networks. Distill, 2020. doi: 10.23915/distill.00024.004. https://distill.pub/2020/circuits/equivariance.

[6] Gruver, Nate et al. (2023). “The Lie Derivative for Measuring Learned Equivariance”.
In: The Eleventh International Conference on Learning Representations. url: https:
//openreview.net/forum?id=JL7Va5Vy15J.

[7] Gideoni, Yonatan. "Implicitly Learned Invariance and Equivariance in Linear Regression."

**Decision:**
As it is I recommend rejecting this paper mostly on the grounds of clarity, but that’s assuming that it presents a deeper novelty than what it currently seems to. It’s unclear if it has meaningful implications for real networks but it might still be insightful to consider this toy case, although this remains to be seen.

---

**Update post-discussions:**

Following a thorough discussion with the authors and them addressing the main comments regarding clarity I am raising my score to 6 and recommend accepting this paper. This is a high quality work where the authors investigate three different settings of a relevant problem that is generally considered open in the geometric deep learning community. The paper's main downside is that of many theoretical deep learning works where theoretical insights are insufficiently tied back to more realistic settings, although the revised manuscript minimises this gap as much as possible without additional experiments. This is a shame as even simple MNIST-esque experiments would go a long way. Still, I believe this paper will be of interest to the community, especially if future work builds upon it.

### Soundness
3

### Presentation
2

### Contribution
2
