# FIG: Flow with Interpolant Guidance for Linear Inverse Problems

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Diffusion and flow matching models have been recently used to solve various linear inverse problems such as image restoration. Using a pre-trained diffusion or flow-matching model as a prior, most existing methods modify the reverse-time sampling process by incorporating the likelihood information from the measurement. However, they struggle in challenging scenarios, e.g., in case of high measurement noise or severe ill-posedness. In this paper, we propose Flow with Interpolant Guidance (FIG), an algorithm  where the reverse-time sampling is efficiently guided with measurement interpolants through theoretically justified schemes. Experimentally, we demonstrate that FIG efficiently produce highly competitive results  on a variety of linear image reconstruction tasks on natural image datasets. We improve upon state-of-the-art baseline algorithms, especially for challenging tasks. Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a method, FIG, to pre-train a flow matching or diffusion model to be used as a prior to solve linear inverse problems. FIG considers the conditioning on the measurements in the diffusion process. However, instead of using the direct measurement y, it conditions on the “measurement interpolants” y_t, as it generates x_t. The authors show that for specific choices of the interplant, the relationship between the signal x_t and the measurement y_t hold with the same linear model of the inverse problem (and adjusted additive noise magnitude).
Theoretical guarantees are provided for the correctness of the proposed optimiser and sampler. FIG is also tested on several inverse problems (SR x4/x16, Gaussian/Motion deblurring, inpainting) and yields state of the art results.

### Strengths
The idea of measurements interpolants seems intuitively good and is clearly supported by the experiments (with state of the art performance especially in very challenging cases).
The authors also introduce the background in both flow matching and diffusion models, and provide some theoretical proof that the proposed method is valid given that Assumption 1 holds.
The proposed method in essence is quite simple and easy to implement (as a change to existing uses of pre-trained flow matching or diffusion models).

### Weaknesses
The presentation could be improved to explain much more clearly the motivation behind FIG.
What are the issues that other methods could not address and that FIG does address? 
My current understanding is that one _can_ condition on the measurement interpolants and then in the conclusions there is a comment that it is easier to create the interpolants than to denoise the signal.
I would suggest to include a specific subsection that explains:
1) What limitations exist in how other methods condition on measurements
2) How measurement interpolants address those limitations
3) Why conditioning on interpolants is theoretically or empirically advantageous

It would then be necessary to demonstrate in the experiments how these limitations are not addressed
by other methods but are addressed by FIG.

### Questions
1) I would like to know the motivation for the measurement interpolants. I have an intuition of why they are used, but I could not find that in the paper and I would like the authors to explain; More precisely, I am asking what was wrong with the conditioning of other methods and how this new approach makes that right.
2) I would like to have an explanation for what each of the theorems contributes. Possibly this is connected to the previous point. I suggest to 1) add a brief paragraph after each theorem explaining its practical implications; 2) include a discussion subsection that ties together how the theorems collectively justify or enable the proposed method; 3) provide intuitive explanations or examples to complement the formal mathematical statements.

### Soundness
3

### Presentation
2

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
This paper proposed a solution for solving linear inverse problem with flow matching model. The author provides both theoritecal justification and experiment results to support the claim that the proposed method can efficiently handle challenging linear inverse problems.

### Strengths
This paper is well-written with both theoretical claim and experiment results.
The model can be deployed in both diffusion and flow matching scenarios.

### Weaknesses
Technically, the paper lacks significant contributions that clearly distinguish it from prior work. My concerns are as follows:

1. **Inverse Problem Approach**: Solving an inverse problem with pre-trained diffusion/flow matching models typically involves classifier guidance by designing a robust $q(y|x_t)$ term, as Bayes’ rule suggests: $
abla p(x|y) = 
abla p(x) + 
abla p(y|x)$. However, the authors do not propose a novel method for posterior estimation. Equation (16) indicates that this work uses a reconstruction guidance scheme. While not explicitly stated, this appears similar to the approach in [1], although the specific implementation details differ.

2. **Application of Existing Methods**: This paper seems primarily focused on adapting existing reconstruction guidance techniques to flow matching models, with only minor adjustments to weighting terms. The core methodology appears to be a direct application of existing methods to a different generative model architecture. The authors should elaborate on the specific novelties in applying these techniques to flow matching, beyond a simple adaptation.

3. **Theorem 1**: This theorem, while presented as a key contribution, has been discussed in previous work. For example, [2] provides a proof connecting unconditional flow and score-based models in Appendix F. Similarly, [3] and [4] offer similar proofs for inverse problem solutions. Therefore, Theorem 1's novelty is questionable and might be better suited for the appendix, rather than being highlighted as a primary contribution.

4. **Omission of Related Work**: The paper omits mention of highly related work, such as [4], which specifically addresses efficiency in solving inverse problems using both flow matching and diffusion models. As this work was posted on arXiv in May, it should be acknowledged, and I recommend that the authors review it thoroughly.

5. **Efficiency Claims**: The authors assert, "Despite promising experimental results, we find prior works struggle to efficiently handle challenging linear inverse problems," which is questionable. The key contribution here appears to be an additional iterative update at each ODE solving step (Algorithm 1, lines 7-8), introducing a hyperparameter $K$. For $K > 1$, this approach could increase inference time due to additional gradient calculations. Although this gradient term may not be computationally prohibitive for linear transformations $A$, it could become costly for non-linear transformations. While the authors focus on the linear case, the method could potentially be extended to non-linear cases using heuristics, as seen in prior work. A more detailed analysis of the computational cost, especially for different values of $K$ and different types of transformations, would be beneficial.

    - **Efficient Inverse Problem Solutions**: Achieving efficiency typically involves (1) reducing NFE (Number of Function Evaluations) without sacrificing quality (e.g., some recent methods achieve NFE=5 for inverse problem solutions), and (2) avoiding costly gradient calculations. The paper should benchmark its NFE and compare it against state-of-the-art methods, particularly in challenging scenarios.

6. **Evaluation Metrics**: The evaluation could be improved. PSNR and SSIM are no longer reliable metrics for generative model assessment, especially when leveraging pre-trained unconditional models. Instead, metrics like FID and KID should be considered. These metrics are more aligned with human perception and are becoming standard in the field.

### Questions
See weakness above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces FIG, a novel algorithm that leverages pre-trained flow matching and diffusion models to solve linear inverse problems. The main contributions include:
FIG introduces a simple but effective method of guiding the reverse-time sampling process with measurement interpolants.
The authors provide a detailed theoretical explanation of FIG, deriving the updating scheme and showing its relation to the posterior log-likelihood.
FIG is evaluated on several image reconstruction tasks using flow matching and diffusion models, demonstrating its effectiveness and efficiency compared to state-of-the-art baselines.

### Strengths
FIG is a novel approach to solving linear inverse problems that combines pre-trained generative models with a theoretically justified interpolation-based guidance scheme. It distinguishes itself from existing methods by directly incorporating measurement information during the reverse sampling process.
The paper presents a well-defined algorithm with strong theoretical justification. The empirical evaluation is comprehensive, covering various tasks and datasets, with thorough comparisons to relevant baselines.
The paper is clearly written and well-structured. The authors effectively explain the core concepts of flow matching and diffusion models, and provide a detailed explanation of FIG. The algorithm is presented in a clear pseudocode, making it easy to follow.
FIG offers a promising approach for tackling linear inverse problems with pre-trained generative models. Its efficiency, effectiveness, and theoretical grounding suggest a significant contribution to the field.

### Weaknesses
The paper acknowledges that FIG, as currently formulated, is not directly applicable to non-linear inverse problems or models with latent encodings. While this is a valid limitation, the authors could further discuss potential extensions or modifications to address these limitations. Specifically, the challenge of incorporating non-linear measurement operators into the measurement interpolant is not sufficiently explored. The paper also lacks a discussion on how the method would handle cases where the generative model operates in a latent space, which is common in many state-of-the-art generative models. 

The ablation study on the measurement interpolant variance rescaling technique could be further expanded. For example, visualizing the effects of different weight values (w) on the reconstructions could provide a more intuitive understanding of the impact of this parameter. The current analysis does not provide sufficient insight into how the choice of 'w' affects the trade-off between fidelity to the measurements and the prior imposed by the generative model. It would be beneficial to see a more detailed analysis of how this parameter interacts with the noise level in the measurements and the complexity of the reconstruction task.

### Questions
To further strengthen the evaluation and demonstrate the broad applicability of FIG, could the authors please consider comparing their approach against additional methods within the same domain, if available.
Could the authors discuss potential strategies for extending FIG to handle non-linear inverse problems?
What modifications would be needed to apply FIG to models with latent encodings?
The paper mentions the possibility of overfitting when applying FIG. Could the authors elaborate on this aspect, providing insights into how to mitigate this risk?

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
2

### Summary
This paper introduces an algorithm that efficiently guides reverse-time sampling using measurement interpolants, supported by theoretically grounded frameworks, to tackle image restoration tasks. The performance in the experiment is strong and surpasses previous methods like DDNM+. However, the novelty of the guidance design appears somewhat limited, and the scope of experimental comparisons could be expanded to provide a more convincing evaluation.

### Strengths
1. The proposed method is sound and the theoretical framework is well-written with mathematical formulations.
2. The experimental results seem nice.
3. The writing is clear and concise.

### Weaknesses
1. The method of using the gradient of reconstruction function to guide the generation direction has been widely explored in recent works. The technique in FIG lacks sufficient novelty in comparison to prior works. 
2. The experiments can be more detailed. The author can involve more related works like GDP[a] in comparisons. 
3. The effectiveness of the measurement interpolation is not verified in the experiments. The author should analyze it with some ablation studies.
4. The method has not been evaluated in blind scenarios. All degradation settings in this paper are fixed and known. However, real-world images suffer from complex and blind degradations. The author should show the performance on real-world samples.

### Questions
Performance with more base models. While the current experimental setup effectively demonstrates the validity of your approach, it would be interesting to assess how it performs with more recent open-source diffusion and flow models, like Flux 1.0, SD3, SDXL and other DiTs.

### Soundness
3

### Presentation
3

### Contribution
2
