# TopoDiffusionNet: A Topology-aware Diffusion Model

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 3, 6, 8

## Abstract
Diffusion models excel at creating visually impressive images %of remarkable appearance 
but often struggle to generate images with a specified \textit{topology}. The Betti number, which represents the number of structures in an image, is a fundamental measure in topology. Yet, diffusion models fail to satisfy even this basic constraint. This limitation restricts their utility %of diffusion models 
in applications requiring exact control, like robotics and environmental modeling. To address this, we propose TopoDiffusionNet (TDN), a novel approach that enforces diffusion models to maintain the desired topology. We leverage tools from topological data analysis, particularly persistent homology, to extract the topological structures within an image. We then design a topology-based objective function to guide the denoising process, preserving intended structures while suppressing noisy ones.  %To address this, we propose TopoDiffusionNet, a novel approach that integrates topology with diffusion models. 
Our experiments across four datasets demonstrate significant improvements in topological accuracy. TDN  is the first to integrate topology with diffusion models, opening new avenues of research in this area.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes TopoDiffusionNet, a method to control some topological properties of 2D image generation, such as the number of distinct objects and separated regions.

TopoDiffusionNet is trained to take as input a condition $c$, representing the number of the structures, and to output a mask with exactly $c$ separate objects or regions. The network is optimized with a loss based on persistent homology; after computing the persistent diagram, the features are separated into "preserve" (the $c$ features with higher persistence), and "noise" (all the others). The network is trained to promote the first while suppressing the others. The generated mask can be used as a condition of a 2D generative ControlNet.

The method is tested on four datasets (Shapes, COCO, CREMI, Google Maps), showing significantly more control than previous methods.

### Strengths
The posed problem is interesting, and it is relevant for a wide community. Defining new ways to control generation and especially incorporating this knowledge into the diffusion process itself provide interesting insights. The paper is also informative and well-organized: The text is well-written, and it is pretty straightforward. The proposed methodology is clear, and the figures are quite insightful. Experiments consider diverse datasets and control results are convincing.

### Weaknesses
My main concern is that the paper does not offer much insight into the trade-off between control and quality. It is pretty natural to wonder how the control impacts the quality of the generation compared with other methods. The qualitative examples shown seem ok, but it is also evident that the quality is quite degraded compared to alternatives -- this might be a cause of the generative 2D ControlNet itself or that the control does not incorporate enough domain knowledge and provide a mask difficult to respect (e.g., the mask of cats and birds do not look realistic, and I guess it requires quite some work for the ControlNet generation to compensate) . The only FID score is reported in an ablation study on the Shape dataset, which is not particularly insightful. I think reporting (at least) the same metric for other datasets and comparing it with other methods would be important to assess how much the provided approach destroys the generative capability of the generative backbone.

### Questions
Please refer to the weaknesses of the main points to clarify.

Some minor curiosities are:

1) Would it be possible to combine 0-dim and 1-dim constraints?
2) Does the computation of persistent homology have an impact on the computational performance of the method?
3) While the method provides control only on the number $c$, is it possible to tune homology parameters to promote also bigger or smaller components?

### Soundness
3

### Presentation
3

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
This paper proposes a procedure for conditioning text-to-image diffusion models on topological constraints. In particular, an auxiliary diffusion model is trained that generates binary segmentation masks that conform to a specified zeroth and first homology ranks (i.e., the number of connected components and holes). This is done both by providing the Betti numbers as input conditions to the network and by imposing a loss on the homology of the predicted image. Because the predicted images at early timesteps are very noisy, an approximation of the denoised image is computed, and the persistence module of that image is what is used in the loss objective.

### Strengths
Maintaining desired compositionality is a key challenge for diffusion models, and getting a model to output the desired quantity of discrete objects is often difficult. Framing this problem through the lens of persistent homology makes a lot of sense and ties nicely to the difficulty of dealing with noisy samples at intermediate timesteps. Additionally, being able to condition on first homology is also a nice feature, albeit it seems a bit more contrived (and indeed the main demonstrated use case is in generating aerial road images).

### Weaknesses
My main concerns with this paper have to do with the overall novelty as well as the overall justification for the approach.

While this paper is indeed the first to consider diffusion-based image generation through the lens of TDA and persistent homology, the actual machinery proposed to accomplish this is very similar to prior work that combines TDA with deep learning --- a key insight is differentiating through the persistence computation, but this is not unique to the diffusion setting. I do agree that the observation that the a persistence module can well represent the homology of a noisy $x_0$ approximation is interesting, but this brings me to my second concern, which is that I am not convinced by the results in this paper that training a diffusion model is critical to the success of this method.

One of the main reasons for the success of image diffusion models is their stability and performance in generating high-quality complex natural images. The masks produced by the diffusion model in this paper, however, are quire primitive and lack detail or high-frequency detail. I wonder if a much simpler generative model, e.g., a VAE, could be just as effective at producing these masks, that could then equally serve as input to a ControlNet. Moreover, I am not convinced that an ML model is necessary to generate these mattes in the first place. Given that the only conditions that the model accepts are the Betti numbers and an object class (nothing more about the actual layout can be specified), it seems to me that such masks could be procedurally generated to obey the desired topology. In fact, looking at Figure 6, it appears that the object class condition is superfluous for the mask model, given that it also appears in the ControlNet prompt. If we look, e.g., at the birds (bottom right), the contour of the second bird from the right is completely different from the input mask. This suggests that the ControlNet largely ignores any higher-frequency context in the mattes.

### Questions
It would be very helpful if the authors could respond to my two points noted above---the second one in particular. At the very least, some simple ablation studies can be conducted to help justify the overall algorithm. For instance, what if the conditioning masks simply contain circles or other basic shapes for the desired objects (even in the case of animals)? Would the ControlNet still understand the object type from the text prompt and use the simplified mask as the cardinality/topology conditioning?

### Soundness
3

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
This paper proposes a generative method for images that can be constrained in its resulting topology - number of objects, as well as the connectivity between objects. The core idea is to use persistent homology which essentially constructs, for each image produced in a diffusion process, a 3D embedding is created by marking all pixels that exceed each z>0 - this enables the authors to produce a topological signature for the image (for different z's) which enables to ignore noisy structures and evaluate the topological invariants of the resulting clean image. The authors then devise a simple loss that uses this information and regularize the neural network to respect the topological constraints.

### Strengths
I am not an expert in image generation, but I like the idea of adding topological constraints to image generation. It could be very interesting to be able to accurately control resulting images' topology.  I found the approach to be rather straightforward and thus easy to understand and implement. Considering I could not find a prior work that aims to achieve the same result, I find this approach novel.

### Weaknesses
Again, I am not an expert in image generation, however it seems to me that in the end, the paper focuses mainly on number of objects and less so on more important topological invariants such as connectivity. There are many interesting tests one could cook up, e.g., choose Betti numbers that force a very specific topology (double annulus) and show the method can achieve that. These more interesting topological invariants are also not directly measured in the quantitative evaluations, as far as I understand. I am also uncertain how far can this type of topological control be effective for practical uses, beyond, again, the trivial case of controlling number of objects. The use of persistent homology, while mathematically sound, seems like overkill for simply counting connected components. It is unclear if the full power of persistent homology is actually leveraged, or if a simpler approach could achieve similar results for this specific task. The paper does not explore the limitations of the method in terms of the complexity of the topological constraints, and it's unclear how well the method would scale to images with very complex topological structures.

### Questions
- Empirically (not in theory), can your code generate more complex specific shapes by choosing the right topological invariants as input?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a method to control the topology of images generated by the diffusion model. By combining the persistent homology theory, a topological mask is generated with noise, and it is fed to the diffusion model as a condition together with the time steps, achieving more accurate topological control of image generation.

### Strengths
The authors claim that they are the first to combine topological and diffusion models on image generation. Although I cannot be sure of this, I think it is indeed a problem that needs to be solved urgently, and this paper provides a possible solution to it.

The combination of persistent homology and diffusion modeling is new to me, and although the combination way is simple, it appears to be effective.

This paper is well written, with rich comparative data and ablation experiments on corresponding parameters.

### Weaknesses
Should authors explain in more detail how persistent homology is calculated? I think the part about how it is integrated into the diffusion model and how the loss between the two sets of P and Q defined is well explained, but the specific calculation of persistent homology seems a bit lacking in details. 

The persistence diagram could be more explicit, for example by using different point sizes and colors to show which P sets are more important.

### Questions
In Figure 4, the lower part of \alpha_3 seems to be cut off by a straight line? Is it because it is a cube? If so, why doesn't it appear on the other three boundaries?

Although I know this is not the task of this paper, it would be nice if higher-dimensional topological control, such as 3D, could be discussed as future work.

### Soundness
3

### Presentation
3

### Contribution
3
