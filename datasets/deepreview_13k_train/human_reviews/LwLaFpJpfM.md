# Active Audio Cancellation with Multi-Band Mamba Network

- Decision: Reject
- Scores: 6, 3, 6, 8

## Abstract
A novel deep learning approach for Active Audio Cancellation (AAC) is presented, which surpasses traditional Active Noise Cancellation (ANC) by effectively canceling any audio signal, regardless of its spectral content. We propose, for the first time, a deep learning approach to AAC using a novel multi-band Mamba architecture. This architecture partitions input audio into multiple frequency bands, allowing for precise anti-signal generation and enhanced phase alignment across frequencies, thereby improving overall cancellation performance. Additionally, we introduce an optimization-driven loss function that provides near-optimal supervisory signals for anti-signal generation. Our experimental results demonstrate substantial improvements over existing methods, achieving up to 7.2dB gain in ANC scenarios and up to 6.2dB improvement in AAC for voice audio signals, outperforming existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
A novel deep learning approach to Active Audio Cancellation (AAC) is proposed based on the multi-band Mamba architecture. The paper claims that it is a more broadly defined problem than the traditional ANC problem as it can handle various other sounds. The proposed method also employs a two-stage training paradigm to overcome the nonlinearity of the ANC path. The performance appears to be good based on the simulated experiments.

### Strengths
- The multiband Mamba architecture appears to be a reasonable choice for the task. 
- Ablation tests and other experimental designs (including the choice of datasets) are well thought-out. 
- The proposed method improves the other baseline methods.

### Weaknesses
 - Although it is a reasonable choice, the proposed multiband Mamba architecture appears to be a straightforward extension of existing architecture into a multiband version. Algorithmic contributions are thus limited. 
- It is not clear why the second stage loss function is needed, if the secondary path filter and loudspeaker processing part is differentiable. Specifically, the secondary path S, derived from room simulation, is a convolution filter and thus differentiable. The need for a separate loss function (Eq. 12) is unclear, especially since the first stage should already account for the secondary path. It is not clear if Eq. 12 is solely about f_LS rather than f_LS AND S.
- All experiments are based on image method-based room simulation. Its effectiveness on real-world test signals has not been reported. 
- The system takes in 3 sec of audio during training. It is not reported what's the delay of the system during the inference. Since most of the ANC applications require real-time processing, this delay might be critical for the proposed method to be useful. 
- Some sections are written without any line breaks, seriously harming readability.

### Questions
- It seems that the second loss function is to improve the model's performance after doing the first round, where the error is supposed to be reduced. The authors said that the secondary path S and the loudspeakr function f_LS is nonlinear, making the algorithm effectively update the Deep AAC model. However, these two functions must be differentiable anyway, so they were part of the inference in the first round. Then, the first round must be able to go through them and update the model anyway? Specifically, S is just a convolution filter acquired from the room simulation? So it must be differentiable? If so, isn't eq 12 solely about f_LS rather than f_LS AND S?

- I think it's an overclaim that what this paper aims to do is a totally different task than ANC. Although ANC, as its name suggests, might be about reducing noise, many systems are trying to cancel "any" sound that's coming into the system, as far as I know.

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
This paper presents a deep learning-based approach for active audio cancellation (AAC), which is a broader problem that encompasses active noise cancellation (ANC) as a special case, where the goal is to suppress general audio signals rather than only the typical noise-like signals. To better handle the more complex case of general audio than just cancellation of noise, the authors present DeepAAC, a deep neural network model featuring three key components: i) multi-band processing, ii) the Mamba architecture (a recent state space model (SSM)), and iii) a new loss function utilizing the so-called "near optimal anti-signa." Experimental results on simulated audio data show the advantages of the proposed method over conventional adaptive filtering-based approaches as well as recent deep learning-based models in terms of the normalized mean squared error (NMSE) across several speech and noise types and settings of loudspeaker distortion. Speech quality evaluations are also provided through speech enhancement experiments in addition to NMSE measurements.

### Strengths
- Utilizing the state space model (Mamba) in the context of active audio or noise cancellation seems novel.

- Comparison with both conventional adaptive filtering approaches (least mean square (LMS) type algorithms) and deep learning-based models is nice.

- Demonstrating better performance over existing approaches across several speech and noise types, including consideration of different settings of the loudspeaker nonlinearity, and various signal-to-noise ratios (SNRs) in speech enhancement tasks.

### Weaknesses
 - The proposed components lack evidence to well support their respective merits. To be more specific,
 > - **Multi-band**: Although Table 4 presents improved NMSE as the number of bands increases, it is not clear if such improvement is obtained due to using multiple frequency bands, or just mainly due to having a larger model size for the case of more bands (e.g., 1 band (15.8M) vs. 4 bands (40M) given in Table 6). Therefore, it is suggested that the authors compare multi-band models to single-band models with equivalent or similar parameter counts, to more conclusively demonstrate the benefits of the multi-band approach.
> - **Mamba blocks**: The benefits brought by using the SSM (Mamba) layers are not demonstrated. It would be nice if the authors conduct ablation studies comparing Mamba to other architectures like transformers, LSTMs, or CNNs while keeping other aspects of the model constant. This would provide clearer evidence of Mamba's advantages in this context. The current comparison lacks crucial details such as the number of layers, kernel sizes, and the uni- or bi-directionality of the compared modules, making it difficult to assess the fairness of the comparison. Furthermore, the computational complexity of Mamba compared to transformers is not analyzed, which is a key factor given that one of the main advantages of SSMs is their linear complexity scaling compared to the quadratic scaling of transformers. This is particularly important for longer audio inputs, where the efficiency gains of Mamba should be more apparent.
> - **NOAS loss**: The motivation of using the near optimal anti-signal (NOAS) loss in eq. (12) is not clear. On lines 239-243, it states that `` The difficulty arises because if the secondary path $S(z)$ attenuates certain frequencies, the error signal $e(n)$ in these bands will be non-zero since the primary signal $d(n)$ may contain energy in these frequencies. Consequently, the ANC controller will encounter errors during the training process regardless of its estimation of the anti-signal $y(n)$.'' However, as shown in eq. (11), the secondary path $S$ is still presented in the optimization criterion. As a result, the aforementioned difficulty due to the attenuation effect of $S(z)$ still remains. Then, how does the NOAS help in alleviating such issues? Please provide a more detailed explanation or mathematical justification for how the NOAS loss addresses the issues with frequency attenuation in the secondary path. Additional comparative experiments showing the performance with and without the NOAS loss on such aspects could also help clarify its benefits.

- The other weakness of the paper is that the proposed DeepAAC is evaluated on simulated data using a room acoustics simulator. It is more desirable to also test the system on real-world recorded audio data with an actual headset, or at least using real-world measured acoustic paths $P(z)$ and $S(z)$ to simulate the test samples (e.g., *Liebich, Stefan, et al. "Acoustic path database for ANC in-ear headphone development," Universitätsbibliothek der RWTH Aachen, 2019*), for better demonstrating the proposed method's capabilities.

### Questions
- In Section 3.4, could you elaborate on the gradient descent-based algorithm employed for eq. (11) during a pre-processing stage? Also, as there is no nonlinear terms in eq. (11), can the optimal solution $\mathbf{y}^*$ be given by just solving the linear least squares problem (where a closed-form solution is available) of it? If yes, could you clarify why choosing a gradient descent-based algorithm over a closed-form solution, and what advantages, if any, this iterative approach offers over direct linear least squares solving?

- Should the $\mathbf{s}$ in Figure 3 be upper-case $\mathbf{S}$? 

- The font size and resolution of plots in Figure 4 and Figure 5 can be improved for better viewing.

-  Section 4.1, line 347, should it be "Table 1 presents.." instead of "Table 4 presents..."?

- For ablation studies in Section 4.3, does ``without NOAS optimization'' mean just using the $\mathcal{L}_{\text{ANC}}$ in eq. (10)? Please explicitly state what loss function is used when NOAS optimization is not applied.

- In Section 4.3, lines 427-428, why is it interesting to see that the "+S-Multiband-NOAS" configuration performance is lower than "+M-Multiband-NOAS"? The former has a much smaller model size (8M) according to Table 6 than the latter (15.8M), so it is not surprising that the performance is worse of the former.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Noise cancellation remains an important problem, even if it has been studied for a long time and machine learning can be a useful component. This paper addresses a particular subcategory of noise cancellation, active audio cancellation, where, apparently, no prior machine learning models have been proposed. While noise cancellation is important, I did not find the subcategory particularly important, and there were no supporting arguments for this application scenario.
The methodology used in the study is mostly high quality. My only worry is that the fixed physical configuration of microphones and loudspeaker will diminish the practical value of the results.

### Strengths
The background is explained in admirable detail.
The machine learning methodology is high quality.
Writing is good.

### Weaknesses
The application scenario is not explained sufficiently to motivate the *audio* cancellation.
Fixed physical setup of sound sources and sinks limits the generality of results.

### Questions
Problem statement
- The differentiation between *noise* cancellation and not active *audio* cancellation is questionable. For typical applications, any sound that is not desired is noise, and the undesired sounds can be any type of audio. The authors are probably right in that noise cancellation has been applied for most application scenarios, but that is the typical desired functionality. It is useful to emphasise the most typical scenarios in training; thus, focusing on noise is usually beneficial. Authors should, therefore, demonstrate why active *audio* cancellation is a desired functionality. What is the expected application scenario where generic audio is the expected distortion?
The vocabulary is unclear; how do you define the secondary path? A figure would have been helpful in Section 3.1. It might be that Figure 2 was intended for this purpose, but it was never referenced in the text. However, that figure does not show how sounds travel in the acoustic space.

Experiment setup
- The setup is otherwise good, but it can be a problem that the physical configuration of microphones and loudspeakers were fixed. This implies that the model would have to be trained for every particular scenario, which is impractical. This is a potential problem unless experiments demonstrate otherwise, but this was not part of the experiments. At least, it has to be mentioned as a drawback of the proposed method.

Minor comments
- In Eq 4, for visual clarity, please scale the parenthesis to match the content inside them (in LaTeX this can be done by \left and \right, before the parenthesis sign)
- Please mention the method you use for frequency decomposition

### Soundness
3

### Presentation
2

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
This paper proposes a Active Noise Cancellation (ANC) network. It represents the first attempt to actively cancel general audio signals with deep learning. The paper introduces a segmentation strategy for separate modeling and incorporates Mamba as a sequence modeling module. Additionally, a new training strategy is proposed during training to generate more fitting anti-signals.

### Strengths
This paper is the first to consider actively canceling general audio signals to address the issues inherent in Active Noise Cancellation. It incorporates a frequency band segmentation strategy in its design to better focus on the characteristics of each frequency band and introduces Mamba for sequence modeling. In addition to structural innovations, the paper proposes a Near Optimal Anti-Signal Optimization strategy to solve the problem of different paths producing different frequencies.

### Weaknesses
The first issue is an expression problem at the beginning of Section 4.1, which should state "Table 1 presents the NMSE for ANC algorithms..." instead of "Table 4 presents the NMSE for ANC algorithms...". The second issue is that the baseline models used for comparison are relatively old and do not strongly demonstrate that this model has reached the state-of-the-art (SOTA). Specifically, while ARN is a relatively recent baseline, the field has seen rapid advancements, and the comparison should include more recent and competitive methods to truly establish the proposed model's superiority. The third issue is that the proposed optimization strategy first finds y' based on the given reference signal x, and then finds the final target y based on y'. Essentially, it is still based on the reference signal for the loss function. Therefore, the significance of this approach and why it leads to performance improvements need to be clarified. The explanation of how this approach addresses the secondary path's frequency response is not sufficiently detailed, and it is unclear how this optimization avoids the model being penalized for high energy at the error microphone when the secondary path cannot fully compensate for the primary path.

### Questions
see in weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
