# Compositional VQ Sampling for Efficient and Accurate Conditional Image Generation

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Compositional diffusion and energy-based models have driven progress in controllable image generation, however the challenge of composing discrete generative models has remained open, holding the potential for improvements in efficiency, interpretability and generation quality. To this end, we propose a framework for controllable conditional generation of images. We formulate a process for composing discrete generation processes, enabling generation with an arbitrary number of input conditions without the need for any specialised training objective. We adapt this result for parallel token prediction with masked generative transformers, enabling accurate and efficient conditional sampling from the discrete latent space of VQ models. In particular, our method attains an average error rate of 19.3% across nine experiments spanning three datasets (between one and three input conditions for each dataset), representing an average 63.4% reduction in error rate relative to the previous state-of-the-art. Our method also outperforms the next-best approach (ranked by error rate) in terms of FID in seven out of nine settings, with an average FID of $24.23$, and average improvement of $-9.58$. Furthermore, our method offers a $2.3\times$ to $12\times$ speedup over comparable methods. We find that our method can generalise to combinations of input conditions that lie outside the training data (e.g. more objects per image for Positional CLEVR) in addition to offering an interpretable dimension of controllability via concept weighting. Outside of the rigorous quantitative settings, we further demonstrate that our approach can be readily applied to an open pre-trained discrete text-to-image model, demonstrating fine-grained control of text-to-image generation. The accuracy and efficiency of our framework across diverse conditional image generation settings reinforces its theoretical foundations, while opening up practical avenues for future work in controllable and composable image generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces an composition algorithm that enables compositional generation (like score composition in EBM [1] or diffusion [2]) for discrete diffusion models or masked generation models. The method is straightforward, effective, and aligns well with intuitive understanding. The authors evaluate their approach on diverse datasets, including Positional CLEVR, Relational CLEVR, and FFHQ, demonstrating strong results.


[1] Du, Yilun, Shuang Li, and Igor Mordatch. "Compositional visual generation with energy based models." Advances in Neural Information Processing Systems 33 (2020): 6637-6647.

[2] Liu, Nan, Shuang Li, Yilun Du, Antonio Torralba, and Joshua B. Tenenbaum. "Compositional visual generation with composable diffusion models." In European Conference on Computer Vision, pp. 423-439. Cham: Springer Nature Switzerland, 2022.

### Strengths
- The study addresses a relatively unexplored area of compositional generation within discrete diffusion and masked generative models, complementing the majority of prior work focused on EBMs or continuous diffusion models. This contributes meaningfully to the field.
- The proposed approach is straightforward, effective, and intuitive, producing promising empirical results across various datasets.

### Weaknesses
 - Lines 191-192 use the phrase “statistically independent of each other,” which may be ambiguous and potentially misleading. It could imply a graphical model with $c_i$ nodes pointing to $x$. My understanding is that equation (1) is derived directly from the product of experts assumption, similar to equation (4) in [1]. The assumption of conditional independence given $x$ should be explicitly stated and justified, especially since the conditions $c_i$ could have underlying dependencies that are not explicitly modeled.
- The method essentially adopts a specialized form of classifier-free guidance (CFG), which has been explored in [3] and has been widely implemented in autoregressive and discrete diffusion models. While the authors' method applies a product-of-experts approach, the underlying mechanism of combining conditional and unconditional scores is fundamentally similar to CFG. The novelty of the approach is therefore questionable, as it appears to be an adaptation of existing techniques to a new problem setting rather than a fundamentally new approach. The claim of theoretical novelty needs stronger justification.
- The paper provides results for compositional operations like AND and NOT, but does not address OR, leaving a gap in the evaluation. The lack of results for the OR operation is a significant omission, as it is a fundamental Boolean operation and should be included for a comprehensive evaluation of the compositional capabilities of the proposed method. This limits the conclusions that can be drawn about the general applicability of the method.

### Questions
- It is unclear how equation (3) follows from equation (2). Could this approach face the same issues highlighted in [4]?

[4] Du, Yilun, Conor Durkan, Robin Strudel, Joshua B. Tenenbaum, Sander Dieleman, Rob Fergus, Jascha Sohl-Dickstein, Arnaud Doucet, and Will Sussman Grathwohl. "Reduce, reuse, recycle: Compositional generation with energy-based diffusion models and mcmc." In International conference on machine learning, pp. 8489-8510. PMLR, 2023.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a new approach for compositional image generation for discrete generative processes, leveraging a compositional code sampling framework applied to discrete spaces with Vector-Quantization technique, and masked token prediction method for efficient image generation. The proposed method combines log-probabilities of discrete generative models, allowing control over compositional generation conditions without specialized training loss. Results across various settings show SOTA performance in terms of accuracy and FID, with notable efficiency improvements compared to continuous methods. The method also integrates seamlessly with pre-trained text-to-image generation models, offering practical applications for controllable image generation.

### Strengths
1. Novelty: The approach is the first of its kind to apply compositional generation to discrete latent spaces, offering potential for increased efficiency and interpretability over traditional continuous sampling.
2. Applicability: Can be integrated with pretrained text-to-image models without fine-tuning, showing its broad applicability and ease of use.
3. Efficiency: The method is computationally efficient, delivering significant speed-ups over continuous methods, making it more practical for real-time or large-scale applications.

### Weaknesses
1. Although this work introduces the first approach for compositional image generation in discrete space, the methodology itself appears similar to ‘concept conjunction’ used in compositional diffusion models [1] within continuous space. Additionally, the rationale behind why the composition technique from continuous space models cannot be directly applied to discrete space remains unclear (as both approaches appear to rely on the composition of log-probabilities). Furthermore, the trade-offs mentioned in the introduction lack sufficient clarity and specificity. Specifically, the paper does not clearly articulate the limitations of applying continuous space composition techniques to discrete latent spaces, nor does it provide a detailed explanation of the theoretical differences that necessitate a new approach. The discussion of trade-offs should be more precise, detailing how specific parameters of the masked generative model (e.g., sampling temperature, number of tokens per timestep) affect the quality and diversity of generated images, and how these trade-offs compare to those in continuous models.
2.	Limited Scope in Evaluated Datasets: The datasets are somewhat limited in complexity (CLEVR, FFHQ). More complex datasets with more varied attributes could better test the method’s generalization. The CLEVR datasets, while useful for controlled experiments, do not fully represent the complexities of real-world image composition. The FFHQ dataset, with only three binary attributes, is also limited in its ability to evaluate the method's performance on more complex compositional tasks. Testing on datasets with a larger number of attributes, more complex relationships between attributes, and greater visual diversity would provide a more robust evaluation of the method's generalization capabilities.

### Questions
1.	How does the proposed compositional VQ sampling method perform when applied to autoregressive-based models?
2.	Regarding the influence of weighting values on attributes:
 * Is the range of weights (e.g., -3 to +3) shown in Figure 6 applicable to all attributes, or does it require tuning for each attribute?
* When involving multiple components, how does varying the weight for each component affect the final generated result? Specifically, how do different weight values interact across components?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper investigates multiple conditioning approaches for the Masked Generative Image Transformer, focusing on the composability of multiple predictions. The authors demonstrate that using multiple conditioning signals improves control over the generation process. Their approach shows substantial improvements across three datasets, significantly reducing the error rate in conditional image generation. Additionally, they present interesting properties for negative conditioning and out-of-distribution generation for text-to-image tasks.

### Strengths
- The paper demonstrates strong results in terms of error rate reduction, highlighting effective conditioning.
- The method leverages the MaskGIT framework, achieving high throughput (compared to diffusion models) while maintaining a low parameter count.
- The paper also reveals interesting properties for out-of-distribution (OoD) synthesis and negative prompting

### Weaknesses
 - The contribution of conditioning the model alone is already well-established through Classifier-Free Guidance (CFG). Applying this technique for multiple conditions for discrete spaces may be a weak contribution. While the authors provide a derivation for compositional conditional generation, the core idea of combining multiple conditions is not novel, and the application to discrete masked generative models, while technically sound, does not represent a significant conceptual leap. The paper would benefit from a more thorough discussion of how this approach differs fundamentally from existing methods beyond the specific architecture used.
- While the manipulation of text-to-image conditioning appears promising, the lack of quantitative results makes it difficult to fully assess its effectiveness. The qualitative results, while visually appealing, are not sufficient to demonstrate the robustness and generalizability of the approach. I think that the complete Figure 13 in the main paper would enhance clarity. The absence of metrics such as CLIP score or other relevant metrics for text-to-image generation makes it hard to evaluate the true impact of the proposed method in this domain.
- Similar to other methods (e.g., [7]), this approach requires additional forward passes, which slow down the overall pipeline. The paper does not adequately address the computational overhead associated with these additional passes, nor does it provide a detailed analysis of the trade-off between improved control and increased computational cost. A more thorough investigation of the efficiency of the method, including a comparison with alternative approaches, is needed.
- The method shows a relatively weak FID score on the FFHQ dataset. While the authors achieve a reduction in error rate, the FID score indicates a potential loss of diversity in the generated images. This trade-off between accuracy and diversity needs to be more carefully examined, and the paper should discuss the implications of this limitation in more detail. The fact that the FID score degrades significantly with the increase in the number of conditioning components raises concerns about the scalability of the approach.

### Questions
- Why does the FID score change when the number of components varies that much (particularly for Table 3)?
- For out-of-distribution synthesis, under what conditions does the model fail? Can it generate more than eight objects? 
- What happens in the case of synthesizing both 𝑐  and −𝑐 ?  
- Is it necessary to maintain all conditioning signals until the end of the generation process? For instance, on FFHQ, conditioning on glasses for the first few iterations and switch to no condition?
- Is the current format for references correct?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a compositional approach for image generation. The authors proposes to incorporate multiple conditions within a discrete masked transformer generation. Under the assumption that these conditions are independent, each condition contributes to the discrete denoising of the masked latent space at each diffusion time. 
 The conditions are shown to control the specific attributes, both positively and negatively, as well as generate high quality images both quantitatively and qualitatively. In addition, the method is shown to be applicable to pre-train t2i discrete diffusion namely aMUSEd).

### Strengths
- The paper is well written and easily understood
- The results support the claims
- The conditions are able to generalize to OOD sampling

### Weaknesses
My main concern is the novelty of this paper.
Masked diffusion transformers are not new as noted by the author it is used for example in aMUSEd.
In addition compositional conditions was presented in "Compositional Visual Generation with Composable Diffusion Models" which derive the same conjunction and negation attributes.  While their are some differences (the use VQ-VAE vs VQGAN) the method can be seem as a compositional aMUSEd, which is quite limited in novelty.
I wish the authors to better explain what exactly this work proposes that aMUSEd and compositional conditions did not.

- The conditions are entangled with other attributes as can be seen in Fig 6.
- Each condition requires a forward pass, in an already slow diffusion generation process.
- Low resolution image generation.

### Questions
- Please address the novelty concern and other weakness mentioned in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2
