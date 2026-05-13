# Mix-LN: Unleashing the Power of Deeper Layers by Combining Pre-LN and Post-LN

- Decision: Accept
- Scores: 6, 5, 8, 6, 6

## Abstract
Large Language Models (LLMs) have achieved remarkable success, yet recent findings reveal that their deeper layers often contribute minimally and can be pruned without affecting overall performance.  While some view this as an opportunity for model compression, we identify it as a training shortfall rooted in the widespread use of Pre-Layer Normalization (Pre-LN). We demonstrate that Pre-LN, commonly employed in models like GPT and LLaMA, leads to diminished gradient norms in its deeper layers, reducing their effectiveness. In contrast, Post-Layer Normalization (Post-LN) preserves larger gradient norms in deeper layers but suffers from vanishing gradients in earlier layers. To address this, we introduce Mix-LN, a novel normalization technique that combines the strengths of Pre-LN and Post-LN within the same model. Mix-LN applies Post-LN to the earlier layers and Pre-LN to the deeper layers, ensuring more uniform gradient norms across layers. This allows all parts of the network—both shallow and deep layers—to contribute effectively to training. Extensive experiments with various model sizes demonstrate that Mix-LN consistently outperforms both Pre-LN and Post-LN, promoting more balanced, healthier gradient norms throughout the network, and enhancing the overall quality of LLM pre-training. Furthermore, we demonstrate that models pre-trained with Mix-LN learn better compared to those using Pre-LN or Post-LN during supervised fine-tuning, highlighting the critical importance of high-quality deep layers. By effectively addressing the inefficiencies of deep layers in current LLMs, Mix-LN unlocks their potential, enhancing model capacity without increasing model size. Our code is submitted.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper the authors context the employment of either pre-layer normalization (Pre-LN) and post layer normalization. (Post-LN) They bring an argument showing vanishing gradient for earlier or later layers. Building on this intuition, they propose to place post-LN in early layers and pre-LN in later ones, to maximize the gradient. The evaluation is performed on LLMs, either large and small scale ones.

### Strengths
- The observation related to gradient norm brought by LN is interesting, clear, and straight to the point.
- Part of the quantitative evaluation is conducted to large-scale LLMs, making this work actual.
- All the empirical evaluation is quite realistic and likely correct.
- Figures in general do an excellent job in providing a display on the distributions.

### Weaknesses
 - The relative gains in terms of perplexity/accuracy for larger model slims down. This in a certain sense contradicts the vanishing gradient argument. Besides, the gap compared to pre-LM becomes slower and slower.
- The success of the approach depends on $\alpha$: there are cases like Llama-1B for BoolQ in which only pre-LM performs better, indicating that tuning $\alpha$ properly can be determinant.
- Metrics are not always complete: I could not find, for example, performance drop when using Mix-LN

### Questions
- How does the performance drop when using Mix-LN?
- Is this approach still valid for other tasks (like for example image classification, with a Transformer architecture on ImageNet-1k)?
- Have the authors attempted to compare with other normalization techniques (like group normalization)?
- Can the authors provide theoretical boundaries to the vanishing/exploding gradient conditions for equations (3) and (4)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Mix-LN, a hybrid normalization approach that combines Pre-Layer Normalization (Pre-LN) and Post-Layer Normalization (Post-LN) within large language models (LLMs). The technique leverages Post-LN in shallow layers to mitigate gradient vanishing and Pre-LN in deeper layers to maintain gradient flow, with the aim of maximizing layer effectiveness throughout the network. While Mix-LN demonstrates some empirical gains, especially in mid-sized LLMs, the contribution remains incremental in the broader landscape of normalization techniques for LLMs. The paper’s main contributions are primarily empirical, and it lacks a strong theoretical foundation to substantiate why Mix-LN improves gradient dynamics compared to recent normalization methods.

### Strengths
- Novel Approach to Gradient Flow in LLMs: Mix-LN’s hybrid approach to layer normalization is unique, attempting to combine the advantages of Pre-LN and Post-LN across different model depths.

- Good Experimental Validation: The paper includes extensive experimentation on multiple model sizes and tasks, showing consistent improvement with Mix-LN, particularly in mid-sized models.

- Improved Training Stability: Mix-LN appears to mitigate some of the training instability issues commonly observed with Post-LN in large models, an advantage for practitioners.

### Weaknesses
 - Lack of Theoretical Rigor: The paper does not provide a detailed theoretical framework to explain why Mix-LN achieves balanced gradient dynamics across layers, which is crucial for the paper’s validity. In the well-explored field of normalization for LLMs, incremental changes require more substantial theoretical backing to make a notable contribution.

- **Limited Comparison** with State-of-the-Art Normalization Techniques: The paper lacks direct comparison with recent normalization methods, such as Admin or Sandwich LN, which also address deep-layer gradient inefficiencies. Without these comparisons, it’s challenging to assert Mix-LN’s effectiveness over other recent innovations.

- **Diminished Gains on Very Large Models**: The benefits of Mix-LN become less pronounced in very large models, such as LLaMA-1B, where performance gains are smaller. This suggests potential scalability issues for Mix-LN in ultra-large models like 7B, 13B and so on, which is a limitation given the trajectory of LLM research.

- Applicability Limited to LLMs: Mix-LN has only been evaluated on LLMs, and its effectiveness on non-language models or other architectures remains untested. This limits the broader applicability and impact of the approach.

- Hyperparameter Sensitivity Not Thoroughly Explored: The paper does not fully address the sensitivity of the hyperparameter 𝛼 (controlling the transition point between Pre-LN and Post-LN), which could impact Mix-LN’s practical usability across different settings.

### Questions
- Could the authors provide more insights or theoretical justifications for why Mix-LN enhances gradient flow differently across shallow and deep layers?

- How does Mix-LN perform when compared to other recent normalization methods, such as Admin or Sandwich LN?

- How sensitive is Mix-LN to the hyperparameter 𝛼, and is this value stable across different tasks and model scales?

- Can the authors clarify Mix-LN’s computational impact during training? Does it introduce any additional training or inference overhead?

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
The paper introduced Mix-LN, which applies Pre-LN and Post-LN in different parts of the LLMs. The author explore the diminished gradient norms of Pre-LN in deeper layers and vanishing gradient of Post-LN in earlier layers, both theoretically and experimentally. They then conduct the experiments comparing Post-LN, DeepNorm, Pre-LN and Mix-LN in pre-training and fine-tuning, with anaylsis on the results. The results show Mix-LN with certain ratios improves the overall capacity and efficiency of LLMs.

### Strengths
1. This paper is very well-organized.
2. This paper introduce the problem with theortical anaysis and strengthen with experiments, which makes the problem clear and well-motivated.
3. Comprehensive experiments for presenting the effect of Mix-LN.
4. The anaysis are insightfull.

### Weaknesses
1. This figures of angular distance are somewhat non-intuitive. Can't understand on the first sight. Block size more like describing the size of the model than distance between two layers under comparison. The first detailed description is actucally in line 402-403.
2. Typo problem: Figure 3-c (in main body) or Figure 3-e (in caption of Figure 3).

3. Figure 4: a&b shows exact opposite result than Figure 2/3. From my understanding, the angular distance will grow bigger (the color will thus go dark) as the distance between two layers increases. However, for example in layer 10 of Figure 4-b, the farthes has smallest angular distance. Please correct me if I am mistaken.

### Questions
1. Figure 2-a: Could you explain the triangle-like yellow areas (which also appears but no so significiant in Figure 2-b)? It seems to be discontinuous changes in angular distance between near or adjacent layers. However, from my understanding, the transformer blocks in BERT are the same. Therefore what makes layer 5/6 or 14/15 so special?
2. Figure 2-b: Could you explain the dark-blue line on the right? It seems to be a significiant change of angular distance in last layer.
3. Section 4: Minor comments. There was no introduction for perlexity?
4. Figure 4: a&b shows exact opposite result than Figure 2/3. From my understanding, the angular distance will grow bigger (the color will thus go dark) as the distance between two layers increases. However, for example in layer 10 of Figure 4-b, the farthes has smallest angular distance. Please correct me if I am mistaken.

### Soundness
4

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
4

### Summary
This paper addresses the inefficiency of deeper layers in Large Language Models (LLMs) by introducing Mix-LN, a novel normalization technique that combines Pre-Layer Normalization (Pre-LN) and Post-Layer Normalization (Post-LN). The authors argue that the widespread use of Pre-LN in models like GPT and LLaMA leads to diminished gradient norms in deeper layers, reducing their effectiveness. Mix-LN applies Post-LN to earlier layers and Pre-LN to deeper layers, ensuring more uniform gradient norms across all layers. Through extensive experiments across various model sizes, the authors demonstrate that Mix-LN consistently outperforms both Pre-LN and Post-LN, promoting more balanced gradient norms throughout the network and enhancing the quality of LLM pre-training and fine-tuning. This approach aims to unlock the full potential of deeper layers in LLMs, improving model capacity without increasing model size.

### Strengths
1. This article conducts a good experimental analysis and points out that the gradient norm of Pre-LN and Post-LN shows different trends as the number of layers increases.
2. Comprehensive experiments on both open-weight and in-house models, with multiple evaluation metrics (Angular Distance, Performance Drop, Gradient Norm).
3. Well-structured presentation and logical flow with clear diagrams and mathematical formulations.

### Weaknesses
1. **Limited Theoretical Foundation:** The paper lacks rigorous mathematical analysis of Mix-LN's properties, particularly in contrast to well-established theoretical frameworks for methods like DeepNorm[1]. This absence of formal proofs for convergence properties and optimal ratio selection limits our understanding of the method's fundamental principles. Specifically, the paper does not provide a clear derivation of the conditions under which Mix-LN will converge, nor does it offer insights into how the transition point between Pre-LN and Post-LN layers affects the overall optimization landscape. A more detailed analysis of the Hessian of the loss function under Mix-LN would be beneficial to understand the curvature and stability of the optimization process.

2. **Scale Limitations:** By restricting experiments to models up to 1B parameters and primarily using LLaMA-based architectures, the work lacks demonstrating scalability to production-scale models (7B-175B parameters) or generalizability across different architecture families. The performance of normalization techniques can vary significantly with model size and architecture, and it is unclear whether the observed benefits of Mix-LN will hold for larger models or models with different architectural designs, such as those employing different attention mechanisms or activation functions. The paper should include a discussion of the potential challenges and limitations of applying Mix-LN to different model scales and architectures.

3. **Incremental Innovation:** The proposed Mix-LN solution, while practical, represents a relatively straightforward combination of existing techniques rather than a fundamental advancement in normalization methodology, especially given extensive prior work referenced in related work and other forums[2,3] in this domain. While the authors show empirical improvements, the core idea of combining different normalization layers is not entirely novel, and the paper does not sufficiently demonstrate a significant theoretical or conceptual leap in our understanding of normalization techniques.

### Questions
1. **Scaling Properties:** How does Mix-LN perform in very large models (>7B parameters), and what theoretical guarantees can be provided for its effectiveness at scale?

2. **Boundary Dynamics:** What are the theoretical considerations and potential instabilities at the transition point between Pre-LN and Post-LN layers?

3. **Asymptotic Performance:** While accelerated convergence is demonstrated, how does Mix-LN's final performance compare to Post-LN when both are trained to complete convergence under same hyperparameter settings? A controlled study with matched configurations training until performance plateaus would help distinguish whether Mix-LN's benefits extend beyond computational efficiency to fundamental improvements in model capability.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper identifies an training shortfall of LLMs that their deep layers contribute minimally to the overall performance, which wastes the model capacity. The paper identifies the reason behind this as the use of Pre-LN leading to diminished gradients in later layers. The paper further proposes to use a mixed LN approach, where post-LNs are applied to the earlier layers and pre-LNs to the later layers. Experiments show enhancement brought by the mixed LN approach in both pretraining and supervised finetuning.

### Strengths
This paper provides novel and interesting insights on the different impact of pre/post LN in the training behavior of earlier and later layers. The observation leads to a straightforward solution of applying mixed LN, which can be easily applied in all models. The paper is well-written and easy to follow. Experiments on multiple models and tasks, as well as ablation studies show solid performance improvement of the proposed method.

### Weaknesses
One major weakness of this paper is that the provided results are not adequate to support the claim that mixed-LN helps deep model by allowing both shallow and deep layers contributes effectively. From the main results in Tab. 1 and 2, it appears that mix-LN improves more over pre-LN in that smaller 71M model (12 layers) than the deeper 1B model (32 layers), which seems to suggest the benefit of mix LN is less in deep models. It would be better to provide results of even larger and deeper models to show that the benefit of mix LN do scale up. If computation resource is limiting the further experiments on larger models, trying a slim but deep architecture may be helpful to verify the effectiveness of the proposed method. Furthermore, the paper does not adequately address the sensitivity of the mixed-LN approach to the choice of the mixing ratio, alpha. The optimal value of alpha may vary significantly depending on the model architecture and size, and the paper lacks a clear methodology for selecting this hyperparameter. This could limit the practical applicability of the method, as users would need to perform extensive hyperparameter tuning for each new model.

### Questions
See weakness part. I would like to see more evidence that the proposed method helps more on deeper models.

### Soundness
3

### Presentation
3

### Contribution
2
