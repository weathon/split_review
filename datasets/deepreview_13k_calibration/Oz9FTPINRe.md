# A Causal Study on The Learnability of Formal Languages

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Understanding the limitations of neural language models is crucial for knowing what such models are capable of and how they can be used safely. A popular approach to analyzing formal limitations takes the form of training models on formal languages, and studying what aspects of the languages affect model performance. Formal languages can, for instance, be designed using manually constructed grammars or randomly sampled by sampling some type of automata. This provides the researcher with unique control over the features of the language of interest. In this paper, we provide an even more fine-grained approach to targeted model evaluation. We develop a method for controlling specific \emph{string} features, on the corpus level, in the language of a given automaton. This gives us control over properties such as symbol frequencies while keeping everything else intact, enabling a causal study of their importance. To describe our framework formally, we turn to \emph{semirings} and introduce finite state automata over a novel---counting---semiring. We devise algorithms that enable string sampling under varying degrees of interventions and demonstrate the utility of our method through several examples showing how targeted interventions over transition, symbol, and state frequencies can be performed. We then train Transformer and LSTM language models on languages under varying degrees of interventions. Our fine-grained analysis allows us to show that different mechanisms influence the learning behavior of these two architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the ability of LMs to learn formal languages by using causal interventions on the data generation process. Specifically, they introduce a counting semiring that allows them to intervene on the number of transitions (and by extension, states and symbols) in a data-generating automata that occur in a dataset of a fixed size. Their novel methods for sampling from automata improve the efficiency in terms of the maximum count of occurrences to set in the intervention. Through an empirical study, they use their methods to investigate what influences the ability of Transformer and RNN models to learn regular languages.

### Strengths
1) A novel sampling method is introduced that could be of independent interest.
2) The paper is well organised and clearly written.
3) The theory is backed by an empirical investigation, showing how the methods could be practically useful.
4) The theory is mathematically rigorous, showing that their construction yields the desired properties.

### Weaknesses
1) It seemed insufficiently motivated why intervening on the exact number of transitions would be useful. Could you provide specific examples of potential real-world applications or research scenarios beyond the one explored in the experimental section where this would be valuable?
2) It is unclear how practically impactful the efficiency of the proposed is. Could you provide concrete examples of scenarios where being able to increase the maximum count n further would be particularly beneficial?
3) A more detailed comparison with the existing methods would help contextualise the importance of the efficiency gain. The current version does not make it clear whether the n^4 method mentioned is a simple baseline or the best previously known method.
4) The experimental results in Figure 2 could be better presented. Perhaps additionally including aggregated statistics would be easier to interpret, e.g. plotting the average across the machines with error bars while retaining the current figure in Appendix.



### Questions
1) What is the rationale for training RNNs for 4 epochs but Transformers for 10? This appears to make comparisons between the two architectures less clear. Borenstein et al., 2024 from which you adapted the configuration uses two epochs for each architecture. Perhaps results with an equal number of epochs could be included to ensure a fair comparison.
2) Why are the occurrences on the plots at irregular values? Is the specified count for the intervention randomly sampled?
3) How did you choose the specific numbers for the empirical results, e.g. the number of states, symbols, and the counts for interventions?

Nitpicks:
1) Some citations are not formatted well, e.g. parentheses on lines 367 and 968.
2) The figures could be formatted better, e.g. with the values on the x axis being less crowded.

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
3

### Summary
This paper introduces a novel algorithm for efficient sampling of strings from regular languages with specific features (e.g., precise occurrence counts of given symbols). The work is motivated by the need to study how specific language features causally impact learnability by neural models. At the core of the algorithm lies a new algebraic structure called the counting semi-ring, which enables tracking occurrence counts of predefined events when sampling from probabilistic finite state automata (PFSA).
The experimental framework consists of sampling random PFSAs and generating sets of strings Y with target features for each PFSA. To evaluate language learnability, both LSTM and Transformer models are trained on these string sets. The evaluation uses KL divergence between the trained models and the original PFSA, along with a decomposed KL metric to assess the impact of interventions on target features.
The empirical results reveal two key findings: (1) Transformers demonstrate superior performance compared to LSTMs in modeling these languages, and (2) the features that indicate language learnability differ between LSTM and Transformer architectures. These findings contribute to understanding of how different neural architectures learn and generalize regular languages.

### Strengths
1. The concept of analyzing neural models through properties of regular languages is valuable and brings a novel perspective to the field. This approach has the potential to deepen our understanding of how neural models can capture structured patterns within regular languages.

2. The proposed algorithm for efficiently sampling arbitrary strings with constrained features represents an important methodological advancement. This tool could facilitate more precise and controlled studies of neural models' behavior in relation to regular languages.

3. The design of various features—such as transitions, states, and symbols—along with related explanatory variables, is both creative and effective, as demonstrated in the experiments. This feature framework may be beneficial for further research into neural models and their capabilities with regular languages.

### Weaknesses
1. While using a semiring approach to study the counting properties of weighted automata is indeed a classical method in automata theory [1], there is limited comparison between the proposed method and these traditional approaches. Including such a comparison would help clarify the contribution and novelty of this work, positioning it more effectively within the broader research landscape.

2. The use of causality in the current structure appears somewhat extraneous. In this context, causal "interventions" seem equivalent to conditioning rather than introducing true causal effects. Since no causal effects are explicitly evaluated in the experiments, it may improve clarity to describe these interventions simply as conditional operations.

3. Some critical experimental details are missing, which impacts reproducibility and clarity. Specifically, more information on the sampling process for probabilistic finite-state automata (PFSAs) with 100 states and 10 samples would be helpful, such as the random seed selection process and the composition of final sets across different intervention types.

### Questions
1. Please refer to the questions in the Weaknesses section.
2. In line 309, the term "DPFSA" is introduced, but prior sections mention only "PFSA". Could the authors clarify the meaning of "DPFSA" and explain how it differs from or relates to "PFSA"?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a efficient method for sampling strings from a probabilistic finite state automata (PFSA) subject to certain constraints. The main application of the technique is in computing the causal effect of certain dataset properties (such as symbol frequencies) on different probabilistic language models (specifically, Transformers and LSTMs).

Preliminary experiments are conducted using PFSA with 100 states and 10 symbols. Experiments explore 3 properties: increasing the number of times a given transition (74 machines), state (149 machines), or symbol (73 machines) occurs when sampling a dataset from PFSA. Two types of analysis are performed. The first is a linear regression of how frequently a given property occurs against the KL divergence between the PFSA and LM output distribution. The second is an analysis of how various properties of the underlying PFSA (e.g., expected string length) relates to the coefficients of the fitted regression.

===

I have read the author's responses. While they have addressed some of my concerns (e.g., length generalization being another benefit of their sampling algorithm), my main concern is still that the analysis of results is rather limited in scope to Transformers / RNNs trained on strings sampled from PFSA, which limits the contributions. I also note that the authors have not answered my question about a full derivation of the runtime complexities, which I think is key given that the improved runtime is a major claimed benefit of the approach.

I thus maintain my score

===

After additional discussion I have raised my score

### Strengths
The idea to explore how different properties of a data generation process are causally related to the trained performance of different LM architectures (transformer, LSTM) is an important topic toward understanding the behavior of LLMs.

The sampling algorithm is, to the best of my knowledge, original, and asymptotically improves upon the naive approach of intersecting FSAs.

The results are also interesting, although I found it difficult to grasp the significance of the results given the specificity of the domain (language modeling applied to strings sampled from a PFSA).

### Weaknesses
The majority of the paper is dedicated to developing an extremely general and abstract framework for efficient constrained generation from PFSA. However, I view the significance of the generality to be somewhat low, given that the experiments are conducted in a single, much more specific setting. For instance, I don't think much is gained by defining the algorithm in terms of a counting semi-ring instead of directly describing the data structure used to track feature counts. I think the presentation would be clearer by directly presenting the specific version of the algorithm actually used in the experiments in the main text, and developing the more general theory in the appendix. This would also free up space for a deeper analysis of the experimental results.

The technique is also limited to finite state automata. Modeling complex joint distributions with FSA incurs a large computational overhead, so it's unclear how to apply a technique based on FSA (even with the asymptotic improvements of the new sampling algorithm) to study more complex types of dataset properties or even natural language.

Finally, I found the results and discussion to be somewhat limited. One suggestion would be to contextualize the observed results to explain differences observed between Transformers and LSTMs in other domains (such as natural language).

More minor concerns:

- The notation gets unclear at points. For instance, $n_i$ is not defined on line 93.
- There are missing references [1] [2]

### Questions
Can you provide derivations for the runtime complexities in lines 125-128?

Is there another instance of a counting semi-ring that would benefit from the sampling algorithm (beyond string feature counts?)

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Previous works have studied language models by characterizing their performance on synthetic datasets samples from families of formal languages. This paper tries to get a more fine-grained understanding of learning language models on regular languages, by controlling for certain statistical features such as the number of times a state occurs. To achieve this, the authors introduce the counting semiring, which allows sampling from the finite state machine conditioned on the count of a feature of interest (e.g. the number of state transitions). Finally, this approach is applied to transformers and LSTMs to study what factors (causally) impact the learned models.

### Strengths
Overall, I like the direction this work takes; providing more fine-grained control in studying language models. As language models are often blamed for being overly reliant on the presence of statistical features, it is especially useful that the authors can correct for these and measure their impact. The proposed sampling approach seems well thought out and novel to me, although I must say I’m not that familiar with this area and so could very much be unaware of related work. Finally, the proposed approach is quite general, and hence might be of broader use outside of the specific demonstration given in the experimental section.

### Weaknesses
My main gripe with the paper lies in the presentation. Firstly, the paper does not include examples of the central contribution: the counting semiring. This makes it difficult to grasp the practical implications of the theoretical framework. Secondly, the notation at many points feels cumbersome and was sometimes confusing. For example, $p(\pi)$ could both mean a probability of a path (e.g. proof of Thm3.2.) and the origin of a path (Eq. 28). The overloaded notation makes it hard to follow the mathematical arguments precisely. For more examples, see the questions. I also felt that this was partly caused by trying to be very general. Indeed, the counting semiring is defined over any semiring, while it seems that in practice only the probabilistic semiring is ever used/needed. This generality, while theoretically interesting, adds unnecessary complexity for the reader.
Thirdly, the paper pushes some definitions to the Appendix (e.g. for forward and backward probability), making the paper less self-contained. This forces the reader to constantly switch between the main text and the appendix, disrupting the flow of understanding. On the other hand, rather straightforward proofs (e.g. for Thm 3.1) are kept in the paper, creating an imbalance in the presentation.

Finally, the new insights provided by using the proposed counting semiring in the experimental section are quite limited. Perhaps this is subjective, but e.g. that transformers perform better than LSTMs is well known. The findings also do not appear to be very actionable. The experiments, while demonstrating the use of the semiring, do not provide significant new understanding of the behavior of language models.

### Questions
- I initially found the naming of "counting semiring" confusing, as it has been used before to describe the semiring over the natural numbers (which can be used to count the number of parses a word has). See e.g. the seminal semiring parsing work by Goodman et al. (1999). 

- On a related note, the paper claims its counting semiring is novel, but it is essentially the same as a polynomial semiring with 1 variable (except that the convolution gets truncated), which has been well studied. I suppose the two pages of proofs in Appendix C wouldn’t be necessary if you observe that there is a homomorphism from the polynomial into the counting semiring.

- Def. 3.3. is unclear. Using both a feature function $\phi$, a set of features $\Phi$, and a lifting function $\mathcal{L}$ seems to unnecessarily complicate things. Furthermore, $\phi$ is a function in $\delta \to \{ 0, 1,\dots N \}$, but then the lifting function uses $\phi(\alpha)$ where $\alpha \in \mathbb{K}$. More importantly, Def 3.3 also doesn’t explicitly define the counting automaton! I assume the transition weights in the counting automaton should contain the one-hot vectors of the lifting function times the original weights, but this is not mentioned.

- The proof of Thm 3.2. seems flawed. I would have expected something like $\sum_{\lvert \pi \rvert_\Phi = n} p(\pi) = \sum w_I (\pi)_n$. Could you elaborate on how the step in Eq. uses Thm 3.1? Why don’t you need a subscript for $w_i(\pi)$ (i.e. you suddenly go from a probability to a vector)? Also: why is the normalization with $\sum p(\pi)$ necessary, isn’t this equal to 1?

- In Corollary 4.1, there’s no mention of what v stands for.

_Minor comments_

- On line 129, What does the \cdot stand for?

- In Figure 3, should the transitions be a_1 and a_2 instead of a and b? (As line 707 defines $\Sigma = \{ a_1, a_2 \}$). I suppose that w_1 and w_2 in this example also should both be 1, instead of arbitrary numbers, as the WFSA is mentioned to be probabilistic)  

- On line 806, there is a broken reference.

**References**

Goodman, J. (1999). Semiring parsing. *Computational Linguistics*, *25*(4), 573-606.

### Soundness
3

### Presentation
1

### Contribution
3
