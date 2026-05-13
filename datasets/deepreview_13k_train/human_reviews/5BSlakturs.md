# Enhancing Compositional Text-to-Image Generation with Reliable Random Seeds

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Text-to-image diffusion models have demonstrated remarkable capability in generating realistic images from arbitrary text prompts. However, they often produce inconsistent results for compositional prompts such as ``two dogs" or ``a penguin on the right of a bowl". Understanding these inconsistencies is crucial for reliable image generation. In this paper, we highlight the significant role of initial noise in these inconsistencies, where certain noise patterns are more reliable for compositional prompts than others. Our analyses reveal that different initial random seeds tend to guide the model to place objects in distinct image areas, potentially adhering to specific patterns of camera angles and image composition associated with the seed. To improve the model's compositional ability, we propose a method for mining these reliable cases, resulting in a curated training set of generated images without requiring any manual annotation. 
By fine-tuning text-to-image models on these generated images, we significantly enhance their compositional capabilities. For numerical composition, we observe relative increases of 29.3\% and 19.5\% for Stable Diffusion and PixArt-$\alpha$, respectively. Spatial composition sees even larger gains, with 60.7\% for Stable Diffusion and 21.1\% for PixArt-$\alpha$.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the author explores the random noise for the diffusion-based generation, especially for the text-to-image generation.

### Strengths
The idea is easy to follow. 
The problem is well-designed. 
The finding is interesting to many diffusion users.

### Weaknesses
1. Section 3.2 are not well-proved for the correlation. I am not convinced about the heatmap results.
- How do you decide the correct / incorrect in Figure 4?  Do this process bring the bias or prefrency over the distribution?
- Which layer is used for the heatmap? the output of diffusion model before VAE decoder?
- The four coins can be parallel or any position arrangement. So why the heatmap in Figure 4 is coincidently splited the 4 grids?

2. More compositional generation results and failure cases
How to generate the partially overlapped objects?
The samples showed are almost no overlapped.

3.  The definition of seed.
So you just fix the seed rather than the noise?
Everytime we will resample the noise according to the seed?
So why there will be a preferency over certain seed in Section3.3?

4. Minor problem
What are the "these images" in abstract? You may training images, which is collected by you? Please specify it.

5. Scalability to unseen prompts.
How about 7 or 8 objects?
How about the ``boundary'' or ``corner''?

### Questions
Please see the Weakness for details.

My main concern is as follows. 
(1) Correctness is decided by the large model CogVLM2.  It will also lead to the bias, like preferring non-overlapping layout. 
Finetuning makes the model overfitted. 

(2) Fixed System Seed. You mean the input noise is also fixed? Actually, we fixed the input noise.

(3) Overlapped result is hard to generate.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper tackles two main aspects of diffusion models: Numerical and spatial generations. The aim is to use the diffusion model as is without additional inputs such as layouts. First, reliable seeds are mined which produce correct results for the numerical and spatial generations. Then, these seeds are used to create a generative dataset and the model is fine-tuned on this dataset to improve performance.

### Strengths
1. The main advantage of this work is that no additional modules/trainable parameters need to be added to the diffusion model which incorporate layouts or bounding boxes like other works usually do.
2. Extensive experimentation is conducted to validate the reliable seeds hypothesis.
3. Once reliable seeds are mined, the authors have experimented with a broad spectrum of ways to use that to enhance the model's performance.

### Weaknesses
1. Baselines: Newer methods to accomplish this task have developed such as [1] after LMD, which show an improvement over LMD. This work should be compared with [1] instead of LMD to demonstrate the efficacy of this approach.

I have clubbed the other points in the questions section

---
[1] Feng, Yutong, et al. "Ranni: Taming text-to-image diffusion for accurate instruction following." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

2. Comparison against baselines: As 512x512 implementation of Stable Diffusion is used for LMD and Multi Diffusion, comparing it with 768x768 version becomes unfair. What are the numbers for Table 4 when using the 512x512 Stable diffusion of this method instead of the 768x768?

---

3. Mixture of objects for numerical compositions. All the results seem to display numerical compositions of a single object. How are the results when I compose multiple objects, such as "2 airplanes and 4 birds in the sky", and how do the baselines compare with this method for such cases?

### Questions
1. What are the numbers when compared to that of [1]?

---

2. Comparison against baselines: As 512x512 implementation of Stable Diffusion is used for LMD and Multi Diffusion, comparing it with 768x768 version becomes unfair. What are the numbers for Table 4 when using the 512x512 Stable diffusion of this method instead of the 768x768?

---

3. Mixture of objects for numerical compositions. All the results seem to display numerical compositions of a single object. How are the results when I compose multiple objects, such as "2 airplanes and 4 birds in the sky", and how do the baselines compare with this method for such cases?

---
---
I will reconsider my rating if these concerns are addressed.

Please correct me if you think I have misunderstood any aspect of the paper.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the challenges faced by text-to-image models in handling compositional prompts, such as accurately rendering object quantities and spatial relations. It highlights the impact of initial random seeds on the arrangement and fidelity of generated images, proposing a method to improve model performance by identifying and leveraging “reliable seeds.” The paper’s main contributions include: 1) a generation strategy based on reliable seeds to reduce the need for manual annotations by automatically generating a high-quality dataset; 2) fine-tuning the model on self-generated reliable data to enhance numerical and spatial compositional accuracy; and 3) implementing a seed-based sampling strategy that improves generation accuracy without additional computation or training.

### Strengths
1. Provides a novel, data-efficient method to improve compositional accuracy in text-to-image generation by harnessing seed variability.
2. The automatic generation of a training dataset with reliable seeds reduces the labor-intensive process of manual annotation.
3. Extensive quantitative and qualitative evaluations demonstrate the approach’s effectiveness in improving both numerical and spatial compositional tasks across different models.

### Weaknesses
1. The reliance on selected seeds may limit the diversity of generated outputs, as increasing accuracy through reliable seeds could restrict the model’s range of variations. Specifically, the method does not explore the potential for mode collapse or reduced coverage of the output space when fine-tuning on a dataset generated from a limited set of reliable seeds. This could lead to the model generating similar images repeatedly, failing to capture the full variability implied by the input prompts.
2. There is no method presented for automatically selecting reliable seeds during inference, limiting the approach’s applicability to other models and use cases. The current reliance on an offline seed selection process makes it impractical for real-time applications or scenarios where new prompts are frequently encountered, as the seed selection process would need to be repeated for each new prompt. This significantly restricts the method's usability.
3. Potential decline in overall image generation quality when fine-tuning on self-generated data remains unexplored, especially concerning aesthetics and real-world accuracy. The paper lacks a thorough analysis of how fine-tuning on self-generated data impacts the overall visual quality of the generated images, such as sharpness, color accuracy, and the presence of artifacts. It is unclear if the focus on compositional accuracy comes at the expense of other important image quality metrics.
4. The approach assumes that data generated with reliable seeds is of higher quality for model fine-tuning, but lacks empirical comparisons with real-world datasets or alternative high-quality sources. The paper does not provide a comparative analysis of the performance when fine-tuning on data generated with reliable seeds versus fine-tuning on a comparable real-world dataset. This makes it difficult to assess the true value of the self-generated data and whether it provides any advantage over existing high-quality datasets.
5. Limited generalization testing to other diffusion models beyond Stable Diffusion and PixArt-α; therefore, the approach’s adaptability to diverse architectures is unclear. Although the method is tested on two different models, there is no analysis of how the method would perform on other diffusion architectures, such as those using different attention mechanisms or sampling strategies. This limits the understanding of the method's general applicability and robustness.

### Questions
The citation format is slightly less standardized and the consistency of the references in the citation section should be ensured.

One key limitation is the lack of an automatic, inference-time method to select reliable seeds for generating accurate compositions. Would the authors consider developing a mechanism, such as a predictive model or algorithm, to dynamically choose reliable seeds based on prompt characteristics? This would significantly improve the model’s generalizability and practical use.

Fine-tuning on self-generated data inherently risks reducing image diversity or amplifying generation biases. Could the authors clarify how they ensured that this self-generated dataset maintains high quality compared to real-world or externally validated datasets? Additionally, what safeguards are in place to prevent potential degradation in image quality or unintended biases?

### Soundness
3

### Presentation
3

### Contribution
3
