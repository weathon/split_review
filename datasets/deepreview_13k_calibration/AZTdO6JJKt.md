# Leveraging AutoML for Sustainable Deep Learning: A Multi-Objective HPO Approach on Deep Shift Neural Networks

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 5, 5, 6, 6

## Abstract
Deep Learning (DL) has advanced various fields by extracting complex patterns from large datasets.
However, the computational demands of DL models pose environmental and resource challenges. Deep shift neural networks (DSNNs) offer a solution by leveraging shift operations to reduce computational complexity at inference.
Following the insights from standard DNNs, we are interested in leveraging the full potential of DSNNs by means of AutoML techniques. 
We study the impact of hyperparameter optimization (HPO) to maximize DSNN performance while minimizing resource consumption. Since this combines multi-objective (MO) optimization with accuracy and energy consumption as potentially complementary objectives, we propose to combine state-of-the-art multi-fidelity (MF) HPO with multi-objective optimization. Experimental results demonstrate the effectiveness of our approach, resulting in models with over 80\% in accuracy and low computational cost.
Overall, our method accelerates efficient model development while enabling sustainable AI applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates the potential of DSNNs to reduce computational complexity and environmental impact in deep learning (DL) models. Through AutoML techniques, the authors explore ways to optimize DSNNs by balancing multiple objectives, including accuracy and energy consumption. By applying multi-fidelity hyperparameter optimization and multi-objective optimization, they identify Pareto-optimal configurations that improve DSNN performance by 20% while reducing emissions by 10% compared to default models. Notably, their findings challenge traditional expectations around quantization, showing that selectively quantizing smaller portions of the network at low precision can yield the best trade-offs between accuracy and energy savings. These results, validated across different model architectures, underscore DSNNs' potential in designing energy-efficient, high-performing DL models.

### Strengths
- The paper sheds light on an interesting design for quantized neural networks, DSNNs, which significantly reduce the computational demands at inference, positioning them as a sustainable AI solution.
- Through multi-fidelity hyperparameter optimization and multi-objective optimization, the proposed approach achieves configurations that improve DSNN performance by 20% while reducing emissions by 10% over baselines.
- The findings challenge conventional beliefs in model quantization, showing that selectively quantizing smaller portions of the network at low precision yields optimal trade-offs between energy efficiency and model accuracy.

### Weaknesses
 - The paper's contribution in terms of novelty is somewhat limited and could benefit from further clarification. The proposed optimization approach for DSNNs appears to directly apply existing optimization techniques (DGEMO and SMAC) for hyperparameter tuning, without substantial adaptation or refinement specific to the DSNN topology or its unique optimization landscape. As it stands, the work reads more as a straightforward application of existing AutoML methods rather than an innovative extension or advancement in the field. To improve the paper's originality, I suggest the authors consider developing an algorithm that more effectively integrates various design dimensions, such as backbone architecture and bit-shifting hyperparameters, with specific tailoring for the DSNN architecture. This could provide a more distinct and impactful contribution to the AutoML research.
- The paper would benefit from a more detailed architectural analysis, particularly w.r.t. the types of layers being quantized and the specific optimizations for bit-shifting. Currently, there is a lack of discussion on how bit-shift quantization affects various layers, which limits the depth of the architectural insights provided. To strengthen the contribution, I suggest the authors include a breakdown of the impact of bit-shift quantization on different layers and specify precisely which layers are being quantized. 
- The evaluation section is somewhat limited, as it currently includes results on only a single model architecture (ResNet20). This narrow focus makes it challenging to draw robust conclusions about the effectiveness and generalizability of the proposed AutoML framework. To strengthen the evaluation, I recommend that the authors test the approach on a broader range of models and datasets. This would provide a more comprehensive assessment of its applicability and impact across different scenarios.
- The discussion on hyperparameter importance is valuable; however, its placement later in the paper limits its impact. Presenting this ablation study earlier would help justify the choice of hyperparameters targeted for optimization, especially since only a few key design hyperparameters significantly influence the results while others contribute minimally. Moving this section forward and providing either empirical or theoretical justification for selecting these specific hyperparameters would enhance the clarity and rigor of the paper's contribution.

### Questions
- Could you clarify the novelty of your optimization approach for DSNNs? Specifically, are there any unique adaptations or modifications in the way DGEMO and SMAC are applied to DSNNs, beyond existing AutoML methods?
- Can you provide more details on the types of layers being quantized and the specific impact of bit-shift quantization across these layers? Are certain layers more affected by quantization than others?
- Have you considered testing your framework on additional model architectures and datasets to demonstrate its generalizability? If not, could you share insights into why ResNet20 was chosen as the sole model for evaluation?
- Could you elaborate on the rationale for the specific hyperparameters chosen for optimization? Given that only a few design hyperparameters appear to have a significant effect on the results, did you consider omitting those with minimal contributions?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper reports on the tuning and optimization of deep shift neural networks (DSNNs) for both accuracy and energy efficiency. Automatic hyperparameter and architecture search is employed to tune models and explore the Pareto front of the accuracy/energy tradeoff for the models. The paper defines the relevant search spaces and discovers configurations improving upon the state-of-the-art for DSNNs.

### Strengths
1. The paper is clear and well-written and provides both sufficient background and context for the work.
2. The paper is targeting improved efficiency for DSNNs, which has the potential for positive environmental impact.
3. The paper identifies improved configurations for DSNNs, and explores the Pareto front to understand the tradeoffs between configurations.
4. The impact of specific hyperparameters are analyzed.

### Weaknesses
1. It is not clear to me what the novelty and broader impact of the work is. It seems, essentially, to use relatively standard automatic tuning approaches to optimize an existing architecture. While this provides some value, it also seems very specific to the DSNNs considered here. To what extent are there generalizable lessons or takeaways from the work that are more broadly applicable?
2. I am unclear on how exactly energy efficiency is measured in order to incorporate it into the optimization process, which is critical for evaluating the paper's methodology (and might be useful for others). CodeCarbon typically requires assumptions about both the hardware being used and the regional energy mixture, as well as experimental measurements. The paper should provide some additional details and discussion on this.
3. Some of the hyperparameter importance measurements w.r.t. emissions (Figure 3) seem strange to me. In particular, how does the learning rate impact the emissions?

### Questions
Please see the comments/questions above under "Weaknesses".

### Soundness
3

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
The paper explores the optimization of Deep Shift Neural Networks (DSNNs) using Automated Machine Learning (AutoML) for balancing performance and energy efficiency. The authors propose an approach that leverages Multi-Fidelity (MF) and Multi-Objective (MO) Hyperparameter Optimization (HPO) to identify Pareto-optimal configurations of DSNNs. Their methodology integrates tools like SMAC3 and CodeCarbon to simultaneously optimize accuracy and reduce carbon emissions. The experiments conducted on architectures such as ResNet20, MobileNetV2, and GoogLeNet across datasets like CIFAR10 and Caltech10.

### Strengths
1. The paper offers detailed quantitative results, hyperparameter importance studies, providing a robust empirical basis for the proposed approach.

2. The motivation of the proposed method is to use shift computing to reduce the computational consumption of DSNNs. The article uses emissions as the target metric, which is interesting and has application value.

3. The work effectively showcases that AutoML can yield DSNN configurations that outperform baseline models in both performance and energy efficiency, emphasizing practical implications for low-resource settings.

### Weaknesses
1. For readers who are not familiar with AutoML or optimization methods, the technicality and depth of this paper may be difficult to grasp. A more detailed introduction in the Background section and a clearer writing style would help convey the motivation of the article. For instance, in Section 3, the description of DSNNs only briefly introduces the weight transformation of DSNNs through Equation 3.3 and Equation 3.4 for the simple flip(·) function. However, as introduced in [1], the core calculation of the shfit function is not explained in the article, making it difficult for readers to understand the true characteristics of DSNNs. From a writing logic perspective, there is not a strong connection between the backgrounds in Sections 3.1-3.3, and there are several typos in the article, such as '$tildeW_q$' in line 143.

2. The core contribution of the paper is the ability to quantify the emissions impact of training and inference of DSNNs, a topic that is environmentally friendly. However, energy efficiency is dependent on the chosen computing platform. The authors conducted tests using the A100. The reliance on energy and emissions tracking tools like CodeCarbon is beneficial, but the paper could improve by discussing limitations or assumptions inherent in these measurements and potential variability due to different hardware.

 3. A small-size model like ResNet20 on A100 may not be comprehensive enough, and researchers would like to see the relationship between the computational energy of different types of neural network structures on various energy-efficient computing devices and the shift configuration.

### Questions
I am curious about how the authors deployed shift-based computations instead of traditional addition and multiplication on the NVIDIA A100 GPU. Can this type of computation be extended to more networks, even though LLMs may be larger in size, what about smaller BERT models?

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
3

### Summary
The paper aimed to address the resource and environmental challenge introduced by the great computational cost of DL models. In particular, they focused on the DNNs using shift operations. They used multi-fidelity (MF) HPO with multi-objective optimization to find some pareto-optimal designs for DSNNs. With this approach, the performance is increased by 20% with 10% less carbon emission.

### Strengths
AutoML based solutions can reduce the design cycle for DSNN model development.
Pareto-optimal design  is a standard way. However it offers flexibility for the performance-energy trade-off.

### Weaknesses
Lacks novelty. The major techniques HPO used for autoML is not new.  
The improvement is marginal (only 20% for performance and 10% for energy reduction). But acceptable when compared with human experts.

### Questions
no

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies Deep Shift Neural Networks and how they can be used for computationally efficient and energy-friendly deployment. Particularly, the paper extends the prior work on DeepShiftQ and DeepShift-PS and uses a multi-fidelity, multi-objective optimization algorithm to better search the optimization space of deep shift networks while ensuring good task accuracy and energy consumption is reduced. The efficacy of the proposed algorithm is demonstrated on ResNet20 architecture.

### Strengths
1. The paper describes the background literature work in good details.
2. The paper discusses the details of results and importance of each choice in optimization landscape. (Section 5).

### Weaknesses
1.  The paper should include a section of how energy efficiency compares to tensor core operations with reduced precisions on modern GPUs (A100, H100). Since these GPUs have high specific dense tensor cores in SMs, these are very energy efficient in comparison to equivalent operations that execute on CUDA cores (this where bit shift operations would execute). If the motivation is design custom ASICS, then the paper should definitely include a section explaining this in depth. Specifically, the paper needs to quantify the energy savings of the proposed method against the highly optimized tensor core operations, which are designed for matrix multiplications at reduced precision. Without this comparison, it's unclear if the proposed method offers a practical advantage on current hardware. Furthermore, if the target is custom ASICs, the paper should detail the hardware design implications, including area, power, and performance trade-offs, which are critical for evaluating the feasibility of the approach.
2. The paper conducts experiments on very small number of networks that are specifically image recognition focused. The paper should definitely include more architectures specifically transformer architectures (vision transformers if the paper only wants to deal with vision related tasks). The current experiments do not provide sufficient evidence to claim general applicability of the proposed method. Expanding the evaluation to include transformer-based models, which have become increasingly important in vision tasks, is essential to demonstrate the method's versatility and robustness. The lack of such experiments limits the impact of the work.
3. Paper should include a pseudo code section describing how various components of the optimization algorithms used. The absence of pseudo-code makes it difficult to understand the implementation details of the optimization algorithm and to reproduce the results. A clear, step-by-step description of the algorithm is crucial for transparency and for other researchers to build upon this work.
4. Figure 1 is hard to understand with few data points and huge space on x axis wasted (what is data point indicated by "x" corresponding to?). The figure lacks clarity and does not effectively convey the information. The meaning of the data point indicated by "x" is unclear, and the excessive whitespace on the x-axis makes it difficult to interpret the results. The figure should be redesigned to be more informative and visually appealing.
5. The paper should include error bars in the results and use the results averaged over multiple seeds (3 seeds in this case). Since quantization methods often have higher variance, providing the mean and standard deviation of the reported numbers would provide a better understanding of the experimental results. The lack of error bars and averaging over multiple seeds makes it difficult to assess the reliability and consistency of the results. Quantization methods are known to be sensitive to initialization and other random factors, so reporting mean and standard deviation is crucial for a rigorous evaluation.
6. The paper seems hard to read and understand in one go for a new reader. I guess its because the core contribution requires dependence on too many methods from Background and these are not described with concrete examples in Background literature.

Nit:
The explanation of DeepShift-PS at line 146 can definitely be improved by adding an example or pseudo code.
Line 143 => tildeWq (looks like wrong text since the formula there on Line 144).

### Questions
Mentioned in weakness section.

### Soundness
3

### Presentation
2

### Contribution
2
