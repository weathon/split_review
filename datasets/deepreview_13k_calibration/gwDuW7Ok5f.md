# Dual Associated Encoder for Face Restoration

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 8, 8, 5, 5

## Abstract
Restoring facial details from low-quality (LQ) images has remained challenging due to the nature of the problem caused by various degradations in the wild. 
The codebook prior has been proposed to address the ill-posed problems by leveraging an autoencoder and learned codebook of high-quality (HQ) features, achieving remarkable quality.
However, existing approaches in this paradigm frequently depend on a single encoder pre-trained on HQ data for restoring HQ images, disregarding the domain gap and distinct feature representations between LQ and HQ images.
As a result, encoding LQ inputs with the same encoder could be insufficient, resulting in imprecise feature representation and leading to suboptimal performance.
To tackle this problem, we propose a novel dual-branch framework named \textit{DAEFR}. Our method introduces an auxiliary LQ branch that extracts domain-specific information from the LQ inputs. 
Additionally, we incorporate association training to promote effective synergy between the two branches, enhancing code prediction and restoration quality.
We evaluate the effectiveness of DAEFR on both synthetic and real-world datasets, demonstrating its superior performance in restoring facial details.
Project page: \href{https://liagm.io/DAEFR/}{https://liagm.io/DAEFR/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents "DAEFR," a novel framework for blind face restoration, specifically focusing on restoring high-quality facial images from low-quality ones. This challenge arises due to complex and unknown sources of degradation in facial images. The key innovation in DAEFR is the introduction of an auxiliary low-quality (LQ) encoder, trained exclusively on LQ data. This branch captures domain-specific information from LQ inputs, addressing the domain gap and distinct feature representations between LQ and HQ images.

DAEFR's methodology involves discrete codebook learning for both HQ and LQ domains, feature association between the HQ and LQ encoders, and a feature fusion stage that combines the information from both encoders. This approach is designed to overcome limitations in existing codebook methods, which often exhibit domain bias due to a reliance on encoders pre-trained solely on HQ data.

The paper's contributions are significant in several aspects:
*  Introduction of the auxiliary LQ encoder for more accurate LQ domain feature representation.
* Utilization of association and feature fusion methods to effectively bridge the domain gap between LQ and HQ images, enhancing restoration outcomes.
* A comprehensive evaluation of DAEFR on synthetic and real-world datasets demonstrates superior performance in restoring facial details compared to existing state-of-the-art methods.
Overall, the paper proposes a novel and effective approach to address the challenges of blind face restoration under severe degradation, emphasizing maintaining the fidelity and identity information present in the original LQ images.

### Strengths
The paper's strengths are notable across various dimensions, including originality, quality, clarity, and significance:

### Originality
- **Innovative Approach**: Introducing an auxiliary LQ encoder specifically trained on LQ data is a creative solution to the domain gap problem in image restoration. This approach significantly differs from conventional methods, primarily relying on encoders pre-trained on HQ data.
- **Feature Fusion and Association Techniques**: The application of feature association techniques and the subsequent fusion of features from both LQ and HQ encoders demonstrate a novel integration of ideas, enhancing the restoration process's effectiveness.

### Quality
- **Comprehensive Evaluation**: The method is thoroughly evaluated on synthetic and real-world datasets, providing substantial evidence of its effectiveness. The comparison with state-of-the-art methods further underlines the quality of the proposed approach.
- **Robustness and Fidelity**: The paper demonstrates the robustness of the DAEFR method in preserving the identity and details in restored images, even under severe degradation conditions.

### Clarity
- **Well-Structured Presentation**: The paper is well-organized, with each section logically flowing into the next. The methodology, experimental setup, and results are clearly explained, making them accessible to readers.
- **Effective Use of Visual Aids**: Including figures and tables aids in illustrating the methodology and showcasing the results, enhancing the overall clarity of the paper.

### Significance
- **Contribution to Blind Face Restoration**: The paper addresses a significant challenge in image restoration, particularly in restoring HQ images from LQ ones. The proposed solution can potentially influence future research directions in this area.
- **Applicability and Impact**: The approach can greatly interest researchers and practitioners in computer vision, offering a novel tool for addressing a common problem in image restoration. Its applicability to real-world, severely degraded images enhances its significance.

### Weaknesses
1.	Absence of Future Research Guidance: The paper does not offer any recommendations or insights into potential future research directions or enhancements for the proposed method.

2.	Omission of Limitation Discourse: The paper lacks a discussion regarding its limitations and possible factors for analysis.

### Questions
1. **Generalization to Other Image Types**: How well does the DAEFR method generalize to other images beyond facial images? Are there specific types of image degradation or different domains where DAEFR might not perform as effectively?

2. **Handling Extreme Degradations**: Could you provide more insights into how DAEFR performs under extremely diverse or uncommon image degradations? Understanding its limitations in such scenarios would be crucial for practical applications.

3. **Computational Efficiency**: Can you provide details regarding the computational efficiency of DAEFR, such as processing time and resource requirements? How scalable is the method for larger datasets or higher-resolution images?

4. **Impact of Auxiliary Encoder**: Could you elaborate on the specific impact of the auxiliary LQ encoder in the restoration process? For instance, how does the restoration quality differ when the auxiliary encoder is not used?

5. **Comparison with Diverse Restoration Methods**: The paper compares DAEFR with similar restoration approaches. Could you compare its performance with restoration techniques that use fundamentally different principles?

6. **User Study for Qualitative Assessment**: Have you considered conducting a user study to evaluate the perceptual quality of the restored images? This could provide valuable insights into the real-world applicability of DAEFR.

7. **Further Methodological Details**: Could you provide more technical details or insights on the feature association techniques used? How do they specifically contribute to bridging the domain gap between LQ and HQ images?

Responses to these questions could greatly enhance the understanding of DAEFR's capabilities, limitations, and potential areas for future development.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new approach called the Dual Associated Encoder for facial restoration. In this method, an auxiliary Low-Quality (LQ) branch is introduced to extract vital information from LQ inputs. Subsequently, it employs a structure similar to CLIP to establish connections between the LQ and High-Quality (HQ) encoders. This connection aims to reduce the domain gap and information loss when restoring HQ images from LQ inputs. The experimental outcomes illustrate the highly promising performance of this novel approach.

### Strengths
1.	The paper offers a coherent and well-founded justification for the research, with a method design that closely aligns with the research objectives.
2.	The paper effectively communicates the method, ensuring readers can easily comprehend the underlying concepts and techniques.
3.	The experimental results showcase remarkable performance, affirming the method's efficacy in tackling the face restoration challenge.

### Weaknesses
1. Can you provide a detailed explanation of the primary differentiation between DAEFR and CodeFormer?

2. The paper does not delve into its limitations or potential factors for analysis, which would greatly enrich its discussion.

3. The paper outperforms baseline methods in the downstream face recognition task. Could you provide a comprehensive explanation of these results?

4. The paper does not provide any suggestions or insights into potential avenues for future research or improvements to the proposed method.

### Questions
1.	While the paper predominantly highlights the advantages of the proposed method, could you offer instances where the method encountered shortcomings or limitations?
2.	Could you elaborate on the key distinction between DAEFR and CodeFormer?
3.	Can you provide further experimental details into the "Effectiveness of Low-Quality Feature from Auxiliary Branch" as examined in your ablation studies?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a dual-branch framework, named DAEFR, designed for the restoration of high-quality (HQ) facial details from low-quality (LQ) images. Within this framework, an auxiliary LQ encoder and an HQ encoder are employed in conjunction with feature association techniques to capture visual characteristics from LQ images. Subsequently, the features extracted from both encoders are combined to enhance their quality. Finally, the HQ decoder is utilized for the reconstruction of high-quality images. The effectiveness of DAEFR is evaluated using both real-world and synthetic datasets.

### Strengths
1. The notion of incorporating an additional encoder with weight sharing is intriguing.

2. The authors have extensively verified the significance of each component via thorough ablation studies.

3. This approach adeptly addresses various common and severe degradations and maintains a high standard of writing quality.

### Weaknesses
1. The contribution looks marginal to me since all the methods used in different stage are well designed and demonstrated. Adding another stream for low-resolution might not be a major contribution for a top-tier venue like ICLR.
2. I got some questions for the experimental results which can be seen in the questions part.



### Questions
Please discuss the concerns in the Weaknesses Section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a framework, named dual associated encoder for face restoration (DAEFR), for face restoration. Specifically, different from the existing codebook based methods using only one autoencoder for high-resolution images, the authors propose to add another stream for low-resolution images. To fuse and align the features from both low and high resolution images, an association stage is designed. The associated features then will be extracted and utilized for face restoration.

Experimental results have demonstrated the effectiveness of the proposed method.

### Strengths
1. The paper is well written.
2. The idea is well presented, explained, and demonstrated.
3. The proposed method may inspire the researchers in this area.

### Weaknesses
1.	The full name of the proposed framework, DAEFR, is missing. It should be mentioned on its first occurrence in the paper.
2.	The proposed method requires training two sets of encoder and decoder for both HQ and LQ images. This will double the training resource requirements.
3.	I think it will be better if there is more elaboration on the domain gap issue that the current works exist, i.e., the motivation of the paper. Currently, it is not intuitive from figure 1 and from current discussion.
4.	Check the spellings. For example, “recently” on the beginning of second paragraph in the “Vector Quantized Codebook Prior” of the related work.
5.	There are some confusions about the training process of the network. In the first stage (section 3.1), you firstly train the two autoencoders of LQ and HQ using the codebook loss. After the first-stage training is complete, you train the two encoders using both the codebook loss and the association loss. Why not combine the two stages into one, or just apply the association loss in stage 2? Besides, in stage 3, you state in the Training Objectives that the MHCA and transformer module are trained in this stage. However, from figure 2(c), the two encoders seem not to be frozen during stage 3.
6.	The results in Table 1 indicate that the proposed method does not significantly outperform other methods, especially for the synthetic CelebA-Test dataset.

### Questions
In Table 2, it seems like all the alter methods outperform the proposed method in terms of LPIPS. Please give discussions or visualizations to explain why this happens.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To address the domain gap between low-quality and high-quality images and improve the performance of face restoration, the paper introduces a novel framework called DAEFR. This framework incorporates LQ (low-quality) image domain information by introducing an auxiliary branch that extracts unique LQ domain-specific features to complement the HQ (high-quality) domain information. To further align the features between the HQ and LQ domains, the paper employs a CLIP-like constraint to enhance the correlation between the two domains. Additionally, to facilitate better feature fusion between these two domains, the framework introduces a multihead cross-attention module. Evaluation results demonstrate the effectiveness of DAEFR.

### Strengths
1.	The paper proposes a framework designed to incorporate distinctive features from low-quality (LQ) images, thereby enhancing the face restoration task.
2.	To mitigate the domain gap between HQ and LQ images, the paper proposes an association strategy during training, and incorporates a multihead cross-attention module for better feature fusion between these two domains.
3.	The experiments on both synthetic and real-world datasets demonstrate the effectiveness of the proposed framework.

### Weaknesses
1.	The full name of the proposed framework, DAEFR, is missing. It should be mentioned on its first occurrence in the paper.
2.	The proposed method requires training two sets of encoder and decoder for both HQ and LQ images. This will double the training resource requirements.
3.	I think it will be better if there is more elaboration on the domain gap issue that the current works exist, i.e., the motivation of the paper. Currently, it is not intuitive from figure 1 and from current discussion.
4.	Check the spellings. For example, “recently” on the beginning of second paragraph in the “Vector Quantized Codebook Prior” of the related work.
5.	There are some confusions about the training process of the network. In the first stage (section 3.1), you firstly train the two autoencoders of LQ and HQ using the codebook loss. After the first-stage training is complete, you train the two encoders using both the codebook loss and the association loss. Why not combine the two stages into one, or just apply the association loss in stage 2? Besides, in stage 3, you state in the Training Objectives that the MHCA and transformer module are trained in this stage. However, from figure 2(c), the two encoders seem not to be frozen during stage 3.
6.	The results in Table 1 indicate that the proposed method does not significantly outperform other methods, especially for the synthetic CelebA-Test dataset.

### Questions
Refer to weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
