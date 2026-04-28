# Towards Control-Centric Representations in Reinforcement Learning from Images

- Decision: Reject
- Scores: 3, 8, 6, 5

## Abstract
Image-based Reinforcement Learning is a practical yet challenging task. A major hurdle lies in extracting control-centric representations while disregarding irrelevant information. While approaches that follow the bisimulation principle exhibit the potential in learning state representations to address this issue, they still grapple with the limited expressive capacity of latent dynamics and the inadaptability to sparse reward environments. To address these limitations, we introduce \modelname, which aims to capture control-centric information by integrating reward-free control information alongside reward-specific knowledge. \modelname~utilizes a transformer architecture to implicitly model the dynamics and incorporates block-wise masking to eliminate spatiotemporal redundancy. Moreover, \modelname~combines bisimulation-based loss with asymmetric reconstruction loss to prevent feature collapse in environments with sparse rewards. Empirical studies on two large benchmarks, including Atari games and DeepMind Control Suit, demonstrate that \modelname~has superior performance compared to existing methods, proving its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents ReBis, a new method for state representation learning in image-based RL, based on the bisimulation metric. It utilizes a transformer architecture with block-wise masking to capture dynamics and address issues inherent in environments with sparse rewards. The authors claim that ReBis prevents feature collapse where standard bisimulation metrics fail, showcasing performance gains on benchmark tasks such as Atari and DMC.

### Strengths
The paper makes a notable attempt to tackle the shortcomings of bisimulation metrics in sparse reward settings by integrating a transformer-based dynamics model. The adoption of block-wise masking as a strategy for sampling stochastic dynamics is an interesting approach. Empirically, the method appears to offer improvements over existing techniques, as demonstrated in the results section which features performance gains across Atari, DMC, and DMC with distraction.

### Weaknesses
The paper aims to address two challenges of bisimulation metrics: the reliance on Gaussian distribution for modeling and the issue of uninformative rewards. However, the justification for how the proposed ReBis method successfully overcomes these challenges remains unconvincing. The paper's method of using block-wise masking observation to simulate the sampling of stochastic dynamics is not fully explained. Various other techniques, such as random cropping as in DrQ, employing Dropout layers, or introducing noise to weights or latent features, could potentially serve a similar purpose. A detailed comparison of these methods within the experimental section would be beneficial for substantiating the need for block-wise masking.
Regarding the challenge of sparse rewards, the explanation of how ReBis overcome this issue is not adequately addressed. The paper should provide a clearer rationale for why its methods would be more effective in such environments.

The paper’s claim to novelty largely rests on the application of a transformer dynamics model, but this alone does not present a compelling case for novelty. The absence of a thorough comparative analysis, especially in the ablation studies, against non-transformer or non-sequential architectures, diminishes the strength of the argument for the proposed method’s innovation. Furthermore, the paper borrows heavily from prior work for various aspects, such as the masked observation approach, the metric used, and the theoretical framework, which detracts from the original contribution.

The theoretical foundation of the paper also shows weaknesses. 
1. The Definition 1 provided is mislabeled as "bisimulation-based" since it lacks the Wasserstein distance. It defines metric like MICo or SimSR but misses an expectation operator in front of $\bar{d}$. 
1. Theorem 2 and 3 for bisimulation metric, originated from (Kemertas & Aumentado-Armstrong, 2021), cannot be directly applied to the metric defined in the paper because their proofs rely on the Wasserstein distance, which is absent from the paper's metric. The authors need to develop new proofs that are pertinent to their specific metric definition.
1. Theorem 4 does not seem intuitive if the metric includes an expectation operator. (Castro et al., 2021) mentioned it is Łukaszyk–Karmowski distance with non-zero distance. The transition from Equation (15) to Equation (16) in the proof is unclear and requires further clarification.

### Questions
1. Could the authors clarify the term "multi-modals" within the paper?
1. In Tables 1 and 2, the blue color is not described. What does it represent in the context of these tables?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper deals with image-based reinforcement learning. Image-based RL requires the extraction of control-specific relevant information from the images while discarding the visual noise. The authors came up with a representation learning algorithm that uses the bisimulation metric to measure distances between states. Bisimulation suffers from issues such as possible collapse in sparse rewards and requiring dynamics modeling which the authors are able to alleviate. The produce competitive results on Atari and distracting dm control suite.

### Strengths
(1) They correctly identify the issues in using the bisimulation metric for quantifying the distances between states. They take measures to solve these.

(2) They use a transformer to implicitly learn the dynamics which improves the expressibility of the dynamics models.

(3) Their reconstruction objective ensures that the representations do not collapse even in a sparse rewards regime.

(4) They produce impressive results in the distracting dm control suite.

### Weaknesses
(1) Can this loss be used as a pretraining loss for learning an encoder? There should have been some experiment depicting this.

(1) The method of representation learning seems way more complex than the RL algorithm itself. If this is an auxiliary loss, the transformer model capturing the dynamics is never used by the RL algorithm which seems a waste of resources.

### Questions
(1) What if the distracting images in distracting dm control are added during training as well? Can the model get distracted then?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper builds on the idea of applying the bisimulation principle to shape the representation of deep RL with task-specific information. The authors first identify several limitations of prior work, for example, the expressiveness of the learned dynamics model and the ability to leverage reward-free control information when the reward is uninformative.

Then, the authors propose ReBis which leverages spatiotemporal consistency and long-term behavior similarity. More specifically, they reduce spatio-temporal redundancy in observations via Siamese encoders with block-wise masking and use a transformer-based dynamics model to capture multi-modal behaviors.

Finally, the authors demonstrate the superiority of ReBis on Atari and DeepMind control suites.

### Strengths
This paper compares with many prior works on learning a good representation for policy learning, including CURL, SimSR, etc., and shows their proposed method, ReBis, outperforms them in most tasks. Moreover, their learned representation is more robust to different backgrounds as demonstrated in the DeepMind control suite with different background distractions.

Experiments and ablations are comprehensive and well-designed. The ablation of different loss components justifies the design of ReBis and shows both reconstruction loss and bi-simulation loss contribute to the gain in ReBis.

The paper writing is easy to follow and has a nice overview of related work.

### Weaknesses
As pointed out by the author, the representation learning part adds non-trivial complexity to the RL algorithm. It would be interesting to experiment with different update frequencies of the representation learning part. For example, what’s the score if we update the representation encoder every 1, 10, 100, or 1000 environmental interactions?

Is the method complementary to other representation learning methods, such as augmentation, video prediction, time contrastive learning, etc? Does combining with other methods lead to better results?

The representation learning part relies on a reward specification by design, which prevents it from being used as a general pre-training method with unknown tasks. The authors should consider discussing this in limitations.

### Questions
Do we need to update the encoder every RL update? Can we update it less frequently than the policy?

Is the method complementary to other representation learning approaches?

Can we use it for pre-training a representation without task specification?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose to improve the bisimulation principle methods in terms of (1) better latent dynamics prediction; (2) handle sparse reward environments. The authors propose ReBis, which combine bisimulation loss with a masked transformer model to learn the latent forward dynamics and latent reconstruction loss can prevent collapse from uninformative rewards.

### Strengths
The motivation is clear. The paper identifies the drawbacks of the existing bisimulation methods, and proposes corresponding algorithms to handle them. In general, the writing is clear and the paper is easy to follow.

### Weaknesses
1. The novelty remains concerned. It seems that the algorithm combines MLR + a bisimulation loss.

2. The algorithm designs (using masked inputs, momentum encoder, etc.) need ablation studies to prove its effectiveness.

3. Though the motivation is to improve the bisimulation method, the proposed algorithm seems to be something between model-based RL (as cited in “Highly Expressive Dynamics Model” part). So I think it is necessary to discuss / compare with these works.

### Questions
1. I find some notations might need more clarification:

a) By stacking 3 frames for each observation (derive $o_t ‘$ from $o_t$), do you stack 3 frames $(o_t, o_t, o_t)$ with different masking, stack $(o_t, o_{t+1}, o_{t+2})$, or other setting?

b) Can you please explain the relative position embedding $\tau_K^p$ in detail? Do you add this position embedding to the state / action tokens, or concatenate this position embedding as an independent input?

c) As for the block masking, I think it will be better to introduce how the images are masked to make the paper self-contained.

2. What are the modifications on the proposed methods w.r.t. MLR besides the behavior loss (bisimulation part)? Most of the merits of the proposed methods (e.g., better forward dynamics, learn asymmetric reconstruction to handle uninformative reward) seems to come from the MLR backbone.

3. I’m also wondering why using the MLR as backbone to improve bisimulation and why not other methods (e.g., Dreamer, TransDreamer, Transformer world model) as cited in your related works.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
