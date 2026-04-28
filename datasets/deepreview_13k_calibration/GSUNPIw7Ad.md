# Bridging Compressed Image Latents and Multimodal Large Language Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
This paper presents the first-ever study of adapting compressed image latents to suit the needs of downstream vision tasks that adopt Multimodal Large Language Models (MLLMs). MLLMs have extended the success of large language models to modalities (e.g. images) beyond text, but their billion scale hinders deployment on resource-constrained end devices. While cloud-hosted MLLMs could be available, transmitting raw, uncompressed images captured by end devices to the cloud requires an efficient image compression system. To address this, we focus on emerging neural image compression and propose a novel framework with a lightweight transform-neck and a surrogate loss to adapt compressed image latents for MLLM-based vision tasks. Given the huge scale of MLLMs, our framework has the striking feature of excluding the entire downstream MLLMs from training our system. This stands out from most existing coding for machine approaches that involve downstream networks in training and thus could be impractical when the networks are MLLMs. The proposed framework is general and applicable to various MLLMs and multiple application scenarios, where the neural image codec can be (1) pre-trained for human perception without updating, (2) fully updated for joint human and machine perception, or (3) fully updated for only machine perception. 
Extensive experiments on different neural image codecs and various MLLMs show that our method achieves great rate-accuracy performance with much less complexity, demonstrating its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper suggests using compressed image latents for more efficient multimodal large language models (MLLMs). Specifically, a lightweight transform-neck and a surrogate loss are proposed to align compressed image latents with backbone LLMs for multimodal tasks. Experiments are conducted on some mainstream multimodal tasks, such as image captioning and VQA, and the proposed method demonstrates that it outperforms the reconstruction baseline.

### Strengths
* This paper is easy to follow
* The topic of reducing the cost of visual input in MLLMs is of great practical value
* The idea of adapting compressed image latent to MLLMs makes sense to me

### Weaknesses
This paper can be further strengthened by:

* One question that remains unclear about the motivation is why we need the proposed method of compressing image latent instead of existing token pruning/merging work on MLLMs such as crossget [1]. These methods can also reduce the costs of MLLMs, and I’d suggest the authors discuss the difference between existing acceleration methods for MLLMs and the proposed method, and highlight their unique contributions to efficient MLLMs.

* The proposed method shows inconsistent performance degradation on different benchmarks. For example, it shows close performance to models using uncompressed image latent on image captioning while suffering from a significant performance degradation on the POPE benchmark. It would be better to have some insight into it.

### Questions
Please refer to Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates adapting compressed image latents to meet the requirements of downstream vision tasks in Multimodal Large Language Models (MLLMs). The authors introduce a framework that employs a "transform-neck" structure and a surrogate loss function to adjust compressed image representations, without involving MLLMs in the training process. This design choice differs from conventional approaches that incorporate downstream models during training, making it potentially more feasible for resource-limited devices. The results show that this method achieves a balance between compression rate and accuracy across various neural image codecs and MLLMs, demonstrating its potential for efficient performance.

### Strengths
1. This paper focuses on an interesting scenario: how to achieve image compression in the context of MLLMs.
2. The writing in this paper is well-organized, making it easy to follow and understand the authors' intentions.

### Weaknesses
1.  The proposed method appears to be a general image compression approach, lacking unique design elements specifically tailored for MLLMs. While the authors emphasize that this approach can achieve image compression in a resource-efficient manner to support MLLMs, they do not provide specific comparisons regarding the reduction in training costs—such as training time or computational resources—compared to methods that incorporate MLLMs directly into the training process. The method's reliance on a surrogate loss, while avoiding direct MLLM backpropagation, does not inherently demonstrate a novel approach to MLLM-specific compression, as the core compression mechanism remains largely agnostic to the nuances of multimodal understanding. The absence of a clear benchmark against methods that explicitly optimize for MLLM performance makes it difficult to assess the true advantage of this approach.
2. The proposed  SURROGATE LOSS is not novel, easily combination of the Mean Squared Error loss and the cross-entropy loss. The combination of MSE and cross-entropy is a common practice in various domains, and the paper does not provide a strong justification for why this specific combination is particularly effective or novel in the context of adapting compressed image latents for MLLMs. The lack of ablation studies on different loss combinations further weakens the claim of novelty.
3. The proposed method has limited applicability, as it requires alignment with specific vision encoders. The authors only align with CLIP, whereas many advanced MLLMs now use other, more powerful vision encoders, such as Intern-ViT or SGLIP. This method may need further adaptation to support these alternative encoders effectively. The dependence on a specific vision encoder limits the method's generalizability and its potential impact on the broader MLLM landscape. The lack of experiments with diverse encoders raises concerns about its practical utility.

### Questions
1. Why are different MLLMs chosen for each task instead of evaluating multiple MLLMs on each task? A consistent comparison across tasks using various MLLMs would provide a clearer understanding of the method’s generalization capability.
2. During Phase 1: Transform-neck Training, the motivation for using different loss functions at various stages across all epochs is not clearly explained, and there is a lack of corresponding ablation studies to support this design choice.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel framework designed to bridge compressed image latents with Multimodal Large Language Models (MLLMs) for downstream vision tasks. It addresses the challenge of deploying MLLMs on resource-constrained devices by proposing a lightweight transform-neck and a surrogate loss to adapt compressed images for MLLM-based vision tasks without the need for decoding the images. This approach reduces computational complexity and is generic, applicable to various neural image codecs and MLLMs sharing the same visual encoder.

### Strengths
1. The paper introduces a lightweight transform-neck and a surrogate loss function, which together reduce computational complexity and avoid the need to back-propagate through the massive MLLMs, making the training process more efficient.
2. The proposed framework is generic and can accommodate various neural image codecs and MLLMs that share the same visual encoder, enhancing its versatility and applicability across different models and tasks.
3. The paper demonstrates the effectiveness of the proposed method through extensive experiments on different neural image codecs and MLLM-based vision tasks, showing improved rate-accuracy performance and less complexity compared to existing methods.

### Weaknesses
1. The paper's approach relies on the assumption that the downstream MLLMs will use the same pre-trained CLIP visual encoder, which may limit the applicability of the proposed method to MLLMs that employ custom or different visual encoders.
2. The paper does not provide a comprehensive comparison with existing image compression methods beyond the context of MLLMs, which could be important for understanding the method's performance in a broader range of applications

### Questions
1. Will you plan to release the code ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores methods to compress and decode images such that the decoded images can be successfully used with Large MLLMs, addressing the substantial overhead required for transmitting images to cloud-hosted MLLMs. Existing image encoding works for machine vision face a common problem: MLLM models are too large to train the neural image codec. To address the computational overhead of image compression and encoding in the context of MLLMs, this paper proposes a lightweight transform-neck and a novel surrogate loss. The lightweight transform-neck aims to align the features of the compressed images with the outputs of the visual encoder, avoiding the need for fully image decoding. The proposed surrogate loss allows the neural image codec to be trained using only the vision encoder, avoiding the need for backpropagating through the entire MLLM. The proposed method can be applied to different MLLMs and various neural image codecs in various application scenarios.

### Strengths
1. This paper claims to be the first work specifically targeting neural image coding for MLLMs.
2. It introduces a lightweight transform-neck that aligns the encoded image latents with the MLLM visual encoder outputs, thereby avoiding the decode operation in neural image coding and reducing computational complexity.
3. The proposed surrogate loss allows updating the neural image coding model via the Visual Encoder without backpropagating through the entire MLLM, hence reducing the computation required.
4. The proposed method is applicable to different downstream MLLMs, applications, and neural image codecs.

### Weaknesses
1. The motivation of this paper—studying image compression under MLLM to avoid transmission overhead—seems to lack practical significance. The primary goal of image compression is to reduce image resolution, which might be meaningless for MLLMs:
* First, most MLLMs use CLIP Image Encoder, which limits image resolution to 224x224. This resolution does not incur significant transmission overhead in current network communications and is negligible compared to the inference time of MLLMs.
* Second, while some works explore using high-resolution images as input, they usually crop high-resolution images into several low-resolution sub-images, often achieving better performance compared to compressed images. Therefore, researching how to compress images as MLLM input seems unnecessary.
* Lastly, the authors do not explain the advantages of using compressed images as MLLM input over exploring more compact Image Encoders.

2. The proposed method requires training different transform-necks and codecs for different downstream tasks, further leading me to question the necessity and rationale of this work.

### Questions
Please refer to the Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
