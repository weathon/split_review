# LaVie: High-Quality Video Generation with Cascaded Latent Diffusion Models

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
This work aims to learn a high-quality text-to-video (T2V) generative model by leveraging a pre-trained text-to-image (T2I) model as a basis. It is a highly desirable yet challenging task to simultaneously \textbf{a)} accomplish the synthesis of visually realistic and temporally coherent videos while \textbf{b)} preserving the strong creative generation nature of the pre-trained T2I model. To this end, we propose \textbf{LaVie}, an integrated video generation framework that operates on cascaded video latent diffusion models, comprising a base T2V model, a temporal interpolation model, and a video super-resolution model. Our key insights are two-fold: \textbf{1)} We reveal that the incorporation of simple temporal self-attentions, coupled with rotary positional encoding, adequately captures the temporal correlations inherent in video data. \textbf{2)} Additionally, we validate that the process of joint image-video fine-tuning plays a pivotal role in producing high-quality and creative outcomes. To enhance the performance of LaVie, we contribute a comprehensive and diverse video dataset named \textbf{Vimeo25M}, consisting of 25 million text-video pairs that prioritize quality, diversity, and aesthetic appeal. Extensive experiments demonstrate that LaVie achieves state-of-the-art performance both quantitatively and qualitatively. Furthermore, we showcase the versatility of pre-trained LaVie models in various long video generation and personalized video synthesis applications. Project page: {\small \url{https://vchitect.io/LaVie-project/}.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors present a text-to-video model consisting of multiple components including text-2-video, temporal interpolation and super-resolution components. The text-2-video model is built on the pre-trained text-2-image model. Additionally, they introduce Vimeo25M dataset to enhance the quality of text-to-video generation. The method is straightforward and the paper showcases the versatility of the model in long video generation and personalized video generation.

### Strengths
- The paper is well-written and easy to follow

- The resulting model is capable of handling both T2I and T2V tasks.

- The paper provides a human evaluation of video generation quality. 

- The paper introduces Vimeo25M dataset which is a collection of 25 million text-video pairs. The dataset aids in boosting the performance of model in terms of quality and diversity.

- Joint image-video training of model is interesting and seems a reasonable approach for training video generation models.

### Weaknesses
1- The technical novelty of the proposed method is limited as it is a combination of existing techniques, including text-to-image generation, frame interpolation, and super-resolution. The core architecture seems to follow a standard design of leveraging a pre-trained text-to-image model and extending it for video generation, which raises concerns about its incremental contribution.

2- Dandi et al.'s work on “Jointly Trained Image and Video Generation using Residual Vectors" is relevant to this paper's exploration of joint image-video training. However, this paper is neither cited nor discussed.

3- There is no analysis of the contribution of individual components or techniques on the video generation performance. The paper mentions the temporal module, joint image-video training, and usage of Vimeo25M dataset for training. However, we don’t see a comprehensive analysis on the impact of each of them on the performance. It’s hard to understand which component has a higher impact on the final model. The only analysis we see is in Fig 10 which is very limited by showing only three images.

4- The role of the temporal self-attention module (SA-T) during image-only training phases is ambiguous. It's unclear from Figure 3 whether SA-T is frozen or entirely excluded from the process, and how this affects the overall learning dynamics, especially since the model is trained jointly on images and videos.

5- It’s not clear what is the benefit of the technique explained on page 4: "our approach differs from conventional video frame interpolation methods, as each frame generated through interpolation replaces the corresponding input frame. In other words, every frame in the output is newly synthesized". It lacks a clear justification why synthesizing all frames, including the input ones, is superior to directly using the input frames and only interpolating the intermediate ones.

6- How did authors make sure there is enough correlation between text and video segment? Details of text-video pair selection are missing, and it is not clear if any filtering or pre-processing was performed to ensure that the text descriptions accurately represent the content of the video segments.

7- In Fig. 9 (b) statistics on resolution are not clear. what “99.9%” means? It's unclear if this refers to the percentage of videos within a certain height range or if it represents a different statistic altogether.

8- There is no comprehensive evaluation of diversity (since the paper claimed to improve it) besides Fig. 4. Did the authors consider evaluating diversity with human evaluation? The paper lacks a rigorous quantitative assessment of diversity, and it's unclear if the presented examples are representative of the model's overall capabilities.

### Questions
see the weakness section.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents LaVie, a novel integrated video generation framework, which is fundamentally constructed on cascaded video latent diffusion models. The authors strategically integrate three principal components into the LaVie framework: a base Text-to-Video (T2V) model, a temporal interpolation model, and a video super-resolution model. Their approach is underscored by two primary insights: firstly, the integration of simplistic temporal self-attentions, when paired with rotary positional encoding, proves essential in capturing the temporal correlations intrinsic to video data efficiently. Secondly, the process of concurrently fine-tuning both image and video, is validated as being crucial in generating outcomes marked by high-quality and creativity.

### Strengths
1. Innovative Integrated Framework:
The paper presents LaVie, a cutting-edge integrated video generation framework with an enormous capacity of 3 billion parameters. LaVie, primarily a text-to-video foundation model, is meticulously constructed to synthesize visually appealing and temporally coherent videos. The model maintains the vigorous creative generation characteristics of a pre-trained Text-to-Image (T2I) model, ensuring synthesized videos are not only realistic but also infused with a strong creative essence.

2. Strategic Incorporation of Key Insights:
The authors introduce two pivotal insights that form the backbone of LaVie’s design. Firstly, a combination of simple temporal self-attention with Rotary Positional Encoding (RoPE) is utilized, proving sufficient in capturing the intrinsic temporal correlations present in video data. Secondly, the paper emphasizes the indispensable role of joint image-video fine-tuning in crafting high-quality and imaginative outcomes, ensuring the model retains and effectively utilizes learned prior knowledge without succumbing to catastrophic forgetting.

3. Introduction of a Comprehensive Dataset:
Recognizing the limitations of existing datasets, the authors contribute a novel text-video dataset named Vimeo25M. This dataset is a treasure trove of 25 million high-resolution videos, each accompanied by text descriptions, curated to overcome the prevalent issues of low-resolution and watermarked content found in previous datasets. The utilization of Vimeo25M significantly amplifies LaVie’s performance, empowering it to churn out results that excel in quality, diversity, and aesthetic allure, thus substantially advancing the Text-to-Video (T2V) synthesis task.

### Weaknesses
1. Some details are not clear. See **Questions** below.

2. Availability of Contributed Dataset:
A significant contribution highlighted in this paper is the introduction of the Vimeo25M dataset. However, it's crucial to clarify that, as of now, this dataset has not been made publicly available for utilization and further exploration.

3. The claim:

>  simple temporal self-attention coupled with RoPE (Su et al., 2021) adequately captures temporal
correlations inherent in video data. More complex architectural design only results in marginal visual improvements to the generated outcomes

isn't supported by experimental results. The paper lacks a comparative analysis demonstrating that more complex temporal modeling approaches do not yield significant improvements. The claim is made without sufficient quantitative or qualitative evidence, making it difficult to assess the true effectiveness of the proposed temporal module.

### Questions
1. Positional Embedding:
Is the utilization of Rotary Positional Encoding (RoPE) distinctly advantageous compared to other available options, such as learnable embeddings? The clarity of the benefits associated with using RoPE, as opposed to its counterparts, would be appreciated.

2. Clarification on Image Concatenation:
The process involving the concatenation of M images along the temporal axis to formulate a T-frame video raises a query. Specifically, is there an equivalence between the variables `M` and  `T` in this context?

3. Query on SA-T Removal in Image Training:
Figure 3 (c) seems to imply that the SA-T is omitted during the image training phase. Could you provide a more comprehensive explanation or clarification regarding this aspect?

4. Interaction of Text Conditioning with Spatial Attention:
The paper suggests that text conditioning primarily interacts with spatial attention. Given this, how does text effectively influence or control motion within the model? More details regarding the interplay between text and motion would enhance understanding.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a text-to-video method by using a pre-trained text-to-image model as the initialization. The authors present two key findings: 1) temporal self-attention with relative position encoding could maintain temporal consistency well. 2) joint image-video fine-tuning is crucial for good performance. This paper also contributes a video dataset named Vimeo25M, with 25 million text-video pairs.

### Strengths
1. The paper is well-written and easy to follow, and the visualization results seem appealing. 
2. The paper proposes a new video-text datasets named Vimeo25M.

### Weaknesses
1. The technical novelty is limited. The authors present two findings which have both been proposed in previous works. 1) temporal attention over a pretrained text-to-image model could address the temporal consistency model well. This idea is first stated in “AnimateDiff: Animate Your Personalized Text-to-Image Diffusion Models without Specific Tuning” and then pointed out in "MagicEdit: High-Fidelity and Temporally Coherent Video Editing". 2) Joint image-video training is a well-known technique to improve the effectiveness of training text-to-video models. It was first proposed by Jonathan Ho et al. in "Video Diffusion Models".
2.  The idea of the cascaded diffusion model, which first trains a base model then temporally interpolates it, and finally performs super-resolution spatially, is a standard procedure to learn a text-to-video model. Similar ideas are also proposed in "Make-A-Video: Text-to-video Generation Without Text-Video Data", "Imagen Video: High Definition Video Generation with Diffusion Models" and "Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models".

### Questions
Will the authors release the newly proposed video dataset Vimeo25M? Since it seems that there is no promise from the authors that they will release the dataset. I would say that the major contribution of the paper is the dataset.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces LaVie, a text-to-video generative model that builds upon a pre-trained text-to-image model.  LaVie consists of cascaded video latent diffusion models, including a base T2V model, a temporal interpolation model, and a video super-resolution model. The key insights include the use of temporal self-attentions and rotary positional encoding to capture temporal correlations in video data. Joint image-video fine-tuning is crucial for high-quality results. The authors also contribute a large and diverse video dataset called Vimeo25M. Experimental results demonstrate that LaVie achieves state-of-the-art performance in both quantitative and qualitative measuress.

### Strengths
The article provides some insights: 
1. The use of simple temporal self-attention mechanisms coupled with rotary positional encoding to capture temporal correlations in video data 
2. Joint image-video fine-tuning in producing high-quality and creative outcomes.
3. The authors contribute the Vimeo25M dataset, which comprises 25 million text-video pairs, serving as a valuable resource for research and development in the field.

### Weaknesses
1. I think the article lacks technical innovation. Its core contribution involves extending the pre-trained LDM to a video generation model, introducing temporal attention, and emphasizing joint image-video training. However, similar techniques have been mentioned in previous works, such as VDM and Align your latent. The authors should clarify the distinguishing aspects of these innovation.

2. The article presents several assertions without strong empirical support or ablation study. For instance, the introduction of RoPE as a positional encoding lacks corresponding experimental evidence to demonstrate its effectiveness and advantages over other encoding methods. The statement, "we validate that the process of joint image-video fine-tuning plays a pivotal role," lacks experimental substantiation in the article.

3. The writing should be improved, and there exist some unclear explanations. For instance, the modules in Figure 2 are not adequately introduced in the text, causing confusion. For example,  I want to know whether 'E' denotes the encoder or denoiser? Additionally, the article mentions "By applying rigorous filtering criteria" to construct Vimeo25M, but the specific criteria are not outlined. Will this dataset be made publicly available?

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
