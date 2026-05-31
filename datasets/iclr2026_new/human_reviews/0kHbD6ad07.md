## Human Reviewer 1

### Summary
This is a primarily theory paper that discusses decoder only transformers being injective. Specifically that each unique prompt maps to a unique last token embedding (from final transformer layer). Paper provides theoretical setup and justification for this argument under acceptable assumptions at initialization (Theorem 2.2) and post SGD-like gradient based training (Theorem 2.3). It is to be noted, that the theorems state how injectivity is very high probability (1 or near 1) event under stated assumption and not proven. For eg., paper discusses how collisions (two different input mapping to same last token representation) can still occur if an adversarial crafts data specifically so (end of Section 2). 

Paper also introduces a prompt recovery method from last token representation. The method "Sequential Inverse Prompt via ITerative updates" or SIP-IT. This method says that at each index position given a current + previous token hidden representation, check each token in vocab to see which will produce current index hidden representation (formal algorithm describe in Algorithm 1). The paper further discusses computational cost of SIP IT.

Review Note: Since the primary results are theoretical, I reduce my confidence to 3 in the reading and review.

### Strengths
- This is a unique and very science paper on LLMs, something we rarely see. Thanks for working on this. (I have what takeaways from this concern but more on that below).
- It cites most related work I know and use proper baselines in experiments.

### Weaknesses
The paper seems poorly organized, I felt lot of important results were pushed into appendix and main paper felt very repetitive at times. I have listed my main qualms in the questions section.

### Questions
1. What is "measure-zero parameter choices"? 
1. If you consider the prompt length progressively growing (i.e. --> \inf) with no upper bound, but the model width (i.e. embedding or hidden representation size) is fixed, then the model's representation has to be overloaded to some extent. This would challenge the injectivity directly since it won't be lossless anymore. So I would argue, in the limit, since the vector dim of hidden dim is capped, transformers are not injective and infact more and more lossy. What do the authors think?
1. Since the language follows power law of Zipf distribution [1], the words occurs as per an exponentially decaying frequency. One example, let us have LLM predict the next token on "Complete this: The quick brown fox jumps over the lazy [dog]" where "dog" is not part of prompt. If this exact phrase is used use with two distinct prompts (i.e. prefixes of this phrase), the next token would always be "dog" for most useful LLMs. Can you please run this as experiment with varied internet data used as prefix? If the next token prediction is same, I expect the last token to be super close if not identical and see if it meets the threshold of 1e-6 used in paper. There can be other examples as well, like cases where "should" is followed by "have" (assuming "should have" token is not part of vocab) with vastly different prompts. This is more inline with Zipfian distribution argument.
1. Why threshold of 1e-6?
1. Can you explain what exactly is the BRUTEFORCE method in Table 2?
1. "distinct prompts produce distinct hidden states under standard initialization and training" is good summary of the paper.
1. I think that under high precision, lookup of hidden activation against data is already expected. This steps from how deterministic models are. Can you clarify, under your threat model, the extractor of data have ONLY the last token embedding/representation with none of the prompt (and no knowledge of it's length either) or its access to each of previous token's embedding/representation as well? Because latter is kind of trivial (to me at least) and former is very difficult and the experiments might be convincing in that case. So yeah, the exact threat model is unclear to me, and kind of not stated clearly enough in the paper.

[1] https://en.wikipedia.org/wiki/Zipf%27s_law

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
The authors claim that a common thought is that language models are have a many to one relationship with regard to input and latent representation (respectively). The authors argue that language models are injective and that this suggests that there is an invertible relationship such that given a latent state, the input provided to arrive at this state is recoverable. 

The authors base the analysis on the belief that initialized transformers don't typically create collisions between prompts and that after a fixed number of training updates, the parameters have not been changed sufficiently to induce collisions. 

The authors propose a method to obtain the input to a language model. However, the method requires knowledge of the total last layer hidden state of the model for every substring of the prompt whose first token is the first token in the prompt.

### Strengths
This paper presents an interesting analysis I have not seen of the transformer architecture and convinced me that the transformer is often real analytic (though that depends on the choice of activation functions).

### Weaknesses
Terms like measure-zero and injective need to be defined. 

A collision must be defined. It's not sufficient to say that a collision didn't occur because a value differed in any way. Some bound must be placed on the distance between the output representations that constitutes a collision. 

Many activation functions are not real analytic functions. 

My understanding is that the zero set necessarily is measure-zero (given that the model is real analytic and we know the model is not the zero function). This doesn't seem to necessarily imply that no two inputs to the function will provide a similar output. I believe the authors intend for the reader to understand that the difference of two activations given dissimilar prompts is itself a real analytic function which then suggests that the difference between any two prompts whose value is zero is a measure-zero set. The problem with this logic is that it is possible that the difference between the last stage activations for two prompts is either the zero function or epsilon close to the zero function for some small epsilon without violating anything in the proof. 

My primary contention is that showing that the zero set is measure-zero is not sufficient to make the strong claim that there are no collisions. A collision should reasonably be considered anything within some small distance of zero rather than those items which have identical values given the reality of executing floating point operations a real machine.   

The SipIT method is trivial - given one knows the latent representation of every substring (which is less probable than simply knowing the input text to begin with), the algorithm can produce the substring by evaluating every possible token in this location. Further, the analysis of the algorithm seems to be either obscured or incorrect. For a prompt of length N and vocabulary of k, the algorithm will in the worst case require k^N time. This is exponential where the paper claims a linear time guarantee. Perhaps the paper meant linear with respect to vocabulary? But this is meaningless since the vocabulary is stationary and the input length is the changing factor.

### Questions
Decoder-only models are claimed to be a lossless representations of their input. This seems to be in contradiction to existing results that transformers are universal function approximators - a universal function approximation ought to be able to learn a many to one mapping if appropriate. However, function approximation is based on an epsilon bound. This seems to suggest that if instead of examining the size of the zero set, one were to examine the set which is epsilon close to the zero set, this would have no theoretic guarantee of being measure-zero. How does this not eliminate the practicality of the paper's analysis?

What degree of fidelity is necessary for this result to hold? If lower precision approximations are used, online batching for practical serving, or significant context information is present, these will create random noise which ought to obscure any such precise mapping as is necessary for the analysis to hold.

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper presents a strong theoretical study showing that decoder-only Transformer architectures are (almost surely) injective: different prompts map to distinct last-token hidden states. Building on this, the authors introduce SIPIT, an algorithm that recovers the exact input prompt from the final hidden state. The method is theory-driven and, across extensive experiments on a wide variety of models, the authors find no collisions, providing compelling empirical support for injectivity.

### Strengths
The main strength of the paper are as follows:

1. This paper makes a significant theoretical contribution by proving that standard decoder-only Transformer language models are almost surely injective – different input prompts will (with probability one) produce distinct hidden representations. The authors use real analysis to show that collisions (two different prompts yielding the same last-token state).
2. Building on the injectivity result, the novel algorithm (SipIt) to recover the exact input text from a model’s hidden activations with provable efficiency is introduced. As prior approaches could only approximate prompts via heavy training of inversion models, whereas SipIt achieves exact recovery by directly using the model's own representations.
3. The paper backs up its theory with comprehensive experiments on two models (a kind of old GPT-2 and more novel Gemma). The authors performed an exhaustive search for representation collisions using 100k prompts drawn from diverse sources, amounting to billions of pairwise comparisons. They report no collisions in any model or layer tested, distinct prompts always yielded distinct last-token embeddings, with clear separation margins.
4. The SipIt algorithm is shown to be not just theoretically sound but practically effective. On GPT-2, SipIt was able to reconstruct 20-token prompts perfectly (100% token-wise accuracy) in reasonable time, without any additional training or approximation.
5. By establishing invertibility as a fundamental property, the work has broad implications. It provides a sound basis for interpretability: knowing that the full input is encoded in the last-layer state means any failure to probe knowledge is due to method limits, not information loss.

### Weaknesses
I would highlight the following weaknesses of this paper:

1. Large vocabulary scaling. How does SipIt handle very large vocabularies (e.g., 100k+ tokens)? Does runtime grow linearly in practice, or do the gradient-based heuristics keep it manageable?
2. Uncertain theoretical result of not-analytic estimation. Most modern models use SwiGLU or SiLU activations. Since your proofs assume analytic activations, can you confirm that these fit the theory?
3. In continuation to the previous point, it is not clear, what happens with the quantized models. It seems that it can be the main source of the collision.
4. The experiments are provided for models of relatively small size, thus, we cannot asses what empirically happens with the larger number of parameters.

### Questions
My questions to the authors are as following:

1. Have you estimated, how SipIt works on datasets that were seen by the models during training, and on OOD samples, that were not observed by the model. Or even some random sequences of tokens? Does inversion speed or accuracy change compared to natural text?
2. Instruction-tuned models with identical answers: For instruction models (or even pre-trained ones) where many prompts lead to the same answer (e.g., "yes" or "no"), do the hidden states remain well separated? Have you measured how close they get?
3. Did you ever find prompts whose hidden states were almost identical? If so, what kind of prompts were they?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
The authors make a significant theoretical and practical contribution by rigorously establishing that standard decoder-only transformer language models are almost surely injective - meaning different input prompts map to distinct last-token hidden representations under common initialization and training regimes. The authors leverage real-analyticity to prove that collisions (non-injective behavior) occur only on a measure-zero set of parameters, and they further demonstrate that gradient descent preserves this injectivity. Building on this foundation, the paper introduces SipIt, a novel algorithm that efficiently reconstructs the exact input prompt from hidden activations with provable linear-time guarantees. This work bridges theory and practice, offering new insights into model transparency, interpretability, and safety.

### Strengths
The following strong points can be highlighted:
1. The theoretical analysis is rigorous, leveraging real-analyticity and measure theory to derive almost-sure guarantees.
2. The injectivity results are novel and counter widespread assumptions about information loss in Transformers.
3. SipIt is both theoretically grounded and empirically validated, demonstrating exact recovery with linear-time complexity.
4. Extensive experiments across multiple models (e.g., GPT-2, Gemma, Llama) confirm the absence of collisions in practice.
5. The paper clearly discusses implications for privacy, interpretability, and model auditing.

The paper’s core contribution is proving injectivity and enabling exact inversion, which addresses foundational questions in deep learning and has immediate relevance to interpretability and safety. The proofs are meticulous, and the experiments are comprehensive, spanning multiple model families and scales. The introduction of SipIt provides a tangible tool for future research, while the theoretical guarantees are robust and well-supported. These qualities align with ICLR’s emphasis on impactful, rigorously evaluated work.

### Weaknesses
Whereas the paper is technically solid, there are several weak points I would like to mention:
1. The scope is limited to decoder-only Transformers with analytic components, excluding architectures with non-analytic activations (e.g., ReLU) or encoder-decoder models.
2. The practical utility of SipIt, while theoretically appealing, is primarily evaluated in a noiseless setting; its robustness to quantization or approximate hidden states is less explored.
3. The discussion of related work, while adequate, could better contextualize how these results complement or challenge prior beliefs about Transformer expressivity.
4. Some proofs in the appendix are highly technical and may be inaccessible to readers without deep mathematical backgrounds.
5. It will be very interesting to analyze injectivity correlation with other internal transformer characteristics like anisotropy and intrinsic feature dimension using such frameworks as LLM-Microscope (https://arxiv.org/abs/2502.15007, https://github.com/AIRI-Institute/LLM-Microscope)

### Questions
1. How does SipIt perform under noisy or quantized hidden states, and can the theory be extended to account for such perturbations?
2. Could the injectivity results generalize to encoder-decoder Transformers or models with non-analytic components (e.g., ReLU)?
3. The paper claims gradient descent preserves injectivity - does this hold for adaptive optimizers like Adam, or only for GD?
4. Are there practical scenarios where the linear-time complexity of SipIt becomes prohibitive, e.g., for very large vocabularies?

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
6

### Confidence
5