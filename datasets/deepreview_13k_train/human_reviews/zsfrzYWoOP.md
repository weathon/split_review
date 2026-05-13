# FABRIC: Personalizing Diffusion Models with Iterative Feedback

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
In an era where visual content generation is increasingly driven by machine learning, the integration of human feedback into generative models presents significant opportunities for enhancing user experience and output quality.
    This study explores strategies for incorporating iterative human feedback into the generative process of diffusion-based text-to-image models.
    We propose FABRIC, a training-free approach applicable to a wide range of popular diffusion models, which exploits the self-attention layer present in the most widely used architectures to condition the diffusion process on a set of feedback images.
    To ensure a rigorous assessment of our approach, we introduce a comprehensive evaluation methodology, offering a robust mechanism to quantify the performance of generative visual models that integrate human feedback. 
    We show that generation results improve over multiple rounds of iterative feedback through exhaustive analysis, implicitly optimizing arbitrary user preferences.
    The potential applications of these findings extend to fields such as personalized content creation and customization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel method to control diffusion models to generate user-preferred images through iterative feedback. This method is based on augmenting the attention module. The proposed method is training-free and model-agnostic (as long as attention plays a core role in the image generation model), and can generate images based on any user preferences by having them provide positive and negative labels of their preference on images.

### Strengths
- The proposed technique is model-free and training-agnostic, and is easily applicable to most attention-based image generation methods.

- The proposed technique surpasses baselines and enable existing models to follow preferences reasonably

- Extensive exploration of important parts of the proposed technique: the trade-off between diversity and quality, and the effects of adjusting feedback strength on PickScore.

### Weaknesses
 - **Limited technical novelty**: While the proposed method is effective in incorporating user feedback, the extension to enabling 'iterative feedback' is rather naive, and the feedback is constrained to binary labels (which the author(s) have acknowledged as a limitation). The iterative feedback mechanism, relying on simple sequential application of the same feedback process, lacks sophistication. It would be more interesting to explore more advanced ways of users' feedback across multiple rounds, such as adaptive feedback strength or incorporating memory of past feedback, and incorporating other modalities, such as text explanations beyond binary preferences, or even more nuanced forms of feedback such as bounding boxes or segmentation masks.

- **Lack of human rating in a paper focused on iterative human feedback**: While the author(s) have used reasonable proxy to evaluate the effectiveness of the model in following human preferences, it would strengthen the paper if the author(s) can include some form of user study, given this papers' focus is in incorporating human feedback in the image generation process. The current evaluation, relying on PickScore, does not fully capture the nuances of human interaction and preference in an iterative setting. A user study could reveal usability issues or unexpected behaviors that are not captured by automated metrics.

- **Missing discussion to some prior work**: I believe the proposed method has some technical similarity to prompt-based image editing methods, such as instruct-pix2pix [1] and prompt2prompt. [2] While the proposed method is different in the types of feedback and preference investigated, it would be great if the author(s) can systematically compare and survey related techniques that use attention map for feedback and/or image editing. I also have some doubts about whether it is reasonable to claim that the method "outperformed" supervised-learning baselines (HPS), see question below.

### Questions
- While the paper claims to outperform a supervised-learning baseline (HPS LoRA), it is unclear to me how does HPS relate to PickScore, as they both appear to measure human preference. Would the author(s) please clarify how might they relate to each other? As the models are evaluated on PickScore but LoRA-tuned on HPS.

- How does the method relate to/differ from prompt2prompt and instruct-pix2pix? As stated above, it would be helpful to systematically compare them (and other related prior work) in a table.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a training-free method for text-to-image generation with iterative feedback, which is a novel and useful tool. The FABRIC framework is proposed and experiments are well-designed, showing the effectiveness of the method.

### Strengths
1. The paper proposes a very interesting and practically meaningful topic.
2. The method design is reasonable, which utilizes the power of self-attention in Stable Diffusion.
3. Despite this is the first training-free iterative-feedback generation work, it designs interesting and sound experiments.
4. The proposed method has great potential to optimize a lot of tasks based on Stable Diffusion.

### Weaknesses
The weakness of the paper mainly lies in writing. It is better to incorporate more method descriptions, including model design and formulations in the main script instead of the appendix.

### Questions
I'd like to accept this paper if the writing problem is addressed.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the growing field of machine learning-driven visual content generation, integrating human feedback can greatly enhance user experience and image quality. This study introduces FABRIC, a method that uses the self-attention layer in popular diffusion-based text-to-image models to condition the generative process on feedback images without additional training. Through a thorough evaluation methodology, the study demonstrates that iterative human feedback significantly improves generation results, paving the way for personalized content creation and customization.

### Strengths
1. Iterative Workflow: The research emphasizes an iterative process, allowing for continuous refinement and improvement of generated images based on previous feedback.
2. Dual Feedback System: By utilizing both positive and negative feedback images from previous generations, the method provides a balanced approach to influence future image results.
3. Reference Image-Conditioning: This approach manipulates future results by conditioning on feedback images, offering a dynamic way to steer the generative process.
4. Enhanced User Experience: By integrating human feedback into the generative models, the research ensures a more tailored and enhanced user experience in visual content generation.
5. Potential in Personalized Content Creation: The findings have significant implications for creating personalized visual content based on individual user preferences and feedback.

Overall, the paper introduces a robust and flexible method for refining machine-generated visual content through iterative human feedback, ensuring better alignment with user preferences.

### Weaknesses
1. Limited Expansion of Distribution: The method struggles to widen the distribution beyond the initial text-conditioned one provided by the model. This is a significant limitation as it restricts the exploration of the latent space and the generation of novel images that deviate from the initial text prompt. The feedback mechanism, while effective in refining existing outputs, does not inherently encourage the discovery of new modes within the data distribution.
2. Feedback Loop Limitation: Since the feedback originates from the model's output, it creates a cyclical limitation where the model might only reinforce its existing biases. This self-referential feedback loop could lead to a narrowing of the generated image space, as the model becomes increasingly attuned to its own outputs rather than exploring the full range of possibilities within the desired distribution. This could also amplify any biases present in the initial model.
3. Diversity Collapse: As the strength of the feedback and the number of feedback images increase, the diversity of the generated images tends to diminish. The images tend to converge towards a single mode that closely resembles the feedback images. This is a critical issue, as it undermines the generative capacity of the model, limiting its ability to produce a variety of outputs and potentially leading to a lack of creative exploration.
4. Binary Feedback System: The current feedback collection method only allows users to provide binary preferences (like/dislike) for the images. This limitation prevents users from providing nuanced feedback about specific aspects of an image. The lack of granularity in feedback restricts the model's ability to learn complex user preferences and fine-tune its output accordingly.
5. Lack of Detailed Feedback: Users cannot specify which particular aspects of an image they appreciate or dislike. This restricts the model's ability to fine-tune its output based on detailed user preferences. Without the ability to pinpoint specific features, the model's learning is limited to a more holistic, less precise understanding of user intent.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
