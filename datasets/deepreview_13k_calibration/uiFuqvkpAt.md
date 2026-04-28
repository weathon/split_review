# Vector Quantized Representations for Efficient Hierarchical Delineation of Behavioral Repertoires

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Understanding animal behaviors and their neural underpinnings requires precise kinematic measurements plus analytical methods to parse these continuous, multidimensional measurements into interpretable, organizational descriptions. Existing approaches can identify stereotyped behavioral motifs, given 2D or 3D keypoint-based data but are limited in their interpretability, computational efficiency, and/or ability to seamlessly integrate new behavioral measurements. In this paper, we propose an end-to-end behavioral analysis approach that dissects continuous body movements into sequences of discrete latent variables using vector quantization (VQ). The discrete latent space naturally defines an interpretable deep behavioral repertoire composed of hierarchically organized behavioral motifs. Using recordings of freely moving rodents, we demonstrate that the proposed framework faithfully supports standard behavioral analysis tasks and enables a series of new applications stemming from the discrete information bottleneck, including realistic synthesis of animal body movements and cross-species behavioral mapping.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose an end-to-end behavioral analysis approach that dissects continuous body movements into sequences of discrete latent variables using vector quantization (VQ). The discrete latent space naturally defines an interpretable deep behavioral repertoire composed of hierarchically organized behavioral motifs. Using recordings of freely moving rodents, the authors demonstrate that the proposed framework faithfully supports standard behavioral analysis tasks and enables a series of new applications stemming from the discrete information bottleneck, including realistic synthesis of animal body movements and cross-species behavioral mapping.

### Strengths
1. The paper is generally well-written and easy to follow.
2. The experimental results seem to support the authors' claims.

### Weaknesses
1. It would be better to compare the proposed method with more advanced baseline approaches to demonstrate its effectiveness. There should also be more ablative analysis the illustrate the effectiveness of each component of the model. Specifically, the comparison should include state-of-the-art methods for behavioral analysis and motion synthesis, and the ablation study should evaluate the impact of the hierarchical structure, the vector quantization process itself, and the size of the codebook on both the quality of behavioral segmentation and the fidelity of motion synthesis. Without these comparisons and ablations, it is difficult to assess the true contribution of the proposed method.
2. There is a missing citation on the first page.
3. The major innovations seem not very clear. It would be better to clearly state the major novelty of the proposed method and indicate its advantages over existing methods in the literature. The related work section is suggested to be refined and moved to an earlier place for readers to understand the context of the field. The novelty should be clearly articulated in terms of both the technical approach and the resulting capabilities, highlighting how it advances the field beyond existing methods. The advantages should be made explicit, such as improved interpretability, better performance on specific tasks, or novel applications that are not feasible with previous techniques.

### Questions
Please focus on addressing the issues in the Weaknesses section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an end-to-end unsupervised behavioral mapping approach that identifies hierarchically organized discrete behavioral motifs from pose time-series data. This is done using a variational encoder to map postural dynamics to a finite-sized discrete embedding with vector quantization.

### Strengths
Well written and technical details are clear.  The evaluations are clear.  The motivations are mostly clear and the applications are well explained.

### Weaknesses
Missing/failed citation in first paragraph

How is the quantization "codebook" initialized and updated?  This is not clear to me.

An ablation showing the benefit of using the proposed quantization would be helpful.

Were there no other SOTA models to compare against?  The evaluations seem a bit lacking.  Additional applications, comparison models and a detailed ablation would help here as well as more detail on limitations and failure cases.

### Questions
How is the quantization "codebook" initialized and updated?

What is the impact of not using quantization on the proposed applications?  This is not clear to me.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper describes a framework to learn representations of animal behavioural data, using a VQ-VAE with multi-level encoding. This choice of latent representation enables the data to be decomposed into different discrete behavioural motifs, and enables analysis and synthesis of movements. The application is intriguing, and the presentation is relatively clear.

### Strengths
- The theoretical development is sound.
- The presentation is relatively clear.
- The application to animal behavioural data is interesting and important.

### Weaknesses
 - Unfortunately, it’s not clear whether there is sufficient technical novelty for the ICLR community. The application of VQ-VAE to animal behavioural data specifically may be novel, but other than the multi-level encoding, it is not clear whether there are architectural/learning improvements that may be relevant to the broader ICLR reader. The listed contributions indicate potential novelty in behavioural neuroscience (ie. that this model simplifies the behavioural pipeline), which could perhaps suggest a different venue might be a better fit.
- There is quite a lot of work on existing work on learning movement primitives or behavioural decomposition via latent variable models in embodied and robotics domains. The work could better be positioned in this context, and architectural design choices could be better justified. Specifically, the use of a VQ-VAE with multi-level encoding, while potentially useful for discrete representation, needs more justification compared to other methods that use sequential latent variable models for time-series data. The paper does not adequately address why this specific approach is superior to alternatives, especially given the temporal nature of the data.
- The analysis could be more thorough; as it stands there is only one table of quantitative results, for motion synthesis, and the method is compared mostly to quite weak baselines (fully-connected MLP, GRU). The evaluation of the learned representations is limited, and there is a lack of analysis on the quality of the discrete behavioral motifs that are learned. It is unclear how well these motifs capture meaningful behavioral patterns, and how they compare to existing methods for behavioral decomposition. The paper would benefit from a more thorough analysis of the learned representations, beyond just motion synthesis.

### Questions
- There is quite a lot of work on learning movement primitives (eg. Paraschos et al, 2013), or behavioural decomposition via latent variable models in embodied and robotics domains.
Merel et al (2019a); Bohez et al (2022) apply hierarchical latent variable models to motion-capture data from humans and other mammals, and Merel et al (2019b) specifically studies learned representations of simulated rodent behaviour.
Other works leverage latent variable representations of offline behavioural data in robotics (eg. Singh et al, 2021), including hierarchical discrete representations that can decompose data into discrete motifs that can execute / synthesize meaningful behaviours (Rao et al, 2022).
- Related to these points, it’s not clear why specific architectural choices were made. For example, encoding entire trajectories into a single latent code scales poorly with dimensionality of the inputs and length of the sequence, and many of the approaches from my previous comment use sequential latent variable models to better model embodied temporal data.

Some minor comments:
- Broken citation reference in the first paragraph
- Having the related work as a final section reads a bit awkwardly to me, as it feels like an afterthought. Consider moving it to at least before the final discussion / conclusions, and ideally before the method itself to provide some scaffolding and context for the contributions and claims.

References:
- Paraschos et al (2013), Probabilistic Movement Primitives
- Merel et al (2019a), Neural Probabilistic Motor Primitives for Humanoid Control
- Merel et al (2019b), Deep Neuroethology of a Virtual Rodent
- Singh et al (2021), Parrot: Data-Driven behavioral priors for reinforcement learning
- Bohez et al (2022), Imitate and Repurpose: Learning Reusable Robot Movement Skills From Human and Animal Behaviors
- Rao et al (2022), Learning Transferable Motor Skills with Hierarchical Latent Mixture Policies

### Soundness
2 fair

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an efficient framework for dissecting animal behavioral data into hierarchically organized, discrete representations using vector quantization (VQ). The authors demonstrate the effectiveness of their proposed method on real animal body movement analysis and cross-species behavioral mapping tasks.

### Strengths
The paper introduces a novel method for analyzing animal behavior, which leverages vector quantization and hierarchical encoding. And they have run experiments on multiple real datasets to analyze animal behavior and map behavior sequences cross-specices.

### Weaknesses
The paper lacks more quantitative comparisons. And there are some unclear parts in the paper. I listed questions in the section below.

- in equation (3), can you elaborate more on the embedding and commitment terms? intuitively what do they mean and how are they derived?

- How robust is the method to variations in the number and granularity of discrete codes? In practice, how do you determine the number of codes in each level?

- what are the quantitative comparison results aginst the KPMS benchmark?

### Questions
- in equation (3), can you elaborate more on the embedding and commitment terms? intuitively what do they mean and how are they derived? 

- How robust is the method to variations in the number and granularity of discrete codes? In practice, how do you determine the number of codes in each level?

- what are the quantitative comparison results aginst the KPMS benchmark?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
