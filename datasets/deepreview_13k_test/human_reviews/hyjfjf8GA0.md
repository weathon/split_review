# A Case Study for the Behaviors of Generalists and Specialists in Competitive Games

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
In this study, we investigate the behavioral change of a heterogeneous population as a system of information exchange. Previous approaches, such as OpenAIFive and NeuPL, have modeled a population as a single conditioned neural network to achieve rapid competitive learning. However, we found that this approach can overgeneralize the population as Generalists and hinder individual learning of specializations. To address this challenge, we propose Joint Entropy Minimization (JEM), a novel policy gradient formulation for heterogeneous populations. Our theoretical and experimental results show that JEM enables the training of Generalist populations to become Specialists. Compared to previous methods, Specialists trained with JEM exhibit increased strategy diversity, improved competitive performance, and reduced population performance disparity. These findings suggest that modeling a heterogeneous population as a group of Specialists can more fully realize the diverse potential of individual agents.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies how a heterogeneous group of agents learn while interacting in a competitive way. More precisely, the authors focus on the question of specialization. They propose a way to make agents who start as generalists learn how to specialize.

### Strengths
The paper considers an interesting question. The tools used (based on information theory) also seem relevant.

### Weaknesses
I found the paper a bit hard to read, partly due some typos or symbols that are not (or not well enough) defined or explained.

### Questions
1. Page 3: below (1) what is $id$ in the inputs of $V$? 

2. Page 4, line 3: Is $N$ a \emph{set} composed of two elements which represent the indices of two players? If so, why is there $\{\dots\}_{k=i}^N$ in the following line?

3. Page 5, equation (9): Could you please give or recall the definition of $w(i;\dots;N+1)$?

4. Page 6, definition of $J$: Could you please clarify how $\psi^k$ in the left-hand side affects the right-hand side? Also, is the $*$ a typo and, if not, what is its meaning?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the behavioural change of a heterogeneous population, and shows that existing approaches may overgeneralize the population as Generalists and hinder individual learning of specialization. A new method based on joint entropy maximization is proposed. The proposed method is shown to increase behavioural diversity and reduce performance disparity.

### Strengths
1. The key research questions are well-motivated.
2. The theoretical analysis of existing approaches, which shows the connection to mutual information, provides new insights.
3. The proposed solution is reasonable.
4. The paper is generally well-written.

### Weaknesses
Some important technical details about this paper lack clarity and need to be further clarified:
1. While one of the main results, Equation 7, looks like mutual information, what does the term $w(x,y)$ of mutual information (defined in Equation 8) correspond to? An explicit connection to mutual information right after Equation 7 is helpful for understanding the claim "The exchange of Policy Gradient between two agents results in the implicit maximization of their Mutual Information (MI) over time. "
2. Similarly, there seems to be a typo in Equation 10 (another key result). In addition, the terms in this equation have not been explained immediately following this equation, making it hard to understand the intuition.
3.  While the paper has emphasized the disadvantage of "generalist", the proposed method (at least, Equation 10) still depends on the policy of the "generalist."  Does the proposed method rely on the existing method to learn the policy of the "generalist"?  How does the proposed method strike a balance between being a "generalist" and being a "specialist"? Will this matter in certain scenarios? The discussion on these issues is not adequate.

### Questions
I would like to see responses to the above weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates how to train heterogeneous agents in competitive games to learn specialized behaviors that leverage their unique strengths, rather than overgeneralizing to a common set of general skills. The paper proposes a novel policy gradient method called Joint Entropy Minimization (JEM), which minimizes the joint entropy between an agent's actions and the average actions of the population. The paper evaluates JEM on a fighting game environment with diverse character attributes and skills and shows that JEM leads to increased behavior diversity, improved win rates, and reduced outcome disparity among agents.

### Strengths
- The paper addresses an interesting and relevant problem of learning heterogeneous behaviors for a diverse population of agents in competitive games.
- The paper evaluates JEM on a realistic and challenging game environment, Naruto Mobile, with over 300 unique characters and complex game mechanics. The paper uses several metrics to measure the behavior similarity, competitive win rate, and outcome disparity of the agents.

### Weaknesses
- The writing of this paper is very unclear and the notation is not precise so it is very hard to follow what is the exact setting and main contribution of the paper.
- The code is not provided for reproduction.

### Questions
- In the PRELIMINARY section, the problem is set as a zero-sum game, why in Eq. (3) the problem is for two policies to jointly maximize a single objective?
- Also in Eq. (3), why are two policies share the same parameter \theta_\tau? Shouldn’t they have their own different parameters?
- In the first line of PRELIMINARY, N={1,2,…,N} is bad notation.
- Right after Eq. (1), the definition of Q(s,a) and V(s, id) are the same?
- Also in this line, what is the definition of id? It is the first time it appears but without properly defined.
- In Eq. (6), what is the definition of T? What is the policy gradient integral over?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method, JEM, to increase the strategy diversity in population-based training in the hope that such a method would improve the performance. Empirical tests suggest that their method indeed improves upon the state of the art.

### Strengths
The method seems novel and interesting, and seems to exhibit favorable experimental results over the state of the art.

### Weaknesses
I found the paper impossible to follow, and gave up on parsing it partway through. Perhaps this is in part due to my lacking certain pieces of background, but I do feel like I am at least somewhat in the target audience of this paper. Here are a few writing concerns, in no particular order.

1. Many technical terms are not defined, some of which are fundamental to understanding the paper. These things ought to have formal, mathematical definitions considering their importance to the paper. Some examples:

    a. Sec 2.1: What is a "population", and what does it mean for a population to be "heterogeneous"? 

    b. Sec 2.2: What is "gradient exchange"?

    c. Sec 2.2.1: I understand x and y to stand in for a^i and a^ii respectively. Is this accurate? In any case this should be stated.

    d. Sec 3: "Generalist" should be defined formally

1. Should I be considering a partially-observable game, or a fully-observable game? The prelims suggest partial observability, but e.g. policies are conditioned on states, which suggests full observability
1. My understanding is that the setting is a two-player zero-sum game. In that setting, a player should never correlate its action with the opposing player, i.e., the mutual information (8) should always be 0 in equilibrium. Why, then, is it interesting to consider (or, indeed, to optimize) the mutual information?

The experimental results seem reasonable, but my ability to parse them is essentially limited to "I see figures in which the current paper seems to do well".  

Due to the writing issues alone, I don't think this paper is publishable in the current state. I vote to reject. If the authors could perform a revision that improves the quality of writing and explanations, I would read such a revision and may change my score. 

Nitpicks (not affecting evaluation):

1. $*$ should probably not be used as a generic multiplication symbol---prefer $\cdot$ (or simply juxtaposition)
1. Some brackets are improperly sized, e.g., Eq (3)
1. Sec 2.2.1: Shouldn't the integral be actually a sum, since at the end of the day these training algorithms operate in discrete time?
1. $\log$ should always use the backslash, i.e., not $log$.
1. It's a bit confusing to use Roman numerals to index the players; why not just use standard Arabic numerals (1, 2, ..., N), as is consistent with most game theory literature?
1. Preliminaries typo: $S : O \times O$ doesn't parse
1. The paper contains a large number of grammatical errors, too many to enumerate. Proofreading would go a long way.
1. Eq (10): it should be explciitly stated that $\mathbb H()$ is the joint entropy (assuming that it actually is).

### Questions
Some questions are listed in the above section; I have none beyond that.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
