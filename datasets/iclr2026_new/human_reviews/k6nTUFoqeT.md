## Human Reviewer 1

### Summary
The paper introduces FASTer, an approach for discrete-token action generation for VLA policies:

- **FASTerVQ (tokenizer)**: A transformer autoencoder with residual VQ (RVQ) over an action patchifier. Training uses a dual-domain reconstruction loss (temporal L1 + DCT-domain L1) to preserve both low and high-frequency motion. The result is a compact, balanced code usage with improved reconstruction.

- **FASTerVLA (policy)**: An autoregressive (AR) policy that (i) adds an action-expert head, (ii) uses RoPE spacing augmentation to avoid positional overfit on fixed horizons, and (iii) employs Block-wise Autoregressive (BAR) decoding with a coarse-to-fine order under a block-causal mask. The paper additionally sketches a “real-time chunking (RTC)” regime for asynchronous control via stochastic training and lightweight logit ensembling.

Across simulators and real-robot setups, the method reports higher success rates and lower inference latency than prior AR tokenizers (e.g., FAST/FAST+), with competitive results to continuous flow/diffusion policies in some regimes. Ablations examine tokenizer design (codebook sizes, RVQ depth, losses) and decoding choices, and provide analysis on vocabulary utilization and reconstruction-error vs compression.

### Strengths
- While built from known parts (transformer RVQ with time+DCT loss, block-wise causal masks for AR, coarse-to-fine action decoding), the specific combination is novel for VLA setting and practically impactful for AR control policies.
- Extensive tokenizer analysis (codebook utilization, reconstruction vs compression rates) and sensible ablations on RVQ/codebook design choices. Reported latency reductions are compelling for real-time control discrete AR policies.
- Method components are described clearly. Design choices are well-motivated (e.g., position overfitting on fixed horizon actions, the coarse-to-fine decode order is intuitive and naturally follows RVQ) accompanied by real world and simulation benchmarks supporting the method.
- Improving throughput/latency without giving up success is valuable in robotics. The work should be useful to groups deploying AR VLAs where continuous policies are costly to train.

### Weaknesses
It is known that diffusion/flow based are slower to train compared to autoregressive models, the paper should report compute comparison between baselines to accurately place the gains in context. I still believe given sufficient compute continuous diffusion/flow policies would outperform discrete AR policies. AR action heads trained with cross-entropy are brittle for real world control, exhibiting unpredictable bin prediction switches with little observation noise. CE loss is non-metric, it only cares about the probability on the ground-truth bin, no matter how the remaining probability mass is distributed among nearby vs far bins. Continuous policies avoid this by design as they directly penalize errors proportional to deviation. How much does the FASTerVQ tokenization mitigate this?

### Questions
- How does Block AR differ from similar approaches used in discrete diffusion literature (see Block Diffusion [1])? It would be good to position this paper appropriately and add references.
- It would be good to have comparisons against $\\pi$-0.5 which is an improved version of $\\pi$-0 with better generalization.
- Was a single policy trained for all LIBERO task suite or each LIBERO suite had a separate policy? OpenVLA-OFT attains higher success rate when using a single policy setting, so the paper should clarify here and update the results accordingly. OpenVLA-OFT also has a FiLM variant which improves language grounding. Please take a look at Appendix in [2] for details and update accordingly.
-  There seems to be some discrepancy in reported latencies for different models and OpenVLA-OFT paper Table III, some clarification here would be helpful. also the main paper should include inference time analysis, detailing out inference latency, action chunk size used and max control frequency supported.
- Could you provide some insight on Figure 5 (c)? Why compression ratio is so different for different dataset?


[1] Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models

[2] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper studies the action tokenization problem, which is valuable for performance and efficiency of autoregression-based policy. The authors propose FASTer, an improved version upon FAST, by incorporating learnable vector quantization (instead of fixed procedure) to improve the compactness and fidelity of action tokenization.

### Strengths
- The paper studies an important problem that carries strong practical applications. 
- The proposed method makes sense, is simple yet effective. 
- The proposed method is extensively evaluated with different metrics, in diverse robot environments, including real-world.

### Weaknesses
- The texts in many figures are quite small and not easy to read especially when printed, particularly in Fig. 2 and Fig. 3.

- Page 4 details the action tokenization process and components. I believe it would be easier for readers if there is an algorithm block that outlines this procedure, like FAST does. Currently, it takes some effort to gather everything from text. 

- [1] is a recent work that incorporates autoregressive action chunk generation without an explicit action tokenizer, and its proposed technique is very relevant to the block-wise autoregression. The authors are recommended to include this in the related work.   [1] Autoregressive Action Sequence Learning for Robotic Manipulation (RAL 2025)

### Questions
- How does it work with diverse robots and action types? If I train a single FASTer tokenizer for multiple robots, does this mean (1) a slower encoding/decoding process, (2) a less compact coding? 

- Fig7 shows FASTer underperforms than Pi0 in in-distribution tasks. I understand the emphasis is OOD performance in that figure, but why is that? 

- Does the space augmentation only change position embedding, or actually change the sequence values? If the latter, is there an example of the space augmentation? 

- Regarding the block-wise autoregression, I am very interested in the step size (block size) in the autoregression. In the paper, the step size = B (size of one codeblock). But what would the performance possibly be if the block size is 1 or N, or other number? Does a irregular granularity will affect autoregression performance?

- Is it possible to provide some failure cases and related analysis?

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper is about making (auto-regressive) vision language action models more useful in contexts like robotics where fast inference and precise reconstruction are important for overall system performance and inference time impacts which action frequency tasks can have. The main focus is on the action tokenization part. The approach designs action tokens (action representation) by performing residual vector quantization and  trains reconstructing action sequences in the time and frequency domain (loss functions). This is supposed to result in compact and highly compressed action sequences. The inference approach infers multiple tokens in parallel by block-wise decoding. The paper also establishes a larger benchmark, collecting several real robots and simulations.

Importantly, this approach is supposed to surpass non-auto-regressive models in inference speed and reconstruction accuracy.

### Strengths
- The paper is nicely written and pedagogical, especially the introduction section and the related work section.

- The general idea of patchifying the continuous actions seems very reasonable.

- RVQ is generally very suitable for this problem.

- Adding the DCT to the step-wise reconstruction loss makes sense for capturing the overall trend as long as the action sequences behave with trends within horizon H.  

- The paper contains a large set of experiments and evaluations which provide insight in the performance and tradeoffs of the proposed method.

### Weaknesses
- The reusability in some figures is low due to the choice of colors, lack in contrast, and lack of clear captions. Page 7 is a good example for this issue. Red-green contrasts should be avoided in general. 

- There are a few types in the manuscript, repeated words, and wrong references (e.g. to Fig. 5 on page 7).

### Questions
- When introducing the VRR measure for evaluation, the authors write that a parameters is set "corresponding to an allowed error of approximately 1cm". It is not clear what this means. Is this 1 cm Euclidean error at the end-effector pose (in case of manipulation)? For many robotic tasks, 1 cm error is substantial and means that the execution of the task will fail. The authors might want to elaborate on the VRR. What happens if the threshold is set of 0.5 cm or 1 mm?

- The related work section makes little effort to contrast the proposed method with the state of the art. While the experiments speak for themselves in terms of quantitative results, it would be an improvement if the authors could also argue the improvement over the state of the art conceptually.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
2

---

## Human Reviewer 4

### Summary
The paper proposes a new learnable tokenizer scheme based on residual vector quantization (RVQ) for robotic manipulation datasets. A custom action patchifier is used to group timesteps and physically similar action dimensions together which is subsequently fed into an RVQ model learning a coarse-to-fine representation of action signals. The tokenizer is trained on a combination of RVQ losses alongside local and global action reconstruction objectives. Furthermore, a custom VLA architecture utilizing the new tokenizer is presented which adds block-wise autoregressive prediction of multiple tokens with a custom decoding order to speed up inference.

### Strengths
-	Overall, the paper is well written and clearly motivates the drawbacks of previous tokenizer designs in VLA models. It encompasses the most relevant previous work and gives a clear outlook of which open problems in the field it tackles.
-	The proposed tokenizer (FASTer) for VLA models addresses relevant challenges of action tokenization, such as achieving good reconstruction quality with high compression rates. The choice of RVQ for this task seems adequate and timely: Learnable tokenizers have shown strong initial results in robotics but rely on partially manual design for converting continuous signals into discrete codes.
-	The use of a custom decoding order in combination with the RVQ tokenizer is well thought out, resembling the strengths of diffusion-based action prediction heads (going from low frequency to high frequency reconstruction) without the need for diffusion training. 
-	An extensive list of experiments is conducted, comparing FASTer VLA with relevant baselines such as pi0 using the FAST tokenizer on a wide range of benchmarks. Aside from inference speedups, FASTer VLA achieves broad success rate improvements across the board with only VLABench lacking behind, suggesting strong generality of the method.
-	The performance of the FASTer tokenizer itself is also analyzed properly, showing good scalability and generalization to out of distribution data.

### Weaknesses
-	Aside from the LIBERO experiments in Table 1, most results seem to combine FASTer VLAs blockwise autoregressive decoding (BAR) with the FASTer tokenizer, making it difficult to judge the impact of the tokenizer itself on success rates. Optimally, a tokenizer should be mostly agnostic to the choice of architecture. This is partially shown in Figure 6 with different VLM backbones but still might rely on custom decoding schemes (see first question).
-	The encoding times of the FASTer tokenizer seem high (150ms on LIBERO) compared to the runtime of the base pi0 model. To the best of my understanding, the paper does not isolate the tokenizer runtime as a standalone metric in the inference speed results.

### Questions
-	It seems that BAR decoding in combination with FASTer leads to significantly higher success rates than just using FASTer. Could we expect similar gains when using BAR in combination with other tokenizers? I would be curious to see the performance when using the FAST tokenizer with BAR to fully determine the benefits of FASTer versus FAST.
-	Similar to the previous question, I  would be curious how much using BAR decoding offsets the potentially slow tokenizer.

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
3