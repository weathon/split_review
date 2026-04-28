# Efficient Neuron Segmentation in Electron Microscopy by Affinity-Guided Queries

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Accurate segmentation of neurons in electron microscopy (EM) images plays a crucial role in understanding the intricate wiring patterns of the brain. Existing automatic neuron segmentation methods rely on traditional clustering algorithms, where affinities are predicted first, and then watershed and post-processing algorithms are applied to yield segmentation results. Due to the nature of watershed algorithm, this paradigm has deficiency in both prediction quality and speed. Inspired by recent advances in natural image segmentation, we propose to use query-based methods to address the problem because they do not necessitate watershed algorithms. However, we find that directly applying existing query-based methods faces great challenges due to the large memory requirement of the 3D data and considerably different morphology of neurons. To tackle these challenges, we introduce affinity-guided queries and integrate them into a lightweight query-based framework. Specifically, we first predict affinities with a lightweight branch, which provides coarse neuron structure information. The affinities are then used to construct affinity-guided queries, facilitating segmentation with bottom-up cues. These queries, along with additional learnable queries, interact with the image features to directly predict the final segmentation results. Experiments on benchmark datasets demonstrated that our method achieved better results over state-of-the-art methods with a 2$\sim$3$\times$ speedup in inference. Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel method for neuron segmentation in electron microscopy (EM) images using affinity-guided queries within a query-based framework. The approach aims to overcome the limitations of traditional methods that rely on watershed algorithms by directly predicting segmentation results, achieving improved accuracy and efficiency. The method is evaluated on benchmark datasets, showing competitive performance.

### Strengths
1. The use of affinity-guided queries in a query-based framework is a novel contribution to the field of neuron segmentation.
2. The method demonstrates a significant speedup (2-3x) over traditional methods, a notable advantage for large-scale data processing.
3. The query-based framework directly predicts the final segmentation results, avoiding the inaccuracy and inefficiency associated with the watershed algorithm used in traditional methods.

### Weaknesses
1. The comparison with state-of-the-art methods is limited to a few selected approaches. A more extensive comparison with a broader range of recent methods would strengthen the paper's contributions, such as [1]. 
2. The paper does not provide a strong theoretical foundation for why affinity-guided queries outperform other query-based methods, especially in terms of handling neuron morphology.  It is better to give a more detailed explanation or analysis of the mechanisms by which affinity-guided queries better capture neuron morphology compared to other query-based approaches.

### Questions
1. How does the method handle variations in image quality or noise levels in EM datasets?
2. What are the specific computational requirements for training and inference, and how do these scale with larger volumes?
3. How do affinity-guided queries compare with other forms of guided queries in terms of performance and efficiency?
4. The paper mentions that the proposed method does not require overlap prediction to address border effects. However, it is unclear how the method handles the continuity and consistency of segmentation results across block boundaries. Can the authors elaborate on this aspect and provide visual examples?

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
5

### Summary
This paper introduces Affinity-Guided Queries (AGQ) as a way to apply query-based instance segmentation to the field of connectomics. AGQ predicts the segments directly, bypassing postprocessing steps such as watershed used in some other approaches. The method is evaluated on two small-scale datasets, showing good results in terms of efficiency and accuracy.

### Strengths
- Evaluation on two datasets acquired with different EM techniques.
- Novel approach to segmentation of 3d EM data (query-based model).
- Good results in terms of efficiency and promising accuracy (but see comments about metrics below).
- Ablations showing the impact of the various modules.
- The paper is clearly written and well-organized.

### Weaknesses
 - Evaluation is performed on a very small scale (tens of um^3). Experience in the field of connectomics shows that such results are often not predictive of reconstruction quality over larger volumes. One of the datasets (ZEBRAFINCH) provides full volume (1M um^3 -scale) skeleton tracings that make it possible to compute topological metrics, which can then be compared to those reported https://doi.org/10.1038/s41592-022-01711-z and https://doi.org/10.1038/s41592-018-0049-4. Having these available, would make it much clearer how the proposed method compares to the state of the art in a practical setting.
- VOI advantage seems to be driven by VOI_split reduction at the cost of VOI_merge. If the mergers happen at the level of supervoxels, the results are in practice less useful for proofreading, where many systems do not make it possible to manually fix this type of error.
- The model is quite architecturally complex, with different losses, modules, and an explicit affinity modeling branch.

### Questions
- Please include VOI_split and VOI_merge breakdown in the main text instead of only in the appendices.
- The intro, abstract and Fig. 1 make it sound as if all currently used neuron reconstruction methods rely on watershed. This is not true (the authors are aware of at least https://doi.org/10.1038/s41592-018-0049-4, which they cite later; there also exist other approaches such as https://openaccess.thecvf.com/content_CVPR_2019/html/Meirovitch_Cross-Classification_Clustering_An_Efficient_Multi-Object_Tracking_Technique_for_3-D_Instance_CVPR_2019_paper.html) and should be more clearly discussed earlier in the paper. The proposed model is far from from the first approach that directly converts 3d EM images into a segmentation.
- 0.08 mm^3 is a fairly specific number to quote as a "typical size of studied volume", and quotes a 6y old paper. It would be best to cite more works here, or just refrain from making statements about what is typical altogether. I would also suggest reformulating the comment about processing requiring "130 days of runtime", as this is highly specific to your specific cluster/hardware configuration.
- How often does your algorithm generate disconnected components for the same predicted object? (Eq. 3 does not guarantee connectivity)
- What's the motivation for predicting affinities and then immediately averaging them in Eq. 7? Why not predict a boundary map?
- Does N_a in Eq. 8 vary between passes through the network? If so, how does that interact the number of learned queries -- is N_l or N kept constant? How is N_l chosen in your work?
- Your method does not require block overlaps to generate consistent results. But wouldn't the additional spatial context help in making the predictions better? Have you explored this?
- What are the error bars for your results in Tab. 1?
- How does your network capacity (parameter count, FLOPS) compare with your baselines?
- Your examples in Fig. 5 focus on dendrites with broken off spines. Could you please also provide a representative figure for axons? (perhaps in the supplement)

### Soundness
2

### Presentation
3

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
This paper presents an approach for neuron segmentation in electron microscopy images by a query-based segmentation framework. Traditional methods often rely on predicting affinities followed by watershed algorithms, which can introduce artifacts and inefficiencies. The proposed method predicts affinities using a lightweight branch to obtain coarse neuron structure information, which is then used to construct Affinity-Guided Queries (AGQs). These queries, along with learnable queries, interact with image features to directly predict the final segmentation results, eliminating the need for watershed algorithms. The method achieves better accuracy and a 2–3× speedup in inference time.

### Strengths
1. Novel and intersting idea that uses a query-based framework to eliminate the need for watershed algorithms used in traditional methods. The proposed method greatly improves efficiency.
2. Very well written manuscript. The paper clearly articulates the shortcomings of existing methods and motivates the need for the query based approach.
3. Comprehensive ablation studies show the contributions of different modules.

### Weaknesses
1. Despite the successful and interesting use of AGQs, I have difficulties to see why similar results couldn't be achieved by inputting image features, predicted affinities, and learnable queries directly into the neuron decoder (with modified architecture). While I understand that predicted affinities are used to create AGQ, I wonder if the LQ could "attend" to the predicted affinity map to construct the necessary queries themselves. It appears that the current neuron decoder is attempting to "rescue" the low-quality segmentation by AGQ in $M_{coarse}$.
2. The choice of $a$ in ConnectedComponent algorithm in eq 8 is not reported and discussed.
3. The computational efficiency is evaluated in terms of inference latency. It would be great if the manuscript could educate the readers about the model's memory consumption, which is important for deployment.

### Questions
1. There are, in fact, parallel/CUDA implementations of watershed algorithms. How would the proposed method compare to these optimized implementations in terms of efficiency?
2. For the Transformer Decoder implementation in Table 3, how do you input the image features and queries?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents an innovative approach to neuron segmentation in electron microscopy (EM) images, a critical task in connectomics research that aims to reconstruct neural connections in the brain. The authors propose an affinity-guided query (AGQ) method, which introduces a lightweight query-based framework to address the limitations of traditional clustering algorithms.

### Strengths
The authors introduce AGQ to incorporate coarse neuron structure information into the query generation process, reducing the learning difficulty and improving segmentation accuracy.

### Weaknesses
While the work is commendable and addresses significant challenges in the field, there are areas where further development and clarification could enhance the contribution and impact of the research. Here are some specific points for consideration:

1. The paper could benefit from a more comprehensive comparison with the latest state-of-the-art (SOTA) methods, such as those referenced in [1][2]. Including these comparisons will provide a clearer picture of how the AGQ method stacks up against the most recent advancements in the field. Specifically, a detailed analysis of the computational cost, memory requirements, and performance trade-offs compared to these methods is needed.
2. Figure 1 (b) suggests that the proposed method relies on agglomeration operations from 'waterz' post-processing. This seems to contradict the claim of directly predicting segmentation results. The authors should clarify whether the proposed method truly bypasses the need for watershed-based post-processing or if it still relies on some aspects of it. The use of agglomeration, even if not directly from 'waterz', needs to be clearly defined and its impact on the end-to-end nature of the method needs to be addressed.
3. The experiments presented in Table 2, while informative, may not be based on benchmarks that are widely recognized in the community. Utilizing more established benchmarks, with consistent training and testing splits, would strengthen the paper's findings and allow for better comparisons with other methods. The lack of standardized benchmarks makes it difficult to assess the generalizability of the proposed method.
4. The motivation behind the proposed affinity-guided queries appears to have similarities with modules found in other works, such as [3]. The authors should elaborate on the novel aspects of their approach and how it differs from or improves upon existing techniques. A more detailed explanation of the architectural differences and the specific advantages of the proposed query mechanism is required.
5. 'typically the neuron gap' in line168 is not unprofessional

### Questions
Comparison with State-of-the-Art Baselines

Clarification on the Use of Agglomerations

Use of Well-Established Benchmarks


Originality of Affinity-Guided Queries

### Soundness
3

### Presentation
3

### Contribution
2
