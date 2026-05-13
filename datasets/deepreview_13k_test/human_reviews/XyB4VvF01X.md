# Graph2Tac: Learning hierarchical representations of math concepts in theorem proving

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
Concepts abound in mathematics and its applications.
    They vary greatly between subject areas,
    and new ones are introduced in each mathematical paper or application.
    A formal theory builds a hierarchy of definitions, theorems and proofs
    that reference each other.
    When an AI agent is proving a new theorem,
    most of the mathematical concepts and lemmas relevant to that theorem may have never been seen during training.
    This is especially true in the Coq proof assistant, which has a diverse library of Coq projects,
    each with its own definitions, lemmas, and even custom tactic procedures used to prove those lemmas.
    It is essential for agents to incorporate such new information into their knowledge base on the fly.
    We work towards this goal by utilizing a new, large-scale, graph-based dataset for machine learning in Coq.
    We leverage a faithful graph-representation of Coq terms that
    induces a directed graph of dependencies between definitions
    to create a novel graph neural network, Graph2Tac (G2T),
    that takes into account not only the current goal,
    but also the entire hierarchy of definitions that led to the current goal.
    G2T is an online model that is deeply integrated into the users' workflow and can adapt in real time to new Coq projects and their definitions.
    It complements well with other online models that learn in real time from new proof scripts.
    Our novel definition embedding task, which is trained to compute representations of mathematical concepts not seen during training,
    boosts the performance of the neural network to rival
    state-of-the-art k-nearest neighbor predictors.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes Graph2Tac, a novel neural-based theorem proving method that can better understand the new definitions defined in the test packages. Besides generating the next proof steps, Graph2Tac is also optimized to generate the embeddings of definitions so that for this definition the predicted embeddings are similar to the learned embeddings. This new training objective equip Graph2Tac the ability to embed the new definitions not seen during training. Graph2Tac is compared with baselines on a collection of Coq packages that are not presented during training. Compared to the Graph2Tac model trained for predicting the next steps only, the new definition prediction training could improve the performance on test set from 17.4% to 26.1%. Combined with a KNN baseline, Graph2Tac+KNN achieve the new start of the art results on the test benchmark.

### Strengths
1 Define new concepts/theorems/methods is a fundamental feature of mathematics. This paper captures this key feature and works on an important and interesting online theorem proving settings where the theorem to prove contain unseen definitions presented in training. 
2 The proposed method is technically sound. By learning to predict the definition embeddings, the model could embed the novel definitions during inference. The design of GNN architecture is also reasonable.
3 Experiments demonstrate the benefits of training to generate definition embeddings.

### Weaknesses
Figure 4 is hard to follow for a new reader. It may help to remove some less important steps and intermediate results to make the figure more clear and helpful.

### Questions
1 It is interesting to see if training to predict definition embeddings could be helpful to in general. Like for the test theorems without unseen definitions, or a Coq package that is largely covered by the training data, could the new training loss improve the results?
2 As mentioned in the paper, this new training objective utilize the hierarchical structure of definitions. It is interesting to see if the learning definition embeddings contain any implicit structures compared to training to generate the next steps only. For example, try to plot the definition embeddings using t-sne.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes Graph2Tac, a graph neural network-based approach to automating interactive theorem proving, particularly targeting the Coq proof assistant. Graph2Tac constructs a graph representing objects (e.g., local hypotheses) relevant to a proof goal in the Coq environment as well as global definitions. Four types of embeddings will be learned for edge labels, node labels, base tactics, and definitions in the training dataset, respectively.  The dataset is a set of Coq packages extracted from the Opam package manager, which consists of 520K definitions and 4.6 million proof state transformations. Graph2Tac communicates with the Coq theorem prover via _synth_ tactic and _Suggest_ command. The experimental evaluation shows that Graph2Tac achieves comparable performance with the classic k-NN-based machine learning approach and a combination of Graph2Tac and k-NN would outperform each individual approach.

### Strengths
In general, the contributions of the current work are more about tooling and data collection rather than technical novelties of either theorem proving or machine learning. I can see the following strengths of this work:

- The graph construction systematically considers various information including proof states in the Coq kernel, global definitions, local variables, and equal terms (which are crucial in proofs by construction).
- The collected dataset represents the real-world applications for certified software
- Like kNN-based approaches, the tight integration with Coq's Tactician framework as well as solid engineering work make Graph2Tac practical to run on a consumer-grade computer. 
- Multiple baselines have been used in experimental evaluation on a wide selection of ITP tasks.

### Weaknesses
The idea of using graph neural networks for automating interactive theorem proving is not new and the improvement is relatively minor, which is the main weakness of this work. More specifically,

- the general idea seems fairly incremental, however, on the other hand, the model architecture is quite complicated, which consists of GNN, several MLPs, argument RNNs, as well as bidirectional LSTM. It is difficult to see the effectiveness of different parts (e.g., are they all essential? Is GNN the most important component?)
- The title and abstract highlight learning hierarchical representations, however, there is no evidence supporting that hierarchy representations really make a big difference. 
- the improvement of Graph2Tac is not very significant, although combining Graph2Tac and k-NN by running them in parallel does give some interesting improvements, which is more like a simple engineering solution rather than a technical one.

### Questions
Can you elaborate a bit more on the objective of the definition task? Shouldn't it be a (separate) pre-training task for learning good representations? 

Having an embedding for each definition might be too expensive. What is the size of the embedding table for definitions? 

Premise selection is one important step for theorem proving, which is not discussed in this work. How to guarantee that all relevant theorems/lemmas are properly included when constructing the graph representation?

### Soundness
2 fair

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
Authors propose a novel method for automated theorem proving in Coq.

They utilize graph neural networks (GNN) to construct a hierarchical representation of Coq theorems and definitions.
They support utilizing the same GNN at inference stage, on previously unseen Coq theorems and definitions.
Embeddings their GNN model constructs aids in theorem proving.

They evaluate their technique and show that in combination with the k-NN method it achieves superior results given a limited time frame of 10 minutes.

### Strengths
- Well written
- Clear motivation
- Involved technique. Architecture authors constructed is complex and involves many steps.
- Authors plan to open source the technique, including both code and dataset.

### Weaknesses
- Evaluation. 
    - It is unclear that proposed technique is superior to others. E.g., in Figure 7, most of the times k-NN performs better.
    - Authors show that their technique in combination with k-NN is superior to others. But, what if we combine some other technique with k-NN?

### Questions
- I am curious to see, given a large time limit (say 24 hours), what is the distribution of theorems solved by different systems?
- Have you noticed some patterns in theorems solved by different systems? You show a Venn diagram and note that different systems solve significantly different sets of theorems.
- Can you show some visualization of embeddings produced by your GNNs? Are there some interesting relations, groups, etc, in the embedding space?
- Can you run your tool on CoqGym, or is it not compatible?
- Typos and minor comments
    - page 1: "are able make" -> "are able to make"
    - page 2: "can not" -> "cannot" (cannot is more common)
    - page 2: "run a on" -> "run on a"
    - Figure 5: Please make the plot clearer, so one can easily distinguish which line corresponds to which setting.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a graph based approach for theorem proving with Coq. To do so, the authors propose to extract graph representations from existing Coq packages, and train a GNN that learns the meaning of definitions and other math symbols, namely G2T. The authors also enable G2T to incorporate unseen definitions by predicting their embeddings on the fly. The proposed method is evaluated on the separate Coq dataset, where it performs similarly to (sometime slightly better than) k-NN method.

### Strengths
This work proposes to represent existing Coq proofs into graph and proposes a new GNN+RNN model to learn the graphs---This approach is interesting and seems novel to me, though I'm not familiar with the literature to be certain that no similar works were proposed before.

The overall methodology proposed in this work seems sound to me, though I'm not able to fully inspect the details due to lack of expertise in Coq and presentation issues (see weakness).

### Weaknesses
Despite being a highly sophisticated model, Fig 5 suggests that G2T does not perform better than simple baselines such as k-NN:
- K-NN outperforms all pure G2T variants in terms of pass rate/sec for the most part, as the author pointed out, maybe for more complicated task G2T will have advantage, but it is not sufficiently demonstrated in the experiments.
- The only method outperforms k-NN is the hybrid one G2T+k-NN, which really cannot prove that G2T is a superior method as it is difficult to tell the contribution apart.
 
That said, I find the empirical significance of this work to be minor.
 
Other than that, the dataset created from the Coq package seems to be a good addition to the literature but there lacks too many details on how the dataset is created and processed, and further comparison to other datasets are needed for readers to assess its novelty and properly position it in the literature.

### Questions
My main concern with the method is the online addition of definition embeddings. It is unclear to me how unknown definition is encoded and predicted without a text encoder. Judging from 3.1, definition nodes that are seen in the training set all get assigned with an embedding, then if an unseen definition comes, supposedly there is no embedding in the table that matches this definition, then how does one encode it into an embedding in the first place? Furthermore, it seems to me the definition task is essential for learning to represent unknown definitions, then for the G2T-NoDef model, how is unseen definition handled if there was not a definition task?

As a reader not familiar with Coq syntax, I find some technical parts very difficult to follow
 
It is Difficult to comprehend the diagrams in Fig 2, 3 and 4:
- For example, While the caption says Fig 2 is the graph representation of Fig 1, it is difficult to see the connections: what do "@" do "up_arrow" correspond to? What does different color mean in the graph? How is online update reflected in the graph representation? Why are there triangles with no symbols?
 
3.1 misses formal definitions of many important components making it difficult to track the architecture. For example:
- The RNN for local and global argument prediction
- The loss for definition and prediction task
- The formal representation of how new definitions are added to the current state, and how are they calculated into an embedding using the definition task.
- Fig 4 is not very helpful either---notations and names do not match very well with the text: what is "const embs"? are they trainable node labels? Which part corresponds to edge embeddings? Which parts correspond to "entry-point" nodes and "local context" nodes?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
