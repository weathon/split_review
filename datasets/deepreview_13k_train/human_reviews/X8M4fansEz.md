# Story-Adapter: A Training-free Iterative Framework for Long Story Visualization

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Story visualization, the task of generating coherent images based on a narrative, has seen significant advancements with the emergence of text-to-image models, particularly diffusion models. 
However, maintaining semantic consistency, generating high-quality fine-grained interactions, and ensuring computational feasibility remain challenging, especially in long story visualization (\textit{i.e.}, up to 100 frames).  
In this work, we propose a training-free and computationally efficient framework, termed \textbf{Story-Adapter}, to enhance the generative capability of long stories. 
Specifically, we propose an \textit{iterative} paradigm to refine each generated image, leveraging both the text prompt and all generated images from the previous iteration. 
Central to our framework is a training-free global reference cross-attention module, which aggregates all generated images from the previous iteration to preserve semantic consistency across the entire story, while minimizing computational costs with global embeddings. This iterative process progressively optimizes image generation by repeatedly incorporating text constraints, resulting in more precise and fine-grained interactions. 
Extensive experiments validate the superiority of Story-Adapter in improving both semantic consistency and generative capability for fine-grained interactions, particularly in long story scenarios.
The project page and associated code can be accessed via~\href{https://jwmao1.io/storyadapter/}{this https URL}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a training-free method for the story visualization task, where an iterative paradigm is implemented to continuously refine previously generated images with the help of a proposed global reference cross-attention module. Both qualitative and quantitative results show that the proposed method effectively improves consistency between frames in a story.

### Strengths
1. The proposed method is training-free and requires few computational resources to generate long stories.

2. The introduced reference cross-attention module is general and could potentially be adopted in other existing story visualization models.

3. A human evaluation was conducted to further assess the effectiveness of the proposed method.

### Weaknesses
1. I am concerned about the effectiveness of the proposed method. As shown in the paper, the method is training-free, and the consistency between different frames in a story relies primarily on the proposed global reference cross-attention (GRCA) module. According to Eq. (1), there is no connection between frames during initialization, and each image frame is generated independently, as x^i=0_k is generated solely from its corresponding text T_k. It is unclear how the GRCA can significantly adjust each image frame to achieve consistent characters and background images. It might be better to include the initialisation images in the paper, and also some discussion about the such powerful capabilities of GRCA.

2. The idea of using global reference cross-attention to incorporate global features into generation does not appear entirely novel. It utilizes global features, which primarily address global consistency between image frames but have limited impact on regional details. Consequently, issues with regional consistency, such as closed-eye issue (L 421), may also be a limitation of the proposed method.

3. How did the authors choose the lambda values in Eq. (4)? Table 3 suggests a tradeoff between text-image alignment and image consistency when adjusting the lambda value.

### Questions
See above weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the Story-Adapter framework, a training-free approach aimed at enhancing long story visualization in computer vision. The proposed method focuses on achieving high semantic consistency and generating intricate character interactions across extended narratives (up to 100 frames) without additional training. The core components include an iterative paradigm and a Global Reference Cross-Attention (GRCA) module. These features enable the model to maintain coherence across all frames by iteratively refining generated images, with GRCA ensuring that each new frame adheres to the global semantic context established by preceding frames.

### Strengths
1. The plug-and-play nature of Story-Adapter allows it to integrate seamlessly with existing pre-trained Stable Diffusion models, offering a practical solution for enhancing model performance without extensive retraining.

2. The framework's iterative approach provides a mechanism to enhance narrative consistency and visual quality over successive iterations, improving fine-grained interactions and maintaining semantic consistency.

3. GRCA reduces computational overhead by leveraging global embeddings, making Story-Adapter suitable for long story visualizations with minimal additional memory usage.

### Weaknesses
1. The novelty of this paper is somewhat limited.

2. The paper is overall hard-to-follow. For example, Eq. 3 is so confusing and lacks clarity in terms of implementation details. The left-hand variables in the first three lines are identical, which raises questions about potential typographical errors.

3. In generating each frame of the story, is the reference image derived from the one frame from the previous round only, or from all images generated in the previous round? If the former, it remains unclear how multiple rounds of using the same image can maintain character consistency across the story. If the latter, as the story progresses and new characters are introduced, how is it ensured that characters who appear less frequently are not overlooked?

4. In Fig. 3, different colors denote different characters. Is a masking mechanism applied for each character to distinguish them? If not, how is it ensured that information about each character can be accurately extracted using global reference cross-attention?

5. Although Fig. 5 highlights the advantages of this method compared to StoryDiffusion, these advantages are less pronounced in Figure 14. For instance, in Figure 14, the male characters appear highly similar. For example, the crew member in the third frame, the captain in the fourth frame, and the adult character 1900 in subsequent frames look nearly identical.

6. Adding a discussion section on the limitations of the proposed method would strengthen the paper's argument.

7. There are some training-free methods that deserve to be discussed.

	a) Cao M, Wang X, Qi Z, et al. Masactrl: Tuning-free mutual self-attention control for consistent image synthesis and editing[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023: 22560-22570.

	b) Tewel Y, Kaduri O, Gal R, et al. Training-free consistent text-to-image generation[J]. ACM Transactions on Graphics (TOG), 2024, 43(4): 1-18.

	c) He H, Yang H, Tuo Z, et al. DreamStory: Open-Domain Story Visualization by LLM-Guided Multi-Subject Consistent Diffusion[J]. arXiv preprint arXiv:2407.12899, 2024.

	d) Cheng J, Lu X, Li H, et al. AutoStudio: Crafting Consistent Subjects in Multi-turn Interactive Image Generation[J]. arXiv preprint arXiv:2406.01388, 2024.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a training-free framework Story-Adapter to achieve consistent image generation. Instead of relying on static reference images, this work incorporates all images generated in previous iterations (in a dynamic manner) into the current iteration, which is achieved through global reference cross-attention. The method adopts an iterative paradigm. For initialization, only the corresponding prompts are used to generate images, just like regular text-to-image generation. Then, all images generated in the previous round are used to update the current generation. Specifically, all images in the previous round are projected into the image tag and used as K and V to calculate a new set of intermediate features, which are finally weighted and summed into the final features.

### Strengths
- Consistent generation, or story generation is a good task with many real-world applications.
- This approach is training-free and can be easily applied into existing framework.

### Weaknesses
- The novelty is quite limited, this is exactly IP-Adapter, but just wrap it up as a storytelling story. The only difference is that it uses all previous images as references.
- It does not make sense to use all previous images as references, if some images are irrelevant to the current generation, it may become a noisy reference and harm the current generation. There is no discussion on how to select reference images adaptively.

### Questions
- Since the framework is basically the same as IP-Adapter, it is valuable to discuss how to adaptively select the reference image.
- Also, it would be interesting to discuss what the real obstacles to achieving consistent generation are, is a CLIP representation enough for detail consistency? If not, if some other representations like DINO-V2 help?

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a framework aimed at improving the quality and consistency of visualizations for stories, especially long stories, using diffusion models. Traditional models often struggle with maintaining semantic consistency and intricate interactions as story length increases. To address this, the authors propose Story-Adapter as a training-free iterative approach.

Story-Adapter features a unique Global Reference Cross-Attention (GRCA) mechanism, which helps maintain consistency across images by using global embeddings from all previously generated frames. Story-Adapter updates each frame iteratively by considering all previous results, performing better in consistency and coherence compared with previous methods.

Experiments show that Story-Adapter outperforms existing methods like StoryGen and StoryDiffusion in both standard and longer story tasks when using CLIP-T, aCSS and aFID as the benchmark.

### Strengths
1. Iterative Enhancement: Unlike previous works that primarily focus on direct generation of consistent results, Story-Adapter leverages iterations as a key dimension for enhancing quality.
2. Detailed Description of Differences: The paper thoroughly analyzes previous works, highlighting their drawbacks and clearly articulating the distinctions between their contributions and those of others.
3. Clear and Concise Expression: The paper articulates complex ideas with clarity, supported by detailed images and diagrams that enhance understanding and reinforce the technical explanations.
4. Comprehensive Experiments and Ablation Studies: The paper includes thorough experimental evaluations and well-structured ablation studies for each module, effectively validating the system's design and performance.
5. Detailed Formulas and Algorithms: The paper provides clear formulas and algorithms to eliminate ambiguity.

### Weaknesses
1. Comparison with Baseline for Regular-length Stories: The paper utilizes IP-Adapter as a key component of the method, making it crucial to include IP-Adapter as a baseline for comparison. While the authors do provide this comparison for long story visualizations in Table 2, it is notably absent for regular-length stories in Table 1.
2. Analysis of Iterative Generation: Iterative generation appears to be a significant differentiator between Story-Adapter and IP-Adapter. However, there is no curve of the performance changes over iteration epochs. The authors should consider including this as part of their experimental evaluation.
3. Insufficient Analysis of Computational Costs: The authors analyze the computational cost between Story-Adapter and StoryDiffusion, yet they do not account for the multiple epochs required for Story-Adapter's generation in their cost calculations. It would be beneficial to present the time consumption explicitly as an additional column in Tables 1 and 2.
4. Ambiguity in Figure 3: The presence of the white and purple masks in the bottom right corner of Figure 3 may create confusion regarding the existence of attention masks.

### Questions
In addition to the weaknesses mentioned, I have another one question.

Your method depends on initialization to generate a fixed character. How does the choice of initialization affect the robustness of the method? For instance, if the initialization produces significantly different images, can Story-Adapter still converge to a consistent character in a relatively short time?

I hope the authors can make up for the weaknesses mentioned and address these questions.

### Soundness
3

### Presentation
3

### Contribution
3
