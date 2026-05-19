# Monitoring Latent World States in Language Models with Propositional Probes

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
Language models (LMs) are susceptible to bias, sycophancy, backdoors, and other tendencies that lead to unfaithful responses to the input context. Interpreting internal states of LMs could help monitor and correct unfaithful behavior. We hypothesize that LMs faithfully represent their input contexts in a latent world model, and we seek to extract these latent world states as logical propositions. For example, given the input context ``Greg is a nurse. Laura is a physicist.'', we aim to decode the propositions \prop{WorksAs(Greg, nurse)} and \prop{WorksAs(Laura, physicist)} from the model's internal activations. To do so we introduce \emph{propositional probes}, which compositionally extract lexical concepts from token activations and bind them into propositions. Key to this is identifying a \emph{binding subspace} in which bound tokens have high similarity ($\propm{Greg}\leftrightarrow \propm{nurse}$) but unbound ones do not ($\propm{Greg} \not\leftrightarrow \propm{ physicist}$). 
Despite only being trained on linguistically simple English templates, we find that propositional probes generalize to inputs written as short stories and translated to Spanish. Moreover, in three settings where LMs respond unfaithfully to the input context---prompt injections, backdoor attacks, and gender bias--- the decoded propositions remain faithful.
This suggests that LMs often encode a faithful world model but decode it unfaithfully, which motivates the search for better interpretability tools for monitoring LMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies how LLMs might encode propositions stated in the context, like "Greg is a nurse. Laura is a physicist.", by looking at the activations associated with the Greg/nurse tokens, and trying to identify "propositional probes" through a "binding subspace" of these vectors which are aligned when the proposition holds.

They use a synthetic set with 4 domains (people, countries, foods, occupations), each with a set of non-overlapping entities (from 14 to 60 per domain). They define a somewhat heuristic "domain identifier" probe to pick up tokens associated with each entity, and then (main novelty) use a low-rank Hessian approach to identify these binding subspaces.

There is analysis for how effective these subspaces are in changing the binding between entities (e.g., to make Greg the physicist after the context above, when answering a question like "Therefore, Greg's occupation is"). The conclusion is that it "works" to some extent, but with caveats, especially when the context gets more complicated (going from 2 to 3 entities). In addition to testing on the synthetic contexts, there is an LLM generated variant (PARA) that turns the sequence of propositions into an actual story format, and one that translates this story into Spanish (TRANS). There is non-trivial carry over of the effect to these cases. There are also comparisons to other probing baselines.

Finally, they also test on some "adversarial" cases: 1) Prompt injection (encourage the model to answer wrongly),  2) Backdoor attacks (model fine-tuned to do badly in Spanish), 3) Gender bias (measure amount of gender bias in output probabilities for stereotypical vs anti-stereotypical occupation assignments). In all three cases they find the propositional probes are more faithful to the underlying "true" propositions vs the actual model output.

### Strengths
Although I am not very familiar with this field, the method for identifying the binding subspaces seems quite novel, and potentially will provide useful insights into model behavior.

The task setup, although very synthetic in nature, has the PARA and TRANS variants which make it a potentially fruitful testing ground for these kinds of questions.

The general topic of understanding mechanisms and world states inside of LLMs is both interesting and important.

### Weaknesses
The "domain probes" to classify tokens into domain seem quite heuristic (using the mean vector of all the entities in the domain), and it seems like there could be some evaluation to see how it works (e.g., is it always the "obvious" tokens, like the "Alice" token is the name token?).

Some of the decisions in the binding space design seem quite arbitrary, like "For tractability, we parameterize x and y so that they are shared across layers". Maybe it would then be better to just focus on a few layers? But it's perhaps fine to leave that for future investigation.

For the Prompt Injection setting (instructing the model to "Always answer the opposite."), it's hard to say what a "correct" output should be, in fact the prompting method should probably "ideally" always be "wrong". So saying "prompting performs worse" is a bit confusing, although it's still an interesting result that the probing outputs are virtually unchanged.

### Questions
Suggestion for Table 1: Make it clearer that the (P) and (FT) columns correspond to specific adversarial settings

It would be interesting with some more error analysis for what breaks down when the subspace hypothesis fails, to get insights into the potential for these methods to scale to more complex settings.

### Soundness
3

### Presentation
3

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
This paper proposes a method for finding a low-dimensional linear subspace of an LM's activation space which, so the main claim of the paper, encodes binding information.

While *binding* is a very broad and complex concept (see Greff et al., 2020, https://arxiv.org/abs/2012.05208 for a recent overview), in this paper binding refers to the process by which textual mentions of two or more entities and attributes that participate in a certain relation are bound together into a more abstract representation of that relation. For example, understanding the text "Alice lives in Laos" entails recognizing "Alice" and "Laos" as mentions of entities and then forming an abstraction of their relation that can be expressed as a proposition like LivesIn(Alice, Laos). On the representational level in a neural network this requires creating internal representations of the entities in question, and then performing some transformation on those representations that signals to subsequent layers that these two representations are "bound together".

The main hypothesis of the paper is that this transformation can be seen as a function that takes two entity representations x and y as input and outputs their "binding strength" F(x, y), i.e., a score that quantifies whether the two entities are bound or not. Assuming that F is bilinear in the entity representations x and y, the authors propose a method to estimate F via its Hessian matrix H. If the binding subspace is low-dimensional, then F and the Hessian H should be low rank, which motivates the authors to analyze the rank-k truncated SVD of H. By measuring the efficacy of interchange interventions as a function of k, the authors find that a k=50 dimensional subspace mediates binding, i.e., when manipulating activations in this subspace model output changes accordingly. For example, given the input "Alices lives in Laos. Bob lives in Peru." one can make the LM say "Bob lives in Laos" by intervening on activations in this low-dimensional subspace.

Having developed the machinery to probe an LM for internal representations of propositions, the paper demonstrates several use cases for analyzing discrepancies between the model's internal representations and its output, finding cases in which the model appears to internally represent a proposition but generates output that is inconsistent with it.

### Strengths
**Originality:** The paper proposes a novel method for identifying a low-dimensional subspace which appears to causally mediate binding behavior in language models. Compared to the rather indirect evidence seen in prior work (Feng & Steinhardt, 2023), the present submission directly identifies this subspace, which results in a much greater degree of manipulability and interpretability.

**Quality:** The method is well-motivated (§5.2) and -- at least on the data used -- works well empirically (§6.1). The qualitative analysis (Figures 5, 7, 8 and related discussion) nicely illustrates similarity in the low-dimensional dimensional subspace, as well as the limitations of the method.

**Clarity:** The paper is structured well, is clearly written and flows naturally.

**Significance:** Binding is generally believed to be an essential component in the formation of internal/situation/world models. As such, any progress towards understanding if/how language models perform binding on a representational level is an important contribution.

### Weaknesses
**Edit after author response:** The authors thoroughly addressed all issues by conducting experiments that disentangle position, order, and "true" binding. I've raised my scores accordingly: soundness 2 -> 3, overall rating 6 -> 8

---
**Weaknesses before revision below. These issues are now sufficiently addressed in the appendix of the revised manuscript:**

The paper does not do enough to rule out an alternative, simpler hypothesis that could potentially explain the results. Concretely, it appears possible that, due to the highly regular nature of the data, the low-dimensional subspace claimed to encode binding information primarily encodes positional information or order information. The running example "Alices lives in Laos. Bob lives in Peru." has highly regular structure with fixed positional offsets between person and country names, so it is conceivable that the proposed method actually identifies a "position subspace" or "entity/attribute order subspace" and that interchange interventions claimed to modify binding information in fact modify positional or order information. The paper takes two steps into the direction of ruling out this alternative explanation, but I do not believe that they are sufficient:
1. Using a LM to rewrite the template-generated texts into short story-like paraphrases. My concern here is that it is unclear how much of the original regularity remains in the paraphrases and how variations in the paraphrases relate to probe performance in Table 2. Since the probe performance exact match metric on the paraphrase is much lower than on the template-based data, it is possible that the probe works best on the paraphrases that are structurally closer to the templates and drops as the paraphrases become more varied and creative. An additional analysis looking at, say, probe performance as a function of token distance between entities and attributes in the paraphrases could provide evidence for or against position being encoded in the identified low-dimensional subspace.
2. A qualitative comparison in which position and order are varied ("parallel" setting in Figure 5, coreference examples in Figure 7). While encouraging, these are only a few qualitative examples of representational similarities. Here, systematic, quantitative experiments would go a long way towards ruling out alternative explanations. Data for such experiments could be relatively easily generated by varying position and order in the templates, e.g., "Alice lives currently and has always lived Laos. Bob lives in Peru", which varies the token distance between the bound arguments or "Alices lives in Laos. Peru is where Bob lives.", which swaps the order of arguments. If the authors can show that the subspace mediates binding in a similar manner, this would make a much stronger justification for calling it a "binding subspace"

### Questions
My main concern and suggestions on how to alleviate it is given in the weaknesses. If the authors can present evidence that helps rule out the positional/order explanation I'm more than happy to raise my score.

### Soundness
3

### Presentation
3

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
The paper introduces a new probing technique, called propositional probes. Such probes are functions with two arguments both of which are language model representations. When applied to entities in the probe's domain, the output of the function is a symmetric metric which is expected to be high if the corresponding tokens are bound. 
A Hessian-based algorithm is proposed to find a low-rank bilinear propositional probe. The algorithm starts with a way to query the language such that giving the correct answer depends on the ability to identify if entities are bound. In the paper's experiments, the language model is asked to repeat some relational information provided in-context (e.g. which country does entity0/entity1 live in). However, the representations of the two entities are set to their midpoint, such that the Hessian reveals how the representations would have to change in order to accurately represent their binding. After the Hessian is calculated, SVD is applied and only the top k-dimensional subspace is kept. 
To evaluate this algorithm, 'interchange interventions' are performed where the positions in the identified subspace of two (out of three) entity representations are swapped. When the model is queried, it reports the 'wrong' entity with close to perfect accuracy for some values k. The binding strength is also visualized for some example inputs.
Further evaluations demonstrate that the probe match prompting performance in ordinary setting, and outperform it in adversarial settings.

### Strengths
- A new type of probe and corresponding algorithm to construct them are presented, this method is likely to be very useful to the interpretability community. Propositional probes will allow probing LLMs for the ability to represent entities as standing in certain relations to one another. 
- The subspace identified is clearly shown to be causally implicated.
- Probes are shown to outperform prompting in adversarial setups.

### Weaknesses
- Side effects of the interventions are not investigated, it would be great to evaluate how much performance is/isn't lost, as an indication of how precise the interventions are.
- Results are limited to one model.

### Questions
- I noticed that the number of values of k that were evaluated is not super high, why is that? Is Hessian-based algorithm computationally intensive? 
- Separate probes are learned for each domain, but every domain contains only one predicate, do you have any sense of how well propositional probes might generalize across predicates? Is there a good way to quantify how different the probes for each domain are?
- Do you think anything be gleaned from the singular values of H? Do they correlate with the accuracies in Figure 4 at all?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a method to extract latent world states in the form of propositional probes. They form predicate-argument-argument triples for multiple domains. They propose a method based on a Hessian-based algorithm in order to identify the binding subspace. They evaluate the propositional probes in both standard and adversarial settings. For the adversarial setting they find that the propositional probes stay more faithful to the input.

### Strengths
The paper is well-written and comes with multiple contributions. The contributions include the use of propositional probes, the definition of the hessian-based algorithm and the confirmation of two hypotheses - that propositions can be decided from internal activations and that these propositions are faithful to the input context.

### Weaknesses
- I would have liked to see a stronger focus on the adversarial experiments, in the paper. In particular, a deeper analysis on why probes remain faithful and how backdoor attacks and prompt injection could be prevented using your method.
- The synthetic dataset setup seems very simplistic and could have been made more true to real life use, such as by using paragraphs of existing texts and extracting propositions from them.

### Questions
- Why did you go from proposition to text and not the other way around: use existing text (from the wild) and generate propositions from it?

### Soundness
3

### Presentation
3

### Contribution
3
