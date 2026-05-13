# A Simple Diffusion Transformer on Unified Video, 3D, and Game Field Generation

- Decision: Accept
- Scores: 6, 6, 3

## Abstract
The probabilistic field models the distribution of continuous functions defined over metric spaces. While these models hold great potential for unifying data generation across various modalities, including images, videos, and 3D geometry, they still struggle with long-context generation beyond simple examples. This limitation can be attributed to their MLP architecture, which lacks sufficient inductive bias to capture global structures through uniform sampling.
To address this, we propose a new and simple model that incorporates a view-wise sampling algorithm to focus on local structure learning, along with autoregressive generation to preserve global geometry. It adapts cross-modality conditions, such as text prompts for text-to-video generation, camera poses for 3D view generation, and control actions for game generation.
Experimental results across various modalities demonstrate the effectiveness of our model, with its 675M parameter size, and highlight its potential as a foundational framework for scalable, modality-unified visual content generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a transformer-based diffusion field model to better capture global structures and long-context dependencies. It does that by introducing a view-wise sampling algorithm and incorporating autoregressive generation. The proposed method is a general framework that can be applied to multiple modalities, such as video, 3D and game. Extensive experiments are conducted to validate the effectiveness of the proposal.

### Strengths
S1. The paper is well-written and mostly clear.

S2. The proposed view-wise sampling algorithm is interesting and novel.

S3. Exploiting autoregressive generation to preserve global geometry is reasonable. 

S4. The experiments are extensive, especially including various tasks.

### Weaknesses
W1. As autoregressive generation is typically slower than parallel generation due to its sequential nature, the authors are encouraged to discuss the inference time of the proposed method and baseline methods.

W2. As shown in Table 1, the proposed method achieves better performance against baseline methods on image and video, but worse FID and LPIPS scores on 3D generation task. The authors are encouraged to discuss this phenomenon.

### Questions
Please see the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a novel method for unified video, 3D, and game generation, by learning a DiT based mapping from metric space to signal space, which is able to process high-resolution inputs by the proposed view-wise sampling strategy, as well as maintaining global struture with introduced inductive bias such as text prompts. Results have demonstrated the effectiveness of the proposed method.

### Strengths
1. With the view-wise sampling strategy, this method can scale up to high-resolution inputs
2. By introducing long context conditioning, cross-view consistency can be avoided to some extent

### Weaknesses
1. The novelty is limited. From my perpective, the method proposed in this paper simply alters the sampling strategy of existing approaches through a straightforward design change, which trades off a reduced number of sampled views for a higher input resolution. Though the introduction of long context conditioning can compensate the global structure, this operation is common, and i don't this operation is powerful enough to recover the information lost during the process of view-wise sampling.

2. Since the method amis to learn a mapping from input coordinates to output properties, i think some other methods should also be compared, such as SIREN[1], and the difference between them should be clarified.

3. I'm wondering that whether the proposed method can be applied to more complex scenes generation, instead of simple objects in the task of 3D novel view synthesis.

### Questions
Please see weakness. I'm gald to increase my scores if my concerns can be addressed.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on unifying data generation across various modalities, including images, videos and 3D geometry. It introduces a view-wise sampling algorithm along with autoregressive generation to improve the performance. The proposed framework can handle various modalities with good performance.

### Strengths
1. The proposed method is a unified framework for various modalities. This is a relatively new task that might benefit the community.

2. Extensive experiments and ablation studies demonstrate the effectiveness of the proposed method.

### Weaknesses
1. **The motivation is unclear.** From the introduction section, the main motivation to use Diffusion Probabilistic Field (DPF) is handling various modalities together with a unified model. As for the unified models, what I understand is a single model that can generate different modalities. However, from the description in the method and experiment sections, each modality has different coordinate-signal pairs and the models are trained for each modality separately. If so, such a method cannot be regarded as a unified framework in my view. The core idea of a unified model should be the sharing of parameters across different modalities, which is not the case here. The authors seem to be using a single architecture but with independently trained weights for each modality, which significantly weakens the claim of a unified framework.

2. **Comparison with conventional diffusion models.** In Line 142-144, when comparing DPF with conventional diffusion models, the main difference is that DPF can be applied to sparse observation of fields. However, in the view-wise sampling subsection (Line 244), each time sample the tokens in n views, which is a dense modeling instead of sparse sampling. The authors claim to use a sparse sampling approach, but the view-wise sampling strategy samples multiple views simultaneously, which is not sparse in the context of the entire data field. This approach seems more like a batch processing of views rather than a sparse sampling of the data field itself. The comparison with DPF regarding sparsity is therefore misleading.

3. **Comparison with DPF.** In my view, the main contribution of DPF is the context query pairs sampling and optimization. However, in Line 502, this paper mentions that the context query pairs are not used, which confuses me about the training objective in this paper. Does this paper use the diffusion optimization objective like epsilon-prediction or velocity-prediction? If so, the method is almost the same with DiT. The paper does not clearly specify the training objective, making it difficult to understand how the proposed method differs from standard diffusion models like DiT. The use of a velocity-prediction objective, if true, would make the method very similar to DiT, and the paper should clarify this point and highlight the differences more clearly.

4. **Limited performance.** I do not see a part describing the dataset and hyperparameters used for training. So I assume the model is trained on each benchmark. If so, the performance is far from satisfactory since the compared methods are generalizable ones instead of fitting to a benchmark. The lack of details about the training datasets and hyperparameters makes it difficult to assess the validity of the experimental results. The performance is especially concerning given that the compared methods are often trained on more general datasets, while the proposed method seems to be trained on specific benchmarks, which should ideally lead to superior performance. The fact that this is not the case raises serious questions about the effectiveness of the proposed approach.

### Questions
I am not an expert in Diffusion Probabilistic Fields, and the writing of this paper makes me even more confusing. I hope the authors could improve the writing and explain more background and related work. In addition, most of my concerns are about the explanation of the method and motivation. Please refer to weaknesses for more details.

## Post Rebuttal
After discussing with the authors, I have decided to assign a reject score to this paper. Below are the key concerns that remain unaddressed:

- **Limited Contribution of the Unified Architecture**: The contribution of a unified architecture trained separately for each dataset is limited, especially since a similar concept has already been introduced by DPF.  
- **In-Distribution vs. Out-of-Distribution Performance**: For a generalizable model, the in-distribution performance should surpass out-of-distribution performance. For instance, in the comparison with Zero-1-to-3 in 3D generation, this expectation is not met.  
- **Video Generation Quality**: The qualitative results for video generation on the rebuttal page are unsatisfactory. None of the examples demonstrate temporally consistent motion. In contrast, the webpage for the compared method, [Latte](https://maxin-cn.github.io/latte_project/), showcases much better video generation results.  
- **Game Generation Quality**: The qualitative results for game generation are also unsatisfactory. Comparing the author-provided [game recording](https://www.youtube.com/watch?v=Gum4GI2Jr0s) with the results on the rebuttal page, the color of the bricks at the bottom of the generated videos is inconsistent. Furthermore, the generated scenes are limited, lacking elements such as flowers and turtles present in the recording, as well as any underground scenarios.

### Soundness
2

### Presentation
1

### Contribution
2
