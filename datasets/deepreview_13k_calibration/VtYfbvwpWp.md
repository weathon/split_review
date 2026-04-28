# GoodDrag: Towards Good Practices for Drag Editing with Diffusion Models

- Decision: Accept
- Avg Score: 5.60
- Scores: 8, 3, 5, 6, 6

## Abstract
In this paper, we introduce GoodDrag, a novel approach to improve the stability and image quality of drag editing. Unlike existing methods that struggle with accumulated perturbations and often result in distortions, GoodDrag introduces an AlDD framework that alternates between drag and denoising operations within the diffusion process, effectively improving the fidelity of the result. We also propose an information-preserving motion supervision operation that maintains the original features of the starting point for precise manipulation and artifact reduction. In addition, we contribute to the benchmarking of drag editing by introducing a new dataset, Drag100, and developing dedicated quality assessment metrics, Dragging Accuracy Index and Gemini Score, utilizing Large Multimodal Models. Extensive experiments demonstrate that the proposed GoodDrag compares favorably against the state-of-the-art approaches both qualitatively and quantitatively. 
    The project page is \url{https://gooddrag.io}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a drag-editing framework using diffusion. The paper comprehensively evaluates and fixes issues in prior work (For ex- introduces information preservation through the feature alignment loss to alleviate drag points' drifting issue). Overall, the framework proposes a simple re-ordering of existing control and denoising steps leading to no additional computational overhead while significantly improving editing fidelity. 

The paper also contributes a dataset (Drag100) geared towards editing evaluation rather than training, in addition to two evaluation metrics for measuring editing fidelity. One of the metric exploits

### Strengths
1. Paper comprehensively evaluates prior work and builds on the weaknesses through a simple alternating dragging & denoising step-framework. 
2. The paper introduces a carefully thought out (natural + synthetic) hybrid evaluation dataset comprising diverse editing scenarios; in addition to two evaluation metrics that might be useful for the drag-editing community. Potential for higher impact.
3. Results look promising and the information preservation feature alignment loss is well grounded.
4. Supplementary contains substantial ablations and empirical visual justifications for proposed components of the framework.

### Weaknesses
1. It makes sense to compare against diffusion based editing techniques since the paper builds on the weaknesses of prior literature. However, it would be nice to still have DragGAN in the main qualitative figure (7) and the quantitative evaluations for the sake of completeness. 
2. Training hardware and memory is not specified in the main text. Consider moving it from the supplementary to the main text?

### Questions
Suggestions: 
1. I strongly recommend moving the user study carried out by the authors (in the supplementary currently) to the main text since that is the common evaluation metric across different papers, not DAI or GScore.
2. L355 - 357 is not needed. It should be apparent to the readers in this (editing/generative) space.
3. Consider making figures bigger. Especially Figures 5, 6 and 7. 
4. Add an ethics/societal impact section.

If these minor weaknesses and suggestions are acknowledged, I would consider giving it an even higher rating for highlighting.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a new approach for enhancing stability and image quality in drag editing tasks. Key contributions include: Alternating Drag and Denoising (AlDD) alternates between drag and denoising steps to prevent artifacts and ensure higher fidelity. Information-Preserving Motion Supervision maintains feature consistency and reduce drifting issues. Experiments are conducted on Drag100 dataset.

### Strengths
1. This paper contributes a new dataset and metric for image editting.
2. The idea for solving accumulation distortion is interesting.

### Weaknesses
1. This paper does not include comparisons with recent works [1, 2], which limits the context for understanding its contributions relative to the latest advancements.

2. It lacks critical experiments on the DragBench dataset [3], especially with the MD and IF metrics, which are widely used in existing literature for standardized evaluation.

Due to above considertation, it is challenging to assess the performance of this paper.

### Questions
See the strengths and weaknesses

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach to improve the stability and image quality of drag editing, namely GoodDrag. GoodDrag adopts an AlDD framework that alternates between drag and denoising operations within the diffusion process, effectively improving the fidelity of the result. They also propose an information-preserving motion supervision operation that maintains the original features of the starting point for precise manipulation and artifact reduction. In addition, they contribute to the benchmarking of drag editing by introducing a new dataset, Drag100, and developing dedicated quality assessment metrics, Dragging Accuracy Index and Gemini Score, utilizing Large Multimodal Models.

### Strengths
1. The paper proposes an effective framework for achieving high-quality drag-based image editing results.
2. The results demonstrate a significant improvement in image fidelity during the drag editing process.
3. The authors introduce a new dataset and additional metrics for evaluating the point-based image editing task.

### Weaknesses
1. The novelty of the ALDD design is limited, as it mainly alters the order of denoising during the drag updating process. A concern is whether separating the process using the hyperparameter 'B' is optimal. Is 'B' fixed, or does it require manual adjustment by the user? Furthermore, the paper does not sufficiently justify why this specific alteration of denoising order is beneficial compared to other possible modifications within the diffusion process. The lack of ablation studies exploring different denoising schedules or comparing the proposed approach with other potential modifications to the diffusion process further weakens this claim.
2. There is confusion about whether "ALDD" and "AlDD" refer to the same concept.
3. There is an unnecessary blank area on Line 054 of the paper.
4. The authors claim that previous datasets are limited in terms of diverse drag tasks. However, the proposed Drag100 dataset contains fewer images compared to DragBench (205 images) [1]. The paper does not provide a clear quantitative measure of task diversity to support this claim. It would be beneficial to see a more detailed breakdown of the types of editing tasks included in Drag100 and a comparison with the task distribution in DragBench.
5. Providing results for the GoodDrag method on the DragBench dataset[1] would enhance the evaluation. The absence of these results makes it difficult to directly compare the performance of the proposed method with existing approaches on a common benchmark.
6. It would be helpful to see how the results are measured using Image Fidelity and Mean Distance metrics in DragDiffusion[1]. Without these metrics, it is difficult to assess the method's performance in terms of both image quality and drag accuracy, which are crucial aspects of drag-based editing.

### Questions
1. The paper may lack a discussion on its limitations.

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
4

### Summary
This paper introduces GoodDrag, a diffusion-based approach designed to enhance the stability and fidelity of image drag editing. The core idea is to alternate between drag and denoising operations within the diffusion process to prevent perturbation accumulation, leading to more stable image generation. To this end, the authors propose the Alternating Drag and Denoising (AIDD) framework along with a new benchmark, Drag100. Experimental results demonstrate the effectiveness of the proposed methods both qualitatively and quantitatively.

### Strengths
1. The paper is well-written, and the proposed approach is technically sound.
2. The qualitative results well demonstrate the effectiveness of the proposed framework.

### Weaknesses
The main concern is the insufficiency of experimental results:
1. Although the authors proposed two quality assessment metrics, widely used evaluation metrics such as Image Fidelity (IF) and Mean Distance (MD) should also be reported.
2. How does the method perform on other benchmarks, such as DRAGBENCH?
3. What is the impact of using different base models on the results?
4. Limitations and failure cases should be discussed and reported.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces GoodDrag, a novel framework designed to enhance the stability and image quality of drag editing using diffusion models. The main contributions of the paper are as follows:

- Alternating Drag and Denoising (AlDD) Framework: GoodDrag employs the AlDD framework, which alternates between drag and denoising steps within the diffusion process. This approach prevents the accumulation of large perturbations, ensuring more refined and manageable editing results. The AlDD framework is depicted as a significant improvement over existing methods that apply all drag operations at once, followed by denoising, which often leads to excessive perturbations and low fidelity.
- Information-Preserving Motion Supervision: To combat common failures in drag editing related to point control, GoodDrag introduces an information-preserving motion supervision operation. This method maintains the original features of the starting point, ensuring more realistic and precise control over the drag process and reducing artifact generation.
- Benchmarking Enhancements: The paper contributes to the benchmarking of drag editing techniques by introducing a new dataset called Drag100 and developing dedicated quality assessment metrics, namely the Dragging Accuracy Index (DAI) and the Gemini Score (GScore). These metrics are designed to evaluate the quality of drag editing more effectively, utilizing Large Multimodal Models for a more accurate assessment.

### Strengths
1. **Introduction of the Drag100 Dataset**: The creation of the Drag100 dataset is a significant advancement for the field of drag editing. This new dataset provides a well-defined and controlled environment for testing and benchmarking drag editing algorithms. It includes a variety of image types and editing scenarios, which ensures comprehensive testing across different contexts and challenges. This diversity helps in evaluating the robustness and versatility of new drag editing methods under varied conditions.

2. **Development of Novel Evaluation Metrics**: The paper introduces two new evaluation metrics, the Dragging Accuracy Index (DAI) and the Gemini Score (GScore). These metrics are designed to provide a more precise and relevant assessment of drag editing quality. DAI focuses on the accuracy of content transfer to target locations, while GScore evaluates the naturalness and fidelity of the edited images using Large Multimodal Models. These metrics contribute to a standardized approach for assessing image editing quality, promoting more objective and reproducible research outcomes in the field.

3. **Well-Structured Presentation and Comprehensive Validation**: The paper excels in its presentation, clearly outlining the methodologies, experiments, and results.

### Weaknesses
1. **Questionable Novelty of AlDD**: The paper claims that existing methods typically conduct all drag operations at once and then attempt to correct accumulated perturbations subsequently. However, methods like DragonDiffusion and DiffEditor have previously explored applying motion supervision across multiple diffusion time steps. This raises questions about the purported novelty of AlDD, as the concept of distributing editing operations across multiple steps is not entirely new. While the authors claim a separation between dragging and denoising, the core mechanism of DiffEditor also involves iterative refinement within the diffusion process, making the distinction less clear-cut than presented. The claim that DiffEditor intertwines drag and denoising is not entirely convincing, as both methods perform iterative updates to the latent space based on both denoising and guidance signals, albeit with potentially different weighting and scheduling strategies. The paper needs to more clearly articulate the specific differences in the update mechanisms and how they lead to the claimed benefits of AlDD.

2. **Lack of Running Time Analysis**: The paper does not provide a comparative analysis of the running times of GoodDrag versus other state-of-the-art methods. Including this information would help evaluate the practical applicability of GoodDrag, especially in real-time or resource-constrained scenarios.

3. **Evaluation Metrics - Mean Distance and LPIPS**: DragDiffusion has already introduced Mean Distance and LPIPS as evaluation metrics for assessing drag editing quality. The paper would benefit from reporting these metrics alongside the newly proposed DAI and GScore to provide a comprehensive evaluation framework that can be directly compared with existing methods. The absence of these established metrics makes it difficult to gauge the relative performance of GoodDrag against prior work using standard measures.

4. **Comparison with More Recent Methods**: The paper lacks comparisons with more recent advancements in drag editing, such as DiffEditor, InstantDrag and LightningDrag. Including these methods in comparative evaluations would strengthen the paper's relevance and demonstrate the efficacy of GoodDrag in the context of the latest research developments.

5. **Use of DragBench and Handling of Masks**: The paper criticizes some datasets for not consistently providing masks, yet a drag-editing model should not alway relies on user-provided masks. And in the original DragGAN formulation, the mask is optional, highlighting a discrepancy in the paper's critique. A more robust approach would be to evaluate GoodDrag's performance on both DragDiffusion and SDEDrag's DragBench (both with and without masks), thereby demonstrating its versatility and alignment with user-friendly design principles seen in earlier methods.

### Questions
**Clarification on Tracking Steps in the Presence of Inversion Strength**: Does the GoodDrag framework continue to utilize point tracking steps within the Alternating Drag and Denoising (AlDD) framework? If so, considering the inversion strength is set to 0.7, which corresponds to a significant amount of noise reduction and thus a deviation from the original image features, how does the system ensure accurate matching and tracking of points? Specifically, since diffusion-based methods can maintain correspondence primarily when the diffusion time step is small, how does GoodDrag handle scenarios where the dragged points do not align with their intended targets due to these potential mismatches in feature correspondence?

### Soundness
2

### Presentation
3

### Contribution
3
