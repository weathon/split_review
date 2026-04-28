# Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Large language models have been successful at tasks involving basic forms of in-context reasoning, such as generating coherent language, as well as storing vast amounts of knowledge. At the core of the Transformer architecture behind such models are feed-forward and attention layers, which are often associated to knowledge and reasoning, respectively. In this paper, we study this distinction empirically and theoretically in a controlled synthetic setting where certain next-token predictions involve both distributional and in-context information. We find that feed-forward layers tend to learn simple distributional associations such as bigrams, while attention layers focus on in-context reasoning. Our theoretical analysis identifies the noise in the gradients as a key factor behind this discrepancy. Finally, we illustrate how similar disparities emerge in pre-trained models through ablations on the Pythia model family on simple reasoning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work theoretically examines a phenomenon regarding the purpose of the feedforward and attention layers of a Transformer model, relative to the reasoning and knowledge learning tasks. It attempts to provide an explanation for the difference through a generic noise token, demonstrating that the feedforward layers store noise while the induction heads in the attention layers are insensitive to the noise tokens.

### Strengths
* The paper sets out to address a clear objective, and designs a 2-layer model that enables a theoretical analysis of the phenomenon of interest, then reduces to a 1-layer model for theoretical analysis, revealing important, mathematically-grounded supporting evidence for said phenomenon. 
* I appreciate that the tasks of interest, and the distinguishment between the two abilities of interest (distributional associations and in-context reasoning) is made clear upfront. 
* Figure 2 is especially helpful to follow the 2-layer setup for the in-context recall task with noise tokens — the finding that the induction head filters out the noisy token is an interesting insight, and reinforced by Theorem 2 and its proof in Appendix D. 
* While the paper is dense, it is also organized quite well and in a manner that emphasizes the key takeaways.

### Weaknesses
 * The novelty presented the results section (Section 4) is unclear — are there any architectural insights informed by the theoretical analyses that could be applied that have been considered, beyond an application of LASER? Aside from this, this section appears to be a more in-depth, investigative analysis on the behavior of the chosen pre-trained models for the selected tasks; it is also unclear how / whether these insights scale as the models considered are small. 
* I have no major concerns about the theoretical results in the work, which reveal the means through which noise is stored both in the presence and absence of feedforward layers, under a simple 1-layer model. I must acknowledge that while I have largely studied and followed the proofs of Theorems 1 and 2 and the theory in Appendix A, I have not thoroughly verified the correctness of the theory in the rest of the appendix.



### Questions
* I would suggest moving the proofs of Lemmas C.1 and C.2 up, before they are invoked in the proof of Theorem 1 / 4. This would make it easier to follow the progression of claims made. 
* In the abstract, the term “gradient noise” is used in line 21, but not referred to in the rest of the paper — please clarify (or remove, if not relevant) this term. 
* The use of the term 'sequel' on line 125 is unclear; this should be clarified or rephrased accordingly. 
* As noted in the weaknesses section, are there any architectural changes that may be proposed, conditioned on the results of the exploration? Is the key takeaway that one should perform low-rank truncation as in LASER on the feed-forward layers since they store noise? Including discussion on this would improve the actionability of the findings of this work and its impact.

### Soundness
3

### Presentation
3

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
Large language models excel in in-context reasoning tasks like coherent language generation and knowledge storage. Their Transformer architecture relies on feed-forward and attention layers linked to knowledge and reasoning. In controlled experiments, the authors found feed-forward layers learn simple distributional associations, while attention layers focus on context reasoning. Gradient noise explains this difference. Pre-trained models, like Pythia, show similar disparities in simple reasoning tasks.

### Strengths
1. This paper uses a large number of experiments and theoretical proof to draw the following conclusions:
For the Transformer architecture of large language model LLM, feed-forward layers learn simple distributional associations, while attention layers focus on context reasoning.

2. The experimental results and conclusions are relatively solid, and the theoretical proof is quite convincing.

3. This work may be helpful for future researchers studying LLM.

### Weaknesses
1. This work is highly theoretical and lacks certain practical significance and applicability.

2. In addition to feed-forward layers and attention layers, there are also wording embedding layers, residual connections, and LayNorm layers in the Transformer architecture. What special role do these layers play in helping the model understand the semantics of the natural language? Did the authors explore?

3. Because the attention module is the interaction between all tokens in the input sequence, it intuitively plays a role in understanding context. It seems obvious that the attention layer mainly focuses on in-context reasoning, right?

4. Are the given conclusions applicable to all models based on the Transformer architecture? Is this applicable to all LLM models?

5. In terms of format:
    Line 1935, Line 1938, Line 1952, Line 2001, Line 2069 exceed the margins and have incorrect formatting.

### Questions
1. In addition to feed-forward layers and attention layers, there are also wording embedding layers, residual connections, and LayNorm layers in the Transformer architecture. What special role do these layers play in helping the model understand the semantics of the natural language? Did the authors explore?

2. Because the attention module is the interaction between all tokens in the input sequence, it intuitively plays a role in understanding context. It seems obvious that the attention layer mainly focuses on in-context reasoning, right?

3. Are the given conclusions applicable to all models based on the Transformer architecture? Is this applicable to all LLM models?

4. In terms of format:
    Line 1935, Line 1938, Line 1952, Line 2001, Line 2069 exceed the margins and have incorrect formatting.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors investigate the role of transformers' self-attention and feed-forward networks (FFNs) both experimentally, in a controlled environment with a simplified model, and theoretically, using an even simpler model that allows them to derive calculations. The authors thus highlight an important distinction: FFNs are biased towards learning distributional associations (i.e. co-occurrence cues), while self-attention focuses on in-context reasoning. 

Concretely, as it is common to have the word “the” after the word “in”, a model using distributional cues only would be tempted to complete the sentence “Madrid is located in” with “the”, whereas a model using in-context reasoning would complete it with “Spain”.

So the authors set up an experiment in which the model is trained on a text containing with equal probability the “a + b” and “a + noise” patterns (where “a” varies from sentence to sentence, while the “noise” token remains the same) and then evaluated on a text containing only the “a + b” pattern. The idea is then to measure in-context recall in such a scenario: indeed, a purely distributional model will perform at 50% accuracy where a perfectly in-context reasoning model will achieve 100%. Using LASER to reduce the rank of the second-layer MLP matrix, until it is completely suppressed (rho = 0), they note that distributional behavior disappears with MLP rank, suggesting that FFNs are biased in this direction. They also note that self-attention manages to focus only on “a + b” patterns, ignoring “a + noise” patterns. 

The authors then propose a theoretical explanation for such behavior, analyzing in particular the first gradient descent step. Finally, the authors propose to test their findings in a more realistic setting, i.e. on real models and real-world reasoning benchmarks.

### Strengths
- It is very well written and clear.
- Their experimental environment is very clearly established, from the creation of their dataset to the architecture of the model.
- I think that experimenting with LLMs in a controlled setting is an excellent methodology.
- The paper proposes a theoretical justification for their discovery that is more than welcome and very rare in the field.
- The findings are very interesting and help to better understand the behavior of LLMs, in particular FFNs, which are often less studied than self-attention.

### Weaknesses
 - The main experiments and theoretical results are based on highly simplified models. However, the observed behavior may not scale with larger models. Specifically, the two-layer transformer used in the core experiments, while allowing for interpretability, may not accurately reflect the complex dynamics of deeper networks. The reliance on a synthetic dataset with controlled 'a + b' and 'a + noise' patterns, while useful for isolating specific behaviors, may not generalize to the more nuanced and varied patterns found in real-world text.
- The theorems and their consequences are relatively complicated to understand for a non-initiated reader of this literature, perhaps try to explain the different terms a little more. The theoretical analysis, while valuable, could benefit from a more intuitive explanation of the mathematical terms and their implications for the behavior of the model. The connection between the theoretical findings and the experimental results could also be made more explicit, particularly for readers who are not deeply familiar with the mathematical formalism.
- Experimental figures have no error bars. This makes it difficult to assess the statistical significance of the results. The absence of error bars raises concerns about the reliability of the observed trends, as it is unclear whether the reported differences are statistically meaningful or simply due to random variation.

### Questions
1) Why did you use such a small model for the experiments? Would it be possible to perform the same kind of analysis with more layers?
2) What is your interpretation of the poorer performance of truncated MLPs after 8-shot on GSM8K (Table 2)?
3) Your results seem to indicate that reducing FFNs greatly improves in-context reasoning, which is often desirable. However, FFNs also play an important role. It would therefore be interesting to study what is lost when they are reduced/removed?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors studied how attention mechanisms and feed-forward layers handle distributional associations and in-context inputs differently. They considered simple two-layer transformers on an in-context recall task and observed the distinct focuses of feed-forward layers and attention mechanisms through analyzing gradient.
They further employed LLMs like GPT-2 and Pythia, concentrating on IOI dataset . Additionally, the authors validate the effectiveness of the LASER technique.
Overall, the authors underscore the differing roles of attention layers and feed-forward layers in language models.

### Strengths
1. The authors conducts an in-depth study on how attention and feed-forward layers differently process distributional associations and contextual inputs, yielding clear and significant conclusions.
2. The flow of the paper is easy to follow. 
3. The authors employ clear theoretical proofs and a logical structure, supporting the authors' arguments.

### Weaknesses
1. The experiments in this paper are insufficient to demonstrate authors’ claim, they only evaluate with limited number of datasets and model structures, which might not be representative of the general behavior.

2. The technique authors recommended, LASER[1], is not introduced by this paper, making this paper seems an extension or complement to LASER. Differentiation between this paper’s contributions and [1]’s should be claimed.

3. The methods and datasets this work employed is interesting but mostly appear a simple extension of that in [2]. This makes the research seem a supplementary work.

### Questions
1. Is there potential modifications or improvements for the authors to propose to LASER that could strengthen this paper’s contributions?
2. In Section 4.2, why LASER struggles with more shots? 
3. Is it possible to make other modifications beyond those in [2], such as designing an entirely new dataset to better validate your claims?

### Soundness
3

### Presentation
3

### Contribution
2
