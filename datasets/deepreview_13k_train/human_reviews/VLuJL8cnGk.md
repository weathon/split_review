# 3D-free meets 3D priors: Novel View Synthesis from a Single Image with Pretrained Diffusion Guidance

- Decision: Reject
- Scores: 5, 8, 3, 6, 3

## Abstract
Recent 3D novel view synthesis (NVS) methods often require extensive 3D data for training, and also typically lack generalization beyond the training distribution. Moreover, they tend to be object centric and struggle with complex and intricate scenes. Conversely, 3D-free methods can generate text-controlled views of complex, in-the-wild scenes using a pretrained stable diffusion model without the need for a large amount of 3D-based training data, but lack camera control. In this paper, we introduce a method capable of generating camera-controlled viewpoints from a single input image, by combining the benefits of 3D-free and 3D-based approaches. Our method excels in handling complex and diverse scenes without extensive training or additional 3D and multiview data. It leverages widely available pretrained NVS models for weak guidance, integrating this knowledge into a 3D-free view synthesis style approach, along with enriching the CLIP vision-language space with 3D camera angle information, to achieve the desired results. Experimental results demonstrate that our method outperforms existing models in both qualitative and quantitative evaluations, achieving high-fidelity, consistent novel view synthesis at desired camera angles across a wide variety of scenes while maintaining accurate, natural detail representation and image clarity across various viewpoints. We also support our method with a comprehensive analysis of 2D image generation models and the 3D space, providing a solid foundation and rationale for our solution.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the problem of generating novel views from a single image without relying on 3D datasets for training. The authors propose to leverage the 3D knowledge embedded in large-scale pretrained diffusion models to create camera-controlled viewpoints through test-time optimization. Specifically, the method fine-tunes the text prompt and diffusion model to align with the input and a pseudo-guidance image, incorporating mutual information guidance during the final diffusion process to enhance image fidelity. The experiments demonstrate that the proposed model can generate semantically consistent novel views for images with complex background.

### Strengths
- The proposed approach effectively integrate 3D-free methods and pretrained 3D-based prior to achieve viewpoint-controlled novel-view synthesis. This technique can generalize to complex scenes without needing large 3D training datasets.

- The mutual information guidance improves fidelity of the generated images over the pseudo guidance.

- The method is tested both qualitatively and quantitatively, showcasing superior performance compared to state-of-the-art models, especially in handling background details and complex scenes.

- The analysis of the significance of CLIP and guidance images provides a solid motivation for the proposed research.

### Weaknesses
 - While the authors acknowledge the limitation of inference-time optimization in terms of real-time applicability and scalability, a direct runtime comparison with baseline models would provide additional clarity.

- This method is incapable of generating arbitrary camera viewpoints. this might be due to the choice of the 3D prior, Zero123++, which can provide guidance images at six fixed viewpoints. Clarifying this limitation or demonstrating the capability of generating arbitrary viewpoints is much needed.

- The novelty of the proposed framework is somewhat limited. The approach builds heavily on the HawkI, with modifications such as replacing guidance images generated via Inverse Perspective Mapping with those from a 3D prior method (Zero123++). This modification, while practical, could be seen as a straightforward combination.

- The generated images across different viewpoints appear inconsistent. Does the proposed method include any mechanisms to encourage consistency across these viewpoints?

### Questions
The generated images across different viewpoints appear inconsistent. Does the proposed method include any mechanisms to encourage consistency across these viewpoints?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a framework for scene-level camera-control novel view synthesis(NVS). The framework combines 2D image generative prior with object-level 3D generative prior to achieve scene-level NVS. The authors start with an analysis on where should generative model learn the viewpoint information, then proposed a multi-stage inference-time optimization method to generate novel views given specific camera conditions and input images. Qualitative and quantitative evaluation on benchmarks show its superior performance comparing to other methods.

### Strengths
1. The idea of combining priors from 2D image generative model and object-level 3D generative model is interesting and can be considered as an effective way to leverage different data source for 3D understanding. I think this idea in general is very important.

2. NVS results on scene images are quite impressive considering no additional training is involved.

### Weaknesses
I think this paper's main weakness is on how the authors present the whole framework in a more motivated way. I'd briefly state this weakness here and leave the others in the following questions section.

1. The connection between the section3 and section4 is very confusing. First, the detailed experiment setting in section3 is not clearly explained (see questions), then it suddenly shift from section3 with CLIP embeddings to section4 on leveraging a diffusion model. I suggest authors revise the high-level motivations and present them more clearly in the paper.

2. The figure 2 for pipeline is actually making it harder to understand. I'd suggest at least add some orderings in it can better illustrate the whole pipeline.

### Questions
Below are some questions or some parts in the paper that I find confusing.

1. What is the detailed procedure of experiments related to figure 3. and figure 4.? What is the actual model that generates those images? CLIP itself isn't a generative model. Does the author mean using Stable Diffusion with different text embeddings? And how is the image guidance been used in (I assume) this standard SD model?

2. Although inference-time optimization with efficient methods like LoRA and embedding finetuning is not that slow, I'd suggest authors also provide the memory consumption and time used in this process, addition to optimization iterations.

3. Are the specific evaluation viewpoints come from Zero123++ settings? So the method is actually limited to certain viewpoints?

4. It's interesting to see that images generated from Zero123++, which is trained on Objaverse, can generate reasonable images' guidance with scene image input. Combining this with previous question, what's the problem of using some open-sourced scene-level NVS models for pseudo guidance? For example, I'd assume ZeroNVS[1] can provide images with any viewpoint input condition.

[1] Sargent, Kyle, et al. "Zeronvs: Zero-shot 360-degree view synthesis from a single real image." CVPR 2024.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents an optimization-based sampling method to generate novel views at inference time. It utilizes multi-view images generated by a pre-trained diffusion model and optimizes the text embeddings and LoRA layers of a text-to-image diffusion model to guide the novel view sampling process.

### Strengths
1. The paper investigates an approach that sequentially optimizes the text embeddings and LoRA layers of a diffusion model to guide the novel view synthesis process.

### Weaknesses
1. The proposed method relies on a pre-trained multi-view diffusion model, Zero123++, and thus shares its limitations: restricted view generation (Zero123++ generates six fixed-view images around the object), modification of background and object, handling multiple objects, and pose misalignment.
2. The evaluation can be seem unfair. For apple to apple comparison, the paper could compare with running the proposed method on Zero123++. Also, measure the CLIP score seem unfair as the proposed method optimizes the CLIP text embeddings.
3. The proposed method introduces additional computational costs: generating a multi-view guidance images from a pre-trained diffusion model and the optimization of text embeddings to reconstruct $I_{input}$ and $I_{view}$.

* L.86, L.90: Some terms are used in contradicting manner. 3D-free methods like Zero123++  and 3D-based models like Zero123++.
* L.95: we (1) we 
* Eqn. 1: The optimization task is provided without details. $L, f, x_t$ is not introduced before.

### Questions
The method could be presented with more detail. Specifically, how do Eq. 1 and Eq. 2 work? Does the diffusion model output clean predicted samples? If not, how is the loss computed between the noisy latent $x_t$ and the clean image $I_{input}$?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper tackles the problem of novel view synthesis from a single image input of a scene by using textual camera view description. The problem statement is very similar to previous works Zero123++, HawkI, except that an additional guidance image is introduced, obtained through a pre-trained model Zero123++, tackling the same problem. The guidance image network Zero123++ is trained on 3D shapes, but for a single object. The introduced method uses a series of 2 double-step optimizations. The first stage optimizes the diffusion-enriched CLIP space of the input view and the second stage does the same for the target view. The results show that the proposed method has better performance in comparison to previous works. It tends to be more consistent in showing both central object and background from a variety of viewpoints (which are specified in terms of azimuth and elevation angles).

### Strengths
1. The method shows a good performance of novel view synthesis on a single view of a scene with object + background. As far as related works are concerned, the method shows - on average - better results using a textual prompt and without depth information for object + background when novel views are synthesized.

2. The results show a consistent performance gain over previous works in both real and synthetically generated data.

### Weaknesses
1. The method is quite convoluted with 4 different test-time optimization steps. No time comparisons are provided. It would be important to mention typical in inference times... 

2. Looking into the intermediate and final results, as well as the method, the main task of aligning the camera appears to be the result of the Zero123++ method, while the test-time optimizations generally improves the image quality. This is also reflected in the particular choice of angles, as only those angles are trained for in Zero123++. However, for small angles (30,30), often the test-time optimization worsens the results, e.g., figure 6, angles = (30,30) for cats. Same for figure 5, angles = (30,30)- the house changes completely after optimization. Due to this reason, it may be a bit dubious to stipulate object + background novel view synthesis as contribution. After the evaluations, both the contributions (1) & (2) could be attributed - at least in part - to Zero123++.

3. The architecture diagram in Figure 2 is not complete in the info provided. Missing: which losses are used? These should be made clear together with the equations (1,2) since this is the crux of the proposed method.

4. L215--L216- "Our model eliminates the need for training data, 3D data or multi-view data". This is somewhat misleading. The camera alignment largely appears to be performed by the guidance method Zero123++, which is trained on Objaverse and more importantly on  the same task. The method implicitly uses Objaverse via Zero123++, a competing method used in the proposed method. It is not clear how Zero123++ performs test-time optimization without the 3D data.

5. The paper glosses over some of the limitations in the results, like the house not being shown in a very consistent fashion when viewpoint is changed. Probably there is a difference in performance between renowned monuments with many photographs that can be scraped from the Internet, compared to rather unique objects / situations. 

6. Given the complete approach, the novelty of the work mainly consists of the combination of methods, whereas the actual novelty drags in the cost of extensive inference optimization. 

7. The English could benefit from some slight polishing at times

### Questions
It would be good if the authors clearly define what they mean by azimuth and elevation angles. The typical definition of the latter would be relative to the horizontal plane. Is that the case here as well, or are angles relative to the guidance view ? In any case, the angles specified in the image captions do not seem to follow one consistent set of definitions... Elevation angles are taking up values larger than 90 degrees, for instance. 

Related work that could be mentioned: Depth self-supervision for single image novel view synthesis, 2023 Giovanni Minelli et al.

The creation of videos with continuously changing viewpoints would be telling when it comes to consistency and angle correctness...

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper argues that current NVS methods are limited to single-object-centric scenes and struggle with complex environments. Moreover, they require extensive 3D data for training. Therefore, this paper proposes a training-free method to combine the benefits of 3D-free and 3D-based methods. It leverages pretrained NVS models for weak guidance and integrates the knowledge into a 3D-free approach to achieve the desired results.

### Strengths
1. The motivation for training-free novel view synthesis is good.
2. The analysis of the current NVS model’s limitation is reasonable.

### Weaknesses
1. The writing is poor and many sentences are extremely confusing without any support. I will list several examples below and there are more similar problems in the submitted paper.
    
    In Line 265. “Explain the subset you used for your results, how you created the,….”. What does the author want to express here?
    
    In section 3.1, why does Fig.3 illustrate these findings? I believe the findings here are that CLIP struggles with 3D comprehension, but I do not see any examples in Fig.3 supporting this viewpoint. Moreover, if CLIP itself can control camera pose change, there is no need for training on 3D-aware data pairs. I do not see the necessity of including this discussion.
    
    In Line 146. “validates the necessity of 3D guidance images.” What is 3D guidance images? Is it a novel view image based on the current image?
    
    In Line 159. “This indicates that the model benefits from the information in the 3D-derived guidance image, and that the guidance image is not simply a source of extra variance.” What does the author want to express here? What is the 3D-derived guidance image? Does it also mean a novel view image? If so, what does the author mean by “not simply a source of extra variance”? What is the variance? From Fig.4, I guess the author is conducting an experiment on using different novel view images as weak guidance while prompting the generation of novel view images using the proposed training-free method. The reviewer thinks using the right guidance image is quite trivial. 
    
2. The performance improvement is weak. From the visualized comparison in Fig.5, I don’t see much difference between Zero123++ and Ours. Is the camera view control more precise or is the image more realistic? From the waterfall example, I think the result of Zero123++ is more realistic. 
3. The novelty is weak and the method is not well explained. I think a training-free method is a good motivation. But the author still requires heavily on a pretrained NVS model. 
4. Related work is not well discussed. To cope with the complexity of real scene instead of object-level, many works have been proposed and the author should include them. I will list several below.

[1] ZeroNVS: Zero-Shot 360-Degree View Synthesis from a Single Real Image, CVPR 2024

[2] MegaScenes: Scene-Level View Synthesis at Scale, ECCV 2024

[3] Generative Camera Dolly: Extreme Monocular Dynamic Novel View Synthesis, ECCV 2024

### Questions
Minor:
In Tab.1 and Tab.2, since the author reports the LPIPS metric, I believe the commonly used PSNR and SSIM metrics can also be reported.

The reviewer suggests that the author revise the writing, conduct more thorough experiments, and propose a clearer explanation of motivation and method.

### Soundness
2

### Presentation
1

### Contribution
1
