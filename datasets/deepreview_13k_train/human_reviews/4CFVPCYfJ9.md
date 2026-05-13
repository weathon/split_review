# Does Vector Quantization Fail in Spatio-Temporal Forecasting? Exploring a Differentiable Sparse Soft-Vector Quantization Approach

- Decision: Reject
- Scores: 5, 8, 5, 6

## Abstract
Spatio-temporal forecasting is crucial in various fields and requires a careful balance between identifying subtle patterns and filtering out noise. Vector quantization (VQ) appears well-suited for this purpose, as it quantizes input vectors into a set of codebook vectors or patterns. Although VQ has shown promise in various computer vision tasks, it surprisingly falls short in enhancing the accuracy of spatio-temporal forecasting. We attribute this to two main issues: inaccurate optimization due to non-differentiability and limited representation power in hard VQ. To tackle these challenges, we introduce Differentiable Sparse Soft-Vector Quantization (SVQ), the first VQ method to enhance spatio-temporal forecasting. SVQ balances detail preservation with noise reduction, offering full differentiability and a solid foundation in sparse regression. Our approach employs a two-layer MLP and an extensive codebook to streamline the sparse regression process, significantly cutting computational costs while simplifying training and improving performance. Empirical studies on five spatio-temporal benchmark datasets show SVQ achieves state-of-the-art results, including a 7.9\% improvement on the WeatherBench-S temperature dataset and an average MAE reduction of 9.4\% in video prediction benchmarks (Human3.6M, KTH, and KittiCaltech), along with a 17.3\% enhancement in image quality (LPIPS). Code is publicly available at https://anonymous.4open.science/r/SVQ-Forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper identifies the limited performance of traditional vector quantization (VQ) in spatiotemporal forecasting due to non-differentiability and limited representation power. It proposes Differentiable Sparse Soft - Vector Quantization (SVQ), which approximates sparse regression with a two-layer MLP for differentiability and uses Soft-VQ with sparse regression to capture patterns and filter noise. Empirical results on multiple datasets show SVQ achieves state-of-the-art performance, is versatile as a plug-in, and effectively balances detail and noise reduction. Ablation studies and additional analyses confirm its key components’ importance and its robustness.

### Strengths
The paper shows originality through the development of SVQ, a novel combination of sparse regression and soft vector quantization for spatio-temporal forecasting with theoretical analysis. Empirical validation is extensive, with experiments on multiple real - world datasets and comparisons to existing methods, achieving state-of-the-art results and validating the method's effectiveness and quality. It has potential applications in various domains and can inspire future research, opening new avenues for exploration and providing insights for model development.

### Weaknesses
1. The novelty of the approach is limited, and the performance improvement appears marginal. Furthermore, there is no discussion on the additional computational overhead that these slight performance enhancements (such as those observed in wind speed and humidity in Table 1, and in the KTH dataset in Table 2, as well as in Table 18) will incur. A more detailed analysis of the computational overhead introduced by SVQ, compared to baseline methods, is needed, especially for cases where the performance gains are smaller.

2. The motivation is unclear. It is not surprising to use huge codebook and sparse representation to improve the effect, because huge codebook itself brings a lot of extra parameter redundancy. So why use vector quantization? Because in other fields (e.g., video compression, video generation), VQ is to compress redundant information, not to add redundant information. You could further explain their rationale for using vector quantization in this context, given its typical use for compression in other fields.

3. The theoretical analysis provided seems unrelated to the content of the article. Furthermore, the article fails to discuss the relationship between the information or features extracted after compression using SVQ and the original spatiotemporal data. Consequently, there is a notable lack of corresponding theoretical discussion. A more in-depth exploration of how the features learned through SVQ are related to the original spatiotemporal data would greatly aid in fully elucidating the mechanism underlying SVQ.

4. The ablation study conducted is insufficient. There is no doubt that setting the code size to 10000 will yield better performance compared to 1000. A more detailed discussion of the trade-offs involved (such as efficiency, convergence, etc.) with larger code sizes would be helpful.

5. The introduction of redundant over-complete codebooks and additional computational overhead has resulted in a lack of discussion on computational efficiency, speed, and complexity, among other factors. Empirical measurements of training and inference times, memory usage, and computational complexity, as a function of codebook size, would provide a more comprehensive illustration of the advantages of SVQ.

### Questions
1. What is the motivation of using vector quantization into spatiotemporal prediction?
2. What is the significance of theoretical analysis in Chapter 4? Is this theoretical analysis related to video prediction?
3. What are the ''improvement'' in Table 1.2.3. refer to, SimVP?
4. Can the method proposed in the paper be compared with diffusion based models? For example, ExtDM: Distribution Extrapolarization Diffusion Model for Video Prediction, CVPR2024. What are the differences between these two methods, e.g., their application scenarios or efficiency?
5. Why are there different types of comparison results between WeatherBench-S and WeatherBench-M in Tab. 1 (Total Cloud Cover in WeatherBench-S and Wind UV in WeatherBench-M)? Why not compare the same subjects? What are the differences in SVQ performance across different physical quantities and data scales?

### Soundness
2

### Presentation
1

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
Vector quantization (VQ) is insufficient in improving the accuracy of spatiotemporal prediction. This paper introduces differentiable sparse soft vector quantization (SVQ) that can strike a balance between detail preservation and noise reduction, providing a solid foundation for full differentiability and sparse regression. Empirical studies on five spatiotemporal benchmark datasets show that SVQ achieves the best results, including a 7.9% improvement on the WeatherBench-S temperature dataset, a 9.4% average MAE reduction in video prediction benchmarks (Human3.6M, KTH, and KittiCaltech), and a 17.3% improvement in image quality (LPIPS).

### Strengths
1. The manuscript proposes a differentiable sparse soft vector quantization (SVQ) method, which is the first vector quantization method applied to spatiotemporal prediction and shows significant improvement.
2. The SVQ method proposed in the manuscript has achieved leading performance in multiple real-world spatiotemporal prediction tasks, significantly reducing errors on multiple benchmark datasets, such as reducing errors by 7.9% on the WeatherBench dataset.
3. The SVQ proposed in the manuscript can be seamlessly integrated into different types of spatiotemporal prediction models as a plug-in, and has improved performance in various architectures, demonstrating the versatility of the method.

### Weaknesses
1.The SVQ method proposed in the manuscript still requires a lot of computing resources, especially in the case of high-dimensional data and large-scale codebooks.
2.The comparison methods cited by the author in Tables 1 and 2 are only up to date in 2022, and lack comparisons of the latest methods in the past two years.

### Questions
1.Will the SVQ module added as a plug-in to the model have similar performance improvements for other tasks (such as image generation or natural language processing)? What are the applicable application scenarios?

### Soundness
3

### Presentation
3

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
The paper introduces a novel Differentiable Sparse Soft-Vector Quantization (SVQ) method, which integrates sparse regression with differentiability to tackle optimization challenges in vector quantization. This approach aims to enhance representation capacity in spatio-temporal forecasting tasks, marking a significant advancement in the field. While the SVQ method presents an innovative approach to vector quantization, the paper would benefit from clearer connections between theory and practice, updated baselines, deeper integration insights, and improved mathematical clarity to strengthen its contributions to the field.
Soundness:2

### Strengths
The proposed Differentiable Sparse Soft-Vector Quantization (SVQ) method represents a novel advancement in vector quantization techniques.

### Weaknesses
The method does not adequately demonstrate how the theoretical advantages of sparse regression are translated into tangible improvements in quantization performance. While the authors discuss optimization strategies, they fail to provide a clear connection between these theoretical claims and the practical outcomes. A more comprehensive explanation of how these optimization techniques directly enhance quantization would bolster the credibility of their approach.
	In the experimental section, I noticed that the baseline models employed are relatively outdated. Given the recent advancements in spatio-temporal forecasting, particularly the emergence of various diffusion-based methods that have demonstrated significant improvements in predictive performance, it would be beneficial for the authors to consider incorporating these state-of-the-art models as baselines. This would provide a more comprehensive evaluation of the proposed method's effectiveness and advantages.
	The explanation of the quantization module's implementation lacks depth regarding its integration with the overall spatio-temporal forecasting model. While the authors outline the architecture and components involved, they do not provide sufficient details on how the quantization process interacts with other model elements or influences the final forecasting results. A more thorough exploration of these interactions would enhance the clarity and applicability of their proposed method.
	In Section 4, the mathematical proof lacks clarity in the notation used, which may hinder readers' understanding. For example, what’s the meaning of g' after Eq. (8)? Additionally, the proof does not establish a strong connection to the problem being addressed. I recommend revising this section to improve the clarity of the symbols and to explicitly link the proof to the main objectives of the paper.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the limitations of traditional Vector Quantization (VQ) and demonstrates impressive performance in spatio-temporal forecasting. SVQ uses a two-layer MLP to approximate sparse regression, reducing computational complexity while maintaining the flexibility to map each input vector to multiple codebook vectors. This soft quantization captures the complex dynamics of spatio-temporal data, preserving essential information while minimizing noise. The experiments confirm that SVQ is an efficient and expressive quantization mechanism applicable to various forecasting tasks. The visualizations provide valuable insights into the behavior and advantages of SVQ.

### Strengths
1. Innovative Approach: The paper effectively combines sparse regression with differentiable quantization, addressing the non-differentiability and limited representational power of traditional VQ. Using MLP to approximate sparse regression allows the model to capture complex patterns efficiently.  
2. Simplicity and Effectiveness: The proposed method is intuitive and easy to implement, with straightforward derivations and motivations. It demonstrates significant improvements across multiple tasks and models.  
3. Comprehensive Experiments: The paper provides detailed evaluations of the proposed quantization mechanism, including ablation studies and supplementary materials that address key questions. The well-designed visualizations offer excellent insights into the behavior and strengths of SVQ.

### Weaknesses
1. Visual Layout: Perhaps due to space constraints, the layout of the figures and tables could be more aesthetically pleasing.

### Questions
1. The paper emphasizes the advantages of the proposed method in spatio-temporal forecasting, but VQ is also widely used in generative tasks (e.g., VQ-VAE). Could this method be applied to such tasks?

### Soundness
3

### Presentation
4

### Contribution
4
