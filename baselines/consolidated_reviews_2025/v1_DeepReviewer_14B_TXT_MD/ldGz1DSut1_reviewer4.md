### Summary

The paper investigates the coexistence of multiple deep learning-based image watermarks within the same image and demonstrates that they can coexist with minimal impact on image quality and decoding robustness. The authors also explore the potential of ensembling watermarking methods, showing that it can increase message capacity and create new trade-offs between capacity, accuracy, robustness, and image quality without retraining the base models. The study includes comprehensive experiments and analysis, providing insights into the practical implications of watermark coexistence and ensembling.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1) The paper addresses an underexplored area in the field of watermarking, specifically the coexistence and ensembling of multiple watermarks in deep learning-based methods.

2) The authors provide a comprehensive experimental analysis, demonstrating the feasibility of watermark coexistence and the benefits of ensembling.

3) The study shows that ensembling can increase message capacity and create new trade-offs between capacity, accuracy, robustness, and image quality.

### Weaknesses

#### Some Related Works


#### comment

1) While the paper demonstrates the feasibility of watermark coexistence and ensembling, it does not delve deeply into the theoretical reasons behind why certain watermarking methods coexist better than others. A more detailed theoretical analysis could provide a stronger foundation for the empirical findings and help in designing watermarking methods that are inherently more compatible for coexistence.

2) The paper focuses on image watermarking, but the principles of coexistence and ensembling might not directly translate to other media types such as video, audio, or text. Further research is needed to explore the applicability of these findings in other domains.

3) The paper does not extensively discuss the computational overhead associated with ensembling multiple watermarking methods. In practical applications, the increased computational cost of encoding and decoding multiple watermarks might be a significant concern, especially for real-time systems or resource-constrained devices.

4) The paper does not explore the potential security implications of watermark coexistence. For example, could an attacker exploit the presence of multiple watermarks to develop more effective attacks? Further research is needed to assess the security of coexisting watermarks.

5) The paper does not provide a detailed analysis of the trade-offs between capacity, accuracy, robustness, and image quality for different ensembling strategies. A more systematic exploration of these trade-offs would be valuable for practitioners.

### Suggestions

The paper would benefit from a more in-depth theoretical analysis of why certain watermarking methods exhibit better coexistence than others. While the empirical results are compelling, a theoretical framework could provide a deeper understanding of the underlying mechanisms. For instance, exploring the frequency domain characteristics of different watermarking techniques and how they interact could reveal why some methods are more compatible. Analyzing the orthogonality of the embedding spaces used by different watermarking algorithms could also provide insights into their coexistence capabilities. Furthermore, investigating the impact of different modulation schemes on coexistence would be valuable. A theoretical model that predicts the degree of coexistence based on the properties of the watermarking methods would be a significant contribution. This could involve analyzing the spectral properties of the watermarks and their interactions, potentially using tools from information theory or signal processing to quantify the degree of interference and compatibility.

To enhance the practical relevance of the study, the authors should investigate the computational overhead associated with ensembling multiple watermarking methods. This should include a detailed analysis of the time and memory requirements for both encoding and decoding processes. The analysis should consider different hardware platforms and software implementations to provide a comprehensive view of the computational costs. Furthermore, the authors should explore techniques to optimize the ensembling process to reduce the computational burden. For example, investigating the use of parallel processing or efficient algorithms could help mitigate the computational overhead. A practical guideline on how to choose the appropriate ensembling strategy based on the available computational resources would be beneficial. This could involve profiling the performance of different ensembling methods on various hardware configurations and providing recommendations based on the trade-off between performance and computational cost.

Finally, the paper should address the potential security implications of watermark coexistence. This should include an analysis of how the presence of multiple watermarks might affect the vulnerability of the watermarked content to attacks. For example, the authors should investigate whether the interaction of multiple watermarks could create new attack vectors or amplify existing ones. Exploring the robustness of coexisting watermarks against various attacks, such as removal, modification, and extraction attacks, is crucial. Furthermore, the authors should consider the potential for adversarial attacks that specifically target the coexistence of multiple watermarks. A thorough security analysis would provide a more complete picture of the practical implications of watermark coexistence. This could involve simulating various attack scenarios and evaluating the resilience of the coexisting watermarks under different conditions.

### Questions

1) How do the authors explain the observed differences in coexistence performance between different pairs of watermarking methods? Is there a theoretical basis for predicting which methods will coexist better?

2) What are the computational costs associated with ensembling multiple watermarking methods? How does this impact the practicality of the proposed approach?

3) How does the presence of multiple watermarks affect the security of the watermarked content? Are there any potential vulnerabilities introduced by watermark coexistence?

4) Can the authors provide more detailed guidelines on how to choose the appropriate ensembling strategy based on the desired trade-offs between capacity, accuracy, robustness, and image quality?

### Rating

6

### Confidence

4

**********
