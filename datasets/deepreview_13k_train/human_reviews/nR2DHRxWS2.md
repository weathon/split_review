# Improving Source Extraction with Diffusion and Consistency Models

- Decision: Reject
- Scores: 6, 3, 5, 3

## Abstract
In this work, we demonstrate the integration of a score-matching diffusion model into a deterministic architecture for time-domain musical source extraction, resulting in enhanced audio quality. To address the typically slow iterative sampling process of diffusion models, we apply consistency distillation and reduce the sampling process to a single step, achieving performance comparable to that of diffusion models, and with two or more steps, even surpassing them. Trained on the Slakh2100 dataset for four instruments (bass, drums, guitar, and piano), our model shows significant improvements across objective metrics compared to baseline methods. 
Sound examples are available at \href{https://consistency-separation.io/}{https://consistency-separation.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper applies consistency distillation of diffusion models to the task of music source separation. The performance is evaluated on a standard task involving the separation of bass, drums, guitar, and piano. The proposed method is efficient, and the separation performance is better than conventional methods in terms of SISDR.

### Strengths
- The paper makes a valuable contribution by being one of the first to apply the latest technique, consistency distillation, to music source separation. While it may not exhibit groundbreaking originality, the work achieves a reasonable level of novelty within the field.
- The literature survey is well-executed, providing a thorough and balanced overview without notable omissions or excesses. The paper provides clear and comprehensive background information, along with a well-explained presentation of the methods used for comparison, making it easy for readers to understand the context.
- The proposed method is highly efficient. While there may be some concerns regarding the evaluation approach, it does show improvements over conventional methods in terms of the objective metric (SISDR).

### Weaknesses
 - The task addressed is fairly standard, and similar studies on this task are quite common. In that sense, the work does not offer groundbreaking novelty. It would also be interesting to explore whether the method is effective for other types of music or instruments, expanding the scope of its applicability.
- A drawback of the proposed method is that it does not demonstrate particular effectiveness in out-of-distribution (OOD) domains, as highlighted in Appendix C. As the authors acknowledge, this limitation remains an open research question for future work.
- To me, SISDR values presented in Table 1 did not seem to align well with the audio quality I perceived when listening to the samples provided on the linked website. When SISDR exceeds 20 dB, it is questionable whether this metric is suitable for evaluating the quality of source separation. Instead of relying solely on waveform-based metrics like SISDR, which are grounded in squared error, it would be worthwhile to consider alternative evaluation methods. For instance, metrics that emulate human auditory perception through neural networks might provide more meaningful insights.
- The detailed comparison of parameters in Figure 2 is commendable and adds valuable insight. However, I am curious whether $\sigma_{\max} = 0.01244, 0.2497, 0.2495$ were specifically chosen to optimize the performance shown in these graphs. It is important to clarify whether the selection of these values involved any potential use of the evaluation data for tuning purposes.

### Questions
- To me, SISDR values presented in Table 1 did not seem to align well with the audio quality I perceived when listening to the samples provided on the linked website. When SISDR exceeds 20 dB, it is questionable whether this metric is suitable for evaluating the quality of source separation. Instead of relying solely on waveform-based metrics like SISDR, which are grounded in squared error, it would be worthwhile to consider alternative evaluation methods. For instance, metrics that emulate human auditory perception through neural networks might provide more meaningful insights.
- The detailed comparison of parameters in Figure 2 is commendable and adds valuable insight. However, I am curious whether $\sigma_{\max} = 0.01244, 0.2497, 0.2495$ were specifically chosen to optimize the performance shown in these graphs. It is important to clarify whether the selection of these values involved any potential use of the evaluation data for tuning purposes.

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
4

### Summary
This paper introduces a method for musical source separation that integrates a score-matching diffusion model with consistency distillation, addressing the typically slow iterative sampling of diffusion-based methods. The authors first train a deterministic model for source separation and then enhance its output by training a diffusion model on top of it. Evaluated on the Slakh2100 dataset, the proposed approach demonstrates improved performance in instrument separation compared to baseline methods.

### Strengths
The integration of score-matching diffusion with consistency distillation for source separation presents an interesting approach, particularly with conditioning on the ground truth source stems during training and on $\hat{x}_s^\text{det}$ during inference, which aligns well with the demands of source separation. This method demonstrates objective improvements over baseline systems, specifically achieving higher performance on the Si-SDR metric when evaluated on the Slakh2100 dataset.

### Weaknesses
The experimental setup in this paper is limited, as the authors primarily rely on the Slakh2100 dataset, which consists of MIDI-synthesized data, raising concerns about the generalizability of the results to real-world music. The use of synthetic data, while convenient, does not capture the complexities of real-world audio, including variations in recording quality, microphone placement, and acoustic environments. Additionally, the evaluation focuses solely on the Si-SDR metric, which, while relevant, does not fully capture separation “quality”. Other metrics, such as SDR, SIR, and SAR, could offer a more comprehensive analysis of the model’s performance, particularly in terms of artifacts introduced by the separation process and the degree of source isolation achieved. Although the authors briefly report results on the MUSDB dataset in the appendix, they only provide results of the Deterministic Model, noting that the diffusion and CD extensions showed no improvement, which they attribute to dataset size limitations. However, many source separation models successfully benchmark on MUSDB, challenging this explanation. The absence of results for the diffusion and CD extensions on MUSDB is a significant limitation, as it leaves the effectiveness of these components unverified on a standard real-world dataset. Incorporating additional datasets, such as MoisesDB [1] and MUSIC [2], would have allowed for a larger and more diverse dataset, strengthening the method’s robustness and improving its generalizability claims. The lack of evaluation on datasets with real-world recordings makes it difficult to assess the practical applicability of the proposed method.

If the authors aim to position their method as state-of-the-art (SoTA) in source separation, they should have tested it more comprehensively across varied datasets and metrics to establish robustness and generalizability. Alternatively, if the focus is to demonstrate the effectiveness of CD, the authors should have either extended their analysis to other data distributions or thoroughly examined why CD works on specific datasets and not others, rather than attributing its limitations solely to dataset size. Unfortunately, the authors have not achieved either, and reliance on a single dataset and limited metrics does not adequately demonstrate the method’s potential, especially for a top-tier conference like ICLR.

### Questions
- Why was a 1D architecture preferred over 2D representations (e.g., complex spectrograms or mel spectrograms with vocoder models)? Are there any findings that suggest better performance with the 1D time-domain approach?
- dataset - What does the percentile of instrumental “presence” mean?
- Baseline systems
    - Were the baseline systems trained from scratch using the same dataset setup as the proposed approach?
    - Table 1: the baseline results are identical to those in [3] (Table 3). Did the authors ensure that the evaluation conditions are consistent?
    - Table 2: the inference time and parameter count for Demucs differ from [3] (Table 4). Could the authors clarify these discrepancies?
- line 307 - can we say CD improves both performance and quality? which metric was used to assess the quality?
- The reviewer didn’t fully get the intention of Figure 2, as it presents results that were observed from previous consistency distillation papers. Why compare CD and Diff according to each denoising steps? Why did the authors use denoising steps of Diff to 5 where it could be denoised with larger number of steps?

[3] Mariani, Giorgio, et al. "Multi-source diffusion models for simultaneous music generation and separation." *in Proc. ICLR* (2024).

-----
- typo @Figure 1 (b) caption: “extantion”
- typo @line 33: “…, as illustrated by the “cocktail party effect” …” → quotation mark
- typo @line 171: “This process continuous until …” → continues
- typo @line 179: “…, CD is a designed as discrete process …”
- Figure 2: better to change the legend “U-Net” to “Deterministic”. use different line style for CD and Diff

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
The paper proposes a novel method of source extraction i.e. the problem of isolating or extracting a specific sound source from a mixture of audio signals. The authors propose a 2-stage pipeline consisting of a discriminative model and a generative model. The discriminative model makes a preliminary estimation of the extracted source x_s given the mixture signal x and the instrument label s. Then, x_s is used as a conditioning input to the diffusion-based generative model to produce a refined version of the extracted source for the instrument s. As the next step, the authors employ knowledge transfer to train a consistency model and speed up the sampling process. The method is tested on data from Slakh2100 and MUSDB18 datasets demonstrating clear advantages over several other models including MSDM and ISDM.

### Strengths
- The paper is well written and easy to follow.  
- The problem addressed by the method is challenging and important for many applications in music information retrieval. 
- The method shows significant improvement over baselines on Slakh2100. 
- Authors successfully train a consistency model and considerably speed up their pipeline.

### Weaknesses
 - Unfortunattely, the full pipeline has demonstrated no improvement on non-MIDI data from MUSDB18 compared to the discriminative part and baseline Demucs v2. The experiment doesn’t provide full understanding of performance of the method on non-MIDI data;
- Source separation problem is treated as a sequence of source extraction problems for each instrument in the mix making either memory or runtime grow linearly with the number of instruments;
- Role of the diffusion-based and/or consistency model used in the method is to refine the outputs of the discriminative model. Both models have U-Net architecture with no essential design changes. Generally, the method doesn’t introduce original design choices.

### Questions
Comparison with Demucs provided in Table 1 doesn’t seem fair as Demucs was trained on much less data. Moreover, Demucs was trained on non-MIDI data and tested on MIDI data while the proposed model was trained and tested on Slakh2100. Did you consider retraining Demucs on Slakh2100 for better comparison?

### Soundness
3

### Presentation
4

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
This paper presents a way to use score-based diffusion models to improve music source separation. By adding a score-based model the performance improves, and consistency distillation improves the model's inference speed and sometimes further improves the performance.

### Strengths
1. This paper demonstrates a new training strategy for source separation models of high SDR and efficiency, which might be beneficial to the community.
2. The improvement of SDR acquired by consistency distillation is pretty interesting. It can open up possibilities for future research.

### Weaknesses
Experiments: The experiments are very weak. Slahk is only a synthetic dataset created by MIDI synthesizers, which generalizes poorly to real-world recordings (as shown in table 3), so a state-of-the-art SDR on Slahk is less meaningful.

The author says that the diffusion model's performance on real-world recordings (MusDB18) is not improved compared to the deterministic model because of the dataset size, and did not report the results in table 3. This raises concerns about the author's conclusion. It would be more appropriate to report whatever the authors got when training the diffusion model and the consistency model using MusDB18. Also, there are many ways to mitigate the dataset size issue by (1) data augmentation like pitch shifting etc [1], (2) combining with other datasets like MoisesDB, and/or (3) using transfer learning.

If the author's claim only holds on a synthetic dataset, it would be highly questionable.

Contributions: It seems that the paper only applies an existing methodology to a specific task. The contribution might be questionable. The idea of using the diffusion model in source separation is not novel either, as cited by the authors.

[1] Défossez, A. (2021). Hybrid spectrogram and waveform source separation. arXiv preprint arXiv:2111.03600.

### Questions
1. The improvement acquired by distillation is questionable. In section 4.2, the model trained by CD uses different hyperparameters (i.e., learning rate) compared to the diffusion model. Could the improvement be caused by learning rate annealing?

2. In 3.2, how is $\bar{x}^\textrm{det}_s$ calculated? It seems in figure 1 that it is from the layers of the frozen u-net. But specifically, which layers? (Also typo in figure 1: diffusion extension?)

3. The title uses the word "source extraction" which seems a little bit strange. Even if each model only extracts one stem at a time, it is usually described as "source separation."

### Soundness
1

### Presentation
2

### Contribution
2
