# FreqPrior: Improving Diffusion Models with Frequency Filtering Gaussian Noise as Prior

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Text-driven video generation has advanced significantly due to developments in diffusion models. Beyond the training and sampling phases, recent studies have investigated noise priors of diffusion models, as improved noise priors yield better generation results. One recent approach employs Fourier transform to manipulate noise, marking the initial exploration of frequency operations in this context. However, it often generates videos that lack motion dynamics and imaging details. In this work, we provide a comprehensive theoretical analysis of the variance decay issue present in existing methods, contributing to the loss of details and motion dynamics. Recognizing the critical impact of noise distribution on generation quality, we introduce FreqPrior, a novel noise initialization strategy that refines noise in the frequency domain.  Our method features a novel filtering technique designed to address different frequency signals while maintaining the noise prior distribution that closely approximates a standard Gaussian distribution. Additionally, we propose a partial sampling process by perturbing the latent at an intermediate timestep during finding the noise prior, significantly reducing inference time without compromising quality. Extensive experiments on VBench demonstrate that our method achieves the highest scores in both quality and semantic assessments, resulting in the best overall total score. These results highlight the superiority of our proposed noise prior.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces FreqPrior, a novel noise initialization strategy for text-to-video diffusion models.  FreqPrior refines noise in the frequency domain using a new filtering technique that addresses different frequency signals while maintaining a noise prior distribution close to a standard Gaussian distribution. This method helps preserve important low-frequency signals, enhancing semantic fidelity. The authors propose a partial sampling process that perturbs the latent space at an intermediate timestep during the noise prior generation. This approach significantly reduces inference time without compromising the quality of the generated videos. The paper provides a comprehensive theoretical analysis of the variance decay issue in existing methods, which contributes to the loss of details and motion dynamics. The authors show that the covariance error of their method is negligible, indicating that their noise prior closely approximates a Gaussian distribution.

### Strengths
The main contributions are:

FreqPrior refines noise in the frequency domain using a new filtering technique that addresses different frequency signals while maintaining a noise prior distribution close to a standard Gaussian distribution. This method helps preserve important low-frequency signals, enhancing semantic fidelity.

 The authors propose a partial sampling process that perturbs the latent space at an intermediate timestep during the noise prior generation. This approach significantly reduces inference time without compromising the quality of the generated videos.

The paper provides a comprehensive theoretical analysis of the variance decay issue in existing methods, which contributes to the loss of details and motion dynamics. The authors show that the covariance error of their method is negligible, indicating that their noise prior closely approximates a Gaussian distribution.

### Weaknesses
The title should explicitly mention "Video Diffusion Models" to clarify that the method is specifically designed for video generation and not applicable to image diffusion models. This will avoid any confusion and make the scope of the paper clearer to readers.

The paper should provide detailed measurements of GPU memory usage before and after applying the proposed FreqPrior method, particularly focusing on peak memory consumption. Given that 3D FFT can be memory-intensive, especially for resolutions higher than 512x512, this information is crucial for understanding the practical feasibility of the method. Include tables or graphs showing the GPU memory usage for different resolutions and compare them with the baseline methods. This will help readers assess the trade-offs between memory consumption and performance improvements.

The paper should explore the impact of different Classifier-Free Guidance (CFG) strengths when using FreqPrior. Since CFG is a common technique used in diffusion models to enhance generation quality, understanding how FreqPrior interacts with varying CFG strengths is important for practical applications.

### Questions
The title should explicitly mention "Video Diffusion Models" to clarify that the method is specifically designed for video generation and not applicable to image diffusion models. This will avoid any confusion and make the scope of the paper clearer to readers.

The paper should provide detailed measurements of GPU memory usage before and after applying the proposed FreqPrior method, particularly focusing on peak memory consumption. Given that 3D FFT can be memory-intensive, especially for resolutions higher than 512x512, this information is crucial for understanding the practical feasibility of the method. Include tables or graphs showing the GPU memory usage for different resolutions and compare them with the baseline methods. This will help readers assess the trade-offs between memory consumption and performance improvements.

The paper should explore the impact of different Classifier-Free Guidance (CFG) strengths when using FreqPrior. Since CFG is a common technique used in diffusion models to enhance generation quality, understanding how FreqPrior interacts with varying CFG strengths is important for practical applications.

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
5

### Summary
The paper presents a novel approach for enhancing noise priors in text-to-video diffusion models. The authors introduce a new frequency filtering method to refine noise priors, improving video quality by preserving essential details and dynamics better than existing baselines such as Gaussian noise, mixed noise, progressive noise, and FreeInit. The core motivation is to keep the standard Gaussian distribution for the frequency-based sampling refinement process. The method requires additional sampling iterations but offers notable performance improvements across multiple metrics evaluated on the VBench benchmark. The experiments are conducted using three open-source text-to-video models (VideoCrafter, ModelScope, and AnimateDiff), and the results highlight that the proposed method outperforms the baselines in both quantitative and qualitative aspects.

### Strengths
1. This work identifies the importance of standard Gaussian distribution in the sampling process for video generation. 

2. This work introduces a new frequency decomposition strategy for random variables.

3. Extensive experiments and theoretical derivation provide a great illustration for the motivation.

### Weaknesses
1. Despite this work has shown the side effects of non-uniformed sampling noise distribution, it is still hard to understand why this will destroy the motion dynamics from the theoretical perspectives. The authors claim a variance decay issue, but a direct theoretical link to motion dynamics is missing. It's unclear how variance decay specifically translates to a loss of motion, and whether other factors might also contribute.

2. The evaluation of this work is only based on VBench, which is somehow not sufficient. It is suggested to include more comparisons in terms of FID, FVD, etc. Whether the conclusion will stand under these metrics.

3. This work lacks user study and does not provide the detailed prompts used for video generation. Since the video quality measurement for AIGCs is not absolutely reliable, providing a user study for video generation is essential. The absence of specific prompts makes it difficult to reproduce the results and assess the method's sensitivity to different types of prompts.

4. How to obtain the equation (7), it needs a detailed explanation.

### Questions
1. My first question is the experimental analysis, why only Vbench is provided?

2. The second question is theoretical evidence for why non-normalized Gaussian distribution will cause the worse motion dynamics.

3. Have you considered or tested other types of frequency filtering (e.g., adaptive filtering methods) to optimize the noise prior? What is the generalization capability of such frequency filtering? It would be important to demonstrate their broader applicability

4. Have you measured the standard deviation for your generated videos with different seeds? It contains lots of randomness in video generation. Whether this work select videos based on human visualization? If not, it takes which principles for results selection?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address the problem of variance-decreasing in FreeInit, the authors propose to re-design the low-pass filter in FreeInit and use two sets of noise to maintain the variance of intermediate diffusion variables. Experiments show that the proposed method is able to preserve more details than FreeInit.

### Strengths
1. The FreqPrior approach addresses detail loss and motion dynamics issues better than previous methods (e.g., FreeInit), leading to improved video fidelity.
2.  The partial sampling process significantly reduces inference time by around 23% compared to similar methods.
3.  FreqPrior achieves higher scores in quality and semantics in evaluations, especially on the VBench benchmark.

### Weaknesses
The paper argues that the variance-decreasing problem in FreeIniit causes it to generate over-smoothed results. But the provided evidence is weak. Although the demo cases at the beginning of this paper support this conclusion, more videos in the supplement files do not verify it.  According to Table 2,  the quantitative improvements over FreeIniit is also marginal.

### Questions
What is the performance on more recent ODE-based diffusion models?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Building on FreeInit, this method introduces a novel frequency filtering approach to obtain an improved noise prior that enhances high-frequency signals and approximates a Gaussian distribution, refining text-to-video diffusion models. 
Additionally, by implementing partial sampling instead of the full sampling used in FreeInit, it effectively reduces the sampling time.

### Strengths
1. Comprehensive theoretical analysis of the variance decay issue of existing methods and addressing the issue by novel filtering technique is interesting and novel.

2. Extensive experiments validate the novel filtering method refine the text-to-video diffusion models significantly.

### Weaknesses
1. This work builds upon FreeInit, so the implementation of FreeInit should remain consistent with the original. However, while the original FreeInit uses 4 extra iterations, the comparisons in this work are made with only 2 extra iterations.

* What would the results be if both FreeInit and FreqPrior were implemented with 4 extra iterations? Would FreqPrior still outperform FreeInit?

2. Applying this method to recent T2V models could enhance the completeness of the paper.
* If high-quality T2V models are available, making low-frequency matching unnecessary, would this method still be effective?
* Additionally, if possible, could the method demonstrate effectiveness on the latest T2V models, such as T2V-Turbo or Pyramidal Flow?

### Questions
Questions are listed in the weakness.

### Soundness
4

### Presentation
4

### Contribution
3
