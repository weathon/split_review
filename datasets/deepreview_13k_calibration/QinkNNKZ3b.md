# Fréchet Wavelet Distance: A Domain-Agnostic Metric for Image Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Modern metrics for generative learning like \ac{fid} demonstrate impressive performance. However, they suffer from various shortcomings, like a bias towards specific generators and datasets.
  To address this problem, we propose the \ac{fwd} as a domain-agnostic metric based on \acf{wpt}.
  \ac{fwd} provides a sight across a broad spectrum of frequencies in images with a high resolution, along with preserving both spatial and textural aspects.
  Specifically, we use \ac{wpt} to project generated and dataset images to packet coefficient space.
  Further, we compute Fr\'echet distance with the resultant coefficients to evaluate the quality of a generator.
  This metric is general-purpose and dataset-domain agnostic, as it does not rely on any pre-trained network while being more interpretable because of frequency band transparency.
  We conclude with an extensive evaluation of a wide variety of generators across various datasets that the proposed \ac{fwd} is able to generalize and improve robustness to domain shift and various corruptions compared to other metrics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper, "Fréchet Wavelet Distance: A Domain-Agnostic Metric for Image Generation", introduces the Fréchet Wavelet Distance (FWD) as a novel metric for evaluating generative models in a domain-agnostic way. FWD leverages the Wavelet Packet Transform (Wp) to project images into a frequency and spatially enriched domain, capturing both the frequency and spatial characteristics of images. This approach enables FWD to evaluate the similarity between generated and real images based on the Fréchet Distance (FD) of their wavelet packet coefficients, providing robustness against domain bias and dataset dependency issues seen in other metrics, such as FID and FD-DINOv2. The authors perform extensive evaluations across various datasets and demonstrate that FWD achieves consistent, domain-agnostic results and outperforms state-of-the-art metrics in terms of robustness and computational efficiency.

### Strengths
1. Domain Independence and Robustness: FWD’s reliance on the wavelet transform offers a substantial improvement in domain-agnostic evaluation, avoiding the biases associated with pre-trained models like InceptionV3. This makes it a more universally applicable metric across datasets and model types.
2. Efficient and Scalable: FWD is computationally efficient, with much lower FLOPs compared to FD-DINOv2, making it suitable for large-scale evaluation. The method’s wavelet packet decomposition also enables interpretable results by isolating specific frequency bands for detailed analysis.

### Weaknesses
1. Limited Comparison with Alternative Frequency-Based Metrics: Although the paper presents strong results, it lacks comparisons with alternative frequency-based metrics, such as those leveraging Fourier transforms or spectral analysis. This comparison could clarify the specific advantages of wavelet-based decomposition over other spectral methods in generative evaluation. It would be beneficial to see a more thorough investigation into why the wavelet transform is superior to other spectral methods, especially given that Fourier transforms are also capable of capturing frequency information and have established use in image analysis. A direct comparison with metrics based on Fourier analysis could reveal if the wavelet transform's spatial localization provides a significant advantage, or if the frequency-based information alone is sufficient for the task.

2. Potential Alignment with Human Evaluation: FID score has been long complaint against that it can not accurately evaluate the quality of generative models, specifically alignment with human preferences. This paper presents some improvement over FID scores on several GAN and Diffusion models, but a wider range of ablations and even human evaluations could better support the validity of this approach. Specifically, while the paper shows FWD correlates better with human perception than FID in some cases, a more comprehensive study is needed. This should include a broader range of generative models, especially the latest diffusion models, and a more rigorous evaluation of how well FWD's rankings align with human preference scores. A detailed analysis of edge cases where FWD might fail to capture human perception would also be valuable.

### Questions
Please refer to the weakness part

### Soundness
3

### Presentation
3

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
Modern generative models exhibit frequency biases, while commonly used metrics such as FID , KID and FD-DINOv2 are affected by domain bias.  
This paper proposes the Fréchet Wavelet Distance ( FWD ) as a dataset- and domain-agnostic metric for evaluation of generative approaches for image synthesis.    
It is  shown that the proposed method is robust to corruption, perturbation, and distractors.  
At the same time, its formulation is computationally efficient.

### Strengths
The proposed metric Fréchet Wavelet Distance ( FWD ) is simple and has no trained parameters, thus it has high efficiency and is robust to domain, corruption, perturbation, and distractors.    

The calculation of FWD is much faster than FID and FD-DINOv2.  

On several dataset, FWD produces more reasonable results than FID and FD-DINOv2.  

Because of the packet and frequency design, FWD has some interpretability.

### Weaknesses
To make the new FWD metric more convincing, a human subject experiment is necessay, as is conducted in the FD-DINOv2 paper. The human evaluation results in FD-DINOv2 paper might be a useful benchmark.

### Questions
Many image quality metirc has been proposed for generative model evaluation, but to my knowledge, FID is still the mostly adopted one. I want to hear the authors opinion on this problem. Will evaluating on SOTA generative models like stable diffusion series help the advocation of a new image quality metric?

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
3

### Summary
This paper claims that FID/FD-DINOv2 suffer from the bias of generator and dataset, and proposes the FWD, a domain-agnostic metric based on the Wavelet Packet Transform. The FWD does not rely on any pre-trained network, and thus is general-purpose and dataset-domain agnostic. The author further claims this new metric is more interpretable due to its ability to compute Fréchet distance per packet.

### Strengths
1. The proposed solution for enhancing FID is attractive, and the FWD is designed to be general-purpose and dataset-domain agnostic, with a solid foundation.
2. The experiments are well-considered.

### Weaknesses
1. The paper appears to be missing comparisons with several competitors. While the FWD is compared with FID/FD-DINOv2, this seems insufficient. For instance, metrics such as IS (Inception Score), KID (Kernel Inception Distance), FID_\infty, IS_\infty, and Clean FID should also be considered. The authors should either include comparisons with these metrics or provide an explanation for their omission. Notably, FID_\infty and IS_\infty are designed to mitigate biases introduced by models, making their inclusion particularly relevant.

2. There is a lack of human evaluation. For a metric evaluating generative models, it would be beneficial to demonstrate alignment with human evaluation results.

3. The underlying mechanism is not entirely clear. Despite the authors’ claim that FWD offers improved transparency, it remains unclear why a hand-designed metric could yield better evaluation results than those based on deep learning techniques. Or you can also explain it.

4. The dataset selection is limited. It appears that all experiments are conducted on just four datasets (face, agricultural, and remote sensing datasets). Including a broader range of datasets, particularly natural images from sources like ImageNet, OpenImage, COCO, or Laion5B, would enhance the robustness of the findings. Or you can also explain it.

### Questions
See weaknesses. As I am not an expert in this field, I would like to adjust my rating if all the reviewers’ concerns are addressed.

### Soundness
2

### Presentation
2

### Contribution
3
