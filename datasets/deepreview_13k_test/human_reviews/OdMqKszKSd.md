# SINGAPO: Single Image Controlled Generation of Articulated Parts in Objects

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
We address the challenge of creating 3D assets for household articulated objects from a single image.
Prior work on articulated object creation either requires multi-view multi-state input, or only allows coarse control over the generation process.
These limitations hinder the scalability and practicality for articulated object modeling.
In this work, we propose a method to generate articulated objects from a single image.
Observing the object in resting state from an arbitrary view, our method generates an articulated object that is visually consistent with the input image.
To capture the ambiguity in part shape and motion posed by a single view of the object, we design a diffusion model that learns the plausible variations of objects in terms of geometry and kinematics.
To tackle the complexity of generating structured data with attributes in multiple domains, we design a pipeline that produces articulated objects from high-level structure to geometric details in a coarse-to-fine manner, where we use a part connectivity graph and part abstraction as proxies.
Our experiments show that our method outperforms the state-of-the-art in articulated object creation by a large margin in terms of the generated object realism, resemblance to the input image, and reconstruction quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel method for generating articulated objects from a single image. Given an image of an object in its rest state, it first asks ChatGPT-4o to output the object's connectivity graph. It then trains a diffusion model to generate coarse descriptions of the parts, conditioned on the input image and the connectivity graph. Finally, it retrieves similar parts from a large database to generate the concrete geometry of each part.

### Strengths
1. The idea of training a diffusion model to generate parts conditioned on a part graph and input image is interesting, as it enables the generation of variations.

2. The authors demonstrate that the proposed method outperforms the baseline and provide extensive ablation studies.

3. Overall, the paper is presented clearly.

### Weaknesses
1. The overall coarse-to-fine pipeline for articulated object generation is not uncommon.

2. The proposed method only handles closed-domain objects and relies on ground-truth annotations for training. However, 3D datasets with fine-grained part annotations are extremely challenging to annotate. In the experiments, the authors focus on only six part categories and seven object categories, which may significantly limit the practical applicability of the proposed method in much more diverse and complex real-world scenarios.

3. The inference of the part connectivity graph relies on GPT-4o, which lacks specific designs and may not be considered a major contribution of the paper. It may also be difficult to inject 3D bias or other priors into the pre-trained GPT-4o.

4. The detailed geometry of parts is retrieved from an existing database. There are concerns about the visual quality and consistency of the parts, which may not be effectively captured by current quantitative metrics like IoU and Chamfer distance. Perceptual metrics may provide better ways to evaluate visual quality and consistency. Can the module retrieve complex and fine-grained parts in addition to primitive-like parts?

Additionally, this retrieval component relies heavily on and is adapted from a previous work.

5. According to Table 2, some components bring minimal gains, such as the classifier-free training on the object category (cCF) and the foreground loss \(L_{fg}\).

### Questions
1. What does `r_i` represent in line 200?

2. I am unclear about the phrase, "the graph determines the ordering of the parts to be generated so that the parts are organized correctly when articulating." Could you explain this in more detail?

3. In line 331, could you clarify why "graph accuracy" for "NAP-ICA-GTgraph" is not 100%?

4. Line 421: The sentence "we report the accuracy (Acc% ↑) in terms of the percentage of correct graph topology" is unclear to me. Could you explain this further?

5. Do you use one token for each part in your transformer?

6. What is the difference between "image guidance (iCF)" and "image cross-attention (ICA)"?

### Soundness
3

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
This paper proposes a framework for single image-conditioned 3D articulated object generation. The framework comprises 3 steps: (i) use a large vision-language models to predict the part connectivity graph from the image; (ii) generate attributes to describe the articulated parts at the abstract level; (iii) retrieve part meshes to assemble the final object.

### Strengths
- The paper addresses an important problem of image-conditioned articulated object generation, with detailed explanations of its importance and challenges.
- The experiments are thorough and well-designed. In addition to the main comparisons, the authors also showed a comparison with a multi-view method Real2Code and ablation studies of each module component as well as data augmentation. There is also a clear discussion of failure cases and limitations.
- Both qualitative and quantitative results look good. Compared to the baselines, the part graphs generated by the proposed method seem to have better global coherence.

### Weaknesses
The overall framework and experiments look good to me. Some minor points:
- If GPT-4o gives a wrong answer to the part graph, there will be no correction to this in the following stages? Intuitively, given an object image, how its part graph can be like should also depend on the prior distribution of part graphs of the object collection.
- As discussed in the introduction, one challenge for the task is that "the parts are small and thin, making them hard to perceive from a single image". The DINOv2 features are on 14x14 image patches, would that be too coarse for the small parts (like handles and knobs)?

### Questions
- For the dataset, when rendering the images, what part states are used? (e.g. door open or closed) It would be good to also explain this. As mentioned in the Introduction, "the object is observed in the closed state where occlusions introduce ambiguity in the part shape and articulation". In fact, it would be interesting to see for the same 3D articulated object rendered under different part states (different joint angles), how would the generation results be like (just an interesting bonus, without this I think the experiments are already quite comprehensive).

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
In this work, the authors proposed a new framework called SINGAPO to generate articulated objects from a single image. The framework designs a modular way to create objects from coarse to fine, including the connectivity graph, attributes to describe the articulated parts at the abstract level, and 3D mesh. The method uses a diffusion model in the process of generating abstract attributes, which allows for variations to account for any ambiguity in the image. The authors also point out that unlike previous methods that require multi-view or multi-state inputs and methods that only allow coarse control over the generation process, this method is the first to explore the generation of articulated objects from a single image.

### Strengths
- Overall, the paper is well-organized and easy to understand. The motivation is clear.
- The paper considers the situation that multiple reasonable articulations of objects may exist when there is only one image input, which is very important for this problem.
- The experimental results show that the proposed method achieves encouraging results on multiple datasets, and the visualization results are reasonable.

### Weaknesses
- Among the limitations mentioned in the paper, it seems that the method has difficulty handling cases with complex textures and cases with complex arrangements. Does this also mean that the method has difficulty handling inputs of real objects? The paper also does not show results with real pictures as input. This raises some concerns about the generalization ability of the model.
- Since the meshes generated by the model come from retrieval, it will not work if there are some shapes in the input image that are not in the model library.
- This method relies too much on the correct connection graph from the input and can not correct the wrong connection graph. This somewhat weakens its claim of "generating articulated objects from a single image".

### Questions
- Quantitative results show that $L_{fg}$ is effective. Could you also visualize the attention map to show what kind of attention map the model learns if the $L{fg}$ is removed?
- Could you provide some results of real image inputs?
- The paper points out the lack of control over the generation process in previous methods. But I don't understand how / if the method can control the model to switch between multiple states due to the ambiguity in the image (shown in Fig. 1). These states are reasonable and the connectivity graph is the same, how can I control it or change the generation results?
- And are these ambiguities taken into account during evaluation? (For example, generate multiple possible states during quantization?)

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
3

### Summary
This paper presents a method for generating 3D articulated objects from a single image, addressing the limitations of prior work that require multi-view or multi-state inputs. Observing an object in a resting state, the proposed approach leverages a diffusion model to capture plausible variations in geometry and kinematics, effectively handling the ambiguity posed by single-view input. The generation pipeline progresses from coarse structure to fine geometric detail, using a part connectivity graph and part abstraction to guide the process. Experiments show that this method outperforms existing approaches in realism, input-image consistency, and reconstruction quality, marking a significant step towards scalable and practical 3D articulated object creation for applications in virtual environments and robotics.

### Strengths
1.	The problem tackled in this paper holds substantial practical significance. In contrast to prior approaches that necessitate multi-view or multi-state inputs, this work enables the reconstruction of articulated 3D assets from a single image, thereby significantly enhancing the generalizability and applicability of the method.
2.	This paper effectively deploys various features to guide the generation process, employing a staged architecture that progresses from coarse to fine detail. The experimental results validate the effectiveness of this staged generation approach in producing high-quality articulated objects.
3.	This paper tackles the ambiguity of generating 3D articulated objects from single-view images, addressing challenges like occlusion and limited visual cues for movable parts. A part connectivity graph guides the spatial layout and articulation hierarchy, ensuring coherence even for small, obscured parts. This approach effectively balances realism and structural plausibility, advancing scalable 3D asset creation from minimal input.

### Weaknesses
1. The proposed method is mainly applied to specific categories of objects (such as cubic furniture and household appliances), and may not be directly applicable to objects with more complex shapes and more diverse categories (such as irregular shapes or soft structures). This limits the versatility of the method.  

2 The use of GPT-4o for part connectivity graph generation faces challenges such as ambiguity handling, prompt sensitivity, and generalization, which are not addressed in the paper. With single-view input, GPT-4o may struggle with occlusion or complex structures, leading to inaccuracies in graph generation. The method's reliance on specific prompts can vary in effectiveness depending on object types and viewpoints, yet the authors do not explore mitigation strategies. Additionally, GPT-4o's performance is limited by its pretraining data, affecting generalization to unseen categories. Addressing these limitations would enhance the method's robustness and applicability in scenarios with high structural variability.

### Questions
1.The article mentions that the coarse-to-fine generation method gives users more editability, but the article does not explain or experiment on this point. Does this mean that users need to be given more interactive experience in the generation stage, similar to text-guided generation?

### Soundness
3

### Presentation
3

### Contribution
3
