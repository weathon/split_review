# Mediator Interpretation and Faster Learning Algorithms for Linear Correlated Equilibria in General Sequential Games

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
A recent paper by Farina and Pipis (2023) established the existence of uncoupled no-linear-swap regret dynamics with polynomial-time iterations in extensive-form games. The equilibrium points reached by these dynamics, known as linear correlated equilibria, are currently the tightest known relaxation of correlated equilibrium that can be learned in polynomial time in any finite extensive-form game. However, their properties remain vastly unexplored, and their computation is onerous. In this paper, we provide several contributions shedding light on the fundamental nature of linear-swap regret. First, we show a connection between linear deviations and a generalization of communication deviations in which the player can make queries to a ``mediator'' who replies with action recommendations, and, critically, the player is not constrained to match the timing of the game as would be the case for communication deviations. We coin this latter set the untimed communication (UTC) deviations. We show that the UTC deviations coincide precisely with the linear deviations, and therefore that any player minimizing UTC regret also minimizes linear-swap regret. We then leverage this connection to develop state-of-the-art no-regret algorithms for computing linear correlated equilibria, both in theory and in practice. In theory, our algorithms achieve polynomially better per-iteration runtimes; in practice, our algorithms represent the state of the art by several orders of magnitude.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies regret minimization for extensive-form games. In detail, the authors established a relationship between the linear deviation and the proposed UTC deviation. Therefore, any algorithms which are used to minimize the UTC regret is equal to minimize the linear swap regret. The authors showed sublinear regret bound and experiment results to suggest that the proposed algorithms are the state of the art.

### Strengths
This paper is technically sound, and the experiment results are also comprehensive.

### Weaknesses
The presentation of this paper can be further improved. In order to further demonstrate the contribution of this work, the authors can have a table which records all existing algorithms for linear-swap regret, as well as their computational complexity. Right now it is a little bit hard for the readers to even identify which of the algorithms (UTC-based CFR or algorithms from Farina and Pipis) are better. Another suggestion is the presentation of Section 5. I understand that the authors want to use the example to demonstrate that UTC is more expressive than communication deviation. However, I spend several hours and still can not get an intuitive understanding about why such a claim hold. For instance, why A and B are 'irrelevant' according to footnote 6? I suggest the authors rewrite Section 5 by reorganizing the Figure 1 into several smaller figures with shorter captions. That would make the demonstration much clearer. 

Following the above comment, I can not tell what is the key contribution of this work. The main theorem (Theorem 4.1) suggests that the deviation sets $\Phi_{lin}$ and $\Phi_{UTC}$ are identical, and later the authors suggested CFR in Zhang et al. can be used to solve UTC, which can be further used to solve linear deviation. How the exactly can CFR be applied to linear deviation? A reduction process is expected, similar to what has been done in Theorem 2.3 (an existing result). Meanwhile, why people are interested in forming the equivalence between UTC and linear deviation but not some other types of game and linear deviation? Last, the authors suggested that the per-iteration complexity of CFR depends on the complexity of computing a fixed point iteration problem. How should we compare such a complexity with previous approaches, like Farina & Pipis (2023)?

### Questions
See weaknesses section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the computation of a relaxed version of correlated equilibria, known as linear correlated equilibria. The authors take a regret minimization perspective and design their algorithm for computing linear correlated equilibria by designing algorithms that minimize linear-swap regret. They demonstrate an equivalence between linear deviation and a generalization of communication deviations, where the deviator can send untimed queries to the mediator. Hence, minimizing linear swap-regret can be done via minimizing regret defined under such deviations with untimed communications. Invoking a previous result on the latter problem then gives a linear-swap regret minimizer. Experiments based on several types of games are further conducted, which demonstrate significant improvement of the proposed algorithm compared with existing ones.

### Strengths
The paper is overall clean and rigorously written. The problem studied is interesting and results presented look sound technically. The empirical results also provide significant improvement in comparison to existing approaches.

### Weaknesses
Some parts of the paper seems to lack necessary details, making them quite hard to follow. In particular, the communication deviations and the UTC decision problem in Section 3 are introduced in a very abstract language. For readers not familiar with previous work on communication equilibrium, it would be quite hard to understand why these concepts are defined in described ways. For example, when communication deviations are introduced, it is said that the deviator will maintain a state with the mediator, but there is no explanation about why there needs to be a state. The introduction of the interaction between the mediator and the deviator also lacks intuitions. Overall, while I find the previous sections clear and informative, Section 3 seems to appear a bit abruptly. It might be helpful to provide some more details about comminication equilibrium, or introduce the concepts in this section along with the example in Section 5 (I think I understand them better after reading the example).

Some typos: 

- In Section 5, the sentence "must immediately its first mediator query" reads problematic.

- In the paragraph above Section 7, "this significant(ly) improves"

- There seem to be some typos in Theorem 2.3. On the second line, "where x^{(t)} \in X ... " Do you mean x^{(t)} \in \Phi instead of X? The utility vector u^{(t)} in this sentence also seems to come from nowhere. And when you say "deterministic" external regret, the notion of deterministic seems undefined.

### Questions
- Could you provide some intuition why deviations in EFGs need to be defined as interactions betweem a mediate and a deviator?

- There seem to be some typos in Theorem 2.3. On the second line, "where x^{(t)} \in X ... " Do you mean x^{(t)} \in \Phi instead of X? The utility vector u^{(t)} in this sentence also seems to come from nowhere. And when you say "deterministic" external regret, the notion of deterministic seems undefined.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper makes a conceptual step towards the design of swap regret minimizing algorithms. In particular, inspired by the $\Phi$-regret framework they introduce a set of deviation mappings called untimed communication (UTC) deviations that are shown to be equivalent to the set of linear deviations. These linear deviations have been recently shown to be useful in obtaining sublinear regret in polynomial time for sequential games. Following that, the authors show that UTC deviations are expressible in terms of scaled extensions, which allows them to apply CFR to learn linear correlated equilibrium much faster than the indicative previous work of Farina and Pipis. Finally, several experiments are shown that corroborate the theory and show fast convergence to linear correlated equilibria.

### Strengths
The paper is well written and the structure is clear. Moreover, showing a connection between linear deviations and communication deviations draws a novel parallel with standard sequential deviation sets. This opens up a wealth of potential untimed deviation mappings (along with accompanying equilibrium concepts) to be studied in future. The example presented also gives an intuitive understanding of the deviation and how it can be useful. Finally, the empirical performance of the CFR algorithm instantiated with regret matching+ greatly speeds up convergence to the linear correlated equilibria.

### Weaknesses
While showing a connection between linear and communication deviations is a very neat result, the paper does not seem to be very substantial in otherwise exploring the full potential of this new class of deviations. The ability to obtain faster convergence to linear correlated equilibria is welcomed, but relies on an existing algorithm. In that sense, the major contribution of this work is introducing UTC as a part of the framework for which fast convergence to equilibria can be obtained. Other than that, none of the other results shown seem technically significant. To alleviate this, more discussion or results about the nature of untimed communication equilibria would be helpful, should space allow (perhaps a section about connections to standard communication equilibria, which has been written in the appendix already).

### Questions
- If a generic definition of untimed communication equilibrium cannot be derived, are there relaxations thereof that can be derived in your framework?
- What is the next reasonable step beyond linear deviations in the search for swap regret minimization?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an extension of communication deviation, termed UTC deviations, and theoretically proves that UTC deviations are equivalent to linear deviations in the context of online convex optimization. Given that UTC deviations can be represented using DAG decision problems, regret minimization algorithms like CFR, when applied to these decision problems, can also be utilized to minimize linear swap regrets in online convex optimization scenarios. Building upon prior findings, employing CFR as a $\Phi_{LIN}$-regret minimizer not only promises the same $O(\sqrt{T}d^2)$ upper bound but also offers superior computational efficiency by avoiding the need for an expensive projection. Empirical evaluations further demonstrate that CFR achieves reduced average regrets and requires significantly less runtime.

### Strengths
- The paper bridges decision problems and the online learning problem by proving the equivalence of UTC deviations and linear deviations. This enables the use of algorithms, such as CFR, in online optimization problems to minimize linear swap regrets.
- The paper provides an intuitive example of a UTC deviation and demonstrates that UTC deviations do not necessarily have to be communication deviations
- The empirical analysis is very persuasive to me. The experimental settings and results are explained clearly.

### Weaknesses
 - There is no improvement in regrets when using CFR based on UTC dynamics. Although Figure 2 shows that the regret of CFR outperforms that of Farina & Pipis (2023), the paper does not provide an explanation for this.
- The paper provides only an informal proof of why UTC dynamics have better computational efficiency than Farina & Pipis (2023) in Section 1. A more formal discussion is required and should be placed in Section 6, rather than in the introduction.
- Some notations, such as ${\text co}{\mathcal X}$, are used before being defined.
- I cannot locate a formal definition of linear deviations. Given its frequent use in this paper, at the very least, an explanation is necessary.

### Questions
- Can you provide some explanations for why CFR achieves a better regret than the algorithm in Farina & Pipis (2023)? Figure 2 is presented without accompanying discussion.
- Since both CFR and Farina & Pipis (2023) offer an upper bound of $O(\sqrt{T}d^2)$, is it possible to demonstrate that this is also the lower bound?
- Could you elaborate on how to employ the algorithm from Cohen et al. (2021) to achieve $\tilde{O}(d^w)$ complexity? What is the linear program that must be solved in formal? This addition would make the paper easier to read.

### Soundness
4 excellent

### Presentation
1 poor

### Contribution
3 good
