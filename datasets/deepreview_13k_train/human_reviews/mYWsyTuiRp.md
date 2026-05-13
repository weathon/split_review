# Analyzing Feed-Forward Blocks in Transformers through the Lens of Attention Maps

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Transformers are ubiquitous in wide tasks. 
Interpreting their internals is a pivotal goal. 
Nevertheless, their particular components, feed-forward (FF) blocks, have typically been less analyzed despite their substantial parameter amounts.
We analyze the input contextualization effects of FF blocks by rendering them in the attention maps as a human-friendly visualization scheme.
Our experiments with both masked- and causal-language models reveal that FF networks modify the input contextualization to emphasize specific types of linguistic compositions. 
In addition, FF and its surrounding components tend to cancel out each other's effects, suggesting potential redundancy in the processing of the Transformer layer

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed methods to analyzed the feed-forward blocks with regards to the input contextualization. It leverages the completeness property of existing norm-based analysis and the integrated gradient method.

The motivation to analyze the feed-forward blocks include the following:
1. The feed-forward blocks account for 2/3 of the layer parameters.
2. There is a growing interest in feed-forward blocks (new approaches focusing on the feed-forward blocks)
3. Previous work reported that feed-forward blocks perform some linguistic operations

Their experiments using masked-LM and casual-LM have shown that feed-forward blocks modify the input contextualization by amplifying specific types of linguistic compositions. Feed-forward blocks and layer normalization largely control contextualization. 

They also found that feed-forward block and other blocks cancel out each other's contextualization effects, which might indicates redundancy in the Transformer computations. (Feed-forward blocks' effects are weekend by surrounding residual and normalization layers.)

### Strengths
The paper is the first to analyze the whole feed-forward blocks, including the non-linear activation function. The non-linear activation function has been previously excluded from the norm-based analyses because it cannot be decomposed additively by the distributive law.

Combining the norm-based and the integrated gradients, the paper is able to quantify and visualize the effects of the whole feed-forward block.

The paper also provides detailed analysis that points to interesting properties of the feed-forward blocks. The discovery of redundancy might leed to new improvement of the architecture.

### Weaknesses
The author pointed out that the future work might be working with the latest large language model. While this is a valid direction, the paper could benefit from a more thorough discussion of the limitations of the current experiments. Specifically, the analysis is performed on BERT and GPT-2 models. It would be helpful to elaborate on how the findings might differ or be similar when applied to larger and more recent models, such as those in the OPT family. Exploring potential challenges or adjustments needed for applying the proposed method to significantly larger models would strengthen the paper.

### Questions
I think it might help the reader with a description or definition of contextualization.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a way of analyzing feedforward blocks (=FFB) [including residual connections and the layer norm layers intervening] extrapolating from the typical attention maps of the mid and late 2010s and the slightly more recent concept of a "refined" attention map that also considers the values and output projection (Equation 8). They call this base formulation ATB. The authors further extend this notion to incorporate FFBs. The FFB's nonlinearity which makes it additively non-decomposable [a-la linearity of expectation] is overcome by using the integration gradients paper [Sundararajan et al, 2017]. The three resultant formulations, which incorporate just the linear, thenceforth residual connections and layer norm are christened ATBFF ATBFFRES and ATBFFRESLN. The Pre-Layer-Norm variants are [like the post-LayerNorm one before] named likewise. 

The authors analyze a good variety of encoder only LM checkpoints in addition to a decoder only lM checkpoint [GPT2-117M] , which is also an instance of the pre-LN formulation.

The authors then interestingly proceed to analyze the contextualization changes caused by the FF block , both in terms of extent of change [based on flattening the pairwise values and taking Spearman Correlation of before-after], linguistic contextualization, as well as the dynamics.

### Strengths
- Their formalism is extended to both pre and post Layer Norm variants of transformers.
- Tested on a large variety of encoder LM architectures.
- Decoder-only architectures are also covered [though just one, i.e. GPT2-117M].

### Weaknesses
 - It would have been nice if the authors could have discussed and potentially also experimented with atleast one alternative formulation to IG, or atleast one of its variants [They do mention other formulations in B.1 Appendix but did not see further broaching of this angle beyond this]
- A marginal weakness but one nonetheless [and this is alluded to in future work], would have been nice to see this for a new-age LLM, of which some variants are available at lower or comparable parametrizations to GPT2-117M (e.g. OPT-125M)


### Questions
- What is the computational [and memory] complexity of generating these maps? This may sound nitpicky but with increasingly large LLMs which barely fit in the accelerator time and memory bounds whether at training or inference time, this can indeed become a factor and consideration in how widely this gets adapted.
- I know mechanistic explanation is a somewhat orthogonal paradigm of interpreting large transformer architectures, but it would be nice to have some comments on how this can relate or synergize with that paradigm [if at all]
- What is the effect of banded local attention [alternating banded local sparse and global attention] are a common part of the architecural recipe in many GPT3 or later LLMs so this would be a valuable insight to have.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to use attention map to analyze the effects of feed-forward blocks in transformers. Different from previous works which mostly focus on studying attention weights, the authors leverage norm-based analysis and integrated gradient methods on the the effect of feed-forward networks, residual connection, and layer normalization. Experiments done one different models (including different sizes of BERT and RoBERTa) and on different dataset (Wikipedia and Stanford Sentiment Treebank) suggest that feedforward networks (FF) amplify specific types of linguistic compositions, and its surrounding components tend to cancel out each other's contextualization effects.

### Strengths
1. This paper studies the contextualization effects of feed-forward blocks by leveraging attention maps, which were mostly ignored before (by only looking at attention weights). This presents new views on analyzing what each block in transformer is functioning.
2. The findings that FF and surrounding components tend to cancel out each other's effects are interesting. This may provide more perspectives in designing and training transformer models.

### Weaknesses
1. The paper suggests that because of the cancelled out effects in surrounding components there is "potential redundancy in transformer layers". However, there is not enough evidence to justify this claim (e.g., by training a transformer model removing some of the components). Without more experiments and results, it is not convincing what the conclusion of this paper is. More importantly, there is no systematic evaluation on the linguistic patterns (e.g., linguistic patterns distribution from different datasets on each layer) apart from some sampled amplified pairs. The results presented in Table 1 and Figure 5 are not evident.
2. The results on different BERT sizes, and different seeds do not seem to be always consistent (e.g., Figure 9, 10 in the appendix).

### Questions
1. Why is b set to a zero vector in equation 12?
2. Why do you think the patterns of changes between BERT and GPT-2 are quick different in each component (e.g., from Fig. 3)? What does this entail for different architectures?
3. Are results from Section 5 averaged across positions? Would position representation bias your findings?
4. How is the micro contextualization change (by subtracting a pre-FF attention map) in Section 5.2 different from measuring correlations?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on analyzing Feed-Forward (FF) blocks in the Transformer model, specifically regarding their impact on input contextualization. The authors utilize a refined attention map by combining norm-based analysis and the integrated gradient method, which offers completeness in understanding the FF block's behavior. In the experiment, Wikipedia excerpts and Stanford Sentiment Treebank v2 datasets are used, and the authors analyzed 11 11 masked LMs and one casual LM. The results show that FF blocks do modify input contextualization by amplifying specific linguistic compositions, such as subword pairs forming a single word. Furthermore, the authors discover that the FF block and its surrounding components tend to cancel out each other's contextualization effects, shedding light on the mechanism and suggesting redundancy in processing within the Transformer layer.

### Strengths
1. Analyzing Feed-Forward (FF) blocks in Transformer models through a refined attention map is novel, which combines norm-based analysis and the integrated gradient method. While previous research has explored the behavior of FF blocks, this study offers a unique perspective by leveraging the aforementioned techniques to gain a comprehensive understanding of their impact on input contextualization. 

2. The experiments conducted with masked and causal language models demonstrate the effectiveness of the approach in capturing the modification of input contextualization by FF blocks. The clarity and precision of the analysis enhance the quality of the research, ensuring reliable and valid results.

3. The paper is clear and easy to follow. The description of the refined attention map, norm-based analysis, and integrated gradient method is presented in a clear and understandable manner. The experiments and their results are well-explained, enabling readers to grasp the implications of FF block behavior on input contextualization.

### Weaknesses
1. To enhance the clarity of the proposed method, it would be beneficial to provide a running example that illustrates the step-by-step process. By walking readers through a concrete example, they can more easily grasp the methodology and its application.

2. To better ground the paper in the existing literature, it would be valuable to provide a more detailed and comprehensive literature review. By thoroughly reviewing relevant prior research, the paper can establish its position within the broader academic discourse and highlight its unique contributions.

### Questions
What could be the challenges of applying the proposed method in larger models, such as OPT, LLaMA, as mentioned in the future work?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
