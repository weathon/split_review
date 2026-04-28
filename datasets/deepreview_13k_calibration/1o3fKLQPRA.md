# DiffPath: Generating Road Network based Path with Latent Diffusion Model

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
With the increasing use of GPS technology, path has become essential for applications such as navigation, urban planning, and traffic optimization. However, obtaining real-world path presents challenges due to privacy concerns and the difficulty of collecting large datasets. Existing methods, including count-based and deep learning approaches, struggle with two main challenges: handling complex distributions of path segments and ensuring global coherence in generated paths. To address these, we introduce DiffPath, a path generation model based on Latent Diffusion Models (LDMs). By embedding path into a continuous latent space and leveraging a transformer architecture, DiffPath captures both local transitions and global dependencies, ensuring the generation of realistic paths. Experimental results demonstrate that our model outperforms existing approaches in generating paths that adhere to real-world road network structures while maintaining privacy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces DiffPath, a path generation model that uses a latent diffusion model (LDM) and a transformer to generate realistic synthetic road paths, addressing privacy concerns and data limitations in urban navigation and planning. DiffPath embeds discrete paths into a continuous latent space, allowing it to capture complex path distributions and ensuring coherence between adjacent and distant road segments. By incorporating a customized loss function, the model aims to generate paths with rare segments often missed by traditional methods. Experimental results on datasets from Chengdu and Xi’an show that DiffPath outperforms existing approaches in generating synthetic paths that align well with real-world road networks.

### Strengths
- This paper tackles a practical problem in the urban computing scenario. It aims to address privacy concerns and data limitations in urban navigation and planning, which is of high practical value.

- The paper proposes a unique angle that is overlooked in previous works. They tend to focus on the local smoothness of the path but lose global-level constraints.

- The paper is well-written and easy to follow.

### Weaknesses
 - The experiments conducted are not enough to evaluate the claimed advantages, i.e., generate more realistic paths, especially those low-frequency ones.

- The proposed method is rather straightforward. Moreover, I think using the transformer and diffusion modeling instead of autoregressive modeling are both vital for capturing long-range correlation within a path.

- Similarity matric seems to suffer from bias issues. What if the generated paths are all the same but highly similar to one ground truth?

### Questions
Please see my review above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces DiffPath, a framework aimed at addressing path generation using a latent diffusion model combined with a transformer. The authors highlight two key challenges in prior work on path generation: complex path distributions and ensuring global coherence in generated paths. They suggest that these issues can be addressed through the integration of latent diffusion models with a transformer architecture. The experimental results indicate that DiffPath performs well on two real-world datasets.

### Strengths
1. The methodology is straightforward and easy to follow.
2. The writing is clear and accessible.
3. The framework has good performance on real-world datasets.

### Weaknesses
1. The core contribution is confusing. This work seems to simply apply the diffusion transformer model on the path generation task without additional optimization specific to this task.
2. While the authors claim that the proposed model addresses the challenges of capturing complex path distributions and ensuring coherence in generated paths, there is a lack of experimental evidence and analysis to support these claims.

### Questions
1. What is the core contribution of this work?
2. How does the proposed framework tackle the claimed challenges?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents DiffPath to address the challenges of complex segment distribution in path generation and to ensure global consistency of the generated paths. Experimental results validate its effectiveness in generating realistic paths.

### Strengths
S1. The solution to the path generation problem offers a certain degree of protection for personal privacy.  
S2. This paper is the first to attempt the use of latent diffusion models, which excel in generative tasks, in the context of path generation, along with targeted design considerations.

### Weaknesses
W1. Compared to the de-identification of real path data, the issues of accuracy and computational complexity in path generation appear more complex and unreliable.  
W2. In related studies, the assumption of maintaining symmetry in the adjacency matrix of existing diffusion models may inaccurately represent one-way streets as bidirectional. This warrants a more in-depth discussion, as directed graphs do not necessarily require a symmetric structure in their adjacency matrices.  
W3. The legend does not correspond with the paper's description; please verify the relationship between paths P1 and P2 in Figure 2 and the accuracy of the related statement in line 64.  
W4. The ablation study analyzes replacing the Transformer with UNet but lacks a thorough analysis of the Diffusion module.  
W5. No reproducible code is provided, making it impossible to verify the validity of the research findings.

### Questions
Q1. Due to the errors in the legend and related descriptions, I do not understand why "P2 does not consider that selecting $v_4$ will result in a longer path to reach $v_7$." Is the distance from $v_2$ to $v_7$ indeed longer? More justification is needed to demonstrate that the generated path adheres to the constraints of the road network to substantiate this challenge.  
Q2. Diffusion-based models typically exhibit high complexity; how does the computational complexity of DiffPath compare to the baseline?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This study model path generation using diffusion model and take advantage of transformer architecture to consider the long-term input.

### Strengths
1. Propose transformer-based diffusion framework for path generation and validate on real-world dataset.

### Weaknesses
1. The motivation of this study is not convincing. In line 59, they claimed that “Another significant challenge in path generation for urban road networks is… because they do not conform to most situations in reality”, if the previous model is trained based on the real-world dataset, why do these models fail to capture suck kind of reality? Besides, it is also unclear how this study addresses the claimed challenge.
2. The novelty is limited compared with the previously proposed diffusion based trajectory generation method[1,2]. The difference between this study and the previous one is only that this study adopts transformer architecture. Moreover, how do this study ensure topology constraint during path generation is not convincing. They proposed to clamp the predicted latent state to the nearest valid road segment embedding. How can generation convergence is guaranteed under this kind of operation? Besides, this operation is not theoretically guaranteed to meet the topology constraint.
3. The experimental studies are not sufficient, for example, they don’t compare with other diffusion-based trajectory generation methods [1,2].

### Questions
None

### Soundness
1

### Presentation
2

### Contribution
2
