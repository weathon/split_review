# How many tokens is an image worth?

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Current vision systems typically assign fixed-length representations to images, regardless of the information content. This contrasts with human intelligence —and even large language models—which allocate varying representational capacities based on entropy, context and familiarity. Inspired by this, we propose an approach to learn variable-length token representations for 2D images. Our encoder-decoder architecture recursively processes 2D image tokens, distilling them into 1D latent tokens over multiple iterations of recurrent rollouts. Each iteration refines the 2D tokens, updates the existing 1D latent tokens, and adaptively increases representational capacity by adding new tokens. This enables compression of images into a variable number of tokens, ranging from 32 to 256. We validate our tokenizer using reconstruction loss and FID metrics, demonstrating that token count aligns with image entropy, familiarity and downstream task requirements. Recurrent token processing with increasing representational capacity in each iteration shows signs of token specialization, revealing potential for object / part discovery.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses a fundamental limitation in current visual representation learning systems: their use of fixed-length representations regardless of image complexity. The authors introduce an Adaptive Visual Tokenizer (AVT) that can generate variable-length representations (ranging from 32 to 256 tokens) through a recursive processing mechanism.

The key innovation is a recurrent encoder-decoder architecture that progressively distills 2D image tokens into 1D latent tokens over multiple iterations. During each iteration, the system not only refines existing tokens but also introduces new ones, allowing for adaptive representation capacity. This approach enables tokens to specialize and focus on specific image regions, leading to emergent object discovery without explicit supervision.

The authors provide extensive empirical evidence demonstrating that optimal token counts naturally vary based on several factors: image complexity/entropy, familiarity with the training distribution, downstream task requirements, and the strength of models using these representations. Through experiments on image reconstruction, classification, and depth estimation tasks, they show that their adaptive approach achieves comparable performance to fixed-length tokenizers while offering the flexibility to use fewer tokens when appropriate.

Beyond the technical contribution, the paper makes a broader conceptual contribution by demonstrating how variable-length representations align with human visual processing and information theory principles. The work suggests promising directions for more efficient visual representation learning, particularly for applications like video understanding where fixed-length representations may be insufficient.

-----------

Update: Added response and modify score to 6, presentation to 2.

### Strengths
**Originality**  
- Novel integration of recurrent processing with visual tokenization, extending beyond fixed architectures like VQGAN/Perceiver
- adapting dynamic computation (from NLP/sequential domains) to visual representation learning
- Fresh perspective on image compression through variable-length tokens, contrasting with traditional fixed-length approaches
- Original empirical framework for analyzing token requirements across complexity, familiarity, and model capacity

**Quality**  
Thorough empirical validation across multiple dimensions:
- Reconstruction quality (L1, FID) is competitive with specialized fixed-length tokenizers
- Linear probing results comparable to larger models (49.9% Top-1 vs Titok's 48.0% with smaller architecture)
- Systematic ablations of architecture choices (continuous vs discrete, network depth, training strategies)
- Strong technical foundation combining quantized latent spaces, recurrent processing, and adaptive computation
- Rigorous analysis of token specialization through attention map visualization and segmentation alignment (57.8 mIOU without explicit supervision)

**Clarity**  
- Clear architectural progression from base distillation to full adaptive system
- Well-structured empirical validation of key hypotheses about token requirements
- Effective use of visualizations to demonstrate token specialization and attention patterns
- Systematic organization of ablation studies exploring key design choices

**significance**:  
- Demonstrates feasibility of variable-length visual representations while maintaining performance
- Introduces techniques potentially valuable for resource-constrained deployment scenarios

The paper's main strength lies in its systematic challenge to the fixed-length paradigm while maintaining competitive performance, backed by comprehensive empirical analysis.

### Weaknesses
The paper's primary weakness lies in its validation strategy and scaling limitations. While the approach shows promise, the core experiments are limited to ImageNet-100 (rather than full ImageNet-1K) for the adaptive tokenization training, making it difficult to assess the method's capabilities at scale fully. The authors acknowledge this limitation in Table 1's footnote, but don't sufficiently explore whether the performance gap with fixed tokenizers (particularly in FID scores for low token counts) is fundamental to the approach or simply due to training scale.

A second significant weakness is the lack of thorough comparison with specialized architectures. While the paper compares with fixed-length tokenizers (VQGAN, Titok), it omits comparisons with other adaptive approaches like FlexViT (variable patch sizes) or hierarchical architectures that naturally handle multi-scale features. It isn't easy to assess whether the benefits come from the variable-length representations or could be achieved through simpler adaptive mechanisms. For instance, the paper does not explore whether a simpler approach of training a fixed-length tokenizer with a variable-length objective (e.g., randomly masking tokens during training) could achieve similar results. The absence of these comparisons makes it difficult to isolate the specific contribution of the recurrent architecture.

A third weakness is the lack of thorough investigation into computational overhead. The approach's recurrent nature requires multiple passes through the encoder-decoder architecture to generate variable-length representations. While Figure 9 includes some ablations on network depth and training, there's no detailed analysis of inference time complexity or memory requirements compared to single-pass approaches like VQGAN or Titok. This is particularly important given the paper's motivation of efficient representation learning. The paper should include a breakdown of the computational cost per iteration, including FLOPs and memory usage, to properly evaluate the practical efficiency of the proposed method.

Finally, while the adaptive token allocation based on complexity is well-motivated, the paper lacks a formal framework for analyzing the optimality of these allocations. The empirical correlations with human-labeled complexity scores are interesting but don't provide theoretical insights into whether the model is making optimal token allocation decisions. Given task constraints, including some theoretical analysis or bounds on optimal token allocation would significantly strengthen the paper's contributions. For example, the paper could explore the relationship between the reconstruction loss and the number of tokens, and whether there is a diminishing return in reconstruction quality as more tokens are added.

### Questions
1. **Computational Efficiecy and scaling**  
- Could you provide a detailed analysis of inference time and memory requirements compared to single-pass approaches?
- How does the recurrent processing overhead scale with a number of iterations?
- Have you explored early stopping strategies to reduce computation for "simple" images?
- What are the key bottlenecks preventing training on total ImageNet-1K?

2.**Token allocation optimality**  
- Given task constraints, Is there a theoretical framework for determining the optimal number of tokens?
- How do you ensure the progressive token addition across iterations efficiently utilizes capacity?
- Have you explored methods to predict the required token count before processing, similar to adaptive computation time in transformers?
- Could you provide an empirical analysis showing token utilization across iterations (e.g., are later tokens less "important")?

3. **Comparison with specialized architectures**:
- How does the method compare with recent adaptive patch-size approaches (like FlexViT) on standard benchmarks?
- Could you provide direct comparisons with self-supervised methods like DINO on standard metrics for object discovery capabilities?
- Have you explored combining your approach with hierarchical architectures that naturally handle multi-scale features?

4.  **Codebook and quantization design**  
- What motivated the choice of shared codebook across iterations versus hierarchical/specialized codebooks?
- How sensitive is the method to codebook size and quantization strategy?
- Could you analyze codebook utilization across different iterations and image complexities?
- Have you explored using learned or adaptive quantization strategies?

These clarifications would help comprehensively assess the method's practical applicability and theoretical foundations.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Representation learning models assign fixed-length representations to samples regardless of their information content. In contrast, the authors aim to present a method for learning variable-length tokenized representations for 2D images.

The paper introduces the Adaptive Visual Tokenizer (AVT), which recursively distills 2D images into 1D latent tokens through an encoder-decoder model trained using a reconstruction objective. To achieve variable-length tokenized representations, the authors add new tokens at every iteration of the recurrence. The authors allow optional masking of specific 2D tokens that are well-reconstructed, enabling "dynamic halting" per token.

Through experiments with their method, the authors provide several insights relating to the adaptive representation capacity of AVT:
- More complex images require more tokens to reconstruct.
- OOD images require more tokens than in-distribution ones to reconstruct.
- As the downstream criterion for accepting the representation increases in complexity, more tokens are required.
- Optimal adaptation for performance occurs when the token selection criterion is relevant to the task of interest.
- Weaker models exhibit smaller relative performance drops with reduced token counts than stronger ones.

The authors also compare AVT reconstructions and linear probe performance with various baselines. They analyze the impact of choosing continuous vs discrete tokenizers. Analyzing attention maps of 1D latent tokens to 2D image tokens reveals that tokens attend to distinct semantically meaningful objects or parts, suggesting the emergence of object discovery. Finally, the authors show that broad attention of early tokens specializes to focus on sparser, more meaningful regions, when new tokens are introduced as the recurrence proceeds.

### Strengths
- The paper presents thorough analysis of the adaptive representation capacity of the proposed method.
- The authors show that their method can lead to the emergence of tokens that exhibit useful semantics.

### Weaknesses
Baselines are very limited.
- The paper is motivated from a representation learning perspective, but there is no comparison with representation learning methods beyond two families of generative models. For vision, methods like CLIP [1], MoCo [2], DINO [3], and MAE [4] (which is also reconstruction-based) should be compared for downstream tasks like linear probe.
- There is no comparison with other variable-length representation baselines, such as with Matryoshka representation learning [5], despite noting the relevance in the paper.

The comparisons with current baselines have very mixed results.
- In Table 1, all baselines perform better than the authors for a specific token count, and many remain better even when compared to the max token count of AVT. The authors note that longer training on larger datasets with deeper networks could bridge the gap. Still, it is not apparent if that would be enough to outperform the baselines, especially ensuring that the training budgets remain fair.
- Linear probe performance in Section 5 is at par with baselines, but often requiring more tokens and recurrent processing.

Discussion of gradients
- There is no discussion of how gradients are treated within the recurrent processing. It is unclear if the authors backpropagate gradients from future iterations all the way back or if they stop the gradient flow between each iteration.

The insight about weak and strong models is not very convincing.
- Weaker models exhibiting smaller relative performance drops with reduced token counts could simply indicate that weak models, due to being weak, do not reach the same peak performances as the strong models. This would result in their performance with more tokens remaining similar to their initial performance.
- In this case, the statement should be that weaker models exhibit lower performance than stronger models, and they reach their performance cap sooner than stronger models as the number of tokens increases, which is not surprising.
- Looking at the absolute performance metrics can provide some insights here.

Dynamic halting is unclear.
- Figure 1 states that dynamic halting is optional, but a clear discussion of when it should be enabled or disabled is missing.
- It is unclear if it is enabled for all experiments or some subset.

Complexity of the method.
- The proposed method is not simple, including multiple stages like learning to reconstruct pre-trained VQGAN tokens, then joint encoder-decoder training, and then GAN loss at some later stage in training.

Minor (no effect on score):
- "Variable-length token representations" is confusing due to ambiguity: it can mean representations per token variable length or a variable number of tokens. Perhaps "variable-length tokenized representations" is a less ambiguous term.
- The footnote marked on Classification on line 397 points to a footnote printed three pages prior, which is confusing and not immediately apparent.
- Table 1 has elements not adequately labeled or described in the caption: what is the # superscript? The caption should also clarify that the numbers under the dataset names are the number of tokens and not some varying attribute of the datasets.
- Relevant paper you might want to cite that also learns tokenized representations (fixed-length) where tokens show the emergence of distinct concepts: [6].

### Questions
Currently, the number of new tokens added per iteration seems to be fixed to 32. What does the relationship between the number of tokens added per iteration and the total number of iterations, for a fixed max token count, look like? It would be interesting to see if trade-offs exist, like incurring higher computational costs by performing more iterations leading to significantly smaller "good enough" representations (each iteration adds a smaller amount of new tokens, but each token gets many more refinement updates).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores the concept of adaptive and recursive representations for image processing, focusing on how many tokens are necessary to effectively represent an image. The authors conduct a series of experiments to evaluate their approach, starting with image reconstruction tasks and linear probing for Top-1 classification. They investigate the impact of using continuous versus discrete tokenizers on reconstruction tasks and analyze the learned tokens' alignment with ground truth segmentation, suggesting potential for object discovery. The role of recurrent processing in achieving these results is also examined.

A key contribution of the paper is the demonstration of a correlation between an image's perceptual complexity and its compressibility, as theorized by Schmidhuber's Low Complexity Art theory. The authors show that images with lower complexity can be reconstructed with fewer tokens, while more complex images require a higher number of tokens for accurate reconstruction. This is evidenced by experiments using out-of-distribution images from the PeopleART dataset, where the model trained on ImageNet-100 successfully reconstructs images of varying complexities with different token capacities.

The paper highlights two main observations: (a) as image complexity increases, using fewer tokens results in higher reconstruction errors, necessitating a larger computational budget; and (b) for a fixed image complexity, increasing the number of tokens reduces the reconstruction loss, showcasing the efficiency of the adaptive representation model. These findings underscore the potential of the proposed approach in efficiently handling images of varying complexities by adjusting the number of tokens used for representation.

### Strengths
Originality: The paper introduces an innovative method for image representation by employing a multi-stage training procedure that combines VQGAN and distillation techniques. The approach of using adaptive and recursive representations, along with the introduction of a shared 1D codebook for token quantization, is a novel contribution to the field. The concept of dynamically halting token processing based on reconstruction quality adds a unique aspect to the methodology, allowing for more efficient and tailored image representation.

Quality: The quality of the research is demonstrated through comprehensive experiments and ablation studies. The paper provides a thorough evaluation of the proposed method, including image reconstruction experiments, linear probing for classification, and analysis of learned tokens for object discovery. The results, such as the high mean IOU achieved in attention map alignment with ImageNet-S GT segmentation, underscore the effectiveness of the approach. The use of GAN loss to enhance photo-realism further attests to the robustness of the training procedure.

Clarity: The paper is well-structured and clearly articulates the training procedure and experimental setup. The inclusion of figures, such as the adaptive visual tokenizer diagram, aids in understanding the complex process of 2D to 1D to 2D distillation. However, some sections could benefit from additional explanations, particularly for readers unfamiliar with the underlying concepts of VQGAN and distillation techniques. The appendix is referenced for implementation details, which is helpful for those seeking to replicate the study.

Significance: The significance of the paper lies in its potential impact on the field of image processing and representation learning. By demonstrating that adaptive representations can lead to emergent properties like object discovery, the research opens new avenues for exploring how different tokenization strategies can enhance image understanding. The ability to achieve high alignment with segmentation tasks without explicit optimization for segmentation highlights the broader applicability of the method in various computer vision tasks.

### Weaknesses
Limited Evaluation Metrics: The evaluation of the model is primarily focused on image reconstruction and classification tasks. While these are important, the paper could benefit from a broader range of evaluation metrics, particularly those that assess the quality and utility of the learned representations in more diverse and complex tasks. For instance, metrics evaluating the disentanglement of the learned representations or their robustness to adversarial attacks would provide a more complete picture of the model's capabilities.

Tokenization Approach: The paper discusses the use of continuous vs. discrete tokenizers but does not provide a comprehensive analysis of the advantages and disadvantages of each approach. A more detailed comparison could help in understanding the trade-offs involved and the scenarios where one might be preferred over the other. For example, the computational cost, memory footprint, and sensitivity to noise for each tokenization method should be analyzed.

Sensitivity to Model Strength: The findings suggest that stronger models are more sensitive to fewer-token reconstructions, which could be a limitation in practical applications where computational resources are constrained. The paper could explore strategies to mitigate this sensitivity and improve the robustness of the approach across different model strengths. For instance, techniques like knowledge distillation or regularization could be used to make the model less sensitive to the number of tokens.

Generalization to Other Tasks: The paper notes that classification tasks do not align well with dense tasks like depth estimation and reconstruction. This indicates a potential limitation in the generalization of the learned representations to various tasks. Further exploration into how these representations can be adapted or extended to perform well across a wider range of tasks would be beneficial. Specifically, the paper should investigate the performance of the learned representations on tasks requiring different levels of abstraction, such as semantic segmentation or object detection.

### Questions
Please refer to the weakness.

### Soundness
3

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
This paper discusses a new approach to variable-length visual token representation learning that addresses the limitations of fixed-length representations for images. The method, AVT, processes image tokens recursively, refining them into 1D latent tokens over multiple iterations while adaptively increasing capacity by adding new tokens. The iterative process potentially facilitates object and part discovery based on image entropy and context.

### Strengths
1. The paper proposed a novel method, AVT, which distills 2D image tokens into 1D variable-length latent tokens, an important topic for Visual Representation Learning.
2. The experiments are solid and comprehensive.
3. The writing is clear and concise.

### Weaknesses
1. The reconstruction effect, FID, of their method AVT in Table 1 has no obvious outstanding improvement compared with existing methods, VQGAN and Tiktok, under the same number of tokens. While the paper introduces a novel approach to variable-length tokenization, the practical benefit in terms of reconstruction quality, as measured by FID, is not clearly demonstrated. The lack of a significant improvement raises questions about the overall effectiveness of the proposed method compared to established techniques.
2. Experimental results, in section 5 Further Experiments & Ablations, can be displayed in the form of figures and tables, which will make them more intuitive. The current presentation of ablation studies and further experiments relies heavily on textual descriptions, making it difficult to quickly grasp the trends and significance of the results. The absence of visual aids and tabular summaries hinders a clear understanding of the experimental outcomes.

### Questions
1. How to determine how many iterations are needed for each picture? I see that you have done a lot of interesting experiments, but currently, it can only be set manually through experiments. Can it be selected adaptively based on the amount of information, for example, information entropy for the image?
2. Compared to 2D fixed-length tokenizers like VQGAN, or distilled 1D fixed-length tokenization methods like Perciver. How much calculation and storage space does the AVT method increase? Is it much slower than the above two methods through iterative reconstruction in AVT?
3. Tab.1 shows that the FID reconstructed through your method is worse than Tiktok and VQGAN. As you explain in line 453, the datasets for training and evaluation are different. Have you tried the experiment under the same situation?

### Soundness
4

### Presentation
3

### Contribution
3
