# RACCooN: A Versatile Instructional Video Editing Framework with Auto-Generated Narratives

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Recent video generative models primarily rely on carefully written text prompts for specific tasks, like inpainting or style editing. They require labor-intensive textual descriptions for input videos, hindering their flexibility to adapt personal/raw videos to user specifications.
This paper proposes \textbf{\method}, a versatile and user-friendly \textbf{video-to-paragraph-to-video} generative framework {that supports multiple video editing capabilities such as removal, addition, and modification, through a unified pipeline.} 
\method consists of two principal stages: \textit{Video-to-Paragraph} (V2P) and \textit{Paragraph-to-Video} (P2V). 
In the V2P stage, we automatically describe video scenes in well-structured natural language, capturing both the holistic context and focused object details. 
Subsequently, in the P2V stage, users 
can optionally refine these descriptions to guide the video diffusion model, enabling various modifications to the input video, such as removing, changing subjects, and/or adding new objects.
The proposed approach stands out from other methods through several significant contributions:
(1) \method suggests a multi-granular spatiotemporal pooling strategy to generate well-structured video descriptions, capturing both the broad context and object details without requiring complex human annotations, simplifying precise video content editing based on text for users.
(2) Our video generative model incorporates auto-generated narratives 
or instructions to enhance the quality and accuracy of the generated content. (3) RACCooN also plans to imagine new objects in a given video, so users simply prompt the model to receive a detailed video editing plan for complex video editing.
The proposed framework demonstrates impressive versatile capabilities in video-to-paragraph generation (up to $9.4\%p \uparrow$ absolute improvement in human evaluations against the baseline), video content editing (relative $49.7\% \downarrow$ in FVD), and can be incorporated into other SoTA video generative models for further enhancement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper targets video editing by proposing a video-to-paragraph-to-video pipeline. The editing is achieved based on the modification of the paragraph.  
The contribution lies in (1) a novel video editing pipeline, and the editing is based on detailed text descriptions, which is user-friendly. (2) improved detailed video captioning performance by a novel multi-granular pooling. (3) A new dataset with high-detailed captions and object caption-mask pairs to facilitate this framework.

### Strengths
- The pipeline for video editing is novel and intuitive. The idea of leveraging the recent development of MLLMs to tackle video editing tasks is interesting.  
- The experiments are comprehensive. The results of single object prediction are good and outperform some strong baselines. The results of video editing show remarkable improvement.  
- The source code is provided in the supplementary materials.
- The method can be integrated with an inversion-based video editing method, and the results are provided.   
- Limitations are discussed.

### Weaknesses
The author can consider providing more video results to demonstrate the actual editing performance in different settings. For example, the video comparison results with Fatezero and Token flow. Also the results of the proposed method with VideoCrafter and DynamiCrafter.

### Questions
The text encoder used for P2V is Clip? Does the max token length be smaller than the input token length? Since the paragraph description is very long, it may exceed the maximum token length of the text encoder. If so, will the information lost will affect the generation sematics?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces a novel approach for video editing that includes both Video-to-Paragraph (V2P) and Paragraph-to-Video (P2V) methodologies. Initially, the V2P method converts video content into a descriptive paragraph. Subsequently, users can edit this textual representation to facilitate video object addition, removal, and modification. Experimental results demonstrate that our approach outperforms existing state-of-the-art methods in the field.

### Strengths
- The proposed Video-to-Paragraph (V2P) method serves as an effective video captioner, capable of capturing multi-granular spatiotemporal features.
- This framework achieves state-of-the-art performance in video editing tasks.
- A novel dataset is introduced, which can be used as a benchmark for video editing, which contains 7.2K high-quality detailed video paragraphs and 5.5K object-level detailed caption-mask pairs.

### Weaknesses
1. The proposed editing approach heavily relies on the accuracy of the Video-to-Paragraph (V2P) method, leading to potentially unnatural modifications. 
   - (1) For video object removal and modification, if the paragraph does not mention a specific object (e.g., in the description of Figure 4, the absence of the female character’s earrings), it raises the question of how to effectively remove or modify that object.
   - (2) While adding objects does not depend on the paragraph's accuracy, it is unclear how to control the timing of additions through text. The mechanism for locating the spatiotemporal position of the mask for object addition is lacking in detail. Is the layout determined using a large language model (LLM), or is there another implementation?
   - (3) The textual descriptions lack a temporal dimension, making it difficult to achieve fine-grained control over video content, such as adding objects at specific time intervals or altering object attributes over time.
   - (4) There is no comparison of the Video-to-Paragraph method with more advanced video LLM techniques. In the single object prediction task, there is a lack of comparison with state-of-the-art methods like Video-Chat2 and Video-LLaVA.
   - (5) While the editing pipeline boasts high accuracy, it is not user-friendly. Unlike methods such as Instruct Pix2Pix, which allow for straightforward edits, this approach requires modifications to the existing paragraph.


2. The multi-granular pooling strategy lacks ablation studies, which are necessary to evaluate its effectiveness.

Additonal discussion:
For image editing, the workflow of converting images to text and then modifying through text works well; however, video editing inherently requires temporal control, and the current approach lacks mechanisms for time-based edits and fine-grained temporal adjustments—an essential aspect of video manipulation.

The pipeline could benefit from further streamlining. Ideally, users would simply input a high-level instruction, and the remainder of the editing process would be handled by the LLM, removing the need for users to read and modify the paragraph directly.

### Questions
See Weakness.

### Soundness
3

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
5

### Summary
This work presents RACCooN, a video-to-paragraph-to-video generative framework designed to simplify video editing by automatically generating structured textual descriptions of video scenes. The process involves two main stages: V2P, which captures both the overall context and detailed object information, and P2V, where users can refine these descriptions to direct modifications to the video.

### Strengths
+ The paper is well-written and easy to understand, and the research questions are quite interesting.
+ The experimental results are relatively sufficient.

### Weaknesses
- The research goal of this work is not focused. The original objective is to address video editing, but in practice, it is solving the problem of video captioning.
- The method lacks some technical innovations. The approach to video editing can be summarized as text-based video inpainting, but it seems that there is no focused and innovative design specifically tailored to this goal.

### Questions
+ Calculating complexity. Video editing tasks can be very simple, but RACCooN complicates this process. Why is a caption model needed as a preprocessing step?
+ I think this work lacks two important baselines: 1) annotating the training set using the VLM from this paper; 2) annotating the training set using other state-of-the-art methods like GPT-4V. Then, we can train a model using Tex+Mask+Video. I believe the performance won't be worse, and this result could likely demonstrate that we do not need the V2P process.
+ Regarding multi-granular pooling, these three dimensions appear to be straightforward and commonly used and are insufficient to support the technical innovations presented in this work.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces RACCooN, a video-to-paragraph-to-video framework for enhancing video editing without the need for labor-intensive text prompts. It operates in two main stages: Video-to-Paragraph (V2P), which automatically generates natural language descriptions of video, and Paragraph-to-Video (P2V), where users can modify the descriptions to guide the video editing process.

### Strengths
1. The illustration figures are informative and help to understand the paper;
2. The experiment section provides detailed evaluations;
3. The supplementary materials help to understand the implementation and technical details.

### Weaknesses
1. The overall framework looks like a straightforward combination of a video understanding MLLM and a video editing diffusion model, and most of the techniques have been intensively explored by previous literature (e.g., the instruction tuning and training of the inpainting model). Thus, the core technical contribution is questionable.

2. I don't follow the formulation of the proposed instruction-based video editing task. Why it would be better to edit a video with intermediate text descriptions as a proxy, compared to directly providing pixel-level instruction?

3. For video editing evaluation, how are the videos selected, and how large is the evaluation set? Also, why it's necessary to evaluate PSNR and SSIM for video editing?

4. As an important component, there lacks an in-depth ablation study on the effects of the MGS pooling.

### Questions
1. What does "oracle mask" in ablation study mean?

2. How are the masks for video inpainting generated? Please consider attaching some results of the mask If it's produced by the LLM.

### Soundness
3

### Presentation
2

### Contribution
3
