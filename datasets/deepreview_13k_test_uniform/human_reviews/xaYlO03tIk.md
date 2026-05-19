# Stem-OB: Generalizable Visual Imitation Learning with Stem-Like Convergent Observation through Diffusion Inversion

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Visual imitation learning methods demonstrate strong performance, yet they lack generalization when faced with visual input perturbations like variations in lighting and textures. This limitation hampers their practical application in real-world settings. To address this, we propose \textbf{\ours} that leverages the inversion process of pretrained image diffusion models to suppress low-level visual differences while maintaining high-level scene structures. This image inversion process is akin to transforming the observation into a shared representation, from which other observations also stem. 
\ours offers a simple yet effective plug-and-play solution that stands in contrast to data augmentation approaches. It demonstrates robustness to various unspecified appearance changes without the need for additional training. We provide theoretical insights and empirical results that validate the efficacy of our approach in simulated and real settings. \textit{\ours} shows an exceptionally significant improvement in real-world robotic tasks, where challenging light and appearance changes are present, with an average increase of \textbf{22.2\%} in success rates compared to the best baseline. See \href{https://hukz18.io/Stem-Ob/}{our website} for more info.

\enlargethispage{\baselineskip}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Stem-OB, a method that enhances visual imitation learning by using image inversion from pretrained diffusion models to reduce low-level visual variations while preserving high-level scene structure. Stem-OB creates a shared representation that is robust to various appearance changes without additional training. Empirical results on several benchmarks demonstrate the effectiveness in challenging environments with lighting and appearance changes.

### Strengths
* This paper focuses on enhancing the robustness of visual imitation learning, addressing a practical and impactful topic. The approach holds significant potential for advancing research in the field of robotics.

* The idea of using diffusion inversion to remove low-level visual variations while preserving high-level scene structures is both novel and intriguing.

* The evaluations are thorough, with experiments conducted in both simulated environments and on real-world robots. The real-world experiments highlight the method's strong generalization capabilities.

### Weaknesses
* I found the structure of this paper somewhat difficult to follow, as certain sections lacked clarity. For instance, in the preliminaries, the definition of diffusion inversion seemed to be a combination of both forward and backward diffusion. But in Figure 2, it seems that proposed method uses the noised observations as the policy input. If the proposed method is trained on the inversion-altered space, why using the noised version of the observation as input can improve the performance? How can the authors guarantee that applying forward diffusion to the image improves generalization?

* There seems to be a trade-off when choosing the inversion step, which can not be either too large or too small. Is there any explanation about this phenomenon? 

* The theoretical analysis section was also challenging to understand. The authors discuss a loss between two latent variables,  $x_0$ and $y_0$. What  is the intuition of calculating the loss of two different images? From my understanding, the attribute loss here should refer to the inversed data $\hat{x}_0$ and its original version $x_0$. Could the authors also clarify the statement, “images with fine-grained attribute changes tend to become indistinguishable sooner than those with coarse-grained modifications under identical diffusion schedules”? 

* Section 4.1 reminded me of another study [1], which employs diffusion models to purify noise within noisy demonstrations while preserving the optimal structure. Are there any conceptual similarities between that approach and the proposed method?

* Typos: Line 242: $er$f should be $erf$.

[1] Imitation Learning from Purified Demonstrations, ICML 2024.

### Questions
Please refer to Weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes to use diffusion inversion as input preprocessing for visual imitation learning methods in order to improve their generalization to visual changes between demonstration and test setup. The proposed approach is evaluated in real-world robotic experiments as well as on 2 simulated datasets.

### Strengths
- The idea is, as the authors write, 'simple yet effective' and the authors manage to neatly package a quite theoretical idea and a very practically result measured in real-world robotic experiments all in 1 paper
- While I lack the background to assess the theoretical grounding, the idea itself is well explained
- The authors combine experiments on simulated datasets with actual real-world tests. Real-world tests are incredibly important for visual methods, yet in case of robotic applications very hard to make reproducible. The combination of both is a commendable experimental design.
- Similarly, the authors conduct real-world user studies to investigate their hypothesis that diffusion inversion progresses along semantic hierarchies.

### Weaknesses
- [**update after discussion: this point was fixed**] I find the derivation in Section 4.1 very hard to follow. Only the first sentence of Section 4.2 makes it clear that the whole derivation is based on the assumption that semantically similar images are closer in latent space. That is a HUGE assumption and the following experiments on intra- and inter-class confusion do not show this over multiple levels of semantic hierarchies, but only for the semantic leafs. The introduction (lines 60-65) however argues that much more than leaf classes, abstract semantic hierarchies are important to generalize over perceptual differences.
In the empirical study on diffusion inversion, one might argue that out of the 5 empirical examples, "bowl" and "cup" are most similar. However, Table 1 shows that the latent representation of 'cup' samples is actually on average closer to any of {'drawer', 'duck', 'faucet'} than to 'bowl'. To me this makes the assumption 'semantically similar images are closer in latent space' quite unbelievable. For sure, this assumption and therefore the formulation of semantic overlap as overlap of latent gaussians is anything but 'intuitive' (line 270) in presence of this data.
- [**update after discussion: this point was fixed**] In relation to the above, I miss a clear definition of what kind of variation should be compensated through diffusion inversion. The abstract and introduction repeatedly claims that diffusion inversion can extract the 'high-level structure' of the scene, suggesting generalization over different object instances, shapes, appearances, relative placements, and robot arms. Section 4.1 considers 'variation', 'fine-grained attribute change', 'coarse-grained modifications', and 'semantic overlap' without defining any of these. The investigation in Section 4.2 is focused on variations within a semantic object class, i.e. a demonstration with 1 cup should be repeated with a different cup. The experiments then consider lighting change and a limited set of object appearance change of sometimes multiple object instances, while locations are fully fixed. The problem is that all of this currently does not fully fit together and it would be good if the authors can define more accurately what kind of variations they expect diffusion inversion to abstract / generalize over, and then design experiments accordingly to show improvement with exactly these variations.
- There are a couple of odd aspects about the simulation experiments that raise questions about the soundness of the results:
  - For the benchmarks from ManiSkill and MimicGen, why were not all tasks evaluated? For ManiSkill, plug-charger seems to be specifically excluded and for MimicGen 4 out of 12 tasks were picked without any explanation.  
[ **update after discussion: now there are 8 out of 12 tasks from MimicGen. It is still a subset, but this indeed makes the results more thorough**]
  - While I did not quickly find comparable numbers for ManiSkill, the MimicGen paper reports much higher success rates for the investigated tasks. E.g. for Threading, MimicGen reports around 19% sucess from just 10 videos and 98% success from 1000 videos. For the 500 videos used in the experiments here, the success is below 19% for 3 out of 4 variants, including the proposed method. Why are the achieved success rates so low? And can the proposed method actually improve anything in a more state-of-the-art setting? [**update after discussion: This concern mostly remains. While the authors show that their success rates for 500 trials are mostly between the baseline MimicGen results of 10 and 1000 trials, there is no case where the authors can demonstrate to improve over these prior results. If one expects the relation between number of trials and success rate to follow a saturation trend rather than a linear trend, their results are still a bit below those of prior works.**]
  - Why is the RO baseline excluded from the simulation experiments? [**update from discussion: this was resolved**]
- In all experiments (real and simulated), most of the differences between methods are within the standard deviation, so it is very hard to say if any conclusion can be drawn. Why is the standard deviation so high? [**update from discussion: this has been thoroughly addressed by the authors. The updated results show, similarly to the question about success rates above, that Stem-OB does not push the state-of-the-art further than where it is. But it does more importantly also not appear to be much worse, while the method in some sense is simpler.**]

### Questions
The most significant questions are already listed under weaknesses. In addition, I would be interested to get a clarification on the following points:

- line 272: How many images?
- line 428: Can the authors explain how they get to this conclusion? The training setting performance of RO in particular looks to me like it was not trained correctly.
- line 430: Given the result in D2B, I don't think the conclusion can be that there is always a high success rate?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes Stem-OB, a method that uses diffusion inversion to transform observations into a shared, robust representation. This approach enhances robustness to various appearance changes, such as shifts in visual patterns and lighting conditions. During inference, Stem-OB approximates the partial inversion process to maintain efficient inference speed.

### Strengths
1. The paper is well-written, with clear motivation and solid experimental validation, including both real-world and simulated experiments.

2. The central idea resonates well: robotic observations often include excessive low-level details, while effective scene understanding requires capturing high-level structural information. This paper draws on an intriguing insight from Yue et al. (2024): "Rather than uniformly removing information from different semantic hierarchies, the process brings structurally similar images closer in the early stages of inversion." Building on this, Stem-OB leverages this observation to project data into a space that prioritizes inherent structural features.

### Weaknesses
Stem-OB enhances the generalization capabilities of robotic systems by using diffusion inversion to map observations into a shared representation. However, another promising line of research—self-supervised representation learning—also aims to unify raw observations into a common representation space, reducing low-level visual discrepancies. I suggest that the authors consider benchmarking Stem-OB against these approaches, particularly methods that leverage self-supervised learning (SSL) for robotic representations, to offer a more comprehensive comparison.

### Questions
The current method conducts experiments solely on Stable Diffusion. It would be valuable to understand if the conclusions drawn from Stem-OB are applicable to other generative models, such as Flux or SD 3 (which uses flow instead of diffusion). Demonstrating that Stem-OB generalizes across different models would strengthen the claim of robustness and broaden the impact of this approach beyond a single model framework.

### Soundness
3

### Presentation
4

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
Visual imitation learning is a method for robots to learn tasks through visual human demonstrations. While multiple methods exist for preprocessing visual data that increase the generalizability of VIL, these methods are only partially efficient. To address the generalization issue, this paper proposes to use the inversion process of a pretrained diffusion model as a preprocessing step to increase the generalizability of visual imitation learning methods. The proposed method relies on the intuitive insight that images with only small perturbations between them are closer in latent space (and therefore become indistinguishable under diffusion faster), than data that exhibits large differences. The method is tested on real and synthetic data and shows that the proposed preprocessing significantly increases the models generalization capabilities.

### Strengths
* The paper relies on a central observation from a previous paper (Yue et al. 2024), which found that during the inversion process of a diffusion model, fine-grained (or high-frequency) details of an image are destroyed first before the low-level semantic concepts. This paper builds on this basic concept and proposes a new preprocessing step that uses this theoretical property of diffusion models as a preprocessing step, which, in the process, improves the generalization of the IL algorithm. 
* The technical principle seems well established at this point, but this paper takes these theoretical findings and applies them to a new problem. While the whole approach is very simple from a technical standpoint, the paper re-introduces the necessary background in section 2 before developing the reader's intuition as to why this preprocessing might work in section 4.2 through theoretical explanation and small experiments. I believe that this paper warrants publication because it shows that diffusion model inversion can be useful for additional tasks. 
* The presentation of the paper is clear and easy to follow overall. 
* The results nicely highlight the drawbacks of previous methods and that the proposed method offers much better generalization capabilities. 
* I appreciated the detailed appendix, with theoretical derivations, additional details for reproducibility, and additional experiments.

### Weaknesses
I believe that the paper's technical novelty is small, as the main concept has already been introduced in other papers. That being said, I also believe that the paper is worth publishing, as it adds to the growing body of literature showing the usefulness of diffusion model inversion for various tasks, and the empirical validation is well executed.

I have additional suggestions to improve the paper's readability and make it easier for the reader to understand.
1. Section 2.2 can be cut (title), and the paragraph can be integrated into Section 3.1. 
2. As a reader, I would really like a short problem formulation that properly introduces the problem the paper addresses. This should properly define the inputs and outputs. I would also suggest rearranging the sections/subsections of the paper to something like this:
* Introduction
* Related Work
* Problem Definition
* Preliminaries
* Method
This would greatly improve the flow of the paper. 
3. While the paper is generally easy to follow, some sentences are should be simplified or run through a writing program. I have added some examples below:
* Line 85: "To be specific, our method is as simple as inverting the image for reasonable steps before" What is reasonable? Maybe rephrase?
* Line 226: "Intuitively, given a source image and its variation, distinguishing between them becomes increasingly difficult" This sentence does not make a lot of sense (although I can guess what is meant).
There are many more of these convoluted sentences. Cleaning up the writing a bit would go a long way to improve the paper.

There

### Questions
See above. I currently give a weak accept to the paper but am inclined to vote for acceptance should my points above be taken into consideration during the rebuttal.

### Soundness
3

### Presentation
3

### Contribution
3
