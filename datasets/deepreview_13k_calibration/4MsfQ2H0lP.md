# Deep Reinforcement Learning for Modelling Protein Complexes

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
AlphaFold can be used for both single-chain and multi-chain protein structure prediction, while the latter becomes extremely challenging as the number of chains increases. In this work, by taking each chain as a node and assembly actions as edges, we show that an acyclic undirected connected graph can be used to predict the structure of multi-chain protein complexes~(a.k.a., protein complex modelling, PCM). However, there are still two challenges: 1) The huge combinatorial optimization space of $N^{N-2}$ ($N$ is the number of chains) for the PCM problem can easily lead to high computational cost. 2) The scales of protein complexes exhibit distribution shift due to variance in chain numbers, which calls for the generalization in modelling complexes of various scales. To address these challenges, we propose \textbf{GAPN}, a  \textbf{G}enerative \textbf{A}dversarial \textbf{P}olicy  \textbf{N}etwork powered by domain-specific rewards and adversarial loss through policy gradient for automatic PCM prediction. Specifically, GAPN learns to efficiently search through the immense assembly space and optimize the direct docking reward through policy gradient. Importantly, we design an adversarial reward function to enhance the receptive field of our model. In this way, GAPN will simultaneously focus on a specific batch of complexes and the global assembly rules learned from complexes with varied chain numbers.
Empirically, we have achieved both significant accuracy (measured by RMSD and TM-Score) and efficiency improvements compared to leading PCM softwares.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a generative adversarial policy network (GAPN) for modeling large protein complexes through sequential assembly of individual protein chains. GAPN uses reinforcement learning to efficiently explore the vast combinatorial search space and find optimal assembly actions. The adversarial reward function in GAPN incorporates global assembly knowledge from complexes of various sizes, enabling it to generalize despite limited training data. Overall, GAPN achieves state-of-the-art accuracy in predicting structures of protein complexes across a wide range of chain numbers with significant speed-up.

### Strengths
This work integrates reinforcement learning, graph neural networks, and adversarial training to tackle the challenging problem of protein complex modeling, which is novel. In detail, the authors identify the key issues of huge search space and lack of generalization across protein complexes of different sizes. The proposed GAPN framework well addresses these challenges through policy-based active search and an adversarial reward function that encodes global assembly knowledge. The graph representation of protein chains and complexes is well-motivated and fits naturally with the assembly actions. The experiments comprehensively evaluate performance over a range of complex sizes, convincingly demonstrating GAPN's accuracy and efficiency advantages when compared to existing baselines. The ablation studies validate the benefits of the adversarial reward.

### Weaknesses
It would be more helpful and intuitive to provide the assembly process of GAPN and MoLPC for the examples shown in Figure 4. 

For the efficiency analysis, it would be better to also theoretically analyze the exploration complexity and empirically analyze the relationship between efficiency and chain number N.

### Questions
The authors mention that they apply two types of dimer structures, the ground-truth dimers (GT Dimer) and dimers predicted by AlphaFold-Multimer (AFM Dimer). In Table 6, the GAPN results using either of them are noted and provided. Are the results in Table 2 achieved by using both or one of them?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Paper is interested in protein folding. Given a protein, i.e., a "graph" of amino acids where each amino acid is a sequence of "residues", paper would like to output the 3D structure of the protein (i.e., the cartesian xyz coordinates of each residue), subject to rotation and translation invariance. The paper achieves that by repeatedly attaching amino acids to one another. Specifically, if a protein consists of $N$ amino acids, then their algorithm runs for $N - 1$ iterations. At each iteration, a pair of amino acids will be paired (the choice of the pair is output by their RL policy, with softmax activation). Their algorithm allows on running on larger proteins (e.g., >20 amino acids)

-------------

# Update

I read the author's response. Accordingly, I am raising my score

### Strengths
# Problem domain
* The paper is an important problem domain: protein folding. Accurate protein folding could imply faster discovery of drugs, especially given the "virus era" erupted by COVID-19.
* The problem comes with some interesting challenges, specifically, models should be in(/equi)variant to rotation and translation.

# Enabling folding of larger proteins

In my understanding (per paper text), the earlier methods either take too long to simulate folding for larger proteins (e.g., >9 chains) or give bad accuracy. The intent of the paper is to fill that gap.

# Dataset

They contribute a dataset containing non-redundant complexes. This is useful to test the generalization of protein modeling.

### Weaknesses
 # Missing primer / prelim
It would be nice if you give some 4-line summary of terminology (even if brief). The ICLR audience might not be familiar with concepts like "docking" and "dimer".

# Adversarial reward Eq.3
The motivation and implementation of Eq.3 are ambiguous. It says that $p_{data}(x)$ is "the underlying distribution of ground-truth assembly action set". Can you give details to the support of the distribution? Is it actually "pairs of amino acid indices"? Do you even have that information in the dataset? I thought you only have protein chains (not set of pairs of indices). Does every protein become $N-1$ entries in $p_{data}$. Importantly, does the order matter of how you order these edges? Perhaps some amino acid $C$ wouldn't bind to $B$ but would bind (from left) to $B$-$A$. The description of $p_{data}$ is confusing, especially given that the input is a set of protein chains, not a set of assembly actions.

# GNN
In Equation 4, the aggregation is done by $D^- U D^-$. Can you please explain function "AGG" or remove it, if it was a typo?

# Clarity
* Second page, around the middle: "Balance between exploration and exploitation". Can you please elaborate in the text?

### Questions
In addition to the points brought-up in "Weaknesses", above, I have the following questions:

Q1. where does $\theta_{old}$ in Eq.6 and Eq.7 come from?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a novel deep reinforcement learning model, named GAPN, to efficiently explore the vast combinatorial optimization space in the protein complex modelling (PCM) prediction problem to find the optimal assembling action. GAPN allows active exploration of a vast space of potential solutions to strike a balance between trying new actions and sticking with known good actions, ensuring it avoids local optima. Additionally, an adversarial reward function incorporating global assembly rules enhances the model's learning process and generalization abilities.

### Strengths
1. The paper is well-organized and easy to follow.
2. Experimental results demonstrates the effectiveness of proposed GAPN in both prediction accuracy and efficacy.

### Weaknesses
This idea is not new, and the models they used are all well established.

### Questions
N.A.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces GAPN, a model designed to predict docking complexes through the application of reinforcement learning. The agent is tasked with determining the optimal docking path, subsequently utilizing precomputed dimer structures to assemble the entire complex. The paper provides an extensive comparative analysis with established methods such as Multi-LZerD, RL-MLZerD, AF-Multimer, ESMFold, and MoLPC, demonstrating GAPN's superior performance across various protein chain number ranges, as evidenced by metrics like TM-Score and RMSD.

### Strengths
1. The paper is articulate, well-structured, and easy to follow.

2. The authors have provided a detailed description of the RL setup, including the state, action, transition, and reward components, which are crucial for understanding the methodology.

### Weaknesses
1. The model primarily focuses on predicting the docking path, relying on precomputed dimer structures for the completion of the docking task. This reliance on precomputed structures potentially limits the model’s applicability in real-world scenarios, as it is sensitive to the quality of these precomputed dimers. Furthermore, the method does not address the potential for error propagation arising from inaccurate precomputed dimer structures. The paper does not explore the impact of using dimers predicted with varying degrees of accuracy, which is a critical consideration for real-world deployment where ground truth dimer structures are unavailable.

2. The protein docking process is simplified to a sequential decision-making problem in the proposed method. Each step in this process is determined by a precomputed dimer. While the precomputed dimers (utilizing AFM or ESMFold) effectively capture bi-interactions, they may not adequately represent the complex interactions that can occur across different chains in a protein complex in real-world settings. This approach neglects the potential for cooperative binding effects and long-range interactions that are often crucial for accurate complex structure prediction. The model's reliance on pairwise interactions could lead to suboptimal configurations in larger complexes where multi-body interactions are significant.

3. There appear to be inconsistencies in some of the comparative results presented. GAPN has the advantage of accessing precomputed/prefetched dimer structures, reducing its task to merely finding a docking path. This setup makes the inference time incomparable to other baselines like AFM and ESMFold, which adopt an end-to-end approach for predicting complex structures. Consequently, the inference speedup showcased in the tables may not translate to tangible benefits in practical applications. The paper does not adequately address the computational cost associated with precomputing these dimer structures, which could be substantial for large protein complexes.

### Questions
1. Could you please clarify the source of the dimer structures used by GAPN in Table 2? If GT-Dimer is utilized, it implies that GAPN has direct access to the ground truth relative positions of different chains, which could potentially skew the results and present a misleading improvement.

2. In Section 4.1, the paper mentions that all possible pairs of chains are precomputed or fetched. Could you provide details on the average time spent in this step and the average number of dimer structures generated?

3. In Table 1, it is indicated that GAPN does not optimize the dimer structure. Could this lead to error accumulation, especially if some precomputed dimer structures significantly deviate from the ground truth dimer structures?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
