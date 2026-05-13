# KernelWarehouse: Rethinking the Design of Dynamic Convolution

- Decision: Reject
- Scores: 5, 6, 8, 5, 5, 6

## Abstract
Dynamic convolution learns a linear mixture of $n$ static kernels weighted with their input-dependent attentions, demonstrating superior performance than normal convolution. However, it increases the number of convolutional parameters by $n$ times, and thus is not parameter efficient. This leads to no research progress that can allow researchers to explore the setting $n>100$ (an order of magnitude larger than the typical setting $n<10$) for pushing forward the performance boundary of dynamic convolution while enjoying parameter efficiency. To fill this gap, in this paper, we propose ~\textit{KernelWarehouse}, a more general form of dynamic convolution, which redefines the basic concepts of ``kernels", ``assembling kernels" and ``attention function" through the lens of exploiting convolutional parameter dependencies within the same layer and across neighboring layers of a ConvNet. We testify the effectiveness of KernelWarehouse on ImageNet and MS-COCO datasets using various ConvNet architectures. Intriguingly, KernelWarehouse is also applicable to Vision Transformers, and it can even reduce the model size of a backbone while improving the model accuracy. For instance, KernelWarehouse ($n=4$) achieves $5.61\%|3.90\%|4.38\%$ absolute top-1 accuracy gain on the ResNet18$|$MobileNetV2$|$DeiT-Tiny backbone, and KernelWarehouse ($n=1/4$) with 65.10\% model size reduction still achieves 2.29\% gain on the ResNet18 backbone.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel method for dynamic convolutions, i.e. a method where the convolutional kernels used depend on the input tensor. This idea is typically achieved by having an attention head (e.g. akin to squeeze-and-excitation networks) to provide some linear coefficients that are then used to linearly combine some kernel basis to build the convolutional kernel. The proposed method breaks the kernel into pieces (e.g. across the channel dimension), each piece is constructed in the way described above, and then the pieces are put together to form the kernel. The authors propose some strong sharing methodology in which the kernel basis are shared by the different "kernel pieces" are across layers. The authors also propose a new way of computing the linear coefficients and some initialization strategy that are key to good performance. Experiments show improvements on imagenet, detection and segmentation for a number of convolutional architectures.

### Strengths
The paper is clearly motivated and it is easy to understand the differentiation with respect to prior work.

The experimental results are comprehensive, covering several architectures, classification, detection and segmentation, has good ablations and even runtimes. I appreciate for example the inclusion of convnext-tiny and runtime measurements.

The paper is not trivial from a technical standpoint. There seems to be a significant amount of effort and experimentation involved into making the idea work.

Results show high performance and ablations show the need for the different components.

### Weaknesses
My main issues are: 1) Architectures have evolved a lot from ResNet18/ResNet50, both in the research as well as the industry areas. 2) Latency is heavily affected. Specifically:

Experiments with ResNet or even MobileNet feel a bit out of sync with the current literature in terms of architecture design. I appreciate the inclusion of convnext-tiny and, while for imagenet results show only moderate gains, there are some clear gains for object detection and segmentation. Besides convolutional architectures, does this kind of technique work for transformers at all? The core idea of dynamic convolutions, which is to generate kernels based on the input, seems conceptually applicable to the weight matrices within transformer layers, particularly in the value and MLP projection matrices. It is unclear if the proposed method can be extended to these architectures, and this limits the impact of the work.

Latency might be partially due to the lack of optimized CUDA kernels for certain operations, but not completely, as CPU also shows similar issues. I believe the sequential nature of the attention mechanism and the need to put together the kernel are important factors contributing to the latency degradation. These issues are very hard to solve for dynamic convolutions, definitely not just restricted to the current work. The specific operations that contribute to the latency, such as the attention mechanism and the kernel assembly, need to be analyzed in more detail. It would be beneficial to have a breakdown of the runtime cost for each of these operations to better understand the bottlenecks.

Some of the design choices are key to making the proposed warehouse idea work, e.g. the initialization, temperature and attention design. Do these components work when are combined with other dynamic convolution approaches or is there something in their design that makes them specific to the kernel warehouse idea? The interplay between the kernel partition, warehouse sharing, and the proposed attention mechanism is not fully explored. It is not clear if the performance gains are due to the specific combination of these components or if they can be used independently with other dynamic convolution methods. It is also unclear if the initialization strategy and temperature parameters are tuned for the specific architecture or if they are generalizable. Overall, it feels like the proposed method improves upon prior work on dynamic convolution, but still is not clear in which sense it offers some optimal trade-off.

Comments that might help with the clarity of the paper, no need to reply:
"Kernel partition" could include some information on how the partition is done. I believe it is across the channel dimension but this only becomes clear later.

Tracking the explanations in "Parameter Efficiency and Representation Power" requires a lot of patience and attention. I believe some table with example parameterizations or some exemplification in addition to the current explanations could help the reader a lot.

It would be nice to have some justification for Eq. 3. Right now it looks like the authors came up with it from thin air, but I'm sure there was a motivation or inspiration.

### Questions
See comments above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes KernelWarehouse as a more general form of dynamic to improve the performance and efficiency of ConvNets. The paper rethinks the basic concept of kernel partition and warehouse. The effectiveness of proposed componets is investigated in detail through the comparison with other attention-based methods in image classification, object detection and instance segmentation.

### Strengths
- The paper investigates dynamic convolution in detail with thorough experiments including the comparison with other sota methods in different downstream tasks.
- The ablation of key parameters of the proposed method is given in detail. This paper is written well with organized tables and figures.

### Weaknesses
 - The improvement of KernelWarehouse is limited as shown in Table1 and Table4 considering two models with the same parameter (+ ODConv (4×) vs + KW (4×)), which can not show the advantage of KernelWarehouse in terms of efficiency and performance.
- The convolutional parameter budget $b$ is an important parameter, how to choose an appropriate parameter of the downstream task. The effect of $b$ on image classification, object detection and instance segmentation is different from the experiment.

### Questions
Listed above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents KernelWarehouse, a more general form of dynamic convolution that enjoys improved parameter efficiency and expressivity. The paper evaluates the proposed method across several convolutional backbones on MS COCO and ImageNet, consistently leading to improvements over existing approaches. The paper provides an extensive number of ablations corroborating many of the design choices in the proposed method.

### Strengths
Altogether I believe this is a very strong submission with some flaws in its presentation. It is a very pleasant read with interesting insights, ablations, visualizations and evaluations. This paper has the potential to have a big impact.

### Weaknesses
To my best assessment, this paper does not have any big weaknesses. However, there are a few things regarding the presentation that would improve reading and the clarity of the proposed method.

* The proposed method is simple, yet, in its current form, the paper presents it in a somewhat convoluted manner. I would encourage the authors to restructure the method section (Sec. 3) such that it is presented in an easier way. I want to emphasize that it is not that the paper is not understandable. I just believe that this would help digest the idea in the paper and therefore, probably improve its impact.

  Things that could help:

  > Present the method as an Algorithm.

  > Add an additional figure in which the different components are better illustrated --In image 1, it is not clear how Assemble is done, for example--.

* I strongly encourage the authors to change the name of NAF. The name New Attention Function sounds somewhat odd to me. I would encourage the authors to use a name that describes what the proposed function is doing.

### Questions
No questions at this point.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes to improve the previous existing works on dynamic convolution by using kernel partition (dividing the convolution kernel into disjoint parts), sharing parameters across diferent layers of the network and by using a “new attention function”.

### Strengths
- the proposed approach is tested on several computer vision tasks and datasets 
- the results on improving the parameter efficiency and improving the recognition performance look promising

### Weaknesses
Weaknesses*
- The work proposes quite incremental contributions over the dynamic convolution, however, the biggest concern I believe is related to the future use in practice of the proposed version for dynamic convolution. The proposed approach significantly impacts the computational costs in a negative way which can be an important bottleneck for future use in practice. Specifically, as presented in Table 10,  the speed on GPU is reduced from 322.7 to 178.5 images/second (if we compare a similar number of parameters of the model between dynamic convolution and the proposed approach). This is a significant limitation of the approach, which adds even more computational costs (on top of already negative impact of the dynamic convolution over the standard convulsion). Also the memory requirements for training and inference can be a potential limitation, I think the work should also report the memory comparison.

-It looks that a significant gain comes from the  “new attention function” (without this, the work is underperforming the dynamic convolution ), the results are not reported also when using  the “new attention function” in the dynamic convolution framework.

-Not clear why the parameters are decreasing when reducing the sharing levels (Table 6 and 7), I was expecting the opposite.

-The improvements for ConvNeXt look quite marginal, it looks that the approach can have a scalability issue (basically not that useful for larger models)

### Questions
See above my concerns

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a dynamic convolution which can extends the choice of candidates from typical n < 10 to n > 100, while not suffering from the explosion of parameters. The proposed method, KernelWarehouse, can use large kernel numbers when fit a desired parameter budget. This is achieved by exploiting convolutional parameter dependencies within the same layer and across successive layers. Experiments on ImageNet and COCO validate the idea and show significant improvement over baselines.

### Strengths
+ Dynamic convolutions, like CondConv, suffer from the explosion of parameters when increasing the kernel choices. This paper proposes a way to alleviate this by exploiting convolutional kernel and layer parameter dependencies. It is a new way to formulate dynamic convolution.

+ Decent improvements are oberseved with different network architectures compared with baselines.

+ Instead of only reporting the parameters, this paper also reports the real runtime in Table 10. Although the proposed method has some limitations, it is still meaningful to report these numbers.

### Weaknesses
 - The paper writing needs to improve. The introduction only has two major paragraphs and is really hard to parse and digest.

- Although the proposed method could save parameters, it actually requires more time to run (see Table 10), which makes the resulted model far from real deployment. The runtime is significantly slower than standard dynamic convolution, which is a major drawback for practical applications. The speed bottleneck seems to stem from the dense attentive mixture and assembling operations, which are not optimized for inference speed.

### Questions
- It is counter-intuitive to see KW (4x) performs worse than KW (2x) with additional parameters in Table 1. Could the authors elaborate on this?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors proposed a new design of dynamic convolution named KernelWarehouse. As a more general form of dynamic convolution, KernelWarehouse can improve the performance of modern ConvNets while enjoying parameter efficiency. Experiments on ImageNet and MS-COCO datasets show its great potential.

### Strengths
The proposed method is simple yet effective. It significantly increases the number of dynamic convolutions (>100) while maintaining the efficiency of the network. It is clearly stated how the proposed method is defined and how it works.

### Weaknesses
The proposed method claims to achieve the SOTA performance over various vision benchmarks. While it outperforms previous ConvNets, the SOTA models are now mainly transformer-based models. There is no comparison/discussion between the proposed method and transformers.

### Questions
In Table 1, why KW 4x is lower than than KW 2x? Any study on this?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
