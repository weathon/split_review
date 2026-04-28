# Efficient Online Pruning and Abstraction for Imperfect Information Extensive-Form Games

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 3, 6, 6

## Abstract
Efficiently computing approximate equilibrium strategies in large Imperfect Information Extensive-Form Games (IIEFGs) poses significant challenges due to the vast size of the game tree. Pruning and abstraction methods effectively reduce this complexity, enhancing computational efficiency. However, seamlessly integrating pruning techniques with variants of Counterfactual Regret Minimization (CFR), a leading method for solving IIEFGs, remains a complex task. Furthermore, existing information abstraction methods often involve high computational costs and may require extensive offline pre-computation, limiting their practical applicability. In this paper, we introduce Expected-Value Pruning and Abstraction (EVPA), an online approach that improves efficiency by leveraging expected value estimation within information sets. EVPA consists of three core components: expected value estimation of information sets, expected value-based pruning, and information abstraction for subgames. It estimates the expected value of information sets based on approximate Nash equilibrium strategies, employing these estimations for both pruning and abstraction. By integrating Minimax pruning with CFR, EVPA streamlines decision-making by permanently eliminating sub-optimal actions from the game tree before CFR starts. Additionally, EVPA features an advanced information abstraction mechanism that merges information sets based on both current and future expected values in the subgame, achieving efficient online abstraction. Experiments on HUNL demonstrate that EVPA outperforms DeepStack's replication and Slumbot with significant win-rate margins in multiple settings. Remarkably, EVPA requires only $1$\%-$2$\% of the solving time to reach an approximate Nash equilibrium compared to DeepStack's replication.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a method called EVPA, for online pruning and abstraction of imperfect-information games (IIGs) based on an evaluation of information sets, which is trained offline, in a preparation of an online play.
The evaluation is done by a collection of neural networks, to which the same information set is used as input.
The collected values serve as an estimate of minimum, maximum, and average values that can encountered for that information set in online play, when solving a subgame.
By employing a minimax-like pruning, a subgame can be reduced in size, in advance of solving that subgame, which reduces the time needed for the online solving.
This contrasts with algorithms like CFR, for which pruning has been done in prior work. CFR prunes the tree only dynamically, based on the current state of the algorithm, and still requires full subgame at the first iteration. 
Additionally, if the estimates of values for structurally-compatible information sets are similar, they can be merged together. This is similar to bucketing done in prior work.
Finally, EVPA is used for large variants of Poker and its performance is measured empirically against other prior strong algorithms. EVPA can find strong strategies while requiring substantially smaller time to do so.

### Strengths
- A simple idea that should be easy to implement and can be generally incorporated into many algorithms, as it mainly concerns a general structural aspect of IIGs.
- Strong performance on poker games.

### Weaknesses
 - The paper offers only empirical results. It makes very little evaluations on choices needed for the offline preparation, and only considers the online parameters like time budget. However, a practitioner has to decide a number of choices for the offline preparation: the number of neural networks, the size of training set, a choice of the delta parameter. It is not clear how the approach is robust to these. While I understand this is computationally expensive, it can be done for some (limited) choices, while not making the budget too high. Looking at appendix, DeepStack (which has been replicated in the paper) training time is 569 days, while EVPA is 74. Spending up to 7x budget on more evaluations thus seems reasonable.

- Establishing theoretical bounds based on the choice of delta and EV estimate errors should not be difficult, but is not present in the paper. However, the approach does seem sound.

- The text is a bit repetitive. Instead, I would appreciate more involved discussion of prior abstraction literature and how this work differs.

### Questions
- L300 "each neural network receives a feature describing the information set" --- What exactly comprises the feature? The value of an infoset is not uniquely defined without the context of ranges for a public state. Is this information included?
- Can you please add results where the time limit is increased, up to 2 and 20 seconds, and against DeepStack, for a time budget?
- For the heads-up results, how many matches have been played? Have you considered using AIVAT to reduce variance?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
***Summary of paper** This paper proposes three techniques to improve CFR: (i) expected value estimation of information sets (ii)expected value-based pruning and (iii)information abstraction for subgames. The authors also gave experimental evaluation against an implementation of DeepStack and SlumBot.

### Strengths
The presentation is clear.

### Weaknesses
Some technical points are not sound.

**Detailed questions and comments.** For the three techniques this paper proposes, I have several concerns and questions.

1. Expected value estimation of information sets: How does it compare with the one used in DeepStack? How do you compute Nash of subgame? Is it exact?  One problem of DeepStack is it generates subgames by random sampling, which may not cover the most essential ones. A more advanced one is used in Student of Games which estimates values by considering those encounter during CFR iteration recursively. Have you tried these alternative.


2. Min-max pruning. I don't think min-max pruning is correct in imperfect information games unless you transform the game into public belief tree representation, which you should include public belief states into the value function. However as far as I see the value function you are using are information-set value function, which is incorrect to use min-max pruning because the opponent can change the reach probabilities by changing its action prior to the current information set. However, it you were use min-max pruning for public-belief tree, it will be much more computationally expensive.

3. Abstraction: How often is the abstraction criterion met? How does it compare with previous abstraction techniques such as nested subgame solving in [Brown & Sandholm '17]

### Questions
**Detailed questions and comments.** For the three techniques this paper proposes, I have several concerns and questions.

1. Expected value estimation of information sets: How does it compare with the one used in DeepStack? How do you compute Nash of subgame? Is it exact?  One problem of DeepStack is it generates subgames by random sampling, which may not cover the most essential ones. A more advanced one is used in Student of Games which estimates values by considering those encounter during CFR iteration recursively. Have you tried these alternative.


2. Min-max pruning. I don't think min-max pruning is correct in imperfect information games unless you transform the game into public belief tree representation, which you should include public belief states into the value function. However as far as I see the value function you are using are information-set value function, which is incorrect to use min-max pruning because the opponent can change the reach probabilities by changing its action prior to the current information set. However, it you were use min-max pruning for public-belief tree, it will be much more computationally expensive.

3. Abstraction: How often is the abstraction criterion met? How does it compare with previous abstraction techniques such as nested subgame solving in [Brown & Sandholm '17]

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce EVPA, which is an algorithm for approximating Nash equilibria in two-player zero-sum games based on Counterfactual Regret Minimization. EVPA seeks to improve the runtime efficiency of CFR by pruning sub-optimal actions and abstracting information online. This leads to much faster, high-quality approximations of Nash equilibria compared to a replication of DeepStack in Heads-up no-limit Texas Hold 'em poker.

### Strengths
* Pruning and abstraction in the context of scaling CFR is highly relevant to the community. Current methods simply do not scale well beyond some of the traditional applications.
* Significant portions of the game tree are successfully pruned, though it's unclear what that means for correctness.
* The overall approach seems to have gained an order of magnitude speedup over DeepStack in both training and online solving time. This suggests that it could be useful in applications that are more time-sensitive than poker.

### Weaknesses
 * The claim that the method for information abstraction reduces "the computational overhead of information abstraction from months to less than 1 second" seems false. The method for information abstraction depends on the expected value of an information set according to an approximation of the equilibrium strategy. This expected value presumably takes a large portion of the 74 training days reported in the appendix. Would it be more correct to rephrase this to explain the algorithm finds new abstractions online in seconds, given estimates of information set EV?

* No theoretical guarantees. It seems that by pruning and abstracting information using the methods presented in this paper, the approach loses the convergence guarantees of DeepStack. Do the authors believe there is a promising avenue to obtain some similar bounds? The empirical results certainly show that EVPA computes strong strategies in this domain, but are there situations where pruning or abstraction like this can have catastrophic effects on performance?

* Application to a domain that has limited room for further progress. Though the speedup and performance are impressive (see comment above), the application to HUNL has the potential to have less impact on the community than if it were applied to new, more challenging domains, where super-human performance has not already been achieved. Can the authors share some insight on what other sorts of domain this approach could have a significant impact? It seems a game with a higher branching factor could be a good candidate.

### Questions
* Can the authors please comment on the quality of Deepstack's replication? How does it perform against local best response (LBR)?

* In the experiments in Table 2, what happens with longer solving times?

* How do we ensure pruning does not severely impact the quality of the final strategy?

* How do we know the method for information abstraction is more applicable to games with large information sets? Or do we specifically mean only Omaha here?

### Soundness
2

### Presentation
3

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
The paper introduces an online pruning and abstraction method for the iterates of CFR. It trains a network to evalute the expected value of information sets under the Nash equilibrium. The network is then used to prune actions with low expected values and to cluster information sets with similar expected values using k-means++ during the online execuration of CFR. The trained agent defeats DeepStack's replication and Slumbot with little solving time.

### Strengths
* The method is intuitive in thought but effective in practice. It achieves a cropping rate of about 75% and allows decisions to be made in less than one second.
* The paper provides good experimental results demonstrating improved performance over Deepstack's replication and Slumbot.

### Weaknesses
 * The papar lacks experimental comparisons with other pruning and abstraction methods. 
* The method relies on evaluating the expected value of all informaion sets, in contrast to DeepStack, which evalutes the information sets at the end of each round. So it requies collecting "at least 10 billion samples" (Lines 302-303), compared to the milliones of samples needed by Deepstack. This should take a long time. 
* The performance gains from information set abstraction are marginal, and this leads to exploitability not decreasing in the later iterations.

### Questions
* What is the training time for DeepStack’s replication? Table 4 in the appendix shows that DeepStack takes 569 days, while EVPA takes 74 days. Does this 74 days include the training time for DeepStack’s replication, given that EVPA’s expected value estimation relies on the networks in DeepStack’s replication?
* What is the element of a subgame $S$? Line 227 states that $S$ is a set of histories. Line 285 states that an information set $I_p$ is in $S$. Line 368 states that a public state $s(I_p')$ is in $S$. 
* Can you explain the condition 2 in Lines 387-388? Where is $I'$? Why is the condition "$\mathcal{P}(I \cdots a_1 \dots a_i) \ne \mathcal{P}(I)$" needed? 
* Why is the significance function in Lines 421-422 needed? The importance of an information set should increase with the size of the pot, but in the function $f(g(s), n)$ , it decreases instead.
* What are the confidence intervals in Table 1 and Figure 3?
* (Line 545) How EVPA is used for any initial chip count? EVPA is based on DeepStack which relies on specific assumptions about players’ initial chips.
* Will the code be released to assist research in the field?

### Soundness
2

### Presentation
3

### Contribution
3
