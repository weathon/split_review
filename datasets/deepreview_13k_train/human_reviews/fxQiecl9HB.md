# Crystalformer: Infinitely Connected Attention for Periodic Structure Encoding

- Decision: Accept
- Scores: 8, 8, 8, 5

## Abstract
Predicting physical properties of materials from their crystal structures is a fundamental problem in materials science. In peripheral areas such as the prediction of molecular properties, fully connected attention networks have been shown to be successful. However, unlike these finite atom arrangements, crystal structures are infinitely repeating, periodic arrangements of atoms, whose fully connected attention results in \emph{infinitely connected attention}. In this work, we show that this infinitely connected attention can lead to a computationally tractable formulation, interpreted as \emph{neural potential summation}, that performs infinite interatomic potential summations in a deeply learned feature space. We then propose a simple yet effective Transformer-based encoder architecture for crystal structures called \emph{Crystalformer}.
Compared to an existing Transformer-based model, the proposed model 
requires only 29.4\% of the number of parameters, with minimal modifications to the original Transformer architecture.
Despite the architectural simplicity, the proposed method outperforms state-of-the-art methods for various property regression tasks on the Materials Project and JARVIS-DFT datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an attention mechanism and a transformer model for periodic structure encoding. The attention mechanism is formulated as an infinite sum over the periodic extensions of the unit cell in all three directions. In order to make the sum tractable, the paper proposes a distance decay attention by which the spatial dependencies between atoms decay exponentially with their distance. The authors present an evaluation of this attention mechanism, incorporated into a transformer architecture, on two data sets and several material property prediction tasks, comparing with a handful of methods from the crystal modelling literature.

### Strengths
This paper is clearly written and easy to follow. I have enjoyed reading it and I believe it will likewise be relevant for the machine learning community working on materials modelling. Concretely, these are some of the strengths I see in this paper:

- The introduction effectively describes the gap in the literature it addresses, namely the periodic nature of crystal structures, which is not considered in the core of the GNN literature devoted to molecular modelling. The paper provides a comprehensive review of graph and transformer models for related tasks and motivates the need for a method to account for the periodic nature of crystal structures.
- Sections 2 and 3 clearly describe the proposed model and the figures effectively support the text descriptions.
- The evaluation seems sound and the results achieved by the proposed method are remarkable compared to existing approaches, including in terms of training and inference time.

### Weaknesses
I do not have any major concerns. If I were to put on the hat of the average machine learning reviewer, I could argue that the technical contribution of this paper is limited because the method is a small adjustment of existing work. However, that is largely irrelevant to me provided the idea is sound, it is clearly described, it addresses a current challenge in materials modelling and the results are competitive.

One comment regarding the presentation of results that I can make is that it would be much easier to interpret the results if they were presented graphically instead of in tables, despite this being the common practice in the machine learning community.

### Questions
- The results in Table 4 demonstrate that the inclusion of the value position encoding systematically improve the performance of the model. However, we observe significant differences in the performance gap between the proposed and simplified models across properties. Do you think this gap in performance could be explained by the characteristics of each property?
- I am also curious whether you have some intuitions about why the performance of the dual space version of the model is significantly better than the baseline in the case of predicting the energy above hull.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To encode infinitely repeating crystal structures, this paper introduces a distance-decay inductive bias into the attention mechanism to ensure tractability. The authors compare their method with five baseline methods on two datasets.

### Strengths
1. The proposed decayed attention naturally incorporates a physical inductive bias, making the attention mechanism for infinite structures computationally tractable.
2. Good experimental results, and each component of the proposed method is also validated through ablation experiments.

### Weaknesses
1. The necessity of $\psi_{ij}(n)$ is unclear. Although the authors give an example in Page 4,  it remains questionable whether it is appropriate to assume $\mathcal{X} = \{x_1\}$ when attempting to prove the necessity of $\psi_{ij}(n)$. Specifically, while the monatomic case highlights the issue of lattice vector insensitivity, it is not clear if this is the only scenario where $\psi_{ij}(n)$ is necessary. The argument would be stronger if it could be shown that without $\psi_{ij}(n)$, the model would fail in more general cases, not just the monatomic one. The current justification feels somewhat limited to a specific edge case rather than a general requirement.
2. Lack of discussion on reflection and periodic transformations [1]. The paper should explicitly address how the model handles reflectional symmetry and other periodic transformations beyond simple translations. It's crucial to understand whether the model is invariant or equivariant to these transformations, and if not, how this might affect its ability to generalize to different crystal orientations.
3. About writing
	- In Figure 2, the representation of the infinitely connected attention is not clear. The figure presents a matrix-based representation of the attention mechanism, which is not immediately intuitive for understanding how the infinite connectivity is achieved. The connection between the matrix operations and the actual infinite structure is not well-explained, making it difficult to grasp the core idea.
	- In Figure 3, the interaction of $X^t$ with $\mathcal{P}$ and $l_1, l_2, l_3$ requires a more detailed and explicit illustration, as they are somewhat hidden within the formulas, which can be challenging for readers to locate. The figure should clearly show how the lattice vectors and periodic structure are incorporated into the attention mechanism, and how they influence the node representations. The current representation is too abstract and lacks a clear visual connection to the underlying physical structure.
	- "With simple algebra, we can rewrite Eq. (3) as..." This rewriting should be included in the appendix somewhere, and please point to it.

### Questions
None

### Soundness
3 good

### Presentation
2 fair

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
The paper proposes a new transformer architecture, called Crystalformer, for crystal structure property prediction that manages the periodic structure of crystals. To completely capture the periodic structure of crystals one would effectively require infinitely connected attention, which is intractable, prompting the papers to introduce a new attention method to effectively manage this requirement using a distance based decay.

The papers starts by introducing the problem of crystal structure property prediction and discusses recent approaches, including GNN-based neural networks and a couple of transformer models, specifically Matformer. The paper then introduces a set of preliminaries, including description of crystal structures and the self-attention mechanism. Subsequently, the authors describe the different components of Crystalformer with a focus on the attention formulation called pseudo-finite periodic attention that encodes relevant crystal information. Next, the authors describe distance decay attention, which applies a Gaussian decay function to place less importance on atoms that are further apart from each other and thereby simplifies the need for infinitely connected attention to a tractable problem. The authors describe relevant details of their attention formulation and distance decay function before outlining their network architecture consisting of multiple attention blocks.

In Section 4, the paper described related work in detail and emphasizes how Crystalformer differs from various competing approaches and showcase experiments on Materials Project and JARVIS in Section 5. The experiments in Section 5 show that Crystalformer generally outperforms relevant GNN and transformer baselines for both datasets. Next, the paper provided a set of ablation studies related to removing positional encodings and performing attention in Fourier space.

### Strengths
The paper has the following strengths:
* The paper presents a new attention formulation for crystal structure design that makes an infinite attention scenario computationally tractable (originality, significance).
* The paper provides detailed problem descriptions and related work outlining how their work differentiates itself from prior methods (clarity, significance).
* The paper provides relevant experimental results and ablations to supports its primary claims (quality).

### Weaknesses
The paper currently provides a somewhat limited scope in its experiments, especially for the datasets, and could be also improved by including additional relevant datasets and models:
* Datasets: OQMD [1], NOMAD [2] which are crystal structure datasets available through the Open MatSci ML Toolkit [3]. Experiments on these datasets would significantly strengthen the claims of the paper since they include significantly more datapoints than the ones in the current experiments. The toolkit also includes a more updated version of Materials Project with ~150k crystal structures.
* Models: FAENet [4], Equiformer [5]. While new experiments would be ideal to strengthen the paper claims, I would at least like to a discussion of these models in related work.

Additionally, the current draft would benefit from additional clarity related to the method, which are described in the section below.

### Questions
The paper could be improved by addressing the following questions related mainly to clarity:
* An example consisting of input features (atom types and atom positions) would make things clearer showing how the data is exactly processed. Figure 3 shows that positions and lattice parameters go into the attention blocks, but their processing is not explained in Figure 2.
* Can you describe stochastic weight averaging? It's first mentioned in Table 1.
* What is the reason for choosing your datasets? It seems like the Materials Project version is significantly smaller than the latest version. It would be good to have more details.
* Did you try other decay functions? Why or why not?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to construct fully connected graphs for crystal materials, with two attention biases between node pairs proposed. From my understanding, the first attention bias ($\alpha$ ones) captures infinite interactions between two nodes, and the second one ($\beta$ ones) captures the local interactions in the summation form. After this, the traditional fully connected transformer architectures can be applied. The experiments show a good improvements beyond Matformer.

### Strengths
The strengths of this method are as follows.

- A reasonably good transformer network with high efficiency for crystal scalar property prediction
- Good presentation, easy to follow writing
- Good efficiency for a transformer architecture

### Weaknesses
However, there are some concerns of this paper.

- One of the most important issue is that there is another work named PotNet[1], already published one year ago, proposed a method to calculate infinite summations for node pairs in crystal structures. The core idea in this paper of calculating the first attention bias ($\alpha$ ones) capturing infinite interactions between two nodes of this paper are very similar to PotNet. But the similarity is not mentioned, and comparison is not provided. Besides the first attention bias ($\alpha$ ones), the second attention bias ($\beta$ ones) is not new. It can be seen as the summation of local radius features.

- The derivation in the appendix might be problematic, the authors use word "may be", which is ambiguous. If authors want to use Equation (S14) in the Appendix to derive the first attention bias, which is one of their major contribution, the coefficient in the reciprocal space needs to be properly derived. 

- The paper uses “computationally tractable” in many places, but the error bound of the summation is still unknown to me. Particularly, the authors say if the $\sigma$ of $\sum_n e^{-\frac{\| r\|^2}{2\sigma}}$ or $\sum_n \| r \| e^{-\frac{\| r\|^2}{2\sigma}}$ has an upper bound and lower bound then is tractable. If it is tractable, then what is the exact error between the authors’ evaluation and the value of every summation $\sum_n e^{-\frac{\| r\|^2}{2\sigma}}$

- The performances of the proposed method is not very significant without the additional stochastic weight averaging (SWA) (Izmailov et al., 2018) by averaging the model weights for the last 50 epochs with a fixed learning rate. If with this module, the comparison is not that fair, but without this module, the performance gains are not very significant.

### Questions
The major questions are provided in the above weakness section. Given the concerns for now, I vote for rejection.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
