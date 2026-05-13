# Looping LOCI: Developing Object Permanence from Videos

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
Recent compositional scene representation learning models have become remarkably good in segmenting and tracking distinct objects within visual scenes. Yet, many of these models require that objects are continuously, at least partially, visible. Moreover, they tend to fail on intuitive physics tests, which infants learn to solve over the first months of their life. Our goal is to advance compositional scene representation algorithms with an embedded algorithm that fosters the progressive learning of intuitive physics, akin to infant development.  As a fundamental component for such an algorithm, we introduce Loci-Looped, which advances a recently published unsupervised object location, identification, and tracking neural network architecture (Loci, Traub et al., ICLR 2023) with an internal processing loop. The loop is designed to adaptively blend pixel-space information with anticipations yielding information-fused activities as percepts. Moreover, it is designed to learn compositional representations of both individual object dynamics and between-objects interaction dynamics. We show that Loci-Looped learns to track objects through extended periods of object occlusions, indeed simulating their hidden trajectories and anticipating their reappearance, without the need for an explicit history buffer. We even find that Loci-Looped surpasses state-of-the-art models on the ADEPT and the CLEVRER dataset, when confronted with object occlusions or temporary sensory data interruptions. This indicates that Loci-Looped is able to learn the physical concepts of object permanence and inertia in a fully unsupervised emergent manner. We believe that even further architectural advancements of the internal loop—also in other compositional scene representation learning
models—can be developed in the near future.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides an improved version of the recently proposed Loci (location and identity tracking) model, by introducing an internal loop of prediction and updating. The major advantage of the proposed Loci-looped model is that the network is able to track objects even when they are occluded or during blackout. The paper claims that it shows surprise signal when an object violates object permanency, reflecting the learning of the rule of object permanency and inertia

### Strengths
The infants' learning of objects' property is holistic: they not only learn to segment objects, but indeed learn certain properties of objects (such as object permanency) without supervision. It is nice to have a model that simultaneously learn both without supervision. As pointed out by the authors, although many models show good performance on some datasets, they use supervision or conditioning signals that are not available to human brain, thus do not provide insight for how these abilities can be jointly learned without supervision as infants.

The idea of separately generating object mask and visibility mask appears to be novel, which is required for demonstrating object permanency.

### Weaknesses
I believe that the ability of correctly segmenting objects in the newly proposed framework largely comes from the information bottleneck. Although it works well with the chosen datasets which have almost pure colors in each object, I doubt it will work well in environments with more complex texture as in nature or in datasets such as MOVI-c and beyond (https://github.com/google-research/kubric/tree/main/challenges/movi). Although I guess segmentation is not treated as a major contribution, I worry about how much the proposed principle can be scaled up and generalize. 

If we are restricted to a simple environment, one can imagine that another model that simply clusters pixels based on colors and estimate the center of mass of the clustered pixels could likely segment and localize objects correctly in the CRATER dataset, without using a neural network. Then an RNN that learns to predict the center of mass based on the previous trajectory extracted with the above approach and weights its loss function based on the number of pixels in the correct color corresponding to that object can also shut down gradient when an object is occluded, and then receive teaching signal once the object reappears. This way, the RNN may also be able to learn to predict a linear moving trajectory. Now perhaps what I describe here essentially is similar to the idea of perceptual gate and perhaps the advantage of the current model is that the gate is learned rather than being hard coded as being decided by pixel counts, what I am trying to say is that the environment may not pose enough challenge for the task that the model aims to solve (all of segmentation, localization and tracking). If an environment allows defining the gate by a pre-defined rule, then learning it seems trivial. I am not against using such dataset for proof of principle. But I think this limitation should not be ignored.


I hope that the writing can be slightly clearer. For example, the meaning of Gestalt has expanded to capture the principle to organize parts into an object due to Gestalt school of psychology. If you follow the simple description of gestalt code as "mainly representing shape and surface pattern" in loci-v1 paper, it is a good idea to define it here as well.

There are other unclear parts. Please see my questions.

The slot error is claimed to serve as a surprise signal. But some details of its pattern appears strange to me. In Figure 3, after frame 30, the slot error is of similar magnitude for both the reappearing and vanishing object. If as the paper tries to claim that the model learns to imagine objects behind the plate during occlusion, then I would expect that it should predict the appearance and location of the object more or less correctly when the object should reappear. In other words, the slot error should be smaller in the reappearing case than in the vanishing case (which violates object permanency and should not be predictable at all). An indifference here seems to indicate either the prediction of occluded object is quite wrong upon reappearing or that the model somehow learns to predict vanishing object somewhat correctly?

### Questions
In equation 2: there seems to be no restriction being mentioned that the visibility mask should be smaller than the object mask (or even within it), I assume it is possible for the numerator to become larger than denominator and for the occlusion state to be negative. How do you stop this? 

There is a sentence between Figure 2 and 3.3: "By adding Gaussian noise with a fixed standard deviation ..., learning is biased to move further into plateaus away from ridges where possible." I am sorry that I did not quite get what plateaus and ridges refer to here. Something about loss landscape as a function of all network weights? 

Below that, it was stated that L0 regularization is imposed on gate opening, but L0 loss has no gradient. If I understand correctly, equation 10 indicates that you instead use 1 as gradient. To me it seems that you are actually imposing L1 loss for positive values instead of L0 loss.

In Result of 4.2 next to Figure 3, I did not really understand "significant correlation between the slot error of vanished objects and the visibility of reappearing objects". If these two quantities are of two different objects, why should we expect them to be correlated? I also don't understand by "likewise, we find the same pattern for the size of visibility mask" what correlation you refer to.

In the experiment of 4.2, does the occluding plate also get assigned a slot, or is it treated as part of the background by the network? How does the prediction for the plate looks like when it falls?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a follow-up architecture with a different set of regularizers based on prior slot attention next-frame prediction work. The authors claim that the system is able to "form concepts of object permanence and inertia from scratch in a fully self-supervised
manner." The authors evaluate the system on two datasets.

### Strengths
- **S1** The study could offer understanding on the advantages and limitations of current machine learning systems for modeling object permanence.
- **S2** The approach description is written clearly. the authors provide detailed descriptions of their proposed approach.

### Weaknesses
 **W1 - A critical aspect of the result - visualization of slot attention decomposition is missing**. 

The result section does not contain any illustrations of slot decomposition and roll-out results across time. Please see **Figure 6** in [1] and **Figure 5** in [2]. It is critical to visualize slot decompositions, especially given how strongly authors are attempting to make the "object permanence" claim.

 
**W2 - More ablation experiments are needed to justify the robustness of the system**. 

- For instance, for **Figure 2**, what would happen if the authors change the camera poses, such as following a spherical trajectory, while rolling out the model? The authors could visualize slot decompositions while varying camera poses. 
- How important is each of the regularizers proposed in **Table 1**? Many changes are made going from Loci-v1 to Loci-looped.


**W3 - More comparisons with baselines are needed** The authors did not compare against many powerful frameworks, such as [1] and [2]. It would be very valuable to know where the proposed approach stands.


**W4 - More discussions and analysis are needed to justify strong claims** such as "forming the concept of object permanence and inertia from scratch." 
- How is inertia property tested in the ADEPT's vanish scenario? 
- Can the proposed system estimate the unknown inertial parameters of rigid bodies in the physical system given videos?

**W5 - What are the limitations of this work? There does not seem to be any discussion.** For example, how would the system perform if non-rigid materials were present in the scene? Suppose a cup of water is being poured into a basket that is occluded by a board, a similar setup to your current experiments. Could the system still infer that the water is permanent across time?

### Questions
Please see the weaknesses section above. Thanks.

### Soundness
2 fair

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
In this manuscript the authors describe an extension of their Loci method for tracking objects in video. They add an internal connection that propagates latent predictions directly to a model that previously had only a loop through pixel space. This addition improves tracking for fully occluded images substantially for simplified rendered scenes.

### Strengths
Overall this approach is interesting as an interpretable model of object tracking and the authors present some observations showing that their method tracks fully occluded objects now. The model still learns in an unsupervised way from video data, is evaluated on a few different tasks and does pass basic object constancy tests as used for children.

### Weaknesses
The tests are all performed in extremely reduced situations where simple objects move along fully predictable straight trajectories, which raises concerns about the scaling and generality of the approach. Additionally the work is clearly incremental as it extends a highly similar method from last year. Thus, I am not convinced this manuscript warrants another publication yet.

For the evaluations, I believe a more natural dataset with higher variability of the trajectories and object motion and/or in the properties of objects would be desirable. And even for the simple situations covered by the manuscript, more comparison models are necessary. At very least the PLATO and ADEPT models mentioned in the manuscript should really be tested on the same data for comparisons. And going further I am also not convinced that other models without explicit object representations categorically cannot represent the objects through occlusions. While I share the intuition that they should be worse, I think this should be shown properly by evaluating  such more general models on the same test data.

And on the model side, it is an observation that this added loop improves the Loci model, but this seems to me like an incremental improvement about this specific model. To be convincing as an insight about models I would require an application to multiple models that shows that this is indeed a general productive direction for object slot models. As it stands now, I don’t see any clear insight to gain from this manuscript beyond the authors presenting a revised version of their model.

### Questions
I don’t have questions for the authors.

### Soundness
3 good

### Presentation
3 good

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
The paper focuses on the problem of compositional scene representation learning from videos. Specifically, the authors propose an extension of the Loci (Traub et al., ICLR 2023) by an additional module where it can decide whether to leverage the sensory input to determine the object state or purely rely on previous object states. In this way, the proposed method is able to handle object occlusions and sensory interruptions (masking random frames to be black). The experiments show that the model obtains better object tracking performance on the ADEPT dataset compared with baselines, and better performance of sensory interruptions on the CLEVERER dataset.

### Strengths
- The paper proposes an interesting extension of Loci to handle object occlusion and sensory interruptions.
- The proposed method exhibits strong object tracking performance on the ADEPT dataset compared with previous methods like Loci and SAVi.

### Weaknesses
 - My major concern about the paper lies in the limited contribution and generalizability of the proposed method. The design of the model is a bit complex and ad-hoc. The core contribution is the introduction of an inner loop that enables the model to imagine object dynamics without sensory inputs. To be more specific,  the proposed model is encouraged to ignore the sensory input when the object is being occluded. This does not make sense when the camera is moving, as the camera motion (which needs to be inferred from video) should also be considered for inferring the view-centered object motion. Failing to account for that makes the model rather limited. I am interested in authors’ opinions about how to extend the current model to support this. It is interesting to see the current model’s performance on the LA-CATER Moving dataset proposed in [1] which contains camera movements.

 - On the other hand, the evaluation of the paper is rather limited. The main experiments regarding object tracking only consider ADEPT, a synthetic object with a simple background and at most 3 moving objects. It is unknown how the method will perform on more complex and realistic datasets. I understand this is a common concern for a lot of compositional scene representation learning works. But given the limited technical contribution of the paper and the complexity of the proposed method, I believe a more comprehensive evaluation will make the paper stronger. For example, why authors do not evaluate on the CLEVRER and Aquarium as in the original Loci paper?

### Questions
Apart from the questions I mention in the weakness section, I have a few more questions:

- In Figure 4, t=42, why the green object ceases to exist in the imagination of loci-looped?
- Can this inner loop mechanism be leveraged in other compositional scene representation learning methods? Demonstrating the effectiveness of this mechanism on other models will also make the paper stronger.
- Can authors provide more qualitative results (e.g. videos) about the tracking performance of the proposed method?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
