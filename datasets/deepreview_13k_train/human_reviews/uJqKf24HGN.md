# UniCon: Unidirectional Information Flow for Effective Control of Large-Scale Diffusion Models

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
We introduce UniCon, a novel architecture designed to enhance control and efficiency in training adapters for large-scale diffusion models like the Diffusion transformer. Unlike existing methods that rely on bidirectional interaction between the diffusion model and control adapter, UniCon implements a unidirectional flow from the diffusion network to the adapter, allowing the adapter alone to generate the final output. UniCon reduces computational demands by eliminating the need for the diffusion model to compute and store gradients during adapter training. UniCon is free from the constrains of encoder-focused designs and is able to utilize all parameters of the diffusion model, making it highly effective for transformer-based architectures. Our results indicate that UniCon reduces GPU memory usage by one-third and increases training speed by 2.3 times, while all maintaining the same adapter parameter size. Additionally, without requiring extra computational resources, UniCon enables the training of adapters with double the parameter volume of existing ControlNets. In a series of image condition generation tasks, UniCon has demonstrated precise response to control information and excellent generation capabilities. UniCon makes the control of large-scale diffusion models feasible and provides a basis for further scaling up of diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents UniCon, a novel architecture aimed at enhancing control and efficiency in training adapters for large-scale diffusion models, such as the Diffusion Transformer (DiT). Unlike existing methods that involve bidirectional communication between the control adapter and diffusion model, UniCon employs a unidirectional information flow, where information flows only from the diffusion model to the adapter. This enables the adapter to generate the final output independently, reducing computational demands and memory requirements by eliminating the need for the diffusion model to compute and store gradients during adapter training.

### Strengths
UniCon’s key strength is demonstrating that gradients through the base diffusion model are unnecessary for effective control, achieving this with a unidirectional flow design. This architecture enables the adapter to independently generate outputs, significantly reducing memory usage and computational costs by omitting gradient calculations for the base model. The work is substantiated with an ablation study for different architectural alternatives.

### Weaknesses
I would have liked to see an insightful reasoning, why the unidirectional flow apparently increases the quality of the output. Would the results converge after longer learning times? Is the effect comparable to a "low" rank regularization (somewhat far fetched)?

The sentence in line 155 "Given a ..." is broken.

### Questions
The sentence in line 155 "Given a ..." is broken.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed a new method called UniCon, using unidirectional flow for adapting diffusion models. Validation had been made on both the SD U-Net diffusion model and the DiT diffusion model, on several datasets. It turns out that UniCon reached a good result of memory reduction and training speeding up while maintaining the same adapter parameter size and generative capabilities.

### Strengths
1. The motivation makes sense: for a faster and more efficient training of controlled generation of diffusion models, towards further scaling up (good for training of scaling up).
2. The evaluation is clear and the experiment results are abundant.
3. Results of unidirectional flow are promising, making a good contribution to the controlled generation of diffusion models and further work.
4. The appendix section of the paper is thorough and contains quality information.

### Weaknesses
1. A more detailed introduction could be made of diffusion models for readers' better following. Along with a detailed explanation of ControlNet.

2. The speeding up and memory reduction are mainly for training. But during inference, will UniCon be similar even worse in latency and memory due to the more complex structure (e.g., more Control Blocks compared to the vanilla one on UNet structure, and each block seems to contain more layers of MLP)? This also seems to explain why UniCon performs better because the block structure is more complex.

3. It seems that the page number of Page1, the header and the edge of Page2 can be incorrectly hyperlinked.

### Questions
1. Can you provide a schematic or computational rule of forward computation and backpropagation during training to compare ControlNet and UniCon? Just looking at Figure1 and Figure2, readers may not understand why UniCon does not require computing and storing gradients for the diffusion model while ControlNet requires. As in Line 187: "For example, when training ControlNet for DiT, when the gradient of ControlNet itself occupies about 18GB VRAM, the gradient brought by the DiT diffusion model needs to occupy 16GB VRAM." 
2. As for the choice of the connector (Line 459) in Table 1b, it seems that each ZeroFT contains $\textbf{2 layers}$ of ZeroMLP (joined by multiplication and addition). Is the ZeroMLP compared here consisting of $\textbf{single-layer}$ structure as the one in the original article? Is it unfair? More rigorous experiment results may be needed to illustrate ZeroFT's effectiveness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces UniCon, a novel approach for effective and efficient control in large-scale diffusion models using unidirectional information flow. The presentation is overall quite good, with clear and informative figures and tables, although there is some room for improvement in the writing accuracy. The experiments appear comprehensive and solid. I look forward to seeing feedback from other reviewers to ensure that I haven’t missed any important aspects.

### Strengths
1. The paper is well-structured and easy to follow. Visual representations in figures and tables effectively support the text.

2. The "Unidirectional information flow" concept is novel, ensuring conditional inputs do not interfere with the inherent data structure, a significant advantage.

3. The experiments conducted are comprehensive, validating the proposed method’s efficiency and performance across different tasks and models.

### Weaknesses
1. A minor typographical error was noted: "PixeArt" should be corrected to "PixArt" (Line 122).
2. The statement that current designs may not be suitable for transformer-based diffusion models (Line 198-205) could be more thoroughly justified, as it might not hold universally. Specifically, the claim that methods like ControlNet and T2I-Adapter, which are primarily designed for UNet architectures, would be inherently suboptimal for Diffusion Transformers (DiT) needs more rigorous backing. While architectural differences exist, it's not immediately clear why these methods couldn't be adapted effectively, or why they would be fundamentally limited in DiT without further analysis.
3. There is an error in Table 1(a), where an incorrect metric has been highlighted and needs correction.
4. I'm afraid I have to disagree with the conclusion drawn in lines 372-376, as the phenomenon might be attributed to the decoder being a more significant part of the model. In fine-tuned models, there is often a trade-off between image quality and controllability—enhanced controllability may lead to a reduction in image quality. The argument that controlling the decoder leads to higher constraints, while plausible, needs more empirical evidence to support the claim that this is the primary reason for the observed trade-off. It could be that the decoder's direct influence on the output is simply more sensitive to any introduced constraints, rather than inherently causing higher constraints.
5. Additionally, "generation effect" does not seem to be the most appropriate term for this context and could be replaced with a more accurate expression.

### Questions
* Will the code and weights be released to facilitate broader adoption and further development by the research community?

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
3

### Summary
This paper presents UniCon, tailored for both UNet-based and DiT-based large-scale diffusion models. The proposed unidirectional flow method is the core method, allowing the adapter alone to generate the final output to reduce VRAM memory consumption. Experiments demonstrate that UniCon achieves good generative performance with lower resource consumption.

### Strengths
1. The writing of this paper is good and easy to read.

2. UniCon offers a new approach to integrating adaptors in DiT-based diffusion models.

3. The visualization and quantitative results from the experiments validate the effectiveness of the method.

### Weaknesses
1. UniCon designs two different methods for incorporating adaptors in UNet-based and DiT-based diffusion models, as shown in Figure 2. The differences between these methods are significant; for instance, UniCon for UNet adds many concatenation operations and skip connections, while the DiT-based model employs a different serial structure.
   - a) What specific motivations led the authors to design these two distinct structures?
   - b) If the method needs to adapt to other frameworks, such as Mamba-based diffusion or XLSTM-diffusion, would the adaptor structure need to be redesigned? This raises concerns about the generalizability of UniCon.

2. One of the core contributions of this paper is the introduction of the ‘unidirectional’ concept. Unlike ControlNet, which still uses the original diffusion model as output and therefore needs to store diffusion gradients, UniCon modifies this by freezing the original diffusion and using the adaptor as output, thereby reducing VRAM consumption. This makes UniCon fundamentally similar to the LoRA adaptor.
   - a) How does the performance of UniCon compare to LoRA methods?
   - b) Has the UniCon-encoder version been tested? This could be considered a unidirectional ControlNet, and I believe it is an essential comparison to make.

3. I appreciate the extensive ablation studies conducted by the authors on different structures (in Figure 3) to validate the framework's effectiveness; however, the results are not surprising. The full version which has the most parameters, performs the best, which is expected. More importantly, what motivation or significant proof do these ablation studies provide for the design of this method (please do not conclude that the full version is better than other non-full structures)? If none, these results would render the paper more of an empirical study.

4. For both the main experiments and the VRAM comparison experiments, please include comparisons with ControlNet-Unidirectional-Encoder, as this is a core experiment to validate the effectiveness of the unidirectional method.

### Questions
Please see the weaknesses. 

If I misunderstand any aspects, I welcome the authors to clarify and discuss.

### Soundness
2

### Presentation
3

### Contribution
2
