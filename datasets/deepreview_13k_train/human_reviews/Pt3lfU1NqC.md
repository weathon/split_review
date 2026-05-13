# RODIN: Injecting 2D Foundational Features to 3D Vision Language Understanding

- Decision: Reject
- Scores: 6, 6, 8, 5

## Abstract
We present RODIN (Referential ODIN), a novel model for 3D vision-language understanding that directly operates on posed RGB-D frames. Consuming posed RGB-D from sensors, such as those from an iPhone, simplifies and speeds up inference compared to existing models that train and test using pointclouds sampled from a reconstructed mesh provided by a dataset. We hypothesize that existing approaches consume pointclouds sampled from mesh instead of sensor RGB-D point clouds due to inaccurate camera poses in existing 3D grounding benchmarks, and show that using the "sensor" pointclouds indeed leads to a 5-10\% drop in performance on 3D referential grounding, for these methods. Yet sensor noise is unavoidable in real-world settings. RODIN instead addresses this with a scalable, end-to-end architecture for various 3D vision-language tasks. Specifically, RODIN combines powerful pretrained 2D weights trained on internet-scale data, adapts them to a 2D-3D encoder using the recently proposed ODIN, and combines that backbone with a proposed 3D mask-language decoder based on the Mask2Former used in SAM. RODIN achieves state-of-the-art performance on multiple 3D vision-language benchmarks, including referential grounding (SR3D, NR3D, ScanRefer), language-prompted object detection (ScanNet200 and Matterport3D), and question-answering (ScanQA and SQA3D). It outperforms previous methods for 3D vision-language tasks, despite consuming only sensor inputs. Because of its combination of effectively leveraging 2D pretrained architectures and finetuning end-to-end on sensor data, RODIN provides a scalable solution for embodied 3D perception.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel 3D vision language model RODIN that directly operates on posted RGBD images rather than sensor point clouds and it argues that the sensor point cloud leads to 5~10% drop in 3D grounding tasks. RODIN extends ODIN model's architecture by adding text encoding/decoding capabilities for language understanding tasks. The whole model is end-to-end trainable. It achieves state-of-the-art performance on multiple 3D vision-language benchmarks including 3D grounding, segmentation, and vision question answering.

### Strengths
1. The performance improvement is significant. RODIN outperforms previous state-of-the-art by more than 10% on SR3D, NR3D, and  ScanRefer.
2. The authors show comprehensive ablation studies validating the architectural designs.
3. This work directly work on the sensor data, without requirements for mesh reconstruction.
4. The whole model is end-to-end trainable and can solve multiple 3D vision-language tasks.
5. This architecture can fully leverage the pre-trained 2D vision foundation model features.

### Weaknesses
1. The contribution might be limited as the main model architecture is based on ODIN, with the author incorporating text encoding and decoding to add text capabilities.
2. Since it depends on pre-trained 2D models, this approach might limit the model’s ability of generalization. Have authors fine-tuned these pre-trained 2D models, and would fine-tuning enhance the model’s performance?
3. How is camera pose inputted into the model? It’s unclear how the model handles noise in the camera pose. Why is this design performance better than using sensor point clouds, especially given that both designs need to address sensor noise?

### Questions
1. Please provide more details about the “posed” RGB-D images. It’s unclear how the camera pose is encoded for each image.
2. How well does RODIN generalize to various camera configurations? If the test set includes different camera setups, will the model still perform effectively?

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
2

### Summary
The authors proposed RODIN in this paper, which is a text-RGBD multimodal model for 3D vision language understanding. RODIN extends ODIN [1] to be able to reason with open-vocabulary texts. It uses the pretrained RGBD encoder in ODIN and a pretrained CLIP language encoder to encode RGBD images and texts. It follows Mask2Former’s mechanism to use a set of object queries and a transformer-based query refinement module. In this module, the authors propose to also update the features from RGB-D encoder with cross-attention and show performance gain in 3D referential grounding. The authors evaluate the proposed model in multiple datasets and benchmarks and show strong performance, especially when using RGB-D data directly from the sensors without mesh postprocessing.


[1] Ayush Jain, Pushkal Katara, Nikolaos Gkanatsios, Adam W Harley, Gabriel Sarch, Kriti Aggarwal, Vishrav Chaudhary, and Katerina Fragkiadaki. Odin: A single model for 2d and 3d segmentation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 3564–3574, 2024.

### Strengths
- The paper is overall well-written and easy to follow.
- The related work provides a comprehensive overview of 3D visual language understanding.
- The overall design of RODIN is sound and valid.
- The authors demonstrate that the model achieves state-of-the-art performance on several 3D language grounding datasets and benchmarks with a large margin.
- The ablation studies presented in Tables 4 and 5 are sound and well-designed, effectively demonstrating the effectiveness of each design component, particularly the visual token updating mechanism in the query refinement module.

### Weaknesses
 - The model designs are not new: it mostly extends the prior work ODIN to open vocabulary, and follows Mask2Former's decoding design. The architecture novelty is thus limited - most noticable change is the visual feature updating scheme in the query refinement module.
- The fairness in comparison: 
    - are the models shown in Table 1 trained on the same set of data? In L323, the authors mentioned that "This is similar in scale to datasets used by prior SOTA methods like PQ3D Zhu et al. (2024) and 3DVista Zhu et al. (2023b)." Could the authors elaborate more on this?
    - In terms of model size, are the models shown in Table 1 of similar model size?


### Questions
- What do each of the losses terms in equation 7 refer to?
- On eq6, what if a none phrase consists of several words?
- typos:
    - L263: "do not update the visual features through during query refinement as we do" is not grammatically sound.
    - L272: naswers -> answers
    - eq 5 & 6: what does $V^T$ mean?
    - eq 6: missing parentheses around $V^T$
    - L286: $f\theta$ -> $f_\theta$

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new model, RODIN, for 3D vision language understanding. RODIN leverages the powerful ODIN's backbone and extends it with a proposed 3D mask-language decoder based on Mask2Former or a text decoder to achieve state-of-the-art performance on multiple down-stream 3D tasks, including visual grounding, open-vocabulary object detection, and 3D QA. Unlike existing models, RODIN can process raw posed RGBD frames directly, increasing its scalability.

### Strengths
1. This work presents a unique approach by combining an ODIN encoder and a 3D mask-language decoder or a text decoder to solve 3D vision-language understanding tasks directly on posed RGBD frames.

2. RODIN achieves significant improvements over previous methods on multiple downstream benchmarks.

3. The paper is well-structured, with a clear presentation.

### Weaknesses
1. This paper's key idea or contribution is simply extending ODIN with existing mask or text decoder designs for 3D visual language understanding. The main components come from experiences of previous works, making it like an engineering combination, although figuring it out to work with SoTA performance is also appreciated. BTW, the benefit of this method, which can process raw RGB-D input to fit the practical setting, also can not be regarded as a contribution because it comes from ODIN. It is also encouraged to supplement some recent works related to this topic to make a more comprehensive discussion:

- EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI
- LLaVA-3D: A Simple yet Effective Pathway to Empowering LMMs with 3D-awareness

2. In the era of LLMs, I am curious about whether such an idea can be applied to MLLMs and how they perform, which I believe can bring more significant progress or attract more attention than solving these tasks in the previous specialist manner.

3. RODIN relies on datasets with segmentation annotations, however most large-scale datasets do not provide segmentation annotations, which may limit the model's scalability. The author discusses this point in Discussion, but it is not addressed.

4. This paper does not discuss the computational efficiency of RODIN, including hardware requirements and inference time. For real-world applications like robotics, efficiency is a critical factor.

### Questions
1. The paper of ODIN mentions that "Inaccurate depth or camera poses cause a sharp decrease in performance." How do these affect the performance of the RODIN?

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
5

### Summary
Building on prior work ODIN, RODIN introduces a language branch for 3D vision-language tasks, directly using posed RGB-D frames for 3D grounding, object detection, and 3D QA, thus bypassing mesh-based point clouds. It employs masked cross-attention modules, inspired by Mask2Former, to facilitate interaction between images and language. RODIN’s performance is validated across benchmarks such as SR3D, NR3D, ScanRefer, SQA, and ScanQA.

### Strengths
1. The work shows promising performance across Referit3D and ScanRefer.
2. The first end-to-end method that leverages 2D features.

### Weaknesses
1. The model primarily appears as a combination of ODIN with an added language branch and cross-modal interaction module, trained on large-scale 3D vision-language (VL) task heads. Compared to ODIN, which also uses RoBERTa as a language encoder, the technical contribution seems focused on engineering, incorporating Mask2Former’s masked cross-attention modules and an additional MLP language head, similar to PQ3D (lines 167-168). The addition of cross-attention from visual features to object queries, while presented as a key contribution, is not a fundamentally novel architectural component, and its impact needs to be more thoroughly justified beyond the observed performance gains. The paper should provide a more detailed analysis of why this specific modification is so effective, perhaps by comparing it to other potential attention mechanisms or by examining its behavior across different layers of the network.

2. The stated contribution, "The first end-to-end model leveraging pretrained 2D features and finetuning for 3D vision-language reasoning in object detection, referential grounding, and question answering," seems weak, as the visual backbone is ODIN-based (lines 195-201) and is not introduced in this paper. While the end-to-end training is a valuable aspect, the reliance on ODIN as the visual backbone diminishes the novelty of the approach. The paper should more clearly articulate the specific challenges in adapting ODIN for 3D vision-language tasks and how the proposed modifications address these challenges. The claim of being the first end-to-end model needs to be more carefully nuanced, acknowledging the existing work in this area, even if they don’t achieve the same performance.

3. The open-vocabulary claim lacks experiments to demonstrate zero-shot capability. The paper should include experiments that evaluate the model's ability to generalize to unseen object categories or language descriptions. Without such experiments, the claim of open-vocabulary capability is not sufficiently supported.

4. Despite incorporating more training data, the model underperforms ODIN on ScanNet-200 and Matterport3D. Moreover, ODIN already uses open-vocabulary detection prompts like GLIP. The paper needs to provide a more thorough investigation into why the model underperforms ODIN on these datasets, despite the increased training data. The analysis should consider potential factors such as dataset biases, model capacity, or training procedures. The fact that ODIN already uses open-vocabulary prompts further weakens the novelty of this aspect.

5. The paper lacks citations to relevant 2D methods, such as MDETR [3] and GLIP [2].

6. Figure 2 lacks details on the visual encoder design, though it references ODIN, which uses a cross-view encoder. The lack of detail in Figure 2 makes it difficult to understand the specific architecture of the visual encoder and how it integrates with the rest of the model. The paper should provide a more detailed diagram or description of the visual encoder, including the cross-view mechanism.

### Questions
See the weakness.

1. Missing evaluation on additional ScanQA metrics such as CIDEr and BLEU, which would provide a more comprehensive assessment of performance.

### Soundness
2

### Presentation
1

### Contribution
2
