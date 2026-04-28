# Hyper-Connections

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
We present hyper-connections, a simple yet effective method that can serve as an alternative to residual connections. This approach specifically addresses common drawbacks observed in residual connection variants, such as the seesaw effect between gradient vanishing and representation collapse. Theoretically, hyper-connections allow the network to adjust the strength of connections between features at different depths and dynamically rearrange layers. We conduct experiments focusing on the pre-training of large language models, including dense and sparse models, where hyper-connections show significant performance improvements over residual connections. Additional experiments conducted on vision tasks also demonstrate similar improvements. We anticipate that this method will be broadly applicable and beneficial across a wide range of AI problems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Hyper-Connections, a novel extension to residual connections that dynamically adjusts the strength of connections between layers in deep neural networks. This method addresses the limitations of traditional residual connections, such as gradient vanishing and representation collapse, by introducing Depth-Connections and Width-Connections thus enabling both cross-layer and intra-layer interactions. A dynamic variant of residual connection named Dynamic Hyper-Connections (DHC), further adapts connection strengths based on input. The approach is evaluated extensively across pretraining of large language models (LLMs), Mixture-of-Experts (MoE) models on vision tasks. Experimental results demonstrate significant improvements in training stability, convergence speed, and model performance on various benchmarks, highlighting Hyper-Connections as a general-purpose enhancement for neural architectures.

### Strengths
- The paper provides a clear and systematic extension to residual connections named Dynamic Hyper-Connections (DHC), where residual could be consider a static hyperconnection, addressing the trade-off between gradient vanishing and representation collapse.
- Experimenttal results demonstrated effectiveness of DHC across diverse domains, including LLM pretraining and vision tasks.

### Weaknesses
 - There seem a lack of comparsion to a fullt enabled depth-connections and width-connections (DenseNet style) where all of the connection in Figure 2 are enabled and learnable.
- The main result focus on LLM and downstream peformance on langugage tasks, the result on Vision task in the appendix seem to demonstrate less gain compare to langugage tasks, can the author elebrate more on this?

### Questions
- The author mentioned other baselines such as Altup and ResiDual had gains in the early stages of training, Can the author show the full loss curve of OLMo-1B-ResiDual and OLMo-1B-Altup×2 in Table4?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents hyper-connexions, a new neural network architectural improvement which consists in dynamically adjusting the residual connections between layers, effectively managing the trade-off between vanishing gradients and feature collapse. Many experiments with LLMs and vision models demonstrate the effectiveness of hyper-connections to improve stability of training and downstream performance. Various hyper-connections patterns are also studied in depth, with thorough ablations and visualizations.

### Strengths
- There is a clear signal that incorporating hyper-connections in LLMs architectures, without any other modification, improves the training loss for a given number of tokens, and boosts performance on downstream metrics. This result is validated for both dense and MOE architectures.

- Hyper-connexions help reduce training instabilities. This is clear by looking at Figure 5 and 6, the training curves of the models with hyper-connections are smoother and do not have spikes, which is a major advantage for training large models.

- The author did a thorough analysis of the learned connections patterns, with nice visualizations.

- The results generalizes to the vision modalities with experiments on image generation and classification. Hyper-connections seem to be a general improvement for the transformer architecture.

### Weaknesses
 - The main concern I have with this paper is the computational impact of replicating the activations of the network $n$ times for hyper-connections. There is no study on the computational impact both in terms of running time and memory usage. The authors mention Line 394 that “Both methods expand the hidden size by n times with negligible computational overhead” but it is not shown with a proper experiment on the throughput, overall running time, and peak memory usage. Also, it seems that n=1 performs worse than no hyper-connection, so if n>=2 is necessary, and the memory usage is high, it is necessary to study the trade-off between downstream performance, stability and computational cost.

- Although the signal is promising, a full experiment with scaling the number of tokens beyond 500B will be necessary to fully validate the approach. Not asking for this experiment, but current best LLMs are trained on many more tokens and exhibit much better performance than the number reported. I would be curious to see if hyper-connections are useful for training state-of-the-art LLMs.

- In section 3.2 several non-learnable patterns are presented but are not tried in practice. It is not clear whether learning the hyper-connection patterns is really better that having simple fixed patterns, and an analysis on that would be interesting.

### Questions
- Why is expansion rate = 1 worse than no hyper-connection, do you have an intuition ?

- Do these findings generalize to other types of architectures such as ResNets ?

- Line 345 typo: “Static”

### Soundness
3

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
3

### Summary
The paper introduced hyperconnection - width and depth connections with learnable strengths. Hyperconnections are proposed to find a balance between the seesaw effect noticed between vanishing gradients and representation collapse. The input is split into n copies for different connections, and these different copies are added together before layer computation.  The paper also introduced dynamic hyperconnections that dynamically update the strength of connections based on inputs. The paper performs comprehensive analysis of effect of hyperconnections on OLMO and OLMOE and image generation and classifcation problems and investigates its effect with prominent residual connections.

### Strengths
1. The results on LLM benchmarks and losses suggest a better balance between vanishing gradients and representation collapse.

2. Section 4.5 discusses the effect of hyperconnections, which displays that hyperconnections eliminate input embeddings from the output, form parallel blocks which have less reliance on each other increasing chances for unique representations. 

3.Parallel block formation is particularly important as similar layers in a transformer block tends to learn similar representations. The ability to parallely form blocks dynamically based on input reduces the chances for similar representations enabling better models.

4. Assessing the hyperconnections can reveal some internal logic of the neural network. For instance, we may find that a set of classes follow similar paths compared to other classes.

5. The paper is well detailed and mathematically sound, proofs, hyperparameters and other implementation details are discussed appropriately.

### Weaknesses
1. The main drawback is when creating $n$ copies,  it leads to a considerable amount of increase in memory, though the burden can be reduced through engineering, the impact is yet to be known.

2. If the goal of creating multiple copies is just to make sure multiple depth connections can be modelled parallelly, is creating such copies actually necessary? Can't a single copy be used with different residual strengths? The only difference would be in gradient computation , were additional terms for each depth connection would be added to the singular copy. Can an ablation be conducted between DHC ($n=4$ and $n=1$) and SHC ($n=4$ an $n=1$) to show the importance and need for additional copies. What I am particularly interested is the advantages with updating the gradients into different copies and then adding them before every layer computation verses  updating all the gradients with a single copy. If there is any other specific need for expansion please free to refute this point.

3. Figure 2 caption improvement. The figure can discuss the diagram better, whats $\beta$, and need to add $\alpha_{1,0}$ and $\alpha_{2,0}$ be explained in the diagram itself. This is important as Figure 2 is the central figure that tries to encompass hyperconnections therefore adding these information would make it more clearer for readers.

### Questions
Some questions that may add more value to the paper:
1. With Dynamic Hyperconnections, there is a possibility for redundant connections (when strength becomes 0) how does these cases affect the seesaw effect of gradient vanishing and representation collapse.
2. Do DHC connections behave similar for images belonging to the same class in case of image classification?

Things I expect from the rebuttal are actions on points 2 and 3.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces hyper-connections, a approach that aims to address the limitations of residual connections of transformers architectures.
The hyper-connections approach introduce depth-connections and width-connections, allowing a more customizable interaction between layers. Depth-connections are weighted connections across different layers, while width-connections facilitate two layers at the same depths. More importantly the hyper-connections are learned, so it improves model adaptability.
Models with hyper-connections have significant performance improvements over the original architectures.

### Strengths
The experimental results seems good enough to claim the hyper-connections is better than the original architectures.

### Weaknesses
1. The presentation is horrible, it is really hard to understand what is model is doing. Probably a better figure or even pseudocode should be provided to explain the methods.
2. Although the experimental results are good, there is no information on how much extra computation is need to achieve such good results. I suspected that the extra performance is highly due to the extra parameters or extra computation it needed. If you make your model have the same floats, probably you could see that the performance is really similar to the original transformers.
3. The ordering of the paper is horrible, there is almost no explanation why you do each thing in the paper.

### Questions
1. In the introduction, you stated that "Post-Norm applies normalization operations after the output of each residual block, weakening the
"strength" of residuals." I don't think it is correct, since post-norm applies normalization after the summation of the skip and residual branch, so it shouldn't weaken the strength of the residuals.

2. Can you also should the flops count for your model and the original model?

### Soundness
2

### Presentation
2

### Contribution
2
