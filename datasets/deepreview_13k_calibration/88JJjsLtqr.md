# Less is More: Masking Elements in Image Condition Features Avoids Content Leakages in Style Transfer Diffusion Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Given a style-reference image as the additional image condition, text-to-image diffusion models have demonstrated impressive capabilities in generating images that possess the content of text prompts while adopting the visual style of the reference image. However, current state-of-the-art methods often struggle to disentangle content and style from style-reference images, leading to issues such as content leakages. To address this issue, we propose a masking-based method that efficiently decouples content from style without the need of tuning any model parameters. By simply masking specific elements in the style reference's image features, we uncover a critical yet under-explored principle: guiding with appropriately-selected fewer conditions (e.g., dropping several image feature elements) can efficiently avoid unwanted content flowing into the diffusion models, enhancing the style transfer performances of text-to-image diffusion models. In this paper, we validate this finding both theoretically and experimentally. Extensive experiments across various styles demonstrate the effectiveness of our masking-based method and support our theoretical results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a style transfer method that can preserve style in the style reference image while ignored the content injection for the final style transfer result.  The key idea of the proposed method is based on IP-adpator while masked out the some image tokens from the reference image.  The masking strategy is first clustering the product feature of style image and content image and then filtering out the feature tokens of high means in style features.   To approve the masked strategy is effective, the authors also provided several theoretical justifications.

### Strengths
The key strengths in this paper are the insights of analyzing different style transfer methods including IP-adpator and Instant Style. With those observations, the proposed method provide a masking solution to demonstrate that removing certain tokens especially the token with high correlations between content and style will result a high fidelity stylized images.

### Weaknesses
There are several weaknesses in this paper:

1. The masked image feature is questionable. Although the proof demonstrate the divergency in a theoretical way, it is clear that it only demonstrate the divergence by comparing with InstantStyle rather than the method itself.   Image token selection is based on the product between content and style feature, such computation is more likely filtering about the foreground style feature.  Thus why not only encode the background  or non-object related style patches? The method's reliance on the product of content and style features for token selection seems overly simplistic. This approach risks disproportionately removing foreground style elements, which are often crucial for capturing the essence of a style. A more nuanced approach might involve analyzing the spatial frequency or semantic content of the features to determine which tokens are most relevant for style transfer, rather than relying solely on a simple product. Furthermore, the paper lacks a clear explanation of how the clustering is performed and how the high-mean tokens are precisely identified, making it difficult to assess the robustness of this selection process.

2. The visual comparison is not in a fair comparison.  Lots of the results are in a cherry pick manner.  For example, StyledDrop and StyleShot focus more in tradition painting like style transfer, while the experiments showing more like photo as a reference image, which not makes much sense.  Moreover, the Figure 8 compare the results with InstantSyle but not StyleShot is also not fair since the setting is more like the traditional style transfer. The comparisons with StyleDrop and StyleShot are indeed problematic given the different nature of the style references used. The paper should have included a more comprehensive evaluation on a dataset that encompasses both artistic and photographic styles. The choice of comparing against InstantStyle in Figure 8, while excluding StyleShot, is also questionable. It would be more informative to compare against StyleShot directly, especially since the proposed method is built upon the StyleShot architecture. This inconsistency in the comparison makes it difficult to assess the true performance of the proposed method relative to the state-of-the-art.

### Questions
Please double check the experiments. For example, I screenshot one style reference image and use the official styleshot demo, I could generate better results shown in the paper.   

Another fair comparison is leveraging existing benchmark (the images used in styledrop and styleshot) and shown more proposed results on that. 

There are also some questions on the visual results. For example, the Figure 1 shows that the proposed method also could not generate visual plausible results especially preserving the style in style reference image. In Figure 8, it is clear to see that some cases InstantStyle gives better results.  As it preserves the content while generates less artifacts.  Thus more results on the existing benchmark maybe a good justification.

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
The paper focuses on the content leakage issues in the text-to-image diffusion model for style transfer, which aims to distangle the content and style characteristics of the style-reference images for generating outputs combining text content and visual styles. It proposes a simple and training-free method to decouple the content from style in style-reference images. By masking specific content-related elements within the image features, the proposed method prevents unwanted content information from influencing the output. The proposed method was evaluated on CIFAR-10 dataset and demonstrates good results.

### Strengths
1. The motivation of this paper is well elaborated, and the limitations of previous methods are clearly described. Therefore, potential readers can easily understand the core problem in style transfer. 
2. The structure of the paper is well-organized and the presentation is easy to follow. 
3. It proposes a masking-based technique to decouple the content and style in the reference images. Fig.3 clearly demonstrates the difference between the proposed method and previous methods.

### Weaknesses
1. The novelty of the proposed method is limited. 1). Compared with IP-adaptor and InstantStyle, the contribution of sampling masking features in the feature space is not significant. 2). Introducing a masking mechanism is effective for manually synthesizing high-quality images, which has been demonstrated in previous studies [1-3].

2. The proposed method aims to decouple the content and style characteristics of the reference images, but this problem is not formally formulated in the paper. Therefore, it is hard to understand why the masking mechanism can achieve this goal.

3. The proposed method needs to carefully select specific features for generating desirable styles, but the selection criteria are not clearly described.

4. The paper claims that it proposes an efficient method to decouple the content and style of the reference images in the introduction part, but the paper does not show significant evidence to demonstrate its efficiency compared with the previous methods.

5. The proposed method is only evaluated on CIFAR-10 dataset, and measured with subjective metrics that are not defined clearly. Therefore, existing experiment results are insufficient to demonstrate the proposed method's advantages.

### Questions
1. It is better to elaborate on the advantages and significant contributions of the proposed method for style transfer compared to previous approaches?

2. What is the formal definition of content leakages? Additionally, how does the proposed method effectively address this issue?

3. How does the proposed method decouple the content and style characteristics of the reference images?

4. How are features selected during the style transfer process? Please provide detailed information on the selection criteria. Are the same selection criteria, including hyperparameters, applied consistently to all output images?

5. What makes the proposed method efficient? Compared to previous approaches, does it require less inference time or fewer GPU resources?
6. It would be beneficial to include more experiments on different datasets. Specifically, how does the proposed method perform when processing high-resolution images?

7. Including additional objective evaluation metrics, such as FID, LPIPS, and CLIP score, would be valuable. Since the fidelity score highly depends on the chosen classifier, how does the performance change when a different classifier is used?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a simple but effective method to avoid content leakages and achieve better performance in style transfer. The main contribution is its innovative masking strategy, and extensive experiments demonstrate its superiority.

### Strengths
1. The paper is well-written and easy to follow. 
2. The proposed masking strategy is novel and effective. 
3. The authors provide both theoretical and experimental evidence to support their claims.

### Weaknesses
1. It remains unclear why clustering is performed on the element-wise product of $e_1$ and $e_2$.  Is there a relationship between $e_1\cdot e_2$ and the energy function? 
2. The inference speed is slower than other methods, likely due to the additional time consumption introduced by the clustering algorithm. What is your inference time in practice? Is there a solution that avoids this additional time cost, or could the clustering algorithm be replaced to improve efficiency?

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a feature masking method to control the content leakage for the stylization task. It requires an additional content description of the image and decouples this content by masking it out in the style features. The authors also provided theoretical proofs to demonstrate the motivation of their method. Both qualitative and quantitative results are superior to the alternatives.

### Strengths
1. The proposed method is intuitive and works well.
2. Theoretical proofs are valid and well support the experiments.
3. Generally the writing is good and the story is complete, though there is some information missing as I mentioned in the following section.
4. Experiment design is comprehensive and the performance looks good.

### Weaknesses
1. The authors should compare with more recent stronger baselines that are proposed to alleviate the content leakage problem like RB-Modulation, which uses attention feature aggregation and different descriptors to decouple content and style. Since it is also training-free and mentioned to outperform InstantStyle, it would serve as a good baseline for comparison. CSGO is another recent work that uses a separately trained style projection layer to avoid content leakage. Though it’s pretty new (released a month before deadline), some qualitative results would help demonstrate the strengths of your method. 
2. In L229, should m^i be 1 or 0?
3. Figure 3(b) is not referred to but seems to be mentioned in the experiments. I thought this should be part of the method you want to introduce. Can you explain how this is used with your proposed method? And how does the linear layer learn the content feature to be subtracted?
4. Theorem 1 indicates that the proposed method archives a smaller divergence. Does “smaller divergence” define better style alignment? I’m asking because there might be several factors that can lead to smaller divergence, like same background/or elements in the images, content leakage, etc. I’d like to get your insights on what is the style in an image?
5. In L215, it seems cluster number K controls how many tokens are masked. Is there any analysis to show how K affects the performance?
6. Can you add more details on how you do binary classification as eval in L369? Specifically, what model is used for the classification, and what threshold is used to determine the classification?
7. Are you using style descriptions in the prompt?
8. Why does image alignment keep dropping in figure 5(a)?
9. Can you provide more details on how you conduct user study? Like instructions to the raters and how you present the images to the raters. Given that you have 10 content objects and 21 image styles with 8 variations each, and 50 generations per prompt, does this mean that each rater evaluated 1050 images per class?

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3
