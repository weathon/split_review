# Systems with Switching Causal Relations: A Meta-Causal Perspective

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Most work on causality in machine learning assumes that causal relationships are driven by a constant underlying process. However, the flexibility of agents' actions or tipping points in the environmental process can change the qualitative dynamics of the system. As a result, new causal relationships may emerge, while existing ones change or disappear, resulting in an altered causal graph. To analyze these qualitative changes on the causal graph, we propose the concept of \textit{meta-causal states}, which groups classical causal models into clusters based on equivalent qualitative behavior and consolidates specific mechanism parameterizations. We demonstrate how meta-causal states can be inferred from observed agent behavior, and discuss potential methods for disentangling these states from unlabeled data. Finally, we direct our analysis towards the application of a dynamical system, showing that meta-causal states can also emerge from inherent system dynamics, and thus constitute more than a context-dependent framework in which mechanisms emerge only as a result of external factors.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces the concept of *meta-causal states*, which attempt to represent how the underlying dynamics of a causal model can change based on context. The authors then examine how meta-causal states could be used in the attribution of responsibility, describe how the number of distinct meta-causal states can be identified empirically (a variety of EM), and provide an example analysis of stress-induced fatigue.

### Strengths
The concept is interesting and the paper is well-written and detailed.

Section 4 presents some diverse and interesting applications of the basic theory.

The graphics, particularly Figure 1, are clear and easy to understand.

### Weaknesses
The paper should cite some relevant prior work in graphical models with “gates” (Minka 2008; Winn 2012). The concepts in those papers are somewhat different, but closely related to the topic of this paper.

The paper should note that some meta-causal states can actually be represented by ordinary SCMs. For example, in an SCM in which Z is caused by both X and Y, it is entirely possible for Y to control *the manner in which* X affects Z. In the simplest case, Y could be a binary variable that determines the functional form of how X affects Z. This complicates the structural equation of Z, but it’s not outside of the standard definition of SCMs. Of course, this approach has limitations. For example, it cannot be used to reverse the direction of causation between two other variables (at least not within the standard definition of SCMs). However, it can toggle the existence of an edge or change the manner in which one or more parent variables affects their child. This should be noted more clearly in the discussion.

The utility of meta-causal states is not immediately evident. That is, what sorts of practical causal inference in medicine, economics, social science, or other domains would be improved by consideration of meta-causal states? What errors are made now using conventional causal modeling that would be avoided by the use of meta-causal states? I suspect that there are good answers to these questions, but it would improve the paper if they were more clearly explained.

**References**

Minka, T., & Winn, J. (2008). Gates. *Advances in Neural Information Processing Systems*, *21*.

Winn, John. "Causality with gates." In *Artificial Intelligence and Statistics*, pp. 1314-1322. PMLR, 2012.

### Questions
What sorts of practical causal inference in medicine, economics, social science, or other domains would be improved by consideration of meta-causal states? 

What errors are made now using conventional causal modeling that would be avoided by the use of meta-causal states?

### Soundness
4

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
This paper defines meta-causal systems to allow us to ask what caused a structural equation to be the way it is. This allows us to attribute responsibility for some variable sometimes to another variable, and sometimes to an external force that intervened on the system, as appropriate. An algorithm using RANSAC and EM is proposed to learn such meta-causal systems from data.

### Strengths
The idea of looking for the causes behind an SCM is very interesting and could be relevant in certain contexts. Putting these ideas in practice required the development of a nontrivial algorithm; while generalizing it is left for future work, this does help to solidify the contribution.

### Weaknesses
- The core concept of the paper seems to be multiply defined. I understand "meta-causal" to refer to questions of what *caused* the structural equations to be what they are (as in line 044-045). But in other places in the paper, it seems to refer to an abstraction where we don't look at the precise structural equations but instead at some qualitative characteristics. E.g. in the dynamical system of stress-induced fatigue in section 4.3, the structural equations remain the same but it is emphasized that there are are different causal states (e.g. self-reinforcing or self-suppressing). It is presented as a major premise of the paper (final sentence of abstract) that meta-causal states do not always result from external influences. But according to the first definition, there is only one meta-causal state, because the structural equations don't change, so this is not an example of meta-causality. (As a consequence of this ambiguity of "meta-causality" in the paper, I find it hard to assess to what extent the emprical results support the claims of the paper.)
- I found the start of section 3 to be rather hard to follow, due to its density and it being unclear what intuition is being formalized. There is no overall description of how SCM and mediation process make up a more complex new process. The transition function seems to imply a dynamical view, with discrete time steps. But it is not made explicit anywhere that variables should be thought of as having a time index (should they?). In definition 1, the presence of the transition function does suggest that transitions between time steps are always happening.

### Questions
- In section 3, I assumed from the matching notation that the variables $\mathbf{X}$ are part of an SCM. Are they?
- In definition 1, line 141, in what way does an element of  $\mathcal{X}_j^{S}$ represent a "change" of $\mathcal{X}_j$?
- An odd point I wanted to note: if an SCM has arrows $X \to Y$ and $Y \to Z$, the meta-causal state would also have an arrow for the indirect effect $X \to Z$. So these arrows aren't structural, merely descriptive. It depend on the answer to my question about $\mathbf{X}$ above whether this is a drawback or merely remarkable.
- Line 171 "As standard causal relations emerge from the underlying mediation process": How do they emerge? Is this always true?

### Soundness
2

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
2

### Summary
The manuscript introduces a framework to analyze dynamic causal relationships that shift based on environmental or internal changes, called meta-causal models (MCM). The framework extends traditional causal models by defining “meta-causal states,” which group standard causal graphs into clusters of qualitative behavior. Then, MCM can dictate the detection of underlying changes in causal structures.

### Strengths
* The manuscript provides a formal framework for handling the dynamics of an SCM. Definitions 1 to 3 are elegant implementations of these ideas. In particular, framing meta-causal models as finite state machines is intuitive and well-suited for applications.
* The framework allows for a systematic attributing responsibility in dynamic scenarios. In Section 4.1, the manuscript shows how counterfactual scenarios can be better explained in a meta-causal model. Furthermore, the paper provides a clear example of when attributing effects via model parameters might fail to explain preventative mechanisms.

### Weaknesses
* Meta-causality scope: the paper isn’t clear on two philosophical aspects of the framework regarding its scope and interpretation, namely (i) the causal-effect relationship between the meta-causal model and the causal model instance it is working with and (ii) the potential sutil difference between meta causal edges and classical ones
	- (i) From the initial example in Figure 1, the reader could question if the meta-causal model is causing the underlying classical causal model. This discussion isn’t handled in the manuscript, but there is an acknowledgment note in Section 3 under “Causal and Anti-Causal Meta-Causal States.”
	- (ii) How do we interpret and handle the subtle difference between meta-causal and classical relationships? For instance, in Fig 1, a classical causal discovery algorithm could attribute Api and Bx as causes of Ax.

### Questions
* Are there other examples or mechanisms where classical models will fail to capture via observed changes in variable values and meta-causal models won’t? How often or realistic are the preventive mechanisms, like the ones described in Section 4.1?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper introduces the concept of meta-causal models to formalize the emergence of causal relationships, which, for instance, allows one to formalize changes in the causal structure over time. While more classical approaches based on graphical causal models assume fixed causal relationships, the proposed meta-causal models can represent and reason about situations where causal mechanisms emerge, change, or disappear. The authors formalize meta-causal states that group similar causal behaviors and demonstrate how to infer these states from data in some toy scenarios.

### Strengths
+ Novel theoretical contribution towards a more generalized way to formalize causality
+ Mostly clear motivation, although the introduction could be improved
+ Although limited, the authors aimed to not only provide a theoretical discussion, but also insights towards a practical application
+ Fair discussion of the limitation of the work

### Weaknesses
- While certain aspects of the theory are well introduced, theoretical (proven) statements and formalization of axioms are somewhat lacking, considering that the goal of the work is to establish a new formalism
- The experimental evaluation is somewhat limited, but this is a minor point as the theoretical contribution is the main focus
- The introduction is too complex and abstract
- The practical applicability to larger, more complex systems remains unclear

### Questions
Overall, the paper provides a great first step towards an alternative formalism to describe and formalize the emergence of causal relationships. Since such types of works typically are more focused on the theoretical work and introduction of new formalisms, the concerns about the practical and experimental aspects are rather minor.

Generally, I would have expected a few more discussions related to the distinction between meta-causal states and traditional latent variable approaches. Although I am not that familiar with related work in this domain, I would have expected some more discussions with work introducing alternative ways to formalize causality, such as:
- "A Measure-Theoretic Axiomatisation of Causality" by Park et al.
- "Phenomenological Causality" by Janzing et al.

These works go in a different direction but seem, on a high level, related.

The introduction is very hard to follow and could be motivated better. While the example in Figure 1 is definitely helpful to understand the idea and limitations, the introduction often sounds too abstract. Maybe starting with the Figure 1 (a) example on a high-level description without further introduction of any formalisms around causal modeling could be helpful for the motivation.

While the practical application in a general setting seems to be limited in the current form, the authors fairly discuss the current limitations and the work still provides a valuable foundation for follow-up work.

When the authors can comment on the lack of theoretical statements (e.g., theorems ensuring that, under certain conditions, one can transform a MCM to a classical SCM), I am willing to further increase the score.

### Soundness
3

### Presentation
3

### Contribution
4
