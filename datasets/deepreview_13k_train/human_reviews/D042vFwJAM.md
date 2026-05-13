# Physics-aligned field reconstruction with diffusion bridge

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
The reconstruction of physical fields from sparse measurements is pivotal in both scientific research and engineering applications. Traditional methods are increasingly supplemented by deep learning models due to their efficacy in extracting features from data. However, except for the low accuracy on complex physical systems, these models often fail to comply with essential physical constraints, such as governing equations and boundary conditions. To overcome this limitation, we introduce a novel data-driven field reconstruction framework, termed the Physics-aligned Schr\"{o}dinger Bridge (PalSB). This framework leverages a diffusion bridge mechanism that is specifically tailored to align with physical constraints. The PalSB approach incorporates a dual-stage training process designed to address both local reconstruction mapping and global physical principles. Additionally, a boundary-aware sampling technique is implemented to ensure adherence to physical boundary conditions. We demonstrate the effectiveness of PalSB through its application to three complex nonlinear systems: cylinder flow from Particle Image Velocimetry experiments, two-dimensional turbulence, and a reaction-diffusion system. The results reveal that PalSB not only achieves higher accuracy but also exhibits enhanced compliance with physical constraints compared to existing methods. This highlights PalSB's capability to generate high-quality representations of intricate physical interactions, showcasing its potential for advancing field reconstruction techniques.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In _Physics-Aligned Field Reconstruction with Diffusion Bridge_, the authors propose a method for reconstructing physical fields from a limited number of measurements. They combine a diffusion Schrödinger bridge, following the $I^2SB$ approach by Liu et al., with a fine-tuning step to improve consistency with physical constraints. Additionally, they adapt their sampling procedure to be "boundary-aware" by padding the input appropriately and achieve good performance with a small number of function evaluations through "early-stop sampling."

### Strengths
The paper addresses the important challenge of reconstructing physical fields, drawing inspiration from recent methods such as $I^2SB$ diffusion Schrödinger bridges and reinforcement learning with human feedback for diffusion models. The authors convincingly demonstrate the effectiveness of their method by evaluating it across three datasets (with two tasks each) and comparing it against several reasonable baselines. Further, they conduct an ablation study, reinforcing the value of their design choices. The early stop sampling strategy in particular could prove to be useful outside of the context of physical field reconstruction as well. The method and results are presented clearly with only minor clarifications needed.

### Weaknesses
There's no major weaknesses of the paper.
For minor opportunities for clarification and cleanup see Questions.

### Questions
Questions / Suggestions for Clarification:
1. In line 083-085: What is the relationship between $m$, $n$ and $d$?
2. I can't quite follow the derivation of eq. (6) from eq. (4), I end up with $f_\theta + x_0$ instead
3. line 268: Doesn't the backpropagation get truncated for all steps $i<N$? That's how I interpret both Fig. 1 and Alg. 2
4. Does finetuning use early stop sampling?
5. Does truncating the backpropagation in the finetuning step affect the adherence to physical constraints in a time-step dependent manner? I think this is alluded to in Appendix C1 but I think it warrants further clarification, especially any potential interaction with early stop sampling.
6. How much padding is used for sampling and does the amount of padding influence performance? Does that interact with the number of sampling steps?
7. Algorithms 2 and 3 are not totally clean:
   - 7: while $j=T$ -> while $j<T$
   - 11: $t_j$ not defined
   - 12: $t$ should instead be $t_j$

Typos/Format etc
- line 065: such diffusion bridge -> such a diffusion bridge
- missing year in reference Fan et al.
- line 329: should this say the physical field cannot be simultaneously acquired at high resolution and covering a large field of view? Surely the resolution and FOV are known.
- line 883: calculate the loss according to eq 4 -> calculate the loss according to eq 6
- line 1063: "observation mentioned above" -> vague, which one?
- Fig 10+11: noisy -> noise-free

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
The paper presents a method for reconstruction of physical fields from sparse information using Schrodinger bridges. The setup uses a dual training approach where the diffusion bridge is first trained to bridge between sparse and high resolution measurements, then it is fine tuned to satisfy physical constraints. This is coupled with a special technique to care for boundary conditions. The method is tested on several examples of physical field reconstruction tasks.

### Strengths
- physical field reconstruction is an important task with potential high impact in applied sciences
- the presented method is well-chosen for the problem
- the method is experimentally validated on several example problems

### Weaknesses
 - while the methodology is well chosen, I don't believe the paper presents major new methodological contributions
- some of the techniques seems somewhat adhoc, i.e. employing early stop sampling. I don't doubt that these techniques work well for the problem at hand, but they are not interesting as such from a methodological point of view
- the experimental validation is somewhat limited being restricted to 2d problems and with fairly limited datasets. A more extensive validation that clearly demonstrates the power of the method would make a stronger case for the paper, given the limited methodological contributions

### Questions
Can you provide strong counterpoints to the above weaknesses?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents the Physics-aligned Schrödinger Bridge (PalSB) method, developed for reconstructing physical fields from sparse data subject to physical constraints. Reconstruction of physical fields is a key task in fields such as fluid mechanics, meteorology, and astrophysics, where spatiotemporal information about systems must be recovered from sparse, often noisy, observations. Despite significant advances in machine learning and the use of diffusion models to solve complex data problems, many existing approaches fail to satisfy physical laws and struggle to cope with the nonlinear nature of complex physical systems.

PalSB proposes a new approach to data reconstruction that incorporates a diffusion bridge mechanism (Schrödinger Bridge) specifically adapted to satisfy physical constraints. The model is trained in two stages: the first stage focuses on local reconstruction map construction, and the second stage focuses on global physical principles. This combination allows for the creation of super-resolved data that not only more accurately but also better satisfy physical constraints than similar methods.

The pretraining stage of PalSB is based on a diffusion Schrödinger bridge, which allows for efficient transition between high-quality and corrupted data distributions. To reduce computational costs and improve the accuracy of the model, the training process is performed on small local patches of the high-resolution field. This helps the model focus on the local structure of the data, avoiding the need for large computational resources. The second stage involves Physics-aligned Finetuning, which allows the model to fit physical laws represented as differential equations. This stage minimizes deviations from physical laws using a combination of physically informed and regression loss functions.

The paper also proposes boundary-aware sampling to handle boundary conditions and early stopping sampling, which improves the generation efficiency and reduces the number of required steps. These strategies allow the model to better account for global conditions and significantly improve the performance of PalSB.

Three complex physical systems were chosen to evaluate PalSB: flow around a cylinder, two-dimensional turbulence, and a reaction-diffusion system. Based on the benchmark results, PalSB demonstrated significant improvements in accuracy and physical compliance compared to other methods, including interpolation, end-to-end models, and physically informed diffusion models (PIDM). In particular, PalSB significantly reduces physical inconsistencies and improves the compliance with spatial patterns in both Fourier and real space interpolation problems.

The study also showed that removing individual PalSB modules (e.g., physically consistent tuning or boundary-aware sampling) degrades the physical compliance and model performance. This highlights the importance of PalSB's integrated approach to achieve high accuracy and compliance with physical laws.

In conclusion, PalSB demonstrates great potential for field reconstruction in complex systems, showing high quality data recovery and improved compliance with physical constraints. In the future, PalSB is expected to be extended to 3D problems, which will cover a wider range of scientific and engineering applications that require compliance with physical laws during the generation process.

### Strengths
First, it provides high accuracy, surpassing traditional methods by using the diffusion bridge mechanism, which allows for efficient data recovery from sparse measurements. Second, PalSB integrates physical constraints (boundary conditions and equations) at the fine-tuning stage, which minimizes mismatches with real physical laws.

### Weaknesses
Unfortunately, I do not understand your motivation for using only the normalized error. I highly recommend that model errors can be estimated using the mean squared error (MSE) and L1 error metrics. In addition, the residual error, which determines how well the predicted field fits the equations describing the physical system, can be used to assess compliance with physical constraints. Also, for the future, I highly recommend combining your approach and this approach https://arxiv.org/pdf/2403.14404

### Questions
Can you additional explain me, why did you use only normalized metrics? Also, can you please explain why you checked on flow equations (like Kolmogorov and Reaction-Diffusion equations)? I highly recommend checking on electrostatic equations as well.

### Soundness
4

### Presentation
4

### Contribution
4
