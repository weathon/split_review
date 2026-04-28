# Link Prediction with Untrained Message Passing Layers

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Message passing neural networks (MPNNs) operate on graphs by exchanging information between neigbouring nodes. 
MPNNs have been successfully applied to various node-, edge-, and graph-level tasks in areas like molecular science, computer vision, natural language processing, and combinatorial optimization. However, most MPNNs require training on large amounts of labeled data, which can be costly and time-consuming. 
In this work, we explore the use of various untrained message passing layers in graph neural networks, i.e. variants of popular message passing architecture where we remove all trainable parameters that are used to transform node features in the message passing step.
Focusing on link prediction, we find that untrained message passing layers can lead to competitive and even superior performance compared to fully trained MPNNs, especially in the presence of high-dimensional features. 
We provide a theoretical analysis of untrained message passing by relating the inner products of features implicitly produced by untrained message passing layers to path-based topological node similarity measures. 
As such, untrained message passing architectures can be viewed as a highly efficient and interpretable approach to link prediction.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work explores the use of untrained message passing layers in GNN for link prediction tasks. The authors showed that, experimentally, untrained message passing layers provides competitive performance when compared against fully trained layers for link prediction. The authors also provided a simple theoretical analysis to justify their claims.

### Strengths
Using untrained message passing layers for GNN can be a computationally efficient approach, which is an important topic in the community.

### Weaknesses
Weakness:

Overall, the presented work gives the impression of an early draft, and I find it challenging to fully assess its contributions in its current form. Below are some clear issues:

1. The presented “theoretical results” are poorly organized, and it is very challenging to judge its correctness given there is no clear distinction between the authors’ contributions and existing results. To be honest, I am not very sure what is the theoretical contributions provided by the authors. The results rely on oversimplified assumptions (e.g., orthonormality line 304); and the authors were linking random things together (e.g., PageRank line 348). It is very challenging for me to decipher what the authors what to convey here.

2. It does not seem like the experimental results support the authors’ claim. In many cases, the untrained variant of the network performs very poorly, especially in Hits@100 dataset. If the authors want to claim the simplified network performs very well, the paper should be written as such.

3. Lack of ablation experiments, intuitive results on synthetic datasets, or example results/visualizations on representative datasets.

4. The presented figure 1 is of low quality. Maybe at least show the standard deviation across different runs?

### Questions
NA

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes untrained and linear message passing layers for graph neural networks for the task of link prediction. Theoretical analysis relates the values computed at the intermediate layers to path-based and random walk based connectivity measures. An assumption is made regarding the orthogonality of the initial node features. Experimentally, the method is shown to be comparable to trained and non-linear layers in a GNN.

### Strengths
The paper is written well and the presentation is good.

The analysis of the inter layer values to path-based measures is nice, though not unexpected.

Experimental results have been carried out on the usual link prediction benchmarks.

### Weaknesses
The idea of untrained and linear layers (as acknowledged by the authors) has previously appeared for node classification in Wu et al, ICML 2019. So, the idea has limited novelty.

The assumption of orthogonality may not always hold especially under conditions of homophily where neighboring nodes have similar features. This is a significant limitation as many real-world networks exhibit homophily, and the theoretical analysis relies heavily on this assumption. The paper does not adequately address the implications of this assumption being violated, particularly in the context of the observed performance gains.

Link prediction has been studied in many works and the impact of another paper is limited.

### Questions
Can you comment on why orthogonality would be expected in homophilic networks?

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
4

### Summary
The paper investigates the use of untrained message-passing layers for link prediction tasks. Both a completely untrained model and a model with a trainable layer after the message passing layers are compared to standard trained message-passing layers. The authors provide theoretical observations to support their empirical analysis.

### Strengths
* To the best of my knowledge, this is the first application of untrained message-passing layers to link prediction.
* The empirical results show that untrained layers perform reasonably well.
* Some theoretical observations are included to complement the empirical analysis.

### Weaknesses
 * Lack of novelty: Most of the work builds directly on top of Wu et al. and mirrors many parts of it. The architecture and setup are almost exactly the same, and even some claims, like the benefit of efficiency and interpretability, are taken straight from there. This is not to say that they are not true, but for example in the case of interpretability, there is not much evidence provided beyond the fact that the architecture is simpler. 

* The theoretical contribution in the paper feels somewhat limited, with unclear takeaways. Although the authors aim to support their work with theory, the analysis falls short of substantiating the core claims. For instance, the authors state that “Our theoretical analysis further provides insights into the effectiveness of widely used node initialization schemes such as one-hot encodings and random features.” However, as this theoretical analysis is restricted to feature vectors that are pairwise orthonormal - often true for one-hot encodings and random features - it doesn’t convincingly explain why these should be more effective than other potential initializations that lack this precondition. Additionally, this analysis seems somewhat peripheral to the main focus of the paper: comparing untrained and trained MPNNs. To strengthen this aspect, I suggest clearly outlining the theoretical contributions by structuring them into theorems with proofs and more directly linking them to the paper’s central claim.

* The main point of the paper is the fact that untrained message-passing layers perform very well in comparison to their trained counterparts. To evaluate this properly, a good benchmarking framework is necessary that guarantees that the difference in predictive performance is coming from what the authors claim it’s coming from, and especially that the comparison is fair. This is where I have my main problem with this paper. No established benchmarking framework is used, and almost no attention is paid to the fact that link prediction tasks are notoriously hard to evaluate. I would recommend the authors to consult recent works like [1] and [2], which go into more detail on various problems, but let me name some important ones here: Looking at the provided code, it looks like negative sampling of edges is done randomly, which is likely to cause bad performance on these tasks. This is problematic because it’s not clear if untrained layers really perform that well in comparison or if the training procedure was just not good. From Table 2, I can tell that in several cases, the final trained linear layer (which was also trained with random negative sampling) performs worse than the untrained one. This is really surprising to me and could be due to the negative samples that were not chosen well. While looking at the code, I also noticed that the test dataset for the untrained variants is not the same as for the trained ones because the random link split in the dataset transform is initialized with `num_val=0.00, num_test=0.1` in contrast to `num_val=0.05, num_test=0.1` for the trained counterpart. While I don’t expect this one to make a huge difference, it just goes to show that the benchmarking is not done thoroughly enough to warrant the claims made in the paper. Getting link prediction right is actually quite hard, considerably more so than for node and graph-level prediction tasks, and a paper that builds on top of these results that much should put more scrutiny into it. My proposal is this: Use an existing benchmarking framework. This also makes it possible to compare the results to other papers and to run with more recent datasets from ogb, which are completely missing from this analysis. On a side note, I think that these would be quite important as they are bigger and could demonstrate the claimed scalability advantage of untrained layers.

### Questions
* While running the code I noticed that the inference for the untrained layers uses considerably more memory than even training the full GNN. So much so that I ran out of memory on my laptop. I’m wondering, could your code actually be used for much larger graphs?
* The meaning of this sentence was a bit unclear to me: “ Since the simplified architectures consist of UTMP layers followed by a trainable linear layer, the consideration of UT models which do not include the linear layer also covers all possible ablation studies” Could you clarify?
* Some other suggestions for improvements were already described together with the weaknesses. 

In light of the weaknesses I mentioned, I tend towards a reject. Especially the empirical analysis has to be improved considerably.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper explores the use of untrained message-passing layers (UTMP) for link prediction tasks in graph neural networks (GNNs). The authors propose simplifying GNN architectures by removing trainable parameters and nonlinear components, resulting in interpretable and computationally efficient models. Their research finds that these simplified architectures can often outperform or match the performance of fully trained GNNs in link prediction tasks.

### Strengths
1. The paper introduces untrained message-passing architectures, extending existing research from node classification to link prediction. This perspective is relatively novel and addresses the computational limitations of GNNs. The untrained models, by eliminating learnable parameters, are shown to be faster and more resource-efficient, making them suitable for large-scale applications.


2. Theoretical results provide a deeper understanding of how UTMP layers approximate traditional path-based link prediction metrics (e.g., random walks and common neighbors), making the models highly interpretable.

### Weaknesses
1. Limited baselines are compared. Path-based methods and edge-wise methods should be compared. This doesn't mean the authors should change them into untrained models and do comparison. The author discuss the theoretical relationship with path-based methods, so the emperical comparison is needed to validate the theory.

2. Limited datasets are included. Large datasets like OGB datasets are not included so the application is limited. 

3. For non-attributed graphs the results of original GNNs are much better than on the attributed graphs, compared to S-models and UT-models. Can the authors do some ablations to discuss this observation? Maybe it's because of the one-hot encoding? Can the authors show the results of one-hot encoding in attributed graphs?

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2
