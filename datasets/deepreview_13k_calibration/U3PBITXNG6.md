# InverseBench: Benchmarking Plug-and-Play Diffusion Models for Scientific Inverse Problems

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
Plug-and-play diffusion prior methods have emerged as a promising research direction for solving inverse problems. 
 However, current studies primarily focus on natural image restoration, leaving the performance of these algorithms in scientific inverse problems largely unexplored. To address this gap, we introduce \textsc{InverseBench}, a unified framework that evaluates diffusion models across five distinct scientific inverse problems. These problems present unique structural challenges that differ from existing benchmarks, arising from critical scientific applications such as black hole imaging, seismology, optical tomography, medical imaging, and fluid dynamics. With \textsc{InverseBench}, we benchmark 15 inverse problem algorithms that use plug-and-play diffusion prior methods against strong, domain-specific baselines, offering valuable new insights into the strengths and weaknesses of existing algorithms. We open-source the datasets, pre-trained models, and the codebase to facilitate future research and development.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
A paper entitled “INVERSEBENCH: BENCHMARKING PLUG-AND-PLAY DIFFUSION MODELS FOR SCIENTIFIC INVERSE PROBLEMS” proposes a systematic benchmark for a number of scientific inverse problems that go beyond natural mages. The authors suggest optical tomography, black hole imaging, medical imaging, seismology, and fluid dynamics as a set of tasks for the benchmark. Next, the authors evaluate a handful of SOTA models with respect to their efficiency and accuracy on respective inverse tasks.

### Strengths
- This is an important and timely contribution. It has the potential to improve generalisation and standardisation across solutions addressing inverse problems in science.

### Weaknesses
 - Using SSIM and PSNR is not always sufficient in medical imaging. Perhaps the authors could propose an approach to quantify the contribution of hallucinations.
- Although the title claims “Scientific Inverse Problems”, the collection of problems is extremely physics-heavy. The only non-physics problem the authors are looking at is MRI, I suggest toning down the claim in the title.

### Questions
Perhaps the authors could propose an approach to quantify the contribution of hallucinations? This is especially important for medical images, as hallucinations can lead to a wrong diagnosis.

### Soundness
3

### Presentation
4

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
This submission made technical contributions by creating and demonstrating the INVERSEBEHCN framework, which is designed for evaluating plug-and-play diffusion models on scientific inverse problems such as black hole imaging, fluid dynamics, medical imaging, and so on. The authors compared 14 representative methods in different problem settings (i.e., forward model), considering the computation efficiency and solution accuracy. What's more, the adaptability of each method to different types of forward models was investigated.

### Strengths
The proposed INVERSEBECH fills a gap in testing diffusion models beyond natural image tasks by evaluating them to scientifically meaningful, diverse, and challenging problems. The selected 14 methods are evaluated in multiple perspectives, such as efficiency, accuracy and adaptability.

### Weaknesses
1. The discussion on sensitivity to hyperparameters and initialization for each method is limited.

2. The investigation into out-of-distribution could be more elaborated, as this could usually happen in the real-world inverse problem. Would a better sampling method help us to overcome the problem caused by out-of-distribution, or is this more related to trained prior?

3. Referring to the selected 14 methods as "plug-and-play" methods is potentially misleading, especially since one of them is specifically a plug-and-play diffusion method (Wu et al., 2024). This raises the question of whether "plug-and-play" should be considered a more narrowly defined concept.

### Questions
1. How to make sure that each method is optimally tuned for different types of inverse problems, such as implementation details, hyperparameter choice? Even we understand that this would be a huge amount of work to tune every method. 

2. As shown in Table 11, methods like Reddiff, DiffPIR, PnPDM, and DAPS have more hyperparameters for tuning than other methods. Meanwhile, these methods tend to have better positions in the benchmark shown in Figure 1. Could this suggest that the other methods are genuinely worse or that they may be undertuned?

3. For the domain-specific evaluation like compressed sensing MRI, the papers that apply generative models to MRI reconstruction in a plug-and-play way have been published in some domain-specific journals. To reach a broader impact, it is reasonable to briefly introduce the following works.

     1. Tezcan, Kerem C., et al. "MR image reconstruction using deep density priors." IEEE transactions on medical imaging 38.7 (2018): 1633-1642.
     2. Luo, Guanxiong, et al. "MRI reconstruction using deep Bayesian estimation." Magnetic resonance in medicine 84.4 (2020): 2246-2261.
     3. Luo, Guanxiong, et al. "Bayesian MRI reconstruction with joint uncertainty estimation using diffusion models." Magnetic Resonance in Medicine 90.1 (2023): 295-311.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors propose InverseBench, a benchmark/framework for evaluating diffusion prior based inverse problem solvers across five distinct scientific inverse problems that arise from black hole imaging, optical tomography, etc. Each of these problems present unique challenges for reconstruction that is different than the existing benchmarks. Authors benchmark 14 diffusion based algorithms that can be grouped into 4 categories (Guidance based, Variable splitting, Variational Bayes, Sequential Monte Carlo) and compare against problem specific baselines.

### Strengths
* The paper is written very well. I truly enjoyed reading it.
* Having a standardized benchmark to evaluate diffusion prior based algorithms is an important contribution to the inverse problems community. I believe the forward models that are included in the InverseBench are diverse, practically relevant with diverse characteristics (linear vs non-linear, with or without SVD decomposition, etc.).
* The diffusion algorithms that are considered in this paper are comprehensive.

### Weaknesses
 * While I appreciate the comprehensiveness of experiments. I would expect more detailed discussion on experimental results. For instance, which methods (or category of methods) work better for each task based on the experimental results? If a method is competitive when used in natural image inpainting, super-resolution but not in InverseBench, is there some intuition/explanation why that might be the case?
* See the questions below.

### Questions
* Line 316: "Since this dataset is not publicly available, we generate synthetic images from a pre-trained diffusion modes..." Do you use the model that is trained using 50k images to synthetically generate 105 more images for validation and test purposes? In general this part is not clear to me.
* As a future direction, robustness of diffusion prior methods can be systematically investigated. That is suppose measurement is obtained via forward model $G$ but reconstructed believing that it came from 
$\tilde{G}$. The experiments conducted on CS-MRI already suggests that PnP diffusion prior methods are more robust than baseline and end-to-end methods but it is also interesting to see comparison between different PnPDP algorithm.
* Have the authors considered benchmarking diffusion model checkpoints that are pre-trained on natural images (such as ImageNet) on these tasks? It would be interesting to see if natural image priors are useful for the tasks in the InverseBench.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper provides a comprehensive summary of the performance of 14 different diffusion-based inverse problem solvers on 5 scientific applications, each with unique forward operators. Extensive experiments on each application reveal general trends such as a bias towards the prior with out-of-distribution data and strong performance compared with conventional baselines. They contribute an open-source codebase of datasets and pretrained models to enable expedited exploration in this space of inverse problems.

### Strengths
- With such a wide and rapidly expanding collection of diffusion-based methods, this paper provides a valuable assessment of existing models across diverse problems. For those working in the space of inverse imaging problems, this gives a strong starting point to assess which model to use for a given application or as a baseline.
- The experiments are extensive and thorough. As such, they are able to discover high-level insights and trends across problems. This breadth of experimentation would be larger unavailable to most researchers; thus, the results present a significant contribution to the community in my view.
- Open-sourced datasets and pretrained models contribute a well-curated foundation for other researchers to build upon
- The paper is very well-written and concise with clear introductions to the complex inverse problems and well-thought-out analyses of the results.

### Weaknesses
 - The value of some of the images in Figure 2 is limited since its difficult to actually see differences between the reconstructions. Particularly, the MRI reconstructions for the PnP methods look the exact same. It may be more useful to provide a zoomed-in region where the differences are more apparent.

Minor Points:
- L161: Typo with "... generally intractable as so various approximations..."
- L508: Typo with "inverse scattering on sources that contain more than cells..."

### Questions
- Are the reported results (say in Table 4) for a single posterior sample? Or do you draw many samples and compute a posterior mean?

### Soundness
4

### Presentation
4

### Contribution
3
