# Exploring the Common Appearance-Boundary Adaptation for Nighttime Optical Flow

- Decision: Accept
- Scores: 6, 8, 1

## Abstract
We investigate a challenging task of nighttime optical flow, which suffers from weakened texture and amplified noise. These degradations weaken discriminative visual features, thus causing invalid motion feature matching. Typically, existing methods employ domain adaptation to transfer knowledge from auxiliary domain to nighttime domain in either input visual space or output motion space. However, this direct adaptation is ineffective, since there exists a large domain gap due to the intrinsic heterogeneous nature of the feature representations between auxiliary and nighttime domains. To overcome this issue, we explore a common-latent space as the intermediate bridge to reinforce the feature alignment between auxiliary and nighttime domains. In this work, we exploit two auxiliary daytime and event domains, and propose a novel common appearance-boundary adaptation framework for nighttime optical flow. In appearance adaptation, we employ the intrinsic image decomposition to embed the auxiliary daytime image and the nighttime image into a reflectance-aligned common space. We discover that motion distributions of the two reflectance maps are very similar, benefiting us to \emph{consistently} transfer motion appearance knowledge from daytime to nighttime domain. In boundary adaptation, we theoretically derive the motion correlation formula between nighttime image and accumulated events within a spatiotemporal gradient-aligned common space. We figure out that the correlation of the two spatiotemporal gradient maps shares significant discrepancy, benefitting us to \emph{contrastively} transfer boundary knowledge from event to nighttime domain. Moreover, appearance adaptation and boundary adaptation are complementary to each other, since they could jointly transfer global motion and local boundary knowledge to the nighttime domain. Extensive experiments have been performed to verify the superiority of the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel common appearance-boundary adaptation framework for nighttime optical flow estimation. The authors explore a common latent space as an intermediate bridge to reinforce feature alignment between auxiliary and nighttime domains. They construct two common spaces: a reflectance-aligned common space between daytime and nighttime domains, and a spatiotemporal gradient-aligned common space between nighttime frame and accumulated events. The appearance adaptation transfers global motion knowledge from daytime to nighttime domain, while the boundary adaptation transfers local motion boundary knowledge from event to nighttime domain. The proposed method, ABDA-Flow, achieves state-of-the-art performance for nighttime optical flow.

### Strengths
1. The common latent space approach effectively mitigates the distribution misalignment issue between source and target domains.
2. The appearance and boundary adaptations complement each other, jointly transferring global motion and local boundary knowledge to the nighttime domain.
3. The proposed method achieves state-of-the-art performance for nighttime optical flow estimation.

### Weaknesses
1. The method may be more complex to implement and train compared to simpler optical flow estimation techniques.
2. The effectiveness of the proposed method may be limited to specific nighttime optical flow tasks and datasets.
3. The runtime of the method may be slower than some other optical flow estimation techniques due to the Transformer architecture.

### Questions
1. How does the proposed common appearance-boundary adaptation framework compare to other domain adaptation techniques in terms of computational complexity and efficiency?
2. Can the proposed method be applied to other challenging optical flow estimation tasks, such as low-light or high-speed scenarios?
3. How does the proposed method handle the trade-off between model size and computational efficiency? Are there any plans to further optimize the runtime or explore other efficient optical flow estimation techniques?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper  focuses on the nighttime optical flow task, which is a challenging.  This paper  expolit two auxiliary daytime adn event domains, and present a common apperance-boundary adaption framework for nighttime optical flow. For apperance and boundary adaption, this paper have the new exploration, and both them are complementary to each other.  Extensive experiments  are conducted on various datasets, showing the SOTA performance.

### Strengths
1. This paper is well-presented, including the figures and tables.

2. The experiments are well-conducted, including  main comparsions, ablation studies and viual results. The method achieves the sota performance.

3. From the provided video demo, the proposed method genelizes well across many scenes.

### Weaknesses
It would be better to add some analyses on the failure cases and show the limitations of the method and give some discussions.

### Questions
Hope authors to release the codes to benefit the community on this field.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The study addresses nighttime optical flow, hampered by low texture and high noise. Traditional methods employ domain adaptation from auxiliary to nighttime domains but struggle due to domain gaps. To overcome this, the study introduces a common-latent space, using daytime and event domains. It shows motion appearance knowledge can be transferred effectively in reflectance-aligned spaces, and theoretical derivations emphasize substantial correlations between spatiotemporal gradients. Appearance and boundary adaptation are complementary and effectively transfer global motion and local boundary knowledge to nighttime domains, as validated by extensive experiments.

### Strengths
1) The paper is clearly written and easy to follow.
2) The novelty of this paper, in my opinion, is significant to the community. The concept of “common space adaptation” is very effective to reinforce feature alignment between domains, and it has great potentials to be applied for any degraded scene understanding tasks. 
3) The constructed common spaces are from both appearance (reflectance) and boundary (gradient) sides. They are complementary and sound reasonable for the performance improvement.

### Weaknesses
While the proposed method appears promising, the complexity of the loss function involving seven balance weights raises concerns. Identifying the appropriate values for these seven weights efficiently is a challenge. Performing a grid search to determine these values might be time-consuming and resource-intensive.

### Questions
Please refer to the weakness part.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
