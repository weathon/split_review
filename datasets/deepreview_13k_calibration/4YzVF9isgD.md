# HyperFace: Generating Synthetic Face Recognition Datasets by Exploring Face Embedding Hypersphere

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
\vspace{-10pt}
Face recognition datasets are often collected by crawling Internet and without individuals' consents, raising  ethical and privacy concerns. Generating synthetic datasets for training face recognition models has emerged as a promising alternative. However, the generation of synthetic datasets remains  challenging as it entails adequate inter-class and intra-class variations. While advances in generative models have made it easier to increase intra-class variations in face datasets (such as pose, illumination, etc.), generating sufficient inter-class variation is still a difficult task. In this paper, we formulate the dataset generation as a packing problem on the embedding space (represented on a hypersphere) of a face recognition model and propose a new synthetic dataset generation approach, called HyperFace. We formalize our packing problem as an optimization problem and solve it with a gradient descent-based approach. Then, we use a conditional face generator model to synthesize face images from the optimized embeddings. We use our generated datasets to train face recognition models and evaluate the trained models on several benchmarking real datasets. Our experimental results show that models trained with HyperFace achieve state-of-the-art performance in training face recognition using synthetic datasets. Project page: \href{https://www.idiap.ch/paper/hyperface}{https://www.idiap.ch/paper/hyperface}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents an approach to generate a synthetic face dataset for face recognition problem by formulating it as an optimization problem and solve it iteratively via gradient descent method to obtain optimized embeddings. Then the synthesize face images can be generated using pre-trained face generator models from those embeddings.
The experiment shows that the models trained with the proposed synthetic datasets can achieve SOTA performance.

### Strengths
1. Well-formulated optimization problem: The paper effectively defines the optimization problem for generating high-quality synthetic face recognition datasets.
2. Efficient solution: The proposed solution is not only effective but also computationally efficient.
3. Extensive experiments: The paper presents comprehensive experiments on various synthetic datasets to validate the approach.
4. Ethical considerations: The authors acknowledge potential ethical concerns, such as identity leakage, demonstrating a responsible approach to AI development.

### Weaknesses
1. Limited scale: While the experiments on datasets with up to 30K identities provide valuable insights, evaluating the method's performance on significantly larger datasets is crucial.  Datasets with 100K and 300K identities would be particularly informative as they would reveal how the method scales and whether performance degrades with increased identity count and potential data noise. This would provide a more comprehensive understanding of the method's robustness and real-world applicability.
2. Narrow focus:  The paper's focus on improving inter-class variation is important, but expanding the scope to address intra-class variability would significantly enhance its impact. Specifically, exploring how the method handles variations in pose, illumination, and expression within the same identity would be valuable. Additionally, investigating the method's robustness to occlusions or image quality degradation would further strengthen the evaluation and demonstrate its potential for real-world scenarios.

### Questions
1. What is the computation resource and time needed to generate larger scale datasets, e.g. n_id = 30k or more?
2. It would be interesting to see if we can use the FR model trained by the proposed synthetic dataset to build another good synthetic dataset

### Soundness
3

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
Interesting paper that proposes some embedding optimisation in the latent space of a pretrained face recognition model. The optimised embeddings are used for generating facial images using a recently proposed generative model, and then the generated images for training a face recognition model. I liked the novelty and simplicity of the proposed approach yet there are a few issues that possibly limit the impact of the proposed work. See my questions below.

### Strengths
- Interesting idea to perform the optimization in the latent space of a discriminatively train face recognition model
- Well written paper, easy to read and understand
- Decent experiments although lacking in some respects

### Weaknesses
It could be that the method has significant limitations in terms of scaling the number of images that can be generated. The impact of the work has not be fully demonstrated. See also my questions below.

### Questions
1. Are both reference embeddings and gallery embeddings generated from StyleGan?  In this case the only difference between them is that the Gallery embeddings are not updated during optimisation?
2. Are all methods in table 1 trained in the same way using the same face recognition model and training pipeline?
3. Fair comparison in table 1 should use 50 images per identity for your method
4. It’s important to compare against SOTA (e.g. DCFace) at scale (i.e. increasing the number of identities). Specifically, table 3 should not be just an ablation study but you need to show that your method scales favorably and/or outperforms SOTA as the number of training images increases. 
5. In general, how the method scales has been poorly studied (there’s only 1 result in table 3). Scaling Dataset Generation section discusses computational issues that may arise from scaling the dataset but does not provide concrete numbers (e.g. a figure showing training time vs dataset size), conclusions or practical solutions (i.e. a solution is proposed but not put in practice)
6. Baselines: what about direct comparison with arc2face? Since they don’t have to solve your optimisation problem, they can generate a lot more images for training

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper propose an interesting solution for synthetic face recognition, i.e. optimizing the hyperspace for generation. The solution is to treat the face generation as a packing problem on the embedding space. The optimization goal is to find feature embedding that is of high inter-class variation. Finally this paper adopt a pretrained generation method to generate the dataset.

### Strengths
1. This paper is good in writing and has a solid mathematical formulation.

### Weaknesses
1. [Major] I don't see the motivation to convert the face generation problem as a packing problem on the embedding space from the storytelling, Please provide some related empirical/ theoretical works regarding why the packing problem could be of use for SFR.

2. [Major] This paper adopts Arc2Face for final image generation. However, (1) The ablation study doesn't show the advance of directly sending random feature embedding (each embedding is ensured by restricting the similarity below a certain threshold, e.g. 0.3) to Arc2Face; (2) The comparison with Arc2Face is missing in Table 1, additionally the experiment is marginal better than DCFace. The average performance is 89.876 which is similar to DCFace and dramatically lower than Arc2Face. 

3. [Major] In Section 'Solving the HyperFace Optimization', the authors choose AdamW for the optimization solution. However, the other alternative optimization methods are not specified and compared in this paper.

4. Another concern is that the proposed method generates more images(640k) to produce similar performance to DCFace (500k).

5. large intra-class variations can not be observed in the visualization section.

6. [Minor] Notation is not specified in fig 1.2. Please provide more description for the reader to understand the mathematical formulation and the whole generation process. For example, what does reference embedding stand for, I understood it only when I saw the 'Image Generation' section. And what is X_{g}?

7. Please give some detailed pseudo-code for the entire process(training/ generation) for the reader to understand the method.

### Questions
Please see the weakness. 

If the authors address the concerns well, I am happy to raise my score.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a synthetic data generation method for FR that aims to improve inter-class variation compared to existing methods. The approach utilizes the embedding space of a pretrained FR model to create an initial gallery, then optimizes these embeddings to uniformly position identities on a unit hypersphere. A conditional diffusion generator is subsequently used to synthesize faces.

### Strengths
1. The paper is well-written and easy to follow.
2. The empirical study shows that the proposed method generalizes well across different validation sets.
3. Experimental results are promising, with satisfactory improvements on benchmark datasets.

### Weaknesses
1. HyperFace Optimization: Figure 2 shows that HyperFace optimization results in a uniform distribution of points on the hypersphere. However, the paper lacks evidence, analysis, or experiments demonstrating that Equation 1 is minimized by this uniform distribution. The optimization process for Equation 1, which aims to maximize the minimum distance between randomly selected pairs, is not sufficiently analyzed. The paper states that the optimization is solved using an iterative approach based on gradient descent, but it does not provide insight into the optimization process or the cost function itself. The connection between maximizing minimum distance and achieving a uniform distribution is not rigorously established, and the paper does not discuss the challenges of optimizing this non-convex objective function, especially in high-dimensional spaces. See [1] for more details.

2. Use of Hyperspherical Points: One key aspect of the method is the use of uniformly positioned points on the hypersphere. While using a pre-trained FR model for generating the identity gallery is reasonable, it would be helpful to see results without applying HyperFace (using pure FR embedding as condition). How would this affect the results?

3. Experimental Section: The experiments section needs major revisions. Most of the subsections only report table results without in-depth discussion or analysis. For a conference of ICLR’s quality, it’s important to explain specific behaviors and insights from the proposed method.

4. Additional Experiments: Additional experiments could improve clarity on the benefits of the method. For example, while Table 3 presents an ablation study on the number of identities on FR performance, it would also be valuable to show how many novel identities the method can generate (what is the saturation point for the number of novel identities).

5. Identity Leakage: The paper mentions identity leakage but lacks in-depth experiments on the synthesized data. What would the performance look like if synthesized images with high similarity to real datasets (e.g., CASIA) were excluded?

### Questions
My main concerns are threefold: (1) the lack of theoretical and empirical analysis on HyperFace optimization (Equation 1), (2) missing ablations and detailed analysis of results, and (3) understanding the limitations of the method in generating novel identities. I am hopeful these concerns can be addressed during the discussion period, and I am open to increasing my score based on the responses. Please also see the weaknesses

### Soundness
4

### Presentation
3

### Contribution
3
