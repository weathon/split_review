# Decoding Intelligence: A Framework for Certifying Knowledge Comprehension in LLMs

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 3, 6

## Abstract
Knowledge comprehension capability is an important aspect of human intelligence. As Large Language Models (LLMs) are being envisioned as superhuman
agents, it is crucial for them to be proficient at knowledge comprehension. However, existing benchmarking studies do not provide consistent, generalizable, and
formal guarantees on the knowledge comprehension capabilities of LLMs. In
this work, we propose the first framework to certify knowledge comprehension in
LLMs with formal probabilistic guarantees. Our certificates are quantitative -
they consist of high-confidence, tight bounds on the probability that a target LLM
gives the correct answer on any knowledge comprehension prompt sampled from
a distribution. We design and certify novel specifications that precisely represent
distributions of knowledge comprehension prompts leveraging knowledge graphs.
We certify SOTA LLMs for specifications over the Wikidata5m knowledge graph.
We find that knowledge comprehension improves with increasing model size.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to provide formal guarantees of model knowledge, as elicited by prompts derived from Wikidata. The object of the formal guarantee is the correctness of an answer to a question representing an arbitrary k-hop question stemming from some pivot node in the Wikidata knowledge graph. The means of formal guarantee is a binomial proportion confidence interval. To the best of my understanding, what this means is that the method guarantees model correctness with high confidence over a subgraph of Wikidata. The reason this requires a probabilistic guarantee, and cannot be done exhaustively, is that the combination of contexts for the questions, distractor text to provide alongside context, and few-shot examples for prompting the method creates a large prompt space that would be infeasible to exhaustively search. Experiments demonstrate that the authors can often bound model accuracy over a subgraph of Wikidata within about +/- .05 points.

### Strengths
- Important: I like the spirit of trying to give formal guarantees to model correctness for LLMs, which are difficult to handle analytically. The approach of using binomial proportion confidence intervals is a simple but appropriate one.
- Important: Experiments are carefully designed to demonstrate the main claims of the paper. A wide variety of models are tested.

### Weaknesses
 - Important: While the main result in this paper is interesting, I also find it hard to say that it is especially impactful. The basic approach is to use a binomial proportion confidence interval to  estimate a model accuracy over a data distribution. The only way that this setting differs from any typical ML benchmark is that the authors define a data distribution over a subnetwork of Wikidata. As the authors note in L.242, longer paths in k-hop questions can result in somewhat surprising or meaningless queries. So I ask, what is really the point of certifying knowledge over such a subgraph? As in the qualitative example, we are not certifying knowledge about a movie. Rather, we are certifying knowledge about a movie, as well as a surprisingly diverse set of entities that are related to the movie. And, even if we were certifying knowledge about a movie, the next question is if the method in this paper merits publication if it primarily just makes use of an existing analytical binomial proportion confidence interval.
- Of some importance: While I believe the central point that we cannot exhaustively test deep learning models over input spaces is well-received, the paper has to introduce some complexity in order to make this difficulty appear in the first place in their setting. Specifically, aliases, contexts, distractors, and few-shot examples are randomly ordered in order to make the input space too large to exhaustively search. I believe it would also be possible to fix a basic set of instructions for strong models like Gemini and do these questions zero-shot. In that setting, there would not be a large combinatorial space to explore. Or, it might be more appropriate to generate model-based paraphrases of the input question, which may be more naturally representative of knowledge query diversity than the chosen approach.

### Questions
- L.65: strictly speaking, it’s not just the high number of parameters, right? Also nonlinearities?
- What makes R in L.274 a random variable? Is the any(.) operator effectively a uniform distribution? How is it defined? Later, when the paper says “we equally prioritize the different possible path lengths”, does this mean that the any(.) operator appropriately reflects this choice, or is there any bias in the estimator?
- Why use a multiple-choice format? Is the task too difficult otherwise?

### Soundness
4

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
The authors introduce QuaCer-C, a framework designed to assess knowledge comprehension in LLMs by sampling paths of lengths 1 to 5 from the WikiData5m knowledge graph and constructing context + distraction + query sets as tasks for the models to complete. Since responses are evaluated on a success/fail binary basis, Clopper-Pearson confidence intervals are used to establish upper and lower bounds for the resulting metrics. Experiments on major closed-source and open-source LLMs indicate that larger models perform better, while shuffled contexts and added distractors degrade performance.

### Strengths
1. Provides a robust quantitative probabilistic framework for evaluation.
2. Overall, the presentation is clear and the structure flows well.
3. Accompanied by code for reproducibility.

### Weaknesses
1. The findings are somewhat predictable and could benefit from deeper insights.
2. Some redundant content in the main text could be replaced by key details currently in the Appendix, such as the process for generating queries and context.
3. There’s ambiguity as to whether the LLM’s responses are derived from embedded knowledge or the provided context, thus raising questions about true comprehension. The prompt itself does not restrict the LLM to answer based solely on the given context. For example, in a hypothetical question like “Matthew Perry→(character_acted_by)→(birth date)→?”, the LLM could respond from its internal knowledge base rather than relying solely on the provided context.

### Questions
1. Given that the framework already uses a probabilistic approach, why not leverage the fact that an LLM can act as an implicit conditional probabilistic model? For instance, adjusting the output threshold or re-querying could yield probabilities that reflect comprehension more accurately.
2. Relating to weakness 3: Why are aliases for entities and relations randomly sampled? This approach may inadvertently query the LLM’s embedded knowledge (e.g., recognizing that alias A corresponds to B), which might not be present in the provided context.
3. Regarding sampling: How does the chosen sample of n=250 compare in ratio to the full knowledge graph? Additionally, how do we justify that this sample is unbiased, given that only the top 2000 nodes and edges are selected?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to develop a formal certification framework for evaluating knowledge comprehension in LLMs. The authors propose an approach that frames knowledge comprehension as a formal specification using a knowledge graph. The accuracy of LLM responses is assessed by the probability of generating correct answers to knowledge comprehension prompts sampled from a distribution based on the knowledge graph. However, this approach, in my opinion, closely resembles a basic KBQA evaluation process for LLMs and lacks difference compared to existing work. Furthermore, current proprietary models, such as Gemini-Pro and GPT-4o, have already demonstrated impressive accuracy in knowledge utilization, as shown in Figure 3, with performance scores between 0.7 and 0.8, which raises questions about the significance of this task and the motivation of this work.

### Strengths
1. This paper provides a detailed description of the approach, including the formalization, theoretical framework, and algorithmic implementation.
2. Models of varying sizes and employing different pretraining techniques are evaluated.

### Weaknesses
This paper provides an extensive and complex introduction and description of the approach for formalizing knowledge comprehension evaluation using a knowledge graph. The knowledge comprehension capability of LLMs is assessed by measuring the accuracy of their responses to prompts sampled from paths within the knowledge graph. However, (1) there is no rigorous theoretical proof to guarantee the approach, and (2) it appears to be a very basic, standard KBQA evaluation process using LLMs nowadays, lacking distinction from existing work. I find the motivation, novelty, and differentiation of this work unclear. Some related work is omitted like [1,2]

### Questions
1. Is the evaluation process merely a standard method of sampling questions from a knowledge graph to assess LLMs? If so, why not utilize existing KBQA/GraphQA datasets?
2. Is there any theoretical guarantee for the bounds introduced?

### Soundness
2

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
The paper introduces QuaCer-C, a protocol to assess the knowledge comprehension abilities of LLMs, i.e. their ability to extract information from reference inputs and reason over it to answer questions. To this end, the authors introduce an evaluation protocol that constructs multi-step reasoning queries together with multiple-choice answers and gathers reference information based on traversing a knowledge graph. By sampling many paths starting from the same root node, the authors are able to estimate confidence intervals for whether an LLM will answer knowledge comprehension queries based on that root node correctly. The paper uses this approach to quantitatively and qualitatively evaluate the knowledge comprehension abilities of several popular open-weight as well as closed models. The results show that closed models significantly outperform closed ones, and sheds lights on the failure modes of knowledge comprehension.

### Strengths
1. Overall, the paper is well-written and easy to follow.
2. I believe that the introduced knowledge comprehension test can serve as a useful benchmark for evaluating the ability of LLMs to retrieve information from prompts, reason about that information and use it to answer complex questions.
3. The paper provides a comprehensive assessment of the knowledge comprehension abilities of many of the currently most popular LLMs.

### Weaknesses
1. I am not sure in which situations the correctness certificates derived by QuaCer-C would be useful. The certificates hold for prompts sampled from the same distribution as the 250 sample prompts. But that means that certificates can only be obtained for cases where a corresponding knowledge graph exist and the relevant queries can be expressed as graph traversals. But in such cases, it would be much simpler to query the knowledge graph directly, rather than using an LLM to extract information from and reason over it. The cases where LLM-based knowledge comprehension is actually required are typically much less structured documents without a corresponding knowledge graph, but in those cases QuaCer-C cannot compute certificates. I still think the prompt construction and evaluation approach can serve as a useful benchmark for the knowledge comprehension abilities of LLMs, but I don't see a scenario where the derived certificates would be useful.
2. The approach might incorrectly mark answers as wrong in case of 1 - n or m - n relationships. E.g. in Figure 4, first row, in the example "Batman Begins: ... -> (characters) -> (artist) -> (nomination received) -> ?" there could be multiple characters (1 - n relationship) whose artists might have received different nominations. The model might pick a different but valid character than intended and then reason correctly, potentially using its parametric knowledge, and arrive at a different than expected, but still correct answer. This issue is not addressed by the multiple-choice format, as the model could correctly reason to a different but valid answer that is not among the choices.
3. The paper claims that larger models are better at knowledge comprehension. While Table 1 provides some evidence in this direction, I believe that it is insufficient to confidently claim a size-dependent relationship, because of a number of potential confounders: 1) The smaller models in the table are all open source ones, while the larger ones are closed, and their size is not (officially) known. 2) Except for (Phi-3-3B, Phi-3-14B) and (Gemini-1.5-Flash, Gemini-1.5-Pro) (whose size difference and other potential differences are unknown), all models belong to different families, so other than size they might also differ in training data mixtures, training strategies and architecture. The only really comparable datapoint here is (Phi-3-3B, Phi-3-14B), and those two models show 1% or less difference. To make claims about model size effects more reliable, comparisons of several (open) models within the same family would be needed.
4. Minor clarity issue: It was not clear to me how the few-shot examples are constructed until I came across Appendix B.5. Please reference the appendix in the main paper and provide some minimal information about the few-shot examples, e.g. that the same fixed set of examples is used for all prompts.

### Questions
### Questions
1. Does the approach also work without few-shot examples? Or are they needed to convey the answer format?
2. How long is the context (per node) and does it contain information beyond the Wikipedia page's abstract? The authors mention that only one distractor is included due to context size limitations. However, all the studied models support, or have versions that support, context lengths of at least 32k. At least if Llama-3.1-8B was used, rather than Llama-3-8B, which I'm not sure about.
3. Do the authors think that techniques like chain-of-thought prompting would change the results? The paper investigates problems that inherently require multi-step reasoning, whereas the evaluation expects models to produce the answer almost as the first token. Allowing for additional reasoning steps might significantly improve accuracy.

### Suggestions
1. It would be helpful to include the appendix into the main paper's PDF, not as a separate file.
2. It might be helpful to name the certified property, i.e. "our overall property", line 228.
3. Currently, prompts are constructed by sampling graph trajectories starting from a specific root node. Another interesting approach might be to sample trajectories whose edges all have the same relationship type, e.g. which are all of the form "... -> (appeared in movie) -> (directed by) -> ?", irrespective of the nodes that appear in them. Such an approach might be able to assess/certify how well a model can comprehend knowledge about a particular multi-step relationship, irrespective of what the exact entities are, e.g. how well the model can comprehend which directors an actor worked with.

### Soundness
3

### Presentation
3

### Contribution
2
