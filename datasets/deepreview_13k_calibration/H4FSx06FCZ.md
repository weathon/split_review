# SecureGS: Boosting the Security and Fidelity of 3D Gaussian Splatting Steganography

- Decision: Accept
- Avg Score: 6.00
- Scores: 3, 8, 8, 6, 5

## Abstract
3D Gaussian splatting (3DGS) has emerged as a premier method for 3D representation due to its real-time rendering and high-quality outputs, underscoring the critical need to protect the copyright and privacy of 3D assets. Traditional NeRF steganography methods fail to address the explicit nature of 3DGS since its point cloud files are publicly accessible. Existing GS steganography solutions mitigate some issues but still struggle with reduced rendering fidelity, increased computational demands, and security flaws, especially in the security of the geometric structure of the visualized point cloud. To address these challenges, we propose a SecureGS, a secure and efficient 3DGS steganography framework inspired by Scaffold-GS's anchor point design and neural decoding. SecureGS utilizes a hybrid decoupled Gaussian encryption mechanism to embed offsets, scales, rotations, and RGB attributes of the hidden 3D Gaussian points within anchor point features, retrievable only by authorized users through privacy-preserving neural networks. To further enhance security, we propose a density region-aware anchor growing and pruning strategy that adaptively locates optimal hiding regions without exposing hidden information. Extensive experiments demonstrate that SecureGS significantly surpasses existing GS steganography methods in rendering fidelity, speed, and security, effectively concealing and accurately extracting 3D objects, images, and bits within original 3D scenes.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces SecureGS, an innovative framework aimed at enhancing the security and fidelity of 3D Gaussian Splatting (3DGS) steganography. It addresses critical challenges in embedding hidden information within 3D scenes, focusing on copyright protection and privacy. SecureGS employs a hybrid decoupled Gaussian encryption mechanism that allows for the secure embedding and retrieval of 3D objects, images, and bits, while maintaining high rendering quality. Key contributions include a density region-aware anchor growing and pruning strategy that enhances security and experimental results demonstrating significant improvements over existing 3DGS methods in rendering fidelity, speed, and overall security. This framework lays a strong foundation for future advancements in 3D steganography, balancing efficiency and security in digital asset management. However, this paper lacks innovation, and the security verification is not sufficient.

### Strengths
SecureGS showcases originality through its hybrid decoupled Gaussian encryption mechanism and a density region-aware anchor strategy. The paper is technically fine and clear, the algorithm seems to scale well, and the results on the different datasets compare very favorably with the different baselines. The experimental results that clearly demonstrate its advantages over existing methods. The clarity of the paper enhances its accessibility, guiding readers through complex concepts with effective visuals and precise descriptions.

### Weaknesses
1: SECUREGS and GS-Hider are notably similar, including their formulas, descriptions, and flowcharts. This resemblance suggests that the research content leans more towards optimizing the memory efficiency of GS-Hider rather than introducing substantial advancements. Consequently, the innovative aspects of this work appear insufficient to establish a distinct contribution to the field of 3DGS security.

2: In terms of robustness verification, this paper fails to address the effectiveness of SecureGS against adversarial attacks and lacks experimental results for hiding scenes within scenes. The framework's ability to withstand pruning does not appear to be robust. Furthermore, the source code for the baseline scheme (GS-Hider) has not been made publicly available, and the paper does not provide detailed descriptions of the relevant parameter settings. As a result, the experimental findings lack credibility and may not be convincing to the reader.

3: In terms of memory optimization, many existing memory optimization strategies use less than 20% of the memory of the original 3DGS, while SecureGS still retains a large number of redundant Gaussian points, which may hinder its ability to achieve real-time rendering in future 3DGS applications. This limitation poses a challenge for practical applications, especially in scenarios that require fast processing and high efficiency.

4: It is better to describe the current research status more systematically. The figures in your paper are a bit blurry. Please consider replacing them with clearer ones.

### Questions
Please list up and carefully describe any questions and suggestions for the authors. Think of the things where a response from the author can change your opinion, clarify a confusion or address a limitation. This is important for a productive rebuttal and discussion phase with the authors.

How effective is SecureGS in defending against adversarial attacks? Please show the code and ablation experiment parameters of the paper, especially the details of the comparison with GS-hider.

### Soundness
2

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
5

### Summary
The paper proposes SecureGS, a new 3D Gaussian splatting (3DGS) steganography framework that improves the security and fidelity of hiding information in 3D scenes.  Existing methods struggle with fidelity, speed, and security, especially regarding the point cloud's geometric structure. 
SecureGS uses a hybrid decoupled Gaussian encryption, concealing hidden Gaussian point positions with a privacy-preserving offset predictor only authorized users can access.  A density region-aware anchor growing strategy further enhances security by dynamically adjusting anchor point density to mask the hidden object's geometry without sacrificing speed or storage.  
Experiments show SecureGS significantly outperforms the existing method GS-Hider, especially for geometry security.

### Strengths
1. SecureGS proposes a hybrid decoupled Gaussian encryption to embed information within anchor points, accessible only to authorized users. 
2. A density region-aware anchor growing and pruning strategy improves security by preventing exposure of the hidden object. 
3.  SecureGS achieves this by ensuring both file format and geometric structure security, compared with the existing baselines GS-Hider and 3DGS+StegaNeRF.

### Weaknesses
1. While the proposed region-aware density optimization effectively utilizes growing 3D Gaussian points, it results in an increased model size, which is a key concern in 3DGS. Actions should be taken to implement specific strategies aimed at mitigating the increased model size. Additionally, the tradeoff between enhanced security and the resulting model size should be thoroughly discussed to provide a clearer perspective on the implications of the proposed approach.

2. The bit accuracy relies on an MLP layer, which is per-scene optimized, which may lead to an unfair comparison setting with the previous baselines CopyRNeRF and NeRFProtector. Why the per-scene optimization-based MLP method is chosen here instead of considering generalizable message extraction methods such as HiDDeN for bit message extraction? Furthermore, the per-scene optimization of the MLP could introduce overfitting issues, potentially leading to poor generalization to unseen data or different scenes. This aspect needs further investigation and discussion.

### Questions
1. Is the proposed method compatible with the GS compression method such as LightGaussian or CompactGS? What are the potential challenges in integrating compression with the proposed steganography approach?
2. Regarding the 3DGS having a point cloud geometry format, how is the 3D robustness towards 3D distortions? Such as Gaussian noise with a Gaussian Kernel $\sigma$, Dropout operation to randomly remove a fraction of the points, and Cropout operations to remove points in a specific 3D bounding box volume.
3. What if the attacker knows the encryption method and tries to remove or add perturbations on the anchor points in the 3DGS model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents SecureGS, a novel method for 3D Gaussian splatting (3DGS) steganography that addresses significant security and fidelity challenges in protecting 3DGS-based assets. It proposes a hybrid decoupled Gaussian encryption mechanism and a region-aware density optimization strategy, enabling efficient embedding and retrieval of hidden 3D objects, images, and bits within original 3D scenes.

### Strengths
(+) Previous steganography lacks a strategy for the explicit point cloud from 3DGS. The paper introduces an interesting and original approach to 3DGS steganography, emphasizing security and fidelity. This innovative framework could pave the way for advancements in the field, inspiring further research into secure 3D content transmission.

(+) Overall, this paper is well-written and has a logical structure. The motivation and contributions are clearly articulated, making it accessible to readers. The figures and diagrams effectively illustrate complex concepts, enhancing reader comprehension.

(+) The authors conduct comprehensive experiments that validate the generalizability and effectiveness of the proposed method across various scenarios. These experiments demonstrate the method's superiority and provide valuable insights into its practical applicability in different contexts.

### Weaknesses
(-) The proposed methods, particularly the hybrid encryption and optimization strategies, may introduce complexity that could hinder practical adoption. This complexity might deter practitioners who require straightforward solutions for embedding and retrieving hidden information.

(-) The enhancements in security and fidelity may come at the cost of increased computational requirements, which could limit real-time applications. If the computational demands are too high, they may negate the benefits of improved rendering fidelity in time-sensitive environments.



### Questions
1.	How does SecureGS compare to traditional steganography methods in terms of computational efficiency and resource requirements?

2.	What specific measures have you taken to ensure the robustness of your method against various types of attacks or degradation, especially in practical deployment scenarios?

3.	Given the complexity of the proposed methods, how do you envision simplifying the implementation for practitioners who may lack advanced technical expertise in 3D steganography?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies a safe and efficient 3D steganography framework. The proposed SecureGS addresses issues existed in previous NeRF-based steganography solutions through a hybrid decoupled Gaussian encryption representation, which secures both file format and geometric structure while concealing 3D objects, images, and bits within anchor points that can only be decoded by authorized users. SecureGS incorporates a region-aware density optimization (RDO) strategy, dynamically adjusting anchor point growth to avoid leaking hidden content.

### Strengths
1. SecureGS provides dual security by protecting both the file format and geometric structure, which reduces risks of hidden information exposure in public files. 

2. The SecureGS framework achieves real-time rendering rates, nearly three times faster than GS-Hider, with storage requirements that are substantially lower.

3. Evaluation results demonstrate SecureGS's resilience to anchor point pruning, achieving reliable decoding.

### Weaknesses
1. Although the author mentioned three shortcomings of existing methods in Introduction, the description is not intuitive and difficult to understand. For example, the concepts of format security and geometric structure security are not explained clearly at the part. I suggest that the current Fig. 2 should be shown at the beginning rather than the pipeline of the proposed method, and the relevant concepts should be described in more detail.

2. The authors claimed that the proposed method addresses the issue of rendering quality existing previous methods. However, the experimental results show that the average improvement is only 1.16 dB. In my experience, such slight changes in PSNR values ​​usually result in only negligible subjective differences. Additionally, the $PSNR_o$ values in Table 2 and 4 are relatively low (below 30 dB), so I think the high-fidelity restoration of hidden objects comes at the expense of the quality of the original scene restoration. This further raises concerns about the fairness of the comparison in Table 1 and 5, because the author did not show the results of $PSNR_0$.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes SecureGS, a 3D Gaussian splatting steganography framework designed to improve fidelity and security in 3D scene steganography. SecureGS combines features from GS-Hider and Scaffold-GS, introducing a hybrid decoupled Gaussian encryption representation where hidden information and original scenes are separately encoded through anchor points. Additionally, a region-aware anchor growth and pruning strategy is introduced to optimize anchor density, enhancing the concealment of hidden information and rendering quality. The experimental results show SecureGS outperforms GS-Hider in rendering speed, fidelity, and security.

### Strengths
1. SecureGS effectively combines the strengths of Scaffold-GS and GS-Hider, leveraging anchors and region-aware density optimization to achieve better fidelity and security in information hiding.
2. The region-aware anchor growth and pruning strategy successfully prevents hidden information from being exposed in the public point cloud by adaptively optimizing anchor density.
3. SecureGS shows improved rendering quality, fidelity, and speed compared to GS-Hider and 3DGS+StegaNeRF, particularly in reducing interference between hidden content and original scenes.

### Weaknesses
1. SecureGS essentially combines elements of GS-Hider and Scaffold-GS, with limited originality. The core method of SecureGS is to create separate anchor points for the hidden objects and the original scene, which is quite similar to GS-Hider’s approach of creating Gaussian points for both separately—only differing in terms of abstraction level, from points to anchors. While SecureGS introduces a region-aware anchor growth and pruning strategy, these improvements are mostly about implementation details rather than any fundamental innovation. Moreover, the anchor growth and pruning strategies resemble those seen in previous 3D scene optimization work, which makes it hard to classify them as novel contributions. Consequently, the theoretical advancement of SecureGS compared to GS-Hider and Scaffold-GS is not adequately demonstrated, and the overall method feels more like an incremental combination of existing techniques rather than a breakthrough, resulting in relatively weak innovation and technical contributions.

2. The motivation for using Scaffold-GS as the foundational framework is insufficiently explained. Although the paper mentions that using anchor points to generate Gaussian points helps keep their attributes and positions secure since they do not need to be directly stored, these advantages are primarily about rendering efficiency and scalability, rather than any inherent suitability for steganography or encryption tasks. Therefore, directly equating the properties of Scaffold-GS with the encryption encoder-decoder in steganography feels like a logical leap without rigorous backing. The authors need to clarify how Scaffold-GS specifically offers unique advantages for the steganography task and strengthen the rationale for this choice.

3. The ablation studies are too simplistic and fail to convincingly demonstrate SecureGS's unique contributions. Despite claims of outperforming other methods in terms of visual quality (such as PSNR) and file size, the reasons for these improvements are insufficiently explained. As shown in Table 1, much of the performance gain could simply be attributed to the foundation provided by Scaffold-GS, rather than any innovations introduced in SecureGS. Since Scaffold-GS is an upgraded version of Gaussian Splatting, which inherently improves rendering quality and efficiency, directly comparing SecureGS (based on Scaffold-GS) to GS-Hider (based on 3DGS) is insufficient to prove the superiority of the proposed method. The authors need more comprehensive ablation studies to clarify the independent contributions of each new module to ensure that the observed improvements come from their own innovations rather than from Scaffold-GS's inherent advantages. Otherwise, it is difficult to consider these enhancements as unique contributions of SecureGS.

4. SecureGS heavily relies on the Scaffold-GS framework, particularly in the way anchor generation and density optimization are integrated. This deep coupling makes SecureGS less flexible and not readily applicable to other Gaussian splatting models.

5. The effectiveness of the region-aware anchor growth and pruning strategy lacks systematic theoretical support. There is no formal proof or analysis provided to demonstrate whether this strategy is optimal for steganography tasks. Section 3.4's gradient handling and anchor splitting thresholds are mostly based on empirical choices rather than rigorous theoretical derivation. Without a theoretical foundation, the robustness and generalizability of these strategies across different scenes are uncertain, which reduces the reliability and stability of the proposed method in real-world applications.

6. The robustness experiments in SecureGS are insufficient, as they only consider the impact of random anchor pruning, neglecting other significant attack scenarios that could affect the security of steganography. Robustness is critical in evaluating steganographic methods, yet SecureGS lacks tests on important attacks such as point cloud denoising, random point deletion or addition, and geometric transformations. These factors are as crucial as visual quality in the domain of steganography and watermarking, and without proper evaluation of these aspects, the practical security of SecureGS remains questionable.

7. In Table 1, SecureGS shows a significant increase in PSNR compared to Scaffold-GS, which the authors attribute to increased anchor density and the decoupling strategy. However, it seems questionable that the PSNR for the original scene is higher despite SecureGS embedding additional hidden information. Scaffold-GS has no additional hidden data and can focus solely on rendering the scene, while SecureGS introduces extra information that could potentially interfere with the fidelity of the original scene. There is no sufficient core optimization provided in the paper to justify this improvement. This effect seems more likely due to increased anchor density and computational resources rather than a genuine methodological advancement in balancing steganography with scene fidelity. More theoretical analysis or experimental validation is recommended to clarify this observation, ensuring that the PSNR improvements are due to actual innovation rather than just additional resource allocation.

### Questions
See weaknesses.

By the way, I do have a small question, purely out of curiosity and not related to the rating: If we perform point cloud downsampling on the anchor points encrypted by SecureGS, would the hidden scene become more apparent in the resulting sparse point cloud? Could it result in a situation similar to GS-Hider as shown in Fig. 7?

### Soundness
2

### Presentation
3

### Contribution
1
