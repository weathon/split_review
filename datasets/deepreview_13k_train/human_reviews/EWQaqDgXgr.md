# Sparse Repellency for Shielded Generation in Text-to-Image Diffusion Models

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
The increased adoption of diffusion models in text-to-image generation has triggered concerns on their reliability.
Such models are now closely scrutinized under the lens of various metrics, notably calibration, fairness, or compute efficiency.
We focus in this work on two issues that arise when deploying these models: a lack of diversity when prompting images, and a tendency to recreate images from the training set.
To solve both problems, we propose a method that coaxes the sampled trajectories of pretrained diffusion models to land on images that fall \textit{outside} of a reference set.
We achieve this by adding \textit{repellency} terms to the diffusion SDE throughout the generation trajectory, which are triggered whenever the path is \textit{expected} to land too closely to an image in the \textit{shielded} reference set.
Our method is \textit{sparse} in the sense that these repellency terms are zero and inactive most of the time, and even more so towards the end of the generation trajectory.
Our method, named \textbf{SPELL} for \textit{sparse repellency}, can be used either with a static reference set that contains protected images, or dynamically, by updating the set at each timestep with the expected images concurrently generated within a batch.
We show that adding SPELL to popular diffusion models improves their diversity while impacting their FID only marginally, and performs comparatively better than other recent training-free diversity methods. We also demonstrate how SPELL can ensure a shielded generation away from a very large set of protected images by considering all 1.2M images from ImageNet as the protected set.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel technique called SPELL to address the challenge of shielded generation and improve generation diversity in text-to-image diffusion models. SPELL shields the model from replicating protected images and promotes intra-batch diversity by adding sparse repellency terms to the diffusion process, guiding generated images away from a reference set and the images in the same batch. The authors demonstrate the effectiveness of their methods via experiments on the state-of-the-art diffusion models. Compared to the previous works, SPELL achieves the best trade-off between image diversity and generation quality. Further, the authors empirically show that SPELL is scalable with a large reference set.

### Strengths
- The paper tackles a timely and practically-relevant problem supported by a fair amount of experiments. Shielded generation of text-to-image diffusion models is an area with limited prior research, making this work particularly valuable.
- Overall, the paper is clearly written and easy to follow.

### Weaknesses
 - One key weakness of this paper is the lack of experiments regarding the main trade-offs against baseline methods. For example, while Table 1 indicates that SPELL has a minor trade-off in precision, the authors do not compare this trade-off with the baselines. Figure 4 is the only comparative result provided, but it lacks an analysis of image quality. Specifically, I would like to know if all models in Figure 4 are capable of similar  generation quality, say in terms of FID.
- Since SPELL is a training-free sampling method, the authors should also provide a quantitative analysis regarding inference time. For instance, an analysis of average wall-clock time compared with baseline methods, or testing with larger reference dataset sizes, would be helpful for readers.
- In the main qualitative analysis in Section 4.5, Figure 6 does not convincingly illustrate improved image generation diversity. For example, the fourth image is repelled from the third image, and it's unclear why this image is closer to the third image than to the first or second. Similarly, in the 13th image, the only notable difference is the color of the ball, and yet the blue ball is the most common color in prior images. Additionally, it would be beneficial if the authors provided examples with multiple image batches, other than a single-image batch.
- Regarding Figure 7, I wonder whether the $L_2$ distance-wise nearest neighbor search was the best choice. This is because many images in the third row (EDM + SPELL) seem more similar to the second row (ImageNet neighbor for EDM) rather than the fourth row (ImageNet neighbor for EDM+SPELL).
- In line 359, it states that "precision and density decrease slightly in 5 out of 6 models." However, according to Table 1, isn't this actually the case for 4 out of 6 models? Please correct me if I am wrong.

### Questions
- In line 359, it states that "precision and density decrease slightly in 5 out of 6 models." However, according to Table 1, isn't this actually the case for 4 out of 6 models? Please correct me if I am wrong.

### Soundness
2

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
1

### Summary
This paper introduces a novel guidance mechanism called SPELL (Sparse Repellency) aimed at enhancing diversity and protecting certain reference images during the generation process in text-to-image diffusion models. This approach addresses two common challenges with diffusion models: the tendency to produce repetitive images for the same prompt and the potential risk of inadvertently recreating training images, which raises privacy and copyright concerns. In summary, SPELL is a post-training intervention that enhances image diversity and safeguards specific images by selectively adjusting generation paths. This method offers a practical solution for more diverse and privacy-respecting image generation in diffusion models.

### Strengths
1. The paper is well written.
2. The addressed problem is important in diffusion models.

### Weaknesses
I am not familiar with this field, but I find the issue addressed in this paper to be interesting and important. AC can disregard my opinion and score.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel way to diversify diffusion generations by introducing repellency terms to the diffusion SDE. It achieves the diversity of generated images from one prompt and/or prevention of similar generation to the reference set, which is one of the significant challenges for real users.

### Strengths
- This paper tackles a very practical problem of repetitive generations of text-to-image diffusion models to both protective images in the training set and previously generated images.
- The proposed method, repellency terms, has a concrete background and intuitive to solve the problem.
- Thorough empirical investigations provide enough understanding of how SPELL can increase the diversity of generated images, and the advantages for real-world applications.

### Weaknesses
 - While SPELL can be used for any diffusion pipelines, the effectiveness of SPELL for smaller models or domains other than ImageNet is not fully investigated.
- The efficiency of SPELL is validated for ImageNet class or simple text prompts where the diversity within a text prompt is huge. Evaluation for more complex text prompts that align with more practical usage of text-to-image diffusion models would validate the effects of SPELL more.
- As noted by authors, the proposed SPELL does not provide a very tight guarantee to avoid generations of similar images to the reference set, which can limit the applicability of SPELL for high-risk cases.

### Questions
- Applying repellency terms based on the current state x_t instead of the expected final output seems applicable for the intra-batch repellency case, providing better diversity to a batch of generated images. Can it be one of the baselines to compare SPELL for the intra-batch case?
- It seems like SPELL forces each trajectory to arrive near the boundary of other balls (shields). Can further methods (something similar to momentum or just larger overcompensation) improve the diversity of generated images?

### Soundness
3

### Presentation
4

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
This paper introduces a novel post-training guidance mechanism, SPELL, which primarily addresses the training-set protection issue and the diversity problem of image diffusion models. SPELL is designed to repell the latents away from a trajectory that is close to a protected image set or from other latents within the same inference batch. It dynamically introduce small corrections to the latents in a way that is sparse and only triggered when the predicted trajectory is too closely to a reference domain. The authors evaluate SPELL on multiple state-of-the-art open-sourced diffsion models, showing its effectiveness. They also provide comparisons to other previous approaches that are also aimed at addressing diversity or with protected image set, which show some superior results on selected trading-off plots.

### Strengths
1. The overall problem that this paper addresses is one of the important issues that current diffusion-based image generation models possess, which adds to the value of motivations for this paper.
2. This paper is well-written and easy-to-understand. Notations within the background section and the method section are self-contained and clear to follow. Fig. 2 further adds readability.
3. The method this paper proposed is novel, which provides conceptual insights particularly in the method section (Sec. 4).
4. Experiments contain both ablation studies and comparisons to other methods. Fig. 3 show the effect of SPELL's only parameter **r**, in which we see effectiveness especially around 10-20.

### Weaknesses
MAJOR:
1. The core issue for this paper is the soundness in terms of the superior effectiveness compared to other similar methods. In Fig. 4, there is only comparisons on recall-precision, converage-density, and vendi-clip trade-off, while other concerning metrics in Tab. 1, such as $\text{FID}$, $\text{FD}_\text{DINOv2}$, are not included. I also failed to find reasoning on why only these three metric-pairs are selected. It is unclear why the authors chose to focus solely on these specific trade-offs, particularly given that metrics like FID and FD_DINOv2 are standard for evaluating image generation quality. The absence of these metrics makes it difficult to assess the overall performance of SPELL compared to other methods.
2. This discussion of the fundamental methodology difference towards **Particle Guidance** on Page 5 is not convincing, as it seems SPELL can be treated as a special case of Particle Guidance when the energy potential $\phi_t$ is simply calculating the difference. The explanation lacks a rigorous mathematical justification for why SPELL cannot be framed as a form of particle guidance with a specific potential function. The argument that SPELL's geometric approach is fundamentally different needs more concrete evidence, especially given that both methods manipulate latent trajectories.
3. This paper provides abundant unconditional results with protected image set being ImageNet-1k in Fig. 17 in the appendix, but it seems that the only qualitative results for diversity is in Fig. 1. This paper could benefit from more concrete visual evidences. The lack of diverse visual examples makes it hard to evaluate the practical impact of SPELL on image diversity. While the quantitative metrics are useful, visual inspection is crucial for assessing the subjective quality and diversity of generated images.

MINOR:
1. In contributions, bullet point 3, **generated** is misspelled.
2. In contributions, bullet point 2, explanations on the **future looking** feature is quite not straight-forward to understand, I'd suggest keeping it brief here as a bullet point in contributions, and further explain it in method section with mathematical symbols, such as $x_t, x_0$.

### Questions
1. As it is difficult to show all possible trade-offs, a better way of giving concrete comparisons would be adding detailed tables for each of the methods. Each table shows all results with rows to be parameters, and columns to be all the metrics. Adding such tables would surely address my core concern, but due to limited time, it is also promising if the reasoning of choosing these trade-offs are persuasive and convincing.
2. I'm generally not quite sure if SPELL could be treated as a special case of Particle Guidance in terms of intra-batch diversity. A brief explanation would be sufficient.
3. This paper would also benefit from providing more diversity results, but it is understandable if this is infeasible considering the limited time for rebuttal.

### Soundness
2

### Presentation
4

### Contribution
3
