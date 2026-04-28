# Rethinking Teacher-Student Curriculum Learning under the Cooperative Mechanics of Experience

- Decision: Reject
- Avg Score: 4.40
- Scores: 6, 3, 5, 5, 3

## Abstract
Teacher-Student Curriculum Learning (TSCL) is a curriculum learning framework that draws inspiration from human cultural transmission and learning. It involves a teacher algorithm shaping the learning process of a learner algorithm by exposing it to controlled experiences. Despite its success, understanding the conditions under which TSCL is effective remains challenging. In this paper, we propose a data-centric perspective to analyze the underlying mechanics of the teacher-student interactions in TSCL. We leverage cooperative game theory to describe how the composition of the set of experiences presented by the teacher to the learner, as well as their order, influences the performance of the curriculum that is found by TSCL approaches. To do so, we demonstrate that for every TSCL problem, an equivalent cooperative game exists, and several key components of the TSCL framework can be reinterpreted using game-theoretic principles. Through experiments covering supervised learning, reinforcement learning, and classical games, we estimate the cooperative values of experiences and use value-proportional curriculum mechanisms to construct curricula, even in cases where TSCL struggles. The framework and experimental setup we present in this work represents a novel foundation for a deeper exploration of TSCL, shedding light on its underlying mechanisms and providing insights into its broader applicability in machine learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the underlying mechanics of the teacher-student interactions in Teacher-Student Curriculum Learning (TSCL). The authors employ cooperative game theory to describe how the composition of the set of experiences presented by the teacher to the learner, as well as their order, influences the performance of the curriculum that are found by TSCL approaches. To do so, we demonstrate that for every TSCL problem, there exists an equivalent cooperative game, and several key components of the TSCL framework can be reinterpreted using game-theoretic principles. The authors also conducted experiments covering supervised learning, reinforcement learning, and classical game.

### Strengths
This paper proposes a novel, promising perspective for theoretically understanding teacher-student learning based on cooperative game. This is an exciting advance for me.

The authors provide rigorous theory with detailed proofs.

The experiments cover a wide range of cases - supervised learning, reinforcement learning, and classical games.

The paper is well written.

### Weaknesses
It is much appreciated that the authors discussed the limitations of the proposed method. However, such a comparison is still not enough. The readers would be much interested in discussions on the differences and advantages of the proposed method from the existing algorithms.

### Questions
Please address the above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provided a game theoretic-based angle to understand teacher student curriculum learning. The paper proposed a data-centric view of the learning process and treat each learning sample as a unit of experience, which could be a batch, dataset, or even an environment. Then each unit of experience is formulated as a player in the game-theoretical framework. The paper considered teacher as an agent to select unit of experience over time with the goal of steering learner's policy to meet some target objective, e.g., maximize performance on a target evaluation set. Using multi-armed bandit as the selection policy for unit of experience, the paper argued that curriculum learning achieves monotonic model improvement when the game is cooperative in nature. Extensive experiments on supervised learning, reinforcement learning among others demonstrate that the new game-theoretic angle is indeed helpful in gaining better insight of curriculum learning.

### Strengths
(1) The paper provided a new perspective of curriculum learning and laid down a foundational framework for assessing the functionality of each individual curriculum based on the cooperative game theoretic framework. The new angle has its own novelty and was never studied before. This opens another road for researchers in this area to gain better understanding of the problem.

(2) Apart from the game-theoretic framework, the work also performed extensive experiments on real-world data such as MNIST to demonstrate the rationality behind the proposed framework, which is pretty interesting and illustrative.

(3) I'd like to highlight that the proposed framework applies to a broad class of learning paradigms, including supervised learning, reinforcement learning, among others. It's easy to see that the proposed methodology can be extended to many other scenarios such as active learning, online learning etc. Therefore, the paper is general enough.

### Weaknesses
(1) While the paper laid down a solid framework for understanding curriculum learning, it lacks a theoretical understanding of the problem, and there are no affirmative theoretical results coming out of it. It provided some generic methodology, but the conclusions are drawn from empirical results. Specifically, the paper does not explore the properties of the cooperative game that is formulated, such as whether it admits a unique Nash equilibrium or the conditions under which the curriculum derived from the game-theoretic framework provably converges to an optimal policy. This makes the paper somewhat weak and less satisfying. A more rigorous analysis of the game's properties and its connection to the convergence and optimality of the curriculum would greatly strengthen the work.

(2) The framework proposed in this paper is nice and elegant, but I am very concerned about the practical side of the methodology - it requires training a model multiple times and evaluating the value of each unit of experience. This is very time consuming if each unit of experience is a large dataset or an RL environment. For instance, in a complex RL environment, evaluating the value of a single unit of experience might require training an agent from scratch, which can take hours or even days. Therefore, it limits the generalizability of the proposed approach. The paper would benefit from a discussion on potential approximation methods or heuristics to make the framework more computationally feasible.

### Questions
(1) Please derive solid theoretical results to support the proposed method, or at least provide some theoretical insights.

(2) Please discuss the generalizability of the proposed method - see comment (2) in the weaknesses part.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a data-centric perspective to analyze the mechanics of teacher-student interactions in TSCL, using cooperative game theory. The set of experiences presented by the teacher to the learner, as well as their order, influence the performance of the curriculum in TSCL. The paper demonstrates that for every TSCL problem, there exists an equivalent cooperative game, and key components of the TSCL framework can be reinterpreted using game-theoretic principles. Experiments covering supervised learning, reinforcement learning, and classical games are conducted to estimate the cooperative values of experiences and construct curricula.

### Strengths
- Originality: The paper introduces a novel perspective on TSCL by analyzing the mechanics of teacher-student interactions using cooperative game theory. This approach is unique and provides a fresh understanding of TSCL.
- Quality: The paper conducts experiments covering supervised learning, reinforcement learning, and classical games to estimate the cooperative values of experiences and construct curricula. This empirical evaluation enhances the quality of the research and validates the proposed framework.
- Clarity: The paper clearly presents the concepts and principles of TSCL, as well as the application of cooperative game theory. The experimental setup and results are well-explained, making it easy for readers to understand the research.
- Significance: The paper's findings shed light on the underlying mechanisms of TSCL and provide insights into its broader applicability in machine learning. This has significant implications for curriculum learning approaches and can contribute to the development of more effective learning algorithms.

### Weaknesses
 - Lack of comparison: The paper does not compare the proposed data-centric perspective with existing approaches or frameworks in the field of TSCL. A comparative analysis could provide insights into the advantages and limitations of the proposed approach. Specifically, the paper lacks a comparison to established curriculum learning algorithms that explicitly consider the difficulty of tasks or experiences when constructing a curriculum. This makes it difficult to assess whether the proposed game-theoretic approach offers a significant improvement over existing methods, or if it simply replicates existing behaviors through a different lens. The absence of such comparisons limits the ability to contextualize the contributions of this work within the broader field.
- Limited scope of experiments: While the paper conducts experiments covering supervised learning, reinforcement learning, and classical games, the scope of these experiments may not be comprehensive enough to fully explore the effectiveness and applicability of the proposed framework. The experiments, while diverse in terms of learning paradigms, are limited in complexity. For example, the supervised learning tasks might not fully capture the challenges associated with real-world datasets, and the reinforcement learning environments may lack the complexity to fully evaluate the proposed method's scalability. Including a wider range of learning scenarios and domains, especially those with known curriculum structures or difficulties, could strengthen the empirical evaluation.

### Questions
My main concern is about the experiments. Since TSCL is mainly for the hard problem which students cannot learn well in the final tasks, however, the experiments here is almost simple tasks. Could you provide a comparative analysis of the proposed data-centric perspective with existing approaches or frameworks in the field of TSCL? This would help in understanding the advantages and limitations of the proposed approach.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyses when and how teacher-student curriculum learning (TSCL) approaches work from a new data-centric perspective. Cooperative game theory is used to understand and interpret the key components of TSCL. It is shown that for every TSCL problem, there exists an equivalent cooperative game, and the learning progression objective and the teacher bandit policy in TSCL methods can be interpreted as an approximation of player marginal contribution and a fair allocation mechanism, respectively. The experiments show that the ordered value-proportional curriculum mechanism proposed can consistently find an (near-) optimal curriculum even when TSCL fails. It is also shown that in settings with significant negative interactions, TSCL cannot produce good curricula.

### Strengths
- The problem studied in the paper is well-motivated. Investigating when and how TSCL algorithms work receives comparatively little attention (compared to studying algorithmic improvements in TSCL) and is an important research problem. 
- Understanding TSCL algorithms from a data-centric perspective looks new to me. Using cooperative game theory to analyse how the teacher-student interactions affect the performance of the curriculum that are found by TSCL algorithms is very interesting. 
- The experimental results seem to show that the proposed game-theoretic and data-centric interpretation of TSCL can be applied to some simple supervised learning and reinforcement learning problems to understand the conditions under which TSCL is effective.

### Weaknesses
 - My main concern of the paper is that the practical use of analysing TSCL algorithms from the proposed data-centric perspective is unclear to me. Given a TSCL problem, it does not seem straightforward to use the game-theoretic analysis presented to understand when and how TSCL works. It is also not clear to me if the formal grounding provided here is more/less useful compared to existing works that aim to understand when and how curriculum learning works as mentioned in the paper (e.g., Wu et al. (2020) and Lee et al. (2021))
- As acknowledged in the paper, all experiments only consider a very small number of "units of experience". In most complex RL tasks, the learner algorithm needs access to hundreds and thousands of units of experience. I do not see how the theory presented can help analyse the TSCL approaches in these more complex settings, such as understanding the conditions under which TSCL is effective. 
- This is a minor problem with respect to the presentation of the paper. I personally found the extensive use of italic type text quite distracting when reading the paper.

### Questions
- I do not really understand how the RL experiment (Section 5.4) answer the research question of "how units’ interactions impact TSCL’s prospects to find useful curricula". The main result seems to just be that the Nowak & Radzik values estimated is in line with folk knowledge that an optimal curriculum exists. Given a particular TSCL method, how do you use a similar analysis to evaluate if the curriculum found by the given TSCL method is useful or not?
- It is mentioned that the experimental result in classical games "contrasts with folk knowledge in population-based training". How to interpret this result? It should be briefly summarised in the main paper. 
- Can you explain the practical use of analysing TSCL algorithms from the proposed game-theoretic and data-centric perspective?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The aim of the paper is to rethink curriculum learning as a game.

### Strengths
The paper is clearly presented as a conceptual paper, but the contribution to the community remains less clear.

### Weaknesses
 The writing style with many words in italics is tedious and distracting. Please fix.

The aim of the paper is to rethink curriculum learning as a game. This has already been demonstrated quite clearly in the work by [Silver et al., Nature,  2017] on AlphaGo Zero, and a body of work building on their results exists, although the authors do not mention this. It is difficult to find a clear contribution, and clear experimental evidence. Also, no clear link to related work has been provided, or a comparison of this algorithms to others.

### Questions
I would advise the authors to study the literature more carefully, to formulate their theory more clearly, to perform more extensive experiments, to use a more approachable writing style, and to make the contributions more explicit.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
