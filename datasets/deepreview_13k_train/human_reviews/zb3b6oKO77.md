# How do Language Models Bind Entities in Context?

- Decision: Accept
- Scores: 6, 5, 6, 5

## Abstract
To correctly use in-context information, language models (LMs) must bind entities to their attributes. For example, given a context describing a ``green square'' and a ``blue circle'', LMs must bind the shapes to their respective colors. We analyze LM representations and identify the \textit{binding ID mechanism}: a general mechanism for solving the binding problem, which we observe in every sufficiently large model from the Pythia and LLaMA families. Using causal interventions, we show that LMs' internal activations represent binding information by attaching \textit{binding ID vectors} to corresponding entities and attributes.  We further show that binding ID vectors form a continuous subspace, in which distances between binding ID vectors reflect their discernability. Overall, our results uncover interpretable strategies in LMs for representing symbolic knowledge in-context, providing a step towards understanding general in-context reasoning in large-scale LMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studied how language models handle a linkage between entity and attribute tokens. The authors argued that language models used a component of the residual stream of each token as a binding vector to mark entities and their corresponding attributes. The authors also claimed that the binding vectors are simply added to the residual stream.  

To prove this empirically, the authors presented a series of causal mediation experiment results on binding tasks, such as determining a city in which a person lives or the color of a shape based on a context. The context typically consisted of two to three entity-attribute pairs. First, the authors showed that binding vectors existed by swapping activations of an entity or an attribute. The results showed that binding changed (by means of changing the mean log probability of attributes.) On the other hand, shifting did not affect the mean log prob of the correct attributes -- suggesting that binding vectors are positional independent. The author then estimated the binding differences and showed that the authors could perform addition or subtraction to manipulate the bindings. In addition, the difference vectors are generalized across different binding tasks. But, the authors suggested one task had an alternative binding mechanism.

### Strengths
1. This paper presented a novel concept of binding mechanism in language models. 
2. The paper provided experiment results based on many datasets, albeit toy data. Figure 3, Tables 1 and 2 supported the main claims of the binding vectors and their additivity property. 
3. The paper was well-written. I found that the definitions and hypotheses were well articulated and precise. It also provided sufficient background to understand the paper.

### Weaknesses
Significance of the Results

1. While the ideas presented in this work were novel, it was unclear how generalized they are. The authors presented a series of experiments based on somewhat synthetic datasets. Had the task been reading comprehension, we might not have observed the same mechanism. I think adding more tasks did not provide meaningful results unless they required different reasoning complexities. In addition, the experiments presented in Section 3 only provided anecdotal evidence from a few samples (Factorization and Position Independence claims). Specifically, the factorization claim relies on substituting only the first token of multi-token attributes, which may not be representative of the entire attribute's representation. The position independence claim also lacks a rigorous analysis of how the binding vector interacts with positional embeddings.
2. Although the paper presented the results using both Pythia and LLaMa as subject LMs, the results in Figure 6 showed opposite trends between the two models. I saw that the accuracies were further apart in Pythia as the sizes went up but opposite in the LLaMa cases. I think the authors should explain this. Did the binding mechanism localize to a family of models? It is unclear if the observed trends are due to differences in model architecture, training data, or other factors. The fact that the trends diverge so significantly raises concerns about the robustness of the proposed binding mechanism.
3. It was unclear whether there was the proposed binding ID when reasoning involving spans of tokens. The experiments focused on single-token entities, but real-world reasoning often involves multi-token entities and attributes. The paper does not adequately address how the binding mechanism would handle such cases, especially when the tokens within a span might have their own internal relationships and dependencies.

Presentation

1. Figure 3 shows the same image for (a) and (b). I was not sure why, or was it a mistake?
2. I found the notion of the *binding function* rather confusing in Eq (1). I had many questions about it. If the binding function specifies how an entity binds to an attribute, why is it a sum of entity representation and the binding vector? What is the relationship between the binding function and the residual stream?

### Questions
1. How many samples did you use to generate Figure 3? (100 or 500)
1. Were the samples you used to estimate the *differences* the same samples for testing in Table 1? If so, why?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes how a language model (LM) correctly associates entities and their attributes described in context (i.e. as a prompt). The authors introduce the idea of binding ID vectors and show that an LM learns a pair of binding ID vectors for each entity-attribute pair so that the LM uses the vectors to correctly identify the right attribute when answering a query about an entity. They also present experimental results suggesting that the binding vectors reside in a linear subspace and are transferable across different tasks.

### Strengths
- The paper explores an interesting topic on representation learning that should contribute to a deeper understanding of LLMs.
- The paper presents a novel idea to explain the phenomenon.and experimental results that support the idea.

### Weaknesses
 - The paper is sometimes difficult to follow. This may be because the main body of the paper contains too many concepts and fails to provide important explanations and examples that would help the reader understand the concepts.
- It is not entirely clear whether the authors’ conclusions are supported by experimental evidence. For instance, the claim that binding vectors reside in a linear subspace is not rigorously demonstrated. The experiments, such as those in Section 4.2, only show that linear combinations of binding ID vectors work, but it does not preclude the existence of other non-linear combinations or vectors outside the subspace that could also function as binding vectors. The paper also lacks a clear explanation of how the binding ID vectors are extracted or computed from the model's activations. This makes it hard to verify the claims or reproduce the results.


### Questions
- Section 2.1: What exactly do you mean by “the k-th entity” and “the k-th attribute”? Is the entity that appears first in the sentence called the 0-th entity?
- Section 2.1: What did you sample N=100 contexts from?
- Section 3.2: What is the experimental setting in the experiment?
- Section 4.2: Does the experimental result really mean that the vectors that are not linear combinations of binding ID vectors do not work?
- Figure 5: What are the x and y axes? Are they the coefficients of the basis vectors?
- p. 8: What exactly is a cyclic shift?
- p. 2: Does a “sample” mean an example?  In statistics, a sample usually means a collection of examples (data points).
- p. 1: alternate -> alternative?
- p. 2: of of -> of
- p. 8 In See -> See

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a hypothetical mechanism to explain how LLMs associate entities to specific properties in the in-context learning setting, which the authors call the _binding problem_. The phenomenon is mostly studied in the context of a very short and simple reasoning task, and the key investigative tool is _causal mediation analysis_, where carefully chosen sets of internal activations are substituted into to the network before generating responses to queries. The experimental results are consistent with a hypothesized "binding ID". Further experiments test other properties and behaviors of this mechanism.

### Strengths
Figure 2 was very helpful in illustrating the substitution scheme. 

I am not completely convinced that the claims follow from the observations due to some clarity (or confusion on my part) issues (see below), but assuming they hold: the _binding ID_ mechanism and its properties represent a really exciting discovery in terms of understanding LLM ICL phenomena. I suppose maybe this sort of lines up with the recent (Bricken et al 2023)[https://transformer-circuits.pub/2023/monosemantic-features/index.html] and associated previous superposition research. In any case, this mechanism would unlock a lot of promising research directions as well as practical applications.

Section 3.1: the hypothesized mechanism and its consequences are, for the most part, laid out clearly and precisely. (nit: "the only information ... that affects the query behavior" _for our specific queries_)

To the extent that I correctly understood the experiments, the ability to, rather surgically, manipulate the "beliefs" of the model was fairly clear evidence consistent with the hypothesized mechanism. The setting where switching both entity and attributing binding IDs restores correct query answering was a "wow" moment for me.

### Weaknesses
Section 2.2: it was not immediately obvious to me whether the stacked activations completely "d-separates" (maybe not exactly this concept?) the intervention token from everything else, without some more detail on the LM architecture.

Section 4.1 is very dense, and I found it difficult to follow without working it out myself on separate paper. Given the importance of these concepts to the rest of the paper, a diagram might help make it clearer. Specifically, the explanation of how the binding ID $k$ is represented by the pair of functions $[b_E(k), b_A(k)]$ and how this relates to the abstract binding IDs (triangle, square) in Figure 1 could be expanded. The $\Delta$ calculation scheme in Eqn 2 and the expectation sampling seem to crucially depend on, eg $b_E(k)$ being a stable/consistent function of (the seemingly arbitrary index?) $k$ across _any context_ $\bf{c}$. This stability assumption needs to be clarified and justified. Without resolving the clarity a bit, it's difficult to fully accept the interpretations of the experiments, as significant as the findings would be.

Section 5 supports the generality of the mechanism across other similar tasks, which further strengthens the central contribution. The existence of the alternative _direct binding_ mechanism was interesting to see and another good contribution of the paper, although it was not super clear without reading the corresponding Appendix. A more concise explanation of this mechanism within Section 5 would improve the flow of the paper.

"If there no context consistent...say that the LM is _confused_" - I didn't fully understand this why or how this would happen, and also it didn't seem to come up elsewhere in the paper. Is it necessary to include?

"A subtle point is that ..." this seems centrally important but only mentioned in passing. This point about the $k$-th entity/attribute always having the same binding ID should be elaborated on, as it is crucial for understanding the proposed mechanism.

Figure 3 b seems like the wrong plot? It doesn't show what the text claims but rather seems to be a copy of Figure 3 a.

Eqn 2: is there any significance to the notation change of introducing $\alpha$ ?

"These random vectors have no effect" - I would have expected it to break things. so I guess this is even further evidence that the binding vectors are treated in a "special" way by the LLM machinery? If so, maybe this reasoning and conclusion could be emphasized. It would be helpful to explain why random vectors do not affect the binding mechanism and what happens when these vectors are scaled up.

Perhaps due to my previous confusion about how binding ID functions work with $k$, but I could not understand what Figure 5 was conveying at all. A more detailed explanation of this figure, along with the concept of a continuous region in activation space for valid binding vectors, would be beneficial.

For any of this to make sense, I guess you are using a word-level tokenizer and not something like BPE/etc? Except it seems like the direct binding experiment uses sub-word tokens? Again, for clarity it might help to lay this out explicitly.

### Questions
"If there no context consistent...say that the LM is _confused_" - I didn't fully understand this why or how this would happen, and also it didn't seem to come up elsewhere in the paper. Is it necessary to include?

"A subtle point is that ..." this seems centrally important but only mentioned in passing.

Figure 3 b seems like the wrong plot? It doesn't show what the text claims but rather seems to be a copy of Figure 3 a. 

Section 4.1: what are we sampling here: from different "X lives in Y"-style context sentences? I don't totally understand why / how we'd expect the $b(k)$ vectors to be consistent for a given value of $k$ across different contexts, or is that not required? *Actually, this may be my central confusion with Section 4 and beyond*: 
* in Figure 1, abstract shapes (triangle, square) are used to represent the abstract binding IDs
* in Section 4.1, binding ID $k$ is represented by some pair of functions $\[b_E(k),b_A(k)\]$
* the $\Delta$ calculation scheme in Eqn 2 and the expectation sampling seem to crucially depend on, eg $b_E(k)$ being a stable/consistent function of (the seemingly arbitrary index?) $k$ across _any context_ $\bf{c}$ 

So, is the hypothesized mechanism that:
1. LLM, internally, have some weird analogue of LISP `gensym` that generates arbitrary but unique abstract binding IDs like "square" and "triangle" (but of course are really lie in a linear subspace of vectors) when an entity/attribute is seen in-context?
2. OR that LLM have some stable/consistent binding function $b_E(k)$, and the first time `llm-gensym` gets called, the result for $k=0$ is returned, and some internal entity counter (?) executes $k++$ ? 
3. OR some other process else altogether that I am missing?

Figure 1 led me to believe case 1, but then Section 4.1 (as far as I can tell) requires case 2, and in fact the experimental results seem consistent with that mechanism. This is even more surprising to me, and I would argue needs to be laid out a bit more explicitly, if this is indeed the correct interpretation. Or possibly, it is case 1 and I am mistaken that the rest of the work depends on the "stable $b(k)$" described in case 2?

Eqn 2: is there any significance to the notation change of introducing $\alpha$ ? 

"These random vectors have no effect" - I would have expected it to break things. so I guess this is even further evidence that the binding vectors are treated in a "special" way by the LLM machinery? If so, maybe this reasoning and conclusion could be emphasized.

Perhaps due to my previous confusion about how binding ID functions work with $k$, but I could not understand what Figure 5 was conveying at all.

For any of this to make sense, I guess you are using a word-level tokenizer and not something like BPE/etc? Except it seems like the direct binding experiment uses sub-word tokens? Again, for clarity it might help to lay this out explicitly.

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates a binding problem in which language models must represent the associations among entities and attributes. The authors empirically check the behavior of binding considering factorizability and position independence, and they introduce the idea of a binding ID vector, considering the additivity of binding functions. The paper shows several pieces of evidence that imply the existence of the binding ID vectors and their generalities.

### Strengths
- The paper proposes novel binding ID vectors that can help understand LLM's behavior. 
- The paper presents empirical evidence of binding by checking substitution and position independence.
- Analyses are provided for biding ID vectors, including geometry and generalization.

### Weaknesses
 - The paper addresses a simple binding problem between a pair of entities. It is unclear how this can be generalized to the binding behavior on more than binary relations and entities involved in multiple binding. 
- Some details are not clear, as in the following questions.

- When the authors substitute activations in Figure 3 or calculate median-calibrated accuracy in Figure 5 and Table 2, which part of the model is substituted and which is frozen? LLMs are autoregressive models, and during decoding, when and how are the parameters substituted? 
- Among what did the authors calculate the mean of log probs in Figure 4? 
- In equation (2), they do sampling, but from what did the authors sample? 
- The lines in the legend do not match those in the graph in Figure 4. In the bottom graph, the mean log probs increase or decrease with the positions, but the authors say they are small changes. How can they be said small?

### Questions
- When the authors substitute activations in Figure 3 or calculate median-calibrated accuracy in Figure 5 and Table 2, which part of the model is substituted and which is frozen? LLMs are autoregressive models, and during decoding, when and how are the parameters substituted? 
- Among what did the authors calculate the mean of log probs in Figure 4? 
- In equation (2), they do sampling, but from what did the authors sample? 
- The lines in the legend do not match those in the graph in Figure 4. In the bottom graph, the mean log probs increase or decrease with the positions, but the authors say they are small changes. How can they be said small?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
