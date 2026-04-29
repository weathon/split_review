# Mechanistic Interpretability Needs Philosophy

- Decision: Reject
- Scores: 7, 8, 8

## Abstract
Mechanistic interpretability (MI) aims to explain how neural networks work by uncovering their underlying causal mechanisms. As the field grows in influence, it is increasingly important to examine not just models themselves, but the assumptions, concepts and explanatory strategies implicit in MI research. We argue that mechanistic interpretability needs philosophy: not as an afterthought, but as an ongoing partner in clarifying its concepts, refining its methods, and assessing the epistemic and ethical stakes of interpreting AI systems. Taking three open problems from the MI literature as examples, this position paper illustrates the value philosophy can add to MI research, and outlines a path toward deeper interdisciplinary dialogue.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper argues that progress in mechanistic interpretability is limited by conceptual ambiguities about what counts as an explanation, a feature, or even a deceptive circuit. It claims that this means philosophy can be helpful within the field, helping clarify some of these core concepts.

It breaks down mechanistic interpretability into three open problems of decomposition, feature identification, and detecting deception. In all three of these, it points out ways in which philosophy can help e.g. pointing out where one might be too narrow-minded on what constitutes a feature, the level of granularity at which we want to decompose a neural network, and what it means for a model to be deceptive.

The paper also pre-empts objections regarding whether philosophy and philosophers might be ill-equipped at contributing to mechanistic interpretability due to the technical barrier, noting both the ability for those studying the philosophy of science to study the science as well, and also the importance of some of the existing philosophical concepts and verbiage in helping talk about issues within mechanistic interpretability.

### Strengths
The core claim is compelling a clear: it outlines three concrete open problems within mechanistic interpretability and cleanly explains why the questions we ask and answers we seek in those problems are not answerable without considering philosophy. The paper supports this view by giving specific evidence and examples of ambiguities that are not resolved by technical means, but instead by thinking about the philosophical goals of the interpretability exercise. Since mechanistic interpretability is a growing field and a relatively pre-paradigmatic one, having a broader framework for how to build a scientific discipline around it is clearly important and relevant to NeurIPS.

### Weaknesses
One way in which the paper could be improved is by increasing the concreteness of the examples. While the thought experiments are compelling, it would be useful to highlight a specific case where doing philosophy has led to useful insights in mechanistic interpretability.

Another is to take more seriously critiques around whether or not the contribution of philosophy to mechanistic interpretability is necessary for making scientific progress, as opposed to merely ancillary and useful for broader understanding. The responses to the potential critiques could be expanded.

Finally, it would be useful to map some specific parts of philosophical discussion to mechanistic interpretability, since a common refrain with these cross disciplinary studies is the inability to accurately communicate across fields.

### Questions
1. What are some specific examples where philosophical inquiry has helped resolve conceptual confusion in mechanistic interpretability?
2. How should philosophers who are not technically versed think about contributing to mechanistic interpretability, and conversely, how should mechanistic interpretability researchers best frame their findings so philosophers of all stripes can contribute?
3. To focus in on decomposition, what is a set of philosophical heuristics which mechanistic interpretability researchers should use in order to most usefully identify the right level of decomposition?

### Presentation
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
The paper argues that mechanistic interpretability can benefit greatly from cross-disciplinary contribution from philosophy. To support this claim, the authors present discussions of 3 research areas in mechanistic interpretability as examples of where MI has gained and could further gain from philosophical analysis.

### Strengths
The position is well argued and well grounded in the MI and philosophical literature.
If the authors' proposal were taken onboard systematically in MI practice, it would have positive transformative effects.
It effectively addresses common objections that are very likely in the minds of the MI and ML communities.

### Weaknesses
Granting that philosophy can be very helpful to MI, the first case study does not seem to offer the best illustration because it seems to map what is already present in MI to the corresponding literature and concepts in philosophy. This in itself is valuable, but not quite what the authors set out to demonstrate. Perhaps there are aspects of this case study that can be brought out where the contribution of philosophy has not yet been taken onboard by other means. This would make a stronger statement that interdisciplinary integration is needed a priori and not as an afterthought.

The second case study suffers, at times, from the same (minor) shortcoming.

The paragraph "Refining experimental approaches" is quite terse. It points to work and mentions the kinds of contributions that philosophy can make but does not explain any of them.

The paper is largely silent on how the cross-disciplinary interaction could/should happen in practice (with some brief exceptions in the Objections section). 

As the authors point out, the call for engagement with philosophy is not novel or uncommon in areas directly adjacent to MI, such as Cognitive Science. Its value and impact will probably be confined to the MI field (no more, no less).

### Questions
* The paragraph on Mechanistic Interpretability makes a distinction between generating explanations for non-specialist audiences and developing explanations for theorists. It likens the latter to using the scientific method but remains silent as to how we should think of the former. How should we think about generating explanations for non-specialist audiences?
* Can case study 1 be made stronger along the lines outlined in Weakness 1?
* How do the authors envision the interdisciplinary integration could/should work in practice? Is the idea to have a philosopher on every team? Or for practitioners to keep up with the philosophical literature the way they do with the technical literature adjacent to MI.
* MI interpretability tackles many problems that have a much longer history in Cognitive Science (e.g., Adolfi et al, 2024; Comp Brain Behav). Can philosophy help identify these underlying problems early such that time and effort is not wasted in rediscovering them and their possible solutions?
* Can anything be said about how cross-disciplinary integration should happen in practice?
* Please update references to current (published) versions (e.g., Adolfi et al., 2025, ICLR; Saphra, Wiegreffe, 2024, ACL, Vilas et al., 2024, ICML)

### Presentation
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
This paper argues that in general, interpretability would be improved as a field by working with philosophers to develop more precision in the claims made and resulting more serious thought on the questions being asked. As examples, they refer to the term mechanistic itself, the level of analysis being conducted, the meaning of the word feature, differences between belief and intent, and work on deception and lying in models that do not necessarily have beliefs.

### Strengths
I found this paper generally convincing and felt that many people in mechanistic interpretability could benefit from thinking more about the definitions of anthropomorphic terms that they are casually using.  I think it’s appropriate for the position track, and would not be improved by adding experiments to move it to the main track. 

I like the suggestion in 103 that there should be more work on mapping unexpected behaviors in edge cases and identifying signatures of specific algorithms.

Some of the sections have really good explanations and examples that illuminate the particular concept being discussed. For example, I like those given in 214-218.

I think that the discussion of the differences between deception and lying and the behavior is documented in interpretability claiming to be out about deception and lying. Another discussion I particularly liked was about the vagueness with which we use the term feature.

I really like the mention in 273 about why a clear belief based definition of deception is specifically important for MI research in particular, because the entire premise of using MI to detect deception assumes that there are internal states which are relevant and not just external behaviors.

### Weaknesses
# Central thesis
I want a more specific thesis than “interpretability needs philosophy”. I didn’t see early signals as to what positions would be argued. Something like, “Mechanistic interpretability needs to be precise and interpretable. Philosophy can show how.”

# Details
Refs are glossed over, but should be explained:
- 147 explan. pluralism
- 210 Harding
- 267 statements
- 292 Azaria & Mitchell
- 298 Marks & Tegmark
- 303 Herrman & Levinstein
- 362 Bickle

# Other

84 Existing MI rarely uses causal methods, so I'm not sure it's appropriate to demand mechanisms. Paper cites other work on defining mechanistic which also disagree with this definition eg Mueller et al. (2024) and Saphra & Wiegreffe (2024)

257 Says roleplay gives untrue statements, not lies. However, they never again address roleplaying, including the defn 263-264. Yet much deception research—especially Anthropic's—has the model roleplay. When models are often understood as roleplaying, this omission is crucial.

349 "Armchair philosophy = nonstarter” Why concede? Methods change. Philosophy can predict future issues.

377: Emphasize the limitations of the small number of philosophers whom the community is familiar with.

Tense is inconsistent past/present.

### Questions
73: Why are functional roles not mechanistic?

226: What are the consequences or examples of relevant cases in interpretability for the conflation between belief and intent?

### Presentation
3
