# Representative Guidance: Diffusion Model Sampling with Consistency

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
The diffusion sampling process faces a persistent challenge stemming from its incoherence, attributable to varying noise directions across different time steps. 
Our Representative Guidance (RepG) offers a new perspective to handle this issue by reformulating the sampling process with a coherent direction towards a representative target.
In this formulation, while the classic classifier guidance improves feature discernment by steering the model away from ambiguous features, it fails to provide a favorable representative target, since the class label is overly compact and leads to sacrificed diversity and the adversarial generation problem.
In contrast, we leverage self-supervised representations as the coherent target and treat sampling as a downstream task, which refines image details and corrects errors rather than settling for simpler samples.
Our representative guidance achieves superior performance and also illustrates the potential of pre-trained self-supervised models in image sampling. Our findings demonstrate that RepG not only substantially enhances vanilla diffusion sampling but also surpasses state-of-the-art benchmarks when combined with the classifier-free guidance. Our code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the **incoherence problem in diffusion models**, where inconsistencies across timesteps lead to artifacts and reduced image quality. The authors introduce a novel approach by framing this issue as **feature discrepancy alignment** between predicted image distributions and representative features across timesteps. They propose **Representative Guidance (RepG)**, which uses representative vectors from self-supervised models to guide sampling coherently. This method successfully enhances the quality of generated images while preserving diversity, offering promising alternative guidance in diffusion models.

### Strengths
1. **Originality:**  This paper tackles the important challenge of enhancing image generation quality in diffusion models. The authors approach this by tackling incoherence in diffusion models and redefining it as a mismatch in predicted image distributions across timesteps. This fresh perspective enables a unique and novel solution to this problem.
2. **Novelty:** Unlike conventional classifier-based guidance, RepG utilizes pre-trained self-supervised models to provide representative vectors, making it effective for fine-grained image sampling. By treating sampling as a downstream task of self-supervised learning, RepG leverages the self-supervised features, which inherently contain richer semantic information than one-hot class labels. This choice addresses the common problem of classifier-guided diffusion models that often overemphasize discriminative features at the cost of generative quality and diversity.
3. **Results:** The experimental results demonstrate that RepG improves image quality, producing generations with finer details and reduced artifacts while preserving diversity.

### Weaknesses
1. **Dependency on Self-Supervised Model Quality**:  It seems that RepG relies heavily on the quality of self-supervised models for guidance. For instance, MoCo-v2 yields the best results, while other models like SimSiam show only marginal improvement over classifier-free guidance (e.g., FID of 1.88 vs. 1.89 on ImageNet64x64). This limitation is not thoroughly addressed in the paper, raising questions about RepG's generalizability and performance across different datasets where MoCo-style representations may not be optimal. The paper lacks a detailed analysis of why certain self-supervised models perform better than others within the RepG framework, and it does not explore the potential for fine-tuning or adapting these models to better suit the specific needs of the diffusion process. The sensitivity to the choice of self-supervised model raises concerns about the robustness of the method. 

2. **Limited Applicability to High-Resolution Image Generation**: The paper shows promising results in lower-resolution settings, but lacks validation on high-resolution datasets. Since RepG’s main advantage lies in enriching details while preserving diversity, testing on high-resolution images could reveal strengths or limitations in its ability to maintain fine-grained coherence and detail at scale. The absence of experiments on high-resolution images makes it difficult to assess the practical applicability of the proposed method in real-world scenarios, where high-resolution image generation is often required. The paper should include experiments on datasets such as ImageNet at 256x256 or higher resolutions to demonstrate its effectiveness in more challenging settings.

3. **Need for More Convincing Quantitative Results**: While Figure 3 provides examples of improvements, some results appear limited or inconsistent. For example, in the last row on the right, although a human figure is partially removed, body parts remain, which makes the result more unrealistic. Additionally, the left example in that row seems to reduce image realism rather than improve it. Including more compelling examples would strengthen the argument for RepG’s claimed improvements in detail and coherence. The paper should include a more thorough analysis of failure cases and provide more diverse examples to demonstrate the consistency of the method's performance. The current set of examples is insufficient to fully validate the claims made by the authors.

### Questions
1. The paper suggests that RepG is more computationally efficient than classifier-based guidance, which often requires noise-aware training. However, it’s unclear what the computational trade-offs are for RepG, given the potential overhead from integrating self-supervised models and tuning features at each timestep. Could the authors provide a more thorough comparison of computational efficiency?
2. In the ablation study on the number of representative vectors 𝐾, lines 480-485, could you provide further explanation? The results suggest sensitivity to 𝐾 values. Given that the level of shared features between different classes may vary significantly across datasets and depends on the chosen self-supervised model, could the authors provide more context on how to select appropriate 𝐾 values? Additional explanations on the trade-offs involved would clarify the model's adaptability to different datasets and feature distributions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors proposed an approach, namely representative guidance (RepG) to make the sampling process of diffusion model along a consistent direction. The proposed RepG is a plugin module, which can be easily adapted to existing framework. Particularly, RepG adopts the self-supervised representation to achieve the aim of consistent sampling direction of diffusion. The proposed approach is evaluated on publicly available ImageNet dataset, which presents improvements to existing diffusion models.

### Strengths
1. The paper is easy to follow.
2. The approach has been evaluated on publicly available dataset, which makes the experimental results convincing.

### Weaknesses
1. There are lots of typos in the paper, such as the caption of Table 1: ImageNet 256x26 -> ImageNet 256x256. The authors should carefully proof-read the manuscript.
2. Some important baselines are missing from Table 1, such as the comparison between RepG and the existing approaches with IDDPM. The comparison with ADM backbone seems to be more comprehensive. The authors should illustrate the reason for such an experimental setting.
3. With ADM backbone, the experimental results are also difficult to directly compare. Too much different setting of the ADM variant. The authors may consider to simply compare the methods with ADM + X (where X is RepG / PxP and the others).
4. Why the performance of MoCo-v3 is lower than MoCo-v2 in Table 2?
5. Please include the visualization results generated by existing approaches as well.

### Questions
Please refer to weakness section for details.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a solution for improving diffusion sampling process that involves tuning image features at each time step to rectify incoherent features. For this purpose, the authors introduce a guidance scheme called Representative Guidance (RepG), which leverages information from representative vectors to steer the sampling process towards a coherent direction. Moreover, RepG represents each class through a set of representative vectors containing features specific to that class. To control the optimal representative information, RepG
employs self-supervision as guidance model. The gradients derived using the pre-trained self-supervised model are directly integrated into the sampling process to facilitate feature tuning in the generated images. Extensive experimental results demonstrate that RepG achieves superior performance in image generation.

### Strengths
- The paper is clearly written and easy to follow
- The related work covers most of the relevant papers in the field
- Experimental validation is extensive and demonstrates the superiority of the proposed approach

### Weaknesses
 - Some details require more clarification

 Here are my concerns:
- Please provide more details on how the representative vectors in RepG capture more valuable information for generative tasks than the one-hot vectors used in classifier guidance.
- You stated in the paper that RepG modifies "faulty" features in the generated images. How does your appoach identify which features are faulty? It could be possible that some key features could be mistakenly modified, thus affecting the image quality?
- You mentioned in the paper that RepG is computationally efficient. Could you provide comparative metrics on the computational savings over traditional classifier-guided methods (including for instance image generation at different resolutions)?
- Definition 4.1: t1 and t2 should be consecutive time steps?
- Equation 13: In the denominator, the superscript of 'r' should be 'i', not 'c'.

### Questions
Here are my concerns:
- Please provide more details on how the representative vectors in RepG capture more valuable information for generative tasks than the one-hot vectors used in classifier guidance.
- You stated in the paper that RepG modifies "faulty" features in the generated images. How does your appoach identify which features are faulty? It could be possible that some key features could be mistakenly modified, thus affecting the image quality?
- You mentioned in the paper that RepG is computationally efficient. Could you provide comparative metrics on the computational savings over traditional classifier-guided methods (including for instance image generation at different resolutions)?
- Definition 4.1: t1 and t2 should be consecutive time steps?
- Equation 13: In the denominator, the superscript of 'r' should be 'i', not 'c'.

### Soundness
4

### Presentation
4

### Contribution
4
