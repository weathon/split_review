# Improving Long-Text Alignment for Text-to-Image Diffusion Models

- Decision: Accept
- Scores: 8, 3, 6, 6

## Abstract
The rapid advancement of text-to-image (T2I) diffusion models has enabled them to generate unprecedented results from given texts. However, as text inputs become longer, existing encoding methods like CLIP face limitations, and aligning the generated images with long texts becomes challenging. To tackle these issues, we propose a segment-level encoding method for processing long texts and a decomposed preference optimization method for effective alignment training. For segment-level encoding, long texts are divided into multiple segments and processed separately. This method overcomes the maximum input length limits of pretrained encoding models. For preference optimization, we provide decomposed CLIP-based preference models to fine-tune diffusion models. Specifically, to utilize CLIP-based preference models for T2I alignment, we delve into their scoring mechanisms and find that the preference scores can be decomposed into two components: a text-relevant part that measures T2I alignment and a text-irrelevant part that assesses other visual aspects of human preference. Additionally, we find that the text-irrelevant part contributes to a common overfitting problem during fine-tuning. To address this, we propose a reweighting strategy that assigns different weights to these two components, thereby reducing overfitting and enhancing alignment. After fine-tuning $512 \\times 512$ Stable Diffusion (SD) v1.5 for about 20 hours using our method, the fine-tuned SD outperforms stronger foundation models in T2I alignment, such as PixArt-$\\alpha$ and Kandinsky v2.2.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel approach to enhance the alignment between long text descriptions and generated images in text-to-image diffusion models, introducing segment-level encoding to overcome input length limitations and decomposed preference optimization to mitigate overfitting and improve text-relevant alignment during fine-tuning.

### Strengths
1. The motivation for using preference models is well-founded, and the paper is well-written.
2. It is interesting to identify two distinct focuses within preference models, and the analysis provided is both reasonable and thorough.

### Weaknesses
weakness
1. I am unsure why multiple <sot> tokens are retained; regarding the retention or removal of tokens, a more detailed explanation or analysis is needed, as it currently leaves me confused.
2.After reweighting, whether there will be a noticeable difference in the aesthetic quality of the generated results (due to text-irrelevant components) remains unclear. For Appendix B.1, it would be beneficial to provide some visualizations of the outcomes from the two loss functions.
3. Segmenting to leverage CLIP's alignment effect is an intuitive innovation, but does this become irrelevant in light of the development of Vision-Language Models (VLMs)? Can the current innovation still contribute to VLMs?
4. On line 363, it mentions mitigating the risk of overfitting to Denscore. Could you clarify where the potential source of this overfitting lies?

### Questions
see Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel method to improve text-to-image (T2I) diffusion models in handling long text inputs. Due to the input length limitations of existing encoders like CLIP, it becomes challenging to accurately align generated images with long texts. To address this issue, the authors propose a segment-level encoding strategy, which divides long texts into segments and encodes them separately, combined with a decomposed preference optimization method to reduce overfitting and enhance alignment. Experimental results show that the fine-tuned model surpasses several existing foundation models in long-text alignment, demonstrating significant improvements in handling long text inputs.

### Strengths
[1] It introduces a segment-level encoding strategy that effectively handles long text inputs by dividing and separately encoding segments, overcoming traditional model input limitations and enhancing text-to-image alignment. 
[2] The preference model is innovatively decomposed into text-relevant and text-irrelevant components, with a reweighting strategy to reduce overfitting and improve alignment precision.
[3] The paper conducts extensive experiments, demonstrating significant improvements in long-text alignment over existing models like PixArt-α and Kandinsky v2.2, proving the method's effectiveness for complex text generation tasks.

### Weaknesses
[1] The paper proposes a segment-level encoding strategy to handle long texts but does not thoroughly validate the performance of this strategy under different text length conditions. For very short or very long texts, can the segment-level encoding still maintain the same alignment effectiveness? The lack of fine-grained comparative experiments makes it difficult to adequately demonstrate the applicability of segment-level encoding across a wide range of text lengths. Specifically, the paper does not explore how the size of segments impacts performance, nor does it analyze the computational overhead associated with segmenting very long texts into many smaller segments. This is crucial because the effectiveness of segment-level encoding might degrade with extremely short segments, losing contextual information, or with an excessive number of segments, increasing computational cost without proportional gains in alignment.
[2] The paper proposes a reweighting strategy to address overfitting, but lacks detailed experimental data to demonstrate its effectiveness, failing to adequately prove its specific impact on reducing overfitting. The description of the reweighting strategy is also vague, lacking details on how the text-relevant and text-irrelevant components are precisely calculated and how the reweighting ratio is determined. Without a clear understanding of these parameters and their impact, it is difficult to assess the robustness and generalizability of this approach. Furthermore, the paper does not provide any ablation studies to show the performance of the model with and without the reweighting strategy, making it hard to isolate the contribution of this component.
[3] The segment-level encoding and preference optimization strategies proposed in this paper show excellent performance in the experiments, but lack an analysis of the method's limitations. It would be beneficial to discuss whether these segment-level encoding methods might lose part of their alignment effectiveness when dealing with texts that have complex contextual dependencies or require strong semantic understanding. The paper does not discuss the potential for information loss when segmenting texts with intricate relationships between different parts, nor does it address how the model handles long-range dependencies that span across multiple segments. This is a critical oversight, as the effectiveness of the method might be significantly reduced when applied to texts with complex semantic structures.

### Questions
[1] Does your proposed segment-level encoding strategy demonstrate significant effectiveness for texts of varying lengths? Specifically, how does the model perform with very short texts (fewer than 10 words) or very long texts (over 500 words)? Could you provide additional experiments to show comparative results under different text length conditions to verify the generalizability of the segment-level encoding strategy?
[2] You mentioned using a reweighting strategy to mitigate the model's overfitting issue, but the description of this process in the paper is rather brief. Could you provide detailed steps or pseudocode to explain the implementation of this strategy? Additionally, does this method have any quantitative results to demonstrate its effectiveness in reducing overfitting in specific scenarios? Could you include comparative data from the experiments to validate the impact of this strategy?
[3] How were the 5k images in the test set specifically selected from datasets like SAM and COCO2017?
[4] Could you briefly explain the selection of models like CLIP-H and HPSv2 in the experimental section of Chapter 5, as well as the chosen evaluation metrics?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a method for enhancing the prompt following of text-to-image models specifically in the case of long prompts. The key contribution for tackling this problem is twofold: a) using a combination of CLIP and T5 encoders (as is becoming increasingly common these days e.g. SD3, Flux) b) the introduction of a preference model tailored for long prompts (Denscore) and applying reward fine-tuning with this Denscore model to enhance the prompt following of SD1.5 models for long prompts.

### Strengths
The paper tackles the crucial challenge of long prompt following in a very effective manner. Using a text encoder that can take the entire long prompt is a sound idea, and the Denscore preference model looks like a useful contribution in general. 
Apart from this, the reward fine-tuning with the orthogonal decomposition and the gradient reweighting looks like a good idea to deal with the "reward-hacking" problem.
Finally, the results also appear quite strong from the evaluations presented in the paper.

### Weaknesses
An important paper that is missed here is ELLA[Hu et al. 2024] for a couple of reasons. The first is that they propose replacing the CLIP encoder of SD1.5 with a T5-XL model and get significantly improved results (far superior numbers to those reported by Lavi-Bridge whose MLP adapter is used here). Therefore, this model might be a valid comparison (although the training cost of ELLA is a bit higher: 7 days with 8 A100s for SD1.5). Alternatively, the adapter provided by ELLA would have probably been a better alternative to the one used in the paper (from Lavi-Bridge). 

Apart from the comparison/use of adapter, there's also DPG-Bench introduced in the paper which is a good benchmark for long prompt following (as compared to existing benchmarks like T2I-Compbench, DSG, TIFA etc.). Evaluating on DPG-Bench would be a useful addition since the 5k evaluation set of this paper is not fully understood and only a few models have been evaluated here. Additionally, from an evaluation standpoint, even on this 5k evaluation set, VQAScore[1] might be a good option to consider, since it uses a T5-XXL model which can take long prompts, and has shown some promising results for text-to-image evaluations. 

Another aspect which is missing here is that all the experiments in this paper are conducted on SD1.5 which is a relatively older model, and there have been newer models in the past 2 years (e.g. SDXL). Therefore, it would have been nicer to also have results with any of the newer, more performant models, but I can understand that this might be a bit more computationally expensive (especially if the training has to be done at 1024 resolution). 

Overall, I dolike the paper, but I believe that incorporating these aspects (especially strengthening the paper with additional evaluations) could improve the paper significantly.

### Questions
I apologize in advance if I missed it, but I do not really see clear details about the training of the Denscore model. B.1 has details on the training objectives and the fact that captions are generated by LLaVA-Next, but beyond this I do not see other implementation details (dataset, other choices etc.), so it would be great if the authors could point me to this.

### Soundness
4

### Presentation
2

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
This paper presents a new approach for long text inputs on text-to-image (T2I) alignment since the clip text encoding only allows 77 tokens. The authors address limitations of existing encoding methods like CLIP by proposing segment-level encoding, where long texts are divided and processed in parts to bypass input length constraints. They further introduce a decomposed preference optimization that separates alignment-related and non-alignment components of CLIP-based preference scores. By reweighting these components, the method reduces overfitting, achieving superior T2I alignment after fine-tuning Stable Diffusion v1.5, outperforming models such as PixArt-α and Kandinsky v2.2.

### Strengths
(1) Comprehensive Survey of Related Work.
The paper presents a thorough and comprehensive survey of existing work in text-to-image (T2I) diffusion models, demonstrating an impressive grasp of the field. By delving deeply into previous approaches and their limitations, the authors effectively set the stage for their contributions, clarifying the gaps their method aims to fill. This background provides readers with valuable context and insight into the evolution of T2I models, particularly in handling longer, complex textual inputs. The comprehensive nature of this survey also reinforces the authors' understanding of the field's current challenges and strengths, building confidence in the relevance and timeliness of the proposed approach.

(2) Importance of the Problem and a Reasonable, Well-Motivated Solution.
The authors tackle a critical issue in T2I diffusion models: the difficulty of aligning generated images with longer text prompts. As the demand for complex, high-fidelity image generation grows, the ability to handle longer text inputs accurately is essential. The segmentation approach, paired with decomposed preference optimization, offers a well-motivated solution to this problem. Segmenting long text into manageable parts allows for better processing within the confines of existing encoding models, while the decomposed preference optimization fine-tunes the alignment, addressing the unique challenges posed by long prompts. The design choices reflect a reasonable and methodical approach to tackling these limitations, and the paper articulates the rationale for each component clearly. This structured approach suggests the authors have carefully considered the problem’s nuances, offering a solution that is not only effective but also grounded in sound methodology.

(3) Demonstrated Superiority over State-of-the-Art Models.
One of the paper's significant strengths is the demonstrated performance improvement over state-of-the-art models. Through rigorous experimentation, the authors show that their method surpasses current leading models like PixArt-α and Kandinsky v2.2 in T2I alignment, particularly for long-text prompts. By fine-tuning Stable Diffusion v1.5 with their approach, they achieve superior alignment, reducing overfitting while preserving text-relevant information in the generated images. This achievement underscores the potential of the proposed method to set a new benchmark for handling longer, more detailed textual inputs within T2I models. The improvement over established models validates the effectiveness of the segmentation and preference optimization strategy, indicating that this approach could meaningfully advance the state of the art in T2I diffusion modeling.

### Weaknesses
Although the proposed method solved an important issue, three major issues remain as listed below.
(1) Limitations and Ambiguities in the Segmentation and Merging Methodology. The segmentation and merging technique proposed in this work introduces a unique approach to handling longer text inputs but raises questions regarding its effectiveness and generalizability. When text inputs exceed 77 tokens, this method still encounters limitations, as it is fundamentally restricted by the underlying model’s capacity to handle “long” sequences since the split-and-merge process does not solve the problem. This constraint is particularly concerning as longer text inputs are common in real-world applications and often essential to producing detailed and contextually accurate image generations. The current approach of segmenting and then merging these sections seems like a workaround rather than a robust solution to handling extended texts, which may inherently limit its scalability and versatility. Furthermore, the mechanics of how segmentation and merging affect the underlying model's cross-attention dynamics remain underexplored. Cross-attention is a critical component in the alignment process between text and image features, and segmenting inputs may disrupt this alignment, especially as certain semantic connections might be lost or diluted across segmented inputs. Investigating the cross-attention differences between the original, unsegmented approach and the segment-and-merge methodology could shed light on any distortions introduced by this technique. A more thorough analysis of cross-attention’s role here could help refine segmentation methods to better retain textual coherence and improve image alignment fidelity, ultimately benefiting downstream performance.

(2) Dependency on an Outdated Baseline Model (Stable Diffusion v1.5):
The use of Stable Diffusion v1.5 as the primary evaluation model poses a significant limitation, given that the field has moved toward more advanced versions like SD-3 and SDXL. These newer versions incorporate improved architectures and training techniques, yielding enhanced performance, especially in terms of image quality and alignment with textual inputs. The reliance on an outdated model not only limits the relevance of the study’s results but also restricts the potential impact of the proposed method. Using v1.5 as the baseline reflects well on the approach’s applicability to older architectures, but it leaves unanswered questions about its efficacy on more sophisticated models that incorporate advancements in diffusion techniques, training scale, and multimodal alignment mechanisms. Moreover, maintaining SD-1.5 as a standard for comparison could inadvertently hold back progress within the research community. As models continue to evolve, it’s essential to align benchmark tests with the latest technologies to ensure that methods are relevant and that advancements reflect real-world capabilities. Preliminary results from newer models, such as SD-3, have demonstrated considerable improvements in T2I alignment, indicating that the proposed method may benefit even further from these architectural updates. Testing on newer models would better position the approach in the context of current technological standards, ensuring that it remains relevant and applicable as diffusion models evolve. Future work should include evaluations on SD-3 and SDXL to substantiate claims of superiority over other methods in a more current setting. The test of SD-3 with the prompt used in the first example of Fig. 1 is shown below.
https://ibb.co/CWyKQTZ

(3) Over-reliance on Long Prompt Training and Lack of Generalizability Testing.
The proposed method seems to rely heavily on training with long prompts, which could limit its flexibility and adaptability. While training on extended text inputs may enhance alignment for similar prompts, it raises concerns about the model's performance on shorter or more varied prompts. In real-world scenarios, prompt lengths and structures vary significantly, and a robust model should perform consistently across this spectrum. By focusing predominantly on long-prompt alignment, the current approach may overfit to specific input lengths, making it less effective for shorter or less detailed prompts where segmentation might not be necessary or where text segments are not sufficiently complex to benefit from this treatment. To address this potential limitation, it would be valuable to conduct experiments that vary prompt lengths and structures systematically, assessing whether the model’s performance holds across different scenarios. Additionally, testing with alternative segmentation designs could reveal whether simpler or more complex methods yield better alignment. These experiments would enhance our understanding of how adaptable the proposed method is, providing insights into its generalizability and robustness. The community would benefit from such insights, as they could guide further development of segmentation-based approaches for T2I tasks.

### Questions
(1) Please better explain why the proposed split-and-merge approach can address the long-text alignment issue.
(2) Please provide the ablation study clearly.

### Soundness
3

### Presentation
3

### Contribution
2
