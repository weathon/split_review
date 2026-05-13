# StyleShot: A snapshot on any style

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
In this paper, we show that, a good style representation is crucial and sufficient for generalized style transfer without test-time tuning.
We achieve this through constructing a style-aware encoder and a well-organized style dataset called StyleGallery.
With dedicated design for style learning, this style-aware encoder is trained to extract expressive style representation with decoupling training strategy, and StyleGallery enables the generalization ability.
We further employ a content-fusion encoder to enhance image-driven style transfer.
We highlight that, our approach, named StyleShot, is simple yet effective in mimicking various desired styles, i.e., 3D, flat, abstract or even fine-grained styles, \textit{without} test-time tuning. Rigorous experiments validate that, StyleShot achieves superior performance across a wide range of styles compared to existing state-of-the-art methods.
The project page is available at: https://styleshot.io/.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an encoder to extract style info from the reference style. The information is combined with text embedding and injects to diffusion models through the cross-attention layer. Meanwhile, to preserve content, contours are extracted and inject to the diffusion network through controlnet-like residue addition. Experimental results were compared with SOTA methods such as InstantStyle, StyleAligned, etc.

### Strengths
The results look interesting and the method is straightforward.

### Weaknesses
In Figure 7, the results from StyleAligned look weird, can you detail how the results were generated?
While training for the style encoder, it seems that a crafted datasets were used. Can you detailed the model training details including the encoder as well as the feature injection part in the diffusion model?

### Questions
Are text-based stylization results generated using the same model and set the content reference as black or is this a different model?

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
5

### Summary
This manuscript describes a stylized image framework in an IP-adaptor fashion. Special attention is paid to learning style representation: a style-aware encoder is proposed. Based on Stable Diffusion, Styleshot uses a multi-scale patch partitioning scheme with MoE and ResBlocks to capture diverse style cues. It then processes these through Transformer Blocks and injects the style embeddings into the model. A style-balanced dataset, StyleGallery, is collected. Text- and image-driven stylization tasks are evaluated.

### Strengths
Overall, the reviewer tends to classify this paper's originality as removing limitations from prior results. The proposed method is reasonable and has good motivation. The focus of learning style representations for style transfer tasks is valid. Some of the generated results are impressive.

### Weaknesses
 - Overall, the reviewer would not rate the technical contribution of the proposed method high. Based on the IP adaptor, the proposed method is somewhat incremental. It seems to be a successful attempt to combine MOE and IP adaptor.

- The reviewer is confused about the claim that the authors ''show that a good style representation is crucial'' for style transfer. Since CAST has already observed related conclusions and proved the usefulness of learning a good style encoder. 

- Related to the first issue, the introduction is organized in a loose way. The authors are suggested to focus more on finding the position of the proposed method in the style transfer research context.

- Given that the proposed method is trained on the newly proposed dataset, the reviewer finds the comparison to be somewhat unfair.  Some results of the selected comparing methods are much worse than common sense, such as the 4th lines in figure 8. All other methods failed to learn the style. Please check and compare with more recent diffusion-based models such as Z-Star (CVPR 2024, also training free).

- NO user study of image-driven style transfer. The reviewer agrees with the authors that different methods were used to evaluate different unavailable datasets. How about considering using third-party dataset such as ''A Comprehensive Evaluation of Arbitrary Image Style Transfer Methods'', IEEE TVCG.

### Questions
The manuscript is presented in an easy-to-follow way. There are no more questions. I have just some suggestions for convincing the audience that the proposed method has good technical contributions; see weaknesses for details. The reviewer is open to valid responses and changing my initial ratings.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a generalized diffusion-based style transfer method called StyleShot which learns style from reference images and learns content from text prompts. The core component of StyleShot is a style-aware encoder which is designed to extract expressive style representation with decoupling training strategy. In addition, a new dataset StyleGallery is constructed to enhance the generalization ability of the proposed method.

### Strengths
1. The artistic images generated by the proposed method is impressive.
2. This paper provides a new style-balanced dataset.
3. The proposed method is simple yet effective.
4. Extensive experiments are conducted to evaluate the performance of the proposed method.

### Weaknesses
1. The quantitative results are not satisfying. The CLIP scores reported in Table 1 show that the proposed method is just comparable with previous methods (no gain). Although the authors claim that these metrics are not ideal for evaluation in style transfer tasks, they are still among the most widely used and authoritative metrics in this field.

2. When comparing with existing text-driven style transfer methods, several more state-of-the-art approaches (such as DreamStyler, T2I-Adapter, and InstantStyle) are only included in the supplementary material. Why not present them in the main paper? Moreover, some of these methods (such as DreamStyler), like the proposed method, can be used for both text-driven style transfer and image-driven style transfer, and thus a more comprehensive comparison with them on both tasks would be appropriate.

3. In the user study, how many users participated in the survey? How many samples were involved?

4. For the proposed de-stylization, this paper provides quantitative experiments in the supplementary material to demonstrate its effectiveness. However, it would be better to also include qualitative experiments to provide a more intuitive observation of its impact.

### Questions
Please see **Weaknesses**.

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
5

### Summary
This paper proposes a style transfer method that consists of: 1) using a pre-trained text-to-image model as the generation backbone, 2) employing multi-scale cropped patches from a style image as the style condition, and 3) using contour conditions from the content image to provide structural guidance. During the generation process, the model can also incorporate text descriptions as additional guidance. Additionally, the authors introduce a new style image dataset named StyleGallery, sourced from MidJourney and WIKIART. Comprehensive experiments are conducted to examine the effects of dataset selection and style image partition strategies. Empirical results suggest that the proposed method generates outputs that are more favorably received by human evaluators.

### Strengths
* The paper is easy to follow, and the qualitative results are well-presented.
* The authors introduce a new dataset, StyleGallery, which offers more diverse and balanced styles compared to the LAION-Aesthetic dataset. Notably, 99.7% of the samples in StyleGallery include style descriptions, making it a valuable resource for future style-related research. Additionally, the authors curated a subset of StyleGallery called StyleBench for the evaluation of style transfer, which could potentially serve as a standard benchmark.

### Weaknesses
1. The proposed StyleShot architecture does not show significant novelty. The overall structure primarily follows the established method of conditional diffusion generation by integrating style and content information into the foundational diffusion layers. This technique is widely used in diffusion-based transfer learning, such as ControlNet [A] and T2I-Adapter [B] (with this work aligning more closely with the latter). The core of the method involves injecting style and content conditions into the U-Net architecture of a pre-trained diffusion model, a strategy that has become a standard practice in the field. While the specific implementation details may vary, the fundamental approach lacks a substantial departure from existing paradigms.

2. Similarly, using patch-based encoding for the style image is not new. Previous works, such as [C, D], also employ transformer encoders for patch-wise style image encoding. While the improvement in this work lies in using multi-scale patch size, unlike prior works that use a single patch size. The reviewer believes this modification offers only limited novelty. The use of multi-scale patches, while potentially beneficial, represents an incremental improvement rather than a fundamental innovation. The core idea of dividing the style image into patches and processing them through a transformer-based encoder remains consistent with prior art. The added complexity of multi-scale processing does not introduce a fundamentally new approach to style representation.

3. The authors emphasize their content extraction approach in the Method section. However, in the comparison shown in Figure 14, Canny, HED, and the proposed methods are evaluated using ControlNet, not the proposed content-fusion encoder. Therefore, the reviewer does not believe that Figure 14 adequately validates the proposed content extraction method as superior to Canny or HED, given that these are not compared under the same conditions as the proposed content extraction (as seen in the last column of Figure 14). Additionally, when Canny, HED, and the proposed method all use ControlNet as a condition (rows 3-5 of Figure 14), it is difficult to support the claim that the proposed method enables greater stylization (Ln 484-485).

4. Typo: Figure 14's caption, "Rows 3-5" --> "Columns 3-5." Also, it would be beneficial to provide more statistical details about the collected StyleGallery, such as the total number of images, total number of styles, and an analysis of the balance of styles within the dataset, etc.

### Questions
My current rating for this paper is borderline accept. The reviewer acknowledges that the quality of the proposed style transfer is commendable, and the contribution of a new style dataset is a noteworthy addition. However, a higher rating is hindered by the limited methodological novelty (see weaknesses 1 and 2) and the lack of fairness in the experimental comparisons (see weakness 3).

### Soundness
2

### Presentation
3

### Contribution
2
