## Human Reviewer 1

### Summary
The authors study the tradeoff between generalization and identification through a notion of finite semantic resolution. They support their theory through a variety of convincing empirics in both a toy neural network and real-world models.

### Strengths
The paper is very well written overall. The exposition is clear, precise, and convincing. The theory is impressively predictive of both synthetic and real-world empirics. The central role of semantic resolution and its influence on the generalization/identification makes for a very compelling story. Well done overall!

### Weaknesses
See Questions below.

### Questions
For your empirics with the toy neural network model, do you have an idea why the model seems to learn a linearly decaying distance function? Since it sounds like the similarity task employed a conventional softmax output / cross-entropy loss, it seems like the natural distance function would be exponentially decaying?

You mention that increasing the decay rate in exponential distance will increase both generalization and identification. In your experiments with Transformers (which presumably employ an exponential distance hard-coded in softmax attention), did you find that increasing the decay rate boosts generalization and identification accordingly? Based on your prescriptions, to optimally employ these models, should we always increase decay rate at test time for maximal performance?

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
10

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper proposes that neural systems with finite semantic resolution face a fundamental tradeoff between generalization (correctly judging similarity between different inputs) and identification (distinguishing exact inputs). The authors derive closed-form Pareto curves characterizing this tradeoff for systems that compare inputs via a decaying similarity function, showing that performance lies on a universal frontier independent of input space geometry. They extend the theory to cases with noise and multiple items, predicting a sharp $1/n$ capacity collapse in multi-input settings. They also provide extensive empirical evidence that semantic resolution acts as a general information constraint in complex systems

### Strengths
1. The central tradeoff (Thm 1) is formally derived under clear assumptions about similarity decay and finite resolution. The analytical Pareto frontier is a nice contribution: mathematically precise, easy to reason about, and interpretable in terms of task accuracy. 

2. The empirical sections demonstrate that real-world models qualitatively follow the predicted tradeoff curves

3. this work links the G-I tradeoff to well-known cognitive constraints like binding failures, generalization gradients, and working memory, providing a cohesive narrative.

### Weaknesses
1. The core tradeoff is derived assuming specific forms of similarity decay and decision rules. Would the authors elaborate how universal or sensitive their conclusion is to the choice of decay function? In Discussion, the authors refer to “finite-resolution similarity” as a universal constraint, suggesting that the existence of the tradeoff is robust, even if the exact shape of the curve depends on the similarity decay. It is unclear whether in those larger models, the similarity function follows the linear decay or takes a different shape.

### Questions
Is there an optimal distance function? the paper motivates its choice of decaying similarity functions using Shepard’s law, stating that generalization should decay with distance. Prior work (e.g., Sims, 2018) has shown that such generalization gradients follow from efficient coding via rate-distortion theory. Would you clarify whether the similarity function is intended to model a learned or designed encoding independently of such optimization?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper investigates the tradeoff between representational fidelity and distinctness under "finite semantic resolution". It shows that if a model’s similarity function has finite “semantic resolution” ε, then its accuracy on generalization tasks (p_S) and on identification tasks (p_I) must lie on a universal Pareto front.

If a model's embedding/similarity has a finite-resolution "floor", we should expect identification to drop as one pushes for broader generalization, and vice versa. Handling n simultaneous items suffers a sharp ∼1/n collapse in identification capacity; i.e., multi-object reasoning should not scale linearly just by adding parameters.
One can choose ε (via architecture, temperature, or thresholding) to target the sweet spot where p_S is maximized (roughly when the “similarity ball” covers half the space).

In short, the paper provides a simple geometry+noise model one can use to set thresholds, pick temperatures, and anticipate how adding more items or pushing for “similarity-aware” training will impact identification.

### Strengths
Comprehensive background section with helpful literature review.

The authors take the time to carefully explain their setup, accompanying notation with helpful illustrative examples.

Authors tested both toy (allowing for theoretical analysis) and realistic models (allowing for confirmation at scale).

Text is well-written, figures are clear, elegant, and helpful.

Code is provided showing how to reproduce the results and figures used the paper.

### Weaknesses
1. As mentioned by the authors in Limitations subsection, compositional representations and hierarchy were outside the scope of the study. Adding a small pilot on a compositional task to show if/why the current theory breaks would strengthen the paper.


__Minor points__:

2. The concept of “semantic resolution” feels somewhat over-introduced. Mathematically, it appears equivalent to a kernel scale or bandwidth that simply controls how similarity decays with distance. While the term is evocative and may carry intuitive meaning across domains, its use risks adding unnecessary jargon. I suggest that the authors clarify whether “semantic resolution” represents a genuinely new construct (i.e., beyond a kernel bandwidth) or simply reinterprets that familiar notion in "semantic" terms. A short comparison or restatement using standard terminology would make the paper easier to follow for readers from machine learning backgrounds.

3. Although there is nothing technically wrong with the abstract, it is very dense and hard to unpack on a first read. The authors could make it a bit lighter in order to appeal to a broader, non-expert audience. For example, by simplifying a few long sentences and highlighting the main contribution more explicitly rather than embedding it deep within the paragraph.

Typos:
- Please fix the m-dashes in line 84.
- and [an] additional one (line 97).
- maximal unncertain[ty] (line 158).
- m-dash in line 189.
- m-dash in line 457.
- m-dashes in lines 464--465.
- please fix hyphen in line 481.

### Questions
How is "semantic resolution" estimated in practice, and does its value depend on how the embeddings are scaled or normalized? That’s important because, otherwise, "semantic resolution" might just be a unit-dependent artefact rather than a stable, interpretable quantity.

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 4

### Summary
The authors derive a theory for how a representation (for constrained resolutions) trades off between generalization and identification, a long known phenomenon from the cognitive science literature. In particular, this theory implies a Pareto frontier between generalization and identification performance. They empirically demonstrate that ReLU networks navigate such a Pareto frontier and find similar performance in a CNN finetuned on a mixture of an identification and generalization task. Finally, they show that LLMs and VLMs both show evidence of a finite resolution, a key assumption of their theory.

### Strengths
This manuscript provides a well articulated contribution to the field, formalizing a tradeoff that had previously been empirically observed. The theory is well-presented and I think the ReLU experiments in particular provide helpful support for the existence of the noted tradeoff. I appreciated the detailed contextualization of this present work in the field. Finally, the paper is generally well-written and the figures are well-designed. Below are some additional parts of the paper I particularly liked:

- The equations (3) and (4) are simply and immediately make the tradeoff intuitive.
- I think it's very interesting that the ReLU networks show some emergent evidence of this tradeoff even though they are only trained on the similarity task, not the identification task.
- Figure 4 demonstrates a good match between their (modified) theory and empirical observations
- Their Proposition 1 demonstrates that this theory can extend beyond the (somewhat minimal) binary similarity measure case.
- The detailed explanation of the different regimes and Fig. 2 are very helpful.

### Weaknesses
As noted above, I liked this paper. My primary concern is that the experiments in section 5 provide rather limited evidence of this tradeoff. Your suggestion (and the suggestion of the prior literature) that this is a universal tradeoff would suggest that it should be apparent even in models that weren't trained explicitly on the identification and similarity task you're measuring. The fact that models become better at identification/similarity as you're varying the parameter prioritizing one or the other loss function is maybe not particularly surprising (though I agree that it demonstrates that there is a tradeoff between those two functions). Moreover, the LLM and VLM experiments don't demonstrate a tradeoff but rather just show that resolution is limited overall. I thought the ReLU experiment was more compelling in this direction, as it trained the ReLU networks only on the similarity task and still demonstrated this emergent tradeoff over different epochs. Unless I'm missing something, I think acknowledging this limitation would be important.

### Questions
- Would you expect an emergent tradeoff between identification and similarity performance if you only trained the CNN on either the identification or similarity task over different epochs (akin to the ReLU network case)?
- Similarly, would you expect such a tradeoff e.g. in different pretrained models?
- Could you discuss how your insights would apply to e.g. the tasks examined in Campbell et al. (2024)?

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4