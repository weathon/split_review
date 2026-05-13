# On the Stability of Expressive Positional Encodings for Graphs

- Decision: Accept
- Scores: 8, 5, 6, 5, 6

## Abstract
Designing effective positional encodings for graphs is key to building powerful graph transformers and enhancing message-passing graph neural networks. Although widespread, using Laplacian eigenvectors as positional encodings faces two fundamental challenges: (1) \emph{Non-uniqueness}: there are many different eigendecompositions of the same Laplacian, and (2) \emph{Instability}: small perturbations to the Laplacian could result in completely different eigenspaces, leading to unpredictable changes in positional encoding. 
 Despite many attempts to address non-uniqueness, most methods overlook stability, leading to poor generalization on unseen graph structures. We identify the cause of instability to be a ``hard partition'' of eigenspaces. Hence, we introduce Stable and Expressive Positional Encodings (SPE), an architecture for processing eigenvectors that uses eigenvalues to ``softly partition'' eigenspaces. SPE is the first architecture that is (1) provably stable, and (2) universally expressive for basis invariant functions whilst respecting all symmetries of eigenvectors. Besides guaranteed stability, we prove that SPE is at least as expressive as existing methods, and highly capable of counting graph structures. Finally, we evaluate the effectiveness of our method on molecular property prediction, and out-of-distribution generalization tasks, finding improved generalization compared to existing positional encoding methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This works further deepens results on basis-invariant GNNs building on work of e.g. Wang et al (ICLR 2022) and Lim&Robinson et al (ICLR 2023). The authors propose a simple generalization of basis-net, with strong theoretical guarantees (Hölder-smoothness / stability and basis-invariance). They achieve strong performance in standard molecular benchmarks, out-of-distribution benchmarks and cycle count tasks.

### Strengths
Extremely well written and easy to follow. Figure 1 is nice!

The proposed model SPE (Eq. 2) is a simple generalization extension of basis-net. It is very interesting to see that such a straightforward modification yields such strong (and non-trivial) theoretical results (Theorem 1, etc.).

Empirical performance is very convincing, e.g. for Zinc and the OOD tests.

------ during rebuttal ------
as reviewers addressed my concerns and in fact added clarifications on runtime and more importantly on the unstability of previous methods I raised my score and now clearly vote for acceptance.

### Weaknesses
The achieved theoretical and empirical results, while very interesting, seem somewhat incremental compared to Wang et al (ICLR 2022) and Lim&Robinson et al (ICLR 2023). The authors should discuss the differences more clearly. In particular:
* The reason for Hölder continuity ($c\neq1$) is not fully clear. E.g. does PEG / standard basis-net already already satisfy your stability criterion Def 3.1 and / or Assumption 3.1.? If yes, what is the conceptual / theoretical benefit of your proposed architecture. If not, could you please provide an argument why the assumptions fail for PEG / basis-net.
* Is $c\neq 1$ crucial for any proof / guarantee / assumption? 
* Are there cases where SPE satisfies the stability assumption of Wang et al (ICLR 2022), i.e., with $c=1$?

Please see also the questions below.

Minor:
* Remark 3.1 Should probably be attributed to Wang et al (ICLR 2022), as they have the same statement for $c=1$.

### Questions
Please provide runtimes for your proposed method. Preferably for pre-processing and overall runtime. This would help to put the achieved results into context with basis-net, etc.

While the OOD generalization bound is very interesting, can you also state a standard PAC-style generalization bound (same distribution for train and test)?

Do you have a counter-example where SPE cannot count $k$-cycles for $k\leq 6$?

The $n\times n\times m$ might be somewhat excessive for certain datasets. Would it be possible to exchange $V\\phi(\cdot) V^T$ to $V^T\phi(\cdot) V^T$ to get the much smaller $d\times d\times m$ instead? If not what would this more compact model correspond to?

If I am notmistaken SPE and basis-net should have the same expressivity and thus at least theoretically be both equally capable of counting cycles etc. Can you provide some intuition why SPE performs significantly better than basis-net in this task (Figure 3)?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes stable and expressive Laplacian positional encodings (SPE) by performing a soft and learnable partition of eigensubspaces. The encoding guarantees that small perturbations to the input Laplacian induce a small change to the final positional encodings. The empirical results suggest a trade-off between stability (correlated with better generalization) and expressive power.

### Strengths
- The idea to address the stability of LapPE is novel, with SPE being a universal basis invariant architecture. 
- The motivation is well established, the difference to other related works is concise, the propositions are described well and the strength of SPE as a universal basis invariant architecture is presented thoroughly. 
- The experiments show the improvement in generalisation for SPE and its improved capabilities in recognising substructures, which are interesting outcomes of the architecture.

### Weaknesses
 - The novelty of the method itself is partially limited as the idea to use a weighted correlation over the eigenvectors closely resembles the correlation used in BasisNet. 
- The experiments are limited. The performance of SPE in Table 1 is sub-par, and details of the experimental results in Figure 2 are unclear and the hyperparameters seem not to be reported, which makes it hard to reproduce the experiments. 
- The point regarding the trade-off between expressivity and generalisation is unclear. Is there a formal explanation which we can quantify? 
- Perhaps additional experiments could be useful, e.g.,:
  - An experiment comparing the generalisation gap of LapPE/BasisNet/SPE.
  - Evaluating the performance of LapPE/BasisNet/SPE on LRGB or TUDatasets.

### Questions
Please refer to my review.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Stable and Expressive Positional Encodings (SPE), an architecture that mainly addresses the challenges of instability in using Laplacian eigenvectors as positional encodings for graph neural networks. The key insight to overcome instability is to avoid `hard partitions' of eigen-subspaces, and instead, use soft partitions via Lipshitz continuous functions over the spectrum. The stability of SPE is proved and validated via out-of-distribution generalization experiments.  Universal expressiveness is also proved, mainly based on another work, i.e., BasisNet.

### Strengths
- S1. I like the design of the experiment in that the authors validate the stability of SPEs from an aspect of out-of-distribution generalization.

- S2. The authors target at robustness/instability and generalization of PEs, which is novel in the literature.

- S3. The paper is overall well written.

### Weaknesses
 >  W1. The instability of prior method (i.e., the so-called hard partition method) is not proved.

 The authors point out under Eq.2 that **hard partition** is induced when $\[\phi_{\ell}(\boldsymbol{\lambda})\]_j=\mathbb{1}$(other places in $\phi(\cdot)$ are zeros),

and then $\boldsymbol{V}\text{diag}(\phi_{\ell}(\boldsymbol{\lambda}))\boldsymbol{V}^{T}$ is the $\ell$-th subspace.

The problem is that, if we set $\{ \phi_i \}_{i=1}^{m}$ that induce the hard partitions, 

then they are **constant functions** and meet the $K_{\ell}$-Lipschitz continuous assumption in Assumption 3.1, which is then used to prove the stability of SPE. 

Therefore, the question is,  **is the prior method (i.e., the counterpart that uses hard partitions) really unstable?** It seems that hard-partitioned SPE can be proved to be stable via exactly the same proof of Theorem 3.1.

> W2. Equivalence for $\{\phi_i\}_{i=1}^{m}$ .

The authors restrict $\{\phi_i\}_{i=1}^{m}$ to be permutation equivariant, whose input is the Laplacian spectrum. Here, the authors are asking for equivalence under the reordering of eigenmaps/eigenvalues, instead of the reordering of graph nodes. 

> W3. On the universal expressiveness. 

The proof of this SPE's universality relies on being reduced to BasisNet. Therefore, two problems arise: 

- The experiment regarding expressiveness, i.e., the graph substructure counting, does not include BasisNet.
- According to Lim et al. (2023), the instance of BasisNet, Unconstrained-BasisNet, universally approximates any continuous basis invariant function. In Unconstrained-BasisNet,  IGN-2 (Maron et al., 2018) is the core part to achieve such expressiveness. However, in implementation, the authors set $\rho$ to be one identical GIN (Xu et al., 2019),  which would surely limit the expressiveness. 

> W4. Lack of description of baseline models.

For the same reason as in W3, in the experimental part, specific choices of baseline instances, i.e.,  $\rho$ and $\phi$ of BasisNet, should be described more clearly.

### Questions
Please check W1, W2, and W3. Below is an additional question: 

Q1: Would the learned  $\\{\phi_i\\}_{i=1}^{m}$ be close to each other? This would lead to similar position encodings.

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
This paper proposes a new approach for generating positional encodings which are stable and can universally approximate basis invariant functions. To compute those encodings, the method first decomposes the Laplacian matrix, it then applies different permutation equivariant functions to the eigenvalues, and uses the output of those layers to produce matrices of dimension $n \times n$ which are then fed to another permutation equivariant network (e.g., a GNN). The proposed method is evaluated on molecular property prediction datasets and also on a dataset with domain shifts where it outperforms other positional encoding methods in most cases.

### Strengths
- The stability of graph learning algorithms is a topic that has not been explored that much yet and deserves more attention from the community. The results presented in this paper contribute to this direction.

- In my view, the paper has some value since several individuals from the graph learning community would be interested in knowing its findings. Practitioners would also be interested in utilizing the proposed encodings since in many settings, existing GNN models fail to generalize to unseen domains.

- The proposed model achieves low values of MAE on the ZINC and Alchemy datasets and outperforms the baselines. This might be related to the model's ability to identify and count cycles of different lengths.

### Weaknesses
 - I feel that the paper lacks some explanations. It is not clear which modules of the proposed method contribute to it being stable. If no $\phi_\ell$ layers are added, wouldn't $K_\ell$ be equal to 1? In my understanding, this wouldn't hurt stability. Also, it seems to me that as $m$ increases the bound becomes looser and looser. If that's the case, why do we need multiple such permutation equivariant layers?

- One of the main weaknesses of this paper is the proposed model's complexity. Function $\rho$ takes a tensor of dimension $n \times n \times m$ as input. This might not be problematic in case the model is trained on molecules since molecules are small graphs. But in case of other types of graphs such as those extracted from social networks which are significantly larger, this can lead to memory issues.

- The proposed approach is much more complex that a standard GNN model, but in most cases it provides minor improvements over a model that does not use positional encodings. For instance, the improvement on Alchemy is minor, and also on DrugOOD, SPE provides minor improvements in the Assay and Scaffold domains and no improvements in the Size domain.

- No running times of the different models are reported in the paper. 

- The proposed model seems to advance the state of the art in the field of positional encodings for graphs, however, it is not clear whether it also advances the state of the art in the graph learning community. I would suggest the authors compare the proposed approach against some recently proposed GNN models, and not only against methods that produce positional encodings.

Typos:\
p.6: "hold and Let" -> "hold and let"\
p.7: "we take to $\rho$ to be" -> "we take $\rho$ to be"\
p.8: "which hypothesizes is because" -> "which is because"

### Questions
In Figure 2, how did you compute the Lipschitz constant of MLPs? We can compute the Lipschitz constant for models that consist of a single layer, but exact computation of the Lipschitz constant of MLPs
is NP-hard [1].

[1] Virmaux, Aladin; Scaman, Kevin. Lipschitz regularity of deep neural networks: analysis and efficient estimation. Advances in Neural Information Processing Systems, 2018.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the stability of eigenvector-based positional encodings while previous methods mainly focus on the sign- and basis-invariant properties. The authors claim that the instability of the previous method is caused by the hard partition of eigenvectors and the ignorance of eigenvalues. To address this challenge, this paper proposes SPE, which leverages the eigenvalues to re-weight the eigenvectors in a soft partition way. SPE is provably stable and shows great expressive power. Experiments on various tasks validate the superiority of the proposed method over baselines.

### Strengths
1. The proposed SPE is provably stable, which means that it can generalize to unseen graphs. I think this strong inductive learning ability is crucial for graph representation learning. The theoretical contribution is great.

2. The proposed SPE shows great expressive power, which not only universally approximates previous basis invariant functions but also can distinguish the cycles in graphs. Experimental results validate the effectiveness of the proposed method.

3. In addition to previous methods that conduct experiments in the basic molecular property prediction tasks, this paper also considers a more challenging out-of-distribution (OOD) task for evaluation.

### Weaknesses
1. The complexity of the proposed SPE is much larger than previous positional encoding methods because it needs to reconstruct graph structures, i.e., $\boldsymbol{V} \operatorname{diag}\left(\phi(\boldsymbol{\lambda})\right) \boldsymbol{V}^{\top}$, whose complexity is $\mathcal{O}(KN^{2})$. In contrast, the Transformer-based methods, e.g., BasisNet, only have the complexity of $\mathcal{O}(NK^{2})$, where $K \ll N$. This computational burden could limit the scalability of SPE to very large graphs, especially considering the need to compute the full eigendecomposition. The matrix multiplication involved in reconstructing the positional encoding is a significant overhead, and it is unclear how this cost scales with the size of the graph in practice, beyond the theoretical complexity. 

2. In the molecular property prediction task, SPE has more parameters than baselines. It would be better if the authors could align the number of parameters across different methods to allow for a more fair comparison. Additionally, in the OOD tasks, the improvement of SPE over baselines is marginal, which raises questions about the practical benefits of the method in challenging scenarios. The small gains on OOD tasks suggest that the proposed stability might not translate to a significant performance boost in practice, and the additional computational cost might not be justified.

### Questions
Here are some concepts that I am not sure I fully understand. Please correct me if there are any misunderstandings.

1. In equation (1), what does $\mathbb{R}^{n \times d} \times \mathbb{R}^d \rightarrow \mathbb{R}^{n \times p}$ mean? I understand that $\mathbb{R}^{n \times d} \rightarrow \mathbb{R}^{n \times p}$ represents the function applied to the position features of each node. What does $\mathbb{R}^d$ indicate? Operation on eigenvalues?

2. What is the difference between a hard partition and a soft partition?  I do not see a clear definition. Does hard partition indicate a fixed number of eigenvectors and does soft partition mean it can handle a variable number of eigenvectors?

3. Is it possible to replace the element-wise MLPs of $\phi$ with polynomial functions? In this situation, I think the complexity can be significantly reduced and the expressiveness can be preserved since polynomials are also non-linear.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
