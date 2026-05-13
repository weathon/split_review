# Diverse Offline Imitation Learning

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
There has been significant recent progress in the area of unsupervised skill discovery, utilizing various information-theoretic objectives as measures of diversity. Despite these advances, challenges remain: current methods require significant online interaction, fail to leverage vast amounts of available task-agnostic data and typically lack a quantitative measure of skill utility. We address these challenges by proposing a principled offline algorithm for unsupervised skill discovery that, in addition to maximizing diversity, ensures that each learned skill imitates state-only expert demonstrations to a certain degree. Our main analytical contribution is to connect Fenchel duality, reinforcement learning, and unsupervised skill discovery to maximize a mutual information objective subject to KL-divergence state occupancy constraints. Furthermore, we demonstrate the effectiveness of our method on the standard offline benchmark D4RL and on a custom offline dataset collected from a 12-DoF quadruped robot for which the policies trained in simulation transfer well to the real robotic system.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel algorithm to connect Fenchel duality, reinforcement learning, and unsupervised skill discovery to maximize a mutual information objective subject to KL-divergence state occupancy constraints. This approach is used to diversify offline policies for a 12-DoF quadruped robot and several environments from the standard D4RL benchmark in terms of both ℓ2 distance of expected successor features and ℓ1 distance of importance ratios.

### Strengths
The strength of this paper is that it proposes a principled offline algorithm for unsupervised skill discovery that maximizes diversity while ensuring each learned skill imitates state-only expert demonstrations to a certain degree. In order to compute the optimal solution to the problem formulation, the authors propose to use an approximation algorithm "alternative optomization". The authors demonstrate the effectiveness of the method on standard offline benchmarks and a custom offline dataset collected from a quadruped robot. The resulting skill diversity naturally entails a trade-off in task performance, which can be controlled via a KL constraint level ϵ.

### Weaknesses
1. In the experiment section, it will be good to see some comparison between the proposed method with other state-of-the-art methods for unsupervised skill discovery. 
2. Computational complexity of the proposed algorithm is not mentioned in the paper. 
3. The paper does not provide a comprehensive evaluation of the proposed method on a wide range of tasks and environments.

### Questions
Is there a convergence analysis of the algorithm? What if the algorithm does not converge?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the question of learning diverse skills from offline dataset while being close to expert. The objective is formulated and existing ideas are used to solve the combined objective effectively. The resulting method is tested on offline datasets from D4RL and a real robot to demonstrate the diversity induced by their method.

### Strengths
1. The paper presents a new objective for unsupervised skill learning from offline datasets - maximize mutual information combined with staying close to expert. To facilitate this, the method leverages algorithms from previous works that are off-policy in nature. To solve the mutual information objective they use the variational lower bound previously seen in DIAYN, to optimize the KL-constraint they use DICE method and for optimizing objective and constraint jointly the lagrangian method is used, commonly seen in safe RL literature. The combination results in a new off-policy skill discovery method.
2.  The paper empirically demonstrates effectiveness of their method on simulated tasks on D4RL by comparing metrics for diversity using the offline dataset. They show the tradeoff of contraint vs diversity and the expected difference of importance ratio.
3. The paper also test the algorithm on a real quaduped which learns gaits with various heights.

### Weaknesses
1. The paper misses to explain the motivation behind proposing the objective:

Why stay close to expert? If the objective is to generate diverse skill, what is the objective of incoporating the constraint of staying close to expert. An explanation through examples might help to motivate the paper better.
KL divergence to expert: Any objective that uses KL divergence is extremely sensitive if the learned skill goes out of support of the expert dataset. It is motivated in the paper the skill should imitate some part of expert but this is not what is enforced by the KL divergence. The KL divergence will penalize any deviation from the expert's distribution, even if that deviation leads to a valid and diverse skill, which is counter to the stated goal of skill discovery. This is especially problematic in offline settings where the expert data may not cover the full range of possible states and actions.

2. Theoretical contributions: I believe the lemma’s are minor variations over previous works in DICE space [1,2,3,4] which might be discussed and compared to more thoroughly. 
3. Evaluation:
    1. Online evaluation: The paper currently only plots metrics on offline dataset. I believe this is not the correct metric. A learned visitation distribution might not be practically feasible although theoretically it should be. One way to test it in simulated domains, is to roll out pi_z for different skills and compare the resulting visitation distribution. The current evaluation does not demonstrate the practical utility of the learned skills in a deployed setting. The offline metrics might not correlate well with the actual performance of the learned skills when executed in the environment.
    2. Qualitative Diversity of skill: An important part of the evaluation process should be a qualitative comparison of the skills the algorithm learns. If the algorithm learn meaningless skills it would be clear from the deployed policy. The paper lacks a detailed analysis of the actual behaviors exhibited by the learned skills. Simply showing a diversity metric is not sufficient to demonstrate that the skills are meaningful and useful.
    3. Baselines and Quantitative diversity of skill: No prior methods for skill discovery are compared against. A standard comparison might be the resulting estimated mutual information of skills between prior methods and DOI. Although prior methods are not developed for offline setting, a simple extension would be to pair them with offline RL. Example: DIAYN could be combined with IQL instead of SAC.

### Questions
1. In the paragraph after Figure 3, How does skill conditioned variant of SMODICE does not have a discriminator?  SMODICE itself learns a discriminator in the original method which estimates ratio of expert to offline data. Do you mean the skill discriminator? 
2. I am not sure how to compute the expectation of importance ratio for different skills. Is the expectation over the offline dataset?
3. For SOLO12, the data is already generated by a skill-based algorithm which seems their is a strong prior to recovering the same skills as the original algorithm? Can you ablate how the learned skills are different from skills found by Domino?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces DOI (Diverse Offline Imitation) for improving diversity of learned skill-conditioned policies. These skills are trained to have maximum diversity (via maximizing mutual information between states and skills) and to be close to expert state distributions. Prior work, SMODICE, is an instance of DOI where the KL-divergence between each skill state-visitation distribution and the expert state-visitation distribution must be 0, but DOI relaxes this constraint to be up to $\varepsilon$.

DOI is evaluated on a 12-DOF quadruped both in sim and real as well as in D4RL and shown to promote greater diversity of skills. However, there is a tradeoff between skill diversity and performance.

### Strengths
- Method was deployed on a real robot, and website has videos showing the learning of presumably 3 different skills involving locomotion at 3 different base heights.
- Figure 1 was helpful.
- Writing in the main text sections of the paper was mostly clear, and the math was pretty understandable step-by-step.

### Weaknesses
## Method, Experiments, and Argument

(A1) Novelty and algorithmic contribution seems quite limited compared to SMODICE. The main differences are (1) Learning a discrete number of skill-based policies instead of a single policy, and (2) allowing skill-based policies and the expert to have up-to-$\\varepsilon$ KL divergence. While the relaxation of the KL divergence constraint to $\\varepsilon$ is a novel aspect, it is presented as an incremental change. The paper would benefit from a more thorough discussion on how this relaxation fundamentally alters the optimization landscape or enables qualitatively different skill discovery compared to the strict constraint in SMODICE. Limited algorithmic novelty is fine if robotic performance on at least a few downstream tasks is a lot better than prior work, but experiments show ultimate performance is not improved with DOI.

(A2) Experimental metrics are not very illustrative of the performance of DOI. Most of the plots (Figure 3, 4a) show proxy measures of how diverse the skills are. Only Figure 4b (and Tables S2, S3) compares DOI performance with SMODICE. Figure 4b shows that performance of DOI at smaller epsilon values is comparable to SMODICE, and Tables S2 and S3 show that SMODICE ($\varepsilon = 0$) does better than any $\varepsilon > 0$. Perhaps this is expected, as the authors argued there is a diversity-performance tradeoff in Section 6. But if so, there should be experiments, such as those testing generalization, where higher skill diversity leads to better robustness than narrowly-learned policies. For instance, an experiment could be designed where the agent trained with DOI is tested in environments with perturbations or obstacles that require a diverse skill set to navigate. The absence of such experiments, which would demonstrate the practical advantages of enhanced skill diversity, raises questions about the conditions under which DOI offers a tangible improvement over SMODICE.

(A3) Abstract and conclusion states that this paper proposes “a principled offline algorithm for unsupervised skill discovery.” However, the paper assumes that the set of skills $Z$ is finite, which suggests that skill candidates are predefined and presumably not continuous-spaced. If predefined, where is the “skill discovery” coming from? The term "skill discovery" implies learning or identifying skills from data, yet the skills appear to be predetermined in this framework. This is different from how CIC [1] does skill discovery, where skill vectors are continuous and sampled from a prior distribution. A clearer definition of what constitutes skill discovery in the context of DOI is needed.


## Presentation/Coherence

Overall, results graphs and algorithm boxes need to be clearer.

(B1) Paper did not precisely define what a skill is, what the set of finite skills $Z$ is initialized to, or where $Z$ is from. Is $z \in Z$ a continuous vector or a one-hot? The lack of clarity on the nature of the skill space and its initialization makes it difficult to fully understand the method's setup and reproduce the results.

(B2) Since method section relies so much on SMODICE, and Figure 2 refers to DICE (which was not introduced until page 7), I would recommend putting the related work section before the preliminaries section.

(B3) Nitpick: Section 3.2.1, first line, should refer to Problem (eqn 7) instead of Problem (eqn 6), I believe.

(B4) Algorithm 1 talks about a discriminator $c^{*}$ mapping state to predicted probability that the state is from $d_E$ vs $d_O$. However, this discriminator is not mentioned anywhere in the main text and can be confused with the skill discriminator $q(z|s)$.

(B5) Phase 2 in Algorithm 1 mentions training $\pi_z^{*}$ when Section 3.2.1 seems to say the policy is trained in Phase 1 instead. This discrepancy creates confusion about the order of operations in the algorithm.

(B6) Section 5, Related Work, reads more like a laundry list of prior papers. There is no comparison at all to this paper’s proposed method, DOI. A more comparative analysis, highlighting the differences and similarities between DOI and related methods, would be beneficial.

(B7) Real robot results are not discussed in Section 6. While the paper mentions deployment on a real robot, the lack of detailed discussion on these results in the main experimental section is a significant omission.

(B8) Tables S2 (Walker2D) and S3 (HalfCheetah) contain the exact same entries (at least for the ~20 cells I looked at). This seems like an unfortunate mistake.

## Reference
[1] CIC: Contrastive Intrinsic Control for Unsupervised Skill Discovery. Laskin et al.

### Questions
1. How would DOI be extendable to a continuous skill space?

2. How did authors define the skill space $Z$ for each of the different environments? What was $Z$ and $|Z|$ for the D4RL envs? Presumably it was $|Z| = 3$ and $Z = [\text{low base}, \text{mid base}, \text{high base}]$ for locomotion?

3. Given Assumption 2.1, I wonder what the state representation is for the locomotion task. Can DOI be adapted to work on image observations, or a learned image feature space?

4. What is $N$ in Tables S2 and S3?

5. What does the color-coding in Figure 3a mean? Is it the same color meaning as Figure 3b?

6. In Algorithm 1, the reward is defined as function of the output of $c^{*}$, which could easily be confused with the reward terms mentioned in Equations 8 and 14. How is this reward term, which doesn’t depend on actions, used to compute importance sampling ratios $\eta_{\tilde{E}}(s,a)$, which does?

7. Figure 3a: x-axis is confusingly labeled “data.” Section 6 describes this as “across the dataset assignment.” What do these things mean?

8. I suggest using a slightly more descriptive title for the paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
