# Discrete Bregman Divergence

- Decision: Accept
- Scores: 8, 8, 5, 6, 8

## Abstract
The Bregman divergence, which is generated from a convex function, is commonly used as a pseudo-distance for comparing vectors or functions in continuous spaces. In contrast, defining an analog of the Bregman divergence for discrete spaces is nontrivial. Iyer & Bilmes (2012b) considered Bregman divergences on discrete domains using submodular functions as generating functions, the discrete analogs of convex functions. In this paper, we further generalize this framework to cases where the generating function is neither submodular nor supermodular, thus increasing the flexibility and representational capacity of the resulting divergence, which we term the difference-of-submodular Bregman divergence. Additionally, we introduce a learnable form of this divergence using permutation-invariant neural networks (NNs) and demonstrate through experiments that it effectively captures key structural properties in discrete data. As a result, the proposed method significantly improves the performance of existing methods on tasks such as clustering and set retrieval problems. This work addresses the challenge of defining meaningful divergences in discrete settings and provides a new tool for tasks requiring structure-preserving distance measures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
Review of "DISCRETE BREGMAN DIVERGENCE" submitted to ICLR 2025.

This paper extends the submodular Bregman divergence methods introduced a few years ago to non-submodular functions. They do this via the notion of a DS (difference of submodular) decomposition of non-submodular functions. The key thing is that in order for the identifiability property of the Bregman divergence to hold (i.e., that D(x,y) = 0 iff x==y), they note that the submodular function needs to be strict (i.e., lie on the interior of the submodular cone), something they point out was not mentioned in the past (although arguably it was implicit). They note that any set function has a DS decomposition in terms of two strict submodular (or two strict supermodular) functions and since submodular functions have both sub-gradients and super-gradients, it is possible to use the two DS components of any set function to define a sub-gradient and a super-gradient based Bregman divergence, and therefore define a Bregman divergence for any set function.

They go on to show that these functions can be learnt, i.e., one can learn two submodular functions and then find the semi-gradients of these to produce a discrete Bregman divergence based on these learnt submodular functions. They show results on some set clustering that seem to me to be reasonable.

While I do not think that the paper is revolutionary, and I do think that the strictness of previous DS decompositions was implicit, I do think it is worth pointing that out more explicitly as this paper (and also the Li & Du, 2020) in fact do, so I agree with this. There are a few issues of tone, however, that I would change in the paper and that I point out below. Also there are a few recent citations that I think you should add. All in all, however, I think the paper should be accepted as it is a nice contribution, and it is in particular good to see the empirical work using their submodular-supermodular Bregman divergence methods.

Here are some comments.

Firstly, I think you might consider changing the title of the paper a Submodular-Supermodular Bregman Divergence, or "Discrete DS Bregman Divergence" since the approach is entirely dependent on there being a DS decomposition. If one only has oracle access to a non-submodular non-supermodular set functions, it can be hard to find a reasonable decomposition (assuming one knows bounds of the function, one can always add and subtract a very large strict submodular function to any set function to transform it to a DS function but that is a fairly vacuous DS decomposition). So unless you really can produce a Bregman Divergence for any set function given only oracle access, I think it is more appropriate to entitle your paper "Submodular-Supermodular Bregman Divergence".

I think you may want to change the tone of lines 213-216 where you say "a formal discussion on the well-definedness is lacked" as that sounds a bit disparaging. You are basing your results strongly on their methods, standing on their shoulders, so you might say something along the lines of "This earlier work, however, did not explicitly mention that in order for the identifiability property of the Bregman divergence to always hold, it is necessary for the submodular functions involved to be strict", i.e., be more explicit in what you are building on rather than saying that the previous paper "is lacked".

I think the numerical experiments are good and, as mentioned above, it is good to see empirical work as well on submodularity, I think there should be more such things.

The submodular functions that you are learning however seem to be either deep submodular functions (DSFs), i.e., see (Bilmes & Bai from 2017, https://arxiv.org/abs/1701.08939) or much more recently deep submodular peripteral networks (DSPNs, https://arxiv.org/abs/2403.08199 from 2024). I think both papers should be cited. In particular, it seems your submodular functions are simple forms of DSPNs, but I think that one could learn two DSPNs and construct one of your Bregman divergences from semi-gradients of DSPNs quite easily, and this would both further extend the expressivity of your Bregman divergences and also extend the utility of these DSPNs. Also DSPNs strictly extend DSFs (removing the only known limitation of DSFs), and this is also useful for discrete Bregman divergences.

### Strengths
see above.

### Weaknesses
see above.

### Questions
see above.

### Soundness
4

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
2

### Summary
The submission proposes new class of divergences on discrete spaces and a learning framework comprised of permutation-invariant neural networks with metric learning loss.

Leveraging difference-of-submodular (DS) decomposition for any set function f, the authors obtain more expressive class of Bregman divergences dubbed discrete Bregman divergences (DBD). Expressiveness advantage over submodular Bregman divergences is achieved by extending the underlying set function class to not necessarily be submodular but rather admit DS decomposition.

The paper validates the proposed approach to learning DBD in a set of numerical experiments.

### Strengths
The paper addresses a problem of extending Bregman divergences to discrete spaces. This is an important problem as many methods that rely on Bregman divergences in continuous settings may be adapted to discrete scenarios.

The submission does a good job providing a structured and clear background on the treated problem.

The central idea of the paper stems from DS decomposition. Typically, one needs a submodular function $f$ to instantiate submoduler Bregman divergence. However, the authors notice that DS decomposition proposed in prior work alleviates this constraint on $f$ itself, and propose to use the difference of two submodular functions, $f = f^1 - f^2$. I'm not an expert in the area, but it seems the idea of using DS decomposition in forming more expressive class of Bregman divergences on discrete spaces has not been explored in the literature and is novel.

The authors provide empirical validation for the proposed learning framework. Given two submodular $f^1, f^2 $ functions, DS decomposition facilitates discrete Bregman divergence specification and with proper implementation of $f^1, f^2$ one can utilize metric learning approach to learn divergence from data. This defines a natural combination of permutation-invariant neural networks (to work with sets) and triplet loss (to learn the divergence). With MNIST experiment, they illustrate that the learned divergence provides reasonable results for dissimilarity between sets of images, with similar image sets getting smaller dissimilarity scores. Point cloud dataset experiments validate that the use of novel divergence class provides benefits over the use of submodular Bregman divergences in set clustering experiment. They further validate that the divergence learned provides semantically close set retrieval.

### Weaknesses
At the very start, the paper highlights the problem of identifiability of divergence, which comes from divergence definition $D(x, y) = 0 \rightarrow x=y$. Thus, later the submission puts a lot of attention on the strict submodularity of the underlying set functions in Bregman divergences as one needs strict inequalities to satisfy the definition requirement. However, the proposed implementation seems problematic to me in this sense. Indeed, the submodularity is guaranteed, but DBD requires strict DS decomposition, so $f^i$s should be strictly submodular, which doesn't seem the case for the adopted architecture:
$$
f_{PN}([x_i]_{i \in X}) = \max_{i \in X} ReLU(h(x_i)),
$$
where $h: \mathcal{X} \rightarrow \mathbb{R}$ instantiated with an MLP with last activation set to ReLU. When argmax is achieved outside the intersection, the inequality from Definition 2.3 holds, but if argmax is inside the intersection, we fail to meet strict modularity. So the proposed implementation doesn't match the requirements of DBD. Perhaps I'm missing something here?

Since the proposed approach targets practical side of things, it seems it needs more extensive experimentation. For example, one would expect to see expressiveness comparison that is not limited to only one task (set clustering) and one dataset (ModelNet40). This will help gain more empirical evidence for the substantial gain in expressiveness across tasks and task complexities, and justify the use of DBD which requires more computational resources (two functions instead of one).

The authors didn't discuss the limitations of their approach, which partly stems from limited experimentation.

### Questions
Formally, the proposed implementation is not divergence as per the Definition 1.1. But rather the generalized divergence? What are the consequences of that in practice? In what scenarios the difference may play a crucial role?

As noted in the weaknesses section, the expressiveness of the new DBD is fully explored empirically. Can we quantify how much more expressive the new class of divergences is compared to the submodular Bregman divergences? I think this is important to show the strength of the new DBD and should be explored empirically.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, the authors generalize discrete Bregman divergences (DBDs) introduced in Iyer and Bilmes (2012a) to the case where the generating functions are not restricted to be submodulars. By leveraging the fact that any set function can be decomposed as the difference of two submodular ones, the authors show that any set function induces a DBD, and that this extension enables to define larger classes of DBDs. Additionally, they propose a framework to learn such divergences from observations by leveraging existing permutation invariant architectures, such as PointNet, that are by construction submodulars. While obtaining the decomposition of a set function as a difference of two submodular ones take exponential complexity, the authors propose to directly model generalized DBDs using the difference of two parametrized submodular functions obtained from PointNets. Then, they propose to learn an adapted DBD from labeled observations using the triplet loss, and show experimentally the application of their approach for clustering and retrieval tasks on two real-world datasets.

### Strengths
The paper is well-written and presented in a clear, accessible manner. The authors thoroughly acknowledge the relevant literature and prior work, thereby enhancing the clarity of their contributions. To the best of my knowledge, the proposed generalization of DBDs is novel, as is the framework introduced for learning them.

### Weaknesses
The main weaknesses of the paper are twofold: (1) a lack of motivation, and, relatedly, (2) a lack of empirical evidence to demonstrate the benefits of the proposed approach. Regarding the first point, while the paper introduces a new mathematical tool—the (generalized) DBD—the motivation for its introduction is not sufficiently developed. Although the authors demonstrate that their extension allows the definition of larger classes of DBDs, the motivations for considering DBDs in the first place for ML tasks are not clearly articulated. This should be clarified in the introduction and related work. Concerning the second point, the authors aim to demonstrate the applications of this tool for clustering and retrieval tasks; however, the experimental results might be insufficient to demonstrate how the proposed generalization improves upon standard DBDs using only submodular generating functions, as only one experiment is provided to demonstrate this point. Furthermore, it remains unclear how DBDs compare to other baseline methods capable of addressing similar tasks as no comparative analysis has been carried out. To enhance the impact of their work, I suggest that the authors strengthen the motivation, and compare the proposed approach with SoTA baselines on the tasks considered.

### Questions
How does the proposed approach compare with other baselines for clustering and retrieval tasks?
Can the authors provide more experimental evidence on the advantage of considering their generalized DBD rather than using the standard one with submodular generating functions?

### Soundness
2

### Presentation
3

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
Bregman divergence is a pseudo-distance for comparing vectors or functions. In this paper, the authors present a new technique to construct such divergence on a discrete domain. Specifically:

1. The authors prove that a strictly submodular function can induce a Bregman divergence (Theorem 3.1).
2. They extend this property, showing that when the function has the form $f + m$, where $m$ is a modular function and $f$ is neither submodular nor supermodular, it can also induce a Bregman divergence (Theorem 3.1').
3. Finally, they demonstrate that the broader the function class, the broader the class of induced divergences (Theorem 3.4).
4. They provide a numerical form of the proposed discrete Bregman divergence (Section 4).
5. Numerical experiments show that the learnable discrete Bregman divergences can capture structure and outperform existing methods in downstream tasks.

### Strengths
1. The authors extend previous work on constructing Bregman divergence by relaxing the requirement that the generator function $f$ must be submodular.  
2. They present a numerical form of the proposed discrete Bregman divergence using permutation-invariant neural networks.  
3. In the experiment section, the authors demonstrate that the constructed Bregman divergence returns smaller values for similar set pairs and larger values for dissimilar set pairs.

### Weaknesses
1. In Section 5.2, *Real Data Application*, it appears that there are no baselines for either the clustering or shape retrieval experiments. Figure 2 demonstrates the performance of the proposed Bregman divergence, but it is difficult to see how this new divergence improves upon previous divergences, such as those presented in [Iyer and Bilmes (2012a)].

Additionally, quantitative metrics (e.g., accuracy in the shape retrieval/classification experiment) and wall-clock comparisons to assess the performance of the proposed divergence should be included and discussed.

2. The differences between the new divergence construction technique and previous work [Iyer and Bilmes (2012a)] remain unclear. For instance, in Equation (7), based on Iyer’s work, $f$ should be submodular, and $h_Y$ serves as its subgradient, which is straightforward to construct. 

In the new divergence construction technique proposed here (presumably based on Theorem 3.1'), $f$ can be any set function, which raises the challenge of finding the appropriate modular mapping $h_Y$. In short, the old technique imposes a requirement on $f$, making $h_Y$ straightforward once $f$ is constructed. The new technique has no requirement for $f$ but requires finding an appropriate $h_Y$. Given this, it is not immediately clear why the new technique would outperform the previous one.

### Questions
1. Regarding the notation in Theorem 3.1, it appears that $h_Y$ and $g_Y$ are indeed independent of the set $Y$. Is that correct?

2. In Table 2, could you clarify the values in each column? Specifically, are they the mean and variance of 10 trials of what particular measure?

3. In Theorem 3.1' and the contribution section (lines 069-071), the authors mention proving that $f$ does not need to be submodular. However, in Section 4, lines 306-307, it appears that the implementation still requires submodular functions $f_1$ and $f_2$. What, then, are the advantages and differences of the new divergence construction technique compared to the original one by [Iyer and Bilmes (2012a)], which requires submodularity? It seems that the proposed technique still relies on submodular properties in the implementation stage.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a novel method to construct Bregman divergences for functions defined on discrete sets. Their method is backed by new theory, and it is learnable and applicable to deep-learning on set data.

Their main contributions are:
1. They provide theoretical justification for the technique of [1] to construct Bregman divergences from strictly submodular generator functions. Namely, they prove that the induced divergence is indeed a divergence.
2. They provide a technique to construct Bregman divergences from *arbitrary* generator set-functions, which need not be submodular. They do so using a submodular analogue of the Difference-of-Convex decomposition.
3. They motivate their construction theoretically by proving that a larger class of generator functions makes for a larger class of induced Bergman divergences.
4. They demonstrate the applicability of their method to deep learning via preliminary experiments. In their experiments they use a neural network based on their construction, which computes discrete Bergman divergences that are learnable.
   - They train their architecture to comptue divergences between sets of MNIST digits, and show through examples that the learned metric makes sense.
   - They demonstrate the advantage of their construction compared to simpler ones (based solely on modular set-functions, or on basic set operations) by performing k-Means clustering on PointNet-40, treating the point clouds as sets and using the computed divergences as a distance measure.
   - They further demonstrate their method in the task of set-retrieval on PointNet-40, showing in several examples that the top 5 retrieved examples indeed belong to the correct class.

[1] Faust, Fauzi, Saunderson (2023) - A Bregman Divergence View on the Difference-of-Convex Algorithm

### Strengths
All in all I believe that this paper provides valuable contribution to the community, as it lays the theoretical foundations for using discrete Bregman divergences in practical learning tasks, which is an intriguing approach that is not often discussed in this context.

### Weaknesses
While the experiments are rudimentary, the paper offers sound theoretical results and demonstrates their applicability to practical learning tasks.

My main concern is that the paper lacks in terms of clarity, particularly in the experiment section. See details below. Should my concerns be addressed, I would be willing to raise my score.

### Questions
## Major comments

1. Crucial details regarding your experiments are missing. For example:
   - Line 359: With that loss function, it seems that the global optimum of zero is trivially attainable. What prevents your method from collapsing to zero?
   - What architectures did you use in practice? (dimensions, numbers of layers etc.)
   - Line 307: How did you compute the subgradients and supergradients of the neural networks a priori?
   
   The paper could seriously benefit from an additional appendix describing the technical details of your experiments.
2. Line 458: "In addition, since our DBD quantifies the differences between discrete data, it is naturally invariant to these rotations. Note that the rotational invariance in point cloud data corresponds to the permutation invariance in set data and this property is not provided by usual divergences over vectors."
   This argument and reasoning are unclear. Are you saying that the DBD between two point-clouds X,Y is rotation invariant, namely D(X,Y) = D(RX,RY) for all rotations R? If this is the case, it is highly nontrivial and requires proof. Anyway the argument itself requires clarification.
3. Line 20: "outperforming existing methods on tasks such as clustering" is too strong a statement, as you did not compare with existing methods outside the realm of discrete set functions.
4. The continuous analog of the core idea in this work, namely to construct Bregman divergences from arbitrary nonconvex generator functions using the Difference-of-Convex decomposition, was studied in [1]. Their contribution should be acknowledged.

## Minor comments

1. How come bar-DBD with decomposition performed worse than grow- and shrink-DBD without decomposition? Is there an intuitive explanation? Are there any examples where you observed a stronger benefit to non-modular over modular generator functions? This could provide stronger empirical support for your theoretical contribution.
2. Lines 422-424: For clarity, I suggest stating explicitly that you calculated the Rand index between the resulting clustering and the clustering induced by the ground-truth labels.
3. In l.213-218, I suggest replacing "a formal discussion on the well-definedness is lacked", which sounds vague, with a clear and explicit statement of what you prove that the referred paper did not.

## Possible errata

1. Lines 213-218 and 236: The citation (Iyer & Bilmes 2012a) should probably be (Iyer & Bilmes 2012b).
2. Line 447, the first instance of 'bar' should probably be 'shrink'.
3. Line 701: 'and' in "and for every" should probably be removed.

### Soundness
3

### Presentation
2

### Contribution
3
