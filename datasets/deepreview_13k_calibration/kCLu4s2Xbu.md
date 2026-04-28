# Trajectory-level Data Generation with Better Alignment for Offline Imitation Learning

- Decision: Reject
- Avg Score: 3.60
- Scores: 1, 3, 6, 3, 5

## Abstract
Offline reinforcement learning (RL) relies heavily on densely precise reward signals, which are labor-intensive and challenging to obtain in many real-world scenarios. To tackle this challenge, offline imitation learning (IL) extracts optimal policies from expert demonstrations and datasets without reward labels. However, the scarcity of expert data and the abundance of suboptimal trajectories within the dataset impede the application of supervised learning methods like behavior cloning (BC). While previous research has focused on learning importance weights for BC or reward functions to integrate with offline RL algorithms, these approaches often result in suboptimal policy performance due to training instabilities and inaccuracies in learned weights or rewards. To address this problem, we introduce Trajectory-level Data Generation with Better Alignment (TDGBA), an algorithm that leverages alignment measures between unlabeled trajectories and expert demonstrations to guide a diffusion model in generating highly aligned trajectories. The aforementioned trajectories allow for the direct application of BC in order to extract optimal policies, negating the necessity for weight or reward learning. In particular, we define implicit expert preferences and, without the necessity of an additional human preference dataset, effectively utilise expert demonstrations to identify the preferences of unlabeled trajectories. Experimental results on the D4RL benchmarks demonstrate that TDGBA significantly outperforms state-of-the-art BC-based IL methods. Furthermore, we illustrate the efficacy of implicit expert preferences, which represents the inaugural application of the benefits of preference learning to offline IL.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes a method called Trajectory-level Data Generation with Better Alignment (TDGBA)  for offline imitation learning (IL). TDGBA leverages alignment measures between unlabeled trajectories and expert demonstrations to guide a diffusion model in generating highly aligned trajectories, which are then used for better behavior cloning. Experimental results on the D4RL demonstrate that TDGBA outperforms SOTA IL methods.

### Strengths
N/A

### Weaknesses
I have sufficient reason to believe that this paper has plagiarized another paper [1] (called flow-to-better (FTB)) in both its method and writing. I will explain this in detail:

**Method:**

The method proposed in this paper, TDGBA, first uses an alignment measurement method to score the trajectories in the dataset, then applies a clustering method to divide all trajectories into several blocks. Next, two trajectories from two neighboring blocks are sampled, respectively labeled as high-alignment and low-alignment trajectories, and these are provided to a diffusion model for learning. Finally, the learned diffusion model is used to generate several high-alignment trajectories as augmented data for imitation learning. This entire process is identical to the FTB method, except that in FTB, human preferences are used as the measurement in the first step, whereas TDGBA proposes its own alignment measurement. However, the paper completely avoids discussing these similarities, only mentioning “Drawing inspiration from previous works...” in Section 3.2.

**Writing:**

The overall structure of the paper is also highly similar to the FTB paper. For example, Section 3.2 is very similar to Section 3.1 in FTB. The experimental sections 4.2 and 4.3 are also similar to sections 4.2 and 4.3 in FTB, and the discussion of generative models in the related work section also closely resembles that of FTB.

In summary, while TDGBA and FTB are methods proposed in different fields—one in offline imitation learning and the other in offline preference-based RL—their method structure, details, and even parts of the writing are very similar. Therefore, I have reason to suspect that this paper may have plagiarized from FTB.

### Questions
I have no further questions because this paper is suspected of plagiarism.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a novel offline imitation learning method, Trajectory-level Data Generation with Better Alignment (TDGBA), designed to optimize policy learning when both expert and unlabeled datasets are available. TDGBA leverages the Wasserstein Distance to measure alignment between unlabeled and expert trajectories, constructing preference pairs from the initially unlabeled dataset. A trajectory diffusion model is then trained to generate higher-aligned trajectories conditioned on lower-aligned ones, progressively enhancing the top-aligned trajectories. The behavior cloning (BC) policy trained on this improved dataset demonstrates significant improvement over baseline algorithms, particularly in mixed-quality datasets such as medium-expert and medium-replay.

### Strengths
1. TDGBA uses implicit preference labeling to guide trajectory generation, enhancing the quality of generated trajectories without requiring additional human labels or preference datasets.

2. TDGBA avoids the complexities and computational costs associated with reward learning in offline settings, simplifying the imitation learning process.

3. Experimental results show that TDGBA outperforms state-of-the-art offline IL methods, especially in mixed-quality datasets like medium-expert and medium-replay.

### Weaknesses
1. Some critical algorithm designs lack sufficient and reasonable explanations. 1) Why are low-preference trajectories used as conditions of the classifier-free guidance, and how about directly using labeled preference values as generation conditions? This choice is not well-justified, and it's unclear if this is the optimal approach. The paper should explore the impact of using preference values directly as conditions, as this could potentially offer more fine-grained control over the generation process. 2) According to Algorithm 1, the expert demonstrations were not used as training data for BC policy. What is the reason for this choice? The exclusion of expert demonstrations from the BC training set is a significant design decision that requires more detailed explanation, especially given that these trajectories are considered to be of high quality. It is unclear why the authors chose to rely solely on the generated trajectories for training the BC policy, and this could be a potential limitation of the approach.

2. Some important technical details are missing on the paper. As the authors did not provide their code implementation, reproducing the results could be challenging. Specifically, what is the length of the trajectories generated by the diffusion model? If it corresponds to the length of an episode, e.g., 1000 steps in MuJoCo, would this make the model’s inference cost very high? The paper lacks a discussion on the computational cost associated with generating long trajectories, which is a critical factor for practical applications. Also, the authors did not mention the model architecture of the diffusion model. Even though the downsample rate in the parameter table suggests it might be a U-Net, the authors did not explicitly clarify this in the paper. The lack of clarity regarding the diffusion model's architecture makes it difficult to assess the complexity and potential limitations of the approach.

3. (minor issues) In Table 6, the "Top trajectories number" is reported as 300, but in Table 7, it varies by environment. Line 47 is missing a space before the left parenthesis, line 197 is missing a closing parenthesis, “confirme” on line 268 should be corrected to "confirm", and a space is missing after the closing parenthesis on line 318.

### Questions
1. In line 3 of Algorithm 1, how did the authors select the expert demonstration trajectory to pair with each unlabeled trajectory? If the selection was random, could this pairing approach create issues in environments where the initial state varies significantly, as the optimal trajectory distribution may differ widely depending on the initial state?

2. Since the diffusion model is applied solely to improve the top trajectories, is it necessary to train on all neighbor blocks? For instance, training the model to generate $B_2$ from $B_1$ might be unnecessary.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Offline reinforcement learning depends on precise reward signals, which are difficult to obtain. Offline imitation learning (IL) seeks to develop policies from expert demonstrations without rewards, but is limited by scarce expert data and numerous suboptimal trajectories, affecting methods like behavior cloning (BC). Traditional approaches using importance weights or reward functions for BC encounter instability and accuracy issues. To address this, we introduce Trajectory-level Data Generation with Better Alignment (TDGBA). This method aligns unlabeled trajectories with expert demonstrations to guide a diffusion model in generating well-aligned trajectories, enabling BC to extract optimal policies directly. It also uses implicit expert preferences to improve stability, fidelity, and diversity. Experiments on D4RL benchmarks demonstrate TDGBA's superior performance over other offline IL methods, confirming the effectiveness of diffusion models and expert preferences in trajectory data generation.

### Strengths
well-written and clear

well-motivated

extensive comparisons and evaluations in experiments

### Weaknesses
The grammar and presentation of some paragraphs need to be improved.

The visualization of the experimental results needs to be improved slightly.

line 212, why using lower-alignment trajectories as the condition？

In Section 4.3, the visualization results were only presented on the hopper-medium-replay-v2 task, which left the reader somewhat confused and curious. How about the results on other tasks?

### Questions
line 212, why using lower-alignment trajectories as the condition？

In Section 4.3, the visualization results were only presented on the hopper-medium-replay-v2 task, which left the reader somewhat confused and curious. How about the results on other tasks?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
1

### Summary
This paper proposes a simple yet effective trajectory alignment approach that combines a W1-distance-based trajectory ranking method with the use of a diffusion policy. This approach demonstrates improved performance in the imitation learning (IL) domain, specifically within Gym-Mujoco.

Additionally, the authors provide extensive analytical experiments and analysis, which illustrate the limitations of previous methods' reward shaping. These experimental results are crucial for understanding the performance of current reward-shaping algorithms.

However, the extent to which improvements result from algorithm innovation rather than model architecture still needs further verification.

### Strengths
This paper proposes a simple yet effective trajectory alignment approach that combines a W1-distance-based trajectory ranking method with a diffusion policy. It demonstrates improved performance in imitation learning (IL) tasks sourced from the Gym-Mujoco domain.

Additionally, the authors conducted extensive analytical experiments and analyses, which highlight the limitations of previous reward shaping methods. These experimental results are essential in helping us understand the constraints of current reward shaping-based IL algorithms.

### Weaknesses
See Question Section

### Questions
**Q.1** How much improvement is brought by your trajectories ranking and sorted out? since the performance of Diffusion policy is considerate enoughy, especially in the long horizonal setting. Meanwhile, most of your baselines chosen are based on MLP policies.

**Q.2**  From your experimental results, I observe that most of your setups focus on continuous control tasks, while there is a lack of long-horizon decision-making tasks. Could you please provide more comparisons across these related domains (such as kitchen, android, etc.)? Thank you.

**Q.3** Could you clarify the advantages of your paper over other alignment and sequential modeling approaches? For instance, the paper [1] utilizes contextualized information to align demonstrations, showcasing improved performance on IL tasks. I also have a question about your **diffusion policy's optimizing objective**.

Specifically, we know diffusion policy can be optimized via ODE or SDE based method. ODE objective includes consistency model e.g.  and SDE methods encompass numerous related researches. Most of those methods optimize models via adding noising to the initial feature till uniform distribution followed by recovering the feature or predicting the added noise. Therefore, I am very confused about your diffusion objective. Why its a maximizing likelihood objective?

If you ignore your objective, I think it's not diffusion policy, I prefer naming it U-NET? Meanwhile, I can provide some method for you to check whether its diffusion policy:

- Render and observe, whether your policy can learn multiple modes. For example, given a state, there are several clusters.
- check your codebase, and observe, whether you just don't correctly write the objective.

I won't directly reject this paper, since your contribution is independent with diffusion policy. I am looking forward to any improvements or corrections.

Reference
[1] Z. Zhang, J. Xu, J. Liu, Z. Zhuang, D. Wang, M. Liu, S. Zhang, Context-Former: Stitching via Latent Conditioned Sequence Modeling

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
It introduces Trajectory-level Data Generation with Better Alignment (TDGBA), which addresses the challenges of scarce expert data and suboptimal trajectories by using a diffusion model guided by alignment measures between unlabeled trajectories and expert demonstrations. The method employs an alignment metric based on optimal transport theory and Wasserstein distance, which is used as an implicit expert preference to train the diffusion model. This approach generates high-quality, diverse trajectories that enable the direct application of Behavior Cloning methods to derive optimal policies, outperforming state-of-the-art offline IL methods on D4RL benchmarks⁠.

### Strengths
This paper introduces a metric using Wasserstein distance to measure the alignment between unlabeled trajectories and expert demonstrations.

### Weaknesses
The conditional diffusion model conditioned on inferior data to generate better data is derived from previous work [1]. Therefore, it is essentially an adaptation to the offline imitation setting.

The defined metric has some practical limitations. Perfect demonstrations may be scarce, and the policy might be multi-modal, making it challenging to formally define the distance. However, practical methods to measure differences, such as training a discriminator, have been proposed in previous work [2]. Thus, the contribution of this work appears limited. Specifically, the paper does not address the potential for the Wasserstein distance to become unreliable when comparing trajectories that are significantly different in length or have vastly different state distributions. Furthermore, the method's reliance on a single expert trajectory as a reference point may not be robust, especially in environments with complex, multi-modal optimal policies. The paper also lacks a thorough analysis of how the quality and diversity of the generated trajectories are affected by the choice of the diffusion model's hyperparameters and the number of unlabeled trajectories used for alignment.

### Questions
Can you visualize the improved generated data? Given that the original conditional diffusion might rely on a large number of human labels, does the expert-demonstration-shaped preference satisfy the data requirements? Ablation studies on the number of preference labels and trajectories are also needed.

### Soundness
2

### Presentation
3

### Contribution
2
