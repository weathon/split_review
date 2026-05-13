# Variable resolution: improving scene visual question answering with a limited pixel budget

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Artificial intelligence (AI) scene understanding systems can benefit from utilizing a large visual field of view (FOV). Some existing systems already employ multiple cameras to extend their FOV, however,  increasing image size and quality presents an overwhelming challenge to the acquisition and computing resources for such systems. An effective solution is to sub-sample the FOV, without impairing the model's  performance on complex visual tasks. In this paper, we show that a variable sampling scheme, inspired by human vision, remarkably outperforms a uniform sampling scheme by 2% accuracy (65% vs. 63%) in the challenging task of scene visual question answering (VQA), under a limited samples budget (3% of the full resolution baseline). The improvement is achieved without any image scanning, and the variable resolution peaks at an arbitrarily chosen fixed image location. Our study also compared basic visual sub-tasks, in particular image classification and object detection. Comparing the variable and uniform models revealed differences in the representations learned by the different models which yield a consistently improved performance of the variable resolution models. We show that the variable sampling scheme allows the models to benefit in low resolution areas, by propagating information from the finer resolution areas, and at the same time higher resolution areas benefit from contextual information at lower resolution in the periphery. The results show the potential of the biologically-inspired image representation to improve the design of visual acquisition and processing models in future AI-based systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors re-evaluate the use an design of a variable resolution visual sensor for neural networks, and try to approach this problem from the angle of representational gains rather than computational efficiency (what is classically accepted in the literature). Authors show several experiments ranging from detection, VQA + interpretability to show the advantage when 2 systems are placed under equal perceptual sensing conditions to perform inference (uniform vs variable) and thus finding that the neural network with a variable resolution sensor in many cases out-performs the equal resolution one (that is usually more blurred).

### Strengths
* The paper tackled the question of the use of a foveated (spatially-adaptive) visual system through the lens of object detection, interpretability + Visual Question Answering (VQA). I will give it to the authors, as I don't think this has ever been done before, which is why I am marginally inclined to accept this paper. Most methods of testing for the representational goal of foveation is through object classification or detection, and even more recently for texture-based discrimination. Authors talk a bit about this too, in addition to present interpretabilty experiments similar to Deza & Konkle. ArXiv, 2021.
* Authors have made a good case for showing representational gains of a foveated visual system

### Weaknesses
There is a long list of critical missing papers that should be cited if this paper is to be accepted. I can not increase my score to accept unless these papers are cited & discussed (and of course, if the other reviewers also think that this paper should be accepted).

Key Missing Critical References:
- Deza & Konkle. ArXiv, 2021. **Emergent Properties of Foveated Perceptual Systems.**
- Wang & Cottrell. Journal of Vision, 2017. **Central and peripheral vision for scene recognition: A neurocomputational modeling exploration.**

Secondary, but also important References:
- Cheung, Weiss & Olshausen. ICLR 2017. Emergence of foveal image sampling from learning to attend in visual scenes
- Gant, Banburski & Deza. SVRHM, 2022. Evaluating the adversarial robustness of a foveated texture transform module in a CNN.
- Reddy, Banburski, Pant & Poggio. NeurIPS 2020. Biologically inspired mechanisms for adversarial robustness
- Wang, Mayo, Deza, Barbu & Conwell. SVRHM, 2021. On the use of Cortical Magnification and Saccades as Biological Proxies for Data Augmentation
- Harrington & Deza. ICLR, 2022. Finding Biological Plausibility for Adversarially Robust Features via Metameric Tasks
- Malkin, Deza & Poggio. SVRHM 2020. CUDA-Optimized real-time rendering of a Foveated Visual System.

### Questions
* While I think the VQA evaluation framework is original, what I do not understand is "why VQA?", why not something less complex such as object recognition or detection where language modelling will not interfere in the output produced by the system. I can only think of an answer if there is an argument somehow linking foveation with language but that does not seem to be the case. I can see an object detection evaluation which I think is nice, but that has already been shown in Pramod et al. 2021.

* Comparison of this work with Deza & Konkle is necessary. They addressed many questions presented in this paper such as training on different types of foveal-peripheral transforms, the use of foveation as a texture-based distortion that mimics crowding vs a more rudimentary baselines such as adaptive gaussian blurring. Furthermore it would have been interesting if the Authors would have compared their results in ImageNet vs Places. Does the same pattern of results hold? Does Foveation do better by virtue of a central image bias where the object is usually put in the center of the image? Presumable more controlled experiments are necessary to try to answer these questions.

* I am not sure what the red dots represent in many of the figures such as Figure 5 and S5.

All in all, I think this paper is exciting, but discussing and adding the missing references is necessary.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors claim that they propose a variable sampling scheme, inspired by human vision, remarkably outperforms a uniform sampling scheme by 2% accuracy (65% vs. 63%) in the challenging task of scene visual question answering (VQA), under a limited samples budget (3% of the full resolution baseline).

### Strengths
The authors claim that they propose a variable sampling scheme, inspired by human vision, remarkably outperforms a uniform sampling scheme by 2% accuracy (65% vs. 63%) in the challenging task of scene visual question answering (VQA), under a limited samples budget (3% of the full resolution baseline).

### Weaknesses
1. According to the title, the author's focus is on VQA. but it seems that only one dataset (VQA v2) from VQA task was used. How does the authors' proposed method perform on other common datasets such as GQA, OOD-GQA, etc.?

2. The method proposed by the authors seems to address object detection and is not a VQA task.

3. Does Sec.5 relate to the VQA task? Why?

4. Is the technical or scientific challenge addressed throughout the article associated with VQA? Why?

### Questions
Please refer to Weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Inspired by the perspective of observing the world through biology, this article makes a bold attempt to apply a variable resolution mechanism of image on a VQA task and tries to make a trade-off between performance and computation cost. The variable resolution is implemented by a simple Log-Polar transformation while achieving a great surpass compared with the naive down-sampling strategy, and a comparable result compared with the full resolution strategy. This work then discovers the interpretability of the variable resolution, trying to prove that higher-resolution areas and lower-resolution areas can benefit from each other.

### Strengths
1. This paper is well written, which is reflected in its proposed variable resolution that effectively reduces the overall computational cost.
2. The innovation point of this paper is simple, and experiments on VQA and object detection have proved its effectiveness.
3. The visualization of the explanation that variable resolution performs better than uniform resolution is thorough. The attention map indicates that higher resolution areas and lower resolution areas can benefit from each other, and the neuronal activation maps and kernel filters explain the better performance from a model perspective.

### Weaknesses
1. Some of the experiments are missing. Firstly, as the title of the article is related to VQA, and models that perform well on object detection tasks may not necessarily have the same effect on VQA tasks, I hope to include more space in the experiment on different types of VQA datasets, such as OK-VQA. Secondly, this work has proved the effectiveness of variable resolution in that the central part has a higher resolution but only makes the comparison with uniform sampling, which is too naive to have a good performance. So I’m also curious about what the result would be when other part of the image has a higher resolution or other sampling strategies.
2. The selection strategy for high-resolution areas in the image needs to be improved. As shown in Figure 4, not all objects reside at the center part of the image, so this could be the cause of the poor performance in Table 2 when compared with the baseline. As this paper raises the HRA metric, it’s better to define a better selection strategy corresponding to this, or just sampling by gradients following the dynamic mask in [1].
3. The interpretability analysis of variable resolution is not convincing enough. Some visualization experiments are not as important as shown in the paper, and some visualization is lacking. 
On the one hand, there are too many visualization examples of the impact of the three sampling methods on the label of an object in the image. As a common sense, if we feed the model with a lower resolution of the image of the object, the model has a higher probability of giving a wrong label. 
On the other hand, as shown in Figure. 3, the variable sampling scheme performs well on the questions that can be answered from parts of the image rather than the whole context of the image. That is because we don't have enough understanding of the correlation between hyperparameters and sampling strategy of variable resolution and global background knowledge. The explanation of this correlation is lacking, but the whole context of the image is important to VQA.

### Questions
Overall, I find the idea of this paper to be simple but reasonable. Because of its simplicity, I find no obvious weaknesses on the technical side but there is still room for improvement in performance. The authors use a large portion of this paper to explain the reason of its effectiveness, some of them are convincable, but the lack of deeper quantitative experiments makes the explanation not sufficient enough.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
