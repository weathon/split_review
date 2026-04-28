# ESpeW: Robust Copyright Protection for LLM-based EaaS via Embedding-Specific Watermark

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Embeddings as a Service (EaaS) is emerging as a crucial role in AI applications. Unfortunately, EaaS is vulnerable to model extraction attacks, highlighting the urgent need for copyright protection. 
Although some preliminary works propose applying embedding watermarks to protect EaaS, recent research reveals that these watermarks can be easily removed. Hence, it is crucial to inject robust watermarks resistant to watermark removal attacks. 
Existing watermarking methods typically inject a target embedding into embeddings through linear interpolation when the text contains triggers. However, this mechanism results in each watermarked embedding having the same component, which makes the watermark easy to identify and eliminate. 
Motivated by this, in this paper, we propose a novel embedding-specific watermarking (ESpeW) mechanism to offer robust copyright protection for EaaS. Our approach involves injecting unique, yet readily identifiable watermarks into each embedding. Watermarks inserted by ESpeW are designed to maintain a significant distance from one another and to avoid sharing common components, thus making it significantly more challenging to remove the watermarks. 
Extensive experiments on four popular datasets demonstrate that ESpeW can even watermark successfully against a highly aggressive removal strategy without sacrificing the quality of embeddings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces ESPEW, a novel approach aimed at providing robust copyright protection for Embeddings as a Service (EaaS). Existing watermarking techniques have been found inadequate, as they can be easily removed by attackers. The authors propose a new watermarking method that injects unique, identifiable watermarks into embeddings, ensuring that these watermarks are difficult to detect and eliminate. The paper presents extensive experimental results demonstrating the effectiveness and robustness of the ESPEW method against various watermark removal attacks.

### Strengths
The proposed method effectively addresses the limitations of existing watermarking techniques by making it difficult for attackers to identify and remove watermarks. The use of distinct watermark positions in embeddings contributes to this robustness.
The authors conduct extensive experiments on four popular datasets under various removal intensities, showcasing the effectiveness of ESPEW compared to traditional methods.

### Weaknesses
Given the need to select specific positions in embeddings with the lowest magnitudes, this approach could impose a high computational load on servers, particularly under scenarios with heavy API usage. This might limit the applicability of ESpeW in high-demand environments or for EaaS providers with extensive traffic.

### Questions
See weekness

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
The paper introduces a novel watermarking technique (ESpeW) designed to protect IP for EaaS provided by LLMs. ESpeW aims to counteract model extraction attacks by embedding unique, hard-to-remove watermarks into each embedding instance. Unlike the existing methods that inject uniform watermark components across all embeddings, ESpeW uses selective, distinct watermark placements, making it more resilient against removal attacks.

### Strengths
1. ESpeW’s approach of using embedding-specific, non-uniform watermark placements addresses significant vulnerabilities in traditional methods. By ensuring that each embedding’s watermark location is unique, ESpeW can reduce the risk of watermark identification and removal, achieving robustness against targeted removal attacks.
2. The selective embedding technique of ESpeW allows the watermarks to remain mostly imperceptible, preserving the original embedding quality and minimizing any adverse effect on downstream task performance. 
3. The paper provides a clear framework for assessing key watermark properties, such as harmlessness, persistence, and resistance to permutation and unauthorized detection. The inclusion of metrics like cosine similarity, L2 distance, and the Kolmogorov-Smirnov (KS) test strengthens the credibility of ESpeW’s evaluation process.

### Weaknesses
1. ESpeW's robustness depends heavily on the confidentiality of the target embedding (used as a private key). If this target embedding were compromised, attackers could potentially reverse-engineer the watermark positions. This is a critical vulnerability, as the entire security of the watermarking scheme hinges on the secrecy of this single embedding. The paper does not adequately address the implications of a compromised key, particularly in scenarios involving sophisticated adversaries.
2. While ESpeW achieves robustness through selective watermark embedding, identifying the smallest-magnitude positions in each embedding may be computationally intensive for large-scale implementations. The paper lacks a thorough analysis of the computational overhead associated with this selection process, especially when dealing with high-dimensional embeddings and large datasets. This could limit the practical applicability of the method.
3. The method may be model-specific since different models can produce embeddings with varying distributions and magnitudes. The paper does not provide a detailed analysis of how the performance of ESpeW varies across different embedding models, and whether the selection of the smallest magnitude positions is equally effective for all models. This raises concerns about the generalizability of the proposed approach.

### Questions
1. To address the computational costs associated with selective position identification, the authors could consider evaluating approximate methods, such as random position selection or grouping embeddings with similar magnitude distributions, to balance efficiency and robustness.
2. Given ESpeW’s reliance on the confidentiality of the target embedding, discussing fallback mechanisms (e.g., embedding renewal or multiple target embeddings) could improve the resilience of the approach under various threat models.

### Soundness
2

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
This paper addresses the vulnerability of Embeddings as a Service (EaaS) to model extraction attacks, emphasizing the urgent need for robust copyright protection. Traditional watermarking methods are easily removed, leading to the development of our novel embedding-specific watermarking (ESpeW) mechanism. ESpeW injects unique, identifiable watermarks into each embedding, making them harder to detect and eliminate. Experiments on popular datasets demonstrate that ESpeW effectively resists aggressive removal strategies without compromising embedding quality.

### Strengths
1. The paper is well-written and well-organized.
2. The experimental results demonstrate the robustness of the watermarking method against CSE.

### Weaknesses
 1. The contribution seems limited, as the primary difference from EmbMarker [1] lies only in the embedding equation (Eq. (2)).
2. The contributions may be overstated. For contribution 2), this paper may not be the "first to propose" a robust watermark approach against CSE, as WARDEN [2] has already addressed this. For contribution 3), the claim that it is the "**only** method that remains effective" should be restricted to the baselines listed.
3. The paper claims that the “proposed method can inject watermark successfully with a minimum α value of 15%”. This implies that at least 15% of each embedding's values are directly replaced with the corresponding values from the target embedding e_t, which seems more detectable. Despite the different replacement positions in each embedding, the 15% replacement rate means that some positions will have the same values replaced. By statistically analyzing the frequency of values at each position, e_t might be estimated.
4. In section 4.4, the paper states "when the $\alpha$ is set to 100%, our method is almost the same as EmbMarker." However, when $\alpha$ is set to 100% in Eq. (1), all entries in M are 1, so e_p = e_t. This is significantly different from EmbMarker.

### Questions
1. WARDEN also claims to be effective against CSE. Why does this paper reach a different conclusion?
2. Minor issues:
    - Line 175: A period is missing before "Right".
    - Line 268: The comma position is incorrect "(,i.e., ...".
    - The citation format in the text is incorrect, affecting readability. Please use \citep and \citet correctly.

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
4

### Summary
This paper proposes a model watermarking method to protect the Embedding-as-a-Service (EaaS) model from model stealing. Specifically, this paper first selects various tokens. The sentences containing these tokens are regarded as trigger samples. If one of the trigger samples is input into the model, this paper proposes to replace part of the trigger sample's embedding with predefined values. Once an adversary utilizes the watermarked embeddings to train a model, the owner of the EaaS model can verify the ownership by validating whether the output embeddings of the trigger samples are more similar to the predefined values than the benign samples.

### Strengths
1. The method is robust to the removal attack, CSE.
2. This paper is generally easy to read.

### Weaknesses
1. **About the threat model:** This paper assumes that the adversary steals the EaaS model and trains its own EaaS model. In this case, the defender can get the output embeddings. However, I think a (maybe more) practical scenario is that the adversary steals the model and uses the model for a downstream task. In such a scenario, the defender can get the final output predictions instead of the embeddings. Is ESpeW proposed in this paper still effective in this scenario?
2. **About the hypothesis test:** This paper proposes to use the hypothesis test to validate whether the distributions of the cosine similarity values in set $C_b$ and $C_n$ are consistent. However, if two benign datasets that are not identically distributed are selected, it is also likely to reject the null hypothesis. Therefore, the reliability of the hypothesis test proposed in this paper is doubtful.
3. **About the robustness against permutation**: The authors claim that their method can resist permutation and they conduct experiments to prove so. However, I did not find the experimental results of this attack in the section of experiments (if I miss such an experiment, please kindly notify me).
4. **About the robustness against model-based attacks**: This paper only considers attacks that modify the output embeddings of the victim model. However, the adversary may also conduct model-based attacks. For instance, the adversary can adaptively design a loss function and fine-tune its model to remove the watermark inside the model.
5. **About the reliability**: This paper only tests whether the watermark can be extracted from the original model. It may be better for the authors to test more unwatermarked models with different architectures. Also, it is also necessary to further confirm whether it is possible for the randomly selected trigger samples and keys to pass the watermark verification. These experiments may comprehensively demonstrate the reliability of ESpeW.
6. **About the experimental results:** As shown in Table 1, the utility of the watermarked models are even higher than the original model. Considering that the proposed method is to replace part of the output embedding with arbitrary values and reduce the available features in the embedding, I think the results are abnormal. It may be better to provide a further study or analysis on the results.

### Questions
Please address the concerns in the weakness section.

### Soundness
2

### Presentation
3

### Contribution
2
