# Revitalizing Channel-dimension Fourier Transform for Image Enhancement

- Decision: Reject
- Scores: 6, 6, 1, 8

## Abstract
Exploring the global representations of Fourier transform for image enhancement has become an alternative and made significant advancements. However, previous works only operate in the spatial dimensional, overlooking the potential of the channel dimension that inherently possesses discriminative features. In this work, we propose a fresh perspective, channel-dimension Fourier transform, for image enhancement. Our designs are simple yet effective and comprise three straightforward steps: applying the Fourier transform to the channel dimension to obtain channel-wise Fourier domain features, performing a channel-wise transformation on both its amplitude and phase components, and then reverting back to the spatial domain. Following the above rules, we offer three alternative implementation formats of the channel transform in different operational spaces, performing operations in 1) the global vector with higher orders; 2)  the global vector with channel groups; and 3) the Fourier features derived from spatial-based Fourier transform. The above core designs, as general operators, can be seamlessly integrated with enhancement networks, achieving remarkable gains and building efficient models. Through extensive experiments on multiple image enhancement tasks, like low-light image enhancement, exposure correction, SDR2HDR translation, and underwater image enhancement, our designs exhibit consistent performance gains. The code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
1. A fresh perspective of Channel-dimension Fourier transform learning (CFTL) mechanism is proposed for image enhancement with three steps design. 
2. Based on the CFTL mechanism , several usage formats are derived, which are compatible with existing methods.
3. The proposed approach showcases extensive ability across diverse image enhancement tasks with performance improvements over the baseline methods.

### Strengths
This paper brings a novel idea of channel-dimension Fourier transform with some strengths:   
1. The overall framework is simple but fresh with introducing negligible computation costs.
2. The reasonableness of the approach’s design is presented with illustrations. 
3. The experiments are sufficient to showcase the effectiveness of the introduced approach. Intermediate results are comprehensive to depict how the approach works.
4. The writing and organization are clear to follow.

### Weaknesses
However, there are several weakness/concerns need to be discussed, especially about some technique descriptions:
1. As far as I know, there is another work [1] attempts to introduce frequency design into channel dimension attention. Although the design and motivation behind the two works are different,  the relevance between the two works are not illustrated. Specifically, the paper does not clearly articulate how its approach differs from [1] in terms of the specific frequency components being leveraged and the resulting impact on channel interactions. A more detailed comparison of the mathematical formulations and the practical implications of these differences is needed.
2. As a core claim, “The primary objective of CFTL is to capture global discriminative
representations by modeling channel-dimension discrepancy ”. What would this property help improve image enhancement are not well-explained. The notion of 'channel-dimension discrepancy' is not sufficiently defined, and it is unclear how modeling this discrepancy leads to improved image enhancement. The paper needs to provide a more rigorous explanation of the underlying mechanism and how it relates to the specific image enhancement tasks.
3. As a core design space, the channel-dimension Fourier transform is applied in the global pooling-based space. The necessity of applying the core operation in this space are not fully discussed. What about using other spaces that possess global information properties? The paper should explore and justify why the global pooling space is the optimal choice for applying the channel-dimension Fourier transform, considering other potential spaces that might also capture global information, such as those derived from self-attention mechanisms or alternative pooling strategies. A comparative analysis of these options would strengthen the argument.
4. As the concrete implementation, the Eq.(6) introduces the attention operation without many explanations. The introduction of the attention operation in Eq. (6) lacks sufficient justification. The paper should elaborate on why this specific attention mechanism is chosen and how it contributes to the overall effectiveness of the proposed method. The relationship between the attention weights and the channel-dimension Fourier transform also needs to be clarified.
5. Based on the above concerns, how to come up with the idea of the channel-dimension Fourier transform is not discussed, although its mechanism is illustrated. The paper should provide more insight into the motivation behind using the channel-dimension Fourier transform. What specific limitations of existing methods led to this design choice? A clear explanation of the rationale behind this approach is crucial for understanding its significance.
6. Besides, more qualitative results are suggested to supplement in the appendix.

### Questions
Please see the above Weakness.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors introduces the channel-dimension Fourier transform for image enhancement. Its design is simple yet effective and comprise three straightforward steps.
The implementation formats is plug-and-play with previous image enhancement networks.
The authors experimentally evaluate the proposed model on various image enhancement tasks to depict its effectiveness.

### Strengths
(i) Overall, the idea is novel and interesting, and authors have clearly presented the motivation and algorithm with numerous figures and descriptions, making the principle of the algorithm easy to understand. 
(ii) The core module design is simple and easy to implement. One particularly inspiring view of this algorithm is that it provides a new perspective of understanding global information representation.  
(iii) The authors have also performed various experiments to validate the motivation, the effectiveness and efficacy of the algorithm, and the extensive application usage of the algorithm.

### Weaknesses
 (i) Authors have performed experiments on various architectures, but some of them are a bit-of-date. In this way, I suspect if I just apply some other operations such as channel attention or spatial attention, the performance could also be improved a lot.  
(ii) If I understand correctly, the improvement comes from the global information modeling. Nevertheless, most of baselines are CNN-based. Therefore, I doubt whether the algorithm would work when the baseline is set as the architecture with large receptive field.   
(iii) Since authors provide various formats of the algorithm, and most of the formats achieve comparable results. I doubt if it is necessary to design so many formats for the usage. 
(iv) The numerical results are improved with the algorithm, but the global information is easy to be affected. I doubt whether the improved version of the baseline has weak generalization ability than the baseline networks.

### Questions
(i) I strongly suggest to include more contemporary method as the baseline methods. 
(ii) I strongly suggest to discuss whether the generalization ability would be affected. 
(iii) I suggest more tasks that related to image enhancement can be included for discuss, such as shadow removal, image harmony and style transfer.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new Fourier transform for image enhancement, consisting of three steps: applying Fourier transform to the channel dimension to obtain channel-wise Fourier domain features, performing a channel-wise transformation on both its amplitude and phase components, and then reverting back to the spatial domain. Based on these three steps, three strategies of channel transform are designed. Extensive experiments are conducted to show the effectiveness of the proposed method.

### Strengths
1.	The proposed method provides a perspective to formulate new Fourier transform for image enhancement, and has achieved SOTA performance on different tasks with efficient parameter number and flops. 

2.	The experiments are sufficient in both main paper and supp.

3.	The writing and organization of this paper is great.

### Weaknesses
1.	The ablation studies in Table 5 can be conducted on more datasets to comprehensively show the effects of each component.

2.	More visual comparisons should be provided as these of Fig. 6.

### Questions
Is the baseline and the baseline with CFTL trained with the same iteration, or is trained still to be converged?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigate a new mechanism of the channel-dimension Fourier transform to enhance the discriminativity of the global information. Based on the core mechanism, the method design consists of several implementation formats. Extensive experiments over several image enhancement tasks and datasets demonstrates the effectiveness and versatility of the proposed method for image enhancement.

### Strengths
1. This paper investigates a new mechanism of channel-dimension Fourier transform, which has not been discussed before as I know. As a new technique, its advantages and mechnism are well-been illustrated.
2. This paper presents quantities of experiments to verify the effectiveness and general ability of the proposed method in both main body and appendix. Moreover, this paper also present quantities of analysis in appendix to exhibit the method’s mechanism, which is inspiring.
3. This paper also provides several implementation formats, which are easy to implement and easy to follow.

### Weaknesses
1. This paper contains few visual results. As an image processing paper, the number of visual results are limited to some extent. 
2. This paper presents several implementation formats. However, the relationship between these formats are not provided. How to derive different implementation formats from the original one?
3. The ablation studies are mainly conducted on exposure correction as shown in Table 5. However, as a main image enhancement task, this paper need to supplement ablation studies on the low-light image enhancement task to verify the effectiveness of the method’s design.

### Questions
Can authors provide more visual results? This is important to depict the effectiveness of the proposed method. Moreover, can authors discuss why the several implementation formats are designed in such manner?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
