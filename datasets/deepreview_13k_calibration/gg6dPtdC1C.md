# Build-A-Scene: Interactive 3D Layout Control for Diffusion-Based Image Generation

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 3, 8, 6

## Abstract
We propose a diffusion-based approach for Text-to-Image (T2I) generation with \emph{interactive 3D layout control}.
Layout control has been widely studied to alleviate the shortcomings of T2I diffusion models in understanding objects' placement and relationships from text descriptions.
Nevertheless, existing approaches for layout control are limited to 2D layouts, require the user to provide a \emph{static} layout beforehand, and fail to preserve generated images under layout changes.
This makes these approaches unsuitable for applications that require 3D object-wise control and iterative refinements, \eg, interior design and complex scene generation. 
To this end, we leverage the recent advancements in depth-conditioned T2I models and propose a novel approach for interactive 3D layout control.
We replace the traditional 2D boxes used in layout control with 3D boxes.
Furthermore, we revamp the T2I task as a multi-stage generation process, where at each stage, the user can insert, change, and move an object in 3D while preserving objects from earlier stages.
We achieve this through our proposed Dynamic Self-Attention (DSA) module and consistent 3D object translation strategy.
Experiments show that our approach can generate complicated scenes based on 3D layouts, boosting the object generation success rate over the standard depth-conditioned T2I methods by $2\times$.
Moreover, it outperforms other methods in comparison in preserving objects under layout changes.
Project Page: \url{https://abdo-eldesokey.io/build-a-scene/}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Based on the recent advancements in depth-conditioned T2I, this work presents a novel approach for interactive 3D layout control.     Further, the authors propose a Dynamic Self-Attention (DSA) module and a consistent 3D object translation strategy, to preserve the existing contents and consistent 3D translation.

### Strengths
1. The task is well-defined.
2. The model is designed reasonably.
3. The paper is well-written and clearly states the contribution.
4. The results are well-organized, and the experiments are comprehensive.

### Weaknesses
1. 3D Awareness. Existing results are mainly about the 3D layout conditioned generation. However, the 3D information is not adequately used. There are several other degrees of freedom in 3D spaces, such as the camera view, the rotation of objects, and the zoom-in/out. These results (even parts) could strengthen this work a lot.

2. User interface. What exactly is the interface? Can you describe the tools for users to use? The interface for the creator is critical, especially for 3D editing. A reasonably designed interface can make this work for real-world applications. Just a demo-based (actually controlled by codes) can not make it practical.

3. The motivation. The motivations of the design of the pipeline is not very clear. The key feature of this work is that it can implement 3D layout-based generation. However, what are the challenges in this task, and why authors must use the proposed pipelines and modules to deal with this challenge?

### Questions
See Weakness.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
BAS introduces a pipeline which allows users to guide the image synthesis through interacting with boxes in the 3D space and using the text prompt. The boxes reflect the position of objects in the image. To keep the image consistency throughout interacting, the author propose the dynamic self attention and object wrapping in order to maintain the background as much as possible. As a new work to introduce 3D interacting into 2D image synthesis, it proposes several benchmarks to evaluate its performance and compare to some image synthesis works.

### Strengths
Firstly, using inpainting to preserve the background during the interacting is a simple but sound idea, and the manipulations in 3D world make the masks’ calculation fully under control. Furthermore, 3D guidance is common and useful when we want to show the relative transformation of objects to the diffusion model, as we usually want it to give image of the real 3D world.

### Weaknesses
(1) The technical contribution seems not to be so sufficient. As the T2I techniques and pre-trained models are mature, would organizing the masks according to the boxes 3D transformation being sufficient for a paper? Well, the dynamic self-attention block is surely a contribution.
(2) However, in the ablation study, it says “when DSA is disabled, the model isn’t capable of inserting new object”, but in the method, DSA is proposed for maintaining the background, which is different from what may happen in the ablation study. The technical contribution turns out to be confusing and doubtful. 
(3) Another consideration is that your run time is 3 times of “loose control”. Would that be harmful to the interaction? Could you please discuss more on that?
(4) Some expression in the “METHOD” still tells why other methods aren’t suitable for this “attention”. That should not appear here.

### Questions
No

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a interactive 3D layout control approach for T2I based on diffusion approach.  Beginning with an generated scene images without objects inside, the proposed approach allows uses to add 3D box and its text description in the bounding box of the scene to specify the 3D layout of the scene.  The depth map of the 3D layout and the text description are used as the condition to guide diffusion model, and the keys are combined according to the mask of the box to maintain the style of the image in each stage, denoted as dynamic self-attention. 

The video demo is nice, which demonstrates the 3D layout control process clearly.

### Strengths
1. A straightforward yet effective approach to control the scene layout and the styles of objects placed in the scene.  With the 3D interface, the user can control how to put the objects on other objects or the relative position between objects, more natural than 2D interface.  The ability to move the object closer or farther away from the camera is also attractive. 

2. The DSA module designed to merge the keys at different stage is easy to implement, and it allows to generate new object of a different style. Also, the combination of latent codes according to the mask  and AdaIN operation can effectively maintain the image styles surrounding the newly inserted object.

### Weaknesses
The composes scene is relatively simple.  All objects are put on the flat surface, such as floor or desk top. It might be partially attributed to the box-based 3D layout control interface.  For example, can we put an object on the sofa if we use freeform surface as the control interface?  If freeform surface, how much effort does the user should pay to place a new object such that the diffusion model can generate the image correctly? The current box-based approach limits the complexity of the scenes that can be generated, restricting objects to planar surfaces and hindering the creation of more intricate arrangements. The lack of support for non-planar surfaces severely limits the potential for creating realistic and diverse scenes. For example, placing a complex object like a draped cloth or a curved sculpture would be extremely difficult, if not impossible, with the current bounding box control. This limitation also impacts the ability to create scenes with objects interacting in a non-trivial way, such as a person sitting on a chair or a book resting on a slanted surface.

### Questions
In the DSA model,  why do you only combine the key tokes between stage i-1 and stage i?  I am wondering the effect of combining V tokens instead.  Discussions on why chose key tokens in DSA is necessary for the deep undstanding the design of DSA.

### Soundness
3

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
3

### Summary
This work is trying to generate an image based on the layout of 3D boxes for each object we desire in the image. It builds upon a depth-conditioned stable diffusion generator, and they make it an iterable fashion where they focus on different object placement in each step to enhance control of each separate object. to keep the information from the last iteration to the next, they presented the Dynamic Self-Attention (DSA) module which blends between attention maps from the previous iteration and the new one, specifically on the mask where the new object is placed.

### Strengths
they present an interesting 3D layout control over generated images, Furthermore, the multi-stage to have more control over each object sounds good.

### Weaknesses
1. you presented in most of the paper examples of moving the object aside (Fig.2), however, with 3D boxes, it is much more interesting to see examples of moving toward me or away from the observer. you provided only two examples like this in Fig.6, I would love to see it as the focus of the paper.
2. your evaluation metrics (Table. 1) have no comparison to 3D information, which is the focus of the paper. i would love o see a new metric that can evaluate the 3D placement, like with monocular depth estimation, or 3D object detection networks.

### Questions
from your pipeline figure (Fig.3) it seems like you didn't talk about some key parts of the method, specifically in stage 2 (warping, DDIM inversion) it might not be novel, but helps to grasp the notion of the method.

### Soundness
2

### Presentation
2

### Contribution
2
