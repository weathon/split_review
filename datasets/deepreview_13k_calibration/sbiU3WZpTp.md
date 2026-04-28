# On the Robustness of Latent Diffusion Models

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Latent diffusion models achieve state-of-the-art performance on a variety of generative tasks, such as image synthesis and image editing. However, the robustness of latent diffusion models is not well studied. Previous works only focus on the adversarial attacks against the encoder or the output image under white-box settings, regardless of the denoising process. Therefore, in this paper, we aim to analyze the robustness of latent diffusion models more thoroughly. We first study the influence of the components inside latent diffusion models on their white-box robustness. In addition to white-box scenarios, we evaluate the black-box robustness of latent diffusion models via transfer attacks, where we consider both prompt-transfer and model-transfer settings and possible defense mechanisms. However, all these explorations need a comprehensive benchmark dataset, which is missing in the literature. Therefore, to facilitate the research of the robustness of latent diffusion models, we propose two automatic dataset construction pipelines for two kinds of image editing models and release the whole dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the robustness of diffusion models from the perspective of adversarial attacks. Firstly, the authors compare the white-box robustness of latent diffusion models used for image editing, demonstrating the most vulnerable components within these diffusion models. Furthermore, they consider two transfer-based black-box scenarios. Finally, they propose an automated data set construction pipeline for building a high-quality, publicly available dataset.

### Strengths
1.The paper addresses the robustness of latent diffusion models, which is highly significant.

2.The paper explores the structure of diffusion models beyond attacking the encoder and discusses black-box attack settings.

3.The proposed attack pipeline is simple and easy to follow.

### Weaknesses
1.	Lack of comparison with other types of diffusion models。The experiments in the paper primarily focus on different versions of Stable Diffusion, lacking comparisons and discussions regarding other types of diffusion models. This may not comprehensively represent all latent diffusion models. I suggest the authors consider comparing with other models, such as UniDiffuser[1].

2.	Limited exploration of diverse attacks and defenses。As the paper aims to explore the robustness of diffusion models from the perspective of adversarial attacks, the paper uses a limited range of attack methods, and the design of attacking method may lack novelty. Additionally, there is no new attack strategy developed based on the unique characteristics of diffusion. Furthermore, the defense methods chosen for experiments appear outdated. I recommend the authors consider incorporating a wider variety of attacks and defenses in their experiments.

3.	Insufficient discussion of denoising steps. In the experiments, the authors only consider 15 denoising steps for generating adversarial examples. However, according to the findings in DiffPure[2], longer denoising steps introduce randomness and enhance robustness. The authors could explore the impact of different denoising steps as a hyperparameter on diffusion model robustness.

### Questions
see the weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a comprehensive study on the robustness of Latent Diffusion Models (LDMs), specifically focusing on their vulnerability to adversarial attacks. The authors delve into the components of LDMs, pinpointing the denoising process, and more precisely the ResNet architecture, as the most susceptible to these attacks. In addition to this vulnerability assessment, the paper makes significant strides in dataset construction, offering an automated pipeline that facilitates the evaluation of LDMs under adversarial conditions. However, to enhance its academic rigor and impact, the authors should address the highlighted weaknesses and consider the posed questions for future work. I recommend this paper for acceptance, contingent upon the incorporation of these suggested improvements.

### Strengths
1. Robustness Evaluation: The paper excels in providing a thorough investigation of the robustness of LDMs, addressing both white-box and black-box adversarial attacks. This dual perspective enriches the paper's contributions and sets a solid foundation for future research in this domain.

2. Dataset Construction: The introduction of an automatic dataset construction pipeline is a noteworthy contribution, as it streamlines the process of evaluating LDMs and ensures a consistent and reproducible framework for future studies.

3. Comprehensive Attack Analysis: Including black-box adversarial attacks alongside the white-box attacks offers a more holistic view of the vulnerabilities in LDMs, showcasing the paper's commitment to a comprehensive analysis.

4. Open-Sourced Results: The decision to open-source the results demonstrates transparency and fosters a collaborative environment, enabling other researchers to build upon this work.

### Weaknesses
1. Methodological Clarity: The paper could benefit from a more explicit elucidation of the adversarial attack strategies employed. Diving deeper into the rationale behind each attack, the expected impacts, and the choice of specific models would significantly enhance the reader's understanding and the paper's overall impact. For instance, the paper mentions attacking latent features but lacks detail on how these attacks are crafted. Are they pixel-space perturbations projected into the latent space, or are they directly applied to the latent representations? Furthermore, the paper should clarify whether the attacks are targeted or untargeted, and what loss functions are used to generate the adversarial examples. The lack of specifics makes it difficult to assess the novelty and effectiveness of the proposed attack methodology.

2. Limited Scope: Focusing solely on LDMs narrows the breadth of the paper's contributions. Expanding the analysis to include comparisons with other models could provide a more comprehensive understanding of the robustness landscape. For example, how do these vulnerabilities compare to those observed in GANs or other generative models? A comparative analysis would help contextualize the findings and highlight whether LDMs are uniquely vulnerable or if these issues are common across generative models. The current scope limits the generalizability of the conclusions.

3. Novelty Concerns: While the dataset construction is a notable effort, the evaluation of LDMs in this context is somewhat straightforward. A more innovative approach or unique insights into the robustness of LDMs would elevate the paper's significance. The paper could explore more sophisticated attack strategies, such as adaptive attacks that take into account the specific architecture of LDMs, or investigate the transferability of adversarial examples across different LDM variants. The current evaluation seems to rely on standard attacks, which might not fully capture the nuances of LDM vulnerabilities.

4. Presentation and Formatting: The paper could improve in terms of presentation, including clearer figures, more concise explanations, and better-structured arguments to enhance readability and comprehension. For example, the figures could be more informative by showing the magnitude of the perturbations and their impact on the generated images. The paper could also benefit from a more detailed discussion of the experimental setup, including the specific hyperparameters used for the attacks and the training of the LDM models.

### Questions
1. Resource Utilization: Could you provide more details on the GPU consumption and running time associated with your method? Understanding the computational efficiency of your approach is crucial for practical applications.

2. Defensive Strategies: Have you explored or considered any novel defense mechanisms to bolster the robustness of LDMs against adversarial attacks? While this might extend beyond the current scope of your work, including discussions or suggestions in this area could significantly strengthen your paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper tries to thoroughly explore the robustness of latent diffusion models. By decomposing the latent diffusion models into different components e.g. encoder, ResNet, denoising, and decoder, we can attack each module by maximizing the changes in output. For white box settings, through experiments, the authors find that attacking the output of the resnet seems to be more effective than other methods. Also, the authors run black box attacks for the first time for LDM, using prompt-transfer attacks and model-transfer attacks.

### Strengths
- This paper aims to explore the robustness of LDM, which is an important problem in the age of large generative models
- The idea of decomposing the DM into sub-modules is good, by exploring each module, we can get some new insights
- The authors did extensive experiments to support their conclusions
- The paper is well-written and is easy to read

### Weaknesses
 - For the white box settings (based on gradient):

  (1) Many attacks on LDM have been studied [1, 2], but are not mentioned in this paper. 

  (2) Attacking the output of the encoder is not an optimal way, previous work tried to minimize the distance between encoded adv-samples and a target image (e.g. some noise or given image) [2]

  (3) Will the combination of the objective functions of different sub-modules be a stronger attack? This point is not discussed


 - For the black box settings: should study the transferability of unconditioned attacks without prompt


- This paper lacks many important literature reviews e.g. adversarial samples for the diffusion model [1, 2] and diffusion model for adversarial samples [3, 4], which should be mentioned and compared


### Questions
- For eps=0.1, what is the range of input, [-1, 1] or [0, 1]
- How exactly is the attack conducted since the computational graph is chained with many U-Net, do we just calculate the final output of a target module? Can we attack the expectation over T of the given objective?
- In 3.4.2 why we need this:  `For the purpose of successful image editing,
we rank and select the top-5 text prompts by the CLIP score between the generated prompt and the
output image of Stable Diffusion V1-5 Rombach et al. (2022).`


I am willing to discuss and change my score if my questions in `Weaknesses` and `Questions` can be solved.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
