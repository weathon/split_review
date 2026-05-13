# CAX: Cellular Automata Accelerated in JAX

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Cellular automata have become a cornerstone for investigating emergence and self-organization across diverse scientific disciplines, spanning neuroscience, artificial life, and theoretical physics.
However, the absence of a hardware-accelerated cellular automata library limits the exploration of new research directions, hinders collaboration, and impedes reproducibility.
In this work, we introduce CAX (Cellular Automata Accelerated in JAX), a high-performance and flexible open-source library designed to accelerate cellular automata research.
CAX offers cutting-edge performance and a modular design through a user-friendly interface, and can support both discrete and continuous cellular automata with any number of dimensions.
We demonstrate CAX's performance and flexibility through a wide range of benchmarks and applications.
From classic models like elementary cellular automata and Conway's Game of Life to advanced applications such as growing neural cellular automata and self-classifying MNIST digits, CAX speeds up simulations up to 2,000 times faster.
Furthermore, we demonstrate CAX's potential to accelerate research by presenting a collection of three novel cellular automata experiments, each implemented in just a few lines of code thanks to the library's modular architecture.
Notably, we show that a simple one-dimensional cellular automaton can outperform GPT-4 on the 1D-ARC challenge.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper present a new library that can model several types of cellular automata (CAs), ranging from simply Wolfram-style automata and Conway's game of life to continuous and/or complex neural cellular automata. This library is based on JAX and can thus utilize modern computation hardware better, leading to significant performance increases in some cases as the authors show on a few common examples for CA applications.

### Strengths
The issue the library tackles is impactful. CAs play a huge role in various areas of research and having efficient implementations is, of course, key to experimenters. Dramatic improvements in performance have been known to enable a way broader research community in other fields.

The library also unifies various scenarios in which CAs are used that have been fragmented over multiple platforms.

The foundation in JAX also seems to allow for comparatively easy integration with other approaches in the field of AI. (A discussion of that point might be helpful.)

The libraries capabilities are demonstrated on a well-selected range of applications.

Various interesting novel applications are defined and well presented in the paper.

### Weaknesses
The paper stresses some standard library features (like documentation or examples) too much compared to more research-relevant parts.

The performance comparison should be broader. Various libraries exist. Why were only two tested in only very specific cases?

The performance difference to TensorFlow is left unexplained. TF should use hardware acceleration as well, so what is happening there?

The figures are not properly referenced in the text.

Some formal problems exist:
- superfluous ")" in "Section 2)" on page 4
- ill-formatted citation of "Mordvintsev et al." on page 6
- many wrong quotation marks on pages 8-10
- "doesn't" on page 8
- "a NCA" on page 8
- superfluous comma "training set," page 10
- ill-formatted reference to Appendix A on page 10

### Questions
None.

### Soundness
2

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
3

### Summary
This paper presents a software library for cellular automata with GPU acceleration through the JAX library. It demonstrates this new library on MNIST digit classification and the 1D version of the Abstract Reasoning Challenge

### Strengths
The article is clearly written and makes a compelling argument for cellular automata. It demonstrates their utility in image analysis and even reasoning tasks. The use of GPU acceleration through JAX is timely and relevant as a new exploration of GPU acceleration capabilities. As the main contribution is a software library, it provides some experimental comparisons with other open-source libraries.

The secondary contribution of the article are three novel applications of NCA. The most concrete of these is the application to the 1D ARC dataset. This demonstrates that NCA can follow patterns from a small number of examples, allowing them to rival GPT4's in-context learning on visual reasoning tasks. To my knowledge, this is the first study of NCA for reasoning; the demonstration that NCA can do low-data pattern matching, whether or not that is "reasoning", is very interesting.

### Weaknesses
A question I had in reviewing this was its relevancy to ICLR. It isn't the standard ICLR paper, so I consulted ICLR's official CFP, which includes:

+ generative models
+ causal reasoning
+ infrastructure, software libraries, hardware, etc.

I believe the article fits into these categories, however the match to ICLR and the general machine learning literature could be strengthened. For example, these works use NCA in more traditional machine learning settings:

Grattarola, Daniele, Lorenzo Livi, and Cesare Alippi. "Learning graph cellular automata." Advances in Neural Information Processing Systems 34 (2021): 20983-20994.

Tesfaldet, Mattie, Derek Nowrouzezahrai, and Chris Pal. "Attention-based neural cellular automata." Advances in Neural Information Processing Systems 35 (2022): 8174-8186.

Pajouheshgar, Ehsan, et al. "Dynca: Real-time dynamic texture synthesis using neural cellular automata." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2023.

None of these are cited, despite being high-profile studies of NCA in machine learning (NeurIPS, CVPR). As the main contribution of this article is a software library, it would be very valuable to know if these studies or similar ones could be reproduced using CAX. For submission to ICLR, this article could do more to relate the contribution to machine learning.

The second major weakness is the limited experimental study. The studies proposed in section 5 function more as demonstrations of the CAX library than new experiments due to their lack of rigor. Only the 1D-ARC experiment presents quantified results and a comparison with another method. The novel diffusion method presented in 5.1 is only demonstrated on a single example, and the self-encoding MNIST digits experiment in 5.2 is only validated through visual comparison of 1 image per digit. As such, claims like " As shown in Figure 7, the NCA successfully reconstructs MNIST digits on the red face, demonstrating its ability to encode, transmit, and decode complex visual information
through a minimal channel" are not fully supported. Experimental details and full reporting of experimental results are necessary to support such claims. As demonstrations of the CAX library, these examples are interesting, but as experiments, they fall short.

### Questions
Are the mentioned works feasible or simple to implement in CAX? Specifically ViTCA is interesting and could lead to an application of NCA on the full ARC set, but is the attention mechanism possible to implement in CAX?

How does the damage repair example of Figure 5 incorporate diffusion? Do you renoise the "damaged" image or is it simply through training on the diffusion process that it is able to recreate the original image? Could this process be used to train a generative NCA over a distribution of images instead of a single one?

### Soundness
3

### Presentation
4

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
The paper presents a new open-source library for performing Cellular Automata studies written in the JAX framework. The use of JAX allows for significant acceleration of such studies, and the framework reduces the amount of boilerplate code scientists need to write when starting such an investigation. 

Several benchmarks are shown to demonstrate the structure of the software API and even demonstrate a result when compared with common language models.

### Strengths
The paper is very well written and easy to read. The authors have made presentation a clear priority in the paper and should be commended. 

The software itself is also a great idea. Reducing the time it takes for people to start working on these kinds of studies and to do so in an accelerated, modern way is very useful and this work presents a framework doing exactly that.

### Weaknesses
While the paper presents a valuable tool, it does so in a very surface-level way. Most software discussions are in the API demonstration, which shows users how to put it into practice. This is important, but in an academic paper presenting the framework, the framework should take centre stage. Further, benchmarks against common test systems are very welcome in a software paper, but the comparison with GPT-4, while certainly interesting, is more of a research result in and of itself and not directly related to the software. I am sure there is more to the code that replacing numpy with JAX, but that should be laid out and explained in the manuscript.

My biggest concern is that ICLR isn't quite the correct platform for such a paper. I understand the desire for it to go there as it is related to ML but it is, at the end of the day, software. If the paper were to present a novel approach to structuring CA algorithms and packaging that up, it would be a different story. However, this decision is likely up to conference organizers. I can see the benefit of using ICLR as a platform to spread this software and perhaps help a lot of scientists. But from a newness perspective, it is not a breakthrough.

The problem of the performance results presented in the manuscript remains. It is still the correct protocol to run hard and soft scaling tests if the goal is to demonstrate the performance of the software. This will likely mirror the hard/soft scaling tests the JAX team could run, but it would still indicate any algorithmic boosts or slowdowns incurred by your implementation.

As a software paper, however, the focus should be on efficient, usable software rather than just demonstrating its use. This means clear architecture diagrams, algorithmic improvements, and proper scaling tests. Otherwise, it reads more like a brochure or advertisement. Figure 2 is the only figure in the main text highlighting an algorithm and is very generic. Outside this figure, we see tables of results and pictures generated from studies. The utilities section of the paper, for example, is far smaller than the examples sections, where these are the tools that are of interest. From my perspective, how the authors built the software and why this stands out are more important than demonstrating that a CA package can implement CAs.

### Questions
* Why not run proper hard and soft scaling tests in the performance comparison? It is always hard to show few numbers in a speed comparison. 
* Further, is the performance improvement only due to JAX or have you also written the code in a way that further improves parts of the algorithms? If so, that would make a key result in the paper and improve its novelty.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors have created an open-sourced python library called CAX (cellular automata accelerated in JAX) that implements a number of recent developments/experiments in the field of cellular automata as JAX models which allows for highly efficient and parallel computing. The authors also implement tools to customize these implementation for future researchers to run their own experiments in order to have a unified library to be used for efficient CA computations. Furthermore, they implement 3 new experiments with this library to demonstrate these customization tools (a diffusion CA model, an auto-encoding CA model, and neural CA model trained on 1D-ARC tasks).

### Strengths
Originality: While this paper does not necessarliy re-invent new methods, they have created an original and unified tool to be used by practitioners of cellular automata in a highly efficient way for a broad set of possible implementations. This is a tool that will surely accelerate the study of emergence and self-organization in cellular automata.

Quality/Clarity: The paper is clearly written with sufficient background context to motivate the necessity of this tool as well as citing the relevant literature that has sparked recent interest in deeper neural cellular automata architectures.

Significance: Related to the originality of this tool, it is significant for practitioners of this field and lowers the barrier of entry for researchers to produce highly efficient code and run larger scale simulations and experiments. As the field of cellular automata is deeply intertwined with the study of emergence, scaling such simulations is a crucial requirement to push the field to new grounds. With such a tool, such experiments become much more feasible and cheaper for researchers.

### Weaknesses
 - the performance increases plotted in figure 3 I feel are not sufficiently demonstrating the utility of such a library. I say this as a user of JAX and PyTorch and know that there are many performance increases when using JAX, and so there needs to be a much more comprehensive case being made here that JAX is actually introducing large speed ups. This is also increasingly important as there doesn't seem to be a massive speed up in the "Growing cellular automata" experiment, so perhaps the authors should compute performance changes for a larger set of experiments. (For example for the [self-organizing textures](https://distill.pub/selforg/2021/textures/) experiment, or [cellular automata controlling cartpole](https://arxiv.org/abs/2106.15240) experiment.

- as someone that has had to write JAX code for my own custom CA implementations, it would be great if the appendix included some annotated code that explains how efficient JAX implementations can be written. I know that curious readers can always read the code on github, and there are some examples shown such as on line 281-289 as well as the example notebook in the appendix (but it has minimal comments), but it would be extremely helpful for new programmers to understand the thought process for writing such a library. This is doubly important because when trying to implement this library for custom experiments, a certain degree of programming in JAX will be required. This is possibly slightly outside the scope or responsibility of the authors, but I think it would go a long way for allowing researchers to adopt this library if there were tutorials or detailed annotations of code that explain this process (I know for myself this would have been very helpful a few years ago).

- I very quickly tried to run one of the colab notebooks for the 1D-ARC tasks and had problems with importing. I did not test with all the notebooks but this should probably be double-checked across the board. I recieved two errors:
   - (on the second cell: `%pip install "cax[examples] @ git+https://github.com/879f4cf7/cax.git"`): after installing most packages, I recieved the following message: `ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
gcsfs 2024.10.0 requires fsspec==2024.10.0, but you have fsspec 2024.9.0 which is incompatible.`
    - (on the third cell: `from cax.core.update.residual_update import ResidualUpdate`):
~~~ 
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-3-7bc79b5c20c3> in <cell line: 11>()
      9 from cax.core.perceive.depthwise_conv_perceive import DepthwiseConvPerceive
     10 from cax.core.perceive.kernels import grad_kernel, identity_kernel
---> 11 from cax.core.update.residual_update import ResidualUpdate
     12 from flax import nnx
     13 from tqdm.auto import tqdm

1 frames
/usr/local/lib/python3.10/dist-packages/cax/core/update/mlp_update.py in <module>
      5 import jax.numpy as jnp
      6 from flax import nnx
----> 7 from flax.nnx.nnx.nn import initializers
      8 from flax.nnx.nnx.nn.linear import default_kernel_init
      9 

ModuleNotFoundError: No module named 'flax.nnx.nnx'
~~~

### Questions
I don't have any major questions regarding this package other than the reason for the import crashes in the notebook I listed in the weaknesses.

### Soundness
4

### Presentation
3

### Contribution
4
