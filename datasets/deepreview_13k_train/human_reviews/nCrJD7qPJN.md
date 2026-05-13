# Distilling Dataset into Neural Field

- Decision: Accept
- Scores: 6, 5, 6, 5

## Abstract
Utilizing large-scale datasets is essential for training high-performance deep learning models, but it also comes with substantial computation and storage costs. To overcome these challenges, dataset distillation has emerged as a promising solution by compressing large-scale datasets into smaller synthetic versions that retain the essential information needed for training. This paper proposes a novel parameterization framework for dataset distillation, coined Distilling Dataset into Neural Field (DDiF), which leverages the neural field to store the necessary information of large-scale datasets. Due to the unique nature of the neural field, which takes coordinates as input and output quantity, DDiF effectively preserves the information and easily generates various shapes of data. Beyond the efficacy, DDiF has larger feature coverage than some previous literature if same budget is allowed, which is proved from the frequency domain perspective. Under the same budget setting, this larger coverage leads to a significant performance improvement in downstream tasks by providing more synthetic instances due to the coding efficiency. DDiF demonstrates both theoretical and empirical evidence of its ability to operate efficiently within a limited budget, while better preserving the information of the original dataset compared to conventional parameterization methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a parameterization-based dataset distillation method called DDIF. The authors enhance traditional parameterization-based methods by introducing a neural field representation. According to the authors, their contributions lie in the theoretical analysis of neural fields for parameterized dataset distillation and the performance gains achieved by their proposed method. The experiments conducted on ImageNet subset and cifar10/100 demonstrates the outstanding performance of DDiF as stated in this paper. Besides the performance, the authors claim that the advantage of their DDiF is the coding efficiency introduced by their neural field representation. Additionally, DDiF is well-suited to datasets with varying resolutions due to its resolution-invariant nature.  The proposed DDiF has a good potential to boost the development of dataset distillation. However, there exists some unclear part of the proposed method.

### Strengths
1. The idea of leveraging neural field for dataset distillation is innovative. 

2. The performance of the parameterized dataset distillation is unexpectedly high in the extreme scenario with IPC = 1.

3. The authors conduct a lot of experiments including cross-architecture experiments and abaltion studies on different distillation loss functions. Also, the performance of DDiF is outstranding.

### Weaknesses
I believe this paper has the potential to be a milestone in dataset distillation. However, it is difficult to follow, which raises several concerns about the proposed method.


1. The paper is not easy to understand:

(a) The algorithm 1 does not tell the most significant improvement introduced by the DDiF, as it is very close to a standard parameterization-based method. What part makes the DDiF outstanding? The design of the decoder network? or the Eq(2).

(b) I cannot understand the coding efficiency mentioned in line 188. While I recognize the resolution-invariant nature, I see no evidence supporting an advantage in coding efficiency. I hope the authors could provide numerical results here instead of rewriting the paragraph from line 188 to 204.

(c) This paper is 27 pages long, yet the authors should provide more details about their experiments. Important settings are missing, such as the calculation of the distillation budget, the architecture of the decoder network, the number of parameters, the training datasets, and specific training details. Additionally, the evaluation metrics for the reported performance are unclear—how many times were the evaluation experiments repeated?

(d) How should I interpret the sentence in line 370: ‘We utilize trajectory matching (TM) for 128 resolution and distribution matching (DM) for 256 resolution’? Why is the performance at 256 resolution significantly lower than at 128 resolution?


2. What is the purpose to repeat Theorem 1(Novello, 2022) and theorem 2 here? I think the reader would like to have an explanation on the outstanding performance of the neural field, instead of a relatively correct theorem and proof.

3. One critical issue with parameterized dataset distillation is the neglect of the decoder network. Only the encoded patterns are included in the distillation budget, while the decoder network is excluded. That explains the greater advantages of parameterized dataset distillation with IPC = 1, due to the marginal information carried by the decoder network. Such advantages will be smaller when ipc increases.

4 Followed by question 3, why did the authors neglect the experiments with IPC=50? Is it due to the performance degradation of parameterized dataset distillation in higher IPC?

### Questions
Most of my questions are listed in the weakness part. The other main concern is how to ensure a fair comparison across parameterized dataset distillation methods. As the decoder network will not be counted into the distillation budget, the architectures, number of parameters, and the training dataset will heavily influence the performance of parameterized dataset distillation. If we could not constrain the decoder network well, the easiest way to boost performance would be using a larger network, better architecture, and training the network with more datasets to boost its generalization ability.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- This paper proposed using Neural Fields to parameterize distilled datasets (DDiF)
- The basic idea is to replace each distilled image by a neural field which implicitly defines the image (by evaluating the field at grid points)
- The method gets performance gains by reducing the parameter count per images (provided each neural field is small enough), so you can you use more images
- The method is robust to different dataset distillation loss choices

### Strengths
- The method is straightforward and is easily compatible with existing DD algorithms.
- Good experimental results, particularly on non-image domains (with high dimensionality, where this method would have the greatest wins)
- Interesting results with cross-resolution generalization, which is a new idea in dataset distillation (although I have questions about the evaluation - see the questions section)

### Weaknesses
 - I don't think the theoretical analysis is particularly enlightening. The theoretical analysis can be boiled down to "if you have more degrees of freedom, then you can get lower distillation loss, and DDiF has more degrees of freedom than FreD since DDiF can modify the frequencies as well as their coefficients, whereas FreD can only modify the coefficients". However, this theoretical analysis is rather meaningless as adding the ability to control the frequencies (and the biases) adds more parameters. This analysis is only useful if you can fix the number of free parameters between FreD and DDiF. I understand this is analysis is difficult and can really only be verified experimentally (which the authors have done), but this caveat with the theoretical analysis needs to be mentioned.
- There is no mention about the additional cost of evaluating the neural field at the coordinate points. The additional cost of evaluating the field at all datapoints could very significant, especially for high-resolution/higher dimensional data, but is not discussed in the paper. It would be useful to compare the additional runtime requirements, compared to directly parameterizing the images/data themselves, particularly for the high-resolution data.

### Questions
- See weaknesses
- For the resolution generalization experiments, can you additionally report the performance of downsampling the full dataset down to the reduced distilled dataset resolution (as opposed to upsampling the distilled datasets, as you have presented). If there is better performance by downsampling the original data, then there would not be a convincing argument why one should upsample the distilled dataset
- Is it not possible to upsample FreD distilled images by just evaluating at more points (like with equation 6)? Did the authors use this method for the upsampling experiments? If not, then this would be very important to make the comparison fair.
- Can you also report for the performance of vanilla dataset distillation performance, with the same number of distilled images in table 1,2,3? If I understand correctly, right now you only present the performance matching the number of parameters, but it would a useful datapoint to consider what performance hit is given by parameterizing with DDiF as opposed to directly parameterizing the images
- Is it possible to produce a curve showing the effect of neural field architecture choices on the performance? For example, given a fixed parameter budget, how does the width of the neural field (for example), affect the distillation performance?

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
4

### Summary
This paper proposes to use a neural field framework to encapsulate and learn a dataset, i.e. dataset distillation. The neural field is prompted by coordinates to generate images, and can produce at different resolutions. The experiments show very promising results.

### Strengths
+ This paper proposes a very interesting extension of parameterization for dataset distillation, and uses a neural field to compress information.
+ The experimental results show very promising performance on challenging datasets
+ The generalization on different resolution capability is intriguing

### Weaknesses
 - The paper's theme is on parameterization of image datasets, yet the introduction section rarely talks about the relevant topic and works to distinguish this paper out. I think the authors should specifically discuss and compare with [1, 2, 3, others] principal-wise to help the reader understand how the progress is made in DD parameterization and the delta in this paper.

- In the experiment section, I'd encourage the authors to add a table row showing the number of images (not ipc budget) used for re-training. Reparameterization methods tend to have more images, which I think is fine, but needs to be explicitly mentioned for clarity.

- One critical point in the experiment: is neural field better than simple basis decomposition used in RTP[1]? In the previous literature, the bases-coefficient decomposition seems to outperform HaBa quite a lot on simpler datasets. It should not be too hard to use RTP's decomposition method (bases + coefficient) and a DD loss that this paper is using (e.g., trajectory matching loss), and run experiments on the ImageNet benchmarks to perform a direct comparison. This will provide more support that neural fields can work very well and outperform the previous SOTA parameterization.

- How heavy is the data augmentation?

### Questions
See above. I think the paper is very interesting. If the authors addresses my questions above, I'd like to consider further recommendation of this paper.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
A neural field-based parameterisation learned to encode the synthetic dataset for the downstream model training termed Distill Dataset into Neural Field (DDiF), is proposed in this submission. Comparied with the line of research that directly stores the synthetic dataset, a few neural fields parameterised by the neural networks are learned to yield pixel values with feed-in coordinates in the inference time, following the principle from FreD. DDiF is empirically tested on dataset condensation benchmarks especially in the image per category 1 and 10 setting on ImageNet with noticeable improvements.

### Strengths
1. The idea is simple to follow and easy to implement. 
2. The experiment results demonstrate the efficiency of neural field embedding but some concerns may be raised that I will point out later. 
3. The writing is clear and easy to follow.

### Weaknesses
1. The theoretical analysis concludes that DDiF has lower synthetic data loss than Fred due to the former feasible space being larger in Theorem2. The main reasons are based on Observations 1 and 2. However, there is no clear clue about the source of the observation. 

2. The budget comparison is not given. Since the DDiF architecture details are not clear, there is no direct comparison of the cost of saving the neural field and the synthetic dataset. Specifically, the number of parameters in the neural field, the number of decoded instances per class, and the overall storage requirements are not clearly detailed, making it difficult to assess the practical memory footprint of DDiF compared to storing raw pixel data or other parameterizations.

3. I'm not sure the algorithm can be generalised to large IPC settings since in most experiments, there are only 1 and 10 IPCs, even for Cifar10 and CIf100 in the appendix. The performance of DDiF in higher IPC settings, such as 50 or 100, is not demonstrated, which is crucial for practical applications where a larger number of synthetic samples per class might be needed.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2
