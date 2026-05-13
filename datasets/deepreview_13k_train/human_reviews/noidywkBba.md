# Chain-of-Focus Prompting: Leveraging Sequential Visual Cues to Prompt Large Autoregressive Vision Models

- Decision: Accept
- Scores: 5, 8, 8, 6

## Abstract
In-context learning (ICL) has revolutionized natural language processing by enabling models to adapt to diverse tasks with only a few illustrative examples. However, the exploration of ICL within the field of computer vision remains limited. Inspired by Chain-of-Thought (CoT) prompting in the language domain, we propose Chain-of-Focus (CoF) Prompting, which enhances vision models by enabling step-by-step visual comprehension. CoF Prompting addresses the challenges of absent logical structure in visual data by generating intermediate reasoning steps through visual saliency. Moreover, it provides a solution for creating tailored prompts from visual inputs by selecting contextually informative prompts based on query similarity and target richness. The significance of CoF prompting is demonstrated by the recent introduction of Large Autoregressive Vision Models (LAVMs), which predict downstream targets via in-context learning with pure visual inputs. By integrating intermediate reasoning steps into visual prompts and effectively selecting the informative ones, the LAVMs are capable of generating significantly better inferences. Extensive experiments on downstream visual understanding tasks validate the effectiveness of our proposed method for visual in-context learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Chain-of-Focus (CoF) Prompting as a method to enhance large autoregressive vision models (LAVMs) for in-context learning (ICL) in computer vision. Drawing inspiration from Chain-of-Thought prompting in natural language processing, CoF Prompting enables vision models to perform step-by-step visual comprehension. It tackles the lack of logical structure in visual data by generating intermediate reasoning steps based on visual saliency. CoF Prompting also facilitates the creation of customized prompts by selecting the most contextually relevant ones, based on query similarity and target richness. The effectiveness of this method is supported by extensive experiments, demonstrating that it significantly improves the models' ability to make inferences on visual understanding tasks, leveraging the recent advancements in LAVMs that utilize purely visual inputs for ICL.

### Strengths
- This paper introduces the interesting method of Chain-of-Focus Prompting, with strong and reasonable motivation. 

- The experiments are comprehensive.

### Weaknesses
 - Compared to previous work, such as "A Generalist Painter for In-Context Visual Learning," this paper only addresses two tasks: image segmentation and pose estimation. If this method does not work for other tasks, it could decrease the contribution of the paper.

- I am somewhat skeptical about why this method works. For instance, would the model perform equally well if it viewed the same number of images within reasoning steps (not randomly selected, such as viewing the same number of final step reasoning images)?

### Questions
- Would the model perform equally well if it viewed the same number of images within reasoning steps (not randomly selected, such as viewing the same number of final step reasoning images)?

- If you simply use this logic for Chain-of-Focus: each step of reasoning progresses from images of a single object to two, and then to multiple objects, where do you think the disadvantages lie compared to your method?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper propose Chain-of-Focus(COF) Prompting, which enhances vision models by enabling step-by-step visual comprehension. CoF automates prompt design by selecting the most relevant and informative prompts from existing candidates and creates intermediate reasoning steps for prompt targets. Experiments on various downstream vision tasks demonstrate the effectiveness of the proposed method.

### Strengths
This paper is well written. The methods are innovative, the experimental results are significant, and the visualizations are intuitive.

### Weaknesses
1. The candidate prompt pool comprises 50,000 training images and annotations, which raises concerns in specific scenarios due to its inability to ensure data privacy. Additionally, it necessitates significant resources for the storage and retrieval of prompts. The reliance on a large, fixed pool of prompts may limit the adaptability of the method to novel or rare visual concepts not well represented in the training data. Furthermore, the computational cost associated with searching through such a large pool during inference needs to be more thoroughly addressed.
2. Figure 3 does not include visualized results of the ground truth.
3. There is no comparison of the computational complexity and resource overhead of the different methods.

### Questions
Can CoF address the issue of distribution shift, that is, when there is no data related to the test data in the prompt pool?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper extends Large Autoregressive Vision Models (LAVMs) with the capability of in-context learning for visual inputs by proposing a chain-of-focus (CoF) prompting approach. The CoF decomposes a visual prompt to intermediate reasoning steps by ranking salient regions of the prompt image, as well as taking into account the visual similarity and annotation richness to the test image. The saliency scores are obtained by an off-the-shelf saliency detector. The relevance of queries is modeled by the Jaccard similarity index of the two sets of visual codebooks in VQ-GAN. The annotation richness is modeled by the number of unique indices in their codebooks. The proposed method has been evaluated on 4 vision tasks, e.g., image segmentation, object detection, image inpainting, and pose estimation, which show the effectiveness of the CoF prompting, upon two backbone LAVMs.

### Strengths
1) The proposed CoF prompting method is well motivated, which shall interest many ICLR attendants.
2) The proposed approaches, using the saliency score rank, the similarity of two sets of codebooks in VQ-GAN, are reasonable and easy to re-produce. 
3) The evaluation is fairly convincing to show the effectiveness of the proposed method, though not as significant as I expected.

Overall, this is a descent work which may deserve to share with the community in time.

### Weaknesses
1) The reasoning steps of 0, 1, 2 are evaluated in Fig.4. More steps (just 2) do not show clear advantage, which is a bit disappointing to validate the proposed CoF prompting. I wonder if just using more diverse visual prompts that are also relevant with enough annotations, the performance may match or even out-perform using intermediate reasoning steps of the visual prompts?  

2) The comparison baseline is a random selection scheme, which may be too simple. The performance gain over this simple baseline is not that significant as I expected.

3) The specific approaches, like the off-the-shelf saliency score and the number of unique indices in their codebooks, are somewhat simple and intuitive.

### Questions
Please discuss the pros and cons of using more diverse visual prompt images or more intermediate reasoning steps of one prompt image.

Any alternatives to the saliency scores to measure the reasoning steps? Some objects like faces, animals or intensive actions tend to capture visual attentions easily. 

Some relevant missing references, please discuss the differences:

Chain-of-Spot: Interactive Reasoning Improves Large Vision-language Models, 2024.
Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight, 2024.

What is the subtle difference between image relevancy and relevance? ll.140 => an image retrieval framework; ll.216, in Fig.2, => query relevance or relevance of the queries; => target informativeness or informativeness of task objectives? Btw: informative and informativeness are very vague terms, please define them first.

### Soundness
3

### Presentation
3

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
This paper aims to address an inherent challenge in the computer vision community, where, unlike language data, images lack clear logical structures. CoF prompting introduces intermediate steps in the visual learning process to enhance the ability of VLMs to understand and predict complex visual images. The authors propose using saliency maps to determine which parts of an image should be focused on sequentially, mimicking human cognitive processes. This method allows VLMs to perform better on fundamental vision tasks such as image segmentation, pose estimation, and object detection by progressively building a context around the test input. The authors comprehensively evaluated the proposed method across several models and datasets, with extensive experiments showing the efficacy of CoF prompting. It outperforms several baseline methods and demonstrates some improvements, such as Intersection over Union (IoU) and Pixel Accuracy (P-ACC). This paper also delves into ablation studies to assess the contributions of different components, providing insights into the role of cognitive reasoning, query relevance, and annotation diversity.

### Strengths
1. Innovative Adaptation of CoT for Vision: The introduction of Chain-of-Focus (CoF) prompting is a creative adaptation of chain-based reasoning, typically used in language models, for vision tasks. The authors contribute a novel and interesting insight into the inherent logical structures of images. Previously, we thought images contained visual redundancy, which was proposed and widely adopted in Masked Autoencoders pretraining. Such insights propose a new idea for visual modeling, which improves vision models to handle complex, multi-step tasks.

2. Comprehensive Evaluation: The authors conducted thorough experiments across various models (e.g., LLaMA-300M, LLaMA-1B, and LLaMA-7B) and tasks (e.g., segmentation, pose estimation, object detection). This robust evaluation not only demonstrates the generalizability of the approach but also its effectiveness across different settings.

3. Interesting Saliency-Based Reasoning: The use of visual saliency to create intermediate reasoning steps adds a cognitive layer to how models process visual data, mirroring human visual attention mechanisms. This results in more informed predictions, especially in tasks where spatial and object importance matters.

4. Detailed Ablation Studies: The authors provide detailed ablation studies, which highlight the relative importance of different components of the proposed method (cognitive reasoning, query relevance, and annotation diversity). This adds clarity to which parts of the model drive the most significant improvements.

### Weaknesses
1. Limited Exploration of Computational Complexity: While the method is novel, there is limited discussion on the computational overhead introduced by the saliency-based intermediate reasoning steps. Given that real-world applications demand efficient processing, an evaluation of the method’s scalability in terms of computational cost would have been valuable. Specifically, the paper lacks a detailed analysis of the time complexity associated with generating the saliency maps and processing them within the VLM. The authors should provide a breakdown of the time spent on each step, including saliency detection, prompt generation, and inference. Furthermore, memory usage should be analyzed, particularly when dealing with large image datasets or high-resolution images. This analysis should include the memory footprint of the saliency maps and the intermediate representations used during the chain-of-focus process. 

2. Generalization Across Different Vision Tasks: While CoF prompting is tested on several vision tasks, the experiments are focused on a few select tasks, mainly segmentation and pose estimation. Broader evaluation on a wider range of tasks, such as video understanding or 3D object recognition, would further validate the method’s versatility. The current evaluation does not adequately demonstrate the method's applicability to tasks that require temporal reasoning or understanding of 3D structures. For example, tasks like action recognition in videos or 3D object reconstruction would provide a more comprehensive assessment of the method's generalizability. Therefore, I strongly suggest the authors try some experiments on video understanding to further elaborate on the effectiveness and commonality of this method.

3. Handling Failure Cases: The authors acknowledge that VLMss can produce failures (such as pure black predictions), but the analysis of these failures remains surface-level. A deeper dive into understanding why these failures occur and how to mitigate them would strengthen the paper’s conclusions. The paper should include a more detailed analysis of the types of failures observed, such as incorrect segmentations, inaccurate pose estimations, or complete prediction failures. It would be beneficial to categorize these failures based on the characteristics of the input images or the generated prompts. Furthermore, the authors should explore potential mitigation strategies, such as incorporating error detection mechanisms or refining the prompt selection process. This part could be integrated into the Conclusion and Limitation section, and it will also inspire follow-up research.

4. Dependence on Saliency Detection: The success of CoF prompting is tied closely to the quality of the saliency detection model used. The authors briefly mention the model (U2-Net), but the sensitivity of the approach to variations in saliency detection quality is not explored. If the saliency model performs poorly, it could compromise the entire prompting process. The paper should include an analysis of how the performance of the CoF prompting method varies with different saliency detection models. It would be beneficial to evaluate the method using saliency maps generated by different algorithms, including those with lower accuracy or higher noise levels. This analysis would provide insights into the robustness of the approach to variations in saliency detection quality.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
3
