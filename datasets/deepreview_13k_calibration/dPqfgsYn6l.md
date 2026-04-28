# Active Gaze Behavior Boosts Self-Supervised Object Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Due to significant variations in the projection of the same object from different viewpoints, machine learning algorithms struggle to recognize the same object across various perspectives. In contrast, toddlers quickly learn to recognize objects from different viewpoints with almost no supervision. Recent works argue that toddlers develop this ability by mapping close-in-time visual inputs to similar representations while interacting with objects. High acuity vision is only available in the central visual field, which may explain why toddlers (much like adults) constantly move their gaze around during such interactions. It is unclear whether/how much toddlers curate their visual experience through these eye movements to support learning object representations. In this work, we explore whether a bio-inspired visual learning model can harness toddlers’ gaze behavior during a play session to develop view-invariant object recognition. Exploiting head-mounted eye tracking during dyadic play, we simulate toddlers’ central visual field experience by cropping image regions centered on the gaze location. This visual stream feeds a time-based self-supervised learning algorithm. Our experiments demonstrate that toddlers’ gaze strategy supports the learning of invariant object representations. Our analysis also reveals that the limited size of the central visual field where acuity is high is crucial for this. We further find that toddlers’ visual experience elicits more robust representations compared to adults’ mostly because toddlers look at objects they hold themselves for longer bouts. Overall, our work reveals how toddlers’ gaze behavior supports self-supervised learning of view-invariant object recognition.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript starts by stating that toddlers are quick in learning view-invariant object recognition. In particular, the writing implies that toddlers are more efficient learners compared to existing self-supervised learning methods. The authors identify that the eye tracking data of toddlers can provide a semantically stable video dataset, which can be exploited by learning time-wise consistencies when coupled with appropriate cropping. They define 3 cropping strategies: gaze-based, random, centroid (reflecting head orientation), as well as 2 oracle methods (objects-focused and so-called “plain background”) then train a self-supervised-through-time method (SimCLR-TT), then perform linear evaluation (keep the ResNet-18 fixed, train 1 classifier layer). They show that when training on data curated using toddlers’ gaze, performance can get close to that of a model trained on objects-focused oracle data. Their ablation study shows that a field-of-view (crop size) of 128x128 is best, and that toddlers hold their gaze steady (shown by trying different time steps in training SimCLR-TT) compared to adults.

### Strengths
The paper is interesting to read, well-written in general, and can be followed reasonably easily. The manuscript poses the question regarding understanding view-invariant object recognition learning, then tackles it methodically by proposing pre-processing steps on the Bambach et al. 2018 dataset and designing several experiments based on it.

The experiments seem to affirm the authors’ assumptions in that:
- toddlers gaze differently at objects, compared to adults, especially in terms of how long they gaze at the objects that they are holding in their hands.
- eye gaze signals can be used for a type of self-supervised learning, thanks to the tendency for both toddlers and adults to look at the same object, over a few time steps.

### Weaknesses
A core thesis of this paper seems to be that existing SSL approaches could learn better. The first sentence of the conclusion says: “Current SSL approaches still struggle to learn robust human-like object representations and the reasons for this remain unclear.” - however, this is never backed by evidence neither in the related work nor in the experiments. It may seem that the authors pose this paper as a first step towards curating a large-scale toddler-driven dataset that would improve upon typical self-supervised learning datasets such as ImageNet-1K or JFT-300M, but this is hard to agree with. It would help if the authors provide specific evidence or citations supporting their claim about the limitations of current SSL approaches in learning human-like object representations.

Furthermore, the paper puts a lot of effort into differentiating between the behavior of toddlers and adults. Some observations are intuitive (toddlers fixate longer at the objects that they hold in their hands), but others are less so (no real difference in SSL results in Figure 4). I can see the value of this paper as a behavioral science paper - one that uses machine learning to show how toddlers may learn view-invariant object recognition. This is because many results seem to be revealing toddlers’ behavioral patterns rather than contributing to improving machine learning. Could the authors please clarify what the primary contribution of their paper is? Is the paper intended to advance machine learning techniques, or is it primarily a study of toddler behavior using machine learning as a tool?

### Questions
- Are you the first to apply SimCLR-TT (or another self-supervised learning through time work) to toddler videos? What about works like [1]?
- Did you consider evaluating several SSL methods such as done in [2]? What was the reason for using a SimCLR-based method? Many SSL methods have been introduced since 2020 (e.g. BYOL, SimSiam, DINO, MAE) and many of them can be easily adapted to the SSL-through-time setting.
- In FIgure 1, why are the examples in E and F of an object that does not exist in the egocentric video? This confuses me somewhat, because I assumed B-E are all different ways of cropping the original A.

[1] Aubret, Arthur, Céline Teulièr, and Jochen Triesch. "Toddler-inspired embodied vision for learning object representations." 2022 IEEE International Conference on Development and Learning (ICDL). IEEE, 2022.

[2] Pandey, Lalit, Samantha Wood, and Justin Wood. "Are vision transformers more data hungry than newborn visual systems?." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
2

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
The paper investigates the adoption of a bio-inspired model of visual learning based on the visual experience of toddlers (compared to adults) captured thanks to the use of an eye-tracker. The hypothesis is that data collected from toddlers from a first-person perspective can improve the robustness of object representations, in particular in the presence of data collected from multiple views. 
The authors assess their method on a dataset of head-camera recordings and gaze tracking from toddlers and adults during play sessions.

### Strengths
- The paper considers an inspiring scientific question, at the crossroads between different disciplines, and as such it may be of interest for a multi-disciplinary community
- The work is well-motivated and contextualised concerning the existing literature

### Weaknesses
 - Besides the scientific question, which I find very interesting indeed, it's not clear to me what would be the use and the impact of this analysis. What are the practical scenarios where these results can be exploited? How the empirical observations that you are making can be turned into actionable insights? For instance, can the insights be turned into suggestions on the way datasets for object recognition should be collected?
- The authors gather strong conclusions from their experiments. However, in my opinion, the provided experiments are not enough to speak in favour of the generality of the outcomes (see Questions)

- The contributions should be clearly stated in the introduction, to fully unveil the intentions of the authors. For instance, are the datasets a contribution? Will you share the data with the community?

- About the datasets: (1) Can you please explain more clearly the motivations behind the centroid fixation dataset? How can you be sure that an object is always present in the selected image portion? (2) You only provided the size of one dataset only, what about the others? (3) About the random dataset: how can you be sure that an object is present in the selected image regions? (4) How different toddler and adult datasets are? (5) What about the variability and complexity of objects? How a state-of-art object recognition method would perform on the datasets?

- Row 304: “…temporally adjacent image xt+∆T at time  t+∆T “. If this is the case, Delta t should be related to the video frame rate. In my opinion, a clearer formulation would consider t and t+1 instead, a more commonly adopted convention with videos. If I misunderstood, the motivations behind the choice of Delta t to be 1/30 should be given.

- Eq 1, unclear. If k is different from t, it would still be equal to t+Delta, which would contribute to both the numerator and denominator. Please clarify

- “We also observe that the gap between the Toddler fixation dataset and other datasets built with the ground truth about objects’ identities is small. We see a similar trend with the adult datasets. This suggests that a biologically inspired visual learning model like SimCLR-TT can leverage human gaze behaviours to build better visual representations. “ I miss the intuition behind this observation

- I find Fig. 4 a bit ambiguous. It may be useful to add details to favour the comprehension, e.g. what the colours refer to. 

- If I’m correctly interpreting Figure 4, it seems to me that the difference between using toddlers and adults data is very little. How do you explain this fact?

- What’s the expected generalization of these observations? For instance: all the experiments are based on a fixed backbone, the ResNet18. What could be the impact of changing the representation?

- The conclusions in Sec, 4.2 are not surprising. If images are cropped so that the object is at the centre and with less background the recognition improves. This seems to be more a sanity check than a useful insight.

### Questions
- The contributions should be clearly stated in the introduction, to fully unveil the intentions of the authors. For instance, are the datasets a contribution? Will you share the data with the community?

- About the datasets: (1) Can you please explain more clearly the motivations behind the centroid fixation dataset? How can you be sure that an object is always present in the selected image portion? (2) You only provided the size of one dataset only, what about the others? (3) About the random dataset: how can you be sure that an object is present in the selected image regions? (4) How different toddler and adult datasets are? (5) What about the variability and complexity of objects? How a state-of-art object recognition method would perform on the datasets?

- Row 304: “…temporally adjacent image xt+∆T at time  t+∆T “. If this is the case, Delta t should be related to the video frame rate. In my opinion, a clearer formulation would consider t and t+1 instead, a more commonly adopted convention with videos. If I misunderstood, the motivations behind the choice of Delta t to be 1/30 should be given.

- Eq 1, unclear. If k is different from t, it would still be equal to t+Delta, which would contribute to both the numerator and denominator. Please clarify

- “We also observe that the gap between the Toddler fixation dataset and other datasets built with the ground truth about objects’ identities is small. We see a similar trend with the adult datasets. This suggests that a biologically inspired visual learning model like SimCLR-TT can leverage human gaze behaviours to build better visual representations. “ I miss the intuition behind this observation

- I find Fig. 4 a bit ambiguous. It may be useful to add details to favour the comprehension, e.g. what the colours refer to. 

- If I’m correctly interpreting Figure 4, it seems to me that the difference between using toddlers and adults data is very little. How do you explain this fact?

- What’s the expected generalization of these observations? For instance: all the experiments are based on a fixed backbone, the ResNet18. What could be the impact of changing the representation?

- The conclusions in Sec, 4.2 are not surprising. If images are cropped so that the object is at the centre and with less background the recognition improves. This seems to be more a sanity check than a useful insight.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This workexamines how toddlers’ gaze helps self-supervised models learn view-invariant object recognition. Using eye-tracking data from toddler play sessions, the authors simulate a limited central vision experience and apply a time-based learning algorithm, SimCLR-TT. Results show that toddlers’ gaze patterns enhance object recognition better than random or adult gaze. Key contributions of this work include insights into how toddlers’ gaze supports learning and how such strategies could benefit ML models.

### Strengths
Originality: The paper introduces a unique, biologically inspired approach to SSL by modeling toddler gaze behavior to improve view-invariant object recognition. Rather than focusing on synthetic or curated datasets, the authors use eye-tracking data to simulate central vision dynamics in real-life toddler play sessions. This approach is a creative blend of insights from developmental psychology and machine learning, making it an original contribution.

Quality: The paper presents a thorough experimental design, comparing toddler and adult gaze strategies and establishing baselines (e.g., random and centroid fixation). The choice of the SimCLR-TT model, combined with a carefully curated dataset, shows a clear effort to test hypotheses in a controlled yet realistic setting. The analysis also includes multiple measures to validate that toddler gaze uniquely supports learning. These methodological choices enhance the paper’s quality and reinforce its claims.

Clarity: The paper is generally clear, with a well-structured explanation of the motivations behind gaze-centered learning and the potential benefits for SSL models. Concepts are explained effectively, with sufficient background to understand why toddler gaze was chosen as the focus. 

Significance: This work has significant implications for both ML and developmental science. The study also contributes to understanding human learning processes, suggesting that toddler gaze behavior naturally supports efficient learning. This could inspire further interdisciplinary work and innovations in adaptive vision systems.

### Weaknesses
 - The model is tested on a controlled dataset with limited objects, which might not generalize to real-world, diverse scenes. Expanding to more varied data or testing on real-world videos would make the findings more robust.

- Comparing toddler gaze data only with adult and random gaze is not sufficient. Adding standard data augmentations like rotation or scaling would better show if gaze-based learning offers unique advantages.

- The model only uses central vision, though peripheral vision plays a big role in human perception

- The paper lacks insight into which features are affected by toddler gaze. 

- Evaluating only on object recognition limits the findings.

### Questions
- Why focus only on central vision? How about peripheral vision’s role in learning?
- How exactly does gaze duration affect feature learning? Any patterns in which features are learned?
- Have you addressed overfitting?
- Any ideas how to evaluate beyond object recognition, like for object localization?
- The dataset is unbalanced. Did you do analysis on that?
- Are toddler vs. adult differences statistically significant? Have you tested with random age samples?
- Are there any visible differences in feature maps from toddler and adult data? Seen patterns in views?
- Do you have evidence that toddlers learn with temporal slowness, or is this an assumption?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores whether a bio inspired visual learning model can harness toddlers’ gaze behavior during a play session to develop view-invariant object recognition. Exploiting head-mounted eye tracking during dyadic play, the authors simulate toddlers’ central visual field experience by cropping image regions centered on the gaze location. This visual stream feeds a time-based self-supervised learning algorithm. The experiments demonstrate that toddlers’ gaze strategy supports the learning of invariant object representations.

### Strengths
1. The idea of combining toddlers’ gaze behavior with self-supervised learning of view-invariant object recognition is interesting.
2. The writing style of this paper is clear and fluent, and the content is easy to understand.
3. The experimental part is quite detailed.

### Weaknesses
This paper claims to "reveal how toddlers’ gaze behavior supports self-supervised learning of view-invariant object recognition". However, 
1. in Sec. 3.1, the proposed random/centroid fixation datasets, i.e, the control groups in experiments, do not contain objects of a specific category, making it difficult to prove the effectiveness of the proposed toddler/adult fixation datasets in the view-invariant object recognition task;
2. the entire work only validated on one self-supervised model, which is clearly lacking in persuasiveness; 
3. in Sec. 4.1, the experimental results in Figure 4 do not support the authors' claim that "toddlers appear to curate their gaze behavior to develop robust object representations quickly". Firstly, there is no significant difference in the experimental results between adults and toddlers. Secondly, the results of toddler/adult fixation datasets are significantly inferior to the objects fixation dataset, indicating that toddler/adult fixation datasets cannot help the self-supervised model learn better representations.

### Questions
`Toddler' refers to children between the ages of 1 and 3. However, all the `toddler' participating in the experiment in Table 2 are between the ages of 12 and 25. Is it the true experimental setting, or is it a typographical error by the authors?

### Soundness
2

### Presentation
3

### Contribution
2
