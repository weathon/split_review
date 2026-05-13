# Selective induction Heads: How Transformers Select Causal Structures in Context

- Decision: Accept
- Scores: 6, 6, 6, 8, 5

## Abstract
Transformers have exhibited exceptional capabilities in sequence modelling tasks, leveraging self-attention and in-context learning. Critical to this success are induction heads, attention circuits that enable copying tokens based on their previous occurrences. In this work, we introduce a novel synthetic framework designed to enable the theoretical analysis of transformers’ ability to dynamically handle causal structures. Existing works rely on Markov Chains to study the formation of induction heads, revealing how transformers capture causal dependencies and learn transition probabilities in-context. However, they rely on a fixed causal structure that fails to capture the complexity of natural languages, where the relationship between tokens dynamically changes with context.  To this end, our framework varies the causal structure through interleaved Markov chains with different lags while keeping the transition probabilities fixed. This setting unveils the formation of *Selective Induction Heads*, a new circuit that endows transformers with the ability to select the correct causal structure in-context. We empirically demonstrate that attention-only transformers learn this mechanism to predict the next token by identifying the correct lag and copying the corresponding token from the past. We provide a detailed construction of a 3-layer transformer to implement the selective induction head, and a theoretical analysis proving that this mechanism asymptotically converges to the maximum likelihood solution. Our findings advance the theoretical understanding of how transformers select causal structures, providing new insights into their functioning and interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new synthetic task based on interleaved Markov Chains in order to better mimic the complex token interactions in natural language. The authors come up with an algorithm to solve this task with a 3 layer attention-only (disentangled) transfomer. Notably, the authors also show that when they train a similar model with gradient descent, it learns similar mechanisms (apparent by comparing the attention maps).

### Strengths
* The paper is well written, I learned something.
* Introduces a new synthetic task and discusses how transformers can successfully solve it with an interpretable mechanism. The authors also show that the same mechanism is learned when training with gradient descent, which I found most interesting.

### Weaknesses
 * I have no major concerns apart from the utility of this insight in the broader language (or sequence) modeling tasks that we actually care about. See questions below.

 * The synthetic task of modeling interleaved Markov Chains is interesting and definitely a step in the right direction. But do you think it is yet a good enough proxy to model the complex dynamics of token interactions? In language modeling, often these interactions are informed by the semantics of the tokens and the context. Whereas I don't think here the token meanings are important in any way.
    
* In my opinion, one of the things that made the induction head work interesting is that they found heads behaving in similar ways in actual large language models which were trained on real textual data. I am not really sure if the same can be said about the selective induction head circuit you found here. If this is something that can only be observed in a synthetic task, do we really care about it? Or, do you have any hypotheses about how selective induction heads might manifest in models trained on natural language texts? And, how do you plan to investigate this hypothesis (maybe in future work)?

* In Section 5 you mentioned that a model when trained with less than k attention heads per layer was also able to successfully solve this task. This either suggests a completely different algorithm or is indicative of head-level superposition of information. Can you get more insights into this by looking at the attention maps?
    * Also, have you tried with more than K heads per layer? I wonder if it would further break the mechanism. Or, you might start seeing duplicate heads behaving in similar ways.
    * A similar question about the number of layers --- You need at least 2 layers to form the usual induction head behavior. Do you really need at least 3 layers for "selective" induction heads? Also, what happens with more layers? Do more layers introduce more "steps"? Or, some of the layers essentially become identity functions?

### Questions
* The synthetic task of modeling interleaved Markov Chains is interesting and definitely a step in the right direction. But do you think it is yet a good enough proxy to model the complex dynamics of token interactions? In language modeling, often these interactions are informed by the semantics of the tokens and the context. Whereas I don't think here the token meanings are important in any way.
    
* In my opinion, one of the things that made the induction head work interesting is that they found heads behaving in similar ways in actual large language models which were trained on real textual data. I am not really sure if the same can be said about the selective induction head circuit you found here. If this is something that can only be observed in a synthetic task, do we really care about it? Or, do you have any hypotheses about how selective induction heads might manifest in models trained on natural language texts? And, how do you plan to investigate this hypothesis (maybe in future work)?

* In Section 5 you mentioned that a model when trained with less than k attention heads per layer was also able to successfully solve this task. This either suggests a completely different algorithm or is indicative of head-level superposition of information. Can you get more insights into this by looking at the attention maps?
    * Also, have you tried with more than K heads per layer? I wonder if it would further break the mechanism. Or, you might start seeing duplicate heads behaving in similar ways.
    * A similar question about the number of layers --- You need at least 2 layers to form the usual induction head behavior. Do you really need at least 3 layers for "selective" induction heads? Also, what happens with more layers? Do more layers introduce more "steps"? Or, some of the layers essentially become identity functions?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents an in context learning task that requires a model to infer what type of markov chain was used to generate the input tokens in order to predict the next token. Then it constructs a solution to this task with a three layer transformer that involves a particular type of attention head they call selective induction heads. In the final two pages an experiment is reported on where a three layer model is trained on this task and then the attention head patterns are visualized. The attention pattern in the constructed model and the trained model is highly similar, suggesting that the very same solution is achieved in both cases. 

The paper is well written, and great care is taken in the presentation of the technical details to the theoretical solution. However, the task here is pretty idiosyncratic and a specialized transformer architecture is used to make the analysis easier to perform. The connection to actual in-context learning scenarios seems like it might be a bit fraught, I’m not sure how much closer a lagging markov chain is to natural language than a normal markov chain. I also get the feeling that moving to a standard transformer architecture would make things a lot less pretty...

Generally, I am amenable to technical papers that deal with toy settings, so I think the core content of this paper is solid. However, I don’t think that the title and framing of the paper is accurate. The process of selecting causal structures in context is incredibly general and complex, and selective induction heads are just a step in the direction of understanding how in context learning occurs. I think the title and framing needs more transparently communicate that this work is largely theoretical. How you do this is totally up to you and I’m willing to raise my score if you address this concern.

The attention pattern visualization is remarkably similar between the constructed model and the trained model, so while this analysis is correlational, I would expect the causal claims to follow as well. That being said, you might wonder whether a standard transformer model trained on this task implements basically the same solution (I assume that the attention head pattern is different, otherwise you would have included results). I think the right way to understand this involves causality, and all the work that you reference comes from an AI safety mechanistic interpretability background, but there has been loads of work done in causal analysis of neural networks. Here are some review/history papers to check out and get some citations from:

https://arxiv.org/abs/2408.01416

https://arxiv.org/abs/2301.04709

https://arxiv.org/abs/2410.09087

### Strengths
See review

### Weaknesses
This paper presents an in context learning task that requires a model to infer what type of markov chain was used to generate the input tokens in order to predict the next token. Then it constructs a solution to this task with a three layer transformer that involves a particular type of attention head they call selective induction heads. In the final two pages an experiment is reported on where a three layer model is trained on this task and then the attention head patterns are visualized. The attention pattern in the constructed model and the trained model is highly similar, suggesting that the very same solution is achieved in both cases.

The paper is well written, and great care is taken in the presentation of the technical details to the theoretical solution. However, the task here is pretty idiosyncratic and a specialized transformer architecture is used to make the analysis easier to perform. The connection to actual in-context learning scenarios seems like it might be a bit fraught, I’m not sure how much closer a lagging markov chain is to natural language than a normal markov chain. The use of a disentangled transformer architecture, while simplifying analysis, raises concerns about the generalizability of the findings to standard transformer architectures. It's unclear if the observed attention patterns and the proposed mechanism of selective induction heads would manifest in the same way within a standard transformer, which has a more complex interaction between query, key, and value matrices. I also get the feeling that moving to a standard transformer architecture would make things a lot less pretty...

Generally, I am amenable to technical papers that deal with toy settings, so I think the core content of this paper is solid. However, I don’t think that the title and framing of the paper is accurate. The process of selecting causal structures in context is incredibly general and complex, and selective induction heads are just a step in the direction of understanding how in context learning occurs. I think the title and framing needs more transparently communicate that this work is largely theoretical. How you do this is totally up to you and I’m willing to raise my score if you address this concern.

The attention pattern visualization is remarkably similar between the constructed model and the trained model, so while this analysis is correlational, I would expect the causal claims to follow as well. That being said, you might wonder whether a standard transformer model trained on this task implements basically the same solution (I assume that the attention head pattern is different, otherwise you would have included results). I think the right way to understand this involves causality, and all the work that you reference comes from an AI safety mechanistic interpretability background, but there has been loads of work done in causal analysis of neural networks. Here are some review/history papers to check out and get some citations from:

https://arxiv.org/abs/2408.01416

https://arxiv.org/abs/2301.04709

https://arxiv.org/abs/2410.09087

### Questions
See review

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces a new circuit in Transformers, “selective induction heads” that enables transformers to determine the lag in causally-structured data as per the context (“in-context”) and apply the induction head copying mechanism. A 3-layer disentangled Transformer model is constructed to achieve this, with specifically designed purposes for each layer towards identifying the correct lag: capturing the transition probabilities, aggregating the probabilities, and summing the probabilities to select the lag. Empirical validation on synthetic data shows that the constructed transformer can achieve performance close to the theoretical maximum likelihood estimator across settings (contiguous, non-contiguous, many lags, single head), and the attention maps verify that the layers are performing the functions they were designed for.

### Strengths
* The general setting is defined in a clear manner, and intuitively demonstrated through Figure 1. 
* The 3-layer disentangled transformer perspective is an interesting construction that is well motivated by designing specific purposes for each layer; the preliminaries are also explained quite well. 
* The paper is written clearly despite it being admittedly challenging to follow some of the notation — the visualizations are immensely helpful to follow the construction in Section 4, as well as the various special cases examined in Appendices E, G, and H. These appendix sections were greatly appreciated, as they thoroughly flesh out the nuances in construction for each such setting.
* The attention maps serve to reinforce the model construction; each layer serves their respective intended purposes.

### Weaknesses
 * More discussion in the empirical validation would be useful, to explain the findings and walk through the plots in Figure 4. For instance, it would be beneficial to explain the difference between the 1 head (1H) and 3 heads (3H) cases, as the proposed construction scales the heads with the number of lags, and detail the implications of these differences. Specifically, the performance differences between the single-head and multi-head settings are not thoroughly explored, particularly in relation to the number of lags being considered. The paper would benefit from a more detailed analysis of how the model's performance changes as the number of heads deviates from the number of lags, and why this occurs.
* The scalability of the method remains unexplored; that is, what are the empirically-realized sets of lags that appear in real-world tasks, and how do they vary across tasks? Many natural language reasoning tasks have a non-linear and more complex causal structure, and it would be good to see how / whether this method extends to such tasks, beyond synthetic ones. The current synthetic data experiments, while useful for isolating the mechanism, do not address the challenges of real-world data, where causal relationships are often noisy, non-stationary, and involve multiple interacting factors. The paper should discuss the limitations of the current approach in handling such complexities.
* While Proposition 1 is defended by construction (and the empirical findings), it is unclear how Claim 1 is supported empirically (although it is acknowledged that this claim has yet to be formally proven) through the results in Section 5. The empirical support for Claim 1 is not clearly tied to the results presented. A more detailed explanation of how the experiments validate this claim, even if it is not formally proven, is needed. The connection between the empirical results and the theoretical claim should be made more explicit.

### Questions
* Continuing from the note on scalability in the “weaknesses” section: is it necessarily true that there is such an idea as a fixed “correct lag” that ever appears in real data? This is partially addressed in the many lags and non-contiguous lags setting, but appears to require further generalization for such a transformer model to be truly useful (for example, in natural language tasks).
* Are there any core (architectural) considerations that might need to be made for scaling to larger data, from an efficiency standpoint? How many heads would be needed, and can this be reduced? This is addressed to some extent in the many lags setting in an Appendices G and H.

### Soundness
3

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
2

### Summary
The paper mainly extends the work of Nichani et al. (2024). Nichani et al. show that Transformers can learn causal structures of Markov chains and estimate transitional probabilities via In-Context Learning (ICL). The current works investigates whether Transformers can learn causal structures from a more complicated variant of that task - particularly from interleaved Markov chain, where a prediction at position t, is not dependent on the state a t-1 necessarily, but some state at t-k. So in this context, Transformers have to not only learn the transition probabilities and Markov chain dependencies, but also have to learn to select the right Markov chain for prediction at t ignoring other interleaved ones that are not relevant for prediction at t. 

The paper makes a theoretical construction based on Disentangled Transformers to show how Transformers, in principle, can utilize in-context examples to solve the task. The paper then empirically investigates and show that Transformers can learn variants of the task through gradient descent.

### Strengths
1. A reasonable extension of a prior publication (Nichani et al. (2024)). 
1. Provides deeper insight into ICL capabilities of Transformers. 
1. The task could be another sanity check for alternative architectures to test whether they can do what Transformers can or not.

### Weaknesses
1. The scope of impact may be a bit limited. While the experiments and construction do deepen our insights to ICL, they don't seem to provide a fundamental shift in our understanding, and may not translate into being particularly informative for specific practical decisions. But this is a more subjective point and I am not factoring this too strongly for the evaluation.

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the ability of transformers to identify the causal dependency in Interleaved Markov Chains. The authors start by introducing Interleaved Markov Chains as a Markov Chain with a random lag. Then, the authors give an explicit construction to show a transformer can implement a predictor for the in-context selection of interleaved Markov chains. Finally, the authors train a transformer on interleaved Markov chains and show that the transformer not only solves the detection task but also exhibits similar attention maps to the theoretical construction given by the authors.

### Strengths
* The paper provides strong evidence that transformers can identify causal structures in the context.
* It is nice to see that the theoretical construction can match the experimental findings in a controlled experiment.
* Some slightly more general cases are discussed: Single-head transformers & Non-contiguous lags.

### Weaknesses
 * The scope of this study is a bit narrow. The authors only discussed the detection of interleaved Markov chains
* It is unclear whether an LLM can detect interleaved Markov chains. Maybe the authors can do some inferences on open-source models to verify this.
* It remains uncertain whether an LLM can retain its ability to detect interleaved Markov chains when trained on data that is unrelated or only loosely related to such structures. Given the artificial nature of this task, it's more effective to assess detection ability in an out-of-distribution setting rather than through direct training on the same task.

### Questions
* Do you have any recommendations for an LLM to improve its understanding and learning of causal structures?

### Soundness
3

### Presentation
3

### Contribution
2
