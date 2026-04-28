# LLM as GNN: Graph Vocabulary Learning for Graph Foundation Model

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
Graphs typically exhibit distinctive structure and domain-specific knowledge, motivating the development of a Graph Foundation Model (GFM) capable of generalizing across various graphs and tasks. While recent efforts have focused on combining the strengths of Large Language Models (LLMs) and Graph Neural Networks (GNNs), they often struggle to maximize mutual benefit due to the decoupled architectures. Moreover, existing methods assign out-of-vocabulary (OOV) tokens to nodes, which are incompatible with the natural language vocabulary for task-oriented prompt generation, hindering knowledge transfer in GFM. In this paper, we introduce PromptGFM, a versatile GFM grounded in graph vocabulary learning, comprising two key components: (1) Graph Understanding Module, which explicitly replicates the finest GNN workflow in the language space using LLMs, enabling seamless GNN-LLM integration and elegant graph-text alignment; (2) Graph Inference Module, where we establish a novel language-based graph vocabulary to ensure expressiveness, transferability, and scalability. This vocabulary enables the generation of readable instructions for LLM inference, resolving modality incompatibility and facilitating positive transfer. Extensive experiments demonstrate the superiority of PromptGFM in node classification and link prediction, along with its strong transferability across different datasets and tasks. The code is available at \url{https://anonymous.4open.science/r/PromptGFM}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a graph foundational model. The proposed method employs one LLM to replicate a GNN’s workflow through prompting and another LLM for fitting downstream tasks. Specifically, they replicate the message-passing and local aggregation processes of a multilayer GNN by summarizing input using an LLM, prompting sampled one-hop neighborhoods of nodes to the LLM, and prompting it for aggregation across the neighborhoods. To mitigate the problem of out-of-vocabulary (OOV) faced by LLMs observing unseen nodes, they introduce graph vocabulary learning by making language-based IDs. This graph vocabulary is used for making prompts for the inferencing LLM. Finally, to increase generalization the LLM of inference module is fine-tuned on different tasks and datasets by multi-instruction learning

### Strengths
- The paper introduces a novel approach by employing multilayer LLMs to replicate the message-passing process of GNNs.
- The authors tackle an important issue of OOV tokens in LLMs when applied to graph tasks.
- Experimental results demonstrate the superiority of their model compared to existing LLM + GNN architectures.
- The paper does a comprehensive review of the current methods and the baselines are state-of-the-art.

### Weaknesses
While the proposed method demonstrates clear superiority over current state-of-the-art techniques, there are several significant concerns regarding the paper that need to be addressed:

- While the use of multiple layers of LLMs to replicate message passing across multi-hop structures is a novel approach, the fundamental concept of prompting LLMs for message passing in 1-hop neighborhoods is well-explored with similar methods [1, 3]. The authors should clearly distinguish their “graph understanding” module from existing techniques. Notably, their method incorporates nodes sequentially, which raises practical concerns for large graphs due to the maximum input length limitations of LLMs and the associated performance decline when handling long sequences. For example, showing how long-range dependencies and long sequences can be captured by their understanding module would discriminate from previous works. Additionally, the authors do not provide a clear example of a template showing how a node's textual representation is constructed. The examples in Figure 3 and the Appendix are not sufficiently informative and differ significantly from the case study provided. A concrete example that aligns with the templates outlined in the paper would greatly enhance understanding of the method. Concerning this, the authors would provide special tokens, words, phrases or more details of matching input text to a unified template.
- The prompt examples provided in the paper, along with the case study, illustrate that the graph understanding module summarizes the input text sequentially across multiple rounds. However, in GNNs, information is propagated through message passing rather than summarized. As a result, the LLM has not effectively replicated the message-passing and aggregation processes. Additionally, because the graph understanding module utilizes a non-deterministic LLM, some nodes and their associated feature and structural information may be lost across multiple layers. Consequently, retrieving the embeddings of all nodes after several rounds of prompting becomes challenging. The paper does not address how this information preservation is ensured, especially since the output of the n-th layer of the LLM is expected to represent all input nodes. For example, to address information loss due to the non-deterministic nature of LLMs authors would keep records of node representations after each round of prompting LLM and do an overall aggregation. 
- The generalization of the LLM module for inference might be limited to the tasks and datasets used for fine-tuning which is far from a universal vocabulary as claimed in the paper. Also, this type of multi-task learning is also studied with GNN modules trained on different tasks and datasets as proposed in [1, 2, 3]. Authors would provide evidence or arguments supporting their claim of a "universal vocabulary", particularly in comparison to existing multi-task learning approaches with GNNs.
- The term "prompt-based GNNs" can be misleading, as the underlying model is actually an LLM, not a GNN, and there are fundamental differences between GNN-based models and LLMs. This confusion is further compounded by the visualization in Figure 2, which portrays the current work as a combination of a GNN and an LLM, despite the absence of a GNN module in the model. To enhance clarity, it would be beneficial to revise the terminology and the visualization to better reflect the model's true nature. For example, they can call their method a "prompt-based information propagation" and also remove the "GNN" block from the figure and keep the single LLM. 
- In the "Data Description" section, the paper states that the Cora, Citeseer, and PubMed datasets are "introduced" by this work. This wording is misleading, as these datasets are not contributions of the paper. Authors would instead use alternatives like "used", "utilized", "evaluated/experiments on", etc.
- The explanations of some components in the proposed method, particularly in the sections on "Graph Vocabulary Learning" and "GNN Replication with LLMs," are overly detailed, which can detract from the paper's fluency. The authors should consider summarizing these sections to better highlight the main contributions. Also, the detailed explanations can be moved to an appendix or supplementary material.

### Questions
- The discussion on generating graph vocabulary remains incomplete. Specifically, which module is responsible for creating the graph vocabulary: the graph understanding module or the graph inference module? Based on Figure 4 and the data flow depicted, it appears that the graph vocabulary is generated before the predictor LLM. However, the paper discusses this in Section 4.2, which focuses on the graph inference module. Could it be that the graph vocabulary is constructed through another process between the two modules?
- The distinction between a regular node textual feature and a language-based ID is unclear. In the case study, the language-based ID seems to be a rephrasing of the input textual features. How, do these language-based IDs address the OOV problem if they only replicate a rephrased version of input?
- The representation of node features in graphs like Cora and PubMed as text is not addressed. Given that these graphs contain high-dimensional features, creating an optimal textual representation from them is challenging. How are these features conveyed in the text domain?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a graph foundation model, PromptGFM. Specifically, it includes a graph understanding module where the LLM is prompted to perform 'message passing,' similar to that in GNNs. Additionally, there is a Graph Inference Module, in which each node in the graph is mapped to text tokens, ensuring expressiveness, transferability, and scalability

### Strengths
It is a good idea to prompt the LLM to simulate message passing in a GNN. The design of feature transformation, message passing, and message aggregation all sound reasonable.

### Weaknesses
 - I am not convinced that this qualifies as a graph foundation model. It is an interesting exploration of how to integrate LLMs and GNNs. However, from a methodological perspective, since PromptGFM prompts the LLM to simulate message passing, it requires text-only attributes and is unable to handle non-textual graphs. In the experiments, the inter-domain ability was demonstrated by transferring from Cora/Citeseer/Arxiv to PubMed. However, this is not a typical inter-domain setting, as they are all citation graphs. There might be shared patterns within citation graphs that contribute to the observed 'inter-domain' ability. I would need more experiments to be convinced of the 'inter-domain' ability.
- Lack of strong baseline models. Table 1 didn't include those strong baseline modesl, such as TAPE[1].

### Questions
- How the node is mapping into the LLM's vocabulary (eq5)? How many tokens are need for each node?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces PromptGFM, an LLM-based approach to perform node classification and link prediction on text-attributed graphs (TAGs) only. First, PromptGFM uses one LLM to summarize textual node features (like a title and abstract of a paper) into a “Language-based ID” string. Second, another LLM is fine-tuned on prompts with this textual node ID and a sub-sample of IDs of its one-hop neighbors to “perform neighbor aggregation” and predict a label for node classification or node ID for link prediction.

### Strengths
S1. Intra- and inter-domain transferability experiments might be of certain interest.

### Weaknesses
 **W1.** The paper completely lacks theoretical and experimental support for its elaborated claims such as “meticulously design a series of prompts to align with the GNN workflow at the finest granularity”, “faithfully reproduce the message passing paradigm of GNNs”, “concise yet meaningful representations”, “we capture semantic and structural information through the prompt-based GNN”, “generate expressive representations”.

There is no formal study, proofs, or experimental analysis of how LLM prompts like “please aggregate the following neighbors” can ever capture the math of message passing or its results. Or how “meaningful” or “expressive” the LLM representations are compared to GNNs (there is a whole body of literature on the theory of GNN expressiveness that might have been of help). Perhaps the biggest mistake in claiming the alignment with GNNs is the fact that GNNs are permutation-invariant models whereas all autoregressive LLMs are by default *permutation-variant*, that is, the result of “Please aggregate <node 1> and <node 2>” is very likely be different from “Please aggregate <node 2> and <node 1>” (at least due to positional encodings which will featurize the nodes differently). Constructing a few prompts and claiming “faithful reproduction” without any formal study or theoretical guarantees is not enough to sell such claims.

Similarly, claiming in the ablations (Section 5.3) that PromptGFM suffers from over-smoothing after 4 “message-passing layer” prompting steps has no theoretical or experimental evidence - since there is no notion of a discrete node in PromptGFM (a node is represented with several tokens from the LLM vocab), then what is getting oversmoothed? There are rather rigorous mathematical analyses of oversmoothing [1,2] that measure the distance between node representations of different layers - it would require evidence of a similar phenomenon in scattered tokenized LLM representations to claim oversmoothing in this case.

[1] Oono, Suzuki. Graph Neural Networks Exponentially Lose Expressive Power for Node Classification. ICLR 2020
[2] Southern, Di Giovanni, et al. Understanding Virtual Nodes: Oversmoothing, Oversquashing, and Node Heterogeneity

**W2.** The paper largely oversells its technical contributions, namely, the Graph Understanding Module that replicates message passing (see **W1** why it does not, there is no evidence of such replication); and the universal graph vocabulary which works “across all the graphs and tasks” - in fact, PromptGFM does not propose any new vocabulary for encoding graphs and just relies on the existing LLM token vocabularies and textual descriptions of nodes. If input graphs do not have textual features (a common case for non-citation graphs), PromptGFM appears to be of questionable value as a graph foundation model. The paper repeatedly claims that “existing methods treat nodes as OOV tokens” whereas the vast majority of “LLMs for graphs” approaches (including compared OFA or GraphText) do exactly the same as PromptGFM and use textual node features as part of an LLM prompt.

**W3**. The experimental agenda is rather underwhelming and raises a lot of questions about the practical applicability of PromptGFM.

* Only 4 standard citation datasets for node classification (NC) and link prediction (LP);
* Link prediction experiments employ GNN baselines unsuited for this task - the authors are aware of the benchmark by Chen et al, 2024 which consists of 20 node/link/graph-level tasks and used much stronger baselines like BUDDY for link prediction;
* Comparing billion-sized components of PromptGFM (GPT 3.5 Turbo for Language Node IDs + fine-tuned T5 for actual tasks) which need several GPUs and high monetary inference costs even for small standard graph datasets like Cora vs much smaller GNNs (often 100-1000x smaller) that run for free even on CPUs presents quite a myopic and biased perspective on the advantages of LLMs for graph learning tasks;
* It is hard to quantify the importance of reported results when many important experimental details are missing. Are node labels in the NC task encoded via text or somehow else? Are LLMs asked to predict a text label of a node label or select one of K options? How many negative samples were used in the LP task? What is the size of T5 fine-tuned on the NC and LP tasks (there are many options)? Was it a full fine-tune or LoRA?

### Questions
- Are node labels in the NC task encoded via text or somehow else? 
- Are LLMs asked to predict a text label of a node label or select one of K options? 
- How many negative samples were used in the LP task for PromptGFM and GNN baselines? 
- What is the size of T5 fine-tuned on the NC and LP tasks (there are many options)? 
- Was it a full fine-tune or LoRA?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents PromptGFM, an approach for integrating LLMs with GNNs by developing a language-based graph vocabulary. It aims to resolve limitations in current GNN-LLM architectures and demonstrates competitive performance in node classification and link prediction.

### Strengths
1. Novel attempt at LLM-GNN unification using natural language as a graph vocabulary.
2. Promising results on basic benchmarks.

### Weaknesses
1. The paper claims applicability to all graph types, though it only demonstrates effectiveness on text-attributed graphs.
2. Lacks evidence that the method generalizes to non-textual graphs, which is critical given the claim of a "universal" graph model.
3. How does the model handle graphs without inherent text attributes?
4. Can the authors provide clarity on novel contributions beyond combining existing techniques?

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
