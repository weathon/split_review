# Homomorphism Counts as Structural Encodings for Graph Learning

- Decision: Accept
- Scores: 6, 8, 8, 6, 6

## Abstract
Graph Transformers are popular neural networks that extend the well-known Transformer architecture to the graph domain. These architectures operate by applying self-attention on graph nodes and incorporating graph structure through the use of positional encodings (e.g., Laplacian positional encoding) or structural encodings (e.g., random-walk structural encoding). The quality of such encodings is critical, since they provide the necessary \emph{graph inductive biases} to condition the model on graph structure. In this work, we propose \emph{motif structural encoding} (\ourpe) as a flexible and powerful structural encoding framework based on counting graph homomorphisms. Theoretically, we compare the expressive power of \ourpe to random-walk structural encoding and relate both encodings to the expressive power of standard message passing neural networks. Empirically, we observe that \ourpe outperforms other well-known positional and structural encodings across a range of architectures, and it achieves state-of-the-art performance on widely studied molecular property prediction datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Motif Structural Encoding (MoSE), a novel structural encoding method based on homomorphism counts for graph learning tasks. MoSE leverages homomorphism counts to represent graph structure effectively, aiming to surpass limitations found in common positional and structural encodings such as Random Walk Structural Encoding (RWSE). Theoretically, MoSE demonstrates enhanced expressiveness compared to RWSE and is shown to be independent of the Weisfeiler-Leman (WL) hierarchy, thus providing a broader graph representation power. The paper provides empirical validation, showing that MoSE achieves superior results over other encoding methods on various datasets, including molecular property prediction on ZINC and QM9.

### Strengths
- MoSE’s homomorphism count-based encoding enhances expressiveness beyond RWSE and aligns well with complex graph structures, as it provides unique structural insights through flexible motif selection.
- The paper rigorously compares MoSE to established methods and relates its expressiveness to the WL hierarchy, grounding its effectiveness in theoretical proofs.
- MoSE achieves state-of-the-art results on benchmarks, showcasing its applicability and effectiveness in both real-world and synthetic datasets, particularly in molecular graph prediction tasks.

### Weaknesses
 - The performance of MoSE may vary depending on the choice of motif graphs, requiring task-specific tuning to achieve optimal results. Specifically, the paper does not provide a clear methodology for selecting appropriate motifs for a given task, and the impact of suboptimal motif selection on performance is not thoroughly explored. This lack of guidance makes it difficult to apply MoSE effectively in practice, as the user is left to rely on trial and error.
- Calculating homomorphism counts for large and complex graphs could increase computational requirements, potentially limiting scalability for very large datasets. While the paper mentions the computational complexity, it does not provide a detailed analysis of the practical implications for different graph sizes and densities. Furthermore, the paper lacks a discussion of potential optimization techniques to mitigate this computational burden, such as approximation methods or parallelization strategies.
- The theoretical analysis of the expressivity of homomorphism counts has been established and well-studied by recent works (e.g., Jin et al. 2024). It is not very clear what additional theoretical contribution this paper has. The paper does not clearly articulate how its theoretical results extend or differ from existing work, and it does not provide a comparative analysis of the theoretical limitations of MoSE compared to other structural encoding methods.

### Questions
Please see Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces MoSE, a graph structural encoding based on homomorphism counts. The authors present theoretical arguments suggesting that MoSE has greater expressive power than RWSE and demonstrate competitive empirical performance when integrated with GTs.

### Strengths
1. The experiments supports the claim that MoSE improves performance on molecular property prediction tasks.
2. The theoretical arguments provide a plausible explanation for the observed performance gains.
3. The paper is well-organized and easy to follow.

### Weaknesses
1. The paper focuses on comparing MoSE with RWSE, justified by RWSE's empirical success. However, several recent graph transformers, such as GRIT, can incorporate edge features and encodings. RRWP, as proposed in the GRIT paper, builds on RWSE by incorporating non-diagonal terms and achieves both greater theoretical expressiveness and empirical performance improvements over RWSE. Although the paper shows that GRIT+MoSE outperforms GRIT+RRWP, a theoretical explanation (e.g., specific examples or proofs, similar to the RWSE discussion) would strengthen this claim. For instance, the authors could provide concrete graph examples where MoSE can distinguish structures that RRWP cannot, or prove that MoSE's homomorphism counts capture information beyond the pairwise relationships considered by RRWP. Additionally, a more detailed discussion on the circumstances under which node-level structural encodings remain competitive, despite the capacity of state-of-the-art GNNs to process edge features and encodings, would be beneficial. This discussion could delve into the limitations of message-passing mechanisms in capturing global structural information and how explicit encodings like MoSE might mitigate these limitations.
2. MoSE's evaluation is based on two molecular datasets, ZINC and QM9. While these datasets are standard in GNN benchmarking, limiting evaluation to these two datasets might be too restrictive.
    - If the paper's primary aim is to propose an encoding specifically for molecular property prediction (as supported by Example 1, which is plausible), evaluation across additional molecular datasets, such as PCQM4M, Peptides-struct, Peptides-func, and AQSOL, could reinforce the validity of MoSE within this domain. Furthermore, clarifying this scope within the paper—by showing that the phenomena in Example 1 generalize across molecular property tasks—would align well with the empirical objectives. My overall rating assumes this as the paper’s main focus.
    - Conversely, if the goal is to propose a general-purpose graph encoding, then broader evaluation across datasets from other domains is necessary. Evaluating MoSE beyond molecular property datasets would better support a general claim. In this case, datasets from GNN Benchmark Datasets beyond ZINC can help validate MoSE's general applicability. For example, testing on datasets like CIFAR10 or MNIST could demonstrate MoSE's effectiveness in capturing structural information relevant to image data.

### Questions
What are the time and space complexities for computing MoSE encodings? How does the empirical preprocessing time compare to RWSE, RRWP, and LapPE?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the topic of positional/structural encodings for graph learning which are typically influential in Graph Transformers since these incorporate the graph inductive biases coming from the adjacency matrix as its often not directly used during the self attention computation. The paper investigates the expressivity of one of such encodings, the random walk based structural encoding (RWSE), and address their shortcomings by proposing a homomorphism count based structural encoding called MoSE, which are claimed powerful than the RWSE. The content of the paper presents the characteristics brought by MoSE, also using example illustrations where RWSE may fail, and demonstrates in details their performance advantages on molecular datasets as well as one synthetic dataset of random graphs.

### Strengths
- the paper is a beautiful read on the limitations of existing RW structural encoding for graph transformers, and how the proposed homomorphism count based SE can address it.
- although the paper does not present a sophisticated new model, the presented SE is carefully studied, and experiments show the advantage (although marginal) brought by MoSE over existing methods in GTs.
- the comparison section of RWSE and MoSE is insightful and shows RWSE is strictly weaker than MoSE, which is reflected in the experimental results, as well as one of the ZINC illustrations.
- the proposed structural encoding has no limitations of LapPE such as sign ambiguity

### Weaknesses
 - although the MoSE is useful as studied, a concerning factor is of the computational complexity of getting the vectors. how does this compare experimentally?
- the utility of the propose structural encoding may be limited to addressing specific failure cases of prior SEs as indicated by the minor changes in experimental numbers.

### Questions
included with weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a novel positional encoding (PE) for graph transformers based on homomorphism counts and explains it's expressivity in terms of k-WL and the comparison to the random-walk positional encoding. The model is evaluated with two different graph transformers as base models and, over molecule and synthetic data, it shows some improvements.

### Strengths
- The research topic makes sense given the recent insights of using homomorphisms in MPNNs.
- The paper is well-structured
- The synthetic data experiment is interesting, and the authors consider two different transformers as base models
- The model seems to achieve good improvements generally (the number of evidence seems a bit low)

### Weaknesses
 - The paper is sometimes annoying to read:
     - The reader is assumed to know quite some details (e.g., 
W/o knowing the details of RWSE, you don't get the introductory example; the tables mention models like GSN and CIN, which are never explained; oblivious k-WL; l.232 how does GRIT deviate from this? What is Spasm(C7∪C8)?)
     - The expressivity analysis is interesting but it would have been nice if the papers would have provided some ideas about the proofs, to better get to know the nature of the PE.

- With all the molecular datasets considered, it would have been nice if the evaluation contained some baseline from the chemistry domain, to see how the model compares in realistic settings.
- Regarding the QM9 experiment, I am computer scientist myself and cannot entirely judge the validity, but wanted to point out that some chemists have strong doubts about this kind of experiment:
"While I appreciate that some claim a 1D representation like SMILES can capture some component of a 3D structure, predicting a property of one molecular conformation from a SMILES doesn’t make much sense. "
https://practicalcheminformatics.blogspot.com/2023/08/we-need-better-benchmarks-for-machine.html

- Beyond that, there's only Zinc12k, which is a bit of a low number of datasets for evaluation

Smaller comments:
- typo: alternative olibious k-WL
- l. 296 "f a graph in G." Is this \mathcal{G} ?
- FYI There's a recent related work: Deep Homomorphism Networks
https://neurips.cc/virtual/2024/poster/95659

### Questions
Maybe the authors can point out why they evaluate on only these datasets.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Graph Transformers apply self-attention on graph nodes and to capture the graph structure, they use positional or structural encodings. This paper proposes to use homomorphism count vectors as the employed structural encoding. The authors show that homomorphism counts are more expressive than the commonly used random walk structural encoding. The proposed encoding is evaluated on two molecular property prediction datasets (ZINC-12k and QM9), and also on a synthetic dataset. The results demonstrate that the proposed encoding outperforms other well-known positional and structural encodings across a range of architectures.

### Strengths
- The proposed structural encoding seems to better capture the graph structure than other enocodings since it outperforms the baseline encodings (including the commonly used random walk structural encoding) on all considered datasets.

- Besides the empirical results, the paper makes a substantial theoretical contribution since it is shown that the proposed encoding is strictly more expressive than the random walk structural encoding.

- The paper is dense in some parts, but overall it is very well-written and the presentation is clear.

### Weaknesses
 - Even though the proposed encoding outperforms the random walk structural encoding, the reported results are not very convincing. On most datasets, the difference in performance between the random walk structural encoding and the proposed encoding is very small. On QM9, the random walk structural encoding even outperforms the proposed encoding for some targets. It is thus unclear whether there is indeed a need for a new encoding in this setting since it does not lead to significance performance gains over the existing method.

- The complexity of computing the proposed encoding is not discussed in the paper, but I would expect that the time required to compute this encoding is significantly higher than the one required to compute the random walk structural encoding. In my understanding, the running time depends on the pattern graph family $\mathcal{G}$. I would thus suggest the authors report in the paper the pre-processing time for each one of the considered encodings. If the additional computational cost is high and given the marginal performance improvements it offers, why one would choose the proposed encoding over other encodings?

- One of my main concerns with this paper is regarding the novelty of the work. Clearly this is not the first paper to use homomorphism counts in the field of graph machine learning. Several previous works which are discussed in section 2 in the paper have annotated nodes with homomorphism counts. The main difference between those works and this paper is that the learning models employed in this paper are Graph Transformers and not MPNNs. However, I doubt if this in enough for the paper to be considered novel.

- The authors choose to integrate the proposed encoding into Graph Transformers, but all the theoretical results presented in the paper hold for the encoding itself (no assumptions are made about the underlying model). Thus, Graph Transformers could be replaced with MPNNs, and all the results would still hold. I thus wonder why the authors chose to place that much focus of the paper on Graph Transformers.

### Questions
- The proposed method relies on a finite set of fixed pattern graphs. One needs to choose the types of considered pattern graphs and this usually requires some domain knowledge. In case such knowledge is not available, what kind of patterns should be chosen?

### Soundness
4

### Presentation
3

### Contribution
3
