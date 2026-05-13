# Counterfactual Realizability

- Decision: Accept
- Scores: 8, 6, 10, 6

## Abstract
It is commonly believed that, in a real-world environment, samples can only be drawn from observational and interventional distributions, corresponding to Layers 1 and 2 of the Pearl Causal Hierarchy. Layer 3, representing counterfactual distributions, is believed to be inaccessible by definition. However, Bareinboim, Forney, and Pearl (2015) introduced a procedure that allows an agent to sample directly from a counterfactual distribution, leaving open the question of what other counterfactual quantities can be estimated directly via physical experimentation. We resolve this by introducing a formal definition of *realizability*, the ability to draw samples from a distribution, and then developing a complete algorithm to determine whether an arbitrary counterfactual distribution is realizable given fundamental physical constraints, such as the inability to go back in time and subject the same unit to a different experimental condition. We illustrate the implications of this new framework for counterfactual data collection using motivating examples from causal fairness and causal reinforcement learning. While the baseline approach in these motivating settings typically follows an interventional or observational strategy, we show that a counterfactual strategy provably dominates both.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper considers a simple procedure that makes it possible to sample certain counterfactual distributions (counterfactual realizability). The key observation is that the perception of a variable to its children can be intervened upon in some cases. This procedure is called counterfactual randomization. It also proposes an algorithm that takes in a candidate counterfactual distirbution and a graph, and outputs a sample from the counterfactual query if and only if it is possible to sample from the input candidate. Finally, a graphical characterization for counterfactual realizability is given.

### Strengths
As the paper points out, the counterfactual randomziation procedure in itself has been alluded to in previous work. But, the main contribution of this paper is a characterization of when a counterfactual distribution can be 'realized'. I liked that the paper operates under this structure for sampling distributions at different levels of the causal hierarchy by the notion of actions. Since counterfactuals are commonplace in many applications and a major hurdle is their non-identifiabilty, this work is certainly significant. The paper is well written and padded with many examples to illustrate the applicability and importance of the procedure.

### Weaknesses
As the paper also mentions, I believe the idea for intervening on perceptions was known before and makes multiple informal appearances. A few other references are (S. Geneletti, A.P. David, Defining and identifying the effect of treatment on the treated, 2010). Also, the notion of SWIGs (Richardson and Robins, 2013) is quite similar. I believe a more thorough comparison with previous work is needed to make the paper more complete.

One interpretation of the counterfactual randomization procedure is that the counterfactual distribution is just an interventional distribution where the intervention is performed on the perception. Given that a few counterfactual distributions are realizable as defined, how does this affect the notion of 'causal hierarchy'?  Some discussion on this would certainly strengthen the paper. 

The main body and the proofs often use the notion of a probability measure of belief of an exogenous agent. I thought that this was ill-defined. Perhaps the authors could make Remark C.7 an axiom that defines this measure?

### Questions
1) One interpretation of the counterfactual randomization procedure is that the counterfactual distribution is just an interventional distribution where the intervention is performed on the perception. Given that a few counterfactual distributions are realizable as defined, how does this affect the notion of 'causal hierarchy'?  Some discussion on this would certainly strengthen the paper. 
2) The main body and the proofs often use the notion of a probability measure of belief of an exogenous agent. I thought that this was ill-defined. Perhaps the authors could make Remark C.7 an axiom that defines this measure?

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
2

### Summary
The authors tackle the complex space of sampling from counterfactuals. 

Specifically, they propose a "formal definition of realizability, the ability to draw samples from a distribution, and then developing a complete algorithm to determine whether an arbitrary counterfactual distribution is realizable given fundamental physical constraints, such as the inability to go back in time and subject the same unit to a different experimental condition"

Both causal fairness and CRL are used as illustrative examples, suggesting that a counterfactual strategy dominates strategies based only on interventional and observational data.

### Strengths
The paper tackles a relevant problem, and covers all key bases to provide its key contribution. 

Sampling from counterfactual distributions is naturally hard, and developing methods and tools to do so is important, as suggested in the paper.

### Weaknesses
I am not an expert in this field, so take it with a grain of salt:

As written by the authors "representing counterfactual distri- butions, is believed to be inaccessible almost by definition."

References are provided for e.g. the 'counterfactual randomisation procedure', i.e. attempts at sampling from CFs, but there is not much discussion about why it is 'believed' why CFs are inaccessible by definition.

"inaccessible almost by definition" is not precise enough to be useful for a reader, "almost" needs to be refined and explicated, ideally both via intuition and formally, even just briefly.

In the conclusion, this rigour is missing, too, when the authors state: "Countering prevalent belief". A reader needs references to be able to follow the thoughts and verify by themselves, that indeed, the venture of CFs sampling is hard (or impossible?)

If CFs are not in fact ""inaccessible almost by definition"", then this paper of course would constitute a huge contribution to the field of causal inference in which case this should be highlighted more.

- [ ] Bounding in mentioned but not referenced? The word "bounding" appears twice in the text, but at first mention is not referenced. Bounding is not a well known method, and without further definition will not be useful to the reader unless at least minimal referenced (and not just in the discussions section)
- [ ] 535 Countering prevalent belief
    - [ ] References pls, readers need to be able to verify claims independently
- [ ] 168 fig 2a does not exist, do you mean top?
- [ ] Assumption 3.1: I worry that this statement is too vague for a reader to agree with. Can you provide more justification for why this is reasonable to hold in practice? If not, provide justification for why a practitioner should entertain this method to provide additional analysis instead.
- Can you define "causal machine learning"? I am aware that this is an emerging term, but in the context of this paper it is unclear to me what part of it the authors are trying to address exactly.

Typos:
- [ ] 507 typo "cotribution"
- [ ] 175 mechanism OF




- [ ] 258 what is an intuition pump?
- [ ] 431 appreciate limitations
    - [ ] What about limitations in general though?
- [ ] 507 typo
- [ ] 507: what bounding do you mean here? References?

### Questions
- [ ] Bounding in mentioned but not referenced? The word "bounding" appears twice in the text, but at first mention is not referenced. Bounding is not a well known method, and without further definition will not be useful to the reader unless at least minimal referenced (and not just in the discussions section)
- [ ] 535 Countering prevalent belief
    - [ ] References pls, readers need to be able to verify claims independently
- [ ] 168 fig 2a does not exist, do you mean top?
- [ ] Assumption 3.1: I worry that this statement is too vague for a reader to agree with. Can you provide more justification for why this is reasonable to hold in practice? If not, provide justification for why a practitioner should entertain this method to provide additional analysis instead. 
- Can you define "causal machine learning"? I am aware that this is an emerging term, but in the context of this paper it is unclear to me what part of it the authors are trying to address exactly. 

Typos: 
- [ ] 507 typo "cotribution"
- [ ] 175 mechanism OF





- [ ] 258 what is an intuition pump?
- [ ] 431 appreciate limitations
    - [ ] What about limitations in general though?
- [ ] 507 typo
- [ ] 507: what bounding do you mean here? References?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors provide necessary and sufficient conditions for a ground truth counterfactual quantity of an SCM to be sampled directly (''realized'') through a ''counterfactual experiment''. Such an experiment involves manipulating the original SCM through adding mediators through some direct causal effects---a process the authors motivate with intuitive real-world examples.

### Strengths
The authors' contributions are original and significant. Their insights are laid out clearly and limitations and discussion of future work are provided. 

The authors show the advantages of counterfactual experiments with intuitive examples. The authors show that counterfactual fairness measures that are not identified through interventions can be realized (and thus identified) through counterfactual experiments. Furthermore, the authors show that bandit policies which allow for counterfactual mediators dominate policies from the classical causal bandits setting.

### Weaknesses
I do have few substantial weaknesses to discuss. In the Questions section I voice a slight disagreement about the interpretation of ''physically possible'' experiments. Below are some minor comments.

(Lines 105--107) Presumably W_* is a tuple of potential outcomes and w is a vector over the support of W_*. These should be defined formally to avoid confusion. I suspect there is a typo on line 107 when defining P^M---perhaps taking the product over t = 1 to |W_*| would clear this up. The current notation makes it unclear how the probability of a specific vector of potential outcomes is calculated, especially given that W_* is described as a *tuple* of potential outcomes, which suggests an ordered collection, while the product notation implies a set.

(Lines 120--121) Read (V)^(i) does not ''measure'' the effect of f_V on V, these mechanisms are in general not identified. This should be reworded---perhaps the physical actions should be defined formally. The term 'measure' is misleading, as it implies a direct quantification of the causal effect of f_V, which is not generally possible without further assumptions. It would be more accurate to describe READ as the action of observing or recording the value of V, rather than measuring the effect of the mechanism.

(Figure 2) Given the discussion in Example 1, it may be more natural to include latent confounding between X and Z in the DAGs. The absence of this confounding may limit the applicability of the proposed framework in settings where such confounding is present.

### Questions
I would argue there do exist physically viable experiments that break the authors’ proposed fundamental constraint on experimentation. For instance, in the authors’ example of an artificial agent’s decision to issue a speeding ticket from video footage based off the color of a car, both the doctored footage of a yellow car and the original footage of a red car could be fed to multiple copies of the same artificial agent. Perhaps the assumption is more properly termed a ''constraint on experimentation without cloning’’?

### Soundness
3

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
4

### Summary
Inspired by (Bareinboim et al., 2015), the authors introduced a new action of "counterfactual randomization (ctf-randomization)" in structural causal models. One of the examples of how such action can be applied is given in Definition 2 (Counterfactual mediator). In particular, for some variable $X$ and its children $Y$, $W$ is the counterfactual mediator of $X$ if the mechanism generating $Y$ can retrieve the value of $X$ from $W$. The authors studied under what conditions on the causal structure and set of available actions (which might include counterfactual randomization), it is feasible to generate i.i.d samples from a counterfactual distribution. This study assumes that each unit undergoes each causal mechanism only once (Assumption 3.1). The authors provide graphical conditions along with an algorithm (CTF-REALIZE) to check the feasibility of sampling (which they call this problem "realizability"). Moreover, they characterized graphical conditions for the case that it is possible to perform ctf-randomization for each child of
each variable, and as a corollary, they obtained the case of "fundamental problem of causal inference". They explored the applications of counterfactual realizability in causal fair analysis and causal bandits. In particular, they showed in an example that the interventional fairness metric fails to preserve disparities
in outcomes across groups while a counterfactual one approach works in it. Moreover, in a specific causal bandit setup, for a specific "MAB template", they showed that the proposed $\mathcal{L}_3$-based strategy is optimal.

### Strengths
Originality/Quality:
The definition of ctf-randomization and the algorithm for checking the counterfactual realizability are new in the field of causality. Moreover, the authors discussed the applications of $\mathcal{L}_3$-based methods in fairness analysis and bandit problems which might be interesting for people in other fields.

Clarity: The writing should be improved as some of the parts need more explanations.

Significance: Although the concept of counterfactual realizability is new in the field, it is not completely clear to what extent such ctf-randomization can be implemented in reality.

### Weaknesses
The content of the paper is fairly dense and the authors did not have enough space to give a sketch of the proofs or even CTF-REALIZE algorithm is not described very well in the paper (For instance, it is not clear why there is a rejection sampling in line 18 of Algorithm 1). This also applies to the results in Section 4. Although the authors showed in some specific scenarios, $\mathcal{L}_3$-based methods perform better than $\mathcal{L}_2$-based methods, there is no intuition given in the paper why this is the case. One might wonder if the causal graphs or the causal mechanism are meticulously engineered to show the advantage of counterfactual reasoning. The core contribution of the paper lies in the soundness and completeness of CTF-REALIZE, as presented in Theorem 3.5. However, the submitted version lacks an adequate explanation of the COMPATIBLE procedure, which is used as a subroutine in CTF-REALIZE. The only reference to it is the pseudocode in Appendix B.1, having undefined terms like "label" and "Natural" in the submitted version. Without knowing how CTF-REALIZE works, it is impossible to verify the results in Theorem 3.5.  Specifically, in COMPATIBLE, step ii.b, what exactly is meant by "minimal intervention"? Why is it required, and how is it determined?

### Questions
1. For what real applications, is it possible to implement ctf-randomization? To my understanding, this might be only possible for some output $Y$, where it is generated by a computer program. Therefore, it is possible to generate the output several times with different inputs with the same randomization.

2. In the definition of counterfactual mediator, it is assumed that the value of $X$ can be retrieved from $W$ in the causal mechanism that generates $Y$. Does it mean that there is no exogenous noise in $W$ and it is generated deterministicly from $X$?

3. It is good to provide some intuitions on the advantage of using $\mathcal{L}_3$-based methods that are discussed in Section 4. 

4. Please provide a clear description of  Algorithm 1 and COMPATIBLE subroutine either in the main body or the appendix. This should start with a general idea of the algorithm or subroutine and then describe the algorithm in detail. In the current version, it is hard to verify the main results for Algorithm 1.

### Soundness
3

### Presentation
2

### Contribution
3
