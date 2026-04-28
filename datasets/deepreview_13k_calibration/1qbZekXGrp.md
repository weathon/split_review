# Generation and Comprehension Hand-in-Hand: Vision-guided Expression Diffusion for Boosting Referring Expression Generation and Comprehension

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Referring expression generation (REG) and comprehension (REC) are vital and complementary in joint visual and textual reasoning.  Existing REC datasets typically contain insufficient image-expression pairs for training, hindering the generalization of REC models to unseen referring expressions. Moreover, REG methods frequently struggle to bridge the visual and textual domains due to the limited capacity, leading to low-quality and restricted diversity in expression generation. To address these issues, we propose a novel VIsion-guided Expression Diffusion Model (VIE-DM) for the REG task, where diverse synonymous expressions adhering to both image and text contexts of the target object are generated to augment REC datasets. VIE-DM consists of a vision-text condition (VTC) module and a transformer decoder. Our VTC and token selection design effectively addresses the feature discrepancy problem prevalent in existing REG methods. This enables us to generate high-quality, diverse synonymous expressions that can serve as augmented data for REC model learning. Extensive experiments on five datasets demonstrate the high quality and large diversity of our generated expressions. Furthermore, the augmented image-expression pairs consistently enhance the performance of existing REC models, achieving state-of-the-art results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores the integration of referring expression generation (REG) and comprehension tasks. To address challenges such as the scarcity of image-expression pairs in training data for REC and the limitations of the REG methods in bridging visual and textual domains, the authors propose a novel vision-guided expression diffusion model for REG. Extensive experiments demonstrate that the proposed method produces high-quality and diverse generated data.

### Strengths
1. The paper explores the potential of applying diffusion models to the REG task, an area that has been largely underexplored.
2. The authors introduce a vision-text conditioning module and a token selection strategy, which significantly enhance the alignment between visual and textual information.
3. Extensive experiments and ablation studies validate the generalization capability and effectiveness of the proposed method’s design choices.

### Weaknesses
1. In the visualization results shown in Figure 3, the response labeled as “recover” in the first sample of the third row appears to be an error, as does the response in the last sample of the same row. These results indicate that while the current method enhances diversity, it still includes some erroneous responses. How do you ensure the quality of the generated responses?
2. It is intriguing that the ViT backbone of CLIP is considered as a unified vision encoder in MLLM. Could this architecture produce different patterns and further improve performance?
3. The definition of CFG is missing in Table 1.
4. While the paper provides extensive interpretation of the experimental results, it lacks an in-depth analysis of the reasons behind the observed patterns in the results.
5. The writing is somewhat verbose. For instance, in Subsection 3.6, the second sentence is redundant as it repeats the information in the first sentence.
6. Some equations could be improved; for example, Equations 9 and 10 differ by only one symbol.
7. There are a few typos, such as a missing period on line 82 and an incorrect number on line 360.

### Questions
See weakness.

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
4

### Summary
This paper addresses referring expression generation (REG) and referring expression comprehension (REC). In particular, the paper proposes a method for REG that utilizes a language model with a diffusion model and experimental results for REC that augment the dataset with the REG method. The experiments are performed on five representative datasets, three RefCOCOs, Flickr30k, and Refclef, and show that the accuracy of the proposed method for REG is better than the existing methods and that the augmentation of the dataset by the proposed method contributes to multiple REC methods.

### Strengths
- To the best of the reviewer's knowledge, this is the first study to introduce language models using diffusion models into REG and REC.
- The proposed method has been evaluated using multiple datasets and multiple ablation studies, and has shown a certain degree of effectiveness.

### Weaknesses
 - The proposed method is composed of a straightforward combination of existing methods. The Cross-Attention and Token Selection Strategy that make up the proposed method, Vision-Text Condtion, are known to the community, and the Minimum Bayes Risk (MBR) and classifier-free guidance (CFG) that are ablated in Table 1 are not newly proposed in this paper. (In addition, the REG performance of VIE-DM w/o CFG is reported as an ablation study, but the author forgot to explain what CFG stands for, so it is only the reviewer's guess that CFG means classifier-free guidance.)
- As mentioned in the Introduction, the existing methods compared in this paper adopt the transformer-LSTM or CNN-LSTM framework. In other words, the proposed method differs from other methods not only in that it formulates a language model using a diffusion model, but also in that it uses a transformer-based decoder. It is not clear how the combination of a transformer-based decoder and diffusion model outperforms only a transformer-based decoder. Without this comparison, it is not possible to show the effect of introducing a diffusion model into REG.
- In line 416, it is claimed that “These results demonstrate the robust data diversity and quality of our VIE-DM.” However, it is misleading to make such a claim of diversity based on Table 1, which discusses the similarity to the ground truth using Meteor and CIDEr. The argument regarding Table 3 is more convincing, so this claim should have been made elsewhere.
- As the authors acknowledge, Table 5 shows that augmenting the REC data using VIE-DM only leads to a limited improvement due to the accuracy of the synthesized expressions. Therefore, it is essential to show whether VIE-DM is superior to existing approaches. On the other hand, it is not clear how much accuracy is improved when the data set is augmented using methods other than VIE-DM. The idea of amplifying REC data using REG methods has already existed since [Mao+, CVPR 2016]. If it is not possible to show how much REC accuracy is improved when expressions are augmented using methods other than VIE-DM, it will not be possible to understand the extent to which this paper contributes to REC.

### Questions
The reviewer would like to receive responses from the authors about the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the Vision-guided Expression Diffusion Model (VIE-DM) to address limitations in referring expression generation (REG) and comprehension (REC) tasks, particularly the scarcity and low diversity of image-expression pairs in existing datasets. The model includes a vision-text condition (VTC) module and a token selection mechanism to mitigate feature discrepancies between the visual and textual domains.

### Strengths
1. Introducing a diffusion model to REG is innovative. VIE-DM generates diverse, high-quality synonymous expressions that align with both the visual and textual context of target objects, enriching REC datasets.
2. The experimental design is well-structured, including ablation studies. Extensive experiments on five datasets demonstrate significant improvements in REC and REG model performance, achieving state-of-the-art results.
3. The paper is clearly written and easy to follow.

### Weaknesses
No obvious disadvantages were seen.
Like any research work, this paper likely has its own limitations, though they are not explicitly discussed. Including a section on potential limitations would provide a more balanced perspective.

### Questions
See weakness.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Existing REC datasets often contain insufficient semantic pairs for training, hindering the REC model's generalization to unseen referring expressions. Additionally, REG methods, due to limited capacity, frequently struggle to bridge the visual and textual domains, resulting in low quality and diversity of generated expressions. In this work, the authors introduce diffusion models into the referring expression generation task, aligning visual features of varying granularity with noisy text. The experiemts are conduted on benchmark datasets.

### Strengths
The method is described in detail, and the motivations are fairly well-founded.

### Weaknesses
1. Some recent representative works, such as CCL[1], are not compared, even though these works use similar ideas to enhance REC performance through REG.
[1] Cycle-Consistency Learning for Captioning and Grounding. AAAI 2024.
2. Failure cases are lacking; diffusion data generation is usually unstable, and the authors need to analyze this point.
3. Statistics on model parameters, training time, and inference time are required.

### Questions
1. Why does performance on certain metrics improve after losing CFG in Table 1?
2. What is the number of samples in each augmented dataset? This needs to be reported.

### Soundness
2

### Presentation
3

### Contribution
2
