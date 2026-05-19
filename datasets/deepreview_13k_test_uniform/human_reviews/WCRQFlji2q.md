# Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models

- Decision: Accept
- Scores: 10, 8, 10, 8

## Abstract
Hallucinations in large language models are a widespread problem, yet the mechanisms behind whether models will hallucinate are poorly understood, limiting our ability to solve this problem. Using sparse autoencoders as an interpretability tool, we discover that a key part of these mechanisms is \textit{entity recognition}, where the model detects if an entity is one it can recall facts about. Sparse autoencoders uncover meaningful directions in the representation space, these detect whether the model recognizes an entity, e.g. detecting it doesn't know about an athlete or a movie. This suggests that models can have self-knowledge: internal representations about their own capabilities. These directions are causally relevant: capable of steering the model to refuse to answer questions about known entities, or to hallucinate attributes of unknown entities when it would otherwise refuse. We demonstrate that despite the sparse autoencoders being trained on the base model, these directions have a causal effect on the chat model's refusal behavior, suggesting that chat finetuning has repurposed this existing mechanism. Furthermore, we provide an initial exploration into the mechanistic role of these directions in the model, finding that they disrupt the attention of downstream heads that typically move entity attributes to the final token.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper discusses some interesting features found in sparse features extracted from Gemma 2 2B and 9B models with the Gemma Scope SAEs. These features, when queried on the final token of an entity mention, are predictive of whether the model correctly recalls facts about that entity in a synthetic task constructed from Wikidata. Some features generalize across multiple (four) entity types, and interventional experiments on chat-tuned models find that they mediate refusals in these models, suggesting that RL training may preferentially lead models to repurpose these mechanisms developed in pretraining. Further analysis shows that these features, when activated, disrupt the normal mechanisms for factual recall by blocking attribute extraction heads. A final experiments identifies SAE latents in a similar spirit which are predictive of model mistakes.

### Strengths
* The paper is excellently written. The prose is very clear and the arguments are well structured.
* The paper fruitfully pursues multiple lines of evidence for its core claims about the latents it identifies in the model it studies. Having correlational and causal analysis on multiple fronts including with the RLHF'd model makes the central idea feel pretty solid.
* The paper is well scoped.

### Weaknesses
Some of the claims of the paper feel not quite adequately supported by the experiments. I'm not really doubtful of the reasonableness of the claims but I think the paper should quantify and qualify them better.
* I think the choice to describe these latents as representing "self-knowledge" is a little bit dicey. The description only clearly applies to the chat model. For the base model I think a sufficient explanation of the evidence with fewer assumptions is to say something like they're latents for "entities it knows about" versus "entities it doesn't know about or treats as novel". You could make progress disentangling this from 'self-knowledge' by looking at how these latents behave on fictional narrative versus newswire versus encyclopedic text (the former two should have been written after training cutoff). I would expect the 'known entity' latents to fire increasingly more as you move from fiction->news->encyclopedia and opposite for 'unknown entity' latents. Analyzing these results could help us understand why the features are learned, e.g., if the the model needs to know whether it is writing stories or stating facts.
* The paper claims that the features generalize over multiple entity types. This is a binary statement but of course is about a graded judgment regarding the amount of generalization. But there is no quantitative claim in the paper about the degree to which this is true in an absolute sense—only that it is _more_ true in the middle layers. That doesn't mean that it's particularly true anywhere. The maxmin metric makes sense for relative comparisons but is difficult to understand on an absolute level. Indeed, when you select the "most general" latents based on this metric it's unclear if these features are actually general across more than the four entity types you use or if you may just be selecting on noise. To measure this, you should measure what happens when you select latents based on their generality across a subset of entity types, and test their separation score on held-out entity types. Some measure of how predictive this selection is of separation for new entity types gives an actual measure of the generality of the latent.
* In the mechanistic analysis (p.6–7) the paper points to figures which seem to show that attention to an entity is decreased when the unknown entity latents are steered (increased). It's not clear to me from the text if this is averaging across all attention scores or some subset ("these attention heads", L345, reads to me like the latter, but I'm not sure which subset) and the results of this experiment aren't quantified. There should be some straightforward measure here which you can use to quantify the suppression effect here (which will also allow you to claim statistical significance — you do say "significantly" on L346 without a relevant quantity or p-value, which leaves it unclear if you actually mean statistical signifiance)
* The results in Figure 5 seem dubious. They are really hard to read because of the overlap of all of the confidence intervals but overall nothing significant seems to be happening here. I think you'd need to run this study on much more data to get something interesting/clearly meaningful and I also find this the least interesting or informative experiment in the paper. Mild recommendation to appendicize it. (and strong rec to make the statistical claims precise either way: is the effect you're talking about significant or not?)

### Questions
* The main text doesn't say which direction d_j you orthogonalize out on p.6. (caption says it but main text description of what you do is disjointed.)
* Equation 11's use of the word `model` is weird. I assume it's supposed to be a metavariable, but I don't feel like the red highlight conveys this (since it's used for something else above). You already frame it as an example—why not use the actual example correct or incorrect answer there? I think it'd be fine to have a line break in there if the problem is making it fit on the page.
* Do you have a succinct/clear and empirically grounded explanation of why you use (your formulation of) latent separation scores for the first analysis and t-statistics for the second? It sounds like the features often activated on both categories and the separation scores probably just weren't as good in the latter case, is that right? Seems worth being explicit about in the paper.
* Can you clarify in the paper how you use the train/test split in the analysis in Section 7? I assume the graphs in Figure 6 plot results for the test set. Also again please give statistics on your results and discuss significance.
* Do you think you can add some discussion in the paper about how your approach can be generalized to other kinds of features? The targeted investigation you do is interesting on its own but I think it'd be great to highlight if there's anything else that someone can expect to discover by adapting your analysis setup to different datasets.

[Edit: many of the weaknesses and questions have been answered adequately by the reviewers, so I've upped the soundness rating from 3 to 4 and overall rating from 8 to 10.]

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Using sparse autoencoders (SAEs), this paper shows the existence of directions in the latent space of LLMs responsible for entity recognition i.e. detecting whether the entity is a known entity or not. The paper shows that these identified latents are causally responsible for LLMs refusing to answer questions. The paper shows how these latent directions are responsible for regulating attention scores, and also responsible for directly expressing knowledge uncertainty. All experiments are conducted with Gemma 2 models (2B and 9B) where SAEs are available.

### Strengths
1. The result showing that directions identified using base model, causally affect refusal in chat-finetuned models is very interesting — the transfer from base to instruction/chat finetuned model is not obvious, and indicates a mechanism for how refusal finetuning can generalize beyond the specific entities it was finetuned on. 

2. All of the experiment and results figures seem thorough and convincing (e.g. error bars, useful and clear visualizations etc.)

3. The paper also shows that interestingly, the same entity recognition directions regulate the model's attention mechanism (the factual recall mechanism) and directly express knowledge uncertainty (line 355, although the effect is not as strong).

### Weaknesses
1. Definition of known and unknown entities — the paper categorizes entities as known if it gets at least two attributes right, and unknown if it gets all attributes wrong. While this is fine, it does leave open the possibility that what is currently categorized as unknown is actually known by the model and can perhaps be elicited with a better prompt or few-shot examples. Alternatives to the current categorization could be – (a) checking across a diverse set of prompts to decide known and unknown as in https://arxiv.org/abs/2405.05904 ; (b) relying on n-gram matching in the pretraining data (would need to use LLMs with open pretraining data) ; (c) focusing on entities which occur after the knowledge cutoff for the unknown category. 

2. Explanation for existence of generalized latents that distinguish between known and unknown entities — the paper currently suggests that this is evidence of ‘self-knowledge’. An alternative and much simpler explanation which currently can’t be ruled out is that these latents are activated on high likelihood tokens (known) and low likelihood tokens (unknown). It would be useful to show some kind of control experiment to show that is not the case. 

3. (minor) In general, I also find it hard to directly interpret the results in Fig 2. The min-max value peaks at around 0.4 for unknown. How high should that value be to conclude the existence of generalized latents? I feel like if the set of the entities is small enough and the set of latents large enough, then there might always exist such latents? (Fwiw the additional results later do make it convincing that these are generalized latents)

### Questions
1. Formatting — the bottom margin seems much bigger than in the ICLR template?

2. Line 160, on average how many attributes does each entity have?

3. I also couldn’t find details about how many entities of each type was used in the analysis.

4. Figure 5 — Prior work has shown that LLMs are better calibrated when using few-shot examples (e.g. https://arxiv.org/abs/2207.05221) — have you tried changing the prompt in 10 (line 359) to see if the intervention has a bigger effect in that case?

5. Line 35 Relevant citation - https://arxiv.org/abs/2310.15910 

6. Sec 7 — prior work (e.g. https://arxiv.org/abs/2310.18168) also shows that linear probes can be trained to predict truthfulness / correctness before the answer (just from the question), which would indicate similar findings as in section 7.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
The paper revealed that the knowledge of a large language model can be detected from a sparse latent space. There are several important findings:

- The last token of known and unknown entities have similar latent representation respectively in a sparse latent space across different entity types.

- The latent representation of entities has an influence on LLM generation and steering the representations will affect the refusal and fact recover behaviors of LLMs.

- The latent representation can predict the correctness of generated answers.

### Strengths
The findings of the paper (see summary) are well supported by the experiments and can provide valuable scientific insights to the community. The presentation is great and readers can easily follow.

### Weaknesses
The experiments are now only for Gemma models. It would be interesting to see the model behavior on other LLMs.

### Questions
How does the model size influence the conclusion of the study?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the mechanisms behind LLM hallucinations by using sparse autoencoders -- SAEs to analyze internal model representations. The key finding is the discovery of "entity recognition" directions in the representation space that detect whether a model can recall facts about specific entities. These directions generalize across different entity types (movies, cities, players, songs) and causally influence whether the model refuses to answer questions or hallucinates information. More interestingly, the directions found with a base model can transfer to a chat model and control the model's tendency in refusing to answer questions.

### Strengths
- Empirically link the "entity recognition" directions and the models' refusal in answering questions
- The experiment includes clear experimental design using diverse entity types
- Shows interesting discovery that base model mechanisms are repurposed during chat model fine-tuning

### Weaknesses
- **Lack of comparison to methods other than SAEs**: If we remove the sparsity of the SAE and reduce the module to a regular AutoEncoder, would the same properties hold? If we further remove the auto encoder and just use a linear probing module, would the same properties hold? Is it really necessary to use sparse and auto encoder modules to get the interpretability? If we borrow the same idea from ITI [1] to steer model towards a more truthful direction in the latent space, can the same property holds? Lack of ablation on the necessity of SAE is a big flaw of this paper.
- **Lack of model diversity**: Only the Gemma models are tested. It would be better if we can see the same findings on LLaMA or other models to show how universal this idea holds.

[1] https://arxiv.org/abs/2306.03341

### Questions
- Can you provide more ablation study to show that it's really necessary to use both 1) sparse and 2) auto encoder modules to get the interpretability?

### Soundness
3

### Presentation
3

### Contribution
3
