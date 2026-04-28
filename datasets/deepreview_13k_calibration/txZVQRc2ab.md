# RAPID: Retrieval Augmented Training of Differentially Private Diffusion Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 5, 6

## Abstract
Differentially private diffusion models (DPDMs) harness the remarkable generative capabilities of diffusion models while enforcing differential privacy (DP) for sensitive data. However, existing DPDM training approaches often suffer from significant utility loss, large memory footprint, and expensive inference cost, impeding their practical uses.  
To overcome such limitations, we present RAPID: Retrieval Augmented PrIvate Diffusion model, a novel approach that integrates retrieval augmented generation (RAG) into DPDM training. Specifically, RAPID leverages available public data to build a knowledge base of sample trajectories; when training the diffusion model on private data, RAPID computes the early sampling steps as queries, retrieves similar trajectories from the knowledge base as surrogates, and focuses on training the later sampling steps in a differentially private manner. Extensive evaluation using benchmark datasets and models demonstrates that, with the same privacy guarantee, RAPID significantly outperforms state-of-the-art approaches by large margins in generative quality, memory footprint, and inference cost, suggesting that retrieval-augmented DP training represents a promising direction for developing future privacy-preserving generative models (code and data are available in the submitted supplemental materials).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents RAPID, a new approach to train differentially private diffusion models by integrating retrieval-augmented generation (RAG) techniques. RAPID utilizes public data to build a knowledge base of sample trajectories, allowing for efficient use of private data by focusing on training later sampling steps under privacy constraints. This approach improves generative quality, memory efficiency, and inference speed compared to existing methods, demonstrating RAPID's effectiveness in privacy-sensitive generative modeling.

### Strengths
Privacy-Utility Trade-off: RAPID effectively balances privacy and utility by using public data for initial steps and focusing on private data for detailed refinement. This selective approach enhances the quality of generated outputs.
Efficiency: The retrieval mechanism reduces memory and computation demands by bypassing intermediate steps, which enhances scalability for larger models.
Generative Quality: Experimental results show that RAPID achieves higher FID and accuracy scores than existing differentially private diffusion models (DPDM), indicating superior output quality and utility.
Innovative Use of Public Data: The approach of leveraging public data to construct a trajectory knowledge base is novel and significantly reduces the computational cost of training on private data.

### Weaknesses
1.Over-Reliance on the Quality and Relevance of Public Data. The method’s effectiveness depends heavily on the quality and relevance of the public data used in the early stages of training. If the public data does not adequately represent the private data or is of low quality, the retrieval-augmented generation process will suffer from poor performance. Specifically, the reliance on high-level layout similarity between public and private datasets is a potential limitation. While the authors suggest that early diffusion steps primarily determine layout, the degree to which this holds true across diverse datasets and noise levels needs more rigorous investigation. The method could be vulnerable if the public data lacks sufficient diversity in layouts or if the noise added during the diffusion process significantly alters the structural information, leading to a mismatch with the private data's underlying structure.

2.The integration of RAG to enhance the privacy-utility tradeoff could introduce a critical flaw in privacy protection. The retrieval mechanism in RAPID depends on accessing external knowledge bases or data repositories to inform the generative process. This retrieval is based on similar data points or trajectories, which risks the accidental exposure of private data that was used to build the retrieval database. Even if the retrieval is performed on public data, the selection of specific trajectories based on similarity to private data could inadvertently reveal information about the private data distribution, especially if the retrieval mechanism is not carefully designed to prevent such leakage.

### Questions
Given that the method heavily relies on public data in the early stages, how do you ensure that the public data sufficiently represents or aligns with the private dataset? Have you tested the model’s robustness when using diverse or low-quality public datasets that may not closely match the private data distribution?

### Soundness
3

### Presentation
4

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
This paper introduces RAPID, an approach to training differentially private diffusion models that leverages retrieval augmented generation (RAG). RAPID works by using public data to train a knowledge base of sample trajectories. Then, when training the diffusion model on private data, it retrieves similar trajectories from the knowledge base and focuses on training the later sampling steps in a differentially private manner. 

RAPID is compared against baseline private diffusion methods for the task of image synthesis. RAPID outperforms the baselines in most settings in terms of generative quality (measured by FID score).

### Strengths
* The paper is clearly written, readable, and well-organized.
* The authors provide a thorough evaluation of RAPID on a variety of benchmark datasets for the task of image synthesis.
* The results show that RAPID outperforms state-of-the-art methods.
* This work opens an avenue for future work incorporating RAG into training.

### Weaknesses
 - No discussion of the limitation of this approach. See question 2.

### Questions
1. Why is the cost of DP hyperparameter tuning small (Line 307)?
2. Does using public data in this way ever reduce the generative quality of the model? For instance, what happens when the public data is wholly unrelated to the private data?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates differentially private (DP) data synthesis through diffusion models, proposing an approach that leverages *public* pre-training data to: (1) pre-train diffusion models, (2) train a feature extractor, and (3) derive trajectories from the forward diffusion process to establish a knowledge base. For training on *private* (sensitive) data, this method queries the knowledge base with a noisy *private* sample to retrieve a partially denoised *public* counterpart, which is then used to update the diffusion model via DP-SGD. This process effectively uses public knowledge to bypass certain intermediate training steps, simplifying model fitting. Experimental results indicate promising improvements compared to standard DP diffusion model training.

### Strengths
- The paper addresses a relevant and important topic, presenting the material clearly. 
- The proposed method is intuitive, straightforward to implement, and readily applicable in practice.
- Experimental results are promising, showing effective improvements over standard DP diffusion model training.

### Weaknesses
While the technical contribution is relatively modest (more of a training technique specifically designed for DP diffusion models, which somewhat narrows its scope), the paper’s main value seems to lie in demonstrating performance improvements with this approach.  

However, I have concerns regarding the experimental evaluation: (1) some key DP diffusion model baselines are missing, making it difficult to thoroughly assess the claimed performance gains, and (2) the paper lacks adequate investigation into large domain shifts between public and private data, a critical consideration for methods that rely on public data. These gaps leave the reported performance improvements less convincing

### Questions
-As previously mentioned, some published works on DP diffusion models are not included in this paper's experimental comparisons, which makes the current evaluation less convincing. Notable examples include:
“Differentially Private Synthetic Data via Foundation Model APIs 1: Images,” ICLR 2024
“PrivImage: Differentially Private Synthetic Image Generation using Diffusion Models with Semantic-Aware Pretraining,” USENIX Security 2024

- Are the timesteps $k$ and $v$ fixed during training? If so, how are these values selected, and what is the robustness to different choices? If not, how is the value of the retrieved timestep $v$ determined, given that the key-value pair only stores the embeddings $(h(x_k), x_v)$?
- For the comparisons, it would improve clarity to present performance across varying $\epsilon$ in a figure, with each method represented as a curve.
- As noted above, the experiments should more thoroughly investigate performance under strong distributional shifts between public and private data (e.g., by using private data with specific domain features, such as medical data).
- As far as I understand, the "Retrieval Augmented Training" approach is orthogonal to model training and architecture. Therefore, it would be more convincing to compare the addition or omission of “Retrieval Augmented Training” on both DPDM and DP-LDM training, showing that adding the proposed  “Retrieval Augmented Training” consistently improves performance in both cases.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel method called RAPID that integrates retrieval-augmented generation (RAG) into the training of differentially private diffusion models (DPDMs). This approach leverages public data to create a knowledge base of sample trajectories, which are used as surrogates during the training on private data. By focusing differential privacy constraints on the later sampling steps and reusing similar public trajectories for the initial steps, RAPID significantly improves the trade-off between privacy and utility. The method improves existing DPDMs by reducing utility loss, memory footprint, and inference costs. Evaluations on benchmark datasets demonstrate that RAPID outperforms state-of-the-art methods in generative quality, memory efficiency, and inference speed. This work suggests that integrating RAG with differentially private training represents a promising direction for developing privacy-preserving generative models.

### Strengths
1. The experiment results demonstrate great improvements in generative quality, compared to existing differentially private diffusion models.

2. The method reduces the memory footprint by minimizing the batch size requirements and enhances inference efficiency by skipping intermediate sampling steps. 

3. The paper is well-structured and clearly written, making it easy to follow the progression of ideas and understand the contributions.

### Weaknesses
1. Could the authors further explain the motivation for integrating RAG into DPDM? For example, consider the "public" model (or pre-trained model) which uses public data to train the diffusion model without adding differential privacy noise. Notice that this model does not include sensitive private data. Is it possible that the differential privacy noise introduced in the fine-tuning step will degrade utility, causing RAPID to underperform this public model? What are the possible scenarios where fine-tuning with differential privacy noise can indeed improve utility? It would be beneficial to explore the conditions under which the fine-tuning process with added noise is advantageous, especially since the public model already captures the general data distribution.

2. Could the authors further analyze the time complexity of the end-to-end algorithm? Though this method improves inference efficiency by skipping intermediate sampling steps via RAG, is it time-consuming to build the trajectory knowledge base? How does the runtime depend on the knowledge base size? It would be helpful if the authors could provide rough runtime comparisons. The analysis should include the time required for knowledge base construction, which is a critical factor in the overall efficiency of the proposed method. Furthermore, the scaling behavior of the runtime with respect to the knowledge base size needs to be quantified, as this will impact the practical applicability of the method.

3. If the private data and the public data are too "dissimilar," how will the trajectory knowledge base trained by the public data affect the later sampling steps? The paper should address the potential for negative transfer when the public and private datasets have significantly different distributions. This is crucial because the method relies on the assumption that the public data can provide useful trajectory information for the private data. A discussion on how to mitigate the impact of dissimilar datasets is needed.

Minor:

4. Line 10 of Algorithm 2: should it be $\tilde{g}$?

### Questions
1. What is the possible reason that DPDM improves sharply in the "EMNIST→MNIST" setting as the privacy budget increases, i.e., for FID 125.7 to 12.9 (the best among all methods), as $\varepsilon$ goes from 0.2 to 10?

2. Could the authors further analyze the time complexity of the end-to-end algorithm? Though this method improves inference efficiency by skipping intermediate sampling steps via RAG, is it time-consuming to build the trajectory knowledge base? How does the runtime depend on the knowledge base size? It would be helpful if the authors could provide rough runtime comparisons.

3. If the private data and the public data are too "dissimilar," how will the trajectory knowledge base trained by the public data affect the later sampling steps?

Minor: 

4. Line 10 of Algorithm 2: should it be $\tilde{g}$?

### Soundness
3

### Presentation
3

### Contribution
3
