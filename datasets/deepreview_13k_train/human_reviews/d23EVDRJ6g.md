# MotionDreamer: One-to-Many Motion Synthesis with Localized Generative Masked Transformer

- Decision: Accept
- Scores: 8, 8, 3, 5

## Abstract
Generative masked transformer have demonstrated remarkable success across various content generation tasks, primarily due to their ability to effectively model large-scale dataset distributions with high consistency. However, in the animation domain, large datasets are not always available. Applying generative masked modeling to generate diverse instances from a single MoCap reference may lead to overfitting, a challenge that remains unexplored. In this work, we present MotionDreamer, a localized masked modeling paradigm designed to learn motion internal patterns from a given motion with arbitrary topology and duration. By embedding the given motion into quantized tokens with a novel distribution regularization method, MotionDreamer constructs a robust and informative codebook for local motion patterns. Moreover, a sliding window local attention is introduced in our masked transformer, enabling the generation of natural yet diverse animations that closely resemble the reference motion patterns. As demonstrated through comprehensive experiments, MotionDreamer outperforms the state-of-the-art methods that are typically GAN or Diffusion-based in both faithfulness and diversity. Thanks to the consistency and robustness of quantization-based approach, MotionDreamer can also effectively perform downstream tasks such as temporal motion editing, crowd motion synthesis, and beat-aligned dance generation, all using a single reference motion. Our implementation, learned models and results are to be made publicly available upon paper acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel method for intrinsic generation for motion, i.e., augmenting a single input motion sequence into multiple versions. The paper employs an underexplored generative approach - the masked transformer - and presents SOTA performance. To improve diversity and overall quality, the paper also offers a simple KL-divergence based loss to encourage full usage of the latent space, to mitigate mode collapse. The paper reports a complete evaluation, including comparisons, ablation studies, quantitative evaluation, qualitative evaluation and a user study.

### Strengths
- Paper is well written and easy to follow.
- Proposed method is simple and elegant
- The mask transformer mechanism is a refreshing approach
- Codebook distribution regularization is interesting
- Evaluation is rigorous, including all conventional metrics

### Weaknesses
 - The application is a niche one 
- The method, being simple, is also limited in contribution
- Qualitative evaluation is limited

### Questions
As stated above, I believe that paper presents interesting ideas, and I would like to see this player out there with the other methods. 

My main concern is the scope of impact. Perhaps these ideas can and should be examined in a wider scope:
- can the codebook regularization loss improve other VQ methods off the bat? 
- More ambitiously, can this method be combined with others, for example can the masked transformer be applied in the bottle neck of a diffusion process? or perhaps instead of the VAE?
- similarly, some more discussion regarding the regularization could benefit the paper. What other alternatives could have been employed?

In addition, I would have liked to see some more qualitative results 

Minor concerns:
- Swin is already rather widely adopted and known for shifting windows (Swin-Transformer), I recommend using another name for the sliding window approach (which I find simple and elegant for reducing the receptive field)
- "Crowd motion synthesis" can also be misinterpreted here, as an algorithm to avoid collisions, I would also find a different name here.
- I find figures 1 and 2 a bit exaggerated. The right side of Fig 2 depicts little information for its size. Figure 1 is also rather overwhelming, half of the amount of characters would probably go a long way.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes Motiondreamer, a framework for one-to-many motion synthesis. The paper aims to learn the underlying motion pattern in a given sequence and leverage the motion pattern to generate natural and diverse motions.
The general idea of the paper is to first quantize a motion sequence into tokens, and then train a masked transformer to generate these motion tokens. 
There are two core technical contributions,  one lies in regularising motion tokenization to encourage more coverage, and the other one lies in injecting localality into the makes transformer to encourage motion decomposition.

### Strengths
- The model is well-designed. Given the scarcity of motion data in this one-to-many setting, the inductive bias in the model design is particularly important. The overall framework follows a masked transformer architecture which is simple, but multiple practical techniques have been contributed to balance the motion faithfulness and the motion diversity, including
    - A KL term is added to the quantizer training besides the standard commitment loss to encourage coverage.
    - A sliding window attention that adds locality to the transformer to encourage diversity.
    - A differentiable dequantization loss that helps to compute loss on the motion space.
    
    All of them are well-motivated and make sense to me.
    
- The ablation study is very comprehensive. Although the above techniques, like KL regularisation, are quite standard and empirical, the paper provides detailed experiments to support their importance to the final results. I find those experiments convincing.
- The paper shows qualitative results on a webpage, which generally looks good to me. Compared to SinMDM, the proposed method reduces unnatural motions. Compared to SinMDM, the generated motion seems more diverse.

### Weaknesses
 - Table 1 and Figure 3 are inconsistent in the comparison between GenMM with Ours. Table 1 shows that GenMM has much better coverage than Ours. However, in Figure 3, the failure mode of GenMM is missing a part of the reference motion.
- The beat-aligned dance synthesis application does not convince me. The generated dances have a clear mismatch with the tempo. Most importantly, the application (including implementation details) is not well documented in the paper so I am not fully sure what is happening there, for example, what is a “light-weight encoder-decoder”? To my understanding, the beat-aligned dance is like an extension of the “subpart generation” task while keeping predefined keyposes on the music beats. That is not sufficient to produce a beat-aligned dance in my opinion.
- Some of the techniques could be a little niche to be presented as part of the method. For example, AttnFuse could better fit into implementation details.
- Minor
    - L281: by progressively fill → by progressively filling.

### Questions
Please address the weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a localized masked modeling paradigm designed to learn motion internal patterns from a given motion with arbitrary topology and duration. It introduces the codebook distribution regularization and sliding window local attention (SwinAttn) mechanism to avoid codebook collapse and overfitting.

### Strengths
The codebook distribution regularization effectively prevents codebook collapse. The sliding window local attention mechanism in the Local-M transformer captures local dependencies and ensures smooth transitions across overlapping windows, enhancing the fidelity and diversity of generated motions.

### Weaknesses
This paper applies some recent advancements from the image domain to motion synthesis, which is a commendable attempt. However, the contribution feels somewhat limited. As a work focused on enhancing the VQVAE structure for motion synthesis, the authors might benefit from incorporating insights and experiments from NCP, rather than simply adapting the network architecture.

### Questions
In the final section of the paper, the authors mention several other applications. Could the authors elaborate on how the network architecture performs and what advantages it offers for these tasks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a generative masked model (MotionDreamer) for motion synthesis domain based on the motivation "large datasets are not always available". MotionDreamer designs a local masked modeling paradigm to learn motion internal patterns from a given motion with a key sliding window local attention module. Experiments demonstrate various motion tasks, including crowd motion synthesis, temporal editing and beat-aligned dance synthesis.

### Strengths
- The paper is well-written and is easy to follow. 

- Qualitatively results look impressive. Ablation studies prove the effectiveness of the designs.

- The authors introduce various applications of motion synthesis and achieve great performance.

### Weaknesses
 - Generative masked modeling for motion synthesis has been investigated in many recent works, such as MMM, Momask, MotionGPT, as described in paper. On the other hand, single motion synthesis is also not new, such as SinMDM. It seems that MotionDreamer integrates the techniques of generative masked modeling into the task of single motion synthesis, including motion tokenization and codebook distribution regularization.

- Capturing local dependencies of motion features is quite important for single motion synthesis. SinMDM introduces QnA layers that allow local attention with a temporally narrow receptive field. And MotionDreamer incorporates sliding window local attention to achieve this. Besides, another key design of codebook distribution regularization has been explored in single image synthesis domain. Therefore, I think the technical contribution of the paper is somewhat limited.

-  In Ablation Studies (Sec. 4.4), it's better to use QnA layers in SinMDM to replace sliding window local attention and show the comparison of the performance. Due to the same task, the paper should demonstrate its unique effectiveness.

### Questions
See Weakness.

### Soundness
3

### Presentation
4

### Contribution
2
