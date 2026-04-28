# A Percolation Model of Emergence: Analyzing Transformers Trained on a Formal Language

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Increase in data, size, or compute can lead to sudden learning of specific capabilities by a neural network---a phenomenon often called "emergence". Beyond scientific understanding, establishing the causal factors underlying such emergent capabilities is crucial to enable risk regulation frameworks for AI. In this work, we seek inspiration from study of emergent properties in other fields and propose a phenomenological definition for the concept in the context of neural networks. Our definition implicates the acquisition of general regularities underlying the data-generating process as a cause of sudden performance growth for specific, narrower tasks. We empirically investigate this definition by proposing an experimental system grounded in a context-sensitive formal language, and find that Transformers trained to perform tasks on top of strings from this language indeed exhibit emergent capabilities. Specifically, we show that once the language's underlying grammar and context-sensitivity inducing regularities are learned by the model, performance on narrower tasks suddenly begins to improve. We then analogize our network's learning dynamics with the process of percolation on a bipartite graph, establishing a formal phase transition model that predicts the shift in the point of emergence observed in our experiments when intervening on the data regularities. Overall, our experimental and theoretical frameworks yield a step towards better defining, characterizing, and predicting emergence in neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies emergent capabilities in transformers via two case studies. In the first study, they look at learning of formal languages (in particular, a language generated via a PCFG). For this setting, they train GPT-2 sized models from scratch for:
-  left-to-right auto-regressive language modeling
- an unscrambling task that requires the model to take a set of words and convert it into a valid string
- a conditional generation task that requires the model to generate a sentence that has certain words in it.

As the model trains they track grammaticality (as measured by whether model generates strings that the PCFG accepts), and if the generated strings follow type constraints. They break down learning into 3 phases, and find that these phases correspond to jumps in the downstream performance (either exact match acc for unscrambling, or loss for language modeling). 

In the second study, they study concept acquisition where entities are associated with types. In particular, they model a concept matrix where row i corresponds to the ith entity, and column j corresponds to the jth type, and the ij entry in the matrix is the probability with which these are seen together. They then define a concept propagation matrix, and use connectedness properties of this propagation matrix to define phase changes. They find that analytic values of these connectedness properties correlate with whether the transformer learns specific concepts.

### Strengths
- The paper is extremely well written, and focuses on clearly understanding the phenomenon of emergence (albeit in the limited setting of language modeling of formal languages).
- Explores a new setting of learning entity type relationship, as percolation on a bipartite graph. I believe such a setting has not been explored before (though i'm not sure how it connects to emergence of skills / behaviors in transformers)

### Weaknesses
Phases of learning: I’m not convinced with the learning dynamics story here. Just because the model can generate accurate sentences does not mean that it has acquired grammar. Understanding whether the model has acquired grammar has been studied previously in NLP: a better method to do this would be to create minimal pairs with one grammatical and one ungrammatical sentence, and check if the model assigns a higher prob to the grammatical sentence. Ofcourse, the design of the minimal pair needs to be well thought-of, to eliminate shortcuts. Here is an example of a minimal pair that checks if a model can produce the correct number for a verb:

S1: The man who likes apples is here

S2: The man who likes apples are here

Not clear what is the point of the percolation model: This seems less about emergence of structure in the model, and more about how at a specific data setting, generalization can happen. I’m not sure what the analogy is between learning type constraints (which is a function of training time), and graph percolation (which is a function of the data properties |E| and |K|). But if the authors can clarify this, i'm happy to increase my score.



Not clear what are new findings in this paper:
- Many of the conclusions from this paper are also in Murty et al. 2024, who also train transformer language models on formal languages, and find emergence of the correct learning rule, with extended training. They also find that such emergence happens alongside the emergence of tree-structures in transformers.
		
- Similarly, Chen et al. also have a very similar setting but with masked language models, and show that grammar is abruptly acquired, and such grammar acquisition has a causal relationship with downstream performance.
- There’s also other work by Allen-Zhu et al, who train transformers on formal languages, and find evidence of learnability under some constraints.

### Questions
- Do you see similar phase transitions for language learning with smaller models or bigger models? In general, do architecture tweaks change the dynamics in non-trivial ways?

### Soundness
2

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
The paper studies the emergence of abilities over the course of training in a transformer language model trained on a formal language. The authors identify distinct phases where different abilities emerge. They also study the point at which one of the abilities transitions from memorization to generalization, and show that this point empirically follows a scaling law that matches the theoretical scaling of bond percolation in a bipartite graph.

### Strengths
The phenomenon of emergence of model abilities with scale, and how suddenly this can occur, is of both scientific and societal importance, together with related questions about the transition from memorization to generalization. The paper studies these using a toy setup that is both similar enough to realistic setups to be interesting, but simple enough to be able to isolate and study both of these phenomena. The theoretical explanation using bond percolation is insightful and deserving of follow-up work.

### Weaknesses
The paper makes claims about "structures learned by the model" (in Definition 1 and Section 5.1 Phase 1), but I do not think that these are really justified by the evidence in the main body of the paper, which only look at performance metrics. There is some analysis of attention maps in Appendix F.6. However, the main evidence given there seems to be that there is increased sparsity at partially-trained checkpoints compared to initialization, and other qualitative claims that are hard to read off from the plots. It would be easier to tell if these were quantified, but my impression is that this evidence is rather weak. I also think that if this evidence were stronger, it should be in the main body of the paper, since it would be necessary to justify this prominent claim. The claim about learning "structures" is not well supported by the analysis, and the definition of structure itself seems somewhat redundant, as it is defined by the performance on downstream tasks that require learning the regularity. It seems that a more parsimonious definition would be simply a discontinuous improvement in the performance of tasks benefiting from the regularity, but this makes the definition almost tautological.

That being said, I think there is enough interesting material in the paper without looking at model internals, so my suggestion would be to remove or significantly de-emphasize these claims/this aspect of the paper.

More broadly, I found some of the opening discussion and the definition given in Section 2 a little unnecessary, and took up space that would have been better devoted to explaining the experimental setup and results more clearly, and perhaps covering more results that only made it into appendices. In my opinion it would have been enough to give the high-level motivation, instead of couching it in terms of a new definition that doesn't really add much (especially if the claim about structure in the model is removed).

I also found that at times the presentation got too bogged down in formal details (e.g. Definition 2), and would have preferred to have seen a more accessible, plain-language explanation of things and simple examples, with formal details relegated to appendices for reference if necessary. At other times I found the exposition too rambling (e.g. Section 5.1 Phase 3), and it would have been easier to follow if the main points had been separated out and made concisely (e.g. using bullet points / short headings).

More minor points:
- In definition 1 (if you are keeping it), "nonlinear" could be confusing (e.g. quadratics are non-linear but still change gradually). Maybe you mean "discontinuous"? Or I would perhaps argue that the relevant thing is how gradual the change is (steepness of slope, even if it is locally linear).
- In definition 2, I would have found it a bit clearer to say that S is a non-terminal symbol, and just say you start from S, instead of treating it as a special case and saying you first map S to other non-terminal symbols – like the definition in Appendix C. (Also, the definition in Appendix C looks messed up, you seem to be swapping between N and NT / Sigma and T, unless I am misunderstanding something.)
- I found definition 3 hard to follow. E.g. "Entities have unique identifiers associated with them to help define subjects and objects in a sentence" - do you mean e.g. "John" will have certain attributes like "tall", "brown-eyed" etc.? Consider using plainer language and an example.
- Line 227 "Humans" vs line 228 "humans" - inconsistent capitalization could cause confusion (I assume these are the same thing).
- Line 260: For the indicator variable, maybe consider \mathbbm{1} (from package bbm) instead of \delta (though this is maybe just personal preference)

### Questions
Is the specific task (free generation/unscrambling/conditional generation) specified to the model somehow, e.g. with a special token?

For the unscrambling task, is the solution necessarily unique? If not, what's the justification for using exact match/average probability of valid tokens?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper  investigates the phenomenon of "emergence" in neural networks, where a model suddenly acquires certain capabilities after reaching a critical data or computational threshold. The authors propose a new definition of emergence in neural networks, linking it to the acquisition of general structures within the data that drive sudden performance improvements in specific tasks. The authors experiment with Transformers trained on a context-sensitive formal language and observe that once the underlying grammar and context-sensitivity structures are learned, performance on various tasks improves dramatically. This phase transition in model learning is likened to percolation on a bipartite graph, where learning dynamics mirror phase changes. Their results suggest that emergence can be theoretically predicted by understanding the structure of the data-generating process, offering insights for regulating and anticipating the behavior of AI models.

### Strengths
Generally, this paper builds a bridge between the LLM and the Physics complex system. The paper uses the phase transition from complex system theory to analyze the emergence of LLMs. This paper has the following strengths:

1. This paper provides a clear definition of emergence, which is slightly differently from previous paper, but it is more formal and general. Also, this definition helps further research the measurement of emergence.

2. This paper trained the LLM from formal languages, which generated from a strict grammar with type check. It aligns with current research.

3. he paper’s findings on emergence and phase transitions are potentially generalizable to other neural network models, not just Transformers trained on formal languages.

### Weaknesses
1. Previous paper[1] has already claimed that the emergence abilities is mirage. The paper does not clearly address contradictions with previous work: why does the phenomenon of emergence still occur in this study? Specifically, the paper does not discuss how their findings reconcile with the claim that apparent emergence can be an artifact of discontinuous evaluation metrics, or how their definition of emergence relates to prior definitions, if it differs.

2. The selection of formal language, though it is very popular in recent researches, but the situation is that the models not trained on formal languages still shows good performance. The observation is not convincing for such situations. The paper does not adequately justify why the findings from formal languages should generalize to natural language, where the underlying structure is far less rigid and explicit. The paper also lacks a discussion on how the specific choice of formal language, with its defined grammar and type system, might influence the observed emergence, and whether similar phenomena would be observed with different formal language structures or with the more complex and ambiguous structure of natural language.

3. In graph theory, diminishing marginal effects are quite common; however, there is no clear evidence linking this to the percolation model proposed in this paper. Many graph-theoretic functions exhibit properties such as submodularity, which is one of the reasons behind these phenomena. The final emergence modeling presented in this paper is not entirely intuitive. The paper does not provide a clear mechanistic explanation of how the percolation model specifically captures the observed emergence, nor does it discuss alternative graph-theoretic models that might also explain the results. The connection between the abstract concept of percolation and the concrete learning dynamics of neural networks remains unclear, and the paper does not address potential limitations of using percolation as an analogy.

### Questions
Please refer to the weakness part:

1. Please justify the relationship with previous paper, and the reason why we can still believe the current LLMs have emergence. If the definition is different, please justify the reason why the new definition is equal or a proper approximation of previous ones.

2. Please justify the use of formal languages, and what will happen if we do not train on well-typed formal languages. 

3. Please provide more physics intuation of current emergence model. For example, during the freezing of water, the Gibbs free energy of water molecules changes, thereby affecting the intermolecular distance and, on a macroscopic level, the volume. We consider this process to be a phase transition.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies emergence of structure and capabilities of a small transformer throughout training on a formal language dataset.
They identify certain phase transitions correlate with the emergence of capabilities to do specific tasks.
They then propose a formulation to predict phase transitions where emergent capabilities, and find that it aligns well with the formal language toy setting.

### Strengths
The paper is well written and a pleasure to read. The paper seems to be also placed well in the context of previous and current related work on emergence. Emergence is an interesting topic for the community, and this paper provides a nice background and definition for studying it in terms of training data. And, while the setting studied is simple, the findings are well supported by their experiments, and the appendix has well-detailed additional evidence.

### Weaknesses
There are other aspects of emergence that are not investigated here that need further study. This paper studies emergence over training data scaling, but they mention other axes (e.g. compute or parameter size) that I feel are also important to make more general claims regarding emergence. While the results in this paper are reasonable for the chosen setting, it is unclear whether they will hold in other settings and data choices. Specifically, the paper focuses on a formal language setting, which may not fully capture the complexities of natural language or other real-world data. The observed phase transitions and their predictability might be specific to the structured nature of the chosen dataset, and it's not clear how well these findings would generalize to less structured or more noisy data environments. This limitation needs to be addressed to make stronger claims about the generalizability of the proposed framework for understanding emergence. 

I also wanted to point out a few (recent) papers there are missing from related work, but seemed relevant. The first is Singh, et al.'s [1] work that studies phase transitions of learning subcircuits for in-context learning tasks. The second is Tigges, et al. [2]'s work, which studies how known circuits evolve in the Pythia suite of models over the course of training.

### Questions
There was a discussion about order parameters early on in the introduction, but this was then ignored until the last paragraph of the conclusion. Can you clarify how your definition of order parameters are different than/related to "progress measures" that others have proposed to study phase transitions (e.g. [3,4])?

___
[3] Barak, et al. Hidden Progress in Deep Learning: SGD Learns Parities Near the Computational Limit. 2022. (https://openreview.net/forum?id=8XWP2ewX-im)

[4] Nanda, et al. Progress measures for grokking via mechanistic interpretability. 2023. (https://openreview.net/forum?id=9XFSbDPmdW)

### Soundness
3

### Presentation
4

### Contribution
3
