# Provable Compositional Generalization for Object-Centric Learning

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
Learning representations that generalize to novel compositions of known concepts is crucial for bridging the gap between human and machine perception.
One prominent effort is learning object-centric representations, which are widely conjectured to enable compositional generalization.
Yet, it remains unclear when this conjecture will be true, as a principled theoretical or empirical understanding of compositional generalization is lacking.
In this work, we investigate when compositional generalization is guaranteed for object-centric representations through the lens of identifiability theory.
We show that autoencoders that satisfy structural assumptions on the decoder and enforce encoder-decoder consistency will learn object-centric representations that provably generalize compositionally.
We validate our theoretical result and highlight the practical relevance of our assumptions through experiments on synthetic image data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of compositional generalization in object-centric autoencoders.
The authors formalize this as requiring the model to identify the ground-truth object latents not just on the training distribution, but also on out-of-distribution combinations.
They make two key assumptions to achieve this: (1) The generative process satisfies compositionality, meaning each pixel depends on one object, and irreducibility, preventing objects from being decomposed.
(2) The decoder is additive, decoding each object slot independently.
Under these assumptions, the authors prove autoencoders can identify objects in-distribution by minimizing reconstruction error.
The additive decoder then guarantees generalization out-of-distribution.
However, the encoder may still fail to generalize.
To address this, the authors propose compositional consistency regularization.
This trains the encoder to invert the decoder on recombined object slots, enabling the full autoencoder to generalize.
By combining in-distribution identifiability and compositional consistency regularization, the authors prove autoencoders satisfying their assumptions will generalize compositionally.
Through synthetic experiments, they provide empirical evidence supporting their theoretical results.
In particular, they demonstrate the importance of additivity and compositional consistency for generalization.

### Strengths
This paper made contributions for 
- Formalizing compositional generalization as an identifiability problem
- Theoretical guarantees for in-distribution identifiability
- Showing an additive decoder enables out-of-distribution generalization
- Introducing compositional consistency regularization
- Providing overall theoretical guarantees for compositional generalization

The work makes theoretical progress on understanding compositional generalization in object-centric representation learning.

### Weaknesses
 - The assumptions of compositionality and irreducibility are quite restrictive. Most real-world datasets likely violate these. Specifically, the assumption that each pixel depends on only one object and that objects cannot be further decomposed is a strong constraint. This limits the applicability of the theory to scenarios where objects are truly independent and non-overlapping, which is rarely the case in natural images.
- The additive decoder limits modeling of complex object interactions and relations. This is a significant limitation as it prevents the model from learning how objects occlude, reflect, or otherwise influence each other. Real-world scenes often involve intricate relationships between objects that cannot be captured by a simple additive combination of their individual representations.
- The consistency regularization implementation requires sampling implausible object combinations. This could lead to the model learning to reconstruct unrealistic scenes, potentially hindering its ability to generalize to real-world data. The method lacks a principled way to sample meaningful combinations, which may result in inefficient training and suboptimal performance. More sophisticated sampling strategies or prior knowledge integration could be beneficial.
- Experiments only validate the theory on simple synthetic datasets. Testing on more diverse and realistic data would better demonstrate applicability, though the evaluation would also be more challenging. The current experiments do not provide sufficient evidence that the proposed method can generalize to more complex scenarios with diverse object appearances and backgrounds.
- The proposed methods, especially when ensuring encoder-decoder consistency and handling latent slots, might pose scalability issues for very large datasets or more complex models. A discussion on the scalability, computational costs, and potential solutions would make the paper more robust. The computational overhead of the consistency loss, which requires additional passes through the encoder and decoder, could become prohibitive for large-scale datasets or high-resolution images.

### Questions
Please see above.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents conditions where compositional generalization is theoretically guaranteed for object-centric learning. 

Specifically, they first extend the identifiability theory of object-centric representations to handle partial joint distribution supports, with an additional assumption/constraint on the decoder to be compositional. This ensures that slots are identifiable in the training distribution. They then ensure the generalizability of decoders (which, e.g., generate images given slot representations) with another assumption/constraint as the decoder being additive. The theoretical analysis is similar to those proving the compositional generalizability of any additive inference models.

The novel step is to enforce the compositional generalizability of encoders by learning with the synthesized data in new compositions of latent slots/symbols given the generalizable decoder. So, in order to learn an encoder that can generalize to unseen combinations of objects, they first build a dataset with new compositions of latent symbols/slots by permutating learned latent symbols/slots in the training distribution. They then generate the fake images using the "supposedly generalizable" decoders on new combinations. The encoder is trained to learn the inverse mapping of the decoder. This process is formulated as a compositional consistency regularization loss in practice.

The experimental results are aligned with the theories in a simple two-object synthetic image environment.

### Strengths
This paper discusses an important problem: learning compositionally generalizable object-centric representations. The paper is well-written and easy to read. The connections with related works are also interesting and inspiring. 

The reviewer especially appreciates the theoretical guarantees and analysis. Even though the assumptions are strong on both the functions to be approximated as well as the parameterization of learned functions, they are still aligned with the image object-centric representation learning setting, and the methods can be relaxed and realized using modern object discovery methods such as slot attentions. 

The proposed regularization loss to enforce the compositional generalizability of encoders is interesting and seems easy to use. 

The ablation study on the additive decoder (softmax v.s. sigmoid in slot attentions) is interesting and inspiring.

### Weaknesses
It would be great if the assumptions could be relaxed, e.g., to handle occluded objects or to handle general latent variable learning domains other than the image objects. 

The "contemporary" work [1] discussed most parts of this paper except for the generalizable encoder. 

The experimental environment is simple with two-object synthetic images. It would be more convincing to see results on multi-object real images.

### Questions
Are there results in more complex environments? 

Can the theories be generalized to more general settings with weaker assumptions?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors theoretically and empirically show that compositional generalization can be achieved through:
1. Structural constraints on the decoder (each data dimension is rendered as the sum of functions operating on slots separately), which ensures that the decoder compositionally generalizes.
2. An encoder-decoder consistency loss (reconstruction loss for the representations) on slot-shuffled representations from the encoder output, which encourages the encoder to compositionally generalize with the additive decoder.

The paper provides a joint encoder-decoder framework for compositional generalization for autoencoders, where previous work has mostly focused on specific aspects of the setting.

### Strengths
- The paper is very well-written.
- The theory is sound and significant for the community.
- The joint encoder-decoder framework for compositional generalization in autoencoders is quite elegant.
- The limitations of the framework and the additivity constraint on the decoder are adequately stated.

### Weaknesses
Although they support the theory, the experiments are quite limited. For instance, these are all with only two slots with 16 dimensions each. See the questions section for additional information that would be interesting to see from experimentation.

### Questions
- How does the effect of the consistency loss scale with the number of slots?
- What is the impact of how slot-supported the training data is? i.e. in Figure 2 (1), what is the impact of the width of the blue band on empirical effectivity?
- How does the method hold up on non-synthetic data, especially if you slightly relax some constraints? For instance, what if you have expressive slot-wise decoding, but allow for a low-expressivity non-linear combination at the end for rendering?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
