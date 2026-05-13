# Transformers Use Causal World Models in Maze-Solving Tasks

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Recent studies in interpretability have explored the inner workings of transformer models trained on tasks across various domains, often discovering that these networks naturally develop surprisingly structured representations. When such representations comprehensively reflect the task domain's structure, they are commonly referred to as ``World Models'' (WMs). In this work, we discover such WMs in transformers trained on maze tasks. In particular, by employing Sparse Autoencoders (SAEs) and analysing attention patterns, we examine the construction of WMs and demonstrate consistency between the circuit analysis and the SAE feature-based analysis. We intervene upon the isolated features to confirm their causal role and, in doing so, find asymmetries between certain types of interventions. Surprisingly, we find that models are able to reason with respect to a greater number of active features than they see during training, even if attempting to specify these in the input token sequence would lead the model to fail. Futhermore, we observe that varying positional encodings can alter how WMs are encoded in a model's residual stream. By analyzing the causal role of these WMs in a toy domain we hope to make progress toward an understanding of emergent structure in the representations acquired by Transformers, leading to the development of more interpretable and controllable AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper discusses the presence of world models in transformers trained on maze tasks. The maze data is given to the model as a series of coordinates and separator tokens including semicolons between maze edges. The authors observe that certain attention heads attend from the semicolon tokens to the coordinate tokens. They also train SAEs on the residual stream and observe that there appear to be features that represent the presence of a single maze edge.

### Strengths
The paper is an interesting case study of maze-solving networks, which have not been the subject of much attention in previous interpretability work. The paper furthers the study of world models and SAEs.

### Weaknesses
1. My main critique is that it's hard to say that the evidence presented is sufficient to claim that maze-solving networks have a "world model." Previous work (Li et al, https://arxiv.org/abs/2210.13382, Gurnee et al, https://arxiv.org/abs/2310.02207) on world models showed that feeding models data that is derived from some state of the world led models to represent the state of the world itself in a similar way that humans would, in a way that was not necessarily obvious was required for the task. I.e. for humans, we think about world -> data and world -> policy, and training on data -> policy causes the model to represent data -> world -> policy. For example, in Li et al, it's not at all obvious that giving the model data like "E3; G4; etc." for Othello and training it to predict legal moves would cause the model to have a representation of "whether each square is occupied by white or black." In Gurnee et al, it's shown that places are represented with latitudinal and longitudinal coordinates in embedding space, making comparison easy.

In this case, however, it seems obvious that the model should have an atomic representation of whether each edge exists because it's given by the input tokens themselves, and recovering these features does not give us a more interesting representation than the input data itself. In fact, we can use a linear probe to classify the input embeddings directly and still recover the same information (which was not possible in the Li and Gurnee examples, which required the model to execute some nontrivial transformation of the data), so it's unsurprising that this data still exists later in the residual stream. The fact that the model represents the presence of an edge with a single feature is not particularly surprising, given that each edge is explicitly represented by a pair of coordinate tokens and a separator token in the input. The model is essentially just learning to associate a feature with a specific sequence of tokens, which is a relatively simple task.

Similarly, in Section 4, the intervention "create or remove some edge" is comparable to completing an intervention in the model input, so the knowledge of how to edit the world model is not doing something with model internals that we couldn't have done otherwise. (On the other hand, world model edits in the Othello/geography world are not necessarily emulating a straightforward change in the model input and can be more surgical.) The interventions are essentially equivalent to adding or removing tokens from the input sequence, which does not demonstrate a deep understanding of the maze structure. The model is not manipulating an internal representation of the world, but rather directly manipulating the input data.

2. I think the fact that the SAEs have a separate feature for each possible edge is a failure mode that occurs when there are too many features. E.g. imagine you have more features than data points, causing every possible activation to have its own feature direction. This suggests that the SAE is not learning a compressed or abstract representation of the maze, but rather memorizing the specific edges present in the training data. This is a common issue with overcomplete dictionaries, where the features become highly specific to the training set and do not generalize well to new data.

3. The writing style and clarity of the paper could be greatly improved. For instance, the use of decision trees needs to be further explained -- is the training objective ablation loss/what features count as the "most relevant"? Additionally, in the present state I do not think Figures 4-5 clearly advance the paper's main arguments. The explanation of the decision tree methodology is insufficient, and it is not clear how the decision trees are used to identify the most relevant features. The figures lack clear explanations and do not effectively support the claims made in the paper.

### Questions
1. Could you clarify what the significance is of attention patterns switching from 1/3 preceding tokens to 5/7 preceding tokens after token position 100? I don't think this is sufficiently explained by Appendix D
2. Why should we expect there to be separate attention heads attending to even vs odd parity cells?

### Soundness
2

### Presentation
2

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
This paper considers the causal world model emergent from transformers trained on maze-solving tasks. By leveraging attention visualizations and SAE feature attribution, the paper presents that transformers indeed encode the maze structure and sometimes causal depending on the positional-encodings. The paper also proposes the decision-tree method that attributes successfully the features most relevant for edge connections and distinguish the models trained with standard positional embeddings to rotary embeddings.

### Strengths
1. Established empirical WM findings in maze-solving transformers. 
2. Authors propose the decision-tree method to distinguish features relevant to edge connections, which is novel and useful in this case for insights on the two positional-encoding schemes.
3. There is some cross-checking between the edge features and SAE features in Figure 7a.

### Weaknesses
1. Although there was an attempt to do circuit analysis on the transformers, it was limited to attention visualizations and magnitudes of vectors from applying OV matrices. There is not much to take away from this. The authors also speculated on linear probes failure reasons but there is no results on probes. It would be more interesting to corroborate the findings from decision-tree to that of linear probe steering. Specifically, the analysis of attention heads and OV matrices lacks depth; simply observing even/odd parity is insufficient. A more rigorous approach would involve quantifying the information flow through these components, perhaps by measuring the mutual information between head outputs and specific features or by analyzing the singular values of the OV matrices to understand their effective rank and dimensionality. Furthermore, the speculation on linear probe failure is not substantiated without empirical results. The authors should have attempted to train linear probes on intermediate representations and then perform causal interventions, such as ablating specific features identified by the decision tree and observing the effect on probe predictions. This would provide a more direct link between the decision tree analysis and the internal representations of the transformer.
2. There is no mention of details of the exact SAE training architecture and procedures as well as a rough sketch of features other than encoding edge connections. The lack of detail regarding the SAE training is a significant omission. The authors should have specified the architecture (number of layers, hidden units, activation functions), the training procedure (optimizer, learning rate, batch size, number of training steps), and the regularization techniques used. Without these details, it is difficult to assess the validity and reproducibility of the SAE results. Furthermore, a more comprehensive analysis of the discovered features is needed. Simply stating that some features encode edge connections is insufficient. The authors should provide a detailed taxonomy of the different feature types, including their sparsity, selectivity, and functional role in the model. For example, are there features that encode specific locations in the maze, or features that represent higher-level concepts such as path segments or decision points?
3. Overall, there is not much contribution other than proposing the decision-tree method in this specific setup and the empirical findings on the WMs of maze-solving transformers in this paper do not add too much to that in Igorevich et.al 2023.

### Questions
1. In Figure 9, it is mentioned that "Stan removal interventions fail as the inputs in
these cases have more connections than the model is able to handle"; however, if I understand correctly, removing the connections reduce the length so the Stan model should not fail in this case?
2. What is the rough statistics of SAE features and what features other than edge connections are encoded?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a transformer network that learns to solve maze puzzles by constructing the cell connection world model in the first layer. They validate this representation by training an SAE and showing that the SAE cell-connection features are similar to the features written by attention heads in the first layer. The authors also show that the features are causal in adding new connections that are not present in the input. The paper contributes novel insights into how positional encoding can affect the world model representation in transformers.

### Strengths
- The claims made in the paper about the maze solving transformer networks are original.
- Most of the claims are well substantiated.
- The analysis of the role of positional encoding in forming the world model is novel.

### Weaknesses
Weaknesses:
- The different mechanisms of the Stan and Terry models are not directly comparable as they have different positional encodings as well as different numbers of attention heads. Varying the positional encoding while keeping everything else the same, including the number of attention heads and the dimensionality of the attention layers, would be helpful in isolating the role of position encoding in the model. The current setup confounds the effects of positional encoding with the architectural differences.
- The result in section 3.1 is qualitative without quantitative support. Adding the average fraction of attention that the ";" token assigns to the previous two cell tokens, perhaps with a standard deviation across multiple maze instances, would provide quantitative evidence for the claim that the attention heads are attending to the relevant cell tokens for connection construction. Furthermore, a visualization of the attention weights for a few example mazes would be beneficial.
- Section 4 claims that Stan fails to generalize to mazes with more connections, referencing Figure 10. However, the intervention tests a 6x6 level with one more connection, which should be solvable given that the model was trained on 7x7 sparsely connected mazes. The paper needs to clarify that the model was not trained on fully connected 6x6 mazes with an additional connection, and that the failure is due to the increased sequence length rather than the number of connections. Clarifying this discrepancy would improve the argument.
- The paper claims that the model is able to reason with respect to more active features than it would have ever observed during training. However, the experiments only perform interventions that add a single connection feature. The paper doesn't perform interventions that add multiple features simultaneously, which would more directly test the claim about reasoning with novel feature combinations. Including such experiments, perhaps with a systematic increase in the number of simultaneous feature additions, would substantiate the original claim.

The writing and the figures are not clear at some places and can be improved. See the clarity improvements provided below.

### Questions
Questions:
- Why does the rotary-embedding based model have half the number of attention heads, and hence, half the parameters compared to the standard model? Figure 10 also doesn't have the (512, 8, 6, 'rotary') tuple. Currently, the difference in results between the Terry and Stan models cannot be solely attributed to the change in positional encoding as the number of heads also changes across these models.
- How good is the reconstruction of the SAE? Please provide number like fraction of loss recovered and  explained variance. The paper also doesn't provide the hyperparameters like learning rate, L1 decay, etc. to reproduce the SAE.
- In Figure 4, what does the "magnitude of vector" mean? Do you mean you take the L0 or L1 norm of the vector resulting from applying Wov to a cell-token embedding?
- In section 4, when calculating intervention accuracy on removing a connection, do you check whether the maze is still solvable after removing the connection? If yes, please mention that in the paper. If not, then it is possible that removing the connection, which adds a wall in the maze, makes the level unsolvable.
- Did you find "token-detector" features in the SAE that activate on the maze cell token? If yes, then it is possible that the connection-removing intervention doesn't work because you are not removing the corresponding two maze cell features, which might be used in later layers to detect the presence of their connection.

Improvements for clarity:
- Figure 1(b) is confusing as a visual representation of the maze as it looks like the walls are also maze cells. Please consider replacing it with a visual similar to the one in Figure 8, where the walls are thin and it is easier to identify the cell positions.
- Please increase the font size in all your figures. All the figures have very small x and y-axis labels, which require a high zoom to be legible.
- It is unclear what is being measured in the bar plots of Figure 7b. The text says "effect of patching attention head on the SAE latent vector," but it is not clear how this effect is measured. What does 100% effect mean? Is it measuring the percentage reduction in the SAE latent activation after patching the attention head score?
- The alternating patterns of the L0H3 and L0H7 for Stan (Figure 4) are poorly explained in section 3.1. It only became clear to me after reading section 3.3 and appendix F how the alternating pattern of Figure 4 relates to the flipping attention head pattern between L0H3 and L0H7 of Figure 3.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper attempts to understand the internal representation of a Transformer trained on maze navigation tasks. It mainly studies the internal structure of two models, namely Stan (learned positional encoding + 8 heads) and Terry (RoPE positional encoding + 4 heads).

### Strengths
1. Some of the observations (e.g., the attention patterns shown in Fig. 3-4) are interesting.

### Weaknesses
1. Overall there does not seem to have a clear picture of the overall internal structured of the learned weights. The paper hits many points but appear disorganized. It is hard to extract the main message.
2. Many claims are not grounded with quantitive evidences, or not conclusive. For example, the paper claims that the Transformer uses "causal world model", but what is the formal definition of the world model in this paper? Does WM mean a collection of correlations shown by attention map? How does such a world model come into play in predicting shortest path? Unfortunately I didn't see clear explanations in the paper.
3. How the decoupling effects of SAE come into play for WM? How is "Isolating irrelevant features" helpful for WM? How to measure the degree of entanglement in the features for Stan and Terry models? The sentences in Sec. 3.2 appear to be very vague.  
4. Are any of these observations generalizable to other instance of runs? Fig. 3 talked about specific neurons L0H3, L0H5 and L0H7 and their behaviors such as even-parity and odd-parity. Will such behaviors change over a different runs?   
5. What is W_{OV}?

### Questions
See above.

### Soundness
1

### Presentation
2

### Contribution
1
