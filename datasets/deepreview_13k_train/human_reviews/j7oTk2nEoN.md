# Gray-Box Fine-Tuning for Single Backbone Domain Experts

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
The emergence of foundational models has greatly improved performance across various downstream tasks, with fine-tuning often yielding even better results. However, existing fine-tuning approaches typically require access to model weights and layers, leading to challenges such as managing multiple model copies or inference pipelines, inefficiencies in edge device optimization, and concerns over proprietary rights, privacy, and exposure to unsafe model variants. In this paper, we address these challenges by exploring "Gray-box" fine-tuning approaches, where the model's architecture and weights remain hidden, allowing only gradient propagation. We introduce a novel yet simple and effective framework that adapts to new tasks using two lightweight learnable modules at the model's input and output. Additionally, we present a less restrictive variant that offers more entry points into the model, balancing performance with model exposure. We evaluate our approaches across several backbones on benchmarks for text-image alignment, text-video alignment, and sketch-image alignment. Our results demonstrate that, despite having limited access to the model, our Gray-box approaches achieve competitive performance with full-access fine-tuning methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper discusses the challenges of traditional fine-tuning methods for foundational models, which require access to model weights and layers, leading to issues like managing multiple model copies, inefficiencies in edge device optimization, and concerns over proprietary rights and privacy. To address these challenges, authors propose "Gray-box" fine-tuning approaches that keep the model's architecture and weights hidden, allowing only gradient propagation. They introduce a framework with two lightweight learnable modules at the model's input and output to adapt to new tasks: DarkGray-Box Input/Output Adapters (DGA) and LighGray-box (LGA). The approaches are evaluated on benchmarks for text-image, text-video, and sketch-image alignment, showing competitive performance compared to full-access fine-tuning methods despite limited model access.

### Strengths
+ The paper focuses on an interesting and practial practical problem: conducting effective and efficient model finetuning for foundational models with limitted access to the model weights and layers.

+ The proposed "Gray-box" fine-tuning approaches (LightGray-box and DarkGray-box), that keep the model's architecture and weights hidden, allowing only gradient propagation. This helps address challenges for this problem. 

+ Experiments are conducted on several text-image, text-video, and sketch-image alignment benchmarks, which demonstrates the effectiveness of the proposed methods. They achieve competitive results compared with White-box baselines and meanwhile keeping the foundation model sealed.

### Weaknesses
 - The paper claims that a new paradigm is proposed for effectively re-use pre-trained foundation models. But it is not clear whether the proposed DGA and LGA can be applied commonly used LLM, VLLM, Text-to-Image/video generation foundation models for various downstream tasks. 

- Experiments can not well support the above claim as well. The studies are mainly on representation learning tasks like text-image, text-video, and sketch-image alignment, image classification using baseline models e.g. CLIP,  BLIP, DINO. There lacks studies on other kinds of foundation models on various tasks such as VQA, image/video captioning, Text-to-image/video generation etc. 

- Technical contributions are limitted and the method design is pretty straightforward.

### Questions
Please refer to details of above "Weaknesses" sections. Basically it is not clear to me if the proposed method can be generalized to various foundation models and achieve good performances on different kinds of tasks.

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
The paper raises the concern for exposure of pretrained model weights and layers. The proposal is to (1) adapt two lightweight adaptors at the model’s input and output, and (2) introduce more entry points for trade-off between model exposure and performance. The model is shown to have generality across various downstream tasks and domains and results close to white-box alternatives.

### Strengths
The author(s) tries to formulate the challenge of model exposure and consider the high-level issues by considering practical use cases. 
The experiments are well designed to verify generality and the ablation study is detailed and insightful.

### Weaknesses
As LoRA is a very strong baseline, the paper needs strong support to indicate that the new method with less access to the original model is a better approach. The claim that full model exposure is risky sounds reasonable but lacks strong evidence - there is no experiment showing that the new method avoids IP violation or saves computation cost.

### Questions
Could it be possible to have some evidence supporting the motivation of the paper to reduce the model exposure?

### Soundness
3

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
2

### Summary
This paper provides a way of fine-tuning models without requiring the exposure of the entire model weights. The authors propose a set of fine-tuning options that trade-off model weight exposure and model performance. They show improvement over black-box optimization methods and close the gap to white-box optimization methods, while also allowing for a tradeoff of model visibility between white and black-box optimization methods.

### Strengths
This work has run a large number of experiments thoroughly detailing the strengths and weaknesses of their work. Specifically, while they show they are on average slightly worse than white-box methods, they show improvement over zero-shot and linear probe methods. The notable exception is the  Stanford-Cars dataset using the BLIP backbone, where they outperform all baselines, which the authors attribute to the lower number of training samples.

### Weaknesses
This paper mentions other grey-box optimization techniques in the related works but doesn't compare against them.

This paper provides a compromise in terms of accuracy and model visibility in terms of what is revealed to the person fine-tuning the model. As a result, they don't show consistent outperformance over the baselines. For me to improve my review I would like to see comparisons against other gray-box training methods. MaPLe was mentioned in the related works as another work that qualifies as a lightgray box training method and it appears their code is publicly available. If the proposed method is shown to outperform other methods with similar level of model visibility consistently I will improve my rating.

Last Layers FT is listed in the white-box category for evaluations. Since this baseline wouldnt require the entire model weights, only the activation for a set of final layers, wouldnt this be considered a gray-box method? Last layer fine tuning seems to consistently outperform the proposed method.

### Questions
Last Layers FT is listed in the white-box category for evaluations. Since this baseline wouldnt require the entire model weights, only the activation for a set of final layers, wouldnt this be considered a gray-box method? Last layer fine tuning seems to consistently outperform the proposed method.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The manuscript presents a Gray-box fine-tuning framework designed to balance model adaptation flexibility with privacy and IP protection. In contrast to full fine-tuning, gray-box fine-tuning restricts access to model weights and layers, providing only limited points for gradient propagation, which allows efficient adaptation while keeping core architecture concealed. Two alternatives are presented: DarkGray-box, which confines modifications to input and output layers, and LightGray-box, which exposes additional entry points in intermediate layers for enhanced adaptability. The proposed method is evaluated on several backbones and benchmarks.

### Strengths
1. The Gray-box framework introduces a significant advance in balancing model adaptability with privacy, a critical requirement in sensitive applications (e.g., medical data), by enabling model use without exposing proprietary information.
2. Through extensive evaluation on text-image, text-video, and sketch-image benchmarks, the framework shows adaptability across multiple modalities and backbone architectures, illustrating its utility across various domains

### Weaknesses
1.	While the paper includes comparisons with prominent methods, additional baselines, such as more recent adapter-based fine-tuning techniques or advanced parameter-efficient methods in federated learning, could provide a more comprehensive view of the framework’s strengths and weaknesses. For example, Liu Shihong et al., in "Language Models as Black-Box Optimizers for Vision-Language Models" (CVPR 2024), Wang Zhengbo et al. Connecting the Dots: Collaborative Fine-tuning for Black-Box Vision-Language Models, (ICML2024), and Lu Wang et al., in "ZooPFL: Exploring Black-box Foundation Models for Personalized Federated Learning" (Arxiv 2310.05143).
2.	In Tab. 8, there is a lack of a comparison of the proposed method with Co-CoOp and MaPLe, which belongs to the gray-box framework.

### Questions
Please see the weakness part, the authors should address the following: 1) a discussion clarifying the distinctions between the proposed Gray-box setting and federated learning, as the two share some similarities but also have key differences; and 2) a more extensive baseline comparison. While results for LoRA and Linear Probing are provided on several benchmarks, additional baselines would offer a more comprehensive evaluation.

### Soundness
3

### Presentation
3

### Contribution
2
