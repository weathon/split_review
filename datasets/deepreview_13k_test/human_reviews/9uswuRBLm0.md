# Beyond Directed Acyclic Computation Graph with Cyclic Neural Network

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
This paper investigates a fundamental yet overlooked design principle of artificial neural networks (ANN): We do not need to build ANNs layer-by-layer sequentially to guarantee the Directed Acyclic Graph (DAG) property. Inspired by biological intelligence, where neurons form a complex, graph-structured network, we introduce the transformative Cyclic Neural Networks (Cyclic NN). It emulates biological neural systems' flexible and dynamic graph nature, allowing neuron connections in any graph-like structure, including cycles. This offers greater flexibility compared to the DAG structure of current ANNs. We further develop the Graph Over Multi-layer Perceptron, the first detailed model based on this new design paradigm. We experimentally validate the advantages of Cyclic NN on widely tested datasets in most generalized cases, demonstrating its superiority over current layer-by-layer DAG neural networks. With the support of Cyclic NN, the Forward-Forward training algorithm also firstly outperforms the current Back-Propagation algorithm. This research illustrates a transformative ANN design paradigm, a significant departure from current ANN designs, potentially leading to more biologically similar ANNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Cyclic Neural Networks (Cyclic NNs), a design paradigm that extends neural network computation beyond sequential, layer-by-layer connections. Inspired by the complex, cyclic connectivity observed in biological neural networks, the authors propose allowing neurons in ANNs to form connections in any graph-like structure, including cycles.

### Strengths
1.	The paper is well-presented with helpful visualization and a relatively clear description of the method and experiment. 
2.	Different shapes of computational graphs are experimented with cyclic NN, which provides insight into how it affects the performance of the model.

### Weaknesses
1.	The innovation of the paper is limited. Directed acyclic computation only applies to relatively simple feedforward neural networks. Alternative computational patterns such as recurrent and graph-shaped fall under their respective category (recurrent neural network and graph neural network). The resulting cyclic NN may be succinctly captured with a recurrent type of GNN. 
2.	The experimental results and comparisons are limited. The improvement of the approach is only supported in the case of a complete cyclic NN graph. The baseline comparison is limited to a feed-forward network.

### Questions
1.	Related to W1, How is GOMLP different from a recurrent graph neural network with the same computational pattern? 
2.	Since local learning is used to avoid training on recurrent connections globally, how is the training stability of the model under different graph configurations? 
3.	What’s the full asymptotic complexity of the model? In section 3.5., only those relevant to the shape of the graph is discussed.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new design of artificial neural networks. The novelty lies in the fact that they don't have a directed acyclic graph (DAG) structure. This is a fundamental innovation because the training of neural networks nowadays depends on the DAG structure so that the gradient of the global loss function can be computed. To support the new architecture, the authors follow the forward-forward algorithm proposed by Hinton (2022), where local losses are used to train individual neurons and the final classifier. The authors demonstrate experiment results, which for the first time suggest that forward-forward training can outperform standard back-propagation training.

### Strengths
- This paper proposes a ground-breaking, innovative idea to build neural networks.

- The idea is backed by attractive experiment results.

- The proposed neural network, Cyclic NN, is a step forward toward a drastically different paradigm of machine learning models that are more biologically sound.

### Weaknesses
Some technical details are unclear. See the following "Questions" section.

Additionally, it would be informative to experimentally compare the proposed architecture with GNNs due to their similarities. Every node in the GNN takes the same input feature and the GNN uses a readout layer similar to the readout in Cyclic NN. In this case, the main difference between a GNN and a Cylic NN is that the GNN uses the same $W$ matrix for every node in a layer and uses different $W$ matrices for different layers, while the Cyclic NN uses different $W$ matrices for different nodes. In this regard, GNN is more parameter efficient. Of course, the training method is fundamentally different. Which architecture performs better?

### Questions
The main question surrounds Eqn (4), which causes confusion when the reader tries to connect it with the inner while loop of Algorithm 1, Figure 2(b) as a special case, and the discussions about unrolling in Section 3.6.

In Eqn (4), the neuron input depends on the outputs of the adjacent neurons. When $t = 0$, the outputs of the adjacent neurons have not been unknown yet. So how is line 6 of Algorithm 1 computed?

Do the authors ignore the outputs of the adjacent neurons when $t = 0$?

If so, we further look into the for loop of Algorithm 1. This loop loops over the neurons $N$. For a later $N$, if it is adjacent to an earlier neuron (call it $N_1$), would the input of the later neuron use the output of the earlier neuron in the last round (before the for loop) or in the current round (inside the for loop)?

In either answer to the above question, it appears that every neuron has one parameter matrix $W$ (as opposed to a few). The inner while loop of Algorithm 1 updates this parameter $T$ times. Is this understanding correct?

If correct, then the $T$ steps of the inner while loop of Algorithm 1 do not propagate information across $T$ hops of the graph. Rather, information is propagated to at most one hop away, no matter how big is $T$. The inner while loop is more like running an optimization $T$ steps rather than propagating information in a $T$-layer GNN.

If the above understanding is correct, then the unrolling in Figure 3 does not make sense. Consider the two $\sigma(W_1)$ on the right of Figure 3. They are the same neuron at different training stages. The first $\sigma(W_1)$ takes the value obtained after line 8 of Algorithm 1, when $t=0$. The second $\sigma(W_1)$ takes the value at $t=1$. This is very different from unrolling an RNN, where the RNN cell uses the same parameter values at different times.

If the above understanding is correct, then the discussion of the expressive power in Section 3.6 is dubious, because the neural network does not have a depth $T$ like in a usual neural network.

Now get back to Eqn (4). The neuron input includes the input representation $h$. This does not seem to be the case in Figure 2(b). If one considers the architecture in Figure 2(b) a special case of Cyclic NN, then following the convention in Figure 2(c) and (d), the black arrows that chain the neurons should be red arrows instead. Moreover, the input should have a black arrow pointing to every neuron.

Do the authors really mean Figure 2(b) to be in the current form, or in the edited form elaborated above? For FF-Chain, do the authors mean the current Figure 2(b) or the edited form? What about BP-Chain and BP-Chain*?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a biologically plausible neural architecture referred to as the cyclic NN. The defining characteristics of the cyclic NN are: (1) each neuron is parametrised as a linear layer, i.e. N to M rather than N to 1 mapping, (2) each (computational) neuron is trained locally, using the forward-forward algorithm (backpropagation across layers does not take place), (3) neuronal information is accumulated by a parameterised “readout” layer to allow for downstream tasks such as classification. As a result of the proposed architecture, the connections can be cyclic - i.e., directed acyclic graph (DAG) structure typical of NNs is not enforced.

### Strengths
**Originality:** The paper proposes a graph structure over MLPs, which is simple yet effective. The proposed architecture elegantly elevates layer-based neural models to a structure that inherently includes both recurrency and ensembling. As such, a higher degree of biological plausibility is achieved.

**Quality and clarity:** The paper is concise and clear, with very minor typos and grammatical mistakes. The ideas are elegant and simple, with potentially significant impact on the field. The code is made available.

**Significance:** The shift from DAGs to recurrent architectures is imminent, as such the paper is quite timely. The significance is diminished by the fact that the authors do not acknowledge any of the work on recurrent neural networks in their study. If the proposed model can be properly contextualised, I would be willing to accept the proposed method as more significant.

### Weaknesses
The closest existing NN architecture that is not a DAG is a recurrent NN (RNN). Plethora of research exists on RNNs, yet the authors do not mention this paradigm in the paper. How are the cyclic NNs different from RNNs? A critical discussion of this point is necessary. Similarly, a more expressive neuron can be compared to a memory block of a long short-term memory (LSTM) network. How does the proposed computational neuron differ from a gated neuron? Section 3.6 discusses how the cycle can be unrolled and interpreted as an arbitrary depth - which is exactly the argument for the adoption of recurrent architectures. The similarity is quite striking and cannot be ignored.

The authors compare their proposed cyclic NNs to traditional DAG architectures. I think a comparison to other biologically plausible architectures would be more applicable, e.g. liquid neural networks. Where do the cyclic NNs fit in the context of existing biologically plausible NNs? Section 5.1 briefly lists existing localised training algorithms, but does not properly put the proposed method in the context.

Another lacking comparison to existing methods is that to ensembling. Each neuron in the cyclic NN is essentially a one-layer MLP. Each MLP learns to differentiate between patterns. Then, the decisions of multiple MLPs are accumulated by the readout layer to make the final prediction. Isn’t this a form of weighted ensembling of MLPs?

### Questions
How does the proposed method differ from the multitude of recurrent architectures?

It is not clear how the parameters of the computational neurons and the readout layer are optimised. Is gradient descent employed? Please explain and/or provide the update equation for the weights.

Table 1 lists standard deviations. How many runs were used per each setup? 

Page 2, line 79: “without waiting gradients” -> “without waiting for gradients”

Page 7, line 305: “Theme 4” - do you mean Section?

Page 7, line 318: “there is a neural network consists…” - grammatically incorrect, please re-write.

Page 7, line 324: origional -> original (typo)

### Soundness
3

### Presentation
2

### Contribution
2
