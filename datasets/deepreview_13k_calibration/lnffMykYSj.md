# On the Long Range Abilities of Transformers

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Despite their dominance in modern DL and, especially, NLP domains, transformer architectures exhibit sub-optimal performance on long-range tasks compared to recent layers that are specifically designed for this purpose. In this work, drawing inspiration from key attributes of long-range layers, such as state-space layers, linear RNN layers, and global convolution layers, we demonstrate that minimal modifications to the transformer architecture can significantly enhance performance on the Long Range Arena (LRA) benchmark, thus narrowing the gap with these specialized layers. We identify that two key principles for long-range tasks are (i) incorporating an inductive bias towards smoothness, and (ii) locality. As we show, integrating these ideas into the attention mechanism improves results with a negligible amount of additional computation and without any additional trainable parameters. {Our {theory and} experiments also shed light on the reasons for the inferior performance of transformers on long-range tasks and identify critical properties that are essential for successfully capturing long-range dependencies.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a modification of the self-attention mechanism in Transformer architectures that facilitates the learning of long-range interactions. As global convolutional layers such as SSMs perform significantly better on long-range tasks, the authors' investigation of these models reveals that the convolution kernel of such models often have an exponentially decaying structure with additional smoothness constraints. This motivates the authors to introduce a modified attention mechanism called LaS-attention, which incorporates exponential decay and smoothing (implemented by average pool) along attention scores to incorporate these inductive biases into the architecture. In this way, the output of each attention layer is mostly only influenced by local interactions with varying degrees of locality, and long-range reasoning is captured hierarchically through compositions. This greatly increases Transformer generalization performance on the LRA benchmark and reduces the gap from global convolutional models. Ablation studies demonstrate the benefit of each proposed component. Additional experiment on sequential MNIST also show improvements with respect to this modification. To summarize the key observation, the paper claims that long-range reasoning is best implemented as compositions of mostly localized interactions as motivated by the SSMs, and demonstrated in the context of transformers.

### Strengths
- The writing of the paper is clear, and original as far as I know.
- The main strength of the paper is the intuition it provides; the reasoning is easy to follow and well-motivated, and it sheds light on the performance gap between SSMs and transformers on long-range tasks, which is a very important problem faced by Transformers.
- The hypothesis that long-range reasoning is best implemented as compositions of (mostly) localized interactions with exponentially decaying dependencies is well-motivated as supported by the investigation of the kernels of global convolutions, and then verified in the experiments by implementing a simple fix in the attention mechanism.

### Weaknesses
 - Methodology: Although the insights are novel, significant, and interesting to read, the methodological novelty is limited. The proposed modification is a simple modification 1) of the pre-softmax linear attention matrix by pointwise multiplication with an exponential decay term, and then 2) smoothing of the activated attention matrix. Especially that a similar modified version appeared in previous work in (Press et al. 2021), and its main difference from 1) is effectively that the distance matrix is exponentiated.
- Experiments:  I also found the experimental aspect somewhat lacking, as only LRA and sequential MNIST is considered, where on LRA there is improvement but not up to par yet with global convolutions. It would also be interesting to know if the proposed upgrade can provide improvements on other Transformer tasks, where it already performs as SOTA.

### Questions
#### Question 1:
The authors claim that "It is fairly straightforward to show that a single layer of a transformer ... can express any state-space
layer" and "each channel of the state-space layer incorporates a long convolution kernel K, which can be expressed via the attention matrices" 

I would like to ask whether the authors have any references for this claim or if they could provide a proof in the appendix? This seems highly non-obvious to me. I am aware of the previous work "On the Expressive Power of Self-Attention Matrices" Likhosherstov et al. 2021, which demonstrates that attention matrix can approximate sparse patterns, but I am not aware of more general results.


#### Question 2:

 In another paragraph, "the lack of generalization, caused by an unsuitable inductive bias that results in an unfavorable hypothesis class. In other words, the existing transformers underfit the long-range data." 

I have two problems with this sentence:
1) is that previously the authors said that " large transformers
can achieve near 100% accuracy", which is not a sign of underfitting but overfitting;
2) is that, although I am not sure about the claim in the previous question at all, if we assume it's true, then it basically says that the issue is not a problem with the hypothesis class in the classical sense, which is all the possible expressible models (although the set of reachable models by common initialization + training procedure combinations is another question, if this is what is meant then it should be clarified).
It seems to me that the issue is either - as the authors stated - that decomposing long-range learning into a series of locality pronounced layers helps in the training procedure for generalizability, i.e. this constraint mitigates overfitting by restricting the hypothesis class rather than enlarging it. I wonder if the authors have any thoughts on this? This is an interesting question.

#### Question 3
Another question is whether the authors have any intuition about why the exponentiation of the distance matrix helps the attention compared to Alibi? This seems weird to me because applying the decay matrix before the softmax decreases large query-key dot-product values as intended, but negative dot-product values are actually increased, which actually degrades the ability of the model to reduce the dependence on certain tokens. I wonder if this is a desired effect due to some implicit regularization phenomenon of being less likely to attend to a very small select few tokens, or if this is might be harmful?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper suggests modifying the attention matrix in transformer layers, drawing inspiration from models like S4, with the aim of enhancing the transformer's capacity to generalize more effectively in long-range contexts.

The authors stress the significance of two main concepts: smoothness and some kind of locality. For smoothness, they implement 1-D average pooling on every row of the attention matrix. For the locality (exponential decaying of attention), an element-wise multiplication is applied between the attention matrix at each head and a locally decaying matrix (not learnable).

LaS the, the proposed method, is evaluated on the LRA benchmark and vectorized MNIST (sequential and permuted) and compared with a few different transformer variants as well as S4, Mega, and LSTM. LaS seem to achieve the best performance among Transformers.

### Strengths
- The proposed method is simple and achieves better results on LRA tasks compared to other transformers.
- Ablation experiments indicate the importance of both components of LaS attention (exponential decay of attention scores and smoothness)

### Weaknesses
 - While experiments that study the impact of context length and sample size are intriguing, interpreting the results is challenging without comparing the patterns to any other baseline. For instance, in the experiment where you restrict the context window size to examine LaS's dependence on long-range dependencies, do we have insights into how a standard transformer might be influenced by a reduced context window size?
- I believe the arguments about expressivity limitations and optimization challenges might be wrong.
   - For instance, a model can fit the training data without necessarily capturing long-range dependencies, simply by leveraging spurious features.
   - For example, I believe there are elements within the transformer block where some kind of diminishing effect might transpire as the context window becomes exceedingly long.
- I am not convinced by the arguments about smoothness and locality as inductive biases. The paper does not provide sufficient evidence to support the claim that these biases are the key to improving the model's capability to handle long-range dependencies. The connection between these biases and the hierarchical nature of long-range dependencies is not clearly established.
- The experiments on language modeling are not sufficiently detailed. The paper mentions that smoothness negatively affects perplexity, but it does not provide a thorough analysis of why this happens. It is not clear if this is due to the specific implementation of the 1D average pooling or if it is a more fundamental limitation of the approach. The paper should also explore the impact of different smoothing techniques.
- The paper mentions that they have tried learning the biases and different patterns, but they did not observe any major improvements. It would be beneficial to include these results in the paper to better justify the proposed solution. Without these results, it is hard to assess the significance of the proposed method.

### Questions
1. Could you explain how one should read Figure 1? What is the x-axis? What is the y-axis?
2. Can you elaborate a bit more on the arguments about smoothness and its relationship to improving the model's capability to handle long-range dependencies?
3. Same question as above about locality! What's the intuition?
4. How does the Transformer architecture perform on other tasks (e.g., standard language modeling or typical image classification)? What do we sacrifice by biasing the models towards solutions that generalize better in long-range context settings?
5. Have you considered learning the biases or explored applying different patterns? How does LaS compare to a model like Synthesizer?
6. What does the final attention score matrix look like?
7. Are there any interactions or side effects from the positional encoding?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates how transformers use long-range dependencies.

The thesis of the paper is that transformers suffer from lack of generalization. They propose several inductive biases to help. Namely, smooth and exponentially decaying kernels. They are inspired by prior work in transformer variants like state-space layers.

They invent a method called Local and Smooth attention (LaS) to test their hypothesis and achieve strong results in Long Range Arena (LRA) and Sequential MNIST. The local comes from weighting with what they call Exponentially Locally Decaying (ELD). The smooth comes from a convolution operator that does average pooling.

They do various ablations to further bolster their claims about generalization and the various operations in LaS.

### Strengths
The empirical part of the paper is strong. The method does well and the ablations support the hypothesis. They investigate the generalization claim by manipulating context length and dataset size.

The refutation that transformers lack expressiveness or suffer from optimization problems is convincing.

Figure 2 makes the method very clear.

### Weaknesses
The section on identifying common design choices of prior work feels a bit handy wavy. Perhaps could be better presented in a table.

There is an error either in Equation 3 or Figure 2. They transpose the softmax and average pooling. My guess is the error is in Equation 3.

There seems to be only empirical evidence about why seemingly "unintuitive" methods work. Some theoretical justification would make the paper stronger.

What is meant by "necessary conditions for achieving success in long-range tasks"? Is it meant in the strict mathematical sense? If so, I would expect to see a proof along the lines of success implies these conditions.

### Questions
What is meant by "necessary conditions for achieving success in long-range tasks"? Is it meant in the strict mathematical sense? If so, I would expect to see a proof along the lines of success implies these conditions.

To further support the lack of generalization due to underfitting hypothesis, have you tried getting more data beyond what's in the LRA dataset?

Since this mechanism works in a causal manner, how well does it perform in decoding tasks like language modeling or translation?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an architectural modification for the transformer's attention mechanism, which allows it to generalize better to longer inputs. The authors argue that the key principles for long-range tasks are (1) inductive bias toward smoothness; and (2) locality. By modifying the transformer's attention with these principles in mind, the authors achieve empirical gains in the Long-Range Arena (LRA) benchmark.

### Strengths
1. Modifying the transformer architecture to better support long-range inputs is an important direction of research.
2. The empirical gains look significant, but I am not sure they were compared to the right baselines.

### Weaknesses
1. The paper contains many assumptions that are inaccurate or unjustified. For example:
>The lack of effectiveness of transformers in this setting [long context]

implies that transformers are ineffective, in general, on long inputs. I am not sure that this is the case - I agree that transformers could be improved, but the main problem seems to me that most transformers cannot even process long inputs. When the input *does* fit in the transformer's context window, most results that I've seen are not that bad. In other words, claiming that "transformers are ineffective in long context" requires some experiments and justification, to show exactly what the authors mean, instead of relying on one paper who said so a few years ago.

Another inaccurate and unjustified claim appears in Section 3:
>the observed sub-optimal performance of transformers on long-range tasks does not arise necessarily from issues of optimization or expressiveness, which are inherent to the architecture. Rather, it is a matter of generalization

This claim assumes that transformers are sub-optimal (compared to what?) on long-range tasks (which?), and claims that the issue is generalization. This is a bit of a vacuous claim, since "Generalization" can contain anything. If the model reaches a zero training loss but is worse at test time, is that generalization? Is that the kind of "generalization" that the authors refer to?

The paper contains further inaccurate claims like:
>Long-range dependencies are often associated with optimization issues, such as exploding and vanishing gradient problems.

which were not justified and references were not provided. I agree that in the past RNN era, this was indeed the common belief. But can this claim be said on "long-range dependencies" in general?

As a final example for inaccurate and unjustified claims, Section 3 says that:
> on the LRA benchmarks including the validation set, large transformers can achieve near 100% accuracy,

but then says that:
> the existing transformers underfit the long-range data.

Don't these two claims contradict each other? If not, there should be provided some justification, numbers, and references.

2. Motivation - the authors motivate their solution with the assumption that:
>smooth and exponentially decaying kernels are associated with a long-range inductive bias

This "axiom" isn't clear - I am not sure what exactly the authors mean by "smoothness". And in general, why? Why would *decaying* any kind of attention would improve any long-range modeling? 
I was not convinced that these are indeed related to the problem/solution.

3. Evaluation - the experiments section does not provide any details regarding the underlying model - number of layers, number of parameters, whether it was pretrained, etc. I am also not sure what is the right baseline - Table 1 lists a variety of baselines, but are they comparable in terms of sizes? Which of them is the baseline that has the exact same number of parameters and layers, but without the proposed attention modification?

4. Clarity - there are many parts of the paper which are unclear. For example, the introduction says:
>We discern two simple yet significant conditions (i) an exponential decaying positional structure, and (ii) a regularized smooth global operator. 

>furthermore (iv) present an SL-chunk variation

At this point in reading the paper, this is meaningless to me.
As another example, the next Background section mentions many terms, but completely meaningless for the uninformed reader. For example:

> An emerging approach implicitly defines the convolution kernel via a learnable function (Romero et al., 2021). Namely, the kernel kh
i (filter) at position i and channel h is defined by a function fh such that fh(i) = ki.

For a reader who did not read the paper by Romero et al. (2021), this doesn't mean anything.
The rest of the Background section continues to cite dozens of papers, while these citations *hurt* the readability of the paper if the reader had not read the referenced papers. Later, Alibi (Press et al., 2021)  is mentioned, along with its equations (Equation 1), without any elaboration, leaving the reader to try to understand the equations and their notations, while Alibi is completely irrelevant to the proposed approach.

Further, some figures in the paper are not explained nor elaborated. Figure 1, for example, shows "Examples of random kernels of several long-range layers", without mentioning (1) what does the x axis mean; (2) what is the y axis; (3) what are the different colored curves, and what should the reader understand from this figure.

### Questions
### Questions

1. What are the number of layers, number of parameters, was the model pretrained, etc.?
2. All tasks in the experimental section are somewhat synthetic. Do the authors' conclusions hold for **text**-based tasks as well, e.g., long-document summarization, long-document QA, etc?
3. Which of the baselines in Table 1 is the baseline that has the exact same number of parameters and layers, but without the proposed attention modification?
4. The models that "rely on global convolutions" in Table 1 perform significantly better than the proposed LaS attention model. If so, what is the benefit of using the proposed LaS model? Who is expected to benefit from using LaS?

### Summary

While the high-level idea is interesting, I feel like this paper suffers from too many weaknesses (detailed above). I thus recommend rejection at this time, and hope that the authors would improve writing and justify their motivation in the future.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
