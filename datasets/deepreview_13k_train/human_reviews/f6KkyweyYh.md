# Biological Sequence Analysis Using B ́ezier Curve

- Decision: Reject
- Scores: 5, 6, 3, 6

## Abstract
The analysis of biological (e.g., protein and DNA) sequences is essential for disease diagnosis, biomaterial engineering, genetic engineering, and drug discovery domains. Conventional analytical methods focus on transforming sequences into numerical representations for applying machine learning/deep learning-based sequence characterization. However, their efficacy is constrained by the intrinsic nature of deep learning (DL) models, which tend to exhibit suboptimal performance when applied to tabular data.
An alternative group of methodologies endeavors to convert biological sequences into image forms by applying the concept of Chaos Game Representation (CGR). However, a noteworthy drawback of these methods lies in their tendency to map individual elements of the sequence onto a relatively small subset of designated pixels within the generated image. The resulting sparse image representation may not adequately encapsulate the comprehensive sequence information, potentially resulting in suboptimal predictions.
In this study, we introduce a novel approach to transform biological sequences into images using the Bézier curve concept for element mapping. Mapping the elements onto a curve enhances the sequence information representation in the respective images, hence yielding better DL-based classification performance.  We employed three distinct protein sequence datasets to validate our system by doing three different classification tasks, and the results illustrate that our Bézier curve method is able to achieve good performance for all the tasks. 
For instance, it has shown tremendous improvement for a protein subcellular location prediction task over the baseline methods, such as improved accuracy by 39.4\% as compared to the FCGR baseline technique using a 2-layer CNN classifier. Moreover, for Coronavirus host classification, our Bézier method has achieved 5.3\% more AUC ROC score than the FCGR using a 3-layer CNN classifier.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new method to transform biological sequences, like protein or DNA sequences, into images using Bezier curves. This allows applying deep learning image models to analyze the sequences. The authors mention that existing/traditional methods convert sequences into numerical features or use Chaos Game Representation (CGR) to create images. But these have limitations like sparsity, high dimensionality, poor representation of sequence information in images.

The proposed method maps each element (amino acid, nucleotide) of a sequence onto a Bezier curve to create an image. Multiple points on the curve represent each element. This captures more information and patterns in the image compared to traditional CGR-based methods where elements map to fixed pixels. Experiments on three protein datasets for classification tasks show the Bezier method outperforms baselines like FCGR and RandomCGR images, and numerical embedding methods.

In the results, the authors demonstrate that for subcellular protein localization dataset, Bezier images achieve 40% higher accuracy than FCGR using CNNs. Furthermore, cluster visualization and histograms also show Bezier embeddings preserve structure better. Overall, the paper demonstrates biological sequence analysis benefits from transforming sequences into images via Bezier curves before applying deep learning models.

### Strengths
+ The paper describes a new idea of using Bezier curves to create visual representations of biological sequences. 
+ The results also demonstrate improved performance over baseline methods on several protein sequence classification tasks.

### Weaknesses
 - In its current format, the paper may not be a good fit for ICLR audience, and the featurization is specific to a small domain of problem.
- The demonstrated evaluation is limited to only protein sequence datasets related to subcellular localization, virus hosts, etc. It was not clear to me how this idea generalizes to broader range of biological problems.

### Questions
1) How much hyper-parameter optimization is needed for this approach? Are these B'ezier features easy to generate
2) Can this idea be generalized to other areas beyond biological approach? Please comment on the generality of the featurization and fit with ICLR audience.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an approach to transform biological sequences into images using Bezier curves for element mapping. A core motivation is enhancing the representation of sequence information in the generated images, as traditional methods like CGR tends to map elements to a limited set of pixels. Through experiments on three protein sequence datasets for tasks including subcellular localization and host prediction, the authors demonstrate the superiority of the proposed Bezier curve encoding method, with significant gains in accuracy over baselines. 

Additionally, the smooth interpolation of control points enabled by Bezier curves is cited as improving interpretability of the visualizations. Overall, encoding sequences as Bezier curve images appears promising as it provides richer representations that translate to markedly improved performance on downstream classification tasks.

### Strengths
- The proposed sequence-to-image transformation technique is novel and a key contribution that could prove widely applicable and beneficial in the field. The simple and straightforward image generation process based on standard Bezier curve equations is clearly explained.
- The authors introduce careful methodological choices; e.g., introducing controlled randomness via deviations to reveal hidden patterns, to overcome limitations of fixed mappings in CGR.
- The authors demonstrated the usefulness of their information-rich curve-based image representations by validating on multiple protein sequence datasets for subcellular localization task. The proposed approach substantially improved classification performance over baseline CGR, highlighting the benefits of the Bezier representation. In addition, the authors also explored the potential of the smoother Bezier curve interpolations in improving interpretability compared to sparse CGR images.
-encoding method is agnostic to the choice of downstream classifier, allowing flexible integration with existing pipelines.
- The proposed approach could generalize well to other types of biological sequences like DNA beyond tested protein use cases.

### Weaknesses
 - The proposed representations might not encode signal about sequential information as amino acid order is not explicitly encoded, which may prove to be necessary in some usecases. Specifically, while the method captures the presence of amino acids, the spatial arrangement of these amino acids is not directly reflected in the image. This could be problematic in cases where the order of amino acids is crucial for the protein's function or structure, such as in the formation of specific secondary structures or binding sites.
- Limited ablation studies were performed to analyze the impact of key parameters like number of control points and deviations. The lack of a systematic analysis makes it difficult to understand the sensitivity of the method to these parameters and to determine the optimal values for different datasets or tasks. For example, it is not clear how the number of control points affects the granularity of the representation, or how the magnitude of the deviations influences the information captured in the image. 
- (minor) There is a notable computational overhead to the proposed approach, although at a benefit of improved performance. While the authors claim the method is fast, the overhead compared to simpler methods like CGR, which directly maps elements to pixels, is not negligible. This overhead could be a concern when dealing with very large datasets or when computational resources are limited.

### Questions
- How does the performance scale with much longer input sequences? At what sequence length does the image encoding become unwieldy?
Opensourcing the code will help reproducibility efforts and also drive adoption of this approach.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a methodology for encoding protein sequences as images in a 2D plane with the use of Bézier curves. Protein and DNA sequences have been mapped into images in the past to take advantage of machine learning methods, including CNNs, and the proposed approach brings a novel transformation that preserves meaningful biological information.

### Strengths
* The paper addresses an important problem, which is the representation of biological sequences.
* The results indicate that the proposed approach has clear advantages over prior methodologies, both quantitatively and qualitatively.
* The benchmarking exercise is extensive. The paper evaluates various architectures and tests several baseline approaches in different datasets.

### Weaknesses
 * From the machine learning perspective, the paper does not have a significant contribution. While the problem is important and the results are very promising, the technical novelty is limited. Perhaps this piece of work can be better appreciated by the bioinformatics community.
* The proposed approach is not a learning algorithm, where the representation is learned automatically. Instead, the approach is a transformation of individual data points into a different representation, which is shown to be more effective for machine learning algorithms. 
* The resulting images are not presented, even though the manuscript claims that these are more interpretable and meaningful. A qualitative comparison of how the images look like with respect to previous attempts for a given sequence (or a portion of it), would be helpful.
* The paper devotes much space in tables with dataset and methods descriptions. This space could be better utilized with different analysis and other results.

### Questions
Unfortunately, I don't think the paper is a good fit for this venue. This does not mean that the paper is incorrect or has major mistakes, it is just that the audience may not be the correct community to present and discuss its true value. The idea is great, and I encourage the authors to consider submitting to a bioinformatics journal or similar, where the machine learning contribution is not expected to be the central contribution of the manuscript.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors describe an algorithm for representing sequences of amino acids as a collection of Bezier Curves in the plane, and show that using these as inputs for classification tasks is superior to using other 1D and 2D representations of the sequence.

### Strengths
- well written
- extensive exploration of different representations of their Bezier curve method

### Weaknesses
 - For a paper about 2D images, there are very few images. The algorithm is complicated enough to warrant at least one example where the authors illustrate the creation an image from a simple sequence. Moreover, they could compare this to other image production methods and demonstrate why they think their images are superior. Specifically, a visualization showing the Bezier curve generation process for a sample sequence, including the control point selection and curve drawing, would be very helpful. It's not clear how the method compares to other sequence-to-image techniques in terms of preserving sequence information in the image representation.
- Train time is a rather weak method for understanding the compute requirements of each method, it would be better to report training flops, and even scatter plot by training flops. Reporting the number of parameters for each model and the FLOPs required for a single training epoch would provide a more detailed understanding of the computational cost. Additionally, a scatter plot of training FLOPs vs. accuracy would allow for a better comparison of the efficiency of each method.

### Questions
- What about a transformer on the sequence itself, rather than just a ViT on images? Seems like an important comparison to make.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
