# AddressVLM: Cross-view Alignment Tuning for Image Address Localization using Large Vision-Language Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 8, 5, 5

## Abstract
Large visual language models (LVLMs) have demonstrated impressive performance in coarse-grained geo-localization at the country or city level, but they struggle with fine-grained street-level localization within urban areas. In this paper, we explore integrating city-wide address localization capabilities into LVLMs, facilitating flexible address-related question answering using street-view images. A key challenge is that the street-view visual question-and-answer (VQA) data provides only microscopic visual cues, leading to subpar performance in fine-tuned models. To tackle this issue, we incorporate perspective-invariant satellite images as macro cues and propose cross-view alignment tuning including a satellite-view and street-view image grafting mechanism, along with an automatic alignment label generation mechanism. This helps build connections between street-view images through cross-view matching, thus enhancing LVLM's global understanding of street distribution. We name our proposed model AddressVLM consisting of two-stage training protocols: cross-view alignment tuning and address localization tuning. Furthermore, we have constructed two street-view VQA datasets based on image address localization datasets from Pittsburgh and San Francisco. Qualitative and quantitative evaluations demonstrate that AddressVLM outperforms counterpart LVLMs by over 9% and 12% in average address localization accuracy on the Pitts-VQA and SF-Base-VQA datasets, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces AddressVLM, a novel approach to enhance Large Vision Language Models (LVLMs) for street-level address localization. The proposed cross-view alignment tuning strategy leverages both street-view and satellite imagery to improve the model's understanding of urban spatial relationships. The work addresses a gap in current LVLM capabilities - while they perform well at city/country-level geo-localization, they struggle with precise street-level localization within cities. Also, This paper constructs two street-view VQA datasets based on image address localization datasets from Pittsburgh and San Francisco.

### Strengths
1. The motivation is clearly stated.
2. The experimental results show the effectiveness of the proposed method.
3. Creating new datasets for the research community.

### Weaknesses
1.The paper uses a pre-trained LVLM to generate textual labels that explain why a street-view image matches a satellite image location. However, any errors or biases in these generated labels become training data for the cross-view alignment tuning stage. These errors could be amplified during the subsequent address localization tuning stage.

2.While improvements are shown, absolute performance is still below specialized discriminative models.

3.Limited evaluation on cities outside the US.

4.While the authors present two novel datasets, the paper would benefit from visual or tabular comparisons highlighting the differences of these two datasets relative to existing ones.

### Questions
1. In Figure 3 (b, c), the authors do not introduce what the different colors and lengths represent.

2. What is the purpose of comparing AddressCLIP in Table 1? The experimental results show that the proposed method is not superior to AddressCLIP in terms of the A_ds indicator. Additionally, the authors have not introduced the meaning of the A_ds indicator. Do A_ds and A_sd (referenced in line 364) represent the same meaning?

3. The ablation experiment in Table 3 is quite confusing. Please redesign it to better demonstrate the effectiveness of each module.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents AddressVLM, a model for fine-grained geo-localization consisting of two training stages: cross-view alignment tuning and address localization tuning. The authors also introduce two new VQA datasets adapted from existing address localization datasets from Pittsburgh and San Francisco.

### Strengths
S1. This paper is very well-written, and the figures are clear. As someone with little background in image address localization, I appreciate the straightforward presentation and review of related work, including Figure 1 which puts the methods of existing work side-by-side with the method in AddressVLM. 

S2. The ablation study is thorough, reporting results on different model variants during each training stage.

### Weaknesses
W1. I would have liked to see evaluations on how AddressVLM does on other related geolocalization benchmarks adapted for VQA in the same way that Pitts-VQA and SF-Base-VQA were created. For example, comparing performance on OpenStreetView-5M [1] or Geoguessr data like in [2] would better show how this method specifically improves fine-grained address localization and the side effects it has on other related tasks (e.g., does this method detract from more coarse, global understanding?). I think this type of evaluation, even if it shows that AddressVLM decreases performance on other forms of geolocalization, can only strengthen the papers as it gives a more thorough presentation of what the method can and cannot do. 

W2. A more thorough study of vision and language backbones would establish a more compelling case for using CLIP and Phi-3.1-mini. SigLIP has been shown to perform better on many VQA tasks, and DINOv2 has been shown to better localize objects in an image (rather than just capture more global, image-level semantics like CLIP); both of these abilities could translate to improvements in the VLM downstream.

### Questions
Q1. What are some limitations of AddressVLM? Are there particular categories of edge cases (e.g., bias toward one street vs. the other when localizing an intersection, low-light conditions, occlusions) that the method performs particularly poorly at, and are these failure patterns similar to the failure patterns of existing models?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method to integrate the address localization capability within a city into large-scale visual-linguistic models (LVLM), in order to achieve flexible address-based question answering based on street view images. The main contributions include exploring the integration of address localization capability within a city into LVLM, proposing a cross-view alignment fine-tuning method, and introducing the AddressVLM model. The experimental results show that AddressVLM significantly outperforms the baseline LVLM and the state-of-the-art GeoReasoner model on the street view VQA dataset and demonstrates the address localization capability across multiple cities.

### Strengths
1. It adopts a cross-view alignment fine-tuning strategy by aligning the sparsely collected street view images with globally consistent satellite images, which enhances the LVLM's understanding of the overall city street distribution. This helps address the challenges that cannot be solved by only using second-stage address localization fine-tuning.

2. Compared to general LVLM, this method can achieve fine-grained understanding of the urban environment using only 4B parameters, providing feasibility for future device deployment and updates. This highlights the practicality and efficiency of the method.

### Weaknesses
1. Although an innovative method for cross-view alignment of street-view images and satellite images was proposed, there is a lack of theoretical analysis and mathematical derivation of this method, which makes it difficult to deeply understand its principles and
limitations. Specifically, the paper does not provide a clear explanation of how the cross-view alignment loss is formulated or how the gradients are propagated during training. This lack of detail makes it difficult to assess the robustness and convergence properties of the proposed method. Furthermore, the paper does not discuss the potential impact of geometric distortions or occlusions present in street-view images on the alignment process.

2. The experimental part is only evaluated in a limited urban area, which cannot fully verify the applicability and scalability of this method in a wider urban environment. The datasets used for evaluation, while relevant, may not be representative of the diversity of urban landscapes, architectural styles, and street layouts found in different cities. This limited scope raises concerns about the generalizability of the proposed method to other geographical locations and urban settings. The paper also lacks an analysis of how the performance of the method might vary across different types of urban areas, such as residential, commercial, or industrial zones.

### Questions
1. In the introduction, the author introduces AddressCLIP, a method based on image and text alignment, points out the related shortcomings, and introduces his own methods. However, the author does not indicate whether his predecessors have done any work on this question-and-answer-based approach. The author needs to make this clear.

2. Please briefly explain the difference between Visual Place Recognition and Cross-view
Geo-localization in a few sentences.

3. In section 3.2, the author mentions that "street-view images are scaled down and grafted onto satellite images like CutMix data augmentation". Could the author briefly explain why other mixup data augmentation methods are not used? Why is cutmix applied?

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
5

### Summary
This paper presents AddressVLM, a novel approach for enhancing fine-grained street-level localization in urban areas using LVLMs through the incorporation of satellite imagery and cross-view alignment. AddressVLM introduces a satellite-view and street-view image grafting mechanism, along with an automatic alignment label generation mechanism. This helps build connections between street-view images through cross-view matching, thereby enhancing the LVLM’s global understanding of street distributions. The model uses a two-stage training protocol: Cross-view alignment tuning, which establishes spatial correlations by combining cross-view images and generating labels automatically, followed by Address localization tuning to further optimize accuracy. The authors created two street-view VQA datasets, Pitts-VQA and SF-Base-VQA, based on image address localization datasets from Pittsburgh and San Francisco, providing valuable resources for evaluating fine-grained urban localization within the community.

The main contribution of this work is the cross-view alignment tuning method, which integrates macro and micro visual cues from urban environments into LVLMs. By grafting street-view and satellite images and employing automated label generation, AddressVLM enhances the model’s global understanding of street distributions, showing significant improvements compared to baseline LVLMs and the state-of-the-art GeoReasoner model. Experimental results indicate that AddressVLM improves accuracy on the Pitts-VQA and SF-Base-VQA datasets by 9% and 12%, respectively.

Overall, this paper demonstrates an innovative use of LVLMs for city-level localization; however, some clarifications on specific points in the theoretical and experimental sections are still needed.

### Strengths
1. The cross-view alignment tuning in AddressVLM addresses the gap in fine-grained street-level localization for LVLMs, a challenging problem that previous work has not fully resolved. This is achieved through a novel image grafting mechanism and automatic label generation, which enhances the model's ability to recognize urban street patterns.

2. The authors introduce two VQA datasets specifically tailored for image address localization. It is hoped that the datasets used for the two-stage training, as well as the trained models and weights, can be made publicly available.

3. The paper is clearly and well written.

### Weaknesses
1. The experimental results lack evidence of the replicated GeoReasoner’s performance at the city and country levels. Is it comparable to the results in the original paper? This makes it difficult to determine whether the replication of GeoReasoner is reasonable.

2. Is there a comparison with UrbanCLIP and UrbanVLP?

3. The paper concludes that the optimal overlap ratio δ between the longer side of the street-view image and the satellite image is 0.5, but more extensive ablation experiments on different overlap ratios, such as values greater than 0.5, are missing. Quantitative experiments on the three grafting methods are also needed.

4. There is a lack of quantitative experiments to demonstrate whether performing the first stage Cross-view alignment tuning has a significant impact.

### Questions
In addition to Weaknesses, I have some confusion：
1. What datasets were used in the first and second stages? Were any additional datasets included? In the second stage, Address localization tuning uses formatted data for fine-tuning—does this impact the model’s performance on other tasks or dialogue capabilities? Are there experiments evaluating this effect?

2. Can the final trained LVLM model only output brief district names as shown in the paper? Is the LVLM capable of providing reasons or analyses that explain how it arrived at the location conclusion?

3. Given that Address localization tuning relies on the formatted VQA dataset proposed in the paper, would the model still return accurate district locations if questions were asked in a free-form style rather than constrained by templates?

4. In the Automatic Alignment Label Generation step, was another LVLM used, such as GPT-4?

5. In section 4.3, the paper states that unfreezing the Vision Encoder (VE) during the second stage generally improves performance compared to keeping it frozen. While this is apparent when comparing CD with (E, AddressVLM), it’s not clear when comparing AB. Why is this?

6. Does the street-view image need to be grafted onto the upper right corner of the satellite view? Would other positions work as well?

7. How does the model’s performance compare to other traditional geo-localization methods, such as Pigeon or GeoCLIP?

### Soundness
2

### Presentation
3

### Contribution
3
