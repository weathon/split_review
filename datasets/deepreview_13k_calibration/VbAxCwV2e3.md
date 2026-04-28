# DC-DPM: A Divide-and-Conquer Approach for Diffusion Reverse Process

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
Diffusion models have achieved great success in generative tasks\textblue{, with the quality of generated samples guaranteed by their convergence properties, typically derived within the context of stochastic differential equations(SDE) and often involving Kolmogorov equations for proofs. This paper introduces a novel method for proving the convergence of diffusion models, which relies on direct estimation of distributions without the need for SDE tools. This approach inspires a \textbf{D}ivide-and-\textbf{C}onquer strategy for approximating the reversed transition kernel of \textbf{D}iffusion \textbf{P}robabilistic \textbf{M}odels (DC-DPM), which is not derived from SDEs, making previous convergence methods inapplicable. However, our method can be easily extended to accommodate this. As} our DC-DPM learns specific kernels for each partition \textblue{, these kernels require merging. According to the proof of convergence, we} design two merging strategies for these cluster-specific kernels along with corresponding training and sampling methods.
Experimental results demonstrate the superior generation quality of our method compared to the traditional single Gaussian kernel. Furthermore, our DC-DPM can synergize with previous kernel optimization methods, enhancing their generation quality, especially with a small number of timesteps.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a strategy called Divide-and-Conquer to accelerate the convergence of Diffusion Probabilistic Models. This approach begins by partitioning the data, allowing for separate learning of transition kernels for each partition. These transition kernels are then combined during both the training and sampling phases to form a unified model. The authors also provide a formal convergence proof for their proposed strategy, reinforcing its theoretical soundness. Experimental results on the CelebA and CIFAR-10 datasets demonstrate that the proposed method improves both the Fréchet Inception Distance (FID) and the visual quality of generated images, highlighting its effectiveness in practical applications.

### Strengths
- The paper presents a straightforward yet effective strategy to enhance the learning performance of Diffusion Probabilistic Models (DPMs).

- The authors also develop a convergence proof for the proposed method, providing a solid theoretical foundation that supports its reliability.

- Additionally, the manuscript is well-organized and clearly presented.

### Weaknesses
 - The paper presents numerous theorems, but it is unclear which are original contributions. Proper citation of existing results is needed to clarify which findings are novel and which build on prior work.
- The evaluation is limited to two datasets, which may not comprehensively assess the proposed method’s effectiveness. Including additional datasets would improve the robustness of the benchmarking.
- Only one baseline method is compared, despite significant related work in kernel representation that could serve as relevant baselines.
- The qualitative results in Figure 3 provide generated images with minimal discussion and analysis, limiting insights into the model's qualitative performance.

### Questions
What is the difference between DC-DPM and GMS, which use GMM as kernels?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a Divide-and-Conquer strategy to improve the traditional single Gaussian transition kernel representation in each denoising step of Diffusion Probabilistic Models (DC-DPM), enhancing generation quality particularly over a limited number of timesteps. By dividing the data into clusters, our DC-DPM learns specific kernels for each partition.

### Strengths
A Divide-and-Conquer strategy to improve the traditional single Gaussian transition kernel representation in each denoising step of Diffusion Probabilistic Models (DC-DPM), which was shown to improve the sample generation quality in the numerical experiments.

### Weaknesses
The model assumptions seem confusing and need more clarification; there is limited comparison with existing theory on diffusion models; see below for more detailed comments.

The core assumption regarding the data distribution as a uniform distribution supported on the training data is problematic. This assumption, formalized in equation (1), implies that the model learns an empirical distribution rather than a continuous one. This raises concerns about the model's ability to generalize beyond the training data, particularly in high-dimensional spaces where the empirical distribution may not accurately represent the true underlying data distribution. The theoretical analysis hinges on this assumption, and its limitations need to be addressed more thoroughly. The paper does not adequately discuss the implications of this assumption on the generative capabilities of the model, specifically whether it can produce samples that are not simply memorizations of the training set. Furthermore, the paper lacks a detailed discussion of how this assumption compares to the more common assumption of a non-parametric continuous distribution in diffusion model theory. The absence of such a discussion makes it difficult to assess the theoretical validity of the proposed approach.

Additionally, the paper does not engage sufficiently with existing theoretical work on diffusion models. While the authors mention the discretization error, they do not adequately position their work within the broader theoretical landscape. For example, the paper does not discuss the convergence properties of the proposed method or its relationship to established results on the minimax optimality of diffusion models. The lack of engagement with these theoretical aspects limits the impact of the paper and raises questions about the novelty of the theoretical contributions.

### Questions
It would be beneficial if the authors could discuss its potential connection with conditional sampling. For example, in the CIFAR example, the clusters are based on the image labels, and thus the $y_\theta$ becomes $y_\theta(x,t,c)$ where c is the data label, this resembles the conditional sampling in certain extent.

My major concern and question are as follows. The data distribution is assumed as eq (1) which is essentially a uniform distribution supported on training data. This is a very confusing assumption to me, and since this is the starting point of all the theoretical analysis, I believe the authors needs to elaborate more on why this assumption is reasonable. Does this imply that the learned diffusion model will simply "memorize" data and cannot generate distribution outside of the empirical support well? Furthermore, I believe that in most theoretical analyses for diffusion models, the ground truth data distribution is assumed as a non-parametric distribution (continuous distribution), rather than the eq(1) assumed here. Additionally, as a paper studying the theoretical perspectives of diffusion models, some representative papers in this field are not cited or discussed, e.g.,  “Oko, Kazusato, Shunta Akiyama, and Taiji Suzuki. Diffusion models are minimax optimal distribution estimators. ICML 2023” and many others.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on the challenge of approximating the reversed transition kernel of diffusion models with a Gaussian distribution. To address this problem, they propose a divide-and-conquer strategy and introduce DC-DPM. This approach clusters the data and learns transition kernels tailored to each cluster. The training and sampling processes are facilitated by two proposed approaches: label diffusion approximation and fixed class approximation. Additionally, the paper provides a theoretical convergence analysis. They empirically demonstrate that the proposed method yields improved data quality on benchmark dataset.

### Strengths
* The proposed method is both intuitive and reasonable. Since the characteristics of the transition kernel may vary depending on the data, adding it as a conditioning factor is likely to be effective. This is further supported by many previous experimental results showing that conditional datasets tend to achieve better FID scores than unconditional ones.
* The theoretical background supporting the proposed method is well-founded and lends credibility to the approach.

### Weaknesses
 * Several assumptions are introduced to support the theoretical background, but it would be beneficial to explain whether these assumptions align with practical applications or under what conditions they hold in practical scenarios.

* Although the paper states that convergence is guaranteed with arbitrary data partitioning, there may be issues related to convergence speed, so it would be beneficial to further explain for the partitioning.

* The arbitrary data partitioning may also pose a challenge for training $a_\phi$ network, as the learning difficulty may vary depending on the partitioning.

* In the explanation of Corollary 3, it is mentioned that $\epsilon_{al}$ is expected to have a smaller influence than $\epsilon_{yl}$. However, this influence could vary depending on the scales of the constants $C_2$ and $C_3$, so further analysis on this point would be valuable.

* As the current experiments focus mainly on benchmark datasets with limited datasets and network structures, further experimental validation would strengthen the credibility of the method.

  * As data partitioning is an important part of the proposed method, it would be helpful to evaluate the effectiveness of the method on datasets with diverse semantic features, such as ImageNet.

  * It would be beneficial to test the proposed method on more advanced diffusion models, such as EDM [1].

  * Demonstrating its applicability to common applications of diffusion models, such as text-to-image generation, would further strengthen the approach.

* The LD variants sometimes underperform compared to the baseline models, so analyzing these cases would provide insight into potential limitations.

### Questions
* Could the authors provide their thoughts on the points mentioned in Weaknesses, particularly regarding the experimental point?
* In the convergence analysis, what distinguishes the proposed method from previous works in terms of achieving the tighter bound?

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
This paper explores accelerating diffusion model sampling by improving the transition kernel of the reverse process. The authors aim to narrow the gap between the ground-truth reverse kernel and the conventional unimodal Gaussian kernel by employing a divide-and-conquer approach—using distinct kernels tailored to clustered data. Leveraging the proposed proof technique, the authors demonstrate that the improved kernel can guarantee convergence to the ground-truth reverse process. Experimental results indicate that this approach may effectively speed up diffusion models while maintaining performance.

### Strengths
1. This paper addresses a crucial problem in accelerating diffusion model sampling from a relatively under-explored perspective, i.e., improving the reverse process kernel.
2. The paper provides a substantial amount of theoretical analysis, along with a novel proof technique that can support convergence analysis.
3. The presentation is clear and easy to follow.

### Weaknesses
1. The motivation of the proposed approach comes from the inherent discrepancy between the ground truth reverse process, expressible as a mixture of Gaussians (in Eq. 5), and the traditional reverse kernel based on uni-modal Gaussian (i.e., Eq. 6). While this is a natural approach, a limitation remains as the authors still rely on the unimodal Gaussian kernel to approximate the MoG kernel for clustered data, as noted in L244-246. The convergence result to the ground-truth reverse process with this uni-modal approximation seems also missing.

2. Although the proposed approach offers advantages in accelerating diffusion models, it necessitates specialized training, making integration into conventional diffusion frameworks—proven to be highly effective—challenging.

3. Empirical validation on challenging, large-scale benchmarks (such as ImageNet) is lacking. The paper primarily focuses on relatively small, simpler datasets, such as CIFAR-10 and CelebA-HQ-256, raising questions about the scalability of the proposed approach when applied to more complex datasets.

4. A broader comparative study would strengthen the paper. Acceleration of diffusion models is a highly active research area, with numerous approaches offering speed improvements from different perspectives. However, the study covers only two baselines, both of which follow a similar methodological approach, i.e., improving the reverse kernel.

5. An analysis of computational costs would provide a more comprehensive comparison with baseline methods, especially since the proposed method involves the learning of multiple kernels, as well as additional neural network training (for DC-LD).

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2
