### Summary

The paper explores the coexistence and ensembling of watermarks, focusing on deep image watermarking methods. It examines the potential for multiple watermarks to be embedded in the same media without interfering with each other, and how ensembling these methods can increase message capacity and create new trade-offs between capacity, accuracy, robustness, and image quality. The study provides a comprehensive analysis of the coexistence of various open-source watermarks, demonstrating that they can coexist with minimal impact on image quality and decoding robustness. The paper also introduces the concept of using ensembling to modify the performance of existing methods without retraining.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper explores a relatively unexplored area of watermark coexistence and ensembling, providing valuable insights for the research community and practitioners.
2. The paper is well-written and organized, making it easy to follow the authors' arguments and findings. The use of figures and tables enhances the presentation of the results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more in-depth analysis of the limitations of watermark coexistence and ensembling, providing a more balanced view of the proposed methods.
2. The study could further explore the theoretical underpinnings of why watermarks can coexist, which would strengthen the paper's contributions.

3. The authors should delve deeper into the potential negative impacts of watermark coexistence, such as the possibility of interference or degradation of image quality. While the paper touches on the robustness of the proposed methods, a more thorough analysis of their limitations is needed. Specifically, the paper should investigate scenarios where the watermarks might interfere with each other, leading to a decrease in decoding accuracy or an increase in perceptual artifacts. For example, what happens when the watermark embedding capacities are pushed to their limits? Does the super watermark introduce any bias or artifacts that could be exploited by an adversary? These aspects need to be explored in more detail.

4. The paper could benefit from a more rigorous theoretical framework that explains the observed coexistence of watermarks. The current explanation is somewhat superficial. A more detailed analysis of the underlying mathematical principles that allow multiple watermarks to coexist without significant interference would greatly enhance the paper's contribution. For instance, the authors could explore the orthogonality of the embedding spaces or the statistical properties of the noise introduced by each watermarking method. This would provide a more solid foundation for the empirical observations.

5. The paper could explore the potential for adversarial attacks on the coexisting watermarks and how to mitigate them. The current study does not consider the possibility of an attacker trying to remove or manipulate the watermarks. It is crucial to investigate the vulnerability of the proposed methods to various adversarial attacks, such as those aimed at removing the watermarks or altering the embedded information. The paper should also discuss potential countermeasures to enhance the security of the coexisting watermarks.

### Suggestions

To address the limitations regarding the in-depth analysis of watermark coexistence, the authors should conduct a series of experiments that systematically vary the embedding strengths and capacities of the individual watermarks. This would help to identify the thresholds at which interference becomes significant and to characterize the trade-offs between watermark robustness, image quality, and coexistence. Specifically, the authors should explore scenarios where the watermarks are embedded at high strengths, pushing the limits of the medium's capacity. This would reveal potential degradation in image quality or decoding accuracy. Furthermore, the authors should investigate the impact of the super watermark on the overall image quality and decoding performance. It is important to determine if the super watermark introduces any bias or artifacts that could be exploited by an adversary. The analysis should include a quantitative evaluation of the perceptual quality of the watermarked images using metrics such as PSNR and SSIM, as well as a qualitative assessment of the visibility of the watermarks.

To strengthen the theoretical underpinnings of the paper, the authors should delve into the mathematical properties of the watermarking algorithms. This could involve analyzing the frequency spectra of the watermarks, the statistical properties of the noise they introduce, and the orthogonality of the embedding spaces. The authors should explore whether the observed coexistence is a result of the watermarks occupying different frequency bands or whether there are other underlying mechanisms at play. A more rigorous theoretical framework would provide a deeper understanding of the conditions under which watermark coexistence is possible and would allow for the development of more robust and efficient watermarking methods. This analysis should also consider the potential for interference between watermarks and how to mitigate it. The authors could also explore the use of techniques such as orthogonal coding or spread spectrum modulation to minimize interference.

Finally, the authors should investigate the vulnerability of the coexisting watermarks to various adversarial attacks. This could include attacks aimed at removing the watermarks, altering the embedded information, or confusing the decoder. The authors should explore potential countermeasures to enhance the security of the watermarks, such as the use of error-correcting codes, cryptographic techniques, or robust embedding algorithms. The paper should also discuss the trade-offs between security, robustness, and image quality. It is important to determine the extent to which the proposed methods can withstand adversarial attacks without compromising the quality of the watermarked images. The authors should also consider the computational cost of the proposed countermeasures and their impact on the overall performance of the watermarking system.

### Questions

1. How do the authors ensure the generalizability of their findings to other types of media, such as video or audio?
2. What are the computational costs associated with ensembling multiple watermarking methods, and how does this impact the practicality of the proposed approach?
3. Could the authors provide more details on the specific types of attacks that the coexisting watermarks can withstand?

### Rating

6

### Confidence

3

**********
