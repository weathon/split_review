# CNS-Bench: Benchmarking Model Robustness Under Continuous Nuisance Shifts

- Decision: Reject
- Scores: 6, 6, 6, 6, 6

## Abstract
One important challenge in evaluating the robustness of vision models is to control individual nuisance factors independently.
While some simple synthetic corruptions are commonly applied to existing models, they do not fully capture all realistic distribution shifts of real-world images. Moreover, existing generative robustness benchmarks only perform manipulations on individual nuisance shifts in one step. 
We demonstrate the importance of gradual and continuous nuisance shifts, as they allow evaluating the sensitivity and failure points of vision models. In particular, we introduce CNS-Bench, a Continuous Nuisance Shift Benchmark for image classifier robustness. CNS-Bench allows generating a wide range of individual nuisance shifts in continuous severities by applying LoRA adapters to diffusion models. After accounting for unrealistic generated images through an improved filtering mechanism for such samples, we perform a comprehensive large-scale study to evaluate the robustness of classifiers under various nuisance shifts. Through carefully-designed comparisons and analyses, we find that model rankings can change for varying shifts and shift scales, which is not captured when averaging the performance over all severities. Additionally, evaluating the model performance on a continuous scale allows the identification of model failure points, providing a more nuanced understanding of model robustness. Overall, our work demonstrated the advantage of using generative models for benchmarking robustness across diverse and continuous real-world nuisance shifts in a controlled and scalable manner.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces CNS-Bench, which uses generative models for benchmarking robustness across diverse continuous nuisance shifts by applying LoRA adapters to diffusion models.

### Strengths
- The paper is well-structured, and the proposed CNS-Bench benchmark is simple yet effective for evaluating model robustness. The authors provide comprehensive discussions along three key dimensions—architecture, number of parameters, and pre-training paradigm—giving clear insights into the paper's findings.
- In addition to the proposed dataset for benchmarking model robustness, the authors present an annotated dataset to benchmark OOC) filtering strategies. They introduce a novel filtering mechanism that significantly improves filter accuracy, which is a notable contribution.
- The application of LoRA sliders to compute shift levels continuously is a particularly innovative and inspiring approach. This adds an interesting methodological contribution to the paper.

### Weaknesses
 - The novelty of the insights presented in this paper could be more compelling. For example, in Figure 6, are there any underlying reasons or mechanisms that could provide a deeper understanding of the results? It would be beneficial to explore these further to add depth to the conclusions.

 - There is a lack of clarity on how the dataset handles potentially unrealistic or counter-intuitive scenarios, such as cars driving on water. How are these cases addressed? A discussion on the handling of such edge cases would improve the comprehensiveness of the dataset.

### Questions
There is a lack of clarity on how the dataset handles potentially unrealistic or counter-intuitive scenarios, such as cars driving on water. How are these cases addressed? A discussion on the handling of such edge cases would improve the comprehensiveness of the dataset.

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
3

### Summary
This paper introduces a novel benchmark dataset for evaluating model robustness by systematically controlling individual nuisance factors. The dataset allows for a precise assessment of the failure points of vision models, based on the severity of these controlled nuisance factors. The authors find that model rankings vary with changes in shift severity, and model architecture is a key factor in robustness.

### Strengths
Instead of measuring average accuracy drop across all nuisance shifts, the authors consider evaluating model performance at specific levels of nuisance shifts, enabling a detailed analysis of failure points in vision models.

### Weaknesses
1. Unclear contributions: The contributions listed in the paper seem overlapping. The distinctions among them are insufficiently clear. Notably, the third contribution is not visible in the main text. While the paper claims 14 distinct nuisance shifts as a key contribution, it lacks an explanation or rationale for selecting these specific shifts. Since this is a foundational aspect of the contribution, detailed descriptions should be provided in the main text, not relegated to the appendix.

2. Ambiguity in benchmark superiority: The authors assert that their benchmark outperforms existing benchmarks for evaluating model robustness by incorporating nuisance shifts across multiple severity levels. However, earlier works by Hendrycks & Dietterich (2018) and Kar et al. (2022) already support multi-severity analysis for vision model failure points. Thus, the authors should clarify how their benchmark framework distinctly advances beyond these existing approaches. The claim of superiority is not sufficiently justified, especially given the prior work in multi-severity analysis.

3. Inconsistent statements on model robustness: In line 451, the authors claim that transformers are more robust than CNNs, yet this statement seems contradicted by Fig. 6a, where ConvNext outperforms ViT and DeiT but performs slightly worse than DeiT3. This inconsistency suggests that CNNs may not always be less robust than transformers, and the statement should be re-evaluated or clarified. The performance of ConvNext relative to ViT and DeiT directly challenges the generalization that transformers are inherently more robust.

4. Validation of realistic nuisance shifts: While the authors argue that the benchmark includes realistic nuisance shifts, the realism of these diffusion-generated images is not substantiated. Proper validation, such as human assessment, would enhance the credibility of this claim. The lack of validation for the generated images raises concerns about the practical relevance of the benchmark.

5. Readability of figures: The font size in several figures is too small, which detracts from readability. Increasing the font size would improve clarity for readers.

### Questions
1. Self-supervised pre-training: Why is DINOv1 using linear probing compared with other models? This seems to create an unfair comparison, as linear probing may not fully reflect the robustness of self-supervised models relative to other models in the evaluation. Could you clarify the rationale behind this comparison approach?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a benchmark, CNS-Bench, composed of synthetic images with gradual and continuous nuisance, to evaluate the robustness of classifiers in detail. The images are generated using Stable Diffusion, incorporating a wide range of individual nuisance shifts with continuous severities through LoRA adapters to diffusion models. This paper provides a detailed evaluation and analysis of various classifiers' behavior on CNS-Bench, emphasizing the advantage of utilizing generative models for benchmarking robustness across diverse continuous nuisance shifts.

### Strengths
1. The paper is well-motivated. Understanding the robustness of models to nuisances of varying degrees is crucial.
2. It is reasonable to generate images with gradual and continuous nuisance using Stable Diffusion and LoRA adapters.
3. The experimental section evaluates various classifiers, providing a better understanding of the robustness capabilities of these classifiers.

### Weaknesses
1.  I don’t understand the failure point concept in Section 3.2. This section may contain many symbols that are confusing, such as: $X_n(S), X(s_n),X_n(S_n)$ , and the subscripts  in $s_n, c_n$.
2. In Section 4, the paper mentions "activate the LoRA adapters with the selected scale for the last 75% of the noise steps". Could you provide some theoretical or empirical evidence to justify the rationale for adjusting LoRA for the last 75% of the noise steps?
3. In Section 4.2, the paper mentions "fine-tune ResNet-50 with our data and show more than 10% gains on ImageNet-R". Was the data used for fine-tuning the entire CNS-Bench or a specific style within it (such as a style closely resembling ImageNet-R distribution)? In Table 3, I noticed that after fine-tuning, the model accuracy on IN/val decreased by 2.04%. I believe the results in Table 3 do not fully support the claim regarding "the realism of generated images.”
4. For experiment about the relation between ID and OOD accuracy in section 4.3，please further elaborate on the rationale for using the slope of the linear fit between ID and OOD accuracies and the significance represented by this slope. Why not use the linear correlation coefficient？Furthermore, please provide a more detailed analysis of the results in Figure 7, particularly elucidating the impact of the strength of nuisance on the relation between ID and OOD accuracy.
5. Figures 6a and 6b evaluate the accuracy drop. I do not think this metric rational because the model size and performance on the ImageNet validation set may not necessarily align. This mismatch could result in accuracy drops of different models that are not directly comparable. Please provide the model's parameter count and the model accuracy on IN/val for reference or other evidence to claim rationality the accuracy drop.
6. Figures 4 and 5 assess using accuracy, while Figure 6 employs accuracy drop. Could you standardize to a single metric for consistency throughout the text?
7. ImageNet-C also contains images with nuisances of different strengths. What are the distinctions between CNS-Bench and ImageNet-C?
8. Could you give some experiment details of the claim “the alignment for one given seed increases in 73% for scales s > 0 for all shifts in our benchmark” in Section 3.2?

### Questions
1.  I don’t understand the failure point concept in Section 3.2. This section may contain many symbols that are confusing, such as: $X_n(S), X(s_n),X_n(S_n)$ , and the subscripts  in $s_n, c_n$.
2. In Section 4, the paper mentions "activate the LoRA adapters with the selected scale for the last 75% of the noise steps". Could you provide some theoretical or empirical evidence to justify the rationale for adjusting LoRA for the last 75% of the noise steps?
3. In Section 4.2, the paper mentions "fine-tune ResNet-50 with our data and show more than 10% gains on ImageNet-R". Was the data used for fine-tuning the entire CNS-Bench or a specific style within it (such as a style closely resembling ImageNet-R distribution)? In Table 3, I noticed that after fine-tuning, the model accuracy on IN/val decreased by 2.04%. I believe the results in Table 3 do not fully support the claim regarding "the realism of generated images.”
4. For experiment about the relation between ID and OOD accuracy in section 4.3，please further elaborate on the rationale for using the slope of the linear fit between ID and OOD accuracies and the significance represented by this slope. Why not use the linear correlation coefficient？Furthermore, please provide a more detailed analysis of the results in Figure 7, particularly elucidating the impact of the strength of nuisance on the relation between ID and OOD accuracy.
5. Figures 6a and 6b evaluate the accuracy drop. I do not think this metric rational because the model size and performance on the ImageNet validation set may not necessarily align. This mismatch could result in accuracy drops of different models that are not directly comparable. Please provide the model's parameter count and the model accuracy on IN/val for reference or other evidence to claim rationality the accuracy drop.
6. Figures 4 and 5 assess using accuracy, while Figure 6 employs accuracy drop. Could you standardize to a single metric for consistency throughout the text?
7. ImageNet-C also contains images with nuisances of different strengths. What are the distinctions between CNS-Bench and ImageNet-C?
8. Could you give some experiment details of the claim “the alignment for one given seed increases in 73% for scales s > 0 for all shifts in our benchmark” in Section 3.2?

### Soundness
3

### Presentation
2

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
This paper introduces CNS-Bench, a benchmark for evaluating the robustness of image classifiers to what the authors call "continuous nuisance shifts" - essentially OOD distortions like no snow -> snow along a continuous axis. CNS-Bench uses LoRA adapters applied to diffusion models to generate images with a wide range of nuisance shifts at various severities. While in principle continuous shifts are possible, most of the article nevertheless focuses on a fixed number of shifts (5 severity levels). The authors then conducted an evaluation of few different visual image classifier families on CNS-Bench.

The paper's contributions are defined, by the authors, as follows:
1. The creation of CNS-Bench & evaluation of models
2. The collection of an annotated dataset for filtering (note: this is a process that becomes necessary since the approach used in the paper may alter the class label, therefore this essentially fixes an issue introduced by the approach)
3. The publication of 14 nuisance shifts at five severity levels. (note: this is essentially part of #1)

### Strengths
- Authors promise to release the dataset under a permissive licences (CC-BY-4.0); code is available from supplementary material via Google Drive.
- I like the approach of measuring a precise failure point. In psychophysics, a related concept is called the threshold of a model - see, e.g., Figure 4 of this 2017 paper on "object recognition when the signal gets weaker": https://arxiv.org/pdf/1706.06969. A threshold is calculated across many samples; the failure point described in this article, in contrast, is the point where an individual test sample is no longer correctly recognized.
- The technical approach is a nice, simple and creative application of generative diffusion models.

### Weaknesses
1. Nuisance shifts affect information that's not related to the nuisance concept. In Figure 22 and 23, some nuisance shifts don't achieve the desired result; e.g. the variation "in rain" (Fig 23f) alters/blurs the background without occluding the object through rain. **Some nuisance shifts introduce confounds**, e.g. "in dust" not only adds dust but also removes half of the people in the image and changes a person's shirt color from red to black. As a consequence, failures cannot be attributed to the nuisance concept itself.


2. The approach is based on generative models, thereby introducing a **real vs. synthetic distribution shift** that may further influence results. A discussion - better yet: an analysis - of this likely confound is recommended. Without this, I'm hesitant to share the author's hope that ("this benchmark can encourage the community to adopt generated images for evaluating the robustness of vision models.").


3. **The paper's main claim to fame remains a bit unclear to me**, and that's my most important concern. At the same time, this might be the biggest opportunity for improvement and clarification from which future readers might benefit. The authors propose a variety of options to choose from, but I'm not convinced (yet - happy to be convinced of the opposite). Specifically:
- Is it about continuous shifts? If so, this can be achieved with parametric distortions too (e.g. Gaussian noise with noise strength as a continuous parameter). Furthermore, the authors end up narrowing it down to 5 severity levels anyways, which is roughly in line with the 5-8 levels from related work.
- Is it about a large number of distortions? Probably not, since the dataset's 14 distortions are in the same ballpark as ImageNet-C (15 test + 4 validation distortions) or model-vs-human (17 distortions).
- Is it about testing a variety of models? While a number of model families are investigated (CLIP, ConvNext, Deit, Dino, MAE, MOCO, ResNet, ViT) that's also similar to previous investigations, some of which tested a broader variety.
- Is it about identifying failure cases? If so, when is it important to know about a specific failure case (as opposed to a model's threshold, averaged across many samples)?
- Is it about the connection between architecture and robustness? The observation that architecture influences model robustness has been reported (extensively) by a range of previous work.
- Is it about precise control? While strength can be controlled, the effect introduced by the nuisance can't be controlled to a level where no confounds would be introduced, as seen in Figures 22 & 23.
- Is it about scalability? If so, why is training separate LoRA adapters for each ImageNet class and shift more scalable than existing approaches?
- Is it about real-world nuisance shifts? If so, see concern #2 on the real vs. synthetic distribution shift.

### Questions
- If it should be a benchmark, people will want to know: who won? What's the score that I need to beat in order to be SOTA? Tables with an overall score would help. Table 1 is a step in the right direction but it's not immediately clear which model is best and which score (Accuracy? Accuracy drop?) is the benchmark score.
- Why were those 14 "nuisances" chosen and not others, why 14 and not, say, 50? (Not saying that the authors should do this but asking out of curiosity)
- What's the robustness of a failure point to random variation?
- Is performance (accuracy) always a monotonous function of the LoRA slider strength? Are there instances when that's not the case? If so, what does it mean if there are images beyond the failure point that are again correctly recognized?
- line 43: "such approaches are not scalable" - why not? If one takes a large dataset and applies cheap corruptions like the ones from ImageNet-C, should that be considered less scaleable?
- What's the computational cost of generating the dataset?

MISC:
- Figure 7: instead of re-using colors that were used in e.g. Figure 6 with a different association, I'd recommend using different colors here to avoid confusion - ideally a sequential color palette, with the legend sorted by scale not arbitrarily. Also, label 1.5 appears twice which is probably not intentional.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel benchmark for evaluating the OOD robustness of vision models. The core idea is to build a system that can generate images from the training distribution, but with natural distribution shifts (like snow) applied *with continuous severity levels*, so that one can smoothly increase the degree of corruption. The authors achieve this by leveraging diffusion models conditioned on the training distribution in combination with LoRA adapters. The resulting benchmark does therefore not only yield scalar accuracy values, but performance curves for different models, relating the severity of the corruption to the drop in classification performance.

### Strengths
The paper seems technically sound and successfully combines different existing methods to achieve the stated goal of generating a benchmark of continuous distribution shifts. I appreciate the thorough analysis and sanity-checks, such as creating a large OOC-detection dataset to make sure that the proposed filtering mechanism works. The writing is mostly clear, although some questions remain (see below). As far as I can tell (although I'm not too familiar with generative models) the authors cite the relevant related work.

### Weaknesses
One fundamental weakness of the paper is the lack of motivation for why a robustness evaluation at different levels is important. I’m aware that ImageNet-C also offers different corruption levels, and I could maybe be convinced that having access to these levels is useful, but the analyses conducted here do not really achieve this: Why is it interesting at which severity level a model fails, especially given that it’s unclear whether the corruption severity levels across different shifts and different classes are properly calibrated against each other (see my question 4)? Of course, having a method of subjecting any training set to a natural distribution shift is great, but the Dataset Interface paper already achieves this. So the overall contribution of the paper is effectively “only” interpolating between uncorrupted images and fully corrupted images, but I wonder why that matters, unless the ordering of models drastically changes across the different levels. That does not seem to be the case overall, according to figure 6a, and I wonder whether the differences in figure 6b and 6c (where values are averaged over fewer trials) are statistically stable. Adding confidence intervals to these plots would help convince me that this is indeed a robust finding. But even if this were the case: If I had a dataset with a painting-corruption, how would I know what the corruption-scale of my dataset is, to then select the best model at that level? And do I really care about the minuscule differences between models (<< 1% accuracy delta) at scale 1, or would I simply select the model that does best at the maximum scale?
While I appreciate that the authors included the failure cases in figure 16, they do make me wonder how reliably the method really works, and whether this unreliability might explain the weird curves in figure 6c. It would be good to also add confidence intervals to figure 3, to give a better idea of the quality of the generated images (but see my question 2 about the y-axis values of figure 3).



### Questions
## Feedback
* I would have liked to take a closer look at the images in the benchmark, but could not unzip the provided benchmark.zip file, apparently because the file was corrupted. I don't think it's an issue on my end, could you look into this?
* I think the writing, especially in section 3.2 where the method is explained, could be improved quite a bit, also to render the paper more self-sustained - I found myself having to look up the referenced papers, even though the relevant parts could have been summarized in a few sentences. For example, how exactly the scale of the sliders works cannot be understood from this paper alone, one needs to read Gandikota et al. 2023.
* The legend of figure 7 is broken. The label for scale 1.5 appears twice and the values are not ordered.
* Minor point, but in figures 9 and 10 it might be better to share the y-axis for more comparability between the plots.

## Questions
1. In line 197, shouldn’t $\theta$ have both $c_t$ and $c_+$ in the subscript, like $\theta_{c_t, c_+}$?
2. In figure 3, how is it possible that the difference of two cosine similarities, which should be <= 2, achieves values of up to 7.5?
3. In line 423, you write that an explanation for the abrupt change in failure rate of the cartoon style is the ImageNet class “comic book”, but I don’t see why images would be mis-classified as comic books more for scale 1.5 than for scale 2 and higher. 
4. Do you have any way of asserting that the severity levels of different shifts and different classes are actually calibrated, i.e. that scale 2.5 of an elephant in snow is the same level of corruption as a scale 2.5 zebra in fog? Since you are training different LoRAs for the different classes, I’m not sure if this will always be the case, but it might be desirable. (I guess one could calibrate this using the CLIP-distances…?)
5. In principle, could you combine different distribution shifts at the same time? E.g., modify the same image to both exhibit fog and snow?

## Final Assessment
Overall, I’m a bit skeptical of the relevance of the contribution of the paper (see above) and could not check how the images in the benchmark look like, qualitatively. I propose to reject for now, but I'm curious to hear the perspectives of the other reviewers and would be willing to increase my score if they deem this work relevant, or if the authors can motivate the need for continuous shifts better.

### Soundness
3

### Presentation
3

### Contribution
2
