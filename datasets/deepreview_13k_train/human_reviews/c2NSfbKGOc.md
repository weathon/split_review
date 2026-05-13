# TangentBind: Unlocking the Potential of Emergent Alignment in Multimodal Model

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
Improving the alignment of modalities has proven effective across various downstream tasks in multimodal models. Currently, modality alignment follows two main research directions: aligning all modalities simultaneously or binding the others by aligning to a core modality. The first ensures direct alignment, but it is difficult to extend to new modalities. The second is scalable but weak in emergent ability due to needing more direct inter-modality alignment. To address these problems, we propose the TangentBind. Specifically, we first align all modalities to a core modality, e.g., image or text. Then, we introduce a generative network that generates the embeddings of the second modality, e.g., text or image, based on the core modality embedding. Thirdly, other modalities, such as audio, are aligned to the core modality and generative embedding, improving emergent ability while retaining alignment with the core modality. During training, in addition to infoNCE, the Tangent Term is introduced to align the new modalities with the generated embeddings. This addresses accuracy issues caused by using generated vectors as representations for modalities. With VISION and TEXT as the core modality, our experiments include other modalities such as AUDIO, DEPTH, and INFRARED.  Eventually, our experiments show that the emergent ability of TangentBind significantly outperforms the original benchmark on 9 datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
TangentBind introduces a novel multi-modal alignment approach using generative networks and a Tangent term to enhance cross-modal performance while maintaining core modality alignment. The method shows significant improvements over baselines across various tasks and datasets, with innovative theoretical contributions in generative network modeling and parameter optimization strategies.

### Strengths
- Theoretical Innovation. TangentBind introduces new concepts through its Tangent term and generative network, backed by rigorous mathematical analysis and proofs. 

- Experimental Validation. The method demonstrates superior performance across multiple modalities (audio, depth, infrared) and diverse datasets (AudioSet, VGG-S, NYU-D), with comprehensive ablation studies validating each component. 

- Practical Robustness. TangentBind exhibits consistent performance across different core modalities (image and text), with minimal degradation in core alignment capabilities. The method's stability is evidenced through detailed parameter sensitivity studies and direct comparisons with alternative approaches like InfoNCE, demonstrating its readiness for real-world deployment.

### Weaknesses
 - Details of Generative Network. There is no detailed description of the generative network architecture, the learning target used, and the training process.

- The Value of Lambda. In line 515, it is shown that the best performance is achieved when lambda is set to 1.25. However, since this value is larger than 1, it seems to contradict the theoretical analysis.

- Writing to be improved. For instance, missing full stop in eq. 5, and incomplete sentence in line 277.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces TangentBind, a multimodal pre-train method based on latent space generation, and a Tangent Term, an improvement of infoNCE, aligning the generated modality embeddings. It also shows that the proposed Tangent Term not only enhances the emergent capabilities of the multimodal alignment model but also preserves alignment with the core modality.

### Strengths
- This paper revises InfoNCE loss by adding Tangent Term, where its functionality is mapping the embedding to the space tangent to the image vector and scaling it to the unit hypersphere. This is novel, and the Tangent Term actually improves the overall performances of multimodal models.

- This paper clearly shows the effectiveness of the TangentBind with comprehensive experiments and outperforming results in various downstream tasks like RGB image, depth image, infrared image, and audio.

### Weaknesses
 - While the whole paper talks about InfoNCE loss and develops it to propose the Tangent Term, the actual InfoNCE paper [1] does not seem to be referenced. This is critical - the author MUST reference the original InfoNCE paper.

- While the proposed TangentBind is novel enough with exhaustive experiments, minor typos, a missing reference, spacing between lines, and the location of figures and table, etc. (please refer to Additional Comments), diminish the overall quality of the paper, making it seem to be incomplete. I would definitely encourage the authors to take a slow look at the entire paper to refine the paper's quality.

### Questions
### Additional Comments
- Please add a line mentioning that the details of the dataset are located in the Appendix at the beginning of Section 5: Experiments and Results.
- Typo in line 315: TangenBind -> TangentBind
- Typo in line 316: i4mage -> image
- I might have missed the other typos in the paper. Please take a careful look to revise the paper's overall quality. I would like to raise my score if the authors revise the paper more like reader-friendly.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a multimodal pre-training method called TangentBind, which aims to enhance the potential alignment capability of multimodal models. Unlike previous methods, TangentBind first aligns all modalities to a core modality (such as image or text), and then introduces a generative network to generate the embeddings of the second modality based on the embeddings of the core modality. The authors also introduce the Tangent Term, which is a loss function that can prevent the generated embeddings from negatively impacting the alignment with the core modality. The experimental results show that TangentBind significantly outperforms previous binding models in terms of potential capability across various datasets and tasks.

### Strengths
1. TangentBind introduces a novel approach to enhance the emergent alignment capabilities between indirectly aligned modalities while maintaining alignment with the core modality.
2. The method's effectiveness is validated through experiments using VISION and TEXT as core modalities and including other modalities such as AUDIO, DEPTH, and INFRARED.
3. The method proposed in the paper do not need additional datasets where all modalities are present simultaneously, nor does it rely on large amounts of generated data across different modalities, making it more efficient and practical.

### Weaknesses
1.Little benefits from the proposal: In this system, the authors proposed two key components. However, the idea of generative network stems from DALLE-2, which lacks its motivation. The idea of TangentTerm has relatively low benefit on final results.
2.Limitations on the significance of the task: In comparison, LanguageBind still performs better on some task compared to TangentBind.
3.Lack of experiments on the structure of generative network: In this paper, the generative network proposed by the authors only compares with noisy embedding. The authors may use some other structures to replace generative network.
4.Lack of ablation study: Reviewer suggest removing tangent term and generative network together, and add them each at a time to show the benefits from either of them more clearly.

### Questions
1.The proposed method trains a Generative Net at Step 2, which generates reconstructed image embeddings conditioned text. The motivation of using a generative network for aligning different modalities seems to be unclear. Since training a generative network consumes much more time and resources than other ways of fusing different modalities.
2.It would help if the authors could provide more details on the training datasets and resources consumption. As the quality of core modality, VISION and TEXT could greatly influence the performance of successive modality encoder.
3.In the experiment part, the authors give the test results on various benchmarks with existing methods like ImageBind and LanguageBind, but it could be strengthened by including more comprehensive comparisons with methods train with modality pairs, (image, text) and (audio, text) for example, like CLIP and AudioCLIP.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces TangentBind, a novel paradigm for training a multimodal unified representation space. By training a generation model capable of producing embeddings-to-embeddings, TangentBind establishes a new alignment anchor when additional modalities are involved. The article elaborates the training methodology of this generation model in detail and demonstrates through experiments that utilizing this additional representation for alignment results in superior performance compared to scenarios where it is not used.

### Strengths
- The paper astutely identifies a critical shortcoming in the current multimodal unified representation spaces, namely the non-unified distribution across different modalities induced by the InfoNCE loss. 
- The paper address the limitations of the single-term InfoNCE loss in characterizing multimodal representation spaces by incorporating a new alignment component provided by a generative model, which enhances the overall alignment quality.

### Weaknesses
*Weakness 1: Regarding Formatting and Writing*

- The positions of Table 1 and Table 2 on page 7 are inverted.
- Numerous small tables occupy excessive space. The authors might consider integrating several tables and restructuring the layout.
- Section 5.4 contains large portions of repeated content.

*Weakness 2: Regarding Table 1 and Figure 1*

- In Table 1, the R@10 data is severely missing. If the paper has indeed conducted reproducibility experiments, both R@1 and R@10 results should have been obtainable; it is peculiar that the paper presents the R@1 results but not the R@10 results.
- There are boldface marking errors: although C-MCR exhibits significantly better performance on Audiocaps, the paper still highlights its own method in bold.
- I am particularly curious why the CLAP results were not included in Table 1 for reference, and similarly, in Figure 1, CLAP's performance is not fully displayed. The performances of Clotho and Audiocaps should not be set to zero.

*Weakness 3: Regarding Figure 6 and Section 5.4*

Given that the loss function optimized by the generative network in the paper is the mean-squared error, and the authors mention in section 3.1 that the representations are normalized to a hypersphere, optimizing the squared error between two unit norm vectors essentially optimizes their cosine similarity. Therefore, the insight that Figure 6 aims to demonstrate is self-evident. This figure merely confirms that the generative network is trained correctly. Although the authors arrange this experiment in the ablation study, in my opinion, the baseline that is really worth comparing should also be other methods of finding alignment anchors, such as directly generating images with captions and then extracting embeddings, or employing retrieval methods as mentioned in C-MCR to find alignment anchors, rather than simply using Gaussian noise for comparison.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2
