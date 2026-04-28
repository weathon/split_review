# EM-GANSim: Real-time and Accurate EM Simulation Using Conditional GANs for 3D Indoor Scenes

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 5, 8

## Abstract
We present a novel machine-learning (ML) approach  (EM-GANSim) for real-time electromagnetic (EM) propagation that is used for wireless communication simulation in 3D indoor environments. Our approach uses a modified conditional Generative Adversarial Network (GAN) that incorporates encoded geometry and transmitter location while adhering to the electromagnetic propagation theory. The overall physically-inspired learning is able to predict the power distribution in 3D scenes, which is represented using heatmaps.  Our overall accuracy is comparable to ray tracing-based EM simulation, as evidenced by lower mean squared error values. Furthermore, our GAN-based method drastically reduces the computation time, achieving a 5X speedup on complex benchmarks. In practice, it can compute the signal strength in a few milliseconds on any location in 3D indoor environments. We also present a large dataset of 3D models and EM ray tracing-simulated heatmaps. To the best of our knowledge, EM-GANSim is the first real-time algorithm for EM simulation in complex 3D indoor environments. We plan to release the code and the dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents a generative framework for simulating Electro-Magnetic wave propagation, as a faster replacement for ray tracing approaches usually used in this application. Authors propose a method based on using cGAN and regularized by physical constrains to generate plausible propagation heatmaps given the structure of the scene. They show through experiments that although the performance is not on-par with Ray Tracing methods, this method allows for a faster simulation.

### Strengths
- Proposing an exciting application for cGANs and generative models in simulating EM propagation
- Providing a dataset of 64M simulated heatmaps with various indoor models
- Adding physical inductive bias to the model so that the generations are physically plausible.

### Weaknesses
Main:
- The proposal to use random input to a GAN to avoid mode collapse is not very well-justified. The proposed set-up is very similar to the common conditional GANs which can easily have mode collapse. Further when adding regularizations, such as the physical regularizations proposed, the risk for mode collapse is increased. The authors mention building the model from simpler problem up to the aimed taks and this helps with fine-tuning and perhaps mode collapse. It would be great to have more experiments/analysis on  what is the breaking point and why the model is stable in its final version.

Minor:
- What representation is used for the conditional geometry? A more thorough description of the modality in line 162 would be helpful. It is unclear how the 3D model is encoded and given to a GAN.
- Figure 2 should be labled with yours vs baseline so its easier to read. The interpretation in the caption as what is the weakness vs strength of your method is not easily understandable from the heatmaps and would be great to highlight them visually.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents EM-GANSim, a learning-based approach for real-time electromagnetic (EM) propagation simulation in indoor environments. The core technical contribution is a modified conditional GAN architecture that incorporates both geometric information and transmitter location to predict power distribution heatmaps while adhering to electromagnetic propagation principles. The authors propose a physically-inspired learning framework that integrates direct propagation, reflection, and diffraction effects through specialized loss terms in the GAN's objective function.

The method claims to achieve comparable accuracy to traditional ray tracing-based simulators while offering significant speed improvements (reported as 5X faster). The authors evaluate their approach on 15 indoor scenes and provide ablation studies examining the impact of noise and physical constraints. They also introduce a dataset comprising over 2,000 indoor scene models with corresponding EM simulation heatmaps.

While I am not an expert in electromagnetic propagation simulation and wireless communications, the paper appears to address an important practical challenge in real-time EM simulation. However, there is some ambiguity in how the method handles true 3D environments versus 2D representations, and the room generation and data preparation processes could benefit from clearer documentation. The paper presents an interesting application of deep learning to physics-based simulation, though both its theoretical foundations and physical accuracy need closer examination.

### Strengths
- The paper presents an interesting application of conditional GANs to EM simulation. While both GANs and EM simulation are established fields, their combination for real-time indoor propagation simulation represents a fresh approach to an important practical problem.
- The method achieves notable acceleration (reported 5X speedup) compared to traditional ray tracing methods. If these results can be thoroughly validated, this could be valuable for real-time applications.
- The attempt to incorporate electromagnetic principles through specialized loss terms (direct propagation, reflection, and diffraction) shows thoughtful consideration of the physics involved, though the theoretical guarantees need more examination.
- While the dataset generation process needs better documentation, the collection of indoor scenes and EM simulation results could be useful for future research in this direction.

### Weaknesses
 - A weakness is the unclear treatment of "3D" simulation. While the paper claims to handle "3D indoor environments," the evidence presented is primarily 2D heatmaps. There's no clear explanation of how height information is processed in the network, no visualization of vertical propagation effects, and no analysis of height-dependent signal variations. Table 2 only specifies area (square meter) without height information. The paper needs to either demonstrate true 3D capability, with visualizations showing signal variations across different heights, or clarify that it's a 2.5D approach, explicitly stating the limitations of the method in capturing full 3D propagation effects. The current presentation lacks the necessary detail to assess the method's ability to model true 3D electromagnetic behavior.
- Critical details about the "2K+ models and 64M heatmaps" are missing. The paper doesn't explain how these indoor scenes were generated, validated, or processed. It is unclear if these are real-world scans, procedurally generated, or a combination. The lack of information regarding the distribution of room sizes, shapes, and material properties makes it difficult to assess the dataset's representativeness and the generalizability of the proposed method. Without this information, readers cannot assess data quality or reproduce the results. The paper should also specify how the material properties were assigned and validated, and whether the simulation accounts for frequency-dependent material characteristics.
- The method description lacks important specifics. The GAN architecture details, such as the number of layers, filter sizes, activation functions, and the specific structure of the generator and discriminator networks, are not fully described. The training process, including batch size, learning rate, and optimization algorithm, is not fully specified. The physics-based loss weights lack justification, and there's minimal discussion of training stability, such as the use of techniques like gradient clipping or early stopping. The paper should provide a more detailed description of the network architecture and training procedure to ensure reproducibility.
- The experimental validation relies mainly on MSE comparisons. The performance measurements lack important context - hardware specifications, memory requirements, and preprocessing costs are not reported. The gap between training (3 dbm²) and testing (8.5 dbm²) MSE also needs explanation. The paper should include more detailed performance metrics, such as peak signal-to-noise ratio (PSNR) or structural similarity index (SSIM), to provide a more comprehensive evaluation of the method's accuracy. Furthermore, the computational cost of both training and inference should be reported, including the training time, inference time per scene, and memory usage, to allow for a more thorough assessment of the method's practicality.

### Questions
- Could you clarify how the method handles true 3D propagation versus 2D layout information? The current results only show 2D heatmaps. Could you provide vertical propagation results at different heights? How does the network architecture specifically process and maintain height information?
- Please describe in detail how the 2K+ room models were created/sourced. What is the distribution of room types, sizes, and configurations in your dataset? How to ensure the synthetic scenes are physically realistic? How are different materials modeled and validated?
- How to determine the weights (α, β, γ) in the physics loss function? What measures are taken to ensure training stability? How to handle varying room sizes in the network?

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
3

### Summary
The authors propose a novel approach to real-time electromagnetic (EM) propagation simulation in complex 3D indoor environments, utilizing a physics-inspired conditional generative adversarial network (cGAN) model. This research is positioned as the first real-time algorithm for EM simulation in these environments, and it holds potential value for applications such as 5G network planning, wireless communication system design, and dynamic indoor environments requiring rapid signal strength calculations.
### Post Discussion.
Thanks for the author's explanation and for their efforts to clarify. These clarifications have addressed some of my concerns. Although I am not an expert in the EM simulation field, I have read many related papers and am very familiar with cGAN. Considering cGAN's inherent instability, the reliability of the underlying theory, and the introduction of numerous hyper-parameters, I am concerned about how this method would perform in real-world situations. Therefore, I have ultimately decided to give this paper rating 5.

### Strengths
The employment of cGAN itself is novel, though it seems to me not much significant change is made to the cGAN architecture and it's more like a domain adaptation. The equations in the paper are quite solid, showing the authors good understanding. The paper has strong experiments across 15 scenes with clear performance metrics showing 5X speedup. The ablation studies are well-structured and there is thorough comparison with established methods demonstrate robust methodology.
The proposed method achieves an impressive real-time speed while maintaining robustness, which suggests the method is of good quality. 
The authors claim to release the code and data to benefit the community.

### Weaknesses
1. The paper lacks comparisons with state-of-the-art methods. It only presents scores in comparison to DCEM, and the detailed quantitative results are relegated to supplementary materials rather than the main manuscript. I've calculated the detailed score: GAN-based (dBm²): 8.69; DCEM (dBm²): 7.89.
This suggests that the GAN-based method performs slightly worse than the DCEM method introduced at VTC 2022. Given the recent methods proposed in the literature (Vaganova et al., 2023; Wang & Manocha, 2023; Haron et al., 2021; Gómez et al., 2023), incorporating more experimental results could lead to a fairer and more comprehensive evaluation.
2. Though the proposed method is faster than traditional RT-based methods, it still takes 3-4 seconds to simulate one room. This is far from what the author frequently claimed to contribute to the 'real-time data analysis.' If the real-time is for per data point, then the traditional RT-based methods are real-time, too.
3. The introduction could be strengthened by including a more detailed rationale for using cGAN in this context, specifically on how its features address the problem. Although section 5 provides some of this analysis, highlighting it earlier would improve the logical flow.
4. The qualitative comparison is not sufficient, and the conclusion "We see with GAN-based methods that the heatmaps show less MSE in general captures and exhibit more pronounced areas of both high and low signal strength, suggesting a finer granularity in the simulation of received powers." is ambiguous. How can the simulation judge by "more pronounced areas of both high and low signal strength"? Besides, the mean mse is higher!

Minor:
1. The plots and tables are not well designed, which makes them hard to understand. e.g. Figure 1 fails to demonstrate the overall method clearly. There is space to improve with regard to color design (Figure 3) and table format. In Figure 2, labels should be inserted into the plot instead of writing the first row: xxx, second row: xxx...in the caption.
2. There are too many {enumerate} and {itemize}, which is not so common in papers. It would take a lot of space and make the paper look loose. 
3. Minor inconsistencies in grammar and terminology, such as a misplaced comma and inconsistent use of terms like "ray tracing" versus "ray-tracing," which should be standardized.
4. Table 3 is hard to understand. Why "Generation time per data point (seconds)" is a column?

### Questions
The organization of this paper is pretty 
1. Why not show the quantative results in the manuscript?
2. Why report the avg. mse?
3. what is the method name for 'the traditional RT approach'?Please make this clear and cite.

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
3

### Summary
The new algorithm of real-time electromagnetic signal processing is presented in this paper. Authors trained a GAN-based neural network to predict electromagnetic power distributions in 3D indoor environments. The indoor electromagnetic signal processing is fundamental problem of indoor tracking, so the work is valuable and actual.

### Strengths
In my opinion applying the GAN-based model to electromagnetic signal processing seems to be the strongest point of the paper: traditional approaches to this task were studied and comprehensively modified by many authors. For this reason, I find the GAN-based approach to be original and good scientific ground. Moreover, the presented method provides a robust result and achieves a 5X speed compared with other pipelines which is important in real-time applications. The Generator and Discriminator training process is described carefully.

Despite the weaknesses, I recommend accepting this work because the authors used an interesting and difficult architecture in a complicated task, and the numerical results were provided. The main reason to accept this paper is strong description of the GAN training, which stresses that the authors comprehensively researched GAN opportunities in the EM propagation domain.

### Weaknesses
However, several weak parts were figured out despite the strong points of the paper. The first question concerns the dataset that authors present in the paper. It seems that this dataset was used for training. This dataset is new so it is expected that there will be a pipeline of dataset generation. However, there is no description how this dataset was collected. This information allows us to judge how accurate the GT labels are. The absence of the source code and developed dataset deprives the opportunity to test the pipeline. In the results section the different materials that objects are made of are mentioned. Did authors analyze the dependance of GAN performance on material? What kind of sensors were used for dataset collection? How do authors measure the sensors’ accuracy? What filters were used to process the raw data of sensors?

### Questions
Have authors tested the Wasserstein loss for GAN? If yes, were the results worse or better? What applications do authors supposed to test the GAN on? Is it possible to verify the trained model on tracking tasks? In the results section the different materials that objects are made of are mentioned. Did authors analyze the dependance of GAN performance on material? What kind of sensors were used for dataset collection? How do authors measure the sensors’ accuracy? What filters were used to process the raw data of sensors?

### Soundness
4

### Presentation
2

### Contribution
3
