# Towards Identifiable Unsupervised Domain Translation: A Diversified Distribution Matching Approach

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
Unsupervised domain translation (UDT) aims to find functions that convert samples from one domain (e.g., sketches) to another domain (e.g., photos) without changing the high-level semantic meaning (also referred to as ``content''). The translation functions are often sought by probability distribution matching of the transformed source domain and target domain. CycleGAN stands as arguably the most representative approach among this line of work. However, it was noticed in the literature that CycleGAN and variants could fail to identify the desired translation functions and produce content-misaligned translations.
This limitation arises due to the presence of multiple translation functions---referred to as ``measure-preserving automorphism" (MPA)---in the solution space of the learning criteria. Despite awareness of such identifiability issues, solutions have remained elusive. This study delves into the core identifiability inquiry and introduces an MPA elimination theory. Our analysis shows that MPA is unlikely to exist, if multiple pairs of diverse cross-domain conditional distributions are matched by the learning function.
Our theory leads to a UDT learner using distribution matching over auxiliary variable-induced subsets of the domains---other than over the entire data domains as in the classical approaches.  The proposed framework is the first to rigorously establish translation identifiability under reasonable UDT settings, to our best knowledge.
Experiments corroborate with our theoretical claims.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims to propose an unsupervised image translation framework that ensures identifiability of underlying generator maps. It achieves the same by relying on auxiliary variables. Promising empirical results showcase the potential of the method on benchmark image datasets.

### Strengths
The writing of the paper is good with detailed exposition of the problem. It also includes detailed notes on related literature. The paper produces promising qualitative and quantitative results based on experiments. It also gives ample ablation and suggestions on the architecture and parameters involved. The brief declaration of limitations is appreciated.

### Weaknesses
The theory under quite strong assumptions tends to be straightforward and does not fully complement what the paper set out to achieve. It revolves around a particular model and due to certain vague notions becomes somewhat vacuous. The empirical results give the paper strength which the theory fails to support. In my opinion, the experiments should be prioritized.

My first concern is regarding the strong assumption that continuous functions $f^*$  and  $g^*$ exist under arbitrary input data on both domains. It is quite challenging to ensure that the optimal transport map between distributions has any regularity (e.g. Lipschitz continuity). Also, in most cases proving so requires the support of the base distribution to have restrictions in terms of convexity. In real data, the same hardly follows. Perhaps sacrificing generality for the sake of accuracy would be better for the theory.

The discussion on the notion of "content" seems vague. Is the content of an image and its rotated counterpart the same? Is there any generalization of it for general group actions?

Is there any way of justifying Assumption 1, even if with examples?

It seems to me that homeomorphic spaces will have the same "content", whereas the assumption claims the converse. Am I right in saying that?

Given there exist non-unique members in the kernel (i.e. multiple solutions bringing about zero loss), is Definition 1 even meaningful in a non-parametric setup, where there is no inherent identifier?

The entire theory revolves around the CycleGAN loss in particular. This does not complement the initial impression of unsupervised domain translation in general. The proposed loss function ($7$) is also a modified CycleGAN setup. Also, what are the "any criterion" in Fact 1?

Does the discriminator play any role in ensuring identifiability? This seems crucial as the resultant translation map would be a result of a stable discriminator.

[Section 3] Can this at all be called unsupervised given that pseudo or weak labels ($u$) are used? Also, what is meant by "sufficiently different" $P_{x|u_i}$ and $P_{x|u_j}$?

Shouldn't the difference between distributions $P_{x|u(A,B)}[A]$ and $P_{x|u(A,B)}[B]$ be based on a divergence measure and not inequality ($\neq$)?

There remain some typographical/grammatical errors in the manuscript (e.g. see the Section Identifiability Characterization).

### Questions
1. My first concern is regarding the strong assumption that continuous functions $f^*$  and  $g^*$ exist under arbitrary input data on both domains. It is quite challenging to ensure that the optimal transport map between distributions has any regularity (e.g. Lipschitz continuity). Also, in most cases proving so requires the support of the base distribution to have restrictions in terms of convexity. In real data, the same hardly follows. Perhaps sacrificing generality for the sake of accuracy would be better for the theory.

2. The discussion on the notion of "content" seems vague. Is the content of an image and its rotated counterpart the same? Is there any generalization of it for general group actions?

Is there any way of justifying Assumption 1, even if with examples? 

It seems to me that homeomorphic spaces will have the same "content", whereas the assumption claims the converse. Am I right in saying that?

3. Given there exist non-unique members in the kernel (i.e. multiple solutions bringing about zero loss), is Definition 1 even meaningful in a non-parametric setup, where there is no inherent identifier?

4. The entire theory revolves around the CycleGAN loss in particular. This does not complement the initial impression of unsupervised domain translation in general. The proposed loss function ($7$) is also a modified CycleGAN setup. Also, what are the "any criterion" in Fact 1?

Does the discriminator play any role in ensuring identifiability? This seems crucial as the resultant translation map would be a result of a stable discriminator.

5. [Section 3] Can this at all be called unsupervised given that pseudo or weak labels ($u$) are used? Also, what is meant by "sufficiently different" $P_{x|u_i}$ and $P_{x|u_j}$?

Shouldn't the difference between distributions $P_{x|u(A,B)}[A]$ and $P_{x|u(A,B)}[B]$ be based on a divergence measure and not inequality ($\neq$)? 

There remain some typographical/grammatical errors in the manuscript (e.g. see the Section Identifiability Characterization).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper seeks to address the issue of content misalignment in unsupervised domain translation. The authors pinpoint the presence of "measure preserving automorphism" (MPA) as the primary culprit and present a theoretically-founded method to neutralize it. Their method was validated on datasets like Edges to Rotated Shoes, yielding high-quality samples that maintained content integrity.

### Strengths
1. It is innovative to introduce auxiliary variables for tackling the MPA issue. I'd like to offer more insights on this approach. Essentially, **supervised domain translation can be seen as a specific instance of their method.** By choosing a specific auxiliary variable, we can tailor each conditional distribution $p(x|u=u_i)$ to hold precisely one sample, $x_i$, with a probability of 1, whereas all other samples in the space have a zero probability. Similarly, we manipulate each conditional distribution $p(y|u=u_i)$ to include only one sample, $y_i$, also with a probability of 1. These corresponding sample pairs, $(x_i, y_i)$, are essentially the supervised pairs for domain translation. By adjusting loss function 7 (i.e., the distance metric of cycle loss and the balance parameter $\lambda$), this approach could replicate any supervised domain translation methods. The paper's impact would be significantly enhanced if the authors included this observation.

2. Overall, the structure of the proof is clear and easy to follow.
3. The experiments verified that this method could generate content-preserved samples with high quality, which corroborates their theory.

### Weaknesses
Overall, the structure of the theory is clear. However, there are several mistakes that should be corrected:
1. The MPA of the PDF of a gaussian distribution $N(\mu, \sigma)$ should be $h(x) = 2\mu - x$, rather than $h(x) = \mu - x$. This is a critical error, as the correct MPA is a reflection around the mean, not a translation by the mean. This significantly impacts the theoretical validity of the approach if not addressed correctly.
2. Within the "Notation" section of the introduction, "A" ought to be a subset of "Y", not "X". This is a fundamental error in the definition of the variable sets and needs to be rectified to ensure correct mathematical formalism.

Honestly, it is impractical to check every detail of the proof. The author should ensure the proof's rigor and review it meticulously.

Additional suggestion: Assumption 1 is confusing. I think it refers to the existence of the content-preserved mapping $f^*$ and $y^*$. Please make it clearer.

### Questions
In this study, it appears that only one auxiliary variable is used to diversify the distribution. What would happen if we used several variables? For example, we're considering not just the distributions $p(x|u=u_i)$ and $p(y|u=u_i)$, but also $p(x|v=v_j)$ and $p(y|v=v_j)$. Intuitively, utilizing one auxiliary variable is akin to "slicing" the original distribution in one way, while employing multiple variables is like trying different ways to make the "cuts".

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies Unsupervised domain translation (UDT),
e.g. to learn to generate cartoon sketches from ID photos
without supervision. The authors study why CycleGANs fail to
learn the desired UDT function; previous work has suggested that
the reason is the existence of automorphisms of the generative
distributions; they corroborate this suggestion with a theoretical
argument and then propose a second theoretical argument that
prevents existence of such automorphisms if one introduces conditioning
on auxiliary variables. They then show the effectiveness of the proposed
automorphisms elimination approach on a few benchmarks.

### Strengths
1. The paper is well written and easy to read.

2. The suggested elimination idea is well-motivated and simple
  to implement.

3. While *Theorem 1* operates under idealized assumptions, *Theorem 2*
  makes an attempt to show that the author's proposal is robust
  under more realistic circumstances.

4. The UDT tasks they experiment on seem challenging enough to be interesting.

### Weaknesses
The abstract sounds very specialistic to me. I think the paper might be of interest to a broader audience, but some readers unfamiliar with the jargon might be put off by the abstract.

My initial rating inclines towards acceptance. A limitation of my review is that I have not a direct experience with the baselines, so I cannot assess if the chosen baselines were too easy to beat.

### Questions
My initial rating inclines towards acceptance. A limitation of my review is that I have not a direct experience with the baselines, so I cannot assess if the chosen baselines were too easy to beat.

**Questions**:
1. In assumption 1 how realistic are the invertibility assumptions?
  Are there weakened versions, e.g. in a probabilistic sense?
2. Regarding Proposition 1 and the MNIST example in Figure 1, it seems
  that for MNIST the support of $P_x$ would not be path-connected, with one path-component
  for each digit. Then Proposition 1 would not apply directly. Can you formulate a case of Proposition 1 that would apply to this case?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper tackles common failures in CycleGAN and variants where the desired translation functions are not successfully identified and the methods produce content-misaligned translations. 

This limitation is claimed to be related to the presence of multiple translation functions (MPA). The authors introduce an MPA elimination theory and suggest a modified learning approach in which the cross-domain distributions are matched over auxiliary variable-induced subsets of the domains (e.g. translation between real human faces to cartoonized figures is conditioned on hair color and gender). 

Quantitative and qualitative evaluation on several geometrically-unaligned pairs of datasets (Rotated MNIST, Rotated Edges-2-Shoes and CelebA to Bitmoji) are presented to support the theoretical claims.

### Strengths
The studied problem of matching the distributions of unaligned image domains is of great interest in the image-to-image translation line of work. The development of theoretical frameworks as the one introduced in this paper can shed light on the limitations of such unsupervised approaches and lead to more robust translation methods.

### Weaknesses
1. The experimental study is not conducted in the most relevant setting in my opinion. As the proposed method relies on several auxiliary variables (e.g. hair color in human faces or the digit class in the MNIST experiment), I believe the baselines should represent methods in weakly-supervised image-to-image translation [1]. Comparison against unsupervised methods is unfair. Specifically, the method's reliance on auxiliary variables for cross-domain matching necessitates a comparison against methods that also leverage such information, rather than solely unsupervised approaches like CycleGAN. The current evaluation does not adequately demonstrate the advantage of the proposed method over other techniques that use similar auxiliary information.

2. The authors claim the auxiliary variables can be queried from available foundation models as CLIP. This idea is already explored in [1], could the authors please provide any experimental benchmark including CLIP-based annotations against [1]? The lack of a direct comparison with [1] using CLIP-based annotations leaves a gap in the evaluation, failing to demonstrate the novelty or superiority of the proposed approach in this specific context. It is crucial to show how the method performs when using the same type of auxiliary information derived from CLIP, as explored in [1].

3. There are some other works relating the failures in geometrically-unaligned image domains to architectural inductive biases [2]. Moreover, methods as [2] present translations between domains with some degree of geometry variation without access to additional labels in the form proposed in this paper. Could the authors provide a comparison to [2] on the celebA-to-bitmoji? The absence of a comparison with [2] is a significant oversight, as it does not address the potential impact of architectural biases on the results. The method should be evaluated against approaches that tackle geometric variations without relying on auxiliary labels, as done in [2], to fully understand its strengths and limitations.

### Questions
1. I find the qualitative results quite limited. For example, In Fig. 8, the translation from human faces to bitmoji does not preserve the facial expression. Considering that the gender and hair color is provided to the model, and the facial expression is not preserved, what other properties should the reader focus on to verify the validity of the translation?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
