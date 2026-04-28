# Group Downsampling with Equivariant Anti-aliasing

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 5, 6

## Abstract
Downsampling layers are crucial building blocks in CNN architectures, which help to increase the receptive field for learning high-level features and reduce the amount of memory/computation in the model. In this work, we study the generalization of the uniform downsampling layer for group equivariant architectures, e.g., $G$-CNNs. That is, we aim to downsample signals (feature maps) on general finite groups *with* anti-aliasing. This involves the following: **(a)** Given a finite group and a downsampling rate, we present an algorithm to form a suitable choice of subgroup.  **(b)** Given a group and a subgroup, we study the notion of bandlimited-ness and propose how to perform anti-aliasing. Notably, our method generalizes the notion of downsampling based on classical sampling theory. When the signal is on a cyclic group, i.e., periodic, our method recovers the standard downsampling of an ideal low-pass filter followed by a subsampling operation. Finally, we conducted experiments on image classification tasks demonstrating that the proposed downsampling operation improves accuracy, better preserves equivariance, and reduces model size when incorporated into $G$-equivariant networks

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a framework for the subsampling of data in group equivariant architecture. The framework explains how to make sure the downsampling operations are anti-aliased, leading to an improved performance. Their approach shows how to choose a sub-sampled group to make sure that the map stays equivariant and how to make sure that data is not aliased.

### Strengths
The paper uses signal processing and group mathematical formulation to formulate how to properly downsample in group equivariance architectures. I appreciate the level of delicacy in discussing the network should be designed to "properly" process data to make sure that information is not corrupted by aliasing in each sub-sampling layer. The paper is written clearly and is well-organized.

### Weaknesses
While the method is thorough, the authors are losing an opportunity to demonstrate the implications and significance of anti-aliasing in an experiment. Given that accuracy and results are only shown on benchmark datasets such as MNIST and CIFAR, whether this approach would benefit large-scale experiments is unknown. Here are suggestions and clarifying comments for improvements:

The paper lacks information on how their work differs from the prior works listed in related works. For example, how is the literature currently performing such a task? Is the literature completely missing such a subsampling framework for equivariance networks, hence the absence of comparison baselines? Is the key message of the paper that prior works don't do anti-aliasing? Or they do sub-sampling differently, which results in a non-equivariant map.

The experiments can be more thorough. They are limited in its current stage.

- Can the author focus on an application where the impact and benefits of anti-aliasing is better shown? Perhaps for an application where high-frequency information is of importance. An analysis on the artifacts and impacts of those due to naive sub-sampling can also help.
Results on MNIST in its current form are limited.


Minor

- I suggest not using bold phrases (such as line 44) in the paper.

- In Example 1, the middle label should be (b).

- I suggest not coloring the Lemma, Claim, etc., and following ICLR formatting instructions.

### Questions
- Is this the "first" work on looking into the subgroup sampling theorem of groups? Xu et al. 2021 discuss group equivariant subsampling. How this work differs from this prior work? Are there other works in the literature that address the discussed issue? If yes, please include these in the intro.

- It would be nice to show with a toy example why subsampling in groups is not an intuitive task of "every other sample" and what can go wrong. In this version of the paper, this intuition is not well-discussed.

- Prior to this paper how the literature is doing sub-sampling on groups? Could Table 1 include such a comparison where other approaches fail?

### Soundness
4

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
This paper proposes a method to subsample signals over groups by a given factor $R$. The authors, motivated, by signal processing, also provide an anti-aliasing operation to ensure bandlimited-ness and also provide a sampling theorem for groups.

### Strengths
The paper has strong connections to signal processing and the approach seems natural from the perspective of signal processing. Concepts are explained well and overall the paper is fairly well-written.

### Weaknesses
The paper has a few weaknesses, mainly:

- unclear motivation,
- unexplained choices.

**Motivation**

There are two crucial choices that are made for the paper, but they are never discussed or motivated. Specifically:

- Signals are defined over groups. This is highly non-standard in the equivariance literature, and it’s not clear how the methods presented here fit into the existing space of equivariant works. This is greatly illustrated in Section 5.1 and Figure 3, where the groups $C_{16}$ and $D_{16}$ are used essentially to label the nodes and have no effect on the actual signal. For rotationally-equivariant architectures, we fully expect the feature maps themselves to exhibit equivariance, which is not the case in this work. If that is not possible using this framework, this severely limits the applicability. The authors do not explain why signals are defined over groups rather than the more typical approach of defining them over the underlying space and then lifting to the group, which would more naturally lead to equivariant feature maps. The lack of motivation for this choice makes it difficult to assess the novelty and relevance of the proposed approach.
- Interpolation in (8) is defined on a subsampled signal. This is highly canonical in signal processing, where interpolation can be applied independently of downsampling. It seems this is necessary for the authors’ analysis, however this is not motivated or explained at all. The authors should clarify why they chose to perform interpolation only on the subsampled signal and not on the original signal, as is common in standard signal processing pipelines. This choice seems to be a critical component of their theoretical analysis, but the lack of justification makes it difficult to understand the practical implications and limitations of this approach.


### Questions
On top of the above weaknesses I had some further questions:

- On line 57 the authors claim that the subsampling layer selects suitable subgroups for the tasks. There are a couple of issues with this: first of all, how is “suitable” defined in this context? In what way do the authors support that claim and how is it evaluated in their experiments? Finally, and maybe most importantly, the statement mentions tasks: however, their subsampling algorithm is task-agnostic and performs the subgroup choice without any knowledge about the downstream task. In what way, then, is the subgroup that is selected suitable for the task?
- The definition of the minimal generating set in 125 is weird. The way things stand, since by construction $e\notin S$, it can never hold that $\langle S \rangle = G$, for any $S$.
- There are multiple typos in the footnote in line 323. There is also a typo in 343 (no space between $\mathcal{M}$ and the previous word), and also on 501 $\textrm{Acc}_{\textrm{orbit}}$ appears twice.

### Soundness
3

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
2

### Summary
This paper presents a method in the context of group equivariant neural networks, to design a subsampling operator where we can derive the subsampled group (called subgroup) and a corresponding anti-aliasing method.

### Strengths
- I really like that some examples are provided.
- I think it's great to clearly illustrate what claims are tested and under which conditions in experiments.
- Results show the interest of the proposed method in the given context.
- Code is provided to allow the replication of the experiments. (I did not try running them)

### Weaknesses
My assessment is based on the lack of clarity of the paper. There small bits and pieces that are confusing but more generally concreteness and link to the application is lacking.

- Clarity: As someone not familiar with group equivariant neural networks, it was very difficult for me to imagine what it means to have a signal indexed by elements of a group. I think section 4 would benefit from having a very visual example beforehand that can explain what all of the objects mentioned are in a concrete setting. Specifically, the paper needs to clarify how a signal is lifted to the group domain, and how the group action transforms the signal. It's unclear how the filter $\psi$ is defined, and how it is transformed by the group elements. Furthermore, the paper should provide concrete examples of the groups $D_N$ and $C_N$ in the context of image processing, and explain how the group elements act on the image signal.
- Experiments: it's not clear what exactly "We apply the proposed subgroup selection and anti-aliasing operator to equivariant CNN architectures" means. I don't understand what is implemented in the code unless I read it, if I stick to the paper. Specifically, it is unclear how the anti-aliasing filter is applied within the G-equivariant CNN architecture. Given that the input to the CNN is of shape `[batch_size, n_channels, n_group, height, width]`, it's not clear how the group convolution is performed, and how the anti-aliasing filter is incorporated into this process. The paper needs to clarify the specific computations performed on this input tensor, and how the proposed method modifies these operations.
- Nit: when introducing the order of a generator, maybe it's worth specifying that it always exists and point to a reference.
- Nit: "the minimal generating subset" -> it's not clarified beforehand whether there exists only one.
- Nit (notations): 
. $V$ is at one point a vector space, then vertices on a graph. This is confusing. 
. The downsampling rate is sometimes $r$ sometimes $R$.

### Questions
- In practice, is it always easy to obtain the minimal generating subset for a certain concrete group G? Or maybe another to phrase the question is: given a generating subset for a group, how easy is it to determine whether it is minimal?
- In example 1, is $S = \{\delta t\}$ ? and then we simply pick $s_d = \Delta t$? 
- What does "reconstructed perfectly" mean in Claim 2?

### Soundness
3

### Presentation
2

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
This paper proposes a method for achieving equivariant (finite) group downsampling with anti-aliasing. The main contributions are twofold:
1. Given a downsampling rate, the authors introduce an algorithm to identify an appropriate subgroup within the given finite group.
2. The authors generalize the concept of a low-pass filter to signals over the group, enabling anti-aliasing and perfect reconstruction after downsampling.

Experiments demonstrate that:
1. The anti-aliasing low-pass filter achieves perfect reconstruction post-downsampling.
2. Performance on image classification improves with rotated MNIST and CIFAR-10

### Strengths
1. The paper is well-written, well-organized, and relatively easy to follow.
2. The concept of automatically determining a subgroup for downsampling the original group signal, given a specific downsampling rate, is intriguing.
3. The approach of identifying a smooth and equivariant low-pass filter (Eq. 15) before performing group downsampling is also interesting.

### Weaknesses
1. A main weakness (as pointed out by the authors themselves) are the limited experiments. The results reported are no where close to the readily-available benchmark on rotated MNIST [1]. Specifically, the reported accuracies on rotated MNIST are significantly lower than those achieved by existing methods, raising concerns about the practical applicability of the proposed approach. The lack of experiments on more complex datasets further limits the generalizability of the findings.
2. The authors argued that, in the MNIST experiment, the proposed equivariant-downsampling achieves comparable results with significantly smaller model size. However, one can argue that the original group C24 and D24 are too "large" and probably unnecessary to begin with. It would be interesting to see the comparison to a G-CNN without any subgroup downsampling and start with the smallest group used in the last layer of the proposed method. This comparison is crucial to understand if the performance gain is due to the proposed downsampling or simply due to the reduced model size, and whether the initial choice of a large group is actually beneficial.
3. Also, the advantage of algrithm 1 (automatically determine a subgroup based on the subsampling rate) on Cn and Dn is not clear. While the algorithm is presented as a key contribution, its practical benefits, especially when dealing with cyclic and dihedral groups, are not well-demonstrated. I would be much interested to see its effectiveness when dealing with larger groups (such as permutation S(n)). The current experiments do not justify the complexity of the proposed algorithm.
4. Although I am no expert on the subject, but I would be surprised that perfect reconstruction for group signals after subsampling on a subgroup has not been considered in the literature. Can the authors cite more results on this subject and compare their result to the available ones? The absence of such comparisons makes it difficult to assess the novelty and significance of the proposed method.

### Questions
1. After subgroup downsampling, the model will only be equivariant to the subgroup. What is the rationale of imposing an equivariant constraint in Eq. 15 on the original larger group?

### Soundness
3

### Presentation
3

### Contribution
2
