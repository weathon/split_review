# The Snowflake Hypothesis: Training Deep GNN with One Node One Receptive field

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
\vspace{-0.6em}
Despite Graph Neural Networks (GNNs) demonstrating considerable promise in graph representation learning tasks, GNNs predominantly face significant issues with over-fitting and over-smoothing as they go deeper as models of computer vision (CV) realm. Given that the potency of numerous CV and language models is attributable to that support reliably training very deep architectures, we conduct a systematic study of deeper GNN research trajectories. Our findings indicate that the current success of deep GNNs primarily stems from (I) the adoption of innovations from CNNs, such as residual/skip connections, or (II) the tailor-made aggregation algorithms like DropEdge. However, these algorithms often lack intrinsic interpretability and indiscriminately treat all nodes within a given layer in a similar manner, thereby failing to capture the nuanced differences among various nodes. In this paper, we introduce \textit{the Snowflake Hypothesis} -- a novel paradigm underpinning the concept of ``one node, one receptive field''. The hypothesis draws inspiration from the unique and individualistic patterns of each snowflake, proposing a corresponding uniqueness in the receptive fields of nodes in the GNNs.

We employ the simplest gradient and node-level cosine distance as guiding principles to regulate the aggregation depth for each node, and conduct comprehensive experiments including: (1) different training scheme; (2) various shallow and deep GNN backbones, especially on deep frameworks such as JKNet, ResGCN, PairNorm \textit{etc.} (3) various numbers of layers (8, 16, 32, 64) on multiple benchmarks (six graphs including dense graphs with millions of nodes); (4) compare with different aggregation strategies. The observational results demonstrate that our framework can serve as a universal operator for a range of tasks, and it displays tremendous potential on deep GNNs.  It can be applied to various GNN frameworks, enhancing its effectiveness when operating in-depth, and guiding the selection of the optimal network depth in an explainable and generalizable way.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents the "Snowflake Hypothesis" for Graph Neural Networks (GNNs) to address overfitting and oversmoothing by assigning unique receptive fields to nodes. This hypothesis is operationalized using edge pruning (via gradient and node-level distance metrics) in order to modify the receptive field / aggregation strategy for each node. The experiments show that this can be flexibly applied with different training schemes and deep GNN backbones on large-scale benchmarks.

### Strengths
- Tackles important problem (mitigates oversmoothing in GNNs)
- The second version of the proposed method (SnoHv2) is scale to large-scale graphs
- Extensive empirical analysis: different training schemes, datasets, GNN backbones. Results suggest that SnoHv{1,2} improve performance. This supports the hypothesis that for a subset of nodes, early stopping is necessary to mitigate oversmoothing, especially as depth increases.

### Weaknesses
The paper is solid, but currently has a lot of stylistic issues. For example, the text contains many filler-sentences ("We have another interesting observation") and hyperlatives ("These astonishing results clearly verify the effectiveness of our algorithm.").  Please go over the text, and keep in mind that good writing should have active voice, be **clear** and **concise**. There is no need to write "we meticulously conduct a multitude of experiments to validate our hypothesis..."  when one could just write "we validate our hypothesis...". This will make the text easier to read. The goal should be to convey your findings, not to convince the reviewers how awesome you are. 

I'd also suggest going over the abstract: it's the most important piece of the text, and it's probably the *only* piece of your work most people will read. The current abstract contains many awkward sentences (what does "Given that the potency of numerous CV and language models is attributable to that support reliably training very deep architectures" even mean?). If available, try to work with someone who has experience in editing text and making it more readable. I think your work is overall interesting, it deserves a good, clean packaging.

I would also strongly suggest to remove the "red numbers" in Table 1, and instead add variances: The relevant part is what the average performance over 5 runs is, plus how much variance there will be between runs. The "best result out of N runs" is not valuable information, it's random-seed-lottery.

### Questions
None, please see weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new training paradigm for Graph Neural Networks (GNNs): they use a masked adjacency matrix to prune the graph structure.
They evaluate on several models and datasets

### Strengths
Originality: as far as I can judge, this is a novel application.
Quality: empirical validation is thorough, and the results appear convincing.
Clarity: while there were some stilistic issue (see Weaknesses), the underlying thoughts were mostly clear. I was able to follow the exposition without much trouble.
Significance: given the solid results, I think this paper is relevant for the GNN community

### Weaknesses
1. The motivation is unclear.
2. overclaim, SnoH does not always improve deepGNN's performance.
3. The GNN backbone is far from STOA, both on Ogbn-Proteins and Ogbn-arxiv dataset.

### Questions
What is the running time (wall clock, FLOPS) of your method vs the baselines?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose SnoH, which use different receptive fields for node aggregation operation in GNN.

However, I am unconvinced that the proposed method offers significant advantages for graph learning tasks. While this method aims to boost deepGNN's performance, the enhancement seems marignal and is considerably distant from the state of the art. Additionally, the SnoH's performance on Ogbn-Arxiv appears random, which contradicts the assertion in the abstract that it "serves as a universal operator for a range of tasks and shows considerable potential with deep GNNs."

### Strengths
1. marginally improve deepGNN's performance.
2. evaluate the model on a range of dataset.

### Weaknesses
1. The motivation is unclear.
2. overclaim, SnoH does not always improve deepGNN's performance.
3. The GNN backbone is far from STOA, both on Ogbn-Proteins and Ogbn-arxiv dataset.

### Questions
1. The motivation is unclear, why enhance deepGNN? many GNN use 2 or 3 layers but still achieve good performance. For example, [1] use 3 layers and achieve 73\% on ogbn-arxiv, higher than the model's performance.

2. In Table 4, performance drops after using SnoHv1, so SnoHv1 is not always helpful for deepGNN.

3. Is SnoH only limited to the GNN proposed here or it also enhance other models' performance,  I would suggest evaluating SnoH on GNN  models that have demonstrated strong performance on Ogbn-Proteins and Ogbn-arxiv.


[1] Huang, Qian, et al. "Combining label propagation and simple models out-performs graph neural networks." arXiv preprint arXiv:2010.13993 (2020).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript "The Snowflake Hypothesis: Training Deep GNN with One Node One Receptive Field"
introduces an innovative approach, termed the Snowflake Hypothesis (SnoH), for training deep Graph
Neural Networks. This hypothesis advocates for the uniqueness of the receptive field for each node in the
graph. The authors propose a method that utilizes gradient and node-level cosine distance as metrics to
regulate the aggregation depth for each node. This approach, which can be likened to an "early stopping"
mechanism at the node level through edge pruning, has shown effectiveness across a variety of backbone
networks, offering enhanced generalizability and interpretability.

### Strengths
1. The paper is well-writtened, ensuring ease of comprehension. It offers a fresh perspective on tackling
the over-smoothing issue in GNN training through the early stopping method under the proposed
Snowflake Hypothesis.
2. The proposed method is not only simple and effective but also exhibits compatibility with diverse
backbone networks and training strategies. This adaptability encourages broader adoption and
potential future extensions.
3. The authors have conducted extensive experiments, encompassing different training schemes, a
variety of GNN backbones on diverse scale benchmarks. The results demonstrate that the framework
can serve as a universal operator for a range of tasks

### Weaknesses
1. The methodology is heavily reliant on the adjacency matrix, which confines its applicability to
message-passing based backbone networks, whose discriminative ability is limited by the 1-Weisfeiler-
Lehman Isomorphism Test. The manuscript does not offer a viable method for extending its
application to subgraph-based and multihop networks.
2. Despite claims of broad applicability, the results presented in Table 1 primarily focus on deep GNN
models, while regular network like GCN sexhibiting notable performance decline as the number of
layers increases. This observation brings into question the framework's generalizability across
different backbone networks.
3. The manuscript lacks an in-depth analysis of the impact of the parameter on the training process of
various models. Furthermore, it does not provide guidelines for setting in accordance with the
specific characteristics like the of the model and dataset.

### Questions
1. The paper choose cosine distance as a metric to determine when the node updation should stop. Why
was this method chosen, given its potential introduction of homogeneity assumptions, and could this
lead to a decline in performance in heterophily networks?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
