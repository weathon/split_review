# Towards Scalable Topological Regularizers

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 5

## Abstract
Latent space matching, which consists of matching distributions of features in latent space, is a crucial component for tasks such as adversarial attacks and defenses, domain adaptation, and generative modelling.
    Metrics for probability measures, such as Wasserstein and maximum mean discrepancy, are commonly used to quantify the differences between such distributions.
    However, these are often costly to compute, or do not appropriately take the geometric and topological features of the distributions into consideration.
    Persistent homology is a tool from topological data analysis which quantifies the multi-scale topological structure of point clouds, and has recently been used as a topological regularizer in learning tasks.
    However, computation costs preclude larger scale computations, and discontinuities in the gradient lead to unstable training behavior such as in adversarial tasks. 
    We propose the use of principal persistence measures, based on computing the persistent homology of a large number of small subsamples, as a topological regularizer.
    We provide a parallelized GPU implementation of this regularizer, and prove that gradients are continuous for smooth densities.
    Furthermore, we demonstrate the efficacy of this regularizer on shape matching, image generation, and semi-supervised learning tasks, opening the door towards a scalable regularizer for topological features.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a regularizer to be used in Generative Adversarial Networks (GANs) in addition to the “standard” distance between distributions (e.g. Wasserstein distance). The regularizer consists in computing the probability of persistent homology diagrams through Principal Persistent Measures (PPM) on both real and generated data and comparing them through MMD. The paper provides a few theorems proving the smoothness of the MMD applied to compare PPM under mild conditions and experimentally shows the benefits of this regularizer on both generative metrics and semi-supervised classification tasks.

### Strengths
The paper pairs the proposed regularizer with a solid theoretical analysis of the smoothness of the resulting loss function, which justifies its use as an additional term to the (W)GAN loss.

Experimental results show that the proposed regularizer provides a significant advantage in training GANs, especially for self-supervised tasks. 

Although the paper is theoretically dense, it can still be followed by non-experts in the PH fields. Nevertheless, it would be helpful to remark the purpose of each theorem, or sequence of theorems, before introducing them.

### Weaknesses
The main weakness of the paper is the introduction and motivation of the problem and the relation of the proposed method to the current literature. From the introduction (and also the title), it isn’t really clear what problem the paper is going to tackle. While the introduction talks about general regularizers for latent space representations, most of the methodological development and the experimental section tackle specifically the problem of regularizing GANs. I would be clearer about this from the beginning of the paper or show applications beyond GANs (beyond the shape-matching toy example).

I would also better frame the work in the context of GANs, and regularization strategies for GANs. A few methods are mentioned in the literature, but none is discussed in depth. For instance, PHom-GeM seems to share objectives and strategies similar to those of the proposed work. It would be ideal to compare also with some of these methods.

Also, it is not clear what theorems are novel, and which ones are just reported or adapted from results in the existing literature. Maybe they are all novel, but specifying the current state of the literature and which gaps need to be filled (from a theoretical point of view) would help to better understand the contribution.

### Questions
I would like the authors to clarify the points I have highlighted on the weaknesses, especially the contribution and the relation with other GAN regularizers.

Moreover, the method proposes the use of MMD rather than WD to compare the PPMs. Is there any theoretical and/or practical reason? Would still be possible to use WD and experimentally compare the performance of WD and MMD?

Minor comments:
- The citation format is weird and interferes with the reading.
- At row 66, what would be the classic PH pipeline?
- In row 155, you provide 5 introductory references to PH, these are far too many, and this does not really help the reader.
- Row 383: “consider provide”
- Table 1: since you computed averages over 10 runs, it would make sense to report also the standard deviation.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes to introduce a topological regularization term to the objective function used in the context of GAN. 

As standard topological descriptors (known as persistence diagrams) are typically too expensive to compute, they propose to rely on the (recently introduced) notion of "principal persistence measure". Losely speaking, the principal persistence measure is a distribution in the space of persistence diagrams, but its elements have (at most) one point, and can thus be (roughly speaking) identified with distribution on the open half-plane $\{b < d,\ (b,d) \in R^2\}$ augmented with an additionnal virtual point $\star$. 

The work then introduce a notion of MMD distance between PPM. The MMD has several benefits: it is fairly easy to compute and induce smooth gradients. 

The authors showcase their method in a series of experiments.

### Strengths
- Good introduction / preliminaries (section 1 and 2). 
- The work mixes results from different ideas (mix of MMD, persistence measures, etc.), and may be useful beyond the scope covered by this paper (improving GAN training). It showcases the use of PPM which are interesting objects in their own, introduce novel possibly useful metric between these topological descriptors, etc. 
- interesting experiments, mixing pedagogical Proof-of-Concept and more advanced experiments. 
- Nice animation in the supplementary material!

### Weaknesses
1. While well written, the introduction and section 2 somewhat fail to motivate the need to account for the geometry/topology when comparing distributions in the latent space. This is just given as a fact (line 142-143), but basically, why should one care about such information? Is there some situations in which this clearly lacks in GAN models? I understand that this needs is empirically confirmed in the experiment sections, but is there a good _a priori_ reason? Specifically, the paper does not adequately explain why standard distribution matching techniques are insufficient, and why incorporating topological information is necessary. It would be beneficial to discuss scenarios where ignoring the underlying topological structure of the data leads to poor performance in GANs, such as mode collapse or the generation of unrealistic samples. A more thorough discussion of the limitations of current methods would strengthen the motivation for the proposed approach.

2. Somewhat in the same vein: Wasserstein-like distances between topological descriptors are discarded because "gradients are not smooth", but is it a real problem in practice? I would expect stochasting GD to not actually bother which such details. The argument against Wasserstein distance (WD) based on gradient smoothness seems weak, especially considering the stochastic nature of GAN training. While the authors mention that WD gradients may be less smooth, they do not provide a concrete example or empirical evidence showing that this is a significant issue in practice. It would be useful to see a comparison of the performance of the proposed method with a similar approach using WD, to justify the choice of MMD. In particular, it is not clear that the non-smoothness of WD gradients would be a significant issue in the context of stochastic gradient descent, which is known to be robust to noisy gradients.

3. One may argue that GAN tend to be outdated in comparison to more modern generative models (DDPM, etc.). I nonetheless believe that this does not significantly impede the contributions of the work, whose interest is not limited to GAN only.

### Questions
See question 1. and 2. in the Weaknesses section. 

Additionnally : 
- I did not have time to read the appendix in details so I may be wrong, but regarding the Remark 1: in theory, PDs may have infinite total mass (here in the work, everything simplify as one consider PDs with at most 1 point), in which case $n,m, N = +\infty$. And even if one restrict to finite diagrams, without putting a uniform bound on their cardinalitty, one may still have $n,m \to \infty$ and (I guess) peculiar behavior of the metric. Does the remark implicitely consider a space of diagrams with uniformly bounded mass/number of points? From a quick glance, $M_{lin}$ only incorporate a standard integrability constraint but nothing about the cardinality of the diagrams. 

- The animations show that optimization let few "leftovers", can you comment on this? Is it due to a mix of (gaussian-kernel based) MMD which indeed tends to let leftovers behind + the subsampling in the PPM which needs to be "lucky" to put some gradient on this points? Would using the Energy-distance MMD $k(x,y) = - |x-y|$ improve on this particular aspect? (note: gradient may no longer be smooth using this MMD)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
One of the prohibitive factors of Topological Data Analysis are computational
constraints imposed on the calculation of Persistent Homology (PH). While
highly optimized CPU-GPU algorithms exist, the computation already become 
unfeasible for small point clouds in low dimensional settings. A remedy is
proposed through the use of a GPU implementation of the Principal Persistence
Measure (PPM) (Gómez & Mémoli 2024). This addresses both difficulties related
to smoothing as well as scalability. Given the scalable backbone the authors
then provide a theoretical framework to turn the PPM into a regularizer that
can be used in generative tasks where the topology of the dataset is of
importance. They provide a strong theoretical foundation for their regularizer
and show that the gradients are continuous.

The authors provide two experiments as empirical evidence of the efficacy of
their method. First is an optimization task where a point cloud is
backpropagated to match a reference shape. Faster convergence to the final
solution is shown, thereby showing topological regularization to be helpful in
convergence. In a final suite of experiments the authors show that the
regularization significantly increases the generative quality of the trained
models and this is demonstrated in both unsupervised and semi-supervised
learning tasks. The computational advantages are shown to have a significant
increase in training time over the traditional PH calculation and not suffer from the
exponential cost.

### Strengths
In general it is great to see a push towards scalable topological methods and
this entails the core strengths of the paper, as it an impactful and relevant
problem to work on. Often in TDA, the focal point lies in theoretical
justification of the methods with only limited emperical evidence, mostly on
small datasets. Lack of scalability of PH being the main driver of this
phenomenon and therefore this paper is of importance in building the bridge in
applying TDA in large scale applications.

The theoretical justification is both thorough and sound and adopts a novel
view on using PH in machine learning applications with the empirical evidence
showing good improvements when using the regularization term.

### Weaknesses
Where the theoretical contributions have good exposition, the implementation
details are less thoroughly addressed. As one of the two cornerstones of the
contributions, it would be nice to see where the authors differ in their
implementation from previous work that allowed them to compute the PH on the
GPU. The details seem to be lacking in the paper and together with the release
of the code, would strengthen the paper considerably.

For the experimental section the optimization of point clouds is not
particularly convincing. In the figure the results could be improved by showing
how the final output has converged and in two dimensions, which would be
natural as other metrics are not provided. Especially since the method (I
assume) optimizes only a subset of the whole point cloud at a time I would like
the doubt of only a subset of the point cloud converging to the reference point
cloud to be taken away. Second, only the loss of the training set over the
iterations is shown. An independent set distance to quantify the results would
strengthen the results. The Wasserstein distance between the point clouds or
the Chamfer Distance would be great examples. Finally, an argument why the
non-zero convergence is correct would also be in place, since none of the loss
functions converge to zero.

The experimental section also heavily relies on the Cramer loss, and although
the paper presenting it was rejected at ICLR 2018, although the paper is
well-cited. The reviewer is not an expert on training GAN's and evaluating
them, hence it would be nice to provide an argument as to why this is the main
loss metric to use and also the main model to use and compare to.

If the reviewer would have to show to the reader that a certain regularization
term is effective, a good strategy would be to take a variety of datasets and a
variety of models (perhaps with certain properties) and show that the
regularization consistently improves the scores across the board. As the paper
is currently presented, the scope of the experiments is rather limited.
Moreover, there is also comparable work on topological regularizers for
classification problems which would also provide a nice comparison partner. A
last potential point of improvement is the connection with other topological
methods and regularization terms.
The application of persistent homology is not new and a comparison with previous work,
both in terms of computational performance and increase in accuracy would also be
very nice.

Although the reviewer commends the line of work the authors have decided to
pursue, a considerable amount of work would have to be done to create a logical
and convincing experimental suite. Multiple reference architectures of GAN's
would have to be implemented with more standard metrics. Perhaps other tasks
would also benefit from this regularization term, such as classification and
regression tasks. The non-standard set up for the point cloud optimization
experiment would also have to be convincingly revised. Once these elements are
addressed, the work has great potential impact on the Topological Data Analysis
community and machine learning in general.

### Questions
- A question that would also be interesting to consider is how the method
    scales with dimension, based on the paper it looks like it might scale
    exponentially in the dimension. 
- What causes loss not to converge to zero in the point cloud optimization
    task? 

Remark:
During the review, some typo's were found. Please give the paper another read
and correct them.

### Soundness
3

### Presentation
3

### Contribution
3
