# Dictionary Contrastive Learning for Efficient Local Supervision without Auxiliary Networks

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
While backpropagation (BP) has achieved widespread success in deep learning, it
faces two prominent challenges: computational inefficiency and biological implausibility.
In response to these challenges, local supervision, encompassing Local
Learning (LL) and Forward Learning (FL), has emerged as a promising research
direction. LL employs module-wise BP to achieve competitive results yet relies on
module-wise auxiliary networks, which increase memory and parameter demands.
Conversely, FL updates layer weights without BP and auxiliary networks but falls
short of BP’s performance. This paper proposes a simple yet effective objective
within a contrastive learning framework for local supervision without auxiliary
networks. Given the insight that the existing contrastive learning framework for
local supervision is susceptible to task-irrelevant information without auxiliary
networks, we present DICTIONARY CONTRASTIVE LEARNING (DCL) that optimizes
the similarity between local features and label embeddings. Our method
using static label embeddings yields substantial performance improvements in the
FL scenario, outperforming state-of-the-art FL approaches. Moreover, our method
using adaptive label embeddings closely approaches the performance achieved by
LL while achieving superior memory and parameter efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies local training, that is training with local error signals so as to eliminate backprop, which is not plausible biologically. The proposed method is dictionary contrastive learning, built upon a prior work that proposed using (supervised) contrastive learning for local learning. The main difference from that prior work is using a embedding dictionary $t_1, \cdots, t_Z$ for each of the $Z$ classes, and aligning intermediate features with the average pooling of these embeddings (for dimension agreement).

### Strengths
1. I think the subject matter of this work is very interesting, and I can see why contrastive learning is relevant in this context, though I should point out that neither the problem nor contrastive learning for local learning is first proposed by this submission.
2. The authors conduct a number of experiments to show that the proposed method is better than previous local learning methods, which is good, though I would say that there is one very important baseline that the authors do not compare to (see below).

### Weaknesses
I am not an expert of local learning or forward learning, though I am very familiar with representation learning and contrastive learning. So I read the most relevant cited papers in this work, and from my understanding, this work is a follow-up work of Wang et al. [1]. And my understanding is that the main difference between this work and [1] is the introduction of $\lbrace t_1, \cdots, t_Z \rbrace$, the dictionary. So while conventional contrastive learning maximizes the similarity between a positive pair of samples' features, this work maximizes the similarity between a sample's feature and its corresponding $t_i$, and $t_i$ is also being updated during training. My following review is mostly based on the above understanding, and the comparison between this work and [1]. Please let me know if there is anything that I misunderstand.

The following are my major questions and concerns:
### 1. Regarding Sections 3 and 4
Sections 3 and 4, arguably the most important two sections of this work, are really confusing. 
- Figure 1 compares "$L_{feat}$" with "$L_{contrast}$", and at first glance seems to suggest that contrastive learning is better than some other method called "feat", but this is not the case. Both methods minimize the contrastive loss, and the difference is that "feat" uses the intermediate outputs $h$ directly while "contrast" fits a network $\phi$ on top of it. So this figure does not show that contrastive learning is better, or "the performance of FF-based approaches falls short in comparison to InfoPro". Instead, it only shows that using a neural network $\phi$ is important. Thus, I am not quite sure what message the authors want to convey with Figure 1, as well as Figure 3.
- An important motivation of this work and LL/FL as a whole is the goal of removing backprop (BP), because BP is not biologically plausible and is not memory efficient. The abstract and intro of this submission make this point very clear. My question is: If you use a neural network $\phi$ in Eqn. (1), then how can you remove BP? Don't you use BP to train this $\phi$? It might be true that using a smaller network $\phi$ can save memory, but my point is BP is still there if you are using this $\phi$, unless you are updating this $\phi$ with local learning too (which I don't think is the case). Thus, I don't think the proposed method can be called forward learning (FL), which by definition should have no BP at all. And it is not very fair to compare the proposed method with FL methods.
- In Section 4, "Mapping labels to embedding vectors", the authors wrote "the label embeddings in the dictionary are updated at each step, making them a dynamic concept". But how are these $t_i$ updated? Are they updated by minimizing the loss $L_{dict}$? If this is the case, then this update is not local, because remember that the same $t_i$ are shared across all layers (which then go through pooling), so the update signals of $t_i$ come from all layers. Consequently, the layers cannot be learned in parallel as FL methods, because all layers need to jointly update $t_i$. I would say that it makes more sense to me if these $t_i$ are fixed, unless there are some imperative reasons that $t_i$ must be updated.
- In Eqn. (2), why there is an average over $K$? And why does there need to be $K$ feature maps for one class in the first place? Eqn. (2) can be simplified as $L_{dict} = -\frac{1}{N} \sum [ \text{log} \frac{\text{exp}( \langle h_n, t_+' \rangle )  }{ \sum \text{exp}( \langle h_n, t_i' \rangle ) } ]$, where $h_n$ is the average of $h_n^k$. So why not just use one $h_n$, but use K $h_n^k$ if they are equivalent?

### 2. Regarding the experiments
- My biggest concern with the experiments is that this work is built upon InfoPro [1], yet in the experiments it is not compared to InfoPro [1] at all. I feel that it is very likely that the method proposed in this work has a very similar performance to InfoPro.
- The experiments compare the proposed method with FL methods, which as I said is not very fair, because I don't think the proposed method is FL since it still uses backprop when updating $\phi$. InfoPro [1] did not claim their method to be FL. In fact, their paper did not mention FL at all.

[1] Wang et al., Revisiting locally supervised learning: an alternative to end-to-end training, ICLR 2021.

### Questions
Minor points:
- The authors wrote $K = H \times W$ in several places, which makes little sense to me. Why does an image need to have as many feature maps as the number of its pixels? And why does it need to have multiple feature maps in the first place?
- Can you explicitly write out the formula of $pool_l$? For example, what does it do when $C_h^l > C_D$? Does it do zero padding? And can you tell me what is the motivation of pooling, other than adjusting the dimensions?


**Summary:** Overall, though I do think that the idea of introducing a dictionary could be interesting, I don't think this work presents this idea very well and makes enough justification. The paper is really confusing at times. Moreover, I feel that even the authors themselves are confused sometimes, when they call their method FL which to my understanding really isn't, and use $K=HW$ features in Eqn. (2) which is equivalent to using a single feature. Thus, I recommend rejecting this submission.

**Rebuttal note:** Score changed from 3 to 6.

My suggestion to the authors would be to read Wang et al. [1] very carefully, which I did before reviewing this submission. Their motivation was to improve over end-to-end training, and they did not mention removing BP or forward learning at all. That's why it makes sense for their method to use a BP-updated neural network, as long as it is modularized. Also, given the great similarity between this work  and [1], InfoPro should be the most important baseline in your experiments.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper offers a new algorithm for Forward Learning that is based on intermediate layer features being close to adaptive label embeddings. This work shows comparison to various FL techniques, and shows that the proposed technique is beneficial in terms of performance, and memory usage.

### Strengths
The paper builds on intuition existing in many previous works (see Questions section for potential missing literature) to create a new FL algorithm. The work is presented well, and the experiments look convincing. Further, the method is simplistic, intuitive, and in my view has great potential in future works. The authors also provided code for reproducibility, which is great.

### Weaknesses
I REALLY enjoyed reading the paper, and I think other than some missing literature and visual comments, the paper is very good. 
One possible comment is that the architectures used are a not exactly SOTA - I would love to see this done with ResNets, ViT, RegNets and so forth - this could enhance the paper greatly.

### Questions
**Questions**:
1. It is interesting that the authors chose to have one embedding per class for all layers. One could think that different layers can achieve different levels of clustering and therefore both the embeddings and the loss weight on them can be different (see for example [2]). Another alternative to this would be to learn an MLP from the features to the embeddings, rather than using average pooling. I wonder if the authors tried this direction. 
2. Another question is wether the authors considered having more than one embedding per class, given that there may be variability within each class. - this could then be some hyperparameter: number of embs per class
 

**Possible missing literature**:
1. I think the paper relates very much to the literature of neural collapse in intermediate layers. It would be great to see the authors mention these works and make the connection. [1-4, 6]

2. There have been previous works that use intermediate layer losses to encourage class label clustering in the BP setting [2, 5].


[1] Papyan, V., Han, X. Y., & Donoho, D. L. (2020). Prevalence of neural collapse during the terminal phase of deep learning training. Proceedings of the National Academy of Sciences, 117(40), 24652-24663. https://doi.org/10.1073/pnas.2015509117

[2] Ben-Shaul, I. &amp; Dekel, S.. (2022). Nearest Class-Center Simplification through Intermediate Layers. <i>Proceedings of Topological, Algebraic, and Geometric Learning Workshops 2022</i>, in <i>Proceedings of Machine Learning Research</i> 196:37-47 Available from https://proceedings.mlr.press/v196/ben-shaul22a.html.

[3] Ben-Shaul, I., Shwartz-Ziv, R., Galanti, T., Dekel, S., & LeCun, Y.  Reverse Engineering Self-Supervised Learning. In Proceedings of the Thirty-seventh Conference on Neural Information Processing Systems (NeurIPS 2023).

[4]  Rangamani, A., Lindegaard, M., Galanti, T. &amp; Poggio, T.A.. (2023). Feature learning in deep classifiers through Intermediate Neural Collapse. <i>Proceedings of the 40th International Conference on Machine Learning</i>, in <i>Proceedings of Machine Learning Research</i> 202:28729-28745 Available from https://proceedings.mlr.press/v202/rangamani23a.html.

[5] Gamaleldin F. Elsayed, Dilip Krishnan, Hossein Mobahi, Kevin Regan, and Samy Bengio. Large margin deep networks for classification. In NeurIPS, 2018.

[6] Galanti, T., Galanti, L., & Ben-Shaul, I. (2023). Comparative Generalization Bounds for Deep Neural Networks. Transactions on Machine Learning Research, (ISSN 2835-8856).

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a back-propagation free training method for neural networks based on a novel contrastive learning loss. This contrastive learning loss is defined in terms of a dictionary of label embeddings. The main motivation for using this loss is reduction of the mutual information between feature representations and a nuisance term, which model task-irrelevant information present in the inputs. The authors demonstrate theoretically that minimizing the proposed loss is equivalent to maximizing the mutual information of representations and labels. Furthermore, they demonstrate empirically that their algorithm reduces the mutual information of representations and the nuisance.

### Strengths
The authors tackle an important direction in the training of neural nets, i.e., back-propagation free training. They do so in a novel way, by proposing a new training objective based on a dictionary of label embeddings. Their contribution is also interesting through the angle of the label embeddings themselves. The resulting algorithm works well in practice, being comparable or even better than existing state-of-the-art, and while being relatively light-weight in comparison with existing approaches.

### Weaknesses
__W1: Presentation issues.__ Below I highlight a few presentation issues,

- The authors mention the mutual information $I$, but never formaly define it. Furthermore, even though the authors given details about how they estimate mutual information, I think an explicit pointer (e.g., Appendix D describes how we estimate the mutual information) in the text could make it the paper easier to read.

- In my view, the result the authors prove in Appendix B is part of the paper's contribution. I think authors should consider moving it to the main paper and properly make a statement about the claim, as it is used throughout the author's analysis.

__W2: Inconsistent notation.__ While in eqn. $i$ and $j$ are used to refer sample indices, in eqn. 2 the authors use $n=1,\cdots,N$. Index $i$ in eqn. 2 then means the class $i=1,\cdots,Z$ and elements of the dictionary are referred to as $\mathbf{t}\_{z} \in \mathbf{D}^{Z}$, which is confusing as well, as $z$ can be easily mistaken by $\mathbf{z} = f_{\phi}(\mathbf{h})$. Furthermore, in page 3, $y \in \mathbb{N}$ would imply an infinite amount of classes. Authors should refer to $y \in \{1,\cdots, Z\}$, as the authors do in table 4. The fact that one has a finite number of classes should be explicit.

__Minor.__ The paper contains some reference errors, especially w.r.t. arxiv references to conference papers. Here is a non-exhaustive list of wrong references,

- Yulin Wang, Zanlin Ni, Shiji Song, Le Yang, and Gao Huang. Revisiting locally supervised learning: an alternative to end-to-end training. arXiv preprint arXiv:2101.10832, 2021. (Published in ICLR 2021)
- Karen Simonyan and Andrew Zisserman. Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556, 2014. (Published in ICLR 2015)

__Note.__ the minor point __did not influenced my final score__.

__Post-Discussion__

The authors have corrected the presentation issues and inconsistent notation. As a result I raised my score towards 8: Accept

### Questions
__Q1.__ While the authors show in Appendix B that minimizing $\mathcal{L}\_{dict}$ is equivalent to maximizing a lower bound of $I(\mathbf{h}, y)$, could a similar statement be derived for $I(\mathbf{h}, r)$ or $I(r, y)$?

__Q2.__ Do the learned label embeddings have any semantic meaning? The authors could verify this through dimensionality reduction on $\mathbf{t} \in \mathbf{D}^{Z}$, in the context of a dataset with a large number of classes (i.e., CIFAR-100).

__Post-Discussion__

The authors added a visualization of label embeddings, in which  they show that the embeddings learned by their method carry semantic meaning.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
