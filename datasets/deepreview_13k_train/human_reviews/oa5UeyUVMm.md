# Graffe: Graph Representation Learning Enabled via Diffusion Probabilistic Models

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Diffusion probabilistic models (DPMs), widely recognized for their potential to generate high-quality samples, tend to go unnoticed in representation learning. While recent progress has highlighted their potential for capturing visual semantics, adapting DPMs to graph representation learning remains in its infancy. In this paper, we introduce **Graffe**, a self-supervised diffusion model proposed for graph representation learning. It features a graph encoder that distills a source graph into a compact representation, which, in turn, serves as the condition to guide the denoising process of the diffusion decoder. To evaluate the effectiveness of our model, we first explore the theoretical foundations of applying diffusion models to representation learning, proving that the denoising objective implicitly maximizes the conditional mutual information between data and its representation. Specifically, we prove that the negative logarithm of denoising score matching loss is a tractable lower bound for the conditional mutual information. Empirically, Graffe delivers competitive results under the linear probing setting on node and graph classification, achieving state-of-the-art performance on 9 of the 11 real-world datasets. These findings indicate that powerful generative models, especially diffusion models, serve as an effective tool for graph representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this submission, the authors propose a self-supervised diffusion model, called Graffe, for graph representation learning. 
Graffe generates a source graph representation via a trainable encoder and leverages the representation as the condition of the diffusion model.
In particular, the authors prove that the denoising objective implicitly maximizes the conditional mutual information between data and its representation, and the negative logarithm of denoising score matching loss is a tractable lower bound for the conditional mutual information.
Experiments on real-world datasets further verify the feasibility of the proposed method.

### Strengths
- Although there have been a few works on leveraging diffusion models for graph representation learning[1,4] or considering the representation abilities of DPM[3], I find this submission quite interesting. The rationale is convincing, and it thoroughly discusses the design of the proposed method.
- The theoretical part seems correct and reveals some interesting results that further support the proposed method's feasibility in practice.

### Weaknesses
 - The experimental results for node classification are promising. However, in the graph classification task, it appears that the SOTA method is GIP[2], which significantly enhances performance in this area. It would be beneficial for the authors to compare Graffe with GIP.


### Questions
Please see above.

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
This paper proposes Graffe, a method that applies Diffusion models, currently the most popular deep generative models, to self-supervised representation learning on graphs. It first uses a graph encoder to obtain a compact representation of a graph/node, then uses a conditional generative model to recover node/graph features based on this representation. Through theoretical analysis, the paper proves that diffusion models can maximize the conditional mutual information between the data and its embeddings. In terms of experimental results, Graffe delivers superior performance compared to previous self-supervised learning models on 9 out of 11 node classification and graph classification datasets.

### Strengths
- I really like the idea proposed in this paper. I am quite familiar with graph self-supervised learning and diffusion models (as well as the Infomax principle), and this paper manages to combine these two seemingly distant topics in a very promising and exciting way.
- The paper provides substantial theoretical proofs and analytical experiments (such as Figure 2), demonstrating the relationships between (conditional) diffusion models, mutual information, and effective data representations.
- The experimental results are very comprehensive. First, it includes both self-supervised node classification datasets and self-supervised graph classification datasets. Second, based on my experience, Graffe achieves state-of-the-art performance on many benchmarks, which is a very impressive result.

### Weaknesses
 - Since DDPM can be understood as a special type of variational autoencoder, this paper could also be interpreted as a special VAE-based self-supervised method.
- In Section 1, the paper mentions the challenge in generalizing the representation learning power of diffusion models on graph data, with one being the non-Euclidean nature of graph data. However, besides using GNN models as encoder and decoder, Graffe doesn't seem to make additional considerations for this challenge. The method does not explicitly address the unique challenges posed by graph data's non-Euclidean structure beyond the use of GNNs, such as how to effectively incorporate structural information into the diffusion process, or how to handle the varying node degrees and local neighborhood structures inherent in graphs. This lack of specific adaptation to graph data could limit its effectiveness compared to methods that directly address these challenges.
- Although the paper provides very detailed theoretical analysis, its conclusions seem relatively trivial: First, since representation is inherently a function of the input, Theorem 2 is obvious. Second, the InfoMax conclusion doesn't explain why the learned representations would be better, because as mentioned in the paper, identity mapping would be the encoding that maximizes Mutual Information. Third, there is a significant gap between theoretical analysis and practical application. The theoretical analysis seems to be aimed at i.i.d. data, where both the encoder's input and decoder's target are x. However, for graphs, the encoder's input consists of two parts (node features and graph structure), while the target is only the node features.

### Questions
1. I want to know how much impact the choice of Encoder has on Graffe's performance. As is well known, many node-level self-supervised models (such as most contrastive learning models) use the most basic two-layer GCN model. Is using GAT unfair for Graffe (I know some other Graph MAE models also use GAT)? How would using a GCN model affect Graffe's performance? What would happen if contrastive learning methods also used GAT models?

2. How important is the Unet structure for the Decoder? What impact would using regular MLPs or GNNs have on performance?

3. How efficient is Graffe? For example, how does it compare in terms of training time with other contrastive methods or MAE methods?

### Soundness
3

### Presentation
3

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
Graph representation learning via diffusion-based approaches which reaches Sota performance.

### Strengths
The writing and visualization are pretty clear and the paper also includes core ablations. The usage of graph U-Net is well-motivated and clarified in the paper. The performance seems to be consistent in the ablations in 5.4. The theoretical insights about conditioning supports better the encoder part.

### Weaknesses
1. Some key insights are missing from the analysis:
  * The effect of mask ratio seems to be very different for different datasets, which will lead to more tuning, as mentioned in the limitations. However, the insight about the impact of mask ratio is also missing in the discussions, and an intuitive guide for choosing this ratio would be helpful. Specifically, the paper lacks a discussion on why certain datasets benefit from higher mask ratios while others do not. This makes it difficult to generalize the findings or provide practical guidance for new datasets. The lack of analysis on the interplay between graph structure and mask ratio is a significant gap.
  * It is very intriguing that A reconstruction seems to only deteriorate the performance as mentioned in the 1st part of 5.4, since A contains richer information than node features for graphs without explicit node features. The insight about this is also missing. The paper does not explore why directly reconstructing the adjacency matrix, which encodes crucial structural information, leads to performance degradation. This is particularly concerning for graphs where node features are sparse or absent, as the adjacency matrix becomes the primary source of information. The paper should investigate this counterintuitive result further.
2. While spectra are a key in related work, this is no further analysis in the experiments and in methods. The related sentence in Line 84 of the Introduction lacks supportive evidence or explanation. The connection to spectral methods is mentioned but not explored, which is a missed opportunity to provide a deeper theoretical grounding for the approach. The paper should either provide experimental evidence to support the spectral interpretation or remove the claim.

### Questions
One question I have is about the difference between the 'encoder' and 'decoder' part, where 'encoder' functions as a condition for the decoder. The mechanism of 'encoder' by masking nodes is very similar to another diffusion process which absorbs nodes sequentially until all nodes become noisy. So the process seems to be somehow a denoising process given 2 types of noising trajectory (one with t being dynamic, and another with t being fixed as the mask ratio). Would the performance change if the encoder/decoder designs switch, out of curiosity? Have you considered using both dynamic 't' as the mask ratio in the 1st part as well?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Graph representation learning has been a critical problem and is commonly addressed by graph neural networks. This paper explores diffusion probabilistic models (DPMs) on graph learning and proposes the Graffe model. Theoretically, the theoretical foundations of Graffe are proved to be the objective of maximizing the conditional mutual information between data and presentations. Empirically, Graffe achieves superior performance on 9 out of 11 datasets on node and graph classification tasks.

### Strengths
1. A necessary theoretical foundation is provided for diffusion models to presentation learning. The lower bound is derived as the objective for model training.

2. Critical claims and designs are well justified with experimental results, e.g., Figure 2 and Figure 3.

3. Experimental results support the effectiveness of the proposed Graffe model.

### Weaknesses
1. As claimed, the aim of the diffusion model for representation learning is to maximize the conditional mutual information between data and its presentation. However, in Equation (8), it seems to replace presentations with labels. Please justify the motivation.

2. Some notations are not properly defined before usage. For example, f(t), g(t), λ(t) in Section 2 and Operator Tr, Cov in Section 3. Those undefined notations impact the comprehension of the content.

3.  The foundation of the diffusion process for representation learning is to maximize the mutual information of data and presentations. However, this design has been discussed for a long time in the design of GNN, such as [1][2]. Could the authors please justify the fundamental differences if any?

4. Polynomial spectral GNNs have demonstrated advantages in graph representation learning. Please justify the advantages of Graffe, a diffusion model over those polynomial GNNs.

5. Several state-of-the-art models for node classification are missing in the experiments, e.g., [1][2][3]. Please include them for comparison in the experiments.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
2

### Contribution
3
