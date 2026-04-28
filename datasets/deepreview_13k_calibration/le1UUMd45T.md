# Solving Multiobjective Combinatorial Optimization via Learn to Improve Method

- Decision: Reject
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Recently, deep reinforcement learning (DRL) has been prevailing for solving multiobjective combinatorial optimization problems (MOCOPs). Most DRL methods are based on the "Learn to Construct" paradigm, where the trained model(s) can directly generate a set of approximate Pareto optimal solutions. However, these methods still suffer from insufficient proximity and poor diversity towards the true Pareto front. In this paper, we propose "Learn to Improve" (L2I), a learning-based improvement method for solving MOCOPs. We embed a weight-related policy network into multiobjective evolutionary algorithm (MOEA) frameworks to effectively guide the search direction. A shared baseline for proximal policy optimization is presented to reduce variance in model training. A quality enhancement mechanism is designed to further improve the Pareto set in model inference. Computational experiments conducted on two classic MOCOPs, i.e., multiobjective traveling salesman problem and multiobjective vehicle routing problem, indicate that our method achieves state-of-the-art results. Notably, our L2I module can be easily integrated into various MOEA frameworks such as NSGA-II, MOEA/D and MOGLS.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new paradigm "learn to improve" in the context of solving Mult objective combinatorial optimization problems (MOCOPs). The proposed approach adds an improvement operation, based on a deep policy network, that works in parallel with individual solutions, using evolutionary technique. The deep network is based on an Encoder-Decoder, where encoder is Transformer-style stacked encoders, with Dual-Aspect Collaborative Attention (DAC-Att). Comparisons with SOA and ablation studies are done.

### Strengths
a. Mathematical fomulation of the proposed method
b. Details of the proposed deep network based on Encoder-Decoder based on Transformer.
c. The use of Dual-Aspect Collaborative Attention (DAC-Att)
d. Details of the algorithm
e. Comparisons with state of the art (SOA) on MOCOPs.
f. Ablation Study

### Weaknesses
 a. In the result tables, the proposed method is not highlighted
 b. The results in tables 1 & 2 are not discussed on why the proposed approach is better only in the last entries?

### Questions
Why the proposed method show better results? Please explain the specificality of the proposed method.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces "Learn to Improve" (L2I), a deep reinforcement learning (DRL) technique designed to address multiobjective combinatorial optimization problems (MOCOPs). L2I contrasts traditional DRL methods by embedding a weight-related policy network into multiobjective evolutionary algorithm (MOEA) frameworks. This assists in directing the search, reduces training variance, and offers an enhanced quality mechanism for better model inference. Computational experiments on classic MOCOPs like multiobjective traveling salesman and vehicle routing problems highlight the superiority of L2I over existing methods.

### Strengths
L2I introduces a new DRL-based approach for MOCOPs. Unlike the traditional "Learn to Construct" methodology, L2I emphasizes iterative improvements. The L2I module has demonstrated adaptability as it can be integrated into various MOEA frameworks, such as NSGA-II, MOEA/D, and MOGLS. This mechanism, applying instance augmentation techniques, improves both the proximity and diversity of the Pareto set. The L2I methodology outperforms other state-of-the-art techniques on standard MOCOPs, even showing better performance than renowned solutions like the LKH solver for specific problems.

### Weaknesses
Since the paper deals with the combinatorial optimization, decomposition methods are not sufficiently elaborated/reviewed.

### Questions
How does L2I compare with methods follows a general scheme of "learn-divide-and-conquer" or "divide-learn-and-conquer"? In a sense, there are approaches that learn how to decompose a problem and there are approaches that decompose a problem before learning. I qualitative assessment may be sufficient.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a new deep reinforcement learning method that involves a learning-based improvement method for solving multi-objective combinatorial optimization problems. A weight-related policy network is embedded into multi-objective evolutionary algorithm frameworks to guide the search. Experimental studies on multi-objective traveling salesman problems and multi-objective vehicle routing problems show the effectiveness of the proposed method.

### Strengths
1.	A learning-based improvement method is proposed for solving multi-objective combinatorial optimization problems with deep reinforcement learning.
2.	An ablation study is conducted to study the proposed method and show its effectiveness.

### Weaknesses
1.	The way the proposed weight-related policy network is embedded is not clearly described. A pseudo-code of the complete method for solving one multi-objective combinatorial optimization problem should be provided. Specifically, the interaction between the evolutionary algorithm and the policy network is unclear. It's not evident how the policy network's output influences the selection, crossover, or mutation steps of the evolutionary algorithm. A detailed step-by-step explanation, preferably with pseudo-code, is needed to clarify this integration.
2.	The proposed method contains several hyperparameters, e.g., the number of transformer-style stacked encoders and the number of attention heads. A summary of them needs to be provided. The paper lacks a comprehensive list of all hyperparameters used in the model, including those related to the reinforcement learning component (e.g., learning rate, discount factor, exploration strategy) and the evolutionary algorithm (e.g., population size, crossover and mutation rates). The absence of this information makes it difficult to reproduce the results and assess the method's sensitivity to parameter choices.
3.	How many times does each algorithm run independently in the experiment? The paper should explicitly state the number of independent runs for each algorithm. This is crucial for understanding the statistical significance of the results. Without this information, it's impossible to assess the robustness of the proposed method and the reliability of the comparisons with baseline algorithms.

### Questions
1.	How does the algorithm perform when using complex operators?
2.	What are the numbers of variables for the test problems in the experiments?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
One of the traditional methods for solving MOCOPs involves the MOEA approach. In this approach, individual solutions in a population pool are continuously updated through cross-overs and enhanced via local search. The authors suggest replacing the local search component within the MOEA. Previously, the local search was driven by a random selection of node pairs; however, the authors now employ a neural network for this pair selection.

### Strengths
1. This is the first L2I approach applied to MOCOPs.

2. A new neural net architecture is introduced, which can accommodate the weight factor used in identifying the Pareto set.

3. A new RL training method is introduced, leveraging the population pool of the MOEA approach.

4. A new quality enhancement method suitable for the MOEA approach is presented.

### Weaknesses
While the authors have commendably applied the L2I approach to MOCOPs, yielding impressive results, the novelty of the ideas underpinning this work doesn't fully meet the expectations I have for ICRL publications.

1. The concept of utilizing a trained neural model to bolster the local search component of a genetic algorithm isn't novel.

2. The presented neural net architecture appears to be a minor variation of an existing one, specifically DACT.

3. The employment of a shared baseline for REINFORCE isn't groundbreaking, as seen in POMO.

4. Similarly, quality enhancement via instance augmentation isn't a pioneering approach.

While I acknowledge that the specific methodologies deployed in the paper are novel, especially given this is the inaugural L2I application to MOCOPs, the broader insights readers can derive from this work seem somewhat limited.

### Questions
Branding the methodology in this paper as "L2I" might lead to confusion in the future. As subsequent research emerges that applies the L2I approach to MOCOPs, referencing this work simply as "L2I" could create ambiguity. Future works that aim to compare their results with this paper would face challenges in distinguishing between this specific approach and other "L2I" methodologies for MOCOPs.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
2 fair
