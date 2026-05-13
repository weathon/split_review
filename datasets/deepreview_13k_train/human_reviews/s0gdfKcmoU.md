# Securing Equal Share: A Principled Approach for Learning Multiplayer Symmetric Games

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
This paper examines multiplayer symmetric constant-sum games with more than two players in a competitive setting, including examples like Mahjong, Poker, and various board and video games. In contrast to two-player zero-sum games, equilibria in multiplayer games are neither unique nor non-exploitable, failing to provide meaningful guarantees when competing against opponents who play different equilibria or non-equilibrium strategies. This gives rise to a series of long-lasting fundamental questions in multiplayer games regarding suitable objectives, solution concepts, and principled algorithms. This paper takes an initial step towards addressing these challenges by focusing on the natural objective of \emph{equal share}—securing an expected payoff of $C/n$ in an $n$-player symmetric game with a total payoff of $C$. We rigorously identify the theoretical conditions under which achieving an equal share is tractable and design a series of efficient algorithms, inspired by no-regret learning, that \emph{provably} attain approximate equal share across various settings. Furthermore, we provide complementary lower bounds that justify the sharpness of our theoretical results. Our experimental results highlight worst-case scenarios where meta-algorithms from prior state-of-the-art systems for multiplayer games fail to secure an equal share, while our algorithm succeeds, demonstrating the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper considers multiplayer symmetric constant-sum games, focusing on achieving equal share - where a player secures an expected payoff of $C/n$ in an n-player game with total payoff $C$. This work is particularly relevant for games like Mahjong, Poker, and Diplomacy, where traditional two-player zero-sum game theory falls short.

The paper makes serveral theoretical contributions. First, they identify two conditions for achieving equal share (over the worst case): all opponents must deploy the same strategy, and they must have limited adaptivity while being modeled by the learning agent. 

For fixed opponents, they employ the Hedge algorithm; for slowly adapting opponents, they introduce the SAOL_H algorithm; and for intermediately adapting opponents, they utilize behavior cloning. Importantly, they provide matching lower bounds that demonstrate their algorithms are near optimal.

---------
Post rebuttal: I have read the author's rebuttal. My concerns on the technical novelty remains (this is also observed by other reviewers). I still think the paper studies an interesting topic.

### Strengths
The mult-player constant sum game is of great interests to practice, and the strength of this paper paper lies in its conceptual contribution.

### Weaknesses
1. The technique is not strong, seems to be a natural modificaiton to the existing (adaptive) online learning algorithm.


Minor issue: Some of the the most up to date (and the state-of-art) literature on hardness of NE and no-regret learning in games:

[1] Inapproximability of Nash equilibrium, Aviad Rubinstein. STOC'15.
(This paper gave the best hardness result for NE)

[2] Fast swap regret minimization and applications to approximate correlated equilibria. Binghui Peng, Aviad Rubinstein. STOC'24

[3] From External to Swap Regret 2.0: An Efficient Reduction for Large Action Spaces. Yual Dagan, Constantinos Daskalakis, Max Fishelson, Noah Golowich. STOC 2024

### Questions
No.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies n-player symmetric constant-sum games, specifically how an agent can guarantee themselves a 1/n- fraction, i.e. "equal share" of the total payoff.  They identify conditions under which a learner can guarantee themselves this equal share against (n-1) opponents. The paper also studies various no-regret algorithms that can guarantee equal share under these conditions and compares their performance to self-play based meta-learners.

They identify two conditions necessary for a single player, called the learner, to learn a strategy that gives them their equal share in a repeated interaction - 
1. All the other (n-1) players, called the opponents, must deploy the same strategy
2. The opponents must have limited adaptivity over the rounds of play

The first condition is shown via analyzing the one-shot version of the game and showing that the minimax theorem does not hold in symmetric n-player constant sum games. This condition is justified by studying the game against opponents drawn from a large random population. The second condition is additionally required to show that strongly adaptive no-regret algorithms achieve small dynamic regret against opponents with limited adaptivity. For intermediate rates of adaptivity, the paper also studies the payoff obtained by mimicking the identical opponents. The final theoretical result is to show matching lower bounds for dynamic regret.

The paper also experimentally compares the performance of these algorithms against that of existing self-play based frameworks.

### Strengths
The main strength of the paper is coming up with a simple and compelling framework to study learning in n-player symmetric games. The paper has some clean results showing that the minimax theorem and variants do not hold in multiplayer symmetric games and uses this to place some reasonable restrictions on opponent behavior. In particular, the paper introduces some exemplar multiplayer symmetric games, such as the majority/ minority vote game, which demonstrate useful properties that provide insight into the nature of equilibria and best-responses in multiplayer symmetric games. The results related to these parts

Another strength of the paper is in coming up with a natural setting (where opponents are drawn from a large population) to justify working with the condition that all opponents behave identically.

The paper establishes matching upper and lower bounds for payoffs in the online learning setting -- for different regimes based on how swiftly the opponent's strategy and the resulting environment is changing. In particular, the lower bounds extend previous results about general multiplayer games to the special case of symmetric games.

### Weaknesses
There are two main weaknesses in my view:

1. One of the main technical results in the paper is about dynamic regret bounds against opponents with limited adaptivity in changing their strategies (and consequently the online optimization environment they induce). To what extent are the ideas in this result different from prior work in this area - is there something specific to symmetric games (such as faster convergence) that is explored in the paper? More broadly, this raises a concern about the technical depth and significance of the results.
 
2. I do not understand the comparison to self-play. If I understand correctly, self-play is used to come up with a static strategy (via playing copies of the learner) that is then tested against a particular benchmark strategy for the (n-1) opponents. Importantly, the self-play process does not get to see the opponents' strategy while learning. On the other hand, the no-regret algorithms get to see the opponents' strategy, either fixed or slowly changing, and are allowed to adapt to this strategy. I'm not sure how meaningful this comparison is, since it does not appear to compare the same shape of object.

### Questions
My questions are related to the weaknesses highlighted above --

1. To what extent are the ideas in the result about dynamic regret different from prior work in this area. Is there something specific to symmetric games (such as faster convergence) that is explored in the paper? Is there a reason that results about dynamic regret do not directly imply Theorem 5.2.

2. Does it make sense to compare self-play to no-regret (and variants) given that the two frameworks (as set up in the paper) get to see different levels of information? For example, if the experiments adversarially pick the opponent strategy based on the result of self-play, then the comparison is trivial since we would then be comparing playing first (self-play) versus best-responding while playing second (no-regret).

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper considers multi-player symmetric zero-sum games, a class which captures many games from realistic applications. In light of the deficiencies of existing solution concepts in such games, the paper proposes a new solution concept, namely equal share---a player must secure a utility or 0. They proceed by identifying sufficient and necessary conditions under which equal share is attainable. Experiments are also conducted to highlight some of the theoretical results.

### Strengths
Identifying reasonable solution concepts beyond two-player zero-sum games has been a major challenge in game theory. Common solution concepts, such as Nash equilibria and correlated equilibria, have many deficiencies, and so attempting to explore different concepts that overcome those issues is certainly a fruitful research direction. The paper contributes to this line of work by proposing a natural objective, described above, which appears to be novel in its current form. Further, the authors provide necessary and sufficient conditions under which that solution concept can be attained. The conditions are very interpretable and natural, and provide a theoretical framework to design principled algorithms in practice. It is plausible that the approach of the paper can guide the performance of systems in practice. The paper is generally well-written, and all claims appear to be sound. The scope of the paper would also make it a good fit for a conference such as ICLR.

### Weaknesses
On the negative side, my main concern is about the novelty of the results. First, all the observations made in the paper (Section 3 and in part Section 6) about the other solution concepts and the self-play framework are well-known and immediate. It is clear that one can devise simple examples where common solution concepts fail in terms of the objective put forward by the paper. For instance, in a three-player game where two players collude against the third, standard Nash equilibrium analysis would not prevent the two colluding players from gaining the majority of the reward, leaving the third player with potentially very little. The more interesting question, in my opinion, is why the self-play framework performs that well in games such as multi-player poker despite those obvious deficiencies. In terms of the conditions identified in the paper in order to achieve equal share, it is again fairly immediate to see that there are necessary and sufficient. In particular, when the opponents are not fully adaptive, most of the positive results obtained in Section 5 follow readily from existing results in the literature on dynamic regret. Specifically, the paper's analysis of achieving equal share under limited opponent adaptivity closely mirrors the regret minimization framework, where convergence to a no-regret strategy guarantees that the average payoff will be at least as good as the best fixed action in hindsight. As to whether equal share is a reasonable objective, I don't believe there is a definite answer. The fact that it does not correspond to an equilibrium is an obvious concern, but I understand that going beyond equilibrium will be necessary to make progress in this line of work. Overall, I believe that the technical contributions of the paper do not go far enough compared to existing results to merit acceptance.

### Questions
I have no further questions.

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
4

### Summary
This paper examines multiplayer symmetric constant-sum games with more than two players in a competitive setting. In contrast to two-player zero-sum games, equilibria in multiplayer games are neither unique nor non-exploitable, failing to provide meaningful guarantees when competing against opponents who play different equilibria or non-equilibrium strategies. This gives rise to a series of long-lasting fundamental questions in multiplayer games regarding suitable objectives, solution concepts, and principled algorithms. This paper addresses these challenges by focusing on the minmax strategy and  the natural objective of equal share—securing an expected payoff of C/n in an n-player symmetric game with a total payoff of C. They rigorously identify the theoretical conditions under which achieving an equal share is tractable and design a series of efficient algorithms, inspired by no-regret learning, that provably attain approximate equal share across various settings.

### Strengths
They rigorously identify the theoretical conditions under which achieving an equal share is tractable.

### Weaknesses
The significance of the contribution is limited.

1) The so-called suitable solution concept for learning in multiplayer games is a minimax strategy, which is not new.

2) This paper mentioned that symmetric games are popular in practice, however, the large games mentioned in this paper are not symmetric. Please give more detailed real-world cases.

3) This paper mentioned that all asymmetric games can be converted to symmetric games. More details should be given, especially how the results in this paper can be used in all asymmetric games.

4) This paper shows that the equal share can be secured under two conditions, making a multiplayer game equivalent to a two-player zero-sum game with the opponent fixed.  This case is trivial for securing an equal share. As two-player zero-sum games have been studied well, then the following algorithm is trivial.

These results may not help solve general multiplayer games.

### Questions
no.

### Soundness
3

### Presentation
2

### Contribution
2
