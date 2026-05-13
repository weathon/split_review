# TokenFormer: Rethinking Transformer Scaling with Tokenized Model Parameters

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Transformers have become the predominant architecture in foundation models due to their excellent performance across various domains. However, the substantial cost of scaling these models remains a significant concern. This problem arises primarily from their dependence on a fixed number of parameters within linear projections. When architectural modifications~(\textit{e.g.}, channel dimensions) are introduced, the entire model typically requires retraining from scratch. As model sizes continue growing, this strategy results in increasingly high computational costs and becomes unsustainable. To overcome this problem, we introduce \ourmethod, a natively scalable architecture that leverages the attention mechanism not only for computations among input tokens but also for interactions between tokens and model parameters, thereby enhancing architectural flexibility. By treating model parameters as tokens, we replace all the linear projections in Transformers with our token-parameter attention layer, where input tokens act as queries and model parameters as keys and values. This reformulation allows for progressive and efficient scaling without necessitating retraining from scratch. Our model scales from 124M to 1.4B parameters by incrementally adding new key-value parameter pairs, achieving performance comparable to Transformers trained from scratch while greatly reducing training costs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes a new architectural component that can be used in transformers to replace linear projections present in the attention and feed-forward layer. A Pattention layer executes an attention mechanism between the input and some learned key and query tokens to output a transformed token. Both the channel dimensions and the number of key-query tokens can be scaled flexibly, in the sense that smaller models can be used as initial configurations for larger models. Iteratively enlarging the model results in significantly smaller training costs and similar performance to comparable architectures.

### Strengths
- Innovative and flexible idea of tokenizing model parameters, that will probably inspire further experimental work in this direction 
- Clearly written, well-motivated and contextualized
- Demonstrated lower training cost in comparison of the proposed approach compared to a number of different open-source architectures and datasets

### Weaknesses
 - The computational complexity of inference and the model itself is only dicussed late in the work. 
- The work would benefit from an explicit discussion of the architectures practical limitations.
- See questions below

- Table 1: "The best performance highlighted for each model" seems to be misleading. It seems it is highlighted in bold for each dataset and model size what the best value is, and even then it is unclear why e.g. LAMBADA acc highlights ours-1.5B and not Pythia 1.8B (this is also the case for several other columns)
- Figure 6: Would you say the (Token)Transformer converged on the test loss respectively (left)?
- It would be nice if the practical relation between parameters, dataset size, scaling stepsize and performance was further investigated. Is there a minimum model size for which this approach only starts being useful? What were your practical considerations in choosing the steps and initializations you did? 
- Is there a different effect of scaling the channels and the dimensions?  
- Are there artifacts of the scaling steps in the final model? E.g. do the norms of the new channels (new tokens) that were initialized at zero have a different magnitude than those from previous time steps?

### Questions
- Table 1: "The best performance highlighted for each model" seems to be misleading. It seems it is highlighted in bold for each dataset and model size what the best value is, and even then it is unclear why e.g. LAMBADA acc highlights ours-1.5B and not Pythia 1.8B (this is also the case for several other columns)
- Figure 6: Would you say the (Token)Transformer converged on the test loss respectively (left)?
- It would be nice if the practical relation between parameters, dataset size, scaling stepsize and performance was further investigated. Is there a minimum model size for which this approach only starts being useful? What were your practical considerations in choosing the steps and initializations you did? 
- Is there a different effect of scaling the channels and the dimensions?  
- Are there artifacts of the scaling steps in the final model? E.g. do the norms of the new channels (new tokens) that were initialized at zero have a different magnitude than those from previous time steps?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an innovative modification to the standard transformer architecture by replacing all linear layers with learned tokens via attention operations. By making this alteration, the proposed architecture can effectively remove all learned parameters (except embedding layers), instead replacing them with learned tokens. This token-parameter-attention mechanism (Pattention) therefore provides an efficient mechanism for scaling parameter counts. The authors validate their architecture with several scaling experiments, on both causal language modeling and vision tasks, demonstrating comparable performance with a significantly reduced training budget. 

Overall, this paper makes a significant architectural contribution to the lineage of transformer architectures. However, the authors primarily focus on the empirical validation of their methodology without sufficient theoretical backing or exploring limitations of this approach. I am therefore inclined to reject, but would be willing to reconsider pending further discussion.

### Strengths
This paper proposes a unique approach to scaling parameters and demonstrates compelling results under those conditions, including vision and language tasks. The authors further support their claims with extensive experimentation, demonstrating a substantial reduction in training costs. Additionally, the authors propose an interesting attention mechanism for their parameter tokens, which solves the issue of vanishing gradients caused by the softmax function in traditional attention. Furthermore, this paper is well-written and easy to follow, with clear figures and tables.

### Weaknesses
-	Throughout the paper, the authors seem to imply that the scaling issue is unique to transformers. However, the increased training cost with scale applies to most DNN architectures. Furthermore, they contradict themselves when attributing training cost to increasing parameters while later showing that cost is dominated by self-attention (which is well known). The proposed training improvements are therefore solely due to fixing the hidden dimension size and resuming, rather than directly due to the Pattention mechanism. The authors should make their motivation more precise, and avoid overly vague and potentially misleading arguments to support their approach.
-	The paper lacks a theoretical foundation as to why their approach works, only briefly mentioning a potential explanation in Section 5, Future Work. Although scaling parameters generally improves performance, this is typically done while also scaling the hidden dimension, which has other benefits beyond parameter count (e.g. larger representation space). While the empirical results are promising, discussing deeper theoretical insights would allow application to other (hybrid) architectures beyond TokenFormer.
-	The authors compare against an old baseline (Net2Net) to demonstrate their model's effectiveness in growth when resuming from a smaller model. It would be more appropriate to compare with newer methods, which have been shown to perform much better (Yao et al., 2024). Furthermore, the practice of initializing extended queries to zero may negatively impact potential performance due to symmetry, where the proposed method instead relies entirely on the value token initialization. The authors should clarify why Net2Net was chosen over newer methods, or why the newer methods would not be a more suitable comparison.



### Questions
1. Your main argument for scaling is based on adding parameter tokens to the Pattention layers. However, this necessarily requires that you fix A) the hidden dimension, and B) the model depth. 
    - 1a. Fixing the hidden dimension can lead to representation crowding, which typically does not occur when increasing it (e.g. larger vector space for representations). Could you investigate this with your scaled models? As a limitation it should result in an upper limit to capacity, where adding new parameter tokens will no longer improve performance.
    - 1b. Fixing the model depth can have a significant impact on the range of functions the transformer can learn. It’s possible that this was not apparent due to the model size and benchmarks, but would severely limit feasibility for more complex problems, which often require larger scales (>70B). Could you address this limitation?
    - 1c. By fixing the hidden dimension, achieving improved performance would then depend on expanding the representation span within a fixed vector space (i.e. approaching 100% channels to capture the variance). This will likely have a negative impact on quantization methods, which may offer substantial computational improvements beyond what Pattention can provide alone. Could you address this?
2. The parameter token scaling method raises several questions that should be addressed.
    - 2a. When scaling the number of parameter tokens, do you observe representation collapse, or do you apply a regularization term to prevent this? Adding fixed parameters without enforced symmetry breaking often leads to vector consolidation into tight groupings. Alternatively, have you confirmed that this behavior is not occurring?
    - 2b. In Figure 2, you suggest keeping the previously learned parameter tokens unfrozen for model growth; is this necessary? It may be more beneficial to keep the previously learned parameters frozen to essentially learn “residuals”. 
3. While you present the mechanism by which Pattention works, there is no explicit connection to linear layers, or is it closer to an FFN? Could you clarify this connection in the appendix? Intuitively, if the GELU scoring is one-hot, then you have a K-V lookup.
4. Your scaling conclusions in Section 4.3, Table 3, and Figure 5 are contingent upon which term dominates in the asymptotic analysis. You require that $l \cdot n \cdot d \cdot T < l \cdot d \cdot T^2$, otherwise Pattention will become more expensive than simply using linear layers. The scaling argument should be more precise, and both acknowledge this point and demonstrate which regime the different model scales are in. Notably, a significant number of parameters were added to the 1.4B model (6.6M per matrix vs. 2.4M), where it would also be appropriate to report the FLOPs required for a forward pass of sequence length $T$, verified with empirical measurement. Furthermore, relying on a fixed $l$ while scaling $n$ may significantly impact parallelism during inference. 
5. To confirm, did you retain the original softmax attention for the MHA layers, or did you apply the GELU scoring there as well? This should be made clear to avoid confusion.
6. Questions about the Future Work section. While it is understandable to suggest exploratory directions in the future work section, some of the proposed ideas would benefit from either preliminary results or a more concrete implementation plan.
    - 6a. You mention adjustable computational cost: can you elaborate on how this could be done? Your current methodology seems to be restricted to $n_\mathrm{new}$ once scaled up, without any way to “adjust” the computational cost. 
    - 6b. The idea of combining vision and language parameter tokens is interesting; however, I am highly skeptical whether this would work. Do you have preliminary results to back up this idea? If not, perhaps the statement should be weakened, as it's not improbable that some features may have significant overlap, allowing for $\mathrm{max}(n_\mathrm{lang}, n_\mathrm{vision}) < n < n_\mathrm{lang} + n_\mathrm{vision}$, where the vision and language tasks are not simply combined after independent training. 
    - 6c. The paragraph on “Increasing interpretability” is vague. How exactly will Pattention improve interpretability? Can you make a connection to Sparse Auto-encoders (SAEs)? This seems like something that should have been added to the appendix.




Additional Comments:

-	It appears you are missing a factor of 2 in the parameter counts in Table 3. According to your description, you learn $n$ Key and $n$ Value tokens, resulting in a total of $2n$. The parameter counts and cost would then be identical to a traditional transformer when $n=d_\mathrm{model}$ and $d_\mathrm{token}=d_\mathrm{model}$. 
-	Please include a discussion connecting the GELU scoring function to your scaling ability. Scaling by setting new keys to zero relies on the GELU function, where GELU(0)=0; in contrast, exp(0)=1, which causes a norm shift.


Yao, Yiqun, Zheng Zhang, Jing Li, and Yequan Wang. ‘Masked Structural Growth for 2x Faster Language Model Pre-Training’. In The Twelfth International Conference on Learning Representations, 2024.

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
The propsoed TokenFormer replaces dense linear layers of transformers with learnable token parameters to achieve progressive model scaling and reduce training cost compared with retraining from scatch of larger models with full data. The original matrix vector production is also replaced with the novel cross-attention between input token with tokenized parameters. Therefore, more token parameters can be easily added to well-trained smaller models incrementally due to flexibility of attention. The training cost is significantly reduced by 3x with similar or even better model performance. This paper proposes a interesting direction to scale LLMs and uses attention for almost all components in LLMs.

### Strengths
This paper proposes the novel TokenFormer that replaces the original linear layers in transformers with Pattention layers to enable more efficient and progressive model scaling without retraining from scratch. Pattention tokenizes the dense weights of query, key, value, and output layers with flexible and scalable token parameters. It then introduces cross-attention between input tokens with those token parameters. Instead of increasing the hidden dimension in transformers, TokenFormer achieves scaling by increasing the number of token parameters, incrementally adds new token parameters, and train all old and new token parameters with less training data. Therefore, it enables effectively reusing smaller model knowledge or weights and faster training of larger models with similar architecture. Experimental results show that the training cost of a 1.4B model is significantly reduced by training a 124M model initially and progressively scaling to 1.4B parameters, compared with training from scratch of a 1.4B model with 300B tokens.

### Weaknesses
1. In this paper, only results of scaling only up to 1.5B parameters are given. What are the complexity and effectiveness of scaling to larger scales such as 7B, 13B, 70B, or even more? In which case, the number of token parameters will increase multiple times and may be larger than token or model dimension.
2. The hidden dimension is relatively constrained to enable progressively scaling and reusing token parameters. Will it limit the capability of LLMs as FFN layers contain knowledge?

### Questions
same as weakness.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
A novel growing architecture called "tokenformer" is introduced. The idea is to replace linear layers in the transformer architecture with a cross attention mechanism where input dependent queries cross attend to key and value parameters. This framing allows for the architecture to accommodate new parameters concatenated to the original key and value parameters. The architecture and training method are validated empirically by pretraining a 124M parameter tokenformer and incrementally growing it to 1.4B parameters. The resulting model performs competitively on evaluations compared to other models of similar size pretrained from scratch.

### Strengths
The main strength of the proposed method in the paper is the flexibility of the architecture to accommodate additional parameters without jeopardizing the capabilities of the original model. Consequently there is no additional cost to "healing" the performance of the original model before continually training and allowing the model to exploit the added parameters. The experimental results reported in the paper are compelling and the key ideas are explained adequately clearly.

### Weaknesses
The presentation of the mathematical form of the "Pattention" operation can be improved - specifically, the notation in equations 4 and 5 are confusing - the function \Theta is described as a "a modified softmax operation for stable optimization of Pattention layer" when in fact the function used in subsequent sections and experiments isn't really a softmax and what's more the function name \Theta doesn't appear. Also it is unclear how equation 5 connects to equation 4, i.e. what exactly the function f has to do with \Theta. Perhaps it would be better to remove any reference to \Theta, and to solely describe the operation in terms of the function f, and to make explicit the choice of the specific form of f clear. Ideally a glossary defining all mathematical symbols in the paper would really help.
 In fact, the authors should make it clear that the structure of the Pattention operation can be seen as an MLP with standard activations: GeLU(RMSNorm(XK)V). The analogy with attention is interesting, but it somewhat obscures the key mathematical form of the operation - especially since there are no tokens (i.e. data) involved in the K and V parameters in Pattention. Also it isn't made clear how the V parameters are expanded - are they also padded with 0?

Also, in addition to the comparison with the Net2Net method, have the authors considered comparing to say the method in  arXiv:2409.12903v2 [cs.CL]  which also aims directly at growing transformer models?

### Questions
Have the authors considered a linear attention version of Pattention, i.e. a version without the gelu activation in the cross attention? Also, it seems that the tokenformer replacement of linear layers can be made in any architecture, i.e. not just transformers. Have the authors experimented with alternative backbone architectures?

### Soundness
3

### Presentation
2

### Contribution
4
