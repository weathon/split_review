# Diverse Policies Recovering via Pointwise Mutual Information Weighted Imitation Learning

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Recovering a spectrum of diverse policies from a set of expert trajectories is an important research topic in imitation learning. After determining a latent style for a trajectory, previous diverse policies recovering methods usually employ a vanilla behavioral cloning learning objective conditioned on the latent style, treating each state-action pair in the trajectory with equal importance. Based on an observation that in many scenarios, behavioral styles are often highly relevant with only a subset of state-action pairs, this paper presents a new principled method in diverse polices recovery. In particular, after inferring or assigning a latent style for a trajectory, we enhance the vanilla behavioral cloning by incorporating a weighting mechanism based on \emph{pointwise mutual information}.
This additional weighting reflects the significance of each state-action pair's contribution to learning the style, thus allowing our method to focus on state-action pairs most representative of that style.
We provide theoretical justifications for our new objective, and extensive empirical evaluations confirm the effectiveness of our method in recovering diverse policies from expert data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores a methodology for deriving diverse policies from expert trajectory data. Rising from the traditional conditional behavior cloning (BC) algorithm, the authors  introduce an additional importance weight based on Pointwise Mutual Information (PMI), to assess the correspondence between state-action pairs and trajectory styles. The experimental results prove the proposed method can improve policy diversity with PMI weighting.

### Strengths
1. The topic studied in this paper is quite interesting, with an objective to improve policy diversity.
2. This article clearly defines the problem and provides a detailed exposition of the method.
3. This article undertakes extensive comparative experiments across Circle 2D, Atari games and professional basketball player dataset, which valiate the effectiveness of the proposed algorithm compared with the baseline methods.

### Weaknesses
1. This paper aims to enhance policy diversity by incorporating a weighting method based on pointwise mutual information to the Conditional Behavioral Cloning framework. The key proposal of this paper is merely the introduction of a data weighting algorithm, which, in my view, does not represent adequate technical contribution.

2. The manuscript does not include sufficient ablation experiments to validate the efficacy of the proposed data weighting method that utilizes pointwise mutual information. It remains unclear how BC-PMI compares to Conditional Behavioral Cloning that is conditioned on style, where each sample point is assigned equal weight. Additionally, its performance against other traditional data weighting methods has not been adequately compared.

### Questions
1. Which behavior cloning (BC) algorithm is selected as the baseline method? Does the proposed PMI general well across different BC algorithms?
2. From Table 1, the improvement of the proposed BC-PMI seems marginal compared with CBC.

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
2

### Summary
In this work, the authors focus on developing a method for imitation learning better diversity of policy. It works under assumption that the expert trajectories in training are collected by stylized experts. The key is to using a pointwise mutual information-based weighting strategy to determine the policy importance. The state-action pair with higher posterior probability is given higher importance. The proposed method achieves good experiment results and also is demonstrated to be covered in the extreme cases, such as zero mutual information or no overlap among different policy styles in a single state-action pair. For the extreme cases, the theoretical evidence is provided to show that the proposed strategy degrades to usual strategy without failing.

### Strengths
1. The proposed method is motivated by an intuitive insight and the failure of existing alternatives. The use of PMI and MINE are well connected for the purpose.
2. The proposed method achieves good experimental results on the datasets of CIRCLE2D , Atari and Basketball Player dataset.

### Weaknesses
1. Given that stylized experts make unbalanced trajectory generation in training, it might be helpful to discuss the disentanglement between the stylized code and the state-action pair. Some previous works have built related benchmark for the purpose such as [1] and [2]. Though the benchmarks may not be originally designed for imitation learning, the corresponding metrics might be worth reference. Such evaluation can be adapted by measuring the mutual information or other metrics between the stylized code and the pair.

2. It remains not unclear, at least not generally convincing across datasets, that PMI shows a significant advance than the usual MI for BC. More evidence or discussion about this can be helpful to enhance the significance of the proposed method as PMI is claimed as a main contribution in this paper. If replacing MI with PMI can result in generalizable performance boosting across datasets, the proposed method can be supported with more experimental significance.

### Questions
Please see my comments in previous sectors.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Behavioral Cloning with Pointwise Mutual Information Weighting (BC-PMI), a new approach for recovering diverse policies in imitation learning. Here, the expert data consists of trajectories coming from different experts, each reflecting a unique approach or style within the task. The authors’ key idea is that, even within a single style, not all state-action pairs equally represent that style’s characteristics. To address this, BC-PMI weights state-action pairs based on their relevance to the style, calculated using pointwise mutual information between $(s,a)$ pairs and the style code $z$. These weighted pairs are then used to learn a style-conditioned policy $\pi(a|s,z)$ using behavioral cloning. This selective weighting allows the model to prioritize pairs that are most representative of the target behavior, thereby enhancing its ability to learn style-conditioned policies that more accurately capture the style within expert trajectories. 

The paper also provides some theoretical insights showing that BC-PMI smoothly interpolates between traditional behavioral cloning and clustering-based behavior cloning, depending on the mutual information between style and state-action pairs.

The authors evaluate BC-PMI in three settings: Circle 2D, a simple 2D setup; Atari Games (Alien, MsPacman, and Space Invaders); and the Professional Basketball Dataset, featuring NBA player movement data. Results show that BC-PMI achieves high style calibration across various metrics, outperforming baselines. However, it is worth noting that the baselines operate in an unsupervised manner and do not have access to the style labels available to BC-PMI.

### Strengths
1. The paper is well written and clearly communicates its key ideas.
2. The idea of selectively weighting state-action pairs based on their relevance to a given style, rather than treating entire trajectories uniformly, is both intuitive and impactful. Existing methods typically operate at the trajectory level, but this paper demonstrates that not all state-action pairs within a trajectory equally represent the intended style.

### Weaknesses
1. A key disadvantage of the method is that it requires style markers for each trajectory in the training dataset. These can be expensive to obtain. A brief note is made about using labeling functions to obtain these markers, but no experiments are included. This also makes the comparison with existing works unfair since they are unsupervised methods. To make the comparisons fair, the authors should include the supervision in other methods, e.g., they can train the posterior network in InfoGAIL using the style labels.

2. The experimental section is relatively brief, lacking analysis on the method’s performance as the number of styles increases or when labels are noisy. The latter case is quite important given that labels generated by programmable labeling functions (as mentioned in L296) may be imperfect. For a comprehensive understanding of these factors, it would be beneficial to include experiments that measure calibration as the number of styles increases, as well as tests assessing robustness to label noise introduced by such labeling functions.

### Questions
1. Why is MINE used to estimate the pointwise mutual information? This can be estimated by simply learning a classifier across different styles, since you are not interested in the $I(S,A;Z)$ rather $p(z|s,a)$. It would be valuable to compare the calibration performance of BC-PMI using a classifier-based approach against the current method with MINE’s statistic network, to assess if simpler alternatives might achieve similar results.
2. What are the calibration metrics used in Tables 3/4? Is it DTW, or ED, or KL?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates how to recover diverse policies from expert trajectories, proposing a new method that leverages the relevance of state-action pairs to trajectory styles. By introducing Pointwise Mutual Information to model this relationship, the method approaches the problem of policy diversity from a different perspective, ultimately achieving results that surpass previous state-of-the-art methods.

### Strengths
1. The motivation is simple but effective, and it will be highly beneficial for the efficient use of imitation learning data in subsequent robot tasks, contributing significantly to the development of the community.
2. The paper is well-written and easy to follow.
3. The experimental results are extensive and convincing.

### Weaknesses
1. I would like to know if there are other reweighting methods that can be used for comparison. If so, could some comparative experiments be included? Specifically, methods that reweight based on the discriminator's output or the policy's probability of the action could provide valuable baselines. It's important to understand how the proposed Pointwise Mutual Information (PMI) approach compares to these more established techniques in imitation learning.
2. Additionally, the current method evaluates the diversity of state-action pairs. As far as I understand, there are also studies specifically focused on state diversity and action diversity. I wonder if these could serve as a standard for comparison? For instance, how does the method's performance compare when evaluated using metrics that explicitly measure the coverage of the state space or the variety of actions taken, rather than a combined state-action diversity measure? It would be beneficial to see if the method excels in both state and action diversity or if it is more effective in one aspect over the other.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
4
