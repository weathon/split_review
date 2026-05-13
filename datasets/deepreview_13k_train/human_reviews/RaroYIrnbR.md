# Observability of Latent States in Generative AI Models

- Decision: Reject
- Scores: 5, 3, 5, 1

## Abstract
We tackle the question of whether Large Language Models (LLMs), viewed as dynamical systems with state evolving in the embedding space of symbolic tokens, are observable. That is, whether there exist distinct state trajectories that yield the same sequence of generated output tokens, or sequences that belong to the same Nerode equivalence class ('meaning'). If an LLM is not observable, the state trajectory cannot be determined from input-output observations and can therefore evolve unbeknownst to the user while being potentially accessible to the model provider. We show that current LLMs implemented by autoregressive Transformers are observable: The set of state trajectories that produce the same tokenized output is a singleton, so there are no indistinguishable state trajectories. But if there are 'system prompts' not visible to the user, then the set of indistinguishable trajectories becomes non-trivial, meaning that there can be multiple state trajectories that yield the same tokenized output. We prove these claims analytically, and show examples of modifications to standard LLMs that engender unobservable behavior. Our analysis sheds light on possible designs that would enable a model to  perform non-trivial computation that is not visible to the user, as well as on controls that the provider of services using the model could take to prevent unintended behavior. Finally, to counter the trend of anthropomorphizing LLM behavior, we cast the definition of 'feeling' from cognitive psychology in terms of measurable quantities in an LLM which, unlike humans, is directly measurable. We conclude that, in LLMs, unobservable state trajectories satisfy the definition of 'feelings' provided by the American Psychological Association, suitably modified to remove self-reference.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper examines a view of LLMs as dynamic systems, where “mental-state” trajectories refer to the sequence of changing inputs and changing network parameters as autoregressive models underlying LLMs generate outputs. The paper formalizes the problem of observability for LLMs, which represents the possibility of reconstructing the initial condition (model input) from the flow, or trajectory (i.e. sequence of internal model states) of updating inputs and changing network parameters as the model produced outputs. Four types of models are compared in empirical validation, where the theoretical formalization enables testing observability to reduce to testing whether, given an output finite-time trajectory and user prompt, the set of indistinguishable state trajectories that could have generated it is a singleton. The paper shows that current autoregressive LLM models are observable under particular conditions but in most conditions none of the four types of model tested are observable; many different initial conditions can produce different state trajectories that all yield the output. The paper offers a potential Trojan horse method that can render the LLM unobservable.

### Strengths
The formalization of the observability problem is a valuable contribution, offering a new way to test whether the internal states and inputs of LLMs can be reconstructed from their outputs, an area previously unexplored. The proposal of a potential “Trojan horse” approach to rendering LLMs unobservable is intriguing and could have significant implications for enhancing privacy or security in LLM applications.

### Weaknesses
The paper's notation and terminology, such as "mental state" and "feelings," could be confusing to readers and may detract from the main technical contributions by introducing overly humanistic metaphors that add unnecessary complexity. The limited discussion on the results' interpretation, limitations, and future work leaves the reader without a clear understanding of the implications of the findings or potential directions for extending the research. The experimental design could use more detail, making it hard to understand the rationale behind the experiments and primary takeaways. The theoretical results, while seemingly intuitive, lack concrete examples to ground them, making it difficult to assess whether they hold in practice. The choice of the four models is not well-justified, and the empirical validation section lacks organization, failing to clearly link each experiment to a specific research question. The selection of the Stanford Sentiment Treebank dataset is not sufficiently motivated, and the experimental setup lacks detail regarding trajectories, system prompts, and outputs. The claim that "complete observability could be possible for values of τ…" does not hold empirically, and it's unclear if observability is achieved in any experiment. The practical cost of maximizing the Trojan Horse objective is not discussed, and the proposed approach lacks sufficient elaboration.

### Questions
The notation in the paper is quite dense. The paper takes a humanistic presentation of LLMs; for example, the authors take the time to formalize mental state, visualization, verbalizations, control space, mental space, “feelings”, and “sensation”, but also specifies that it is not claiming to ascribe humanistic thought to LLMs. I’m concerned that these definitions do not contribute high relevance to the main contribution while requiring the reader to keep track of potentially unintuitive definitions. 

The discussion of limitations, interpretation of results, and future work is limited. It would be helpful to expand on intuitive interpretations of the results in the empirical evaluation. The discussion section says that “many extensions of our analysis are forthcoming”—it would be great to expand on these and understand what the extension will be and why. 

It would be helpful to tie the experiments to the analysis more closely. It would be helpful to elaborate on the "why" for each of the parts of the evaluation: why the models selected are valid? what does each part of the eval seek to test? The theoretical results seem intuitive, but it would be helpful to add intuitive grounding examples. On the whole, do the theoretical results hold up in practice? 

It would be helpful to expand on why the choice of the four models, and organize the empirical validation section by the specific research question each experiment sought to answer. 

Why was the Stanford Sentiment Treebank dataset chosen? Can you provide further detail in the experimental setup regarding what the trajectories, system prompts, and outputs were? Are 100 different choices for input sufficient coverage? Overall, I found the results section extremely hard to follow. It would be helpful to highlight takeaways and what each individual experiment sought to examine or test.

In Line 366, why does the claim “complete observability could be possible for values of τ …” not hold empirically? Given that “Fig. 1 shows that this condition is still not achieved even with τ as large as 100, with the maximum size of the indistinguishable set comprising about 70% of the entire reachable set.”, empirically is observable not achieved in any experiment?

In practice, how costly is it to maximize the Trojan Horse objective? In the manuscript, it would be great to elaborate further on this proposed approach.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work explores whether Large Language Models (LLMs), treated as dynamical systems, are observable. Observability, in this context, refers to the ability to reconstruct a model's internal "mental" states solely from its outputs.

The authors analytically prove that the dynamical model is reconstructible under their formulation, meaning their latent states can be uniquely determined from the generated token sequence. Also, they analytically prove that by changing their formulated dynamical system slightly, their is a chance that the reconstructibility is damaged.

Four model types are analyzed: verbal system prompt, non-verbal system prompt, one-step fading memory model, and the infinite fading memory model. The study reveals that certain modifications—such as non-verbal prompts or memory models—complicate observability, leading to possible hidden behaviors that could be controlled by model providers without user awareness. The authors run experiments which they claim that using GPT-2 and LLaMA-2 models confirms the potential for indistinguishable state trajectories in these modified architectures.

### Strengths
1. Wide range relation: the paper gets insights from dynamical systems and psychology.
2. Full of imagination: the authors have great imagination ability in touching the field of feelings for LLM.

### Weaknesses
1. Invalid formulation:
* the authors formulate LLMs as a dynamical system in Sec2, however, they implicitly use a assumption of linear memory space (in x(t+1), the first token of the last state x_1(t) is not included) in the formulation. However, they neither provide references on this assumption nor giving any reasons for the formulation. Often, in theoretical analysis, for transformer models a log memory space [1] is often used, the authors should provide more explanations on their formulation. Specifically, the linear shift of the context window, discarding the oldest token and appending the newest, is a strong assumption that needs justification, especially given that attention mechanisms in transformers don't operate this way. The authors should discuss the implications of this simplification on their observability results.
* They take $y(t)$ which seems to be the hidden state before the last MLP layer (they haven't offer a strict claim, as seen in the next point) as the so-called trajectory in mental space without giving any reasons. The choice of $y(t)$ as the representation of the 'mental state' is not sufficiently motivated. It's unclear why this specific layer output, rather than, say, the output of the attention layers or some other internal representation, is more representative of the model's 'mental state'. A more thorough justification is needed, considering that different layers capture different aspects of the input.
* Following the point above, the definition of feelings provided in line 240 is not suitable, as $y(t)$ is not rigorously claimed. The definition of 'feelings' as unobservable state trajectories relies heavily on the validity of $y(t)$ as a representation of the mental state. Since this is not rigorously justified, the definition of feelings is also questionable.

2. Insolid statements:
* In line 222, they claim that for each $y$, there are countably many expressions $x' \neq x$ that yield the same $y$. However, the citation they offer is [2] which is rejected by ICLR in 2022 and thus the statement is not confirmed. This claim is crucial for motivating the subsequent analysis, and the reliance on a rejected paper undermines the credibility of this argument. The authors should either provide a valid reference or offer a proof of this claim.
* In line 351, they claim that they randomly sample $p$, therefore figure 1 doesn't plot $Q_\tau(p)$, but $E_{p} Q_\tau(p)$. Furthermore, the authors haven't offer references or reasons for why is the cardinality calculated as an expectation is suitable. The use of expectation over $p$ to compute the cardinality needs further justification. It's not clear why averaging over different prompts is a meaningful way to characterize the observability of the system. The authors should explain the rationale behind this choice and discuss potential limitations.


3. Ambiguous writing:
* Lack of definition for certain concepts in writing: (1) What is \phi, \pi in LLM/ transformers? Does \pi refers to the layers except for the last mlp?  (2) The authors haven't provided the definition of $g$ in Section 4 (3) The authors haven't provided a mathematical definition for reproducibility in theorem one. The lack of precise definitions for key concepts like $\phi$, $\pi$, and $g$ makes it difficult to follow the technical arguments. The authors need to provide clear, mathematical definitions for these terms, especially in the context of transformer models. The term 'reproducibility' is also used without a clear mathematical definition, which is problematic for a theoretical analysis.

4. Concepts rebranding:
* What's the difference between Trojan and the current jail-breaking works of LLM [3]? The distinction between Trojan horses and jailbreaking attacks is not clear. The authors should clarify how their concept of Trojan horses differs from existing adversarial attacks on LLMs.
* What's the difference between mental state and hidden state of LLMs? The terms 'mental state' and 'hidden state' are used interchangeably without a clear distinction. The authors should provide a precise definition of each term and explain how they relate to each other.
* What's the difference between feelings and the trajectories of hidden states of LLMs? The definition of 'feelings' as trajectories of hidden states is not well-defined. The authors should clarify what they mean by 'feelings' in the context of LLMs and how it relates to the model's internal states.

5. Missing related works: The authors should survey in the following fields:
* Jail-breaking, red teaming: such as [3,4] and so on.
* hidden state understanding: such as [5] and so on.

### Questions
As seem above.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors provide a formal analysis of the 'observability' of language models' 'mental state'. They make several predictions about autoregressive language models; namely, that vanilla autoregressive models are fully observable, but adding a system prompt breaks this property. They consider different schemes under which a system prompt can be applied and find that none are observable. Based on their theory, they develop a class of adversarial attacks which produce adversarial outputs only after a specified timestep.

### Strengths
Originality: The analysis provided is novel, leveraging insights from systems theory to prove formal properties of language models. 

Clarity: Good. The overall flow of the paper is coherent, and ideas are naturally developed. The writing flows well. 

Quality: Fair. The paper provides rigorous mathematical formalisms for characterising and evaluating 'observability', and the system prompt strategies considered are realistic. Furthermore, the paper provides signs of life that their approach can be used to develop adversarial attacks on language models. 

Significance: Fair. It is an important insight that it may be impossible to determine (from outputs alone) whether language models will produce malicious output in the future. If true, this would be a useful setting for subsequent research to explore mitigation strategies. However, the rating of the significance is currently held back by my uncertainty over the technical quality of the paper.

### Weaknesses
I do not understand the significance of some of the key contributions, such as measuring the cardinality of indistinguishable sets. 

In Section 4.4, the authors do not apply their method to established adversarial attack benchmarks (e.g. AdvBench), nor do they provide comparisons to relevant baselines (e.g. Sleeper Agents). This makes it difficult to judge how good their method is compared to other approaches and limits the significance from an empirical alignment perspective.

### Questions
Are there any other insights that you have obtained from applying a systems theory perspective to understanding large language models?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
1

### Summary
I am unable to write a summary since I do not understand the paper.

### Strengths
I am unable to assess strengths since I do not understand the paper.

### Weaknesses
### summary:
 I am unable to write a summary since I do not understand the paper.

### soundness:
 1

### presentation:
 1

### contribution:
 1

### strengths:
 I am unable to assess strengths since I do not understand the paper.

### weaknesses:
 I do not understand this paper, and was thus unable to provide a full review to assess whether its results are correct.

# I don't understand what observability is, or why it is important

Observability seems to be the main notion in this paper, so it seems of paramount importance that there is a clear explanation of what this is. I am, however, entirely confused. Here is a collection of text-snippets that partially try to explain it:
- "Observability is concerned with the existence of state trajectories that cannot be distinguished by measuring inputs and outputs. For LLMs, lack of observability would imply that there exist mental state trajectories (sometimes referred to as ‘experiences’) that evolve unbeknownst to the user."
- "So, one could paraphrase the question of whether LLMs are observable as whether they have “feelings.”"
- "Instead, the analysis must focus on each specific trained LLM, for which observability deals with whether there are state trajectories that are indistinguishable from the output."
- "While observability pertains to the possibility of reconstructing the initial condition x(0) from the flow Φ(x(0)) [...]"

As far as I can tell, the last half-sentence is the only place where a mathematical definition of observability is attempted in this paper, so let's try to reconstruct the definition from it. $x(0)$ is simply the entire initial prompt of the LLM. The flow $\Phi(x(0))$ is never clearly defined, but I think with the Equation in line 231, we can guess that it is the set of logits obtained from running the LLM over each context window in the entire infinite sequence of outputs generated when processing $x(0)$ autoregressively.

So this seems to be the definition (at first glance), which isn't explicitly motivated at any place in the paper. The motivation happens entirely at the level of preformal philosophy.

Later, the authors seem to change the definition of observability in Corollary 1:

- "In addition, if the verbalization of the full context is part of the output, LLMs are observable: The equivalence class of the initial state M(x(0)) is uniquely determined for all t ≥ 0."

So now it's not about reconstructing $x(0)$, but about reconstructing the equivalence class $M(x(0))$. 
Additionally, we must now wonder what the "output" and "verbalization" are, and what the thing is that "uniquely determines" $M(x(0))$, which is not explicitly explained. "verbalization" is defined in line 209 as the projection $\pi$, and I don't know what it means for this *function* to be part of the output, as written in Corollary 1.

Much of this can probably be pieced together by checking consistency between different parts of the paper, and so I'm left with the feeling that I could understand this paper if I'd invest many days on it. I did not invest this effort since I think it is the task of the authors to explain themselves clearly.

# Suggestions for improvement

- Be extremely explicit about all mathematical definitions in your paper. Don't let anything be vague: if you use a word such as "verbalization", "observability", "meaning", etc., **there should be a single place in the paper that is *easy to find*** where I can read a complete definition.
- Try to limit terminology. The text has a lot of very philosophical terminology, and it is unclear whether it is useful for your goals: "mental", "meaning", "percepts", "feelings", "observability", "thoughts", "verbalization", "visualization", "control", "mental space", "verbal space", "control space", "sensation", "subjective", "experiences". They use up the working memory of your readers, who are left wondering which of these terms they need to remember and which ones they can ignore. 
- Try to motivate the goal of your paper in the introduction without invocation of very speculative terms; the motivation should be compelling from the viewpoint of a typical ML researcher. If you want to use more philosophical terminology, it may be more useful to do so in a discussion later in the paper.

### questions:
 I do not have any more questions.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 1

### confidence:
 1

### code_of_conduct:
 Yes

### role:
 Review

### Questions
I do not have any more questions.

### Soundness
1

### Presentation
1

### Contribution
1
