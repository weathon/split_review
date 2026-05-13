# ECHOPulse: ECG Controlled Echocardio-gram Video Generation

- Decision: Accept
- Scores: 8, 6, 6, 6, 8

## Abstract
Echocardiography (ECHO) is essential for cardiac assessments, but its video quality and interpretation heavily relies on manual expertise, leading to inconsistent results from clinical and portable devices. ECHO video generation offers a solution by improving automated monitoring through synthetic data and generating high-quality videos from routine health data. However, existing models often face high computational costs, slow inference, and rely on complex conditional prompts that require experts' annotations. To address these challenges, we propose \projectname{}, an ECG-conditioned ECHO video generation model. \projectname{} introduces two key advancements: (1) it accelerates ECHO video generation by leveraging VQ-VAE tokenization and masked visual token modeling for fast decoding, and (2) it conditions on readily accessible ECG signals, which are highly coherent with ECHO videos, bypassing complex conditional prompts. To the best of our knowledge, this is the first work to use time-series prompts like ECG signals for ECHO video generation. \projectname{} not only enables controllable synthetic ECHO data generation but also provides updated cardiac function information for disease monitoring and prediction beyond ECG alone. Evaluations on three public and private datasets demonstrate state-of-the-art performance in ECHO video generation across both qualitative and quantitative measures. Additionally, \projectname{} can be easily generalized to other modality generation tasks, such as cardiac MRI, fMRI, and 3D CT generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose the first Echocardiography generation model conditioned in ECG signals named ECHOPulse. The overall pipeline ECHOPulse consists of three stages. The first stage is video tokenizer training, which utilizes a VQ-VAE based model to train the tokenizer for ECHO video quantization. The second stage is to align the ECG and video tokens, and the ECG-FM is used to encode the ECG and masked token prediction is used for alignment. The final stage is video generation, which is autoregressive video token generation conditioned on ECG tokens.

### Strengths
1. The paper contains novel contribution in that it is the first paper to present Echo video generation conditioned on ECG signals, and also plan to release the ECHO videos paired with ECG dataset.

2. The paper is well-written and easy to follow, with the pipeline figure covering all three steps used in EchoPulse.

3. The experiments compare the tokenization performance and video generation performance, and compares to other related papers despite this paper being the first to explore ECG-guided ECHO video generation.

### Weaknesses
1. The video tokenization performance results in Table 1 compare the reconstruction metrics of MSE and MAE between EchoNet-Synthetic and ECHOPulse. However, there should also be qualitative result comparison to compare the reconstruction results between the two tokenization models, similar to qualitative video generation results in Figure 3. Specifically, visual examples of reconstructed videos from both models would allow for a more intuitive understanding of the trade-offs in reconstruction quality, which is not captured by MSE and MAE alone.

2. Similar to the video tokenization weakness above, the video generation experiments also do not contain any qualitative comparison between other models such as MoonShot, VideoComposer, and HeartBeat. The figures only display the qualitative results of ECHOPulse under different ECG conditions. Therefore, qualitative results should be displayed for each models. This is crucial to understand the relative strengths and weaknesses of ECHOPulse compared to existing state-of-the-art video generation models, especially in terms of visual fidelity and temporal coherence.

3. As mentioned in the Limitation and Future Works section, instead of using GAN loss for ECHOPulse, it will be better to see combination of diffusion models in this pipeline for ECHO video generation. The current GAN-based approach might suffer from mode collapse and lack of diversity in the generated videos. Exploring diffusion models, which have shown superior performance in image and video generation tasks, could potentially lead to more realistic and diverse outputs.

### Questions
1. As mentioned in the weaknesses section, was there a specific reason the qualitative comparison for tokenization models (reconstructed video comparison) and video generation models (generated video comparison) were not conducted?
2. Instead of using non-overlapping patches for video tokenization, would the VQ-VAE based tokenization improve performance using overlapping patches? Was this explored experimentally?

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
This manuscript propose ECHOPULSE, a method to synthesize echo videos from easily accessible ECG signals. The method creatively uses the ECG signal, which is highly consistent with the ultrasound video, as a condition to generate the echo video. Experiments on multiple datasets and provided demos show excellent performance.

### Strengths
Strengths: 
1) Significance: The most important contribution of this manuscript is the use of easily accessible ECG signals as control conditions to generate echo videos. The proposed method tries to combine these two modalities of video data and time series data (ECG), which is significant for medical image analysis and provides new research directions. The synthesized video data can be applied to many downstream tasks and the methods used can be generalized to more tasks.
2) Originality: Although this paper uses a several of the published techniques, the work centers on synthesizing echo videos using more temporally informative time-series data, rather than using text or otherwise.
3) Quality: The manuscript is clearly structured and accurately presented, and the figures and tables are of high quality.
4) Reproducibility: the authors provide detailed experimental procedures and details in the main text and appendices with corresponding code, which greatly helps in the reproduction of this work.

### Weaknesses
Weaknesses:
1) Although ECGs can be easily obtained from wearable devices, how should condition images be obtained when the method is applied in practice? How to ensure that the condition image is reasonable? Specifically, the manuscript does not address the variability in image quality and view angles that are inherent in real-world ultrasound acquisitions. The method's reliance on a single, high-quality condition image raises concerns about its robustness when presented with less ideal inputs. Furthermore, the selection process for the condition image is not clearly defined, and it is unclear how the method would handle cases where a suitable condition image is not readily available or is of poor quality.
2) Compared with the previous method, the generation of real-time has been greatly improved, but still can not reach the real-time generation requirements. It is not clear how much inference resources are consumed by this method (Flops, GPU Mem et al). This determines whether it can be deployed on wearable devices. The manuscript lacks a detailed analysis of the computational complexity of the proposed method, making it difficult to assess its feasibility for deployment on resource-constrained devices. While the authors mention improved generation speed, they do not provide concrete metrics such as frames per second (FPS) or latency, which are crucial for evaluating real-time performance. Additionally, a breakdown of the computational cost associated with different stages of the pipeline would be beneficial for understanding potential bottlenecks and optimization opportunities.

### Questions
Questions:
See Weaknesses

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
3

### Summary
The paper introduces ECHOPulse, an ECG-controlled ECHO video generation model that creates echocardiography (ECHO) videos using only ECG signals as input, claiming that it allows bypassing the need for complex conditional annotations. ECHOPulse uses a VQ-VAE-based tokenization and a transformer model to align ECG with video data, achieving efficient, realistic video generation suitable for scalable clinical applications.

### Strengths
- The method shows potential generalizability to other medical video modalities, like cardiac MRI and CT, indicating versatility beyond ECHO generation.
- The paper is novel and interesting
- The language and presentation is proper

### Weaknesses
 - The use of comic sans font on the figures should re-evaluated 
- High model complexity and memory demands may restrict usability on devices with limited processing power, potentially limiting real-time deployment in resource-constrained settings, such as medical ones.
- The method is over-engineered
- The premise of the paper and the approach taken actually have semantic issues. The difficulty in ECHO data comes from the poor quality of the data as the authors correctly point out, however , to the best of the reviewers knowledge, the solution is not to create synthetic to monitor patients when only ECGs are provided. Details in the videos and images have clinical significance and the proposed method makes no attempt to ensure fidelity and the trustworthiness of the generated videos, making clinical significance limited 
- There is no mention of medical professionals evaluating the quality of the videos and how realistic they are 
- There is no discussion about confounding factors that could influence  the generation of the videos and hence lead the model to hallucinate 
- There is insufficient discussion about the use of such a video generation tool to train downstream models
- Going from an ECG to a video is an information creating process and the method makes no attempt to constrain this so the model does not generate implausible or unrelated to the patient information. Especially when there is no conditioning image/video

### Questions
- How would such method actually have clinical impact ? 
- How much do the generated data contribute in training downstream tasks ? 
- How would we ensure that the model doesn't hallucinate and provide clinically irrelevant  or harmful information ?
- Why there is no thought given to potential confounding factors that would effect the generating process ?

Overall the method is over engineered, with limited guardrails and questionable clinical significance

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose Echopulse, a video diffusion model conditioned on time-series data. Their pipeline is split into different parts including a tokenization step for efficient generation, a feature alignment step to align visual features with time series data, and a generation step for video generation. 
In general, the paper is well written and easy to follow. 
While their contribution is clear, I am not convinced that the proposed method is better than what was previously proposed in the literature. The main experiments lack exhaustive comparison (eg. Tab.1 private data, tab2 private data) and multiple things proposed in the paper are not properly validated. Overall I give a weak reject.

### Strengths
I believe the idea of aligning the representation of frames with ECG data is very good and has a large potential to work for other domains as well. 

The writing is very clear and from beginning to end it is easy to understand what the authors are doing. 

I believe that conditioning videos on time-series data could have a strong impact even outside of ultrasound videos.

### Weaknesses
There is not enough evidence supporting the claim that the generated videos follow the ECG signal. The LVEF estimation presented in Table 3 only considers ED and ES phases which are only a part of the ECG cycle. Furthermore, the results on EF estimation are inferior compared to previous methods in terms of R2 score which is the gold standard metric for estimating EF. Figure 3 only shows one example and is difficult to understand. Maybe it would help to add LVED and LVES values to the frames. 

Table 3 is missing references. Why is EchoNet-Synthetic not mentioned as a baseline in Table 3? Their inference time is below 3 seconds.

It is unclear how much influence reconstruction has on the final results. While the reconstruction results of the method presented are best, I am not convinced that the difference will be visible when using the method for downstream tasks such as video generation or EF estimation. I think it would be helpful to provide metrics such as rFID or rLVEF (reconstruction LVEF) to get an estimate to how much information is lost through encoding and how much better EchoPulse is compared to previous methods. 

Inconsequent comparison: Why are there no generative results for EchoDiffusion or EchoNetSynthetic on Private data? Also, Table 1 misses the EchoNet-Synthetic baseline. 

Motivation: While I think the application is exciting I believe there is a lack of motivation for ECG to video generation in particular. It would help if you could further motivate. Especially on what is the motivation of doing ECG conditioned generation over EF condtioined video generation. 

Minor: 
Table 2 should be separated into all datasets to make comparison easier.

### Questions
Do you have details about how good the models are without pretraining on natural data?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose a Transformer and VQVAE-based generative model for echocardiogram generation, conditioned on ECG signals. This is a novel approach that seeks to explore ECG-based conditioning for controlling cardiac motion during echocardiogram generation, a relatively under-explored area.

### Strengths
- The use of ECG signals for controlling cardiac motion in echocardiogram generation is a novel and under-explored area, making the concept innovative and potentially impactful.
- The methodology is well-grounded in leveraging VQVAE tokenization for fast decoding, which addresses some of the computational bottlenecks in generative models.

### Weaknesses
several concerns and inaccuracies in the paper need to be addressed for clarity and rigor.

First, the abstract claims that existing methods have high computational costs, slow inference, and rely on complex conditioning prompts. This statement is not entirely accurate. For example, the paper does not provide a comparison with EchoNet-Synthetic when discussing generation times, which is essential for validating such claims. Neglecting such a comparison is poor practice and can mislead the reader about the novelty and efficiency of the proposed method.

In Section 2.3, there is a reference to "Reynaud et al. (2024) introducing EchoNet-Dynamic." However, this passage is unclear, and it appears there might be confusion between the works of Reynaud et al. (2024) and Ouyang et al. (2020). Clarifying this would help avoid misattribution of prior work.

Additionally, the statement that these studies are conditioned on carefully curated prompts such as segmentation masks and clinical text is not fully correct. Only HeartBeat (Zhou et al., 2024) uses these forms of conditioning. EchoDiffusion (Reynaud et al., 2023) and EchoNet-Synthetic (Reynaud et al., 2024) use image and EF as conditioning inputs. This oversimplification of related work needs to be corrected.

Furthermore, Eq. 1 lacks proper citations. The loss function used in this equation appears to be inspired by previous works, yet no references are given. The authors should consider citing relevant works such as Gu et al. (2022) [1], Rombach et al. (2022) [2], and Esser et al. (2021) [3] to give due credit.

Section 4.1 presents an incorrect conclusion. The numbers extracted from the EchoNet-Synthetic paper reflect only the VAE model metrics, without involving the diffusion model. Similarly, the metrics for ECHOPulse involve only the VQVAE, not the token-prediction model. Therefore, the comparison between VQ-VAEs and diffusion models is not valid, and the conclusion that VQ-VAEs outperform diffusion models cannot be drawn from this comparison.

In Table 2, there are several points that need further explanation. It is unclear how MoonShot and VideoComposer were evaluated for this task, as the numbers seem to have been taken from the HeartBeat paper without further elaboration. Additionally, EchoNet-Dynamic includes only A4C views, so it is not clear how ECHOPulse was evaluated on A2C views, given that these metrics are not reported in EchoDiffusion and EchoNet-Synthetic. The SSIM computation is also problematic, as SSIM generally requires paired input/output data, and it is not clear how ECHOPulse reconstructs a video. Moreover, how the text conditionings for CAMUS and EchoNet-Dynamic were generated should be clarified. Lastly, the table construction raises questions, particularly why HeartBeat and EchoNet-Synthetic are singled out at the end.

Section 4.2 discusses the comparison with baselines, but the experimental setup lacks sufficient explanation, making the comparisons appear unfair. MoonShot and VideoComposer are general -- purpose generative models, so it is unsurprising that they perform worse than domain -- specific models. HeartBeat’s use of multiple conditions emphasizes the importance of using as many conditioning variables as possible. However, only the ablation results of HeartBeat are compared to other methods, which limits the value of the comparison. Furthermore, the conclusion of this section is poorly formulated. While the qualitative results clearly indicate that the visual quality of ECHOPulse samples lags behind, the conclusion only hints at this issue without directly acknowledging it. Moreover, the FID and FVD metrics are poor indicators of quality in this specific task, and this should be discussed more critically.

In Table 3, EchoNet-Synthetic is conspicuously absent. Including this model would provide a more complete comparative analysis.

In the paragraph following Table 3, the method for calculating LVEF in this paper is substantially different from that used for the EchoNet-Dynamic dataset, making direct comparisons problematic. This discrepancy is not adequately addressed, and the conclusion is again misleading, as EchoNet-Synthetic is not included in this analysis, even though it shows superior performance in all reported metrics.

Section 5 makes some strong claims about the performance of the proposed approach. While the novelty of the idea is clear, the assertion that it achieves the best results is far-fetched. Previous works such as EchoNet-Synthetic and HeartBeat have demonstrated better performance. The authors should focus on highlighting the innovative aspects of their method rather than making overstated claims about its superiority.

Overall, using ECG signals for ECHO video generation is an intriguing approach. The idea of using ECG is interesting, the method (VQVAE + Transformer) is less common in the field if image/video genetation, similar to Phenaki [4]. However, the literature review and baseline comparisons are inadequate, and the paper is riddled with oversights and false conclusions. A more thorough review and revision of the comparisons and claims would significantly improve the work. Additionally, proper citations for key components of the methodology are necessary.

### Questions
- Can you provide specific details or comparisons that validate the claims in the abstract regarding the computational cost, slow inference, and complex conditioning of existing methods? Why was EchoNet-Synthetic not included when discussing generation times?

- There appears to be some confusion between the works of Reynaud et al. (2024) and Ouyang et al. (2020) in Section 2.3. Could you clarify the differences between these works and how they relate to your methodology?

- The paper suggests that prior works such as EchoDiffusion and EchoNet-Synthetic use complex conditional prompts like segmentation masks and clinical text, but these models actually use image and EF for conditioning. Could you revise this section to more accurately reflect the conditioning methods used in these studies?

- The loss function presented in Equation 1 lacks references to foundational works. Could you cite the relevant literature that inspired or derived this loss, such as Gu et al. (2022), Rombach et al. (2022), or Esser et al. (2021)?

- The comparison between VQ-VAE and diffusion models seems incomplete, as the EchoNet-Synthetic metrics presented relate only to the VAE model. Could you clarify how these models were compared and whether it is appropriate to conclude that VQ-VAEs surpass diffusion models based on these metrics?

- How were MoonShot and VideoComposer evaluated for this specific task? Did you replicate their results, or were the metrics taken from the HeartBeat paper? Additionally, can you clarify how SSIM was computed, considering it typically requires paired input/output data, which is not evident for ECHOPulse?

- EchoNet-Dynamic contains only A4C views. How was ECHOPulse evaluated on A2C views, given that these metrics are not reported in EchoDiffusion and EchoNet-Synthetic?

- The comparison with baselines such as MoonShot and VideoComposer appears unfair, given that these are general-purpose models. Could you explain how the experimental setup ensures fair comparison with domain-optimized models, and why only the ablation results of HeartBeat were compared?

- EchoNet-Synthetic is conspicuously absent from Table 3. Why was this model excluded from the comparison, and how would including it impact the conclusions?

- The method for calculating LVEF in this paper differs significantly from that used in the EchoNet-Dynamic dataset. How do you account for this discrepancy, and does it affect the validity of the comparisons?

- While the novelty of using ECG signals is appreciated, the claim that your model achieves state-of-the-art results seems overstated. Can you clarify the specific advantages of your model compared to EchoNet-Synthetic and HeartBeat, without overstating the performance? 

- The qualitative results suggest that the visual quality of ECHOPulse samples is lower than that of competing models, but this is not explicitly acknowledged in the text. How do you address this issue, and why were FID and FVD metrics chosen for evaluation, given their limitations for this task?

### Soundness
3

### Presentation
3

### Contribution
2
