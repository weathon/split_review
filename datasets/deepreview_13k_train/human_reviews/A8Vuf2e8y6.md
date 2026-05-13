# From MLP to NeoMLP: Leveraging Self-Attention for Neural Fields

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
Neural fields (NeFs) have recently emerged as a state-of-the-art method for encoding spatio-temporal signals of various modalities. Despite the success of NeFs in reconstructing individual signals, their use as representations in downstream tasks, such as classification or segmentation, is hindered by the complexity of the parameter space and its underlying symmetries, in addition to the lack of powerful and scalable conditioning mechanisms. In this work, we draw inspiration from the principles of connectionism to design a new architecture based on MLPs, which we term *Neo*MLP. We start from an MLP, viewed as a graph, and transform it from a multi-partite graph to a _complete graph_ of input, hidden, and output nodes, equipped with _high-dimensional features_. We perform message passing on this graph and employ weight-sharing via _self-attention_ among all the nodes. *Neo*MLP has a built-in mechanism for conditioning through the hidden and output nodes, which function as a set of latent codes, and as such, *Neo*MLP can be used straightforwardly as a conditional neural field. We demonstrate the effectiveness of our method by fitting high-resolution signals, including multi-modal audio-visual data. Furthermore, we fit datasets of neural representations, by learning instance-specific sets of latent codes using a single backbone architecture, and then use them for downstream tasks, outperforming recent state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose to create a 'new MLP' architecture which instead models the MLP as self-attention over a fully connected graph of input, hidden, and output 'nodes' (which take the form of learned embeddings). This model is then applied to neural field modeling tasks, demonstrating strong reconstruction performance, and some tangential applications to downstream tasks using the learned node embeddings.  

In conclusion, while the idea is interesting and certainly worthy of further investigation, it seems the paper is not quite ready for publication in my opinion. The claims of state-of-the-art are not quite founded by the results (significantly more baselines are needed), and the writing of the paper seems to be heavily engrained in the neural-field literature, despite making claims which seem to extend beyond that space. I would encourage the authors to re-write the paper with a more in-depth discussion of related work and prior work, allowing the reader to situate the proposed model better in the current field.

### Strengths
- The application of self attention to perform message passing over an 'mlp-like' graph is interesting and clever. 
- The use of extra node embeddings for conditioning is additionally clever and appears to work well for neural field modeling.  
- The reconstruction results seem promising on the few datasets tested.

### Weaknesses
 - Line 39 typo: 'nconditional'
- Writing is not the most clear. Especially the introduction is more a rushed list of related work. 
- There is no background section to describe formally what a neural field is, despite this being a core application of the proposed model. The large algorithm blocks could be moved to the appendix to allow for this background information to be included in the main text. 
- The authors use significant jargon without proper explanation when discussing neural field models (such as 'latent code' & 'latent conditional') which makes the interpretation of their model unclear to anyone not familiar with that literature. 
- Despite the author's efforts, the connection with the MLP is tentative at best. It is perhaps a bit misleading to call the method the NeoMLP, since in actuality it appears to be much more similar to a simple Transformer which has additional placeholder tokens which are believed to allow 'intermediate computations'. Furthermore, since the authors only evaluate the model on 'neural field' tasks, it seems a bit presumptuous to call it the NeoMLP considering how broad of applications traditional MLPs can and have been used for. The core of the model seems to be a transformer operating on a graph structure, where the nodes of the graph are input, hidden, and output embeddings, and the edges are implicitly defined through the self-attention mechanism. This is a significant departure from the standard MLP architecture, and the justification for the name is not entirely clear.
- Only a single baseline is reported (Siren, 2020) for the neural field modeling work (Table 1), this is insufficient given the claimed generality of the proposed model -- and the claims of 'state of the art' in the conclusion. The lack of comparison to other recent neural field methods makes it difficult to assess the true contribution of the proposed model. Specifically, comparisons to methods that use similar conditioning techniques, or those that employ different activation functions, would be beneficial.
- Section 3.2 again starts with a rushed list of related work without sufficient explanation of the methods to allow interpretation by outside parties. The description of the downstream tasks and the methods used is too brief, making it hard to understand the experimental setup and the significance of the results. The connection between the learned node embeddings and the downstream tasks is not clearly explained, and the motivation for using these embeddings in this way is lacking.
- The downstream task performance improvement in Table 2 is marginal, although the reconstruction quality is high. The reported improvements are not substantial enough to justify the claim that the model is learning meaningful representations beyond the neural field task. The lack of statistical significance testing further weakens the claims of performance improvement.
- As the authors note, this model seems very similar to the Graph Neural Machine of Nikolentzos et al. with a transformer used in place of a graph neural network. The authors should provide a more detailed comparison to this method, highlighting the key differences and the advantages of their approach. The current discussion is too brief and does not adequately address the similarities and differences between the two methods.
- Typo, line 508: " indicating that inductive biases that can be leveraged to increase downstream performance"

### Questions
- How is the NeoMLP different from a transformer with extra placeholder tokens (with unique learned 'embeddings')? 
- Can you provide more details for why you need the separate fitting and fine-tuning steps?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a new neural network paradigm for neural function approximation, particularly motivated by improving the fitting capacity and representations of *Neural Fields* (NeFs). In particular, the authors propose to replace the feed-forward nature of MLPs with a fully connected neural network, coined NeoMLP. In this case, information processing happens with synchronous message passing, where neurons (input, hidden and output) are all connected and exchange information.

To make this possible, the authors propose to initialise the features of all nodes (apart from the input ones which are initialised using input values) using learnable embeddings for hidden and output nodes. Additionally, they use attention for information aggregation to reduce the number of parameters, where the attention weights are shared across the entire graph. This architecture is also used for conditional neural fields, i.e. to fit multiple neural fields using the same backbone, where the hidden/output embeddings are learned and can be later used as a representation for each neural field. Experimentally, the proposed method shows promising performance in terms of its ability to accurately fit neural fields, as well as the ability of the learned representations to perform well on downstream tasks, compared with other NeF processing architectures.

### Strengths
- **Significance**. The paper attempts to address an important and timely problem. In particular, as NeFs are becoming increasingly popular in various deep learning application domains, designing new methodologies for learning informative NeF representations is a key desideratum of the field.
- **Novelty**. The paradigm proposed for function approximation is, to the best of my knowledge, a new and refreshing idea (also a quite natural one) and could potentially allow for further advancements beyond classical MLPs.
- **Simplicity and Presentation**. The modifications to MLPs proposed are simple and easy to implement. Additionally, they are mostly well-presented and easy to follow.
- **Experimental evidence**. The provided results seem promising both in terms of fitting capacity, as well as generalisation of the representations in downstream tasks.

### Weaknesses
 - **Evaluation**. One of the major weaknesses that I see in this paper is that some aspects are not well-evaluated. In detail:
   - The authors have not adequately examined the trade-offs in terms of runtime. In particular, neither the fitting phase nor the finetuning phase are evaluated w.r.t. this aspect, although this architecture might turn out to be slower, e.g. compared to the Functa approach, especially w.r.t. the finetuning phase. Also, reporting the training time of Siren vs NeoMLP would be a helpful addition. It is crucial to understand the computational overhead of the proposed method, especially given the fully connected nature of the network, which could lead to increased memory usage and slower training times compared to more sparse architectures or methods optimized for meta-learning based finetuning. A thorough analysis should include wall-clock time for both training and inference, as well as memory consumption, to provide a complete picture of the method's practical applicability.
   - Certain implementation details are not well-justified or ablated:
        - Why did the authors use Random Fourier features? Is that a necessary addition? I would suggest ablating this choice, e.g. by comparing with an MLP + RFF or NeoMLP without RFF vs MLP. The use of Random Fourier Features (RFF) needs more justification. While RFFs can help with learning high-frequency components, it's not clear if they are essential for the performance of NeoMLP or if a simpler positional encoding or even a learnable linear layer could achieve similar results. An ablation study is needed to isolate the impact of RFFs, comparing performance with and without them, and also against a standard MLP with RFFs to understand if the benefit is specific to the proposed architecture.
        - Why did the authors choose a Transformer-like architecture and not a GNN, with e.g. linear/MLP aggregation? Perhaps baselining with such an approach can provide an adequate justification via experimental evidence. Note that this approach will probably also be more computationally friendly. The choice of a Transformer-like architecture over a Graph Neural Network (GNN) is not well-justified. Given that NeoMLP operates on a fully connected graph, a GNN with linear or MLP aggregation could be a more computationally efficient alternative. A comparison with a GNN baseline would help to understand the specific advantages of the Transformer architecture in this context, especially given the quadratic complexity of self-attention.

- **Analysis of the method/Theory**. I believe that since this is a new paradigm, additional effort is expected to analyse its behaviour. For example, 
     - Could the authors discuss the internal symmetries of this approach? My understanding was that since the authors are using positional embeddings for the hidden nodes, then there might not be any permutation symmetries, but the authors mention that such symmetries do exist. I think this claim should be made formal. The discussion on internal symmetries needs to be more rigorous. The claim that permutation symmetries exist despite the use of positional embeddings for hidden nodes requires a formal proof or a detailed explanation. It is not immediately obvious how these symmetries arise, and a more in-depth analysis is necessary to clarify this point.
     - Could the authors discuss the expressivity of this paradigm? MLPs are known to be universal approximators. Could it be the case that NeoMLP is also universal? The expressivity of the proposed architecture needs to be discussed. While MLPs are known to be universal approximators, it is not clear if NeoMLP possesses the same property. A discussion on the theoretical capabilities of NeoMLP, possibly drawing connections to existing work on the expressivity of Transformers, would significantly strengthen the paper.
- **Motivation**. Although I liked the idea and it seems reasonable, I am unsure if the motivation provided is adequate. It may be improved by discussing the aspects I mentioned in the previous bullet point, but currently, it seems mostly ad hoc. For example, the authors mention: L058: “*shares the connectionist principle: cognitive processes can be described by interconnected networks of simple and often uniform units*.”. I do not see how this statement can be related to learning better NeF representations while fitting them to signal data. Could the authors provide more concrete arguments concerning that?

### Questions
**Minor:**
- L122: “Finally, instead of having scalar node features, we increase the dimensionality of node features, which makes self-attention more scalable” --> I would understand using high-dimensional features as a means to make the network more *expressive* (although this is not discussed), but I do not understand why this makes the network more scalable.
- There are a few typos throughout the text. I suggest that the authors perform a thorough proof-reading before updating their manuscript
- L112: “we create learnable parameters for the hidden and output neurons” --> I believe the authors here refer to the initialisation of the features of the neurons (input neurons are initialised with input values, while hidden + output are initialised with a learnable initialisation). Is my understanding here correct? Perhaps, explaining this in detail will help the interested reader.
- Does the number of latents in Table 3 correspond to the number of hidden nodes?
- There are some very recent papers providing algorithms to process NeF parameters among others (related to their symmetries) that the authors might want to cite. For example:
   - The Empirical Impact of Neural Parameter Symmetries, or Lack Thereof, Lim et al., NeurIPS'24
   - Monomial Matrix Group Equivariant Neural Functional Networks, Tran et al., NeurIPS'24
   - Scale Equivariant Graph Metanetworks, Kalogeropoulos et al., NeurIPS'24

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper targets an important problem in NeFs which is how to represent the signals with good reconstruction ability while maintaining good classification ability. The authors propose NeoMLP, viewing MLP as a complete graph, and employ self-attention for message passing among all the nodes. The experiments show that NeoMLP can represent complex signals, especially multi-modality signals such as video with audio, and have a better performance on downstream classification task.

### Strengths
1. The idea of viewing MLP as a complete graph is novel.
2. The experiment on multi-modality data is cool.

### Weaknesses
1. Some important closely related works are missing. Apart from conditioning NeFs with an auto-decoder, a more efficient condition method is hyper-network, such as [1][2]. More importantly, the idea of delivering self-attention for handling vectors that consist of nodes of MLP is quite similar to [1][2].

2. The definition of NeoMLP is not clear. In Figure 1, NeoMLP is the MLP with a fully connected graph while  in Figure 2, NeoMLP is the self-attention backbone.

3. There is no clear evidence that viewing MLP as a fully connected graph may help to improve the reconstruction and classification ability. Current improvement may be due to the better fitting ability from self-attention. I suggest the authors use simple Linear layers as their symmetric function. Then the NeoMLP will just become a simple MLP with more input dimension and output dimension due to the fully connected graph. If this simple MLP still has better performance, the claim that viewing MLP as a fully connected graph leads to a better reconstruction and classification ability can be better proved.

4. The quantitative ablation of the self-attention backbone is missing. Is it possible to replace the self-attention with other symmetric functions in graph learning? 

5. The details for I, H, and O in line 179 are missing. From line 680, it seems that I+H+O=8, then for a audio regression task, we have I=1, O=1, and H=6?

6.  The claim that “the optimal downstream performance was often achieved with medium quality reconstructions” needs more evidence. To show your method has a better performance to balance PSNR and classification accuracy, I suggest the authors provide curves for different methods for PNSR vs. accuracy, rather than the PSNR at best Accuracy.

7. More examples and compared methods such as Miner [3] should be discussed in Table 1.

### Questions
1. The comparison with the hyper-network-based condition methods.
2. The clear evidence for the claim that viewing MLP as a fully connected graph leads to a better reconstruction and classification ability.
3. The curves for different methods for PNSR vs. accuracy. 
4. More examples and compared methods should be in Table 1.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors change the architecture of an MLP for a neural field into a similar format of a transformer, self-attend input tokens representing a position with learned tokens, and finally use it to regress the values of the target object at that position.

### Strengths
- Very interesting method of unifying transformer architecture with INRs…was definitely wondering if something like this existed and the authors seem have come up with it. Excited for what other researchers can build on this.
- Strong results showing the internal representations of the trained networks can be used for classification (i.e. MNIST) against several recent baselines (Table 2)
- Strong ablation studies

### Weaknesses
 - Too much hyperparameter tuning to be generalizable (i.e. all of Appendix B). Authors should defend why this is ok. Since they are from a single sample, I wonder if they are overfit to them, and if researchers can reliably use this for other samples without extensive tuning?

- Should use stronger baselines. For video, SPDER seems to be the most similar to SIREN but stronger. There is also NeRV (Neural Representations for Videos) and VideoINR which are more complex but probably should be compared also.
- Image representation is standard for INR experiments and is missing.
- Novel view synthesis is not included (NeRF)
- The parameter count may be the same as SIREN, but due to the fitting/fine-tuning on a large dataset (which SIREN does not do as it fits to a sample) I suspect the FLOPs of this model are significantly higher, which means it’s not fair to compare it to a model with no “pre-training”. I may be misunderstanding the “fitting dataset” here but just referencing 2.3 paragraph 3.

### Questions
- Are there quantitative results for audio? Figure D in the Appendix is quite suspicious as no metrics are included and the errors seem quite large even though they’re better than SIREN.

### Soundness
4

### Presentation
2

### Contribution
4
