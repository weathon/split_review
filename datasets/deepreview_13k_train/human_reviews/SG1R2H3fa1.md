# Revisiting Random Walks for Learning on Graphs

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
We revisit a simple idea for machine learning on graphs, where a random walk on a graph produces a machine-readable record, and this record is processed by a deep neural network to directly make vertex-level or graph-level predictions.
    We refer to these stochastic machines as \textbf{random walk neural networks}, and show that we can design them to be isomorphism invariant while capable of universal approximation of graph functions in probability.
    A useful finding is that almost any kind of record of random walk guarantees probabilistic invariance as long as the vertices are anonymized.
    This enables us to record random walks in plain text and adopt a language model to read these text records to solve graph tasks.
    We further establish a parallelism to message passing neural networks using tools from Markov chain theory, and show that over-smoothing in message passing is alleviated by construction in random walk neural networks, while over-squashing manifests as probabilistic under-reaching.
    We show that random walk neural networks based on pre-trained language models can solve several hard problems on graphs, such as separating strongly regular graphs where the 3-WL test fails, counting substructures, and transductive classification on arXiv citation network without training.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper considers random-walk based techniques for graph learning. It introduces a framework splitting the random walk function, recording function (drawing features from the graph), and reader NN (actually processing those features). They then show that for invariance one needs to have it on the first two levels but not the third. In terms of expressiveness, everything that is sufficiently powerful suffices, which is again made formal. Also on the theoretical side, over-smoothing does not happen for RW-based methods. 

On the practical side, the paper combines efficient non-backtracking walks while always recording the neighborhood, outputting the result as a string which is then fed into an LLM. This architecture works very well for oversmoothing, over-squashing, isomorphism learning and node classification.

### Strengths
The whole part about random walk strategies and cover times is novel and interesting. The suggested method of compiling the walk information (including anonymization and neighborhood information) into a string to be fed into an LLM is also new, even though building upon exisitng work (this could be more explicit when describing the model).

The theoretical results seem sound too.

### Weaknesses
A lot of the theory has been implicitly used e.g. in CraWl, e.g. by using 1D CNNs as reader NN. Also the anonymization and neighborhood recording is already done there (with the difference that it outputs a matrix instead of a string). Also there is quite a bit of literature on anonymization and e.g. that anonymization alone is enough to recover the graph which I would have expected to be discussed in that context.

The expressive power section is quite lengthy while not saying much - by now we should all know that there are universal function approximators so if no information is lost during preprocessing (message passing or random walks), any such model is universal. While writing down the exact details on what it means to be universal/expressive, I consider most of section 3.1 entirely unsurprising and somewhat trivial. The formal treatment of universality, while technically sound, does not offer significant new insights given the established understanding of universal function approximators and lossless preprocessing.

There should definitely be more experiments. Currently the experiments cover two types of toy datasets and one real-world one. Graph classification that the main competitor Crawl exclusively covers is left out in the real-world setting which is odd and I believe should be added. Also having more than one node-classification dataset would be nice.

Code is unavailable. This makes reproducing the results a lot harder (even though the description of walks and feature extraction is detailed, the exact use of the LLM and the finetuning procedures are not well-enough described to confidently repeat the experiments).

Details: 
- Grammar/Structure in 87ff is off. especially: "given that..." and "The result also..."
- Table 3/4: maybe just put the link to the reference on the method name to avoid the cluttered look of the table.

### Questions
Is there a simple intuitive reason why RWNN also outputs something based on the stationary vector in Thm 3.5?

would it be possible to include Crawl and WalkLM in Table2? As those seem to be the only two methods to compare to..

I would be very interested in graph learning performance, especially since Crawl was surprisingly good there.

Would it be possible to include SimTeG methods in Table 4? They also combine LLM and GNN, just in the opposite order. I also believe that using SimTeG features would further improve your results and make them actually SOTA. Currently the table is misleading.

Is there anything to say about cases where walks do not cover the whole graph?

### Soundness
3

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
The paper revisits the usage of random walks for learning on graphs. In particular, they consider the setting where the model consists of three components: a random walk algorithm, a recording function producing a machine-readable record of the random walk, and a reader neural network that processes the record and produces an output. The authors show that probabilistic invariance can be achieved by requiring invariance conditions on the random walk algorithm and the recording function. They also show connections with over-smoothing and over-squashing.

### Strengths
The problem is interesting, and using llms to process outputs from the recording function makes the results more practical and significant.

### Weaknesses
The readability of the paper can be improved. The paper is quite dense and has many theoretical results, while the experiments appear only at the end. Perhaps move the corresponding experiments closer to the relative sections would improve readability.

Generally speaking, I find it confusing that the authors emphasize the invariance of the random walk algorithm, while instead this is a probabilistic invariance, that is, an invariance of the distribution. While the authors discuss that they accept the probabilistic notion of invariance (eq. 2), they sometimes only refer to it as invariance (eq. 3). I think this point should be better clarified throughout the paper. Moreover, since it is well known that one can average over all random walks to obtain the invariance of permutations (Srinivasan and Ribeiro, 2020), I encourage the authors to connect the probabilistic invariance to the notion of invariance more commonly used in graph learning.

### Questions
1. Can you include results on real-world graph-level datasets? I think only evaluating graph-level synthetic datasets is a bit restrictive.

2. What is the impact of voting in the node-level task? I think the fact that you need to average across multiple voters reflects the difference between invariance and probabilistic invariance.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces RWNNs as a unified framework of graph learning approaches that sample random walks from an input graph and then process a suitable representation of those walks with a reader neural network. This general concept covers a range of recent approaches.

The work provides a theoretical analysis of sufficient conditions on the walks and walk records that ensure permutation invariance regardless of the choice of the reader architecture. The paper further proves that RWNNs are probabilistically universal if the random walks are sufficiently likely to cover a graph and that RWNNs inherently avoid the phenomenon of over-smoothing.

An empirical study further studies how RWNNs with transformer-based reader functions perform on various tasks. Here, a training-free approach that passes a text-based walk representation to a Llama model is explored to solve classification tasks in citation networks with in-context learning. The overall performance of this method is reported to be competitive.

### Strengths
* The work provides multiple novel theoretical insights on random-walk-based GNNs and a general framework for modeling and studying such approaches further.
* Applying pre-trained language models to text-based representations of random walks to perform in-context learning is a novel idea, and the presented results seem promising.

### Weaknesses
While I think the theoretical contributions are significant, I think the experiment section lacks some details that would improve the paper:

* What is the runtime of the compared methods during inference? While the RWNN-Llama model requires no training, I would expect its computational cost during inference to be substantially larger than that of a standard GNN. This by itself is not a problem as LLMs are expected to be costly, and RWNN also allows for more efficient choices for the reader model. However, this tradeoff should be discussed more clearly, and providing some runtime measurements would be very helpful to the reader.

* The cover time of different walk distributions is examined in section 5.1. However, no further comparison of different walks on the predictive tasks of 5.2 or 5.3 is performed. It is therefore not clear whether or not the difference in cover time translates to a significant difference in downstream tasks in practice. Specifically, it's unclear if the observed differences in cover time are practically meaningful for the tasks considered, or if other factors dominate performance.

*  The main walk hyperparameters (length and restart probability) are not specified in Sections 5.2 and 5.3. This makes it difficult to reproduce the results or to understand the sensitivity of the method to these parameters. The lack of specific values for these hyperparameters hinders a complete understanding of the experimental setup.

There are also some grammatical mistakes that would benefit from a spell checker.

### Questions
* What is the inference cost for RWNN-Llama in section 5.3? How does it compare to inductive GNN-based approaches?
* How are the results in section 5.2 and 5.3 affected by the choice of random walks? Would uniform random walks with or without backtracking yield significant performance differences on the downstream tasks? 
* What walk length and restart probabilities are used in sections 5.2 and 5.3?
* Why is a DeBERTa model that was pretrained on natural language used in the experiments for isomorphism learning? The used walk records do not resemble written language and it is not clear which information learned during language pretaining is useful here. Is there a significant benefit to using this model as opposed to a randomly initialized one?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper delivers a well-structured analysis, both theoretical and empirical, of the potential of random walk approaches as feature extractors for subsequent neural networks. The contribution is relevant both as a summary of previous random walk-based approaches and as a theoretical connection to the problems of oversmoothing, oversquashing, and underreaching. The paper first discusses the requirements for a random-walk feature extractor to be invariant to graph isomorphism, and later it shows that invariant random walks extractors can discriminate, in probability, any two graphs provided a sufficient length of the random walk is used. Random walks neural networks do not suffer from oversmoothing and the oversquashing is intimately related to probabilistic under-reaching (whereas in MPNNs one knows exactly how many steps are needed to reach a node).

### Strengths
This is one, if not the most, beautiful papers I have reviewed, and as such it deserves one of the most positive reviews I have ever written. The scope is well defined, the presentation is excellent and overall it is a pleasure to read. Coming from the GNN field, I found the connection of RWs and oversmoothing etc problems extremely fascinating. 

Intuitive ideas have been well formalized into theorems (most of which seem ok, although I did not check all proofs carefully due to time shortage), some of which (Th. 3.2 and 3.4) are especially important to convince the GNN expressiveness community that it might be time to move beyond the WL-test arguments. The integration of GNNs and RWs seems a promising research direction in the future and this paper inspired me to think about it.

The empirical results support all theoretical findings (Figure 3 might be improved) and show some strong performance on discriminating regular graphs. The transformer architecture, and especially self-attention, seems to me a particularly adequate architecture for the tasks of Table 2, but it would be interesting to see how a simple MLP performs on top of the random walk features.

The authors also took care of efficiently implementing the core of their method so as to speed up the computation of random walks.

### Weaknesses
These are mostly suggestions for improvement, as there are no particular concerns on this reviewer’s side. One suggestion for the authors is to discuss more explicitly the empirical tasks, such as the one of Table 2; what is the target to be predicted? It is not enough to mention the relevant paper in this case, and the reader might get lost. Also, more details about the empirical procedure, such as hyper-parameters tried and model-selection/risk-assessment procedures, might contribute to improve replicability of the experiments.

I would also suggest to define the meaning of the symbols =d (define precisely what  means equal in probability) and ~ (the isomorphism relation). The authors use them a lot in the paper and they should be properly defined.

Another point that would need clarification is to specify how one can deal with named neighborhoods outside of the textual representation of the record. The authors could clarify possible options and hopefully run a demonstrative example, with an MLP for instance, in place of a language model.

In terms of experiments, I believe the authors might be trying to position RWNN-Llama3 too positively with respect to the literature. It is well-known that GraphSAGE, one of the simplest GNNs, already achieves 77% test accuracy on the ogbn-arxiv leaderboard. A proper model-selection was enough to significantly improve the original scores of the paper. So, while the paper deserves acceptance, it would do a service to the community to highlight this fact.

- Line  34: the authors cannot make a general claim that all GNNs are less expressive than 1-WL. The statement should be probably massaged to consider this
- Line 53: should it be “Addressing such questions is important”?
- Table 1: the authors claim that in principle the Reader NN of RWNN can be any universal function. I believe this might be true for many other methods the authors listed in the table. In light of this, I would suggest that the authors maintain consistency and replace “Any universal” with “Language Model”, since they have not shown how to combine RW+Neighbor Information records with models different from language models
- Theorems 2.1, 2.2, 2.3 formalize rather intuitive concepts, and the proofs are mostly about stating the definition of invariance. Maybe the authors could “downgrade” them to Propositions to inform the reader that some results have more relevance than others?
- Lines 347-349: recent architectures such as [1] show that it is possible to modify the computation over the topology to control oversmoothing and oversquashing, and these two concepts are not as entangled to the original topology and related to each other anymore. Perhaps the authors would like to rephrase their statement in light of this? [1] Errica F., et al. "Adaptive Message Passing: A General Framework to Mitigate Oversmoothing, Oversquashing, and Underreaching." arXiv preprint arXiv:2312.16560 (2023).
- Figure 3: what are colors and lines? The authors should improve the figure a bit by adding a legend.

### Questions
These are mostly related to typos and requests for modification
  - Line  34: the authors cannot make a general claim that all GNNs are less expressive than 1-WL. The statement should be probably massaged to consider this
  - Line 53: should it be “Addressing such questions is important”?
  - Table 1: the authors claim that in principle the Reader NN of RWNN can be any universal function. I believe this might be true for many other methods the authors listed in the table. In light of this, I would suggest that the authors maintain consistency and replace “Any universal” with “Language Model”, since they have not shown how to combine RW+Neighbor Information records with models different from language models
  - Theorems 2.1, 2.2, 2.3 formalize rather intuitive concepts, and the proofs are mostly about stating the definition of invariance. Maybe the authors could “downgrade” them to Propositions to inform the reader that some results have more relevance than others?
  - Lines 347-349: recent architectures such as [1] show that it is possible to modify the computation over the topology to control oversmoothing and oversquashing, and these two concepts are not as entangled to the original topology and related to each other anymore. Perhaps the authors would like to rephrase their statement in light of this? [1] Errica F., et al. "Adaptive Message Passing: A General Framework to Mitigate Oversmoothing, Oversquashing, and Underreaching." arXiv preprint arXiv:2312.16560 (2023).
  - Figure 3: what are colors and lines? The authors should improve the figure a bit by adding a legend.

### Soundness
3

### Presentation
4

### Contribution
4
