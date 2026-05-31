## Human Reviewer 1

### Summary
This paper proposes NVDP (Nonparametric Variational Differential Privacy), a new method to provide local differential privacy for transformer embeddings. The motivation stems from the observation that transformer hidden states may leak sensitive information, allowing adversaries to reconstruct or infer private attributes. To mitigate this, the authors integrate a Nonparametric Variational Information Bottleneck into a transformer encoder. NVIB, based on a Dirichlet Process latent prior, stochastically samples weighted vectors (token-level embeddings) that preserve utility while controlling information flow. The method injects learned, task-calibrated noise into embeddings, and privacy is quantified via Rényi Differential Privacy and converted into interpretable Bayesian Differential Privacy guarantees.

### Strengths
- The paper is well structured, with clear separation between background, method, and experiments.
- Introduces the first integration of NVIB and differential privacy within transformer architectures, bridging information bottleneck theory and formal privacy guarantees.
- Provides a viable way to share transformer embeddings safely.

### Weaknesses
- NVIB sampling and RD computation over all input pairs are expensive (O(n²) pairs). No runtime, memory, or scalability analysis is provided.
- While the paper repeatedly claims local DP, its formulation (sampling embeddings within the model) seems effectively performs mechanism-level DP, not user-level DP.

### Questions
- How tight is your analytical RD bound (Eq. 7)? Any empirical validation or confidence intervals?
- How does NVDP compare with other DP mechanisms on the same tasks?
- What is the computational overhead (training time per epoch, GPU hours)?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes NVDP (Nonparametric Variational Differential Privacy), a framework that integrates Bayesian DP and RDP with a nonparametric variational information bottleneck (VIB). The approach aims to achieve privacy-preserving embeddings by learning stochastic representations that limit mutual information between inputs and embeddings. NVDP introduces internal probabilistic noise through a variational layer parameterized by $\mu, \sigma, \alpha$. The model thus learns to generate privacy-compliant embeddings by minimizing the expected RDP distance between output distributions across data samples.

### Strengths
- S1: Conceptually appealing integration: The unification of RDP and BDP within an information bottleneck formulation is a novel and elegant conceptual contribution. It provides a fresh probabilistic perspective on DP, reframing privacy as information compression rather than explicit noise injection.
- S2: Learning-based noise adaptation: Unlike conventional DP mechanisms with fixed noise levels, NVDP allows the model to adapt its internal noise dynamically via learned parameters $(\sigma(x), \alpha(x))$. This could, in principle, improve the privacy–utility trade-off.

### Weaknesses
- W1: Lack of practical validation: The experiments do not convincingly demonstrate real-world usefulness. It remains unclear for which downstream applications (e.g., classification, retrieval, or fine-tuning) the learned embeddings preserve performance while providing privacy.
- W2: While $\epsilon$ is computed through RDP/BDP metrics, it is not specified or controlled in the same way as standard DP. The reader cannot interpret what an obtained $\epsilon$ actually means in practical or regulatory terms.
- W3: Since the model operates under a local DP assumption, each client may achieve a different effective privacy strength. The implications for consistency, fairness, and aggregation are not discussed.
- W4: Approximate, not formal DP guarantees: The framework measures privacy using divergence bounds but does not prove formal composition or post-processing guarantees. As a result, it is more accurately described as ``DP-inspired” rather than strictly DP-compliant.
- W5: Despite the emphasis on ``Transformer embeddings,” the proposed method does not exploit any specific properties of Transformer architectures. The model merely applies the NVDP layer on top of general embeddings, meaning that the approach could equally apply to CNNs or MLP-based encoders.

### Questions
Address W1-5.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper proposes Nonparametric Variational Differential Privacy (NVDP) that offers privacy protection on transformer embeddings. It modifies NVIB by noisy embedding sampling and subsequent denoising, providing RDP and BDP guarantee. Experiment results demonstrate that NVDP effectively balance privacy and utility.

### Strengths
- The paper tackles a real-world problem of privacy-preserving data sharing.
- This paper adapts NVIB to provide formal privacy guarantee during embedding sharing.
- NVDP offers better privacy and utility trade-off compared with the baselines.

### Weaknesses
- The experiment lacks comparison with existing DP baselines [1][2].
- The discussion on neighboring dataset is vague. It is unclear how the neighbors map to the token/sentence scenario.
- The experiment lacks attack analysis on the privatized embeddings, such as 

[1] Du, M., Yue, X., Chow, S. S., & Sun, H. (2023, April). Sanitizing sentence embeddings (and labels) for local differential privacy. In Proceedings of the ACM Web Conference 2023 (pp. 2349-2359).

[2] Meehan, C., Mrini, K., & Chaudhuri, K. (2022, May). Sentence-level Privacy for Document Embeddings. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (pp. 3367-3380).

### Questions
NA

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3