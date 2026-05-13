# Linear-Time Sequence Modeling with MLPs

- Decision: Reject
- Scores: 8, 5, 6

## Abstract
We present Causal Relation Networks (CausalRNs), the first all-MLP sequence modeling architecture with linear-time parallel training.
To enable autoregressive modeling, we made Relation Networks (RNs) equivariant and causal through relaxation and masking.
Contrary to the earlier belief that RNs are quadratic-time, we show that when using exp(x) as the activation function, any RN is linear-time, fully parallelizable, and numerically stable.
Our derivation spontaneously gave rise to familiar design choices adopted by state-of-the-art architectures, e.g. exponential gating and state expansion.
Such duality provided a new perspective, from which we not only validated popular design choices, but also discovered new design considerations.
Experiments on autoregressive language modeling and image classification showed CausalRNs to be comparable to Linear Transformers.
The quadratic variant of CausalRNs achieved perfect retrieval on the copying task, which was previously only possible with Transformers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The main contribution of the paper is to extend Relation Networks to be both causal and stackable by providing a novel (to my knowledge) new building block they call Bidirectional Relation Networks.  They compute pairwise functions of previous blocks in a causal manner, with a quadratic time like a normal transformer.  They then go on to show that BiRNs can be computed in linear time by choosing the activation function to be an \exp.  

However, this linear time version makes certain tasks (like copying string) harder, so they introduce a quadratic variant where they add pre-activation normalization to the pairwise computations, which makes the computational cost be quadratic again but increases the performance on recall tasks like copying.  

They perform 3 ablations to show that the pre-normalization activation is important (that increases the cost to be quadratic), that the post-normalization activation is important and that the exponential function is the best normalization function.  They finally demonstrate reasonable performance on text prediction and image classification.  

Other interesting observations include the similarity of the training curves to that of a transformer, and the interpretability of their network in the image domain due to their normalization.

### Strengths
Introducing simplified new architectures can help elucidate the performance of the most advanced systems; for example the match between the training behavior of the transformer and their model is very interesting.  Newer, simpler architectures can also be more amenable to theoretical analysis and potentially be more interpretable.  Another interesting future question is if the model can perform ICL like a transformer.  

Additionally, new architectural units can also be used in conjunction with existing systems (e.g., alternate with attention units), which may further improve global performance.  Overall, it’s important and useful to explore the space of powerful, simplified models, like the authors have done.

### Weaknesses
Performance was quite a bit weaker, and the scaling characteristics are unclear.  Naturally, if the performance had been SOTA that would have been very impressive but that is highly unlikely for a new architecture without more optimization.  

There isn't quite enough detail of the entire architecture to be able to easily recreate it in their experiments.  Was this a replacement for the attention layer, was no other layer used then 12 of the BiRN layers?  They mention they can use residual connections - were they used?  What tokenizer was used for the text experiment?  Apologies if this was mentioned somewhere and I just missed it.  

Minor corrections
* Equation 8 should be p_i + q_j
* Lines in Figure 3 aren’t red-green colorblind friendly, please change.  
* (minor) Be clearer in the experiments when cost is exponential vs. linear.

### Questions
* See the weakness section for questions about the setup.  
* 3c seems surprising - I got from the text that the advantage of the exp is computation, vs. training time or accuracy.  Any comment on why the exp is more efficient for training?  Would something simple like a bias term help
* Was positional encoding used in the text/image tasks?  In general, there isn't quite enough detail in the 
* What was the relative computational cost in the experiments vs Transformer and Mamba?  
* I’m confused by the state expansion experiment - clarifying within the paper or an appendix would be useful.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents Causal Relation Networks (CausalRNs), a novel approach to sequence modeling with MLPs. The key innovation is using exponential activation functions to reduce complexity from quadratic to linear by exploiting distributive properties when mixing sequence elements. The architecture combines dot products between activations with causal masking and normalization. Empirical results are given which show that CausalRNs do not outperform transformers, linear transformers, or Mamba in accuracy or perplexity, but do perform better than linear transformers in terms of handling long context.

### Strengths
1. Clear and logical presentation, particularly in deriving CausalRNs from relation networks.
2. Well-motivated choice of exponential mapping and normalization methods.
3. Thorough ablation studies demonstrating necessity of each architectural component for CausalRNs.
4. Clear evaluation methodology in the experimental section.

### Weaknesses
1. The novelty of the architecture is not obvious, particularly given its similarity to linear attention mechanisms. The paper doesn't sufficiently differentiate the method from prior work on linear attention variants. The basic equation seems quite similar to equation (9) in the linear transformers paper, where the output at position \(j\) is given by a partial sum up to position \(j\). It would be very useful if the authors could clarify how their work differs from linearized attention.
2. The empirical results show significant limitations. The model consistently achieves higher perplexity than comparable architectures. Meanwhile, no clear computational or memory advantages are demonstrated.
3. Overall, there is no clear demonstration of a useful contribution. Some improved in-context learning capabilities are suggested by Figure 6 and warrant deeper investigation which is not given in the paper. More generally, there are no compelling use cases presented where CausalRNs would be the preferred architecture. The theoretical connections to infinite-width networks are mentioned but not really developed.

### Questions
1. What are the concrete benefits and practical use cases where CausalRNs would be preferred over existing architectures?
2. Beyond being an "interesting research object," can the authors suggest ways in which this could advance our theoretical understanding of sequence modeling?
3. How does this architecture fundamentally differ from linear attention mechanisms, and is it a special case of linear attention?

EDIT: After reviewing the authors' response, I'm happy to see they have addressed my question about linear attention. I now agree that it is materially distinct from linear attention. I have raised my rating to reflect that. However, I would still not champion acceptance, since the 'research questions' that the authors raise come off as a somewhat random grab-bag of results--there isn't necessarily a clear scientific question or area of study, just some disconnected results.

### Soundness
4

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present an extension of Relation Networks, dubbed CausalRNs. Authors position CausalRNs as a tool to better understand sequence modeling rather than as a replacement for existing architectures (SSMs, Transformers). They employ clever tricks such as normalization approximation and exponential activation to build CausalRNs. Experiments are conducted on WikiText, CIFAR and a copying task to demonstrate that CausalRNs CAN model sequences albeit not as effectively as Transformers.

### Strengths
1. The proposed architecture is novel, interesting and it pushes Relation Networks one step further.
2. They scale better than transformers on copying task according to Figure 6

### Weaknesses
1. Imho, a major weakness of paper is a mismatch between their positioning and their experiments - authors wish use CausalRNs to study sequence modeling architectures, but present limited insights/ablations against Transformers. Following are a few examples, hopefully actionable:
1A. Authors claim that CausalRNs are worse than transformers because they do not have multi-head attention, tensor cores, no I/O aware. At least the first two limitations can be applied to Transformers - remove the MHA and train on CPUs, compare against such a transformer.
1B. Related to Figure 6, Authors claim that CausalRNs converge faster than transformer but provide no explanation. This could be interesting because Figure 5 shows a similar phenomenon where Transformer loss is higher. Some interesting questions we could ask: Is the gain in convergence mostly in warm-up, or does it sustain through training (i.e., are Causal RN's somehow more data efficient?)

2. One of the benefits of CausalRNs is being able to stack them/make them deeper, or use residual connections - I'd like to see some ablations to see how these models improve with increasing depth.

### Questions
Typos?

1. Eq 8: q_j instead of q_i?

### Soundness
3

### Presentation
3

### Contribution
2
