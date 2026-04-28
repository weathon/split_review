# StyleGuide: Crafting visual style prompting with negative visual query guidance

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 5, 6

## Abstract
In the domain of text-to-image generation, diffusion models have emerged as powerful tools. Recently,  studies on visual prompting, where images are used as prompts, have enabled more precise control over style and content. However, existing methods often suffer from content leakage, where undesired elements from the visual style prompt are transferred along with the intended style (content leakage). To address this issue, we 1) extends classifier-free guidance (CFG) to utilize swapping self-attention and propose 2)negative visual query guidance (NVQG) to reduce the transfer of unwanted contents. NVQG employ negative score by intentionally simulating content leakage scenarios which swaps queries instead of key and values of self-attention layers from visual style prompts. This simple yet effective method significantly reduces content leakage. Furthermore, we provide careful solutions for using a real image as a visual style prompts and for image-to-image (I2I) tasks. Through extensive evaluation across various styles and text prompts, our method demonstrates superiority over existing approaches, reflecting the style of the references and ensuring that resulting images match the text prompts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper sets the new state-of-the-art method for image generation tasks given visual style prompts. This paper mainly addresses the content leakage issue by incorporating swapping self-attention in CFG and utilizing negative visual guidance. More specifically, the improved CFG ensures the balance between style and content, and using negative visual guidance suppresses the content leaking into the generated image. Further, stochastic encoding and color calibration tricks are introduced to improve the generation quality.

### Strengths
- The quantitative and qualitative assessments showcase the superior effectiveness of the method proposed.

- The intuitive and effective negative visual guidance proposed serves to prevent content leakage.

- Comprehensive experiments are carried out to aid readers in understanding the proposed pipeline and key components.

### Weaknesses
 - Certain design decisions (such as determining the optimal layers for balancing style and content, exchanging self-attention, and color calibration) exhibit effectiveness but lack in-depth analysis or theoretical derivation.

- I would appreciate seeing quantitative ablation studies to further illustrate the effectiveness of stochastic encoding and color calibration. Do they play the most crucial role in the end outcomes? If that is the case, the effectiveness of self-attention swapping in CFG and the use of negative visual guidance diminishes. Furthermore, since they could potentially be integrated into other diffusion-based techniques, exploring their utility in other methods would be interesting.

- Typo correction: Line 18 employ -> employs.

### Questions
It would be great if the weaknesses raised above could be addressed in the rebuttal.

### Soundness
3

### Presentation
3

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
This paper focuses on Style Transfer using diffusion-based models, in which a style given by a reference image is transferred to the input image (e.g., transferring the "polygon" style in the reference image to a photo of a dog).
To that end, this paper conducts an extensive study on each component of diffusion-based models (e.g., classifier-free guidance, negative prompts, etc.) to propose a final approach that achieves state-of-the-art performance in style transfer.

### Strengths
- Overall, style transfer is a popular topic in the Image Editing community with many useful applications.
- This paper carries out thorough studies and proposes a method to prevent content leakage based on the insights. I think both the insights and the proposed method are useful to readers, as "content leakage" is a common problem in many image editing/manipulation methods.

### Weaknesses
I find it unclear how competitive the proposed method is compared to existing work (e.g., StyleDrop). I also wonder if inference time might limit this approach, as it involves multiple steps. Furthermore, with each new {reference style, input image} pair, all these steps need to be repeated.

### Questions
I’m inclined to accept this paper due to its superior quantitative results, it'd be much appreciated if authors can clarify in the rebuttal about training/ inference of proposed methods vs. existing works.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper propose visual style prompting which receives a text prompt and a visual style prompt to generate new images. Specificaly, this method utilize classifier-free guidance conbined with swapping self-attention to achieve style transfer, and use negative visual query guidance (NVQG) to reduce the transfer of unwanted contents. Extensive experimental verification on both T2I  and I2I has validated the effectiveness of this method.

### Strengths
- This paper is well written and easy to follow

- This method is training-free and achieves outstanding preference for style transfer without content leakage

- The experiments and analysis are thoroughly reasonable and justified

### Weaknesses
 - The methods employed for comparison by the author appear somewhat outdated. Stylization is a rapidly evolving field, as demonstrated by the recent emergence of models such as DEADiff, InstantStyle(-Plus), and CSGO this year. To validate the effectiveness of the proposed approach and assess the issue of content leakage, it is essential to compare it comprehensively with these state-of-the-art techniques.

- Furthermore, the computational efficiency of the algorithm has not been sufficiently analyzed. Given that the method involves multiple attention computations among latent variables, a fair comparison of runtime and memory usage with other methods is essential to assess the feasibility of the proposed approach.

### Questions
- In the recently mentioned approaches (such as DEADiff, InstantStyle(-Plus), and CSGO), I haven’t noticed any significant content leakage. Have you verified whether this issue occurs in those methods as well? A direct comparison with these models would help emphasize the strengths of your own approach.

- I also recommend incorporating a few quantitative metrics to evaluate the effectiveness of style transfer. While you don’t need to include many metrics, incorporating some quantitative ones is necessary to validate the effectiveness of the method objectively. Relying solely on selected images can be misleading, as they may have been cherry-picked to showcase the best results.

- Additionally, further experimental analysis on computational efficiency is advised to provide a more comprehensive evaluation of the method.

I will revise my rating according to the author's feedback and the reviewer's discussion.

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
This paper introduces innovative methods in text-to-image generation, addressing content leakage issues in existing approaches. The authors extend classifier-free guidance (CFG) with swapping self-attention and propose negative visual query guidance (NVQG) to reduce unwanted content transfer. These methods are simple yet effective, achieving precise control over style and content. Extensive evaluations demonstrate the superiority of the proposed methods, ensuring generated images reflect the reference style and match text prompts. Overall, the paper presents significant improvements, providing a solid foundation for future work and practical applications.

### Strengths
- The paper is logically structured, providing a thorough analysis of the content leakage issue in style transfer. It proposes the NVQG method to address this problem, thereby improving the quality of generated images. 
- The experiments are detailed, with extensive comparative experiments and visual analyses supporting the main contributions of the paper.

### Weaknesses
 - The proposed CFG with swapping self-attention and  NVQG  in the paper mainly combines previous work, which shows a slight lack of innovation. Additionally, the derivation of equations in section 2.2 is not sufficiently clear.
- Writing and structure: inconsistent terminology usage, NVQG in introduction and NVG in section 3; the layout of Figures 3 and 4 is not aligned; a large number of instances in the formulas where K and V are combined, making it difficult to understand.
-  Experiments comparision on I2I task did not include some of the latest methods of style transfer, such as InstantStyle, InstantStyle-Plus.

### Questions
- In the experiments regarding content leakage, the comparison with other models mainly involves qualitative analysis through visualization of certain examples (Figure 7, 10). However, in fact, this paper uses quantitative metrics in Figure 5 to evaluate content leakage. I am curious why these metrics were not used to assess content leakage across different models, considering that content leakage is the main issue this paper aims to address.

### Soundness
3

### Presentation
3

### Contribution
3
