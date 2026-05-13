# Can a Bayesian oracle prevent harm from an agent?

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Is there a way to design powerful AI systems based on machine learning methods that would satisfy probabilistic safety guarantees? With the long-term goal of obtaining a probabilistic guarantee that would apply in every context, we consider estimating a context-dependent bound on the probability of violating a given safety specification.  Such a risk evaluation would need to be performed at run-time to provide a guardrail against dangerous actions of an AI. Noting that different plausible hypotheses about the world could produce very different outcomes, and because we do not know which one is right, we derive bounds on the safety violation probability predicted  under the true but unknown hypothesis. Such bounds could be used to reject potentially dangerous actions. Our main results involve searching for cautious but plausible hypotheses, obtained by a maximization that involves Bayesian posteriors over hypotheses. We consider two forms of this result, in the \iid case and in the non-\iid case, and conclude with open problems towards turning such theoretical results into practical AI guardrails.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the problem of designing AI systems that satisfy probabilistic safety guarantees. Within a Bayesian framework and given the safety specifications (as a probability), the authors provide risk bounds for potentially harmful decisions, showing that the probability of harm can be upper-bounded by a probability that can be estimated by approximating Bayseian posterior over theories given the observed data. They study two settings: i.i.d case and non i.i.d case and provide a simple experiment to evaluate the performance of safety guardrails.

### Strengths
This is a very well written paper, and it is easy to follow. 

The proposed approach represents a promising initial step toward designing AI systems that ensure safety through built-in probabilistic guarantees, rather than relying solely on external safety mechanisms.

The authors also outline several open problems for future work.

### Weaknesses
The authors present an upper bound on the harm probability, though it appears to be highly conservative. It would be valuable if they could offer a convergence rate or practical guarantees to make the framework more usable. Additionally, it is unclear how this approach compares to other conservative methods for preventing harm. 

Since the theoretical results lack practical assurances, I would have appreciated more experimental validation, especially in complex and realistic settings. 

Obtaining a Bayesian oracle could be very challenging (posterior distribution). 

Overall, while the paper introduces a promising method for designing safer AI systems, it would greatly benefit from additional components (both theoretical and experimental) before publication.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the problem of bounding the probability of some event in the context of an unknown but consistent distribution and a Bayesian setting. 

The paper is motivated by the prevention of harm by AI agents. In short, harm is inherently unavoidable since in real applications we have no direct access to the distribution governing the environment. However, if we assume a fixed distribution, and a prior assumption of that distribution, we can get better and better approximations when data is presented to us, by using the data to update our prior knowledge of the distribution. With this, we can theoretically bound the probability of doing harm. In deployment, actions whose probability of harm is larger than some threshold can be blocked.

The paper explores two cases: incoming data as iid and non iid, and obtains bounds on the probability of harm in both cases.

The paper presents an experimental evaluation on a multi-armed bandits example, blocking actions that are considered unsafe according to the different bounds obtained as well as a baseline (with an unrealistic assumption of the underlying model). The paper ends with a discussion of the open problems still to be solved to be able to use this method as a reliable guardrails for AI agents.

### Strengths
S1. The topic of AI safety is timely and relevant for ICLR.

S2. The theoretical results (as far as I could check) are sound.

S3. The experimental evaluation serves to showcase how these bounds could be used in a realistic scenario.

### Weaknesses
W1. I understand the appeal to frame this work in the context of harm by an AI agent, and I think it is an interesting point. However, there is nothing inherent to "harm" in the concept presented. The concept of "harm" could be substituted by "reward at a state" and we could be discussing the same results in a different light. I think the paper may benefit from a more general motivation. Specifically, the mathematical framework seems to focus on bounding probabilities of events, which is a general problem, and the specific application to harm seems like a particular case. The paper could be strengthened by explicitly acknowledging this generality and discussing how the results could be applied in other contexts beyond AI safety, for example, in risk management or decision-making under uncertainty.

W2. While the experimental evaluation is welcome, it is a very simple example, and one wonders if these theoretical bounds would find applicability in problems that are more complex and close to the real applications of guardrails. The multi-armed bandit example, while illustrative, does not capture the complexities of real-world AI systems. For example, the state space in the experiment is very small and the harm function is quite simple. It is unclear how these bounds would scale to problems with high-dimensional state spaces, complex action spaces, and more intricate definitions of harm. A more compelling evaluation would involve scenarios that are closer to the intended application of the guardrails, such as simulated environments with more complex dynamics and reward structures.

W3. The concept of guardrails presented here, as an algorithm that blocks an action if it shows an expected harm larger than some threshold, is very similar to the concept of probabilistic shielding in MDPs [1] (which is essentially the "cheating guardrail in Sec. 5), and this can be extended to partially observable MDPs to eliminate the (unrealistic) assumption of having full knowledge of the ground truth [2]. The paper would benefit from comparing to these methods, especially with [2]. The current work does not adequately differentiate itself from these existing approaches, and a detailed comparison is needed to highlight the novel contributions and limitations of the proposed method in relation to probabilistic shielding techniques, especially in the context of partial observability.

W4. The paper does not engage in some recent work on defining harm in similar scenarios, see for example [3] or [4]. It could be useful to understand, in light of different definitions of harm, whether the results are specific to harm prevention, or can be framed in a more general understanding of bounds over rewards. The lack of engagement with these different definitions of harm is a significant oversight. The paper should discuss how the proposed bounds relate to these alternative definitions and whether the results are robust to different interpretations of what constitutes harm. This discussion is crucial for understanding the scope and limitations of the proposed approach.

### Questions
Q1. How do you envision these guardrails to be applied in realistic scenarios? For example, consider the situation of a language model trying to obtain your passwords, or an autonomous car trying to crash with another vehicle. Could this notion of harm be applied efficiently to these realistic scenarios?

Q2. How sensitive are the results to the choice of priors in the Bayesian framework? Can the authors discuss the robustness of the proposed approach under different prior choices?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the problem of evaluating an unknown world model from observed data to determine whether it satisfies a certain safety metric. The safety metric, or guardrail, is a binary variable $H$, taking other variables in the world model as input. The authors utilize a Bayesian approach. It assumes access to the actual prior distribution over the groundtruth world model. The authors first prove that under certain parametric assumptions, the posterior distribution over candidate models will uniquely converge to the ground-truth model at the limit of large samples. Building on this concentration results, the authors derive an upper bound over the posterior probability of the harmful event $H = 1$ conditioning on the observed data. This concentration bound is then extended to non-i.i.d settings where observed samples are correlated. Finally, simulations were performed, and results supported the proposed theory.

### Strengths
- The paper is well-organized and clearly written. All the theoretical assumptions have been stated.
- The proposed concentration results seem reasonable. The derivations seem technically sound.
- Training large AI systems to satisfy certain safety criteria (i.e., with guardrails) is an exciting problem. This paper formulates this problem as a hypothesis-testing problem and presents non-trivial algorithms to perform the test. This problem formulation could be inspiring for other AI researchers across domains.

### Weaknesses
 - The concentration result in Prop. 3.1 assumes "all theories in $M$ are distinct as probability measures." This assumption does not seem to hold many common probabilistic models. For instance, in the linear component analysis, the number of independent components is generally not uniquely discernible (i.e., not identifiable) with non-linear mixing functions. Also, the number of latent components in Gaussian mixtures is generally not identifiable from the observed data. This seems to suggest that the application of the proposed concentration results might be limited. The assumption of distinct probability measures is particularly restrictive, as it requires that even infinitesimally different parameterizations must result in observably different distributions, which is rarely the case in practice. This identifiability issue is a significant hurdle for applying the theoretical results to real-world scenarios.
- The proposed concentration results also assume access to the actual prior distribution generating the ground-truth world model. It is unclear whether the upper bound could still hold when the prior distribution is unknown and misspecified. Specifically, the sensitivity of the derived bounds to the choice of prior is not analyzed. A misspecified prior, even if it assigns positive probability to the true model, could lead to a significantly different posterior distribution and invalidate the derived concentration bounds. This is a crucial point, as in practice, the true prior is almost always unknown and must be approximated, and the impact of this approximation needs to be rigorously addressed.
- Other concentration bounds exist over the target estimates using Baysian methods. Generally, one should be able to translate empirical concentration bounds to the Bayesian settings. For instance, (Osband & Van Roy, ICML'17) translates the concentration bounds for online reinforcement learning to Bayesian regret. How does the proposed method compare to other related work? This paper should include a section discussing related work in large deviation theory and how this paper is situated in the existing literature. The paper lacks a discussion on how the proposed approach relates to existing Bayesian concentration results, and how the assumptions and guarantees compare to other methods such as PAC-Bayes bounds. Without this comparison, it is difficult to assess the novelty and practical advantages of the proposed approach.

### Questions
1. How does the upper bound in Prop. 3.4 apply if the prior distribution $P$ is misspecified?
2. How does this work compare to the existing literature on concentration bounds in the Bayesian setting? For instance, these methods could include analysis of Bayesian regret in RL, and PAC Bayes.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper is tackling the problem of safety in AI. The authors take the view of defining safety as avoiding certain undesirable states in specific contexts.
They introduce a framework based on Bayesian inference from which an agent can derive safe policies that come with (probabilistic) guarantees of preventing harm.
The approach is safe-by-design, i.e. able to prevent undesired outcomes even if no concrete example of harmful states was ever observed in the system.

### Strengths
The main strength of the paper is the introduction of a (as far as I am aware) novel view at safe-by-design in AI at runtime and opening the possibilities for future Bayesian methods to utilize the safety guarantees shown in the paper. Allowing for safety guarantees and steering future work in a direction that empashizes those is a significant problem in AI.
I especially appreciate the discussion on open problems of the approach in the conclusion.

The theory being developed is also quite general and spans over a wide range of possible systems/problems.

The paper is well motivated and generally well structured, introducing formal concepts as needed in the respective sections. A small experimental evaluation is performed and well discussed. Proofs are provided in the appendix and I could not find any mistakes.

### Weaknesses
My main critique points of the paper are the lack of technical novelty (or at least it is not clarified enough if there are new results) and questions on applicability.

For the former, essentially all Propositions and Lemmata are either adaptations of well known results (Prop 3.1), taken from previous literature (Lemma 4.1, Prop 4.2), or rather simple Corollary derived from them (Lemma 3.3, Props. 3.4, 4.4, 4.5, 4.6). For Prop. 4.2 is is shown that the result is tight (Remark 4.3). To me it did not became clear whether this is a known result or a new contribution. It is also not clear whether the derived results (Props. 4.4, 4.5, 4.6) are also tight as a consequence or whether there is room for improvement. For Prop. 4.5 and 4.6 in particular, restricting the possible world models indeces to $\mathcal{I}^{\alpha}_{1\colon t}$ is essential, however, the choice of definition of $\mathcal{I}^{\alpha}$ is not really motivated. At the same time, Fig. 2(a) shows a substantial gap between applying Prop 4.6 in practice, and the theoretical optimum. This begs the question whether a different definition of $\mathcal{I}^{\alpha}$ (e.g. a simple cutoff, or requiring $\mathcal{I}^{\alpha}$ to have a certain probability mass) has potential to yield tighter bounds. However, as the definition of $\mathcal{I}^{\alpha}$ is not motivated, these questions remain unadressed.

For the applicability, my core concern is that the main problem in AI is not providing safety guarantees under certain assumptions, but rather designing a Bayesian agent that actually works well for a given problem while satisfying these assumptions. To go into detail, section 3 only provides "law of large numbers"-style guarantees which are not useful in practice. A small paragraph on the rate of convergence (which would be very helpful to know) is included but essentially is very problem-dependent and thus not discussed in detail in this more general framework. In the experimental evaluation, where Prop. 3.4 is utilized, it is not even clear whether $t$ is large enough for the guarantee statement of Prop. 3.4 to hold (on top of Prop 3.4 not being applicable due to non-i.i.d. as the authors mention themselves). Section 4 then relaxes to probabilistic guarantees, which is a more practical approach. However, to apply the results of section 4 in practice it ultimately relies on defining a hyperparameter alpha. On the theoretical side, the guarantees in section 4 only hold if alpha is chosen small enough (which is impossible to know without knowing the system in the first place) and on the practical side, the evaluation in section 5 shows that choosing alpha too large can have catastrophic consequences, even for the simple bandit system considered in section 5. In summary, I do not see any immediate way to take advantage of the theoretical results the paper provides. This is also amplified by the fact that the main body essentially does not discuss related work, and how existing approaches can be embedded into the framework.

*These weaknesses make the paper feel like more of a statement paper with some additional mathematical background, rather than a fully fletched research paper.*

As a minor comment, from a reader's POV, the paper can be hard to follow at times, especially in the formal sections. Many paragraphs are written in a very technical way, assuming a deep mathematical background. While this surely can be expected from an audience like ICLR, I feel like many sections disrupt the flow of the paper, e.g. the two paragraphs "Setting" (l.155ff and l. 268ff). While these are defnitely important to make the paper rigorous, they are not strictly required to convey the main ideas of the paper. In the interest of readability, it might be advantageous to instead outsource the technical definitions to a separate section.

### Questions
1. Can you detail how you can utilize the CLT to obtain convergence rates (line 238ff)? If you applied this to the example in seciton 5, would it yield practical bounds?

2. Are the results in Propositions 4.4 to 4.6 tight (in a similar vein as Remark 4.3 shows for Proposition 4.2)?

3. How do you motivate the definition of $\mathcal{I}^{\alpha}_{1\colon t}$ and have you considered different approaches?

4. Can you provide some heuristics on choosing a safe, yet effective $\alpha$ a priori? Which information might be helpful for this from e.g. which model paramteres have the biggest impact on $\alpha$ and what information from a domain expert could be incorporated?

5. Can you make any predictions on how you proposed guardrails perform on larger, more complex models? In particular, how do you expect the overestimation of harm (see Fig. 2) to be affected?

6. Are there any existing works in which your framework fits, i.e. for which you can give (probabilistic) guarantees where they were previously unavailable?
If not, are there certain settings in which you can make reasonable a priori assumptions such that your framework is applicable and concrete guarantees can be derived for a given data set?

minor comments:
- line 96: explain what $q$ is
- line 193: introduce delta as dirac notation beforehand
- the axis and legends in the figures in section 5 are barely readable

### Soundness
4

### Presentation
2

### Contribution
2
