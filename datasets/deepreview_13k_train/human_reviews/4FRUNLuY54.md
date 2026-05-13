# Dragonfly: Multi-Resolution Zoom-In Encoding Enhances Vision-Language Models

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Recent advances in vision-language models (VLMs) have demonstrated the advantages of processing images at higher resolutions and utilizing multi-crop features to preserve native resolution details. However, despite these improvements, existing vision transformers (ViTs) still struggle to capture fine-grained details from less prominent objects, charts, and embedded text, limiting their effectiveness in certain tasks. In this paper, we extend recent high-resolution and multi-crop techniques by not only preserving the native resolution, but zooming in beyond it and extracting features from a large number of image sub-crops. This enhancement allows our model to better capture fine-grained details, overcoming the limitations of current ViTs. To manage the increased token count and computational complexity, we demonstrate that a simple mean-pooling aggregation over tokens is effective. Our model, {\model}, achieves competitive performance on general-domain tasks such as ScienceQA and AI2D, and excels in tasks requiring fine-grained image understanding, including TextVQA and ChartQA. Among models in the 7-8B parameter range, {\model} consistently ranks at the top across ten general-domain benchmarks, achieving the highest or second-highest scores in most cases, outperforming models that are significantly larger or trained on larger datasets. Our biomedical model, {\modelbiomed}, sets new benchmarks on several medical tasks, achieving 91.6\% accuracy on SLAKE (compared to 84.8\% for Med-Gemini), a 67.1\% token F1 score on Path-VQA (compared to 62.7\% for Med-PaLM M), and state-of-the-art results across the majority of image captioning tasks. Overall, our work highlights the persistent challenge of engineering visual representations with fixed-resolution ViTs, and proposes a simple yet effective solution to address this issue and boost performance in both general and specialized domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces DragonFly to enhance vision-language models. The main idea is to combine the multi-cropping with mean pooling, so that the VLM can use high-resolution image encoders and work on images' native resolution, while ensuring the efficiency of the model. The proposed enhanced VLM performs well in tasks needing finer details, such as biomedical tasks.

### Strengths
1. Dragonfly uses multi-crop techniques to process images at high resolutions, thus enhancing the model’s capability to capture fine details. Meanwhile, it uses a simple mean-pooling strategy to reduce visual tokens effectively, which retains the efficiency of the model.
2. The proposed method achieves competitive performance across multiple benchmarks and shows strong generalizability across both general and specialized biomedical tasks.

### Weaknesses
The paper introduces a method, Dragonfly, that combines multi-crop and mean-pooling techniques to enhance Vision-Language Models (VLMs). While the approach demonstrates competitive performance, the core strategy lacks a strong theoretical foundation. The motivation for selecting mean-pooling over alternative compression techniques is not adequately justified. The paper primarily presents empirical results, stating that mean-pooling is effective without a deep exploration into why it outperforms other strategies. For instance, what are the specific characteristics of the image data or the model architecture that make mean-pooling particularly suitable in this context?  Furthermore, the choice of the pooling window size seems arbitrary. The paper does not provide a clear rationale for the selected window size, nor does it investigate the potential impact of different window sizes on the model's ability to capture fine details. A more rigorous analysis of the trade-offs between compression, computational efficiency, and detail preservation is necessary. Does this direct pooling approach potentially harm the extraction of fine details, especially in regions with high information density? A thorough investigation into the effects of pooling on different image regions and feature types would strengthen the paper's claims.

### Questions
Please refer to the weaknesses part. Additionally, is there a comparison of the inference time or flops of different methods?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces multi-crop techniques beyond the native resolution for high-resolution images. To handle the huge number of numbers, the authors employ the average pooling startegy on each crop. Except for general domain of benchmarks on fine-grained image understanding, this paper also introduce the contributioni on biomedical tasks. They also curate a SFT dataset including 2.4M general images and 1.4M biomedical images for training.

### Strengths
1. The ablation studies proves their proposed strategy.
2. Biomedical domain is considered by this paper.
3. The motivation is nature and easy to follow.
4. A SFT dataset with different domains and huge number of images is built.

### Weaknesses
1. The novelty is limited. The proposed strategy is only an extension of any-resolution technical. Compared to any-resolution which uses two levels of rosulotions, they only resize the image, crop more patches and use three levels of resolutions of image.
2. The visualizations only shows the response of the proposed Dragonfly, other MLLM's responses are encouraged to be listed for better comparision.
3. To balance the computational costs and performance, they use mean pooling within each crop. The paper lacks the dicussion about how to choose a proper compressing ratio for trade-off.

### Questions
Please see weaknesses.

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
4

### Summary
The manuscript presents Dragonfly, a novel Vision-Language Model (VLM) that employs a multi-resolution zoom-in encoding strategy to enhance fine-grained visual understanding. Unlike conventional Vision Transformers (ViTs) that downsample images to fixed, low resolutions—thereby losing critical details—Dragonfly processes images at higher resolutions and employs a multi-crop technique that exceeds the native resolution. This approach allows the model to capture intricate details from non-dominant objects, charts, and embedded text, which are often challenging for existing ViTs. To address the computational complexity arising from the increased token count, Dragonfly utilizes a mean-pooling aggregation strategy. The model demonstrates competitive performance across ten general-domain benchmarks and sets new benchmarks in several biomedical tasks, outperforming larger models trained on significantly more extensive datasets.

### Strengths
1. Dragonfly introduces an innovative multi-resolution zoom-in encoding strategy that surpasses native image resolutions, enabling the capture of intricate details from non-dominant objects, charts, and embedded text.
2. It implements a simple yet effective mean-pooling aggregation method and achieves good performance across a diverse set of benchmarks.

### Weaknesses
1. Novelty. The proposed method builds upon existing multi-resolution and multi-crop techniques without offering substantial novel contributions. The idea of processing images at higher resolutions and using multi-crop strategies has been explored in prior works, and Dragonfly does not sufficiently differentiate itself beyond these established methods. The core mechanism of extracting multiple crops and feeding them into the language model is not new, and the paper needs to more clearly articulate what specific innovation it brings to this well-trodden area. The use of mean-pooling for aggregation, while simple, also lacks a strong justification for why this particular method was chosen over other potential aggregation techniques.
2. Model Comparison: Dragonfly is developed using the more advanced Llama3 model, whereas comparable methods utilize less capable language models, such as Llama2 and Qwen2. This discrepancy raises concerns about the fairness of comparisons. How does Dragonfly's performance measure up when evaluated against these models? The paper needs to provide a more controlled comparison, ideally with all models evaluated using the same language model backbone to isolate the impact of the visual encoding strategy. The current comparisons are confounded by differences in language model capabilities, making it difficult to assess the true contribution of the proposed method.
3. Data Influence: It is unclear whether the observed performance improvements with Dragonfly stem from the curated data or from the model's design. How does Dragonfly perform when tested with a commonly used dataset? The paper needs to demonstrate that the performance gains are not simply due to a specific training dataset, and should include results on standard benchmark datasets to ensure the generalizability of the findings. Without this, it is difficult to ascertain whether the improvements are a result of the model architecture or the training data.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2
